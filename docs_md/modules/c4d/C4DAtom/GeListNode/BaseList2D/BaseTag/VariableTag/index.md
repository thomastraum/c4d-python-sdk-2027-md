<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/index.html -->

# c4d.VariableTag <a id="c4d-variabletag"></a>

## *class* `c4d.VariableTag` <a id="c4d.VariableTag"></a>

A tag class that can store multiple elements with variable data size.

> **See also:** [Variable Tag Types](../../../../../../../types/tags_variable.md).

Parent Class:

- [`c4d.BaseTag`](../index.md#c4d.BaseTag)

Children Classes:

- [`c4d.SegmentTag`](SegmentTag/index.md#c4d.SegmentTag)
- [`c4d.TangentTag`](TangentTag/index.md#c4d.TangentTag)
- [`c4d.PointTag`](PointTag/index.md#c4d.PointTag)
- [`c4d.PolygonTag`](PolygonTag/index.md#c4d.PolygonTag)
- [`c4d.NormalTag`](NormalTag/index.md#c4d.NormalTag)
- [`c4d.UVWTag`](UVWTag/index.md#c4d.UVWTag)
- [`c4d.VertexColorTag`](VertexColorTag/index.md#c4d.VertexColorTag)

## Overview <a id="overview"></a>

**Buffer Access**

- [`VariableTag.GetLowlevelDataAddressR()`](#c4d.VariableTag.GetLowlevelDataAddressR): Gets the read-only buffer object for the variable tag’s data.
- [`VariableTag.GetLowlevelDataAddressW()`](#c4d.VariableTag.GetLowlevelDataAddressW): Gets the writable buffer object for the variable tag’s data.

**Data Dimensions**

- [`VariableTag.GetDataCount()`](#c4d.VariableTag.GetDataCount): Gets the number of data elements in the variable tag.
- [`VariableTag.GetDataSize()`](#c4d.VariableTag.GetDataSize): Gets the size of one data element in bytes.

**High-Level Data**

- [`VariableTag.GetAllHighlevelData()`](#c4d.VariableTag.GetAllHighlevelData): Gets the data for the variable tag.
- [`VariableTag.SetAllHighlevelData()`](#c4d.VariableTag.SetAllHighlevelData): Sets the data for the variable tag.

**Magic Methods**

- [`VariableTag.__init__()`](#c4d.VariableTag.__init__): Creates a [`VariableTag`](#c4d.VariableTag).

## Members <a id="members"></a>

### Buffer Access <a id="c4d.VariableTag-method-Buffer-Access"></a>

#### `VariableTag.GetLowlevelDataAddressR(self)` <a id="c4d.VariableTag.GetLowlevelDataAddressR"></a>

Gets the read-only buffer object for the variable tag’s data.

> **Warning:** Use with special care.

**Return type:** memoryview

**Returns:** The buffer object.

#### `VariableTag.GetLowlevelDataAddressW(self)` <a id="c4d.VariableTag.GetLowlevelDataAddressW"></a>

Gets the writable buffer object for the variable tag’s data.

> **Warning:** Use with special care. Only if the host tag is still alive.

**Return type:** memoryview

**Returns:** The buffer object.

### Data Dimensions <a id="c4d.VariableTag-method-Data-Dimensions"></a>

#### `VariableTag.GetDataCount(self)` <a id="c4d.VariableTag.GetDataCount"></a>

Gets the number of data elements in the variable tag.

> **Warning:** The **Tnormal** / [`NormalTag`](NormalTag/index.md#c4d.NormalTag) data contains *12* times more elements than [`GetDataCount()`](#c4d.VariableTag.GetDataCount) returns.

**Return type:** int

**Returns:** The number of data elements.

#### `VariableTag.GetDataSize(self)` <a id="c4d.VariableTag.GetDataSize"></a>

Gets the size of one data element in bytes.

**Return type:** int

**Returns:** The byte size of a data element.

### High-Level Data <a id="c4d.VariableTag-method-High-Level-Data"></a>

#### `VariableTag.GetAllHighlevelData(self)` <a id="c4d.VariableTag.GetAllHighlevelData"></a>

Gets the data for the variable tag.

The following code prints the weights from a vertex map tag.

```python
tag = op.GetTag(c4d.Tvertexmap)
if tag:
    print(tag.GetAllHighlevelData())
```

> **Note:** See warning in [`GetDataCount()`](#c4d.VariableTag.GetDataCount) for *Tnormal* / [`NormalTag`](NormalTag/index.md#c4d.NormalTag).

**Return type:** Any

**Returns:** The data for the variable tag. See table in [Variable Tag Types](../../../../../../../types/tags_variable.md).

#### `VariableTag.SetAllHighlevelData(self, data)` <a id="c4d.VariableTag.SetAllHighlevelData"></a>

Sets the data for the variable tag.

> **Note:** See warning in [`GetDataCount()`](#c4d.VariableTag.GetDataCount) for **Tnormal** / [`NormalTag`](NormalTag/index.md#c4d.NormalTag).

**Parameters:** **data** (*any*) – The data for the variable tag. See table in :doc:`/types/tags_variable`.

### Magic Methods <a id="c4d.VariableTag-method-Magic-Methods"></a>

#### `VariableTag.__init__(self, type, count)` <a id="c4d.VariableTag.__init__"></a>

Creates a [`VariableTag`](#c4d.VariableTag).

> **Note:** Use [`VariableTag`](#c4d.VariableTag) children classes to create a [`UVWTag`](UVWTag/index.md#c4d.UVWTag), [`NormalTag`](NormalTag/index.md#c4d.NormalTag), [`PointTag`](PointTag/index.md#c4d.PointTag) etc.

Here is how to create a vertex map tag and add it to the current polygon object.

```python
tag = c4d.VariableTag(c4d.Tvertexmap, op.GetPointCount())
op.InsertTag(tag)
c4d.EventAdd()
```

**Parameters:**

- **type** (*int*) –

  The variable tag type:

  The table lists the supported variable tags by `VariableTag.GetAllHighlevelData()`/`SetAllHighlevelData()` and their corresponding data.

  | Tag | Data | Description |
  |---|---|---|
  | *Tpoint* | list of [`c4d.Vector`](../../../../../Vector/index.md#c4d.Vector) | The points. |
  | *Tpolygon* | list of [`c4d.CPolygon`](../../../../../CPolygon/index.md#c4d.CPolygon) | The polygons. |
  | *Ttangent* | list of ([`c4d.Vector`](../../../../../Vector/index.md#c4d.Vector), [`c4d.Vector`](../../../../../Vector/index.md#c4d.Vector)) | The tangents left and right interpolation. |
  | *Tsegment* | list of dict{*cnt*: int, *closed*: bool} | The segments number of points and closed state. |
  | *Tline* | list of dict{*pos*: float, *t*: float} | The line points percentage position and original spline point. |
  | *Tvertexmap* | list of float | The vertex map values. |
  | *Tnormal* | List[int]eger | The normals. Note: Contains *12* times more elements than `VariableTag.GetDataCount()` returns. |
  | *Tvertexcolor* | list of dict{*a*, *b*, *c*, *d*: [`c4d.Vector4d`](../../../../../Vector4d/index.md#c4d.Vector4d)} | The vertex colors for a polygon. |
  | *Tsoftselection* | list of float | The soft selection values. |

- **count** (*int*) – The number of data elements in the tag.
