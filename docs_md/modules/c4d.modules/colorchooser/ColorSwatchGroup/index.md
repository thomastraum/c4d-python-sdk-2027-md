<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/colorchooser/ColorSwatchGroup/index.html -->

# c4d.modules.colorchooser.ColorSwatchGroup <a id="c4d-modules-colorchooser-colorswatchgroup"></a>

## *class* `c4d.modules.colorchooser.ColorSwatchGroup` <a id="c4d.modules.colorchooser.ColorSwatchGroup"></a>

*New in version R18.011.*

## Overview <a id="overview"></a>

**Color Editing**

- [`ColorSwatchGroup.AddColor()`](#c4d.modules.colorchooser.ColorSwatchGroup.AddColor): Adds a new *color* to the group.
- [`ColorSwatchGroup.AddColors()`](#c4d.modules.colorchooser.ColorSwatchGroup.AddColors): Adds colors to the group.
- [`ColorSwatchGroup.SetColor()`](#c4d.modules.colorchooser.ColorSwatchGroup.SetColor): Edits the color at the given *index*.

**Color Inspection**

- [`ColorSwatchGroup.GetColor()`](#c4d.modules.colorchooser.ColorSwatchGroup.GetColor): Retrieves the color at the given *index*.
- [`ColorSwatchGroup.GetColorCount()`](#c4d.modules.colorchooser.ColorSwatchGroup.GetColorCount): Retrieves the number of colors stored in the group.
- [`ColorSwatchGroup.GetColors()`](#c4d.modules.colorchooser.ColorSwatchGroup.GetColors): Retrieves the colors stored in the group.

**Color Organization**

- [`ColorSwatchGroup.HasDuplicatedColors()`](#c4d.modules.colorchooser.ColorSwatchGroup.HasDuplicatedColors): Checks if the group has duplicated colors.
- [`ColorSwatchGroup.RemoveDuplicatedColors()`](#c4d.modules.colorchooser.ColorSwatchGroup.RemoveDuplicatedColors): Removes duplicated colors in the group.
- [`ColorSwatchGroup.SortColors()`](#c4d.modules.colorchooser.ColorSwatchGroup.SortColors): Sorts colors in the group based on their HSV values.

**Color Removal**

- [`ColorSwatchGroup.RemoveColor()`](#c4d.modules.colorchooser.ColorSwatchGroup.RemoveColor): Removes the color at the given *index*.
- [`ColorSwatchGroup.RemoveSelectedColors()`](#c4d.modules.colorchooser.ColorSwatchGroup.RemoveSelectedColors): Removes all selected colors from the group.
- [`ColorSwatchGroup.Reset()`](#c4d.modules.colorchooser.ColorSwatchGroup.Reset): Removes all colors from the group.

**Group Naming**

- [`ColorSwatchGroup.GetName()`](#c4d.modules.colorchooser.ColorSwatchGroup.GetName): Retrieves the group name.
- [`ColorSwatchGroup.SetName()`](#c4d.modules.colorchooser.ColorSwatchGroup.SetName): Sets the group name.

**Group Transfer**

- [`ColorSwatchGroup.CopyFrom()`](#c4d.modules.colorchooser.ColorSwatchGroup.CopyFrom): Copies a group.
- [`ColorSwatchGroup.Merge()`](#c4d.modules.colorchooser.ColorSwatchGroup.Merge): Merges colors from *group*.

**Magic Methods**

- [`ColorSwatchGroup.__init__()`](#c4d.modules.colorchooser.ColorSwatchGroup.__init__): Creates a new swatch group.

**Selection Management**

- [`ColorSwatchGroup.InvertSelection()`](#c4d.modules.colorchooser.ColorSwatchGroup.InvertSelection): Inverts the selection state of all colors, so the currently selected colors will be unselected and vice-versa.
- [`ColorSwatchGroup.IsColorSelected()`](#c4d.modules.colorchooser.ColorSwatchGroup.IsColorSelected): Checks if the color at the given *index* is selected.
- [`ColorSwatchGroup.IsGroupSelected()`](#c4d.modules.colorchooser.ColorSwatchGroup.IsGroupSelected): Checks if the group is selected.
- [`ColorSwatchGroup.SelectColor()`](#c4d.modules.colorchooser.ColorSwatchGroup.SelectColor): Selects/unselects the color at the given *index*.
- [`ColorSwatchGroup.SelectGroup()`](#c4d.modules.colorchooser.ColorSwatchGroup.SelectGroup): Selects the group.

## Members <a id="members"></a>

### Color Editing <a id="c4d.modules.colorchooser.ColorSwatchGroup-method-Color-Editing"></a>

#### `ColorSwatchGroup.AddColor(self, color, selected=False, insertAt=-1)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.AddColor"></a>

Adds a new *color* to the group.

**Parameters:**

- **color** ([*c4d.Vector4d*](../../../c4d/Vector4d/index.md#c4d.Vector4d)) – The color value.
- **selected** (*bool*) – The initial selection state of the color.
- **insertAt** (*int*) – The index of the new color (the list size will increase and the existing elements are moved) or *-1* to add it to the end of the list.

**Return type:** int

**Returns:** The index of the new color or *-1* if an error occurred.

#### `ColorSwatchGroup.AddColors(self, colors, selected=False, merge=True, insertAt=-1)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.AddColors"></a>

Adds colors to the group.

*Changed in version R20:* *colors* changed to a maxon.BaseArray of maxon.ColorA.

**Parameters:**

- **colors** (maxon.BaseArray[[`maxon.ColorA`](../../../maxon_generated/datatypes/vec_col_mat/maxon.ColorA.md#module-maxon.ColorA)]) – The colors to add.
- **selected** (*bool*) – The initial selection state of added colors.
- **merge** (*bool*) – Set to **True** to merge the colors with current group colors. Set to **False** to replace the content of the group.
- **insertAt** (*int*) – If *merge* is set to **True**, this is the index to insert the new colors.

**Return type:** int

**Returns:** The index of the new colors or *-1* if an error occurred.

#### `ColorSwatchGroup.SetColor(self, index, color, selected)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.SetColor"></a>

Edits the color at the given *index*.

*Changed in version R20:* *color* changed to maxon.ColorA type.

**Parameters:**

- **index** (*int*) – The index of the color. Must be 0 <= *index* < [`GetColorCount()`](#c4d.modules.colorchooser.ColorSwatchGroup.GetColorCount).
- **color** (*maxon.ColorA*) – The new color value.
- **selected** (*int*) – The new selection status. Possible values are: *-1* = keep current selection status unchanged, 0 = *unselect*, 1 = *select*.

**Return type:** bool

**Returns:** **True** if the color could be changed, otherwise **False**.

### Color Inspection <a id="c4d.modules.colorchooser.ColorSwatchGroup-method-Color-Inspection"></a>

#### `ColorSwatchGroup.GetColor(self, index)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.GetColor"></a>

Retrieves the color at the given *index*.

*Changed in version R20:* The function returns a maxon.ColorA in the tuple.

**Parameters:** **index** (*int*) – The index of the color. Must be 0 <= *index* < [`GetColorCount()`](#c4d.modules.colorchooser.ColorSwatchGroup.GetColorCount).

**Return type:** Tuple[[`maxon.ColorA`](../../../maxon_generated/datatypes/vec_col_mat/maxon.ColorA.md#module-maxon.ColorA), bool]

**Returns:** The color value and its selection status.

#### `ColorSwatchGroup.GetColorCount(self)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.GetColorCount"></a>

Retrieves the number of colors stored in the group.

**Return type:** int

**Returns:** The number of colors stored in the group.

#### `ColorSwatchGroup.GetColors(self, selectedOnly=False)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.GetColors"></a>

Retrieves the colors stored in the group.

*Changed in version R20:* The function returns a maxon.BaseArray of maxon.ColorA.

**Parameters:** **selectedOnly** (*bool*) – Set to **True** to get only the selected colors, set to **False** to get all colors (default).

**Return type:** maxon.BaseArray[[`maxon.ColorA`](../../../maxon_generated/datatypes/vec_col_mat/maxon.ColorA.md#module-maxon.ColorA)]

**Returns:** The list of colors.

### Color Organization <a id="c4d.modules.colorchooser.ColorSwatchGroup-method-Color-Organization"></a>

#### `ColorSwatchGroup.HasDuplicatedColors(self)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.HasDuplicatedColors"></a>

Checks if the group has duplicated colors.

**Return type:** bool

**Returns:** **True** if duplicated colors were found, otherwise **False**.

#### `ColorSwatchGroup.RemoveDuplicatedColors(self)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.RemoveDuplicatedColors"></a>

Removes duplicated colors in the group.

#### `ColorSwatchGroup.SortColors(self)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.SortColors"></a>

Sorts colors in the group based on their HSV values.

### Color Removal <a id="c4d.modules.colorchooser.ColorSwatchGroup-method-Color-Removal"></a>

#### `ColorSwatchGroup.RemoveColor(self, index, removeCount=1)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.RemoveColor"></a>

Removes the color at the given *index*.

**Parameters:**

- **index** (*int*) – The index of the color. Must be 0 <= *index* < [`GetColorCount()`](#c4d.modules.colorchooser.ColorSwatchGroup.GetColorCount).
- **removeCount** (*int*) – Number of colors to be removed. If *removeCnt* is higher than what is available only the number of remaining colors will be removed.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `ColorSwatchGroup.RemoveSelectedColors(self)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.RemoveSelectedColors"></a>

Removes all selected colors from the group.

#### `ColorSwatchGroup.Reset(self)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.Reset"></a>

Removes all colors from the group.

### Group Naming <a id="c4d.modules.colorchooser.ColorSwatchGroup-method-Group-Naming"></a>

#### `ColorSwatchGroup.GetName(self)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.GetName"></a>

Retrieves the group name.

**Return type:** str

**Returns:** The group name.

#### `ColorSwatchGroup.SetName(self, name)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.SetName"></a>

Sets the group name.

**Parameters:** **name** (*str*) – The new group name.

### Group Transfer <a id="c4d.modules.colorchooser.ColorSwatchGroup-method-Group-Transfer"></a>

#### `ColorSwatchGroup.CopyFrom(self, group)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.CopyFrom"></a>

Copies a group.

**Parameters:** **group** ([*c4d.modules.colorchooser.ColorSwatchGroup*](#c4d.modules.colorchooser.ColorSwatchGroup)) – The group to copy colors from.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `ColorSwatchGroup.Merge(self, group)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.Merge"></a>

Merges colors from *group*.

**Parameters:** **group** ([*c4d.modules.colorchooser.ColorSwatchGroup*](#c4d.modules.colorchooser.ColorSwatchGroup)) – The group to merge colors from.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Magic Methods <a id="c4d.modules.colorchooser.ColorSwatchGroup-method-Magic-Methods"></a>

#### `ColorSwatchGroup.__init__(self, name='', selected=False, colors=None)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.__init__"></a>

Creates a new swatch group.

*Changed in version R20:* *colors* changed to a maxon.BaseArray of maxon.ColorA.

**Parameters:**

- **name** (*str*) – The name of the group.
- **selected** (*bool*) – The selection state of the group.
- **colors** (Optional[[`maxon.BaseArray`](../../../maxon_generated/datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.ColorA`](../../../maxon_generated/datatypes/vec_col_mat/maxon.ColorA.md#module-maxon.ColorA)]]) – The colors to fill the group with.

### Selection Management <a id="c4d.modules.colorchooser.ColorSwatchGroup-method-Selection-Management"></a>

#### `ColorSwatchGroup.InvertSelection(self)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.InvertSelection"></a>

Inverts the selection state of all colors, so the currently selected colors will be unselected and vice-versa.

#### `ColorSwatchGroup.IsColorSelected(self, index)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.IsColorSelected"></a>

Checks if the color at the given *index* is selected.

**Parameters:** **index** (*int*) – The index of the color. Must be 0 <= *index* < [`GetColorCount()`](#c4d.modules.colorchooser.ColorSwatchGroup.GetColorCount).

**Return type:** bool

**Returns:** **True** if the color is selected, **False** if it is unselected or *index* is invalid.

#### `ColorSwatchGroup.IsGroupSelected(self)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.IsGroupSelected"></a>

Checks if the group is selected.

**Return type:** bool

**Returns:** **True** if the group is selected, otherwise **False**.

#### `ColorSwatchGroup.SelectColor(self, index, selected)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.SelectColor"></a>

Selects/unselects the color at the given *index*.

**Parameters:**

- **index** (*int*) – The index of the color. Must be 0 <= *index* < [`GetColorCount()`](#c4d.modules.colorchooser.ColorSwatchGroup.GetColorCount).
- **selected** (*bool*) – The new selection status.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `ColorSwatchGroup.SelectGroup(self, select)` <a id="c4d.modules.colorchooser.ColorSwatchGroup.SelectGroup"></a>

Selects the group. This will select/unselect the group icon and all colors in the group.

**Parameters:** **select** (*bool*) – The new selection status.
