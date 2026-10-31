<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/volume/datatype/maxon.VolumeConversionPolygon.html -->

# maxon.VolumeConversionPolygon <a id="maxon-volumeconversionpolygon"></a>

## Description <a id="module-maxon.VolumeConversionPolygon"></a><a id="description"></a>

Data used, to converts [`c4d.PolygonObject`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) to a Volume Polygon.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Struct`](../../../datatypes/base_core/maxon.Struct.md#module-maxon.Struct)
- [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.VolumeConversionPolygon.a`](maxon.VolumeConversionPolygon.a.md#maxon.VolumeConversionPolygon.a) | (int) Point index matching the `c4d.Cpolygon` |
| [`maxon.VolumeConversionPolygon.b`](maxon.VolumeConversionPolygon.b.md#maxon.VolumeConversionPolygon.b) | (int) Point index matching the `c4d.Cpolygon` |
| [`maxon.VolumeConversionPolygon.c`](maxon.VolumeConversionPolygon.c.md#maxon.VolumeConversionPolygon.c) | (int) Point index matching the `c4d.Cpolygon` |
| [`maxon.VolumeConversionPolygon.d`](maxon.VolumeConversionPolygon.d.md#maxon.VolumeConversionPolygon.d) | (int) Point index matching the `c4d.Cpolygon` |
| [`maxon.VolumeConversionPolygon.size`](maxon.VolumeConversionPolygon.size.md#maxon.VolumeConversionPolygon.size) | (int) Defines the number of point used in the polygon. |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`SetTriangle`](#maxon.VolumeConversionPolygon.SetTriangle)() | Defines the polygon as a triangle (d is no more used). |
| [`__getitem__`](#maxon.VolumeConversionPolygon.__getitem__)(index) | Retrieves the value of the *a*, *b*, *c* or *d* component of the polygon. |
| [`__init__`](#maxon.VolumeConversionPolygon.__init__)() | Initializes each index of the polygon to the value 4294967295. |
| [`__maxon_convert__`](#maxon.VolumeConversionPolygon.__maxon_convert__)(expected) |  |

## Methods Definition <a id="methods-definition"></a>

### `VolumeConversionPolygon.SetTriangle()` <a id="maxon.VolumeConversionPolygon.SetTriangle"></a>

Defines the polygon as a triangle (d is no more used).

### `VolumeConversionPolygon.__getitem__(index)` <a id="maxon.VolumeConversionPolygon.__getitem__"></a>

Retrieves the value of the *a*, *b*, *c* or *d* component of the polygon.  
The component is identified by an index in the interval *[0, 3]*.

**Parameters:** **index** (*int*) – The component index.

**Raises:** **IndexError** – When *index* does not satisfy *0 <= index < 3*.

**Return type:** float

**Returns:** The polygon component.

### `VolumeConversionPolygon.__init__()` <a id="maxon.VolumeConversionPolygon.__init__"></a>

Initializes each index of the polygon to the value 4294967295.

### `VolumeConversionPolygon.__maxon_convert__(expected)` <a id="maxon.VolumeConversionPolygon.__maxon_convert__"></a>
