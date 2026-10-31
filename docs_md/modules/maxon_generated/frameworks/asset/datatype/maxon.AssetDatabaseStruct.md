<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/datatype/maxon.AssetDatabaseStruct.html -->

# maxon.AssetDatabaseStruct <a id="maxon-assetdatabasestruct"></a>

## Description <a id="module-maxon.AssetDatabaseStruct"></a><a id="description"></a>

An object of this class can store every type of data as long as that type has been registered (see [`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)
- [`maxon.Struct`](../../../datatypes/base_core/maxon.Struct.md#module-maxon.Struct)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`__init__`](#maxon.AssetDatabaseStruct.__init__)(otherOrDbUrl[, active, …]) | Initializes the appropriate C++ Data object and store it within the _data member. |
| [`__str__`](#maxon.AssetDatabaseStruct.__str__)() | Returns the string representation of a data. |

## Methods Definition <a id="methods-definition"></a>

### `AssetDatabaseStruct.__init__(otherOrDbUrl, active=True, exportOnSaveProject=True, isBuiltin=False)` <a id="maxon.AssetDatabaseStruct.__init__"></a>

Initializes the appropriate C++ Data object and store it within the _data member.

If C is a Data then _data store a copy the C++ Data is done and stored.  
If C is a C++ Data then _data store a reference of the C++ Data.  
If C is not defined the C++ data is created and stored in the _data member.

**Parameters:** **C** (Optional[[`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)]) – Input data from which the Data should be created.

### `AssetDatabaseStruct.__str__()` <a id="maxon.AssetDatabaseStruct.__str__"></a>

Returns the string representation of a data.

**Return type:** str
