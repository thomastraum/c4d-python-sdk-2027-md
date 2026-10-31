<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/index.html -->

# c4d.PointObject <a id="c4d-pointobject"></a>

## *class* `c4d.PointObject` <a id="c4d.PointObject"></a>

This is an abstract baseclass.

Parent Class:

- [`c4d.BaseObject`](../index.md#c4d.BaseObject)

Children Classes:

- [`c4d.PolygonObject`](PolygonObject/index.md#c4d.PolygonObject)
- [`c4d.LineObject`](LineObject/index.md#c4d.LineObject)
- [`c4d.SplineObject`](SplineObject/index.md#c4d.SplineObject)
- [`c4d.ParticleGroupObject`](ParticleGroupObject/index.md#c4d.ParticleGroupObject)

## Overview <a id="overview"></a>

**Collection Structure**

- [`PointObject.GetPointCount()`](#c4d.PointObject.GetPointCount): Return the number of points.
- [`PointObject.ResizeObject()`](#c4d.PointObject.ResizeObject): Changes the number of points in the point object.

**Coordinates And Weights**

- [`PointObject.CalcVertexMap()`](#c4d.PointObject.CalcVertexMap): Get an array of vertex weights.
- [`PointObject.GetAllPoints()`](#c4d.PointObject.GetAllPoints): Return all point positions.
- [`PointObject.GetPoint()`](#c4d.PointObject.GetPoint): Get the position of a point.
- [`PointObject.SetAllPoints()`](#c4d.PointObject.SetAllPoints): Set all points of the point object.
- [`PointObject.SetPoint()`](#c4d.PointObject.SetPoint): Set the position of a point.

**Visibility And Selection**

- [`PointObject.GetPointH()`](#c4d.PointObject.GetPointH): Return the hidden points.
- [`PointObject.GetPointS()`](#c4d.PointObject.GetPointS): Return the selected points.

## Members <a id="members"></a>

### Collection Structure <a id="c4d.PointObject-method-Collection-Structure"></a>

#### `PointObject.GetPointCount(self)` <a id="c4d.PointObject.GetPointCount"></a>

Return the number of points.

**Return type:** int

**Returns:** The number of points.

#### `PointObject.ResizeObject(self, pcnt)` <a id="c4d.PointObject.ResizeObject"></a>

Changes the number of points in the point object.

**Parameters:** **pcnt** (*int*) – The new number of points.

**Return type:** bool

**Returns:** Success of changing the number of points.

### Coordinates And Weights <a id="c4d.PointObject-method-Coordinates-And-Weights"></a>

#### `PointObject.CalcVertexMap(self, modifier)` <a id="c4d.PointObject.CalcVertexMap"></a>

Get an array of vertex weights.

*Changed in version R19.053:* Previous name was *CalcVertexmap* (still works for backward compatibility).

**Parameters:** **modifier** ([*c4d.BaseObject*](../index.md#c4d.BaseObject)) – The modifier object.

**Return type:** Optional[List[float]]

**Returns:** The list of weights, or **None** if failed.

#### `PointObject.GetAllPoints(self)` <a id="c4d.PointObject.GetAllPoints"></a>

Return all point positions.

**Return type:** List[[c4d.Vector](../../../../../Vector/index.md#c4d.Vector)]

**Returns:** The list of positions.

#### `PointObject.GetPoint(self, id)` <a id="c4d.PointObject.GetPoint"></a>

Get the position of a point.

**Parameters:** **id** (*int*) – The point index.

**Raises:** **IndexError** – If the point index *id* is out of range : *0<=id<*[`GetPointCount()`](#c4d.PointObject.GetPointCount).

**Return type:** [c4d.Vector](../../../../../Vector/index.md#c4d.Vector)

**Returns:** The position of the point.

#### `PointObject.SetAllPoints(self, p)` <a id="c4d.PointObject.SetAllPoints"></a>

Set all points of the point object.  
The length of the passed list object must be equal the count of points.

> **Note:** Call `obj.Message` (*c4d.MSG_UPDATE*) after you set all your points to update the object.

**Parameters:** **p** (*List*[[*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)]) – The list of positions.

#### `PointObject.SetPoint(self, id, pos)` <a id="c4d.PointObject.SetPoint"></a>

Set the position of a point.

> **Note:** Call `obj.Message` (*c4d.MSG_UPDATE*) after you set all your points to update the object.

**Parameters:**

- **id** (*int*) – The point index.
- **pos** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The position of the point.

**Raises:** **IndexError** – If the point index *id* is out of range : *0<=id<*[`GetPointCount()`](#c4d.PointObject.GetPointCount).

### Visibility And Selection <a id="c4d.PointObject-method-Visibility-And-Selection"></a>

#### `PointObject.GetPointH(self)` <a id="c4d.PointObject.GetPointH"></a>

Return the hidden points.

**Return type:** [c4d.BaseSelect](../../../../../BaseSelect/index.md#c4d.BaseSelect)

**Returns:** The hidden points.

#### `PointObject.GetPointS(self)` <a id="c4d.PointObject.GetPointS"></a>

Return the selected points.

**Return type:** [c4d.BaseSelect](../../../../../BaseSelect/index.md#c4d.BaseSelect)

**Returns:** The selected points.
