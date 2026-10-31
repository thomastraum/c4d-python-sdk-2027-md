<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/BaseSelect/index.html -->

# c4d.BaseSelect <a id="c4d-baseselect"></a>

## *class* `c4d.BaseSelect` <a id="c4d.BaseSelect"></a>

This class is used to keep track of point and polygon selections.  
Each method will raise an exception when a host object is established, but not alive anymore.

## Overview <a id="overview"></a>

**Copying And Cloning**

- [`BaseSelect.CopyTo()`](#c4d.BaseSelect.CopyTo): Copy the selection elements in this selection object to another BaseSelect.
- [`BaseSelect.GetClone()`](#c4d.BaseSelect.GetClone): Make a duplicate of this selection object with its elements.

**File Serialization**

- [`BaseSelect.Read()`](#c4d.BaseSelect.Read): Reads a selection from a file.
- [`BaseSelect.Write()`](#c4d.BaseSelect.Write): Saves the selection to a file.

**Magic Methods**

- [`BaseSelect.__init__()`](#c4d.BaseSelect.__init__): Initializes a new base selection.

**Selection Editing**

- [`BaseSelect.Deselect()`](#c4d.BaseSelect.Deselect): Deselects an element.
- [`BaseSelect.DeselectAll()`](#c4d.BaseSelect.DeselectAll): Deselect all elements.
- [`BaseSelect.Select()`](#c4d.BaseSelect.Select): Selects an element.
- [`BaseSelect.SelectAll()`](#c4d.BaseSelect.SelectAll): Selects all elements within the given range.
- [`BaseSelect.SetAll()`](#c4d.BaseSelect.SetAll): Set all selected elements from a list.
- [`BaseSelect.Toggle()`](#c4d.BaseSelect.Toggle): Toggles the selection state of an element.
- [`BaseSelect.ToggleAll()`](#c4d.BaseSelect.ToggleAll): Toggle the selection state of all elements in the given range.

**Selection Inspection**

- [`BaseSelect.FindSegment()`](#c4d.BaseSelect.FindSegment): Returns which segment contains the element *num*.
- [`BaseSelect.GetAll()`](#c4d.BaseSelect.GetAll): Returns all selected elements in a list.
- [`BaseSelect.GetCount()`](#c4d.BaseSelect.GetCount): Get the number of selected elements.
- [`BaseSelect.GetLastElement()`](#c4d.BaseSelect.GetLastElement): Returns the last element.
- [`BaseSelect.GetRange()`](#c4d.BaseSelect.GetRange): Returns the selected elements contained in a segment.
- [`BaseSelect.GetSegments()`](#c4d.BaseSelect.GetSegments): Get the number of segments that contain elements.
- [`BaseSelect.IsSelected()`](#c4d.BaseSelect.IsSelected): Get the selection state of an element.

**Selection Set Operations**

- [`BaseSelect.Cross()`](#c4d.BaseSelect.Cross): Intersects all elements in *src*.
- [`BaseSelect.DeselectFrom()`](#c4d.BaseSelect.DeselectFrom): Deselects all elements that are selected in *src*.
- [`BaseSelect.Merge()`](#c4d.BaseSelect.Merge): Selects all elements that are selected in *src*.

**State And Lifetime**

- [`BaseSelect.GetDirty()`](#c4d.BaseSelect.GetDirty): Returns the dirty counter of the selection.
- [`BaseSelect.HostAlive()`](#c4d.BaseSelect.HostAlive): Returns if the host object is still alive.

## Members <a id="members"></a>

### Copying And Cloning <a id="c4d.BaseSelect-method-Copying-And-Cloning"></a>

#### `BaseSelect.CopyTo(self, dest)` <a id="c4d.BaseSelect.CopyTo"></a>

Copy the selection elements in this selection object to another BaseSelect.

**Parameters:** **dest** ([*c4d.BaseSelect*](#c4d.BaseSelect)) – The destination selections object.

**Return type:** bool

**Returns:** Success of copying the selection elements.

#### `BaseSelect.GetClone(self)` <a id="c4d.BaseSelect.GetClone"></a>

Make a duplicate of this selection object with its elements.

**Return type:** [c4d.BaseSelect](#c4d.BaseSelect)

**Returns:** The clone object.

### File Serialization <a id="c4d.BaseSelect-method-File-Serialization"></a>

#### `BaseSelect.Read(self, hf)` <a id="c4d.BaseSelect.Read"></a>

Reads a selection from a file.

**Parameters:** **hf** ([*c4d.storage.HyperFile*](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile)) – The hyperfile to read from.

**Return type:** bool

**Returns:** True if successful, otherwise False.

#### `BaseSelect.Write(self, hf)` <a id="c4d.BaseSelect.Write"></a>

Saves the selection to a file.

**Parameters:** **hf** ([*c4d.storage.HyperFile*](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile)) – The hyperfile to write to.

### Magic Methods <a id="c4d.BaseSelect-method-Magic-Methods"></a>

#### `BaseSelect.__init__(self)` <a id="c4d.BaseSelect.__init__"></a>

Initializes a new base selection.

### Selection Editing <a id="c4d.BaseSelect-method-Selection-Editing"></a>

#### `BaseSelect.Deselect(self, num)` <a id="c4d.BaseSelect.Deselect"></a>

Deselects an element.

**Parameters:** **num** (*int*) – The element index to deselect.

**Return type:** bool

**Returns:** **True** if the element was already deselected.

#### `BaseSelect.DeselectAll(self)` <a id="c4d.BaseSelect.DeselectAll"></a>

Deselect all elements.

**Return type:** bool

**Returns:** Success of deselecting all elements.

#### `BaseSelect.Select(self, num)` <a id="c4d.BaseSelect.Select"></a>

Selects an element.

**Parameters:** **num** (*int*) – The element index to select.

**Return type:** bool

**Returns:** **True** if the element was already selected.

#### `BaseSelect.SelectAll(self, max, min=0, deselectAll=True)` <a id="c4d.BaseSelect.SelectAll"></a>

Selects all elements within the given range.

> **Note:** All previous selections are cleared.

> **Warning:** *min* and *max* parameters are swapped compared to the C++ API version and *min* gets a default value of *0*.

Here is an example showing how to select all the edges of a [`PolygonObject`](../C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject).

```python
import c4d

def main():
    nbr = c4d.utils.Neighbor()
    nbr.Init(op) # Initialize neighbor with a polygon object

    edges = c4d.BaseSelect()
    edges.SelectAll(nbr.GetEdgeCount()-1) # Select all edges in the range [0, nbr.GetEdgeCount()]

    op.SetSelectedEdges(nbr, edges, c4d.EDGESELECTIONTYPE_SELECTION) # Select edges from our edges selection
    c4d.EventAdd() # Update Cinema 4D

if __name__ == '__main__':
    main()
```

**Parameters:**

- **max** (*int*) – The last element in the range to select.

- **min** (*int*) – The first element in the range to select. Default to *0*.

- **deselectAll** (*bool*) –

  *New in version R17.048.*

  Deselects all previously selected elements before creating the new selection (equivalent to **SELECTION_NEW**).

**Return type:** bool

**Returns:** Success of selecting the elements.

#### `BaseSelect.SetAll(self, states)` <a id="c4d.BaseSelect.SetAll"></a>

Set all selected elements from a list.  
The elements in the list are interpreted as boolean: *0* means the element is *unselected*, and *1* means it is *selected*.

> **Note:** The old selection will be completely overridden.

**Parameters:** **states** (*List*[*int*]) – A list of elements to select.

**Return type:** bool

**Returns:** Success of selecting the elements.

#### `BaseSelect.Toggle(self, num)` <a id="c4d.BaseSelect.Toggle"></a>

Toggles the selection state of an element.

**Parameters:** **num** (*int*) – The index of the element to toggle.

**Return type:** bool

**Returns:** Success of changing the selection state of the element.

#### `BaseSelect.ToggleAll(self, min, max)` <a id="c4d.BaseSelect.ToggleAll"></a>

Toggle the selection state of all elements in the given range.

**Parameters:**

- **min** (*int*) – The first element to toggle.
- **max** (*int*) – The last element to toggle in the range.

**Return type:** bool

**Returns:** Success of changing the selection state.

### Selection Inspection <a id="c4d.BaseSelect-method-Selection-Inspection"></a>

#### `BaseSelect.FindSegment(self, num)` <a id="c4d.BaseSelect.FindSegment"></a>

Returns which segment contains the element *num*.

*New in version R19.*

**Parameters:** **num** (*int*) – The index of the element.

**Return type:** int

**Returns:** The found segment index. *-1* if no segment was found.

#### `BaseSelect.GetAll(self, max)` <a id="c4d.BaseSelect.GetAll"></a>

Returns all selected elements in a list.

**Parameters:** **max** (*int*) – The maximum number of elements to place into the array.

**Return type:** List[int]

**Returns:** The list

#### `BaseSelect.GetCount(self)` <a id="c4d.BaseSelect.GetCount"></a>

Get the number of selected elements.

**Return type:** int

**Returns:** The number of selected elements.

#### `BaseSelect.GetLastElement(self)` <a id="c4d.BaseSelect.GetLastElement"></a>

Returns the last element.

**Return type:** int

**Returns:** Last element.

#### `BaseSelect.GetRange(self, seg, max)` <a id="c4d.BaseSelect.GetRange"></a>

Returns the selected elements contained in a segment.  
See `BaseSelect.GetSegments()`.

*New in version R19.*

**Parameters:**

- **seg** (*int*) – The segment to get the elements for: 0 <= *seg* < [`GetSegments()`](#c4d.BaseSelect.GetSegments)

- **max** (*int*) –

  The maximum value for the returned elements numbers.  
  Usually pass `PolygonObject.GetPolygonCount()` or `PointObject.GetPointCount()` or the edge count of the object.  
  The method makes sure they are < *max*.

**Return type:** Optional[Tuple[int,int]]

**Returns:**

The index of the first and last selected elements in the given segment.  
If the segment has a length of one, the same if will be set for the first and last entry in the tuple.  
**None** if the function failed.

#### `BaseSelect.GetSegments(self)` <a id="c4d.BaseSelect.GetSegments"></a>

Get the number of segments that contain elements.  
For example: the selections 0..4, 6..7, 9..12 would be three segments.  
This method would return 3 and [`GetCount()`](#c4d.BaseSelect.GetCount) would return 11.

**Return type:** int

**Returns:** The number of selected segments.

#### `BaseSelect.IsSelected(self, num)` <a id="c4d.BaseSelect.IsSelected"></a>

Get the selection state of an element.

To efficiently go through selections use the following code.

```python
bs = op.GetPointS()
sel = bs.GetAll(op.GetPointCount())
for index, selected in enumerate(sel):
    if not selected:
        continue
    print(f"Index {index} is selected")
```

This is faster than.

```python
bs = op.GetPointS()
for index in range(op.GetPointCount()):
    if bs.IsSelected(index):
        print(f"Index {index} is selected")
```

**Parameters:** **num** (*int*) – The element index to select.

**Return type:** bool

**Returns:** **True** if the element was already selected.

### Selection Set Operations <a id="c4d.BaseSelect-method-Selection-Set-Operations"></a>

#### `BaseSelect.Cross(self, src)` <a id="c4d.BaseSelect.Cross"></a>

Intersects all elements in *src*.

*New in version R19.*

**Parameters:** **src** ([*c4d.BaseSelect*](#c4d.BaseSelect)) – The source selection object.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `BaseSelect.DeselectFrom(self, src)` <a id="c4d.BaseSelect.DeselectFrom"></a>

Deselects all elements that are selected in *src*.

> **Note:** For C++ developers: This function is redirected to **Bool Deselect(const BaseSelect *src)**

**Parameters:** **src** ([*c4d.BaseSelect*](#c4d.BaseSelect)) – The source selection object.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `BaseSelect.Merge(self, src)` <a id="c4d.BaseSelect.Merge"></a>

Selects all elements that are selected in *src*.

**Parameters:** **src** ([*c4d.BaseSelect*](#c4d.BaseSelect)) – The source selection object.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### State And Lifetime <a id="c4d.BaseSelect-method-State-And-Lifetime"></a>

#### `BaseSelect.GetDirty(self)` <a id="c4d.BaseSelect.GetDirty"></a>

Returns the dirty counter of the selection.  
This counter is increased every time a function is called that changes the selection.

**Return type:** int

**Returns:** Dirty counter.

#### `BaseSelect.HostAlive(self)` <a id="c4d.BaseSelect.HostAlive"></a>

Returns if the host object is still alive.

**Return type:** int

**Returns:**

- **2** if the instance has no host object.
- **1** if the host object is alive if set.
- **0** if the object is not alive.
