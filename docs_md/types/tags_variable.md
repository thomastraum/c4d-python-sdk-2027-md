<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/types/tags_variable.html -->

# Variable Tag Types <a id="variable-tag-types"></a>

The table lists the supported variable tags by `VariableTag.GetAllHighlevelData()`/`SetAllHighlevelData()` and their corresponding data.

| Tag | Data | Description |
|---|---|---|
| *Tpoint* | list of [`c4d.Vector`](../modules/c4d/Vector/index.md#c4d.Vector) | The points. |
| *Tpolygon* | list of [`c4d.CPolygon`](../modules/c4d/CPolygon/index.md#c4d.CPolygon) | The polygons. |
| *Ttangent* | list of ([`c4d.Vector`](../modules/c4d/Vector/index.md#c4d.Vector), [`c4d.Vector`](../modules/c4d/Vector/index.md#c4d.Vector)) | The tangents left and right interpolation. |
| *Tsegment* | list of dict{*cnt*: int, *closed*: bool} | The segments number of points and closed state. |
| *Tline* | list of dict{*pos*: float, *t*: float} | The line points percentage position and original spline point. |
| *Tvertexmap* | list of float | The vertex map values. |
| *Tnormal* | List[int]eger | The normals. Note: Contains *12* times more elements than `VariableTag.GetDataCount()` returns. |
| *Tvertexcolor* | list of dict{*a*, *b*, *c*, *d*: [`c4d.Vector4d`](../modules/c4d/Vector4d/index.md#c4d.Vector4d)} | The vertex colors for a polygon. |
| *Tsoftselection* | list of float | The soft selection values. |
