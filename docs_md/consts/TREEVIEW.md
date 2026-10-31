<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/TREEVIEW.html -->

# TREEVIEW <a id="treeview"></a>

|   |   |   |
|---|---|---|
| *TREEVIEW_BORDER* | int | Border type: |

> |   |   |
> |---|---|
> | *BORDER_NONE* | No border. |
> | *BORDER_THIN_IN* | Thin border inward. |
> | *BORDER_THIN_OUT* | Thin border outward. |
> | *BORDER_IN* | Normal border inward. |
> | *BORDER_OUT* | Normal border outward. |
> | *BORDER_GROUP_IN* | Group border inside. |
> | *BORDER_GROUP_OUT* | Group border outside. |
> | *BORDER_OUT2* | Outward border 2. |
> | *BORDER_OUT3* | Outward border 3 |
> | *BORDER_BLACK* | Thin black line. |
> | *BORDER_ACTIVE_1* | Active border 1. |
> | *BORDER_ACTIVE_2* | Active border 2. |
> | *BORDER_ACTIVE_3* | Active border 3. |
> | *BORDER_ACTIVE_4* | Active border 4. |
> | *BORDER_GROUP_TOP* | Border along the top. |
> | *BORDER_ROUND* | Border with round corners. |
> | *BORDER_SCHEME_EDIT* | Edit field border like the shortcut gadget for example. |
> | *BORDER_SCHEME_EDIT_NUMERIC* | Edit field border that is open to the right like the link field for example. |
> | *BORDER_OUT3l* | Outward border 3, open to the left. |
> | *BORDER_OUT3r* | Outward border 3, open to the right. |
> | *BORDER_THIN_INb* | Thin border inward, open to the botton. |
> | *BORDER_MASK* | Masks out border type. |
> | *BORDER_TEXT_DOTTED* | Only used with `GeDialog.AddStaticText()`.  <br>Draws a dotted line at right of text, useful to visually connect the text with its parameter. |
> | *BORDER_WITH_TITLE_MONO* | Display group title with monospaced font. |
> | *BORDER_WITH_TITLE_BOLD* | Display group title with bold font. |
> | *BORDER_WITH_TITLE* | Display group title in the border. |

|   |   |   |
|---|---|---|
| *TREEVIEW_OUTSIDE_DROP* | bool | **True** if an object may be dropped under all the objects in the tree view. |
| *TREEVIEW_HIDE_LINES* | bool | **True** if no lines should be drawn. |
| *TREEVIEW_CTRL_DRAG* | bool | **True** if item may be duplicated by Ctrl + Drag. |
| *TREEVIEW_NO_MULTISELECT* | bool | **True** if no multiple selection is allowed. |
| *TREEVIEW_HAS_HEADER* | bool | **True** if the tree view may have a header line. |
| *TREEVIEW_RESIZE_HEADER* | bool | **True** if the column width can be changed by the user. |
| *TREEVIEW_MOVE_COLUMN* | bool | **True** if the user can move the columns. |
| *TREEVIEW_FIXED_LAYOUT* | bool | **True** if all lines have the same height. |
| *TREEVIEW_NOAUTOCOLUMNS* | bool | **True** if only the first line is asked for the columns width, resulting in a huge speedup. |
| *TREEVIEW_NO_OPEN_CTRLCLK* | bool | **True** if it is not allowed to open the complete tree with Ctrl + Click. |
| *TREEVIEW_ALT_DRAG* | bool | **True** if Alt should be used instead of Ctrl for drag and drop; implies item may be duplicated by Alt + Drag. |
| *TREEVIEW_NO_BACK_DELETE* | bool | Disable “delete pressed” messages if backspace was hit. |
| *TREEVIEW_NO_DELETE* | bool | Disable Delete Message Callback completely for backspace and delete. |
| *TREEVIEW_ALTERNATE_BG* | bool | Alternate background per line. |
| *TREEVIEW_CURSORKEYS* | bool | **True** if cursor keys should be processed. Note: The focus item has to be set to None if it is deleted and this flag is set. |
| *TREEVIEW_CUSTOM_BG_COLOR* | int or c4d.Vector | Custom Background Color. Can be an color ID ([COLOR constants](COLOR.md)) or a Vector color in range [0.0, 1.0].  <br>If unset, default application background color will be used.<br>> **Note:**<br>><br>> Only is applied if TREEVIEW_ALTERNATE_BG is **False**;  <br>> `TreeViewFunctions.GetBackgroundColor()` overrides it. |
| *TREEVIEW_NOENTERRENAME* | bool | Suppresses the rename popup when the user presses enter. |
| *TREEVIEW_NO_VERTICALSCROLL* | bool | **True** to disable vertical scrolling and show the full list. |
| *TREEVIEW_ADDROW* | bool | Show an add new column row at the bottom of the list. |
| *TREEVIEW_RESIZABLE* | bool | The treeview is resizable from the bottom edge. |
| *TREEVIEW_VERTICAL_SPACE* | int | *New in version R24:* vertical space between lines in pixel |
