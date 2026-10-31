<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/Matrix/index.html -->

# c4d.Matrix <a id="c4d-matrix"></a>

## *class* `c4d.Matrix` <a id="c4d.Matrix"></a>

A type to represent a transform.

> **See also:** [Matrices](../../../manuals/manual_matrices.md#matrix-fundamental)

> **Warning:** The Matrix type does not support the function *copy.copy()*, please use the [`Matrix`](#c4d.Matrix) copy constructor instead.
>
> ```python
> >>> import c4d
> >>> import copy
>
> >>> # An identity matrix and its Python object id.
> >>> m = c4d.Matrix()
> >>> id(m), m
> (2671923600768, Matrix(v1: (1, 0, 0); v2: (0, 1, 0); v3: (0, 0, 1); off: (0, 0, 0)))
>
> >>> # We are only creating a reference to the same object.
> >>> ref = m
> >>> id(ref), ref
> (2671923600768, Matrix(v1: (1, 0, 0); v2: (0, 1, 0); v3: (0, 0, 1); off: (0, 0, 0)))
>
> >>> # Cinema's types usually do not work with Python's copy module.
> >>> copy.deepcopy(m)
> ...
> TypeError: can't pickle c4d.Matrix objects.
>
> >>> # But we can copy objects via copy constructors.
> >>> copy = c4d.Matrix(m)
> >>> id(copy), copy
> (2671923600512, Matrix(v1: (1, 0, 0); v2: (0, 1, 0); v3: (0, 0, 1); off: (0, 0, 0)))
> ```

**Attributes**

## `c4d.Matrix.v1` <a id="c4d.Matrix.v1"></a>

The X axis of a left-handed coordinate system.

**Type:** [`Vector`](../Vector/index.md#c4d.Vector)

## `c4d.Matrix.v2` <a id="c4d.Matrix.v2"></a>

The Y axis of a left-handed coordinate system.

**Type:** [`Vector`](../Vector/index.md#c4d.Vector)

## `c4d.Matrix.v3` <a id="c4d.Matrix.v3"></a>

The Z axis of a left-handed coordinate system.

**Type:** [`Vector`](../Vector/index.md#c4d.Vector)

## `c4d.Matrix.off` <a id="c4d.Matrix.off"></a>

The translation vector.

**Type:** [`Vector`](../Vector/index.md#c4d.Vector)

## Overview <a id="overview"></a>

**Magic Methods**

- [`Matrix.__add__()`](#c4d.Matrix.__add__): Adds two matrices.
- [`Matrix.__div__()`](#c4d.Matrix.__div__): Divides each element in the matrix by a scalar.
- [`Matrix.__eq__()`](#c4d.Matrix.__eq__): Checks if two matrices are equal.
- [`Matrix.__ge__()`](#c4d.Matrix.__ge__): raise NotImplemented.
- [`Matrix.__gt__()`](#c4d.Matrix.__gt__): raise NotImplemented.
- [`Matrix.__init__()`](#c4d.Matrix.__init__): Initializes a new [`Matrix`](#c4d.Matrix).
- [`Matrix.__invert__()`](#c4d.Matrix.__invert__): Inverts the matrix.
- [`Matrix.__le__()`](#c4d.Matrix.__le__): raise NotImplemented.
- [`Matrix.__lt__()`](#c4d.Matrix.__lt__): raise NotImplemented.
- [`Matrix.__mul__()`](#c4d.Matrix.__mul__): Computes the product of the [`Matrix`](#c4d.Matrix) and another type.
- [`Matrix.__ne__()`](#c4d.Matrix.__ne__): Checks if two matrices are not equal.
- [`Matrix.__rdiv__()`](#c4d.Matrix.__rdiv__): Not implemented.
- [`Matrix.__rmul__()`](#c4d.Matrix.__rmul__): Computes the product of another type and the [`Matrix`](#c4d.Matrix).
- [`Matrix.__str__()`](#c4d.Matrix.__str__): Returns a string representation of the Matrix object.
- [`Matrix.__sub__()`](#c4d.Matrix.__sub__): Subtracts two matrices.

**Normalization**

- [`Matrix.GetNormalized()`](#c4d.Matrix.GetNormalized): Returns the normalized matrix for the instance.
- [`Matrix.Normalize()`](#c4d.Matrix.Normalize): Normalizes the frame of the instance.

**Scale And Tensor Properties**

- [`Matrix.GetScale()`](#c4d.Matrix.GetScale): Returns the scale stored by the matrix.
- [`Matrix.GetTensorMatrix()`](#c4d.Matrix.GetTensorMatrix): Returns the matrix’ tensor.
- [`Matrix.Scale()`](#c4d.Matrix.Scale): Performs uniform matrix scaling (float) or non-uniform matrix scaling (vector).

**Vector Transformation**

- [`Matrix.Mul()`](#c4d.Matrix.Mul): Multiply the vector by the matrix, this includes any translation in the matrix.
- [`Matrix.MulV()`](#c4d.Matrix.MulV): Multiply the vector by the matrix, this does not include any translation.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.Matrix-method-Magic-Methods"></a>

#### `Matrix.__add__(self, other)` <a id="c4d.Matrix.__add__"></a>

Adds two matrices.

**Parameters:** **other** ([*c4d.Matrix*](#c4d.Matrix)) – The other matrix.

**Return type:** [c4d.Matrix](#c4d.Matrix)

**Returns:** The result matrix.

#### `Matrix.__div__(self, other)` <a id="c4d.Matrix.__div__"></a>

Divides each element in the matrix by a scalar.

**Parameters:** **other** (*float*) – The scalar.

**Return type:** [c4d.Matrix](#c4d.Matrix)

**Returns:** The result matrix.

#### `Matrix.__eq__(self, other)` <a id="c4d.Matrix.__eq__"></a>

Checks if two matrices are equal.

**Parameters:** **other** ([*c4d.Matrix*](#c4d.Matrix)) – The other matrix.

**Return type:** bool

**Returns:** **True** if matrices are equal.

#### `Matrix.__ge__(self, other)` <a id="c4d.Matrix.__ge__"></a>

raise NotImplemented.

#### `Matrix.__gt__(self, other)` <a id="c4d.Matrix.__gt__"></a>

raise NotImplemented.

#### `Matrix.__init__(self, off=<_custom_c4d.Vector object at 0x0000012D720635E0>, v1=<_custom_c4d.Vector object at 0x0000012D72072820>, v2=<_custom_c4d.Vector object at 0x0000012D72079C60>, v3=<_custom_c4d.Vector object at 0x0000012D7206EF20>)` <a id="c4d.Matrix.__init__"></a>

Initializes a new [`Matrix`](#c4d.Matrix).  
A Matrix is the type to represent linear transforms in Cinema 4D. A Matrix has four components:

- v1 is the x-axis or the basis vector i of the frame of the linear transform defined by an Matrix instance.
- v2 is the y-axis or the basis vector j of the frame of the linear transform defined by an Matrix instance.
- v3 is the z-axis or the basis vector k of the frame of the linear transform defined by an Matrix instance.
- off is the additional translation component for an [`c4d.Matrix`](#c4d.Matrix) instance.

A matrix can be instantiated in multiple ways, since all its constructor arguments are optional:

```python
>>> # The Matrix constructor with no arguments will give us the identity 
>>> # matrix with the zero vector as the offset.
>>> c4d.Matrix()
Matrix(v1: (1, 0, 0); v2: (0, 1, 0); v3: (0, 0, 1); off: (0, 0, 0)

>>> # Here we define only the frame of the Matrix in its arguments, it 
>>> # will rotate by 90° ccw on the z-axis.
>>> m = c4d.Matrix(v1=c4d.Vector( 0, 1, 0),
                   v2=c4d.Vector(-1, 0, 0),
                   v3=c4d.Vector( 0, 0, 1))
>>> m
Matrix(v1: (0, 1, 0); v2: (-1, 0, 0); v3: (0, 0, 1); off: (0, 0, 0))

>>> # We can also modify components of an instance. 
>>> m.off = c4d.Vector(100, 0, 0)
>>> m
Matrix(v1: (0, 1, 0); v2: (-1, 0, 0); v3: (0, 0, 1); off: (100, 0, 0))
```

**Parameters:**

- **off** (*Optional*[[*c4d.Vector*](../Vector/index.md#c4d.Vector)]) – The translation vector.
- **v1** (*Optional*[[*c4d.Vector*](../Vector/index.md#c4d.Vector)]) – The X axis of a left-handed coordinate system.
- **v2** (*Optional*[[*c4d.Vector*](../Vector/index.md#c4d.Vector)]) – The Y axis of a left-handed coordinate system.
- **v3** (*Optional*[[*c4d.Vector*](../Vector/index.md#c4d.Vector)]) – The Z axis of a left-handed coordinate system.

#### `Matrix.__invert__(self)` <a id="c4d.Matrix.__invert__"></a>

Inverts the matrix.

```python
>>> u = c4d.Vector(1, 0, 0)

>>> # A transform rotating by 90° ccw and translating by 100 units on v3.
>>> M = c4d.Matrix(v1=c4d.Vector(0, 1, 0),
                   v2=c4d.Vector(-1, 0, 0),
                   v3=c4d.Vector(0, 0, 1),
                   off=c4d.Vector(0, 0, 100))
>>> M
Matrix(v1: (0, 1, 0); v2: (-1, 0, 0); v3: (0, 0, 1); off: (0, 0, 100))

>>> The inverse of M is the inverse transform of M.
>>> ~M
Matrix(v1: (0, -1, 0); v2: (1, 0, 0); v3: (0, 0, 1); off: (0, 0, -100))

>>> Applying the inverse of M to the point u transformed by M will yield u again.
>>> v = u * M
>>> v
Vector(0, 1, 100)
>>> v * ~M
Vector(1, 0, 0)
```

**Return type:** [c4d.Matrix](#c4d.Matrix)

**Returns:** The inverted matrix.

#### `Matrix.__le__(self, other)` <a id="c4d.Matrix.__le__"></a>

raise NotImplemented.

#### `Matrix.__lt__(self, other)` <a id="c4d.Matrix.__lt__"></a>

raise NotImplemented.

#### `Matrix.__mul__(self, other)` <a id="c4d.Matrix.__mul__"></a>

Computes the product of the [`Matrix`](#c4d.Matrix) and another type.  
If *other* is of type [`Matrix`](#c4d.Matrix), it computes the matrix product `self * other`.  
If *other* is of type [`Vector`](../Vector/index.md#c4d.Vector), it will return the transform of *other* by *self*, including the translation defined in *self*.

```python
>>> import math

>>> u = c4d.Vector(1, 0, 0)
>>> quarter_pi = math.pi * .25

>>> # A transform rotating by 90° ccw and translating by 100 units on v3.
M = c4d.Matrix(v1=c4d.Vector(0, 1, 0),
               v2=c4d.Vector(-1, 0, 0),
               v3=c4d.Vector(0, 0, 1),
               off=c4d.Vector(0, 0, 100))

>>> # Transforms u by M, including translations.
>>> M * u
Vector(0, 1, 100)

>>> # A transform rotating by 45° ccw on the x-axis.
>>> X = c4d.utils.MatrixRotX(quarter_pi)
>>> X
Matrix(v1: (1, 0, 0); v2: (0, 0.707, -0.707); v3: (0, 0.707, 0.707); off: (0, 0, 0))

>>> # A transform rotating by 45° cw on the y-axis.
>>> Y = c4d.utils.MatrixRotY(-quarter_pi)
>>> Y
Matrix(v1: (0.707, 0, -0.707); v2: (0, 1, 0); v3: (0.707, 0, 0.707); off: (0, 0, 0))

>>> # A transform rotating by 45° ccw on the z-axis.
>>> Z = c4d.utils.MatrixRotZ(quarter_pi)
>>> Z
Matrix(v1: (0.707, -0.707, 0); v2: (0.707, 0.707, 0); v3: (0, 0, 1); off: (0, 0, 0))

>>> # The product of the three matrices is a matrix rotating by 45° ccw on x, then 45° cw 
>>> # on y and finally by 45° ccw on z.
>>> X * Y * Z
Matrix(v1: (0.5, -0.854, 0.146); v2: (0.5, 0.146, -0.854); v3: (0.707, 0.5, 0.5); off: (0, 0, 0))

>>> # Due to matrix multiplication not being commutative, executing the transforms in a 
>>> # different order will yield another matrix product.
>>> Z * Y * X
Matrix(v1: (0.5, -0.5, -0.707); v2: (0.146, 0.854, -0.5); v3: (0.854, 0.146, 0.5); off: (0, 0, 0))
```

**Parameters:** **other** (*Union*[[*c4d.Matrix*](#c4d.Matrix), [*c4d.Vector*](../Vector/index.md#c4d.Vector), *int*, *float*]) – The other operand.

**Return type:** Union[[c4d.Matrix](#c4d.Matrix), [c4d.Vector](../Vector/index.md#c4d.Vector)]

**Returns:** The resulting matrix or vector.

#### `Matrix.__ne__(self, other)` <a id="c4d.Matrix.__ne__"></a>

Checks if two matrices are not equal.

**Parameters:** **other** ([*c4d.Matrix*](#c4d.Matrix)) – The other matrix.

**Return type:** bool

**Returns:** **True** if matrices are not equal.

#### `Matrix.__rdiv__(self, other)` <a id="c4d.Matrix.__rdiv__"></a>

Not implemented.

**Raise:** *TypeError*.

#### `Matrix.__rmul__(self, other)` <a id="c4d.Matrix.__rmul__"></a>

Computes the product of another type and the [`Matrix`](#c4d.Matrix).  
If *other* is of type [`Vector`](../Vector/index.md#c4d.Vector), it will return the transform of *other* by *self*, including the translation defined in *self*.  
If *other* is a numeric type, it will scale each basis vector in *self* with it.

```python
>>> u = c4d.Vector(1, 0, 0)

>>> # A transform rotating by 90° ccw and translating by 100 units on v3.
>>> M = c4d.Matrix(v1=c4d.Vector( 0, 1, 0),
                   v2=c4d.Vector(-1, 0, 0),
                   v3=c4d.Vector( 0, 0, 1),
                   off=c4d.Vector(0, 0, 100))

>>> # Transforms u by M, including translations.
>>> u * M
Vector(0, 1, 100)

>>> # Scale each component of M by the factor of two.
>>> 2 * M
Matrix(v1: (0, 2, 0); v2: (-2, 0, 0); v3: (0, 0, 2); off: (0, 0, 200))
```

**Parameters:** **other** (*Union*[*int*, *float*, [*c4d.Vector*](../Vector/index.md#c4d.Vector)]) – The other operand.

**Return type:** Union[[c4d.Vector](../Vector/index.md#c4d.Vector), [c4d.Matrix](#c4d.Matrix)]

**Returns:** The resulting matrix or vector.

#### `Matrix.__str__(self)` <a id="c4d.Matrix.__str__"></a>

Returns a string representation of the Matrix object.  
Called if [str()](https://docs.python.org/3.9/library/functions.html#func-str) is invoked on a [`Matrix`](#c4d.Matrix) object. See [object.__str__()](https://docs.python.org/3.9/reference/datamodel.html#object.__str__) for more information on Python’s data model.

```python
>>> m = c4d.Matrix(v1=c4d.Vector( 0, 1, 0),
                   v2=c4d.Vector(-1, 0, 0),
                   v3=c4d.Vector( 0, 0, 1))
>>> print(m)
Matrix(v1: (0, 1, 0); v2: (-1, 0, 0); v3: (0, 0, 1); off: (0, 0, 0))
```

**Return type:** str

**Returns:** The Vector as string.

#### `Matrix.__sub__(self, other)` <a id="c4d.Matrix.__sub__"></a>

Subtracts two matrices.

**Parameters:** **other** ([*c4d.Matrix*](#c4d.Matrix)) – The other matrix.

**Return type:** [c4d.Matrix](#c4d.Matrix)

**Returns:** The result matrix.

### Normalization <a id="c4d.Matrix-method-Normalization"></a>

#### `Matrix.GetNormalized(self)` <a id="c4d.Matrix.GetNormalized"></a>

Returns the normalized matrix for the instance.

```python
>>> # A transform rotating by 90° ccw and translating by 100 units on v3.
>>> M = c4d.Matrix(v1=c4d.Vector( 0, 1, 0),
                   v2=c4d.Vector(-1, 0, 0),
                   v3=c4d.Vector( 0, 0, 1),
                   off=c4d.Vector(0, 0, 100))

>>> # Scale each component of M by the factor of two.
>>> N = 2 * M
>>> N
Matrix(v1: (0, 2, 0); v2: (-2, 0, 0); v3: (0, 0, 2); off: (0, 0, 200))

>>> # Returns the normalized form of N.
>>> N.GetNormalized()
Matrix(v1: (0, 1, 0); v2: (-1, 0, 0); v3: (0, 0, 1); off: (0, 0, 200))
```

**Return type:** [c4d.Matrix](#c4d.Matrix)

**Returns:** The normalized matrix.

#### `Matrix.Normalize(self)` <a id="c4d.Matrix.Normalize"></a>

Normalizes the frame of the instance.

```python
>>> # A transform rotating by 90° ccw and translating by 100 units on v3.
>>> M = c4d.Matrix(v1=c4d.Vector( 0, 1, 0),
                   v2=c4d.Vector(-1, 0, 0),
                   v3=c4d.Vector( 0, 0, 1),
                   off=c4d.Vector(0, 0, 100))

>>> # Scale each component of M by the factor of two.
>>> N = 2 * M
>>> N
Matrix(v1: (0, 2, 0); v2: (-2, 0, 0); v3: (0, 0, 2); off: (0, 0, 200))

>>> # Normalize the three basis vectors of N, i.e., set them to a length of 1.
>>> N.Normalize()
>>> N
Matrix(v1: (0, 1, 0); v2: (-1, 0, 0); v3: (0, 0, 1); off: (0, 0, 200))
```

### Scale And Tensor Properties <a id="c4d.Matrix-method-Scale-And-Tensor-Properties"></a>

#### `Matrix.GetScale(self)` <a id="c4d.Matrix.GetScale"></a>

Returns the scale stored by the matrix.

**Returns:** The scale.

**Return type:** [c4d.Vector](../Vector/index.md#c4d.Vector)

#### `Matrix.GetTensorMatrix(self)` <a id="c4d.Matrix.GetTensorMatrix"></a>

Returns the matrix’ tensor.

**Return type:** [c4d.Matrix](#c4d.Matrix)

**Returns:** The tensor matrix.

#### `Matrix.Scale(self, v)` <a id="c4d.Matrix.Scale"></a>

Performs uniform matrix scaling (float) or non-uniform matrix scaling (vector).

**Parameters:** **v** (*Union*[[*c4d.Vector*](../Vector/index.md#c4d.Vector), *float*]) – The scaling scalar.

### Vector Transformation <a id="c4d.Matrix-method-Vector-Transformation"></a>

#### `Matrix.Mul(self, v)` <a id="c4d.Matrix.Mul"></a>

Multiply the vector by the matrix, this includes any translation in the matrix.

> **Note:** This is a verbose form of *Vector.__mul__ \<c4d.Vector.__mul__*.

**Parameters:** **v** ([*c4d.Vector*](../Vector/index.md#c4d.Vector)) – The vector to multiply.

**Return type:** [c4d.Vector](../Vector/index.md#c4d.Vector)

**Returns:** The resulting vector.

#### `Matrix.MulV(self, v)` <a id="c4d.Matrix.MulV"></a>

Multiply the vector by the matrix, this does not include any translation.

> **Note:** This is a verbose form of *Vector.__xor__ \<c4d.Vector.__xor__*.

**Parameters:** **v** ([*c4d.Vector*](../Vector/index.md#c4d.Vector)) – The vector to multiply.

**Return type:** [c4d.Vector](../Vector/index.md#c4d.Vector)

**Returns:** The resulting vector.
