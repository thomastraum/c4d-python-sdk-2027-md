<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/SplineObject/index.html -->

# c4d.SplineObject <a id="c4d-splineobject"></a>

## *class* `c4d.SplineObject` <a id="c4d.SplineObject"></a>

Cinema 4D gives you a generous number of predefined curves.  
Add to this the possibility to convert vector based artwork files from other programs and to add graphic characters and you have a large number of spline primitives at your fingertips.  
All of these spline primitives are parameterized.  
This means that the spline is merely the graphical representation of a mathematical formula built controlled by parameters you can edit the Attribute Manager.

The instance object class of type *Ospline*.

> **See also:** [`SplineHelp`](../../../../../../../c4d.utils/SplineHelp/index.md#c4d.utils.SplineHelp) [`SplineLengthData`](../../../../../../../c4d.utils/SplineLengthData/index.md#c4d.utils.SplineLengthData)

Parent Class:

- [`c4d.PointObject`](../index.md#c4d.PointObject)

> **See also:** [Spline Types](../../../../../../../../types/spline.md).

## Overview <a id="overview"></a>

**Curve Evaluation**

- [`SplineObject.GetSplinePoint()`](#c4d.SplineObject.GetSplinePoint): Get the spline point at a position along the given segment.
- [`SplineObject.GetSplineTangent()`](#c4d.SplineObject.GetSplineTangent): Get the spline tangent at a position along the given segment.

**Magic Methods**

- [`SplineObject.__init__()`](#c4d.SplineObject.__init__)

**Segment Structure**

- [`SplineObject.GetSegment()`](#c4d.SplineObject.GetSegment): Returns information about the segment.
- [`SplineObject.GetSegmentCount()`](#c4d.SplineObject.GetSegmentCount): Returns the count of segments.
- [`SplineObject.ResizeObject()`](#c4d.SplineObject.ResizeObject): Change the number of segments and points for this spline.
- [`SplineObject.SetSegment()`](#c4d.SplineObject.SetSegment): Set properties of the segment.

**Spline Configuration**

- [`SplineObject.GetInterpolationType()`](#c4d.SplineObject.GetInterpolationType): Get the type of spline.
- [`SplineObject.IsClosed()`](#c4d.SplineObject.IsClosed): Checks if spline is closed.
- [`SplineObject.SetDefaultCoeff()`](#c4d.SplineObject.SetDefaultCoeff): Initialise the spline with default coefficients.

**Tangent Data**

- [`SplineObject.GetTangent()`](#c4d.SplineObject.GetTangent): Return a tangent.
- [`SplineObject.GetTangentCount()`](#c4d.SplineObject.GetTangentCount): Returns the count of tangents.
- [`SplineObject.SetTangent()`](#c4d.SplineObject.SetTangent): Set a tangent.

## Members <a id="members"></a>

### Curve Evaluation <a id="c4d.SplineObject-method-Curve-Evaluation"></a>

#### `SplineObject.GetSplinePoint(self, t, segment=0)` <a id="c4d.SplineObject.GetSplinePoint"></a>

Get the spline point at a position along the given segment.

**Parameters:**

- **t** (*float*) – The position *0.0<=t<=1.0* along the segment.
- **segment** (*int*) – The segment.

**Raises:** **IndexError** – If the *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.SplineObject.GetSegmentCount).

**Return type:** [c4d.Vector](../../../../../../Vector/index.md#c4d.Vector)

**Returns:** The spline point.

#### `SplineObject.GetSplineTangent(self, t, segment=0)` <a id="c4d.SplineObject.GetSplineTangent"></a>

Get the spline tangent at a position along the given segment.

**Parameters:**

- **t** (*float*) – The position *0.0<=t<=1.0* along the segment.
- **segment** (*int*) – The segment to get the point in.

**Raises:** **IndexError** – If the *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.SplineObject.GetSegmentCount).

**Return type:** [c4d.Vector](../../../../../../Vector/index.md#c4d.Vector)

**Returns:** The spline point.

### Magic Methods <a id="c4d.SplineObject-method-Magic-Methods"></a>

#### `SplineObject.__init__(self, pcnt, type)` <a id="c4d.SplineObject.__init__"></a>

**Parameters:**

- **pcnt** (*int*) – Point count.

- **type** (*int*) –

  Spline type. Check out [Spline Types](../../../../../../../../types/spline.md#spline-type).

  |   |   |
  |---|---|
  | *SPLINETYPE_LINEAR* | Linear. |
  | *SPLINETYPE_CUBIC* | Cubic. |
  | *SPLINETYPE_AKIMA* | Akima. |
  | *SPLINETYPE_BSPLINE* | B-Spline. |
  | *SPLINETYPE_BEZIER* | Bezier. |

### Segment Structure <a id="c4d.SplineObject-method-Segment-Structure"></a>

#### `SplineObject.GetSegment(self, id)` <a id="c4d.SplineObject.GetSegment"></a>

Returns information about the segment.

```python
>>> op.GetSegment(0)
{'closed': True, 'cnt': 4}
```

**Parameters:** **id** (*int*) – The segment.

**Raises:** **IndexError** – If the segment index *id* is out of range : *0<=id<*[`GetSegmentCount()`](#c4d.SplineObject.GetSegmentCount).

**Return type:** dict{**cnt**: int, **closed**: bool}

**Returns:** The segment.

#### `SplineObject.GetSegmentCount(self)` <a id="c4d.SplineObject.GetSegmentCount"></a>

Returns the count of segments.

**Return type:** int

**Returns:** The count.

#### `SplineObject.ResizeObject(self, pcnt, scnt=-1)` <a id="c4d.SplineObject.ResizeObject"></a>

Change the number of segments and points for this spline.  
If *scnt* is -1 or not set, the method `PointObject.ResizeObject()` of [`PointObject`](../index.md#c4d.PointObject) is used.

**Parameters:**

- **pcnt** (*int*) – The new point count.
- **scnt** (*int*) – The new segment count.

**Return type:** bool

**Returns:** Success of changing the number of points and segments.

#### `SplineObject.SetSegment(self, id, cnt, closed)` <a id="c4d.SplineObject.SetSegment"></a>

Set properties of the segment.

**Parameters:**

- **id** (*int*) – The segment
- **cnt** (*int*) – The count of points.
- **closed** (*bool*) – **True** if the segment is closed.

**Raises:** **IndexError** – If the *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.SplineObject.GetSegmentCount).

### Spline Configuration <a id="c4d.SplineObject-method-Spline-Configuration"></a>

#### `SplineObject.GetInterpolationType(self)` <a id="c4d.SplineObject.GetInterpolationType"></a>

Get the type of spline.

**Return type:** int

**Returns:**

The type of spline. Check out [Spline Types](../../../../../../../../types/spline.md#spline-type).

|   |   |
|---|---|
| *SPLINETYPE_LINEAR* | Linear. |
| *SPLINETYPE_CUBIC* | Cubic. |
| *SPLINETYPE_AKIMA* | Akima. |
| *SPLINETYPE_BSPLINE* | B-Spline. |
| *SPLINETYPE_BEZIER* | Bezier. |

#### `SplineObject.IsClosed(self)` <a id="c4d.SplineObject.IsClosed"></a>

Checks if spline is closed.

**Return type:** bool

**Returns:** **True** if the spline is closed.

#### `SplineObject.SetDefaultCoeff(self)` <a id="c4d.SplineObject.SetDefaultCoeff"></a>

Initialise the spline with default coefficients.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Tangent Data <a id="c4d.SplineObject-method-Tangent-Data"></a>

#### `SplineObject.GetTangent(self, id)` <a id="c4d.SplineObject.GetTangent"></a>

Return a tangent.

```python
>>> data = op.GetTangent(0)
>>> data
{'vl': Vector(0, -83, 0), 'vr': Vector(0, 83, 0)}
```

**Parameters:** **id** (*int*) – The tangent index.

**Raises:** **IndexError** – If the tangent index *id* is out of range : *0<=segment<*[`GetTangentCount()`](#c4d.SplineObject.GetTangentCount).

**Return type:** dict{**vl**: [`Vector`](../../../../../../Vector/index.md#c4d.Vector), **vr**: [`Vector`](../../../../../../Vector/index.md#c4d.Vector)}

**Returns:** Left and right part that defines the tangent.

#### `SplineObject.GetTangentCount(self)` <a id="c4d.SplineObject.GetTangentCount"></a>

Returns the count of tangents.

**Return type:** int

**Returns:** The count.

#### `SplineObject.SetTangent(self, id, vl, vr)` <a id="c4d.SplineObject.SetTangent"></a>

Set a tangent.

```python
>>> # This is a continuation of the GetTangent() example.
>>> op.SetTangent(2, data["vl"], data["vr"])
```

**Parameters:**

- **id** (*int*) – The tangent index.
- **vl** ([*c4d.Vector*](../../../../../../Vector/index.md#c4d.Vector)) – The left tangent.
- **vr** ([*c4d.Vector*](../../../../../../Vector/index.md#c4d.Vector)) – The right tangent.

**Raises:** **IndexError** – If the tangent index *id* is out of range.
