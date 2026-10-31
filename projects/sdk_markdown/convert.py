"""Converts the Sphinx HTML documentation of the Cinema 4D Python SDK into agent-readable Markdown.

The HTML pages in `docs/` are converted one-to-one into `docs_md/`, mirroring the folder structure
so that every `page.html` becomes `page.md` and all relative links keep working. Sphinx anchor ids
of symbols and sections are preserved as `<a id="..."></a>` tags so that `page.md#c4d.BaseObject`
style links resolve and fully qualified names can be grepped. Referenced images are copied, inline
SVG diagrams are extracted into files, and interactive widgets are reduced to their text content.

Besides the pages, the script generates the lookup files an agent needs to navigate the result:

- `docs_md/symbols.tsv`: every class, method, function, attribute, constant, type id, description
  resource, and description parameter mapped to its Markdown file and anchor.
- `docs_md/INDEX.md` and `docs_md/index/*.md`: section indexes with page titles and summaries.
- `llms.txt`: the curated entry point following the llms.txt proposal (https://llmstxt.org).

Usage:
    pip install beautifulsoup4 lxml
    python projects/sdk_markdown/convert.py [sdkRoot]

    `sdkRoot` defaults to the SDK folder three levels above this script. Existing output in
    `docs_md/` is overwritten. Requires Python 3.10+; this is a standalone tool, not a Cinema 4D
    script.
"""

import os
import re
import shutil
import sys
import zlib

from bs4 import BeautifulSoup, NavigableString, Tag

ONLINE_ROOT: str = "https://developers.maxon.net/docs/py/2027_0_0/"
SDK_TITLE: str = "Cinema 4D Python SDK 2027.0.0"

# Pages without static content worth converting.
SKIP_PAGES: set[str] = {"search.html"}

# Pages whose content is rendered by JavaScript from data that already exists as Markdown in the
# `.agents/` folder of the SDK. Their body is replaced with links to that data.
REPLACED_PAGES: dict[str, str] = {
    "indexes/resource_index.html":
        "# Resource Index\n\n"
        "The HTML version of this page is an interactive browser. The same resource data is "
        "available as Markdown:\n\n"
        "- [Descriptions](../../.agents/descriptions/_overview.md): parameter ids, types, and "
        "flags of objects, tags, materials, shaders, and nodes, one file per `.res` file.\n"
        "- [Description data types](../../.agents/descriptiondatatypes/_overview.md): the "
        "parameter types used in description resources.\n"
        "- [Node spaces](../../.agents/nodespaces/_overview.md): node templates and ports of the "
        "material and scene node spaces.\n",
}

# Elements which are interactive, decorative, or navigation only.
DROP_TAGS: set[str] = {
    "script", "style", "button", "input", "select", "option", "fieldset", "label", "output",
    "dialog", "form", "nav", "noscript", "colgroup", "col", "title", "desc"}
DROP_CLASSES: set[str] = {
    "headerlink", "clearer", "mxn-item-list-nav", "mxn-card-icon", "bi", "mxn-geo__controls",
    "mxn-geo__view", "mxn-geo__readout", "mxn-landing-logo", "mxn-dark-theme-only",
    "mxn-search-busy", "linenodiv"}

BLOCK_TAGS: set[str] = {
    "p", "div", "section", "dl", "dt", "dd", "ul", "ol", "li", "table", "pre", "blockquote",
    "h1", "h2", "h3", "h4", "h5", "h6", "figure", "figcaption", "iframe", "svgref", "hr",
    "thead", "tbody", "tr", "td", "th", "caption", "legend"}

CODE_LANGUAGES: dict[str, str] = {
    "python": "python", "py": "python", "default": "python", "python3": "python",
    "pycon": "pycon", "py3tb": "pytb", "c++": "cpp", "cpp": "cpp", "javascript": "javascript",
    "json": "json", "html": "html", "text": "text", "c4dres": "c4dres", "c4dstr": "c4dstr"}


class Site:
    """Holds the paths and the state shared by all page conversions.
    """

    def __init__(self, sdkRoot: str) -> None:
        self.sdkRoot: str = os.path.abspath(sdkRoot)
        self.htmlRoot: str = os.path.join(self.sdkRoot, "docs")
        self.mdRoot: str = os.path.join(self.sdkRoot, "docs_md")
        self.assets: set[str] = set()
        self.pages: dict[str, tuple[str, str]] = {}  # md rel path -> (title, summary)
        self.sources: dict[str, str] = {}  # md rel path of an example -> repo rel source path
        self.tableSymbols: list[tuple[str, str, str, str]] = []  # (name, role, path, title)

    def HtmlPages(self) -> list[str]:
        """Returns the paths of all content pages relative to the HTML root, in sorted order.
        """
        result: list[str] = []
        for folder, dirs, files in os.walk(self.htmlRoot):
            dirs[:] = sorted(d for d in dirs if not d.startswith((".", "_")))
            for name in sorted(files):
                rel: str = os.path.relpath(os.path.join(folder, name), self.htmlRoot)
                rel = rel.replace(os.sep, "/")
                if name.endswith(".html") and rel not in SKIP_PAGES:
                    result.append(rel)
        return result


