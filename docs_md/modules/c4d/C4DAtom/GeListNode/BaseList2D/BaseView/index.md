<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseView/index.html -->

# c4d.BaseView <a id="c4d-baseview"></a>

## *class* `c4d.BaseView` <a id="c4d.BaseView"></a>

BaseView represents an editor view.  
In most cases the sub-class BaseDraw is used. It adds functions for drawing into the view.

See the `dbasedraw.h` description file for container IDs.

> **Warning:** This type cannot be instantiated.

Parent Class:

- [`c4d.BaseList2D`](../index.md#c4d.BaseList2D)

Child Class:

- [`c4d.BaseDraw`](BaseDraw/index.md#c4d.BaseDraw)

## Overview <a id="overview"></a>

**Camera Matrices**

- [`BaseView.GetBaseMatrix()`](#c4d.BaseView.GetBaseMatrix): Gets the base matrix.
- [`BaseView.GetMg()`](#c4d.BaseView.GetMg): Returns the camera matrix, i.e.
- [`BaseView.GetMi()`](#c4d.BaseView.GetMi): Returns the inverse of the camera matrix.
- [`BaseView.SetBaseMatrix()`](#c4d.BaseView.SetBaseMatrix): Sets the base matrix.

**Clipping Boundaries**

- [`BaseView.ZSensitiveFar()`](#c4d.BaseView.ZSensitiveFar): Indicates if the view has Z far clipping.
- [`BaseView.ZSensitiveFarClipping()`](#c4d.BaseView.ZSensitiveFarClipping): Returns the far clipping of Z sensitive view.
- [`BaseView.ZSensitiveNear()`](#c4d.BaseView.ZSensitiveNear): Indicates if the view has Z near clipping.
- [`BaseView.ZSensitiveNearClipping()`](#c4d.BaseView.ZSensitiveNearClipping): Returns the near clipping of Z sensitive view.

**Coordinate Conversion**

- [`BaseView.CS()`](#c4d.BaseView.CS): Camera to screen conversion.
- [`BaseView.CW()`](#c4d.BaseView.CW): Camera to world conversion.
- [`BaseView.CW_V()`](#c4d.BaseView.CW_V): Camera to world vector conversion.
- [`BaseView.SC()`](#c4d.BaseView.SC): Screen to camera conversion.
- [`BaseView.SW()`](#c4d.BaseView.SW): Screen to world conversion.
- [`BaseView.WC()`](#c4d.BaseView.WC): World to camera conversion.
- [`BaseView.WC_V()`](#c4d.BaseView.WC_V): World to camera vector conversion.
- [`BaseView.WS()`](#c4d.BaseView.WS): World to screen conversion.

**Geometric Projection**

- [`BaseView.ProjectPointOnLine()`](#c4d.BaseView.ProjectPointOnLine): Calculates the nearest point on the line defined by *p* and *v* for a given mouse coordinate.
- [`BaseView.ProjectPointOnPlane()`](#c4d.BaseView.ProjectPointOnPlane): Calculates the nearest point on the plane defined by *p* and *v* for a given mouse coordinate.

**Pixel Scaling**

- [`BaseView.PW_S()`](#c4d.BaseView.PW_S): Returns the size in world units for a single pixel at the given Z-depth *z*.
- [`BaseView.PW_W()`](#c4d.BaseView.PW_W): Returns the size in world units for a single pixel at screen space vector *p*.
- [`BaseView.WP_S()`](#c4d.BaseView.WP_S): Returns the size in pixels for a single world unit at the given Z-depth *z*.
- [`BaseView.WP_W()`](#c4d.BaseView.WP_W): Returns the size in screen space pixels for a single world unit at world position *p*.

**Planar Orientation**

- [`BaseView.GetPlanarRotation()`](#c4d.BaseView.GetPlanarRotation): Gets the rotation of the planar views.
- [`BaseView.SetPlanarRotation()`](#c4d.BaseView.SetPlanarRotation): Sets the rotation of the planar views.

**Projection Settings**

- [`BaseView.GetProjection()`](#c4d.BaseView.GetProjection): Returns the projection used by the view.
- [`BaseView.GetViewParameter()`](#c4d.BaseView.GetViewParameter): Retrieves the parameters for the current projection.

**View Dimensions**

- [`BaseView.GetFrame()`](#c4d.BaseView.GetFrame): The dimension in pixels of the view window.
- [`BaseView.GetSafeFrame()`](#c4d.BaseView.GetSafeFrame): The dimension in pixels of the render lines.

**Visibility Testing**

- [`BaseView.BackfaceCulling()`](#c4d.BaseView.BackfaceCulling): Tests the face with center *p* and normal *n* for backface culling.
- [`BaseView.TestClipping3D()`](#c4d.BaseView.TestClipping3D): Tests if a bounding box is visible in the view according to the current projection.
- [`BaseView.TestPoint()`](#c4d.BaseView.TestPoint): Returns **True** if the point is within the boundary returned by `GetFrame()`.
- [`BaseView.TestPointZ()`](#c4d.BaseView.TestPointZ): Tests if the point is visible in the view according to the current projection.

## Members <a id="members"></a>

### Camera Matrices <a id="c4d.BaseView-method-Camera-Matrices"></a>

#### `BaseView.GetBaseMatrix(self)` <a id="c4d.BaseView.GetBaseMatrix"></a>

Gets the base matrix.

*New in version R14.014.*

> **Note:** The base matrix is multiplied with the camera matrix so that it is possible to have e.g. a frontal view into another direction than +Z.

**Return type:** [c4d.Matrix](../../../../Matrix/index.md#c4d.Matrix)

**Returns:** The base matrix.

#### `BaseView.GetMg(self)` <a id="c4d.BaseView.GetMg"></a>

Returns the camera matrix, i.e. the global object matrix of the current camera object.

**Return type:** [c4d.Matrix](../../../../Matrix/index.md#c4d.Matrix)

**Returns:** The camera matrix.

#### `BaseView.GetMi(self)` <a id="c4d.BaseView.GetMi"></a>

Returns the inverse of the camera matrix.

Equivalent to [`GetMg()`](#c4d.BaseView.GetMg), but faster.

**Return type:** [c4d.Matrix](../../../../Matrix/index.md#c4d.Matrix)

**Returns:** The inverted camera matrix.

#### `BaseView.SetBaseMatrix(self, mg)` <a id="c4d.BaseView.SetBaseMatrix"></a>

Sets the base matrix.

*New in version R14.014.*

> **Note:** The base matrix is multiplied with the camera matrix so that it is possible to have e.g. a frontal view into another direction than +Z.

**Parameters:** **mg** ([*c4d.Matrix*](../../../../Matrix/index.md#c4d.Matrix)) – The new base matrix.

### Clipping Boundaries <a id="c4d.BaseView-method-Clipping-Boundaries"></a>

#### `BaseView.ZSensitiveFar(self)` <a id="c4d.BaseView.ZSensitiveFar"></a>

Indicates if the view has Z far clipping.

**Return type:** bool

**Returns:** **True** if the view has Z clipping far, otherwise **False**.

#### `BaseView.ZSensitiveFarClipping(self)` <a id="c4d.BaseView.ZSensitiveFarClipping"></a>

Returns the far clipping of Z sensitive view.

**Return type:** float

**Returns:** Far clipping distance.

#### `BaseView.ZSensitiveNear(self)` <a id="c4d.BaseView.ZSensitiveNear"></a>

Indicates if the view has Z near clipping.

**Return type:** bool

**Returns:** **True** if the view has Z clipping near, otherwise **False**.

#### `BaseView.ZSensitiveNearClipping(self)` <a id="c4d.BaseView.ZSensitiveNearClipping"></a>

Returns the near clipping of Z sensitive view.

### Coordinate Conversion <a id="c4d.BaseView-method-Coordinate-Conversion"></a>

#### `BaseView.CS(self, p, z_inverse)` <a id="c4d.BaseView.CS"></a>

Camera to screen conversion.  
Converts *p* from camera space to screen space (pixels relative to the view) and returns the result.

**Parameters:**

- **p** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – A point in camera space.

- **z_inverse** (*bool*) –

  If **True** the Z coordinate of the converted point is inverted.  
  This is used by the Z-buffer.

**Return type:** [c4d.Vector](../../../../Vector/index.md#c4d.Vector)

**Returns:** A point in screen space.

#### `BaseView.CW(self, p)` <a id="c4d.BaseView.CW"></a>

Camera to world conversion.  
Converts *p* from camera space to world space and returns the result.

**Parameters:** **p** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – A point in camera space.

**Return type:** [c4d.Vector](../../../../Vector/index.md#c4d.Vector)

**Returns:** The point in world space.

#### `BaseView.CW_V(self, v)` <a id="c4d.BaseView.CW_V"></a>

Camera to world vector conversion.  
Converts the camera vector *v* to world space and returns the result.

**Parameters:** **v** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – A vector in camera space.

**Return type:** [c4d.Vector](../../../../Vector/index.md#c4d.Vector)

**Returns:** The vector in world space.

#### `BaseView.SC(self, p)` <a id="c4d.BaseView.SC"></a>

Screen to camera conversion.  
Converts *p* from screen space (pixels relative to the view) to camera space and returns the result.  
The X and Y coordinates of the point are given in screen space; the Z coordinate is the orthogonal distance in world units to the point from the view plane.

**Parameters:** **p** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – A point in screen space.

**Return type:** [c4d.Vector](../../../../Vector/index.md#c4d.Vector)

**Returns:** The point in camera space.

#### `BaseView.SW(self, p)` <a id="c4d.BaseView.SW"></a>

Screen to world conversion.  
Converts *p* from screen space (pixels relative to the view) to world space.  
The X and Y coordinates of the point are given in screen space; the Z coordinate is the orthogonal distance in world units to the point from the view plane. The result of the conversion is returned.

**Parameters:** **p** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – A point in screenspace.

**Return type:** [c4d.Vector](../../../../Vector/index.md#c4d.Vector)

**Returns:** The point in worldspace.

#### `BaseView.WC(self, p)` <a id="c4d.BaseView.WC"></a>

World to camera conversion.  
Converts *p* from world space to camera space and returns the result.

**Parameters:** **p** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – A point in world space.

**Return type:** [c4d.Vector](../../../../Vector/index.md#c4d.Vector)

**Returns:** The point in camera space.

#### `BaseView.WC_V(self, v)` <a id="c4d.BaseView.WC_V"></a>

World to camera vector conversion.  
Converts the world vector *v* to camera space and returns the result.

**Parameters:** **v** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – A vector in world space.

**Return type:** [c4d.Vector](../../../../Vector/index.md#c4d.Vector)

**Returns:** The vector in camera space.

#### `BaseView.WS(self, p)` <a id="c4d.BaseView.WS"></a>

World to screen conversion.  
Converts *p* from world space to screen space (pixels relative to the view), and returns the conversion.  
The orthogonal distance to the world point is stored in world units in the Z axis of the result.

**Parameters:** **p** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – A point in world space.

**Return type:** [c4d.Vector](../../../../Vector/index.md#c4d.Vector)

**Returns:** The point in screen space.

### Geometric Projection <a id="c4d.BaseView-method-Geometric-Projection"></a>

#### `BaseView.ProjectPointOnLine(self, p, v, mouse_x, mouse_y)` <a id="c4d.BaseView.ProjectPointOnLine"></a>

Calculates the nearest point on the line defined by *p* and *v* for a given mouse coordinate.

**Parameters:**

- **p** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – Start position of the line in world space.
- **v** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – Direction of the line. The length of this vector determines the scaling of the returned offset.
- **mouse_x** (*float*) – Mouse X-coordinate.
- **mouse_y** (*float*) – Mouse Y-coordinate.

**Return type:** Tuple[[c4d.Vector](../../../../Vector/index.md#c4d.Vector), float, int]

**Returns:**

The *nearest point* on the line, the *distance* from *p* scaled by the length of *v* (*offset* = distance to p / length of v) and an *error code*:

- 1 = Failed to find nearest point correctly, lines may be beyond horizon, behind camera, or ray line and line may be parallel.
- 2 = Point is either beyond the start or end of the described segment (but a point will still be returned for the line/ray).

#### `BaseView.ProjectPointOnPlane(self, p, v, mouse_x, mouse_y)` <a id="c4d.BaseView.ProjectPointOnPlane"></a>

Calculates the nearest point on the plane defined by *p* and *v* for a given mouse coordinate.

**Parameters:**

- **p** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – The plane’s position in world space.
- **v** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – The plane’s normal in world space.
- **mouse_x** (*float*) – Mouse X-coordinate.
- **mouse_y** (*float*) – Mouse Y-coordinate.

**Return type:** Tuple[[c4d.Vector](../../../../Vector/index.md#c4d.Vector), int]

**Returns:**

The *nearest point* on the plane and an *error code*:

- 1 = Failed to find nearest point correctly, lines may be beyond horizon, behind camera, or ray line and line may be parallel.
- 2 = Point is either beyond the start or end of the described segment (but a point will still be returned for the line/ray).

### Pixel Scaling <a id="c4d.BaseView-method-Pixel-Scaling"></a>

#### `BaseView.PW_S(self, z, horizontal)` <a id="c4d.BaseView.PW_S"></a>

Returns the size in world units for a single pixel at the given Z-depth *z*.

**Parameters:**

- **z** (*float*) – The Z-depth.

- **horizontal** (*bool*) –

  **True** if the size is measured horizontally, **False** for vertical measurement.  
  This is useful for non-square pixel aspect ratios.

**Return type:** float

**Returns:** The size in world units.

#### `BaseView.PW_W(self, p, horizontal)` <a id="c4d.BaseView.PW_W"></a>

Returns the size in world units for a single pixel at screen space vector *p*.

**Parameters:**

- **p** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – The pixel in screen space.

- **horizontal** (*bool*) –

  **True** if the size is measured horizontally, **False** for vertical measurement.  
  This is useful for non-square pixel aspect ratios.

**Return type:** float

**Returns:** Size in world units.

#### `BaseView.WP_S(self, z, horizontal)` <a id="c4d.BaseView.WP_S"></a>

Returns the size in pixels for a single world unit at the given Z-depth *z*.

**Parameters:**

- **z** (*float*) – The Z-depth.

- **horizontal** (*bool*) –

  **True** if the size is measured horizontally, **False** for vertical measurement.  
  This is useful for non-square pixel aspect ratios.

**Return type:** float

**Returns:** The size in pixels.

#### `BaseView.WP_W(self, p, horizontal)` <a id="c4d.BaseView.WP_W"></a>

Returns the size in screen space pixels for a single world unit at world position *p*.

**Parameters:**

- **p** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – The world unit in world space.

- **horizontal** (*bool*) –

  **True** if the size is measured horizontally, **False** for vertical measurement.  
  This is useful for non-square pixel aspect ratios.

**Return type:** float

**Returns:** Size in screen space pixels.

### Planar Orientation <a id="c4d.BaseView-method-Planar-Orientation"></a>

#### `BaseView.GetPlanarRotation(self)` <a id="c4d.BaseView.GetPlanarRotation"></a>

Gets the rotation of the planar views.

*New in version R14.014.*

**Return type:** float

**Returns:** The planar rotation.

#### `BaseView.SetPlanarRotation(self, r)` <a id="c4d.BaseView.SetPlanarRotation"></a>

Sets the rotation of the planar views.

*New in version R14.014.*

**Parameters:** **mg** (*float*) – The new planar rotation.

### Projection Settings <a id="c4d.BaseView-method-Projection-Settings"></a>

#### `BaseView.GetProjection(self)` <a id="c4d.BaseView.GetProjection"></a>

Returns the projection used by the view. See `Ocamera.h` for values.

**Return type:** int

**Returns:** The projection type.

#### `BaseView.GetViewParameter(self)` <a id="c4d.BaseView.GetViewParameter"></a>

Retrieves the parameters for the current projection. See `Ocamera.h` for projection types.  
The following is the code used internally to project points.

```python
CAMDIST = 0.05

def WorldToCamera(p, camera_matrix):
    return p * (~camera_matrix)

def CameraToWorld(p, camera_matrix):
    return p * camera_matrix

def CameraToScreen(pp):
    p = c4d.Vector(pp)
    if projection == c4d.Pperspective:
        nz = 1.0 / CAMDIST if p.z <= 0 else 1.0 / (p.z + CAMDIST)
        p.x = p.x * scale.x * nz+off.x
        p.y = p.y * scale.y * nz+off.y
        return p

    p.x = (p.x * scale.x) + off.x
    p.y = (p.y * scale.y) + off.y

    if projection in (c4d.Pmilitary, c4d.Pfrog, c4d.Pgentleman):
        p.x += p.z * scale.x * sclaez.x
        p.y -= p.z * scale.y * scalez.y
    return p

def ScreenToCamera(pp):
    p = c4d.Vector(pp)
    if projection in (c4d.Pmilitary, c4d.Pfrog, c4d.Pgentleman):
        p.x -= p.z * scale.x * scalez.x
        p.y += p.z * scale.y * scalez.y

    p.x = (p.x - off.x) / scale.x
    p.y = (p.y - off.y) / scale.y

    if projection == c4d.Pperspective:
        nz = p.z + CAMDIST
        p.x *= nz
        p.y *= nz
    return p
```

For non-axometric projection here’s the code how to calculate off/scale.

```python
def InitView(camera, xres, yres, pix_x, pix_y):

    opm = camera.GetMg()
    data = camera.GetDataInstance()
    project = data.GetInt32(c4d.CAMERA_PROJECTION, c4d.Pperspective)

    if projection not in (c4d.Pperspective, c4d.Pparallel):
        opm.v1 = c4d.Vector(1.0, 0.0, 0.0)
        opm.v2 = c4d.Vector(0.0, 1.0, 0.0)
        opm.v3 = c4d.Vector(0.0, 0.0, 1.0)

    off.x = xres * 0.5
    off.y = yres * 0.5

    if b_ab == c4d.Pperspective:
        ap = data.GetFloat(c4d.CAMERAOBJECT_APERTURE, 36.0)
        scale.x = data.GetFloat(c4d.CAMERA_FOCUS, 36.0) / ap * xres
    else:
        scale.x = xres / 1024.0 * data.GetFloat(c4d.CAMERA_ZOOM, 1.0)

    scale.y = -scale.x * pix_x / pix_y
    # ... calculated here
```

Example for how to use `BaseView.GetViewParameter()`:

```python
>>> bd = doc.GetActiveBaseDraw()
>>> bd
<c4d.BaseDraw object called Perspective with ID 110305 at 1694970435200>
>>> bd.GetViewParameter()
{'offset': Vector(348.5, 221, 0), 'scale': Vector(697, -697, 0), 'scale_z': Vector(0, 0, 0)}
```

**Return type:** Dict[[c4d.Vector](../../../../Vector/index.md#c4d.Vector), [c4d.Vector](../../../../Vector/index.md#c4d.Vector), [c4d.Vector](../../../../Vector/index.md#c4d.Vector)]

**Returns:** The dimension, is never **None**.

### View Dimensions <a id="c4d.BaseView-method-View-Dimensions"></a>

#### `BaseView.GetFrame(self)` <a id="c4d.BaseView.GetFrame"></a>

The dimension in pixels of the view window.  
The coordinates are relative to the upper left corner of the view, and specify visible pixels. (I.e. the border is not included.).

```python
>>> bd = doc.GetActiveBaseDraw()
>>> bd
<c4d.BaseDraw object called Perspective with ID 110305 at 1694970435200>
>>> bd.GetFrame()
{'cl': 0, 'ct': 0, 'cr': 696, 'cb': 441}
```

**Return type:** Dict[int, int, int, int]

#### `BaseView.GetSafeFrame(self)` <a id="c4d.BaseView.GetSafeFrame"></a>

The dimension in pixels of the render lines.  
The render lines show what part of the view is included in the rendered picture.

```python
>>> bd = doc.GetActiveBaseDraw()
>>> bd
<c4d.BaseDraw object called Perspective with ID 110305 at 1694970435200>
>>> bd.GetSafeFrame()
{'cl': 0, 'ct': 25, 'cr': 696, 'cb': 417}
```

**Return type:** Dict[int, int, int, int]

### Visibility Testing <a id="c4d.BaseView-method-Visibility-Testing"></a>

#### `BaseView.BackfaceCulling(self, n, p)` <a id="c4d.BaseView.BackfaceCulling"></a>

Tests the face with center *p* and normal *n* for backface culling.

> **Note:** Both vector must be defined in the same space coordinate.

**Parameters:**

- **n** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – The face normal.
- **p** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – The face center.

**Return type:** [c4d.Vector](../../../../Vector/index.md#c4d.Vector)

**Returns:** **True** if the face should be visible, otherwise **False**.

#### `BaseView.TestClipping3D(self, mp, rad, mg)` <a id="c4d.BaseView.TestClipping3D"></a>

Tests if a bounding box is visible in the view according to the current projection.

The box is defined with passed *mp*, *rad* and *mg* by these eight corner coordinates

```python
p0 = c4d.Vector(mp.x + rad.x, mp.y + rad.y, mp.z + rad.z) * mg
p1 = c4d.Vector(mp.x + rad.x, mp.y + rad.y, mp.z - rad.z) * mg
p2 = c4d.Vector(mp.x + rad.x, mp.y - rad.y, mp.z + rad.z) * mg
p3 = c4d.Vector(mp.x + rad.x, mp.y - rad.y, mp.z - rad.z) * mg
p4 = c4d.Vector(mp.x - rad.x, mp.y + rad.y, mp.z + rad.z) * mg
p5 = c4d.Vector(mp.x - rad.x, mp.y + rad.y, mp.z - rad.z) * mg
p6 = c4d.Vector(mp.x - rad.x, mp.y - rad.y, mp.z + rad.z) * mg
p7 = c4d.Vector(mp.x - rad.x, mp.y - rad.y, mp.z - rad.z) * mg
```

**Parameters:**

- **mp** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – The center of the box.
- **rad** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – The radius of the box.
- **mg** ([*c4d.Matrix*](../../../../Matrix/index.md#c4d.Matrix)) – The transformation to world space from *mp*/*rad* space.

**Return type:** Dict[bool, bool, bool]

**Returns:**

A dictionary with the following information:

’visible’: **True** if the box is visible, otherwise **False**.  
’clip2d’: **True** if the box needs 2D clipping, i.e. if any part of it is outside of the view boundaries. Otherwise **False**.  
’clipz’: **True** if the box needs Z clipping, i.e. if any part of it is too close to or behind the camera. Otherwise **False**.

#### `BaseView.TestPoint(self, x, y)` <a id="c4d.BaseView.TestPoint"></a>

Returns **True** if the point is within the boundary returned by [`GetFrame()`](#c4d.BaseView.GetFrame).  
The point coordinates must be in screen space.

**Parameters:**

- **x** (*int*) – X coordinate
- **y** (*int*) – Y coordinate

**Return type:** bool

**Returns:** **True** if the point is inside, otherwise **False**.

#### `BaseView.TestPointZ(self, p)` <a id="c4d.BaseView.TestPointZ"></a>

Tests if the point is visible in the view according to the current projection.  
The point must be in camera space.

**Parameters:** **p** ([*c4d.Vector*](../../../../Vector/index.md#c4d.Vector)) – The point to check.

**Return type:** bool

**Returns:** **True** if the point is visible in the view, otherwise **False**.
