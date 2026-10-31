<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/vec_col_mat/maxon.Vec3.html -->

# maxon.Vec3 <a id="maxon-vec3"></a>

## Description <a id="module-maxon.Vec3"></a><a id="description"></a>

A vector consisting of three components X, Y and Z.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

Children Classes:

- [`maxon.Vector32`](maxon.Vector32.md#module-maxon.Vector32)
- [`maxon.Vector64`](maxon.Vector64.md#module-maxon.Vector64)
- [`maxon.IntVector32`](maxon.IntVector32.md#module-maxon.IntVector32)
- [`maxon.IntVector64`](maxon.IntVector64.md#module-maxon.IntVector64)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.Vec3.STRIDE`](maxon.Vec3.STRIDE.md#maxon.Vec3.STRIDE) |  |
| [`maxon.Vec3.x`](maxon.Vec3.x.md#maxon.Vec3.x) | (float) the x component |
| [`maxon.Vec3.y`](maxon.Vec3.y.md#maxon.Vec3.y) | (float) the y component |
| [`maxon.Vec3.z`](maxon.Vec3.z.md#maxon.Vec3.z) | (float) the z component |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Clamp01`](#maxon.Vec3.Clamp01)() | Returns a vector that is clamped to the range [0.0 . |
| [`GetAverage`](#maxon.Vec3.GetAverage)() | Calculates the average value of ‘x’, ‘y’, ‘z’. |
| [`GetLength`](#maxon.Vec3.GetLength)() | Retrieves the length of the vector. |
| [`GetMax`](#maxon.Vec3.GetMax)() | Returns the maximum of ‘x’, ‘y’, ‘z’. |
| [`GetMin`](#maxon.Vec3.GetMin)() | Return the minimum of ‘x’, ‘y’, ‘z’. |
| [`GetSquaredLength`](#maxon.Vec3.GetSquaredLength)() | Retrieves the squared length of the vector. |
| [`IsEqual`](#maxon.Vec3.IsEqual)(other[, epsilon]) | Tests component-wise if the difference is no bigger than ‘epsilon’. |
| [`IsZero`](#maxon.Vec3.IsZero)() | Checks if each component is zero. |
| [`LessThanOrEqual`](#maxon.Vec3.LessThanOrEqual)(v) | Checks if each component are less or equal to v |
| [`MaxonConvert`](#maxon.Vec3.MaxonConvert)([expected]) | Converts the data to the expected type (built-in). |
| [`SetZero`](#maxon.Vec3.SetZero)() | Sets all components to zero. |
| [`__add__`](#maxon.Vec3.__add__)(scalar) | Adds another vector to the current vector. |
| [`__div__`](#maxon.Vec3.__div__)(scalar) | Divides each vector component by a scalar. |
| [`__eq__`](#maxon.Vec3.__eq__)(other) | Checks if two vectors are equal. |
| [`__getitem__`](#maxon.Vec3.__getitem__)(index) | Retrieves the value of the *x*, *y* or *z* component of the vector. |
| [`__hash__`](#maxon.Vec3.__hash__)() | Returns the hash code of a vector. |
| [`__iadd__`](#maxon.Vec3.__iadd__)(other) | Adds another vector to the current vector. |
| [`__idiv__`](#maxon.Vec3.__idiv__)(scalar) | Divides each vector component by a scalar. |
| [`__imul__`](#maxon.Vec3.__imul__)(scalar) | Multiplies each vector components by the scalar and returns the vector result. |
| [`__init__`](#maxon.Vec3.__init__)([x, y, z]) | Initializes a new three component vector. |
| [`__isub__`](#maxon.Vec3.__isub__)(other) | Subtracts another vector to the current vector. |
| [`__iter__`](#maxon.Vec3.__iter__)() | Iterates vector values in the next order: x, y, z. |
| [`__len__`](#maxon.Vec3.__len__)() |  |
| [`__maxon_convert__`](#maxon.Vec3.__maxon_convert__)([expected]) |  |
| [`__mul__`](#maxon.Vec3.__mul__)(scalar) | Multiplies each vector components by the scalar and returns the vector result. |
| [`__ne__`](#maxon.Vec3.__ne__)(other) | Checks if two vectors are not equal. |
| [`__setitem__`](#maxon.Vec3.__setitem__)(index, value) | Assigns a value to the *x*, *y* or *z* component of the vector. |
| [`__str__`](#maxon.Vec3.__str__)() | Returns the string representation of a data. |
| [`__sub__`](#maxon.Vec3.__sub__)(scalar) | Subtracts another vector to the current vector. |

## Methods Definition <a id="methods-definition"></a>

### `Vec3.Clamp01()` <a id="maxon.Vec3.Clamp01"></a>

Returns a vector that is clamped to the range [0.0 .. 1.0].

**Returns:** The vector clamped.

**Return type:** [`maxon.Vec3`](#module-maxon.Vec3)

### `Vec3.GetAverage()` <a id="maxon.Vec3.GetAverage"></a>

Calculates the average value of ‘x’, ‘y’, ‘z’.

**Returns:** the average value.

**Return type:** float

### `Vec3.GetLength()` <a id="maxon.Vec3.GetLength"></a>

Retrieves the length of the vector.

**Returns:** Vector length.

**Return type:** float

### `Vec3.GetMax()` <a id="maxon.Vec3.GetMax"></a>

Returns the maximum of ‘x’, ‘y’, ‘z’.

**Returns:** The maximum value.

**Returns:** float

### `Vec3.GetMin()` <a id="maxon.Vec3.GetMin"></a>

Return the minimum of ‘x’, ‘y’, ‘z’.

**Returns:** The minimum value.

**Returns:** float

### `Vec3.GetSquaredLength()` <a id="maxon.Vec3.GetSquaredLength"></a>

Retrieves the squared length of the vector.

**Returns:** Vector squared length.

**Return type:** float

### `Vec3.IsEqual(other, epsilon=0.01)` <a id="maxon.Vec3.IsEqual"></a>

Tests component-wise if the difference is no bigger than ‘epsilon’.

**Parameters:**

- **other** ([`maxon.Vec3`](#module-maxon.Vec3)) – The other color to compare with.
- **epsilon** (*float*) – The tolerance value.

**Returns:** **True** if both color are identical.

**Return type:** bool

### `Vec3.IsZero()` <a id="maxon.Vec3.IsZero"></a>

Checks if each component is zero.

**Returns:** **True** if all component is zero.

**Return type:** bool

### `Vec3.LessThanOrEqual(v)` <a id="maxon.Vec3.LessThanOrEqual"></a>

Checks if each component are less or equal to v

**Parameters:** **v** – The maximum value to checks for.

**Returns:** **True** if all components are less or equals to the passed value.

**Return type:** bool

### `Vec3.MaxonConvert(expected=None)` <a id="maxon.Vec3.MaxonConvert"></a>

Converts the data to the expected type (built-in).

**Parameters:** **expected** (*Any*) – The expected type after the conversion.

**Returns:** The data converted.

**Return type:** Same as expected

### `Vec3.SetZero()` <a id="maxon.Vec3.SetZero"></a>

Sets all components to zero.

### `Vec3.__add__(scalar)` <a id="maxon.Vec3.__add__"></a>

Adds another vector to the current vector.

**Parameters:** **scalar** ([`maxon.Vec3`](#module-maxon.Vec3)) – The other vector.

**Return type:** [`maxon.Vec3`](#module-maxon.Vec3)

**Returns:** The resulting vector.

### `Vec3.__div__(scalar)` <a id="maxon.Vec3.__div__"></a>

Divides each vector component by a scalar.

**Parameters:** **scalar** (*Union*[*int*, *float*]) – The other operand.

**Return type:** [`maxon.Vec3`](#module-maxon.Vec3)

**Returns:** The resulting vector.

### `Vec3.__eq__(other)` <a id="maxon.Vec3.__eq__"></a>

Checks if two vectors are equal.

**Parameters:** **other** ([`maxon.Vec3`](#module-maxon.Vec3)) – The other vector.

**Return type:** bool

**Returns:** **True** if vector are equal.

### `Vec3.__getitem__(index)` <a id="maxon.Vec3.__getitem__"></a>

Retrieves the value of the *x*, *y* or *z* component of the vector.  
The component is identified by an index in the interval *[0, 2]*.

**Parameters:** **index** (*int*) – The component index.

**Raises:** **IndexError** – When *index* does not satisfy *0 <= index < 2*.

**Return type:** float

**Returns:** The vector component.

### `Vec3.__hash__()` <a id="maxon.Vec3.__hash__"></a>

Returns the hash code of a vector.

### `Vec3.__iadd__(other)` <a id="maxon.Vec3.__iadd__"></a>

Adds another vector to the current vector.

**Parameters:** **other** ([`maxon.Vec3`](#module-maxon.Vec3)) – The other vector.

**Return type:** [`maxon.Vec3`](#module-maxon.Vec3)

**Returns:** The resulting vector.

### `Vec3.__idiv__(scalar)` <a id="maxon.Vec3.__idiv__"></a>

Divides each vector component by a scalar.

**Parameters:** **scalar** (*Union*[*int*, *float*]) – The other operand.

**Return type:** [`maxon.Vec3`](#module-maxon.Vec3)

**Returns:** The resulting vector.

### `Vec3.__imul__(scalar)` <a id="maxon.Vec3.__imul__"></a>

Multiplies each vector components by the scalar and returns the vector result.

**Parameters:** **scalar** (*float*) – The other vector.

**Return type:** [`maxon.Vec3`](#module-maxon.Vec3)

**Returns:** The resulting vector.

### `Vec3.__init__(x=None, y=None, z=None)` <a id="maxon.Vec3.__init__"></a>

Initializes a new three component vector.  
It is possible to instantiate a new vector without any arguments, causing the *x, y, z*  
components to default to the value *0*. The type can otherwise be instantiated with one or  
three arguments, either setting all components to the same value or copying another  
[`maxon.Vec3`](#module-maxon.Vec3) instance, or setting all three components individually.

**..note** This type should not be instantiated directly, use instead the type [`maxon.Vector`](maxon.Vector.md#module-maxon.Vector).

**Parameters:**

- **x** (Optional[[`maxon.Vec4`](maxon.Vec4.md#module-maxon.Vec4), float]) – If *x* is the only passed argument. If this is a float set this value to X/Y/Z components. If this is a vector, this vector is copied.
- **y** (*float*) – The z component. Can only be passed if *z* is also defined.
- **z** (*float*) – The z component

### `Vec3.__isub__(other)` <a id="maxon.Vec3.__isub__"></a>

Subtracts another vector to the current vector.

**Parameters:** **other** ([`maxon.Vec3`](#module-maxon.Vec3)) – The other vector.

**Return type:** [`maxon.Vec3`](#module-maxon.Vec3)

**Returns:** The resulting vector.

### `Vec3.__iter__()` <a id="maxon.Vec3.__iter__"></a>

Iterates vector values in the next order: x, y, z.

### `Vec3.__len__()` <a id="maxon.Vec3.__len__"></a>

### `Vec3.__maxon_convert__(expected=None)` <a id="maxon.Vec3.__maxon_convert__"></a>

### `Vec3.__mul__(scalar)` <a id="maxon.Vec3.__mul__"></a>

Multiplies each vector components by the scalar and returns the vector result.

**Parameters:** **scalar** (*float*) – The other vector.

**Return type:** [`maxon.Vec3`](#module-maxon.Vec3)

**Returns:** The resulting vector.

### `Vec3.__ne__(other)` <a id="maxon.Vec3.__ne__"></a>

Checks if two vectors are not equal.

**Parameters:** **other** ([`maxon.Vec3`](#module-maxon.Vec3)) – The other vector.

**Return type:** bool

**Returns:** **True** if both vector are not equal.

### `Vec3.__setitem__(index, value)` <a id="maxon.Vec3.__setitem__"></a>

Assigns a value to the *x*, *y* or *z* component of the vector.  
The component is identified by an index in the interval *[0, 2]*.

**Parameters:**

- **index** (*int*) – The index to which the value should be assigned.
- **value** (*float*) – The value to assign for the given index.

### `Vec3.__str__()` <a id="maxon.Vec3.__str__"></a>

Returns the string representation of a data.

**Return type:** str

### `Vec3.__sub__(scalar)` <a id="maxon.Vec3.__sub__"></a>

Subtracts another vector to the current vector.

**Parameters:** **scalar** ([`maxon.Vec3`](#module-maxon.Vec3)) – The other vector.

**Return type:** [`maxon.Vec3`](#module-maxon.Vec3)

**Returns:** The resulting vector.
