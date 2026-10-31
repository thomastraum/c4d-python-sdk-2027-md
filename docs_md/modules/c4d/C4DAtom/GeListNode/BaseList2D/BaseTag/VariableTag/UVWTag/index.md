<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/UVWTag/index.html -->

# c4d.UVWTag <a id="c4d-uvwtag"></a>

## *class* `c4d.UVWTag` <a id="c4d.UVWTag"></a>

Represents the UVW tag.  
Handles the UVW coordinates for textures.

> **Note:** When assigning a UVW tag to an object ensure the texture is set to UVW.

The instance object class of type *Tuvw*.

Parent Class:

- [`c4d.VariableTag`](../index.md#c4d.VariableTag)

## Overview <a id="overview"></a>

**Magic Methods**

- [`UVWTag.__init__()`](#c4d.UVWTag.__init__)

**Pin Point Selection**

- [`UVWTag.AddToPinSelection()`](#c4d.UVWTag.AddToPinSelection): Adds the point selection specified to the pin point selection.
- [`UVWTag.ClearPinSelection()`](#c4d.UVWTag.ClearPinSelection): Clears the pin point selection for this tag.
- [`UVWTag.GetPinSelection()`](#c4d.UVWTag.GetPinSelection): Obtains the current pin point selection for this tag.
- [`UVWTag.RemoveFromPinSelection()`](#c4d.UVWTag.RemoveFromPinSelection): Removes from the pin point selection the points in the selection specified.
- [`UVWTag.SetPinSelection()`](#c4d.UVWTag.SetPinSelection): Replaces the pin point selection for this tag with the point selection specified.

**UV Coordinate Editing**

- [`UVWTag.CpySlow()`](#c4d.UVWTag.CpySlow): Copy a UVW coordinate.
- [`UVWTag.GetSlow()`](#c4d.UVWTag.GetSlow): Get the UVW coordinate for a polygon.
- [`UVWTag.SetSlow()`](#c4d.UVWTag.SetSlow): Set the UVW coordinates of a polygon.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.UVWTag-method-Magic-Methods"></a>

#### `UVWTag.__init__(self, count)` <a id="c4d.UVWTag.__init__"></a>

**Parameters:** **count** (*int*) – The number of elements in the tag.

### Pin Point Selection <a id="c4d.UVWTag-method-Pin-Point-Selection"></a>

#### `UVWTag.AddToPinSelection(self, uvPointSelection)` <a id="c4d.UVWTag.AddToPinSelection"></a>

Adds the point selection specified to the pin point selection.

*New in version S22.114.*

**Parameters:** **uvPointSelection** ([*c4d.BaseSelect*](../../../../../../BaseSelect/index.md#c4d.BaseSelect)) – Pin selection to add.

**Returns:** True on success.

**Return type:** bool

#### `UVWTag.ClearPinSelection(self)` <a id="c4d.UVWTag.ClearPinSelection"></a>

Clears the pin point selection for this tag.

*New in version S22.114.*

#### `UVWTag.GetPinSelection(self)` <a id="c4d.UVWTag.GetPinSelection"></a>

Obtains the current pin point selection for this tag.

*New in version S22.114.*

**Returns:** A non-writable reference to the pin selection.

**Return type:** [c4d.BaseSelect](../../../../../../BaseSelect/index.md#c4d.BaseSelect)

#### `UVWTag.RemoveFromPinSelection(self, uvPointSelection)` <a id="c4d.UVWTag.RemoveFromPinSelection"></a>

Removes from the pin point selection the points in the selection specified.

*New in version S22.114.*

> **Note:** Points in the specified selection that are not part of the current pin point selection are simply ignored.

**Parameters:** **uvPointSelection** ([*c4d.BaseSelect*](../../../../../../BaseSelect/index.md#c4d.BaseSelect)) – Pin point selection to remove.

**Returns:** True on success.

**Return type:** bool

#### `UVWTag.SetPinSelection(self, uvPointSelection)` <a id="c4d.UVWTag.SetPinSelection"></a>

Replaces the pin point selection for this tag with the point selection specified.

*New in version S22.114.*

**Parameters:** **uvPointSelection** ([*c4d.BaseSelect*](../../../../../../BaseSelect/index.md#c4d.BaseSelect)) – New pin selection to set.

**Returns:** True on success.

**Return type:** bool

### UV Coordinate Editing <a id="c4d.UVWTag-method-UV-Coordinate-Editing"></a>

#### `UVWTag.CpySlow(self, i, srctag, src)` <a id="c4d.UVWTag.CpySlow"></a>

Copy a UVW coordinate.

**Parameters:**

- **i** (*int*) – The destinate polygon index in this UVWTag.
- **srctag** ([*c4d.UVWTag*](#c4d.UVWTag)) – The UVWTag for the source polygon.
- **src** (*int*) – The source polygon index in this UVWTag.

**Raises:** **IndexError** – If *i* is out of range (*0<=i<*`VariableTag.GetDataCount()`) for *self* and/or *src*.

#### `UVWTag.GetSlow(self, i)` <a id="c4d.UVWTag.GetSlow"></a>

Get the UVW coordinate for a polygon.

```python
>>> op
<c4d.PolygonObject object called Plane/Polygon with ID 5100 at 1694970385536>
>>> tag = op.GetTag(c4d.Tuvw)
>>> tag
<c4d.UVWTag object called UVW/UVW with ID 5671 at 1694956664000>
>>> for i in range(tag.GetDataCount()):
...     print(tag.GetSlow(i))
...
{'a': Vector(0, 1, 0), 'b': Vector(0, 0, 0), 'c': Vector(1, 0, 0), 'd': Vector(1, 1, 0)}
```

**Parameters:** **i** (*int*) – The index of the polygon to get the coordinates for.

**Raises:** **IndexError** – If *i* is out of range : *0<=i<*`VariableTag.GetDataCount()`.

**Return type:** dict{**a**: [`Vector`](../../../../../../Vector/index.md#c4d.Vector), **b**: [`Vector`](../../../../../../Vector/index.md#c4d.Vector), **c**: [`Vector`](../../../../../../Vector/index.md#c4d.Vector), **d**: [`Vector`](../../../../../../Vector/index.md#c4d.Vector)}

**Returns:** The UVW coordinates.

#### `UVWTag.SetSlow(self, i, a, b, c, d)` <a id="c4d.UVWTag.SetSlow"></a>

Set the UVW coordinates of a polygon.

**Parameters:**

- **i** (*int*) – The index of the polygon to set the coordinates for.
- **a** ([*c4d.Vector*](../../../../../../Vector/index.md#c4d.Vector)) – The coordinate of the first point.
- **b** ([*c4d.Vector*](../../../../../../Vector/index.md#c4d.Vector)) – The coordinate of the second point.
- **c** ([*c4d.Vector*](../../../../../../Vector/index.md#c4d.Vector)) – The coordinate of the third point.
- **d** ([*c4d.Vector*](../../../../../../Vector/index.md#c4d.Vector)) – The coordinate of the fourth point.

**Raises:** **IndexError** – If *i* is out of range : *0<=i<*`VariableTag.GetDataCount()`.
