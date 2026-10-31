<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/UNDOTYPE.html -->

# UNDOTYPE <a id="undotype"></a>

| Symbol ID | Description |
|---|---|
| UNDOTYPE_NONE | None. |
| UNDOTYPE_CHANGE | Any change to an object, including hierarchy modifications; modification in positioning (object has been moved from A to B), substructures etc. (Needs to be called *before* the change.) |
| UNDOTYPE_CHANGE_NOCHILDREN | Same as *UNDOTYPE_CHANGE*, but without child modifications. (Needs to be called *before* the change.) |
| UNDOTYPE_CHANGE_SMALL | Change to local data only (e.g. data container), no substructures (e.g. no tags on an object) and no children. (Needs to be called *before* the change.) |
| UNDOTYPE_CHANGE_SELECTION | Change to point/poly/edge selection only. (Needs to be called *before* the change.) |
| UNDOTYPE_NEWOBJ | New object/node/tag etc. was created. (Needs to be called *after* the change.) |
| UNDOTYPE_DELETEOBJ | Object/node/tag etc. to be deleted. (Needs to be called *before* the change.) |
| UNDOTYPE_ACTIVATE | Automatically managed by `BaseDocument.SetActiveObject()`/`SetActiveTag()`/`SetActiveMaterial()` etc. No need to use manually. |
| UNDOTYPE_DEACTIVATE | Automatically managed by `BaseDocument.SetActiveObject()`/`SetActiveTag()`/`SetActiveMaterial()` etc. No need to use manually. |
| UNDOTYPE_BITS | Change to object bits, e.g. selection status. (Needs to be called *before* the change.) |
| UNDOTYPE_HIERARCHY_PSR | Change in hierarchical placement and PSR values. (Needs to be called *before* the change.) |
| UNDOTYPE_PRIVATE_STRING | Private |
| UNDOTYPE_PRIVATE_MULTISELECTIONAXIS | Private. |
| UNDOTYPE_START | Private. |
| UNDOTYPE_END | Private. |
