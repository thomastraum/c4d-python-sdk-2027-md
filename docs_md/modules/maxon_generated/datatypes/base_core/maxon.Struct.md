<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/base_core/maxon.Struct.html -->

# maxon.Struct <a id="maxon-struct"></a>

## Description <a id="module-maxon.Struct"></a><a id="description"></a>

Represents a C++ structure.

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

## Inheritance diagram <a id="inheritance-diagram"></a>

Children Classes:

- [`maxon.SourceLocation`](../core/maxon.SourceLocation.md#module-maxon.SourceLocation)
- [`maxon.UnknownDataType`](maxon.UnknownDataType.md#module-maxon.UnknownDataType)
- [`maxon.ConfigInit`](../core/maxon.ConfigInit.md#module-maxon.ConfigInit)
- [`maxon.GradientKnot`](../../interfaces/misc/maxon.GradientKnot.md#module-maxon.GradientKnot)
- [`maxon.AssetDatabaseStruct`](../../frameworks/asset/datatype/maxon.AssetDatabaseStruct.md#module-maxon.AssetDatabaseStruct)
- [`maxon.DragAndDropDataAssetArray`](../../frameworks/asset/datatype/maxon.DragAndDropDataAssetArray.md#module-maxon.DragAndDropDataAssetArray)
- [`maxon.AssetDependencyStruct`](../../frameworks/asset/datatype/maxon.AssetDependencyStruct.md#module-maxon.AssetDependencyStruct)
- [`maxon.StoreAssetStruct`](../../frameworks/asset/datatype/maxon.StoreAssetStruct.md#module-maxon.StoreAssetStruct)
- [`maxon.ResolveAssetDependenciesStruct`](../../frameworks/asset/datatype/maxon.ResolveAssetDependenciesStruct.md#module-maxon.ResolveAssetDependenciesStruct)
- [`maxon.GraphTransaction`](../../frameworks/graph/datatype/maxon.GraphTransaction.md#module-maxon.GraphTransaction)
- [`maxon.Wires`](../../frameworks/graph/datatype/maxon.Wires.md#module-maxon.Wires)
- [`maxon.GraphNode`](../../frameworks/graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode)
- [`maxon.MeshAttribute`](../../frameworks/mesh_misc/datatype/maxon.MeshAttribute.md#module-maxon.MeshAttribute)
- [`maxon.SqMat3`](../vec_col_mat/maxon.SqMat3.md#module-maxon.SqMat3)
- [`maxon.SqMat3_32`](../vec_col_mat/maxon.SqMat3_32.md#module-maxon.SqMat3_32)
- [`maxon.SqMat3_64`](../vec_col_mat/maxon.SqMat3_64.md#module-maxon.SqMat3_64)
- [`maxon.Matrix32`](../vec_col_mat/maxon.Matrix32.md#module-maxon.Matrix32)
- [`maxon.Matrix64`](../vec_col_mat/maxon.Matrix64.md#module-maxon.Matrix64)
- [`maxon.SDFFilterSettings`](../../frameworks/volume/datatype/maxon.SDFFilterSettings.md#module-maxon.SDFFilterSettings)
- [`maxon.FilterSettings`](../../frameworks/volume/datatype/maxon.FilterSettings.md#module-maxon.FilterSettings)
- [`maxon.FieldSampleData`](../../frameworks/volume/datatype/maxon.FieldSampleData.md#module-maxon.FieldSampleData)
- [`maxon.VolumeConversionPolygon`](../../frameworks/volume/datatype/maxon.VolumeConversionPolygon.md#module-maxon.VolumeConversionPolygon)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`__dir__`](#maxon.Struct.__dir__)() | Returns a list of all the attributes names of the current instance including the member names for the underlying structure type. |
| [`__getattribute__`](#maxon.Struct.__getattribute__)(name) | Returns the attribute value stored under the given name. |
| [`__repr__`](#maxon.Struct.__repr__)() | Returns the string representation of a struct. |
| [`__setattr__`](#maxon.Struct.__setattr__)(name, value) | Stores the given value under the given attribute name if it exists. |

## Methods Definition <a id="methods-definition"></a>

### `Struct.__dir__()` <a id="maxon.Struct.__dir__"></a>

Returns a list of all the attributes names of the current instance including the member names for the underlying structure type.

**Returns:** The list of all attributes names.

**Return type:** list[str]

### `Struct.__getattribute__(name)` <a id="maxon.Struct.__getattribute__"></a>

Returns the attribute value stored under the given name.

**Parameters:** **name** (*str*) – The name of the attribute.

**Returns:** The resolved attribute or raise AttributeError if the given name can’t be found.

**Return type:** Any

### `Struct.__repr__()` <a id="maxon.Struct.__repr__"></a>

Returns the string representation of a struct.

**Return type:** str

### `Struct.__setattr__(name, value)` <a id="maxon.Struct.__setattr__"></a>

Stores the given value under the given attribute name if it exists.

**Parameters:**

- **name** (*str*) – The name of the attribute.
- **value** ([`maxon.Data`](maxon.Data.md#module-maxon.Data)) – The value we want to assign to the attribute.