class PageConverter:
    """Converts the main content of a single Sphinx HTML page into Markdown.
    """

    def __init__(self, site: Site, rel: str) -> None:
        self.site: Site = site
        self.rel: str = rel
        self.dir: str = os.path.dirname(rel)
        self.level: int = 1
        self.inTable: bool = False
        self.svgFiles: list[str] = []

    # --- Links and assets ---------------------------------------------------------------------

    def RewriteHref(self, href: str) -> str:
        """Maps an HTML link of the page to the equivalent link in the Markdown mirror.
        """
        if not href or re.match(r"^[a-z][a-z0-9+.-]*:", href, re.I) or href.startswith("#"):
            return href
        path, _, fragment = href.partition("#")
        if path.split("?")[0].endswith(".html"):
            path = path.split("?")[0][:-5] + ".md"
        elif path:
            self.AddAsset(path)
        return path + ("#" + fragment if fragment else "")

    def AddAsset(self, path: str) -> None:
        """Registers a non-page file referenced by the page for copying into the mirror.
        """
        target: str = os.path.normpath(os.path.join(self.dir, path.split("?")[0]))
        target = target.replace(os.sep, "/")
        if not target.startswith("..") and os.path.isfile(os.path.join(self.site.htmlRoot, target)):
            self.site.assets.add(target)

    # --- Inline content -----------------------------------------------------------------------

    def Inline(self, node: Tag | NavigableString) -> str:
        """Returns the inline Markdown for #node and its children.
        """
        if isinstance(node, NavigableString):
            if node.__class__.__name__ in ("Comment", "Doctype", "ProcessingInstruction"):
                return ""
            text: str = re.sub(r"\s+", " ", str(node))
            return re.sub(r"<(?=[A-Za-z/!])", r"\\<", text)
        if self.IsDropped(node):
            return ""
        name: str = node.name
        classes: list[str] = node.get("class", [])
        if name in ("code", "tt", "kbd", "samp", "var"):
            return Backtick(node.get_text())
        if name == "br":
            return "<br>" if self.inTable else "  \n"
        if name == "img":
            return self.Image(node)
        if name in ("svgref",):
            return self.SvgRef(node)
        if name == "a":
            return self.Link(node)
        if name == "span" and node.get("id") and not node.contents:
            return Anchor(node["id"])
        if name == "div" and "line" in classes:
            return self.Children(node).strip() + ("<br>" if self.inTable else "  \n")
        if name == "iframe":
            return self.Iframe(node)
        inner: str = self.Children(node)
        if name in ("em", "i", "cite") or "versionmodified" in classes:
            # Sphinx emphasizes the brackets of type annotations separately, e.g. `Optional[int]`.
            if re.fullmatch(r"[\s\[\](),|]*|\s*or\s*", inner):
                return inner
            return Wrap(inner, "*")
        if name in ("strong", "b"):
            return Wrap(inner.replace("**", ""), "**")
        if name == "p" or name in BLOCK_TAGS:
            return " " + inner.strip() + " "
        return inner

    def Children(self, node: Tag) -> str:
        """Returns the concatenated inline Markdown of all children of #node.
        """
        return "".join(self.Inline(child) for child in node.children)

    def Link(self, node: Tag) -> str:
        """Returns the Markdown for an anchor element, which can be a link, a card, or a target.
        """
        classes: list[str] = node.get("class", [])
        if "mxn-card-link" in classes:
            title: str = self.Inline(node.find("strong")).strip() if node.find("strong") else ""
            descNode: Tag | None = node.find(class_="mxn-card-description")
            desc: str = self.Inline(descNode).strip() if descNode else ""
            link: str = f"[{title.strip('*')}]({self.RewriteHref(node.get('href', ''))})"
            return link + (f": {desc}" if desc else "")
        inner: str = self.Children(node).strip()
        href: str | None = node.get("href")
        if href is None:
            return (Anchor(node["id"]) if node.get("id") else "") + inner
        if not inner:
            return ""
        return f"[{inner}]({self.RewriteHref(href)})"

    def Image(self, node: Tag) -> str:
        """Returns the Markdown for an image and registers the image file as an asset.
        """
        src: str = node.get("src", "")
        if not src or src.startswith("data:"):
            return ""
        alt: str = re.sub(r"\s+", " ", node.get("alt", "")).strip()
        return f"![{alt}]({self.RewriteHref(src)})"

    def Iframe(self, node: Tag) -> str:
        """Returns a link for an embedded frame such as a video.
        """
        title: str = node.get("title") or "Embedded content"
        return f"[{title}]({node.get('src', '')})"

    def SvgRef(self, node: Tag) -> str:
        """Returns the image link for an inline SVG diagram that was extracted into a file.
        """
        index: int = int(node["data-n"])
        path, label = self.svgFiles[index]
        return f"![{label}]({path})"

    # --- Block content ------------------------------------------------------------------------

    def Blocks(self, node: Tag) -> list[str]:
        """Returns the Markdown blocks for the children of the container #node.

        Consecutive inline children are merged into a single paragraph.
        """
        blocks: list[str] = []
        run: list[str] = []

        def flush() -> None:
            text: str = Clean("".join(run))
            if text:
                blocks.append(text)
            run.clear()

        for child in node.children:
            if isinstance(child, Tag) and self.IsBlock(child):
                flush()
                blocks.extend(self.Block(child))
            else:
                run.append(self.Inline(child))
        flush()
        return blocks

    def IsBlock(self, node: Tag) -> bool:
        """Returns whether #node is rendered as a block.
        """
        return node.name in BLOCK_TAGS or node.name == "svgref" or (
            node.name == "a" and "mxn-card-link" in node.get("class", []))

    def IsDropped(self, node: Tag) -> bool:
        """Returns whether #node carries no content for the Markdown output.
        """
        if node.name in DROP_TAGS:
            return True
        return bool(DROP_CLASSES.intersection(node.get("class", [])))

    def Block(self, node: Tag) -> list[str]:
        """Returns the Markdown blocks for the block element #node.
        """
        if self.IsDropped(node):
            return []
        name: str = node.name
        classes: list[str] = node.get("class", [])
        anchor: str = Anchor(node["id"]) if node.get("id") else ""

        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.level = int(name[1])
            parent: Tag | None = node.parent
            ids: str = anchor
            heading: Tag | None = parent.find(re.compile("^h[1-6]$")) if parent else None
            if parent is not None and parent.get("id") and heading is node:
                ids = Anchor(parent["id"]) + ids
            text: str = Clean(self.Children(node))
            return ["#" * self.level + " " + text + (" " + ids if ids else "")]
        if name == "p":
            text: str = Clean(self.Children(node))
            if not text:
                return [anchor] if anchor else []
            if "rubric" in classes or "mxn-item-list-title" in classes \
                    or "mxn-change-title" in classes:
                text = Wrap(text, "**")
            elif "caption" in classes:
                text = Wrap(text, "*")
            return [anchor + text]
        if name in ("pre",):
            return [Fence(node.get_text(), "")]
        if name == "div" and any(c.startswith("highlight-") for c in classes):
            return [self.Code(node)]
        if name == "div" and "highlight" in classes:
            pre: Tag | None = node.find("pre")
            return [Fence(pre.get_text(), "")] if pre else []
        if name == "table":
            return [anchor + self.Table(node)] if anchor else [self.Table(node)]
        if name in ("ul", "ol"):
            return self.List(node)
        if name == "dl":
            return self.DefinitionList(node)
        if name == "blockquote":
            return [Quote("\n\n".join(self.Blocks(node)))]
        if name == "div" and "admonition" in classes:
            return ([anchor] if anchor else []) + [self.Admonition(node)]
        if name == "div" and "line-block" in classes:
            lines: list[str] = [
                Clean(self.Children(line)) if "line" in line.get("class", [])
                else "  \n".join(self.Block(line))
                for line in node.find_all("div", recursive=False)]
            return ["  \n".join(line for line in lines if line)]
        if name == "div" and "mxn-math" in classes:
            label: str = re.sub(r":math:`([^`]*)`", r"$\1$", node.get("aria-label", ""))
            return [f"> *Interactive figure (HTML only): {label}*"] if label else []
        if name == "div" and "mxn-card" in classes and node.find("a", class_="mxn-card-link"):
            card: Tag = node.find("a", class_="mxn-card-link")
            return ["- " + self.Link(card)]
        if name == "a" and "mxn-card-link" in classes:
            return ["- " + self.Link(node)]
        if name == "div" and "mxn-change-header" in classes:
            parts: list[str] = [Clean(self.Children(p)) for p in node.find_all("p")]
            return [f"**{parts[0]}** " + " ".join(parts[1:])] if parts else []
        if name == "iframe":
            return [self.Iframe(node)]
        if name == "svgref":
            return [self.SvgRef(node)]
        if name == "hr":
            return ["---"]

        # Generic containers; cards are merged into one list so that they render as bullets.
        blocks: list[str] = self.Blocks(node)
        blocks = MergeBullets(blocks)
        if anchor and not (blocks and blocks[0].startswith("#")):
            blocks.insert(0, anchor)
        return blocks

    def Code(self, node: Tag) -> str:
        """Returns a fenced code block for a Pygments highlight container.
        """
        lang: str = next(c[10:] for c in node.get("class", []) if c.startswith("highlight-"))
        lang = CODE_LANGUAGES.get(lang.lower(), lang.lower())
        codeCell: Tag | None = node.find("td", class_="code")
        pre: Tag | None = (codeCell or node).find("pre")
        return Fence(pre.get_text() if pre else node.get_text(), lang)

    def Admonition(self, node: Tag) -> str:
        """Returns a block quote for a note, warning, see-also, or similar admonition.
        """
        titleNode: Tag | None = node.find("p", class_="admonition-title", recursive=False)
        title: str = Clean(self.Children(titleNode)) if titleNode else "Note"
        if titleNode:
            titleNode.extract()
        body: list[str] = self.Blocks(node)
        if body and "\n" not in body[0] and not body[0].startswith(("-", "#", ">", "`", "|")):
            body[0] = f"**{title}:** {body[0]}"
        else:
            body.insert(0, f"**{title}:**")
        return Quote("\n\n".join(body))

    def List(self, node: Tag) -> list[str]:
        """Returns a Markdown list for an ordered or unordered HTML list.
        """
        items: list[str] = []
        number: int = int(node.get("start", 1))
        for li in node.find_all("li", recursive=False):
            marker: str = f"{number}. " if node.name == "ol" else "- "
            number += 1
            body: str = "\n\n".join(self.Blocks(li)) or ""
            if li.get("id"):
                body = Anchor(li["id"]) + body
            items.append(Indent(marker, body))
        tight: bool = all("\n\n" not in item for item in items)
        return [("\n" if tight else "\n\n").join(items)] if items else []

    def DefinitionList(self, node: Tag) -> list[str]:
        """Returns Markdown for API descriptions, field lists, and plain definition lists.
        """
        classes: list[str] = node.get("class", [])
        blocks: list[str] = []
        if "py" in classes:
            return self.ApiEntry(node)
        for dt in node.find_all("dt", recursive=False):
            dd: Tag | None = dt.find_next_sibling("dd")
            term: str = Clean(self.Children(dt)).rstrip(":")
            body: list[str] = self.Blocks(dd) if dd else []
            if "field-list" in classes:
                term = f"**{term}:**"
            else:
                term = f"**{term.replace('**', '')}**"
            if len(body) == 1 and "\n" not in body[0] and not body[0].startswith(
                    ("-", "#", ">", "`", "|", "1.")):
                blocks.append(f"{term} {body[0]}")
            else:
                blocks.append(term)
                blocks.extend(body)
        return blocks

    def ApiEntry(self, node: Tag) -> list[str]:
        """Returns a heading with the signature for a Sphinx object description plus its body.
        """
        blocks: list[str] = []
        outerLevel: int = self.level
        entryLevel: int = min(6, outerLevel + 1)
        for dt in node.find_all("dt", recursive=False):
            dd: Tag | None = dt.find_next_sibling("dd")
            prop: Tag | None = dt.find("em", class_="property", recursive=False)
            prefix: str = Clean(prop.get_text()) if prop else ""
            if prop:
                prop.extract()
            for link in dt.find_all("a", class_="headerlink"):
                link.extract()
            signature: str = re.sub(r"\s+", " ", dt.get_text()).strip()
            signature = re.sub(r"\(\s+", "(", re.sub(r"\s+\)", ")", signature))
            heading: str = "#" * entryLevel + " " + (f"*{prefix}* " if prefix else "")
            heading += Backtick(signature) if signature else ""
            if dt.get("id"):
                heading += " " + Anchor(dt["id"])
            blocks.append(heading)
            if dd is not None and dd.find_previous_sibling("dt") is dt:
                self.level = entryLevel
                blocks.extend(self.Blocks(dd))
                self.level = outerLevel
        return blocks

    def Table(self, node: Tag) -> str:
        """Returns a Markdown table, or a bullet list for the member overview tables of classes.
        """
        rows: list[Tag] = [tr for tr in node.find_all("tr") if tr.find_parent("table") is node]
        outerInTable: bool = self.inTable
        self.inTable = True
        try:
            if node.find_parent("div", class_="maxon-overview"):
                return self.OverviewList(rows)
            grid: list[list[str]] = []
            headerRows: int = 0
            for tr in rows:
                cells: list[str] = []
                for cell in tr.find_all(("td", "th"), recursive=False):
                    text: str = self.CellText(cell)
                    cells.append(text)
                    cells.extend([""] * (int(cell.get("colspan", 1)) - 1))
                if tr.find_parent("thead") is not None:
                    headerRows += 1
                else:
                    self.CollectTableSymbol(node, tr, cells)
                grid.append(cells)
        finally:
            self.inTable = outerInTable
        if not grid:
            return ""
        width: int = max(len(r) for r in grid)
        grid = [r + [""] * (width - len(r)) for r in grid]
        header: list[str] = grid[0] if headerRows else [" "] * width
        body: list[list[str]] = grid[1:] if headerRows else grid
        lines: list[str] = ["| " + " | ".join(header) + " |", "|" + "---|" * width]
        lines += ["| " + " | ".join(r) + " |" for r in body]
        return "\n".join(lines)

    def CellText(self, cell: Tag) -> str:
        """Returns the single line content of a table cell.
        """
        parts: list[str] = []
        for block in self.Blocks(cell):
            if block.startswith("```"):
                code: list[str] = block.split("\n")[1:-1]
                block = "<br>".join(Backtick(line) for line in code if line.strip())
            elif block.startswith("| "):
                # A nested table becomes one `cell: cell` line per row; its cells are escaped.
                rows: list[str] = []
                for line in block.split("\n")[1:]:
                    cells: list[str] = [c.strip() for c in line.strip()[1:-1].split(" | ")]
                    if not set("".join(cells)) <= set("-|"):
                        rows.append(": ".join(c for c in cells if c))
                parts.append("<br>".join(rows))
                continue
            parts.append(block.replace("\n", "<br>").replace("|", "\\|"))
        return "<br>".join(parts)

    def OverviewList(self, rows: list[Tag]) -> str:
        """Returns the member overview of a class or module as a categorized bullet list.
        """
        lines: list[str] = []
        for tr in rows:
            cells: list[Tag] = tr.find_all("td", recursive=False)
            if len(cells) == 1:
                lines.append(f"\n**{Clean(self.Children(cells[0]))}**\n")
            elif len(cells) >= 2:
                name: str = self.CellText(cells[0]).replace("\\|", "|")
                desc: str = self.CellText(cells[1]).replace("\\|", "|")
                lines.append(f"- {name}" + (f": {desc}" if desc else ""))
        return "\n".join(lines).strip()

    # --- Page ---------------------------------------------------------------------------------

    def ExtractSvgs(self, html: str) -> str:
        """Writes inline SVG diagrams to files and replaces them with placeholders.

        The SVG markup is copied from the raw source because HTML parsers lowercase SVG attributes
        such as `viewBox`, which breaks the rendering of the files.
        """
        stem: str = re.sub(r"[^A-Za-z0-9]+", "_", self.rel[:-5]).strip("_")

        def replace(match: re.Match) -> str:
            svg: str = match.group(0)
            index: int = len(self.svgFiles)
            fileRel: str = f"_images/inline/{stem}_{index}.svg"
            target: str = os.path.join(self.site.mdRoot, fileRel)
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "w", encoding="utf-8") as f:
                f.write(svg)
            title: re.Match | None = re.search(r"<title[^>]*>(.*?)</title>", svg, re.S)
            desc: re.Match | None = re.search(r"<desc[^>]*>(.*?)</desc>", svg, re.S)
            label: str = " ".join(m.group(1).strip() for m in (title, desc) if m)
            label = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", label)).replace("]", ")")
            link: str = os.path.relpath(target, os.path.join(self.site.mdRoot, self.dir))
            self.svgFiles.append((link.replace(os.sep, "/"), label or "Diagram"))
            return f'<svgref data-n="{index}"></svgref>'

        return re.sub(r"<svg\b.*?</svg>", replace, html, flags=re.S)

    def Convert(self) -> str:
        """Converts the page and returns its Markdown.
        """
        with open(os.path.join(self.site.htmlRoot, self.rel), encoding="utf-8") as f:
            html: str = self.ExtractSvgs(f.read())
        soup: BeautifulSoup = BeautifulSoup(html, "lxml")
        body: Tag | None = soup.select_one("div.body")
        if body is None:
            raise RuntimeError(f"No content body in {self.rel}")
        markdown: str = "\n\n".join(FoldAnchors(MergeBullets(self.Blocks(body))))
        if self.rel in REPLACED_PAGES:
            markdown = REPLACED_PAGES[self.rel]
        markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n"

        title: str = soup.title.get_text().split(" \u2014 ")[0].strip() if soup.title else ""
        # The summary is the first prose paragraph of the page or of its class description; member
        # descriptions, tables, notes, and labels such as "Parent Class:" do not qualify.
        summary: str = ""
        skip: tuple[str, ...] = ("table", "li", "dt", "blockquote")
        members: re.Pattern = re.compile(r"method|function|attribute|data|property")
        for para in body.find_all("p"):
            text: str = Clean(para.get_text())
            if len(text) < 25 or text.endswith(":") or para.find_parent(skip) or para.find_parent(
                    "div", class_=re.compile(r"admonition|version|deprecated|field-list")) or \
                    para.find_parent("dl", class_="field-list") or \
                    para.find_parent("dl", class_=members):
                continue
            summary = text
            break
        self.site.pages[self.rel[:-5] + ".md"] = (title, Truncate(summary, 160))

        header: str = f"<!-- Source: {ONLINE_ROOT}{self.rel} -->\n\n"
        source: str = "examples/" + self.rel[len("examples/"):-5]
        if self.rel.startswith("examples/") and os.path.isfile(
                os.path.join(self.site.sdkRoot, source)):
            link: str = os.path.relpath(os.path.join(self.site.sdkRoot, source),
                                        os.path.join(self.site.mdRoot, self.dir))
            header += f"Local source: [{source}]({link.replace(os.sep, '/')})\n\n"
            self.site.sources[self.rel[:-5] + ".md"] = source
        return header + markdown

    def CollectTableSymbol(self, table: Tag, tr: Tag, cells: list[str]) -> None:
        """Records the symbol of a row in a constant or type id table for `symbols.tsv`.

        Constants and type ids are documented as table rows and are therefore missing in the Sphinx
        inventory. The anchor is the row link of the symbol or else the closest anchor above it.
        """
        if not self.rel.startswith(("consts/", "types/")) or len(cells) < 2:
            return
        first: Tag | None = tr.find(("td", "th"))
        name: str = first.get_text().strip() if first else ""
        if not re.fullmatch(r"(c4d\.)?[A-Za-z_][A-Za-z0-9_]*", name):
            return
        link: Tag | None = first.find("a", href=re.compile("^#"))
        target: Tag | None = table.find_parent(attrs={"id": True})
        anchor: str = link["href"][1:] if link else (target["id"] if target else "")
        name = name if name.startswith("c4d.") else "c4d." + name
        role: str = "c4d:constant" if self.rel.startswith("consts/") else "c4d:type"
        desc: str = re.sub(r"<br>.*", "", cells[-1]).replace("\\|", "|")
        desc = Truncate(re.sub(r"[*`]|\[([^\]]*)\]\([^)]*\)", r"\1", desc), 120)
        path: str = self.rel[:-5] + ".md" + (f"#{anchor}" if anchor else "")
        self.site.tableSymbols.append((name, role, path, desc))


