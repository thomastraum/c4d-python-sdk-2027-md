<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/vec_col_mat/maxon.Vec4.html -->

# maxon.Vec4 <a id="maxon-vec4"></a>

## Description <a id="module-maxon.Vec4"></a><a id="description"></a>

An object of this class can store every type of data as long as that type has been registered (see [`maxon.DataType`](../base_core/maxon.DataType.md#module-maxon.DataType)).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

Children Classes:

- [`maxon.Vector4d32`](maxon.Vector4d32.md#module-maxon.Vector4d32)
- [`maxon.Vector4d64`](maxon.Vector4d64.md#module-maxon.Vector4d64)
- `maxon.IntVector4d32`
- `maxon.IntVector4d64`

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.Vec4.STRIDE`](maxon.Vec4.STRIDE.md#maxon.Vec4.STRIDE) |  |
| [`maxon.Vec4.w`](maxon.Vec4.w.md#maxon.Vec4.w) | (float) the w component |
| [`maxon.Vec4.x`](maxon.Vec4.x.md#maxon.Vec4.x) | (float) the x component |
| [`maxon.Vec4.y`](maxon.Vec4.y.md#maxon.Vec4.y) | (float) the y component |
| [`maxon.Vec4.z`](maxon.Vec4.z.md#maxon.Vec4.z) | (float) the z component |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Clamp01`](#maxon.Vec4.Clamp01)() | Returns a vector that is clamped to the range [0.0 . |
| [`GetAverage`](#maxon.Vec4.GetAverage)() | Calculates the average value of ‘x’, ‘y’, ‘z’ and ‘w’. |
| [`GetLength`](#maxon.Vec4.GetLength)() | Retrieves the length of the vector. |
| [`GetMax`](#maxon.Vec4.GetMax)() | Returns the maximum of ‘x’, ‘y’, ‘z’ and ‘w’. |
| [`GetMin`](#maxon.Vec4.GetMin)() | Return the minimum of ‘x’, ‘y’, ‘z’ and ‘w’. |
| [`GetSquaredLength`](#maxon.Vec4.GetSquaredLength)() | Retrieves the squared length of the vector. |
| [`IsEqual`](#maxon.Vec4.IsEqual)(other[, epsilon]) | Tests component-wise if the difference is no bigger than ‘epsilon’. |
| [`IsZero`](#maxon.Vec4.IsZero)() | Checks if each component is zero. |
| [`LessThanOrEqual`](#maxon.Vec4.LessThanOrEqual)(v) | Checks if each component are less or equal to v |
| [`MaxonConvert`](#maxon.Vec4.MaxonConvert)([expected]) | Converts the data to the expected type (built-in). |
| [`SetZero`](#maxon.Vec4.SetZero)() | Sets all components to zero. |
| [`__add__`](#maxon.Vec4.__add__)(scalar) | Adds another vector to the current vector. |
| [`__div__`](#maxon.Vec4.__div__)(scalar) | Divides each vector component by a scalar. |
| [`__eq__`](#maxon.Vec4.__eq__)(other) | Checks if two vectors are equal. |
| [`__getitem__`](#maxon.Vec4.__getitem__)(index) | Retrieves the value of the *x*, *y*, *z* or *w* component of the vector. |
| [`__hash__`](#maxon.Vec4.__hash__)() | Returns the hash code of a vector. |
| [`__iadd__`](#maxon.Vec4.__iadd__)(other) | Adds another vector to the current vector. |
| [`__idiv__`](#maxon.Vec4.__idiv__)(scalar) | Divides each vector component by a scalar. |
| [`__imul__`](#maxon.Vec4.__imul__)(scalar) | Multiplies each vector components by the scalar and returns the vector result. |
| [`__init__`](#maxon.Vec4.__init__)([x, y, z, w]) | Initializes a new four component vector. |
| [`__isub__`](#maxon.Vec4.__isub__)(other) | Subtracts another vector to the current vector. |
| [`__iter__`](#maxon.Vec4.__iter__)() | Iterates vector values in the next order: x, y, z, w. |
| [`__len__`](#maxon.Vec4.__len__)() |  |
| [`__maxon_convert__`](#maxon.Vec4.__maxon_convert__)([expected]) |  |
| [`__mul__`](#maxon.Vec4.__mul__)(scalar) | Multiplies each vector components by the scalar and returns the vector result. |
| [`__ne__`](#maxon.Vec4.__ne__)(other) | Checks if two vectors are not equal. |
| [`__setitem__`](#maxon.Vec4.__setitem__)(index, value) | Assigns a value to the *x*, *y* or *z* *w* component of the vector. |
| [`__str__`](#maxon.Vec4.__str__)() | Returns the string representation of a data. |
| [`__sub__`](#maxon.Vec4.__sub__)(scalar) | Subtracts another vector to the current vector. |

## Methods Definition <a id="methods-definition"></a>

### `Vec4.Clamp01()` <a id="maxon.Vec4.Clamp01"></a>

Returns a vector that is clamped to the range [0.0 .. 1.0].

**Returns:** The vector clamped.

**Return type:** [`maxon.Vec4`](#module-maxon.Vec4)

### `Vec4.GetAverage()` <a id="maxon.Vec4.GetAverage"></a>

Calculates the average value of ‘x’, ‘y’, ‘z’ and ‘w’.

**Returns:** the average value.

**Return type:** float

### `Vec4.GetLength()` <a id="maxon.Vec4.GetLength"></a>

Retrieves the length of the vector.

**Returns:** Vector length.

**Return type:** float

### `Vec4.GetMax()` <a id="maxon.Vec4.GetMax"></a>

Returns the maximum of ‘x’, ‘y’, ‘z’ and ‘w’.

**Returns:** The maximum value.

**Returns:** float

### `Vec4.GetMin()` <a id="maxon.Vec4.GetMin"></a>

Return the minimum of ‘x’, ‘y’, ‘z’ and ‘w’.

**Returns:** The minimum value.

**Returns:** float

### `Vec4.GetSquaredLength()` <a id="maxon.Vec4.GetSquaredLength"></a>

Retrieves the squared length of the vector.

**Returns:** Vector squared length.

**Return type:** float

### `Vec4.IsEqual(other, epsilon=0.01)` <a id="maxon.Vec4.IsEqual"></a>

Tests component-wise if the difference is no bigger than ‘epsilon’.

**Parameters:**

- **other** ([`maxon.Vec3`](maxon.Vec3.md#module-maxon.Vec3)) – The other color to compare with.
- **epsilon** (*float*) – The tolerance value.

**Returns:** **True** if both color are identical.

**Return type:** bool

### `Vec4.IsZero()` <a id="maxon.Vec4.IsZero"></a>

Checks if each component is zero.

**Returns:** **True** if all component is zero.

**Return type:** bool

### `Vec4.LessThanOrEqual(v)` <a id="maxon.Vec4.LessThanOrEqual"></a>

Checks if each component are less or equal to v

**Parameters:** **v** – The maximum value to checks for.

**Returns:** **True** if all components are less or equals to the passed value.

**Return type:** bool

### `Vec4.MaxonConvert(expected=None)` <a id="maxon.Vec4.MaxonConvert"></a>

Converts the data to the expected type (built-in).

**Parameters:** **expected** (*Any*) – The expected type after the conversion.

**Returns:** The data converted.

**Return type:** Same as expected

### `Vec4.SetZero()` <a id="maxon.Vec4.SetZero"></a>

Sets all components to zero.

### `Vec4.__add__(scalar)` <a id="maxon.Vec4.__add__"></a>

Adds another vector to the current vector.

**Parameters:** **scalar** ([`maxon.Vec4`](#module-maxon.Vec4)) – The other vector.

### `Vec4.__div__(scalar)` <a id="maxon.Vec4.__div__"></a>

Divides each vector component by a scalar.

**Parameters:** **scalar** (*Union*[*int*, *float*]) – The other operand.

**Return type:** [`maxon.Vec4`](#module-maxon.Vec4)

**Returns:** The resulting vector.

### `Vec4.__eq__(other)` <a id="maxon.Vec4.__eq__"></a>

Checks if two vectors are equal.

**Parameters:** **other** ([`maxon.Vec4`](#module-maxon.Vec4)) – The other vector.

**Return type:** bool

**Returns:** **True** if both vectors are equal.

### `Vec4.__getitem__(index)` <a id="maxon.Vec4.__getitem__"></a>

Retrieves the value of the *x*, *y*, *z* or *w* component of the vector.  
The component is identified by an index in the interval *[0, 3]*.

**Parameters:** **index** (*int*) – The component index.

**Raises:** **IndexError** – When *key* does not satisfy *0 <= key < 3*.

**Return type:** float

**Returns:** The vector component.

### `Vec4.__hash__()` <a id="maxon.Vec4.__hash__"></a>

Returns the hash code of a vector.

### `Vec4.__iadd__(other)` <a id="maxon.Vec4.__iadd__"></a>

Adds another vector to the current vector.

**Parameters:** **other** ([`maxon.Vec4`](#module-maxon.Vec4)) – The other vector.

### `Vec4.__idiv__(scalar)` <a id="maxon.Vec4.__idiv__"></a>

Divides each vector component by a scalar.

**Parameters:** **scalar** (*Union*[*int*, *float*]) – The other operand.

**Return type:** [`maxon.Vec4`](#module-maxon.Vec4)

**Returns:** The resulting vector.

### `Vec4.__imul__(scalar)` <a id="maxon.Vec4.__imul__"></a>

Multiplies each vector components by the scalar and returns the vector result.

**Parameters:** **scalar** (*float*) – The other vector.

**Return type:** [`maxon.Vec4`](#module-maxon.Vec4)

**Returns:** The resulting vector.

### `Vec4.__init__(x=None, y=None, z=None, w=None)` <a id="maxon.Vec4.__init__"></a>

Initializes a new four component vector.  
It is possible to instantiate a new vector without any arguments, causing the *x, y, z, w*  
components to default to the value *0*. The type can otherwise be instantiated with one or  
four arguments, either setting all components to the same value or copying another  
[`maxon.Vec4`](#module-maxon.Vec4) instance, or setting all three components individually.

**..note** This type should not be instantiated directly, use instead the type [`maxon.Vector4d`](maxon.Vector4d.md#module-maxon.Vector4d).

**Parameters:**

- **x** (Optional[[`maxon.Vec4`](#module-maxon.Vec4), float]) – If *x* is the only passed argument. If this is a float set this value to X/Y/Z/W components. If this is a vector, this vector is copied.
- **y** (*float*) – The z component. Can only be passed if *z* and *w* are also defined.
- **z** (*float*) – The z component. Can only be passed if *w* is also defined.
- **w** (*float*) – The w component.

### `Vec4.__isub__(other)` <a id="maxon.Vec4.__isub__"></a>

Subtracts another vector to the current vector.

**Parameters:** **other** ([`maxon.Vec4`](#module-maxon.Vec4)) – The other vector.

**Return type:** [`maxon.Vec4`](#module-maxon.Vec4)

**Returns:** The resulting vector.

### `Vec4.__iter__()` <a id="maxon.Vec4.__iter__"></a>

Iterates vector values in the next order: x, y, z, w.

### `Vec4.__len__()` <a id="maxon.Vec4.__len__"></a>

### `Vec4.__maxon_convert__(expected=None)` <a id="maxon.Vec4.__maxon_convert__"></a>

### `Vec4.__mul__(scalar)` <a id="maxon.Vec4.__mul__"></a>

Multiplies each vector components by the scalar and returns the vector result.

**Parameters:** **scalar** (*float*) – The other vector.

**Return type:** [`maxon.Vec4`](#module-maxon.Vec4)

**Returns:** The resulting vector.

### `Vec4.__ne__(other)` <a id="maxon.Vec4.__ne__"></a>

Checks if two vectors are not equal.

**Parameters:** **other** ([`maxon.Vec4`](#module-maxon.Vec4)) – The other vector.

**Return type:** bool

**Returns:** **True** if both vectors are not equal.

### `Vec4.__setitem__(index, value)` <a id="maxon.Vec4.__setitem__"></a>

Assigns a value to the *x*, *y* or *z* *w* component of the vector.  
The component is identified by an index in the interval *[0, 3]*.

**Parameters:**

- **index** (*int*) – The index to which the value should be assigned.
- **value** (*float*) – The value to assign for the given index.

### `Vec4.__str__()` <a id="maxon.Vec4.__str__"></a>

Returns the string representation of a data.

**Return type:** str

### `Vec4.__sub__(scalar)` <a id="maxon.Vec4.__sub__"></a>

Subtracts another vector to the current vector.

**Parameters:** **scalar** ([`maxon.Vec4`](#module-maxon.Vec4)) – The other vector.

**Return type:** [`maxon.Vec4`](#module-maxon.Vec4)

**Returns:** The resulting vector.
