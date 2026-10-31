<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/LineObject/index.html -->

# c4d.LineObject <a id="c4d-lineobject"></a>

## *class* `c4d.LineObject` <a id="c4d.LineObject"></a>

Represents a Line object.

> **Note:**
>
> To access the line/segment data, retrieve the line/segment tag from the object and call `VariableTag.GetAllHighlevelData()`/`SetAllHighlevelData()`.  
> For instance, to print the line data from a line object use:
>
> ```python
> tag = op.GetTag(c4d.Tline)
> if tag:
>     print(tag.GetAllHighlevelData())
> ```

The instance object class of type *Oline*.

Parent Class:

- [`c4d.PointObject`](../index.md#c4d.PointObject)

## Overview <a id="overview"></a>

**Geometry Management**

- [`LineObject.GetSegmentCount()`](#c4d.LineObject.GetSegmentCount): Gets the number of segments.
- [`LineObject.Triangulate()`](#c4d.LineObject.Triangulate): Converts the line object into polygons.

**Magic Methods**

- [`LineObject.__init__()`](#c4d.LineObject.__init__): Creates a [`LineObject`](#c4d.LineObject).

## Members <a id="members"></a>

### Geometry Management <a id="c4d.LineObject-method-Geometry-Management"></a>

#### `LineObject.GetSegmentCount(self)` <a id="c4d.LineObject.GetSegmentCount"></a>

Gets the number of segments.

**Return type:** int

**Returns:** The number of elements in the segments array.

#### `LineObject.Triangulate(self, regular)` <a id="c4d.LineObject.Triangulate"></a>

Converts the line object into polygons.

**Parameters:** **regular** (*float*) – The size of polygons to fill the inside of the line object with. Pass *0.0* to connect the contour with no filling.

**Return type:** [c4d.PolygonObject](../PolygonObject/index.md#c4d.PolygonObject)

**Returns:** The created polygon object.

### Magic Methods <a id="c4d.LineObject-method-Magic-Methods"></a>

#### `LineObject.__init__(self, pcnt, scnt)` <a id="c4d.LineObject.__init__"></a>

Creates a [`LineObject`](#c4d.LineObject).

**Parameters:**

- **pcnt** (*int*) – The point count.
- **scnt** (*int*) – The segment count.