# --- Markdown helpers -------------------------------------------------------------------------

def Clean(text: str) -> str:
    """Collapses the whitespace of inline Markdown while keeping explicit line breaks.
    """
    lines: list[str] = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("  \n")]
    return "  \n".join(line for line in lines if line).strip()


def Wrap(text: str, marker: str) -> str:
    """Wraps #text into an emphasis #marker, keeping surrounding whitespace outside the markers.
    """
    stripped: str = text.strip()
    if not stripped:
        return text
    lead: str = text[: len(text) - len(text.lstrip())]
    trail: str = text[len(text.rstrip()):]
    return f"{lead}{marker}{stripped}{marker}{trail}"


def Backtick(text: str) -> str:
    """Returns #text as an inline code span which is safe for embedded backticks.
    """
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return ""
    if "`" not in text:
        return f"`{text}`"
    return f"`` {text} ``"


def Anchor(name: str) -> str:
    """Returns an HTML anchor tag which keeps a Sphinx id addressable in Markdown.
    """
    return f'<a id="{name}"></a>'


def FoldAnchors(blocks: list[str]) -> list[str]:
    """Removes repeated anchor ids and moves anchor only blocks into the following heading.

    Code blocks are passed through unchanged, they can contain HTML anchors as literal text.
    """
    seen: set[str] = set()
    anchorPattern: re.Pattern = re.compile(r'<a id="([^"]*)"></a>')

    def dedupe(match: re.Match) -> str:
        if match.group(1) in seen:
            return ""
        seen.add(match.group(1))
        return match.group(0)

    result: list[str] = []
    pending: str = ""
    for block in blocks:
        if not block.startswith("```"):
            block = anchorPattern.sub(dedupe, block).rstrip()
        if not block.strip():
            continue
        if anchorPattern.sub("", block).strip() == "":
            pending += block.strip()
            continue
        if pending and block.startswith("#"):
            block += " " + pending
        elif pending:
            result.append(pending)
        pending = ""
        result.append(block)
    if pending:
        result.append(pending)
    return result


