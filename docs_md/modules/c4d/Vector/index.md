<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/Vector/index.html -->

# c4d.Vector <a id="c4d-vector"></a>

## *class* `c4d.Vector` <a id="c4d.Vector"></a>

Single precision vector mathematics.  
A vector class represents a point, a color, a direction, an HPB-angle or a simple coordinate in a 3D space using the Cartesian coordinates x, y and z. The values are stored in the members *x, y and z*.  
For example, positions are stored in the order (X position; Y position; Z position) and rotations in the order (H angle; P angle; B angle).  
Cinema 4D also uses vectors to store colors and their values of an RGB (Red, Green, Blue) color model.  
The vector class can also represent a direction, an arrow pointing from the origin of the coordinates, such as (0,0,0), to an endpoint3.

> **Note:** Cinema 4D uses a left-handed coordinate system.

> **Warning:** The [`Vector`](#c4d.Vector) type does not support the function *copy.copy()*, please use the [`Vector`](#c4d.Vector) copy constructor instead.
>
> ```python
> >>> import c4d
> >>> import copy
>
> >>> # A vector and its Python object id.
> >>> vec = c4d.Vector(1)
> >>> id(vec), vec
> (1331515356992, Vector(1, 1, 1))
>
> >>> # We are only creating a reference to the same object.
> >>> ref = vec
> >>> id(ref), ref
> (1331515356992, Vector(1, 1, 1))
>
> >>> # Cinema's types usually do not work with Python's copy module.
> >>> copy.deepcopy(vec)
> ...
> TypeError: can't pickle c4d.Vector objects.
>
> >>> # But we can copy objects via copy constructors.
> >>> copy = c4d.Vector(vec)
> >>> id(copy), copy
> (1331515387904, Vector(1, 1, 1))
> ```

**Attributes**

## `c4d.Vector.x` <a id="c4d.Vector.x"></a>

X component of the vector.

**Type:** float

## `c4d.Vector.y` <a id="c4d.Vector.y"></a>

Y component of the vector.

**Type:** float

## `c4d.Vector.z` <a id="c4d.Vector.z"></a>

Z component of the vector.

**Type:** float

## Overview <a id="overview"></a>

- [`Vector.GetDistance()`](#c4d.Vector.GetDistance): Retrieve the distance between two vectors.

**Comparison And State**

- [`Vector.GetHashCode()`](#c4d.Vector.GetHashCode): Returns the hash code of the vector used for hash maps and comparisons.
- [`Vector.IsEqual()`](#c4d.Vector.IsEqual): Tests component-wise if the difference is no bigger than ‘epsilon’.
- [`Vector.IsZero()`](#c4d.Vector.IsZero): Checks if each component is zero.
- [`Vector.SetZero()`](#c4d.Vector.SetZero): Sets all components to zero.

**Component Aggregates**

- [`Vector.GetAverage()`](#c4d.Vector.GetAverage): Calculates the average value of ‘x’, ‘y’ and ‘z’.
- [`Vector.GetMax()`](#c4d.Vector.GetMax): Returns the maximum of ‘x’, ‘y’ and ‘z’.
- [`Vector.GetMin()`](#c4d.Vector.GetMin): Returns the minimum of ‘x’, ‘y’ and ‘z’.
- [`Vector.GetSum()`](#c4d.Vector.GetSum): Calculates the sum of ‘x’, ‘y’ and ‘z’.

**Component Operations**

- [`Vector.Abs()`](#c4d.Vector.Abs): Returns the vector with absolute value for each entry
- [`Vector.Clamp01()`](#c4d.Vector.Clamp01): Returns a vector that is clamped to the range [0.0 .. 1.0].
- [`Vector.ClampMax()`](#c4d.Vector.ClampMax): Set the maximum of each component.
- [`Vector.ClampMin()`](#c4d.Vector.ClampMin): Set the minimum of each component.
- [`Vector.Max()`](#c4d.Vector.Max): Calculates the maximum of each component.
- [`Vector.Min()`](#c4d.Vector.Min): Calculates the minimum of each component.
- [`Vector.SetMax()`](#c4d.Vector.SetMax): Set the maximum of each component.
- [`Vector.SetMin()`](#c4d.Vector.SetMin): Set the minimum of each component.

**Magic Methods**

- [`Vector.__abs__()`](#c4d.Vector.__abs__): Returns a vector with the absolute (positive) value of each component.
- [`Vector.__add__()`](#c4d.Vector.__add__): Adds an operand to the vector.
- [`Vector.__del__()`](#c4d.Vector.__del__): Not implemented.
- [`Vector.__div__()`](#c4d.Vector.__div__): Divides each vector component by a scalar.
- [`Vector.__eq__()`](#c4d.Vector.__eq__): Checks if two vectors are equal.
- [`Vector.__ge__()`](#c4d.Vector.__ge__): Not implemented.
- [`Vector.__getitem__()`](#c4d.Vector.__getitem__): Retrieves the value of the *x*, *y* or *z* component of the vector.
- [`Vector.__gt__()`](#c4d.Vector.__gt__): Not implemented.
- [`Vector.__hash__()`](#c4d.Vector.__hash__): Returns the hash code of the vector used for hash maps and comparisons.
- [`Vector.__init__()`](#c4d.Vector.__init__): Initializes a new [`Vector`](#c4d.Vector).
- [`Vector.__invert__()`](#c4d.Vector.__invert__): Returns the normalized vector.
- [`Vector.__le__()`](#c4d.Vector.__le__): Not implemented.
- [`Vector.__lt__()`](#c4d.Vector.__lt__): Not implemented.
- [`Vector.__mod__()`](#c4d.Vector.__mod__): Calculates the cross product of the vector and an operand.
- [`Vector.__mul__()`](#c4d.Vector.__mul__): Calculates the product of the vector and an left-side operand.
- [`Vector.__ne__()`](#c4d.Vector.__ne__): Check if two vectors are not equal.
- [`Vector.__neg__()`](#c4d.Vector.__neg__): Returns the inverse of the vector.
- [`Vector.__radd__()`](#c4d.Vector.__radd__): Adds the vector to an operand.
- [`Vector.__rdiv__()`](#c4d.Vector.__rdiv__): Not implemented.
- [`Vector.__rmul__()`](#c4d.Vector.__rmul__): Calculates the product of the vector and a right-side operand.
- [`Vector.__rsub__()`](#c4d.Vector.__rsub__): Subtracts the vector from an operand.
- [`Vector.__rxor__()`](#c4d.Vector.__rxor__): Not implemented.
- [`Vector.__setitem__()`](#c4d.Vector.__setitem__): Assigns a value to the *x*, *y* or *z* component of the vector.
- [`Vector.__str__()`](#c4d.Vector.__str__): Returns a string representation of the vector.
- [`Vector.__sub__()`](#c4d.Vector.__sub__): Subtracts an operand from the vector.
- [`Vector.__xor__()`](#c4d.Vector.__xor__): Calculates an alternative product operation of the vector and a left-side operand.

**Magnitude And Normalization**

- [`Vector.GetLength()`](#c4d.Vector.GetLength): Calculates the length of the vector.
- [`Vector.GetLengthSquared()`](#c4d.Vector.GetLengthSquared): Calculates the squared length of the vector.
- [`Vector.GetNormalized()`](#c4d.Vector.GetNormalized): Calculates the normalized vector, so that `GetLength()` returns *1.0*.
- [`Vector.GetSquaredLength()`](#c4d.Vector.GetSquaredLength): Returns the squared length of the vector.
- [`Vector.Normalize()`](#c4d.Vector.Normalize): Normalizes the vector, so that `GetLength()` returns *1.0*.

**Spatial Operations**

- [`Vector.Cross()`](#c4d.Vector.Cross): Calculates the cross product of the vector and vector **v2**.
- [`Vector.Dot()`](#c4d.Vector.Dot): Calculates the dot product of the vector and vector **v2**.
- [`Vector.GetAngle()`](#c4d.Vector.GetAngle): Calculates angle (in radians) between v1 and v2.
- [`Vector.GetRightRotated()`](#c4d.Vector.GetRightRotated): Returns a vector where the components have been rotated to the right (in the usual (x, y, z)-representation).

## Members <a id="members"></a>

### Spatial Operations <a id="c4d.Vector-staticmethod-Spatial-Operations"></a>

#### *static* `Vector.GetDistance(v1, v2)` <a id="c4d.Vector.GetDistance"></a>

Retrieve the distance between two vectors.

**Parameters:**

- **v1** ([*c4d.Vector*](#c4d.Vector)) – The first vector.
- **v2** ([*c4d.Vector*](#c4d.Vector)) – The second vector.

**Returns:** the distance from v1 to v2.

**Return type:** float

### Comparison And State <a id="c4d.Vector-method-Comparison-And-State"></a>

#### `Vector.GetHashCode(self)` <a id="c4d.Vector.GetHashCode"></a>

Returns the hash code of the vector used for hash maps and comparisons.

*New in version R26.*

**Returns:** The vector’s hash code.

**Return type:** int

#### `Vector.IsEqual(self, other, epsilon)` <a id="c4d.Vector.IsEqual"></a>

Tests component-wise if the difference is no bigger than ‘epsilon’.

*New in version R26.*

**Parameters:**

- **other** ([*c4d.Vector*](#c4d.Vector)) – The other vector to test.
- **epsilon** (*float*) – The threshold value.

**Returns:** **True** if other is in the range of epsilon, **False** otherwise.

**Return type:** bool

#### `Vector.IsZero(self, epsilon=1e-10)` <a id="c4d.Vector.IsZero"></a>

Checks if each component is zero.

*New in version R26.*

**Parameters:** **epsilon** (*float*) – The threshold value.

**Returns:** **False** if one or more component are bigger than epsilon, otherwise **True**.

**Return type:** bool

#### `Vector.SetZero(self)` <a id="c4d.Vector.SetZero"></a>

Sets all components to zero.

*New in version R26.*

### Component Aggregates <a id="c4d.Vector-method-Component-Aggregates"></a>

#### `Vector.GetAverage(self)` <a id="c4d.Vector.GetAverage"></a>

Calculates the average value of ‘x’, ‘y’ and ‘z’.

*New in version R26.*

**Returns:** The average value of ‘x’, ‘y’ and ‘z’.

**Return type:** float

#### `Vector.GetMax(self)` <a id="c4d.Vector.GetMax"></a>

Returns the maximum of ‘x’, ‘y’ and ‘z’.

*New in version R26.*

**Returns:** A new float with the maximum of ‘x’, ‘y’ and ‘z’.

**Return type:** float

#### `Vector.GetMin(self)` <a id="c4d.Vector.GetMin"></a>

Returns the minimum of ‘x’, ‘y’ and ‘z’.

*New in version R26.*

**Returns:** A new float with the minimum of ‘x’, ‘y’ and ‘z’.

**Return type:** float

#### `Vector.GetSum(self)` <a id="c4d.Vector.GetSum"></a>

Calculates the sum of ‘x’, ‘y’ and ‘z’.

*New in version R26.*

**Returns:** The sum value of ‘x’, ‘y’ and ‘z’.

**Return type:** float

### Component Operations <a id="c4d.Vector-method-Component-Operations"></a>

#### `Vector.Abs(self)` <a id="c4d.Vector.Abs"></a>

Returns the vector with absolute value for each entry

*New in version R26.*

**Returns:** A new absolute vector.

**Return type:** [c4d.Vector](#c4d.Vector)

#### `Vector.Clamp01(self)` <a id="c4d.Vector.Clamp01"></a>

Returns a vector that is clamped to the range [0.0 .. 1.0].

*New in version R26.*

**Returns:** The clamped vector.

**Return type:** [c4d.Vector](#c4d.Vector)

#### `Vector.ClampMax(self, other)` <a id="c4d.Vector.ClampMax"></a>

Set the maximum of each component.

*New in version R26.*

**Parameters:** **other** ([*c4d.Vector*](#c4d.Vector)) – The maximum value of ‘x’, ‘y’ and ‘z’.

#### `Vector.ClampMin(self, other)` <a id="c4d.Vector.ClampMin"></a>

Set the minimum of each component.

*New in version R26.*

**Parameters:** **other** ([*c4d.Vector*](#c4d.Vector)) – The minimum value of ‘x’, ‘y’ and ‘z’.

#### `Vector.Max(self, other)` <a id="c4d.Vector.Max"></a>

Calculates the maximum of each component.

*New in version R26.*

**Parameters:** **other** ([*c4d.Vector*](#c4d.Vector)) – The other vector.

**Returns:** The vector containing the maximum of each component.

**Return type:** [c4d.Vector](#c4d.Vector)

#### `Vector.Min(self, other)` <a id="c4d.Vector.Min"></a>

Calculates the minimum of each component.

*New in version R26.*

**Parameters:** **other** ([*c4d.Vector*](#c4d.Vector)) – The other vector.

**Returns:** The vector containing the minimum of each component.

**Return type:** [c4d.Vector](#c4d.Vector)

#### `Vector.SetMax(self, other)` <a id="c4d.Vector.SetMax"></a>

Set the maximum of each component.

*New in version R26.*

**Parameters:** **other** ([*c4d.Vector*](#c4d.Vector)) – The other vector.

#### `Vector.SetMin(self, other)` <a id="c4d.Vector.SetMin"></a>

Set the minimum of each component.

*New in version R26.*

**Parameters:** **other** ([*c4d.Vector*](#c4d.Vector)) – The other vector.

### Magic Methods <a id="c4d.Vector-method-Magic-Methods"></a>

#### `Vector.__abs__(self)` <a id="c4d.Vector.__abs__"></a>

Returns a vector with the absolute (positive) value of each component.

```python
>>> abs(c4d.Vector(-1, -2, -3))
Vector(1,2,3)
```

**Return type:** [c4d.Vector](#c4d.Vector)

**Returns:** The absolute vector.

#### `Vector.__add__(self, other)` <a id="c4d.Vector.__add__"></a>

Adds an operand to the vector.

```python
>>> c4d.Vector(1, 2, 3) + 1
Vector(2,3,4)

>>> c4d.Vector(1, 2, 3) + c4d.Vector(2, 3, 4)
Vector(3,5,7)
```

**Parameters:** **other** (*Union*[[*c4d.Vector*](#c4d.Vector), *int*, *float*]) – The other operand.

**Return type:** [c4d.Vector](#c4d.Vector)

**Returns:** The resulting vector.

#### `Vector.__del__(self)` <a id="c4d.Vector.__del__"></a>

Not implemented.

> **Note:** The [`Vector`](#c4d.Vector) does not support item deletion, e.g., by calling *del(v[0])*.

**Raise:** TypeError.

#### `Vector.__div__(self, other)` <a id="c4d.Vector.__div__"></a>

Divides each vector component by a scalar.

```python
>>> c4d.Vector(1, 2, 3) / 5
Vector(0.2, 0.4, 0.6)
```

**Parameters:** **other** (*Union*[*int*, *float*]) – The other operand.

**Return type:** [c4d.Vector](#c4d.Vector)

**Returns:** The resulting vector.

#### `Vector.__eq__(self, other)` <a id="c4d.Vector.__eq__"></a>

Checks if two vectors are equal.

**Parameters:** **other** ([*c4d.Vector*](#c4d.Vector)) – The other vector.

**Return type:** bool

**Returns:** **True** if both vectors are equal.

#### `Vector.__ge__(self, other)` <a id="c4d.Vector.__ge__"></a>

Not implemented.

**Raise:** *TypeError*.

#### `Vector.__getitem__(self, key)` <a id="c4d.Vector.__getitem__"></a>

Retrieves the value of the *x*, *y* or *z* component of the vector.  
The component is identified by an index in the interval *[0, 2]*.

*New in version R14.014.*

```python
>>> v = c4d.Vector(1, 2, 3)
>>> v[0]
1.0
>>> v[1]
2.0
>>> v[2]
3.0
```

**Parameters:** **key** (*int*) – The component index.

**Raises:** **IndexError** – When *key* does not satisfy *0 <= key < 2*.

**Return type:** float

**Returns:** The vector component.

#### `Vector.__gt__(self, other)` <a id="c4d.Vector.__gt__"></a>

Not implemented.

**Raise:** *TypeError*.

#### `Vector.__hash__(self)` <a id="c4d.Vector.__hash__"></a>

Returns the hash code of the vector used for hash maps and comparisons.

*New in version R26.*

**Returns:** The vector’s hash code.

**Return type:** int

#### `Vector.__init__(self, x=0.0, y=0.0, z=0.0)` <a id="c4d.Vector.__init__"></a>

Initializes a new [`Vector`](#c4d.Vector).  
All arguments are optional so it is possible to create a new vector without any arguments. All components are simply *0*.  
Otherwise *x* can be a [`Vector`](#c4d.Vector) so all components of the passed vector will be copied to the new vector.  
If only a number is passed, all components will be set to this.

```python
>>> c4d.Vector()
Vector(0,0,0)

>>> c4d.Vector(100)
Vector(100,100,100)

>>> v = c4d.Vector(100, 100, 100)
>>> c4d.Vector(v)
Vector(100,100,100)

>>> c4d.Vector(1, 2, 3)
Vector(1,2,3)
```

**Parameters:**

- **x** (*Optional*[*Union*[*int*, *float*, [*c4d.Vector*](#c4d.Vector)]]) – If *x* is a number and is the only passed argument, set this to all components. If *x* is a vector, clone it. Otherwise set the X component.
- **y** (*Optional*[*Union*[*int*, *float*]]) – Set the Y component.
- **z** (*Optional*[*Union*[*int*, *float*]]) – Set the Z component.

#### `Vector.__invert__(self)` <a id="c4d.Vector.__invert__"></a>

Returns the normalized vector.

```python
>>> ~c4d.Vector(1, 2, 3)
Vector(0.267,0.535,0.802)
```

**Return type:** [c4d.Vector](#c4d.Vector)

**Returns:** The normalized vector.

#### `Vector.__le__(self, other)` <a id="c4d.Vector.__le__"></a>

Not implemented.

**Raise:** *TypeError*.

#### `Vector.__lt__(self, other)` <a id="c4d.Vector.__lt__"></a>

Not implemented.

**Raise:** *TypeError*.

#### `Vector.__mod__(self, other)` <a id="c4d.Vector.__mod__"></a>

Calculates the cross product of the vector and an operand.

```python
>>> c4d.Vector(1, 0, 0) % c4d.Vector(0, 1, 0)
Vector(0, 0, 1)
```

**Parameters:** **other** ([*c4d.Vector*](#c4d.Vector)) – The other operand.

**Return type:** [c4d.Vector](#c4d.Vector)

**Returns:** The resulting vector.

#### `Vector.__mul__(self, other)` <a id="c4d.Vector.__mul__"></a>

Calculates the product of the vector and an left-side operand.  
If *other* is a float, it multiplies each vector component by the scalar.  
If *other* is a vector, calculates the dot product of the vectors.  
If *other* is a matrix, the vector is transformed by it, including translations.

> **See also:**
>
> `Vector.__xor__()` is the operator implementation for alternative product operations.

```python
>>> u = c4d.Vector(1, 0, 0)
>>> v = c4d.Vector(2, 0, 0)

>>> # A transform rotating by 90° ccw and translating by 100 units on v3 (i.e., the 
>>> # z-axis, the basis vector k).
>>> M = c4d.Matrix(v1=c4d.Vector( 0, 1, 0),
                   v2=c4d.Vector(-1, 0, 0),
                   v3=c4d.Vector( 0, 0, 1),
                   off=c4d.Vector(0, 0, 100))

>>> # Calculates the dot product of u and v.
>>> u * v
2.0

>>> # Scales u by the factor of 5.
>>> u * 5.
Vector(5, 0, 0)

>>> # Transforms u by M, including translations.
>>> u * M
Vector(0, 1, 100)
```

**Parameters:** **other** (*Union*[*int*, *float*, [*c4d.Vector*](#c4d.Vector), [*c4d.Matrix*](../Matrix/index.md#c4d.Matrix)]) – The other operand.

**Return type:** Union[[c4d.Vector](#c4d.Vector), float]

**Returns:** A float, if **other** is of type [`Vector`](#c4d.Vector). | A vector, if *other* is of type float or [`Matrix`](../Matrix/index.md#c4d.Matrix).

#### `Vector.__ne__(self, other)` <a id="c4d.Vector.__ne__"></a>

Check if two vectors are not equal.

**Parameters:** **other** ([*c4d.Vector*](#c4d.Vector)) – The other vector.

**Return type:** bool

**Returns:** **True** if both vectors are not equal.

#### `Vector.__neg__(self)` <a id="c4d.Vector.__neg__"></a>

Returns the inverse of the vector.

```python
>>> -c4d.Vector(1, 2, 3)
Vector(-1,-2,-3)
```

**Return type:** [c4d.Vector](#c4d.Vector)

**Returns:** The inverse vector.

#### `Vector.__radd__(self, other)` <a id="c4d.Vector.__radd__"></a>

Adds the vector to an operand.

```python
>>> 1 + c4d.Vector(1, 2, 3)
Vector(2,3,4)

>>> c4d.Vector(1, 2, 3) + c4d.Vector(2, 3, 4)
Vector(3,5,7)
```

**Parameters:** **other** (*Union*[[*c4d.Vector*](#c4d.Vector), *int*, *float*]) – The other operand.

**Return type:** [c4d.Vector](#c4d.Vector)

**Returns:** The resulting vector.

#### `Vector.__rdiv__(self, other)` <a id="c4d.Vector.__rdiv__"></a>

Not implemented.

**Raise:** *TypeError*.

#### `Vector.__rmul__(self, other)` <a id="c4d.Vector.__rmul__"></a>

Calculates the product of the vector and a right-side operand.  
If *other* is a float, it multiplies each vector component by the scalar.  
If *other* is a matrix, the vector is transformed by it, including translations.

```python
>>> u = c4d.Vector(1, 0, 0)
>>> v = c4d.Vector(2, 0, 0)

>>> # A transform rotating by 90° ccw and translating by 100 units on v3 (i.e., the 
>>> # z-axis, the basis vector k).
>>> M = c4d.Matrix(v1=c4d.Vector( 0, 1, 0),
                   v2=c4d.Vector(-1, 0, 0),
                   v3=c4d.Vector( 0, 0, 1),
                   off=c4d.Vector(0, 0, 100))

>>> # Calculates the dot product of u and v.
>>> u * v
2.0

>>> # Scales u by the factor of 5.
>>> 5. * u
Vector(5, 0, 0)

>>> # Transforms u by M, including translations.
>>> M * u
Vector(0, 1, 100)
```

**Parameters:** **other** (*Union*[*int*, *float*, [*c4d.Vector*](#c4d.Vector), [*c4d.Matrix*](../Matrix/index.md#c4d.Matrix)]) – The other operand.

**Return type:** Union[[c4d.Vector](#c4d.Vector), float]

**Returns:** A float, if **other** is of type [`Vector`](#c4d.Vector). | A vector, if *other* is of type float or [`Matrix`](../Matrix/index.md#c4d.Matrix).

#### `Vector.__rsub__(self, other)` <a id="c4d.Vector.__rsub__"></a>

Subtracts the vector from an operand.

```python
>>> 1 - c4d.Vector(1, 2, 3)
Vector(0,-1,-2)

>>> c4d.Vector(1, 2, 3) - c4d.Vector(2, 3, 4)
Vector(-1,-1,-1)
```

**Parameters:** **other** (*Union*[[*c4d.Vector*](#c4d.Vector), *int*, *float*]) – The other operand.

**Return type:** [c4d.Vector](#c4d.Vector)

**Returns:** The resulting vector.

#### `Vector.__rxor__(self, other)` <a id="c4d.Vector.__rxor__"></a>

Not implemented.

**Raise:** *TypeError*.

#### `Vector.__setitem__(self, key, value)` <a id="c4d.Vector.__setitem__"></a>

Assigns a value to the *x*, *y* or *z* component of the vector.  
The component is identified by an index in the interval *[0, 2]*.

*New in version R14.014.*

```python
>>> v = c4d.Vector(1, 2, 3)
>>> v[0] = 0
>>> v
Vector(0, 2, 3)
```

**Parameters:**

- **key** (*int*) – The component index.
- **value** (*Union*[*float*, *int*]) – The new vector component.

**Raises:** **IndexError** – When *key* does not satisfy *0 <= key < 2*.

#### `Vector.__str__(self)` <a id="c4d.Vector.__str__"></a>

Returns a string representation of the vector.  
Called if [str()](https://docs.python.org/3.9/library/functions.html#func-str) is invoked on a vector object. See [object.__str__()](https://docs.python.org/3.9/reference/datamodel.html#object.__str__) for more information on Python’s data model.

```python
>>> c4d.Vector(30, 40, 2)
Vector(30.0, 40.0, 2.0)
```

**Return type:** str

**Returns:** The Vector as string.

#### `Vector.__sub__(self, other)` <a id="c4d.Vector.__sub__"></a>

Subtracts an operand from the vector.

```python
>>> c4d.Vector(1, 2, 3) - 1
Vector(0,1,2)

c4d.Vector(1, 2, 3) - c4d.Vector(2, 3, 4)
Vector(-1,-1,-1)
```

**Parameters:** **other** (*Union*[[*c4d.Vector*](#c4d.Vector), *int*, *float*]) – The other operand.

**Return type:** [c4d.Vector](#c4d.Vector)

**Returns:** The resulting vector.

#### `Vector.__xor__(self, other)` <a id="c4d.Vector.__xor__"></a>

Calculates an alternative product operation of the vector and a left-side operand.  
If *other* is a vector, calculates the component-wise product of the vectors.  
If *other* is a matrix, the vector is transformed by it, excluding translations.

> **See also:**
>
> `Vector.__mul__()` is the operator implementation for the primary product operations.

```python
>>> u = c4d.Vector(1, 0, 0)
>>> v = c4d.Vector(2, 0, 0)

>>> # A transform rotating by 90° ccw and translating by 100 units on v3 (i.e., the 
>>> # z-axis, the basis vector k).
>>> M = c4d.Matrix(v1=c4d.Vector( 0, 1, 0),
                   v2=c4d.Vector(-1, 0, 0),
                   v3=c4d.Vector( 0, 0, 1),
                   off=c4d.Vector(0, 0, 100))

>>> # Computes the component-wise product of u and v.
>>> u ^ v
Vector(2, 0, 0)

>>> # Transforms u by M, excluding translations. 
>>> u ^ M
Vector(0, 1, 0)
```

**Parameters:** **other** (*Union*[[*c4d.Vector*](#c4d.Vector), [*c4d.Matrix*](../Matrix/index.md#c4d.Matrix)]) – The other operand.

**Return type:** Union[[c4d.Vector](#c4d.Vector), float]

**Returns:** A float, if **other** is of type [`Vector`](#c4d.Vector). | A vector, if *other* is of type float or [`Matrix`](../Matrix/index.md#c4d.Matrix).

### Magnitude And Normalization <a id="c4d.Vector-method-Magnitude-And-Normalization"></a>

#### `Vector.GetLength(self)` <a id="c4d.Vector.GetLength"></a>

Calculates the length of the vector.

**Return type:** float

**Returns:** The length.

#### `Vector.GetLengthSquared(self)` <a id="c4d.Vector.GetLengthSquared"></a>

Calculates the squared length of the vector.

*Deprecated since version R26.000:* Use `Vector.GetSquaredLength()` instead.

**Return type:** float

**Returns:** The squared length.

#### `Vector.GetNormalized(self)` <a id="c4d.Vector.GetNormalized"></a>

Calculates the normalized vector, so that [`GetLength()`](#c4d.Vector.GetLength) returns *1.0*.

**Return type:** [c4d.Vector](#c4d.Vector)

**Returns:** The normalized vector.

#### `Vector.GetSquaredLength(self)` <a id="c4d.Vector.GetSquaredLength"></a>

Returns the squared length of the vector.

*New in version R26.*

**Returns:** The squared length of the vector.

**Return type:** float

#### `Vector.Normalize(self)` <a id="c4d.Vector.Normalize"></a>

Normalizes the vector, so that [`GetLength()`](#c4d.Vector.GetLength) returns *1.0*.

### Spatial Operations <a id="c4d.Vector-method-Spatial-Operations"></a>

#### `Vector.Cross(self, v2)` <a id="c4d.Vector.Cross"></a>

Calculates the cross product of the vector and vector **v2**.

**Parameters:** **v2** ([*c4d.Vector*](#c4d.Vector)) – The other vector.

**Return type:** [c4d.Vector](#c4d.Vector)

**Returns:** The result.

#### `Vector.Dot(self, v2)` <a id="c4d.Vector.Dot"></a>

Calculates the dot product of the vector and vector **v2**.

**Parameters:** **v2** ([*c4d.Vector*](#c4d.Vector)) – The second vector.

**Return type:** float

**Returns:** The dot product.

#### `Vector.GetAngle(self, other)` <a id="c4d.Vector.GetAngle"></a>

Calculates angle (in radians) between v1 and v2.

*New in version R26.*

**Parameters:** **other** ([*c4d.Vector*](#c4d.Vector)) – The other vector.

**Returns:** The angle.

**Return type:** float

#### `Vector.GetRightRotated(self, rots)` <a id="c4d.Vector.GetRightRotated"></a>

Returns a vector where the components have been rotated to the right (in the usual (x, y, z)-representation). E.g., with a value of 1 for rots, the result will be (z, x, y).

> *New in version R26.*

**Parameters:** **rots** (*int*) – Number of rotations, may be negative. The result depends only on the number modulo 3.

**Returns:** A new rotated vector.

**Return type:** [c4d.Vector](#c4d.Vector)
