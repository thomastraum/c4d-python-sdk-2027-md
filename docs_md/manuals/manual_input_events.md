<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_input_events.html -->

# Input Events <a id="input-events"></a><a id="inputevents"></a>

Input events are messages about input from the keyboard or from the mouse.

## Distribution <a id="distribution"></a>

All input events are stored in a central queue. The events are automatically sent to `GeUserArea.InputEvent()` if the user area is in focus. They can also be intercepted in `GeDialog.Message()`.  
Further, any code can either poll the event queue with [`GetInputEvent()`](../modules/c4d.gui/index.md#c4d.gui.GetInputEvent) or get the current input state with [`GetInputState()`](../modules/c4d.gui/index.md#c4d.gui.GetInputState).

## Structure <a id="structure"></a>

Input events are stored in [`BaseContainer`](../modules/c4d/BaseContainer/index.md#c4d.BaseContainer) objects. The ID of the container is *BFM_INPUT* (this is also the ID to look for in `GeDialog.Message()`). The content of the container is:

|   |   |   |
|---|---|---|
| *BFM_INPUT_QUALIFIER* | int | A bit mask with the qualifiers at the time when the event occurred: |
|  | *QUALIFIER_NONE* | None. |
|  | *QUALIFIER_SHIFT* | Shift key. |
|  | *QUALIFIER_CTRL* | Ctrl key. |
|  | *QUALIFIER_MOUSEHIT* | Indication in `ObjectData.DetectHandle()` that the user pressed the mouse. |
|  |  | For instance if *QUALIFIER_MOUSEHIT* and *QUALIFIER_CTRL* are set, a new element could be created. |
| *BFM_INPUT_MODIFIERS* | int | Same as *BFM_INPUT_QUALIFIER* but also contains bits > *0xf*. Private. |
| *BFM_INPUT_DEVICE* | int | Device: |
|  | *BFM_INPUT_MOUSE* | Mouse. |
|  | *BFM_INPUT_KEYBOARD* | Keyboard. |
| *BFM_INPUT_ASC* | str | Contains the Unicode input from keyboard. |
| *BFM_INPUT_CHANNEL* | int | Contains the key or button. See also [KEY](../consts/KEY.md). |
|  | *BFM_INPUT_MOUSELEFT* | Left mouse button. |
|  | *BFM_INPUT_MOUSERIGHT* | Right mouse button. |
|  | *BFM_INPUT_MOUSEMIDDLE* | Middle mouse button. |
|  | *BFM_INPUT_MOUSEX1* | Fourth mouse button. |
|  | *BFM_INPUT_MOUSEX2* | Five mouse button. |
|  | *BFM_INPUT_MOUSEWHEEL* | Mouse wheel. |
|  | *BFM_INPUT_MOUSEMOVE* | Mouse move. |
| *BFM_INPUT_VALUE* | int | Value of the input channel (Usually **True**/**False** or a int value, e.g. for scroll wheel data). |
| *BFM_INPUT_VALUE_REAL* | float | Channel value (e.g. pressure). |
| *BFM_INPUT_X* | int32 | Mouse X position. |
| *BFM_INPUT_Y* | int32 | Mouse Y position. |
| *BFM_INPUT_Z* | int32 | Mouse Z position. |
| *BFM_INPUT_TILT* | int | Pen tilt. |
| *BFM_INPUT_ORIENTATION* | float | Pen rotation. |
| *BFM_INPUT_P_ROTATION* | float | Pen rotation around its own axis. |
| *BFM_INPUT_FINGERWHEEL* | int | Finger wheel. |
| *BFM_INPUT_DOUBLECLICK* | bool | Double click. |
| *BFM_INPUT_AFTER_SCROLL* | int | Input message ID sent after scroll area processed input messages. |

There are also the key symbols which are important in the context of input events.

|   |   |
|---|---|
| *KEY_MLEFT* |  |
| *KEY_MRIGHT* |  |
| *KEY_MMIDDLE* |  |
| *KEY_MX1* |  |
| *KEY_MX2* |  |
| *KEY_SHIFT* |  |
| *KEY_CONTROL* |  |
| *KEY_ALT* |  |
| *KEY_CAPSLOCK* |  |
| *KEY_MODIFIERS* |  |
| *KEY_COMMAND* |  |
| *KEY_BACKSPACE* |  |
| *KEY_TAB* |  |
| *KEY_ENTER* |  |
| *KEY_ESC* |  |
| *KEY_SPACE* |  |
| *KEY_DELETE* |  |
| *KEY_UP* |  |
| *KEY_DOWN* |  |
| *KEY_LEFT* |  |
| *KEY_RIGHT* |  |
| *KEY_PGUP* |  |
| *KEY_PGDOWN* |  |
| *KEY_HOME* |  |
| *KEY_END* |  |
| *KEY_INSERT* |  |
| *KEY_F1* |  |
| *KEY_F2* |  |
| *KEY_F3* |  |
| *KEY_F4* |  |
| *KEY_F5* |  |
| *KEY_F6* |  |
| *KEY_F7* |  |
| *KEY_F8* |  |
| *KEY_F9* |  |
| *KEY_F10* |  |
| *KEY_F11* |  |
| *KEY_F12* |  |
| *KEY_F13* |  |
| *KEY_F14* |  |
| *KEY_F15* |  |
| *KEY_F16* |  |
| *KEY_F17* |  |
| *KEY_F18* |  |
| *KEY_F19* |  |
| *KEY_F20* |  |
| *KEY_F21* |  |
| *KEY_F22* |  |
| *KEY_F23* |  |
| *KEY_F24* |  |
| *KEY_F25* |  |
| *KEY_F26* |  |
| *KEY_F27* |  |
| *KEY_F28* |  |
| *KEY_F29* |  |
| *KEY_F30* |  |
| *KEY_F31* |  |
| *KEY_F32* |  |

> **Note:** The values for *BFM_INPUT_DEVICE* and *BFM_INPUT_CHANNEL* are used with [`GetInputState()`](../modules/c4d.gui/index.md#c4d.gui.GetInputState) and [`GetInputEvent()`](../modules/c4d.gui/index.md#c4d.gui.GetInputEvent) to get specific events only.

## Continuous Polling <a id="continuous-polling"></a>

There are no events for things like mouse-up or mouse-leave in Cinema 4D. The reason is that there is no reliable way to get such messages that is completely portable. Therefore it is sometimes necessary to enter a manual while loop that ends when the mouse is released. For example, to track how the user drags something with the left button down one would do:

```python
state = c4d.BaseContainer()
x, y = None, None

while gui.GetInputState(c4d.BFM_INPUT_MOUSE, c4d.BFM_INPUT_MOUSELEFT, state):
    if state.GetInt32(c4d.BFM_INPUT_VALUE)==0:
        break

    x = state.GetInt32(c4d.BFM_INPUT_X)
    y = state.GetInt32(c4d.BFM_INPUT_Y)

# Use x and y as Python will expose the last state of x and y in the 'while' scope to the outer scope.
if None in (x, y):
    raise RuntimeError("Left mouse button has not been pressed.")

if lowerBoundary.x <= x <= upperBoundary.x:
    # ...
```

Make sure to not to get caught in infinite loops during such polls. When sending *BFM_ACTION* messages, for example from a custom slider control, set the *BFM_ACTION_INDRAG* flag to **True** in those messages while in the loop.

## Polling for Character and Special Character Keys <a id="polling-for-character-and-special-character-keys"></a>

For modifier and control keys Cinema 4D does provide symbols, as shown in the table above, with which one can poll for them. But one can also poll for character and special character keys, which are identified by their standard decimal ASCII number. Note that Cinema 4D always treats characters as upper-keys in this context, since modifier keys are being handled separately. This also limits the number of special characters that can be polled depending on they keyboard layout, i.e., polled can only be these, which do not require a modifier key like SHIFT. The example function below showcases how to carry out the polling for multiple character keys at a time, to, for example, invoke a shortcut.

```python
def GetCharacterKeysInput(*args: tuple[str]) -> dict[str]:
    """Returns the key state for an arbitrary number of character keys.
    """
    result = {}
    for char in (n.upper() for n in args if isinstance(n, str) and len(n)==1):
        bc = c4d.BaseContainer()
        if not c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, ord(char), bc):
            raise RuntimeError("Failed to poll the keyboard.")

        result[char] = True if bc[c4d.BFM_INPUT_VALUE] == 1 else False

    return result

result = GetCharacterKeysInput("A", "F", "+")
print (result)
```

### See Also <a id="see-also"></a>

- [Message System](manual_message_system.md): Explains messages between Cinema 4D scene elements and interfaces.
- [Implementing Plugins](manual_implementing_plugins.md): Explains the basic concepts of implementing plugins.
- [Example user_area_drag.py](../examples/gui/user_area_drag.py.md): Creates and attaches a GeUserArea to a Dialog. Creates a series of aligned squares, that can be dragged and swapped together.
- [Example py_tool_ui.pyp](../examples/plugins/py_tool_ui/py_tool_ui.pyp.md): Demonstrates how to implement a ToolData with a linkBox where it’s possible to drag and drop an object, which is then cloned and added to the document in a random position.
