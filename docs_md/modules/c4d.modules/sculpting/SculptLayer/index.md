<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/sculpting/SculptLayer/index.html -->

# c4d.modules.sculpting.SculptLayer <a id="c4d-modules-sculpting-sculptlayer"></a>

## *class* `c4d.modules.sculpting.SculptLayer` <a id="c4d.modules.sculpting.SculptLayer"></a>

A [`SculptLayer`](#c4d.modules.sculpting.SculptLayer) can contain one or more [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) children.

*New in version R15.037.*

Parent Class:

- [`c4d.modules.sculpting.SculptLayerBase`](../SculptLayerBase/index.md#c4d.modules.sculpting.SculptLayerBase)

## Overview <a id="overview"></a>

**Layer Lifecycle**

- [`SculptLayer.ClearLayer()`](#c4d.modules.sculpting.SculptLayer.ClearLayer): Clear all the offset data for this layer.
- [`SculptLayer.GetCurrentSculptLayer()`](#c4d.modules.sculpting.SculptLayer.GetCurrentSculptLayer): Get the currently used layer data.
- [`SculptLayer.GetFirstSculptLayer()`](#c4d.modules.sculpting.SculptLayer.GetFirstSculptLayer): Get the first layer data for this layer.
- [`SculptLayer.IsBaseLayer()`](#c4d.modules.sculpting.SculptLayer.IsBaseLayer): Check if this layer is the Base Object layer in which case it will have more than one [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) children.

**Mask Controls**

- [`SculptLayer.AddToMask()`](#c4d.modules.sculpting.SculptLayer.AddToMask): Add to the existing mask value at this point (between 0 and 1).
- [`SculptLayer.ClearMask()`](#c4d.modules.sculpting.SculptLayer.ClearMask): Clear the mask data for the layer.
- [`SculptLayer.GetMask()`](#c4d.modules.sculpting.SculptLayer.GetMask): Get the mask value for the point (between 0 and 1).
- [`SculptLayer.HasMask()`](#c4d.modules.sculpting.SculptLayer.HasMask): Check if this layer has a mask at the current subdivision level.
- [`SculptLayer.InitializeAllMaskData()`](#c4d.modules.sculpting.SculptLayer.InitializeAllMaskData): Make sure all the data has been allocated to store all the mask data.
- [`SculptLayer.IsMaskEnabled()`](#c4d.modules.sculpting.SculptLayer.IsMaskEnabled): Check if the mask is enabled for this layer at the current subdivision level.
- [`SculptLayer.SetMask()`](#c4d.modules.sculpting.SculptLayer.SetMask): Set the mask value for the point (between 0 and 1).
- [`SculptLayer.SetMaskEnabled()`](#c4d.modules.sculpting.SculptLayer.SetMaskEnabled): Set the mask enabled *state* for the current layer data at this current subdivision level.
- [`SculptLayer.TouchMaskForUndo()`](#c4d.modules.sculpting.SculptLayer.TouchMaskForUndo): Mark the masked point so that any modifications to the mask can be undone.

**Point Offsets**

- [`SculptLayer.AddOffset()`](#c4d.modules.sculpting.SculptLayer.AddOffset): Add an offset vector to the existing offset for the given point on the layer.
- [`SculptLayer.GetOffset()`](#c4d.modules.sculpting.SculptLayer.GetOffset): Get the offset value for the point *index* on the layer.
- [`SculptLayer.GetPointCount()`](#c4d.modules.sculpting.SculptLayer.GetPointCount): Get the number of points this layer has.
- [`SculptLayer.InitializeAllPointData()`](#c4d.modules.sculpting.SculptLayer.InitializeAllPointData): Make sure all the data has been allocated to store all the point data.
- [`SculptLayer.SetOffset()`](#c4d.modules.sculpting.SculptLayer.SetOffset): Set the offset vector for the given point on the layer.
- [`SculptLayer.TouchPointForUndo()`](#c4d.modules.sculpting.SculptLayer.TouchPointForUndo): Mark the point so that any modifications to it can be undone.

## Members <a id="members"></a>

### Layer Lifecycle <a id="c4d.modules.sculpting.SculptLayer-method-Layer-Lifecycle"></a>

#### `SculptLayer.ClearLayer(self)` <a id="c4d.modules.sculpting.SculptLayer.ClearLayer"></a>

Clear all the offset data for this layer.

> **Note:** This method will get the correct [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) for this layer and call the corresponding method for it.

#### `SculptLayer.GetCurrentSculptLayer(self)` <a id="c4d.modules.sculpting.SculptLayer.GetCurrentSculptLayer"></a>

Get the currently used layer data.

> **Note:**
>
> In the case of the Base Object layer it will get the data for the current subdivision level.  
> For all other layers it will return the same as [`GetFirstSculptLayer()`](#c4d.modules.sculpting.SculptLayer.GetFirstSculptLayer).

**Return type:** [c4d.modules.sculpting.SculptLayerData](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData)

**Returns:** The current sculpt layer data.

#### `SculptLayer.GetFirstSculptLayer(self)` <a id="c4d.modules.sculpting.SculptLayer.GetFirstSculptLayer"></a>

Get the first layer data for this layer.  
The Base Object layer will have more than one, other layers only have 1.

**Return type:** [c4d.modules.sculpting.SculptLayerData](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData)

**Returns:** The first sculpt layer data.

#### `SculptLayer.IsBaseLayer(self)` <a id="c4d.modules.sculpting.SculptLayer.IsBaseLayer"></a>

Check if this layer is the Base Object layer in which case it will have more than one [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) children.

**Return type:** bool

**Returns:** **True** if this layer is the Base Object layer, **False** if it is a regular layer.

### Mask Controls <a id="c4d.modules.sculpting.SculptLayer-method-Mask-Controls"></a>

#### `SculptLayer.AddToMask(self, index, mask)` <a id="c4d.modules.sculpting.SculptLayer.AddToMask"></a>

Add to the existing mask value at this point (between 0 and 1).

> **Note:** This method will get the correct [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) for this layer and call the corresponding method for it.

**Parameters:**

- **index** (*int*) – The index of the point on the layer.
- **mask** (*float*) – The value to add to the mask.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayer.GetPointCount).

#### `SculptLayer.ClearMask(self)` <a id="c4d.modules.sculpting.SculptLayer.ClearMask"></a>

Clear the mask data for the layer.

> **Note:** This method will get the correct [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) for this layer and call the corresponding method for it.

#### `SculptLayer.GetMask(self, index)` <a id="c4d.modules.sculpting.SculptLayer.GetMask"></a>

Get the mask value for the point (between 0 and 1).

> **Note:** This method will get the correct [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) for this layer and call the corresponding method for it.

**Parameters:** **index** (*int*) – The index of the point on the layer.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayer.GetPointCount).

**Return type:** float

**Returns:** The mask value for the given point.

#### `SculptLayer.HasMask(self)` <a id="c4d.modules.sculpting.SculptLayer.HasMask"></a>

Check if this layer has a mask at the current subdivision level.

> **Note:** This method will get the correct [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) for this layer and call the corresponding method for it.

**Return type:** bool

**Returns:** **True** if there is a mask, otherwise **False**.

#### `SculptLayer.InitializeAllMaskData(self)` <a id="c4d.modules.sculpting.SculptLayer.InitializeAllMaskData"></a>

Make sure all the data has been allocated to store all the mask data.

> **Note:** If you are going to call [`SetMask()`](#c4d.modules.sculpting.SculptLayer.SetMask) or [`AddToMask()`](#c4d.modules.sculpting.SculptLayer.AddToMask) from multiple threads then the data needs to be initialized before these calls are made.

> **Note:** If you are not using multiple threads the calls to [`SetMask()`](#c4d.modules.sculpting.SculptLayer.SetMask) and [`AddToMask()`](#c4d.modules.sculpting.SculptLayer.AddToMask) will only allocate data if required.

#### `SculptLayer.IsMaskEnabled(self)` <a id="c4d.modules.sculpting.SculptLayer.IsMaskEnabled"></a>

Check if the mask is enabled for this layer at the current subdivision level.

> **Note:** This method will get the correct [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) for this layer and call the corresponding method for it.

**Return type:** bool

**Returns:** *True** if mask is enabled, otherwise **False**.

#### `SculptLayer.SetMask(self, index, mask)` <a id="c4d.modules.sculpting.SculptLayer.SetMask"></a>

Set the mask value for the point (between 0 and 1).

> **Note:** This method will get the correct [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) for this layer and call the corresponding method for it.

**Parameters:**

- **index** (*int*) – The index of the point on the layer.
- **mask** (*float*) – The mask value for the given point.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayer.GetPointCount).

#### `SculptLayer.SetMaskEnabled(self, state)` <a id="c4d.modules.sculpting.SculptLayer.SetMaskEnabled"></a>

Set the mask enabled *state* for the current layer data at this current subdivision level.

> **Note:** This method will get the correct [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) for this layer and call the corresponding method for it.

**Parameters:** **state** (*bool*) – The state of the mask.

#### `SculptLayer.TouchMaskForUndo(self, index)` <a id="c4d.modules.sculpting.SculptLayer.TouchMaskForUndo"></a>

Mark the masked point so that any modifications to the mask can be undone.

> **Note:** Must be called after `SculptObject.StartUndo()`.

> **Warning:** This method cannot be called from multiple threads.

**Parameters:** **index** (*int*) – The index of the point on the layer.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayer.GetPointCount).

### Point Offsets <a id="c4d.modules.sculpting.SculptLayer-method-Point-Offsets"></a>

#### `SculptLayer.AddOffset(self, index, offset)` <a id="c4d.modules.sculpting.SculptLayer.AddOffset"></a>

Add an offset vector to the existing offset for the given point on the layer.

> **Note:** This method will get the correct [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) for this layer and call the corresponding method for it.

> **Warning:**
>
> Be sure to call `SculptObject.Update()` after all changes to the offets have been made.  
> This will update the [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject) display.

**Parameters:**

- **index** (*int*) – The index of the point on the layer.
- **offset** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The offset to add.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayer.GetPointCount).

#### `SculptLayer.GetOffset(self, index)` <a id="c4d.modules.sculpting.SculptLayer.GetOffset"></a>

Get the offset value for the point *index* on the layer. This method will get the correct [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) for this layer and call the corresponding method for it.

**Parameters:** **index** (*int*) – The index of the point on the layer.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayer.GetPointCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The offset of the point.

#### `SculptLayer.GetPointCount(self)` <a id="c4d.modules.sculpting.SculptLayer.GetPointCount"></a>

Get the number of points this layer has.

> **Note:** The point count will be the same as the number of points on the [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) for the subdivision level that this layer is at.

**Return type:** int

**Returns:** The number of points.

#### `SculptLayer.InitializeAllPointData(self)` <a id="c4d.modules.sculpting.SculptLayer.InitializeAllPointData"></a>

Make sure all the data has been allocated to store all the point data.

> **Note:** If you are going to call [`SetOffset()`](#c4d.modules.sculpting.SculptLayer.SetOffset) or [`AddOffset()`](#c4d.modules.sculpting.SculptLayer.AddOffset) from multiple threads then the data needs to be initialized before these calls are made.

> **Note:** If you are not using multiple threads the calls to [`SetOffset()`](#c4d.modules.sculpting.SculptLayer.SetOffset) and [`AddOffset()`](#c4d.modules.sculpting.SculptLayer.AddOffset) will only allocate data if required.

#### `SculptLayer.SetOffset(self, index, offset)` <a id="c4d.modules.sculpting.SculptLayer.SetOffset"></a>

Set the offset vector for the given point on the layer.

> **Note:** This method will get the correct [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) for this layer and call the corresponding method for it.

> **Warning:**
>
> Be sure to call `SculptObject.Update()` after all changes to the offets have been made.  
> This will update the [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject) display.

**Parameters:**

- **index** (*int*) – The index of the point on the layer.
- **offset** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The full offset to set.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayer.GetPointCount).

#### `SculptLayer.TouchPointForUndo(self, index)` <a id="c4d.modules.sculpting.SculptLayer.TouchPointForUndo"></a>

Mark the point so that any modifications to it can be undone.

> **Note:** Must be called after `SculptObject.StartUndo()`.

> **Warning:** This method cannot be called from multiple threads.

**Parameters:** **index** (*int*) – The index of the point on the layer.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptLayer.GetPointCount).
