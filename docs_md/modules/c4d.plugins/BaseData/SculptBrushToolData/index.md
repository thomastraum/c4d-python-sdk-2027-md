<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseData/SculptBrushToolData/index.html -->

# c4d.plugins.SculptBrushToolData <a id="c4d-plugins-sculptbrushtooldata"></a>

## *class* `c4d.plugins.SculptBrushToolData` <a id="c4d.plugins.SculptBrushToolData"></a>

A data class for creating sculpt brushes.

*New in version R16.021.*

Parent Class:

- [`c4d.plugins.BaseData`](../index.md#c4d.plugins.BaseData)

## Overview <a id="overview"></a>

**Dab Processing**

- [`SculptBrushToolData.ApplyDab()`](#c4d.plugins.SculptBrushToolData.ApplyDab): Called to modify the sculpt object.
- [`SculptBrushToolData.EndDab()`](#c4d.plugins.SculptBrushToolData.EndDab): Called after `ApplyDab()` function.
- [`SculptBrushToolData.StartDab()`](#c4d.plugins.SculptBrushToolData.StartDab): Called before the `ApplyDab()` override is called which will then process the dab.

**Input Handling**

- [`SculptBrushToolData.GetCursorInfo()`](#c4d.plugins.SculptBrushToolData.GetCursorInfo): Called when the cursor is over the editor window to get the state of the mouse pointer.
- [`SculptBrushToolData.HandleFillTool()`](#c4d.plugins.SculptBrushToolData.HandleFillTool): Private.
- [`SculptBrushToolData.HandleNonModelPickMode()`](#c4d.plugins.SculptBrushToolData.HandleNonModelPickMode): Private.
- [`SculptBrushToolData.KeyboardInput()`](#c4d.plugins.SculptBrushToolData.KeyboardInput): Called when the user types something in any of the editor views.
- [`SculptBrushToolData.MouseData()`](#c4d.plugins.SculptBrushToolData.MouseData): Constantly receives data about the object underneath the mouse.
- [`SculptBrushToolData.MouseInput()`](#c4d.plugins.SculptBrushToolData.MouseInput): Called when the user clicks with the mouse in any of the editor views.

**Plugin Metadata**

- [`SculptBrushToolData.GetResourceSymbol()`](#c4d.plugins.SculptBrushToolData.GetResourceSymbol): Return the name of the resource file for this brush.
- [`SculptBrushToolData.GetToolPluginId()`](#c4d.plugins.SculptBrushToolData.GetToolPluginId): Return the unique id for the tool plugin as obtained from www.plugincafe.com.

**Settings Management**

- [`SculptBrushToolData.AllocSubDialog()`](#c4d.plugins.SculptBrushToolData.AllocSubDialog): Called to get a GUI for the Active Tool window.
- [`SculptBrushToolData.GetEnabling()`](#c4d.plugins.SculptBrushToolData.GetEnabling): Called internally by the sculpting system to check if an UI element is enabled or not.
- [`SculptBrushToolData.InitDefaultSettings()`](#c4d.plugins.SculptBrushToolData.InitDefaultSettings): Called to let initialize the default tool settings in *data*.
- [`SculptBrushToolData.OverwriteLoadedPresetSettings()`](#c4d.plugins.SculptBrushToolData.OverwriteLoadedPresetSettings): After a preset has been loaded this method will get called to allow the brush to disable or change any of the loaded settings if required.
- [`SculptBrushToolData.PostInitDefaultSettings()`](#c4d.plugins.SculptBrushToolData.PostInitDefaultSettings): When a brush is reset by the user, in the UI, then it sets it back to its defaults.

**Stroke Lifecycle**

- [`SculptBrushToolData.EndStroke()`](#c4d.plugins.SculptBrushToolData.EndStroke): Called on mouse up after `EndStrokeInstance()` has been called for each instance.
- [`SculptBrushToolData.EndStrokeInstance()`](#c4d.plugins.SculptBrushToolData.EndStrokeInstance): Called on mouse up after a brush stroke.
- [`SculptBrushToolData.EndStrokeInstanceDabs()`](#c4d.plugins.SculptBrushToolData.EndStrokeInstanceDabs): Called after all the dabs have been drawn for a single instance of the brush.
- [`SculptBrushToolData.EndSymmetry()`](#c4d.plugins.SculptBrushToolData.EndSymmetry): Called after all the dabs for all the instances have been drawn for a single mouse movement on screen.
- [`SculptBrushToolData.StartStroke()`](#c4d.plugins.SculptBrushToolData.StartStroke): The number of instances will change depending on the symmetry mirroring and radial settings.
- [`SculptBrushToolData.StartStrokeInstance()`](#c4d.plugins.SculptBrushToolData.StartStrokeInstance): Called after `StartStroke()`. Called once for each brush instance at the start of a stroke.
- [`SculptBrushToolData.StartStrokeInstanceDabs()`](#c4d.plugins.SculptBrushToolData.StartStrokeInstanceDabs): Called before all the dabs for a single instance are about to be drawn.
- [`SculptBrushToolData.StartSymmetry()`](#c4d.plugins.SculptBrushToolData.StartSymmetry): Called directly before each individual brush instance is about to be handled.

**Tool Operations**

- [`SculptBrushToolData.DoCommand()`](#c4d.plugins.SculptBrushToolData.DoCommand): Called by [`SendModelingCommand()`](../../../c4d.utils/index.md#c4d.utils.SendModelingCommand) to perform a command.
- [`SculptBrushToolData.FreeTool()`](#c4d.plugins.SculptBrushToolData.FreeTool): Called each time the user chooses another tool.
- [`SculptBrushToolData.GetState()`](#c4d.plugins.SculptBrushToolData.GetState): Called to check if the tool should be enabled, checked or not.
- [`SculptBrushToolData.InitTool()`](#c4d.plugins.SculptBrushToolData.InitTool): Called each time the tool is selected.
- [`SculptBrushToolData.Message()`](#c4d.plugins.SculptBrushToolData.Message): Called when the tool receives messages.

**View Rendering**

- [`SculptBrushToolData.Draw()`](#c4d.plugins.SculptBrushToolData.Draw): Called when the editor view is updated so you can display graphics for your tool in the view.
- [`SculptBrushToolData.DrawNonModelPickMode()`](#c4d.plugins.SculptBrushToolData.DrawNonModelPickMode): Private.
- [`SculptBrushToolData.HasDrawMode()`](#c4d.plugins.SculptBrushToolData.HasDrawMode): Override to let the system know what draw modes the brush supports.

## Members <a id="members"></a>

### Dab Processing <a id="c4d.plugins.SculptBrushToolData-method-Dab-Processing"></a>

#### `SculptBrushToolData.ApplyDab(self, dab)` <a id="c4d.plugins.SculptBrushToolData.ApplyDab"></a>

Called to modify the sculpt object. Implement the functionality of your brush here!

**Parameters:** **dab** ([*c4d.modules.sculpting.BrushDabData*](../../../c4d.modules/sculpting/BrushDabData/index.md#c4d.modules.sculpting.BrushDabData)) – The brush dab data.

#### `SculptBrushToolData.EndDab(self, strokeInstanceID)` <a id="c4d.plugins.SculptBrushToolData.EndDab"></a>

Called after [`ApplyDab()`](#c4d.plugins.SculptBrushToolData.ApplyDab) function.

> **Note:** **EndDab()** will only be called if `SculptBrushParams.EnableBrushAccess()` has been set to **True**.

**Parameters:** **strokeInstanceID** (*int*) – The ID of the brush instance being drawn.

#### `SculptBrushToolData.StartDab(self, strokeInstanceID)` <a id="c4d.plugins.SculptBrushToolData.StartDab"></a>

Called before the [`ApplyDab()`](#c4d.plugins.SculptBrushToolData.ApplyDab) override is called which will then process the dab.  
Use this method to setup any data on your brush that you might want to access from within your [`ApplyDab()`](#c4d.plugins.SculptBrushToolData.ApplyDab) override via `BrushDabData.GetBrush()`.

> **Note:** **StartDab()** will only be called if `SculptBrushParams.EnableBrushAccess()` has been set to **True**.

**Parameters:** **strokeInstanceID** (*int*) – The ID of the brush instance being drawn.

### Input Handling <a id="c4d.plugins.SculptBrushToolData-method-Input-Handling"></a>

#### `SculptBrushToolData.GetCursorInfo(self, doc, data, bd, x, y, bc)` <a id="c4d.plugins.SculptBrushToolData.GetCursorInfo"></a>

Called when the cursor is over the editor window to get the state of the mouse pointer.

The bubble help and cursor can be set using.

```python
bc.SetString(c4d.RESULT_BUBBLEHELP, "My Tools Help")
bc.SetLong(c4d.RESULT_CURSOR, c4d.MOUSE_POINT_HAND)
```

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

**Returns:** **False** if a problem occured.

#### `SculptBrushToolData.HandleFillTool(self, doc, data, bd, win, msg)` <a id="c4d.plugins.SculptBrushToolData.HandleFillTool"></a>

Private.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The current document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The brush data.
- **bd** ([*c4d.BaseDraw*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The editor view the tool is being used in.
- **win** ([*c4d.gui.EditorWindow*](../../../c4d.gui/EditorWindow/index.md#c4d.gui.EditorWindow)) – The editor window the tool is being used in.
- **msg** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The mouse/tablet message data.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SculptBrushToolData.HandleNonModelPickMode(self, doc, data, bd, win, msg)` <a id="c4d.plugins.SculptBrushToolData.HandleNonModelPickMode"></a>

Private. Do something special when the first mouse click is not on the model.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The current document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The brush data.
- **bd** ([*c4d.BaseDraw*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The editor view the tool is being used in.
- **win** ([*c4d.gui.EditorWindow*](../../../c4d.gui/EditorWindow/index.md#c4d.gui.EditorWindow)) – The editor window the tool is being used in.
- **msg** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The mouse/tablet message data.

**Return type:** bool

**Returns:** **True** if handled, otherwise **False**. In the case where you wish to only handle the mouse click and not the mouse drag it can return **False**.

#### `SculptBrushToolData.KeyboardInput(self, doc, data, bd, win, msg)` <a id="c4d.plugins.SculptBrushToolData.KeyboardInput"></a>

Called when the user types something in any of the editor views.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The currently active document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.
- **bd** ([*c4d.BaseDraw*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The [`BaseDraw`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw) object for the active editor view.
- **win** ([*c4d.gui.EditorWindow*](../../../c4d.gui/EditorWindow/index.md#c4d.gui.EditorWindow)) – The [`EditorWindow`](../../../c4d.gui/EditorWindow/index.md#c4d.gui.EditorWindow) object for the active editor view.
- **msg** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The original message container.

**Return type:** bool

**Returns:** **False** if a problem occured.

#### `SculptBrushToolData.MouseData(self, strokeInstanceID, brushData, md)` <a id="c4d.plugins.SculptBrushToolData.MouseData"></a>

Constantly receives data about the object underneath the mouse. This method will get called when you move the cursor over an object on screen and happens when the mouse button is up or down.

*New in version R17.048.*

> **Note:** **MouseData()** will only be called if `SculptBrushParams.EnableMouseData()` has been set to **True**.

**Parameters:**

- **strokeInstanceID** (*int*) – The ID of the brush instance being drawn.

- **brushData** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The BaseContainer data for the brush.

- **md** (*dict*) –

  The mouse data information for the current position of the mouse on the surface of the object:

  - ”pObject”: [`SculptObject`](../../../c4d.modules/sculpting/SculptObject/index.md#c4d.modules.sculpting.SculptObject) The selected Object underneath the mouse.
  - ”mouseCoord”: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) The screen coordinates for the mouse location in the current viewport.
  - ”hitPoint”: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) The hitpoint on the surface of the model at the center of the brush dab.
  - ”normal”: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) The normal on the surface of the model at the center of the brush dab.
  - ”barryCoord”: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) The barycentric coordinates within the triangle for the hit polygon.
  - ”polygon”: int The Index of the hit polygon.
  - ”mouseDrag”: **True** if the mouse button is held down and being dragged in the viewport.
  - ”distance”: The distance from the mouse in local space to the surface of the object.
  - ”isBackface”: **True** if the polygon under the mouse is backfacing.

#### `SculptBrushToolData.MouseInput(self, doc, data, bd, win, msg)` <a id="c4d.plugins.SculptBrushToolData.MouseInput"></a>

Called when the user clicks with the mouse in any of the editor views.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The currently active document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.
- **bd** ([*c4d.BaseDraw*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The [`BaseDraw`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw) object for the active editor view.
- **win** ([*c4d.gui.EditorWindow*](../../../c4d.gui/EditorWindow/index.md#c4d.gui.EditorWindow)) – The [`EditorWindow`](../../../c4d.gui/EditorWindow/index.md#c4d.gui.EditorWindow) object for the active editor view.
- **msg** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The original message container.

**Return type:** bool

**Returns:** **False** if a problem occured.

### Plugin Metadata <a id="c4d.plugins.SculptBrushToolData-method-Plugin-Metadata"></a>

#### `SculptBrushToolData.GetResourceSymbol(self)` <a id="c4d.plugins.SculptBrushToolData.GetResourceSymbol"></a>

Return the name of the resource file for this brush.

**Return type:** str

**Returns:** The name of the resource file for this brush.

#### `SculptBrushToolData.GetToolPluginId(self)` <a id="c4d.plugins.SculptBrushToolData.GetToolPluginId"></a>

Return the unique id for the tool plugin as obtained from www.plugincafe.com.

**Return type:** int

**Returns:** The tool plugin ID.

### Settings Management <a id="c4d.plugins.SculptBrushToolData-method-Settings-Management"></a>

#### `SculptBrushToolData.AllocSubDialog(self, bc)` <a id="c4d.plugins.SculptBrushToolData.AllocSubDialog"></a>

Called to get a GUI for the Active Tool window. Return an instance of your tool’s dialog.

**Parameters:** **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Currently not used.

**Return type:** [c4d.gui.SubDialog](../../../c4d.gui/GeDialog/SubDialog/index.md#c4d.gui.SubDialog)

**Returns:** The allocated subdialog.

#### `SculptBrushToolData.GetEnabling(self, id)` <a id="c4d.plugins.SculptBrushToolData.GetEnabling"></a>

Called internally by the sculpting system to check if an UI element is enabled or not.

If this method is overridden then make sure to also check the return value of this method directly by calling *SculptBrushToolData.GetEnabling(id)* at the end.

**Parameters:** **id** (*int*) – The id of the UI element from the *.res* file.

**Return type:** bool

**Returns:** **True** if the element should be enabled, otherwise **False**.

#### `SculptBrushToolData.InitDefaultSettings(self, doc, data)` <a id="c4d.plugins.SculptBrushToolData.InitDefaultSettings"></a>

Called to let initialize the default tool settings in *data*.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The currently active document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.

#### `SculptBrushToolData.OverwriteLoadedPresetSettings(self, data)` <a id="c4d.plugins.SculptBrushToolData.OverwriteLoadedPresetSettings"></a>

After a preset has been loaded this method will get called to allow the brush to disable or change any of the loaded settings if required.

**Parameters:** **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The settings for the loaded brush.

#### `SculptBrushToolData.PostInitDefaultSettings(self, doc, data)` <a id="c4d.plugins.SculptBrushToolData.PostInitDefaultSettings"></a>

When a brush is reset by the user, in the UI, then it sets it back to its defaults.  
Afterwards this method is called so you can overwrite any of the standard brush settings with your own for this brush.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The current document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The settings for the loaded brush.

### Stroke Lifecycle <a id="c4d.plugins.SculptBrushToolData-method-Stroke-Lifecycle"></a>

#### `SculptBrushToolData.EndStroke(self)` <a id="c4d.plugins.SculptBrushToolData.EndStroke"></a>

Called on mouse up after [`EndStrokeInstance()`](#c4d.plugins.SculptBrushToolData.EndStrokeInstance) has been called for each instance.

> **Note:** **EndStroke()** will only be called if `SculptBrushParams.EnableBrushAccess()` has been set to **True**.

#### `SculptBrushToolData.EndStrokeInstance(self, strokeInstanceID)` <a id="c4d.plugins.SculptBrushToolData.EndStrokeInstance"></a>

Called on mouse up after a brush stroke. This method is called once for each instance.  
Use this method to delete any temporary data you may have allocated in your [`StartStrokeInstance()`](#c4d.plugins.SculptBrushToolData.StartStrokeInstance) override.

> **Note:** **EndStrokeInstance()** will only be called if `SculptBrushParams.EnableBrushAccess()` has been set to **True**.

**Parameters:** **strokeInstanceID** (*int*) – The ID of the brush instance being drawn.

#### `SculptBrushToolData.EndStrokeInstanceDabs(self, strokeInstanceID)` <a id="c4d.plugins.SculptBrushToolData.EndStrokeInstanceDabs"></a>

Called after all the dabs have been drawn for a single instance of the brush.

> **Note:** **EndStrokeInstanceDabs()** will only be called if `SculptBrushParams.EnableBrushAccess()` has been set to **True**.

**Parameters:** **strokeInstanceID** (*int*) – The ID of the brush instance being drawn.

#### `SculptBrushToolData.EndSymmetry(self)` <a id="c4d.plugins.SculptBrushToolData.EndSymmetry"></a>

Called after all the dabs for all the instances have been drawn for a single mouse movement on screen.

> **Note:** **EndSymmetry()** will only be called if `SculptBrushParams.EnableBrushAccess()` has been set to **True**.

#### `SculptBrushToolData.StartStroke(self, strokeCount, data)` <a id="c4d.plugins.SculptBrushToolData.StartStroke"></a>

[`StartStroke()`](#c4d.plugins.SculptBrushToolData.StartStroke) is called once at the start of the stroke. It passes the total number of instances of the brush that will be drawn.  
The number of instances will change depending on the symmetry mirroring and radial settings.  
Use this method to setup any data on your brush that you might want to access from within your [`ApplyDab()`](#c4d.plugins.SculptBrushToolData.ApplyDab) override via `BrushDabData.GetBrush()`.  
Calling order for brush stroke methods:

- [`StartStroke()`](#c4d.plugins.SculptBrushToolData.StartStroke): Called once at the start of the stroke.
- [`StartStrokeInstance()`](#c4d.plugins.SculptBrushToolData.StartStrokeInstance): Call for each instance of a stroke that will be used. Use this to initialize any data you might need for the duration of the entire brush stroke.
- [`StartSymmetry()`](#c4d.plugins.SculptBrushToolData.StartSymmetry): Called once before all the instances are about to be drawn for a small mouse movement. This will be called MANY times during a stroke as the mouse moves over the model.
- [`StartStrokeInstanceDabs()`](#c4d.plugins.SculptBrushToolData.StartStrokeInstanceDabs): Called once before a bunch of consecutive dabs will be draw for a single instance (mirrored brush).
- [`StartDab()`](#c4d.plugins.SculptBrushToolData.StartDab): Called for each dab that needs to be drawn between 2 mouse locations on the object for a single brush stroke instance.
- [`ApplyDab()`](#c4d.plugins.SculptBrushToolData.ApplyDab) gets called to process the dab.
- [`EndDab()`](#c4d.plugins.SculptBrushToolData.EndDab)
- [`EndStrokeInstanceDabs()`](#c4d.plugins.SculptBrushToolData.EndStrokeInstanceDabs)
- [`EndSymmetry()`](#c4d.plugins.SculptBrushToolData.EndSymmetry): Called once when all symmetrical strokes have finished.
- [`EndStrokeInstance()`](#c4d.plugins.SculptBrushToolData.EndStrokeInstance): Called for each instance of a stroke that was used.
- [`EndStroke()`](#c4d.plugins.SculptBrushToolData.EndStroke)

> **Note:** **StartStroke()** will only be called if `SculptBrushParams.EnableBrushAccess()` has been set to **True**.

**Parameters:**

- **strokeCount** (*int*) – The number of instances of the brush that will be drawn.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The data for the brush.

#### `SculptBrushToolData.StartStrokeInstance(self, strokeInstanceID)` <a id="c4d.plugins.SculptBrushToolData.StartStrokeInstance"></a>

Called after [`StartStroke()`](#c4d.plugins.SculptBrushToolData.StartStroke). Called once for each brush instance at the start of a stroke.  
The number of instances will change depending on the symmetry mirroring and radial settings.  
Use this method to allocate any data you may want to access during a brush stroke, that may be specific for each individual instance.  
Setup here any data on your brush that you might want to access from within your [`ApplyDab()`](#c4d.plugins.SculptBrushToolData.ApplyDab) override via `BrushDabData.GetBrush()`.

> **Note:** **StartStrokeInstance()** will only be called if `SculptBrushParams.EnableBrushAccess()` has been set to **True**.

**Parameters:** **strokeInstanceID** (*int*) – The ID of the brush instance being drawn.

#### `SculptBrushToolData.StartStrokeInstanceDabs(self, strokeInstanceID)` <a id="c4d.plugins.SculptBrushToolData.StartStrokeInstanceDabs"></a>

Called before all the dabs for a single instance are about to be drawn.  
After this call all the dabs for just one instance of the brush on the surface will interpolate between the 2 mouse locations on the object then draw all the dabs for that instance.  
Use this method to setup any data on your brush that you might want to access from within your [`ApplyDab()`](#c4d.plugins.SculptBrushToolData.ApplyDab) override via `BrushDabData.GetBrush()`.

> **Note:** **StartStrokeInstanceDabs()** will only be called if `SculptBrushParams.EnableBrushAccess()` has been set to **True**.

**Parameters:** **strokeInstanceID** (*int*) – The ID of the brush instance being drawn.

#### `SculptBrushToolData.StartSymmetry(self)` <a id="c4d.plugins.SculptBrushToolData.StartSymmetry"></a>

Called directly before each individual brush instance is about to be handled.  
Between this method and [`EndSymmetry()`](#c4d.plugins.SculptBrushToolData.EndSymmetry) all the dabs for each instance will be drawn from one mouse location on the surface of the model to another.  
This method will be called every time the user moves its mouse over the object on the screen to indicate that a new batch of dabs is going to be drawn.  
Use this method to setup any data on your brush that you might want to access from within your [`ApplyDab()`](#c4d.plugins.SculptBrushToolData.ApplyDab) override via `BrushDabData.GetBrush()`.

> **Note:** **StartSymmetry()** will only be called if `SculptBrushParams.EnableBrushAccess()` has been set to **True**.

### Tool Operations <a id="c4d.plugins.SculptBrushToolData-method-Tool-Operations"></a>

#### `SculptBrushToolData.DoCommand(self, mode, arr, bc, doc, flags)` <a id="c4d.plugins.SculptBrushToolData.DoCommand"></a>

Called by [`SendModelingCommand()`](../../../c4d.utils/index.md#c4d.utils.SendModelingCommand) to perform a command.

**Parameters:**

- **mode** (*int*) –

  The modeling mode:

  |   |   |
  |---|---|
  | *MODELINGCOMMANDMODE_ALL* | All points/polygons. |
  | *MODELINGCOMMANDMODE_POINTSELECTION* | Only the current point selection. |
  | *MODELINGCOMMANDMODE_POLYGONSELECTION* | Only the current polygon selection. |
  | *MODELINGCOMMANDMODE_EDGESELECTION* | Only the current edge selection. |

- **arr** (*List*[[*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]) – The input objects.

- **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The modeling command settings container.

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the operation.

- **flags** (*int*) –

  The flags:

  |   |   |
  |---|---|
  | *MODELINGCOMMANDFLAGS_NONE* | None. |
  | *MODELINGCOMMANDFLAGS_CREATEUNDO* | Creates undo and inserts newly created objects into the passed document, instead of returning result. |

#### `SculptBrushToolData.FreeTool(self, doc, data)` <a id="c4d.plugins.SculptBrushToolData.FreeTool"></a>

Called each time the user chooses another tool.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The original tool settings container.

**Return type:** bool

**Returns:** **True** if there was no error, otherwise **False**.

#### `SculptBrushToolData.GetState(self, doc)` <a id="c4d.plugins.SculptBrushToolData.GetState"></a>

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

#### `SculptBrushToolData.InitTool(self, doc, data, bt)` <a id="c4d.plugins.SculptBrushToolData.InitTool"></a>

Called each time the tool is selected.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The original tool settings container.
- **bt** ([*c4d.threading.BaseThread*](../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)) – The thread this method is being called from.

**Return type:** bool

**Returns:** **True** if there was no error, otherwise **False**.

#### `SculptBrushToolData.Message(self, doc, data, type, t_data)` <a id="c4d.plugins.SculptBrushToolData.Message"></a>

Called when the tool receives messages.

> **See also:** [C4DAtom and Plugin Messages](../../../../consts/MSG_C4DATOM_PLUGINS.md) for information on the messages type, data and input/output.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The currently active document.
- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The current tool data.
- **type** (*int*) – The message type.
- **t_data** (*any*) – Depends on *type*.

**Return type:** bool

**Returns:** Depends on the message type.

### View Rendering <a id="c4d.plugins.SculptBrushToolData-method-View-Rendering"></a>

#### `SculptBrushToolData.Draw(self, doc, data, bd, bh, bt, flags)` <a id="c4d.plugins.SculptBrushToolData.Draw"></a>

Called when the editor view is updated so you can display graphics for your tool in the view.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The currently active document.

- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The tool settings container.

- **bd** ([*c4d.BaseDraw*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The [`BaseDraw`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw) object for the active editor view.

- **bh** ([*c4d.plugins.BaseDrawHelp*](../../BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp)) – The [`BaseDrawHelp`](../../BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp) object for the active editor view.

- **bt** ([*c4d.threading.BaseThread*](../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)) – The thread this method is being called from.

- **flags** (*int*) –

  The flags are:

  |   |   |
  |---|---|
  | *TOOLDRAWFLAGS_NONE* | None. |
  | *TOOLDRAWFLAGS_INVERSE_Z* | Inverse Z-buffer mode. If set, the drawing engine of Cinema 4D will only draw elements if they are further away from the camera than other objects.  <br>This is mostly used for help lines (such as the semi-transparent axis inside of objects).<br>> **Note:** This mode only works when all objects are drawn so it should be passed last. |
  | *TOOLDRAWFLAGS_HIGHLIGHT* | Highlight mode. |

**Return type:** int

**Returns:**

The values for this are:

|   |   |
|---|---|
| *TOOLDRAW_NONE* | None. |
| *TOOLDRAW_HANDLES* | The active objects handles will be drawn. |
| *TOOLDRAW_AXIS* | The active objects axes will be drawn. |
| *TOOLDRAW_HIGHLIGHTS* | The highlights will be drawn. |

#### `SculptBrushToolData.DrawNonModelPickMode(self, doc, data, bd, bh, bt, flags)` <a id="c4d.plugins.SculptBrushToolData.DrawNonModelPickMode"></a>

Private.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The current document.

- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The brush data.

- **bd** ([*c4d.BaseDraw*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The editor view the tool is being used in.

- **bh** ([*c4d.plugins.BaseDrawHelp*](../../BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp)) – The [`BaseDrawHelp`](../../BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp) object for the active editor view.

- **bt** ([*c4d.threading.BaseThread*](../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)) – The thread this method is being called from.

- **flags** (*int*) –

  The flags:

  |   |   |
  |---|---|
  | *TOOLDRAWFLAGS_NONE* | None. |
  | *TOOLDRAWFLAGS_INVERSE_Z* | Inverse Z-buffer mode. If set, the drawing engine of Cinema 4D will only draw elements if they are further away from the camera than other objects.  <br>This is mostly used for help lines (such as the semi-transparent axis inside of objects).<br>> **Note:** This mode only works when all objects are drawn so it should be passed last. |
  | *TOOLDRAWFLAGS_HIGHLIGHT* | Highlight mode. |

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SculptBrushToolData.HasDrawMode(self, mode)` <a id="c4d.plugins.SculptBrushToolData.HasDrawMode"></a>

Override to let the system know what draw modes the brush supports.  
The system will call this method to check if a draw mode is supported by this brush. If the brush supports all the draw modes then it can just return **True**.  
Otherwise you can specify which draw modes should be enabled by checking each of them.

**Parameters:** **mode** (*int*) – The ID for the DrawMode. For example *MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_LINE*.

**Return type:** bool

**Returns:** **True** if the draw *mode* is supported, otherwise **False**.
