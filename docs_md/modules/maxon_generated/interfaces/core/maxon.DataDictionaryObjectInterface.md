<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/core/maxon.DataDictionaryObjectInterface.html -->

# maxon.DataDictionaryObjectInterface <a id="maxon-datadictionaryobjectinterface"></a>

## Description <a id="module-maxon.DataDictionaryObjectInterface"></a><a id="description"></a>

Class to store and find any [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data) type under any type of key.

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Children Classes:

- [`maxon.BaseStreamInterface`](../io/maxon.BaseStreamInterface.md#module-maxon.BaseStreamInterface)
- [`maxon.IoConnectionInterface`](../io/maxon.IoConnectionInterface.md#module-maxon.IoConnectionInterface)
- [`maxon.FileFormatInterface`](../io/maxon.FileFormatInterface.md#module-maxon.FileFormatInterface)
- [`maxon.AssetTypeInterface`](../../frameworks/asset/interface/maxon.AssetTypeInterface.md#module-maxon.AssetTypeInterface)
- [`maxon.AssetRepositoryInterface`](../../frameworks/asset/interface/maxon.AssetRepositoryInterface.md#module-maxon.AssetRepositoryInterface)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`EraseData`](#maxon.DataDictionaryObjectInterface.EraseData)(key) | Removes a data entry from the dictionary. |
| [`Get`](#maxon.DataDictionaryObjectInterface.Get)(key[, defaultValue]) | Gets the value for the given key in the dictionary. |
| [`GetData`](#maxon.DataDictionaryObjectInterface.GetData)(key) | Gets data stored under a specific id. |
| [`IsEmpty`](#maxon.DataDictionaryObjectInterface.IsEmpty)() | Checks if the dictionary is empty. |
| [`Reset`](#maxon.DataDictionaryObjectInterface.Reset)() | Frees the entire dictionary. |
| [`Set`](#maxon.DataDictionaryObjectInterface.Set)(key, value) | Sets a value for the given key in the dictionary. |
| [`SetData`](#maxon.DataDictionaryObjectInterface.SetData)(key, value) | Sets [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data) under a specific id. |

## Methods Definition <a id="methods-definition"></a>

### `DataDictionaryObjectInterface.EraseData(key)` <a id="maxon.DataDictionaryObjectInterface.EraseData"></a>

Removes a data entry from the dictionary.

> **Warning:** This function doesn’t check if the dictionary contained the key.

**Parameters:** **key** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id) under which the data is stored.

### `DataDictionaryObjectInterface.Get(key, defaultValue=None)` <a id="maxon.DataDictionaryObjectInterface.Get"></a>

Gets the value for the given key in the dictionary.  
A value can be retrieved in two ways:

> 1. Using a FId: *dict.Get(maxon.MAXCHINEINFO.COMPUTERNAME)*
> 2. Using a registered data type: *dict.Get\<String>(Int32(5))*

**Parameters:**

- **key** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – Key under which the data is stored.
- **defaultValue** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data).) – Default value which should be returned if the key cannot be found.

**Raises:** **KeyError** – When the given key does not exist.

**Returns:** [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data) converted to the right type if found in the dictionary, otherwise the default value.

### `DataDictionaryObjectInterface.GetData(key)` <a id="maxon.DataDictionaryObjectInterface.GetData"></a>

Gets data stored under a specific id.

**Parameters:** **key** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id) under which the data is stored.

**Returns:** [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data) as [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data) class.

**Return type:** [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `DataDictionaryObjectInterface.IsEmpty()` <a id="maxon.DataDictionaryObjectInterface.IsEmpty"></a>

Checks if the dictionary is empty.

**Returns:** True if the dictionary does not contain any elements.

**Return type:** bool

### `DataDictionaryObjectInterface.Reset()` <a id="maxon.DataDictionaryObjectInterface.Reset"></a>

Frees the entire dictionary. After this call the DataDictionary is empty.

### `DataDictionaryObjectInterface.Set(key, value)` <a id="maxon.DataDictionaryObjectInterface.Set"></a>

Sets a value for the given key in the dictionary.  
A value can be set in two ways:

> 1. Using a FId: *dict.Set(maxon.MAXCHINEINFO.COMPUTERNAME, “data”)*
> 2. Using an registered data type: *dict.Set(maxon.Int32(5), “data”)*

**Parameters:**

- **key** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id) under which the data is stored.
- **value** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – Move reference to the data.

### `DataDictionaryObjectInterface.SetData(key, value)` <a id="maxon.DataDictionaryObjectInterface.SetData"></a>

Sets [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data) under a specific id.

**Parameters:**

- **key** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id) under which the data is stored.
- **value** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – Move reference to the data.
