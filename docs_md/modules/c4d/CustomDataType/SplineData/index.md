<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/SplineData/index.html -->

# c4d.SplineData <a id="c4d-splinedata"></a>

## *class* `c4d.SplineData` <a id="c4d.SplineData"></a>

Spline data type (*CUSTOMDATATYPE_SPLINE*) for the [`SplineCustomGui`](../../../c4d.gui/BaseCustomGui/SplineCustomGui/index.md#c4d.gui.SplineCustomGui) GUI

This type is called by value.

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Data Initialization And Transfer**

- [`SplineData.CopyTo()`](#c4d.SplineData.CopyTo): Copies this spline data values into the destination spline data.
- [`SplineData.MakePointBuffer()`](#c4d.SplineData.MakePointBuffer): Makes an uninitialized spline with *lPoints* number of points.

**Deprecated**

- [`SplineData.GetRound()`](#c4d.SplineData.GetRound): This method is only available in R12 and always returns 0.0 in R13.

**Interpolation And Tangents**

- [`SplineData.SetKnot()`](#c4d.SplineData.SetKnot): Sets knot properties.
- [`SplineData.SetRound()`](#c4d.SplineData.SetRound): Set the tension.
- [`SplineData.SetType()`](#c4d.SplineData.SetType): Sets the interpolation type of the selected knots.
- [`SplineData.SetZero()`](#c4d.SplineData.SetZero): Sets the tangents of selected knots to zero.

**Knot Editing**

- [`SplineData.DeleteAllPoints()`](#c4d.SplineData.DeleteAllPoints): Deletes all points.
- [`SplineData.DeleteKnot()`](#c4d.SplineData.DeleteKnot): Deletes a knot.
- [`SplineData.InsertKnot()`](#c4d.SplineData.InsertKnot): Inserts a knot.

**Knot Inspection**

- [`SplineData.GetKnotCount()`](#c4d.SplineData.GetKnotCount): Gets the knot count.
- [`SplineData.GetKnots()`](#c4d.SplineData.GetKnots): Returns all knots.
- [`SplineData.GetPoint()`](#c4d.SplineData.GetPoint): Gets a point from its X coordinate.
- [`SplineData.SortKnots()`](#c4d.SplineData.SortKnots): Sort the knots.

**Magic Methods**

- [`SplineData.__init__()`](#c4d.SplineData.__init__): Creates a default 2 points spline.

**Range Management**

- [`SplineData.AdaptRange()`](#c4d.SplineData.AdaptRange): Adapts the internal 0-1 range of the old spline GUI to the range set by *xmin*, *xmax*, *ymin* and *ymax*.
- [`SplineData.GetRange()`](#c4d.SplineData.GetRange): Gets the range of the spline.
- [`SplineData.SetRange()`](#c4d.SplineData.SetRange): Set the range of the spline.

**Selection And Flags**

- [`SplineData.GetSelectCount()`](#c4d.SplineData.GetSelectCount): Returns the count of knots which are selected.
- [`SplineData.InitDefaultFlag()`](#c4d.SplineData.InitDefaultFlag): Sets the knot flag for selected knots.
- [`SplineData.SelectAll()`](#c4d.SplineData.SelectAll): Selects all points.

**Shape Transformations**

- [`SplineData.Flip()`](#c4d.SplineData.Flip): Flips the spline.
- [`SplineData.Maximum()`](#c4d.SplineData.Maximum): Makes all Y coordinates less than or equal to 1.
- [`SplineData.Minimum()`](#c4d.SplineData.Minimum): Makes all Y coordinates greater than or equal to 0.
- [`SplineData.Mirror()`](#c4d.SplineData.Mirror): Mirrors the spline.

**Spline Generation**

- [`SplineData.MakeAbsCosSpline()`](#c4d.SplineData.MakeAbsCosSpline): Makes an absolute cosinus spline with *lPoints* number of points.
- [`SplineData.MakeCubicSpline()`](#c4d.SplineData.MakeCubicSpline): Makes a cubic spline with *lPoints* number of points.
- [`SplineData.MakeInversSpline()`](#c4d.SplineData.MakeInversSpline): Makes an inverse spline with *lPoints* number of points.
- [`SplineData.MakeLinearSplineBezier()`](#c4d.SplineData.MakeLinearSplineBezier): Makes a linear bezier spline with *lPoints* number of points.
- [`SplineData.MakeLinearSplineLinear()`](#c4d.SplineData.MakeLinearSplineLinear): Makes a linear spline with *lPoints* number of points.
- [`SplineData.MakeRootSpline()`](#c4d.SplineData.MakeRootSpline): Makes a root spline with *lPoints* number of points.
- [`SplineData.MakeSinSpline()`](#c4d.SplineData.MakeSinSpline): Makes a sinus spline with *lPoints* number of points.
- [`SplineData.MakeSquareSpline()`](#c4d.SplineData.MakeSquareSpline): Makes a square spline with *lPoints* number of points.
- [`SplineData.MakeUserSpline()`](#c4d.SplineData.MakeUserSpline): Makes a user spline from *str* with *lPoints* number of points.

## Members <a id="members"></a>

### Data Initialization And Transfer <a id="c4d.SplineData-method-Data-Initialization-And-Transfer"></a>

#### `SplineData.CopyTo(self, pDest)` <a id="c4d.SplineData.CopyTo"></a>

Copies this spline data values into the destination spline data.

*New in version R14.014.*

**Parameters:** **pDest** ([*c4d.SplineData*](#c4d.SplineData)) – The destination spline data.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**

#### `SplineData.MakePointBuffer(self, lPoints=-1)` <a id="c4d.SplineData.MakePointBuffer"></a>

Makes an uninitialized spline with *lPoints* number of points.

**Parameters:** **lPoints** (*int*) – Number of points, or -1 to get the default value.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Deprecated <a id="c4d.SplineData-method-Deprecated"></a>

#### `SplineData.GetRound(self)` <a id="c4d.SplineData.GetRound"></a>

*Deprecated since version Since:* R13

This method is only available in R12 and always returns 0.0 in R13.

Gets the tension.

**Return type:** float

**Returns:** Tension.

### Interpolation And Tangents <a id="c4d.SplineData-method-Interpolation-And-Tangents"></a>

#### `SplineData.SetKnot(self, index, vPos=<_custom_c4d.Vector object at 0x0000012ECC395E60>, lFlagsSettings=0, bSelect=False, vTangentLeft=<_custom_c4d.Vector object at 0x0000012ECC3972A0>, vTangentRight=<_custom_c4d.Vector object at 0x0000012ECC38AE20>, interpol=0)` <a id="c4d.SplineData.SetKnot"></a>

Sets knot properties.

**Parameters:**

- **index** (*int*) – The knot index.

- **vPos** ([*c4d.Vector*](../../Vector/index.md#c4d.Vector)) – The knot position, optional, defaults to *(0,0,0)*.

- **lFlagsSettings** (*int*) –

  The flags for the operation, optional, defaults to *0*:

  |   |   |
  |---|---|
  | *FLAG_KNOT_T_BREAK* | Break knot tangents. |
  | *FLAG_KNOT_LOCK_X* | Lock knot’s X movement. |
  | *FLAG_KNOT_LOCK_Y* | Lock knot’s Y movement. |
  | *FLAG_KNOT_T_LOCK_A* | Lock knot’s tangent angle. |
  | *FLAG_KNOT_T_LOCK_L* | Lock knot’s tangent length. |
  | *FLAG_KNOT_T_KEEPVISUALANGLE* | Keep visual angle between knot’s tangents. |
  | *ADD_KNOT_ADAPT_TANGENTS* | Tangents of new knots are set in such a way that the resulting spline will match the curvature of the original spline. |

  > **Note:** Also contains the point index ID. The ID can be accessed using these functions:

  ```python
  def SplineKnotGetID(flags):
      return ((flags >> 16) & 0x0000ffff)

  def SplineKnotSetID(flags, flag_id):
      flags = (flags & 65535) | ((flag_id & 0x0000ffff) << 16)
  ```

  > **Important:** This means that the flags must only be accessed using **‘|=’** and **‘&=’** (a good advice for any set of flags, for maximum forward compatibility).

- **bSelect** (*bool*) – Internal select state. Do not change this.

- **vTangentLeft** ([*c4d.Vector*](../../Vector/index.md#c4d.Vector)) – The left tangent for the knot, optional, defaults to *(0,0,0)*.

- **vTangentRight** ([*c4d.Vector*](../../Vector/index.md#c4d.Vector)) – The right tangent for the knot, optional, defaults to *(0,0,0)*.

- **interpol** (*int*) –

  The interpolation type, optional, defaults to *CustomSplineKnotInterpolationBezier*:

  |   |   |
  |---|---|
  | *CustomSplineKnotInterpolationBezier* | Bezier interpolation. |
  | *CustomSplineKnotInterpolationLinear* | Linear interpolation. |
  | *CustomSplineKnotInterpolationCubic* | Cubic interpolation. |

**Raises:** **RangeError** – If the knot *index* is out of range : *0<=index<*[`GetKnotCount()`](#c4d.SplineData.GetKnotCount).

#### `SplineData.SetRound(self, r)` <a id="c4d.SplineData.SetRound"></a>

Set the tension.

**Parameters:** **r** (*float*) – The tension

#### `SplineData.SetType(self, id, bAll)` <a id="c4d.SplineData.SetType"></a>

Sets the interpolation type of the selected knots.

**Parameters:**

- **id** – The interpolation type.
- **bAll** (*bool*) – Pass **True** to set all knots, **False** to set selected knots only.

**Returns:** **True** if successful, otherwise **False**.

**Return type:** bool

#### `SplineData.SetZero(self, bY, bAll)` <a id="c4d.SplineData.SetZero"></a>

Sets the tangents of selected knots to zero.

**Parameters:**

- **bY** (*bool*) – **True** to set the tangets’ Y coordinate to zero, **False** to set the X coordinate.
- **bAll** (*bool*) – **True** to set all tangents, **False** to set the tangents of selected knots only.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Knot Editing <a id="c4d.SplineData-method-Knot-Editing"></a>

#### `SplineData.DeleteAllPoints(self)` <a id="c4d.SplineData.DeleteAllPoints"></a>

Deletes all points.

#### `SplineData.DeleteKnot(self, a)` <a id="c4d.SplineData.DeleteKnot"></a>

Deletes a knot.

**Parameters:** **a** (*int*) – The knot index to delete.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SplineData.InsertKnot(self, x, y, flags=0)` <a id="c4d.SplineData.InsertKnot"></a>

Inserts a knot.

**Parameters:**

- **x** (*float*) – X coordinate

- **y** (*float*) – Y coordinate

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *FLAG_KNOT_T_BREAK* | Break knot tangents. |
  | *FLAG_KNOT_LOCK_X* | Lock knot’s X movement. |
  | *FLAG_KNOT_LOCK_Y* | Lock knot’s Y movement. |
  | *FLAG_KNOT_T_LOCK_A* | Lock knot’s tangent angle. |
  | *FLAG_KNOT_T_LOCK_L* | Lock knot’s tangent length. |
  | *FLAG_KNOT_T_KEEPVISUALANGLE* | Keep visual angle between knot’s tangents. |
  | *ADD_KNOT_ADAPT_TANGENTS* | Tangents of new knots are set in such a way that the resulting spline will match the curvature of the original spline. |

**Return type:** int

**Returns:** Knot index.

### Knot Inspection <a id="c4d.SplineData-method-Knot-Inspection"></a>

#### `SplineData.GetKnotCount(self)` <a id="c4d.SplineData.GetKnotCount"></a>

Gets the knot count.

**Return type:** int

**Returns:** Knot count.

#### `SplineData.GetKnots(self)` <a id="c4d.SplineData.GetKnots"></a>

Returns all knots.

**Return type:** List[Dict[**vPos**: [`Vector`](../../Vector/index.md#c4d.Vector), **lFlagsSettings**: int, **bSelect**: bool, **vTangentLeft**: [`Vector`](../../Vector/index.md#c4d.Vector), **vTangentRight**: [`Vector`](../../Vector/index.md#c4d.Vector), **interpol**: int]]

**Returns:** A list of dictionaries with information about the knot.

#### `SplineData.GetPoint(self, r)` <a id="c4d.SplineData.GetPoint"></a>

Gets a point from its X coordinate.

**Parameters:** **r** (*float*) – The x position

**Return type:** [c4d.Vector](../../Vector/index.md#c4d.Vector)

**Returns:** The position

#### `SplineData.SortKnots(self)` <a id="c4d.SplineData.SortKnots"></a>

Sort the knots.

**Return type:** int

**Returns:** The new index of the active knot.

### Magic Methods <a id="c4d.SplineData-method-Magic-Methods"></a>

#### `SplineData.__init__(self, v=None)` <a id="c4d.SplineData.__init__"></a>

Creates a default 2 points spline.

**Parameters:** **v** (*Optional*[[*c4d.SplineData*](#c4d.SplineData)]) – Source spline data for copy constructor.

### Range Management <a id="c4d.SplineData-method-Range-Management"></a>

#### `SplineData.AdaptRange(self, xmin, xmax, xsteps, ymin, ymax, ysteps)` <a id="c4d.SplineData.AdaptRange"></a>

Adapts the internal 0-1 range of the old spline GUI to the range set by *xmin*, *xmax*, *ymin* and *ymax*.

**Parameters:**

- **xmin** (*float*) – The new X minimum.
- **xmax** (*float*) – The new X maximum.
- **xsteps** (*float*) – The new X step size.
- **ymin** (*float*) – The new Y minimum.
- **ymax** (*float*) – The new Y maximum.
- **ysteps** (*float*) – The new Y step size.

#### `SplineData.GetRange(self)` <a id="c4d.SplineData.GetRange"></a>

Gets the range of the spline.

```python
def PrintRange(sd):
    sdrange = sd.GetRange()
    if not range: return

    print(sdrange["xmin"], sdrange["xmax"], sdrange["xstep"], sdrange["ymin"], sdrange["ymax"], sdrange["ystep"])
```

**Return type:** Optional[Dict[**xmin**: float, **xmax**: float, **xstep**: float, **ymin**: float, **ymax**: float, **ystep**: float]]

**Returns:** The range dictionary or **None**.

#### `SplineData.SetRange(self, xmin, xmax, xsteps, ymin, ymax, ysteps)` <a id="c4d.SplineData.SetRange"></a>

Set the range of the spline.

**Parameters:**

- **xmin** (*float*) – The X min range.
- **xmax** (*float*) – The X max range.
- **xsteps** (*float*) – The X steps.
- **ymin** (*float*) – The Y min range.
- **ymax** (*float*) – The Y max range.
- **ysteps** (*float*) – The Y steps.

### Selection And Flags <a id="c4d.SplineData-method-Selection-And-Flags"></a>

#### `SplineData.GetSelectCount(self)` <a id="c4d.SplineData.GetSelectCount"></a>

Returns the count of knots which are selected.

**Return type:** int

**Returns:** The count

#### `SplineData.InitDefaultFlag(self, flag)` <a id="c4d.SplineData.InitDefaultFlag"></a>

Sets the knot flag for selected knots.

**Parameters:**

**flag** (*int*) –

A combination of these flags:

|   |   |
|---|---|
| *FLAG_KNOT_T_BREAK* | Break knot tangents. |
| *FLAG_KNOT_LOCK_X* | Lock knot’s X movement. |
| *FLAG_KNOT_LOCK_Y* | Lock knot’s Y movement. |
| *FLAG_KNOT_T_LOCK_A* | Lock knot’s tangent angle. |
| *FLAG_KNOT_T_LOCK_L* | Lock knot’s tangent length. |
| *FLAG_KNOT_T_KEEPVISUALANGLE* | Keep visual angle between knot’s tangents. |
| *ADD_KNOT_ADAPT_TANGENTS* | Tangents of new knots are set in such a way that the resulting spline will match the curvature of the original spline. |

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SplineData.SelectAll(self)` <a id="c4d.SplineData.SelectAll"></a>

Selects all points.

### Shape Transformations <a id="c4d.SplineData-method-Shape-Transformations"></a>

#### `SplineData.Flip(self)` <a id="c4d.SplineData.Flip"></a>

Flips the spline.

#### `SplineData.Maximum(self)` <a id="c4d.SplineData.Maximum"></a>

Makes all Y coordinates less than or equal to 1.

#### `SplineData.Minimum(self)` <a id="c4d.SplineData.Minimum"></a>

Makes all Y coordinates greater than or equal to 0.

#### `SplineData.Mirror(self)` <a id="c4d.SplineData.Mirror"></a>

Mirrors the spline.

### Spline Generation <a id="c4d.SplineData-method-Spline-Generation"></a>

#### `SplineData.MakeAbsCosSpline(self, lPoints=-1)` <a id="c4d.SplineData.MakeAbsCosSpline"></a>

Makes an absolute cosinus spline with *lPoints* number of points.

**Parameters:** **lPoints** (*int*) – Number of points, or -1 to get the default value.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SplineData.MakeCubicSpline(self, lPoints=-1)` <a id="c4d.SplineData.MakeCubicSpline"></a>

Makes a cubic spline with *lPoints* number of points.

**Parameters:** **lPoints** (*int*) – Number of points, or -1 to get the default value.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SplineData.MakeInversSpline(self, lPoints=-1)` <a id="c4d.SplineData.MakeInversSpline"></a>

Makes an inverse spline with *lPoints* number of points.

**Parameters:** **lPoints** (*int*) – Number of points, or -1 to get the default value.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SplineData.MakeLinearSplineBezier(self, lPoints=-1)` <a id="c4d.SplineData.MakeLinearSplineBezier"></a>

Makes a linear bezier spline with *lPoints* number of points.

**Parameters:** **lPoints** (*int*) – Number of points, or -1 to get the default value.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SplineData.MakeLinearSplineLinear(self, lPoints=-1)` <a id="c4d.SplineData.MakeLinearSplineLinear"></a>

Makes a linear spline with *lPoints* number of points.

**Parameters:** **lPoints** (*int*) – Number of points, or -1 to get the default value.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SplineData.MakeRootSpline(self, lPoints=-1)` <a id="c4d.SplineData.MakeRootSpline"></a>

Makes a root spline with *lPoints* number of points.

**Parameters:** **lPoints** (*int*) – Number of points, or -1 to get the default value.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SplineData.MakeSinSpline(self, lPoints=-1)` <a id="c4d.SplineData.MakeSinSpline"></a>

Makes a sinus spline with *lPoints* number of points.

**Parameters:** **lPoints** (*int*) – Number of points, or -1 to get the default value.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SplineData.MakeSquareSpline(self, lPoints=-1)` <a id="c4d.SplineData.MakeSquareSpline"></a>

Makes a square spline with *lPoints* number of points.

**Parameters:** **lPoints** (*int*) – Number of points, or -1 to get the default value.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SplineData.MakeUserSpline(self, str, lPoints)` <a id="c4d.SplineData.MakeUserSpline"></a>

Makes a user spline from *str* with *lPoints* number of points.

**Parameters:**

- **str** (*str*) – User spline string. Any valid formula can be used.
- **lPoints** (*int*) – Number of points, or -1 to get the default value.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.
