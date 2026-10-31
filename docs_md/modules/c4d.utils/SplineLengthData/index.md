<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.utils/SplineLengthData/index.html -->

# c4d.utils.SplineLengthData <a id="c4d-utils-splinelengthdata"></a>

## *class* `c4d.utils.SplineLengthData` <a id="c4d.utils.SplineLengthData"></a>

## Overview <a id="overview"></a>

**Lifecycle Management**

- [`SplineLengthData.Free()`](#c4d.utils.SplineLengthData.Free): Called to free the spline.
- [`SplineLengthData.Init()`](#c4d.utils.SplineLengthData.Init): Initialize the spline length data object with a spline.

**Magic Methods**

- [`SplineLengthData.__init__()`](#c4d.utils.SplineLengthData.__init__)

**Spline Measurements**

- [`SplineLengthData.GetLength()`](#c4d.utils.SplineLengthData.GetLength): Returns the length of the spline data object.
- [`SplineLengthData.GetSegmentLength()`](#c4d.utils.SplineLengthData.GetSegmentLength): Get the length of the segment.
- [`SplineLengthData.UniformToNatural()`](#c4d.utils.SplineLengthData.UniformToNatural): Get the natural position along the spline.

## Members <a id="members"></a>

### Lifecycle Management <a id="c4d.utils.SplineLengthData-method-Lifecycle-Management"></a>

#### `SplineLengthData.Free(self)` <a id="c4d.utils.SplineLengthData.Free"></a>

Called to free the spline.

#### `SplineLengthData.Init(self, op, segment)` <a id="c4d.utils.SplineLengthData.Init"></a>

Initialize the spline length data object with a spline.

**Parameters:**

- **op** ([*c4d.SplineObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/SplineObject/index.md#c4d.SplineObject)) – The spline object to use.
- **segment** (*int*) – The segment of the spline.

**Raises:** **IndexError** – If the *segment* index is out of range : *0<=segment<*`SplineObject.GetSegmentCount()`.

### Magic Methods <a id="c4d.utils.SplineLengthData-method-Magic-Methods"></a>

#### `SplineLengthData.__init__(self)` <a id="c4d.utils.SplineLengthData.__init__"></a>

### Spline Measurements <a id="c4d.utils.SplineLengthData-method-Spline-Measurements"></a>

#### `SplineLengthData.GetLength(self)` <a id="c4d.utils.SplineLengthData.GetLength"></a>

Returns the length of the spline data object.

**Return type:** float

**Returns:** The length.

#### `SplineLengthData.GetSegmentLength(self, a, b)` <a id="c4d.utils.SplineLengthData.GetSegmentLength"></a>

Get the length of the segment.

**Parameters:**

- **a** (*int*) – Start of the segment.
- **b** (*int*) – End of the segment.

#### `SplineLengthData.UniformToNatural(self, t)` <a id="c4d.utils.SplineLengthData.UniformToNatural"></a>

Get the natural position along the spline.  
The uniform position is with respect to the actual length of the spline, whereas the natural position only cares about the interpolation of the curve parameter.

**Parameters:** **t** (*float*) – The uniform position along the spline.

**Return type:** float

**Returns:** The natural position in the segment.
