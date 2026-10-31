<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/Vector4d/index.html -->

# c4d.Vector4d <a id="c4d-vector4d"></a>

## *class* `c4d.Vector4d` <a id="c4d.Vector4d"></a>

*New in version R18.020.*

**Attributes**

## `c4d.Vector4d.x` <a id="c4d.Vector4d.x"></a>

X component of the vector.

**Type:** float

## `c4d.Vector4d.y` <a id="c4d.Vector4d.y"></a>

Y component of the vector.

**Type:** float

## `c4d.Vector4d.z` <a id="c4d.Vector4d.z"></a>

Z component of the vector.

**Type:** float

## `c4d.Vector4d.w` <a id="c4d.Vector4d.w"></a>

W component of the vector.

**Type:** float

## Overview <a id="overview"></a>

**Coordinate Conversion**

- [`Vector4d.GetVector3()`](#c4d.Vector4d.GetVector3): Retrieves a [`c4d.Vector`](../Vector/index.md#c4d.Vector) from the [`c4d.Vector4d`](#c4d.Vector4d).
- [`Vector4d.MakeVector3()`](#c4d.Vector4d.MakeVector3): Scales the vector so that `Vector4d.w` equals *1*.
- [`Vector4d.NormalizeW()`](#c4d.Vector4d.NormalizeW): Scales the vector so that `Vector4d.w` equals *1*.

**Magic Methods**

- [`Vector4d.__add__()`](#c4d.Vector4d.__add__): Adds another [`c4d.Vector4d`](#c4d.Vector4d) to the [`c4d.Vector4d`](#c4d.Vector4d)
- [`Vector4d.__del__()`](#c4d.Vector4d.__del__): Not implemented.
- [`Vector4d.__eq__()`](#c4d.Vector4d.__eq__): Checks if 2 vectors are equal.
- [`Vector4d.__ge__()`](#c4d.Vector4d.__ge__): Not implemented.
- [`Vector4d.__getitem__()`](#c4d.Vector4d.__getitem__): Retrieves X/Y/Z/W components by index
- [`Vector4d.__gt__()`](#c4d.Vector4d.__gt__): Not implemented.
- [`Vector4d.__init__()`](#c4d.Vector4d.__init__): Initializes a new [`Vector4d`](#c4d.Vector4d).
- [`Vector4d.__le__()`](#c4d.Vector4d.__le__): Not implemented.
- [`Vector4d.__lt__()`](#c4d.Vector4d.__lt__): Not implemented.
- [`Vector4d.__mul__()`](#c4d.Vector4d.__mul__): If *other* is a [`c4d.Vector4d`](#c4d.Vector4d), multiplies each vector component in the left-hand vector by its counterpart in the right-hand vector and returns the vector result.
- [`Vector4d.__ne__()`](#c4d.Vector4d.__ne__): Check if 2 vectors are not equal.
- [`Vector4d.__rmul__()`](#c4d.Vector4d.__rmul__): Not implemented.
- [`Vector4d.__setitem__()`](#c4d.Vector4d.__setitem__): Assigns X/Y/Z/W components by index
- [`Vector4d.__str__()`](#c4d.Vector4d.__str__): Returns a string representation of the Vector4D object.
- [`Vector4d.__sub__()`](#c4d.Vector4d.__sub__): Subtracts another [`c4d.Vector4d`](#c4d.Vector4d) from the [`c4d.Vector4d`](#c4d.Vector4d)

**Vector Operations**

- [`Vector4d.Dot()`](#c4d.Vector4d.Dot): Calculates the dot product of the [`c4d.Vector4d`](#c4d.Vector4d) and [`c4d.Vector4d`](#c4d.Vector4d) *b*.
- [`Vector4d.SetZero()`](#c4d.Vector4d.SetZero): Sets all vector components to zero.

## Members <a id="members"></a>

### Coordinate Conversion <a id="c4d.Vector4d-method-Coordinate-Conversion"></a>

#### `Vector4d.GetVector3(self)` <a id="c4d.Vector4d.GetVector3"></a>

Retrieves a [`c4d.Vector`](../Vector/index.md#c4d.Vector) from the [`c4d.Vector4d`](#c4d.Vector4d).

**Return type:** [`c4d.Vector`](../Vector/index.md#c4d.Vector)

**Returns:** The converted [`c4d.Vector`](../Vector/index.md#c4d.Vector).

#### `Vector4d.MakeVector3(self)` <a id="c4d.Vector4d.MakeVector3"></a>

Scales the vector so that `Vector4d.w` equals *1*.

#### `Vector4d.NormalizeW(self)` <a id="c4d.Vector4d.NormalizeW"></a>

Scales the vector so that `Vector4d.w` equals *1*.

*New in version R20.*

### Magic Methods <a id="c4d.Vector4d-method-Magic-Methods"></a>

#### `Vector4d.__add__(self, other)` <a id="c4d.Vector4d.__add__"></a>

Adds another [`c4d.Vector4d`](#c4d.Vector4d) to the [`c4d.Vector4d`](#c4d.Vector4d)

```python
>>> c4d.Vector4d(1, 2, 3, 4) + c4d.Vector4d(2, 3, 4, 5)
Vector4d(3, 5, 7, 9)
```

**Parameters:** **other** ([*c4d.Vector4d*](#c4d.Vector4d)) – The other vector.

**Return type:** [`c4d.Vector4d`](#c4d.Vector4d)

**Returns:** The resulting vector.

#### `Vector4d.__del__(self)` <a id="c4d.Vector4d.__del__"></a>

Not implemented.

> **Note:** The [`Vector4d`](#c4d.Vector4d) does not support item deletion, e.g., by calling *del(v[0])*.

**Raise:** TypeError.

#### `Vector4d.__eq__(self, other)` <a id="c4d.Vector4d.__eq__"></a>

Checks if 2 vectors are equal.

**Parameters:** **other** ([*c4d.Vector4d*](#c4d.Vector4d)) – The other vector.

**Return type:** bool

**Returns:** **True** if both vectors are equal, otherwise **False**.

#### `Vector4d.__ge__(self, other)` <a id="c4d.Vector4d.__ge__"></a>

Not implemented.

**Raise:** *TypeError*.

#### `Vector4d.__getitem__(self, key)` <a id="c4d.Vector4d.__getitem__"></a>

Retrieves X/Y/Z/W components by index

```python
>>> v = c4d.Vector4d(1, 2, 3, 4)
>>> v[0]
1
>>> v[1]
2
>>> v[2]
3
>>> v[3]
4
```

**Parameters:** **key** (*int*) – The component index.

**Raises:** **IndexError** – If the index *key* is out of range : *0<=key<3*.

**Return type:** float

**Returns:** The [`c4d.Vector4d`](#c4d.Vector4d) component.

#### `Vector4d.__gt__(self, other)` <a id="c4d.Vector4d.__gt__"></a>

Not implemented.

**Raise:** *TypeError*.

#### `Vector4d.__init__(self, x, y, z, w)` <a id="c4d.Vector4d.__init__"></a>

Initializes a new [`Vector4d`](#c4d.Vector4d).  
All arguments are optional so it is possible to create a new vector without any arguments. X/Y/Z components are simply *0* and W *1*.  
If only 1 argument is passed, it can be either a number or [`c4d.Vector`](../Vector/index.md#c4d.Vector): - number: All components are set to this number. - [`c4d.Vector`](../Vector/index.md#c4d.Vector): X/Y/Z components of the passed vector are copied to the new vector and W is set *1*.  
If 2 arguments are passed: - The first argument has to be a [`c4d.Vector`](../Vector/index.md#c4d.Vector) and the second one a number. X/Y/Z components of the passed vector are copied to the new vector and W is set the number argument.  
If 4 arguments are passed: - *x*, *y*, *z*, *w* have to be floats and are respectively assigned to X/Y/Z/W components.

```python
>>> c4d.Vector4d()
Vector4d(0,0,0,1)

>>> c4d.Vector4d(5)
Vector4d(5, 5, 5, 5)

>>> v = c4d.Vector(5, 5, 5)
>>> c4d.Vector(v)
Vector4d(5, 5, 5, 1)

>>> c4d.Vector4d(1, 2, 3, 4)
Vector4d(1, 2, 3, 4)
```

**Parameters:**

- **x** (*Union*[*int*, *float*, [*c4d.Vector*](../Vector/index.md#c4d.Vector)]) – If *x* is a number and is the only passed argument, set this to X/Y/Z components. If *x* is a [`c4d.Vector`](../Vector/index.md#c4d.Vector), its X/Y/Z components are copied to the new vector. Otherwise set the X component.
- **y** (*number*) – The Y component. If 2 arguments are passed, set to W component.
- **z** (*number*) – The Z component.
- **w** (*number*) – The W component.

#### `Vector4d.__le__(self, other)` <a id="c4d.Vector4d.__le__"></a>

Not implemented.

**Raise:** *TypeError*.

#### `Vector4d.__lt__(self, other)` <a id="c4d.Vector4d.__lt__"></a>

Not implemented.

**Raise:** *TypeError*.

#### `Vector4d.__mul__(self, other)` <a id="c4d.Vector4d.__mul__"></a>

If *other* is a [`c4d.Vector4d`](#c4d.Vector4d), multiplies each vector component in the left-hand vector by its counterpart in the right-hand vector and returns the vector result.  
If *other* is a number, multiplies each vector components by the scalar and returns the vector result.

```python
>>> c4d.Vector4d(1, 2, 3, 4) * c4d.Vector4d(2, 3, 4, 5)
Vector4d(2, 6, 12, 20)

>>> c4d.Vector4d(1, 2, 3, 4) * 5
Vector4d(5, 10, 15, 20)
```

**Parameters:** **other** (*Union*[*int*, *float*, [*c4d.Vector*](../Vector/index.md#c4d.Vector)]) – The other operand.

**Return type:** [`c4d.Vector4d`](#c4d.Vector4d)

**Returns:** The resulting vector.

#### `Vector4d.__ne__(self, other)` <a id="c4d.Vector4d.__ne__"></a>

Check if 2 vectors are not equal.

**Parameters:** **other** ([*c4d.Vector4d*](#c4d.Vector4d)) – The other vector.

**Return type:** bool

**Returns:** **True** if both vectors are not equal, otherwise **False**.

#### `Vector4d.__rmul__(self, other)` <a id="c4d.Vector4d.__rmul__"></a>

Not implemented.

**Raise:** *TypeError*.

#### `Vector4d.__setitem__(self, key, value)` <a id="c4d.Vector4d.__setitem__"></a>

Assigns X/Y/Z/W components by index

```python
>>> v = c4d.Vector4d(1, 2, 3, 4)
>>> v[3] = 0
>>> v
Vector4d(1, 2, 3, 0)
```

**Parameters:**

- **key** (*int*) – The component index.
- **value** (*float*) – The new value for the [`c4d.Vector4d`](#c4d.Vector4d) component.

**Raises:** **IndexError** – If the index *key* is out of range : *0<=key<3*.

#### `Vector4d.__str__(self)` <a id="c4d.Vector4d.__str__"></a>

Returns a string representation of the Vector4D object.  
Called if [str()](https://docs.python.org/3.9/library/functions.html#func-str) is invoked on a [`Vector4d`](#c4d.Vector4d) object. See [object.__str__()](https://docs.python.org/3.9/reference/datamodel.html#object.__str__) for more information on Python’s data model.

```python
>>> c4d.Vector4d(3.0, 4.0, 2.0, 5.0)
Vector4d(3, 4, 2, 5)
```

**Return type:** str

**Returns:** The [`c4d.Vector4d`](#c4d.Vector4d) as string.

#### `Vector4d.__sub__(self, other)` <a id="c4d.Vector4d.__sub__"></a>

Subtracts another [`c4d.Vector4d`](#c4d.Vector4d) from the [`c4d.Vector4d`](#c4d.Vector4d)

```python
>>> c4d.Vector4d(1, 2, 3, 4) - c4d.Vector4d(2, 3, 4, 5)
Vector4d(-1, -1, -1, -1)
```

**Parameters:** **other** ([*c4d.Vector4d*](#c4d.Vector4d)) – The other vector.

**Return type:** [`c4d.Vector4d`](#c4d.Vector4d)

**Returns:** The resulting vector.

### Vector Operations <a id="c4d.Vector4d-method-Vector-Operations"></a>

#### `Vector4d.Dot(self, b)` <a id="c4d.Vector4d.Dot"></a>

Calculates the dot product of the [`c4d.Vector4d`](#c4d.Vector4d) and [`c4d.Vector4d`](#c4d.Vector4d) *b*.

**Parameters:** **b** ([*c4d.Vector4d*](#c4d.Vector4d)) – The other vector.

**Return type:** float

**Returns:** The dot product.

#### `Vector4d.SetZero(self)` <a id="c4d.Vector4d.SetZero"></a>

Sets all vector components to zero.
