<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.html -->

# c4d.PolygonObject <a id="c4d-polygonobject"></a>

## *class* `c4d.PolygonObject` <a id="c4d.PolygonObject"></a>

Represents a Polygon object.

The instance object class of type *Opolygon*.

Parent Class:

- [`c4d.PointObject`](../index.md#c4d.PointObject)

## Overview <a id="overview"></a>

**Magic Methods**

- [`PolygonObject.__init__()`](#c4d.PolygonObject.__init__)

**Mesh Structure**

- [`PolygonObject.GetEdgeCount()`](#c4d.PolygonObject.GetEdgeCount): The number of edges contained in this object.
- [`PolygonObject.GetNgonCount()`](#c4d.PolygonObject.GetNgonCount): Get the number of N-gons in the object, i.e.
- [`PolygonObject.GetPolygonCount()`](#c4d.PolygonObject.GetPolygonCount): Returns the count of polygons.
- [`PolygonObject.ResizeObject()`](#c4d.PolygonObject.ResizeObject): Change the number of points and polygons in the object.

**N-Gon Topology**

- [`PolygonObject.GetNgonEdgesCompact()`](#c4d.PolygonObject.GetNgonEdgesCompact): Retrieves a list that contains N-gon edges information for each polygon.
- [`PolygonObject.GetNGonTranslationMap()`](#c4d.PolygonObject.GetNGonTranslationMap): Gets a translation map from N-gon indices to polygon indices.
- [`PolygonObject.GetPolygonTranslationMap()`](#c4d.PolygonObject.GetPolygonTranslationMap): Gets a translation map from polygon indices to N-gon indices.

**Polygon Data Access**

- [`PolygonObject.GetAllPolygons()`](#c4d.PolygonObject.GetAllPolygons): Returns all polygons.
- [`PolygonObject.GetPolygon()`](#c4d.PolygonObject.GetPolygon): Get a polygon.
- [`PolygonObject.GetPolygonR()`](#c4d.PolygonObject.GetPolygonR): Gets the start of the read-only array of polygons.
- [`PolygonObject.GetPolygonW()`](#c4d.PolygonObject.GetPolygonW): Gets the start of the writable array of polygons.
- [`PolygonObject.SetPolygon()`](#c4d.PolygonObject.SetPolygon): Set a polygon.

**Selection And Visibility**

- [`PolygonObject.GetEdgeH()`](#c4d.PolygonObject.GetEdgeH): Get the hidden edges.
- [`PolygonObject.GetEdgeS()`](#c4d.PolygonObject.GetEdgeS): Get the selected edges.
- [`PolygonObject.GetEdgeSelection()`](#c4d.PolygonObject.GetEdgeSelection): Deselects all edges in ‘sel’ that are N-gon edges as specified by type.
- [`PolygonObject.GetHiddenNgons()`](#c4d.PolygonObject.GetHiddenNgons): Copies the current hidden N-gon selection into *sel*.
- [`PolygonObject.GetPolygonH()`](#c4d.PolygonObject.GetPolygonH): Return the hidden polygons.
- [`PolygonObject.GetPolygonS()`](#c4d.PolygonObject.GetPolygonS): Return the selected polygons.
- [`PolygonObject.GetSelectedEdges()`](#c4d.PolygonObject.GetSelectedEdges): Get the selected, hidden or phong break edges.
- [`PolygonObject.GetSelectedNgons()`](#c4d.PolygonObject.GetSelectedNgons): Copies the current N-gon selection into sel.
- [`PolygonObject.SetSelectedEdges()`](#c4d.PolygonObject.SetSelectedEdges): Set the selected, hidden or phong break edges.
- [`PolygonObject.ValidateEdgeSelection()`](#c4d.PolygonObject.ValidateEdgeSelection): Deselects all selected edges in *sel* that are N-gon edges.

**Shading And Normals**

- [`PolygonObject.CreatePhongNormals()`](#c4d.PolygonObject.CreatePhongNormals): Returns a list with the stored phong normals of the object.
- [`PolygonObject.GetPhongBreak()`](#c4d.PolygonObject.GetPhongBreak): Get the phong break edges.
- [`PolygonObject.GetShadingBreak()`](#c4d.PolygonObject.GetShadingBreak): Gets the shading break edges based on neighbor polygons shading edges and a specified angle limit.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.PolygonObject-method-Magic-Methods"></a>

#### `PolygonObject.__init__(self, pcnt, vcnt)` <a id="c4d.PolygonObject.__init__"></a>

**Parameters:**

- **pcnt** (*int*) – Point count.
- **vcnt** (*int*) – Polygon count.

### Mesh Structure <a id="c4d.PolygonObject-method-Mesh-Structure"></a>

#### `PolygonObject.GetEdgeCount(self)` <a id="c4d.PolygonObject.GetEdgeCount"></a>

The number of edges contained in this object.

*New in version 2024.0.0.*

**Returns:** The edge count

**Return type:** int

#### `PolygonObject.GetNgonCount(self)` <a id="c4d.PolygonObject.GetNgonCount"></a>

Get the number of N-gons in the object, i.e. the number of polygons with more points than 4.

**Return type:** int

**Returns:** The number of N-gons for this object.

#### `PolygonObject.GetPolygonCount(self)` <a id="c4d.PolygonObject.GetPolygonCount"></a>

Returns the count of polygons.  
Is the fastest way to get the count of polygons.

**Return type:** int

**Returns:** The count.

#### `PolygonObject.ResizeObject(self, pcnt, vcnt=-1)` <a id="c4d.PolygonObject.ResizeObject"></a>

Change the number of points and polygons in the object.  
If *vcnt* is -1 or not set, the method of `PointObject.ResizeObject()` is used.

**Parameters:**

- **pcnt** (*int*) – The new number of points.
- **vcnt** (*int*) – The new number of polygons.

**Return type:** bool

**Returns:** Success of changing the number of points and segments.

### N-Gon Topology <a id="c4d.PolygonObject-method-N-Gon-Topology"></a>

#### `PolygonObject.GetNgonEdgesCompact(self)` <a id="c4d.PolygonObject.GetNgonEdgesCompact"></a>

Retrieves a list that contains N-gon edges information for each polygon.  
The edge compact value is based on the mask *1 << edgeIndex* with *edgeIndex* between *0* - *3* for quads, and *0*, *1*, *3* for triangles.  
If the value for a polygon is zero then it has no N-gon edge.  
Otherwise check each edge of the polygon with *edges[polyIndex] & (1 << edgeIndex) == 0* (with *edges* the list of N-gon edges compact values). If the condition is **True** then the edge is a N-gon edge.

**Return type:** list

**Returns:** N-gon edges information list.

#### `PolygonObject.GetNGonTranslationMap(self, ngoncnt, polymap)` <a id="c4d.PolygonObject.GetNGonTranslationMap"></a>

Gets a translation map from N-gon indices to polygon indices.

*New in version R19.024.*

**Parameters:**

- **ngoncnt** (*int*) – The number of N-gons. Pass the number of N-gons returned by [`GetPolygonTranslationMap()`](#c4d.PolygonObject.GetPolygonTranslationMap), not the value given by [`GetNgonCount()`](#c4d.PolygonObject.GetNgonCount).
- **polymap** (*List*[*int*]) – The polygon map. Pass the list returned by [`GetPolygonTranslationMap()`](#c4d.PolygonObject.GetPolygonTranslationMap), or a similarly formatted array.

**Return type:** Optional[List[List[int]]]

**Returns:**

The polygon index map if successful, otherwise **None**.

> **Note:**
>
> The number of polygons in N-gon *i* is stored in *List[i][0]*.  
> Then the polygon indices are stored in *List[i][j]* where *j* goes from *1* to *List[i][0]*.

#### `PolygonObject.GetPolygonTranslationMap(self)` <a id="c4d.PolygonObject.GetPolygonTranslationMap"></a>

Gets a translation map from polygon indices to N-gon indices.

**Return type:** Tuple[int, List[int]]

**Returns:**

The number of N-gons (and remaining polygons) and the list of N-gon indices. (*0*, []) if the function failed.

*Changed in version R19.024:* Was only returning the list of N-gon indices.

> **Note:**
>
> The number of n-gon correspond to all N-gons and all remaining polygons which are not part of any N-gons.  
> The *list* has an amount of entries corresponding to the Cpolygon count of the Polygon Object.  
> Where each number of the *list* correspond to the Cpolygon id and the value to the N-gon this Cpolygon belongs to.  
> An Abstract example [0, 4] means the CPolygon 0 belongs to the N-gon 0 and the CPolygon 1 belongs to the N-gon 4.

### Polygon Data Access <a id="c4d.PolygonObject-method-Polygon-Data-Access"></a>

#### `PolygonObject.GetAllPolygons(self)` <a id="c4d.PolygonObject.GetAllPolygons"></a>

Returns all polygons.

**Return type:** List[[c4d.CPolygon](../../../../../../CPolygon/index.md#c4d.CPolygon)]

**Returns:** A list of copied polygons.

#### `PolygonObject.GetPolygon(self, id)` <a id="c4d.PolygonObject.GetPolygon"></a>

Get a polygon.

**Parameters:** **id** (*int*) – The index.

**Raises:** **IndexError** – If the polygon index *id* is out of range : *0<=id<*[`GetPolygonCount()`](#c4d.PolygonObject.GetPolygonCount).

**Return type:** [c4d.CPolygon](../../../../../../CPolygon/index.md#c4d.CPolygon)

**Returns:** The polygon at index *id*.

#### `PolygonObject.GetPolygonR(self)` <a id="c4d.PolygonObject.GetPolygonR"></a>

Gets the start of the read-only array of polygons.

*New in version R18.011.*

> **Note:**
>
> While this function may sound trivial and cheap, internally it is not.  
> For performance reasons, it is not recommended to use this function inside a loop or inside a loop condition.

**Return type:** PyCObject

**Returns:** The start of the read-only polygon array.

#### `PolygonObject.GetPolygonW(self)` <a id="c4d.PolygonObject.GetPolygonW"></a>

Gets the start of the writable array of polygons.

*New in version R18.011.*

> **Note:**
>
> While this function may sound trivial and cheap, internally it is not.  
> For performance reasons, it is not recommended to use this function inside a loop or inside a loop condition.

**Return type:** PyCObject

**Returns:** The start of the writable polygon array.

#### `PolygonObject.SetPolygon(self, id, polygon)` <a id="c4d.PolygonObject.SetPolygon"></a>

Set a polygon.

> **Note:** Call `obj.Message` (*c4d.MSG_UPDATE*) after you set all your polygons to update the object.

**Parameters:**

- **id** (*int*) – The index.
- **polygon** ([*c4d.CPolygon*](../../../../../../CPolygon/index.md#c4d.CPolygon)) – The polygon to set at index *id*.

**Raises:** **IndexError** – If the polygon index *id* is out of range : *0<=id<*[`GetPolygonCount()`](#c4d.PolygonObject.GetPolygonCount).

### Selection And Visibility <a id="c4d.PolygonObject-method-Selection-And-Visibility"></a>

#### `PolygonObject.GetEdgeH(self)` <a id="c4d.PolygonObject.GetEdgeH"></a>

Get the hidden edges.  
The edges are indexed by *4 * polygon + edge* where polygon is the polygon index and edge is the edge index between *0 and 3*.

> **Note:** The edges are only hidden within the editor.

> **Warning:**
>
> If you change this selection you must make sure that it is still valid, so that shared edges have a well-defined selection status.  
> It is safer to use [`SetSelectedEdges()`](#c4d.PolygonObject.SetSelectedEdges).

**Return type:** [c4d.BaseSelect](../../../../../../BaseSelect/index.md#c4d.BaseSelect)

**Returns:** A reference to the selection of hidden edges.

#### `PolygonObject.GetEdgeS(self)` <a id="c4d.PolygonObject.GetEdgeS"></a>

Get the selected edges.  
The edges are indexed by *4 * polygon + edge* where polygon is the polygon index and edge is the edge index between *0 and 3*.

> **Warning:**
>
> If you change this selection you must make sure that its still valid, so that shared edges have a well-defined selection status.  
> It is safer to use [`SetSelectedEdges()`](#c4d.PolygonObject.SetSelectedEdges).

**Return type:** [c4d.BaseSelect](../../../../../../BaseSelect/index.md#c4d.BaseSelect)

**Returns:** A reference to the selection of visible edges.

#### `PolygonObject.GetEdgeSelection(self, sel, type)` <a id="c4d.PolygonObject.GetEdgeSelection"></a>

Deselects all edges in ‘sel’ that are N-gon edges as specified by type.

**Parameters:**

- **sel** ([*c4d.BaseSelect*](../../../../../../BaseSelect/index.md#c4d.BaseSelect)) – The selection to check for N-gon edges.

- **type** (*int*) –

  The type of selection to check:

  |   |   |
  |---|---|
  | *EDGESELECTIONTYPE_SELECTION* | Selected edges. |
  | *EDGESELECTIONTYPE_HIDDEN* | Hidden edges. |
  | *EDGESELECTIONTYPE_PHONG* | Phong edges. |

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `PolygonObject.GetHiddenNgons(self, sel)` <a id="c4d.PolygonObject.GetHiddenNgons"></a>

Copies the current hidden N-gon selection into *sel*.

**Parameters:** **sel** ([*c4d.BaseSelect*](../../../../../../BaseSelect/index.md#c4d.BaseSelect)) – Assigned the current hidden N-gon selection.

#### `PolygonObject.GetPolygonH(self)` <a id="c4d.PolygonObject.GetPolygonH"></a>

Return the hidden polygons.

**Return type:** [c4d.BaseSelect](../../../../../../BaseSelect/index.md#c4d.BaseSelect)

**Returns:** A reference to the hidden polygon structure.

#### `PolygonObject.GetPolygonS(self)` <a id="c4d.PolygonObject.GetPolygonS"></a>

Return the selected polygons.

**Return type:** [c4d.BaseSelect](../../../../../../BaseSelect/index.md#c4d.BaseSelect)

**Returns:** A reference to the selected polygon structure.

#### `PolygonObject.GetSelectedEdges(self, e, ltype)` <a id="c4d.PolygonObject.GetSelectedEdges"></a>

Get the selected, hidden or phong break edges.  
The edges are indexed uniquely by a [`Neighbor`](../../../../../../../c4d.utils/Neighbor/index.md#c4d.utils.Neighbor) object, so each edge has a single index.

> **Note:** This is a convenience wrapper around [`GetEdgeS()`](#c4d.PolygonObject.GetEdgeS), [`GetEdgeH()`](#c4d.PolygonObject.GetEdgeH) and [`GetPhongBreak()`](#c4d.PolygonObject.GetPhongBreak).

**Parameters:**

- **e** ([*c4d.utils.Neighbor*](../../../../../../../c4d.utils/Neighbor/index.md#c4d.utils.Neighbor)) – The neighbor object with information about the edge topology. Must be initialized with all polygons, i.e. with `Neighbor.Init()`.

- **ltype** (*int*) –

  The type of selection to get:

  |   |   |
  |---|---|
  | *EDGESELECTIONTYPE_SELECTION* | Selected edges. |
  | *EDGESELECTIONTYPE_HIDDEN* | Hidden edges. |
  | *EDGESELECTIONTYPE_PHONG* | Phong edges. |

**Return type:** [c4d.BaseSelect](../../../../../../BaseSelect/index.md#c4d.BaseSelect)

**Returns:** The selected edges.

#### `PolygonObject.GetSelectedNgons(self, sel)` <a id="c4d.PolygonObject.GetSelectedNgons"></a>

Copies the current N-gon selection into sel.

**Parameters:** **sel** ([*c4d.BaseSelect*](../../../../../../BaseSelect/index.md#c4d.BaseSelect)) – Assigned the current N-gon selection.

#### `PolygonObject.SetSelectedEdges(self, e, pSel, ltype)` <a id="c4d.PolygonObject.SetSelectedEdges"></a>

Set the selected, hidden or phong break edges.  
The edges are indexed uniquely by a [`Neighbor`](../../../../../../../c4d.utils/Neighbor/index.md#c4d.utils.Neighbor) object, so each edge has a single index.

> **Note:** This is a convenience wrapper around [`GetEdgeS()`](#c4d.PolygonObject.GetEdgeS), [`GetEdgeH()`](#c4d.PolygonObject.GetEdgeH) and [`GetPhongBreak()`](#c4d.PolygonObject.GetPhongBreak).

**Parameters:**

- **e** ([*c4d.utils.Neighbor*](../../../../../../../c4d.utils/Neighbor/index.md#c4d.utils.Neighbor)) – The neighbor object with information about the edge topology. Must be initialized with all polygons, i.e. with `Neighbor.Init()`.

- **pSel** ([*c4d.BaseSelect*](../../../../../../BaseSelect/index.md#c4d.BaseSelect)) – The edge to select.

- **ltype** (*int*) –

  The type of selection to get:

  |   |   |
  |---|---|
  | *EDGESELECTIONTYPE_SELECTION* | Selected edges. |
  | *EDGESELECTIONTYPE_HIDDEN* | Hidden edges. |
  | *EDGESELECTIONTYPE_PHONG* | Phong edges. |

**Return type:** bool

**Returns:** **True** if the selection succeeded, otherwise **False**.

#### `PolygonObject.ValidateEdgeSelection(self, sel)` <a id="c4d.PolygonObject.ValidateEdgeSelection"></a>

Deselects all selected edges in *sel* that are N-gon edges.

**Parameters:** **sel** ([*c4d.BaseSelect*](../../../../../../BaseSelect/index.md#c4d.BaseSelect)) – The selection to check for N-gon edges.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Shading And Normals <a id="c4d.PolygonObject-method-Shading-And-Normals"></a>

#### `PolygonObject.CreatePhongNormals(self)` <a id="c4d.PolygonObject.CreatePhongNormals"></a>

Returns a list with the stored phong normals of the object.

**Return type:** Optional[List[[c4d.Vector](../../../../../../Vector/index.md#c4d.Vector)]]

**Returns:** The list or **None** if the object has no Phong Tag.

#### `PolygonObject.GetPhongBreak(self)` <a id="c4d.PolygonObject.GetPhongBreak"></a>

Get the phong break edges.  
The edges are indexed by *4 * polygon + edge* where polygon is the polygon index and edge is the edge index between *0 and 3*.

> **Warning:**
>
> If you change this selection you must make sure that its still valid, so that shared edges have a well-defined phong break status.  
> it is safer to use [`SetSelectedEdges()`](#c4d.PolygonObject.SetSelectedEdges).

**Return type:** [c4d.BaseSelect](../../../../../../BaseSelect/index.md#c4d.BaseSelect)

**Returns:** The phong break.

#### `PolygonObject.GetShadingBreak(self, includeBorderEdges, includeUserBreak, includeUserNormals, userNormalsAngle=0.0872665, autoNormalsAngle=3.14159)` <a id="c4d.PolygonObject.GetShadingBreak"></a>

Gets the shading break edges based on neighbor polygons shading edges and a specified angle limit.  
Border edges can optionally be marked as break edges.  
Current break edges can optionally be included (merged) in the resulting break edges.  
Finally, user normal vectors can optionally be considered using a separate angle limit for this purpose.

*New in version R19.*

> **Note:** The edges are indexed by *4 * polygon + edge* where *polygon* is the polygon index and *edge* is the edge index between *0* and *3*.

**Parameters:**

- **includeBorderEdges** (*bool*) – **True** to mark border edges as break edges, otherwise **False**.
- **includeUserBreak** (*bool*) – **True** to include the user break edges (same as obtained with [`GetPhongBreak()`](#c4d.PolygonObject.GetPhongBreak)), otherwise **False**.
- **includeUserNormals** (*bool*) – **True** to consider user normals using the *userNormalAngle* parameter, otherwise **False**.
- **userNormalsAngle** (*float*) – Optional angle limit, in radians, beyond which polygon vertex normals sharing edge vertices create a break edge.
- **autoNormalsAngle** (*float*) – Optional angle limit, in radians, beyond which polygon normals sharing an edge create a break edge.

**Return type:** [c4d.BaseSelect](../../../../../../BaseSelect/index.md#c4d.BaseSelect)

**Returns:** The shading break edges.
