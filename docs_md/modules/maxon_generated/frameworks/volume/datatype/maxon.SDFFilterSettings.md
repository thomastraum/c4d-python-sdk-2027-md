<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/volume/datatype/maxon.SDFFilterSettings.html -->

# maxon.SDFFilterSettings <a id="maxon-sdffiltersettings"></a>

## Description <a id="module-maxon.SDFFilterSettings"></a><a id="description"></a>

An object of this class can store every type of data as long as that type has been registered (see [`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)
- [`maxon.Struct`](../../../datatypes/base_core/maxon.Struct.md#module-maxon.Struct)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.SDFFilterSettings.accuracy`](maxon.SDFFilterSettings.accuracy.md#maxon.SDFFilterSettings.accuracy) | ([`maxon.FILTERACCURACY`](../../../enums/maxon.FILTERACCURACY.md#module-maxon.FILTERACCURACY)) Filter accuracy type. |
| [`maxon.SDFFilterSettings.filterType`](maxon.SDFFilterSettings.filterType.md#maxon.SDFFilterSettings.filterType) | ([`maxon.SDFFILTERTYPE`](../../../enums/maxon.SDFFILTERTYPE.md#module-maxon.SDFFILTERTYPE)) The used filter type. |
| [`maxon.SDFFilterSettings.halfWidth`](maxon.SDFFilterSettings.halfWidth.md#maxon.SDFFilterSettings.halfWidth) | (int) Target halfwidth of the resize filter. |
| [`maxon.SDFFilterSettings.iterations`](maxon.SDFFilterSettings.iterations.md#maxon.SDFFilterSettings.iterations) | (int) Amount of iterations that the filter is applied. |
| [`maxon.SDFFilterSettings.offset`](maxon.SDFFilterSettings.offset.md#maxon.SDFFilterSettings.offset) | (int) Offset value for the dilate, erode and offset filter. |
| [`maxon.SDFFilterSettings.stencilWidth`](maxon.SDFFilterSettings.stencilWidth.md#maxon.SDFFilterSettings.stencilWidth) | (int) Voxel distance of the filter stencil. |
| [`maxon.SDFFilterSettings.strength`](maxon.SDFFilterSettings.strength.md#maxon.SDFFilterSettings.strength) | (float) The Strength of the filter. |
