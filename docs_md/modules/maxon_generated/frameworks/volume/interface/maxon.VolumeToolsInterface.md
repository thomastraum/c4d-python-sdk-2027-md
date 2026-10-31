<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/volume/interface/maxon.VolumeToolsInterface.html -->

# maxon.VolumeToolsInterface <a id="maxon-volumetoolsinterface"></a>

## Description <a id="module-maxon.VolumeToolsInterface"></a><a id="description"></a>

[`maxon.VolumeToolsInterface`](#module-maxon.VolumeToolsInterface) provides methods to process volumes.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`ApplyFilterToVolume`](#maxon.VolumeToolsInterface.ApplyFilterToVolume)(volume, filterType, thread) | Applies a filter operation to any volume. |
| [`ApplySDFFilterToVolume`](#maxon.VolumeToolsInterface.ApplySDFFilterToVolume)(volume, filterType, …) | Applies a filter operation to a SDF volume. |
| [`BoolVolumes`](#maxon.VolumeToolsInterface.BoolVolumes)(voumeOne, volumeTwo, type) | Bools two SDF volumes into one with a given bool type of `maxon.BOOLTYPE`. |
| [`ConvertFogToSDF`](#maxon.VolumeToolsInterface.ConvertFogToSDF)(volume, iso, thread) | Convert a fog Volume to a SDF volume. |
| [`ConvertSDFToFog`](#maxon.VolumeToolsInterface.ConvertSDFToFog)(volume, cutoff) | Convert a SDF Volume to a fog volume. |
| [`ConvertVectorToFog`](#maxon.VolumeToolsInterface.ConvertVectorToFog)(volume, thread) | Convert a vector volume to a fog volume. |
| [`CreateCurlVolume`](#maxon.VolumeToolsInterface.CreateCurlVolume)(volume, thread) | Creates a vector volume representing the curl of a vector volume. |
| [`CreateGradientVolume`](#maxon.VolumeToolsInterface.CreateGradientVolume)(volume, thread) | Creates a gradient volume from a numeric volume. |
| [`CreateMeanCurvatureVolume`](#maxon.VolumeToolsInterface.CreateMeanCurvatureVolume)(*args) | NormalizeVectorVolume(volume, thread) Creates a curvature volume from a numeric volume. |
| [`CreateNewFloat32Volume`](#maxon.VolumeToolsInterface.CreateNewFloat32Volume)(background) | Creates a new float volume with default transform. |
| [`CreateNewVector32Volume`](#maxon.VolumeToolsInterface.CreateNewVector32Volume)(background) | Creates a new float vector volume with default transform. |
| [`CreatePlatonicVolume`](#maxon.VolumeToolsInterface.CreatePlatonicVolume)(sides, size, position, …) | Creates a SDF volume of a platonic shape. |
| [`CreateSphereVolume`](#maxon.VolumeToolsInterface.CreateSphereVolume)(radius, position, …[, …]) | Creates a SDF volume of a spherical shape. |
| [`GetGridNamesFromFile`](#maxon.VolumeToolsInterface.GetGridNamesFromFile)(filename) | Read and return the gridnames from a .vdb file. |
| [`GetMetaDataFromFile`](#maxon.VolumeToolsInterface.GetMetaDataFromFile)(filename) | Read and return the metadata from a .vdb file. |
| [`LoadAllGridsIntoVolumes`](#maxon.VolumeToolsInterface.LoadAllGridsIntoVolumes)(filename, scale, …) | Loads all grids into a list of volumes from a .vdb file. |
| [`LoadGridIntoVolume`](#maxon.VolumeToolsInterface.LoadGridIntoVolume)(filename, scale, …) | Loads a grid into a volume from a .vdb file. |
| [`LoadVDBFile`](#maxon.VolumeToolsInterface.LoadVDBFile)(filename, scale, gridNames, …) | Loads volumes from a .vdb file. |
| [`MeshToVolume`](#maxon.VolumeToolsInterface.MeshToVolume)(vertices, polygons, …[, …]) | Converts a polygon object to a SDF volume. |
| [`MixVectorVolumes`](#maxon.VolumeToolsInterface.MixVectorVolumes)(volumeOne, volumeTwo, type) | Mix two volumes into one with a given mix type of `maxon.MIXVECTORTYPE`. |
| [`MixVolumes`](#maxon.VolumeToolsInterface.MixVolumes)(volumeOne, volumeTwo, type) | Mix two volumes into one with a given mix type of `maxon.MIXTYPE`. |
| [`NormalizeVectorVolume`](#maxon.VolumeToolsInterface.NormalizeVectorVolume)(volume, thread) | Creates a normalized vector volume from an input vector volume. |
| [`PointsToVolume`](#maxon.VolumeToolsInterface.PointsToVolume)(pointObjects, gridSize, …) | Converts points in space to a SDF volume. |
| [`ResampleVolume`](#maxon.VolumeToolsInterface.ResampleVolume)(volume, resampleTransform, …) | Resample a volume into a new transformation matrix. |
| [`RotateVectorVolume`](#maxon.VolumeToolsInterface.RotateVectorVolume)(volume, rotationAxis, …) | Rotate the vectors of a vector volume by a specified angle around a rotation axis. |
| [`SaveVDBFile`](#maxon.VolumeToolsInterface.SaveVDBFile)(filename, scale, volumes, metaData) | Saves volumes to a .vdb file. |
| [`VolumeToMesh`](#maxon.VolumeToolsInterface.VolumeToMesh)(volume, iso, adaptiveValue) | Extracts a polygon object iso surface from a volume. |

## Methods Definition <a id="methods-definition"></a>

### *static* `VolumeToolsInterface.ApplyFilterToVolume(volume, filterType, thread, maskVolume=None, maskField=None)` <a id="maxon.VolumeToolsInterface.ApplyFilterToVolume"></a>

Applies a filter operation to any volume.

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The volume that should be filtered.
- **filterType** ([`maxon.FilterSettings`](../datatype/maxon.FilterSettings.md#module-maxon.FilterSettings)) – Settings for the filter operation
- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.
- **maskVolume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – An optional volume object to be used as mask.
- **maskField** ([`maxon.FieldSampleData`](../datatype/maxon.FieldSampleData.md#module-maxon.FieldSampleData)) – An optional field data struct to be used as field mask.

**Returns:** A new filtered version of the input volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.ApplySDFFilterToVolume(volume, filterType, thread, maskVolume=None, maskField=None)` <a id="maxon.VolumeToolsInterface.ApplySDFFilterToVolume"></a>

Applies a filter operation to a SDF volume.

> **Warning:** This work only on SDF volumes.

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The volume that should be filtered.
- **filterType** ([`maxon.SDFFilterSettings`](../datatype/maxon.SDFFilterSettings.md#module-maxon.SDFFilterSettings)) – Settings for the filter operation
- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.
- **maskVolume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – An optional volume object to be used as mask.
- **maskField** ([`maxon.FieldSampleData`](../datatype/maxon.FieldSampleData.md#module-maxon.FieldSampleData)) – An optional field data struct to be used as field mask.

**Returns:** A new filtered version of the input volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.BoolVolumes(voumeOne, volumeTwo, type)` <a id="maxon.VolumeToolsInterface.BoolVolumes"></a>

Bools two SDF volumes into one with a given bool type of `maxon.BOOLTYPE`.

> **Note:** This methods only works for SDF volume, for FOG volume, use [`maxon.VolumeToolsInterface.MixVolumes()`](#maxon.VolumeToolsInterface.MixVolumes)

**Parameters:**

- **voumeOne** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The first SDF volume for the boolean operation.
- **volumeTwo** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The second SDF volume for the boolean operation.
- **type** (`maxon.BOOLTYPE`.) – The bool type.

**Returns:** The booled volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.ConvertFogToSDF(volume, iso, thread)` <a id="maxon.VolumeToolsInterface.ConvertFogToSDF"></a>

Convert a fog Volume to a SDF volume.

> **Note:** The resulting surface of the SDF volume is defined by the passed iso value.

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The fog volume that should be converted.
- **iso** (*float*) – The iso value at which the surface should be created.
- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.

**Returns:** A SDF volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.ConvertSDFToFog(volume, cutoff)` <a id="maxon.VolumeToolsInterface.ConvertSDFToFog"></a>

Convert a SDF Volume to a fog volume.

> **Note:** The interior of the SDF object will be filled with data ranging from 0.0 to 1.0 with a falloff.

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The SDF volume that should be converted.
- **cutoff** (*float*) – The distance for the falloff from 0.0 (SDF 0.0 value) to 1.0.

**Returns:** A fog volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.ConvertVectorToFog(volume, thread)` <a id="maxon.VolumeToolsInterface.ConvertVectorToFog"></a>

Convert a vector volume to a fog volume.

*New in version R21.*

> **Note:** The resulting volume will have the length of the vectors stored at the original voxel position.

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The fog volume that should be converted.
- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.

**Returns:** A fog volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.CreateCurlVolume(volume, thread)` <a id="maxon.VolumeToolsInterface.CreateCurlVolume"></a>

Creates a vector volume representing the curl of a vector volume.

*New in version R21.*

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The vector volume the curl should be calculated from.
- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.

**Returns:** The newly created curl volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.CreateGradientVolume(volume, thread)` <a id="maxon.VolumeToolsInterface.CreateGradientVolume"></a>

Creates a gradient volume from a numeric volume.

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The numeric volume.
- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.

**Returns:** The newly created gradient volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.CreateMeanCurvatureVolume(*args)` <a id="maxon.VolumeToolsInterface.CreateMeanCurvatureVolume"></a>

NormalizeVectorVolume(volume, thread) Creates a curvature volume from a numeric volume.

*New in version R21.*

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The numeric volume.
- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.

**Returns:** The newly created curvature volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.CreateNewFloat32Volume(background)` <a id="maxon.VolumeToolsInterface.CreateNewFloat32Volume"></a>

Creates a new float volume with default transform.

> **Note:** The gridtype will be `c4d.GRIDCLASS_UNKNOWN`.

**Parameters:** **background** (*float*) – The background value for the volume.

**Returns:** The newly created volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.CreateNewVector32Volume(background)` <a id="maxon.VolumeToolsInterface.CreateNewVector32Volume"></a>

Creates a new float vector volume with default transform.

*New in version R21.*

> **Note:** The gridtype will be `c4d.GRIDCLASS_UNKNOWN`.

**Parameters:** **background** ([`maxon.Vector32`](../../../datatypes/vec_col_mat/maxon.Vector32.md#module-maxon.Vector32)) – The background vector value for the volume.

**Returns:** The newly created volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *classmethod* `VolumeToolsInterface.CreatePlatonicVolume(sides, size, position, gridSize, bandWidth, thread, creationTransform=None)` <a id="maxon.VolumeToolsInterface.CreatePlatonicVolume"></a>

Creates a SDF volume of a platonic shape.

> **Note:** If invalid Arguments are set the function returns an empty volume.

**Parameters:**

- **sides** (*int*) –

  The number of sides of the platonic.

  Define the valid Arguments in the description of the parameter

- **size** (*float*) – The size of the created platonic.

- **position** (Union[[`maxon.Vector`](../../../datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector), [`c4d.Vector`](../../../../c4d/Vector/index.md#c4d.Vector)]) – The position of the platonic.

- **gridSize** (*float*) – The desired gridsize of the created volume.

- **bandWidth** (*int*) –

  The amount of interior and exterior voxels that distance information is calculated for.

  Should be greater than 1.

- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.

- **creationTransform** ([`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix)) – An optional override to the target grid matrix.

**Returns:** The created SDF volume representing the input platonic settings.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.CreateSphereVolume(radius, position, gridSize, bandWidth, thread, creationTransform=None)` <a id="maxon.VolumeToolsInterface.CreateSphereVolume"></a>

Creates a SDF volume of a spherical shape.

**Parameters:**

- **radius** – The radius of the created sphere.

- **radius** – float

- **position** – The position of the sphere.

- **position** – Union[[`maxon.Vector`](../../../datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector), [`c4d.Vector`](../../../../c4d/Vector/index.md#c4d.Vector)]

- **gridSize** – The desired gridsize of the created volume.

- **gridSize** – float

- **bandWidth** –

  The amount of interior and exterior voxels that distance information is calculated for.

  Should be greater than 1.

- **bandWidth** – int

- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.

- **creationTransform** ([`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix)) – An optional override to the target grid matrix.

**Returns:** The created SDF volume representing the input sphere settings.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.GetGridNamesFromFile(filename)` <a id="maxon.VolumeToolsInterface.GetGridNamesFromFile"></a>

Read and return the gridnames from a .vdb file.

**Parameters:** **filename** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – The url of the file.

**Returns:** A data dictionary with metadata stored under string keys.

**Return type:** [`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)

### *static* `VolumeToolsInterface.GetMetaDataFromFile(filename)` <a id="maxon.VolumeToolsInterface.GetMetaDataFromFile"></a>

Read and return the metadata from a .vdb file.

**Parameters:** **filename** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – The url of the file.

**Returns:** A data dictionary with metadata stored under string keys.

**Return type:** [`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)

### *static* `VolumeToolsInterface.LoadAllGridsIntoVolumes(filename, scale, volume, metaData)` <a id="maxon.VolumeToolsInterface.LoadAllGridsIntoVolumes"></a>

Loads all grids into a list of volumes from a .vdb file.

**Parameters:**

- **filename** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – The url of the file to load from.
- **scale** (*float*) – A scale factor for loading the grids.
- **volume** ([`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)]) – The output list of loaded volumes.
- **metaData** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – If passed, will be filled with the metadata from the file.

### *static* `VolumeToolsInterface.LoadGridIntoVolume(filename, scale, gridIndex, volume, metaData)` <a id="maxon.VolumeToolsInterface.LoadGridIntoVolume"></a>

Loads a grid into a volume from a .vdb file.

**Parameters:**

- **filename** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – The url of the file to load from.
- **scale** (*float*) – A scale factor for loading the grids.
- **gridIndex** (*int*) – The index of the grid in the .vdb file.
- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The volume reference to load the grid into.
- **metaData** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – If passed, will be filled with the metadata from the file.

### *static* `VolumeToolsInterface.LoadVDBFile(filename, scale, gridNames, gridIndices, metaData)` <a id="maxon.VolumeToolsInterface.LoadVDBFile"></a>

Loads volumes from a .vdb file.

**Parameters:**

- **filename** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – The url of the file to load from.
- **scale** (*float*) – A scale factor for loading the grids.
- **gridNames** ([`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String)]) – If a [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) is passed, it will be filled with the grid names.
- **gridIndices** ([`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.Int`](../../../datatypes/simple/maxon.Int.md#module-maxon.Int)]) – Optional list of indices that should be loaded from the file.
- **metaData** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – If passed, will be filled with the metadata from the file.

**Returns:** A list of volumes that were loaded from the .vdb file.

**Return type:** [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)]

### *classmethod* `VolumeToolsInterface.MeshToVolume(vertices, polygons, polygonObjectMatrix, gridSize, bandWidthInterior, bandWidthExterior, thread, conversionSettings=maxon.POLYGONCONVERSIONFLAGS.NONE, creationTransform=None)` <a id="maxon.VolumeToolsInterface.MeshToVolume"></a>

Converts a polygon object to a SDF volume.

**Parameters:**

- **vertices** ([`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [`maxon.Vecor`]) – The vertex positions of the polygon object.

- **polygons** ([`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.VolumeConversionPolygon`](../datatype/maxon.VolumeConversionPolygon.md#module-maxon.VolumeConversionPolygon)]) – The polygon information.

- **polygonObjectMatrix** ([`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix)) – The global position, scale and rotation matrix of the polygon object.

- **gridSize** (*float*) – The desired gridsize of the created volume.

- **bandWidthInterior** (*int*) – The amount of exterior voxels that distance information is calculated for.

- **bandWidthExterior** (*int*) – The amount of interior voxels that distance information is calculated for.

- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.

- **conversionSettings** ([`maxon.POLYGONCONVERSIONFLAGS`](../../../enums/maxon.POLYGONCONVERSIONFLAGS.md#module-maxon.POLYGONCONVERSIONFLAGS)) – Optional settings for the conversion to Volume

- **creationTransform** –

  An optional override to the target grid matrix.

  If this is used the *gridSize* is ignored.

- **creationTransform** – [`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix)

**Returns:** The converted SDF volume representing the input polygon object.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.MixVectorVolumes(volumeOne, volumeTwo, type)` <a id="maxon.VolumeToolsInterface.MixVectorVolumes"></a>

Mix two volumes into one with a given mix type of `maxon.MIXVECTORTYPE`.

*New in version R21.*

**Parameters:**

- **volumeOne** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The first vector volume for the mix operation.
- **volumeTwo** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The second vector volume for the mix operation.
- **type** (`maxon.MIXVECTORTYPE`.) – The mix type.

**Returns:** The mixed vector volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.MixVolumes(volumeOne, volumeTwo, type)` <a id="maxon.VolumeToolsInterface.MixVolumes"></a>

Mix two volumes into one with a given mix type of `maxon.MIXTYPE`.

**Parameters:**

- **volumeOne** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The first volume for the mix operation.
- **volumeTwo** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The second volume for the mix operation.
- **type** (`maxon.MIXTYPE`.) – The mix type.

**Returns:** The mixed volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.NormalizeVectorVolume(volume, thread)` <a id="maxon.VolumeToolsInterface.NormalizeVectorVolume"></a>

Creates a normalized vector volume from an input vector volume.

*New in version R21.*

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The vector volume that should be normalized.
- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.

**Returns:** The newly created normalized vector volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.PointsToVolume(pointObjects, gridSize, bandWidth, thread, creationTransform=None, velocityScale=0.0)` <a id="maxon.VolumeToolsInterface.PointsToVolume"></a>

Converts points in space to a SDF volume.  
This can be used to convert particles, vertices, spline sampling points or other points to a volume.

**Parameters:**

- **pointObjects** – A list of Delegate/Object pairs that specify how to get point positions from the object.

- **gridSize** (*float*) – The desired gridsize of the created volume.

- **bandWidth** (*int*) – The amount of voxels around the creates spheres that distance information is calculated for.

- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.

- **creationTransform** ([`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix)) –

  An optional override to the target grid matrix.

  If this is used the *gridSize* is ignored.

- **velocityScale** (*float*) – A velocity scale that the volumes will be extended to if they have a direction set.

**Returns:** The converted SDF volume representing the input polygon object.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.ResampleVolume(volume, resampleTransform, interpolationType, thread)` <a id="maxon.VolumeToolsInterface.ResampleVolume"></a>

Resample a volume into a new transformation matrix.

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The volume that should be resampled.
- **resampleTransform** ([`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix)) – The transformation matrix in which the volume should be resampled into.
- **interpolationType** ([`maxon.RESAMPLEINTERPOLATIONTYPE`](../../../enums/maxon.RESAMPLEINTERPOLATIONTYPE.md#module-maxon.RESAMPLEINTERPOLATIONTYPE)) – The resample interpolation type.
- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.

**Returns:** The created resampled volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.RotateVectorVolume(volume, rotationAxis, angle, thread, maskField=None)` <a id="maxon.VolumeToolsInterface.RotateVectorVolume"></a>

Rotate the vectors of a vector volume by a specified angle around a rotation axis.

*New in version R21.*

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The vector volume to rotate.
- **rotationAxis** ([`maxon.Vector`](../../../datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector)) – The rotation axis to rotate around.
- **angle** (*float*) – The angle in radians to rotate.
- **thread** ([`maxon.ThreadRef`](../../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)) – A thread reference that cancellation is tested against.
- **maskField** ([`maxon.FieldSampleData`](../datatype/maxon.FieldSampleData.md#module-maxon.FieldSampleData)) – An optional field data struct to be used as field mask.

**Returns:** The newly created curvature volume.

**Return type:** [`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

### *static* `VolumeToolsInterface.SaveVDBFile(filename, scale, volumes, metaData)` <a id="maxon.VolumeToolsInterface.SaveVDBFile"></a>

Saves volumes to a .vdb file.

**Parameters:**

- **filename** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – The url of the file to save to.

- **scale** (*float*) – A scale factor for saving the grids.

- **volumes** ([`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)]) – A list of volumes that should be saved to the .vdb file.

- **metaData** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) –

  Optional Metadata to write to the file.

  Have to be added under string keys to the data dictionary.

### *static* `VolumeToolsInterface.VolumeToMesh(volume, iso, adaptiveValue)` <a id="maxon.VolumeToolsInterface.VolumeToMesh"></a>

Extracts a polygon object iso surface from a volume. This is done by a marching cube algorithm.

**Parameters:**

- **volume** ([`maxon.VolumeRef`](../reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The volume to extract a surface from.
- **iso** (*float*) – The iso value at which a surface should be extracted.
- **adaptiveValue** (*float*) – An adaptive value between 0.0 and 1.0 that reduces the polygon count based on curvature.

**Returns:** The extracted polygon object.

**Return type:** [`c4d.PolygonObject`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject)
