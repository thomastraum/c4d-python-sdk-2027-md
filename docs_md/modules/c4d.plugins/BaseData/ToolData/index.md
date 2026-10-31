<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseData/ToolData/index.html -->

# c4d.plugins.ToolData <a id="c4d-plugins-tooldata"></a>

## *class* `c4d.plugins.ToolData` <a id="c4d.plugins.ToolData"></a>

A data class for creating tool plugins. Use [`RegisterToolPlugin()`](../../index.md#c4d.plugins.RegisterToolPlugin) to register the tool plugin.

Parent Class:

- [`c4d.plugins.BaseData`](../index.md#c4d.plugins.BaseData)

## Overview <a id="overview"></a>

**Editor Interaction**

- [`ToolData.Draw()`](#c4d.plugins.ToolData.Draw): Called when the editor view is updated so you can display graphics for your tool in the view.
- [`ToolData.GetCursorInfo()`](#c4d.plugins.ToolData.GetCursorInfo): Called when the cursor is over editor window to get the state of the mouse pointer.
- [`ToolData.KeyboardInput()`](#c4d.plugins.ToolData.KeyboardInput): Override - Called when the user types something in any of the editors views.
- [`ToolData.MouseInput()`](#c4d.plugins.ToolData.MouseInput): Override - Called when the user clicks with the mouse in any of the editors views.

**Interface Configuration**

- [`ToolData.AllocSubDialog()`](#c4d.plugins.ToolData.AllocSubDialog): Called to get a GUI for the Active Tool window.
- [`ToolData.GetDDescription()`](#c4d.plugins.ToolData.GetDDescription): Called to add parameters to the description for the tool.
- [`ToolData.GetDEnabling()`](#c4d.plugins.ToolData.GetDEnabling): Called to let decide which parameters should be enabled or disabled (ghosted).
- [`ToolData.GetDParameter()`](#c4d.plugins.ToolData.GetDParameter): Called to override the reading of description parameters.
- [`ToolData.SetDParameter()`](#c4d.plugins.ToolData.SetDParameter): Called to override the writing of parameters.
- [`ToolData.TranslateDescID()`](#c4d.plugins.ToolData.TranslateDescID): Called by the Attribute Manager for every tool and every description ID.

**Tool Lifecycle**

- [`ToolData.FreeTool()`](#c4d.plugins.ToolData.FreeTool): Override - Called each time the user chooses another tool.
- [`ToolData.GetState()`](#c4d.plugins.ToolData.GetState): Called to check if the tool should be enabled, checked or not.
- [`ToolData.InitDefaultSettings()`](#c4d.plugins.ToolData.InitDefaultSettings): Called to let you initialize the default tool settings in *data*.
- [`ToolData.InitTool()`](#c4d.plugins.ToolData.InitTool): Override - Called each time the tool is selected.
- [`ToolData.Message()`](#c4d.plugins.ToolData.Message): Called when the tool receives messages.

## Members <a id="members"></a>

### Editor Interaction <a id="c4d.plugins.ToolData-method-Editor-Interaction"></a>

#### `ToolData.Draw(self, doc, data, bd, bh, bt, flags)` <a id="c4d.plugins.ToolData.Draw"></a>

Called when the editor view is updated so you can display graphics for your tool in the view.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document.

- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.

- **bd** ([*c4d.BaseDraw*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The [`BaseDraw`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw) object for the active editor view.

- **bh** ([*c4d.plugins.BaseDrawHelp*](../../BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp)) – The helper for the editor’s view. The caller owns the pointed base draw helper.

- **flags** (*int*) –

  The flags are:

  |   |   |
  |---|---|
  | *TOOLDRAWFLAGS_NONE* | None. |
  | *TOOLDRAWFLAGS_INVERSE_Z* | Inverse Z-buffer mode. If set, the drawing engine of Cinema 4D will only draw elements if they are further away from the camera than other objects.  <br>This is mostly used for help lines (such as the semi-transparent axis inside of objects).<br>> **Note:** This mode only works when all objects are drawn so it should be passed last. |
  | *TOOLDRAWFLAGS_HIGHLIGHT* | Highlight mode. |

- **bt** ([*c4d.threading.BaseThread*](../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)) – The calling thread.

**Return type:** int

**Returns:**

The values for this are:

|   |   |
|---|---|
| *TOOLDRAW_NONE* | None. |
| *TOOLDRAW_HANDLES* | The active objects handles will be drawn. |
| *TOOLDRAW_AXIS* | The active objects axes will be drawn. |
| *TOOLDRAW_HIGHLIGHTS* | The highlights will be drawn. |

#### `ToolData.GetCursorInfo(self, doc, data, bd, x, y, bc)` <a id="c4d.plugins.ToolData.GetCursorInfo"></a>

Called when the cursor is over editor window to get the state of the mouse pointer.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The currently active document.

- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.

- **bd** ([*c4d.BaseDraw*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The [`BaseDraw`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw) object for the active editor view.

- **x** (*float*) – The x coordinate of the mouse cursor relative to the top-left of the currently active editor view.

- **y** (*float*) – The y coordinate of the mouse cursor relative to the top-left of the currently active editor view.

- **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) –

  The container to store the result in. Use the following container IDs:

  |   |   |   |
  |---|---|---|
  | *RESULT_BUBBLEHELP_TITLE* | str | Bubble help text title. Printed in bold for the bubble help, not visible in the status bar. |
  | *RESULT_BUBBLEHELP* | str | Bubble text help. |
  | *RESULT_CURSOR* | int | Mouse cursor: [MOUSE](../../../../consts/MOUSE.md). |

**Return type:** bool

**Returns:** **False** if a problem occured during this function.

#### `ToolData.KeyboardInput(self, doc, data, bd, win, msg)` <a id="c4d.plugins.ToolData.KeyboardInput"></a>

Override - Called when the user types something in any of the editors views.

> **Note:** Make sure that you only use this function when the user is somehow working with your plugin, so that other plugins can also use this hook when it is their turn.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The currently active document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.
- **bd** ([*c4d.BaseDraw*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The [`BaseDraw`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw) object for the active editor view.
- **win** ([*c4d.gui.EditorWindow*](../../../c4d.gui/EditorWindow/index.md#c4d.gui.EditorWindow)) – The [`EditorWindow`](../../../c4d.gui/EditorWindow/index.md#c4d.gui.EditorWindow) object for the active editor view.
- **msg** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The original message container.

**Return type:** bool

**Returns:** **False** if a problem occured during this function.

#### `ToolData.MouseInput(self, doc, data, bd, win, msg)` <a id="c4d.plugins.ToolData.MouseInput"></a>

Override - Called when the user clicks with the mouse in any of the editors views.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The currently active document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.
- **bd** ([*c4d.BaseDraw*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The [`BaseDraw`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw) object for the active editor view.
- **win** ([*c4d.gui.EditorWindow*](../../../c4d.gui/EditorWindow/index.md#c4d.gui.EditorWindow)) – The [`EditorWindow`](../../../c4d.gui/EditorWindow/index.md#c4d.gui.EditorWindow) object for the active editor view.
- **msg** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The original message container.

**Return type:** bool

**Returns:** **False** if a problem occured during this function.

### Interface Configuration <a id="c4d.plugins.ToolData-method-Interface-Configuration"></a>

#### `ToolData.AllocSubDialog(self, bc)` <a id="c4d.plugins.ToolData.AllocSubDialog"></a>

Called to get a GUI for the Active Tool window. Return an instance of your tool’s dialog.

**Parameters:** **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Currently not used.

**Return type:** [c4d.gui.SubDialog](../../../c4d.gui/GeDialog/SubDialog/index.md#c4d.gui.SubDialog)

**Returns:** The allocated sub dialog.

#### `ToolData.GetDDescription(self, doc, data, description, flags)` <a id="c4d.plugins.ToolData.GetDDescription"></a>

Called to add parameters to the description for the tool. Modify the passed description as needed and return the appropriate flags.

*New in version R18.011.*

> **Note:** If only a description resource is used it is not needed to overload `GetDDescription()`.

> **See also:**
>
> `NodeData.GetDDescription()`

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document.

- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.

- **description** ([*c4d.Description*](../../../c4d/Description/index.md#c4d.Description)) – The description to add the parameters to.

- **flags** (*int*) –

  The flags for the description operation:

  |   |   |
  |---|---|
  | *DESCFLAGS_DESC_NONE* | None. |
  | *DESCFLAGS_DESC_RESOLVEMULTIPLEDATA* | Private and unused. |
  | *DESCFLAGS_DESC_LOADED* | Set if elements have been added to the description, either by loading or manual addition. |
  | *DESCFLAGS_DESC_RECURSIONLOCK* | Private. |
  | *DESCFLAGS_DESC_DONTLOADDEFAULT* | If set, the object description will also contain the tag’s descriptions (as sub-containers). |
  | *DESCFLAGS_DESC_MAPTAGS* | If specified, the object description will also contain the tag’s descriptions (as sub-containers). |
  | *DESCFLAGS_DESC_NEEDDEFAULTVALUE* | Set if *“Reset to Default”* was called by the user. |

**Return type:** Union[bool, Tuple[bool, int]]

**Returns:**

One of these options:

bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.  
Tuple[bool, int]: The status (**True** if successful, otherwise **False**) and description flags (*DESCFLAGS_DESC*].

#### `ToolData.GetDEnabling(self, doc, data, id, t_data, flags, itemdesc)` <a id="c4d.plugins.ToolData.GetDEnabling"></a>

Called to let decide which parameters should be enabled or disabled (ghosted).  
This can be used both for parameters that are stored in the tool’s container and for custom parameters.  
Just read the passed *t_data* if the right *id* was provided, and return **True** to enable the parameter or **False** to disable it depending on the value.  
And if the passed *id* element is not processed, include a call to the base class method as last return.

```python
return ToolData.GetDEnabling(self, doc, data, id, t_data, flags, itemdesc)
```

*New in version R18.011.*

> **See also:**
>
> `NodeData.GetDEnabling()`

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.
- **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The ID of the parameter.
- **t_data** (*any*) – The current data for the parameter.
- **flags** (*int*) – Not used.
- **itemdesc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The description, encoded to a container as described in [`c4d.Description`](../../../c4d/Description/index.md#c4d.Description).

**Return type:** bool

**Returns:**

**True** if the parameter should be enabled, otherwise **False**.

> **Note:** It is recommended to include a call to the base class method as last return.

#### `ToolData.GetDParameter(self, doc, data, id, flags)` <a id="c4d.plugins.ToolData.GetDParameter"></a>

Called to override the reading of description parameters. Necessary for parameters that are not simply stored in the tool’s container e.g. class members.  
Return the parameter data and the appropriate flags if the right *id* is provided.

*New in version R18.011.*

> **Note:** If only a description resource is used it is not needed to overload `GetDParameter()`.

> **See also:**
>
> `NodeData.GetDParameter()`

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document.

- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.

- **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The ID of the parameter.

- **flags** (*int*) –

  The flags for the description operation:

  |   |   |
  |---|---|
  | *DESCFLAGS_GET_NONE* | None. |
  | *DESCFLAGS_GET_PARAM_GET* | Parameter retrieved. |
  | *DESCFLAGS_GET_NO_GEDATADEFAULTVALUE* | If set, the C++ *GeData* default type will not be initialized for `C4DAtom.GetParameter()`. |
  | *DESCFLAGS_GET_NO_GLOBALDATA* | Private. |

**Return type:** Union[bool, Tuple[bool, any, int]]

**Returns:**

One of these options:

bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.  
Tuple[bool, object, int]: The status (**True** if successful, otherwise **False**), parameter data and description flags (*DESCFLAGS_DESC*].

#### `ToolData.SetDParameter(self, doc, data, id, t_data, flags)` <a id="c4d.plugins.ToolData.SetDParameter"></a>

Called to override the writing of parameters. Read the passed *t_data* if the right *id* is provided, store the data and return the appropriate flags.

*New in version R18.011.*

> **Note:** If only a description resource is used it is not needed to overload `SetDParameter()`.

> **See also:**
>
> `NodeData.SetDParameter()`

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document.

- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.

- **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The ID of the parameter.

- **t_data** (*any*) – The parameter data to set.

- **flags** (*int*) –

  The flags for the description operation:

  |   |   |
  |---|---|
  | *DESCFLAGS_SET_NONE* | None. |
  | *DESCFLAGS_SET_PARAM_SET* | Parameter set. |
  | *DESCFLAGS_SET_USERINTERACTION* | Set when the GUI is calling `SetParameter()`. This is the only time when `SetParameter()` is allowed to use user interaction elements (e.g. open dialogs, display messages etc.). |
  | *DESCFLAGS_SET_DONTCHECKMINMAX* | No check is internally done if the parameter passed is within the [min/max] range of the description, to save some time. |
  | *DESCFLAGS_SET_DONTAFFECTINHERITANCE* | No parameter inheritance, for render settings and post effects only. |
  | *DESCFLAGS_SET_FORCESET* | Forces the set value without `GetParameter()`/Compare. Use only for calls where for sure the value was changed! |
  | *DESCFLAGS_SET_DONTFREESPLINECACHE* | **Private.** *New in version R16.038.* |
  | *DESCFLAGS_SET_INDRAG* | **Gadget (e.g. Slider) in dragging mode (not finished). Only used when *DESCFLAGS_SET_USERINTERACTION* is set.** *New in version R17.053.* |

**Return type:** Union[bool, Tuple[bool, int]]

**Returns:**

One of these options:

bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.  
Tuple[bool, int]: The status (**True** if successful, otherwise **False**) and description flags (*DESCFLAGS_DESC*].

#### `ToolData.TranslateDescID(self, doc, data, id)` <a id="c4d.plugins.ToolData.TranslateDescID"></a>

Called by the Attribute Manager for every tool and every description ID.  
Gives the opportunity to route a description ID in the description of a tool to another one.

*New in version R18.011.*

> **See also:**
>
> `NodeData.TranslateDescID()`

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.
- **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The source description ID.

**Return type:** Union[bool, Tuple[bool, [c4d.DescID](../../../c4d/DescID/index.md#c4d.DescID), [c4d.C4DAtom](../../../c4d/C4DAtom/index.md#c4d.C4DAtom)]]

**Returns:**

One of these options:

bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.  
Tuple[bool, c4d.DescID, :c4d.C4DAtom): The status (**True** if successful, otherwise **False**], target description ID and tool.

### Tool Lifecycle <a id="c4d.plugins.ToolData-method-Tool-Lifecycle"></a>

#### `ToolData.FreeTool(self, doc, data)` <a id="c4d.plugins.ToolData.FreeTool"></a>

Override - Called each time the user chooses another tool.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The original tool settings container.

#### `ToolData.GetState(self, doc)` <a id="c4d.plugins.ToolData.GetState"></a>

Called to check if the tool should be enabled, checked or not.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document the tool is being used in.

**Return type:** int

**Returns:**

The return flags:

| Symbol ID | Description |
|---|---|
| CMD_ENABLED | Enabled. |
| CMD_VALUE | Checked. |
| CMD_HIDDEN | Hidden. |

#### `ToolData.InitDefaultSettings(self, doc, data)` <a id="c4d.plugins.ToolData.InitDefaultSettings"></a>

Called to let you initialize the default tool settings in *data*.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The currently active document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.

#### `ToolData.InitTool(self, doc, data, bt)` <a id="c4d.plugins.ToolData.InitTool"></a>

Override - Called each time the tool is selected.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The original tool settings container.
- **bt** ([*c4d.threading.BaseThread*](../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)) – The calling thread.

**Return type:** bool

**Returns:** **True** if there was no error, otherwise **False**.

#### `ToolData.Message(self, doc, data, type, t_data)` <a id="c4d.plugins.ToolData.Message"></a>

Called when the tool receives messages.

> **See also:** [C4DAtom and Plugin Messages](../../../../consts/MSG_C4DATOM_PLUGINS.md) for information on the messages type, data and input/output.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The current document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The current tool data.
- **type** (*int*) – The message type.
- **t_data** (*any*) – Depends on *type*.

**Return type:** bool

**Returns:** Depends on the message *type*.
