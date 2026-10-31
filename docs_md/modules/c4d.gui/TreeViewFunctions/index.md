<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.gui/TreeViewFunctions/index.html -->

# c4d.gui.TreeViewFunctions <a id="c4d-gui-treeviewfunctions"></a>

## *class* `c4d.gui.TreeViewFunctions` <a id="c4d.gui.TreeViewFunctions"></a>

Inherit this class to supply a data and view model for [`c4d.gui.TreeViewCustomGui`](../BaseCustomGui/TreeViewCustomGui/index.md#c4d.gui.TreeViewCustomGui).  
Create an instance of the implemented class and pass it to `TreeViewCustomGui.SetRoot()`.

<a id="drawinfo-dict"></a>**DrawInfo Dict**

|   |   |   |
|---|---|---|
| *bgCol* | int or [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector) | The background color ID or vector. |
| *frame* | [`c4d.gui.GeUserArea`](../GeUserArea/index.md#c4d.gui.GeUserArea) | The user area to draw in. |
| *xpos* | int | The position X coordinate. |
| *ypos* | int | The position Y coordinate. |
| *width* | int | The width. |
| *height* | int | The height. |
| *line* | int | The line. |
| *col* | int | The column. |

<a id="mouseinfo-dict"></a>**MouseInfo Dict**

|   |   |   |
|---|---|---|
| *mx* | float | The mouse X coordinate. |
| *my* | float | The mouse Y coordinate. |
| *button* | int | The mouse button:<br>> \|   \|   \|<br>> \|---\|---\|<br>> \| *MOUSEINFO_BUTTON_LEFT* \| Left button. \|<br>> \| *MOUSEINFO_BUTTON_RIGHT* \| Right button. \|<br>> \| *MOUSEINFO_BUTTON_MIDDLE* \| Middle button. \| |
| *mxRelative* | float | The mouse position relative to the end of the horizontal tree lines.  <br>Usually mouse coordinates are in list view space.  <br>This can become difficult when the user clicks into the **LV_USERTREE** column, hence this member. |
| *startDrag* | bool | Not used. |
| *startpaint* | bool | This is needed in the Layer Manager. The user can change the state of the column by clicking somewhere and dragging the mouse.  <br>To start this drag, set *startpaint* to **True** in `TreeViewFunctions.MouseDown()`. |
| *inpaint* | bool | This is needed in the Layer Manager. The user can change the state of the column by clicking somewhere and dragging the mouse.  <br>`TreeViewFunctions.MouseDown()` will be called for each line with *inpaint* set to **True**. |
| *inputmsg* | [`c4d.BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer) | The container originally sent to the `GeUserArea.InputEvent()` of the tree view’s user area. Never **None**. |
| *frame* | [`c4d.gui.GeUserArea`](../GeUserArea/index.md#c4d.gui.GeUserArea) | The user area to draw in. |
| *xpos* | int | The position X coordinate. |
| *ypos* | int | The position Y coordinate. |
| *width* | int | The width. |
| *height* | int | The height. |
| *line* | int | The line. |
| *col* | int | The column. |

<a id="treeviewfloatsliderinfo-dict"></a>**TreeViewFloatSliderInfo Dict**

| Key | Value Type | Description |
|---|---|---|
| value | float | The current value for the entry. |
| minValue | float | The minimum range of the slider as drawn. |
| maxValue | float | The maximum range of the slider as drawn. |
| minNominalValue | float | The minimum range of the slider should the user drag the value out of bounds to re-size the slider range extents. |
| maxNominalValue | float | The maximum range of the slider should the user drag the value out of bounds to re-size the slider range extents. |
| increment | float | The increment used for vertical modification. |
| floatFormat | int | The format one of the following FORMAT_PERCENT, FORMAT_DEGREE, FORMAT_FLOAT, FORMAT_METER. |
| state | int | Set to the current state of the slider. |
| unit | int | The sliders unit. |

<a id="treeviewdropdownmenuinfo-dict"></a>**TreeViewDropDownMenuInfo Dict**

| Key | Value Type | Description |
|---|---|---|
| entry | int | The selected entry. |
| menu | c4d.BaseContainer | The menu itself described by id : string(name). |
| state | int | Set to the current state of the dropdown. |

## Overview <a id="overview"></a>

**Check**

- [`TreeViewFunctions.IsChecked()`](#c4d.gui.TreeViewFunctions.IsChecked): Called to retrieve the checkbox status of object *obj* for column *lColumn*.
- [`TreeViewFunctions.SetCheck()`](#c4d.gui.TreeViewFunctions.SetCheck): Called to set the checkbox status of object *obj*.

**Context Menu**

- [`TreeViewFunctions.ContextMenuCall()`](#c4d.gui.TreeViewFunctions.ContextMenuCall): Called by a command in the context menu setup in `CreateContextMenu()`.
- [`TreeViewFunctions.CreateContextMenu()`](#c4d.gui.TreeViewFunctions.CreateContextMenu): Called to build a context menu for object *obj* and column *lColumn*.

**Drag**

- [`TreeViewFunctions.AcceptDragObject()`](#c4d.gui.TreeViewFunctions.AcceptDragObject): Called to check if object *obj* can accept the specified drag-and-drop action, and in that case what the result would be.
- [`TreeViewFunctions.DragStart()`](#c4d.gui.TreeViewFunctions.DragStart): Called to determine if object *obj* can be dragged or not and if dragged objects will be selected or not.
- [`TreeViewFunctions.GenerateDragArray()`](#c4d.gui.TreeViewFunctions.GenerateDragArray): Called to generate a drag array for object *obj*.
- [`TreeViewFunctions.GetDragType()`](#c4d.gui.TreeViewFunctions.GetDragType): Called to retrieve the drag type of object *obj*, i.e.
- [`TreeViewFunctions.SetDragObject()`](#c4d.gui.TreeViewFunctions.SetDragObject): Called to set the drag object to *obj*.

**Draw**

- [`TreeViewFunctions.DrawCell()`](#c4d.gui.TreeViewFunctions.DrawCell): Called to draw the cell for object *obj* in column *col* into the user *area* in *drawinfo[‘frame’]*.
- [`TreeViewFunctions.DrawHeaderCell()`](#c4d.gui.TreeViewFunctions.DrawHeaderCell): Called to draw the header for column *col* into the user *area* in *drawinfo[‘frame’]*.

**Drop Down Menu**

- [`TreeViewFunctions.GetDropDownMenu()`](#c4d.gui.TreeViewFunctions.GetDropDownMenu): Gets a drop down menu and it’s current selected entry.
- [`TreeViewFunctions.SetDropDownMenu()`](#c4d.gui.TreeViewFunctions.SetDropDownMenu): Called to set the current menu entry by e.g.

**Float Slider**

- [`TreeViewFunctions.GetFloatValue()`](#c4d.gui.TreeViewFunctions.GetFloatValue): Called to retrieve the current value of a float slider.
- [`TreeViewFunctions.SetFloatValue()`](#c4d.gui.TreeViewFunctions.SetFloatValue): Called when a new value of a float slider has been set.

**Header/Column**

- [`TreeViewFunctions.GetHeaderSortArrow()`](#c4d.gui.TreeViewFunctions.GetHeaderSortArrow): Called to retrieve the sort mode of column *lColID*.
- [`TreeViewFunctions.IsMoveColAllowed()`](#c4d.gui.TreeViewFunctions.IsMoveColAllowed): Called to check if column *lColID* can be moved or not.
- [`TreeViewFunctions.IsResizeColAllowed()`](#c4d.gui.TreeViewFunctions.IsResizeColAllowed): Called to check if column *lColID* can be resized or not.

**ID**

- [`TreeViewFunctions.GetId()`](#c4d.gui.TreeViewFunctions.GetId): Called to retrieve the ID of object *obj*.

**Input Events**

- [`TreeViewFunctions.DeletePressed()`](#c4d.gui.TreeViewFunctions.DeletePressed): Called when a delete event is received.
- [`TreeViewFunctions.DoubleClick()`](#c4d.gui.TreeViewFunctions.DoubleClick): Called when a mouse double click event is received.
- [`TreeViewFunctions.FinishInput()`](#c4d.gui.TreeViewFunctions.FinishInput): Called at the end of the complete input handling.
- [`TreeViewFunctions.HeaderClick()`](#c4d.gui.TreeViewFunctions.HeaderClick): Called when a header has been clicked.
- [`TreeViewFunctions.InputEvent()`](#c4d.gui.TreeViewFunctions.InputEvent): Called when an input event is received.
- [`TreeViewFunctions.MouseDown()`](#c4d.gui.TreeViewFunctions.MouseDown): Called when a mouse down event is received.
- [`TreeViewFunctions.StartInput()`](#c4d.gui.TreeViewFunctions.StartInput): Called before input loop starts.

**Insert Object**

- [`TreeViewFunctions.InsertObject()`](#c4d.gui.TreeViewFunctions.InsertObject): Called to insert *dragobject* as specified.

**Layout**

- [`TreeViewFunctions.GetBackgroundColor()`](#c4d.gui.TreeViewFunctions.GetBackgroundColor): Called to specify the background color of *line*.
- [`TreeViewFunctions.GetColors()`](#c4d.gui.TreeViewFunctions.GetColors): Called to specify the text colors of object *obj*.
- [`TreeViewFunctions.GetColumnWidth()`](#c4d.gui.TreeViewFunctions.GetColumnWidth): Called to retrieve the column width of object *obj* in column *col*.
- [`TreeViewFunctions.GetHeaderColumnWidth()`](#c4d.gui.TreeViewFunctions.GetHeaderColumnWidth): Called to retrieve the width of the header for column *col*.
- [`TreeViewFunctions.GetLineHeight()`](#c4d.gui.TreeViewFunctions.GetLineHeight): Called to retrieve the line height of object *obj* in column *col*.
- [`TreeViewFunctions.GetMinHeaderHeight()`](#c4d.gui.TreeViewFunctions.GetMinHeaderHeight): Called to retrieve the minimum header height.

**Name and Bubble help**

- [`TreeViewFunctions.EmptyText()`](#c4d.gui.TreeViewFunctions.EmptyText): Called to requests the text to display when the treeview area is completely empty such as “Drag falloff object’s here”
- [`TreeViewFunctions.GetBubbleHelp()`](#c4d.gui.TreeViewFunctions.GetBubbleHelp): Called to retrieve the bubble help of object.
- [`TreeViewFunctions.GetName()`](#c4d.gui.TreeViewFunctions.GetName): Called to retrieve the name of object *obj*.
- [`TreeViewFunctions.GetNameForEdit()`](#c4d.gui.TreeViewFunctions.GetNameForEdit): Called to retrieve the name of object obj for display in the edit text box.
- [`TreeViewFunctions.SetName()`](#c4d.gui.TreeViewFunctions.SetName): Called to set the name of object *obj*.

**Navigation**

- [`TreeViewFunctions.GetDown()`](#c4d.gui.TreeViewFunctions.GetDown): Called to retrieve the first child of *obj*.
- [`TreeViewFunctions.GetFirst()`](#c4d.gui.TreeViewFunctions.GetFirst): Called to retrieve the first object of the tree.
- [`TreeViewFunctions.GetNext()`](#c4d.gui.TreeViewFunctions.GetNext): Called to retrieve the object after *obj*.
- [`TreeViewFunctions.GetPred()`](#c4d.gui.TreeViewFunctions.GetPred): Called to retrieve the object before *obj*.

**Notifications**

- [`TreeViewFunctions.AddRow()`](#c4d.gui.TreeViewFunctions.AddRow): Called when a requests to add a row to the treeview.
- [`TreeViewFunctions.ColumnMoved()`](#c4d.gui.TreeViewFunctions.ColumnMoved): Called when a column has been moved.
- [`TreeViewFunctions.PaintFinished()`](#c4d.gui.TreeViewFunctions.PaintFinished): Called when a paint selection has been performed in the tree view.
- [`TreeViewFunctions.Scrolled()`](#c4d.gui.TreeViewFunctions.Scrolled): Called when the tree view has been scrolled.
- [`TreeViewFunctions.SelectionChanged()`](#c4d.gui.TreeViewFunctions.SelectionChanged): Called when selection has changed.

**Open**

- [`TreeViewFunctions.IsOpened()`](#c4d.gui.TreeViewFunctions.IsOpened): Called to retrieve the folding status of object *obj*.
- [`TreeViewFunctions.Open()`](#c4d.gui.TreeViewFunctions.Open): Called to open or close object *obj*.

**Select**

- [`TreeViewFunctions.IsSelectable()`](#c4d.gui.TreeViewFunctions.IsSelectable): Checks if the object is selectable, used to determine if the object should be skipped (not selectable) or not (selectable) when changing selection with keyboard (Up/Down/Home/End keys).
- [`TreeViewFunctions.IsSelected()`](#c4d.gui.TreeViewFunctions.IsSelected): Called to retrieve the selection status of object *obj*.
- [`TreeViewFunctions.Select()`](#c4d.gui.TreeViewFunctions.Select): Called to select object *obj*.

**Tristate**

- [`TreeViewFunctions.IsTristate()`](#c4d.gui.TreeViewFunctions.IsTristate): Called to retrieve the tristate flag of the tree.

## Members <a id="members"></a>

### Check <a id="c4d.gui.TreeViewFunctions-method-Check"></a>

#### `TreeViewFunctions.IsChecked(self, root, userdata, obj, lColumn)` <a id="c4d.gui.TreeViewFunctions.IsChecked"></a>

Called to retrieve the checkbox status of object *obj* for column *lColumn*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **lColumn** (*int*) – The column index.

**Return type:** int

**Returns:**

A combination of the following flags or **c4d.NOTOK** to show no checkbox:

|   |   |
|---|---|
| *LV_CHECKBOX_ENABLED* | Checkbox is enabled. |
| *LV_CHECKBOX_CHECKED* | Checkbox is checked. |
| *LV_CHECKBOX_TRISTATE* | Checkbox tristate. |
| *LV_CHECKBOX_HIDE* | Checkbox is hidden. |

#### `TreeViewFunctions.SetCheck(self, root, userdata, obj, lColumn, bCheck, bcMsg)` <a id="c4d.gui.TreeViewFunctions.SetCheck"></a>

Called to set the checkbox status of object *obj*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **lColumn** (*int*) – The column index.
- **bCheck** (*bool*) – **True** if the checkbox should be checked, otherwise **False**.
- **bcMsg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The container originally sent to the `GeUserArea.InputEvent()` of the tree view’s user area.

### Context Menu <a id="c4d.gui.TreeViewFunctions-method-Context-Menu"></a>

#### `TreeViewFunctions.ContextMenuCall(self, root, userdata, obj, lColumn, lCommand)` <a id="c4d.gui.TreeViewFunctions.ContextMenuCall"></a>

Called by a command in the context menu setup in [`CreateContextMenu()`](#c4d.gui.TreeViewFunctions.CreateContextMenu).

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **lColumn** (*int*) – The column index.
- **lCommand** (*int*) – The menu command ID.

**Return type:** bool

**Returns:** **True** if the command has been processed and the data needs to be updated, otherwise **False**.

#### `TreeViewFunctions.CreateContextMenu(self, root, userdata, obj, lColumn, bc)` <a id="c4d.gui.TreeViewFunctions.CreateContextMenu"></a>

Called to build a context menu for object *obj* and column *lColumn*.

> **See also:** [`c4d.gui.ShowPopupDialog()`](../index.md#c4d.gui.ShowPopupDialog) for the format.

> **Note:**
>
> *bc* container already contains 2 default items: **c4d.ID_TREEVIEW_CONTEXT_REMOVE** and **c4d.ID_TREEVIEW_CONTEXT_RESET**. These may be removed.  
> The added menu entry IDs must be larger than **c4d.ID_TREEVIEW_FIRST_NEW_ID**.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **lColumn** (*int*) – The column index.
- **bc** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Add context menu entries to this container.

### Drag <a id="c4d.gui.TreeViewFunctions-method-Drag"></a>

#### `TreeViewFunctions.AcceptDragObject(self, root, userdata, obj, dragtype, dragobject)` <a id="c4d.gui.TreeViewFunctions.AcceptDragObject"></a>

Called to check if object *obj* can accept the specified drag-and-drop action, and in that case what the result would be.

> **Note:** If *obj* is **None** then *dragobject* should be inserted as a child of the root.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.

- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.

- **obj** (*Optional*[*any*]) – An object in the tree.

- **dragtype** (*int*) –

  The drag type:

  > |   |   |
  > |---|---|
  > | *DRAGTYPE_ATOMARRAY* | Atom array. The data is a list of [`c4d.C4DAtom`](../../c4d/C4DAtom/index.md#c4d.C4DAtom). |
  > | *DRAGTYPE_CMDPALETTE* | Not supported. |
  > | *DRAGTYPE_COMMAND* | Not supported. |
  > | *DRAGTYPE_DESCID* | Description ID. The data is a dict(‘did’: [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID), ‘arr’: list of [`c4d.C4DAtom`](../../c4d/C4DAtom/index.md#c4d.C4DAtom)). |
  > | *DRAGTYPE_ICON* | Not supported. |
  > | *DRAGTYPE_FILES* | Files. The data is a string with the filename. |
  > | *DRAGTYPE_FILENAME_IMAGE* | Image. The data is a string with the filename. |
  > | *DRAGTYPE_FILENAME_OTHER* | Other filename. The data is a string with the filename. |
  > | *DRAGTYPE_FILENAME_SCENE* | Scene filename. The data is a string with the filename. |
  > | *DRAGTYPE_MANAGER* | Not supported. |
  > | *DRAGTYPE_RGB* | RGB color. The data is a [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector). |
  > | *DRAGTYPE_RGB_ARRAY* | RGB color array. The data is a list of [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector). |
  > | *DRAGTYPE_RGBA_ARRAY* | RGBA color array. The data is a [`maxon.BaseArray`](../../maxon_generated/datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) of [`maxon.ColorA`](../../maxon_generated/datatypes/vec_col_mat/maxon.ColorA.md#module-maxon.ColorA). |
  > | *DRAGTYPE_BROWSER* | Browser drag message. The data is a list of string with the filename. |
  > | *DRAGTYPE_ASSET* | *New in version 2023.2.0:* Message ID for Asset browser assets, the message data is a [`maxon.DragAndDropDataAssetArray`](../../maxon_generated/frameworks/asset/datatype/maxon.DragAndDropDataAssetArray.md#module-maxon.DragAndDropDataAssetArray). Exposed as *maxon.DRAGTYPE_ASSET* in Python. |

- **dragobject** (*any*) – The drag object.

**Return type:** Tuple[int, bool]

**Returns:**

A tuple with the following information:

- int: The insert mode:

  > |   |   |
  > |---|---|
  > | *INSERT_BEFORE* | Insert before. |
  > | *INSERT_AFTER* | Insert after. |
  > | *INSERT_UNDER* | Insert under. |
  > | *INSERT_REPLACE* | Replace the object. |
  >
  > > **Note:** The **ACCEPT_DRAG_OBJECT_FORCE_COPY** bit flag can be used together with the **INSERT** constants.

- bool: **True** if copying is allowed to this position, otherwise **False**.

#### `TreeViewFunctions.DragStart(self, root, userdata, obj)` <a id="c4d.gui.TreeViewFunctions.DragStart"></a>

Called to determine if object *obj* can be dragged or not and if dragged objects will be selected or not.

*New in version R19.024.*

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.

**Return type:** int

**Returns:**

A combination of the following flags:

|   |   |
|---|---|
| *TREEVIEW_DRAGSTART_ALLOW* | Allow dragging. |
| *TREEVIEW_DRAGSTART_SELECT* | Select the picked object. |

#### `TreeViewFunctions.GenerateDragArray(self, root, userdata, obj)` <a id="c4d.gui.TreeViewFunctions.GenerateDragArray"></a>

Called to generate a drag array for object *obj*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.

**Return type:** List[[c4d.C4DAtom](../../c4d/C4DAtom/index.md#c4d.C4DAtom)]

**Returns:** The drag objects for *obj*.

#### `TreeViewFunctions.GetDragType(self, root, userdata, obj)` <a id="c4d.gui.TreeViewFunctions.GetDragType"></a>

Called to retrieve the drag type of object *obj*, i.e. the type that the user would get if he started a drag in that cell.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.

**Return type:** int

**Returns:**

The object drag type, or **c4d.NOTOK** to disable drag-and-drop:

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

#### `TreeViewFunctions.SetDragObject(self, root, userdata, obj)` <a id="c4d.gui.TreeViewFunctions.SetDragObject"></a>

Called to set the drag object to *obj*.

*New in version R19.024.*

> **Note:**
>
> Helps to determine if dragging happens internally (rearranged items) or externally (dragged items from another treeview for instance).  
> To check this, store the drag object data and compare it with *dragobject* in [`InsertObject()`](#c4d.gui.TreeViewFunctions.InsertObject).

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – The drag object on drag start.

### Draw <a id="c4d.gui.TreeViewFunctions-method-Draw"></a>

#### `TreeViewFunctions.DrawCell(self, root, userdata, obj, col, drawinfo, bgcolor)` <a id="c4d.gui.TreeViewFunctions.DrawCell"></a>

Called to draw the cell for object *obj* in column *col* into the user *area* in *drawinfo[‘frame’]*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **col** (*int*) – The column index.
- **drawinfo** (*dict*) – The draw information. See [DrawInfo Dict](#drawinfo-dict).
- **bgcolor** (int or [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector)) – The background color.

**Return type:** int or [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The background color as color ID or vector.

#### `TreeViewFunctions.DrawHeaderCell(self, root, userdata, col, drawinfo)` <a id="c4d.gui.TreeViewFunctions.DrawHeaderCell"></a>

Called to draw the header for column *col* into the user *area* in *drawinfo[‘frame’]*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **col** (*int*) – The column index.
- **drawinfo** (*dict*) – The draw information. See [DrawInfo Dict](#drawinfo-dict).

**Return type:** bool

**Returns:** **True** if the header has been drawn or **False** if the header should be drawn by the tree view.

### Drop Down Menu <a id="c4d.gui.TreeViewFunctions-method-Drop-Down-Menu"></a>

#### `TreeViewFunctions.GetDropDownMenu(self, root, userdata, obj, lColumn, menuInfo)` <a id="c4d.gui.TreeViewFunctions.GetDropDownMenu"></a>

Gets a drop down menu and it’s current selected entry.

*New in version 25.*

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **lColumn** (*int*) – The column index.
- **menuInfo** (The menu information. See [TreeViewDropDownMenuInfo Dict](#treeviewdropdownmenuinfo-dict).) – dict

#### `TreeViewFunctions.SetDropDownMenu(self, root, userdata, obj, lColumn, entry)` <a id="c4d.gui.TreeViewFunctions.SetDropDownMenu"></a>

Called to set the current menu entry by e.g. user interaction.

*New in version 25.*

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **lColumn** (*int*) – The column index.
- **entry** (*The entry that the user has picked.*) – int

### Float Slider <a id="c4d.gui.TreeViewFunctions-method-Float-Slider"></a>

#### `TreeViewFunctions.GetFloatValue(self, root, userdata, obj, lColumn, sliderInfo)` <a id="c4d.gui.TreeViewFunctions.GetFloatValue"></a>

Called to retrieve the current value of a float slider.

*New in version 25.*

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **lColumn** (*int*) – The column index.
- **sliderInfo** (The slider information. See [TreeViewFloatSliderInfo Dict](#treeviewfloatsliderinfo-dict).) – dict

#### `TreeViewFunctions.SetFloatValue(self, root, userdata, obj, lColumn, value, finalValue)` <a id="c4d.gui.TreeViewFunctions.SetFloatValue"></a>

Called when a new value of a float slider has been set.

*New in version 25.*

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **lColumn** (*int*) – The column index.
- **value** (*float*) – The new value which has been set.
- **finalValue** (*bool*) – If this the last value in a drag session because the user has released the mouse button.

### Header/Column <a id="c4d.gui.TreeViewFunctions-method-Header-Column"></a>

#### `TreeViewFunctions.GetHeaderSortArrow(self, root, userdata, lColID)` <a id="c4d.gui.TreeViewFunctions.GetHeaderSortArrow"></a>

Called to retrieve the sort mode of column *lColID*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **lColID** (*int*) – The column index.

**Return type:** int

**Returns:** The sort direction.

#### `TreeViewFunctions.IsMoveColAllowed(self, root, userdata, lColID)` <a id="c4d.gui.TreeViewFunctions.IsMoveColAllowed"></a>

Called to check if column *lColID* can be moved or not.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **lColID** (*int*) – The column index.

**Return type:** bool

**Returns:** **True** if the column can be moved, otherwise **False**.

#### `TreeViewFunctions.IsResizeColAllowed(self, root, userdata, lColID)` <a id="c4d.gui.TreeViewFunctions.IsResizeColAllowed"></a>

Called to check if column *lColID* can be resized or not.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **lColID** (*int*) – The column index.

**Return type:** bool

**Returns:** **True** if the column can be resized, otherwise **False**.

### ID <a id="c4d.gui.TreeViewFunctions-method-ID"></a>

#### `TreeViewFunctions.GetId(self, root, userdata, obj)` <a id="c4d.gui.TreeViewFunctions.GetId"></a>

Called to retrieve the ID of object *obj*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.

**Return type:** int

**Returns:** The object ID.

### Input Events <a id="c4d.gui.TreeViewFunctions-method-Input-Events"></a>

#### `TreeViewFunctions.DeletePressed(self, root, userdata)` <a id="c4d.gui.TreeViewFunctions.DeletePressed"></a>

Called when a delete event is received.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.

#### `TreeViewFunctions.DoubleClick(self, root, userdata, obj, col, mouseinfo)` <a id="c4d.gui.TreeViewFunctions.DoubleClick"></a>

Called when a mouse double click event is received.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **col** (*int*) – The column index.
- **mouseinfo** (*dict*) – The mouse information. See [MouseInfo Dict](#mouseinfo-dict).

**Return type:** bool

**Returns:** **True** if the event was handled, otherwise **False**.

#### `TreeViewFunctions.FinishInput(self, root, userdata, data)` <a id="c4d.gui.TreeViewFunctions.FinishInput"></a>

Called at the end of the complete input handling.

*New in version 24.*

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.

**Param:** Data generated in `TreeViewCustomGui.StartInput()`.

**Type:** [`maxon.Data`](../../maxon_generated/datatypes/base_core/maxon.Data.md#module-maxon.Data)

#### `TreeViewFunctions.HeaderClick(self, root, userdata, lColID, lChannel, bDblClk, mouseX, mouseY, ua)` <a id="c4d.gui.TreeViewFunctions.HeaderClick"></a>

Called when a header has been clicked.

*Changed in version R20:* Added parameters *mouseX*, *mouseY* and *ua*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.

- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.

- **lColID** (*int*) – The column index.

- **lChannel** (*int*) –

  The mouse channel:

  > |   |   |
  > |---|---|
  > | *BFM_INPUT_MOUSELEFT* | Left mouse button. |
  > | *BFM_INPUT_MOUSERIGHT* | Right mouse button. |
  > | *BFM_INPUT_MOUSEMIDDLE* | Middle mouse button. |
  > | *BFM_INPUT_MOUSEX1* | Fourth mouse button. |
  > | *BFM_INPUT_MOUSEX2* | Five mouse button. |
  > | *BFM_INPUT_MOUSEWHEEL* | Mouse wheel message. |
  > | *BFM_INPUT_MOUSEMOVE* | Mouse move message. |
  > | *BFM_INPUT_MOUSEMOVE* | Mouse move message. |
  > | *BFM_INPUT_WHEELSCROLL* | **True** for scroll events on a classic wheel mouse.  <br>**False** for everything else (touchpad, magic mouse). |

- **bDblClk** (*int*) – **True** for double-click event, otherwise **False**.

- **mouseX** (*int*) –

  *New in version R20:* The mouse horizontal position local to the left hand edge of the column, or *NOTOK* if TREEVIEW_MOVE_COLUMN is set to true.

- **mouseY** (*int*) –

  *New in version R20:* The mouse vertical position local to the header top, or *NOTOK* if TREEVIEW_MOVE_COLUMN is set to true.

- **ua** (*Optional*[[*c4d.gui.GeUserArea*](../GeUserArea/index.md#c4d.gui.GeUserArea)]) –

  *New in version R20:* The header’s user area, or **None** if TREEVIEW_MOVE_COLUMN is set to true.

**Return type:** bool

**Returns:** **True** if the tree view needs to be updated, otherwise **False**.

#### `TreeViewFunctions.InputEvent(self, root, userdata, pArea, msg)` <a id="c4d.gui.TreeViewFunctions.InputEvent"></a>

Called when an input event is received.

> **Note:** All information about the input event is stored in the *msg* container.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **pArea** ([*c4d.gui.GeUserArea*](../GeUserArea/index.md#c4d.gui.GeUserArea)) – The user area of the tree view.
- **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The event container.

**Return type:** bool

**Returns:** **True** if the event was handled, otherwise **False**.

#### `TreeViewFunctions.MouseDown(self, root, userdata, obj, col, mouseinfo, rightButton)` <a id="c4d.gui.TreeViewFunctions.MouseDown"></a>

Called when a mouse down event is received.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **col** (*int*) – The column index.
- **mouseinfo** (*dict*) – The mouse information. See [MouseInfo Dict](#mouseinfo-dict).
- **rightButton** (*bool*) – **True** if the right mouse button was used, otherwise **False**.

**Return type:** bool

**Returns:** **True** if the event was handled, otherwise **False**.

#### `TreeViewFunctions.StartInput(self, root, userdata)` <a id="c4d.gui.TreeViewFunctions.StartInput"></a>

Called before input loop starts.  
This functions allows to lock resources while input events are executed.

*New in version 24.*

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.

**Returns:** data which will be passed to `TreeViewCustomGui.FinishInput()`.

**Return type:** [`maxon.Data`](../../maxon_generated/datatypes/base_core/maxon.Data.md#module-maxon.Data)

### Insert Object <a id="c4d.gui.TreeViewFunctions-method-Insert-Object"></a>

#### `TreeViewFunctions.InsertObject(self, root, userdata, obj, dragtype, dragobject, insertmode, bCopy)` <a id="c4d.gui.TreeViewFunctions.InsertObject"></a>

Called to insert *dragobject* as specified.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.

- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.

- **obj** (*any*) – An object in the tree.

- **dragtype** (*int*) –

  The drag type:

  > |   |   |
  > |---|---|
  > | *DRAGTYPE_ATOMARRAY* | Atom array. The data is a list of [`c4d.C4DAtom`](../../c4d/C4DAtom/index.md#c4d.C4DAtom). |
  > | *DRAGTYPE_CMDPALETTE* | Not supported. |
  > | *DRAGTYPE_COMMAND* | Not supported. |
  > | *DRAGTYPE_DESCID* | Description ID. The data is a dict(‘did’: [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID), ‘arr’: list of [`c4d.C4DAtom`](../../c4d/C4DAtom/index.md#c4d.C4DAtom)). |
  > | *DRAGTYPE_ICON* | Not supported. |
  > | *DRAGTYPE_FILES* | Files. The data is a string with the filename. |
  > | *DRAGTYPE_FILENAME_IMAGE* | Image. The data is a string with the filename. |
  > | *DRAGTYPE_FILENAME_OTHER* | Other filename. The data is a string with the filename. |
  > | *DRAGTYPE_FILENAME_SCENE* | Scene filename. The data is a string with the filename. |
  > | *DRAGTYPE_MANAGER* | Not supported. |
  > | *DRAGTYPE_RGB* | RGB color. The data is a [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector). |
  > | *DRAGTYPE_RGB_ARRAY* | RGB color array. The data is a list of [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector). |
  > | *DRAGTYPE_RGBA_ARRAY* | RGBA color array. The data is a [`maxon.BaseArray`](../../maxon_generated/datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) of [`maxon.ColorA`](../../maxon_generated/datatypes/vec_col_mat/maxon.ColorA.md#module-maxon.ColorA). |
  > | *DRAGTYPE_BROWSER* | Browser drag message. The data is a list of string with the filename. |
  > | *DRAGTYPE_ASSET* | *New in version 2023.2.0:* Message ID for Asset browser assets, the message data is a [`maxon.DragAndDropDataAssetArray`](../../maxon_generated/frameworks/asset/datatype/maxon.DragAndDropDataAssetArray.md#module-maxon.DragAndDropDataAssetArray). Exposed as *maxon.DRAGTYPE_ASSET* in Python. |

- **dragobject** (*any*) – The drag object on drag receive.

- **insertmode** (*int*) –

  The insert mode:

  > |   |   |
  > |---|---|
  > | *INSERT_BEFORE* | Insert before. |
  > | *INSERT_AFTER* | Insert after. |
  > | *INSERT_UNDER* | Insert under. |
  > | *INSERT_REPLACE* | Replace the object. |

- **bCopy** (*bool*) – **True** if the object should be copied, otherwise **False**.

### Layout <a id="c4d.gui.TreeViewFunctions-method-Layout"></a>

#### `TreeViewFunctions.GetBackgroundColor(self, root, userdata, obj, line, col)` <a id="c4d.gui.TreeViewFunctions.GetBackgroundColor"></a>

Called to specify the background color of *line*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **line** (*int*) – The line index.
- **col** (*Union*[*int*, [*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)]) – Set this to the background color for line. Can be a vector or a color

**Return type:** Union[int, [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The background color for *line* as color ID or vector.

#### `TreeViewFunctions.GetColors(self, root, userdata, obj, pNormal, pSelected)` <a id="c4d.gui.TreeViewFunctions.GetColors"></a>

Called to specify the text colors of object *obj*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **pNormal** (*Union*[*int*, [*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)]) – Set this to the normal text color for obj. Can be a vector or a color ID.
- **pSelected** (*Union*[*int*, [*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)]) – Set this to the selected text color for obj. Can be a vector or a color ID.

**Return type:** Union[Tuple[Union[int, [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)], Union[int, [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)]], List[Union[int, [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)], Union[int, [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)]]]

**Returns:** The normal and selected text color as color ID or vector.

#### `TreeViewFunctions.GetColumnWidth(self, root, userdata, obj, col, area)` <a id="c4d.gui.TreeViewFunctions.GetColumnWidth"></a>

Called to retrieve the column width of object *obj* in column *col*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **col** (*int*) – The column index.
- **area** ([*c4d.gui.GeUserArea*](../GeUserArea/index.md#c4d.gui.GeUserArea)) – The user area used to determine the text width with `GeUserArea.DrawGetTextWidth()`.

**Return type:** int

**Returns:** The column width.

#### `TreeViewFunctions.GetHeaderColumnWidth(self, root, userdata, col, area)` <a id="c4d.gui.TreeViewFunctions.GetHeaderColumnWidth"></a>

Called to retrieve the width of the header for column *col*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **col** (*int*) – The column index.
- **area** ([*c4d.gui.GeUserArea*](../GeUserArea/index.md#c4d.gui.GeUserArea)) – The user area used to determine the text width with `GeUserArea.DrawGetTextWidth()`.

**Return type:** int

**Returns:** The header column width, or a negative number for auto header width.

#### `TreeViewFunctions.GetLineHeight(self, root, userdata, obj, col, area)` <a id="c4d.gui.TreeViewFunctions.GetLineHeight"></a>

Called to retrieve the line height of object *obj* in column *col*.

> **Note:** Always return a positive value.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **col** (*int*) – The column index.
- **area** ([*c4d.gui.GeUserArea*](../GeUserArea/index.md#c4d.gui.GeUserArea)) – The user area used to determine the text height with `GeUserArea.DrawGetFontHeight()`.

**Return type:** int

**Returns:** The line height.

#### `TreeViewFunctions.GetMinHeaderHeight(self, root, userdata, area)` <a id="c4d.gui.TreeViewFunctions.GetMinHeaderHeight"></a>

Called to retrieve the minimum header height.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **area** ([*c4d.gui.GeUserArea*](../GeUserArea/index.md#c4d.gui.GeUserArea)) – The user area used to determine the text height with `GeUserArea.DrawGetFontHeight()`.

**Return type:** int

**Returns:** The minimum header height, or a negative value for auto header height.

### Name and Bubble help <a id="c4d.gui.TreeViewFunctions-method-Name-and-Bubble-help"></a>

#### `TreeViewFunctions.EmptyText(self, root, userdata)` <a id="c4d.gui.TreeViewFunctions.EmptyText"></a>

Called to requests the text to display when the treeview area is completely empty such as “Drag falloff object’s here”

*New in version R25.010.*

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.

**Returns:** the text to display in the empty treeview area.

**Return type:** str

#### `TreeViewFunctions.GetBubbleHelp(self, root, userdata, obj, col, info)` <a id="c4d.gui.TreeViewFunctions.GetBubbleHelp"></a>

Called to retrieve the bubble help of object.

*New in version 24.*

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **col** (*int*) – The column index.
- **info** (*dict*) – The mouse information. See [MouseInfo Dict](#mouseinfo-dict).

**Return type:** str

**Returns:** The bubble help of the object.

#### `TreeViewFunctions.GetName(self, root, userdata, obj)` <a id="c4d.gui.TreeViewFunctions.GetName"></a>

Called to retrieve the name of object *obj*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.

**Return type:** str

**Returns:** The object name.

#### `TreeViewFunctions.GetNameForEdit(self, root, userdata, obj)` <a id="c4d.gui.TreeViewFunctions.GetNameForEdit"></a>

Called to retrieve the name of object obj for display in the edit text box.

*New in version R25.010.*

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.

**Returns:** The object name.

**Return type:** str

#### `TreeViewFunctions.SetName(self, root, userdata, obj, str)` <a id="c4d.gui.TreeViewFunctions.SetName"></a>

Called to set the name of object *obj*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **str** (*str*) – The new object name.

### Navigation <a id="c4d.gui.TreeViewFunctions-method-Navigation"></a>

#### `TreeViewFunctions.GetDown(self, root, userdata, obj)` <a id="c4d.gui.TreeViewFunctions.GetDown"></a>

Called to retrieve the first child of *obj*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.

**Return type:** Optional[Any]

**Returns:** The first child of *obj*.

#### `TreeViewFunctions.GetFirst(self, root, userdata)` <a id="c4d.gui.TreeViewFunctions.GetFirst"></a>

Called to retrieve the first object of the tree.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.

**Return type:** Optional[Any]

**Returns:** The first object.

#### `TreeViewFunctions.GetNext(self, root, userdata, obj)` <a id="c4d.gui.TreeViewFunctions.GetNext"></a>

Called to retrieve the object after *obj*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.

**Return type:** Optional[Any]

**Returns:** The object after *obj*.

#### `TreeViewFunctions.GetPred(self, root, userdata, obj)` <a id="c4d.gui.TreeViewFunctions.GetPred"></a>

Called to retrieve the object before *obj*.

> **Note:** This is only used for drag and drop checks.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.

**Return type:** Optional[Any]

**Returns:** The object before *obj*.

### Notifications <a id="c4d.gui.TreeViewFunctions-method-Notifications"></a>

#### `TreeViewFunctions.AddRow(self, root, userdata)` <a id="c4d.gui.TreeViewFunctions.AddRow"></a>

Called when a requests to add a row to the treeview.

*New in version R25.010.*

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.

#### `TreeViewFunctions.ColumnMoved(self, root, userdata, lColID, lInsertBeforeCol, plIndexMap, pbcLayout)` <a id="c4d.gui.TreeViewFunctions.ColumnMoved"></a>

Called when a column has been moved.

*New in version R25.010.*

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **lColID** (*int*) – The horizontal scroll steps.
- **lInsertBeforeCol** (*int*) – The column to insert **lColID** before.
- **plIndexMap** (*List*[*int*]) – The column index map array.
- **pbcLayout** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The new layout container. Basically the same as the container passed in `TreeViewCustomGui.SetLayout()` but reflecting the changed column order.

#### `TreeViewFunctions.PaintFinished(self, root, userdata)` <a id="c4d.gui.TreeViewFunctions.PaintFinished"></a>

Called when a paint selection has been performed in the tree view.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.

#### `TreeViewFunctions.Scrolled(self, root, userdata, h, v, x, y)` <a id="c4d.gui.TreeViewFunctions.Scrolled"></a>

Called when the tree view has been scrolled.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **h** (*int*) – The horizontal scroll steps.
- **v** (*int*) – The vertical scroll steps.
- **x** (*int*) – The X offset.
- **y** (*int*) – The Y offset.

#### `TreeViewFunctions.SelectionChanged(self, root, userdata)` <a id="c4d.gui.TreeViewFunctions.SelectionChanged"></a>

Called when selection has changed.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.

### Open <a id="c4d.gui.TreeViewFunctions-method-Open"></a>

#### `TreeViewFunctions.IsOpened(self, root, userdata, obj)` <a id="c4d.gui.TreeViewFunctions.IsOpened"></a>

Called to retrieve the folding status of object *obj*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.

**Return type:** bool

**Returns:** **True** if the object is opened, otherwise **False**.

#### `TreeViewFunctions.Open(self, root, userdata, obj, onoff)` <a id="c4d.gui.TreeViewFunctions.Open"></a>

Called to open or close object *obj*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.
- **onoff** (*bool*) – **True** if *obj* should be opened, otherwise **False**.

### Select <a id="c4d.gui.TreeViewFunctions-method-Select"></a>

#### `TreeViewFunctions.IsSelectable(self, root, userdata, obj)` <a id="c4d.gui.TreeViewFunctions.IsSelectable"></a>

Checks if the object is selectable, used to determine if the object should be skipped (not selectable) or not (selectable) when changing selection with keyboard (Up/Down/Home/End keys).

*New in version R25.010.*

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.

**Returns:** **True** if The object is selectable, otherwise **False**.

**Return type:** bool

#### `TreeViewFunctions.IsSelected(self, root, userdata, obj)` <a id="c4d.gui.TreeViewFunctions.IsSelected"></a>

Called to retrieve the selection status of object *obj*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.
- **obj** (*any*) – An object in the tree.

**Return type:** bool

**Returns:** **True** if the object is selected, otherwise **False**.

#### `TreeViewFunctions.Select(self, root, userdata, obj, mode)` <a id="c4d.gui.TreeViewFunctions.Select"></a>

Called to select object *obj*.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.

- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.

- **obj** (*any*) – An object in the tree.

- **mode** (*int*) –

  The selection mode:

  |   |   |
  |---|---|
  | *SELECTION_NEW* | Starts a new selection. |
  | *SELECTION_ADD* | Adds to the current selection |
  | *SELECTION_SUB* | Subtracts from the current selection. |

### Tristate <a id="c4d.gui.TreeViewFunctions-method-Tristate"></a>

#### `TreeViewFunctions.IsTristate(self, root, userdata)` <a id="c4d.gui.TreeViewFunctions.IsTristate"></a>

Called to retrieve the tristate flag of the tree.

**Parameters:**

- **root** (*any*) – The tree root passed to `TreeViewCustomGui.SetRoot()`.
- **userdata** (*any*) – The user data passed to `TreeViewCustomGui.SetRoot()`.

**Return type:** bool

**Returns:** **True** if the tristate flag is set, otherwise **False**.
