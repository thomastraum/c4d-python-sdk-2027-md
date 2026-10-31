<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/DRAGTYPE.html -->

# DRAGTYPE <a id="dragtype"></a>

|   |   |
|---|---|
| *DRAGTYPE_ATOMARRAY* | Atom array. The data is a list of [`c4d.C4DAtom`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom). |
| *DRAGTYPE_CMDPALETTE* | Not supported. |
| *DRAGTYPE_COMMAND* | Not supported. |
| *DRAGTYPE_DESCID* | Description ID. The data is a dict(‘did’: [`c4d.DescID`](../modules/c4d/DescID/index.md#c4d.DescID), ‘arr’: list of [`c4d.C4DAtom`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom)). |
| *DRAGTYPE_ICON* | Not supported. |
| *DRAGTYPE_FILES* | Files. The data is a string with the filename. |
| *DRAGTYPE_FILENAME_IMAGE* | Image. The data is a string with the filename. |
| *DRAGTYPE_FILENAME_OTHER* | Other filename. The data is a string with the filename. |
| *DRAGTYPE_FILENAME_SCENE* | Scene filename. The data is a string with the filename. |
| *DRAGTYPE_MANAGER* | Not supported. |
| *DRAGTYPE_RGB* | RGB color. The data is a [`c4d.Vector`](../modules/c4d/Vector/index.md#c4d.Vector). |
| *DRAGTYPE_RGB_ARRAY* | RGB color array. The data is a list of [`c4d.Vector`](../modules/c4d/Vector/index.md#c4d.Vector). |
| *DRAGTYPE_RGBA_ARRAY* | RGBA color array. The data is a [`maxon.BaseArray`](../modules/maxon_generated/datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) of [`maxon.ColorA`](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA.md#module-maxon.ColorA). |
| *DRAGTYPE_BROWSER* | Browser drag message. The data is a list of string with the filename. |
| *DRAGTYPE_ASSET* | *New in version 2023.2.0:* Message ID for Asset browser assets, the message data is a [`maxon.DragAndDropDataAssetArray`](../modules/maxon_generated/frameworks/asset/datatype/maxon.DragAndDropDataAssetArray.md#module-maxon.DragAndDropDataAssetArray). Exposed as *maxon.DRAGTYPE_ASSET* in Python. |
