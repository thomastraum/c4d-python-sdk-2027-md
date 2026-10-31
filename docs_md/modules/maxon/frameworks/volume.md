<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon/frameworks/volume.html -->

# maxon.frameworks.volume <a id="maxon-frameworks-volume"></a><a id="framework-volume"></a>

> **Note:** Members documented here are defined in `maxon.frameworks.volume` module and are also exposed to the global `maxon` module. See the [Maxon API](../../../manuals/manual_api_overview.md#maxon-api-introduction) section of the API Overview for more information about the special conventions of this API.

## Description <a id="description"></a>

Module for OpenVDB data.

## Interfaces <a id="interfaces"></a>

|   |   |
|---|---|
| [`GridAccessorCreationInterface`](../../maxon_generated/frameworks/volume/interface/maxon.GridAccessorCreationInterface.md#module-maxon.GridAccessorCreationInterface)() | Helper class to create the templated interface [`maxon.GridAccessorInterface`](../../maxon_generated/frameworks/volume/interface/maxon.GridAccessorInterface.md#module-maxon.GridAccessorInterface). |
| [`GridAccessorInterface`](../../maxon_generated/frameworks/volume/interface/maxon.GridAccessorInterface.md#module-maxon.GridAccessorInterface)() | [`maxon.GridAccessorInterface`](../../maxon_generated/frameworks/volume/interface/maxon.GridAccessorInterface.md#module-maxon.GridAccessorInterface) allows to access volume data. |
| [`PointsToVolumeListInterface`](../../maxon_generated/frameworks/volume/interface/maxon.PointsToVolumeListInterface.md#module-maxon.PointsToVolumeListInterface)() | Interface to convert point position to a volume. |
| [`VolumeInterface`](../../maxon_generated/frameworks/volume/interface/maxon.VolumeInterface.md#module-maxon.VolumeInterface)(*args) | [`maxon.VolumeInterface`](../../maxon_generated/frameworks/volume/interface/maxon.VolumeInterface.md#module-maxon.VolumeInterface) represents a core volume object in cinema. |
| [`VolumeToolsInterface`](../../maxon_generated/frameworks/volume/interface/maxon.VolumeToolsInterface.md#module-maxon.VolumeToolsInterface)() | [`maxon.VolumeToolsInterface`](../../maxon_generated/frameworks/volume/interface/maxon.VolumeToolsInterface.md#module-maxon.VolumeToolsInterface) provides methods to process volumes. |

## References <a id="references"></a>

|   |   |
|---|---|
| [`GridAccessorRef`](../../maxon_generated/frameworks/volume/reference/maxon.GridAccessorRef.md#module-maxon.GridAccessorRef)(*args) | Reference class for [`maxon.GridAccessorInterface`](../../maxon_generated/frameworks/volume/interface/maxon.GridAccessorInterface.md#module-maxon.GridAccessorInterface). |
| [`PointsToVolumeListRef`](../../maxon_generated/frameworks/volume/reference/maxon.PointsToVolumeListRef.md#module-maxon.PointsToVolumeListRef)(*args) | Reference class for [`maxon.PointsToVolumeListInterface`](../../maxon_generated/frameworks/volume/interface/maxon.PointsToVolumeListInterface.md#module-maxon.PointsToVolumeListInterface). |
| [`VolumeRef`](../../maxon_generated/frameworks/volume/reference/maxon.VolumeRef.md#module-maxon.VolumeRef)(*args) | Represents a reference of a [`maxon.VolumeInterface`](../../maxon_generated/frameworks/volume/interface/maxon.VolumeInterface.md#module-maxon.VolumeInterface) |

## Data Types <a id="data-types"></a>

|   |   |
|---|---|
| [`FieldSampleData`](../../maxon_generated/frameworks/volume/datatype/maxon.FieldSampleData.md#module-maxon.FieldSampleData)([C]) | Initializes the appropriate C++ Data object and store it within the _data member. |
| [`FilterSettings`](../../maxon_generated/frameworks/volume/datatype/maxon.FilterSettings.md#module-maxon.FilterSettings)([C]) | Initializes the appropriate C++ Data object and store it within the _data member. |
| [`SDFFilterSettings`](../../maxon_generated/frameworks/volume/datatype/maxon.SDFFilterSettings.md#module-maxon.SDFFilterSettings)([C]) | Initializes the appropriate C++ Data object and store it within the _data member. |
| [`VolumeConversionPolygon`](../../maxon_generated/frameworks/volume/datatype/maxon.VolumeConversionPolygon.md#module-maxon.VolumeConversionPolygon)() | Data used, to converts [`c4d.PolygonObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) to a Volume Polygon. |

## Enums <a id="enums"></a>

|   |   |
|---|---|
| [`VOLUMESAMPLER`](../../maxon_generated/enums/maxon.VOLUMESAMPLER.md#module-maxon.VOLUMESAMPLER) |  |
| [`SDFFILTERTYPE`](../../maxon_generated/enums/maxon.SDFFILTERTYPE.md#module-maxon.SDFFILTERTYPE) |  |
| [`FILTERACCURACY`](../../maxon_generated/enums/maxon.FILTERACCURACY.md#module-maxon.FILTERACCURACY) |  |
| [`POLYGONCONVERSIONFLAGS`](../../maxon_generated/enums/maxon.POLYGONCONVERSIONFLAGS.md#module-maxon.POLYGONCONVERSIONFLAGS) |  |
| [`RESAMPLEINTERPOLATIONTYPE`](../../maxon_generated/enums/maxon.RESAMPLEINTERPOLATIONTYPE.md#module-maxon.RESAMPLEINTERPOLATIONTYPE) |  |
