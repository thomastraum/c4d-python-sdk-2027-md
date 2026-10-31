<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/NormalTag/index.html -->

# c4d.NormalTag <a id="c4d-normaltag"></a>

## *class* `c4d.NormalTag` <a id="c4d.NormalTag"></a>

Tag which handles normal buffers.

The instance object class of type *Tnormal*.

It consists of a list of integer.

> **Note:** Contains *12* times more elements than `VariableTag.GetDataCount()` returns.

Parent Class:

- [`c4d.VariableTag`](../index.md#c4d.VariableTag)

## Overview <a id="overview"></a>

- [`NormalTag.Copy()`](#c4d.NormalTag.Copy): Copies point normals.
- [`NormalTag.Get()`](#c4d.NormalTag.Get): Gets the point normals for a polygon.
- [`NormalTag.Set()`](#c4d.NormalTag.Set): Sets the point normals for a polygon.

**Data Access**

- [`NormalTag.GetDataAddressR()`](#c4d.NormalTag.GetDataAddressR): Gets a handle to the read-only point normal data.
- [`NormalTag.GetDataAddressW()`](#c4d.NormalTag.GetDataAddressW): Gets a handle to the writable point normal data.

**Magic Methods**

- [`NormalTag.__init__()`](#c4d.NormalTag.__init__)

## Members <a id="members"></a>

### Data Manipulation <a id="c4d.NormalTag-staticmethod-Data-Manipulation"></a>

#### *static* `NormalTag.Copy(destptr, dst, srcptr, src)` <a id="c4d.NormalTag.Copy"></a>

Copies point normals.

*New in version R26.*

**Parameters:**

- **destptr** (*PyCObject*) – The handle to the destination point normal data. The PyCObject returned by `NormalTag.GetDataAddressW()`.
- **dst** (*int*) – The destination polygon index in the destination data destptr.
- **srcptr** (*PyCObject*) – The handle to the source point normal data. The PyCObject returned by `NormalTag.GetDataAddressR()`.
- **src** (*int*) – The source polygon index in the source data srcptr.

#### *static* `NormalTag.Get(data, i)` <a id="c4d.NormalTag.Get"></a>

Gets the point normals for a polygon.

*New in version R26.*

**Parameters:**

- **data** (*PyCObject*) – The handle to the point normal data. The PyCObject returned by `NormalTag.GetDataAddressR()`.
- **i** (*int*) – The index of the polygon to get the point normals for.

**Returns:** The assigned the point normals.

**Return type:** Dict[**a**: c4d.Vector, **b**: c4d.Vector, **c**: c4d.Vector, **c**: c4d.Vector]

#### *static* `NormalTag.Set(data, i, s)` <a id="c4d.NormalTag.Set"></a>

Sets the point normals for a polygon.

*New in version R26.*

**Parameters:**

- **data** (*PyCObject*) – The handle to the point normal data. The PyCObject returned by `NormalTag.GetDataAddressW()`.
- **i** (*int*) – The index of the polygon to set the point normals for.
- **s** (Dict[**a**: c4d.Vector, **b**: c4d.Vector, **c**: c4d.Vector, **c**: c4d.Vector]) – The point normals to set.

### Data Access <a id="c4d.NormalTag-method-Data-Access"></a>

#### `NormalTag.GetDataAddressR(self)` <a id="c4d.NormalTag.GetDataAddressR"></a>

Gets a handle to the read-only point normal data.

*New in version R26.*

**Returns:** The read-only point normal data.

**Return type:** PyCObject.

#### `NormalTag.GetDataAddressW(self)` <a id="c4d.NormalTag.GetDataAddressW"></a>

Gets a handle to the writable point normal data.

*New in version R26.*

**Returns:** The writable point normal data.

**Return type:** PyCObject.

### Magic Methods <a id="c4d.NormalTag-method-Magic-Methods"></a>

#### `NormalTag.__init__(self, count)` <a id="c4d.NormalTag.__init__"></a>

**Parameters:** **count** (*int*) – The number of elements in the tag.