def Fence(code: str, lang: str) -> str:
    """Returns a fenced code block whose fence is longer than any backtick run in #code.
    """
    code = code.strip("\n")
    longest: int = max((len(m) for m in re.findall(r"`+", code)), default=0)
    fence: str = "`" * max(3, longest + 1)
    return f"{fence}{lang}\n{code}\n{fence}"


def Quote(text: str) -> str:
    """Prefixes every line of #text with a block quote marker.
    """
    return "\n".join(("> " + line) if line else ">" for line in text.split("\n"))


def Indent(marker: str, body: str) -> str:
    """Returns a list item whose continuation lines are indented to the width of #marker.
    """
    pad: str = " " * len(marker)
    lines: list[str] = body.split("\n")
    rest: list[str] = [(pad + line) if line else "" for line in lines[1:]]
    return "\n".join([marker + lines[0]] + rest)


def MergeBullets(blocks: list[str]) -> list[str]:
    """Merges consecutive single line bullet blocks, such as cards, into one tight list.
    """
    result: list[str] = []
    for block in blocks:
        if result and block.startswith("- ") and "\n" not in block \
                and result[-1].startswith("- ") and "\n\n" not in result[-1]:
            result[-1] += "\n" + block
        else:
            result.append(block)
    return result


def Truncate(text: str, length: int) -> str:
    """Shortens #text to its first sentence, but at most to #length characters.
    """
    text = re.sub(r"\s+", " ", text).strip()
    match: re.Match | None = re.match(r"(.+?[.!?])(\s|$)", text)
    if match:
        text = match.group(1)
    return text if len(text) <= length else text[: length - 1].rstrip() + "\u2026"


