<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/render/InitRenderStruct/index.html -->

# c4d.modules.render.InitRenderStruct <a id="c4d-modules-render-initrenderstruct"></a>

## *class* `c4d.modules.render.InitRenderStruct` <a id="c4d.modules.render.InitRenderStruct"></a>

**Attributes**

## `c4d.modules.render.InitRenderStruct.version` <a id="c4d.modules.render.InitRenderStruct.version"></a>

[Read-only]

The version of Cinema 4D.

**Type:** int

## `c4d.modules.render.InitRenderStruct.time` <a id="c4d.modules.render.InitRenderStruct.time"></a>

[Read-only]

The current time.

**Type:** [`BaseTime`](../../../c4d/BaseTime/index.md#c4d.BaseTime)

## `c4d.modules.render.InitRenderStruct.fps` <a id="c4d.modules.render.InitRenderStruct.fps"></a>

[Read-only]

The framerate.

**Type:** int

## `c4d.modules.render.InitRenderStruct.docpath` <a id="c4d.modules.render.InitRenderStruct.docpath"></a>

[Read-only]

The path for the document.

**Type:** str

## `c4d.modules.render.InitRenderStruct.vd` <a id="c4d.modules.render.InitRenderStruct.vd"></a>

[Read-only]

The volume data.

**Type:** Optional[c4d.modules.render.VolumeData]

> **Note:** Can be **None**, always check.

## `c4d.modules.render.InitRenderStruct.doc` <a id="c4d.modules.render.InitRenderStruct.doc"></a>

[Read-only]

The document to render.

**Type:** Optional[c4d.documents.BaseDocument]

> **Note:** Can be **None**, always check.

## `c4d.modules.render.InitRenderStruct.thread` <a id="c4d.modules.render.InitRenderStruct.thread"></a>

[Read-only]

The current thread or **None** for the main Cinema 4D thread.

**Type:** Optional[c4d.threading.BaseThread]

## `c4d.modules.render.InitRenderStruct.flags` <a id="c4d.modules.render.InitRenderStruct.flags"></a>

[Read-only]

Flags:

|   |   |
|---|---|
| *INITRENDERFLAG_NONE* | No flags. |
| *INITRENDERFLAG_TEXTURES* | Use textures. |
| *INITRENDERFLAG_PAINTERNOMIP* | Disable MIP for painting. |
| *INITRENDERFLAG_NOMIP* | Disable MIP. |
| *INITRENDERFLAG_PREVIEWRENDER* | Preview render. |
| *INITRENDERFLAG_IRR* | Interactive region render. |

## `c4d.modules.render.InitRenderStruct.linear_workflow` <a id="c4d.modules.render.InitRenderStruct.linear_workflow"></a>

[Read/Write]

*Changed in version R17.032:* Attribute can be set.

Linear workflow enabled/disabled.

**Type:** bool

## `c4d.modules.render.InitRenderStruct.document_colorprofile` <a id="c4d.modules.render.InitRenderStruct.document_colorprofile"></a>

[Read/Write]

*Changed in version R17.032:* Attribute can be set.

The color profile of the document:

|   |   |
|---|---|
| *DOCUMENT_COLORPROFILE_SRGB* | sRGB color profile. |
| *DOCUMENT_COLORPROFILE_LINEAR* | Linear color profile. |
| *DOCUMENT_COLORPROFILE_DISABLED* | Color profile disabled. |

## Overview <a id="overview"></a>

- [`InitRenderStruct.__init__()`](#c4d.modules.render.InitRenderStruct.__init__): Initializes a new [`InitRenderStruct`](#c4d.modules.render.InitRenderStruct), optionally from *doc* [`BaseDocument`](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) if passed.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.modules.render.InitRenderStruct-method-Magic-Methods"></a>

#### `InitRenderStruct.__init__(self, doc)` <a id="c4d.modules.render.InitRenderStruct.__init__"></a>

Initializes a new [`InitRenderStruct`](#c4d.modules.render.InitRenderStruct), optionally from *doc* [`BaseDocument`](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) if passed.

*New in version R18.020.*

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The optional document to initialize with.
