<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/VertexColorTag/index.html -->

# c4d.VertexColorTag <a id="c4d-vertexcolortag"></a>

## *class* `c4d.VertexColorTag` <a id="c4d.VertexColorTag"></a>

[`c4d.VertexColorTag`](#c4d.VertexColorTag) is a Variable Tag that stores RGBA colors for the polygons of the host polygon object.  
The data can be stored in 2 ways: per polygon (per polygon vertex mode, default) and per vertex (per point mode).

- The per polygon vertex mode (default) is very similar to how [`c4d.UVWTag`](../UVWTag/index.md#c4d.UVWTag) or [`c4d.NormalTag`](../NormalTag/index.md#c4d.NormalTag) store data (4 values per polygon index).  
  Just create it using [`c4d.VertexColorTag()`](#c4d.VertexColorTag) with *count* == `PolygonObject.GetPolygonCount()`.
- The per point mode stores a single color value per vertex and can be used even on objects without any polygon.  
  Create it using [`c4d.VertexColorTag()`](#c4d.VertexColorTag) with *count* == `PointObject.GetPointCount()`.

The tag provides methods to set/get color per polygons or per vertex (average) in per polygon vertex mode.  
It also defines some convenience functions to set/get just color or just alpha value in both modes.

The instance object class of type *Tvertexcolor*.

*New in version R18.020.*

It consist to a list of dict{*a*, *b*, *c*, *d*: [`c4d.Vector4d`](../../../../../../Vector4d/index.md#c4d.Vector4d)}, the vertex colors for a polygon.

Parent Class:

- [`c4d.VariableTag`](../index.md#c4d.VariableTag)

## Overview <a id="overview"></a>

- [`VertexColorTag.GetAlpha()`](#c4d.VertexColorTag.GetAlpha): Retrieves the vertex color alpha value for the vertex *pIndex*.
- [`VertexColorTag.GetColor()`](#c4d.VertexColorTag.GetColor): Retrieves the vertex color for the vertex *pIndex*.
- [`VertexColorTag.GetPoint()`](#c4d.VertexColorTag.GetPoint): Retrieves the vertex color for the vertex *pIndex*.
- [`VertexColorTag.GetPolygon()`](#c4d.VertexColorTag.GetPolygon): Retrieves the vertex colors for the polygon *i* in per polygon vertex mode.
- [`VertexColorTag.SetAlpha()`](#c4d.VertexColorTag.SetAlpha): Sets the vertex color alpha value for the vertex *pIndex*.
- [`VertexColorTag.SetColor()`](#c4d.VertexColorTag.SetColor): Sets the vertex color for the vertex *pIndex*.
- [`VertexColorTag.SetPoint()`](#c4d.VertexColorTag.SetPoint): Sets the vertex color for the vertex *pIndex*.
- [`VertexColorTag.SetPolygon()`](#c4d.VertexColorTag.SetPolygon): Sets the vertex colors for the polygon *i* in per polygon vertex mode.

**Data Access**

- [`VertexColorTag.GetDataAddressR()`](#c4d.VertexColorTag.GetDataAddressR): Gets the read-only data handle.
- [`VertexColorTag.GetDataAddressW()`](#c4d.VertexColorTag.GetDataAddressW): Gets the writable data handle.

**Magic Methods**

- [`VertexColorTag.__init__()`](#c4d.VertexColorTag.__init__): Creates a [`c4d.VertexColorTag`](#c4d.VertexColorTag).

**Storage Mode**

- [`VertexColorTag.IsPerPointColor()`](#c4d.VertexColorTag.IsPerPointColor): Checks if the data is stored per point (vertex) or per polygon vertex.
- [`VertexColorTag.SetPerPointMode()`](#c4d.VertexColorTag.SetPerPointMode): Sets whatever the data is stored per point (vertex) or per polygon vertex.

## Members <a id="members"></a>

### Color Data Operations <a id="c4d.VertexColorTag-staticmethod-Color-Data-Operations"></a>

#### *static* `VertexColorTag.GetAlpha(data, nb, vadr, pIndex)` <a id="c4d.VertexColorTag.GetAlpha"></a>

Retrieves the vertex color alpha value for the vertex *pIndex*.

> **Note:**
>
> If the tag is in per polygon vertex mode it traverses all polygons attached to it.  
> If different values are found then the average value will be returned.

Example.

```python
>>> op
<c4d.PolygonObject object called Plane/Polygon with ID 5100 at 1694970435456>
>>> tag = op.GetTag(c4d.Tvertexcolor)
>>> tag
<c4d.VertexColorTag object called Vertex Color/Vertex Color with ID 431000045 at 1694956554240>
>>> data = tag.GetDataAddressR()
>>> data
<capsule object NULL at 0x0000018AA34B01C0>
>>> for idx in range(op.GetPointCount()):
...     alpha = c4d.VertexColorTag.GetAlpha(data, None, None, idx)
...     print(alpha)
...
0.0
0.0
0.0
0.0
```

**Parameters:**

- **data** (*PyCObject*) – The data handle.
- **nb** (*Optional*[[*c4d.utils.Neighbor*](../../../../../../../c4d.utils/Neighbor/index.md#c4d.utils.Neighbor)]) – A neighbor helper class. Can be initialized with a polygon selection to limit the function to a specific object part. Pass **None** if in per vertex mode.
- **vadr** (*Optional*[*PyCObject*]) – The object [`c4d.CPolygon`](../../../../../../CPolygon/index.md#c4d.CPolygon) array. Pass **None** if in per vertex mode. See `PolygonObject.GetPolygonR()`.
- **pIndex** (*int*) – The point index.

**Return type:** float

**Returns:** The alpha value for the passed vertex, or the average alpha value if multiple values were found.

#### *static* `VertexColorTag.GetColor(data, nb, vadr, pIndex)` <a id="c4d.VertexColorTag.GetColor"></a>

Retrieves the vertex color for the vertex *pIndex*.

> **Note:**
>
> If the tag is in per polygon vertex mode it traverses all polygons attached to it.  
> If different values are found then the average value will be returned.

Example.

```python
>>> op
<c4d.PolygonObject object called Plane/Polygon with ID 5100 at 1694970435456>
>>> tag = op.GetTag(c4d.Tvertexcolor)
>>> tag
<c4d.VertexColorTag object called Vertex Color/Vertex Color with ID 431000045 at 1694956554240>
>>> data = tag.GetDataAddressR()
>>> data
<capsule object NULL at 0x0000018AA34B01C0>
>>> for idx in range(op.GetPointCount()):
...  color = c4d.VertexColorTag.GetColor(data, None, None, idx)
...  print(color)
...
Vector(0, 0, 0)
Vector(0.845, 0, 0)
Vector(0, 0, 0.965)
Vector(0, 1, 0)
```

**Parameters:**

- **data** (*PyCObject*) – The data handle.
- **nb** (*Optional*[[*c4d.utils.Neighbor*](../../../../../../../c4d.utils/Neighbor/index.md#c4d.utils.Neighbor)]) – A neighbor helper class. Can be initialized with a polygon selection to limit the function to a specific object part. Pass **None** if in per vertex mode.
- **vadr** (*Optional*[*PyCObject*]) – The object [`c4d.CPolygon`](../../../../../../CPolygon/index.md#c4d.CPolygon) array. Pass **None** if in per vertex mode. See `PolygonObject.GetPolygonR()`.
- **pIndex** (*int*) – The point index.

**Return type:** [`c4d.Vector`](../../../../../../Vector/index.md#c4d.Vector)

**Returns:** The RGB color for the passed point index, or the average color if multiple values were found.

#### *static* `VertexColorTag.GetPoint(data, nb, vadr, pIndex)` <a id="c4d.VertexColorTag.GetPoint"></a>

Retrieves the vertex color for the vertex *pIndex*.

> **Note:**
>
> If the tag is in per polygon vertex mode it traverses all polygons attached to it.  
> If different values are found then the average value will be returned.

Example.

```python
>>> op
<c4d.PolygonObject object called Plane/Polygon with ID 5100 at 1694970348800>
>>> tag = op.GetTag(c4d.Tvertexcolor)
>>> tag
<c4d.VertexColorTag object called Vertex Color/Vertex Color with ID 431000045 at 1694956683136>
>>> data = tag.GetDataAddressR()
>>> data
<capsule object NULL at 0x0000018AA3491140>
>>> for idx in range(op.GetPointCount()):
...     point = c4d.VertexColorTag.GetPoint(data, None, None, idx)
...     print(point)
...
Vector4d(0, 0, 0, 0)
Vector4d(0.845, 0, 0, 0)
Vector4d(0, 0, 0.965, 0)
Vector4d(0, 1, 0, 0)
```

**Parameters:**

- **data** (*PyCObject*) – The data handle.
- **nb** (*Optional*[[*c4d.utils.Neighbor*](../../../../../../../c4d.utils/Neighbor/index.md#c4d.utils.Neighbor)]) – A neighbor helper class. Can be initialized with a polygon selection to limit the function to a specific object part. Pass **None** if in per vertex mode.
- **vadr** (*Optional*[*PyCObject*]) – The object [`c4d.CPolygon`](../../../../../../CPolygon/index.md#c4d.CPolygon) array. Pass **None** if in per vertex mode. See `PolygonObject.GetPolygonR()`.
- **pIndex** (*int*) – The point index.

**Return type:** [`c4d.Vector4d`](../../../../../../Vector4d/index.md#c4d.Vector4d)

**Returns:** The RGBA color for the passed vertex, or the average color if multiple values were found.

#### *static* `VertexColorTag.GetPolygon(data, i)` <a id="c4d.VertexColorTag.GetPolygon"></a>

Retrieves the vertex colors for the polygon *i* in per polygon vertex mode.

Example.

```python
<c4d.PolygonObject object called Plane/Polygon with ID 5100 at 1694970385536>
>>> tag = op.GetTag(c4d.Tvertexcolor)
>>> tag
<c4d.VertexColorTag object called Vertex Color/Vertex Color with ID 431000045 at 1694956509632>
>>> data = tag.GetDataAddressR()
>>> data
<capsule object NULL at 0x0000018AA3491B00>
>>> for idx in range(op.GetPolygonCount()):
...     poly = c4d.VertexColorTag.GetPolygon(data, idx)
...     print(poly)
...
{'a': Vector4d(0, 0, 0, 0), 'b': Vector4d(0.845, 0, 0, 0), 'c': Vector4d(0, 0, 0.965, 0), 'd': Vector4d(0, 1, 0, 0)}
```

**Parameters:**

- **data** (*PyCObject*) – The data handle.
- **i** (*int*) – The polygon index.

**Return type:** Dict[“a”: [`c4d.Vector4d`](../../../../../../Vector4d/index.md#c4d.Vector4d), “b”: [`c4d.Vector4d`](../../../../../../Vector4d/index.md#c4d.Vector4d), “c”: [`c4d.Vector4d`](../../../../../../Vector4d/index.md#c4d.Vector4d), “d”: [`c4d.Vector4d`](../../../../../../Vector4d/index.md#c4d.Vector4d)]

**Returns:** The retrieved vertex color data.

#### *static* `VertexColorTag.SetAlpha(data, nb, vadr, pIndex, value)` <a id="c4d.VertexColorTag.SetAlpha"></a>

Sets the vertex color alpha value for the vertex *pIndex*.

```python
import c4d

tag = op.GetTag(c4d.Tvertexcolor)
data = tag.GetDataAddressW()

pointCount = op.GetPointCount()
for idx in range(pointCount):
    c4d.VertexColorTag.SetAlpha(data, None, None, idx, 0.5)

c4d.EventAdd()
```

**Parameters:**

- **data** (*PyCObject*) – The data handle.
- **nb** (*Optional*[[*c4d.utils.Neighbor*](../../../../../../../c4d.utils/Neighbor/index.md#c4d.utils.Neighbor)]) – A neighbor helper class. Can be initialized with a polygon selection to limit the function to a specific object part. Pass **None** if in per vertex mode.
- **vadr** (*Optional*[*PyCObject*]) – The object [`c4d.CPolygon`](../../../../../../CPolygon/index.md#c4d.CPolygon) array. Pass **None** if in per vertex mode. See `PolygonObject.GetPolygonW()`.
- **pIndex** (*int*) – The point index.
- **value** (*float*) – The new alpha value to be assigned to the vertex.

#### *static* `VertexColorTag.SetColor(data, nb, vadr, pIndex, color)` <a id="c4d.VertexColorTag.SetColor"></a>

Sets the vertex color for the vertex *pIndex*.

Example.

```python
import c4d

tag = op.GetTag(c4d.Tvertexcolor)
data = tag.GetDataAddressW()

white = c4d.Vector(1.0, 1.0, 1.0)
pointCount = op.GetPointCount()
for idx in range(pointCount):
    c4d.VertexColorTag.SetColor(data, None, None, idx, white)

c4d.EventAdd()
```

**Parameters:**

- **data** (*PyCObject*) – The data handle.
- **nb** (*Optional*[[*c4d.utils.Neighbor*](../../../../../../../c4d.utils/Neighbor/index.md#c4d.utils.Neighbor)]) – A neighbor helper class. Can be initialized with a polygon selection to limit the function to a specific object part. Pass **None** if in per vertex mode.
- **vadr** (*Optional*[*PyCObject*]) – The object [`c4d.CPolygon`](../../../../../../CPolygon/index.md#c4d.CPolygon) array. Pass **None** if in per vertex mode. See `PolygonObject.GetPolygonW()`.
- **pIndex** (*int*) – The point index.
- **color** ([*c4d.Vector*](../../../../../../Vector/index.md#c4d.Vector)) – The new RGB color to be assigned to the vertex.

#### *static* `VertexColorTag.SetPoint(data, nb, vadr, pIndex, color)` <a id="c4d.VertexColorTag.SetPoint"></a>

Sets the vertex color for the vertex *pIndex*.

Example.

```python
import c4d

tag = op.GetTag(c4d.Tvertexcolor)
data = tag.GetDataAddressW()

white = c4d.Vector4d(1.0, 1.0, 1.0, 1.0)
pointCount = op.GetPointCount()
for idx in range(pointCount):
    c4d.VertexColorTag.SetPoint(data, None, None, idx, white)

c4d.EventAdd()
```

**Parameters:**

- **data** (*PyCObject*) – The data handle.
- **nb** (*Optional*[[*c4d.utils.Neighbor*](../../../../../../../c4d.utils/Neighbor/index.md#c4d.utils.Neighbor)]) – A neighbor helper class. Can be initialized with a polygon selection to limit the function to a specific object part. Pass **None** if in per vertex mode.
- **vadr** (*Optional*[*PyCObject*]) – The object [`c4d.CPolygon`](../../../../../../CPolygon/index.md#c4d.CPolygon) array. Pass **None** if in per vertex mode. See `PolygonObject.GetPolygonW()`.
- **pIndex** (*int*) – The point index.
- **color** ([*c4d.Vector4d*](../../../../../../Vector4d/index.md#c4d.Vector4d)) – The new RGBA color to be assigned to the vertex.

#### *static* `VertexColorTag.SetPolygon(data, i, polygon)` <a id="c4d.VertexColorTag.SetPolygon"></a>

Sets the vertex colors for the polygon *i* in per polygon vertex mode.

Example.

```python
tag = op.GetTag(c4d.Tvertexcolor)
data = tag.GetDataAddressW()

white = c4d.Vector4d(1.0, 1.0, 1.0, 1.0)
poly = {"a": white, "b": white, "c": white, "d": white}

polyCount = op.GetPolygonCount()
for idx in range(polyCount):
    c4d.VertexColorTag.SetPolygon(data, idx, poly)

c4d.EventAdd()
```

**Parameters:**

- **data** (*PyCObject*) – The data handle.
- **i** (*int*) – The polygon index.
- **polygon** (*Dict*) – The vertex color data **a, b, c and d** to be set to the polygon

### Data Access <a id="c4d.VertexColorTag-method-Data-Access"></a>

#### `VertexColorTag.GetDataAddressR(self)` <a id="c4d.VertexColorTag.GetDataAddressR"></a>

Gets the read-only data handle.  
It automatically recognizes if the tag is in per polygon vertex or per vertex mode.

**Return type:** PyCObject

**Returns:** The handle to the read-only vertex color data.

#### `VertexColorTag.GetDataAddressW(self)` <a id="c4d.VertexColorTag.GetDataAddressW"></a>

Gets the writable data handle.  
It automatically recognizes if the tag is in per polygon vertex or per vertex mode.

**Return type:** PyCObject

**Returns:** The handle to the writable vertex color data.

### Magic Methods <a id="c4d.VertexColorTag-method-Magic-Methods"></a>

#### `VertexColorTag.__init__(self, count)` <a id="c4d.VertexColorTag.__init__"></a>

Creates a [`c4d.VertexColorTag`](#c4d.VertexColorTag).

**Parameters:** **count** (*int*) – The number of elements in the tag. Must be equal to the object’s polygon count if the tag is in per polygon vertex mode, otherwise must be equal to the object’s point count in per vertex mode.

### Storage Mode <a id="c4d.VertexColorTag-method-Storage-Mode"></a>

#### `VertexColorTag.IsPerPointColor(self)` <a id="c4d.VertexColorTag.IsPerPointColor"></a>

Checks if the data is stored per point (vertex) or per polygon vertex.

**Return type:** bool

**Returns:** **True** if vertex colors are stored per vertex, otherwise **False**.

#### `VertexColorTag.SetPerPointMode(self, perPointColor)` <a id="c4d.VertexColorTag.SetPerPointMode"></a>

Sets whatever the data is stored per point (vertex) or per polygon vertex.

> **Note:** The item count is automatically updated and the data converted if possible.

> **Warning:** All handles are invalidated after the call.

**Parameters:** **perPointColor** (*bool*) – If **True** the data will be stored per vertex otherwise per polygon vertex.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.
