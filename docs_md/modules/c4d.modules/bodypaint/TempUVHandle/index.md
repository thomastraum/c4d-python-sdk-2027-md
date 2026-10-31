<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/bodypaint/TempUVHandle/index.html -->

# c4d.modules.bodypaint.TempUVHandle <a id="c4d-modules-bodypaint-tempuvhandle"></a>

## *class* `c4d.modules.bodypaint.TempUVHandle` <a id="c4d.modules.bodypaint.TempUVHandle"></a>

*New in version R18.011.*

## Overview <a id="overview"></a>

**Mesh Geometry**

- [`TempUVHandle.GetBaseObject()`](#c4d.modules.bodypaint.TempUVHandle.GetBaseObject): Retrieves the object of the UV set.
- [`TempUVHandle.GetPointCount()`](#c4d.modules.bodypaint.TempUVHandle.GetPointCount): Retrieves the point count.
- [`TempUVHandle.GetPoints()`](#c4d.modules.bodypaint.TempUVHandle.GetPoints): Retrieves the read-only points array.
- [`TempUVHandle.GetPolyCount()`](#c4d.modules.bodypaint.TempUVHandle.GetPolyCount): Retrieves the polygon count.
- [`TempUVHandle.GetPolys()`](#c4d.modules.bodypaint.TempUVHandle.GetPolys): Retrieves the read-only polygons array.

**Polygon Visibility**

- [`TempUVHandle.GetPolyHid()`](#c4d.modules.bodypaint.TempUVHandle.GetPolyHid): Retrieves the hidden polygons.
- [`TempUVHandle.GetPolySel()`](#c4d.modules.bodypaint.TempUVHandle.GetPolySel): Retrieves the selected polygons.

**UV Coordinates**

- [`TempUVHandle.GetUVW()`](#c4d.modules.bodypaint.TempUVHandle.GetUVW): Retrieves the UV list.
- [`TempUVHandle.SetUVW()`](#c4d.modules.bodypaint.TempUVHandle.SetUVW): Applies changes of the UV set to the object.
- [`TempUVHandle.SetUVWFromTextureView()`](#c4d.modules.bodypaint.TempUVHandle.SetUVWFromTextureView): Applies changes of the UV set to the object.

**UV Selections**

- [`TempUVHandle.GetUVEdgeSel()`](#c4d.modules.bodypaint.TempUVHandle.GetUVEdgeSel): Retrieves the selected edges.
- [`TempUVHandle.GetUVPointSel()`](#c4d.modules.bodypaint.TempUVHandle.GetUVPointSel): Retrieves the selected UV points.
- [`TempUVHandle.SetUVEdgeSelection()`](#c4d.modules.bodypaint.TempUVHandle.SetUVEdgeSelection): Sets the UV Edge selection.
- [`TempUVHandle.SetUVPointSelectionFromTextureView()`](#c4d.modules.bodypaint.TempUVHandle.SetUVPointSelectionFromTextureView): Sets the UV Point selection.

**UV State**

- [`TempUVHandle.GetMode()`](#c4d.modules.bodypaint.TempUVHandle.GetMode): Retrieves the current UV editor mode.
- [`TempUVHandle.IsEditable()`](#c4d.modules.bodypaint.TempUVHandle.IsEditable): Checks if UVs are editable or not.

## Members <a id="members"></a>

### Mesh Geometry <a id="c4d.modules.bodypaint.TempUVHandle-method-Mesh-Geometry"></a>

#### `TempUVHandle.GetBaseObject(self)` <a id="c4d.modules.bodypaint.TempUVHandle.GetBaseObject"></a>

Retrieves the object of the UV set.

**Return type:** [`c4d.BaseObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

**Returns:** The object of the UV set.

#### `TempUVHandle.GetPointCount(self)` <a id="c4d.modules.bodypaint.TempUVHandle.GetPointCount"></a>

Retrieves the point count.

**Return type:** int

**Returns:** The point count.

#### `TempUVHandle.GetPoints(self)` <a id="c4d.modules.bodypaint.TempUVHandle.GetPoints"></a>

Retrieves the read-only points array.

**Return type:** List[[c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The points.

#### `TempUVHandle.GetPolyCount(self)` <a id="c4d.modules.bodypaint.TempUVHandle.GetPolyCount"></a>

Retrieves the polygon count.

**Return type:** int

**Returns:** The polygon count.

#### `TempUVHandle.GetPolys(self)` <a id="c4d.modules.bodypaint.TempUVHandle.GetPolys"></a>

Retrieves the read-only polygons array.

**Return type:** List[[c4d.CPolygon](../../../c4d/CPolygon/index.md#c4d.CPolygon)]

**Returns:** The polygons.

### Polygon Visibility <a id="c4d.modules.bodypaint.TempUVHandle-method-Polygon-Visibility"></a>

#### `TempUVHandle.GetPolyHid(self)` <a id="c4d.modules.bodypaint.TempUVHandle.GetPolyHid"></a>

Retrieves the hidden polygons.

**Return type:** [`c4d.BaseSelect`](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)

**Returns:** The hidden polygons selection.

#### `TempUVHandle.GetPolySel(self)` <a id="c4d.modules.bodypaint.TempUVHandle.GetPolySel"></a>

Retrieves the selected polygons.

**Return type:** [`c4d.BaseSelect`](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)

**Returns:** The polygons selection.

### UV Coordinates <a id="c4d.modules.bodypaint.TempUVHandle-method-UV-Coordinates"></a>

#### `TempUVHandle.GetUVW(self)` <a id="c4d.modules.bodypaint.TempUVHandle.GetUVW"></a>

Retrieves the UV list.

**Return type:** List[Dict[‘a’,’b’,’c’,’d’]]

**Returns:** The UV list.

#### `TempUVHandle.SetUVW(self, uvw)` <a id="c4d.modules.bodypaint.TempUVHandle.SetUVW"></a>

Applies changes of the UV set to the object.

**Parameters:** **uvw** (*List*[*Dict*[*'a'*,*'b'*,*'c'*,*'d'*]]) – The UV list to set.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `TempUVHandle.SetUVWFromTextureView(self, uvw, ignoreHidden, ignoreUnselected, autoSelectAll, registerUndo=True)` <a id="c4d.modules.bodypaint.TempUVHandle.SetUVWFromTextureView"></a>

Applies changes of the UV set to the object.

**Parameters:**

- **uvw** (*List*[*Dict*[*'a'*,*'b'*,*'c'*,*'d'*]]) – The UV list to set.
- **ignoreHidden** (*bool*) – If **True**, do not affect the UV coordinates of UV Polygons or UV Points of hidden polygons.
- **ignoreUnselected** (*bool*) – If **True**, do not affect the UV coordinates of UV Polygons, or UV Points (depending on the current mode) that are unselected in the Texture View.
- **autoSelectAll** (*bool*) – If **True**, automatically selects all UV Polygons, or UV Points (depending on the current mode).
- **registerUndo** (*Optional*[*bool*]) – If **True**, an undo is added for the operation.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### UV Selections <a id="c4d.modules.bodypaint.TempUVHandle-method-UV-Selections"></a>

#### `TempUVHandle.GetUVEdgeSel(self)` <a id="c4d.modules.bodypaint.TempUVHandle.GetUVEdgeSel"></a>

Retrieves the selected edges.

*New in version S22.114.*

**Return type:** [`c4d.BaseSelect`](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)

**Returns:** The edge selection.

#### `TempUVHandle.GetUVPointSel(self)` <a id="c4d.modules.bodypaint.TempUVHandle.GetUVPointSel"></a>

Retrieves the selected UV points.

> **Note:** The points are indexed by *4* * *polygon* + *point* where *polygon* is the polygon index and *point* is the point index between *0* and *3*.

**Return type:** [`c4d.BaseSelect`](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)

**Returns:** The hidden polygons selection.

#### `TempUVHandle.SetUVEdgeSelection(self, uvEdgeSelection)` <a id="c4d.modules.bodypaint.TempUVHandle.SetUVEdgeSelection"></a>

Sets the UV Edge selection.

> **Note:** The edges have to be indexed as follows: 4 * polygon + edge where **c** polygon is the polygon index and **c** edge is the edge index between **0 and 3**.

**Parameters:** **uvEdgeSelection** ([*c4d.BaseSelect*](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)) – The pointer to the new UV Edge selection.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `TempUVHandle.SetUVPointSelectionFromTextureView(self, uvPointSelection, bleedSelection)` <a id="c4d.modules.bodypaint.TempUVHandle.SetUVPointSelectionFromTextureView"></a>

Sets the UV Point selection.  
The points have to be indexed as follows: 4 * polygon + point where **c** polygon is the polygon index and **c** point is the point index between **0 and 3** (a, b, c, d).

*New in version S22.*

**Parameters:**

- **uvPointSelection** ([*c4d.BaseSelect*](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)) – The Point BaseSelect that will be defined from the UV Point selection.

- **bleedSelection** (*bool*) –

  If **True,** ensures that if one UV point is selected, all UV points having the same coordinates are selected as well.  
  If false it doesn’t check, which is faster.

**Returns:** **True** if successful, otherwise **False**.

**Return type:** bool

### UV State <a id="c4d.modules.bodypaint.TempUVHandle-method-UV-State"></a>

#### `TempUVHandle.GetMode(self)` <a id="c4d.modules.bodypaint.TempUVHandle.GetMode"></a>

Retrieves the current UV editor mode.

**Return type:** int

**Returns:**

The UV editor mode:

|   |   |
|---|---|
| *Mcamera* | Camera mode. |
| *Mobject* | Object mode. |
| *Mtexture* | Texture mode. |
| *Mtextureaxis* | Texture axis mode. |
| *Mpoints* | Point edit mode. |
| *Medges* | Edge edit mode. |
| *Mpolygons* | Polygon edit mode. |
| *Manimation* | Animation mode. |
| *Mkinematic* | IK mode. |
| *Mmodel* | Model mode. |
| *Mpaint* | Paint mode. |
| *Muvpoints* | UV points mode. |
| *Muvpolygons* | UV polygons mode. |
| *Mdrag* | Drag mode. |
| *Mpolyedgepoint* | Combined poly/edge/point mode. Must only be used in [`ViewportSelect`](../../../c4d.utils/ViewportSelect/index.md#c4d.utils.ViewportSelect). |
| *Medgepoint* | Combined edge/point mode. Must only be used in [`ViewportSelect`](../../../c4d.utils/ViewportSelect/index.md#c4d.utils.ViewportSelect). |
| *Mworkplane* | Workplane mode. |
| *Mdrag* | Drag mode. |
| *Muvedges* | Uv Edge node is enabled. |
| *Muvon* | Uv mode is enabled. |

#### `TempUVHandle.IsEditable(self)` <a id="c4d.modules.bodypaint.TempUVHandle.IsEditable"></a>

Checks if UVs are editable or not.  
Polygon objects have editable UVs, object generators usually not.

**Return type:** [`c4d.BaseObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

**Returns:** The object of the UV set.
