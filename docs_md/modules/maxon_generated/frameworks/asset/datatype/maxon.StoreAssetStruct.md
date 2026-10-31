<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/datatype/maxon.StoreAssetStruct.html -->

# maxon.StoreAssetStruct <a id="maxon-storeassetstruct"></a>

## Description <a id="module-maxon.StoreAssetStruct"></a><a id="description"></a>

An object of this class can store every type of data as long as that type has been registered (see [`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)
- [`maxon.Struct`](../../../datatypes/base_core/maxon.Struct.md#module-maxon.Struct)

Child Class:

- [`maxon.AddAssetDepencendyStruct`](maxon.AddAssetDepencendyStruct.md#module-maxon.AddAssetDepencendyStruct)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`__init__`](#maxon.StoreAssetStruct.__init__)(parentCategory[, saveRepository, …]) | Initializes the appropriate C++ Data object and store it within the _data member. |

## Methods Definition <a id="methods-definition"></a>

### `StoreAssetStruct.__init__(parentCategory, saveRepository=None, lookupRepository=None)` <a id="maxon.StoreAssetStruct.__init__"></a>

Initializes the appropriate C++ Data object and store it within the _data member.

If C is a Data then _data store a copy the C++ Data is done and stored.  
If C is a C++ Data then _data store a reference of the C++ Data.  
If C is not defined the C++ data is created and stored in the _data member.

**Parameters:** **C** (Optional[[`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)]) – Input data from which the Data should be created.
