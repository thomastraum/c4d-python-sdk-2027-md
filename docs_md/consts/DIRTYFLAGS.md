<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/DIRTYFLAGS.html -->

# DIRTYFLAGS <a id="dirtyflags"></a>

Expresses dirty state categories for a single scene element. Unlike `HDIRTYFLAGS`, these flags only track changes on the element itself.

|   |   |
|---|---|
| *DIRTYFLAGS_NONE* | Signals no state. |
| *DIRTYFLAGS_MATRIX* | Signals that the matrix of a [`BaseObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) has changed. |
| *DIRTYFLAGS_DATA* | Signals that container or parameter data of a scene element has changed. |
| *DIRTYFLAGS_SELECT* | Signals that a point, edge, or polygon selection of a [`BaseObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) has changed. |
| *DIRTYFLAGS_CACHE* | Signals that the cache of a [`BaseObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) has changed or been rebuilt. |
| *DIRTYFLAGS_CHILDREN* | Signals that owned child data of a scene element, such as animation keys, has changed. |
| *DIRTYFLAGS_DESCRIPTION* | Signals that the description of a scene element has changed. |
| *DIRTYFLAGS_VISIBILITY* | Signals that the visibility state of a scene element has changed. |
| *DIRTYFLAGS_SELECTION_OBJECTS* | Signals that the object selection of a [`BaseDocument`](../modules/c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) has changed. |
| *DIRTYFLAGS_SELECTION_TAGS* | Signals that the tag selection of a [`BaseDocument`](../modules/c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) has changed. |
| *DIRTYFLAGS_SELECTION_MATERIALS* | Signals that the material selection of a [`BaseDocument`](../modules/c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) has changed. |
| *DIRTYFLAGS_ALL* | Signals all states. |
