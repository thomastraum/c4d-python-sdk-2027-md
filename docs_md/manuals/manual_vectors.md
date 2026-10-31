<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_vectors.html -->

# Vectors <a id="vectors"></a><a id="vector-fundamental"></a>

Explains how to carry out vector operations.

Positions, directions, and sizes in a Cinema 4D scene are all described by vectors. This manual explains what a [`c4d.Vector`](../modules/c4d/Vector/index.md#c4d.Vector) is and walks through the operations that the Cinema API provides for it. Matrices, which combine vectors into transforms, are explained in [Matrices](manual_matrices.md).

## Overview <a id="overview"></a>

A vector is a tuple of numbers. In mathematics, the tuple can have any number of components: two, three, or many more. The Cinema API’s [`c4d.Vector`](../modules/c4d/Vector/index.md#c4d.Vector) always has three components, `x`, `y`, and `z`.

In 3D Euclidean space, the components are coordinates relative to three basis vectors, which define the X, Y, and Z axes of a coordinate system. Starting at the origin, the dotted path follows the x, y, and z components in turn to point `P`. Offset dimension lines with short feet mark each step, and their labels show the component values. The arrow can also be read as a direction with magnitude. Cinema 4D uses a left-handed coordinate system: X points right, Y up, and Z away from the viewer. One unit is one centimeter.

> *Interactive figure (HTML only): A vector reaches point P from the origin. Dotted lines show the component path; offset dimension lines with feet show x, y, and z and their values. Drag the arrowhead to change the vector, orbit to inspect the coordinate system.*

## Operations <a id="operations"></a>

Select an operation to understand how it works.

<a id="item-addition"></a>

**Addition**

[Adding](https://en.wikipedia.org/wiki/Euclidean_vector#Addition_and_subtraction) two vectors chains two vectors together tip to end. Start at the origin, follow the first vector, and from where you end up, follow the second one. The result is the single arrow from the origin to that final point. The order does not matter, because both routes end at the same point.

```python
import c4d

a: c4d.Vector = c4d.Vector(2, 1, 1)
b: c4d.Vector = c4d.Vector(1, 2, 0.5)
r: c4d.Vector = a + b # (3, 3, 1)
```

> *Interactive figure (HTML only): The 3D sum of vectors a and b. Drag the arrowheads to change the operands, orbit to inspect the parallelogram.*

<a id="item-subtraction"></a>

**Subtraction**

[Subtracting](https://en.wikipedia.org/wiki/Euclidean_vector#Addition_and_subtraction) one vector from another gives is the vector that starts at the tip of the vector being subtracted and ends at the tip of the vector it is subtracted from. Swapping the two vectors makes the arrow point the other way.

```python
import c4d

a: c4d.Vector = c4d.Vector(3, 3, 1)
b: c4d.Vector = c4d.Vector(1, 2, 0.5)
r: c4d.Vector = a - b # (2, 1, 0.5)
```

> *Interactive figure (HTML only): The 3D difference a - b, drawn from the tip of b to the tip of a. Drag the arrowheads to change the operands.*

<a id="item-scalar-multiplication"></a>

**Scalar Multiplication**

Multiplying by a scalar stretches the vector, and a negative scalar also reverses it. The direction stays on the same line through the origin.

```python
import c4d

a: c4d.Vector = c4d.Vector(2, 1, 0.5)
k: float = 2.0
r: c4d.Vector = a * k # (4, 2, 1)
```

> *Interactive figure (HTML only): A 3D vector and its scalar multiple. Drag the arrowhead to change a, orbit to inspect the direction.*

<a id="item-component-wise-product"></a>

**Component-wise Product**

Multiplying two vectors component-wise means multiplying each corresponding component together. It is rarely needed apart from nulling components of a vector on specific axes.

```python
import c4d

a: c4d.Vector = c4d.Vector(2, 0.5, 1)
b: c4d.Vector = c4d.Vector(0.5, 2, 1)
r: c4d.Vector = a ^ b # (1, 1, 1)

# Nulling the x component of a vector in an ongoing calculation. Here we null the x component
# of the r-vector before adding it to another vector.
s: c4d.Vector = c4d.Vector(1, 2, 3) ^ (r ^ c4d.Vector(0, 1, 1))
```

> *Interactive figure (HTML only): The 3D component-wise product of vectors a and b. Drag the arrowheads to change the operands.*

<a id="item-normalization"></a>

**Normalization**

Normalizing keeps a vector’s direction and sets its length to one. The result is a unit vector on the unit sphere. `Normalize()` does the same in place. The zero vector cannot be normalized.

```python
import c4d

a: c4d.Vector = c4d.Vector(3, 2, 1)
r: c4d.Vector = a.GetNormalized()  # (0.802, 0.535, 0.267)
r: c4d.Vector = ~a  # alternative notation for normalization
```

> *Interactive figure (HTML only): A 3D vector and its unit vector on the unit sphere. Drag the arrowhead to change a.*

<a id="item-negation"></a>

**Negation**

Negation reverses a vector without changing its length. It is the same as multiplying by `-1`.

```python
import c4d

a: c4d.Vector = c4d.Vector(2, 1, 0.5)
r: c4d.Vector = -a  # (-2, -1, -0.5)
```

> *Interactive figure (HTML only): A 3D vector and its negation, pointing in opposite directions. Drag the arrowhead to change a.*

<a id="item-length"></a>

**Length**

The length of a vector follows from its components with the Pythagorean theorem. Computing it needs a square root, so prefer `GetLengthSquared()` for comparisons where the distance is not needed.

```python
import c4d

a: c4d.Vector = c4d.Vector(3, 2, 1)
r: float = a.GetLength()  # 3.741
s: float = a.GetLengthSquared() # 14
```

> *Interactive figure (HTML only): The 3D vector a with its length marked by a dimension line. Drag the arrowhead to change a.*

<a id="item-cross-product"></a>

**Cross Product**

The [cross product](https://en.wikipedia.org/wiki/Cross_product) is perpendicular to both vector operands, and its length is the area of the parallelogram they span. It is commonly used to construct a surface normal. In Cinema 4D’s left-handed system, the result follows the left-hand rule. Swapping the operands flips the result.

```python
import c4d

a: c4d.Vector = c4d.Vector(2, 0, 1)
b: c4d.Vector = c4d.Vector(1, 2, 0)
r: c4d.Vector = a.Cross(b)  # (-2, 1, 4)
s: c4d.Vector = a % b # alternative notation for cross product
```

> *Interactive figure (HTML only): The 3D cross product r of vectors a and b, perpendicular to their plane. Drag the arrowheads to change the operands.*

<a id="item-dot-product"></a>

**Dot Product**

The [dot product](https://en.wikipedia.org/wiki/Dot_product) measures how much two vectors point in the same direction. It is positive when they point broadly the same way, zero when they are perpendicular, and negative when they oppose each other. The result is a number, not a vector. For unit vectors it is the cosine of the angle between them; geometrically, it gives the projection of one vector onto the other.

```python
import c4d

a: c4d.Vector = c4d.Vector(3, 1, 1)
b: c4d.Vector = c4d.Vector(1, 3, 0.5)
r: float = a.Dot(b)  # 10.5
s: float = a * b  # alternative notation for dot product
```

> *Interactive figure (HTML only): The dot product of vectors a and b, with the angle between them. Drag the arrowheads to change the operands.*

<a id="item-projection-onto-a-vector"></a>

**Projection onto a Vector**

[Projecting](https://en.wikipedia.org/wiki/Vector_projection) a vector onto another asks how much of it points along the direction of the other. Picture the other vector as a line, with light shining straight onto it from the side: the shadow cast on that line is the result. What is left over, the dashed remainder, stands at a right angle to the line. It splits a movement into a part along a direction and a part across it. The vector to project onto cannot be the zero vector.

```python
import c4d

a: c4d.Vector = c4d.Vector(2, 3, 1)
b: c4d.Vector = c4d.Vector(4, 0.5, 1)
if b.GetLengthSquared() > 0.0:
    r: c4d.Vector = b * (a.Dot(b) / b.GetLengthSquared())
```

> *Interactive figure (HTML only): The 3D projection of a onto b, with its perpendicular remainder. Drag the arrowheads to change the operands.*

<a id="item-projection-onto-a-plane"></a>

**Projection onto a Plane**

Projecting onto a plane flattens a vector onto a flat surface, like the shadow an object casts on the floor from a light straight above. The plane is described by its [normal](https://en.wikipedia.org/wiki/Normal_(geometry)) `n`, the direction standing upright on it. The vector is split into a part along the normal and a part that lies within the plane. Removing the first part leaves the second, the flattened result. It is how you keep a movement on the ground or slide along a surface. The normal must have a length of one. Orbit the preview to inspect the vectors and plane in 3D.

```python
import c4d

a: c4d.Vector = c4d.Vector(2, 2.2, 1.5)
n: c4d.Vector = c4d.Vector(0, 1, 0)  # Must be a unit vector.
r: c4d.Vector = a - n * a.Dot(n)
```

> *Interactive figure (HTML only): The 3D vector a projected onto a plane with unit normal n. Drag the arrowhead to change a.*

<a id="item-rotation"></a>

**Rotation**

Rotating a vector in 2D is equivalent to moving it along the [unit circle](https://en.wikipedia.org/wiki/Unit_circle).

> **Note:** This section explains the relation between the circle functions and the rotation of a vector in 2D space. It shows you why [rotation matrices](https://en.wikipedia.org/wiki/Rotation_matrix) work and why DCC apps deal with rotations in [radians](https://en.wikipedia.org/wiki/Radian) under the hood. Doing it manually as shown here is not necessary, use [`c4d.utils.MatrixRotX()`](../modules/c4d.utils/index.md#c4d.utils.MatrixRotX), [`c4d.utils.MatrixRotY()`](../modules/c4d.utils/index.md#c4d.utils.MatrixRotY), and [`c4d.utils.MatrixRotZ()`](../modules/c4d.utils/index.md#c4d.utils.MatrixRotZ) instead.

A vector can be rotated using the [trigonometric identities](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions) adjacent over hypotenuse and opposite over hypotenuse, which correspond to the [cosine and sine](https://en.wikipedia.org/wiki/Sine_and_cosine) functions, respectively. With that we can rotate a vector on the unit circle by an angle, as the rotated vector will be described by a triangle with the original vector as the [hypotenuse](https://en.wikipedia.org/wiki/Hypotenuse).

Broadly speaking, the sine and cosine functions describe the relationship between the angle and the coordinates of a point on the unit circle; they literally trace out the coordinates of a point on the unit circle, rotated by the given angle. From this insight follows then notion of a ‘rotation matrix’, a little tool that rotates a vector by a given angle.

Below you can find in the top left corner the two trigonometric identities to compute x and y coordinates of a rotated vector. On the top left you find the corresponding rotation matrices. On the bottom left you see the unit circle with the rotated vector. Here you can drag the rotated point to see the diagram update. And on the bottom right, you can see a corresponding sine and cosine plot.

```python
import c4d
import math

angle: float = c4d.utils.DegToRad(30)  # Angles are in radians.
a: c4d.Vector = c4d.Vector(1, 0, 0)

# Rotating with the Cinema API.
M: c4d.Matrix = c4d.utils.MatrixRotZ(angle)
r: c4d.Vector = M * a  # (0.866, -0.5, 0)

# Rotating manually, same as #r.
cos: float = math.cos(angle)
sin: float = math.sin(angle)
s: c4d.Vector = c4d.Vector(a.x * cos + a.y * sin,
                           a.y * cos - a.x * sin,
                           a.z)
```

> *Interactive figure (HTML only): The unit circle and the X and Y coordinates of the rotated vector over one turn. Drag the arrowhead to change the angle.*

## See Also <a id="see-also"></a>

- [Matrices](manual_matrices.md): Explains how to carry out transform operations.
- [Example _c4d_vector.py](../examples/math/_c4d_vector.py.md): Demonstrates working with vectors.
