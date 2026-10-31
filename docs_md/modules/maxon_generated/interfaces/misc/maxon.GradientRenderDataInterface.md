<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/misc/maxon.GradientRenderDataInterface.html -->

# maxon.GradientRenderDataInterface <a id="maxon-gradientrenderdatainterface"></a>

## Description <a id="module-maxon.GradientRenderDataInterface"></a><a id="description"></a>

## Inheritance diagram <a id="inheritance-diagram"></a>

Child Class:

- [`maxon.GradientRenderData`](maxon.GradientRenderData.md#module-maxon.GradientRenderData)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`CalcGradientPixel`](#maxon.GradientRenderDataInterface.CalcGradientPixel)(pos) | Calculates a gradient pixel. |
| [`Compare`](#maxon.GradientRenderDataInterface.Compare)(arg2) | Compares this with another GradientRenderData value. |
| [`GetHashCode`](#maxon.GradientRenderDataInterface.GetHashCode)() | Gets the checksum of the gradient render data. |
| [`GetKnot`](#maxon.GradientRenderDataInterface.GetKnot)(index) | Gets a pointer to the knot at #index. |
| [`GetKnotCount`](#maxon.GradientRenderDataInterface.GetKnotCount)() | Gets the number of knots for GetRenderKnot() |
| [`GetKnots`](#maxon.GradientRenderDataInterface.GetKnots)() | Gets a read only reference to internal knot list for fast access. |

## Methods Definition <a id="methods-definition"></a>

### `GradientRenderDataInterface.CalcGradientPixel(pos)` <a id="maxon.GradientRenderDataInterface.CalcGradientPixel"></a>

Calculates a gradient pixel.

**Parameters:** **pos** (*float*) – The X position.

**Returns:** The calculated gradient pixel.

**Return type:** [`maxon.Color`](../../datatypes/vec_col_mat/maxon.Color.md#module-maxon.Color)

### `GradientRenderDataInterface.Compare(arg2)` <a id="maxon.GradientRenderDataInterface.Compare"></a>

Compares this with another GradientRenderData value.

**Parameters:** **arg2** ([`maxon.GradientRenderDataInterface`](#module-maxon.GradientRenderDataInterface)) – The other GradientRenderData value to compare with.

**Returns:** The comparison result.

**Return type:**

`maxon.COMPARERESULT`

### `GradientRenderDataInterface.GetHashCode()` <a id="maxon.GradientRenderDataInterface.GetHashCode"></a>

Gets the checksum of the gradient render data.

**Returns:** The checksum of the gradient render data.

**Return type:** int

### `GradientRenderDataInterface.GetKnot(index)` <a id="maxon.GradientRenderDataInterface.GetKnot"></a>

Gets a pointer to the knot at #index.

**Parameters:** **index** (*int*) – The knot index. 0 <= #index < GetKnotCount()

**Returns:** The render knot at #index.

**Return type:** [`maxon.GradientKnot`](maxon.GradientKnot.md#module-maxon.GradientKnot)

### `GradientRenderDataInterface.GetKnotCount()` <a id="maxon.GradientRenderDataInterface.GetKnotCount"></a>

Gets the number of knots for GetRenderKnot()

**Returns:** The render knot count.

**Return type:** int

### `GradientRenderDataInterface.GetKnots()` <a id="maxon.GradientRenderDataInterface.GetKnots"></a>

Gets a read only reference to internal knot list for fast access.

**Returns:** The knot list.

**Return type:** [`maxon.BaseArray`](../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.GradientKnot`](maxon.GradientKnot.md#module-maxon.GradientKnot)]