# --- Indexes ----------------------------------------------------------------------------------

def ReadInventory(path: str) -> list[tuple[str, str, str, str]]:
    """Reads a Sphinx `objects.inv` file and returns (name, role, uri, display name) tuples.
    """
    with open(path, "rb") as f:
        for _ in range(4):
            f.readline()
        data: str = zlib.decompress(f.read()).decode("utf-8")
    entries: list[tuple[str, str, str, str]] = []
    pattern: re.Pattern = re.compile(r"(.+?)\s+(\S+)\s+(-?\d+)\s+?(\S*)\s+(.*)")
    for line in data.splitlines():
        match: re.Match | None = pattern.match(line.rstrip())
        if not match:
            continue
        name, role, _, uri, display = match.groups()
        if uri.endswith("$"):
            uri = uri[:-1] + name
        entries.append((name, role, uri, name if display == "-" else display))
    return entries


def ReadDescriptionSymbols(site: Site) -> list[tuple[str, str, str, str]]:
    """Returns the symbols of the description resources in `.agents/descriptions`.

    Every description file yields its resource symbol, e.g. `Osphere`, its parameter symbols, and
    the cycle values of its parameters. Inherited parameters such as those of `Obase` are repeated
    in hundreds of files; symbols found in more than three files are therefore listed once, pointing
    to the smallest description that contains them, which is the description that declares them.
    """
    folder: str = os.path.join(site.sdkRoot, ".agents", "descriptions")
    if not os.path.isdir(folder):
        return []
    resources: list[tuple[str, str, str, str]] = []
    occurrences: dict[tuple[str, str], list[tuple[int, str, str]]] = {}
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md") or name.startswith("_"):
            continue
        with open(os.path.join(folder, name), encoding="utf-8") as f:
            text: str = f.read()
        symbol: re.Match | None = re.search(r"^- \*\*Symbol:\*\* `([^`]+)`", text, re.M)
        title: re.Match | None = re.search(r"^# Description: (.+)$", text, re.M)
        owner: str = symbol.group(1) if symbol else name[:-3]
        path: str = f".agents/descriptions/{name}"
        resources.append((owner, "description", path, title.group(1) if title else owner))
        rows: list[list[str]] = [
            [c.strip() for c in line.split(" | ")] for line in text.splitlines()
            if line.count(" | ") >= 6 and not line.startswith(("Name |", "----"))]
        for row in rows:
            label, param, dataType, cycles = row[0], row[1], row[2], row[-1]
            if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", param):
                occurrences.setdefault((param, "description:parameter"), []).append(
                    (len(rows), path, f"{owner}: {label} ({dataType})"))
            for cycle in filter(None, (c.strip() for c in cycles.split(";"))):
                occurrences.setdefault((cycle, "description:cycle"), []).append(
                    (len(rows), path, f"{owner}: value of {param}"))
    entries: list[tuple[str, str, str, str]] = resources
    for (symbol, role), found in occurrences.items():
        unique: dict[str, tuple[int, str, str]] = {p: (n, p, t) for n, p, t in found}
        if len(unique) > 3:
            count, path, title = min(unique.values())
            entries.append((symbol, role, path, f"{title}, shared by {len(unique)} descriptions"))
        else:
            entries.extend((symbol, role, path, title) for _, path, title in unique.values())
    return entries


