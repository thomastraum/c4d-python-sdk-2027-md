<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.gui/EditorWindow/index.html -->

# c4d.gui.EditorWindow <a id="c4d-gui-editorwindow"></a>

## *class* `c4d.gui.EditorWindow` <a id="c4d.gui.EditorWindow"></a>

## Overview <a id="overview"></a>

**Coordinate Conversion**

- [`EditorWindow.Global2Local()`](#c4d.gui.EditorWindow.Global2Local): Transforms global window coordinates (relative to the top left corner of the application window) to local coordinates (relative to the top left corner of the user area).
- [`EditorWindow.Local2Global()`](#c4d.gui.EditorWindow.Local2Global): Transforms local coordinates (relative to the top left corner of the user area) to global window coordinates (relative to the top left corner of the application window).
- [`EditorWindow.Local2Screen()`](#c4d.gui.EditorWindow.Local2Screen): Transforms local coordinates (relative to the top left corner of the user area) to screen coordinates (relative to the top left corner of the system screen).
- [`EditorWindow.Screen2Local()`](#c4d.gui.EditorWindow.Screen2Local): Transforms screen coordinates (relative to the top left corner of the system screen) to local coordinates (relative to the top left corner of the user area).

**Input Handling**

- [`EditorWindow.BfGetInputEvent()`](#c4d.gui.EditorWindow.BfGetInputEvent): Gets the next input event for a certain device from the event queue.
- [`EditorWindow.BfGetInputState()`](#c4d.gui.EditorWindow.BfGetInputState): Polls a certain channel of a device for the current input state.
- [`EditorWindow.IsHotkeyDown()`](#c4d.gui.EditorWindow.IsHotkeyDown): Checks the standard navigation hotkeys.

**Mouse Interaction**

- [`EditorWindow.MouseDrag()`](#c4d.gui.EditorWindow.MouseDrag): Checks for the mouse drag status.
- [`EditorWindow.MouseDragEnd()`](#c4d.gui.EditorWindow.MouseDragEnd): Checks why the mouse drag ended.
- [`EditorWindow.MouseDragStart()`](#c4d.gui.EditorWindow.MouseDragStart): Initializes a mouse dragging loop.

**Visual Feedback**

- [`EditorWindow.DrawXORLine()`](#c4d.gui.EditorWindow.DrawXORLine): Draws an XOR line in the editor view.
- [`EditorWindow.StatusSetText()`](#c4d.gui.EditorWindow.StatusSetText): Sets the text in the status bar.

## Members <a id="members"></a>

### Coordinate Conversion <a id="c4d.gui.EditorWindow-method-Coordinate-Conversion"></a>

#### `EditorWindow.Global2Local(self)` <a id="c4d.gui.EditorWindow.Global2Local"></a>

Transforms global window coordinates (relative to the top left corner of the application window) to local coordinates (relative to the top left corner of the user area).

```python
x, y = win.Global2Local()
```

**Return type:** Tuple[int, int]

**Returns:** The local x and y coordinate.

**Raises:** **RuntimeError** – If the coordinates cannot be transformed.

#### `EditorWindow.Local2Global(self)` <a id="c4d.gui.EditorWindow.Local2Global"></a>

Transforms local coordinates (relative to the top left corner of the user area) to global window coordinates (relative to the top left corner of the application window).

```python
x, y = win.Local2Global()
```

**Return type:** Tuple[int, int]

**Returns:** The global x and y coordinate.

**Raises:** **RuntimeError** – If the coordinates cannot be transformed.

#### `EditorWindow.Local2Screen(self)` <a id="c4d.gui.EditorWindow.Local2Screen"></a>

Transforms local coordinates (relative to the top left corner of the user area) to screen coordinates (relative to the top left corner of the system screen).

```python
x, y = win.Local2Screen()
```

**Return type:** Tuple[int, int]

**Returns:** The screen x and y coordinate.

**Raises:** **RuntimeError** – If the coordinates cannot be transformed.

#### `EditorWindow.Screen2Local(self)` <a id="c4d.gui.EditorWindow.Screen2Local"></a>

Transforms screen coordinates (relative to the top left corner of the system screen) to local coordinates (relative to the top left corner of the user area).

```python
x, y = win.Screen2Local()
```

**Return type:** Tuple[int, int]

**Returns:** The local x and y coordinate.

**Raises:** **RuntimeError** – If the coordinates cannot be transformed.

### Input Handling <a id="c4d.gui.EditorWindow-method-Input-Handling"></a>

#### `EditorWindow.BfGetInputEvent(self, askdevice, res)` <a id="c4d.gui.EditorWindow.BfGetInputEvent"></a>

Gets the next input event for a certain device from the event queue.

**Parameters:**

- **askdevice** (*int*) – The device to ask. Either **BFM_INPUT_MOUSE** or **BFM_INPUT_KEYBOARD**.
- **res** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The result container.

**Return type:** bool

**Returns:** **True** if the event could be retrieved in *res*, otherwise **False**.

#### `EditorWindow.BfGetInputState(self, askdevice, askchannel, res)` <a id="c4d.gui.EditorWindow.BfGetInputState"></a>

Polls a certain channel of a device for the current input state.

**Parameters:**

- **askdevice** (*int*) – The device to ask. Either **BFM_INPUT_MOUSE** or **BFM_INPUT_KEYBOARD**.
- **askchannel** (*int*) – The channel to ask.
- **res** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The result container.

**Return type:** bool

**Returns:** **True** if the state could be retrieved in *res*, otherwise **False**.

#### `EditorWindow.IsHotkeyDown(self, id)` <a id="c4d.gui.EditorWindow.IsHotkeyDown"></a>

Checks the standard navigation hotkeys.

*New in version R23.105.*

**Parameters:**

**id** (*int*) –

The hotkey to check:

|   |   |
|---|---|
| *HOTKEY_CAMERA_MOVE* | Camera move. |
| *HOTKEY_CAMERA_SCALE* | Camera scale |
| *HOTKEY_CAMERA_ROTATE* | Camera rotate. |
| *HOTKEY_OBJECT_MOVE* | Object move. |
| *HOTKEY_OBJECT_SCALE* | Object scale |
| *HOTKEY_OBJECT_ROTATE* | Object rotate. |
| *HOTKEY_SELECT_FREE* | Freehand selection. |
| *HOTKEY_SELECT_LIVE* | Live selection. |
| *HOTKEY_SELECT_RECT* | Rectangle selection. |
| *HOTKEY_MODEL_SCALE* | Model scale. |
| *HOTKEY_ZOOM* | Zoom. |
| *HOTKEY_PARENT_MOVE* | Parent object move. |
| *HOTKEY_RESIZE_BRUSH* | Resize brush. |

**Returns:**

A value != 0 if the hotkey is pressed.

|   |   |
|---|---|
| *HOTKEYFLAGS_NONE* | Nothing was used. |
| *HOTKEYFLAGS_MOUSE* | Mouse was used. |
| *HOTKEYFLAGS_KEYBOARD* | Keyboard was used. |

**Return type:** int

### Mouse Interaction <a id="c4d.gui.EditorWindow-method-Mouse-Interaction"></a>

#### `EditorWindow.MouseDrag(self)` <a id="c4d.gui.EditorWindow.MouseDrag"></a>

Checks for the mouse drag status.

```python
result, dx, dy, channels = win.MouseDrag()
```

**Return type:** Tuple[int, float, float, [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)]

**Returns:** A tuple.

#### `EditorWindow.MouseDragEnd(self)` <a id="c4d.gui.EditorWindow.MouseDragEnd"></a>

Checks why the mouse drag ended. Allows to perform any undo operations needed if the user canceled the drag.

**Return type:** int

**Returns:**

The mouse drag result:

|   |   |
|---|---|
| *MOUSEDRAGRESULT_ESCAPE* | Drag aborted. |
| *MOUSEDRAGRESULT_FINISHED* | Drag finished. |
| *MOUSEDRAGRESULT_CONTINUE* | Drag still in progress. |

#### `EditorWindow.MouseDragStart(self, button, mx, my, flags)` <a id="c4d.gui.EditorWindow.MouseDragStart"></a>

Initializes a mouse dragging loop.

For instance in a `ToolData.MouseInput()`.

```python
mousex = msg[c4d.BFM_INPUT_X]
mousey = msg[c4d.BFM_INPUT_Y]

win.MouseDragStart(c4d.KEY_MLEFT, mousex, mousey, c4d.MOUSEDRAGFLAGS_DONTHIDEMOUSE|c4d.MOUSEDRAGFLAGS_NOMOVE)

mx = mousex
my = mousey
while True:
    result, dx, dy, channels = win.MouseDrag()
    if result !=c4d.MOUSEDRAGRESULT_CONTINUE:
        break

    mx += dx
    my += dy
    print(f"Mouse Dragging at position {mx}, {my}")

print(f"Mouse Dragging Ended: {win.MouseDragEnd()}")
```

**Parameters:**

- **button** (*int*) – State of the mouse buttons.

- **mx** (*float*) – The mouse X coordinate.

- **my** (*float*) – The mouse Y coordinate.

- **flags** (*int*) –

  The mouse drag flags:

  |   |   |
  |---|---|
  | *MOUSEDRAGFLAGS_NONE* | None. |
  | *MOUSEDRAGFLAGS_DONTHIDEMOUSE* | Show mouse pointer during drag. |
  | *MOUSEDRAGFLAGS_NOMOVE* | *MouseDrag()* returns *MOUSEDRAGRESULT_CONTINUE* even if mouse is not moved. Otherwise *MouseDrag()* only returns if mouse is moved. |
  | *MOUSEDRAGFLAGS_EVERYPACKET* | Receive every packet of the queue, otherwise only data of the last packet. |
  | *MOUSEDRAGFLAGS_COMPENSATEVIEWPORTORG* | Compensates the viewport origin during drag. |
  | *MOUSEDRAGFLAGS_AIRBRUSH* | Airbrush mode. |

### Visual Feedback <a id="c4d.gui.EditorWindow-method-Visual-Feedback"></a>

#### `EditorWindow.DrawXORLine(self, x1, y1, x2, y2)` <a id="c4d.gui.EditorWindow.DrawXORLine"></a>

Draws an XOR line in the editor view.

**Parameters:**

- **x1** (*int*) – Start X coordinate of the line.
- **y1** (*int*) – Start Y coordinate of the line.
- **x2** (*int*) – End X coordinate of the line.
- **y2** (*int*) – End Y coordinate of the line.

#### `EditorWindow.StatusSetText(self, str)` <a id="c4d.gui.EditorWindow.StatusSetText"></a>

Sets the text in the status bar.

*New in version R23.105.*

**Parameters:** **str** (*str*) – The text for the status bar.
