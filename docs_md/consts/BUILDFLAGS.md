<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/BUILDFLAGS.html -->

# BUILDFLAGS <a id="buildflags"></a>

| Symbol ID | Description |
|---|---|
| BUILDFLAGS_NONE | The object is being built with no special context. This flag being set as the only flag is extremely rare and the actual ‘default’ flag is *BUILDFLAGS_INTERACTIVEEDITOR*. |
| BUILDFLAGS_INTERNALRENDERER | The object is being built for the internal render event. |
| BUILDFLAGS_EXTERNALRENDERER | The object is being built for an external render event. This covers the vast majority of render events these days. It is also common practice to check both render flags in tandem and treat them as one context. |
| BUILDFLAGS_ISOPARM | The object is being built for its iso-parametric representation, you must return a [`c4d.LineObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/LineObject/index.md#c4d.LineObject) that is the iso-parametric representation of your object. |
| BUILDFLAGS_EXPORTONLY | The object is being built for export by a scene exporter plugin such as Alembic, FBX, USD, etc. |
| BUILDFLAGS_INTERACTIVEEDITOR | The object is being built for the viewport. This is the default context for building and what plugins will implicitly use when they do not explicitly check for build flags. |
| BUILDFLAGS_PRIVATE_NO_CLEAR_PASS | Internal, do not use. |
| BUILDFLAGS_PREROLL | The object is being built for a pre-roll event, e.g., a caching or rendering mechanism that is meant to start from a certain frame in the document and is now advancing through the timeline to reach that frame. |
| BUILDFLAGS_MAKEEDITABLE | The object is being built for being made editable. This happens when the user presses the *C* key or invokes the *Make Editable* command from the context menu in the Object Manager to collapse the object to its cache. |
