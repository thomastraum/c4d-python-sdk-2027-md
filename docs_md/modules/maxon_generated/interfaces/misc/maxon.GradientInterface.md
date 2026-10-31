<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/misc/maxon.GradientInterface.html -->

# maxon.GradientInterface <a id="maxon-gradientinterface"></a>

## Description <a id="module-maxon.GradientInterface"></a><a id="description"></a>

This is the interface for the Gradient data type.  
The data is reference-counted and a copy will automatically be created if a non-const function is called.  
Alpha Gradients ONLY set Brightness, Color is always 1.0 while regular Gradients can set Brightness & Color.

## Inheritance diagram <a id="inheritance-diagram"></a>

Child Class:

- [`maxon.Gradient`](maxon.Gradient.md#module-maxon.Gradient)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Compare`](#maxon.GradientInterface.Compare)(arg2) | Compares this with another gradient. |
| [`ConvertToAlphaGradient`](#maxon.GradientInterface.ConvertToAlphaGradient)() | Converts the current gradient to an alpha gradient. |
| [`DescribeIO`](#maxon.GradientInterface.DescribeIO)(stream) | Describes all elements of this class for I/O operations. |
| [`DistributeKnots`](#maxon.GradientInterface.DistributeKnots)() | Distributes the knots evenly. |
| [`DoubleKnots`](#maxon.GradientInterface.DoubleKnots)() | Doubles the knots. |
| [`Flush`](#maxon.GradientInterface.Flush)() | Flushes all the knots. |
| [`GetAlphaGradient`](#maxon.GradientInterface.GetAlphaGradient)() | Returns the internal alpha gradient as read-only. |
| [`GetHashCode`](#maxon.GradientInterface.GetHashCode)() | Gets the hash code for the gradient. |
| [`GetKnot`](#maxon.GradientInterface.GetKnot)(index) | Gets the knot at #index. |
| [`GetKnotCount`](#maxon.GradientInterface.GetKnotCount)() | Gets the number of knots. |
| [`InsertKnot`](#maxon.GradientInterface.InsertKnot)(knot[, keepId]) | Inserts a knot |
| [`InvertKnots`](#maxon.GradientInterface.InvertKnots)() | Inverts the knots. |
| [`IsAlphaGradient`](#maxon.GradientInterface.IsAlphaGradient)() | Checks if this is an alpha gradient. |
| [`RemoveKnot`](#maxon.GradientInterface.RemoveKnot)(index) | Inserts a knot |
| [`SetIsAlphaGradient`](#maxon.GradientInterface.SetIsAlphaGradient)(alphaGradient) | Sets the alpha mode. |
| [`SetKnot`](#maxon.GradientInterface.SetKnot)(index, k) | Sets knot at #index. |
| [`SortKnots`](#maxon.GradientInterface.SortKnots)() | Sorts the knots according to their position. |
| [`transformColorDelegate`](#maxon.GradientInterface.transformColorDelegate)(transformColorDelegate) | Initializes the gradient for rendering. |

## Methods Definition <a id="methods-definition"></a>

### `GradientInterface.Compare(arg2)` <a id="maxon.GradientInterface.Compare"></a>

Compares this with another gradient.

**Parameters:** **arg2** ([`maxon.GradientInterface`](#module-maxon.GradientInterface)) – The other gradient to compare with.

**Returns:** The comparison result.

**Return type:**

`maxon.COMPARERESULT`

### `GradientInterface.ConvertToAlphaGradient()` <a id="maxon.GradientInterface.ConvertToAlphaGradient"></a>

Converts the current gradient to an alpha gradient.

### *static* `GradientInterface.DescribeIO(stream)` <a id="maxon.GradientInterface.DescribeIO"></a>

Describes all elements of this class for I/O operations.

**Parameters:** **stream** (`maxon.DataSerializeInterface`) – The stream that is used to register the class members.

### `GradientInterface.DistributeKnots()` <a id="maxon.GradientInterface.DistributeKnots"></a>

Distributes the knots evenly.

**Returns:** True if any knot distributed, otherwise false.

**Return type:** bool

### `GradientInterface.DoubleKnots()` <a id="maxon.GradientInterface.DoubleKnots"></a>

Doubles the knots.

**Returns:** True if any knot doubled, otherwise false.

**Return type:** bool

### `GradientInterface.Flush()` <a id="maxon.GradientInterface.Flush"></a>

Flushes all the knots.

### `GradientInterface.GetAlphaGradient()` <a id="maxon.GradientInterface.GetAlphaGradient"></a>

Returns the internal alpha gradient as read-only.

**Returns:** The alpha gradient.

**Return type:** Optional[[`maxon.Gradient`](maxon.Gradient.md#module-maxon.Gradient)]

### `GradientInterface.GetHashCode()` <a id="maxon.GradientInterface.GetHashCode"></a>

Gets the hash code for the gradient.

**Returns:** The checksum.

**Return type:** int

### `GradientInterface.GetKnot(index)` <a id="maxon.GradientInterface.GetKnot"></a>

Gets the knot at #index.

**Parameters:** **index** (*int*) – The knot index. 0 <= #index < GetKnotCount()

**Returns:** The knot.

**Return type:** [`maxon.GradientKnot`](maxon.GradientKnot.md#module-maxon.GradientKnot)

### `GradientInterface.GetKnotCount()` <a id="maxon.GradientInterface.GetKnotCount"></a>

Gets the number of knots.

**Returns:** The knot count.

**Return type:** int

### `GradientInterface.InsertKnot(knot, keepId=False)` <a id="maxon.GradientInterface.InsertKnot"></a>

Inserts a knot

**Parameters:**

- **knot** ([`maxon.GradientKnot`](maxon.GradientKnot.md#module-maxon.GradientKnot)) – The knot to insert.
- **keepId** (*bool*) – Specifies if the knot ID should be taken from knot or if a new one should be generated.

**Returns:** The index of the inserted knot, GetKnotCount() - 1

**Return type:** int

### `GradientInterface.InvertKnots()` <a id="maxon.GradientInterface.InvertKnots"></a>

Inverts the knots.

**Returns:** True if any knot inverted, otherwise false.

**Return type:** bool

### `GradientInterface.IsAlphaGradient()` <a id="maxon.GradientInterface.IsAlphaGradient"></a>

Checks if this is an alpha gradient.

**Returns:** True, if this is an alpha gradient.

**Return type:** bool

### `GradientInterface.RemoveKnot(index)` <a id="maxon.GradientInterface.RemoveKnot"></a>

Inserts a knot

**Parameters:** **index** (*int*) – The knot index. 0 <= #index < GetKnotCount()

### `GradientInterface.SetIsAlphaGradient(alphaGradient)` <a id="maxon.GradientInterface.SetIsAlphaGradient"></a>

Sets the alpha mode.

**Parameters:** **alphaGradient** (*bool*) – The gradient alpha type.

### `GradientInterface.SetKnot(index, k)` <a id="maxon.GradientInterface.SetKnot"></a>

Sets knot at #index.

**Parameters:**

- **index** (*int*) – The knot index. 0 <= #index < GetKnotCount()
- **k** ([`maxon.GradientKnot`](maxon.GradientKnot.md#module-maxon.GradientKnot)) – The knot.

### `GradientInterface.SortKnots()` <a id="maxon.GradientInterface.SortKnots"></a>

Sorts the knots according to their position.

### `GradientInterface.transformColorDelegate(transformColorDelegate)` <a id="maxon.GradientInterface.transformColorDelegate"></a>

Initializes the gradient for rendering.

**Parameters:** **transformColorDelegate** (Callable[[[`maxon.Color64`](../../datatypes/vec_col_mat/maxon.Color64.md#module-maxon.Color64)], [`maxon.Color64`](../../datatypes/vec_col_mat/maxon.Color64.md#module-maxon.Color64)]) – A delegate to transform the color of a gradient knot.

**Returns:** The render data.

**Return type:** [`maxon.GradientRenderData`](maxon.GradientRenderData.md#module-maxon.GradientRenderData)
