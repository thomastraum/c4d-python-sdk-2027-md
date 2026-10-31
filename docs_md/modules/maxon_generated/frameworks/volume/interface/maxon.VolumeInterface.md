<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/volume/interface/maxon.VolumeInterface.html -->

# maxon.VolumeInterface <a id="maxon-volumeinterface"></a>

## Description <a id="module-maxon.VolumeInterface"></a><a id="description"></a>

[`maxon.VolumeInterface`](#module-maxon.VolumeInterface) represents a core volume object in cinema.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`ConvertToSpace`](#maxon.VolumeInterface.ConvertToSpace)(worldSpace) | Converts a vector-valued grid to world or local space depending on the bool input. |
| [`CreateFromFile`](#maxon.VolumeInterface.CreateFromFile)(url, scale, gridIndex) | Creates a new volume from a .vdb file. |
| [`GetActiveVoxelCount`](#maxon.VolumeInterface.GetActiveVoxelCount)() | Retrieve the active voxel count. |
| [`GetActiveVoxelDim`](#maxon.VolumeInterface.GetActiveVoxelDim)() | Retrieve the active voxel dimensions. |
| [`GetBackground`](#maxon.VolumeInterface.GetBackground)() | Retrieve the background value of the grid. |
| [`GetGridClass`](#maxon.VolumeInterface.GetGridClass)() | Retrieve the grid class of this grid. |
| [`GetGridName`](#maxon.VolumeInterface.GetGridName)() | Retrieve the grid name for this grid. |
| [`GetGridTransform`](#maxon.VolumeInterface.GetGridTransform)() | Retrieve the grid transform for this grid. |
| [`GetGridType`](#maxon.VolumeInterface.GetGridType)() | Retrieve the datatype of this grid. |
| [`GetMemUsage`](#maxon.VolumeInterface.GetMemUsage)() | Returns the amount of memory in bytes used by this volume. |
| [`GetMinMaxValues`](#maxon.VolumeInterface.GetMinMaxValues)([includeBackground]) | Returns the Min and Max values of the volume. |
| [`GetWorldBoundingBox`](#maxon.VolumeInterface.GetWorldBoundingBox)() | Retrieve the bounding box of all active voxels of this grid. |
| [`HasGrid`](#maxon.VolumeInterface.HasGrid)() | Retrieve if a grid is attached to this volume. |
| [`IsInWorldSpace`](#maxon.VolumeInterface.IsInWorldSpace)() | Returns True if the voxel values are already in world space. |
| [`LoadFromFile`](#maxon.VolumeInterface.LoadFromFile)(url, scale, gridIndex) | Loads a grid from .vdb file into this volume object. |
| [`MergeVolume`](#maxon.VolumeInterface.MergeVolume)(otherVolume[, keepOldVolume]) | Merges two volumes of same Type and Class. |
| [`SetGridClass`](#maxon.VolumeInterface.SetGridClass)(gridClass) | Set the grid class for this grid. |
| [`SetGridName`](#maxon.VolumeInterface.SetGridName)(name) | Set the grid name for this grid. |
| [`SetGridTransform`](#maxon.VolumeInterface.SetGridTransform)(newTransform) | Set the grid transform for this grid. |
| [`WriteToFile`](#maxon.VolumeInterface.WriteToFile)(url, scale, metaData) | Writes the attached grid to a .vdb file. |

## Methods Definition <a id="methods-definition"></a>

### `VolumeInterface.ConvertToSpace(worldSpace)` <a id="maxon.VolumeInterface.ConvertToSpace"></a>

Converts a vector-valued grid to world or local space depending on the bool input.

World-space means that the actual values of the grid are in world space and do not need to be additionally  
transformed when reading the data, but they need to be kept in sync with the grid’s transform.

> **Note:** No matter the underlying space, the returned values from the GridAccessor and GridIterator will be in world space.

**Parameters:** **worldSpace** (*bool*) – True to convert the vector grid values to world space, else local space.

### *static* `VolumeInterface.CreateFromFile(url, scale, gridIndex)` <a id="maxon.VolumeInterface.CreateFromFile"></a>

Creates a new volume from a .vdb file.

**Parameters:**

- **url** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – The url of the file.
- **scale** (*float*) – The scale to load the volume with.
- **gridIndex** (*int*) – The index of the grid in the file.

**Returns:** The created volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### `VolumeInterface.GetActiveVoxelCount()` <a id="maxon.VolumeInterface.GetActiveVoxelCount"></a>

Retrieve the active voxel count.

**Returns:** The amount of active voxels in this volume.

**Return type:** int

### `VolumeInterface.GetActiveVoxelDim()` <a id="maxon.VolumeInterface.GetActiveVoxelDim"></a>

Retrieve the active voxel dimensions.

**Returns:** The active voxel dimensions of this volume.

**Return type:** [`maxon.IntVector32`](../../../datatypes/vec_col_mat/maxon.IntVector32.md#module-maxon.IntVector32)

### `VolumeInterface.GetBackground()` <a id="maxon.VolumeInterface.GetBackground"></a>

Retrieve the background value of the grid.

**Returns:** The background value of the grid.

**Return type:** [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `VolumeInterface.GetGridClass()` <a id="maxon.VolumeInterface.GetGridClass"></a>

Retrieve the grid class of this grid.

**Returns:** The GRIDCLASS of this volume.

**Return type:**

`maxon.GRIDCLASS`

### `VolumeInterface.GetGridName()` <a id="maxon.VolumeInterface.GetGridName"></a>

Retrieve the grid name for this grid.

**Returns:** The name of this volume.

**Return type:** str

### `VolumeInterface.GetGridTransform()` <a id="maxon.VolumeInterface.GetGridTransform"></a>

Retrieve the grid transform for this grid.

**Returns:** The transformation matrix of this volume.

**Return type:** [`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix)

### `VolumeInterface.GetGridType()` <a id="maxon.VolumeInterface.GetGridType"></a>

Retrieve the datatype of this grid.

**Returns:** The GRIDTYPE of this volume.

**Return type:**

`maxon.GRIDTYPE`

### `VolumeInterface.GetMemUsage()` <a id="maxon.VolumeInterface.GetMemUsage"></a>

Returns the amount of memory in bytes used by this volume.

**Returns:** The memory usage in bytes.

**Return type:** int

### `VolumeInterface.GetMinMaxValues(includeBackground=False)` <a id="maxon.VolumeInterface.GetMinMaxValues"></a>

Returns the Min and Max values of the volume.  
If it is the first time being called the resulting values are being cached.  
Only works for numerical gridtypes.  
If the volume is a vector volume, the magnitude of the vectors will be used.

**Parameters:** **includeBackground** (*bool*) – If true the volume background will be part of the `maxon.Range`, otherwise not.

**Returns:** The Minimum and Maximum Value of this volume.

**Returns:**

`maxon.Range` ([`maxon.Float`](../../../datatypes/simple/maxon.Float.md#module-maxon.Float))

### `VolumeInterface.GetWorldBoundingBox()` <a id="maxon.VolumeInterface.GetWorldBoundingBox"></a>

Retrieve the bounding box of all active voxels of this grid.

**Returns:** The bounding box of the active voxels of this volume.

**Return type:**

`maxon.Range` ([`maxon.Vector`](../../../datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector))

### `VolumeInterface.HasGrid()` <a id="maxon.VolumeInterface.HasGrid"></a>

Retrieve if a grid is attached to this volume.

**Returns:** True if this volume holds a grid.

**Return type:** bool

### `VolumeInterface.IsInWorldSpace()` <a id="maxon.VolumeInterface.IsInWorldSpace"></a>

Returns True if the voxel values are already in world space.  
Return False if they are in local space (only relevant for vector grids).

**Return type:** bool

### `VolumeInterface.LoadFromFile(url, scale, gridIndex)` <a id="maxon.VolumeInterface.LoadFromFile"></a>

Loads a grid from .vdb file into this volume object.

**Parameters:**

- **url** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – The url of the file.
- **scale** (*float*) – The scale to load the volume with.
- **gridIndex** (*int*) – The index of the grid in the file.

### `VolumeInterface.MergeVolume(otherVolume, keepOldVolume=False)` <a id="maxon.VolumeInterface.MergeVolume"></a>

Merges two volumes of same Type and Class.

**Parameters:**

- **otherVolume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The volume to merge into the current one.
- **keepOldVolume** (*bool*) – If False the otherVolume will be flushed/emptied.

### `VolumeInterface.SetGridClass(gridClass)` <a id="maxon.VolumeInterface.SetGridClass"></a>

Set the grid class for this grid.

**Parameters:** **gridClass** (`maxon.GRIDCLASS`) – The GRIDCLASS to set for this volume.

### `VolumeInterface.SetGridName(name)` <a id="maxon.VolumeInterface.SetGridName"></a>

Set the grid name for this grid.

**Parameters:** **name** (*str*) – The name to set for this volume.

### `VolumeInterface.SetGridTransform(newTransform)` <a id="maxon.VolumeInterface.SetGridTransform"></a>

Set the grid transform for this grid.

**Parameters:** **newTransform** ([`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix)) – The transformation matrix to set for this volume.

### `VolumeInterface.WriteToFile(url, scale, metaData)` <a id="maxon.VolumeInterface.WriteToFile"></a>

Writes the attached grid to a .vdb file.

**Parameters:**

- **url** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – The url of the file.

- **scale** (*float*) – The scale to write the volume with.

- **metaData** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) –

  Optional meta data to write to the file.

  These need to be stored with a string key in the data dictionary.

- **metaData** –
