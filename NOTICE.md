# Notice

This repository contains the Cinema 4D Python SDK 2027.0.0 by Maxon Computer GmbH, as distributed at
<https://developers.maxon.net>. The SDK is licensed under the Creative Commons
Attribution-NoDerivatives 4.0 International License, see [LICENSE.md](LICENSE.md). Code examples of the
SDK may be used, modified, and redistributed freely, as stated in the SDK license.

Differences to the original download:

- The HTML documentation in `docs/` is not included. Its pages are provided in `docs_md/` in
  Markdown format instead, with the text unchanged. Navigation, scripts, and interactive widgets of
  the HTML pages are omitted. The original online documentation is available at
  <https://developers.maxon.net/docs/py/2027_0_0/index.html>; every Markdown page names the URL
  of its source page in its first line.
- `llms.txt`, `NOTICE.md`, `.gitignore`, `docs_md/INDEX.md`, `docs_md/index/`, and
  `docs_md/symbols.tsv` are generated navigation aids which are not part of the SDK.
- `AGENTS.md` lists `llms.txt` as an additional entry point.
- `projects/sdk_markdown/convert.py` is the tool that generates `docs_md/`, `llms.txt`, and the
  indexes from the HTML documentation. Run it from an SDK download that contains `docs/`.

Cinema 4D and Maxon are trademarks of Maxon Computer GmbH. This repository is not affiliated with or
endorsed by Maxon Computer GmbH.