def WriteSymbols(site: Site) -> int:
    """Writes `docs_md/symbols.tsv`, the symbol lookup table of the SDK.

    The table merges the Sphinx inventory (modules, classes, functions, methods, attributes, pages),
    the constants and type ids of the constant and type tables, and the description resources with
    their parameter and cycle symbols. Paths are relative to the SDK root.
    """
    entries: list[tuple[str, str, str, str]] = []
    for name, role, uri, display in ReadInventory(os.path.join(site.htmlRoot, "objects.inv")):
        path, _, fragment = uri.partition("#")
        if path.endswith(".html"):
            path = path[:-5] + ".md"
        if not os.path.isfile(os.path.join(site.mdRoot, path)):
            continue  # Generated Sphinx pages such as the search page are not converted.
        entries.append((name, role, path + (f"#{fragment}" if fragment else ""), display))
    known: set[str] = {e[0] for e in entries}
    tableSymbols: dict[tuple[str, str], tuple[str, str, str, str]] = {}
    for entry in site.tableSymbols:
        if entry[0] not in known:
            tableSymbols.setdefault((entry[0], entry[2]), entry)
    entries += tableSymbols.values()
    entries = [(n, r, "docs_md/" + p, t) for n, r, p, t in entries]
    entries += ReadDescriptionSymbols(site)

    lines: list[str] = ["name\trole\tpath\ttitle"]
    for name, role, path, title in sorted(entries, key=lambda e: (e[0].lower(), e[1], e[2])):
        lines.append(f"{name}\t{role}\t{path}\t{title}")
    with open(os.path.join(site.mdRoot, "symbols.tsv"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    return len(entries)


# Index file name, title, description, and the path prefixes of the pages the index lists.
INDEX_SECTIONS: list[tuple[str, str, str, tuple[str, ...]]] = [
    ("manuals", "Manuals", "Conceptual guides: quickstart, scene structure, plugins, resources.",
     ("manuals/",)),
    ("cinema_api", "Cinema API Reference",
     "Modules, classes, and functions of `c4d` and `mxutils`.",
     ("modules/c4d", "modules/cinema_api", "modules/mxutils")),
    ("maxon_api", "Maxon API Reference",
     "Frameworks, interfaces, data types, and enums of the `maxon` package.",
     ("modules/maxon",)),
    ("types", "Type Indexes", "Object, tag, shader, material, track, and field type ids.",
     ("types/",)),
    ("consts", "Constants", "Enumerations and symbol groups such as `COPYFLAGS` or `DIRTYFLAGS`.",
     ("consts/",)),
    ("examples", "Examples", "Annotated example scripts and plugins of the SDK.",
     ("examples/",)),
    ("indexes", "Other Indexes", "What's new, example index, type index, resource index.",
     ("indexes/",)),
]


def WriteIndexes(site: Site) -> None:
    """Writes `docs_md/INDEX.md` and one page list per documentation section.

    Pages named `index.md` are nested by folder depth, which reproduces the class hierarchy of the
    Cinema API, all other pages are grouped under a heading per folder.
    """
    os.makedirs(os.path.join(site.mdRoot, "index"), exist_ok=True)
    top: list[str] = [
        f"# {SDK_TITLE}: Markdown Documentation Index", "",
        "Markdown conversion of the official HTML documentation. Every page mirrors the path of "
        f"the online page under {ONLINE_ROOT} with `.html` replaced by `.md`.", "",
        "- Find a symbol: search [symbols.tsv](symbols.tsv) for its name, for example "
        "`c4d.documents.BaseDocument.InsertObject`, `c4d.COPYFLAGS_NO_HIERARCHY`, `Osphere`, or "
        "`PRIM_SPHERE_RAD`. The `path` column is the file and anchor relative to the SDK root.",
        "- Start page of the documentation: [index.md](index.md)", ""]
    for fileName, title, description, prefixes in INDEX_SECTIONS:
        def Key(page: str) -> str:
            return page[:-9] if page.endswith("/index.md") else page

        pages: list[str] = sorted((p for p in site.pages if p.startswith(prefixes)), key=Key)
        lines: list[str] = [f"# {title}", "", f"> {description}", ""]
        folder: str = prefixes[0].split("/")[0]
        for page in pages:
            pageTitle, summary = site.pages[page]
            depth: int = 0
            if page.endswith("/index.md"):
                depth = max(0, Key(page).count("/") - 1)
            elif os.path.dirname(page) != folder:
                folder = os.path.dirname(page)
                lines += ["", f"## {folder}", ""]
            entry: str = f"{'  ' * depth}- [{pageTitle or page}](../{page})"
            if page in site.sources:
                entry += f" ([source](../../{site.sources[page]}))"
            lines.append(entry + (f": {summary}" if summary and fileName != "consts" else ""))
        with open(os.path.join(site.mdRoot, "index", fileName + ".md"), "w", encoding="utf-8",
                  newline="\n") as f:
            f.write("\n".join(lines) + "\n")
        top.append(f"- [{title}](index/{fileName}.md): {description} ({len(pages)} pages)")
    with open(os.path.join(site.mdRoot, "INDEX.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(top) + "\n")


def WriteLlmsTxt(site: Site) -> None:
    """Writes the curated `llms.txt` entry point into the SDK root.
    """
    def Entry(page: str, root: str = "docs_md/") -> str:
        title, summary = site.pages.get(page, (page, ""))
        if not summary and page.endswith("/index.md"):
            # Modules without a description are summarized by the classes they contain.
            folder: str = page[:-8]
            names: list[str] = [site.pages[p][0].split(".")[-1] for p in sorted(site.pages)
                                if p.startswith(folder) and p.endswith("/index.md") and p != page]
            if names:
                more: str = ", \u2026" if len(names) > 16 else ""
                summary = "Classes: " + ", ".join(names[:16]) + more
        return f"- [{title}]({root}{page})" + (f": {summary}" if summary else "")

    manuals: list[str] = [Entry(p) for p in sorted(site.pages) if p.startswith("manuals/")]
    modules: list[str] = [
        Entry(p) for p in sorted(site.pages)
        if re.fullmatch(r"modules/[^/]+/index\.md|modules/([^/]+/)?[^/]+_api\.md", p)]
    agentGuides: list[str] = []
    agentsDir: str = os.path.join(site.sdkRoot, ".agents")
    for name in sorted(os.listdir(agentsDir)):
        if name.endswith(".md"):
            with open(os.path.join(agentsDir, name), encoding="utf-8") as f:
                heading: str = next((l.lstrip("# ").strip() for l in f if l.startswith("#")), name)
            agentGuides.append(f"- [{heading}](.agents/{name})")
    text: str = "\n".join([
        f"# {SDK_TITLE}", "",
        "> Python API of Maxon Cinema 4D: the `c4d` (Cinema API), `maxon` (Maxon API), and "
        "`mxutils` packages, with manuals, constant tables, and runnable examples. This repository "
        "holds the official SDK download with its HTML documentation converted to Markdown in "
        "`docs_md/`.", "",
        "How to use this repository:", "",
        "- Look up any class, method, function, constant (`c4d.COPYFLAGS_NO_HIERARCHY`), type id "
        "(`c4d.Osphere`), description resource (`Osphere`), or description parameter "
        "(`PRIM_SPHERE_RAD`) by name in [docs_md/symbols.tsv](docs_md/symbols.tsv). Columns: "
        "name, role, path#anchor relative to the SDK root, title. Grep it, it is too large to "
        "read whole.",
        "- Markdown pages mirror the online documentation paths; `<a id=\"...\"></a>` tags keep "
        "the original Sphinx anchors, so `#c4d.BaseObject.GetMg` style fragments resolve.",
        "- Description parameter ids of objects, tags, and materials are in "
        "[.agents/descriptions](.agents/descriptions/_overview.md); node space ports are in "
        "[.agents/nodespaces](.agents/nodespaces/_overview.md).",
        "- Example source code lives in [examples/](examples/); coding rules for agents are in "
        "[AGENTS.md](AGENTS.md).", "",
        "## Indexes", "",
        "- [Documentation index](docs_md/INDEX.md): all sections with page counts",
        "- [Documentation start page](docs_md/index.md)",
        "- [What's new](docs_md/indexes/whatisnew.md): changes in this release",
        "- [Symbol table](docs_md/symbols.tsv): API symbols, constants, type ids, and description "
        "parameters mapped to their files", "",
        "## Manuals", "", *manuals, "",
        "## API Reference", "", *modules, "",
        "## Agent Guides", "", *agentGuides, "",
        "## Optional", "",
        *[f"- [{t}](docs_md/index/{f}.md): {d}" for f, t, d, _ in INDEX_SECTIONS], ""])
    with open(os.path.join(site.sdkRoot, "llms.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main() -> None:
    """Converts all pages, copies assets, and writes the indexes.
    """
    here: str = os.path.dirname(os.path.abspath(__file__))
    sdkRoot: str = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "..", "..")
    site: Site = Site(sdkRoot)
    if os.path.isdir(site.mdRoot):
        shutil.rmtree(site.mdRoot)
    os.makedirs(site.mdRoot)

    pages: list[str] = site.HtmlPages()
    for i, rel in enumerate(pages):
        markdown: str = PageConverter(site, rel).Convert()
        target: str = os.path.join(site.mdRoot, rel[:-5] + ".md")
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8", newline="\n") as f:
            f.write(markdown)
        if i % 200 == 0:
            print(f"[{i}/{len(pages)}] {rel}")

    for asset in sorted(site.assets):
        target = os.path.join(site.mdRoot, asset)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        shutil.copy2(os.path.join(site.htmlRoot, asset), target)

    symbolCount: int = WriteSymbols(site)
    WriteIndexes(site)
    WriteLlmsTxt(site)
    print(f"Converted {len(pages)} pages, copied {len(site.assets)} assets, "
          f"indexed {symbolCount} symbols.")


if __name__ == "__main__":
    main()
