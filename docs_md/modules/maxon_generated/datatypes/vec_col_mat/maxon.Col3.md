<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/vec_col_mat/maxon.Col3.html -->

# maxon.Col3 <a id="maxon-col3"></a>

## Description <a id="module-maxon.Col3"></a><a id="description"></a>

An object of this class can store every type of data as long as that type has been registered (see [`maxon.DataType`](../base_core/maxon.DataType.md#module-maxon.DataType)).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

Children Classes:

- [`maxon.Color32`](maxon.Color32.md#module-maxon.Color32)
- [`maxon.Color64`](maxon.Color64.md#module-maxon.Color64)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.Col3.STRIDE`](maxon.Col3.STRIDE.md#maxon.Col3.STRIDE) |  |
| [`maxon.Col3.b`](maxon.Col3.b.md#maxon.Col3.b) | The blue component |
| [`maxon.Col3.g`](maxon.Col3.g.md#maxon.Col3.g) | The green component |
| [`maxon.Col3.r`](maxon.Col3.r.md#maxon.Col3.r) | The red component |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Clamp01`](#maxon.Col3.Clamp01)() | Returns a vector that is clamped to the range [0.0 . |
| [`GetAverage`](#maxon.Col3.GetAverage)() | Calculates the average value of ‘r’, ‘g’, ‘b’. |
| [`GetMax`](#maxon.Col3.GetMax)() | Returns the maximum of ‘r’, ‘g’, ‘b’. |
| [`GetMin`](#maxon.Col3.GetMin)() | Return the minimum of ‘r’, ‘g’, ‘b’. |
| [`IsEqual`](#maxon.Col3.IsEqual)(other[, epsilon]) | Tests component-wise if the difference is no bigger than ‘epsilon’. |
| [`IsZero`](#maxon.Col3.IsZero)() | Checks if each component is zero. |
| [`MaxonConvert`](#maxon.Col3.MaxonConvert)([expected]) | Converts the data to the expected type (built-in). |
| [`SetZero`](#maxon.Col3.SetZero)() | Sets all components to zero. |
| [`__add__`](#maxon.Col3.__add__)(scalar) | Adds another color to the current color. |
| [`__div__`](#maxon.Col3.__div__)(scalar) | Divides each color component by a scalar. |
| [`__eq__`](#maxon.Col3.__eq__)(other) | Checks if two colors are equal. |
| [`__getitem__`](#maxon.Col3.__getitem__)(index) | Retrieves the value of the *r*, *g* or *b* component of the color. |
| [`__hash__`](#maxon.Col3.__hash__)() | Returns the hash code of a color. |
| [`__iadd__`](#maxon.Col3.__iadd__)(other) | Adds another color to the current color. |
| [`__idiv__`](#maxon.Col3.__idiv__)(scalar) | Divides each color component by a scalar. |
| [`__imul__`](#maxon.Col3.__imul__)(scalar) | Multiplies each color components by the scalar and returns the color result. |
| [`__init__`](#maxon.Col3.__init__)([r, g, b]) | Initializes a new three component color. |
| [`__isub__`](#maxon.Col3.__isub__)(other) | Subtracts another color to the current color. |
| [`__iter__`](#maxon.Col3.__iter__)() | Iterates color values in the next order: r, g, b. |
| [`__maxon_convert__`](#maxon.Col3.__maxon_convert__)([expected]) |  |
| [`__mul__`](#maxon.Col3.__mul__)(scalar) | Multiplies each color components by the scalar and returns the color result. |
| [`__ne__`](#maxon.Col3.__ne__)(other) | Checks if two colors are not equal. |
| [`__setitem__`](#maxon.Col3.__setitem__)(index, value) | Assigns a value to the *r*, *g* or *b* component of the color. |
| [`__str__`](#maxon.Col3.__str__)() | Returns the string representation of a data. |
| [`__sub__`](#maxon.Col3.__sub__)(scalar) | Subtracts another color to the current color. |

## Methods Definition <a id="methods-definition"></a>

### `Col3.Clamp01()` <a id="maxon.Col3.Clamp01"></a>

Returns a vector that is clamped to the range [0.0 .. 1.0].

**Returns:** The color clamped.

**Return type:** [`maxon.Col3`](#module-maxon.Col3)

### `Col3.GetAverage()` <a id="maxon.Col3.GetAverage"></a>

Calculates the average value of ‘r’, ‘g’, ‘b’.

**Returns:** the average value.

**Return type:** float

### `Col3.GetMax()` <a id="maxon.Col3.GetMax"></a>

Returns the maximum of ‘r’, ‘g’, ‘b’.

**Returns:** The maximum value.

**Returns:** float

### `Col3.GetMin()` <a id="maxon.Col3.GetMin"></a>

Return the minimum of ‘r’, ‘g’, ‘b’.

**Returns:** The minimum value.

**Returns:** float

### `Col3.IsEqual(other, epsilon=0.01)` <a id="maxon.Col3.IsEqual"></a>

Tests component-wise if the difference is no bigger than ‘epsilon’.

**Parameters:**

- **other** ([`maxon.Col3`](#module-maxon.Col3)) – The other color to compare with.
- **epsilon** (*float*) – The tolerance value.

**Returns:** **True** if both color are identical.

**Return type:** bool

### `Col3.IsZero()` <a id="maxon.Col3.IsZero"></a>

Checks if each component is zero.

**Returns:** **True** if all component is zero.

**Return type:** bool

### `Col3.MaxonConvert(expected=None)` <a id="maxon.Col3.MaxonConvert"></a>

Converts the data to the expected type (built-in).

**Parameters:** **expected** (*Any*) – The expected type after the conversion.

**Returns:** The data converted.

**Return type:** Same as expected

### `Col3.SetZero()` <a id="maxon.Col3.SetZero"></a>

Sets all components to zero.

### `Col3.__add__(scalar)` <a id="maxon.Col3.__add__"></a>

Adds another color to the current color.

**Parameters:** **scalar** ([`maxon.Col3`](#module-maxon.Col3)) – The other color.

**Return type:** [`maxon.Col3`](#module-maxon.Col3)

**Returns:** The resulting color.

### `Col3.__div__(scalar)` <a id="maxon.Col3.__div__"></a>

Divides each color component by a scalar.

**Parameters:** **scalar** (*Union*[*int*, *float*]) – The other operand.

**Return type:** [`maxon.Col3`](#module-maxon.Col3)

**Returns:** The resulting color.

### `Col3.__eq__(other)` <a id="maxon.Col3.__eq__"></a>

Checks if two colors are equal.

**Parameters:** **other** ([`maxon.Col3`](#module-maxon.Col3)) – The other color.

**Return type:** bool

**Returns:** **True** if colors are equal.

### `Col3.__getitem__(index)` <a id="maxon.Col3.__getitem__"></a>

Retrieves the value of the *r*, *g* or *b* component of the color.

The component is identified by an index in the interval *[0, 2]*.

**Parameters:** **index** (*int*) – The component index.

**Raises:** **IndexError** – When *index* does not satisfy *0 <= index < 2*.

**Return type:** float

**Returns:** The color component.

### `Col3.__hash__()` <a id="maxon.Col3.__hash__"></a>

Returns the hash code of a color.

### `Col3.__iadd__(other)` <a id="maxon.Col3.__iadd__"></a>

Adds another color to the current color.

**Parameters:** **other** ([`maxon.Col3`](#module-maxon.Col3)) – The other color.

**Return type:** [`maxon.Col3`](#module-maxon.Col3)

**Returns:** The resulting color.

### `Col3.__idiv__(scalar)` <a id="maxon.Col3.__idiv__"></a>

Divides each color component by a scalar.

**Parameters:** **scalar** (*Union*[*int*, *float*]) – The other operand.

**Return type:** [`maxon.Col3`](#module-maxon.Col3)

**Returns:** The resulting color.

### `Col3.__imul__(scalar)` <a id="maxon.Col3.__imul__"></a>

Multiplies each color components by the scalar and returns the color result.

**Parameters:** **scalar** (*float*) – The other color.

**Return type:** [`maxon.Col3`](#module-maxon.Col3)

**Returns:** The resulting color.

### `Col3.__init__(r=None, g=None, b=None)` <a id="maxon.Col3.__init__"></a>

Initializes a new three component color.

It is possible to instantiate a new color without any arguments, causing the *r, g, b* components to default to the value *0*. The type can otherwise be instantiated with one or three arguments, either setting all components to the same value, or setting them individually.

**..note** This type should not be instantiated directly, use instead the type [`maxon.Color`](maxon.Color.md#module-maxon.Color).

**Parameters:**

- **r** (*Optional*[*number*]) – If *r* is the only passed argument, set this to R/G/B components. Otherwise, set the red component.
- **g** (*Optional*[*number*]) – The green component. Can only be passed if *b* is also defined.
- **b** (*Optional*[*number*]) – The blue component.

**Return type:** [`maxon.Col3`](#module-maxon.Col3)

**Returns:** A new [`maxon.Col3`](#module-maxon.Col3).

### `Col3.__isub__(other)` <a id="maxon.Col3.__isub__"></a>

Subtracts another color to the current color.

**Parameters:** **other** ([`maxon.Col3`](#module-maxon.Col3)) – The other color.

**Return type:** [`maxon.Col3`](#module-maxon.Col3)

**Returns:** The resulting color.

### `Col3.__iter__()` <a id="maxon.Col3.__iter__"></a>

Iterates color values in the next order: r, g, b.

### `Col3.__maxon_convert__(expected=None)` <a id="maxon.Col3.__maxon_convert__"></a>

### `Col3.__mul__(scalar)` <a id="maxon.Col3.__mul__"></a>

Multiplies each color components by the scalar and returns the color result.

**Parameters:** **scalar** (*float*) – The other color.

**Return type:** [`maxon.Col3`](#module-maxon.Col3)

**Returns:** The resulting color.

### `Col3.__ne__(other)` <a id="maxon.Col3.__ne__"></a>

Checks if two colors are not equal.

**Parameters:** **other** ([`maxon.Col3`](#module-maxon.Col3)) – The other color.

**Return type:** bool

**Returns:** **True** if both colors are not equal.

### `Col3.__setitem__(index, value)` <a id="maxon.Col3.__setitem__"></a>

Assigns a value to the *r*, *g* or *b* component of the color.

The component is identified by an index in the interval *[0, 2]*.

**Parameters:**

- **index** (*int*) – The index to which the value should be assigned.
- **value** (*float*) – The value to assign for the given index.

### `Col3.__str__()` <a id="maxon.Col3.__str__"></a>

Returns the string representation of a data.

**Return type:** str

### `Col3.__sub__(scalar)` <a id="maxon.Col3.__sub__"></a>

Subtracts another color to the current color.

**Parameters:** **scalar** ([`maxon.Col3`](#module-maxon.Col3)) – The other color.

**Return type:** [`maxon.Col3`](#module-maxon.Col3)

**Returns:** The resulting color.
