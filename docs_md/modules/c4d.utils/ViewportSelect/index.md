<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.utils/ViewportSelect/index.html -->

# c4d.utils.ViewportSelect <a id="c4d-utils-viewportselect"></a>

## *class* `c4d.utils.ViewportSelect` <a id="c4d.utils.ViewportSelect"></a>

## Overview <a id="overview"></a>

- [`ViewportSelect.PickMaterial()`](#c4d.utils.ViewportSelect.PickMaterial): Pick the material at the given pixel coordinates in the viewport.
- [`ViewportSelect.PickObject()`](#c4d.utils.ViewportSelect.PickObject): Pick objects.

**Magic Methods**

- [`ViewportSelect.__init__()`](#c4d.utils.ViewportSelect.__init__)

**Nearest Element Selection**

- [`ViewportSelect.GetNearestEdge()`](#c4d.utils.ViewportSelect.GetNearestEdge): Retrieves nearest edge information at the pixel position (*x*, *y*).
- [`ViewportSelect.GetNearestPoint()`](#c4d.utils.ViewportSelect.GetNearestPoint): Retrieves nearest point information at the pixel position (*x*, *y*).
- [`ViewportSelect.GetNearestPolygon()`](#c4d.utils.ViewportSelect.GetNearestPolygon): Retrieves nearest polygon information at the pixel position (*x*, *y*).

**Viewport Coordinate And Asset Picking**

- [`ViewportSelect.GetCameraCoordinates()`](#c4d.utils.ViewportSelect.GetCameraCoordinates): Converts the pixel position (*x*, *y*, *z*) to camera coordinates.

**Viewport Overlay Drawing**

- [`ViewportSelect.DrawHandle()`](#c4d.utils.ViewportSelect.DrawHandle): Draws a handle into the internal pixel structure, so that pixels inside the handle will be associated with *i* and *op* in the viewport pixel retrieved.
- [`ViewportSelect.DrawPolygon()`](#c4d.utils.ViewportSelect.DrawPolygon): Draws a polygon into the internal pixel structure, so that pixels inside the polygon will be associated with *i* and *op* in the viewport pixel retrieved.
- [`ViewportSelect.SetBrushRadius()`](#c4d.utils.ViewportSelect.SetBrushRadius): Sets the radius for `ShowHotspot()`.
- [`ViewportSelect.ShowHotspot()`](#c4d.utils.ViewportSelect.ShowHotspot): Draws an XOR circle to the view *bw* at the pixel position (*x*, *y*). The radius is set by `SetBrushRadius()`.

**Viewport Setup And Pixel Data**

- [`ViewportSelect.ClearPixelInfo()`](#c4d.utils.ViewportSelect.ClearPixelInfo): Deletes the pixel information at (*x*, *y*) according to mask.
- [`ViewportSelect.GetPixelInfoEdge()`](#c4d.utils.ViewportSelect.GetPixelInfoEdge): Retrieves edge information at the pixel position (*x*, *y*):
- [`ViewportSelect.GetPixelInfoPoint()`](#c4d.utils.ViewportSelect.GetPixelInfoPoint): Retrieves point information at the pixel position (*x*, *y*):
- [`ViewportSelect.GetPixelInfoPolygon()`](#c4d.utils.ViewportSelect.GetPixelInfoPolygon): Retrieves polygon information at the pixel position (*x*, *y*):
- [`ViewportSelect.Init()`](#c4d.utils.ViewportSelect.Init): Initializes the viewport information for multiple objects.

## Members <a id="members"></a>

### Viewport Coordinate And Asset Picking <a id="c4d.utils.ViewportSelect-staticmethod-Viewport-Coordinate-And-Asset-Picking"></a>

#### *static* `ViewportSelect.PickMaterial(bd, doc, x, y, radius)` <a id="c4d.utils.ViewportSelect.PickMaterial"></a>

Pick the material at the given pixel coordinates in the viewport.

Polygon selections, generators, and instances are supported. If the object under the mouse has no material, the function will try to deduce it from its parent objects.

**Parameters:**

- **bd** ([*c4d.BaseDraw*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The viewport base draw.
- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.
- **x** (*int*) – The X position of the picking circle within the viewport.
- **y** (*int*) – The Y position of the picking circle within the viewport.
- **radius** (*int*) – The radius in pixels for the search.

**Return type:** Dict[Optional[[c4d.BaseMaterial](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial)], Optional[[c4d.BaseObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]]

**Returns:**

A dict containing:

- pickedMaterial (c4d.BaseMaterial or None): The picked material, or None in case of default material.
- pickedObject (c4d.BaseObject or None): The top picked object. This does not guarantee that the object has the picked material attached; the function may iterate on its hierarchy children or parents to find the material at that pixel.

#### *static* `ViewportSelect.PickObject(bd, doc, x, y, rad, flags)` <a id="c4d.utils.ViewportSelect.PickObject"></a>

Pick objects.

**Parameters:**

- **bd** ([*c4d.BaseDraw*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The viewport base draw.

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – Document.

- **x** (*int*) – An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to [`Init()`](#c4d.utils.ViewportSelect.Init).

- **y** (*int*) – An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to [`Init()`](#c4d.utils.ViewportSelect.Init).

- **rad** (*int*) – A radius for the search in pixels.

- **flags** (*int*) –

  Flags:

  | Symbol ID | Description |
  |---|---|
  | VIEWPORT_PICK_FLAGS_NONE | None. |
  | VIEWPORT_PICK_FLAGS_ALLOW_OGL | Allow OpenGL. |
  | VIEWPORT_PICK_FLAGS_DONT_STOP_THREADS | Do not stop threads. |
  | VIEWPORT_PICK_FLAGS_USE_SEL_FILTER | Use selection filter. |
  | VIEWPORT_PICK_FLAGS_OGL_ONLY_TOPMOST | Picks only topmost object. Use this only when the object pointer is not needed. Only works with OpenGL. |
  | VIEWPORT_PICK_FLAGS_OGL_ONLY_VISIBLE | Picks only visible. Only works with OpenGL.<br>> > **Note:** Not supported by Python API. |
  | VIEWPORT_PICK_FLAGS_OGL_IGNORE_Z | Picks ignore Z position. Set this to only check if an object (and which) was hit, not its Z position. Only works with OpenGL. |
  | VIEWPORT_PICK_FLAGS_OGL_ONLY_TOPMOST_WITH_OBJ | Picks only topmost object but returns the topmost object with its Z position. Only works with OpenGL. |
  | VIEWPORT_PICK_FLAGS_NO_DEPTH_CORRECTION | To support old tools, the matrix is usually corrected so that the depth can be in the [-1, 1] range. With this option set, this does not happen any more.<br>> *New in version R23.105.* |

**Return type:** Optional[List[[c4d.BaseObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]]

**Returns:** Object list or **None** on failure.

### Magic Methods <a id="c4d.utils.ViewportSelect-method-Magic-Methods"></a>

#### `ViewportSelect.__init__(self)` <a id="c4d.utils.ViewportSelect.__init__"></a>

### Nearest Element Selection <a id="c4d.utils.ViewportSelect-method-Nearest-Element-Selection"></a>

#### `ViewportSelect.GetNearestEdge(self, op, x, y, maxrad=2147483647, onlyselected=False, ignorelist=None, ignorecnt=0, onlyVisible=False)` <a id="c4d.utils.ViewportSelect.GetNearestEdge"></a>

Retrieves nearest edge information at the pixel position (*x*, *y*).

**Parameters:**

- **op** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object to search for the closest element.

- **x** (*int*) – An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to [`Init()`](#c4d.utils.ViewportSelect.Init). If an element was found the reference is updated to reflect the X coordinate of the nearest point.

- **y** (*int*) – An Y coordinate within the viewport. Must be *0 <= y < h*, where *y* is the width given to [`Init()`](#c4d.utils.ViewportSelect.Init). If an element was found the reference is updated to reflect the Y coordinate of the nearest point.

- **maxrad** (*int*) – A maximal radius for the search in pixels.

- **onlyselected** (*bool*) – If this is True only selected elements are included in the search.

- **ignorelist** (*Optional*[*List*[*int*]]) – List of points to ignore.

- **ignorecnt** (*int*) – Ignore list count.

- **onlyVisible** (*bool*) –

  *New in version 2024.0.0.*

  True to ignore not visible points.

**Return type:**

Optional[Dict[int, c4d.BaseObject, float, float, float]]

|   |   |   |   |
|---|---|---|---|
| **i** | int | Element index. The index depends on the element type: |  |
|  |  | point | point index |
|  |  | polygon | polygon index |
|  |  | edge | 4*polygon + edge index |
|  |  | spline | point segment offset + point index |
| **op** | [`BaseObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) | Object. |  |
| **z** | float | Z coordinate of the current element. |  |
| **x** | float | X pixel position. |  |
| **y** | float | Y pixel position. |  |

**Returns:** The retrieved pixel information or **None** if no information could be retrieved.

#### `ViewportSelect.GetNearestPoint(self, op, x, y, maxrad=2147483647, onlyselected=False, ignorelist=None, ignorecnt=0, onlyVisible=False)` <a id="c4d.utils.ViewportSelect.GetNearestPoint"></a>

Retrieves nearest point information at the pixel position (*x*, *y*).

**Parameters:**

- **op** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object to search for the closest element.

- **x** (*int*) – An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to [`Init()`](#c4d.utils.ViewportSelect.Init). If an element was found the reference is updated to reflect the X coordinate of the nearest point.

- **y** (*int*) – An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to [`Init()`](#c4d.utils.ViewportSelect.Init). If an element was found the reference is updated to reflect the Y coordinate of the nearest point.

- **maxrad** (*int*) – A maximal radius for the search in pixels.

- **onlyselected** (*bool*) – If this is True only selected elements are included in the search.

- **ignorelist** (*Optional*[*List*[*int*]]) – List of points to ignore.

- **ignorecnt** (*int*) – Ignore list count.

- **onlyVisible** (*bool*) –

  *New in version 2024.0.0.*

  True to ignore not visible points.

**Return type:**

Optional[Dict[int, c4d.BaseObject, float, float, float]]

|   |   |   |   |
|---|---|---|---|
| **i** | int | Element index. The index depends on the element type: |  |
|  |  | point | point index |
|  |  | polygon | polygon index |
|  |  | edge | 4*polygon + edge index |
|  |  | spline | point segment offset + point index |
| **op** | [`BaseObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) | Object. |  |
| **z** | float | Z coordinate of the current element. |  |
| **x** | float | X pixel position. |  |
| **y** | float | Y pixel position. |  |

**Returns:** The retrieved pixel information or **None** if no information could be retrieved.

#### `ViewportSelect.GetNearestPolygon(self, op, x, y, maxrad=2147483647, onlyselected=False, ignorelist=None, ignorecnt=0)` <a id="c4d.utils.ViewportSelect.GetNearestPolygon"></a>

Retrieves nearest polygon information at the pixel position (*x*, *y*).

**Parameters:**

- **op** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object to search for the closest element.
- **x** (*int*) – An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to [`Init()`](#c4d.utils.ViewportSelect.Init). If an element was found the reference is updated to reflect the X coordinate of the nearest point.
- **y** (*int*) – An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to [`Init()`](#c4d.utils.ViewportSelect.Init). If an element was found the reference is updated to reflect the Y coordinate of the nearest point.
- **maxrad** (*int*) – A maximal radius for the search in pixels.
- **onlyselected** (*bool*) – If this is True only selected elements are included in the search.
- **ignorelist** (*Optional*[*List*[*int*]]) – List of points to ignore.
- **ignorecnt** (*int*) – Ignore list count.

**Return type:**

Optional[Dict[int, c4d.BaseObject, float, float, float]]

|   |   |   |   |
|---|---|---|---|
| **i** | int | Element index. The index depends on the element type: |  |
|  |  | point | point index |
|  |  | polygon | polygon index |
|  |  | edge | 4*polygon + edge index |
|  |  | spline | point segment offset + point index |
| **op** | [`BaseObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) | Object. |  |
| **z** | float | Z coordinate of the current element. |  |
| **x** | float | X pixel position. |  |
| **y** | float | Y pixel position. |  |

**Returns:** The retrieved pixel information or **None** if no information could be retrieved.

### Viewport Coordinate And Asset Picking <a id="c4d.utils.ViewportSelect-method-Viewport-Coordinate-And-Asset-Picking"></a>

#### `ViewportSelect.GetCameraCoordinates(self, x, y, z)` <a id="c4d.utils.ViewportSelect.GetCameraCoordinates"></a>

Converts the pixel position (*x*, *y*, *z*) to camera coordinates.

**Parameters:**

- **x** (*float*) – An X coordinate within the viewport.
- **y** (*float*) – An Y coordinate within the viewport.
- **z** (*float*) – A Z coordinate.

**Return type:** [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The calculated camera coordinate.

### Viewport Overlay Drawing <a id="c4d.utils.ViewportSelect-method-Viewport-Overlay-Drawing"></a>

#### `ViewportSelect.DrawHandle(self, p, i, op, onlyvisible=-1)` <a id="c4d.utils.ViewportSelect.DrawHandle"></a>

Draws a handle into the internal pixel structure, so that pixels inside the handle will be associated with *i* and *op* in the viewport pixel retrieved.

**Parameters:**

- **p** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) –

  The position of the handle.

  > **Note:** All coordinates are in screen space.

- **i** (*int*) – The polygon index to associate with this polygon.

- **op** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object to associate with this polygon.

- **onlyvisible** (*int*) – If this is **True**, only visible parts of the handle are drawn.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `ViewportSelect.DrawPolygon(self, p, i, op, onlyvisible=-1)` <a id="c4d.utils.ViewportSelect.DrawPolygon"></a>

Draws a polygon into the internal pixel structure, so that pixels inside the polygon will be associated with *i* and *op* in the viewport pixel retrieved.

**Parameters:**

- **p** (*array* ([`Vector`](../../c4d/Vector/index.md#c4d.Vector))) –

  An array of points that make up the polygon.

  > **Note:** All coordinates are in screen space.

- **i** (*int*) – The polygon index to associate with this polygon.

- **op** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object to associate with this polygon.

- **onlyvisible** (*int*) – If this is **True**, only visible parts of the polygon are drawn.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `ViewportSelect.SetBrushRadius(self, r)` <a id="c4d.utils.ViewportSelect.SetBrushRadius"></a>

Sets the radius for [`ShowHotspot()`](#c4d.utils.ViewportSelect.ShowHotspot).

**Parameters:** **r** (*float*) – The new radius in pixels.

#### `ViewportSelect.ShowHotspot(self, bw, x, y)` <a id="c4d.utils.ViewportSelect.ShowHotspot"></a>

Draws an XOR circle to the view *bw* at the pixel position (*x*, *y*). The radius is set by [`SetBrushRadius()`](#c4d.utils.ViewportSelect.SetBrushRadius).

**Parameters:**

- **bw** ([*c4d.gui.EditorWindow*](../../c4d.gui/EditorWindow/index.md#c4d.gui.EditorWindow)) – The editor window to draw to.
- **x** (*int*) – An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to [`Init()`](#c4d.utils.ViewportSelect.Init).
- **y** (*int*) – An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to [`Init()`](#c4d.utils.ViewportSelect.Init).

### Viewport Setup And Pixel Data <a id="c4d.utils.ViewportSelect-method-Viewport-Setup-And-Pixel-Data"></a>

#### `ViewportSelect.ClearPixelInfo(self, x, y, mask)` <a id="c4d.utils.ViewportSelect.ClearPixelInfo"></a>

Deletes the pixel information at (*x*, *y*) according to mask.

This is used for example in the live edge selection with “tolerant” deactivated to find out how many pixels of a certain edge was selected. If an edge is determined under the cursor, the pixel counter is decremented and the edge information is deleted afterwards.

**Parameters:**

- **x** (*int*) – An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to [`Init()`](#c4d.utils.ViewportSelect.Init).

- **y** (*int*) – An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to [`Init()`](#c4d.utils.ViewportSelect.Init).

- **mask** (*int*) –

  A bitfield of what to clear:

  |   |   |
  |---|---|
  | *VIEWPORT_CLEAR_POINT* | Clear points. |
  | *VIEWPORT_CLEAR_POLYGON* | Clear polygons. |
  | *VIEWPORT_CLEAR_EDGE* | Clear edges. |

#### `ViewportSelect.GetPixelInfoEdge(self, x, y)` <a id="c4d.utils.ViewportSelect.GetPixelInfoEdge"></a>

Retrieves edge information at the pixel position (*x*, *y*):

```python
import c4d
# Creates a new ViewportSelect
vpSelect = c4d.utils.ViewportSelect()
# Initialise the ViewportSelect with a list of object
vpSelect.Init(width, height, bd, [op], c4d.Mpolyedgepoint, True, c4d.VIEWPORTSELECTFLAGS_IGNORE_HIDDEN_SEL)
# Gives a Sample point
xPos, yPos = 100, 100

# Retrieves the information with GetPixelInfoEdge
infoEdge = vpSelect.GetPixelInfoEdge(xPos, yPos)

if not infoEdge:
    return

i = infoEdge["i"]  # int
op = infoEdge["op"]  # c4dBaseObject
z = infoEdge["z"]  # float
```

**Parameters:**

- **x** (*int*) – An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to [`Init()`](#c4d.utils.ViewportSelect.Init).
- **y** (*int*) – An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to [`Init()`](#c4d.utils.ViewportSelect.Init).

**Return type:**

Optional[Dict[int, c4d.BaseObject, float]]

|   |   |   |   |
|---|---|---|---|
| **i** | int | Element index. The index depends on the element type: |  |
|  |  | point | point index |
|  |  | polygon | polygon index |
|  |  | edge | 4*polygon + edge index |
|  |  | spline | point segment offset + point index |
| **op** | [`BaseObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) | Object. |  |
| **z** | float | Z coordinate of the current element. |  |

**Returns:** The retrieved pixel information or **None** if no information could be retrieved.

#### `ViewportSelect.GetPixelInfoPoint(self, x, y)` <a id="c4d.utils.ViewportSelect.GetPixelInfoPoint"></a>

Retrieves point information at the pixel position (*x*, *y*):

```python
import c4d
# Creates a new ViewportSelect
vpSelect = c4d.utils.ViewportSelect()
# Initialise the ViewportSelect with a list of object
vpSelect.Init(width, height, bd, [op], c4d.Mpolyedgepoint, True, c4d.VIEWPORTSELECTFLAGS_IGNORE_HIDDEN_SEL)
# Gives a Sample point
xPos, yPos = 100, 100

# Retrieves the information with GetPixelInfoPoint
infoPoint = vpSelect.GetPixelInfoPoint(xPos, yPos)

if not infoPoint:
    return

i = infoPoint["i"]  # int
op = infoPoint["op"]  # c4d.BaseObject
z = infoPoint["z"]  # float
```

**Parameters:**

- **x** (*int*) – An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to [`Init()`](#c4d.utils.ViewportSelect.Init).
- **y** (*int*) – An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to [`Init()`](#c4d.utils.ViewportSelect.Init).

**Return type:**

Optional[Dict[int, c4d.BaseObject, float]]

|   |   |   |   |
|---|---|---|---|
| **i** | int | Element index. The index depends on the element type: |  |
|  |  | point | point index |
|  |  | polygon | polygon index |
|  |  | edge | 4*polygon + edge index |
|  |  | spline | point segment offset + point index |
| **op** | [`BaseObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) | Object. |  |
| **z** | float | Z coordinate of the current element. |  |

**Returns:** The retrieved pixel information or **None** if no information could be retrieved.

#### `ViewportSelect.GetPixelInfoPolygon(self, x, y)` <a id="c4d.utils.ViewportSelect.GetPixelInfoPolygon"></a>

Retrieves polygon information at the pixel position (*x*, *y*):

```python
import c4d
# Creates a new ViewportSelect
vpSelect = c4d.utils.ViewportSelect()
# Initialise the ViewportSelect with a list of object
vpSelect.Init(width, height, bd, [op], c4d.Mpolyedgepoint, True, c4d.VIEWPORTSELECTFLAGS_IGNORE_HIDDEN_SEL)
# Gives a Sample point
xPos, yPos = 100, 100

# Retrieves the information with GetPixelInfoPolygon
infopolygon = vpSelect.GetPixelInfoPolygon(xPos, yPos)

if not infopolygon:
    return

i = infopolygon["i"]  # int
op = infopolygon["op"]  # c4d.BaseObject
z = infopolygon["z"]  # float
```

**Parameters:**

- **x** (*int*) – An X coordinate within the viewport. Must be *0 <= x < w*, where *w* is the width given to [`Init()`](#c4d.utils.ViewportSelect.Init).
- **y** (*int*) – An Y coordinate within the viewport. Must be *0 <= y < h*, where *h* is the height given to [`Init()`](#c4d.utils.ViewportSelect.Init).

**Return type:**

Optional[Dict[int, c4d.BaseObject, float]]

|   |   |   |   |
|---|---|---|---|
| **i** | int | Element index. The index depends on the element type: |  |
|  |  | point | point index |
|  |  | polygon | polygon index |
|  |  | edge | 4*polygon + edge index |
|  |  | spline | point segment offset + point index |
| **op** | [`BaseObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) | Object. |  |
| **z** | float | Z coordinate of the current element. |  |

**Returns:** The retrieved pixel information or **None** if no information could be retrieved.

#### `ViewportSelect.Init(self, w, h, bd, ops, mode, onlyvisible, flags)` <a id="c4d.utils.ViewportSelect.Init"></a>

Initializes the viewport information for multiple objects. This has to be done before the pixel information can be retrieved. You have to retrieve the width and height of the viewport manually:

```python
import c4d
# Retrieves the active BaseDraw. Use the one passed as argument if you can.
bd = doc.GetActiveBaseDraw()
# Retrieves the frame information
frame = bd.GetFrame()

left = frame["cl"]
right = frame["cr"]
top = frame["ct"]
bottom = frame["cb"]
# Calculates the width and height of the screen
width = right - left + 1
height = bottom - top + 1

# Creates a new ViewportSelect
vpSelect = c4d.utils.ViewportSelect()
# Initialise the ViewportSelect with a list of object
vpSelect.Init(width, height, bd, [op], c4d.Mpolyedgepoint, True, c4d.VIEWPORTSELECTFLAGS_IGNORE_HIDDEN_SEL)
```

**Parameters:**

- **w** (*int*) – Width of the viewport in pixels.

- **h** (*int*) – Height of the viewport in pixels.

- **bd** ([*c4d.BaseDraw*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The viewport base draw.

- **ops** (*List*[[*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – A list with objects to get the information for.

- **mode** (*int*) –

  Editor mode:

  |   |   |
  |---|---|
  | *Mpoints* | Point edit mode. |
  | *Medges* | Edge edit mode. |
  | *Mpolygons* | Polygon edit mode. |
  | *Mpolyedgepoint* | Combined poly/edge/point mode. Must only be used in [`ViewportSelect`](#c4d.utils.ViewportSelect). |
  | *Medgepoint* | Combined edge/point mode. Must only be used in [`ViewportSelect`](#c4d.utils.ViewportSelect). |

- **onlyvisible** (*bool*) – If this is **True** only visible elements are included.

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *VIEWPORTSELECTFLAGS_NONE* | None. |
  | *VIEWPORTSELECTFLAGS_USE_HN* | Use HyperNURBS. |
  | *VIEWPORTSELECTFLAGS_USE_DEFORMERS* | Use deformers. |
  | *VIEWPORTSELECTFLAGS_REGION_SELECT* | A rectangle, polygon and lasso selection counts the number of vertices of a polygon within its area. Usually hidden vertices are not taken into account. This flag allows hidden vertices to be taken into account, otherwise it would not be possible to select polygons if for example all points are hidden. |
  | *VIEWPORTSELECTFLAGS_IGNORE_HIDDEN_SEL* | Ignore hidden selection. |
  | *VIEWPORTSELECTFLAGS_USE_DISPLAY_MODE* | If this flag is set and the display mode is Wireframe or Isoparms only edges and vertices are written into the [`ViewportSelect`](#c4d.utils.ViewportSelect) buffer. The [`ViewportSelect`](#c4d.utils.ViewportSelect) mode must be *Mpolyedgepoint*. |
  | *VIEWPORTSELECTFLAGS_FORCE_USE_DEFORMERS* | Use deformers even when the viewport *DISPLAYEDITSTATE_DEFORM* is disabled. |

**Returns:** **True** if successful, otherwise **False**.
