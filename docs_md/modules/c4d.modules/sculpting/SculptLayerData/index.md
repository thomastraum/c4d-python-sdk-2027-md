<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/sculpting/SculptLayerData/index.html -->

# c4d.modules.sculpting.SculptLayerData <a id="c4d-modules-sculpting-sculptlayerdata"></a>

## *class* `c4d.modules.sculpting.SculptLayerData` <a id="c4d.modules.sculpting.SculptLayerData"></a>

A [`SculptLayerData`](#c4d.modules.sculpting.SculptLayerData) node contains all the offset data and mask data for that layer at its subdivision level.

*New in version R15.037.*

Parent Class:

- [`c4d.BaseList2D`](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

## Overview <a id="overview"></a>

**Layer Data**

- [`SculptLayerData.ClearLayer()`](#c4d.modules.sculpting.SculptLayerData.ClearLayer): Clear all the offsets for this layer.
- [`SculptLayerData.GetPointCount()`](#c4d.modules.sculpting.SculptLayerData.GetPointCount): Get the number of points on the polygon object that this layer has.
- [`SculptLayerData.GetSubdivisionLevel()`](#c4d.modules.sculpting.SculptLayerData.GetSubdivisionLevel): Get the level that this layer contains data for.
- [`SculptLayerData.InitializeAllMaskData()`](#c4d.modules.sculpting.SculptLayerData.InitializeAllMaskData): Make sure all the data has been allocated to store all the mask data.
- [`SculptLayerData.InitializeAllPointData()`](#c4d.modules.sculpting.SculptLayerData.InitializeAllPointData): Make sure all the data has been allocated to store all the point data.

**Mask Data**

- [`SculptLayerData.AddToMask()`](#c4d.modules.sculpting.SculptLayerData.AddToMask): Adds the mask at the given point.
- [`SculptLayerData.ClearMask()`](#c4d.modules.sculpting.SculptLayerData.ClearMask): Clear all the mask data for this layer.
- [`SculptLayerData.GetMask()`](#c4d.modules.sculpting.SculptLayerData.GetMask): Get the value (between 0 and 1) of the mask at the given point *index*.
- [`SculptLayerData.HasMask()`](#c4d.modules.sculpting.SculptLayerData.HasMask): Check if this Layer has a mask applied to it.
- [`SculptLayerData.SetMask()`](#c4d.modules.sculpting.SculptLayerData.SetMask): Set the mask at the given point.

**Offset Editing**

- [`SculptLayerData.AddOffset()`](#c4d.modules.sculpting.SculptLayerData.AddOffset): Add to the existing offset value at the given point *index*.
- [`SculptLayerData.GetOffset()`](#c4d.modules.sculpting.SculptLayerData.GetOffset): Get the offset for the given point *index* on the layer.
- [`SculptLayerData.SetOffset()`](#c4d.modules.sculpting.SculptLayerData.SetOffset): Set the offset for the given point *index*.

**Undo Tracking**

- [`SculptLayerData.TouchMaskForUndo()`](#c4d.modules.sculpting.SculptLayerData.TouchMaskForUndo): Marks the masked point so that any modifications to the mask can be undone.
- [`SculptLayerData.TouchPointForUndo()`](#c4d.modules.sculpting.SculptLayerData.TouchPointForUndo): Mark the point so that any modifications to it can be undone.

## Members <a id="members"></a>

### Layer Data <a id="c4d.modules.sculpting.SculptLayerData-method-Layer-Data"></a>

#### `SculptLayerData.ClearLayer(self)` <a id="c4d.modules.sculpting.SculptLayerData.ClearLayer"></a>

Clear all the offsets for this layer.

#### `SculptLayerData.GetPointCount(self)` <a id="c4d.modules.sculpting.SculptLayerData.GetPointCount"></a>

Get the number of points on the polygon object that this layer has.

**Return type:** int

**Returns:** Number of points on the polygon object.

#### `SculptLayerData.GetSubdivisionLevel(self)` <a id="c4d.modules.sculpting.SculptLayerData.GetSubdivisionLevel"></a>

Get the level that this layer contains data for.

**Return type:** int

**Returns:** The subdivision level.

#### `SculptLayerData.InitializeAllMaskData(self)` <a id="c4d.modules.sculpting.SculptLayerData.InitializeAllMaskData"></a>

Make sure all the data has been allocated to store all the mask data.

> **Note:** If you are going to call [`SetMask()`](#c4d.modules.sculpting.SculptLayerData.SetMask) or [`AddToMask()`](#c4d.modules.sculpting.SculptLayerData.AddToMask) from multiple threads then the data needs to be initialized before these calls are made.

> **Note:** If you are not using multiple threads the calls to [`SetMask()`](#c4d.modules.sculpting.SculptLayerData.SetMask) and [`AddToMask()`](#c4d.modules.sculpting.SculptLayerData.AddToMask) will only allocate data if required.

#### `SculptLayerData.InitializeAllPointData(self)` <a id="c4d.modules.sculpting.SculptLayerData.InitializeAllPointData"></a>

Make sure all the data has been allocated to store all the point data.

> **Note:** If you are going to call [`SetOffset()`](#c4d.modules.sculpting.SculptLayerData.SetOffset) or [`AddOffset()`](#c4d.modules.sculpting.SculptLayerData.AddOffset) from multiple threads then the data needs to be initialized before these calls are made.

> **Note:** If you are not using multiple threads the calls to [`SetOffset()`](#c4d.modules.sculpting.SculptLayerData.SetOffset) and [`AddOffset()`](#c4d.modules.sculpting.SculptLayerData.AddOffset) will only allocate data if required.

### Mask Data <a id="c4d.modules.sculpting.SculptLayerData-method-Mask-Data"></a>

#### `SculptLayerData.AddToMask(self, index, mask)` <a id="c4d.modules.sculpting.SculptLayerData.AddToMask"></a>

Adds the mask at the given point. The value will be clamped between 0 and 1.

**Parameters:**

- **index** (*int*) – Index of the point on the polygon object.
- **mask** (*float*) – The amount to add to the existing mask.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayerData.GetPointCount).

#### `SculptLayerData.ClearMask(self)` <a id="c4d.modules.sculpting.SculptLayerData.ClearMask"></a>

Clear all the mask data for this layer.

#### `SculptLayerData.GetMask(self, index)` <a id="c4d.modules.sculpting.SculptLayerData.GetMask"></a>

Get the value (between 0 and 1) of the mask at the given point *index*.

**Parameters:** **index** (*int*) – Index of the point on the polygon object.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayerData.GetPointCount).

**Return type:** Optional[float]

**Returns:** The mask value for the given point, or **None** if there was no mask value at that point.

#### `SculptLayerData.HasMask(self)` <a id="c4d.modules.sculpting.SculptLayerData.HasMask"></a>

Check if this Layer has a mask applied to it.

**Return type:** bool

**Returns:** **True** if if there is mask data, otherwise **False**.

#### `SculptLayerData.SetMask(self, index, mask)` <a id="c4d.modules.sculpting.SculptLayerData.SetMask"></a>

Set the mask at the given point. The value will be clamped between 0 and 1.

**Parameters:**

- **index** (*int*) – Index of the point on the polygon object.
- **mask** (*float*) – The mask value to set.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayerData.GetPointCount).

### Offset Editing <a id="c4d.modules.sculpting.SculptLayerData-method-Offset-Editing"></a>

#### `SculptLayerData.AddOffset(self, index, offset)` <a id="c4d.modules.sculpting.SculptLayerData.AddOffset"></a>

Add to the existing offset value at the given point *index*.

> **Note:**
>
> Be sure to call `SculptObject.Update()` after all changes to the offsets have been made.  
> This will update the [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject) display.

**Parameters:**

- **index** (*int*) – Index of the point on the polygon object.
- **offset** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The offset to add.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayerData.GetPointCount).

#### `SculptLayerData.GetOffset(self, index)` <a id="c4d.modules.sculpting.SculptLayerData.GetOffset"></a>

Get the offset for the given point *index* on the layer.

**Parameters:** **index** (*int*) – Index of the point on the polygon object.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayerData.GetPointCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The offset of the point.

#### `SculptLayerData.SetOffset(self, index, offset)` <a id="c4d.modules.sculpting.SculptLayerData.SetOffset"></a>

Set the offset for the given point *index*.

> **Note:**
>
> Be sure to call `SculptObject.Update()` after all changes to the offets have been made.  
> This will update the [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject) display.

**Parameters:**

- **index** (*int*) – Index of the point on the polygon object.
- **offset** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The full offset to set.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayerData.GetPointCount).

### Undo Tracking <a id="c4d.modules.sculpting.SculptLayerData-method-Undo-Tracking"></a>

#### `SculptLayerData.TouchMaskForUndo(self, index)` <a id="c4d.modules.sculpting.SculptLayerData.TouchMaskForUndo"></a>

Marks the masked point so that any modifications to the mask can be undone.

> **Note:** Must be called after `SculptObject.StartUndo()`.

> **Warning:** This method cannot be called from multiple threads.

**Parameters:** **index** (*int*) – The index of the point on the layer.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayerData.GetPointCount).

#### `SculptLayerData.TouchPointForUndo(self, index)` <a id="c4d.modules.sculpting.SculptLayerData.TouchPointForUndo"></a>

Mark the point so that any modifications to it can be undone.

> **Note:** Must be called after `SculptObject.StartUndo()`.

> **Warning:** This method cannot be called from multiple threads.

**Parameters:** **index** (*int*) – The index of the point on the layer.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayerData.GetPointCount).
