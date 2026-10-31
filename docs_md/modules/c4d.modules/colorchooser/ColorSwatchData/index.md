<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/colorchooser/ColorSwatchData/index.html -->

# c4d.modules.colorchooser.ColorSwatchData <a id="c4d-modules-colorchooser-colorswatchdata"></a>

## *class* `c4d.modules.colorchooser.ColorSwatchData` <a id="c4d.modules.colorchooser.ColorSwatchData"></a>

This type handles the Swatch Data stored globally, in a [`BaseDocument`](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) or a preset.  
It holds 2 kinds of groups:

- A global color group that is shared between all Cinema 4D documents and has special methods to handle it.
- Document-based color groups stored in a Cinema 4D document.

*New in version R18.011.*

## Overview <a id="overview"></a>

**Data Transfer**

- [`ColorSwatchData.CopyFrom()`](#c4d.modules.colorchooser.ColorSwatchData.CopyFrom): Copies color swatch data.
- [`ColorSwatchData.Merge()`](#c4d.modules.colorchooser.ColorSwatchData.Merge): Merges groups from *data*.

**Document Persistence**

- [`ColorSwatchData.Load()`](#c4d.modules.colorchooser.ColorSwatchData.Load): Loads color groups.
- [`ColorSwatchData.Save()`](#c4d.modules.colorchooser.ColorSwatchData.Save): Saves the document-based color groups into the given document.

**Group Management**

- [`ColorSwatchData.AddGroup()`](#c4d.modules.colorchooser.ColorSwatchData.AddGroup): Adds a new group.
- [`ColorSwatchData.GetGroupAtIndex()`](#c4d.modules.colorchooser.ColorSwatchData.GetGroupAtIndex): Retrieves the group at the given *index*.
- [`ColorSwatchData.GetGroupCount()`](#c4d.modules.colorchooser.ColorSwatchData.GetGroupCount): Returns the number of groups stored in *category*.
- [`ColorSwatchData.InsertGroup()`](#c4d.modules.colorchooser.ColorSwatchData.InsertGroup): Inserts an existing group.
- [`ColorSwatchData.RemoveGroup()`](#c4d.modules.colorchooser.ColorSwatchData.RemoveGroup): Removes the document-based group at the given *index*.
- [`ColorSwatchData.SetGroupAtIndex()`](#c4d.modules.colorchooser.ColorSwatchData.SetGroupAtIndex): Replaces the group at the given *index*.

**Magic Methods**

- [`ColorSwatchData.__init__()`](#c4d.modules.colorchooser.ColorSwatchData.__init__): Creates a new swatch data.

**Selection Clearing**

- [`ColorSwatchData.RemoveSelectedItems()`](#c4d.modules.colorchooser.ColorSwatchData.RemoveSelectedItems): Removes all selected groups and colors, including selected global colors.
- [`ColorSwatchData.Reset()`](#c4d.modules.colorchooser.ColorSwatchData.Reset): Removes all groups and colors, including globals.

## Members <a id="members"></a>

### Data Transfer <a id="c4d.modules.colorchooser.ColorSwatchData-method-Data-Transfer"></a>

#### `ColorSwatchData.CopyFrom(self, data)` <a id="c4d.modules.colorchooser.ColorSwatchData.CopyFrom"></a>

Copies color swatch data.

**Parameters:** **data** ([*c4d.modules.colorchooser.ColorSwatchData*](#c4d.modules.colorchooser.ColorSwatchData)) – The data to copy groups from.

**Return type:** bool

**Returns:** **True** if the color swatch data was successfully copied, otherwise **False**.

#### `ColorSwatchData.Merge(self, data)` <a id="c4d.modules.colorchooser.ColorSwatchData.Merge"></a>

Merges groups from *data*.

**Parameters:** **data** ([*c4d.modules.colorchooser.ColorSwatchData*](#c4d.modules.colorchooser.ColorSwatchData)) – The data to merge groups from.

**Return type:** bool

**Returns:** **True** if the groups were successfully merged, otherwise **False**.

### Document Persistence <a id="c4d.modules.colorchooser.ColorSwatchData-method-Document-Persistence"></a>

#### `ColorSwatchData.Load(self, doc, merge=False, globalColors=False)` <a id="c4d.modules.colorchooser.ColorSwatchData.Load"></a>

Loads color groups.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to load the color groups from.

- **merge** (*Optional*[*bool*]) –

  If **True** the colors of the given document are merged with the stored colors.  
  Otherwise the existing colors are discarded (default).

- **globalColors** (*Optional*[*bool*]) –

  *New in version R20:* If **True** the global colors are loaded.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `ColorSwatchData.Save(self, doc, globalColors=False)` <a id="c4d.modules.colorchooser.ColorSwatchData.Save"></a>

Saves the document-based color groups into the given document.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to store the color groups into.

- **globalColors** (*Optional*[*bool*]) –

  *New in version R20:* If **True** the global colors are saved.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Group Management <a id="c4d.modules.colorchooser.ColorSwatchData-method-Group-Management"></a>

#### `ColorSwatchData.AddGroup(self, category=1, name='', selected=False, insertAt=-1, colors=None)` <a id="c4d.modules.colorchooser.ColorSwatchData.AddGroup"></a>

Adds a new group.

**Parameters:**

- **category** (*Optional*[*int*]) –

  *New in version R20:* The group category:

  |   |   |
  |---|---|
  | *SWATCH_CATEGORY_GLOBAL* | Global. |
  | *SWATCH_CATEGORY_DOCUMENT* | Document. |

- **name** (*str*) – The name of the new group. If empty the default string “Untitled” will be used.

- **selected** (*bool*) – The initial selection state of the new group.

- **insertAt** (*int*) – The index of the new group (the list size will increase and the existing elements will be moved) or *-1* to add it to the end of the list (default).

- **colors** (Optional[List[[`maxon.ColorA`](../../../maxon_generated/datatypes/vec_col_mat/maxon.ColorA.md#module-maxon.ColorA)]]) – The colors to fill the group with.

**Return type:** Optional[[c4d.modules.colorchooser.ColorSwatchGroup](../ColorSwatchGroup/index.md#c4d.modules.colorchooser.ColorSwatchGroup)]

**Returns:** The new swatch group or **None**.

#### `ColorSwatchData.GetGroupAtIndex(self, index, category=1)` <a id="c4d.modules.colorchooser.ColorSwatchData.GetGroupAtIndex"></a>

Retrieves the group at the given *index*.

**Parameters:**

- **index** (*int*) – The index of the color group. Must be 0 <= *index* < [`GetGroupCount()`](#c4d.modules.colorchooser.ColorSwatchData.GetGroupCount).

- **category** (*Optional*[*int*]) –

  *New in version R20:* The group category:

  |   |   |
  |---|---|
  | *SWATCH_CATEGORY_GLOBAL* | Global. |
  | *SWATCH_CATEGORY_DOCUMENT* | Document. |

**Return type:** Optional[[c4d.modules.colorchooser.ColorSwatchGroup](../ColorSwatchGroup/index.md#c4d.modules.colorchooser.ColorSwatchGroup)]

**Returns:** The swatch group or **None**.

#### `ColorSwatchData.GetGroupCount(self, category=1)` <a id="c4d.modules.colorchooser.ColorSwatchData.GetGroupCount"></a>

Returns the number of groups stored in *category*.

**Parameters:**

**category** (*Optional*[*int*]) –

*New in version R20:* The group category:

> |   |   |
> |---|---|
> | *SWATCH_CATEGORY_GLOBAL* | Global. |
> | *SWATCH_CATEGORY_DOCUMENT* | Document. |

**Return type:** int

**Returns:** The number of color groups.

#### `ColorSwatchData.InsertGroup(self, group, insertAt=-1, category=1)` <a id="c4d.modules.colorchooser.ColorSwatchData.InsertGroup"></a>

Inserts an existing group.

**Parameters:**

- **group** ([*c4d.modules.colorchooser.ColorSwatchGroup*](../ColorSwatchGroup/index.md#c4d.modules.colorchooser.ColorSwatchGroup)) – The group to insert.

- **insertAt** (*Optional*[*int*]) – The index of the new group (the list size will increase and the existing elements will be moved) or *-1* to add it to the end of the list (default).

- **category** (*Optional*[*int*]) –

  *New in version R20:* The group category:

  |   |   |
  |---|---|
  | *SWATCH_CATEGORY_GLOBAL* | Global. |
  | *SWATCH_CATEGORY_DOCUMENT* | Document. |

**Return type:** bool

**Returns:** **True** if the group was successfully inserted, otherwise **False**.

#### `ColorSwatchData.RemoveGroup(self, index, category=1)` <a id="c4d.modules.colorchooser.ColorSwatchData.RemoveGroup"></a>

Removes the document-based group at the given *index*.

**Parameters:**

- **index** (*int*) – The index of the color group to remove. Must be 0 <= *index* < [`GetGroupCount()`](#c4d.modules.colorchooser.ColorSwatchData.GetGroupCount).

- **category** (*Optional*[*int*]) –

  *New in version R20:* The group category:

  |   |   |
  |---|---|
  | *SWATCH_CATEGORY_GLOBAL* | Global. |
  | *SWATCH_CATEGORY_DOCUMENT* | Document. |

**Return type:** bool

**Returns:** **True** if the group was successfully removed, otherwise **False**.

#### `ColorSwatchData.SetGroupAtIndex(self, index, group, category=1)` <a id="c4d.modules.colorchooser.ColorSwatchData.SetGroupAtIndex"></a>

Replaces the group at the given *index*.

**Parameters:**

- **index** (*int*) – The index of the color group. Must be 0 <= *index* < [`GetGroupCount()`](#c4d.modules.colorchooser.ColorSwatchData.GetGroupCount).

- **group** ([*c4d.modules.colorchooser.ColorSwatchGroup*](../ColorSwatchGroup/index.md#c4d.modules.colorchooser.ColorSwatchGroup)) – The group to set.

- **category** (*Optional*[*int*]) –

  *New in version R20:* The group category:

  |   |   |
  |---|---|
  | *SWATCH_CATEGORY_GLOBAL* | Global. |
  | *SWATCH_CATEGORY_DOCUMENT* | Document. |

**Return type:** bool

**Returns:** **True** if the group was successfully set, otherwise **False**.

### Magic Methods <a id="c4d.modules.colorchooser.ColorSwatchData-method-Magic-Methods"></a>

#### `ColorSwatchData.__init__(self, doc=None, global_=False)` <a id="c4d.modules.colorchooser.ColorSwatchData.__init__"></a>

Creates a new swatch data.

**Parameters:**

- **doc** (*Optional*[[*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]) – Optional document to load swatches from.
- **global** (*Optional*[*bool*]) – If **True** the Global Swatch Group will be loaded.

### Selection Clearing <a id="c4d.modules.colorchooser.ColorSwatchData-method-Selection-Clearing"></a>

#### `ColorSwatchData.RemoveSelectedItems(self)` <a id="c4d.modules.colorchooser.ColorSwatchData.RemoveSelectedItems"></a>

Removes all selected groups and colors, including selected global colors.

#### `ColorSwatchData.Reset(self)` <a id="c4d.modules.colorchooser.ColorSwatchData.Reset"></a>

Removes all groups and colors, including globals.
