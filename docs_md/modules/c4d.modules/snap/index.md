<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/snap/index.html -->

# c4d.modules.snap <a id="c4d-modules-snap"></a>

## *class* `c4d.modules.snap` <a id="c4d.modules.snap"></a>

This is the snap module to access the snap settings, quantizing options, workplane etc.

*New in version R14.034.*

## Overview <a id="overview"></a>

**Quantization Controls**

- [`c4d.modules.snap.GetQuantizeStep()`](#c4d.modules.snap.GetQuantizeStep): Gets a quantize step value.
- [`c4d.modules.snap.IsQuantizeEnabled()`](#c4d.modules.snap.IsQuantizeEnabled): Check if quantizing is enabled for the document *doc*.
- [`c4d.modules.snap.SetQuantizeStep()`](#c4d.modules.snap.SetQuantizeStep): Sets a quantize step value.

**Snapping Controls**

- [`c4d.modules.snap.EnableSnap()`](#c4d.modules.snap.EnableSnap): Set the snap enabled status for the document *doc* or a particular *snapmode*.
- [`c4d.modules.snap.GetSnapSettings()`](#c4d.modules.snap.GetSnapSettings): Get the snap settings for the document *doc* or a specific *snapmode*.
- [`c4d.modules.snap.IsSnapEnabled()`](#c4d.modules.snap.IsSnapEnabled): Check if snap is enabled for the document *doc* or for a specific *snapmode*.
- [`c4d.modules.snap.SetSnapSettings()`](#c4d.modules.snap.SetSnapSettings): Set the snap settings for the document *doc* or a specific *snapmode*.

**Workplane Management**

- [`c4d.modules.snap.GetWorkplaneMatrix()`](#c4d.modules.snap.GetWorkplaneMatrix): Get the workplane matrix.
- [`c4d.modules.snap.GetWorkplaneObject()`](#c4d.modules.snap.GetWorkplaneObject): Retrieve the workplane object for document *doc*.
- [`c4d.modules.snap.IsWorkplaneLock()`](#c4d.modules.snap.IsWorkplaneLock): Get the workplane locked status for document *doc*.
- [`c4d.modules.snap.SetWorkplaneLock()`](#c4d.modules.snap.SetWorkplaneLock): Set the workplane locked status.

## Members <a id="members"></a>

### Quantization Controls <a id="c4d.modules.snap-function-Quantization-Controls"></a>

#### `c4d.modules.snap.GetQuantizeStep(doc, bd, quantize_mode)` <a id="c4d.modules.snap.GetQuantizeStep"></a>

Gets a quantize step value.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

- **bd** (*Optional*[[*c4d.BaseDraw*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)]) – Currently not used. Pass **None**.

- **quantize_mode** (*int*) –

  The mode to retrieve the value for:

  |   |   |   |
  |---|---|---|
  | *QUANTIZE_GRID* | bool | Set quantize move step to use the grid size. |
  | *QUANTIZE_MOVE* | float | Movement. |
  | *QUANTIZE_ROTATE* | float | Rotation. |
  | *QUANTIZE_SCALE* | float | Scaling. |
  | *QUANTIZE_TEXTURE* | float | Texture. |

#### `c4d.modules.snap.IsQuantizeEnabled(doc)` <a id="c4d.modules.snap.IsQuantizeEnabled"></a>

Check if quantizing is enabled for the document *doc*.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to test for.

**Return type:** bool

**Returns:** **True** if quantizing is enabled, otherwise **False**.

#### `c4d.modules.snap.SetQuantizeStep(doc, bd, quantize_mode, val)` <a id="c4d.modules.snap.SetQuantizeStep"></a>

Sets a quantize step value.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

- **bd** (*Optional*[[*c4d.BaseDraw*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)]) – Currently not used. Pass **None**.

- **quantize_mode** (*int*) –

  The mode to set the value for:

  |   |   |   |
  |---|---|---|
  | *QUANTIZE_GRID* | bool | Set quantize move step to use the grid size. |
  | *QUANTIZE_MOVE* | float | Movement. |
  | *QUANTIZE_ROTATE* | float | Rotation. |
  | *QUANTIZE_SCALE* | float | Scaling. |
  | *QUANTIZE_TEXTURE* | float | Texture. |

- **val** (*float*) – The quantize step value to set.

### Snapping Controls <a id="c4d.modules.snap-function-Snapping-Controls"></a>

#### `c4d.modules.snap.EnableSnap(state, doc, snapmode=-1)` <a id="c4d.modules.snap.EnableSnap"></a>

Set the snap enabled status for the document *doc* or a particular *snapmode*.

**Parameters:**

- **state** (*bool*) – The state to set: **True** to enable, **False** to disable.

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to set the snap mode state for.

- **snapmode** (*Optional*[*int*]) –

  Optionnally set a snap mode instead of enabling snap for the document. One of the following:

  |   |   |
  |---|---|
  | *SNAPMODE_POINT* | Snap to a vertex on a mesh. |
  | *SNAPMODE_EDGE* | Snap to any point along an edge. |
  | *SNAPMODE_POLYGON* | Snap to the surface of a polygon. |
  | *SNAPMODE_SPLINE* | Snap to any point along a spline. |
  | *SNAPMODE_AXIS* | Snap to the axis of an object. |
  | *SNAPMODE_INTERSECTION* | Snap to the intersections of objects and guides. |
  | *SNAPMODE_MIDPOINT* | Snap to midpoint. Allows sub-snapping. |
  | *SNAPMODE_EDGEMID* | Snap to middle of an edge. |
  | *SNAPMODE_POLYGONCENTER* | Snap to the center of individual polygons. |
  | *SNAPMODE_SPLINEMID* | Snap to the middle of a spline segment. |
  | *SNAPMODE_WORKPLANE* | Snap to the surface of the workplane. |
  | *SNAPMODE_GRIDPOINT* | Snap to the intersection points of the grid on the workplane. |
  | *SNAPMODE_GRIDLINE* | Snap to the grid lines on the workplane. |
  | *SNAPMODE_GUIDEMID* | Snap to the mid point in between of static guides intersections. |
  | *SNAPMODE_GUIDE* | Snap to guide obejcts. |
  | *SNAPMODE_DYNAMICGUIDE* | Snap using dynamic or inferred guides. |
  | *SNAPMODE_ORTHO* | Snap perpendicular to guides edges and splines. |
  | *SNAPMODE_PIXEL* | Snap to the texture’s pixels in the UV viewport. |

#### `c4d.modules.snap.GetSnapSettings(doc, snapmode=-1)` <a id="c4d.modules.snap.GetSnapSettings"></a>

Get the snap settings for the document *doc* or a specific *snapmode*.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document related snap settings to retrieve.

- **snapmode** (*Optional*[*int*]) –

  Specify a snap mode to get or modify its specific settings instead of the global settings (pass **NOTOK**). One of the following:

  |   |   |
  |---|---|
  | *SNAPMODE_POINT* | Snap to a vertex on a mesh. |
  | *SNAPMODE_EDGE* | Snap to any point along an edge. |
  | *SNAPMODE_POLYGON* | Snap to the surface of a polygon. |
  | *SNAPMODE_SPLINE* | Snap to any point along a spline. |
  | *SNAPMODE_AXIS* | Snap to the axis of an object. |
  | *SNAPMODE_INTERSECTION* | Snap to the intersections of objects and guides. |
  | *SNAPMODE_MIDPOINT* | Snap to midpoint. Allows sub-snapping. |
  | *SNAPMODE_EDGEMID* | Snap to middle of an edge. |
  | *SNAPMODE_POLYGONCENTER* | Snap to the center of individual polygons. |
  | *SNAPMODE_SPLINEMID* | Snap to the middle of a spline segment. |
  | *SNAPMODE_WORKPLANE* | Snap to the surface of the workplane. |
  | *SNAPMODE_GRIDPOINT* | Snap to the intersection points of the grid on the workplane. |
  | *SNAPMODE_GRIDLINE* | Snap to the grid lines on the workplane. |
  | *SNAPMODE_GUIDEMID* | Snap to the mid point in between of static guides intersections. |
  | *SNAPMODE_GUIDE* | Snap to guide obejcts. |
  | *SNAPMODE_DYNAMICGUIDE* | Snap using dynamic or inferred guides. |
  | *SNAPMODE_ORTHO* | Snap perpendicular to guides edges and splines. |
  | *SNAPMODE_PIXEL* | Snap to the texture’s pixels in the UV viewport. |

**Return type:** [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:**

A copy of the settings in a [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer). The snap settings IDs are:

|   |   |   |
|---|---|---|
| *SNAP_SETTINGS_ENABLED* | bool | Enable snapping. |
| *SNAP_SETTINGS_RADIUS* | float | Snap radius. |
| *SNAP_SETTINGS_TOOL* | bool | Tool specific. |
| *SNAP_SETTINGS_GUIDEANGLE* | float | Guide angle. |
| *SNAP_SETTINGS_MODE* | int | Mode: |
|  | *SNAP_SETTINGS_MODE_AUTO* | Auto snapping. |
|  | *SNAP_SETTINGS_MODE_2D* | 2D snapping. |
|  | *SNAP_SETTINGS_MODE_3D* | 3D snapping. |
| *SNAP_SETTINGS_PIXELMODE* | int | Mode: |
|  | *SNAP_SETTINGS_PIXELMODE_CENTER* | Snap to the center of the pixels. |
|  | *SNAP_SETTINGS_PIXELMODE_EDGE* | Snap to the top left corner of the pixel. |

|   |   |   |
|---|---|---|
| *QUANTIZE_ENABLED* | bool | Enable quantizing. |
| *QUANTIZE_GRID* | bool | Set quantize move step to use the grid size. |
| *QUANTIZE_MOVE* | float | Movement. |
| *QUANTIZE_ROTATE* | float | Rotation. |
| *QUANTIZE_SCALE* | float | Scaling. |
| *QUANTIZE_TEXTURE* | float | Texture. |

#### `c4d.modules.snap.IsSnapEnabled(doc, snapmode=-1)` <a id="c4d.modules.snap.IsSnapEnabled"></a>

Check if snap is enabled for the document *doc* or for a specific *snapmode*.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to test for.

- **snapmode** (*Optional*[*int*]) –

  Optionnally set a snap mode instead of checking snap for the document. One of the following:

  |   |   |
  |---|---|
  | *SNAPMODE_POINT* | Snap to a vertex on a mesh. |
  | *SNAPMODE_EDGE* | Snap to any point along an edge. |
  | *SNAPMODE_POLYGON* | Snap to the surface of a polygon. |
  | *SNAPMODE_SPLINE* | Snap to any point along a spline. |
  | *SNAPMODE_AXIS* | Snap to the axis of an object. |
  | *SNAPMODE_INTERSECTION* | Snap to the intersections of objects and guides. |
  | *SNAPMODE_MIDPOINT* | Snap to midpoint. Allows sub-snapping. |
  | *SNAPMODE_EDGEMID* | Snap to middle of an edge. |
  | *SNAPMODE_POLYGONCENTER* | Snap to the center of individual polygons. |
  | *SNAPMODE_SPLINEMID* | Snap to the middle of a spline segment. |
  | *SNAPMODE_WORKPLANE* | Snap to the surface of the workplane. |
  | *SNAPMODE_GRIDPOINT* | Snap to the intersection points of the grid on the workplane. |
  | *SNAPMODE_GRIDLINE* | Snap to the grid lines on the workplane. |
  | *SNAPMODE_GUIDEMID* | Snap to the mid point in between of static guides intersections. |
  | *SNAPMODE_GUIDE* | Snap to guide obejcts. |
  | *SNAPMODE_DYNAMICGUIDE* | Snap using dynamic or inferred guides. |
  | *SNAPMODE_ORTHO* | Snap perpendicular to guides edges and splines. |
  | *SNAPMODE_PIXEL* | Snap to the texture’s pixels in the UV viewport. |

**Return type:** bool

**Returns:** **True** if snap is enabled, otherwise **False**.

#### `c4d.modules.snap.SetSnapSettings(doc, bc, snapmode=-1)` <a id="c4d.modules.snap.SetSnapSettings"></a>

Set the snap settings for the document *doc* or a specific *snapmode*.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to set the snap settings for.

- **bc** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) –

  The [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer) with the settings for the document *doc* and/or *snapmode*. The snap settings IDs are:

  |   |   |   |
  |---|---|---|
  | *SNAP_SETTINGS_ENABLED* | bool | Enable snapping. |
  | *SNAP_SETTINGS_RADIUS* | float | Snap radius. |
  | *SNAP_SETTINGS_TOOL* | bool | Tool specific. |
  | *SNAP_SETTINGS_GUIDEANGLE* | float | Guide angle. |
  | *SNAP_SETTINGS_MODE* | int | Mode: |
  |  | *SNAP_SETTINGS_MODE_AUTO* | Auto snapping. |
  |  | *SNAP_SETTINGS_MODE_2D* | 2D snapping. |
  |  | *SNAP_SETTINGS_MODE_3D* | 3D snapping. |
  | *SNAP_SETTINGS_PIXELMODE* | int | Mode: |
  |  | *SNAP_SETTINGS_PIXELMODE_CENTER* | Snap to the center of the pixels. |
  |  | *SNAP_SETTINGS_PIXELMODE_EDGE* | Snap to the top left corner of the pixel. |

  |   |   |   |
  |---|---|---|
  | *QUANTIZE_ENABLED* | bool | Enable quantizing. |
  | *QUANTIZE_GRID* | bool | Set quantize move step to use the grid size. |
  | *QUANTIZE_MOVE* | float | Movement. |
  | *QUANTIZE_ROTATE* | float | Rotation. |
  | *QUANTIZE_SCALE* | float | Scaling. |
  | *QUANTIZE_TEXTURE* | float | Texture. |

- **snapmode** (*Optional*[*int*]) –

  *Deprecated since version R25.010.*

### Workplane Management <a id="c4d.modules.snap-function-Workplane-Management"></a>

#### `c4d.modules.snap.GetWorkplaneMatrix(doc, bd)` <a id="c4d.modules.snap.GetWorkplaneMatrix"></a>

Get the workplane matrix.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.
- **bd** (*Optional*[[*c4d.BaseDraw*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)]) – The viewport you want to get the workplane’s matrix from. If **None** the locked matrix is returned independently from view.

**Return type:** [c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The workplane matrix.

#### `c4d.modules.snap.GetWorkplaneObject(doc)` <a id="c4d.modules.snap.GetWorkplaneObject"></a>

Retrieve the workplane object for document *doc*.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

**Return type:** [c4d.BaseObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

**Returns:** The workplane object.

#### `c4d.modules.snap.IsWorkplaneLock(doc)` <a id="c4d.modules.snap.IsWorkplaneLock"></a>

Get the workplane locked status for document *doc*.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

**Return type:** bool

**Returns:** **True** if the workplane is locked.

#### `c4d.modules.snap.SetWorkplaneLock(bd, locked)` <a id="c4d.modules.snap.SetWorkplaneLock"></a>

Set the workplane locked status.

**Parameters:**

- **bd** ([*c4d.BaseDraw*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The viewport to lock the workplane.
- **locked** (*bool*) – **True** to lock the workplane.
