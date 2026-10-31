<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/HierarchyHelp/index.html -->

# c4d.plugins.HierarchyHelp <a id="c4d-plugins-hierarchyhelp"></a>

## *class* `c4d.plugins.HierarchyHelp` <a id="c4d.plugins.HierarchyHelp"></a>

Provides read-only context for virtual object hierarchy evaluation.

Instances are provided by Cinema 4D in callbacks such as `ObjectData.GetVirtualObjects()` and Python generator *main()*.

## Overview <a id="overview"></a>

**Evaluation Context**

- [`HierarchyHelp.GetDocument()`](#c4d.plugins.HierarchyHelp.GetDocument): Returns the document for the current hierarchy evaluation.
- [`HierarchyHelp.GetMg()`](#c4d.plugins.HierarchyHelp.GetMg): Returns the cached global matrix for the current hierarchy evaluation.
- [`HierarchyHelp.GetThread()`](#c4d.plugins.HierarchyHelp.GetThread): Returns the calling thread for the hierarchy evaluation.

**Evaluation State**

- [`HierarchyHelp.GetBuildFlags()`](#c4d.plugins.HierarchyHelp.GetBuildFlags): Returns the build flags for the current hierarchy evaluation.
- [`HierarchyHelp.GetLOD()`](#c4d.plugins.HierarchyHelp.GetLOD): Returns the level of detail for the current hierarchy evaluation.
- [`HierarchyHelp.IsProfilingEnabled()`](#c4d.plugins.HierarchyHelp.IsProfilingEnabled): Returns if hierarchy profiling is enabled.

## Members <a id="members"></a>

### Evaluation Context <a id="c4d.plugins.HierarchyHelp-method-Evaluation-Context"></a>

#### `HierarchyHelp.GetDocument(self)` <a id="c4d.plugins.HierarchyHelp.GetDocument"></a>

Returns the document for the current hierarchy evaluation.

**Return type:** Optional[[c4d.documents.BaseDocument](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]

**Returns:** The document, or **None**.

#### `HierarchyHelp.GetMg(self)` <a id="c4d.plugins.HierarchyHelp.GetMg"></a>

Returns the cached global matrix for the current hierarchy evaluation.

**Return type:** [c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The global matrix.

#### `HierarchyHelp.GetThread(self)` <a id="c4d.plugins.HierarchyHelp.GetThread"></a>

Returns the calling thread for the hierarchy evaluation.

**Return type:** Optional[[c4d.threading.BaseThread](../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)]

**Returns:** The thread, or **None**.

### Evaluation State <a id="c4d.plugins.HierarchyHelp-method-Evaluation-State"></a>

#### `HierarchyHelp.GetBuildFlags(self)` <a id="c4d.plugins.HierarchyHelp.GetBuildFlags"></a>

Returns the build flags for the current hierarchy evaluation.

**Return type:** int

**Returns:**

Flags:

| Symbol ID | Description |
|---|---|
| BUILDFLAGS_NONE | The object is being built with no special context. This flag being set as the only flag is extremely rare and the actual ‘default’ flag is *BUILDFLAGS_INTERACTIVEEDITOR*. |
| BUILDFLAGS_INTERNALRENDERER | The object is being built for the internal render event. |
| BUILDFLAGS_EXTERNALRENDERER | The object is being built for an external render event. This covers the vast majority of render events these days. It is also common practice to check both render flags in tandem and treat them as one context. |
| BUILDFLAGS_ISOPARM | The object is being built for its iso-parametric representation, you must return a [`c4d.LineObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/LineObject/index.md#c4d.LineObject) that is the iso-parametric representation of your object. |
| BUILDFLAGS_EXPORTONLY | The object is being built for export by a scene exporter plugin such as Alembic, FBX, USD, etc. |
| BUILDFLAGS_INTERACTIVEEDITOR | The object is being built for the viewport. This is the default context for building and what plugins will implicitly use when they do not explicitly check for build flags. |
| BUILDFLAGS_PRIVATE_NO_CLEAR_PASS | Internal, do not use. |
| BUILDFLAGS_PREROLL | The object is being built for a pre-roll event, e.g., a caching or rendering mechanism that is meant to start from a certain frame in the document and is now advancing through the timeline to reach that frame. |
| BUILDFLAGS_MAKEEDITABLE | The object is being built for being made editable. This happens when the user presses the *C* key or invokes the *Make Editable* command from the context menu in the Object Manager to collapse the object to its cache. |

#### `HierarchyHelp.GetLOD(self)` <a id="c4d.plugins.HierarchyHelp.GetLOD"></a>

Returns the level of detail for the current hierarchy evaluation.

**Return type:** float

**Returns:** The level of detail.

#### `HierarchyHelp.IsProfilingEnabled(self)` <a id="c4d.plugins.HierarchyHelp.IsProfilingEnabled"></a>

Returns if hierarchy profiling is enabled.

**Return type:** bool

**Returns:** **True** when profiling is enabled.
