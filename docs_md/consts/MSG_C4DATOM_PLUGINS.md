<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/MSG_C4DATOM_PLUGINS.html -->

# C4DAtom and Plugin Messages <a id="c4datom-and-plugin-messages"></a>

The following messages can be send with `C4DAtom.Message()` and received in the `Message` methods of [`CommandData`](../modules/c4d.plugins/BaseData/CommandData/index.md#c4d.plugins.CommandData), [`FalloffData`](../modules/c4d.plugins/BaseData/FalloffData/index.md#c4d.plugins.FalloffData), [`NodeData`](../modules/c4d.plugins/BaseData/NodeData/index.md#c4d.plugins.NodeData), [`SculptBrushToolData`](../modules/c4d.plugins/BaseData/SculptBrushToolData/index.md#c4d.plugins.SculptBrushToolData), and [`ToolData`](../modules/c4d.plugins/BaseData/ToolData/index.md#c4d.plugins.ToolData) and their derived interfaces.

> **Warning:** Only messages that have an explicit `Broadcast to Atoms` section in their description are supported to be send with `C4DAtom.Message()`, and only messages that have an explicit `Handle in Plugins` section are supported to be received with plugin interfaces. Attempting to send which are not supported in Python will have no effect, or in some cases might even crash Cinema 4D.

| Symbol | Numeric Value | Description |
|---|---|---|
| [c4d.MSG_ANIMATE](#msg-animate) | 300001037 | Sent to objects after they have been animated. |
| [c4d.MSG_BASECONTAINER](#msg-basecontainer) | 9 | Sent to pass arbitrary data in a container to a node. |
| [c4d.MSG_CHANGE](#msg-change) | 7 | Sent if any data except for the matrix has been changed. |
| [c4d.MSG_COLLECTC4DFALLOFF](#msg-collectc4dfalloff) | 440000221 | Sent to atoms that might contain a falloff. |
| [c4d.MSG_COMMANDINFORMATION](#msg-commandinformation) | 300001001 | Sent to retrieve command information. |
| [c4d.MSG_DESCRIPTION_ALLOWOVERRIDE](#msg-description-allowoverride) | 431000094 | Sent to check if take override operation is allowed. |
| [c4d.MSG_DESCRIPTION_CHECKDRAGANDDROP](#msg-description-checkdraganddrop) | 26 | Sent to ask an atom if a drag and drop operation is accepted. |
| [c4d.MSG_DESCRIPTION_CHECKUPDATE](#msg-description-checkupdate) | 17 | Sent to allow elements to determine the type of refresh after a parameter has been changed. |
| [c4d.MSG_DESCRIPTION_COMMAND](#msg-description-command) | 18 | Sent for button description elements. |
| [c4d.MSG_DESCRIPTION_CUSTOMGUI_NOTIFICATION](#msg-description-customgui-notification) | 431000175 | Sent by a custom GUI to its parent node. |
| [c4d.MSG_DESCRIPTION_EDIT_ENTRY](#msg-description-edit-entry) | 25 | Sent to tell an atom to edit a description entry. |
| [c4d.MSG_DESCRIPTION_GETBITMAP](#msg-description-getbitmap) | 27 | Sent to query a description for a [`c4d.gui.BitmapButtonCustomGui`](../modules/c4d.gui/BaseCustomGui/BitmapButtonCustomGui/index.md#c4d.gui.BitmapButtonCustomGui) bitmap. |
| [c4d.MSG_DESCRIPTION_INITUNDO](#msg-description-initundo) | 16 | Sent to allows elements to create undo actions for the following parameter changes. |
| [c4d.MSG_DESCRIPTION_POPUP](#msg-description-popup) | 300001046 | Sent to handle description popup menus in the Attribute Manager. |
| [c4d.MSG_DESCRIPTION_POSTSETPARAMETER](#msg-description-postsetparameter) | 19 | Sent after a `C4DAtom.SetParameter()` call. |
| [c4d.MSG_DESCRIPTION_REMOVE_ENTRY](#msg-description-remove-entry) | 24 | Sent to tell an atom to remove a description entry. |
| [c4d.MSG_DESCRIPTION_VALIDATE](#msg-description-validate) | 20 | Sent to update dependencies or to check for invalid values after a parameter change. |
| [c4d.MSG_DOCUMENT_MODE_CHANGED](#msg-document-mode-changed) | 200000091 | Sent to the active tool plugin when document mode is changed. |
| [c4d.MSG_DOCUMENTINFO](#msg-documentinfo) | 1001078 | Sent when a document has been loaded, saved, merged or other document related actions occurred. |
| [c4d.MSG_DRAGANDDROP](#msg-draganddrop) | 1018756 | Sent to elements in the Object Manager when something is dropped on it. |
| [c4d.MSG_EDIT](#msg-edit) | 21 | Sent to perform an action when element is being edited. |
| [c4d.MSG_FILTER](#msg-filter) | 14 | Sent to allow or block `C4DAtom.MultiMessage()` calls. |
| [c4d.MSG_GET_MODATASELECTION](#msg-get-modataselection) | 1021339 | Sent to retrieve the data of MoGraph selection tags. |
| [c4d.MSG_GET_MODATAWEIGHTS](#msg-get-modataweights) | 440000230 | Sent to retrieve the data for MoGraph weights tags. |
| [c4d.MSG_GETALLASSETS](#msg-getallassets) | 112004 | Sent to retrieve all assets from an object. |
| [c4d.MSG_GETCUSTOMICON](#msg-getcustomicon) | 1001090 | Sent to retrieve a custom icon. |
| [c4d.MSG_GETCUSTOMICON_SETTINGS](#msg-getcustomicon-settings) | 1041699 | Sent to retrieve the custom icon settings of an object. |
| [c4d.MSG_GETREALCAMERADATA](#msg-getrealcameradata) | 1028476 | Sent to get a real camera object from a generator. |
| [c4d.MSG_GETREALTAGDATA](#msg-getrealtagdata) | 1036447 | Sent to get the real tag object from a virtual ‘generator’ tag. |
| [c4d.MSG_MENUPREPARE](#msg-menuprepare) | 22 | Sent to allow tags, objects, shaders etc. to do some setup work when called from the menu. |
| [c4d.MSG_MULTI_CLEARSUGGESTEDFOLDER](#msg-multi-clearsuggestedfolder) | 200000040 | Sent to nodes to convert absolute paths to filename. |
| [c4d.MSG_MULTI_DOCUMENTCLONED](#msg-multi-documentcloned) | 11 | Sent when a document is being cloned. |
| [c4d.MSG_MULTI_RENDERNOTIFICATION](#msg-multi-rendernotification) | 1001071 | Sent to a document and all of its elements before a render starts. |
| [c4d.MSG_POINTS_CHANGED](#msg-points-changed) | 1 | Sent to notify an object its points have changed. |
| [c4d.MSG_POLYGONS_CHANGED](#msg-polygons-changed) | 2 | Sent to notify an object its polygons have changed. |
| [c4d.MSG_RETRIEVEPRIVATEDATA](#msg-retrieveprivatedata) | 23 | Sent to retrieve private data from an atom. |
| [c4d.MSG_SCALEDOCUMENT](#msg-scaledocument) | 300001069 | Sent to signal that another document with different scale has been merged with the current document. |
| [c4d.MSG_SEGMENTS_CHANGED](#msg-segments-changed) | 10 | Sent to notify an object that its segments have changed. |
| [c4d.MSG_SMALLUPDATE](#msg-smallupdate) | 6 | Sent if part of an object has changed and does not need cache rebuilding. |
| [c4d.MSG_UPDATE](#msg-update) | 5 | Sent to inform an object that its bounding box must be recalculated. Otherwise use [MSG_CHANGE](#msg-change). |
| [maxon.neutron.MSG_GET_ASSET_WITH_VERSION](#msg-get-asset-with-version) | 1062823 | Sent to get the identifier of the node asset from which this capsule originates. |
| [c4d.MSG_GETCUSTOM_NAME_ADDITION](#msg-getcustom-name-addition) | 1060371 | Sent to retrieve a custom name addition. |
| [c4d.MSG_CHECKINSIDEUNDO](#msg-checkinsideundo) | 1063385 | Sent to check if the document is currently processing an undo. |
| [c4d.MSG_MULTI_MARKMATERIALS](#msg-multi-markmaterials) | 1073741828 | Sent to do different operations on materials used by a C4DAtom. |

## `c4d.MSG_ANIMATE` <a id="c4d.MSG_ANIMATE"></a> <a id="msg-animate"></a>

Sent to objects after they have been animated.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `None`  
**return**: `None`

## `c4d.MSG_BASECONTAINER` <a id="c4d.MSG_BASECONTAINER"></a> <a id="msg-basecontainer"></a>

Sent to pass arbitrary data in a container to a node.  
It is good practice to qualify the content of the container by settings its container identifier via [`BaseContainer.SetId()`](../modules/c4d/BaseContainer/index.md#c4d.BaseContainer.SetId) or by providing such identifier when instantiating the container.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `c4d.BaseContainer`  
**return**: `None`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `c4d.BaseContainer`  
**return**: `None`

## `c4d.MSG_CHANGE` <a id="c4d.MSG_CHANGE"></a> <a id="msg-change"></a>

Sent to atoms when any data aside from their matrix has been changed.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `None`  
**return**: `None`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `None`  
**return**: `None`

## `c4d.MSG_COLLECTC4DFALLOFF` <a id="c4d.MSG_COLLECTC4DFALLOFF"></a> <a id="msg-collectc4dfalloff"></a>

Sent to atoms that might contain a falloff.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict[]`  
**return**: `` `dict['falloff'] ``

**Parameters:** **falloff** (*c4d.modules.mograph.C4D_Falloff*) – The contained falloff if there is any.

## `c4d.MSG_COMMANDINFORMATION` <a id="c4d.MSG_COMMANDINFORMATION"></a> <a id="msg-commandinformation"></a>

Sent to retrieve command information.  
Allows to restrict shortcuts to a dialog. To do so, `managergroup` has to be set to a dialog identifier. `parentid` can be set to a command identifier to get its shortcut, icon, tooltip etc. For instance, if `IDM_SELECTALL` is set for `parentid`, then `command_id` inherits the “Select All” command of Cinema 4D.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['command_id', 'managergroup', 'parentid']`  
**return**: `dict['managergroup', 'parentid']`

**Parameters:**

- **command_id** (*int*) – The command identifier.
- **managergroup** (*int*) – The identifier of the manger group.
- **parentid** (*int*) – The identifier of the parent.

## `c4d.MSG_DESCRIPTION_ALLOWOVERRIDE` <a id="c4d.MSG_DESCRIPTION_ALLOWOVERRIDE"></a> <a id="msg-description-allowoverride"></a>

Sent to check if take override operation is allowed.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict['_takeData', '_overrideTake', '_descid']`  
**return**: `dict['_parent', '_parentId', '_allow', '_overrideEnabled']`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['_takeData', '_overrideTake', '_descid']`  
**return**: `dict['_parent', '_parentId', '_allow', '_overrideEnabled']`

**Parameters:**

- **_takeData** ([*c4d.modules.takesystem.TakeData*](../modules/c4d.modules/takesystem/TakeData/index.md#c4d.modules.takesystem.TakeData)) – Take system context.
- **_overrideTake** ([*c4d.modules.takesystem.BaseTake*](../modules/c4d.modules/takesystem/BaseTake/index.md#c4d.modules.takesystem.BaseTake)) – The take asking for the override.
- **_descid** ([*c4d.DescID*](../modules/c4d/DescID/index.md#c4d.DescID)) – Description ID to be overridden.
- **_parent** ([*c4d.BaseList2D*](../modules/c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – Parent node if the override must be assigned to it and not to the original node. Especially useful in case of branched structures.
- **_parentId** ([*c4d.DescID*](../modules/c4d/DescID/index.md#c4d.DescID)) – If `parent` is set also a translated parameter ID needs to be set.
- **_allow** (*bool*) – `True` if the parameter can be overridden, otherwise `False`.
- **_overrideEnabled** (*bool*) – `True` if the global switch allow the override, otherwise `False`.

## `c4d.MSG_DESCRIPTION_CHECKDRAGANDDROP` <a id="c4d.MSG_DESCRIPTION_CHECKDRAGANDDROP"></a> <a id="msg-description-checkdraganddrop"></a>

Sent to ask an atom if a drag and drop operation is accepted.  
Not all parameter types that might appear eligible actually do support this message, it is for example not supported by FieldList parameters.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['id', 'element']`  
**return**: `dict['result']`

**Parameters:**

- **id** ([*c4d.DescID*](../modules/c4d/DescID/index.md#c4d.DescID)) – ID of the drop field.
- **element** ([*c4d.BaseList2D*](../modules/c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – Element to drop.
- **result** (*bool*) – Set to `True` if the drop is acceptable, otherwise `False`.

## `c4d.MSG_DESCRIPTION_CHECKUPDATE` <a id="c4d.MSG_DESCRIPTION_CHECKUPDATE"></a> <a id="msg-description-checkupdate"></a>

Sent to allow elements to determine the type of refresh after a parameter has been changed.  
This message is being handled by all plugin base classes.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict['doc', 'drawflags', 'descid']`  
**return**: `None`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `` None````dict['doc', 'drawflags', 'descid'] ``  
**return**: `None`

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../modules/c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The current document.
- **drawflags** (*int*) – Draw flags. See [MSG_DESCRIPTION_CHECKUPDATE](MSG_DESCRIPTION_CHECKUPDATE.md).
- **descid** ([*c4d.DescID*](../modules/c4d/DescID/index.md#c4d.DescID)) – The identifier of the parameter that triggered the command.

## `c4d.MSG_DESCRIPTION_COMMAND` <a id="c4d.MSG_DESCRIPTION_COMMAND"></a> <a id="msg-description-command"></a>

Sent for button description elements.  
See example [here](../modules/c4d.plugins/BaseData/NodeData/index.md#msg-description-command-example).

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict['id']`  
**return**: `None`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['id']`  
**return**: `None`

**Parameters:** **id** ([*c4d.DescID*](../modules/c4d/DescID/index.md#c4d.DescID)) – The identifier of the parameter that did trigger the command.

## `c4d.MSG_DESCRIPTION_CUSTOMGUI_NOTIFICATION` <a id="c4d.MSG_DESCRIPTION_CUSTOMGUI_NOTIFICATION"></a> <a id="msg-description-customgui-notification"></a>

Sent by a custom GUI to its parent node.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['_descId', '_customGuiId', '_subId', '_data']`  
**return**: `None`

**Parameters:**

- **_descId** ([*c4d.DescID*](../modules/c4d/DescID/index.md#c4d.DescID)) – Description ID.
- **_customGuiId** (*int*) – Custom GUI plugin ID.
- **_subId** (*int*) – Message type sub-ID. Depending on the custom GUI implementation a different sub-ID can be passed with different data.
- **_data** ([*c4d.BaseContainer*](../modules/c4d/BaseContainer/index.md#c4d.BaseContainer)) – Data for the message.

## `c4d.MSG_DESCRIPTION_EDIT_ENTRY` <a id="c4d.MSG_DESCRIPTION_EDIT_ENTRY"></a> <a id="msg-description-edit-entry"></a>

Sent to tell an atom to edit a description entry.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict['id']`  
**return**: `None`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['id']`  
**return**: `None`

**Parameters:** **id** ([*c4d.DescID*](../modules/c4d/DescID/index.md#c4d.DescID)) – The identifier of the parameter that did trigger the command.

## `c4d.MSG_DESCRIPTION_GETBITMAP` <a id="c4d.MSG_DESCRIPTION_GETBITMAP"></a> <a id="msg-description-getbitmap"></a>

Sent to query a description for a [`c4d.gui.BitmapButtonCustomGui`](../modules/c4d.gui/BaseCustomGui/BitmapButtonCustomGui/index.md#c4d.gui.BitmapButtonCustomGui) bitmap.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict['id']`  
**return**: `dict['bmp', 'bmpflags']`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['id']`  
**return**: `dict['bmp', 'bmpflags']`

**Parameters:**

- **id** ([*c4d.DescID*](../modules/c4d/DescID/index.md#c4d.DescID)) – The description identifier of the bitmap button.
- **bmp** ([*c4d.bitmaps.BaseBitmap*](../modules/c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – Bitmap for the button.
- **bmpflags** (*int*) – Flags. See [ICONDATAFLAGS](ICONDATAFLAGS.md).

## `c4d.MSG_DESCRIPTION_INITUNDO` <a id="c4d.MSG_DESCRIPTION_INITUNDO"></a> <a id="msg-description-initundo"></a>

Sent to allows elements to create undo actions for the following parameter changes.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['doc', 'descid']`  
**return**: `None`

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../modules/c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The current document.
- **descid** ([*c4d.DescID*](../modules/c4d/DescID/index.md#c4d.DescID)) – The description identifier of the parameter.

## `c4d.MSG_DESCRIPTION_POPUP` <a id="c4d.MSG_DESCRIPTION_POPUP"></a> <a id="msg-description-popup"></a>

Sent to handle description popup menus in the Attribute Manager.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: *dict[‘id’, ‘chosen’, ‘popup’]`*  
**return**: *dict[‘id’, ‘chosen’, ‘popup’]`*

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: *dict[‘id’, ‘chosen’, ‘popup’]`*  
**return**: *dict[‘id’, ‘chosen’, ‘popup’]`*

**Parameters:**

- **id** ([*c4d.DescID*](../modules/c4d/DescID/index.md#c4d.DescID)) – The identifier of the parameter that triggered the command.
- **chosen** (*int*) – Selected element of the popup.
- **popup** ([*c4d.BaseContainer*](../modules/c4d/BaseContainer/index.md#c4d.BaseContainer)) – Popup menu container.

## `c4d.MSG_DESCRIPTION_POSTSETPARAMETER` <a id="c4d.MSG_DESCRIPTION_POSTSETPARAMETER"></a> <a id="msg-description-postsetparameter"></a>

Sent after a [`C4DAtom.SetParameter()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.SetParameter) call.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['descid']`  
**return**: `None`

**Parameters:** **descid** ([*c4d.DescID*](../modules/c4d/DescID/index.md#c4d.DescID)) – The description identifier of the parameter that has been set.

## `c4d.MSG_DESCRIPTION_REMOVE_ENTRY` <a id="c4d.MSG_DESCRIPTION_REMOVE_ENTRY"></a> <a id="msg-description-remove-entry"></a>

Sent to tell an atom to remove a description entry.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['id']`  
**return**: `None`

**Parameters:** **id** ([*c4d.DescID*](../modules/c4d/DescID/index.md#c4d.DescID)) – The identifier of the parameter that did trigger the command.

## `c4d.MSG_DESCRIPTION_VALIDATE` <a id="c4d.MSG_DESCRIPTION_VALIDATE"></a> <a id="msg-description-validate"></a>

Sent to update dependencies or to check for invalid values after a parameter change.  
Used for example to ensure that the inner radius of a light object is always smaller than its outer radius.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['flags']`  
**return**: `None`

**Parameters:** **flags** (*int*) – *Not used*.

## `c4d.MSG_DOCUMENT_MODE_CHANGED` <a id="c4d.MSG_DOCUMENT_MODE_CHANGED"></a> <a id="msg-document-mode-changed"></a>

Sent to the active tool plugin when document mode is changed.

> **See also:**
>
> `BaseDocument.SetMode()`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `None`  
**return**: `None`

## `c4d.MSG_DOCUMENTINFO` <a id="c4d.MSG_DOCUMENTINFO"></a> <a id="msg-documentinfo"></a>

Sent when a document has been loaded, saved, merged or other document related actions occurred.

> **See also:** To send `MSG_DOCUMENTINFO` it is recommended to use `BaseDocument.SendInfo()`.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict['type', 'fileformat', 'filename']`  
**return**: `None`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['type', 'fileformat', 'filename', 'doc', 'bl']`  
**return**: `None`

**Parameters:**

- **type** (*int*) – The message type. See [MSG_DOCUMENTINFO_TYPE](MSG_DOCUMENTINFO_TYPE.md).
- **fileformat** (*int*) – The file format. See [FORMAT Export](FORMAT_export.md).
- **filename** (*str*) – The document filename.
- **doc** ([*c4d.documents.BaseDocument*](../modules/c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The current document.
- **bl** ([*c4d.BaseList2D*](../modules/c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The atom that has been inserted. Is being provided when `type` is `MSG_DOCUMENTINFO_TYPE_OBJECT_INSERT`, `` MSG_DOCUMENTINFO_TYPE_TAG_INSERT``or ``MSG_DOCUMENTINFO_TYPE_MATERIAL_INSERT ``.

## `c4d.MSG_DRAGANDDROP` <a id="c4d.MSG_DRAGANDDROP"></a> <a id="msg-draganddrop"></a>

Sent to elements in the Object Manager when something is dropped on it.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['doc', 'sender', 'flags', 'type', 'data', 'x', 'y', 'msg']`  
**return**: `dict['flags', 'type', 'data', 'result']`

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../modules/c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The current document.
- **sender** (*c4d.BaseList2*) – The sender of the drag operation.
- **flags** (*int*) – The flags of the operation.
- **type** (*int*) – The drag type.
- **data** (*PyCObject*) – The dragged data.
- **x** (*int*) – The x position where the drag operation has been released.
- **y** (*int*) – The y position where the drag operation has been released.
- **msg** ([*c4d.BaseContainer*](../modules/c4d/BaseContainer/index.md#c4d.BaseContainer)) – Valid if `DRAGANDDROP_FLAG_MSGVALID` is set so items like *BFM_INPUT_QUALIFIER* are available.
- **result** (*int*) – *Unused*.

## `c4d.MSG_EDIT` <a id="c4d.MSG_EDIT"></a> <a id="msg-edit"></a>

Sent to perform an action when element is being edited.  
Is being sent for example when the user does edit an object by double-clicking it in the Object Manager.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `None`  
**return**: `None`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `None`  
**return**: `None`

## `c4d.MSG_FILTER` <a id="c4d.MSG_FILTER"></a> <a id="msg-filter"></a>

Sent to allow or block [`C4DAtom.MultiMessage()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.MultiMessage) calls.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['type', 'route', 'data']`  
**return**: `None`

**Parameters:**

- **type** (*int*) – Message type.
- **route** (*int*) – Flags. See [MULTIMSG_ROUTE](MULTIMSG_ROUTE.md).
- **data** (*PyCObject*) – Message data. Depends on the message *type*.

## `c4d.MSG_GET_MODATASELECTION` <a id="c4d.MSG_GET_MODATASELECTION"></a> <a id="msg-get-modataselection"></a>

Sent to retrieve the data of MoGraph selection tags.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict[]`  
**return**: `dict['sel']`

**Parameters:** **sel** ([*c4d.BaseSelect*](../modules/c4d/BaseSelect/index.md#c4d.BaseSelect)) – The selected clones.

## `c4d.MSG_GET_MODATAWEIGHTS` <a id="c4d.MSG_GET_MODATAWEIGHTS"></a> <a id="msg-get-modataweights"></a>

Sent to retrieve the data for MoGraph weights tags.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict[]`  
**return**: `dict['_weight']`

**Parameters:** **_weight** (*list*[*float*]) – The weight data.

## `c4d.MSG_GETALLASSETS` <a id="c4d.MSG_GETALLASSETS"></a> <a id="msg-getallassets"></a>

Sent to retrieve all assets from an object.

> **Warning:** This message is only supported in Python as an outgoing message in node implementations. Sending this message in Python via [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) will crash Cinema 4D. Use instead [`c4d.documents.GetAllAssetsNew()`](../modules/c4d.documents/index.md#c4d.documents.GetAllAssetsNew) to retrieve all asset data from a document.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['doc', 'flags', 'assets']`  
**return**: `dict['assets': list[dict['filename', 'bl', netRequestOnDemand]]]`

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../modules/c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The current document.
- **flags** (*int*) – The flags for the operation.
- **assets** (*list*) – List of assets.
- **filename** (*str*) – Filename of the asset.
- **bl** ([*c4d.BaseList2D*](../modules/c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – Base list reporting the missing name.
- **netRequestOnDemand** (*bool*) – Net request on demand.

## `c4d.MSG_GETCUSTOMICON` <a id="c4d.MSG_GETCUSTOMICON"></a> <a id="msg-getcustomicon"></a>

Sent to retrieve a custom icon.

*Changed in version R21:* An instance of *c4d.IconData* can be passed with the fields `useDat` and `dat` when returning icon data in plugins. The bitmap data inputs will be ignored when when `useDat` has been set to `True`.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict[]`  
**return**: `dict['filled', 'bmp', 'x', 'y', 'w', 'h', 'flags']`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict[]`  
**return**: `dict['filled', 'bmp', 'x', 'y', 'w', 'h', 'flags', 'useDat', 'dat']`

**Parameters:**

- **filled** (*bool*) – `True` if the icon was set.
- **bmp** ([*c4d.bitmaps.BaseBitmap*](../modules/c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – Icon’s bitmap. Can be `None`.
- **x** (*int*) – X coordinate of the upper-left corner of the icon.
- **y** (*int*) – Y coordinate of the upper-left corner of the icon.
- **w** (*int*) – Width of the icon.
- **h** (*int*) – Height of the icon.
- **flags** (*int*) – See [ICONDATAFLAGS](ICONDATAFLAGS.md).
- **useDat** (*bool*) – Must be set to `True` when the `IconData` `dat` should be used.
- **dat** ([*c4d.IconData*](../modules/c4d/IconData/index.md#c4d.IconData)) – The icon data to use instead of the raw bitmap data.

## `c4d.MSG_GETCUSTOMICON_SETTINGS` <a id="c4d.MSG_GETCUSTOMICON_SETTINGS"></a> <a id="msg-getcustomicon-settings"></a>

Sent to retrieve the custom icon settings of an object.

*New in version R21.*

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `None`  
**return**: `dict['setting']`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['setting']`  
**return**: `None`

**Parameters:** **setting** ([*c4d.CustomIconSettings*](../modules/c4d/CustomIconSettings/index.md#c4d.CustomIconSettings)) – The [`c4d.CustomIconSettings`](../modules/c4d/CustomIconSettings/index.md#c4d.CustomIconSettings) for the atom.

## `c4d.MSG_GETREALCAMERADATA` <a id="c4d.MSG_GETREALCAMERADATA"></a> <a id="msg-getrealcameradata"></a>

Sent to get a real camera object from a generator.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict[]`  
**return**: `dict['res']`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict[]`  
**return**: `dict['res']`

**Parameters:** **res** ([*c4d.BaseObject*](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The real camera object.

## `c4d.MSG_GETREALTAGDATA` <a id="c4d.MSG_GETREALTAGDATA"></a> <a id="msg-getrealtagdata"></a>

Sent to get the real tag object from a virtual ‘generator’ tag.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict[]`  
**return**: `dict['res']`

**Parameters:** **res** ([*c4d.BaseTag*](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)) – The real tag.

## `c4d.MSG_MENUPREPARE` <a id="c4d.MSG_MENUPREPARE"></a> <a id="msg-menuprepare"></a>

Sent to allow tags, objects, shaders and other Cinema API nodes to do setup work when called from the menu.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `c4d.BaseContainer`  
**return**: `None`

## `c4d.MSG_MULTI_CLEARSUGGESTEDFOLDER` <a id="c4d.MSG_MULTI_CLEARSUGGESTEDFOLDER"></a> <a id="msg-multi-clearsuggestedfolder"></a>

Sent to nodes to convert absolute paths to filename.  
When “Save Project with Assets” is being invoked, all assets are moved to the new target directory. In this case all absolute paths must be converted to filenames because the files are next to the document and the absolute paths are not needed anymore.

> **Note:** Both `MSG_GETALLASSETS` and `MSG_MULTI_CLEARSUGGESTEDFOLDER` are important for “Save Project” to work and to collect all items. This messages must only be supported when also the message `MSG_GETALLASSETS` is being used to handle assets.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `None`  
**return**: `None`

## `c4d.MSG_MULTI_DOCUMENTCLONED` <a id="c4d.MSG_MULTI_DOCUMENTCLONED"></a> <a id="msg-multi-documentcloned"></a>

Sent when a document is being cloned.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `None`  
**return**: `None`

## `c4d.MSG_MULTI_RENDERNOTIFICATION` <a id="c4d.MSG_MULTI_RENDERNOTIFICATION"></a> <a id="msg-multi-rendernotification"></a>

Sent to a document and all of its elements before a render starts.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['doc', 'external', 'start', 'animated', 'flags']`  
**return**: `dict['external', 'start', 'animated']`

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../modules/c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to be rendered.

- **external** (*bool*) – `True` if the rendering is not in the editor view, otherwise `False`.

- **start** (*bool*) – Determines if this is a start (`True`) or stop (`False`) notification. Stop notifications are only sent if the document will not be deleted, which more or less only happens if there is an editor render.

- **animated** (*bool*) – Determines if this is an animation sequence being rendered.

- **flags** (*int*) –

  *New in version 2024.0.0.*

  A combination of the render flags. See [RENDERFLAGS](RENDERFLAGS.md).

## `c4d.MSG_POINTS_CHANGED` <a id="c4d.MSG_POINTS_CHANGED"></a> <a id="msg-points-changed"></a>

Sent to notify an object its points have changed.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict['old_cnt', 'new_cnt', 'vc_flags', 'map']`  
**return**: `None`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['old_cnt', 'new_cnt', 'vc_flags', 'map']`  
**return**: `None`

**Parameters:**

- **old_cnt** (*int*) – Number of elements before the change.
- **new_cnt** (*int*) – Number of elements after the change.
- **vc_flags** (*int*) – Flags. See [VC_FLAGS](VC_FLAGS.md).
- **map** (*list*[*int*]) – Optional translation map.

## `c4d.MSG_POLYGONS_CHANGED` <a id="c4d.MSG_POLYGONS_CHANGED"></a> <a id="msg-polygons-changed"></a>

Sent to notify an object its polygons have changed.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['old_cnt', 'new_cnt', 'vc_flags', 'map']`  
**return**: `None`

**Parameters:**

- **old_cnt** (*int*) – Number of elements before the change.
- **new_cnt** (*int*) – Number of elements after the change.
- **vc_flags** (*int*) – Flags. See [VC_FLAGS](VC_FLAGS.md).
- **map** (*list*[*int*]) – Optional translation map.

## `c4d.MSG_RETRIEVEPRIVATEDATA` <a id="c4d.MSG_RETRIEVEPRIVATEDATA"></a> <a id="msg-retrieveprivatedata"></a>

Sent to retrieve private data from an atom.

> **Note:** Used to obtain loader/saver settings.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict[]`  
**return**: `dict['imexporter']`

**Parameters:** **imexporter** ([*c4d.BaseList2D*](../modules/c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – Scene loader/saver.

## `c4d.MSG_SCALEDOCUMENT` <a id="c4d.MSG_SCALEDOCUMENT"></a> <a id="msg-scaledocument"></a>

Sent to signal that another document with different scale has been merged with the current document.

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['scale']`  
**return**: `None`

**Parameters:** **scale** (*float*) – The scale of the merged document.

## `c4d.MSG_SEGMENTS_CHANGED` <a id="c4d.MSG_SEGMENTS_CHANGED"></a> <a id="msg-segments-changed"></a>

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `dict['old_cnt', 'new_cnt', 'vc_flags', 'map']`  
**return**: `None`

**Parameters:**

- **old_cnt** (*int*) – Number of elements before the change.
- **new_cnt** (*int*) – Number of elements after the change.
- **vc_flags** (*int*) – Flags. See [VC_FLAGS](VC_FLAGS.md).
- **map** (*list*[*int*]) – Optional translation map.

## `c4d.MSG_SMALLUPDATE` <a id="c4d.MSG_SMALLUPDATE"></a> <a id="msg-smallupdate"></a>

Sent if part of an object has changed and does not need cache rebuilding.

> **Note:** This message should be used very carefully, it is there for small performance enhancements. For example, if a polygon selection has been changed, then the caches do not need to be rebuilt; `MSG_SMALLUPDATE` can be sent.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `None`  
**return**: `None`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `None`  
**return**: `None`

## `c4d.MSG_UPDATE` <a id="c4d.MSG_UPDATE"></a> <a id="msg-update"></a>

Must be sent when the bounding box has to be recalculated.  
Otherwise use [c4d.MSG_CHANGE](#msg-change).

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `None`  
**return**: `None`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
**data**: `None`  
**return**: `None`

## `maxon.neutron.MSG_GET_ASSET_WITH_VERSION` <a id="msg-get-asset-with-version"></a>

Sent to get the identifier of the node asset from which this capsule originates

**Broadcast to Atoms:**

Can be sent with `C4DAtom.Message()` with the message data `data`.  
**data**: `dict[]`  
**return**: `dict['id', 'version']`

**Parameters:**

- **id** (*str*) – The asset identifier of the asset used by the capsule.
- **version** (*str*) – The version of the asset used by the capsule.

## `c4d.MSG_GETCUSTOM_NAME_ADDITION` <a id="c4d.MSG_GETCUSTOM_NAME_ADDITION"></a> <a id="msg-getcustom-name-addition"></a>

Sent to retrieve a custom name addition.

**Broadcast to Atoms:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
**data**: `dict[]`  
**return**: `dict['res']`

**Handle in Plugins:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
The atoms needs to be registered with c4d.OBJECT_CUSTOM_NAME_ADDITION to have the additional name displayed in the Object Manager.  
**data**: `None`  
**return**: `dict['res']`

**Parameters:** **res** (*str*) – The additional string name to b displayed in the Object Manager.

## `c4d.MSG_CHECKINSIDEUNDO` <a id="c4d.MSG_CHECKINSIDEUNDO"></a> <a id="msg-checkinsideundo"></a>

Sent to check if the document is currently processing an undo.

*New in version 2026.0.0.*

**Broadcast to Atoms:**

**data**: None  
**return**: `bool`

## `c4d.MSG_MULTI_MARKMATERIALS` <a id="c4d.MSG_MULTI_MARKMATERIALS"></a> <a id="msg-multi-markmaterials"></a>

Sent to do different operations on materials used by a C4DAtom.

*New in version 2026.0.0.*

This message support 3 different modes:

1. data is None this is sent to atoms to let them set the BIT_MATMARK of the materials they use.
2. data is a Python dictionary with “omat” defined and “nmat” potentially defined to replace any usage of *omat* with *nmat* in the Atom.
3. data is an empty Python dictionary therefor a list of all used materials will be returned.

**Broadcast to Atoms Option 1:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
Let the Atom set the BIT_MATMARK of the materials it use.  
**data**: None  
**return**: `bool`

**Broadcast to Atoms Option 2:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
Replace any usage of *omat* with *nmat* in the Atom.  
**data**: `dict['omat', 'nmat']`  
**return**: `bool`

**param omat:** Original material.

**param Optional[c4d.BaseMaterial] nmat:** New material

**Broadcast to Atoms Option 3:**

Can be sent with [`C4DAtom.Message()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.Message) with the message data `data`.  
Returns all materials used by an Atom.  
**data**: `dict[]`  
**return**: `list[c4d.BaseMaterial]`

**Handle in Plugins Option 1:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
Should define the BIT_MATMARK of the materials the current Atom plugin use.  
**data**: `None`  
**return**: `bool`

**Handle in Plugins Option 2:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
Should replace any usage of *omat* with *nmat* in the current Atom plugin.  
**data**: `dict['omat', 'nmat']`  
**return**: `bool`

**param c4d.BaseMaterial omat:** Original material.

**param Optional[c4d.BaseMaterial] nmat:** New material

**Broadcast to Plugins Option 3:**

Can be received as plugin messages with the message data argument `data` or `t_data`, depending on the plugin interface `Message()` implementation:  
Should return all materials used by the current Atom plugin.  
**data**: `dict[]`  
**return**: `list[c4d.BaseMaterial]`
