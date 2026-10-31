<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/volume/interface/maxon.GridAccessorCreationInterface.html -->

# maxon.GridAccessorCreationInterface <a id="maxon-gridaccessorcreationinterface"></a>

## Description <a id="module-maxon.GridAccessorCreationInterface"></a><a id="description"></a>

Helper class to create the templated interface [`maxon.GridAccessorInterface`](maxon.GridAccessorInterface.md#module-maxon.GridAccessorInterface).

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to use this class directly.  
> Instead create a Reference and use [`maxon.GridAccessorRef`](../reference/maxon.GridAccessorRef.md#module-maxon.GridAccessorRef).

## Inheritance diagram <a id="inheritance-diagram"></a>

Child Class:

- [`maxon.GridAccessorRef`](../reference/maxon.GridAccessorRef.md#module-maxon.GridAccessorRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetActiveState`](#maxon.GridAccessorCreationInterface.GetActiveState)(coords) | Retrieve the active state of a voxel at a voxel index. |
| [`GetCoords`](#maxon.GridAccessorCreationInterface.GetCoords)(position) | Retrieve the sub voxel index position of the volume at the given world position. |
| [`GetValue`](#maxon.GridAccessorCreationInterface.GetValue)(coords) | _GetValue(coords) Retrieve the value of the volume at the given world position. |
| [`Init`](#maxon.GridAccessorCreationInterface.Init)(volume[, sampler]) | Initialize the accessor with a volume object in a read only state. |
| [`InitWithWriteAccess`](#maxon.GridAccessorCreationInterface.InitWithWriteAccess)(volume[, sampler]) | Initialize the accessor with a volume object with both read and write access. |
| [`SetActiveState`](#maxon.GridAccessorCreationInterface.SetActiveState)(coords, state) | Sets the active state of a voxel at a voxel index. |
| [`SetSampler`](#maxon.GridAccessorCreationInterface.SetSampler)(sampler) | Changes the sampler Type. |
| [`SetValue`](#maxon.GridAccessorCreationInterface.SetValue)(coords, val) | _SetValue(coords, val) Sets a voxel value at a voxel index. |
| [`SetValueOnly`](#maxon.GridAccessorCreationInterface.SetValueOnly)(coords, val) | Sets a voxel value at a voxel index. |

## Methods Definition <a id="methods-definition"></a>

### `GridAccessorCreationInterface.GetActiveState(coords)` <a id="maxon.GridAccessorCreationInterface.GetActiveState"></a>

Retrieve the active state of a voxel at a voxel index.

**Parameters:** **coords** ([`maxon.Vector`](../../../datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector)) – The voxel index at which the active state will be checked.

**Returns:** The active state of the voxel at that voxel index.

**Return type:** bool

### `GridAccessorCreationInterface.GetCoords(position)` <a id="maxon.GridAccessorCreationInterface.GetCoords"></a>

Retrieve the sub voxel index position of the volume at the given world position.

> **Note:** This value depends on the [`maxon.VOLUMESAMPLER`](../../../enums/maxon.VOLUMESAMPLER.md#module-maxon.VOLUMESAMPLER) that was set.

**Parameters:** **position** (Union[[`maxon.Vector`](../../../datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector), [`c4d.Vector`](../../../../c4d/Vector/index.md#c4d.Vector)]) – The world position at which the sub voxel index position should be retrieved.

**Returns:** The sub voxel index position at the passed position.

**Return type:** [`maxon.Vector`](../../../datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector)

### `GridAccessorCreationInterface.GetValue(coords)` <a id="maxon.GridAccessorCreationInterface.GetValue"></a>

_GetValue(coords) Retrieve the value of the volume at the given world position.

> **Note:** This value depends on the VOLUMESAMPLER that was set.

**Parameters:** **coords** (Union[[`maxon.Vector`](../../../datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector), [`c4d.Vector`](../../../../c4d/Vector/index.md#c4d.Vector)]) – The world position at which the data should be retrieved.

**Returns:** The voxel value at the world position.

**Return type:** Any

### `GridAccessorCreationInterface.Init(volume, sampler=maxon.VOLUMESAMPLER.NEAREST)` <a id="maxon.GridAccessorCreationInterface.Init"></a>

Initialize the accessor with a volume object in a read only state.

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The volume object to initialize this accessor for.
- **sampler** ([`maxon.VOLUMESAMPLER`](../../../enums/maxon.VOLUMESAMPLER.md#module-maxon.VOLUMESAMPLER)) – The used sampler for position sampling

### `GridAccessorCreationInterface.InitWithWriteAccess(volume, sampler=maxon.VOLUMESAMPLER.NEAREST)` <a id="maxon.GridAccessorCreationInterface.InitWithWriteAccess"></a>

Initialize the accessor with a volume object with both read and write access.

*New in version R21.*

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The volume object to initialize this accessor for.
- **sampler** ([`maxon.VOLUMESAMPLER`](../../../enums/maxon.VOLUMESAMPLER.md#module-maxon.VOLUMESAMPLER)) – The used sampler for position sampling

### `GridAccessorCreationInterface.SetActiveState(coords, state)` <a id="maxon.GridAccessorCreationInterface.SetActiveState"></a>

Sets the active state of a voxel at a voxel index.

**Parameters:**

- **coords** ([`maxon.Vector`](../../../datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector)) – The voxel index at which the active state will be set.
- **state** (*bool*) – The state to set, true means active, false inactive.

### `GridAccessorCreationInterface.SetSampler(sampler)` <a id="maxon.GridAccessorCreationInterface.SetSampler"></a>

Changes the sampler Type.

**Parameters:** **sampler** ([`maxon.VOLUMESAMPLER`](../../../enums/maxon.VOLUMESAMPLER.md#module-maxon.VOLUMESAMPLER)) – The used sampler for position sampling.

### `GridAccessorCreationInterface.SetValue(coords, val)` <a id="maxon.GridAccessorCreationInterface.SetValue"></a>

_SetValue(coords, val) Sets a voxel value at a voxel index.

> **Note:** This will activate a voxel

**Parameters:**

- **coords** ([`maxon.Vector`](../../../datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector)) – The voxel index at which the value will be set.
- **val** (*Any*) – The value to set.

### `GridAccessorCreationInterface.SetValueOnly(coords, val)` <a id="maxon.GridAccessorCreationInterface.SetValueOnly"></a>

Sets a voxel value at a voxel index.

> **Note:** Same as `maxon.GridAccessorCreationInterface._SetValue()`, but this will not activate a voxel

**Parameters:**

- **coords** ([`maxon.Vector`](../../../datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector)) – The voxel index at which the value will be set.
- **val** (*Any*) – The value to set.
