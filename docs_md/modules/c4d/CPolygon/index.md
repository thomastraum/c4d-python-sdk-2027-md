<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CPolygon/index.html -->

# c4d.CPolygon <a id="c4d-cpolygon"></a>

## *class* `c4d.CPolygon` <a id="c4d.CPolygon"></a>

Represents a polygon.

**Attributes**

## `c4d.CPolygon.a` <a id="c4d.CPolygon.a"></a>

Index of first point in the polygon.

**Type:** int

## `c4d.CPolygon.b` <a id="c4d.CPolygon.b"></a>

Index of second point in the polygon.

**Type:** int

## `c4d.CPolygon.c` <a id="c4d.CPolygon.c"></a>

Index of third point in the polygon.

**Type:** int

## `c4d.CPolygon.d` <a id="c4d.CPolygon.d"></a>

Index of optional fourth point in the polygon.

## Overview <a id="overview"></a>

**Magic Methods**

- [`CPolygon.__init__()`](#c4d.CPolygon.__init__)
- [`CPolygon.__str__()`](#c4d.CPolygon.__str__): Returns a string representation of the polygon object.

**Shape And Topology**

- [`CPolygon.EdgePoints()`](#c4d.CPolygon.EdgePoints): Retrieves the point indices for *edge*.
- [`CPolygon.Find()`](#c4d.CPolygon.Find): Checks if one of the polygon vertex indices is equal to *index* and returns the found polygon vertex number (*0*-*3*, equals `a` - `d`).
- [`CPolygon.FindEdge()`](#c4d.CPolygon.FindEdge): Checks if the vertex indices *index1* and *index2* form an edge in this polygon.
- [`CPolygon.IsTriangle()`](#c4d.CPolygon.IsTriangle): Checks if the polygon is a triangle.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.CPolygon-method-Magic-Methods"></a>

#### `CPolygon.__init__(self, t_a, t_b, t_c, t_d)` <a id="c4d.CPolygon.__init__"></a>

**Parameters:**

- **t_a** (*int*) – Index of first point in the polygon.
- **t_b** (*int*) – Index of second point in the polygon.
- **t_c** (*int*) – Index of third point in the polygon.
- **t_d** (*int*) – Index of optional fourth point in the polygon.

#### `CPolygon.__str__(self)` <a id="c4d.CPolygon.__str__"></a>

Returns a string representation of the polygon object.  
Called if [str()](https://docs.python.org/3.9/library/functions.html#func-str) is invoked on a [`CPolygon`](#c4d.CPolygon) object. See [object.__str__()](https://docs.python.org/3.9/reference/datamodel.html#object.__str__) for more information on Python’s data model.

**Return type:** str

**Returns:** The string representation of the polygon.

### Shape And Topology <a id="c4d.CPolygon-method-Shape-And-Topology"></a>

#### `CPolygon.EdgePoints(self, edge)` <a id="c4d.CPolygon.EdgePoints"></a>

Retrieves the point indices for *edge*.

*New in version R16.021.*

**Parameters:** **edge** (*int*) – The edge index (*0*-*3*).

**Return type:** Tuple[int, int]

**Returns:** The index of the first and second edge point.

#### `CPolygon.Find(self, index)` <a id="c4d.CPolygon.Find"></a>

Checks if one of the polygon vertex indices is equal to *index* and returns the found polygon vertex number (*0*-*3*, equals [`a`](#c4d.CPolygon.a) - [`d`](#c4d.CPolygon.d)).

*New in version R16.021.*

**Parameters:** **index** (*int*) – The vertex index to check.

**Return type:** int

**Returns:** The matching polygon vertex number (*0*-*3*, equals [`a`](#c4d.CPolygon.a) - [`d`](#c4d.CPolygon.d)). **NOTOK** is returned if there is no match.

#### `CPolygon.FindEdge(self, index1, index2)` <a id="c4d.CPolygon.FindEdge"></a>

Checks if the vertex indices *index1* and *index2* form an edge in this polygon. If so the polygon edge number is returned (*0*-*3*).

*New in version R16.021.*

**Parameters:**

- **index1** (*int*) – The vertex index of the first edge point.
- **index2** (*int*) – The vertex index of the second edge point.

**Return type:** int

**Returns:** The found polygon edge number (*0*-*3*). **NOTOK** is returned if there is no match.

#### `CPolygon.IsTriangle(self)` <a id="c4d.CPolygon.IsTriangle"></a>

Checks if the polygon is a triangle.

*New in version R16.021.*

**Return type:** bool

**Returns:** **True** if the polygon is a triangle, otherwise **False**.
