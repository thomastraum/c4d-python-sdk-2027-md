<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/volume/interface/maxon.PointsToVolumeListInterface.html -->

# maxon.PointsToVolumeListInterface <a id="maxon-pointstovolumelistinterface"></a>

## Description <a id="module-maxon.PointsToVolumeListInterface"></a><a id="description"></a>

Interface to convert point position to a volume.

## Inheritance diagram <a id="inheritance-diagram"></a>

Child Class:

- [`maxon.PointsToVolumeListRef`](../reference/maxon.PointsToVolumeListRef.md#module-maxon.PointsToVolumeListRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`AppendPoint`](#maxon.PointsToVolumeListInterface.AppendPoint)(position, radius, velocity) | Adds a point to the point list that will be converted to a volume. |
| [`GetCount`](#maxon.PointsToVolumeListInterface.GetCount)() | Returns the amount of points that were added to the point list. |

## Methods Definition <a id="methods-definition"></a>

### `PointsToVolumeListInterface.AppendPoint(position, radius, velocity)` <a id="maxon.PointsToVolumeListInterface.AppendPoint"></a>

Adds a point to the point list that will be converted to a volume.

**Parameters:**

- **position** (Union[[`maxon.Vector`](../../../datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector), [`c4d.Vector`](../../../../c4d/Vector/index.md#c4d.Vector)]) – The position of the point.
- **radius** (*float*) – The radius of the volume sphere that will be created around that point.
- **velocity** (Union[[`maxon.Vector`](../../../datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector), [`c4d.Vector`](../../../../c4d/Vector/index.md#c4d.Vector)]) – The velocity of the points for trails.

### `PointsToVolumeListInterface.GetCount()` <a id="maxon.PointsToVolumeListInterface.GetCount"></a>

Returns the amount of points that were added to the point list.

**Returns:** The amount of already added points.

**Return type:** int
