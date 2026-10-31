<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.gui/GeUserArea/index.html -->

# c4d.gui.GeUserArea <a id="c4d-gui-geuserarea"></a>

## *class* `c4d.gui.GeUserArea` <a id="c4d.gui.GeUserArea"></a>

This class helps you to create custom gadgets for dialogs in Cinema 4D.

> **Note:**
>
> Just take care about the lifetime of your [`GeUserArea`](#c4d.gui.GeUserArea) instance.  
> If you pass an instance of this class to a dialog, a reference is hold by the dialog and released when the dialog is freed.  
> That also means that each instance of your [`GeUserArea`](#c4d.gui.GeUserArea) class is still alive until the host-dialog is freed, even you dont hold a reference to it.  
> If you want to use the same instance of your [`GeUserArea`](#c4d.gui.GeUserArea) class on the next time you open the dialog, you have to store the instance in the class scope.

The class to create custom user areas.

## Overview <a id="overview"></a>

**Basic Functions**

- [`GeUserArea.LayoutChanged()`](#c4d.gui.GeUserArea.LayoutChanged): Tells Cinema 4D that the user area now has new dimensions.

**Basic Methods**

- [`GeUserArea.GetHeight()`](#c4d.gui.GeUserArea.GetHeight): Returns the height of the user area.
- [`GeUserArea.GetId()`](#c4d.gui.GeUserArea.GetId): Returns the ID of the user area.
- [`GeUserArea.GetWidth()`](#c4d.gui.GeUserArea.GetWidth): Returns the width of the user area.
- [`GeUserArea.HasFocus()`](#c4d.gui.GeUserArea.HasFocus): Indicates the focus state.
- [`GeUserArea.IsEnabled()`](#c4d.gui.GeUserArea.IsEnabled): Indicates the enabled state.
- [`GeUserArea.IsR2L()`](#c4d.gui.GeUserArea.IsR2L): Checks if the user area has to be drawn in right-to-left layout mode.
- [`GeUserArea.Redraw()`](#c4d.gui.GeUserArea.Redraw): Forces the user area to redraw itself.
- [`GeUserArea.SendParentMessage()`](#c4d.gui.GeUserArea.SendParentMessage): Use this function to send a custom message to the parent dialog.
- [`GeUserArea.SendParentMessageResult()`](#c4d.gui.GeUserArea.SendParentMessageResult): Sends a custom message to the parent dialog.
- [`GeUserArea.SetTimer()`](#c4d.gui.GeUserArea.SetTimer): Initializes the timer clock, so that `Timer()` is called every timer milliseconds.

**Border Methods**

- [`GeUserArea.GetBorderSize()`](#c4d.gui.GeUserArea.GetBorderSize): Retrieves the space required to draw a border.

**Coordinates Transformation**

- [`GeUserArea.Global2Local()`](#c4d.gui.GeUserArea.Global2Local): Transforms global coordinates (relative to the top left corner of the physical window) to local coordinates (relative to the top left corner of the dialog). Result is a dict with member keys *x* and *y* of type *int*.
- [`GeUserArea.Local2Global()`](#c4d.gui.GeUserArea.Local2Global): Transforms local coordinates (relative to the top left corner of the dialog) to global coordinates (relative to the top left corner of the physical window). Result is a dict with member keys *x* and *y* of type *int*.
- [`GeUserArea.Local2Screen()`](#c4d.gui.GeUserArea.Local2Screen): Transforms local coordinates (relative to the top left corner of the dialog) to screen coordinates (relative to the top left corner of the system screen). Result is a dict with member keys *x* and *y* of type *int*.
- [`GeUserArea.Screen2Local()`](#c4d.gui.GeUserArea.Screen2Local): Transforms screen coordinates (relative to the top left corner of the system screen) to local coordinates (relative to the top left corner of the dialog). Result is a dict with member keys *x* and *y* of type *int*.

**Dialog Information Methods**

- [`GeUserArea.GetColorRGBA()`](#c4d.gui.GeUserArea.GetColorRGBA): Gets the RGBA values associated with a color ID.

**Drag and Drop Methods**

- [`GeUserArea.CheckDropArea()`](#c4d.gui.GeUserArea.CheckDropArea): Checks the drag position in a drag event message against the user area’s position in the layout.
- [`GeUserArea.GetDragObject()`](#c4d.gui.GeUserArea.GetDragObject): Extracts the object from a drag and drop message.
- [`GeUserArea.GetDragPosition()`](#c4d.gui.GeUserArea.GetDragPosition): Extracts local drag coordinates from a drag and drop event.
- [`GeUserArea.HandleMouseDrag()`](#c4d.gui.GeUserArea.HandleMouseDrag): Starts a drag and drop operation.
- [`GeUserArea.MouseDrag()`](#c4d.gui.GeUserArea.MouseDrag): Polls the mouse during a drag started with `MouseDragStart()`.
- [`GeUserArea.MouseDragEnd()`](#c4d.gui.GeUserArea.MouseDragEnd): Checks why the mouse drag ended.
- [`GeUserArea.MouseDragStart()`](#c4d.gui.GeUserArea.MouseDragStart): Starts a mouse drag.
- [`GeUserArea.SetDragDestination()`](#c4d.gui.GeUserArea.SetDragDestination): Sets the correct cursor during drag and drop handling.

**Draw Helpers Methods**

- [`GeUserArea.ClearClippingRegion()`](#c4d.gui.GeUserArea.ClearClippingRegion): Clears any clipping region set with `SetClippingRegion()`.
- [`GeUserArea.OffScreenOn()`](#c4d.gui.GeUserArea.OffScreenOn): Enables double buffering to avoid blinking and flickering effects.
- [`GeUserArea.SetClippingRegion()`](#c4d.gui.GeUserArea.SetClippingRegion): Should be used at the top of the `DrawMsg()` function to specify the clipping region.

**Draw Methods**

- [`GeUserArea.DrawBezier()`](#c4d.gui.GeUserArea.DrawBezier): Draws concatenated bezier curves.
- [`GeUserArea.DrawBezierFill()`](#c4d.gui.GeUserArea.DrawBezierFill): Draws concatenated Bezier curves.
- [`GeUserArea.DrawBezierLine()`](#c4d.gui.GeUserArea.DrawBezierLine): Draws concatenated Bezier curves.
- [`GeUserArea.DrawBitmap()`](#c4d.gui.GeUserArea.DrawBitmap): Draws a bitmap into the user area.
- [`GeUserArea.DrawBitmapRounded()`](#c4d.gui.GeUserArea.DrawBitmapRounded): Draw a bitmap with rounded edges into the user area.
- [`GeUserArea.DrawBorder()`](#c4d.gui.GeUserArea.DrawBorder): Fills a rectangular area with the current pen color between (x1,y1) and (x2,y2).
- [`GeUserArea.DrawCustomButton()`](#c4d.gui.GeUserArea.DrawCustomButton): Draws a button.
- [`GeUserArea.DrawEllipseFill()`](#c4d.gui.GeUserArea.DrawEllipseFill): Draws an ellipse filled with color.
- [`GeUserArea.DrawEllipseLine()`](#c4d.gui.GeUserArea.DrawEllipseLine): Draws an ellipse line.
- [`GeUserArea.DrawFrame()`](#c4d.gui.GeUserArea.DrawFrame): Draws a rectangular frame with the current pen color between (*x1,y1*) and (*x2,y2*).
- [`GeUserArea.DrawGetFontBaseLine()`](#c4d.gui.GeUserArea.DrawGetFontBaseLine): Returns the base line of the set font.
- [`GeUserArea.DrawGetFontHeight()`](#c4d.gui.GeUserArea.DrawGetFontHeight): Returns the height in pixels of a line of text in the current font.
- [`GeUserArea.DrawGetTextIndexFromPixel()`](#c4d.gui.GeUserArea.DrawGetTextIndexFromPixel): Retrieves the index from a position within the text.
- [`GeUserArea.DrawGetTextWidth()`](#c4d.gui.GeUserArea.DrawGetTextWidth): Returns the width in pixels of the string *text*, if it were drawn in the current font.
- [`GeUserArea.DrawGetTextWidth_ListNodeName()`](#c4d.gui.GeUserArea.DrawGetTextWidth_ListNodeName): Retrieves the width in pixels of the name of *node*.
- [`GeUserArea.DrawImageRef()`](#c4d.gui.GeUserArea.DrawImageRef): Draws a image into the user area.
- [`GeUserArea.DrawLine()`](#c4d.gui.GeUserArea.DrawLine): Draws a line with the current pen color between (*x1,y1*) and (*x2,y2*).
- [`GeUserArea.DrawPolyFill()`](#c4d.gui.GeUserArea.DrawPolyFill): Draws a polygon filled with color.
- [`GeUserArea.DrawPolyLine()`](#c4d.gui.GeUserArea.DrawPolyLine): Draws a polygon line.
- [`GeUserArea.DrawRectangle()`](#c4d.gui.GeUserArea.DrawRectangle): Fills a rectangular area with the current pen color between (x1,y1) and (x2,y2).
- [`GeUserArea.DrawRoundedFrame()`](#c4d.gui.GeUserArea.DrawRoundedFrame): Draws a rectangular frame with the current pen color between (*x1,y1*) and (*x2,y2*).
- [`GeUserArea.DrawRoundedRectangle()`](#c4d.gui.GeUserArea.DrawRoundedRectangle): Fills a rectangular area with the current pen color between (x1,y1) and (x2,y2).
- [`GeUserArea.DrawSetFont()`](#c4d.gui.GeUserArea.DrawSetFont): Sets the text font.
- [`GeUserArea.DrawSetOpacity()`](#c4d.gui.GeUserArea.DrawSetOpacity): Sets the opacity value.
- [`GeUserArea.DrawSetPen()`](#c4d.gui.GeUserArea.DrawSetPen): Sets the draw color.
- [`GeUserArea.DrawSetTextCol()`](#c4d.gui.GeUserArea.DrawSetTextCol): Sets the draw color.
- [`GeUserArea.DrawSetTextRotation()`](#c4d.gui.GeUserArea.DrawSetTextRotation): Rotates the font for drawing.
- [`GeUserArea.DrawText()`](#c4d.gui.GeUserArea.DrawText): Draws the string *txt* with the upper left corner at the position (*x*, *y*).
- [`GeUserArea.FillBitmapBackground()`](#c4d.gui.GeUserArea.FillBitmapBackground): Fills the bitmap *bmp* with the current pen color.
- [`GeUserArea.GetColorRGB()`](#c4d.gui.GeUserArea.GetColorRGB): Gets the RGB values associated with a color ID.

**Fading Methods**

- [`GeUserArea.ActivateFading()`](#c4d.gui.GeUserArea.ActivateFading): Activates the fading.
- [`GeUserArea.AdjustColor()`](#c4d.gui.GeUserArea.AdjustColor): Sets the blend colors for user area fading.

**Inputs Methods**

- [`GeUserArea.GetInputEvent()`](#c4d.gui.GeUserArea.GetInputEvent): Gets the next input event for a certain device from the event queue.
- [`GeUserArea.GetInputState()`](#c4d.gui.GeUserArea.GetInputState): Polls a certain channel of a device for the current input state.
- [`GeUserArea.IsHotkeyDown()`](#c4d.gui.GeUserArea.IsHotkeyDown): Checks the standard navigation hotkeys.
- [`GeUserArea.KillEvents()`](#c4d.gui.GeUserArea.KillEvents): Flushes all events from the window message queue.

**Magic Methods**

- [`GeUserArea.__init__()`](#c4d.gui.GeUserArea.__init__): Creates a user area that is not attached to any dialog.

**Methods to Override**

- [`GeUserArea.CoreMessage()`](#c4d.gui.GeUserArea.CoreMessage): Called when a Cinema 4D core messages is received.
- [`GeUserArea.DrawMsg()`](#c4d.gui.GeUserArea.DrawMsg): Called when Cinema 4D wants you to draw your userarea.
- [`GeUserArea.GetMinSize()`](#c4d.gui.GeUserArea.GetMinSize): Override this function to specify a minimum size for the user area.
- [`GeUserArea.Init()`](#c4d.gui.GeUserArea.Init): Called once when the user area is initialized by the GUI, before the layout is calculated.
- [`GeUserArea.InitValues()`](#c4d.gui.GeUserArea.InitValues): Called after the layout is calculated, before the user area is drawn.
- [`GeUserArea.InputEvent()`](#c4d.gui.GeUserArea.InputEvent): Called when an input event is received.
- [`GeUserArea.Message()`](#c4d.gui.GeUserArea.Message): Override this function to react to more messages than covered by the other functions.
- [`GeUserArea.Sized()`](#c4d.gui.GeUserArea.Sized): Called when the user area is resized.
- [`GeUserArea.Timer()`](#c4d.gui.GeUserArea.Timer): If you subscribe to timer events using `SetTimer()` (x), this function is called every *x* th millisecond.

**Miscellaneous**

- [`GeUserArea.GetPixelRatio()`](#c4d.gui.GeUserArea.GetPixelRatio): Always returns 1.0 except for user areas shown on OS X Retina displays, where it returns 2.0.
- [`GeUserArea.ScrollArea()`](#c4d.gui.GeUserArea.ScrollArea): Scrolls the area from *(x,y)* to *(x+w,y+h)* in the direction specified by *xdiff* and *ydiff*.

**Parent Dialog**

- [`GeUserArea.GetDialog()`](#c4d.gui.GeUserArea.GetDialog): Gets the user area’s parent dialog.

## Members <a id="members"></a>

### Basic Functions <a id="c4d.gui.GeUserArea-method-Basic-Functions"></a>

#### `GeUserArea.LayoutChanged(self)` <a id="c4d.gui.GeUserArea.LayoutChanged"></a>

Tells Cinema 4D that the user area now has new dimensions. That causes c4d to call:

> 1. [`GetMinSize()`](#c4d.gui.GeUserArea.GetMinSize)
> 2. [`Sized()`](#c4d.gui.GeUserArea.Sized)
> 3. [`InitValues()`](#c4d.gui.GeUserArea.InitValues)
> 4. [`DrawMsg()`](#c4d.gui.GeUserArea.DrawMsg)

### Basic Methods <a id="c4d.gui.GeUserArea-method-Basic-Methods"></a>

#### `GeUserArea.GetHeight(self)` <a id="c4d.gui.GeUserArea.GetHeight"></a>

Returns the height of the user area.

**Return type:** int

**Returns:** Height in pixels.

#### `GeUserArea.GetId(self)` <a id="c4d.gui.GeUserArea.GetId"></a>

Returns the ID of the user area.

**Return type:** int

**Returns:** The ID.

#### `GeUserArea.GetWidth(self)` <a id="c4d.gui.GeUserArea.GetWidth"></a>

Returns the width of the user area.

**Return type:** int

**Returns:** Width in pixels.

#### `GeUserArea.HasFocus(self)` <a id="c4d.gui.GeUserArea.HasFocus"></a>

Indicates the focus state.

**Return type:** bool

**Returns:** **True** if the user area has the focus in the dialog, otherwise **False**.

#### `GeUserArea.IsEnabled(self)` <a id="c4d.gui.GeUserArea.IsEnabled"></a>

Indicates the enabled state.

**Return type:** bool

**Returns:** **True** if the user area is enabled in the dialog, otherwise **False**.

#### `GeUserArea.IsR2L(self)` <a id="c4d.gui.GeUserArea.IsR2L"></a>

Checks if the user area has to be drawn in right-to-left layout mode.

**Return type:** bool

**Returns:** **True** if the user area is in right-to-left layout mode, otherwise **False**.

#### `GeUserArea.Redraw(self, thread=False)` <a id="c4d.gui.GeUserArea.Redraw"></a>

Forces the user area to redraw itself.

**Parameters:** **thread** (*bool*) – Must be set to **True** if the function is called from another thread than the main Cinema 4D thread.

#### `GeUserArea.SendParentMessage(self, msg)` <a id="c4d.gui.GeUserArea.SendParentMessage"></a>

Use this function to send a custom message to the parent dialog.

**Parameters:** **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The message container.

#### `GeUserArea.SendParentMessageResult(self, msg)` <a id="c4d.gui.GeUserArea.SendParentMessageResult"></a>

Sends a custom message to the parent dialog.

*New in version 24.*

**Parameters:** **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The message container.

**Returns:** Return the result of the message.

**Return type:** Any

#### `GeUserArea.SetTimer(self, x)` <a id="c4d.gui.GeUserArea.SetTimer"></a>

Initializes the timer clock, so that [`Timer()`](#c4d.gui.GeUserArea.Timer) is called every timer milliseconds.

> **Note:**
>
> Depending on the speed of the computer, the operating system, the complexity of the dialog and the threads running in the background, there is no guarantuee that event messages will occur on a regular basis.  
> Using a value of 500 ms should be no problem but if using a value of 1 ms one might get events with the following time spaces: 3 ms, 76 ms, 15 ms, 19 ms, 67 ms…

> **Note:** Keep in mind that using small timer values results in heavy message traffic in the application which may slow down Cinema 4D (and all other applications running on the computer) to a point where nothing is working any longer besides your dialog.

**Parameters:** **x** (*int*) – The timer interval in milliseconds.

### Border Methods <a id="c4d.gui.GeUserArea-method-Border-Methods"></a>

#### `GeUserArea.GetBorderSize(self, type)` <a id="c4d.gui.GeUserArea.GetBorderSize"></a>

Retrieves the space required to draw a border.

**Parameters:**

**type** (*int*) –

The border type:

|   |   |
|---|---|
| *BORDER_NONE* | No border. |
| *BORDER_THIN_IN* | Thin border inward. |
| *BORDER_THIN_OUT* | Thin border outward. |
| *BORDER_IN* | Normal border inward. |
| *BORDER_OUT* | Normal border outward. |
| *BORDER_GROUP_IN* | Group border inside. |
| *BORDER_GROUP_OUT* | Group border outside. |
| *BORDER_OUT2* | Outward border 2. |
| *BORDER_OUT3* | Outward border 3 |
| *BORDER_BLACK* | Thin black line. |
| *BORDER_ACTIVE_1* | Active border 1. |
| *BORDER_ACTIVE_2* | Active border 2. |
| *BORDER_ACTIVE_3* | Active border 3. |
| *BORDER_ACTIVE_4* | Active border 4. |
| *BORDER_GROUP_TOP* | Border along the top. |
| *BORDER_ROUND* | Border with round corners. |
| *BORDER_SCHEME_EDIT* | Edit field border like the shortcut gadget for example. |
| *BORDER_SCHEME_EDIT_NUMERIC* | Edit field border that is open to the right like the link field for example. |
| *BORDER_OUT3l* | Outward border 3, open to the left. |
| *BORDER_OUT3r* | Outward border 3, open to the right. |
| *BORDER_THIN_INb* | Thin border inward, open to the botton. |
| *BORDER_MASK* | Masks out border type. |
| *BORDER_TEXT_DOTTED* | Only used with `GeDialog.AddStaticText()`.  <br>Draws a dotted line at right of text, useful to visually connect the text with its parameter. |
| *BORDER_WITH_TITLE_MONO* | Display group title with monospaced font. |
| *BORDER_WITH_TITLE_BOLD* | Display group title with bold font. |
| *BORDER_WITH_TITLE* | Display group title in the border. |

**Return type:** dict{**l**: int, **t**: int, **r**: int, **b**: int}

**Returns:** The space.

### Coordinates Transformation <a id="c4d.gui.GeUserArea-method-Coordinates-Transformation"></a>

#### `GeUserArea.Global2Local(self)` <a id="c4d.gui.GeUserArea.Global2Local"></a>

Transforms global coordinates (relative to the top left corner of the physical window) to local coordinates (relative to the top left corner of the dialog). Result is a dict with member keys *x* and *y* of type *int*.

**Return type:** Optional[Dict[**x**: int, **y**: int]]

**Returns:** The converted coordinates or **None**.

#### `GeUserArea.Local2Global(self)` <a id="c4d.gui.GeUserArea.Local2Global"></a>

Transforms local coordinates (relative to the top left corner of the dialog) to global coordinates (relative to the top left corner of the physical window). Result is a dict with member keys *x* and *y* of type *int*.

**Return type:** Optional[Dict[**x**: int, **y**: int]]

**Returns:** The converted coordinates or **None**.

#### `GeUserArea.Local2Screen(self)` <a id="c4d.gui.GeUserArea.Local2Screen"></a>

Transforms local coordinates (relative to the top left corner of the dialog) to screen coordinates (relative to the top left corner of the system screen). Result is a dict with member keys *x* and *y* of type *int*.

**Return type:** Optional[Dict[**x**: int, **y**: int]]

**Returns:** The converted coordinates or **None**.

#### `GeUserArea.Screen2Local(self)` <a id="c4d.gui.GeUserArea.Screen2Local"></a>

Transforms screen coordinates (relative to the top left corner of the system screen) to local coordinates (relative to the top left corner of the dialog). Result is a dict with member keys *x* and *y* of type *int*.

**Return type:** Optional[Dict[**x**: int, **y**: int]]

**Returns:** The converted coordinates or **None**.

### Dialog Information Methods <a id="c4d.gui.GeUserArea-method-Dialog-Information-Methods"></a>

#### `GeUserArea.GetColorRGBA(self, colorid)` <a id="c4d.gui.GeUserArea.GetColorRGBA"></a>

Gets the RGBA values associated with a color ID.

*New in version 2025.2.0.*

**Parameters:** **colorid** (*int*) – The color ID. See [COLOR constants](../../../consts/COLOR.md).

**Return type:** dict{**r**: int, **g**: int, **b**: int, **a**: int}

**Returns:** The color in the dict with the keys *r*, *g*, *b* and *a*.

### Drag and Drop Methods <a id="c4d.gui.GeUserArea-method-Drag-and-Drop-Methods"></a>

#### `GeUserArea.CheckDropArea(self, msg, horiz, vert)` <a id="c4d.gui.GeUserArea.CheckDropArea"></a>

Checks the drag position in a drag event message against the user area’s position in the layout.

> **Note:** The check can be limited to only X or Y coordinates.

**Parameters:**

- **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The drag message.
- **horiz** (*bool*) – If **True** the drag position is checked against the horizontal bounds of the region.
- **vert** (*bool*) – If **True** the drag position is checked against the vertical bounds of the region.

**Return type:** bool

**Returns:** **True** if the drag message is within the bounds specified, otherwise **False**.

#### `GeUserArea.GetDragObject(self, msg)` <a id="c4d.gui.GeUserArea.GetDragObject"></a>

Extracts the object from a drag and drop message.

**Parameters:** **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The original message.

**Return type:** dict{‘type’: int, ‘object’: any}

**Returns:**

The type of drag and the object itself. The types are:

|   |   |
|---|---|
| *DRAGTYPE_ATOMARRAY* | Atom array. The data is a list of [`c4d.C4DAtom`](../../c4d/C4DAtom/index.md#c4d.C4DAtom). |
| *DRAGTYPE_CMDPALETTE* | Not supported. |
| *DRAGTYPE_COMMAND* | Not supported. |
| *DRAGTYPE_DESCID* | Description ID. The data is a dict(‘did’: [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID), ‘arr’: list of [`c4d.C4DAtom`](../../c4d/C4DAtom/index.md#c4d.C4DAtom)). |
| *DRAGTYPE_ICON* | Not supported. |
| *DRAGTYPE_FILES* | Files. The data is a string with the filename. |
| *DRAGTYPE_FILENAME_IMAGE* | Image. The data is a string with the filename. |
| *DRAGTYPE_FILENAME_OTHER* | Other filename. The data is a string with the filename. |
| *DRAGTYPE_FILENAME_SCENE* | Scene filename. The data is a string with the filename. |
| *DRAGTYPE_MANAGER* | Not supported. |
| *DRAGTYPE_RGB* | RGB color. The data is a [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector). |
| *DRAGTYPE_RGB_ARRAY* | RGB color array. The data is a list of [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector). |
| *DRAGTYPE_RGBA_ARRAY* | RGBA color array. The data is a [`maxon.BaseArray`](../../maxon_generated/datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) of [`maxon.ColorA`](../../maxon_generated/datatypes/vec_col_mat/maxon.ColorA.md#module-maxon.ColorA). |
| *DRAGTYPE_BROWSER* | Browser drag message. The data is a list of string with the filename. |
| *DRAGTYPE_ASSET* | *New in version 2023.2.0:* Message ID for Asset browser assets, the message data is a [`maxon.DragAndDropDataAssetArray`](../../maxon_generated/frameworks/asset/datatype/maxon.DragAndDropDataAssetArray.md#module-maxon.DragAndDropDataAssetArray). Exposed as *maxon.DRAGTYPE_ASSET* in Python. |

#### `GeUserArea.GetDragPosition(self, msg)` <a id="c4d.gui.GeUserArea.GetDragPosition"></a>

Extracts local drag coordinates from a drag and drop event.

**Parameters:** **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The original message.

**Return type:** dict{‘x’: int, ‘y’: int}

**Returns:** The local X and Y position.

#### `GeUserArea.HandleMouseDrag(self, msg, type, data, dragflags)` <a id="c4d.gui.GeUserArea.HandleMouseDrag"></a>

Starts a drag and drop operation.

*New in version R19.024.*

**Parameters:**

- **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The mouse event message that triggered the drag and drop.

- **type** (*int*) –

  The type of *data*:

  |   |   |
  |---|---|
  | *DRAGTYPE_ATOMARRAY* | Atom array. The data is a list of [`c4d.C4DAtom`](../../c4d/C4DAtom/index.md#c4d.C4DAtom). |
  | *DRAGTYPE_CMDPALETTE* | Not supported. |
  | *DRAGTYPE_COMMAND* | Not supported. |
  | *DRAGTYPE_DESCID* | Description ID. The data is a dict(‘did’: [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID), ‘arr’: list of [`c4d.C4DAtom`](../../c4d/C4DAtom/index.md#c4d.C4DAtom)). |
  | *DRAGTYPE_ICON* | Not supported. |
  | *DRAGTYPE_FILES* | Files. The data is a string with the filename. |
  | *DRAGTYPE_FILENAME_IMAGE* | Image. The data is a string with the filename. |
  | *DRAGTYPE_FILENAME_OTHER* | Other filename. The data is a string with the filename. |
  | *DRAGTYPE_FILENAME_SCENE* | Scene filename. The data is a string with the filename. |
  | *DRAGTYPE_MANAGER* | Not supported. |
  | *DRAGTYPE_RGB* | RGB color. The data is a [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector). |
  | *DRAGTYPE_RGB_ARRAY* | RGB color array. The data is a list of [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector). |
  | *DRAGTYPE_RGBA_ARRAY* | RGBA color array. The data is a [`maxon.BaseArray`](../../maxon_generated/datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) of [`maxon.ColorA`](../../maxon_generated/datatypes/vec_col_mat/maxon.ColorA.md#module-maxon.ColorA). |
  | *DRAGTYPE_BROWSER* | Browser drag message. The data is a list of string with the filename. |
  | *DRAGTYPE_ASSET* | *New in version 2023.2.0:* Message ID for Asset browser assets, the message data is a [`maxon.DragAndDropDataAssetArray`](../../maxon_generated/frameworks/asset/datatype/maxon.DragAndDropDataAssetArray.md#module-maxon.DragAndDropDataAssetArray). Exposed as *maxon.DRAGTYPE_ASSET* in Python. |

- **data** (*any*) – Depends on *type*.

- **dragflags** (*int*) – The drag flags. Private.

**Return type:** bool

**Returns:**

**True** if the user moved the mouse and a drag and drop operation was initiated.  
**False** if the user did not move the mouse, so that the original event is a normal mouse click event.

#### `GeUserArea.MouseDrag(self)` <a id="c4d.gui.GeUserArea.MouseDrag"></a>

Polls the mouse during a drag started with [`MouseDragStart()`](#c4d.gui.GeUserArea.MouseDragStart).

The best way to use this function is.

```python
while True:
    result, mx, mx, channels = ua.MouseDrag()
    if result != c4d.MOUSEDRAGRESULT_CONTINUE:
        break
```

To check for qualifiers see the channels container.

```python
if channels[c4d.BFM_INPUT_QUALIFIER] & QSHIFT:
    ...
if channels[c4d.BFM_INPUT_QUALIFIER] & QCTRL:
    ...
```

**Return type:** Tuple[int, float, float, [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)]

**Returns:**

A tuple with the following information:

int: The mouse drag result:

> |   |   |
> |---|---|
> | *MOUSEDRAGRESULT_ESCAPE* | Drag aborted. |
> | *MOUSEDRAGRESULT_FINISHED* | Drag finished. |
> | *MOUSEDRAGRESULT_CONTINUE* | Drag still in progress. |

float: The X delta-coordinate of the mouse (the amount the mouse has moved).  
float: The Y delta-coordinate of the mouse (the amount the mouse has moved).  
[`c4d.BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer): The channels values. Also contains these pen values:

> |   |   |
> |---|---|
> | *PENPRESSURE* | Pressure. |
> | *PENTILT* | Tilt. |
> | *PENROTATION* | Rotation. |
> | *PENDRAWROTATION* | Draw rotation. |
> | *PENDRAWRANDOMNESS* | Draw randomness. |
> | *PENDRAWWHEELROTATION* | Draw wheel rotation. |
> | *PENDRAWWHEELPRESSURE* | Draw wheel pressure. |
> | *PENDRAWDISTANCE* | Draw distance. |
> | *PENFINGERWHEEL* | Finger wheel. |

#### `GeUserArea.MouseDragEnd(self)` <a id="c4d.gui.GeUserArea.MouseDragEnd"></a>

Checks why the mouse drag ended. Allows to perform any undo operations needed if the user canceled the drag.

**Return type:** int

**Returns:**

The mouse drag result:

|   |   |
|---|---|
| *MOUSEDRAGRESULT_ESCAPE* | Drag aborted. |
| *MOUSEDRAGRESULT_FINISHED* | Drag finished. |
| *MOUSEDRAGRESULT_CONTINUE* | Drag still in progress. |

#### `GeUserArea.MouseDragStart(self, button, mx, my, flag)` <a id="c4d.gui.GeUserArea.MouseDragStart"></a>

Starts a mouse drag. Only call this when a mouse down message is received.  
Then repeatedly poll with [`MouseDrag()`](#c4d.gui.GeUserArea.MouseDrag) during the drag.

**Parameters:**

- **button** (*int*) –

  The mouse button that is pressed:

  |   |   |
  |---|---|
  | *BFM_INPUT_MOUSELEFT* | Left mouse button. |
  | *BFM_INPUT_MOUSERIGHT* | Right mouse button. |
  | *BFM_INPUT_MOUSEMIDDLE* | Middle mouse button. |
  | *BFM_INPUT_MOUSEX1* | Fourth mouse button. |
  | *BFM_INPUT_MOUSEX2* | Five mouse button. |
  | *BFM_INPUT_MOUSEWHEEL* | Mouse wheel message. |
  | *BFM_INPUT_MOUSEMOVE* | Mouse move message. |
  | *BFM_INPUT_MOUSEMOVE* | Mouse move message. |
  | *BFM_INPUT_WHEELSCROLL* | **True** for scroll events on a classic wheel mouse.  <br>**False** for everything else (touchpad, magic mouse). |

- **mx** (*float*) – The X position of the mouse.

- **my** (*float*) – The Y position of the mouse.

- **flag** (*int*) –

  The mouse drag flags:

  |   |   |
  |---|---|
  | *MOUSEDRAGFLAGS_NONE* | None. |
  | *MOUSEDRAGFLAGS_DONTHIDEMOUSE* | Show mouse pointer during drag. |
  | *MOUSEDRAGFLAGS_NOMOVE* | *MouseDrag()* returns *MOUSEDRAGRESULT_CONTINUE* even if mouse is not moved. Otherwise *MouseDrag()* only returns if mouse is moved. |
  | *MOUSEDRAGFLAGS_EVERYPACKET* | Receive every packet of the queue, otherwise only data of the last packet. |
  | *MOUSEDRAGFLAGS_COMPENSATEVIEWPORTORG* | Compensates the viewport origin during drag. |
  | *MOUSEDRAGFLAGS_AIRBRUSH* | Airbrush mode. |

#### `GeUserArea.SetDragDestination(self, cursor)` <a id="c4d.gui.GeUserArea.SetDragDestination"></a>

Sets the correct cursor during drag and drop handling.

**Parameters:**

**cursor** (*int*) –

A mouse cursor:

|   |   |
|---|---|
| *MOUSE_HIDE* | Hide cursor. |
| *MOUSE_SHOW* | Show cursor. |
| *MOUSE_NORMAL* | Normal cursor. |
| *MOUSE_BUSY* | Busy cursor. |
| *MOUSE_CROSS* | Cross cursor. |
| *MOUSE_QUESTION* | Question cursor |
| *MOUSE_ZOOM_IN* | Zoom in cursor. |
| *MOUSE_ZOOM_OUT* | Zoom out cursor. |
| *MOUSE_FORBIDDEN* | Forbidden cursor. |
| *MOUSE_DELETE* | Delete cursor. |
| *MOUSE_COPY* | Copy cursor. |
| *MOUSE_INSERTCOPY* | Insert copy cursor. |
| *MOUSE_INSERTCOPYDOWN* | Insert copy down cursor. |
| *MOUSE_MOVE* | Move cursor. |
| *MOUSE_INSERTMOVE* | Insert move cursor. |
| *MOUSE_INSERTMOVEDOWN* | Insert move cursor. |
| *MOUSE_ARROW_H* | Horizontal cursor. |
| *MOUSE_ARROW_V* | Vertical cursor. |
| *MOUSE_ARROW_HV* | Horizontal and vertical arrow cursor. |
| *MOUSE_POINT_HAND* | Point hand cursor. |
| *MOUSE_MOVE_HAND* | Move hand cursor. |
| *MOUSE_IBEAM* | I-beam cursor. |
| *MOUSE_SELECT_LIVE* | Live selection cursor. |
| *MOUSE_SELECT_FREE* | Free selection cursor. |
| *MOUSE_SELECT_RECT* | Rectangle selection cursor. |
| *MOUSE_SELECT_POLY* | Polygon selection cursor. |
| *MOUSE_SPLINETOOLS* | Spline tools cursor. |
| *MOUSE_EXTRUDE* | Extrude cursor. |
| *MOUSE_NORMALMOVE* | Normal move cursor. |
| *MOUSE_ADDPOINTS* | Add points cursor. |
| *MOUSE_ADDPOLYGONS* | Add polygons cursor. |
| *MOUSE_BRIDGE* | Bridge cursor. |
| *MOUSE_MIRROR* | Mirror cursor. |
| *MOUSE_PAINTMOVE* | Paint move cursor. |
| *MOUSE_PAINTSELECTRECT* | Paint select rectangle cursor. |
| *MOUSE_PAINTSELECTCIRCLE* | Paint select circle cursor. |
| *MOUSE_PAINTSELECTPOLY* | Paint select polygon cursor. |
| *MOUSE_PAINTSELECTFREE* | Paint select free cursor. |
| *MOUSE_PAINTMAGICWAND* | Paint magic wand cursor. |
| *MOUSE_PAINTCOLORRANGE* | Paint color range cursor. |
| *MOUSE_PAINTFILL* | Paint fill cursor. |
| *MOUSE_PAINTPICK* | Paint pick cursor. |
| *MOUSE_PAINTBRUSH* | Paint brush cursor. |
| *MOUSE_PAINTCLONE* | Paint clone cursor. |
| *MOUSE_PAINTTEXT* | Paint text cursor. |
| *MOUSE_PAINTCROP* | Paint crop cursor. |
| *MOUSE_PAINTLINE* | Paint line cursor. |
| *MOUSE_PAINTPOLYSHAPE* | Paint polygon shape cursor. |

**Return type:** bool

**Returns:** **True** if the cursor could be set, otherwise **False**.

### Draw Helpers Methods <a id="c4d.gui.GeUserArea-method-Draw-Helpers-Methods"></a>

#### `GeUserArea.ClearClippingRegion(self)` <a id="c4d.gui.GeUserArea.ClearClippingRegion"></a>

Clears any clipping region set with [`SetClippingRegion()`](#c4d.gui.GeUserArea.SetClippingRegion).

#### `GeUserArea.OffScreenOn(self, x=-1, y=0, w=0, h=0)` <a id="c4d.gui.GeUserArea.OffScreenOn"></a>

Enables double buffering to avoid blinking and flickering effects.  
Sets the clipping area to the rectangular area determined by *x*, *y*, *w* and *h*.  
If x == c4d.NOTOK the size will be calculated automatically.

> **Note:** The GUI will automatically switch planes.

> **Note:** Just call this function before drawing things.

**Parameters:**

- **x** (*int*) – X-coordinate of the clipping area.
- **y** (*int*) – Y-coordinate of the clipping area.
- **w** (*int*) – Width of the clipping area.
- **h** (*int*) – Height of the clipping area.

**Return type:** bool

**Returns:** **True** if double buffering could be enabled, otherwise **False**.

#### `GeUserArea.SetClippingRegion(self, x, y, w, h)` <a id="c4d.gui.GeUserArea.SetClippingRegion"></a>

Should be used at the top of the [`DrawMsg()`](#c4d.gui.GeUserArea.DrawMsg) function to specify the clipping region.  
Without specifying a dedicated clipping region everything will be painted, even if it is outside the user area!

> **Note:** The method [`OffScreenOn()`](#c4d.gui.GeUserArea.OffScreenOn) automatically sets the clipping region to the whole user area, so normally this function is not necessary.

**Parameters:**

- **x** (*int*) – X coordinate of the upper left corner of the clipping region.
- **y** (*int*) – Y coordinate of the upper left corner of the clipping region.
- **w** (*int*) – Width of the clipping region.
- **h** (*int*) – Height of the clipping region.

### Draw Methods <a id="c4d.gui.GeUserArea-method-Draw-Methods"></a>

#### `GeUserArea.DrawBezier(self, sx, sy, p, closed, filled)` <a id="c4d.gui.GeUserArea.DrawBezier"></a>

Draws concatenated bezier curves.

*New in version R14.014.*

> **Note:** Due to improve speed performance, the elements of *p* will be modified and might be invalid and all values must be set again if [`DrawBezier()`](#c4d.gui.GeUserArea.DrawBezier) will be called again with the same array.

**Parameters:**

- **sx** (*float*) – X coordinate of the upper left corner of the drawn curve. This is the X coordinate of the starting point.

- **sy** (*float*) – Y coordinate of the upper left corner of the drawn curve. This is the Y coordinate of the starting point.

- **p** (*List*[*float*]) –

  An array with the bezier curves points.

  Here is an example of initializing the curve points array.

  ```python
  points = array.array('f', range(6))

  points[0] = 35  # The X coordinate of the control point for the starting point.
  points[1] = 200 # The Y coordinate of the control point for the starting point.
  points[2] = 220 # The X coordinate of the control point for the ending point.
  points[3] = 260 # The Y coordinate of the control point for the ending point.
  points[4] = 220 # The X coordinate of the ending point.
  points[5] = 40 # The Y coordinate of the ending point.

  self.DrawBezier(120, 160, points, False, False)
  ```

- **closed** (*bool*) – If **True**, the last point of the last segment connects back to the starting point ( *sx* , *sy*).

- **filled** (*bool*) – If **True**, fills the drawn bezier curves, only if it is also *closed*.

#### `GeUserArea.DrawBezierFill(self, startPoint, bezierPoints, closed)` <a id="c4d.gui.GeUserArea.DrawBezierFill"></a>

Draws concatenated Bezier curves.

*New in version R25.010.*

**Parameters:**

- **startPoint** (*List*[*float*]) – The XY coordinate of the upper left corner of the drawn curve. The list should have 2 elements, the first entry is X the second is Y.

- **bezierPoints** (*List*[*float*]) –

  An array containing a struct of Bezier curves points.

  Here is an example of initializing the curve points array.

  > **Note:** To define the line segment, you have to introduce three points, two handle and one end point. Each point is defined by two float, so the length of the bezierPoint should be a multiple of six. Handle’s coordinates must be set within the GeUserArea space coordinate.

  ```python
  points = array.array('f', range(6))

  points[0] = 35  # The X coordinate for the starting point's handle.
  points[1] = 200 # The Y coordinate for the starting point's handle.
  points[2] = 220 # The X coordinate for the ending point's handle.
  points[3] = 260 # The Y coordinate for the ending point's handle.
  points[4] = 220 # The X coordinate of the ending point.
  points[5] = 40 # The Y coordinate of the ending point.

  self.DrawBezierLine(120, 160, points, False, False)
  ```

- **closed** (*bool*) – If **True**, the last point of the last segment connects back to the starting point ( *sx* , *sy*).

#### `GeUserArea.DrawBezierLine(self, startPoint, bezierPoints, closed, lineWidth=1.0, lineStyle=0)` <a id="c4d.gui.GeUserArea.DrawBezierLine"></a>

Draws concatenated Bezier curves.

*New in version R25.010.*

**Parameters:**

- **startPoint** (*List*[*float*]) – The XY coordinate of the upper left corner of the drawn curve. The list should have 2 elements, the first entry is X the second is Y.

- **bezierPoints** (*List*[*float*]) –

  An array containing a struct of Bezier curves points.

  Here is an example of initializing the curve points array.

  > **Note:** To define the line segment, you have to introduce three points, two handle and one end point. Each point is defined by two float, so the length of the bezierPoint should be a multiple of six. Handle’s coordinates must be set within the GeUserArea space coordinate.

  ```python
  points = array.array('f', range(6))

  points[0] = 35  # The X coordinate for the starting point's handle.
  points[1] = 200 # The Y coordinate for the starting point's handle.
  points[2] = 220 # The X coordinate for the ending point's handle.
  points[3] = 260 # The Y coordinate for the ending point's handle.
  points[4] = 220 # The X coordinate of the ending point.
  points[5] = 40 # The Y coordinate of the ending point.

  self.DrawBezierLine(120, 160, points, False, False)
  ```

- **closed** (*bool*) – If **True**, the last point of the last segment connects back to the starting point ( *sx* , *sy*).

- **lineWidth** (*float*) – The width of the Bezier curve.

- **lineStyle** (*int*) –

  The line style of the Bezier curve:

  | Symbol ID |
  |---|
  | *NORMAL* |
  | *DOTTED* |
  | *DASHED* |
  | *DASHED_INV* |
  | *DASHED_BIG* |

#### `GeUserArea.DrawBitmap(self, bmp, wx, wy, ww, wh, x, y, w, h, mode)` <a id="c4d.gui.GeUserArea.DrawBitmap"></a>

Draws a bitmap into the user area.

The region (x, y) to x + w, y + h) from the bitmap will be scaled and transformed into the region (wx, wy) to (wx + ww, wy + wh) of the destination area.

> **Note:** *BMP_ALLOWALPHA* can be combined with the other modes.

**Parameters:**

- **bmp** ([*c4d.bitmaps.BaseBitmap*](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The bitmap to draw.

- **wx** (*int*) – X coordinate of the upper left corner of the destination area.

- **wy** (*int*) – Y coordinate of the upper left corner of the destination area.

- **ww** (*int*) – Width of the destination area.

- **wh** (*int*) – Height of the destination area.

- **x** (*int*) – X coordinate of the upper left corner of the bitmap area.

- **y** (*int*) – Y coordinate of the upper left corner of the bitmap area.

- **w** (*int*) – Width of the bitmap area.

- **h** (*int*) – Height of the bitmap area.

- **mode** (*int*) –

  Can be a combination of the following flags:

  |   |   |
  |---|---|
  | *BMP_NORMAL* | Standard scaling by the operating system. Fast but low quality when using uneven scaling factors. |
  | *BMP_NORMALSCALED* | Scaling with sampling for high quality. Slow. |
  | *BMP_GRAYEDOUT* | *New in version R21:* \| Embosses the bitmap (like the grayed palette icons in Cinema 4D). \| Previously called BMP_EMBOSSED. |
  | *BMP_ALLOWALPHA* | Uses the alpha channel to blend with the current draw color set with `GeUserArea.DrawSetPen()`. |
  | *BMP_APPLY_COLORPROFILE* | Applies the color profile. |
  | *BMP_DIMIMAGE* | Darkens the bitmap (like the activated palette icons in Cinema 4D) |
  | *BMP_MIRROR_H* | Mirrors the bitmap horizontally. |
  | *BMP_MIRROR_H_FORBID* | Does not mirror the bitmap horizontally. |
  | *BMP_MIRROR_V* | Mirrors the bitmap vertically. |
  | *BMP_MIRROR_V_FORBID* | Does not mirror the bitmap vertically. |

#### `GeUserArea.DrawBitmapRounded(self, bmp, wx, wy, ww, wh, x, y, w, h, mode, radius)` <a id="c4d.gui.GeUserArea.DrawBitmapRounded"></a>

Draw a bitmap with rounded edges into the user area.

The region (x, y) to x + w, y + h) from the bitmap will be scaled and transformed into the region (wx, wy) to (wx + ww, wy + wh) of the destination area.

> **Note:** *BMP_ALLOWALPHA* can be combined with the other modes.

**Parameters:**

- **bmp** ([*c4d.bitmaps.BaseBitmap*](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The bitmap to draw.

- **wx** (*int*) – The X coordinate of the upper left corner of the destination area.

- **wy** (*int*) – The Y coordinate of the upper left corner of the destination area.

- **ww** (*int*) – The width of the destination area.

- **wh** (*int*) – The height of the destination area.

- **x** (*int*) – The X coordinate of the upper left corner of the bitmap area.

- **y** (*int*) – The Y coordinate of the upper left corner of the bitmap area.

- **w** (*int*) – The width of the bitmap area.

- **h** (*int*) – The height of the bitmap area.

- **mode** (*int*) –

  Can be a combination of the following flags:

  |   |   |
  |---|---|
  | *BMP_NORMAL* | Standard scaling by the operating system. Fast but low quality when using uneven scaling factors. |
  | *BMP_NORMALSCALED* | Scaling with sampling for high quality. Slow. |
  | *BMP_GRAYEDOUT* | *New in version R21:* \| Embosses the bitmap (like the grayed palette icons in Cinema 4D). \| Previously called BMP_EMBOSSED. |
  | *BMP_ALLOWALPHA* | Uses the alpha channel to blend with the current draw color set with `GeUserArea.DrawSetPen()`. |
  | *BMP_APPLY_COLORPROFILE* | Applies the color profile. |
  | *BMP_DIMIMAGE* | Darkens the bitmap (like the activated palette icons in Cinema 4D) |
  | *BMP_MIRROR_H* | Mirrors the bitmap horizontally. |
  | *BMP_MIRROR_H_FORBID* | Does not mirror the bitmap horizontally. |
  | *BMP_MIRROR_V* | Mirrors the bitmap vertically. |
  | *BMP_MIRROR_V_FORBID* | Does not mirror the bitmap vertically. |

- **radius** (*float*) – The radius of the rounded edge.

#### `GeUserArea.DrawBorder(self, type, x1, y1, x2, y2)` <a id="c4d.gui.GeUserArea.DrawBorder"></a>

Fills a rectangular area with the current pen color between (x1,y1) and (x2,y2).

**Parameters:**

- **type** (*int*) –

  The border type. Possible values:

  |   |   |
  |---|---|
  | *BORDER_NONE* | No border. |
  | *BORDER_THIN_IN* | Thin border inward. |
  | *BORDER_THIN_OUT* | Thin border outward. |
  | *BORDER_IN* | Normal border inward. |
  | *BORDER_OUT* | Normal border outward. |
  | *BORDER_GROUP_IN* | Group border inside. |
  | *BORDER_GROUP_OUT* | Group border outside. |
  | *BORDER_OUT2* | Outward border 2. |
  | *BORDER_OUT3* | Outward border 3 |
  | *BORDER_BLACK* | Thin black line. |
  | *BORDER_ACTIVE_1* | Active border 1. |
  | *BORDER_ACTIVE_2* | Active border 2. |
  | *BORDER_ACTIVE_3* | Active border 3. |
  | *BORDER_ACTIVE_4* | Active border 4. |
  | *BORDER_GROUP_TOP* | Border along the top. |
  | *BORDER_ROUND* | Border with round corners. |
  | *BORDER_SCHEME_EDIT* | Edit field border like the shortcut gadget for example. |
  | *BORDER_SCHEME_EDIT_NUMERIC* | Edit field border that is open to the right like the link field for example. |
  | *BORDER_OUT3l* | Outward border 3, open to the left. |
  | *BORDER_OUT3r* | Outward border 3, open to the right. |
  | *BORDER_THIN_INb* | Thin border inward, open to the botton. |
  | *BORDER_MASK* | Masks out border type. |
  | *BORDER_TEXT_DOTTED* | Only used with `GeDialog.AddStaticText()`.  <br>Draws a dotted line at right of text, useful to visually connect the text with its parameter. |
  | *BORDER_WITH_TITLE_MONO* | Display group title with monospaced font. |
  | *BORDER_WITH_TITLE_BOLD* | Display group title with bold font. |
  | *BORDER_WITH_TITLE* | Display group title in the border. |

- **x1** (*int*) – The X coordinate of the first corner.

- **y1** (*int*) – The Y coordinate of the first corner.

- **x2** (*int*) – The X coordinate of the opposite corner.

- **y2** (*int*) – The Y coordinate of the opposite corner.

#### `GeUserArea.DrawCustomButton(self, x, y, w, h, ids, nofill, focus)` <a id="c4d.gui.GeUserArea.DrawCustomButton"></a>

Draws a button.

*New in version R25.010.*

**Parameters:**

- **x** (*int*) – The X start coordinate.
- **y** (*int*) – The Y start coordinate.
- **w** (*int*) – The button width.
- **h** (*int*) – The button height.
- **ids** (*List*[*int*]) – A list of ids.
- **nofill** (*bool*) – **True** if the button should not be filled, otherwise **False**.
- **focus** (**True** if the button should be drawn as focused, otherwise **False**.) – bool

#### `GeUserArea.DrawEllipseFill(self, centerPoint, radius)` <a id="c4d.gui.GeUserArea.DrawEllipseFill"></a>

Draws an ellipse filled with color.

*New in version R25.010.*

**Parameters:**

- **centerPoint** (*List*[*float*]) – The XY coordinate of the center of the ellipse. The list should have 2 elements, the first entry is X the second is Y.
- **radius** (*List*[*float*]) – The radius of the ellipse. The list should have 2 elements, the first entry correspond respectively to the width and the height of the ellispe.

#### `GeUserArea.DrawEllipseLine(self, centerPoint, radius, lineWidth=1.0, lineStyle=0)` <a id="c4d.gui.GeUserArea.DrawEllipseLine"></a>

Draws an ellipse line.

*New in version R25.010.*

**Parameters:**

- **centerPoint** (*List*[*float*]) – The XY coordinate of the center of the ellipse. The list should have 2 elements, the first entry is X the second is Y.

- **radius** (*List*[*float*]) – The list should have 2 elements, the first entry correspond respectively to the width and the height of the ellispe.

- **lineWidth** (*float*) – The width of the ellipse curve.

- **lineStyle** (*int*) –

  The line style of the ellipse curve:

  | Symbol ID |
  |---|
  | *NORMAL* |
  | *DOTTED* |
  | *DASHED* |
  | *DASHED_INV* |
  | *DASHED_BIG* |

#### `GeUserArea.DrawFrame(self, x1, y1, x2, y2, lineWidth=1.0, lineStyle=0)` <a id="c4d.gui.GeUserArea.DrawFrame"></a>

Draws a rectangular frame with the current pen color between (*x1,y1*) and (*x2,y2*).

**Parameters:**

- **x1** (*int*) – The X start coordinate.

- **y1** (*int*) – The Y start coordinate.

- **x2** (*int*) – The X end coordinate.

- **y2** (*int*) – The Y end coordinate.

- **lineWidth** (*float*) – Line width to draw the line.

- **lineStyle** (*int*) –

  The line style of the Bezier curve:

  | Symbol ID |
  |---|
  | *NORMAL* |
  | *DOTTED* |
  | *DASHED* |
  | *DASHED_INV* |
  | *DASHED_BIG* |

#### `GeUserArea.DrawGetFontBaseLine(self)` <a id="c4d.gui.GeUserArea.DrawGetFontBaseLine"></a>

Returns the base line of the set font.

**Return type:** int

**Returns:** The base line of the set font.

#### `GeUserArea.DrawGetFontHeight(self)` <a id="c4d.gui.GeUserArea.DrawGetFontHeight"></a>

Returns the height in pixels of a line of text in the current font.

**Return type:** int

**Returns:** Height in pixels.

#### `GeUserArea.DrawGetTextIndexFromPixel(self, text, pixelPosition)` <a id="c4d.gui.GeUserArea.DrawGetTextIndexFromPixel"></a>

Retrieves the index from a position within the text.

*New in version 2024.0.0.*

**Parameters:**

- **text** (*str*) – Text to process.
- **pixelPosition** (*float*) – Pixel to examine.

**Return type:** int

**Returns:** Index of the pixel within the text.

#### `GeUserArea.DrawGetTextWidth(self, text)` <a id="c4d.gui.GeUserArea.DrawGetTextWidth"></a>

Returns the width in pixels of the string *text*, if it were drawn in the current font.

**Parameters:** **text** (*str*) – The string to measure.

**Return type:** int

**Returns:** The width in pixels.

#### `GeUserArea.DrawGetTextWidth_ListNodeName(self, node, fontid=1)` <a id="c4d.gui.GeUserArea.DrawGetTextWidth_ListNodeName"></a>

Retrieves the width in pixels of the name of *node*.

**Parameters:**

- **node** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The node to check.

- **fontid** (*int*) –

  The font to use:

  |   |   |
  |---|---|
  | *FONT_DEFAULT* | Default font. |
  | *FONT_STANDARD* | Standard font. |
  | *FONT_BOLD* | Bold font. |
  | *FONT_MONOSPACED* | Monospaced font. |
  | *FONT_BIG* | Big font. |
  | *FONT_BIG_BOLD* | Big Bold font. |
  | *FONT_ITALIC* | Italic font. |

**Return type:** int

**Returns:** The text width in pixels.

#### `GeUserArea.DrawImageRef(self, imageRef, wx, wy, ww, wh, opacity, mode)` <a id="c4d.gui.GeUserArea.DrawImageRef"></a>

Draws a image into the user area.

**Parameters:**

- **imageRef** (`maxon.ImageBaseRef`) – `maxon.ImageRef` to draw.
- **wx** (*int*) – X coordinate of the upper left corner of the destination area.
- **wy** (*int*) – Y coordinate of the upper left corner of the destination area.
- **ww** (*int*) – Width of the destination area.
- **wh** (*int*) – Height of the destination area.
- **opacity** (*float*) – Opacity to draw with (0.0 == completely transparent, 1.0 == fully opaque)
- **mode** (*int*) – `maxon.IMAGEINTERPOLATIONMODE`

#### `GeUserArea.DrawLine(self, x1, y1, x2, y2)` <a id="c4d.gui.GeUserArea.DrawLine"></a>

Draws a line with the current pen color between (*x1,y1*) and (*x2,y2*).

**Parameters:**

- **x1** (*int*) – The X start coordinate.
- **y1** (*int*) – The Y start coordinate.
- **x2** (*int*) – The X end coordinate.
- **y2** (*int*) – The Y end coordinate.

#### `GeUserArea.DrawPolyFill(self, p, closed)` <a id="c4d.gui.GeUserArea.DrawPolyFill"></a>

Draws a polygon filled with color.

*New in version R25.010.*

**Parameters:**

- **p** (*List*[*float*]) –

  The XY coordinate of each vertices of the final polygon.

  > **Note:** Each vertex is defined by 2 float, so the length of *p* should be a multiple of 2 where the first entry is X and the second is Y.

- **closed** (*bool*) – If **True**, the last point of the last segment connects back to the starting point, otherwise **False**.

#### `GeUserArea.DrawPolyLine(self, p, closed, lineWidth=1.0, lineStyle=0)` <a id="c4d.gui.GeUserArea.DrawPolyLine"></a>

Draws a polygon line.

*New in version R25.010.*

**Parameters:**

- **p** (*List*[*float*]) –

  The XY coordinate of each vertices of the final polygon.

  > **Note:** Each vertex is defined by 2 float, so the length of *p* should be a multiple of 2 where the first entry is X and the second is Y.

- **closed** (*bool*) – If **True**, the last point of the last segment connects back to the starting point, otherwise **False**.

- **lineWidth** (*float*) – The width of the polygon curve.

- **lineStyle** (*int*) –

  The line style of the polygon curve:

  | Symbol ID |
  |---|
  | *NORMAL* |
  | *DOTTED* |
  | *DASHED* |
  | *DASHED_INV* |
  | *DASHED_BIG* |

#### `GeUserArea.DrawRectangle(self, x1, y1, x2, y2)` <a id="c4d.gui.GeUserArea.DrawRectangle"></a>

Fills a rectangular area with the current pen color between (x1,y1) and (x2,y2).

**Parameters:**

- **x1** (*int*) – The X coordinate of the first corner.
- **y1** (*int*) – The Y coordinate of the first corner.
- **x2** (*int*) – The X coordinate of the opposite corner.
- **y2** (*int*) – The Y coordinate of the opposite corner.

#### `GeUserArea.DrawRoundedFrame(self, x1, y1, x2, y2, radiusWidth, radiusHeight, lineWidth=1.0, lineStyle=0)` <a id="c4d.gui.GeUserArea.DrawRoundedFrame"></a>

Draws a rectangular frame with the current pen color between (*x1,y1*) and (*x2,y2*).

*New in version 2025.2.0.*

**Parameters:**

- **x1** (*int*) – The X start coordinate.

- **y1** (*int*) – The Y start coordinate.

- **x2** (*int*) – The X end coordinate.

- **y2** (*int*) – The Y end coordinate.

- **radiusWidth** (*float*) – The rounded corner radius width.

- **radiusHeight** (*float*) – The rounded corner radius height.

- **lineWidth** (*float*) – Line width to draw the line.

- **lineStyle** (*int*) –

  The line style of the Bezier curve:

  | Symbol ID |
  |---|
  | *NORMAL* |
  | *DOTTED* |
  | *DASHED* |
  | *DASHED_INV* |
  | *DASHED_BIG* |

#### `GeUserArea.DrawRoundedRectangle(self, x1, y1, x2, y2, radiusWidth, radiusHeight)` <a id="c4d.gui.GeUserArea.DrawRoundedRectangle"></a>

Fills a rectangular area with the current pen color between (x1,y1) and (x2,y2).

*New in version 2025.2.0.*

**Parameters:**

- **x1** (*int*) – The X coordinate of the first corner.
- **y1** (*int*) – The Y coordinate of the first corner.
- **x2** (*int*) – The X coordinate of the opposite corner.
- **y2** (*int*) – The Y coordinate of the opposite corner.
- **radiusWidth** (*float*) – The rounded corner radius width.
- **radiusHeight** (*float*) – The rounded corner radius height.

#### `GeUserArea.DrawSetFont(self, fontid)` <a id="c4d.gui.GeUserArea.DrawSetFont"></a>

Sets the text font.

**Parameters:**

**fontid** (*int*) –

The font to use:

|   |   |
|---|---|
| *FONT_DEFAULT* | Default font. |
| *FONT_STANDARD* | Standard font. |
| *FONT_BOLD* | Bold font. |
| *FONT_MONOSPACED* | Monospaced font. |
| *FONT_BIG* | Big font. |
| *FONT_BIG_BOLD* | Big Bold font. |
| *FONT_ITALIC* | Italic font. |

#### `GeUserArea.DrawSetOpacity(self, opacity)` <a id="c4d.gui.GeUserArea.DrawSetOpacity"></a>

Sets the opacity value.

**Parameters:** **opacity** (*float*) – The opacity to set from 0.0 to 1.0.

#### `GeUserArea.DrawSetPen(self, color)` <a id="c4d.gui.GeUserArea.DrawSetPen"></a>

Sets the draw color.

**Parameters:** **color** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The color to set from 0.0 to 1.0.

#### `GeUserArea.DrawSetTextCol(self, fg, bg)` <a id="c4d.gui.GeUserArea.DrawSetTextCol"></a>

Sets the draw color.

**Parameters:**

- **fg** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – A color vector from 0.0 to 1.0.
- **bg** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – A color vector from 0.0 to 1.0.

#### `GeUserArea.DrawSetTextRotation(self, textrotation)` <a id="c4d.gui.GeUserArea.DrawSetTextRotation"></a>

Rotates the font for drawing.

> **Note:** Rotation is clockwise and must be set to 0 after drawing.

**Parameters:** **textrotation** (*float*) – The text rotation in degree.

#### `GeUserArea.DrawText(self, text, x, y, flags=0)` <a id="c4d.gui.GeUserArea.DrawText"></a>

Draws the string *txt* with the upper left corner at the position (*x*, *y*).

> **Note:** Use [`DrawGetTextWidth()`](#c4d.gui.GeUserArea.DrawGetTextWidth) and [`DrawGetFontHeight()`](#c4d.gui.GeUserArea.DrawGetFontHeight) to find out where to place the text.

**Parameters:**

- **text** (*str*) – The string to draw.
- **x** (*int*) – X coordinate of the upper left corner of the drawn text.
- **y** (*int*) – Y coordinate of the upper left corner of the drawn text.
- **flags** (*int*) – Flags.

#### `GeUserArea.FillBitmapBackground(self, bmp, offsetx, offsety)` <a id="c4d.gui.GeUserArea.FillBitmapBackground"></a>

Fills the bitmap *bmp* with the current pen color.  
The *offsetx* and *offsety* parameters are used when the background is a pattern and are given in local coordinates of the user area.

> **Note:** This can be used to make semi-transparent bitmap blits.

**Parameters:**

- **bmp** ([*c4d.bitmaps.BaseBitmap*](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The bitmap to fill.
- **offsetx** (*int*) – The X offset in pixels.
- **offsety** (*int*) – The X offset in pixels.

#### `GeUserArea.GetColorRGB(self, colorid)` <a id="c4d.gui.GeUserArea.GetColorRGB"></a>

Gets the RGB values associated with a color ID.

**Parameters:** **colorid** (*int*) – The color ID. See [COLOR constants](../../../consts/COLOR.md).

**Return type:** dict{**r**: int, **g**: int, **b**: int}

**Returns:** The color from 0 to 255 in the dict with the keys *r*, *g* and *b*.

### Fading Methods <a id="c4d.gui.GeUserArea-method-Fading-Methods"></a>

#### `GeUserArea.ActivateFading(self, milliseconds)` <a id="c4d.gui.GeUserArea.ActivateFading"></a>

Activates the fading.

*New in version R14.014.*

**Parameters:** **milliseconds** (*int*) – Time for the fading.

#### `GeUserArea.AdjustColor(self, colorid, highlightid, percent)` <a id="c4d.gui.GeUserArea.AdjustColor"></a>

Sets the blend colors for user area fading.

*New in version R14.014.*

**Parameters:**

- **colorid** (*int*) – A color ID to fade from. See [COLOR constants](../../../consts/COLOR.md).
- **highlightid** (*int*) – A color ID to fade to. See [COLOR constants](../../../consts/COLOR.md).
- **percent** (*float*) – Fading percentage.

### Inputs Methods <a id="c4d.gui.GeUserArea-method-Inputs-Methods"></a>

#### `GeUserArea.GetInputEvent(self, askdevice, res)` <a id="c4d.gui.GeUserArea.GetInputEvent"></a>

Gets the next input event for a certain device from the event queue.

**Parameters:**

- **askdevice** (*int*) – The device to ask. Either **BFM_INPUT_MOUSE** or **BFM_INPUT_KEYBOARD**.
- **res** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The result container.

**Return type:** bool

**Returns:** **True** if the event could be retrieved in *res*, otherwise **False**.

#### `GeUserArea.GetInputState(self, askdevice, askchannel, res)` <a id="c4d.gui.GeUserArea.GetInputState"></a>

Polls a certain channel of a device for the current input state.

**Parameters:**

- **askdevice** (*int*) – The device to ask. Either **BFM_INPUT_MOUSE** or **BFM_INPUT_KEYBOARD**.
- **askchannel** (*int*) – The channel to ask.
- **res** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The result container.

**Return type:** bool

**Returns:** **True** if the state could be retrieved in *res*, otherwise **False**.

#### `GeUserArea.IsHotkeyDown(self, id)` <a id="c4d.gui.GeUserArea.IsHotkeyDown"></a>

Checks the standard navigation hotkeys.

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

**Return type:** int

**Returns:**

A value != 0 if the hotkey is pressed.

|   |   |
|---|---|
| *HOTKEYFLAGS_NONE* | Nothing was used. |
| *HOTKEYFLAGS_MOUSE* | Mouse was used. |
| *HOTKEYFLAGS_KEYBOARD* | Keyboard was used. |

#### `GeUserArea.KillEvents(self)` <a id="c4d.gui.GeUserArea.KillEvents"></a>

Flushes all events from the window message queue.

> **Note:** For example if you loop while the mouse is down (polling) you can call this command to flush all keydowns/mouseclicks that are made during the loop.

### Magic Methods <a id="c4d.gui.GeUserArea-method-Magic-Methods"></a>

#### `GeUserArea.__init__(self)` <a id="c4d.gui.GeUserArea.__init__"></a>

Creates a user area that is not attached to any dialog.

> **Note:** The user area must be attached to a dialog with `GeDialog.AttachUserArea()` before it can be used.

### Methods to Override <a id="c4d.gui.GeUserArea-method-Methods-to-Override"></a>

#### `GeUserArea.CoreMessage(self, id, msg)` <a id="c4d.gui.GeUserArea.CoreMessage"></a>

Called when a Cinema 4D core messages is received.  
The message type is given by *id* and the message information is stored in *msg*.

**Parameters:**

- **id** (*int*) – The received *core message\<MSG_CORE_EVENT>*.
- **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The message container.

**Return type:** bool

**Returns:** Currently not used - but you have to return a bool value.

#### `GeUserArea.DrawMsg(self, x1, y1, x2, y2, msg)` <a id="c4d.gui.GeUserArea.DrawMsg"></a>

Called when Cinema 4D wants you to draw your userarea.  
Use the drawing functions to update your user area in the region specified by the rectangle from (x1,y1) to (x2,y2).

**Parameters:**

- **x1** (*int*) – The upper left x coordinate.
- **y1** (*int*) – The upper left y coordinate.
- **x2** (*int*) – The lower right x coordinate.
- **y2** (*int*) – The lower right y coordinate.
- **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – A mesage container.

#### `GeUserArea.GetMinSize(self)` <a id="c4d.gui.GeUserArea.GetMinSize"></a>

Override this function to specify a minimum size for the user area.

```python
def GetMinSize(self):
    #do a calculation here
    return self.width, self.height
```

**Return type:** Tuple[int, int]

**Returns:** A tuple with two elements just like this.

#### `GeUserArea.Init(self)` <a id="c4d.gui.GeUserArea.Init"></a>

Called once when the user area is initialized by the GUI, before the layout is calculated.  
Override this function if you need to initialize anything.

> **Note:** Return **True** if successful, or **False** to signalize an error.

**Return type:** bool

**Returns:** **True** if successful, or **False** to signalize an error.

#### `GeUserArea.InitValues(self)` <a id="c4d.gui.GeUserArea.InitValues"></a>

Called after the layout is calculated, before the user area is drawn.  
Override this function if you need to initialize anything.

> **Note:** Return **True** if successful, or **False** to signalize an error.

**Return type:** bool

**Returns:** **True** if successful, or **False** to signalize an error.

#### `GeUserArea.InputEvent(self, msg)` <a id="c4d.gui.GeUserArea.InputEvent"></a>

Called when an input event is received.  
The information about the input event is stored in the *msg* container.

**Parameters:** **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The event container.

**Return type:** bool

**Returns:** **True** if the event was handled, otherwise **False**.

#### `GeUserArea.Message(self, msg, result)` <a id="c4d.gui.GeUserArea.Message"></a>

Override this function to react to more messages than covered by the other functions. Normally this is not necessary.

> **Note:** If overridden, include a call to the base version of this function, `GeUserArea.Message()`:
>
> ```python
> def Message(self, msg, result):
>     if msg.GetId():
>         #Do something
>         return True
>
>     return c4d.gui.GeUserArea.Message(self, msg, result)
> ```

> **See also:** [C4DAtom and Plugin Messages](../../../consts/MSG_C4DATOM_PLUGINS.md) for information on the messages type, data and input/output.

**Parameters:**

- **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The message container.
- **result** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – A container to store results in.

**Return type:** int

**Returns:** The return value depends on the message.

#### `GeUserArea.Sized(self, w, h)` <a id="c4d.gui.GeUserArea.Sized"></a>

Called when the user area is resized.

> **Note:** Override if you need to update anything.

**Parameters:**

- **w** (*int*) – The new width in pixels.
- **h** (*int*) – The new height in pixels.

#### `GeUserArea.Timer(self, msg)` <a id="c4d.gui.GeUserArea.Timer"></a>

If you subscribe to timer events using [`SetTimer()`](#c4d.gui.GeUserArea.SetTimer) (x), this function is called every *x* th millisecond.  
The raw timer message is stored in *msg*.

**Parameters:** **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The timer message container.

### Miscellaneous <a id="c4d.gui.GeUserArea-method-Miscellaneous"></a>

#### `GeUserArea.GetPixelRatio(self)` <a id="c4d.gui.GeUserArea.GetPixelRatio"></a>

Always returns 1.0 except for user areas shown on OS X Retina displays, where it returns 2.0.

**Returns:** Always 1.0 except for user areas shown on OS X Retina displays.

**Return type:** float

#### `GeUserArea.ScrollArea(self, xdiff, ydiff, x, y, w, h)` <a id="c4d.gui.GeUserArea.ScrollArea"></a>

Scrolls the area from *(x,y)* to *(x+w,y+h)* in the direction specified by *xdiff* and *ydiff*.

**Parameters:**

- **xdiff** (*int*) – X distance to scroll.
- **ydiff** (*int*) – Y distance to scroll.
- **x** (*int*) – X coordinate of the upper left corner of the area to scroll.
- **y** (*int*) – Y coordinate of the upper left corner of the area to scroll.
- **w** (*int*) – Width of the area to scroll.
- **h** (*int*) – Height of the area to scroll.

### Parent Dialog <a id="c4d.gui.GeUserArea-method-Parent-Dialog"></a>

#### `GeUserArea.GetDialog(self)` <a id="c4d.gui.GeUserArea.GetDialog"></a>

Gets the user area’s parent dialog.

> **Warning:** Only works if the parent dialog is a Python dialog.

**Return type:** [c4d.gui.GeDialog](../GeDialog/index.md#c4d.gui.GeDialog)

**Returns:** The user area’s parent dialog.
