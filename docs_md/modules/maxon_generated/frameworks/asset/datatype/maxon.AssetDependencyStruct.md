<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/datatype/maxon.AssetDependencyStruct.html -->

# maxon.AssetDependencyStruct <a id="maxon-assetdependencystruct"></a>

## Description <a id="module-maxon.AssetDependencyStruct"></a><a id="description"></a>

Helper class to pass several arguments into asset creation functions.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)
- [`maxon.Struct`](../../../datatypes/base_core/maxon.Struct.md#module-maxon.Struct)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.AssetDependencyStruct.assetCreationDate`](maxon.AssetDependencyStruct.assetCreationDate.md#maxon.AssetDependencyStruct.assetCreationDate) | Asset Creation time |
| [`maxon.AssetDependencyStruct.assetIdAndVersion`](maxon.AssetDependencyStruct.assetIdAndVersion.md#maxon.AssetDependencyStruct.assetIdAndVersion) | IdAndVersion of the asset. |
| [`maxon.AssetDependencyStruct.assetTypeId`](maxon.AssetDependencyStruct.assetTypeId.md#maxon.AssetDependencyStruct.assetTypeId) | Asset Type |
| [`maxon.AssetDependencyStruct.originalName`](maxon.AssetDependencyStruct.originalName.md#maxon.AssetDependencyStruct.originalName) | Original asset name |
| [`maxon.AssetDependencyStruct.updatePolicy`](maxon.AssetDependencyStruct.updatePolicy.md#maxon.AssetDependencyStruct.updatePolicy) | Update policy |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`ToString`](#maxon.AssetDependencyStruct.ToString)() | Returns a string representation of the content. |
| [`__eq__`](#maxon.AssetDependencyStruct.__eq__)(other) | Checks if two asset dependency struct are equal. |
| [`__hash__`](#maxon.AssetDependencyStruct.__hash__)() | Returns the hash code of a data. |
| [`__init__`](#maxon.AssetDependencyStruct.__init__)([other]) | Initializes the appropriate C++ Data object and store it within the _data member. |
| [`__ne__`](#maxon.AssetDependencyStruct.__ne__)(other) | Checks if two asset dependency struct are not equal. |
| [`__str__`](#maxon.AssetDependencyStruct.__str__)() | Returns the string representation of a data. |

## Methods Definition <a id="methods-definition"></a>

### `AssetDependencyStruct.ToString()` <a id="maxon.AssetDependencyStruct.ToString"></a>

Returns a string representation of the content.

**Returns:** The string representation of the content of the [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data).

**Return type:** *maxon.String*

### `AssetDependencyStruct.__eq__(other)` <a id="maxon.AssetDependencyStruct.__eq__"></a>

Checks if two asset dependency struct are equal.

**Parameters:** **other** ([`maxon.AssetDependencyStruct`](#module-maxon.AssetDependencyStruct)) – The other asset dependency struct.

**Return type:** bool

**Returns:** **True** if asset dependency struct are equal.

### `AssetDependencyStruct.__hash__()` <a id="maxon.AssetDependencyStruct.__hash__"></a>

Returns the hash code of a data.

### `AssetDependencyStruct.__init__(other=None)` <a id="maxon.AssetDependencyStruct.__init__"></a>

Initializes the appropriate C++ Data object and store it within the _data member.

If C is a Data then _data store a copy the C++ Data is done and stored.  
If C is a C++ Data then _data store a reference of the C++ Data.  
If C is not defined the C++ data is created and stored in the _data member.

**Parameters:** **C** (Optional[[`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)]) – Input data from which the Data should be created.

### `AssetDependencyStruct.__ne__(other)` <a id="maxon.AssetDependencyStruct.__ne__"></a>

Checks if two asset dependency struct are not equal.

**Parameters:** **other** ([`maxon.AssetDependencyStruct`](#module-maxon.AssetDependencyStruct)) – The other asset dependency struct.

**Return type:** bool

**Returns:** **True** if both asset dependency struct are not equal.

### `AssetDependencyStruct.__str__()` <a id="maxon.AssetDependencyStruct.__str__"></a>

Returns the string representation of a data.

**Return type:** str
