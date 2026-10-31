<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/LV.html -->

# LV <a id="lv"></a>

|   |   |
|---|---|
| *LV_TREE* | Tree or list. |
| *LV_USERTREE* | User tree. If set, the tree view calls `TreeViewFunctions.DrawCell()` for the left cell of each line (otherwise it would display the object’s name in the cell). |
| *LV_USER* | Custom. |
| *LV_CHECKBOX* | Checkbox. If set, the tree view calls `TreeViewFunctions.IsChecked()` and `TreeViewFunctions.SetCheck()` for each column and row. |
| *LV_CHECKBOXUSER* | Checkbox. If set, the tree view calls `TreeViewFunctions.IsChecked()` and `TreeViewFunctions.SetCheck()` for each column and row. User draw by `TreeViewFunctions.DrawCell()`. |
| *LV_SLIDER* | Slider. If set, the tree view calls `TreeViewFunctions.GetFloatValue()` and `TreeViewFunctions.SetFloatValue()` for each column and row. |
| *LV_DROPDOWN* | Dropdown cycle box. If set, the tree view calls `TreeViewFunctions.GetDropDownMenu()` and `TreeViewFunctions.SetDropDownMenu()` for each column and row. |
