<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_geometry.html -->

# Geometry Model <a id="geometry-model"></a>

Explains the geometry model of Cinema 4D: polygons, edges, normals, caches, and splines.

All geometry in the Cinema 4D API is represented by [`BaseObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) instances. A `BaseObject` can also be something other than geometry, such as a light or camera. There are two fundamental kinds of geometry objects: *generators* and *non-generators*. Most geometry types follow this hierarchy (`VolumeObject` is an exception):

```python
c4d.BaseObject
+-- c4d.PointObject
    +-- c4d.LineObject
    +-- c4d.PolygonObject
    +-- c4d.SplineObject
```

Generators create geometry from parameters in the Attribute Manager. A Cube, for example, has size, segment, and fillet settings; changing them rebuilds its geometry cache for the viewport and renderer. The generated cache cannot be edited directly, including through the API, because the generator will replace it on the next update.

Non-generators such as [`LineObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/LineObject/index.md#c4d.LineObject) and [`PolygonObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) store discrete geometry rather than parameters that generate it. Both derive from [`PointObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/index.md#c4d.PointObject), which holds [`Vector`](../modules/c4d/Vector/index.md#c4d.Vector) positions in object-local space (see [Vectors](manual_vectors.md)). A polygon object stores points and polygons; a line object stores points and segments. [`SplineObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/SplineObject/index.md#c4d.SplineObject) is the exception: it has editable spline points *and* acts as a generator. Both a parameterized Circle spline and an editable `SplineObject` produce a `LineObject` cache at their current interpolation settings.

## Caches <a id="caches"></a>

There are two kinds of caches. A generator’s *cache* represents the parameters from which it was built: for a Cube it is a `PolygonObject`, but it can also be a hierarchy containing other generators and their caches. A *deform cache* is the deformed state of a non-generator `PolygonObject` or `LineObject`; a Bend creates one without changing the original geometry. For an Array with two copies of a Cylinder and its Bend deformer, compare the Object Manager with the tree *after* the document builds its caches:

**Object Manager (input)**

```
Array (generator)
+-- Cylinder (generator)
    +-- Bend (deformer)
```

**Evaluated tree (input + output)**

```
Array (generator)
+-- [cache] Null
|   +-- Cylinder.1 (clone)
|   |   +-- [cache] PolygonObject
|   |   |   +-- [deform] bent PolygonObject
|   |   +-- Bend (cloned child)
|   +-- Cylinder.2 (clone)
|       +-- [cache] PolygonObject
|       |   +-- [deform] bent PolygonObject
|       +-- Bend (cloned child)
+-- Cylinder (original input)
    +-- Bend (original input)
```

The Array’s [`BaseObject.GetCache()`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject.GetCache) points to the generated Null. Its children are *clones* of the input Cylinder, each still a generator with its own polygon cache. The cloned Bend produces a *deform cache* on that polygon object, not on the Array or Cylinder; follow [`BaseObject.GetDeformCache()`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject.GetDeformCache) from the polygon to reach the bent result. The original Cylinder and Bend remain input children, not output. Cache links are separate from child links, so walking the final geometry requires following both, recursively. Caches are read-only and may be absent before evaluation. See [Scene Structure](manual_scene_structure.md) for the scene graph; the matching cache-tree example is linked below.

## Polygons <a id="polygons"></a>

A [`PolygonObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) owns a list of points and a list of [`CPolygon`](../modules/c4d/CPolygon/index.md#c4d.CPolygon) entries. Each polygon holds four **indices into that object’s point list** (`a, b, c, d`), not four positions. In the view, P references points `(0, 1, 2, 3)` and Q references `(1, 4, 5, 2)`: points 1 and 2 are shared. Move either point and both polygons move.

Cinema 4D always represents a polygon with four index slots. For a triangle the last slot repeats the third: `CPolygon(0, 1, 2, 2)`. An n-gon is represented internally by triangles and quads, not a larger `CPolygon`.

### Winding and Normals <a id="winding-and-normals"></a>

The index order is the *winding*. It determines the front face and polygon normal. For neighboring faces with aligned normals, their winding crosses the shared edge in opposite directions: P goes `1 -> 2`, Q goes `2 -> 1`. Flip Q in the view to see its normal reverse.

Drag to orbit, Ctrl + wheel to zoom, hover or tap an element for details.

### Vertex, Polygon, and Phong Normals <a id="vertex-polygon-and-phong-normals"></a>

A mesh distinguishes three normals:

| Normal | One per | Meaning and access |
|---|---|---|
| Polygon normal | Polygon | The face’s orientation, derived from its winding; not stored. |
| Vertex normal | Point | The average of the normals of faces sharing that point; not stored. |
| Phong normal | Polygon corner | A shading normal for each polygon corner, so one point can have different normals on different faces. Read via [`PolygonObject.CreatePhongNormals()`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject.CreatePhongNormals) or a [`NormalTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/NormalTag/index.md#c4d.NormalTag). |

Phong normals smooth shared corners until the fold exceeds the Phong angle limit; then each corner keeps its face normal and the edge looks hard. Try the Fold and Phong limit controls above. The view averages only the two visible faces; Cinema 4D’s exact weighting can differ. Polygon and vertex normals must be derived; Phong normals require a Phong or Normal tag.

### Edges <a id="edges"></a>

There is no separate edge list on a [`PolygonObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject). Each polygon contributes four sides, even a triangle (whose last side repeats a point). A raw edge index is `polygonIndex * 4 + sideIndex` (AB, BC, CD, DA). Thus the shared edge `1 -> 2` of P and `2 -> 1` of Q has **two** raw indices. Turn on Raw edges in the view above and hover either half. Selections use these raw indices; user-facing edge indices may merge the two halves.

## Splines <a id="splines"></a><a id="geometry-splines"></a>

A [`SplineObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/SplineObject/index.md#c4d.SplineObject) stores editable points in open or closed *segments*. It also generates a [`LineObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/LineObject/index.md#c4d.LineObject) cache: straight pieces sampled from its curve. The one view below has two segments; turn off Cache to see the underlying dashed curve, or show normals to compare orientations along it.

| Concept | What it controls |
|---|---|
| Type | Linear joins points directly; Cubic and Akima pass smoothly through them; B-Spline is drawn toward them; Bezier uses editable left and right tangent offsets (`vl`, `vr`). The view draws Linear and Bezier. |
| Interpolation | Sets cache density independently of type. None uses the vertices; Natural and Uniform insert a fixed number of points; Adaptive samples bends; Subdivided also limits piece length. The view approximates Natural and Uniform with evenly spaced parameter values. |
| Normals | [`c4d.utils.SplineHelp`](../modules/c4d.utils/SplineHelp/index.md#c4d.utils.SplineHelp) provides a mathematical normal (`GetNormal()`), which vanishes and flips at inflections, and a parallel-transport frame (`GetMatrix()`), which keeps its orientation along the curve. |

Drag to orbit, Ctrl + wheel to zoom, hover or tap for details.

Parameterized spline generators such as Circle do not own editable spline points; their spline representation is available through [`BaseObject.GetRealSpline()`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject.GetRealSpline). Initialize `SplineHelp` with an up vector; use `GetMatrix(offset, realoffset=True)` to place objects by distance along the spline. The starting up vector determines the transported frame. The forum discussion [Place multiple objects on spline and align](https://developers.maxon.net/forum/topic/14467/place-multiple-objects-on-spline-and-align) explores the difference.

## See Also <a id="see-also"></a>

- [Scene Structure](manual_scene_structure.md): Explains how a Cinema 4D scene is organized with hierarchies and branches, and how to traverse it.
- [Vectors](manual_vectors.md): Explains how to carry out vector operations.
- [Matrices](manual_matrices.md): Explains how to carry out transform operations.
- [Example geometry_cache.py](../examples/modeling/geometry_cache.py.md): Explains the geometry model of the Cinema API in Cinema 4D.
- [Example geometry_polygon_object.py](../examples/modeling/geometry_polygon_object.py.md): Explains the user-editable polygon object model of the Cinema API.
- [Example geometry_spline_object.py](../examples/modeling/geometry_spline_object.py.md): Explains the user-editable spline object model of the Cinema API.
