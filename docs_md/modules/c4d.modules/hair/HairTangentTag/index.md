<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/hair/HairTangentTag/index.html -->

# c4d.modules.hair.HairTangentTag <a id="c4d-modules-hair-hairtangenttag"></a>

## *class* `c4d.modules.hair.HairTangentTag` <a id="c4d.modules.hair.HairTangentTag"></a>

A variety of properties can be added to objects using tags.  
For example, adding smoothing (Phong tag) or preventing an object from being edited accidentally (Protection tag).

Parent Class:

- [`c4d.BaseTag`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)

## Overview <a id="overview"></a>

**Geometry Counts**

- [`HairTangentTag.GetCount()`](#c4d.modules.hair.HairTangentTag.GetCount): Gets the tangent count.
- [`HairTangentTag.GetPointCount()`](#c4d.modules.hair.HairTangentTag.GetPointCount): Gets the number of points.
- [`HairTangentTag.GetPolygonsSegments()`](#c4d.modules.hair.HairTangentTag.GetPolygonsSegments): Gets the number of polygon segments.
- [`HairTangentTag.GetSegments()`](#c4d.modules.hair.HairTangentTag.GetSegments): Gets the segment count.

**Magic Methods**

- [`HairTangentTag.__init__()`](#c4d.modules.hair.HairTangentTag.__init__)

**Tangent Data**

- [`HairTangentTag.GetTangents()`](#c4d.modules.hair.HairTangentTag.GetTangents): Returns a list of tangents.
- [`HairTangentTag.SetTangent()`](#c4d.modules.hair.HairTangentTag.SetTangent): Set a tangent.

## Members <a id="members"></a>

### Geometry Counts <a id="c4d.modules.hair.HairTangentTag-method-Geometry-Counts"></a>

#### `HairTangentTag.GetCount(self)` <a id="c4d.modules.hair.HairTangentTag.GetCount"></a>

Gets the tangent count.

**Return type:** int

**Returns:** Tangent count.

#### `HairTangentTag.GetPointCount(self)` <a id="c4d.modules.hair.HairTangentTag.GetPointCount"></a>

Gets the number of points.

**Return type:** int

**Returns:** Point count.

#### `HairTangentTag.GetPolygonsSegments(self)` <a id="c4d.modules.hair.HairTangentTag.GetPolygonsSegments"></a>

Gets the number of polygon segments.

**Return type:** int

**Returns:** Polygons segments count.

#### `HairTangentTag.GetSegments(self)` <a id="c4d.modules.hair.HairTangentTag.GetSegments"></a>

Gets the segment count.

**Return type:** int

**Returns:** Segment count.

### Magic Methods <a id="c4d.modules.hair.HairTangentTag-method-Magic-Methods"></a>

#### `HairTangentTag.__init__(self)` <a id="c4d.modules.hair.HairTangentTag.__init__"></a>

### Tangent Data <a id="c4d.modules.hair.HairTangentTag-method-Tangent-Data"></a>

#### `HairTangentTag.GetTangents(self)` <a id="c4d.modules.hair.HairTangentTag.GetTangents"></a>

Returns a list of tangents.

**Return type:** List[[c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The vector list.

#### `HairTangentTag.SetTangent(self, i, p)` <a id="c4d.modules.hair.HairTangentTag.SetTangent"></a>

Set a tangent.

**Parameters:**

- **i** (*int*) – The tangent index.
- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The tangent.

**Raises:** **IndexError** – If the tangent index *i* is out of range : *0<=i<*[`GetCount()`](#c4d.modules.hair.HairTangentTag.GetCount).
