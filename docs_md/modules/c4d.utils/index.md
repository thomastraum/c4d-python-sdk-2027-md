<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.utils/index.html -->

# c4d.utils <a id="c4d-utils"></a>

## *class* `c4d.utils` <a id="c4d.utils"></a>

- [`c4d.utils.ConvexHullDecomposition`](ConvexHullDecomposition/index.md#c4d.utils.ConvexHullDecomposition)

- [`c4d.utils.GeRayCollider`](GeRayCollider/index.md#c4d.utils.GeRayCollider)

- [`c4d.utils.KDTree`](KDTree/index.md#c4d.utils.KDTree)

- [`c4d.utils.KDTreeQuery`](KDTreeQuery/index.md#c4d.utils.KDTreeQuery)

- [`c4d.utils.Neighbor`](Neighbor/index.md#c4d.utils.Neighbor)

- [`c4d.utils.noise`](noise/index.md#c4d.utils.noise)

  > - [`c4d.utils.noise.C4DNoise`](noise/C4DNoise/index.md#c4d.utils.noise.C4DNoise)

- [`c4d.utils.PolygonReduction`](PolygonReduction/index.md#c4d.utils.PolygonReduction)

- [`c4d.utils.SplineHelp`](SplineHelp/index.md#c4d.utils.SplineHelp)

- [`c4d.utils.SplineLengthData`](SplineLengthData/index.md#c4d.utils.SplineLengthData)

- [`c4d.utils.ViewportSelect`](ViewportSelect/index.md#c4d.utils.ViewportSelect)

## Overview <a id="overview"></a>

**Angle And Trigonometric Utilities**

- [`c4d.utils.DegToRad()`](#c4d.utils.DegToRad): Convert a degrees value into radians.
- [`c4d.utils.RadToDeg()`](#c4d.utils.RadToDeg): Convert a radians value into degrees.
- [`c4d.utils.SinCos()`](#c4d.utils.SinCos): Get sine and cosine of w:

**Color Processing**

- [`c4d.utils.CutColor()`](#c4d.utils.CutColor): Limit a color vector between 0.0 and 1.0.
- [`c4d.utils.HSLtoRGB()`](#c4d.utils.HSLtoRGB): Converts HSL into the RGB color space and returns the converted value.
- [`c4d.utils.HSVToRGB()`](#c4d.utils.HSVToRGB): Converts HSV into the RGB color space and returns the converted value.
- [`c4d.utils.RGBToHSL()`](#c4d.utils.RGBToHSL): Converts RGB into the HSL color space and returns the converted value.
- [`c4d.utils.RGBToHSV()`](#c4d.utils.RGBToHSV): Converts RGB into the HSV color space and returns the converted value.
- [`c4d.utils.TransformColor()`](#c4d.utils.TransformColor): Transforms a color from one color profile to another.

**Deprecated**

- [`c4d.utils.Deg()`](#c4d.utils.Deg): Use `RadToDeg()` instead for better understanding of code.
- [`c4d.utils.Rad()`](#c4d.utils.Rad): Use `DegToRad()` instead for better understanding of code.

**Interpolation And Blending**

- [`c4d.utils.MixNum()`](#c4d.utils.MixNum): Returns a mixed value of v1 and v2 using the parameter t, as calculated by *v1+(v2-v1)*t*.
- [`c4d.utils.MixVec()`](#c4d.utils.MixVec): Mixes the two vectors together, such as mixing two colours.
- [`c4d.utils.QBlend()`](#c4d.utils.QBlend): Linear interpolation of the quaternions *q1* and *q2* with parameter *r*.
- [`c4d.utils.QSlerp()`](#c4d.utils.QSlerp): Spherical interpolation of the quaternions *q1* and *q2* with the parameter *alfa*.
- [`c4d.utils.QSmoothCubic()`](#c4d.utils.QSmoothCubic): Smooth blends the quaternions *qn* and *qn_p1* using Cubic interpolation with parameter *t*.
- [`c4d.utils.QSpline()`](#c4d.utils.QSpline): Smooth blends the quaternions *qn* and *qn_p1* using spherical spline interpolation with parameter *t*.
- [`c4d.utils.QSquad()`](#c4d.utils.QSquad): Cubic interpolates the quaternions *q1* and *q2* with parameter *alfa* using spherical quadrangle interpolation.

**Mesh And Object Operations**

- [`c4d.utils.BooleanSplines()`](#c4d.utils.BooleanSplines): Booleans an initial spline object with an array of other spline objects along a passed projection axis (in 2D).
- [`c4d.utils.CalculateVisiblePoints()`](#c4d.utils.CalculateVisiblePoints): Checks if points in the polygon object *op* are visible in the view *bd*.
- [`c4d.utils.CheckDisplayFilter()`](#c4d.utils.CheckDisplayFilter): Checks if object *op* would be displayed with the given *filter*.
- [`c4d.utils.DisjointMesh()`](#c4d.utils.DisjointMesh): Separates the mesh of the object to make each polygon/line segment independent.
- [`c4d.utils.GenerateUVW()`](#c4d.utils.GenerateUVW): Generates a UVW tag for an object.
- [`c4d.utils.GetBBox()`](#c4d.utils.GetBBox): Calculates the bounding box of a hierarchy.
- [`c4d.utils.SendModelingCommand()`](#c4d.utils.SendModelingCommand): Executes a builtin modelling operation as for example extruding a polygon selection or selecting all points of an object.

**Numeric Conversion**

- [`c4d.utils.FormatNumber()`](#c4d.utils.FormatNumber): Converts *val* to a string.
- [`c4d.utils.StringToNumber()`](#c4d.utils.StringToNumber): Converts a string expressing a numeric value to a data value of type `float` or `int`.

**Quaternion Algebra**

- [`c4d.utils.QAdd()`](#c4d.utils.QAdd): Calculates the quaternion addition of quaternions *q1* and *q2*.
- [`c4d.utils.QDeriv()`](#c4d.utils.QDeriv): Calculates the derivative of quaternion *q* by vector *w*.
- [`c4d.utils.QDot()`](#c4d.utils.QDot): Calculates the Dot Product between *q1* and *q2*.
- [`c4d.utils.QExpQ()`](#c4d.utils.QExpQ): Calculates the exponential of quaternion *q*.
- [`c4d.utils.QInvert()`](#c4d.utils.QInvert): Calculates the inverse of quaternion *q*.
- [`c4d.utils.QLogN()`](#c4d.utils.QLogN): Calculates the natural logarithm of quaternion *q*.
- [`c4d.utils.QMul()`](#c4d.utils.QMul): Calculates the quaternion product of quaternions *q1* and *q2*.
- [`c4d.utils.QMulS()`](#c4d.utils.QMulS): Calculates the product of quaternion *q* with scalar *s*.
- [`c4d.utils.QNorm()`](#c4d.utils.QNorm): Gets a normalized copy of quaternion *q*.
- [`c4d.utils.QSub()`](#c4d.utils.QSub): Calculates the quaternion subtraction of quaternions *q1* and *q2*.

**Range And Value Shaping**

- [`c4d.utils.Bias()`](#c4d.utils.Bias): Returns the bias as the defined in the book “Texturing and Modeling” by Ebert.
- [`c4d.utils.Boxstep()`](#c4d.utils.Boxstep): Returns 0.0 if *x* is less than *a* and 1.0 if *x* is greater than *b*, else returns *x* mapped on the range *[a,b]* (*a* number between 0.0 and 1.0).
- [`c4d.utils.CalcLOD()`](#c4d.utils.CalcLOD): This is a helper function to modify a user chosen subdivision value.
- [`c4d.utils.Clamp()`](#c4d.utils.Clamp): Returns *a* if *x* is less than *a* and *b* if *x* is greater than *b*, else returns *x*.
- [`c4d.utils.ClampValue()`](#c4d.utils.ClampValue): Returns *a* if *x* is less than *a* and *b* if *x* is greater than *b*, else returns *x*.
- [`c4d.utils.FCut()`](#c4d.utils.FCut): Limit the value of *a* to between *b* and *c*.
- [`c4d.utils.RangeMap()`](#c4d.utils.RangeMap): Map the value of a range to another, optionnaly applying a spline curve.
- [`c4d.utils.Smoothstep()`](#c4d.utils.Smoothstep): Returns *0.0* if *x* is less than *a* and *1.0* if *x* is greater than *b*, else returns *x* mapped on the range [a,b] (a number between 0.0 and 1.0). The mapping is smoothed using an ease-in/ease-out curve.
- [`c4d.utils.Step()`](#c4d.utils.Step): Returns 1.0 if *b* is greater than or equal to *a*, else 0.0.
- [`c4d.utils.Truncate()`](#c4d.utils.Truncate): Limit a color vector between 0.0 and 1.0.

**Rotation Conversions**

- [`c4d.utils.GetOptimalAngle()`](#c4d.utils.GetOptimalAngle): Modify *hpb_new* so that the “distance” to the last angle *hpb_old* is at minimum.
- [`c4d.utils.HPBToMatrix()`](#c4d.utils.HPBToMatrix): Construct matrix from the euler angles *hpb*.
- [`c4d.utils.MatrixRotX()`](#c4d.utils.MatrixRotX): Creates a rotation matrix about the X axis.
- [`c4d.utils.MatrixRotY()`](#c4d.utils.MatrixRotY): Creates a rotation matrix about the Y axis.
- [`c4d.utils.MatrixRotZ()`](#c4d.utils.MatrixRotZ): Creates a rotation matrix about the Z axis.
- [`c4d.utils.MatrixToHPB()`](#c4d.utils.MatrixToHPB): Calculate euler angles from the matrix *m*.
- [`c4d.utils.MatrixToRotAxis()`](#c4d.utils.MatrixToRotAxis): Calculates rotation axis and angle from matrix *m*:
- [`c4d.utils.RotAxisToMatrix()`](#c4d.utils.RotAxisToMatrix): Calculate matrix from rotation axis *v* and angle *w*.
- [`c4d.utils.VectorToHPB()`](#c4d.utils.VectorToHPB): Calculate euler angles from the vector *p*. The bank is always set to 0.0.

**Spatial Geometry**

- [`c4d.utils.CircleLineIntersection()`](#c4d.utils.CircleLineIntersection): Calculates the intersection points between a line and a circle in 2D space (although *Z* will also be calculated on the resulting hit points).
- [`c4d.utils.PointLineDistance()`](#c4d.utils.PointLineDistance): Calculates the distance from a point to a line.
- [`c4d.utils.PointLineSegmentDistance()`](#c4d.utils.PointLineSegmentDistance): Calculates the distance from a point to a line segment between two points.
- [`c4d.utils.PointLineSegmentDistance2D()`](#c4d.utils.PointLineSegmentDistance2D): Calculates the distance from a point to a line segment between two points in 2D ignoring the Z value.
- [`c4d.utils.ReflectRay()`](#c4d.utils.ReflectRay): Find the ray vector after a reflection about a surface normal.
- [`c4d.utils.SphereLineIntersection()`](#c4d.utils.SphereLineIntersection): Calculates the intersection points between a line and a sphere in 3D space.

**Spline Operations**

- [`c4d.utils.CalcSpline()`](#c4d.utils.CalcSpline): Calculates the value of a spline at a point.
- [`c4d.utils.CalcSplineDefaultTangents()`](#c4d.utils.CalcSplineDefaultTangents): Calculates the default tangents for the passed points (spline segment) based on the spline type.
- [`c4d.utils.CalcSplineInsert()`](#c4d.utils.CalcSplineInsert): Calculates data about a point would if it were inserted into the spline at the passed offset.
- [`c4d.utils.CalcSplineMovement()`](#c4d.utils.CalcSplineMovement): Moves a point on a spline curve to a user specified new position.
- [`c4d.utils.CalcSplinePoint()`](#c4d.utils.CalcSplinePoint): Calculates a point along a spline curve from a set of points in 3D space.
- [`c4d.utils.CalcSplineTangent()`](#c4d.utils.CalcSplineTangent): Calculates the tangent of a point along a spline curve from a given set of points and optional tangents.
- [`c4d.utils.CalcSplineV()`](#c4d.utils.CalcSplineV): Calculates the value of a spline at a point.
- [`c4d.utils.FitCurve()`](#c4d.utils.FitCurve): Creates a spline object that has the best fit through the given points.
- [`c4d.utils.TransformTangent()`](#c4d.utils.TransformTangent): Creates a transformed tangent around a point and plane, allowing to directly set the position of one of the tangent handles and automatically rotating the rest of the tangent to match.

**Texture Baking**

- [`c4d.utils.BakeTexture()`](#c4d.utils.BakeTexture): Bakes the texture(s) specified by the last `InitBakeTexture()` call into *bmp*.
- [`c4d.utils.InitBakeTexture()`](#c4d.utils.InitBakeTexture): Initializes a bake operation of a single tag for `BakeTexture()`.

**Tolerance Checks**

- [`c4d.utils.CompareFloatTolerant()`](#c4d.utils.CompareFloatTolerant): Compares if two floats are close to each other on a bit basis (rather than a fixed epsilon).
- [`c4d.utils.VectorEqual()`](#c4d.utils.VectorEqual): Check if vector v1 and v2 are within *epsilon* of each other.

**Transform Matrices**

- [`c4d.utils.CalculateTranslationScale()`](#c4d.utils.CalculateTranslationScale): Calculates the scale between *src* and *dst*.
- [`c4d.utils.MatrixMove()`](#c4d.utils.MatrixMove): Create a translation matrix.
- [`c4d.utils.MatrixScale()`](#c4d.utils.MatrixScale): Create a scaling matrix.

**Vector Analysis**

- [`c4d.utils.GetAngle()`](#c4d.utils.GetAngle): Calculates the angle of two vectors.
- [`c4d.utils.VectorAngle()`](#c4d.utils.VectorAngle): Calculates the angle between two vectors in radians.
- [`c4d.utils.VectorGray()`](#c4d.utils.VectorGray): Sum the vector components and multiply by 1/3.
- [`c4d.utils.VectorMax()`](#c4d.utils.VectorMax): Find the maximum component of the vector.
- [`c4d.utils.VectorMin()`](#c4d.utils.VectorMin): Find the minimum component of the vector.
- [`c4d.utils.VectorSum()`](#c4d.utils.VectorSum): Sum the vector components.

## Members <a id="members"></a>

### Angle And Trigonometric Utilities <a id="c4d.utils-function-Angle-And-Trigonometric-Utilities"></a>

#### `c4d.utils.DegToRad(d)` <a id="c4d.utils.DegToRad"></a>

Convert a degrees value into radians.

*New in version R18.039.*

**Parameters:** **r** (*number*) – Input value in degrees.

**Return type:** number

**Returns:** Converted value in radians.

#### `c4d.utils.RadToDeg(r)` <a id="c4d.utils.RadToDeg"></a>

Convert a radians value into degrees.

*New in version R18.039.*

**Parameters:** **r** (*number*) – Input value in radians.

**Return type:** number

**Returns:** Converted value in degrees.

#### `c4d.utils.SinCos(w)` <a id="c4d.utils.SinCos"></a>

Get sine and cosine of w:

```python
import c4d

sn, cs = c4d.utils.SinCos(80)
```

**Parameters:** **w** (*float*) – Value.

**Return type:** list

**Returns:** Sine and Cosine.

### Color Processing <a id="c4d.utils-function-Color-Processing"></a>

#### `c4d.utils.CutColor(vec)` <a id="c4d.utils.CutColor"></a>

Limit a color vector between 0.0 and 1.0.

**Parameters:** **vec** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – Bias value.

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** The limited color vector.

#### `c4d.utils.HSLtoRGB(col)` <a id="c4d.utils.HSLtoRGB"></a>

Converts HSL into the RGB color space and returns the converted value.

*New in version R14.014.*

**Parameters:** **col** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – HSL color.

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** RGB color.

#### `c4d.utils.HSVToRGB(col)` <a id="c4d.utils.HSVToRGB"></a>

Converts HSV into the RGB color space and returns the converted value.

**Parameters:** **col** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – HSV color.

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** RGB color.

#### `c4d.utils.RGBToHSL(col)` <a id="c4d.utils.RGBToHSL"></a>

Converts RGB into the HSL color space and returns the converted value.

*New in version R14.014.*

**Parameters:** **col** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – RGB color.

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:**

HSL color.

> **Note:** If you want the Hue value to be in degree, you have to multiply it yourself.

#### `c4d.utils.RGBToHSV(col)` <a id="c4d.utils.RGBToHSV"></a>

Converts RGB into the HSV color space and returns the converted value.

**Parameters:** **col** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – RGB color.

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** HSV color.

#### `c4d.utils.TransformColor(input, colortransformation)` <a id="c4d.utils.TransformColor"></a>

Transforms a color from one color profile to another.

**Parameters:**

- **input** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The color to transform.

- **colortransformation** (*int*) –

  Transformation mode:

  | Symbol ID | Description |
  |---|---|
  | NONE | None. |
  | COLORSPACETRANSFORMATION_LINEAR_TO_SRGB | Linear to sRGB color space transformation. |
  | COLORSPACETRANSFORMATION_SRGB_TO_LINEAR | sRGB to linear color space transformation. |
  | COLORSPACETRANSFORMATION_LINEAR_TO_VIEW | Linear to display color space transformation. |
  | COLORSPACETRANSFORMATION_SRGB_TO_VIEW | sRGB to display color space transformation. |

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** The transformed color.

### Deprecated <a id="c4d.utils-function-Deprecated"></a>

#### `c4d.utils.Deg(r)` <a id="c4d.utils.Deg"></a>

*Deprecated since version R18.039:* Use [`RadToDeg()`](#c4d.utils.RadToDeg) instead for better understanding of code.

Convert a radians value into degrees.

**Parameters:** **r** (*number*) – Input value in radians.

**Return type:** number

**Returns:** Converted value in degrees.

#### `c4d.utils.Rad(d)` <a id="c4d.utils.Rad"></a>

*Deprecated since version R18.039:* Use [`DegToRad()`](#c4d.utils.DegToRad) instead for better understanding of code.

Convert a degrees value into radians.

**Parameters:** **r** (*number*) – Input value in degrees.

**Return type:** number

**Returns:** Converted value in radians.

### Interpolation And Blending <a id="c4d.utils-function-Interpolation-And-Blending"></a>

#### `c4d.utils.MixNum(v1, v2, t)` <a id="c4d.utils.MixNum"></a>

Returns a mixed value of v1 and v2 using the parameter t, as calculated by *v1+(v2-v1)*t*.

**Parameters:**

- **v1** (*float*) – Value to mix.
- **v2** (*float*) – Value to mix.
- **t** (*number*) – Mix amount: *0* < *t* < *1.0*.

**Return type:** float

**Returns:** Mix amount, with *0 <= t <= 1.0*.

#### `c4d.utils.MixVec(v1, v2, t)` <a id="c4d.utils.MixVec"></a>

Mixes the two vectors together, such as mixing two colours.

**Parameters:**

- **v1** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – Vector to mix.
- **v2** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – Vector to mix.
- **t** (*number*) – Mix amount: *0* < *t* < *1.0*.

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** The mixed vector.

#### `c4d.utils.QBlend(q1, q2, r)` <a id="c4d.utils.QBlend"></a>

Linear interpolation of the quaternions *q1* and *q2* with parameter *r*.

*New in version R17.048.*

**Parameters:**

- **q1** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The first quaternion.
- **q2** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The second quaternion.
- **alfa** (*float*) – The blending parameter. Between *0.0* (*q1*) and *1.0* (*q2*).

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** The interpolated quaternion.

#### `c4d.utils.QSlerp(q1, q2, alfa)` <a id="c4d.utils.QSlerp"></a>

Spherical interpolation of the quaternions *q1* and *q2* with the parameter *alfa*.

*New in version R17.048.*

**Parameters:**

- **q1** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The first quaternion.
- **q2** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The second quaternion.
- **alfa** (*float*) – The interpolation parameter. Between *0.0* (*q1*) and *1.0* (*q2*).

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** The interpolated quaternion.

#### `c4d.utils.QSmoothCubic(qn_m1, qn, qn_p1, t)` <a id="c4d.utils.QSmoothCubic"></a>

Smooth blends the quaternions *qn* and *qn_p1* using Cubic interpolation with parameter *t*.  
*qn_m1* (-1) and *qn_p2* (-1+2) are used to provide C1-continuity at the borders (tangents).

*New in version R18.020.*

**Parameters:**

- **qn_m1** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The first quaternion (-1) to provide continuity.
- **qn** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The first quaternion to interpolate from.
- **qn_p1** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The second quaternion to interpolate from.
- **t** (*float*) – The blending parameter. Between *0.0* (*qn*) and *1.0* (*qn_p1*).

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** The interpolated quaternion.

#### `c4d.utils.QSpline(qn_m1, qn, qn_p1, qn_p2, t)` <a id="c4d.utils.QSpline"></a>

Smooth blends the quaternions *qn* and *qn_p1* using spherical spline interpolation with parameter *t*.  
*qn_m1* (-1) and *qn_p2* (-1+2) are used to provide C1-continuity at the borders (tangents).

*New in version R17.048.*

**Parameters:**

- **qn_m1** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The first quaternion (-1) to provide continuity.
- **qn** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The first quaternion to interpolate from.
- **qn_p1** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The second quaternion to interpolate from.
- **qn_p2** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The second quaternion (+2) to provide continuity.
- **t** (*float*) – The blending parameter. Between *0.0* (*qn*) and *1.0* (*qn_p1*).

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** The interpolated quaternion.

#### `c4d.utils.QSquad(q0, q1, q2, q3, alfa)` <a id="c4d.utils.QSquad"></a>

Cubic interpolates the quaternions *q1* and *q2* with parameter *alfa* using spherical quadrangle interpolation.  
*q0* and *q3* are used to provide C1-continuity at the borders (tangents): *q0* = i-1, *q1* = i, *q2* = i+1, *q3* = i+2

*New in version R17.048.*

**Parameters:**

- **q0** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The first quaternion to provide continuity.
- **q1** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The first quaternion to interpolate from.
- **q2** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The second quaternion to interpolate from.
- **q3** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The second quaternion to provide continuity.
- **alfa** (*float*) – The interpolation parameter. Between *0.0* (*q1*) and *1.0* (*q2*).

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** The interpolated quaternion.

### Mesh And Object Operations <a id="c4d.utils-function-Mesh-And-Object-Operations"></a>

#### `c4d.utils.BooleanSplines(initialSpline, booleanObjects, doc, bd, projectionAxis, booleanMode)` <a id="c4d.utils.BooleanSplines"></a>

Booleans an initial spline object with an array of other spline objects along a passed projection axis (in 2D).

*New in version R17.048.*

**Parameters:**

- **initialSpline** ([*c4d.BaseObject*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The original spline object that will have the operations applied to it.

- **booleanObjects** (*List*[[*c4d.SplineObject*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/SplineObject/index.md#c4d.SplineObject)]) – The array of spline objects to boolean with *initialSpline*.

- **doc** ([*c4d.documents.BaseDocument*](../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document that the objects belong to.

- **bd** ([*c4d.BaseDraw*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The active basebraw.

- **projectionAxis** (*int*) –

  The projection axis to use:

  |   |   |
  |---|---|
  | *SPLINEBOOL_AXIS_NONE* | No axis. |
  | *SPLINEBOOL_AXIS_SCREEN* | Project into the current screen. |
  | *SPLINEBOOL_AXIS_ZY* | Project on the ZY (X axis) plane. |
  | *SPLINEBOOL_AXIS_XZ* | Project on the XZ (Y axis) plane. |
  | *SPLINEBOOL_AXIS_XY* | Project on the XY (Z axis) plane. |

- **booleanMode** (*int*) –

  The type of boolean to apply:

  |   |   |
  |---|---|
  | *SPLINEBOOL_MODE_AMINUSB* | Subtract B from A. |
  | *SPLINEBOOL_MODE_BMINUSA* | Subtract A from B. |
  | *SPLINEBOOL_MODE_UNION* | Union of both A and B. |
  | *SPLINEBOOL_MODE_AND* | And intersection (overlap) of region of A and B. |
  | *SPLINEBOOL_MODE_OR* | Or intersection (outside of overlap) of region of A and B. |
  | *SPLINEBOOL_MODE_INTERSECTION* | Intersection (all segments inside and out) of region of A and B. |

**Return type:** Optional[[c4d.BaseList2D](../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The spline object result of the Boolean operation, **None** if there was an error.

#### `c4d.utils.CalculateVisiblePoints(bd, op, visible=False)` <a id="c4d.utils.CalculateVisiblePoints"></a>

Checks if points in the polygon object *op* are visible in the view *bd*.

**Parameters:**

- **bd** ([*c4d.BaseDraw*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The base draw to check.

- **op** ([*c4d.PolygonObject*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject)) – The object to check.

- **visible** (*Optional*[*bool*]) –

  *New in version R19.068:* **True** to include only visible points, otherwise **False** (default) to also include hidden points like for example those from the back of an object.

**Return type:** Optional[List[int]]

**Returns:**

A list of integers with the visibility status for each point: *1* if the point is visible otherwise *0*.  
**None** if the function fails.

#### `c4d.utils.CheckDisplayFilter(op, filter)` <a id="c4d.utils.CheckDisplayFilter"></a>

Checks if object *op* would be displayed with the given *filter*.

Example:

```python
import c4d

activeView = doc.GetActiveBaseDraw()
displayFilter = activeView.GetDisplayFilter()
if c4d.utils.CheckDisplayFilter(op, displayFilter):
    print "Object Displayed!"
else:
    print "Object Not Displayed!"
```

**Parameters:**

- **op** ([*c4d.BaseObject*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object to check.

- **filter** (*int*) –

  The filter bitmask:

  | DISPLAYFILTER_NONE | None. |
  |---|---|
  | DISPLAYFILTER_NULLOBJECT | Null. |
  | DISPLAYFILTER_POLYGON | Polygon. |
  | DISPLAYFILTER_SPLINE | Spline. |
  | DISPLAYFILTER_GENERATOR | Generator. |
  | DISPLAYFILTER_HYPERNURBS | Subdivision Surface. |
  | DISPLAYFILTER_UNUSED1 | Unused. |
  | DISPLAYFILTER_DEFORMER | Deformer. |
  | DISPLAYFILTER_CAMERA | Camera. |
  | DISPLAYFILTER_LIGHT | Light. |
  | DISPLAYFILTER_SCENE | Scene. |
  | DISPLAYFILTER_PARTICLE | Particle. |
  | DISPLAYFILTER_OTHER | Other. |
  | DISPLAYFILTER_UNUSED2 | *New in version S22:* Unused. |
  | DISPLAYFILTER_GRID | Grid. |
  | DISPLAYFILTER_HORIZON | Horizon. |
  | DISPLAYFILTER_WORLDAXIS | World axis. |
  | DISPLAYFILTER_BOUNDS | Bounding-box. |
  | DISPLAYFILTER_HUD | HUD. |
  | DISPLAYFILTER_SDS | HN mesh. |
  | DISPLAYFILTER_HIGHLIGHTING | Highlighting. |
  | DISPLAYFILTER_MULTIAXIS | Multi-select axis. |
  | DISPLAYFILTER_OBJECTHANDLES | Highlight handles. |
  | DISPLAYFILTER_HANDLEBANDS | Axis bands. |
  | DISPLAYFILTER_SDSCAGE | HN cage. |
  | DISPLAYFILTER_NGONLINES | N-gon lines. |
  | DISPLAYFILTER_JOINT | Joint objects. |
  | DISPLAYFILTER_OBJECTHIGHLIGHTING | Private. |
  | DISPLAYFILTER_GUIDELINES | Axis Guidelines. |
  | DISPLAYFILTER_POI | Navigation cross. |
  | DISPLAYFILTER_GRADIENT | Gradient. |
  | DISPLAYFILTER_BASEGRID | Base grid. |
  | DISPLAYFILTER_HANDLES | Handles. |
  | DISPLAYFILTER_HAIR | *New in version S22:* Hair. |
  | DISPLAYFILTER_FIELD | *New in version S22:* Field. |

**Return type:** bool

**Returns:** **True** if the object would be displayed, otherwise **False**.

#### `c4d.utils.DisjointMesh(op)` <a id="c4d.utils.DisjointMesh"></a>

Separates the mesh of the object to make each polygon/line segment independent.  
Each polygon/line will be given its own points thereby separating them so they can be moved independently, such as the Explosion object.

**Parameters:** **op** ([*c4d.PointObject*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/index.md#c4d.PointObject)) – The point object to disjoint.

**Return type:** bool

**Param:** **True** if the mesh was disjointed successfully, otherwise **False**.

#### `c4d.utils.GenerateUVW(op, opmg, tp, texopmg, view=None)` <a id="c4d.utils.GenerateUVW"></a>

Generates a UVW tag for an object.

**Parameters:**

- **op** ([*c4d.BaseObject*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object to generate the UVW coordinates for.
- **opmg** ([*c4d.Matrix*](../c4d/Matrix/index.md#c4d.Matrix)) – The object’s global matrix.
- **tp** ([*c4d.TextureTag*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/TextureTag/index.md#c4d.TextureTag)) – The texture tag to generate the UVW coordinates from.
- **texopmg** ([*c4d.Matrix*](../c4d/Matrix/index.md#c4d.Matrix)) – The global matrix of the object that carries the texture tag.
- **view** (*Optional*[[*c4d.BaseView*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/index.md#c4d.BaseView)]) – The optional current view.

**Return type:** Optional[[c4d.UVWTag](../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/UVWTag/index.md#c4d.UVWTag)]

**Returns:**

The created UVW tag, or **None** if the texture type is already UV or if the function failed.  
If **None** is returned the UVW tag must be retrieved from the object itself.

#### `c4d.utils.GetBBox(pObj, mg)` <a id="c4d.utils.GetBBox"></a>

Calculates the bounding box of a hierarchy.

**Parameters:**

- **pObj** ([*c4d.BaseObject*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The root object of a hierarchy.
- **mg** ([*c4d.Matrix*](../c4d/Matrix/index.md#c4d.Matrix)) – The transformation matrix for the bounding box.

**Return type:** Tuple[[c4d.Vector](../c4d/Vector/index.md#c4d.Vector), [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The center and the radius of the bounding box.

#### `c4d.utils.SendModelingCommand(command, list, mode=0, bc=None, doc=None, flags=0)` <a id="c4d.utils.SendModelingCommand"></a>

Executes a builtin modelling operation as for example extruding a polygon selection or selecting all points of an object.  
It is recommened to always pass the document *doc`for modelling operations. When `doc* is being passed, all *BaseObject* contained in *list* must be part of that passed document. The commands *MCOMMAND_JOIN*, *MCOMMAND_MAKEEDITABLE*, *MCOMMAND_CURRENTSTATETOOBJECT*, and *MCOMMAND_SPLINE_PROJECT* always require *doc* to be passed.

> **Note:** It is not allowed to allocate or deallocate scene elements outside from the main thread for loaded documents, e.g., the active document. This applies by extension also to *SendModelingCommand* and in cases where a modelling command must be executed outside from the main thread, this must always be done in a dummy document.

**Parameters:**

- **command** (*int*) – The identifier of the command to execute. See [MCOMMAND](../../consts/MCOMMAND.md).

- **list** (*List*[[*c4d.BaseObject*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – The collection of objects to which the command should be applied.

- **bc** (*Optional*[[*c4d.BaseContainer*](../c4d/BaseContainer/index.md#c4d.BaseContainer)]) – The setttings container for the command which is executed.

- **mode** (*int*) –

  The editing mode in which the command should be executed.

  |   |   |
  |---|---|
  | *MODELINGCOMMANDMODE_ALL* | All points/polygons. |
  | *MODELINGCOMMANDMODE_POINTSELECTION* | Only the current point selection. |
  | *MODELINGCOMMANDMODE_POLYGONSELECTION* | Only the current polygon selection. |
  | *MODELINGCOMMANDMODE_EDGESELECTION* | Only the current edge selection. |

- **doc** (*Optional*[[*c4d.documents.BaseDocument*](../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]) – The document all *BaseObject* instances hold by *list* are a member of.

- **flags** (*int*) –

  The flags for the command.

  |   |   |
  |---|---|
  | *MODELINGCOMMANDFLAGS_NONE* | None. |
  | *MODELINGCOMMANDFLAGS_CREATEUNDO* | Creates undo and inserts newly created objects into the passed document, instead of returning result. |

**Returns:** The result of the command. Some commands return a copy their inputs as their result, in his case a list of *BaseObject* is being returned. Otherwise, a boolean is returned to indicate the success of the operation. In this case, the objects inside *list* have been modified in place.

**Return type:** Union[bool, List[[c4d.BaseObject](../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]]

**Example:**

```python
import c4d
from c4d import utils

# Example for in-place modifying an object inside a loaded document.
# --------------------------------------------------------------------------------------------------

# Get the active document and the first object in it.
doc: c4d.documents.BaseDocument = c4d.documents.GetActiveDocument()
op: c4d.BaseObject = doc.GetFirstObject()

# Since the inputs will result in the active document being modified and chamfering a spline
# only works for spline objects, we must restrict the command to being on the main thread and
# #op being a spline object.

if c4d.threading.GeIsMainThreadAndNoDrawThread() and op.GetType() == c4d.Ospline:

    # Define the settings container for the tool.
    settings: c4d.BaseContainer = c4d.BaseContainer()
    settings.SetFloat(c4d.MDATA_SPLINE_OUTLINE, 25.0)

    # Run the command and print the result.
    res: bool = utils.SendModelingCommand(
        command=c4d.MCOMMAND_SPLINE_CREATEOUTLINE,
        list=[op],
        mode=c4d.MODELINGCOMMANDMODE_POINTSELECTION,
        bc=settings,
        doc=doc)

    print (f"MCOMMAND_SPLINE_CREATEOUTLINE succeeded: {res}")
    
# Example for modifying an object in a dummy document from a threaded context.
# --------------------------------------------------------------------------------------------------

class MyPlugin (c4d.plugins.ObjectData):
    """Realizes an object plugin which computes the current state of its first child object.
    """
    def GetVirtualObjects(self, op: c4d.BaseObject, hh: object) -> c4d.BaseObject | None:
        """Called by Cinema 4D to build the cache of #op. 

        This method will not run on the main thread and is therefore subject to threading resections.
        """
        # Get the first child of the node. Even when we would be okay with modifying this object
        # it is not allowed to do this in this context, because GVO is being called from outside of
        # the main thread, and firstChild is part of a loaded document.
        firstChild: c4d.BaseObject = op.GetDown()
        if not firstChild:
            return c4d.BaseObject(c4d.Onull)

        # Clone firstChild and insert it into a temporary document. When these fail, we ran out of
        # memory and must halt the plugin execution by returning `None`.
        clone: c4d.BaseObject = firstChild.GetClone(c4d.COPYFLAGS_NO_HIERARCHY, None)
        if not clone:
            return None
        
        temp: c4d.documents.BaseDocument = c4d.documents.BaseDocument()
        if not temp:
            return None

        temp.InsertObject(clone)
        
        # Run the command on clone and the temporary document, CTSO is one of the cases where the 
        # result is a copy.
        res: list[c4d.BaseObject] = utils.SendModelingCommand(
            command=c4d.MCOMMAND_CURRENTSTATETOOBJECT,
            list=[clone],
            mode=c4d.MODELINGCOMMANDMODE_POINTSELECTION,
            bc=c4d.BaseContainer(),
            doc=temp)

        # When the command fails, we probably do not want return None, i.e., halt the plugin 
        # execution, as that could change through a different user input, i.e., firstChild changing.
        if not res:
            return c4d.BaseObject(c4d.Onull)
        
        # Get the result of the command and proceed to use it in this method.
        currentState: c4d.BaseObject = res[0]
        ...
```

### Numeric Conversion <a id="c4d.utils-function-Numeric-Conversion"></a>

#### `c4d.utils.FormatNumber(val, format, fps, bUnit=True)` <a id="c4d.utils.FormatNumber"></a>

Converts *val* to a string.

**Parameters:**

- **val** (*any*) – The value to convert to a string. Must be of type float, int or [`c4d.BaseTime`](../c4d/BaseTime/index.md#c4d.BaseTime).

- **format** (*int*) –

  The format:

  |   |   |
  |---|---|
  | *FORMAT_FLOAT* | Floating point without unit. |
  | *FORMAT_INT* | Integer without unit. |
  | *FORMAT_PERCENT* | Floating point with % sign, *1.0* = *100%*. |
  | *FORMAT_DEGREE* | Floating point with ° sign. Measured in radians, displayed in degrees. |
  | *FORMAT_METER* | Floating point in the current working unit. |
  | *FORMAT_FRAMES* | Time formatted as frames. (Overrided by user preference.) |
  | *FORMAT_SECONDS* | Time formatted as seconds. (Overrided by user preference.) |
  | *FORMAT_SMPTE* | Time formatted as SMPTE. (Overrided by user preference.) |

- **fps** (*int*) – The frames per second, for time values.

- **bUnit** (*bool*) – If **True** the unit is included in the formatted string.

**Return type:** str

**Returns:** The formatted string.

#### `c4d.utils.StringToNumber(text, format, fps, lengthunit)` <a id="c4d.utils.StringToNumber"></a>

Converts a string expressing a numeric value to a data value of type `float` or `int`.

**Parameters:**

- **text** (*str*) – The string to convert to a value.

- **format** (*int*) –

  The format:

  |   |   |
  |---|---|
  | *FORMAT_FLOAT* | Floating point without unit. |
  | *FORMAT_INT* | Integer without unit. |
  | *FORMAT_PERCENT* | Floating point with % sign, *1.0* = *100%*. |
  | *FORMAT_DEGREE* | Floating point with ° sign. Measured in radians, displayed in degrees. |
  | *FORMAT_METER* | Floating point in the current working unit. |
  | *FORMAT_FRAMES* | Time formatted as frames. (Overrided by user preference.) |
  | *FORMAT_SECONDS* | Time formatted as seconds. (Overrided by user preference.) |
  | *FORMAT_SMPTE* | Time formatted as SMPTE. (Overrided by user preference.) |

- **fps** (*int*) – The frames per second, for time values.

- **lengthunit** (*int*) –

  *New in version R18.057.*

  Can be used to override the units conversion. By default the function uses the document’s units.  
  For example a string of “50” results in *0.5* if the document’s units are Meters and the unit display setting is centimeters.  
  If *lengthunit* is specified its value will be used instead of the document’s units setting.

**Return type:** Union[int, float]

**Returns:** The converted value.

### Quaternion Algebra <a id="c4d.utils-function-Quaternion-Algebra"></a>

#### `c4d.utils.QAdd(q1, q2)` <a id="c4d.utils.QAdd"></a>

Calculates the quaternion addition of quaternions *q1* and *q2*.

*New in version R17.048.*

**Parameters:**

- **q1** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The first quaternion.
- **q2** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The second quaternion.

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** The quaternion addition of *q1* and *q2*.

#### `c4d.utils.QDeriv(q, w)` <a id="c4d.utils.QDeriv"></a>

Calculates the derivative of quaternion *q* by vector *w*.

*New in version R17.048.*

**Parameters:**

- **q** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The quaternion.
- **w** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The vector.

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** The quaternion derivative of *q* by *w*.

#### `c4d.utils.QDot(q1, q2)` <a id="c4d.utils.QDot"></a>

Calculates the Dot Product between *q1* and *q2*.

*New in version R18.020.*

**Parameters:**

- **q1** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The first quaternion.
- **q2** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The second quaternion.

**Return type:** float

**Returns:** The Dot Product of *q1* and *q2*.

#### `c4d.utils.QExpQ(q)` <a id="c4d.utils.QExpQ"></a>

Calculates the exponential of quaternion *q*.

*New in version R17.048.*

**Parameters:** **q** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The quaternion.

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** The exponential of *q*.

#### `c4d.utils.QInvert(q)` <a id="c4d.utils.QInvert"></a>

Calculates the inverse of quaternion *q*.

*New in version R17.048.*

**Parameters:** **q** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The quaternion to invert.

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** The quaternion inverse of q.

#### `c4d.utils.QLogN(q)` <a id="c4d.utils.QLogN"></a>

Calculates the natural logarithm of quaternion *q*.

*New in version R17.048.*

**Parameters:** **q** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The quaternion.

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** The natural logarithm of *q*.

#### `c4d.utils.QMul(q1, q2)` <a id="c4d.utils.QMul"></a>

Calculates the quaternion product of quaternions *q1* and *q2*.

*New in version R17.048.*

**Parameters:**

- **q1** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The first quaternion.
- **q2** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The second quaternion.

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** The quaternion product of *q1* and *q2*.

#### `c4d.utils.QMulS(q, s)` <a id="c4d.utils.QMulS"></a>

Calculates the product of quaternion *q* with scalar *s*.

*New in version R17.048.*

**Parameters:**

- **q** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The quaternion.
- **s** (*float*) – The scalar.

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** The product of *q* with *s*.

#### `c4d.utils.QNorm(q)` <a id="c4d.utils.QNorm"></a>

Gets a normalized copy of quaternion *q*.

*New in version R17.048.*

**Parameters:** **q** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The quaternion to normalize.

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** A normalized copy of *q*.

#### `c4d.utils.QSub(q1, q2)` <a id="c4d.utils.QSub"></a>

Calculates the quaternion subtraction of quaternions *q1* and *q2*.

*New in version R17.048.*

**Parameters:**

- **q1** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The first quaternion.
- **q2** ([*c4d.Quaternion*](../c4d/Quaternion/index.md#c4d.Quaternion)) – The second quaternion.

**Return type:** [c4d.Quaternion](../c4d/Quaternion/index.md#c4d.Quaternion)

**Returns:** The quaternion subtraction of *q1* and *q2*.

### Range And Value Shaping <a id="c4d.utils-function-Range-And-Value-Shaping"></a>

#### `c4d.utils.Bias(b, x)` <a id="c4d.utils.Bias"></a>

Returns the bias as the defined in the book “Texturing and Modeling” by Ebert.

The internal code:

```python
import math

def Bias(b, x):
    return math.pow(x, -math.log(b) / 0.693147180559945)
```

**Parameters:**

- **b** (*number*) – Bias value.
- **x** (*number*) – The real value.

**Return type:** float

**Returns:** The bias.

#### `c4d.utils.Boxstep(a, b, x)` <a id="c4d.utils.Boxstep"></a>

Returns 0.0 if *x* is less than *a* and 1.0 if *x* is greater than *b*, else returns *x* mapped on the range *[a,b]* (*a* number between 0.0 and 1.0).

**Parameters:**

- **a** (*number*) – The float value.
- **b** (*number*) – The float value.
- **x** (*number*) – The float value.

**Return type:** float

**Returns:** The stepped value.

#### `c4d.utils.CalcLOD(val, lod, min, max)` <a id="c4d.utils.CalcLOD"></a>

This is a helper function to modify a user chosen subdivision value.

For example:

```python
sub = c4d.utils.CalcLOD(op[TUBEOBJECT_SUB, 1], hh["lod"], 1, 1000)
```

**Parameters:**

- **val** (*int*) – The user chosen lod value.
- **lod** (*float*) – The LOD value.
- **min** (*int*) – The minimum lod.
- **max** (*int*) – The maximum lod.

#### `c4d.utils.Clamp(a, b, x)` <a id="c4d.utils.Clamp"></a>

Returns *a* if *x* is less than *a* and *b* if *x* is greater than *b*, else returns *x*.

> **Note:** The order of parameters are different to Peachey’s definition.

**Parameters:**

- **a** (*number*) – The float value.
- **b** (*number*) – The float value.
- **x** (*number*) – The float value.

**Return type:** float

**Returns:** The clamped value.

#### `c4d.utils.ClampValue(x, a, b)` <a id="c4d.utils.ClampValue"></a>

Returns *a* if *x* is less than *a* and *b* if *x* is greater than *b*, else returns *x*.

*New in version R15.037.*

> **Note:** The order of parameters are the same to Peachey’s definition.

**Parameters:**

- **x** (*number*) – The float value.
- **a** (*number*) – The float value.
- **b** (*number*) – The float value.

**Return type:** float

**Returns:** The clamped value.

#### `c4d.utils.FCut(a, b, c)` <a id="c4d.utils.FCut"></a>

Limit the value of *a* to between *b* and *c*.

**Parameters:**

- **a** (*float*) – Value
- **b** (*float*) – Lower bound
- **c** (*float*) – Upper bound

#### `c4d.utils.RangeMap(value, mininput, maxinput, minoutput, maxoutput, clampval, curve)` <a id="c4d.utils.RangeMap"></a>

Map the value of a range to another, optionnaly applying a spline curve. Similiar to the RangeMapper Node in XPresso.

Here are several examples:

```python
import c4d

c4d.utils.RangeMap(value=0.5, mininput=0, maxinput=1, minoutput=5, maxoutput=10, clampval=False)
# Output: 7.5

c4d.utils.RangeMap(value=1.5, mininput=0, maxinput=1, minoutput=5, maxoutput=10, clampval=False)
# Output: 12.5

c4d.utils.RangeMap(value=1.5, mininput=0, maxinput=1, minoutput=5, maxoutput=10, clampval=True)
# Output: 10.0
```

**Parameters:**

- **value** (*float*) – The value to map.
- **mininput** (*float*) – The minimum input.
- **maxinput** (*float*) – The maximum input.
- **minoutput** (*float*) – The minimum output.
- **maxoutput** (*float*) – The maximum output.
- **clampval** (*bool*) – Pass **True** to clamp the value in the range [*minoutput*, *maxoutput*].
- **curve** (*Optional*[[*c4d.SplineData*](../c4d/CustomDataType/SplineData/index.md#c4d.SplineData)]) – The optional curve to use.

**Returns:** The mapped valued.

**Return type:** float

#### `c4d.utils.Smoothstep(a, b, x)` <a id="c4d.utils.Smoothstep"></a>

Returns *0.0* if *x* is less than *a* and *1.0* if *x* is greater than *b*, else returns *x* mapped on the range [a,b] (a number between 0.0 and 1.0). The mapping is smoothed using an ease-in/ease-out curve.

**Parameters:**

- **a** (*float*) – The float value.
- **b** (*float*) – The float value.
- **x** (*float*) – The float value.

**Return type:** float

**Returns:** The smoothed value.

#### `c4d.utils.Step(a, b)` <a id="c4d.utils.Step"></a>

Returns 1.0 if *b* is greater than or equal to *a*, else 0.0.

**Parameters:**

- **a** (*number*) – The float value.
- **b** (*number*) – The float value.

**Return type:** float

**Returns:** The step value (1.0 or 0.0).

#### `c4d.utils.Truncate(x)` <a id="c4d.utils.Truncate"></a>

Limit a color vector between 0.0 and 1.0.

The internal code:

```python
import c4d
import math

# Internal code of c4d.utils.Truncate
def Truncate(x):
    if x >= 0.0:
        return math.floor(x)
    else:
        return math.fceil(x)

print c4d.utils.Truncate(1.5) == Truncate(1.5)
```

**Parameters:** **x** (*number*) – The value to truncate.

**Return type:** float

**Returns:** The truncated value.

### Rotation Conversions <a id="c4d.utils-function-Rotation-Conversions"></a>

#### `c4d.utils.GetOptimalAngle(hpb_old, hpb_new, rotation_order)` <a id="c4d.utils.GetOptimalAngle"></a>

Modify *hpb_new* so that the “distance” to the last angle *hpb_old* is at minimum. This helps to avoid HPB singularity effects.

**Parameters:**

- **hpb_old** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The old HPB.

- **hpb_new** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The new HPB.

- **rotation_order** (*int*) –

  The order of rotation:

  |   |   |
  |---|---|
  | *ROTATIONORDER_YXZGLOBAL* | Global YXZ order. |
  | *ROTATIONORDER_YZXGLOBAL* | Global YZX order. |
  | *ROTATIONORDER_ZYXGLOBAL* | Global ZYX order. |
  | *ROTATIONORDER_ZXYGLOBAL* | Global ZXY order. |
  | *ROTATIONORDER_XZYGLOBAL* | Global XZY order. |
  | *ROTATIONORDER_XYZGLOBAL* | Global XYZ order. |
  | *ROTATIONORDER_YXZLOCAL* | Local YXZ order. |
  | *ROTATIONORDER_YZXLOCAL* | Local YZX order. |
  | *ROTATIONORDER_ZYXLOCAL* | Local ZYX order. |
  | *ROTATIONORDER_ZXYLOCAL* | Local ZXY order. |
  | *ROTATIONORDER_XZYLOCAL* | Local XZY order. |
  | *ROTATIONORDER_XYZLOCAL* | Local XYZ order. |
  | *ROTATIONORDER_HPB* | HPB order. |
  | *ROTATIONORDER_DEFAULT* | Default order. *ROTATIONORDER_HPB*. |

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** The optimal angle.

#### `c4d.utils.HPBToMatrix(hpb, order=6)` <a id="c4d.utils.HPBToMatrix"></a>

Construct matrix from the euler angles *hpb*.

**Parameters:**

- **hpb** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The input HPB.

- **order** (*int*) –

  The order of rotation:

  |   |   |
  |---|---|
  | *ROTATIONORDER_YXZGLOBAL* | Global YXZ order. |
  | *ROTATIONORDER_YZXGLOBAL* | Global YZX order. |
  | *ROTATIONORDER_ZYXGLOBAL* | Global ZYX order. |
  | *ROTATIONORDER_ZXYGLOBAL* | Global ZXY order. |
  | *ROTATIONORDER_XZYGLOBAL* | Global XZY order. |
  | *ROTATIONORDER_XYZGLOBAL* | Global XYZ order. |
  | *ROTATIONORDER_YXZLOCAL* | Local YXZ order. |
  | *ROTATIONORDER_YZXLOCAL* | Local YZX order. |
  | *ROTATIONORDER_ZYXLOCAL* | Local ZYX order. |
  | *ROTATIONORDER_ZXYLOCAL* | Local ZXY order. |
  | *ROTATIONORDER_XZYLOCAL* | Local XZY order. |
  | *ROTATIONORDER_XYZLOCAL* | Local XYZ order. |
  | *ROTATIONORDER_HPB* | HPB order. |
  | *ROTATIONORDER_DEFAULT* | Default order. *ROTATIONORDER_HPB*. |

**Return type:** [c4d.Matrix](../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The rotation matrix.

#### `c4d.utils.MatrixRotX(w)` <a id="c4d.utils.MatrixRotX"></a>

Creates a rotation matrix about the X axis.

**Parameters:** **w** (*float*) – The angle around X.

**Return type:** [c4d.Matrix](../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The rotation matrix.

#### `c4d.utils.MatrixRotY(w)` <a id="c4d.utils.MatrixRotY"></a>

Creates a rotation matrix about the Y axis.

**Parameters:** **w** (*float*) – The angle around Y.

**Return type:** [c4d.Matrix](../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The rotation matrix.

#### `c4d.utils.MatrixRotZ(w)` <a id="c4d.utils.MatrixRotZ"></a>

Creates a rotation matrix about the Z axis.

**Parameters:** **w** (*float*) – The angle around Z.

**Return type:** [c4d.Matrix](../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The rotation matrix.

#### `c4d.utils.MatrixToHPB(m, order=6, isNormalized=False)` <a id="c4d.utils.MatrixToHPB"></a>

Calculate euler angles from the matrix *m*.

**Parameters:**

- **m** ([*c4d.Matrix*](../c4d/Matrix/index.md#c4d.Matrix)) – The rotation matrix.

- **order** (*int*) –

  The order of rotation:

  |   |   |
  |---|---|
  | *ROTATIONORDER_YXZGLOBAL* | Global YXZ order. |
  | *ROTATIONORDER_YZXGLOBAL* | Global YZX order. |
  | *ROTATIONORDER_ZYXGLOBAL* | Global ZYX order. |
  | *ROTATIONORDER_ZXYGLOBAL* | Global ZXY order. |
  | *ROTATIONORDER_XZYGLOBAL* | Global XZY order. |
  | *ROTATIONORDER_XYZGLOBAL* | Global XYZ order. |
  | *ROTATIONORDER_YXZLOCAL* | Local YXZ order. |
  | *ROTATIONORDER_YZXLOCAL* | Local YZX order. |
  | *ROTATIONORDER_ZYXLOCAL* | Local ZYX order. |
  | *ROTATIONORDER_ZXYLOCAL* | Local ZXY order. |
  | *ROTATIONORDER_XZYLOCAL* | Local XZY order. |
  | *ROTATIONORDER_XYZLOCAL* | Local XYZ order. |
  | *ROTATIONORDER_HPB* | HPB order. |
  | *ROTATIONORDER_DEFAULT* | Default order. *ROTATIONORDER_HPB*. |

- **isNormalized** (*bool*) – True if the matrix is already normalized.

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** The HPB.

#### `c4d.utils.MatrixToRotAxis(m)` <a id="c4d.utils.MatrixToRotAxis"></a>

Calculates rotation axis and angle from matrix *m*:

```python
import c4d
import math

# 90 degree
angle = math.pi * .5
m = c4d.utils.MatrixRotX(angle)

v, w = c4d.utils.MatrixToRotAxis(m)
# v is the rotation axis, c4d.Vector
# w is the rotation angle, float
```

**Parameters:** **m** ([*c4d.Matrix*](../c4d/Matrix/index.md#c4d.Matrix)) – Rotation matrix.

**Return type:** list

**Returns:** The rotation axis, and the angle.

#### `c4d.utils.RotAxisToMatrix(v, w)` <a id="c4d.utils.RotAxisToMatrix"></a>

Calculate matrix from rotation axis *v* and angle *w*.

**Parameters:**

- **v** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The axis.
- **w** (*float*) – The angle of rotation.

**Return type:** [c4d.Matrix](../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The rotation matrix.

#### `c4d.utils.VectorToHPB(p)` <a id="c4d.utils.VectorToHPB"></a>

Calculate euler angles from the vector *p*. The bank is always set to 0.0.

**Parameters:** **p** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The vector to find the HPB for.

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** The rotation HPB.

### Spatial Geometry <a id="c4d.utils-function-Spatial-Geometry"></a>

#### `c4d.utils.CircleLineIntersection(linePoint1, linePoint2, circleCenter, circleRadius)` <a id="c4d.utils.CircleLineIntersection"></a>

Calculates the intersection points between a line and a circle in 2D space (although *Z* will also be calculated on the resulting hit points).

*New in version R16.021.*

**Parameters:**

- **linePoint1** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The first point of the line.
- **linePoint2** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The second point of the line.
- **circleCenter** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The center of the circle.
- **circleRadius** (*float*) – The radius of the circle.

**Return type:** Tuple[bool, float, float, [c4d.Vector](../c4d/Vector/index.md#c4d.Vector), [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)]

**Returns:**

A tuple with the following information:

1. bool: **True** if the line segment intersected the circle, otherwise **False**.
2. float: The first intersection point (lowest) as an offset between *linePoint1* and *linePoint2*.
3. float: The second intersection point (highest) as an offset between *linePoint1* and *linePoint2*.
4. [`Vector`](../c4d/Vector/index.md#c4d.Vector): The actual 3D point where the line first intersects (enters) the circle, *Z* may also be calculated.
5. [`Vector`](../c4d/Vector/index.md#c4d.Vector): The actual 3D point where the line subsequently intersects (exits) the circle, *Z* may also be calculated.

#### `c4d.utils.PointLineDistance(p0, v, p)` <a id="c4d.utils.PointLineDistance"></a>

Calculates the distance from a point to a line.

**Parameters:**

- **p0** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The starting point of the line.
- **v** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The line vector.
- **p** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The point.

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** Point-line vector.

#### `c4d.utils.PointLineSegmentDistance(segmentPoint1, segmentPoint2, pos)` <a id="c4d.utils.PointLineSegmentDistance"></a>

Calculates the distance from a point to a line segment between two points.

*New in version R17.048.*

**Parameters:**

- **segmentPoint1** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The line segment first point.
- **segmentPoint2** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The line segment second point.
- **pos** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The point to test against the line segment.

**Return type:** Tuple[float,[c4d.Vector](../c4d/Vector/index.md#c4d.Vector), float]

**Returns:**

A tuple with the following information:

1. The distance between the point and the line segment.
2. The intersection point on the segment.
3. The offset along the segment of the intersection point.

#### `c4d.utils.PointLineSegmentDistance2D(segmentPoint1, segmentPoint2, pos)` <a id="c4d.utils.PointLineSegmentDistance2D"></a>

Calculates the distance from a point to a line segment between two points in 2D ignoring the Z value.

*New in version R17.048.*

**Parameters:**

- **segmentPoint1** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The line segment first point.
- **segmentPoint2** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The line segment second point.
- **pos** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The point to test against the line segment.

**Return type:** Tuple[float, [c4d.Vector](../c4d/Vector/index.md#c4d.Vector), float]

**Returns:**

A tuple with the following information:

1. The distance between the point and the line segment.
2. The intersection point on the segment.
3. The offset along the segment of the intersection point.

#### `c4d.utils.ReflectRay(v, n)` <a id="c4d.utils.ReflectRay"></a>

Find the ray vector after a reflection about a surface normal.

**Parameters:**

- **v** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The incoming ray.
- **n** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The surface normal.

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** The reflected ray.

#### `c4d.utils.SphereLineIntersection(linePoint1, linePoint2, sphereCenter, sphereRadius)` <a id="c4d.utils.SphereLineIntersection"></a>

Calculates the intersection points between a line and a sphere in 3D space.

*New in version R16.021.*

**Parameters:**

- **linePoint1** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The first point of the line.
- **linePoint2** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The second point of the line.
- **sphereCenter** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The center of the sphere.
- **sphereRadius** (*float*) – The radius of the sphere.

**Return type:** Tuple[bool, float, float, [c4d.Vector](../c4d/Vector/index.md#c4d.Vector), [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)]

**Returns:**

A tuple with the following information:

1. bool: **True** if the line segment intersected the sphere, otherwise **False**.
2. float: The first intersection point (lowest) as an offset between *linePoint1* and *linePoint2*.
3. float: The second intersection point (highest) as an offset between *linePoint1* and *linePoint2*.
4. [`Vector`](../c4d/Vector/index.md#c4d.Vector): The actual 3D point where the line first intersects (enters) the sphere.
5. [`Vector`](../c4d/Vector/index.md#c4d.Vector): The actual 3D point where the line subsequently intersects (exits) the sphere.

### Spline Operations <a id="c4d.utils-function-Spline-Operations"></a>

#### `c4d.utils.CalcSpline(x, knots)` <a id="c4d.utils.CalcSpline"></a>

Calculates the value of a spline at a point.

**Parameters:**

- **x** (*float*) – The position on the spline.
- **knots** (*List*[*float*]) – The knots list.

**Return type:** float

**Returns:** The spline value.

#### `c4d.utils.CalcSplineDefaultTangents(type, closed, pcnt, padr)` <a id="c4d.utils.CalcSplineDefaultTangents"></a>

Calculates the default tangents for the passed points (spline segment) based on the spline type.

*New in version R17.048.*

**Parameters:**

- **type** (*int*) –

  The type of spline to move. Check out [Spline Types](../../types/spline.md#spline-type).

  |   |   |
  |---|---|
  | *SPLINETYPE_LINEAR* | Linear. |
  | *SPLINETYPE_CUBIC* | Cubic. |
  | *SPLINETYPE_AKIMA* | Akima. |
  | *SPLINETYPE_BSPLINE* | B-Spline. |
  | *SPLINETYPE_BEZIER* | Bezier. |

- **closed** (*bool*) – The closed state of the spline.

- **pcnt** (*int*) – The number of points in the spline.

- **padr** (*List*[[*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)]) – The points that describe the spline.

**Return type:** List[Dict[str: c4d.Vector]]

**Returns:** The resulting tangents. A tangent dictionary is defined as: Dict[‘vl’: [`Vector`](../c4d/Vector/index.md#c4d.Vector), ‘vr’: [`Vector`](../c4d/Vector/index.md#c4d.Vector)]

#### `c4d.utils.CalcSplineInsert(offset, type, closed, pcnt, padr, tadr=None)` <a id="c4d.utils.CalcSplineInsert"></a>

Calculates data about a point would if it were inserted into the spline at the passed offset.

*New in version R17.048.*

**Parameters:**

- **offset** (*float*) – The offset along the spline from *0.0* to *1.0*.

- **type** (*int*) –

  The type of spline. Check out [Spline Types](../../types/spline.md#spline-type).

  |   |   |
  |---|---|
  | *SPLINETYPE_LINEAR* | Linear. |
  | *SPLINETYPE_CUBIC* | Cubic. |
  | *SPLINETYPE_AKIMA* | Akima. |
  | *SPLINETYPE_BSPLINE* | B-Spline. |
  | *SPLINETYPE_BEZIER* | Bezier. |

- **closed** (*bool*) – Whether the spline is closed or not.

- **pcnt** (*int*) – The number of points in the spline.

- **padr** (*List*[[*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)]) – The points array.

- **tadr** (*Optional*[*List*[*Dict*[*str: c4d.Vector*]]]) –

  The tangents array, required for Bezier, Cubic and Akima spline types (otherwise will default to b-spline).  
  A tangent dictionary has to be defined as: Dict[‘vl’: [`Vector`](../c4d/Vector/index.md#c4d.Vector), ‘vr’: [`Vector`](../c4d/Vector/index.md#c4d.Vector)]

**Return type:** Dict[int, [`Vector`](../c4d/Vector/index.md#c4d.Vector), Tangent, [`Vector`](../c4d/Vector/index.md#c4d.Vector), [`Vector`](../c4d/Vector/index.md#c4d.Vector)]

**Returns:** A dictionary with the following information:

- “pointIndex”: The index that the resulting point would be if it were inserted into the spline.
- “resultPoint”: The position of the resulting point.
- “resultTangent”: The spline tangent information of the resulting point. Dict[‘vl’: [`Vector`](../c4d/Vector/index.md#c4d.Vector),’vr’: [`Vector`](../c4d/Vector/index.md#c4d.Vector)]
- “leftTangent”: The correct new left tangent (*tadr[pointIndex - 1].vr*).
- “rightTangent”: The correct new right tangent (*tadr[pointIndex].vl*).

#### `c4d.utils.CalcSplineMovement(newPos, offset, type, splineMg, bd, planeNormal, closed, lockTangentAngle, lockTangentLength, breakTangents, pcnt, padr, tadr)` <a id="c4d.utils.CalcSplineMovement"></a>

Moves a point on a spline curve to a user specified new position.

*New in version R17.048.*

**Parameters:**

- **newPos** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The new position for the point of the curve at *offset*.

- **offset** (*float*) – The offset to move to the position newPos.

- **type** (*int*) –

  The type of spline to move. Check out [Spline Types](../../types/spline.md#spline-type).

  |   |   |
  |---|---|
  | *SPLINETYPE_LINEAR* | Linear. |
  | *SPLINETYPE_CUBIC* | Cubic. |
  | *SPLINETYPE_AKIMA* | Akima. |
  | *SPLINETYPE_BSPLINE* | B-Spline. |
  | *SPLINETYPE_BEZIER* | Bezier. |

- **splineMg** ([*c4d.Matrix*](../c4d/Matrix/index.md#c4d.Matrix)) – The matrix of the spline.

- **bd** (*Optional*[[*c4d.BaseDraw*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)]) – The optional basedraw. Can be **None**.

- **planeNormal** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The normal for tangent rotation, typically *Vector(0,0,1)*.

- **closed** (*bool*) – The closed state of the spline.

- **lockTangentAngle** (*bool*) – **True** if tangents angle may not be changed by this routine.

- **lockTangentLength** (*bool*) – **True** if the tangents length may not be changed by this routine.

- **breakTangents** (*int*) –

  Set to break the tangents while manipulating the curve if tangents exist:

  | Symbol ID | Description |
  |---|---|
  | BREAKTANGENTS_V_FALSE | Do not break any tangents. |
  | BREAKTANGENTS_V_TRUE | Break the tangents. |
  | BREAKTANGENTS_V_AUTO | Only break the tangents if they are already broken. |

- **pcnt** (*int*) – The number of points in the spline.

- **padr** (*List*[[*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)]) – The points that describe the spline.

- **tadr** (*Optional*[*List*[*Dict*[*str: c4d.Vector*]]]) –

  The tangents that are used by the spline.  
  A tangent dictionary has to be defined as: Dict[‘vl’: [`Vector`](../c4d/Vector/index.md#c4d.Vector), ‘vr’: [`Vector`](../c4d/Vector/index.md#c4d.Vector)]

**Return type:** Tuple[List[[c4d.Vector](../c4d/Vector/index.md#c4d.Vector)], List[Dict[str: c4d.Vector]]]

**Returns:** The resulting lists of points and tangents.

#### `c4d.utils.CalcSplinePoint(offset, type, closed, pcnt, padr, tadr=None)` <a id="c4d.utils.CalcSplinePoint"></a>

Calculates a point along a spline curve from a set of points in 3D space.

*New in version R17.048.*

**Parameters:**

- **offset** (*float*) – The offset along the spline from *0.0* to *1.0*.

- **type** (*int*) –

  The type of spline. Check out [Spline Types](../../types/spline.md#spline-type).

  |   |   |
  |---|---|
  | *SPLINETYPE_LINEAR* | Linear. |
  | *SPLINETYPE_CUBIC* | Cubic. |
  | *SPLINETYPE_AKIMA* | Akima. |
  | *SPLINETYPE_BSPLINE* | B-Spline. |
  | *SPLINETYPE_BEZIER* | Bezier. |

- **closed** (*bool*) – Whether the spline is closed or not.

- **pcnt** (*int*) – The number of points in the spline.

- **padr** (*List*[[*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)]) – The points array.

- **tadr** (*Optional*[*List*[*Dict*[*str: c4d.Vector*]]]) –

  The tangents array, required for Bezier, Cubic and Akima spline types (otherwise will default to b-spline).  
  A tangent dictionary has to be defined as: Dict[‘vl’: [`Vector`](../c4d/Vector/index.md#c4d.Vector), ‘vr’: [`Vector`](../c4d/Vector/index.md#c4d.Vector)]

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** The resulting point calculated from the offset.

#### `c4d.utils.CalcSplineTangent(offset, type, closed, pcnt, padr, tadr=None)` <a id="c4d.utils.CalcSplineTangent"></a>

Calculates the tangent of a point along a spline curve from a given set of points and optional tangents.

*New in version R17.048.*

**Parameters:**

- **offset** (*float*) – The offset along the spline from *0.0* to *1.0*.

- **type** (*int*) –

  The type of spline. Check out [Spline Types](../../types/spline.md#spline-type).

  |   |   |
  |---|---|
  | *SPLINETYPE_LINEAR* | Linear. |
  | *SPLINETYPE_CUBIC* | Cubic. |
  | *SPLINETYPE_AKIMA* | Akima. |
  | *SPLINETYPE_BSPLINE* | B-Spline. |
  | *SPLINETYPE_BEZIER* | Bezier. |

- **closed** (*bool*) – Whether the spline is closed or not.

- **pcnt** (*int*) – The number of points in the spline.

- **padr** (*List*[[*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)]) – The points array.

- **tadr** (*Optional*[*List*[*Dict*[*str: c4d.Vector*]]]) –

  The tangents array, required for Bezier, Cubic and Akima spline types (otherwise will default to b-spline).  
  A tangent dictionary has to be defined as: Dict[‘vl’: [`Vector`](../c4d/Vector/index.md#c4d.Vector), ‘vr’: [`Vector`](../c4d/Vector/index.md#c4d.Vector)]

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** The resulting tangent (normalized) for the given offset.

#### `c4d.utils.CalcSplineV(x, knots)` <a id="c4d.utils.CalcSplineV"></a>

Calculates the value of a spline at a point.

**Parameters:**

- **x** (*float*) – The position on the spline.
- **knots** (*List*[[*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)]) – The knots list.

**Return type:** [c4d.Vector](../c4d/Vector/index.md#c4d.Vector)

**Returns:** The spline value.

#### `c4d.utils.FitCurve(padr, error, bt=None)` <a id="c4d.utils.FitCurve"></a>

Creates a spline object that has the best fit through the given points.

**Parameters:**

- **padr** (*List*[[*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)]) – The points to fit a curve to.

- **error** (*float*) – Sets how closely the curve must match the passed points. The lower the value then the closer the curve will match.

- **bt** (*Optional*[[*c4d.threading.BaseThread*](../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)]) –

  *New in version R18.057:* An optional thread.

**Return type:** [`c4d.SplineObject`](../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/SplineObject/index.md#c4d.SplineObject)

**Returns:** A Spline object that fits the given points, or AllocationFailed error if a spline object cannot be obtained.

#### `c4d.utils.TransformTangent(newPos, planeNormal, position, tangent, tangentSide, flags=4)` <a id="c4d.utils.TransformTangent"></a>

Creates a transformed tangent around a point and plane, allowing to directly set the position of one of the tangent handles and automatically rotating the rest of the tangent to match.

*New in version R17.048.*

**Parameters:**

- **newPos** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The new position for the tangent handle.

- **planeNormal** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The normal of the plane for rotation of the handles.

- **position** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The position of the center of the tangent being modified.

- **tangent** (*dict*) –

  The tangent to modify/derive the resulting tangent from.  
  A tangent dictionary has to be defined as: Dict[‘vl’: [`Vector`](../c4d/Vector/index.md#c4d.Vector), ‘vr’: [`Vector`](../c4d/Vector/index.md#c4d.Vector)]

- **tangentSide** (*int*) –

  The handle to modify of the tangent, left, right, or none:

  |   |   |
  |---|---|
  | *TANGENTSIDE_NONE* | No tangent handles being modified. |
  | *TANGENTSIDE_LEFT* | Modify the left tangent handle. |
  | *TANGENTSIDE_RIGHT* | Modify the right tangent handle. |

- **flags** (*int*) –

  The flags for controlling tangent breaking, rotation and scale locking etc.

  |   |   |
  |---|---|
  | *TANGENTTRANSFORMFLAG_NONE* | None. |
  | *TANGENTTRANSFORMFLAG_LOCK_LENGTH* | Fix the length of the tangents, only change the rotation. |
  | *TANGENTTRANSFORMFLAG_LOCK_ANGLE* | Fix the angle of the tangents, only change the length. |
  | *TANGENTTRANSFORMFLAG_BREAK_SCALE* | Only scale one handle (but rotate both). |
  | *TANGENTTRANSFORMFLAG_BREAK* | Only modify one handle. |

**Return type:** Dict[‘vl’: [`Vector`](../c4d/Vector/index.md#c4d.Vector),’vr’: [`Vector`](../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The resulting transformed tangent.

### Texture Baking <a id="c4d.utils-function-Texture-Baking"></a>

#### `c4d.utils.BakeTexture(doc, data, bmp, th, hook)` <a id="c4d.utils.BakeTexture"></a>

Bakes the texture(s) specified by the last [`InitBakeTexture()`](#c4d.utils.InitBakeTexture) call into *bmp*.

*New in version R18.011.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

- **data** ([*c4d.BaseContainer*](../c4d/BaseContainer/index.md#c4d.BaseContainer)) –

  The bake settings:

  |   |   |   |
  |---|---|---|
  | *BAKE_TEX_USE_CAMERA_VECTOR* | bool | Use camera vector. |
  | *BAKE_TEX_USE_POLYSELECTION* | bool | Use polygon selection. |
  | *BAKE_TEX_AMBIENT_OCCLUSION* | bool | Bake ambient occlusion. |
  | *BAKE_TEX_NORMAL* | bool | Bake normal channel. |
  | *BAKE_TEX_SURFACECOLOR* | bool | Bake surface color. |
  | *BAKE_TEX_COLOR* | bool | Bake color. |
  | *BAKE_TEX_DIFFUSION* | bool | Bake diffusion channel. |
  | *BAKE_TEX_LUMINANCE* | bool | Bake luminance. |
  | *BAKE_TEX_ALPHA* | bool | Bake alpha channel. |
  | *BAKE_TEX_ILLUMINATION* | bool | Bake illumination. |
  | *BAKE_TEX_SHADOWS* | bool | Bake shadows. |
  | *BAKE_TEX_BUMP* | bool | Bake bump. |
  | *BAKE_TEX_TRANSPARENCY* | bool | Bake transparency. |
  | *BAKE_TEX_UVMAP* | bool | Bake UV map. |
  | *BAKE_TEX_REFLECTION* | bool | Bake reflection. |
  | *BAKE_TEX_DISPLACEMENT* | bool | Bake displacement. |
  | *BAKE_TEX_WIDTH* | int | Width. |
  | *BAKE_TEX_HEIGHT* | int | Height. |
  | *BAKE_TEX_PIXELBORDER* | int | Pixel border. |
  | *BAKE_TEX_FILL_COLOR* | [`Vector`](../c4d/Vector/index.md#c4d.Vector) | Fill color. |
  | *BAKE_TEX_UV_LEFT* | float | Left UV coordinate. |
  | *BAKE_TEX_UV_RIGHT* | float | Right UV coordinate. |
  | *BAKE_TEX_UV_TOP* | float | Top UV coordinate. |
  | *BAKE_TEX_UV_BOTTOM* | float | Bottom UV coordinate. |
  | *BAKE_TEX_SUPERSAMPLING* | int | Supersampling. |
  | *BAKE_TEX_USE_BUMP* | bool | Use bump. |
  | *BAKE_TEX_NO_GI* | bool | No GI. |
  | *BAKE_TEX_CONTINUE_UV* | bool | Continue UV. |
  | *BAKE_TEX_USE_PHONG_TAG* | bool | The pixel will be clamped to the current polygon if set to **True** and if the angle between polygons is bigger than their phong angle. Only needed if *BAKE_TEX_CONTINUE_UV* is set to **True**. |
  | *BAKE_TEX_COLORPROFILE* | [`ColorProfile`](../c4d.bitmaps/ColorProfile/index.md#c4d.bitmaps.ColorProfile) | Color profile of the baked texture. |
  | *BAKE_TEX_SHOW_STATUS* | bool | Show status. |
  | *BAKE_TEX_PROGRESS_BITMAP* | bool | Show the bitmap in a preview during baking. |
  | *BAKE_TEX_GENERATE_UNDO* | bool | Generate undo for UVW tags and Vertex tags created by the baker. |
  | *BAKE_TEX_PREVIEW* | bool | Bake texture preview. |
  | *BAKE_TEX_COLOR_ILLUM* | bool | Illumination in color. |
  | *BAKE_TEX_COLOR_SHADOWS* | bool | Shadows in color. |
  | *BAKE_TEX_COLOR_LUMINANCE* | bool | Luminance in color. |
  | *BAKE_TEX_COLOR_DIFFUSION* | bool | Diffusion in color. |
  | *BAKE_TEX_LUMINANCE_DIFFUSION* | bool | Diffusion in luminance. |
  | *BAKE_TEX_ILLUMINATION_SHADOWS* | bool | Shadows in luminance. |
  | *BAKE_TEX_NORMAL_METHOD* | int | Normal method: |
  | *BAKE_TEX_NORMAL_METHOD_OBJECT* |  | Object. |
  | *BAKE_TEX_NORMAL_METHOD_TANGENT* |  | Tangent. |
  | *BAKE_TEX_NORMAL_METHOD_WORLD* |  | World. |
  | *BAKE_TEX_NORMAL_FLIP_X* | bool | Flip X. |
  | *BAKE_TEX_NORMAL_FLIP_Y* | bool | Flip Y. |
  | *BAKE_TEX_NORMAL_FLIP_Z* | bool | Flip Z. |
  | *BAKE_TEX_NORMAL_SWAP_YZ* | bool | Swap Y/Z. |
  | *BAKE_TEX_NORMAL_SOURCE* | link | Normal source. |
  | *BAKE_TEX_NORMAL_USE_RAYCAST* | bool | *New in version R18:* Whether the normal map will be generated using ray casting. True when baking the normal map only. |
  | *BAKE_TEX_SURFACE_ILLUMINATION* | bool | Surface illumination. |
  | *BAKE_TEX_AO_VERTEX_MAP* | bool | Ambient occlusion in vertex map. |
  | *BAKE_TEX_AO_SELFINTERSECTION* | bool | Ambient occlusion self-intersection. |
  | *BAKE_TEX_AO_VERTEXMAPS* | [`BaseContainer`](../c4d/BaseContainer/index.md#c4d.BaseContainer) | A container that stores all new generated vertex maps. |
  | *BAKE_TEX_DISPLACEMENT_SOURCE* | link | The high-res source object. |
  | *BAKE_TEX_DISPLACEMENT_HEIGHT* | float | A float that will receive the displacement height. |
  | *BAKE_TEX_DISPLACEMENT_METHOD* | int | Displacement method: |
  | *BAKE_TEX_DISPLACEMENT_METHOD_OBJECT* |  | Object. |
  | *BAKE_TEX_DISPLACEMENT_METHOD_WORLD* |  | World. |
  | *BAKE_TEX_DISPLACEMENT_METHOD_TANGENT* |  | Tangent. |
  | *BAKE_TEX_DISPLACEMENT_METHOD_INTENSITY* |  | Intensity. |
  | *BAKE_TEX_DISPLACEMENT_METHOD_CENTEREDINTENSITY* |  | Centered intensity. |
  | *BAKE_TEX_DISPLACEMENT_METHOD_REDGREEN* |  | Red <-> Green. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY* | bool | Displacement subpoly. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_SUBDIVISION* | int | Displacement subpoly subdivision. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_ROUND* | bool | Displacement subpoly round. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_ROUNDCONTOUR* | bool | Displacement subpoly round contour. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_HQREMAPPING* | bool | Displacement subpoly HQ remapping. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_MAPRESULT* | bool | Displacement subpoly map result. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_KEEPEDGES* | bool | Displacement subpoly keep edges. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_DISTRIBUTION* | bool | Displacement subpoly distribution. |
  | *BAKE_TEX_RAYCAST_USE_MAX_DISTANCE* | bool | *New in version R18:* Use maximum ray casting distance. |
  | *BAKE_TEX_RAYCAST_CUSTOM_MAX_DISTANCE* | float | *New in version R18:* Custom maximum ray casting distance. |
  | *BAKE_TEX_RAYCAST_USE_AUTO_SPIKE_FILTER_THRESHOLD* | bool | *New in version R18:* Use automatic spike filter threshold. |
  | *BAKE_TEX_RAYCAST_CUSTOM_SPIKE_FILTER_THRESHOLD* | float | *New in version R18:* Custom spike filter threshold. |
  | *BAKE_TEX_OPTIMAL_MAPPING* | int | Optimal mapping: |
  | *BAKE_TEX_OPTIMAL_MAPPING_OFF* |  | Off. |
  | *BAKE_TEX_OPTIMAL_MAPPING_CUBIC* |  | Cubic. |
  | *BAKE_TEX_OPTIMAL_MAPPING_ANGLE* |  | Angle. |
  | *BAKE_TEX_OPTIMAL_MAPPING_PACKED* |  | Packed. |
  | *BAKE_TEX_OPTIMAL_MAPPING_RELAXCOUNT* | int | Optimal mapping relax count. |
  | *BAKE_TEX_OPTIMAL_MAPPING_PREVIEW* | int | Optimal mapping preview. |
  | *BAKE_TEX_NO_INIT_BITMAP* | bool | Set to **True** if the passed [`MultipassBitmap`](../c4d.bitmaps/BaseBitmap/MultipassBitmap/index.md#c4d.bitmaps.MultipassBitmap) is already initialized. |
  | *BAKE_TEX_AUTO_SIZE* | bool | Auto size. |
  | *BAKE_TEX_AUTO_SIZE_MIN* | int | Minimum auto size. |
  | *BAKE_TEX_AUTO_SIZE_MAX* | int | Maximum auto size. |
  | *BAKE_TEX_AUTO_PIXEL_SIZE* | float | Automatic pixel size. |
  | *BAKE_TEX_STATUSBAR* | str | Status bar text. |

- **bmp** ([*c4d.bitmaps.BaseBitmap*](../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The bitmap to bake to.

- **th** (*Optional*[[*c4d.threading.BaseThread*](../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)]) – The current thread. Can be **None**.

- **hook** (*Optional*[*Callable*[[*Dict*[]], *Optional*[*bool*]]]) –

  The bake progress hook callback function. This function gets passed a dictionary with the following information:

  |   |   |   |
  |---|---|---|
  | ’version’ | int | Bake version. |
  | ’state’ | int | Bake state: |
  |  | *BAKE_STATE_NONE* | None. |
  |  | *BAKE_STATE_PREPARE* | Prepare. |
  |  | *BAKE_STATE_GI_PREPASS* | GI prepass. |
  |  | *BAKE_STATE_FILL_IMAGE* | Fill image. |
  |  | *BAKE_STATE_COMPLETE* | Complete. |
  |  | *BAKE_STATE_INITIALIZE* | Initialize. |
  |  | *BAKE_STATE_RESIZENOTIFY* | Resize notify. |
  | ’data’ | tuple(int, int, [`BaseBitmap`](../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) | Only used in case of *BAKE_STATE_RESIZENOTIFY* state. Tuple data is resize width, resize height and cake bitmap. |
  | ’timedelta’ | int | Time. |
  | ’r’ | float | Progress, between *0* and *1*. |
  | ’starttime’ | int | Start time in milliseconds. |

  If the state is *BAKE_STATE_RESIZENOTIFY*, the return value has to be a bool to set the result of the resize operation. Otherwise the hook must return **None**.

**Return type:** int

**Returns:**

*BAKE_TEX_ERR_NONE* if successful, otherwise one of these errors:

|   |   |
|---|---|
| *BAKE_TEX_ERR_NONE* | None. |
| *BAKE_TEX_ERR_NO_DOC* | No document. |
| *BAKE_TEX_ERR_NO_MEM* | No more memory available. |
| *BAKE_TEX_ERR_NO_RENDER_DOC* | No render document. |
| *BAKE_TEX_ERR_NO_TEXTURE_TAG* | *textag* is **None** or not in *doc*. |
| *BAKE_TEX_ERR_NO_OBJECT* | One of the tags is not assigned to an object or to another object. |
| *BAKE_TEX_ERR_NO_UVW_TAG* | UVW tag is missing. |
| *BAKE_TEX_ERR_TEXTURE_MISSING* | No texture. |
| *BAKE_TEX_ERR_WRONG_BITMAP* | [`MultipassBitmap`](../c4d.bitmaps/BaseBitmap/MultipassBitmap/index.md#c4d.bitmaps.MultipassBitmap) was used, but it has the wrong type or wrong resolution. |
| *BAKE_TEX_ERR_USERBREAK* | User break. |
| *BAKE_TEX_ERR_NO_OPTIMAL_MAPPING* | Optimal mapping failed. |
| *BAKE_TEX_ERR_NO_SOURCE_UVW_TAG* | UVW tag for the source object is missing. |

#### `c4d.utils.InitBakeTexture(doc, textags, texuvws, destuvws, bc, th=None)` <a id="c4d.utils.InitBakeTexture"></a>

Initializes a bake operation of a single tag for [`BakeTexture()`](#c4d.utils.BakeTexture).

*New in version R18.011.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

- **textags** ([*c4d.TextureTag*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/TextureTag/index.md#c4d.TextureTag)) – The texture tag(s) to bake. Must be assigned to an object.

- **texuvws** ([*c4d.UVWTag*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/UVWTag/index.md#c4d.UVWTag)) – The UVW tag(s) to bake. Must be valid if UVW projection is selected in the texture tag(s), ignored otherwise.

- **destuvws** (*Optional*[[*c4d.UVWTag*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/UVWTag/index.md#c4d.UVWTag)]) – The destination UVW tag for the bake. If not **None**, the current projection is transformed into the UVW tag.

- **bc** ([*c4d.BaseContainer*](../c4d/BaseContainer/index.md#c4d.BaseContainer)) –

  The bake settings:

  |   |   |   |
  |---|---|---|
  | *BAKE_TEX_USE_CAMERA_VECTOR* | bool | Use camera vector. |
  | *BAKE_TEX_USE_POLYSELECTION* | bool | Use polygon selection. |
  | *BAKE_TEX_AMBIENT_OCCLUSION* | bool | Bake ambient occlusion. |
  | *BAKE_TEX_NORMAL* | bool | Bake normal channel. |
  | *BAKE_TEX_SURFACECOLOR* | bool | Bake surface color. |
  | *BAKE_TEX_COLOR* | bool | Bake color. |
  | *BAKE_TEX_DIFFUSION* | bool | Bake diffusion channel. |
  | *BAKE_TEX_LUMINANCE* | bool | Bake luminance. |
  | *BAKE_TEX_ALPHA* | bool | Bake alpha channel. |
  | *BAKE_TEX_ILLUMINATION* | bool | Bake illumination. |
  | *BAKE_TEX_SHADOWS* | bool | Bake shadows. |
  | *BAKE_TEX_BUMP* | bool | Bake bump. |
  | *BAKE_TEX_TRANSPARENCY* | bool | Bake transparency. |
  | *BAKE_TEX_UVMAP* | bool | Bake UV map. |
  | *BAKE_TEX_REFLECTION* | bool | Bake reflection. |
  | *BAKE_TEX_DISPLACEMENT* | bool | Bake displacement. |
  | *BAKE_TEX_WIDTH* | int | Width. |
  | *BAKE_TEX_HEIGHT* | int | Height. |
  | *BAKE_TEX_PIXELBORDER* | int | Pixel border. |
  | *BAKE_TEX_FILL_COLOR* | [`Vector`](../c4d/Vector/index.md#c4d.Vector) | Fill color. |
  | *BAKE_TEX_UV_LEFT* | float | Left UV coordinate. |
  | *BAKE_TEX_UV_RIGHT* | float | Right UV coordinate. |
  | *BAKE_TEX_UV_TOP* | float | Top UV coordinate. |
  | *BAKE_TEX_UV_BOTTOM* | float | Bottom UV coordinate. |
  | *BAKE_TEX_SUPERSAMPLING* | int | Supersampling. |
  | *BAKE_TEX_USE_BUMP* | bool | Use bump. |
  | *BAKE_TEX_NO_GI* | bool | No GI. |
  | *BAKE_TEX_CONTINUE_UV* | bool | Continue UV. |
  | *BAKE_TEX_USE_PHONG_TAG* | bool | The pixel will be clamped to the current polygon if set to **True** and if the angle between polygons is bigger than their phong angle. Only needed if *BAKE_TEX_CONTINUE_UV* is set to **True**. |
  | *BAKE_TEX_COLORPROFILE* | [`ColorProfile`](../c4d.bitmaps/ColorProfile/index.md#c4d.bitmaps.ColorProfile) | Color profile of the baked texture. |
  | *BAKE_TEX_SHOW_STATUS* | bool | Show status. |
  | *BAKE_TEX_PROGRESS_BITMAP* | bool | Show the bitmap in a preview during baking. |
  | *BAKE_TEX_GENERATE_UNDO* | bool | Generate undo for UVW tags and Vertex tags created by the baker. |
  | *BAKE_TEX_PREVIEW* | bool | Bake texture preview. |
  | *BAKE_TEX_COLOR_ILLUM* | bool | Illumination in color. |
  | *BAKE_TEX_COLOR_SHADOWS* | bool | Shadows in color. |
  | *BAKE_TEX_COLOR_LUMINANCE* | bool | Luminance in color. |
  | *BAKE_TEX_COLOR_DIFFUSION* | bool | Diffusion in color. |
  | *BAKE_TEX_LUMINANCE_DIFFUSION* | bool | Diffusion in luminance. |
  | *BAKE_TEX_ILLUMINATION_SHADOWS* | bool | Shadows in luminance. |
  | *BAKE_TEX_NORMAL_METHOD* | int | Normal method: |
  | *BAKE_TEX_NORMAL_METHOD_OBJECT* |  | Object. |
  | *BAKE_TEX_NORMAL_METHOD_TANGENT* |  | Tangent. |
  | *BAKE_TEX_NORMAL_METHOD_WORLD* |  | World. |
  | *BAKE_TEX_NORMAL_FLIP_X* | bool | Flip X. |
  | *BAKE_TEX_NORMAL_FLIP_Y* | bool | Flip Y. |
  | *BAKE_TEX_NORMAL_FLIP_Z* | bool | Flip Z. |
  | *BAKE_TEX_NORMAL_SWAP_YZ* | bool | Swap Y/Z. |
  | *BAKE_TEX_NORMAL_SOURCE* | link | Normal source. |
  | *BAKE_TEX_NORMAL_USE_RAYCAST* | bool | *New in version R18:* Whether the normal map will be generated using ray casting. True when baking the normal map only. |
  | *BAKE_TEX_SURFACE_ILLUMINATION* | bool | Surface illumination. |
  | *BAKE_TEX_AO_VERTEX_MAP* | bool | Ambient occlusion in vertex map. |
  | *BAKE_TEX_AO_SELFINTERSECTION* | bool | Ambient occlusion self-intersection. |
  | *BAKE_TEX_AO_VERTEXMAPS* | [`BaseContainer`](../c4d/BaseContainer/index.md#c4d.BaseContainer) | A container that stores all new generated vertex maps. |
  | *BAKE_TEX_DISPLACEMENT_SOURCE* | link | The high-res source object. |
  | *BAKE_TEX_DISPLACEMENT_HEIGHT* | float | A float that will receive the displacement height. |
  | *BAKE_TEX_DISPLACEMENT_METHOD* | int | Displacement method: |
  | *BAKE_TEX_DISPLACEMENT_METHOD_OBJECT* |  | Object. |
  | *BAKE_TEX_DISPLACEMENT_METHOD_WORLD* |  | World. |
  | *BAKE_TEX_DISPLACEMENT_METHOD_TANGENT* |  | Tangent. |
  | *BAKE_TEX_DISPLACEMENT_METHOD_INTENSITY* |  | Intensity. |
  | *BAKE_TEX_DISPLACEMENT_METHOD_CENTEREDINTENSITY* |  | Centered intensity. |
  | *BAKE_TEX_DISPLACEMENT_METHOD_REDGREEN* |  | Red <-> Green. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY* | bool | Displacement subpoly. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_SUBDIVISION* | int | Displacement subpoly subdivision. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_ROUND* | bool | Displacement subpoly round. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_ROUNDCONTOUR* | bool | Displacement subpoly round contour. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_HQREMAPPING* | bool | Displacement subpoly HQ remapping. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_MAPRESULT* | bool | Displacement subpoly map result. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_KEEPEDGES* | bool | Displacement subpoly keep edges. |
  | *BAKE_TEX_DISPLACEMENT_SUBPOLY_DISTRIBUTION* | bool | Displacement subpoly distribution. |
  | *BAKE_TEX_RAYCAST_USE_MAX_DISTANCE* | bool | *New in version R18:* Use maximum ray casting distance. |
  | *BAKE_TEX_RAYCAST_CUSTOM_MAX_DISTANCE* | float | *New in version R18:* Custom maximum ray casting distance. |
  | *BAKE_TEX_RAYCAST_USE_AUTO_SPIKE_FILTER_THRESHOLD* | bool | *New in version R18:* Use automatic spike filter threshold. |
  | *BAKE_TEX_RAYCAST_CUSTOM_SPIKE_FILTER_THRESHOLD* | float | *New in version R18:* Custom spike filter threshold. |
  | *BAKE_TEX_OPTIMAL_MAPPING* | int | Optimal mapping: |
  | *BAKE_TEX_OPTIMAL_MAPPING_OFF* |  | Off. |
  | *BAKE_TEX_OPTIMAL_MAPPING_CUBIC* |  | Cubic. |
  | *BAKE_TEX_OPTIMAL_MAPPING_ANGLE* |  | Angle. |
  | *BAKE_TEX_OPTIMAL_MAPPING_PACKED* |  | Packed. |
  | *BAKE_TEX_OPTIMAL_MAPPING_RELAXCOUNT* | int | Optimal mapping relax count. |
  | *BAKE_TEX_OPTIMAL_MAPPING_PREVIEW* | int | Optimal mapping preview. |
  | *BAKE_TEX_NO_INIT_BITMAP* | bool | Set to **True** if the passed [`MultipassBitmap`](../c4d.bitmaps/BaseBitmap/MultipassBitmap/index.md#c4d.bitmaps.MultipassBitmap) is already initialized. |
  | *BAKE_TEX_AUTO_SIZE* | bool | Auto size. |
  | *BAKE_TEX_AUTO_SIZE_MIN* | int | Minimum auto size. |
  | *BAKE_TEX_AUTO_SIZE_MAX* | int | Maximum auto size. |
  | *BAKE_TEX_AUTO_PIXEL_SIZE* | float | Automatic pixel size. |
  | *BAKE_TEX_STATUSBAR* | str | Status bar text. |

- **th** (*Optional*[[*c4d.threading.BaseThread*](../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)]) – The optional thread. Can be **None**. New in version R18.039.

**Return type:** Tuple[[c4d.documents.BaseDocument](../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument), int]

**Returns:**

A tuple with the following information:

[`c4d.documents.BaseDocument`](../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument): The document for the bake to use for the call to [`BakeTexture()`](#c4d.utils.BakeTexture).  
int: The error result. *BAKE_TEX_ERR_NONE* if successful, otherwise one of these errors:

|   |   |
|---|---|
| *BAKE_TEX_ERR_NONE* | None. |
| *BAKE_TEX_ERR_NO_DOC* | No document. |
| *BAKE_TEX_ERR_NO_MEM* | No more memory available. |
| *BAKE_TEX_ERR_NO_RENDER_DOC* | No render document. |
| *BAKE_TEX_ERR_NO_TEXTURE_TAG* | *textag* is **None** or not in *doc*. |
| *BAKE_TEX_ERR_NO_OBJECT* | One of the tags is not assigned to an object or to another object. |
| *BAKE_TEX_ERR_NO_UVW_TAG* | UVW tag is missing. |
| *BAKE_TEX_ERR_TEXTURE_MISSING* | No texture. |
| *BAKE_TEX_ERR_WRONG_BITMAP* | [`MultipassBitmap`](../c4d.bitmaps/BaseBitmap/MultipassBitmap/index.md#c4d.bitmaps.MultipassBitmap) was used, but it has the wrong type or wrong resolution. |
| *BAKE_TEX_ERR_USERBREAK* | User break. |
| *BAKE_TEX_ERR_NO_OPTIMAL_MAPPING* | Optimal mapping failed. |
| *BAKE_TEX_ERR_NO_SOURCE_UVW_TAG* | UVW tag for the source object is missing. |

### Tolerance Checks <a id="c4d.utils-function-Tolerance-Checks"></a>

#### `c4d.utils.CompareFloatTolerant(a, b)` <a id="c4d.utils.CompareFloatTolerant"></a>

Compares if two floats are close to each other on a bit basis (rather than a fixed epsilon).

**Parameters:**

- **a** (*float*) – The first parameter.
- **b** (*float*) – The second parameter.

**Return type:** bool

**Returns:** **True** if *a* and *b* are sufficiently close to each other, otherwise **False**.

#### `c4d.utils.VectorEqual(v1, v2, epsilon=0.01)` <a id="c4d.utils.VectorEqual"></a>

Check if vector v1 and v2 are within *epsilon* of each other.

**Parameters:**

- **v1** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The first vector.
- **v2** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The second vector.
- **epsilon** (*float*) – The epsilon value.

**Return type:** bool

**Returns:** **True** if the vectors are equal.

### Transform Matrices <a id="c4d.utils-function-Transform-Matrices"></a>

#### `c4d.utils.CalculateTranslationScale(src, dst)` <a id="c4d.utils.CalculateTranslationScale"></a>

Calculates the scale between *src* and *dst*.

> **Note:** Both *src* and *dst* have to be of the same type: either [`c4d.documents.BaseDocument`](../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) or [`c4d.UnitScaleData`](../c4d/CustomDataType/UnitScaleData/index.md#c4d.UnitScaleData).

**Parameters:**

- **src** (*Union*[[*c4d.documents.BaseDocument*](../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument), [*c4d.UnitScaleData*](../c4d/CustomDataType/UnitScaleData/index.md#c4d.UnitScaleData)]) – The source document or unit scale data.
- **dst** (*Union*[[*c4d.documents.BaseDocument*](../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument), [*c4d.UnitScaleData*](../c4d/CustomDataType/UnitScaleData/index.md#c4d.UnitScaleData)]) – The destination document or unit scale data.

**Return type:** float

**Returns:** The scale.

#### `c4d.utils.MatrixMove(vec)` <a id="c4d.utils.MatrixMove"></a>

Create a translation matrix.

**Parameters:** **vec** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The translation vector.

**Return type:** [c4d.Matrix](../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The translation matrix.

#### `c4d.utils.MatrixScale(s)` <a id="c4d.utils.MatrixScale"></a>

Create a scaling matrix.

**Parameters:** **s** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The scaling vector for the axes.

**Return type:** [c4d.Matrix](../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The scaling matrix.

### Vector Analysis <a id="c4d.utils-function-Vector-Analysis"></a>

#### `c4d.utils.GetAngle(v1, v2)` <a id="c4d.utils.GetAngle"></a>

Calculates the angle of two vectors.

**Parameters:**

- **v1** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – First position.
- **v2** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – Second position.

**Return type:** float

**Returns:** The angle in radians.

#### `c4d.utils.VectorAngle(vec1, vec2)` <a id="c4d.utils.VectorAngle"></a>

Calculates the angle between two vectors in radians.

**Parameters:**

- **vec1** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The first vector.
- **vec2** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The second vector.

**Return type:** float

**Returns:** The angle in radians.

#### `c4d.utils.VectorGray(vec)` <a id="c4d.utils.VectorGray"></a>

Sum the vector components and multiply by 1/3.

**Parameters:** **vec** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – A color

**Return type:** float

**Returns:** The gray value.

#### `c4d.utils.VectorMax(vec)` <a id="c4d.utils.VectorMax"></a>

Find the maximum component of the vector.

**Parameters:** **vec** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The vector to find the maximum component of.

**Return type:** float

**Returns:** The maximum component of the vector.

#### `c4d.utils.VectorMin(vec)` <a id="c4d.utils.VectorMin"></a>

Find the minimum component of the vector.

**Parameters:** **vec** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – The vector to find the minimum component of.

**Return type:** float

**Returns:** The minimum component of the vector.

#### `c4d.utils.VectorSum(vec)` <a id="c4d.utils.VectorSum"></a>

Sum the vector components.

**Parameters:** **x** ([*c4d.Vector*](../c4d/Vector/index.md#c4d.Vector)) – A color

**Return type:** float

**Returns:** The sum of the components.
