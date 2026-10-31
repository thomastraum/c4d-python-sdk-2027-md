<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/hair/HairSelectionTag/index.html -->

# c4d.modules.hair.HairSelectionTag <a id="c4d-modules-hair-hairselectiontag"></a>

## *class* `c4d.modules.hair.HairSelectionTag` <a id="c4d.modules.hair.HairSelectionTag"></a>

Parent Class:

- [`c4d.BaseTag`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)

## Overview <a id="overview"></a>

**Magic Methods**

- [`HairSelectionTag.__init__()`](#c4d.modules.hair.HairSelectionTag.__init__)

**Selection Data**

- [`HairSelectionTag.GetSelected()`](#c4d.modules.hair.HairSelectionTag.GetSelected): Gets the selection.
- [`HairSelectionTag.GetSelectionType()`](#c4d.modules.hair.HairSelectionTag.GetSelectionType): Get the selection type.
- [`HairSelectionTag.SetSelected()`](#c4d.modules.hair.HairSelectionTag.SetSelected): Sets the selection.
- [`HairSelectionTag.SetSelectionType()`](#c4d.modules.hair.HairSelectionTag.SetSelectionType): Set the selection type.

**Selection Metrics**

- [`HairSelectionTag.GetCount()`](#c4d.modules.hair.HairSelectionTag.GetCount): Gets the count.
- [`HairSelectionTag.GetSegments()`](#c4d.modules.hair.HairSelectionTag.GetSegments): Gets the segment count.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.modules.hair.HairSelectionTag-method-Magic-Methods"></a>

#### `HairSelectionTag.__init__(self)` <a id="c4d.modules.hair.HairSelectionTag.__init__"></a>

### Selection Data <a id="c4d.modules.hair.HairSelectionTag-method-Selection-Data"></a>

#### `HairSelectionTag.GetSelected(self)` <a id="c4d.modules.hair.HairSelectionTag.GetSelected"></a>

Gets the selection.

**Return type:** Optional[[c4d.BaseSelect](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)]

**Returns:** The selection or **None**.

#### `HairSelectionTag.GetSelectionType(self)` <a id="c4d.modules.hair.HairSelectionTag.GetSelectionType"></a>

Get the selection type.

**Return type:** int

**Returns:**

The type:

|   |   |
|---|---|
| *HAIR_MODE_LOCKED* | Locked mode |
| *HAIR_MODE_HIDDEN* | Hidden mode. |
| *HAIR_MODE_TIPS* | Tips mode. |
| *HAIR_MODE_POINTS* | Points mode. |
| *HAIR_MODE_GUIDES* | Guides mode. |
| *HAIR_MODE_ROOTS* | Roots mode. |
| *HAIR_MODE_VERTEX* | Vertex mode. |

#### `HairSelectionTag.SetSelected(self, bs)` <a id="c4d.modules.hair.HairSelectionTag.SetSelected"></a>

Sets the selection.

**Parameters:** **bs** ([*c4d.BaseSelect*](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)) – The selection.

**Return type:** bool

**Returns:** **True** on success, otherwise **False**.

#### `HairSelectionTag.SetSelectionType(self, mode)` <a id="c4d.modules.hair.HairSelectionTag.SetSelectionType"></a>

Set the selection type.

**Parameters:**

**mode** (*int*) –

The type:

|   |   |
|---|---|
| *HAIR_MODE_LOCKED* | Locked mode |
| *HAIR_MODE_HIDDEN* | Hidden mode. |
| *HAIR_MODE_TIPS* | Tips mode. |
| *HAIR_MODE_POINTS* | Points mode. |
| *HAIR_MODE_GUIDES* | Guides mode. |
| *HAIR_MODE_ROOTS* | Roots mode. |
| *HAIR_MODE_VERTEX* | Vertex mode. |

### Selection Metrics <a id="c4d.modules.hair.HairSelectionTag-method-Selection-Metrics"></a>

#### `HairSelectionTag.GetCount(self)` <a id="c4d.modules.hair.HairSelectionTag.GetCount"></a>

Gets the count.

**Return type:** int

**Returns:** Number of elements.

#### `HairSelectionTag.GetSegments(self)` <a id="c4d.modules.hair.HairSelectionTag.GetSegments"></a>

Gets the segment count.

**Return type:** int

**Returns:** Number of segments.
