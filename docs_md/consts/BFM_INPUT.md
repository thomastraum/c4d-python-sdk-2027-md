<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/BFM_INPUT.html -->

# BFM_INPUT <a id="bfm-input"></a>

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
| *BFM_INPUT_CHANNEL* | int | Contains the key or button. See also [KEY](KEY.md). |
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
