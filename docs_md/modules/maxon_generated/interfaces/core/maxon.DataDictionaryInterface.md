<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/core/maxon.DataDictionaryInterface.html -->

# maxon.DataDictionaryInterface <a id="maxon-datadictionaryinterface"></a>

## Description <a id="module-maxon.DataDictionaryInterface"></a><a id="description"></a>

Class to store and find any data type under any type of key.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Contains`](#maxon.DataDictionaryInterface.Contains)(key) | Tests if the given key is a key of the dictionary. |
| [`Erase`](#maxon.DataDictionaryInterface.Erase)(key) | Erases data stored under the given key. |
| [`Get`](#maxon.DataDictionaryInterface.Get)(key[, defaultValue]) | Gets the value for the given key in the dictionary. |
| [`GetCount`](#maxon.DataDictionaryInterface.GetCount)() | Returns the number of entries in the dictionary. |
| [`InitIterator`](#maxon.DataDictionaryInterface.InitIterator)(end) | Helper functions for initialize an iterator. |
| [`IsEmpty`](#maxon.DataDictionaryInterface.IsEmpty)() | Checks if the dictionary is empty. |
| [`IsPopulated`](#maxon.DataDictionaryInterface.IsPopulated)() | Checks if the dictionary contains anything. |
| [`Reset`](#maxon.DataDictionaryInterface.Reset)() | Frees the entire dictionary. |
| [`Set`](#maxon.DataDictionaryInterface.Set)(key, value) | Sets a value for the given key in the dictionary. |

## Methods Definition <a id="methods-definition"></a>

### `DataDictionaryInterface.Contains(key)` <a id="maxon.DataDictionaryInterface.Contains"></a>

Tests if the given key is a key of the dictionary.

**Parameters:** **key** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – Key under which the data should be stored.

**Returns:** True if existent.

**Return type:** bool

### `DataDictionaryInterface.Erase(key)` <a id="maxon.DataDictionaryInterface.Erase"></a>

Erases data stored under the given key.  
Does not check if the dictionary does contain the key and can be called in two ways:

> 1. Using a FId: *dict.Erase(maxon.MAXCHINEINFO.COMPUTERNAME, “data”)*
> 2. Using a registered data: *dict.Erase(maxon.Int32(5))*

**Parameters:** **key** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – Key under which the data is stored.

### `DataDictionaryInterface.Get(key, defaultValue=None)` <a id="maxon.DataDictionaryInterface.Get"></a>

Gets the value for the given key in the dictionary.  
A value can be retrieved in two ways:

> 1. Using a FId: *dict.Get(maxon.MAXCHINEINFO.COMPUTERNAME)*
> 2. Using a registered data type: *dict.Get\<String>(Int32(5))*

**Parameters:**

- **key** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – Key under which the data is stored.
- **defaultValue** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data).) – Default value which should be returned if the key cannot be found.

**Raises:** **KeyError** – When the given key does not exist.

**Returns:** [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data) converted to the right type if found in the dictionary, otherwise the default value.

### `DataDictionaryInterface.GetCount()` <a id="maxon.DataDictionaryInterface.GetCount"></a>

Returns the number of entries in the dictionary.

**Returns:** Number of dictionary entries.

**Return type:** int

### `DataDictionaryInterface.InitIterator(end)` <a id="maxon.DataDictionaryInterface.InitIterator"></a>

Helper functions for initialize an iterator.

### `DataDictionaryInterface.IsEmpty()` <a id="maxon.DataDictionaryInterface.IsEmpty"></a>

Checks if the dictionary is empty.

**Returns:** True if the dictionary does not contain any elements.

**Return type:** bool

### `DataDictionaryInterface.IsPopulated()` <a id="maxon.DataDictionaryInterface.IsPopulated"></a>

Checks if the dictionary contains anything.

**Returns:** True if the dictionary contains any elements.

**Return type:** bool

### `DataDictionaryInterface.Reset()` <a id="maxon.DataDictionaryInterface.Reset"></a>

Frees the entire dictionary. After this call the DataDictionary is empty.

### `DataDictionaryInterface.Set(key, value)` <a id="maxon.DataDictionaryInterface.Set"></a>

Sets a value for the given key in the dictionary.  
A value can be set in two ways:

> 1. Using a FId: *dict.Set(maxon.MAXCHINEINFO.COMPUTERNAME, “data”)*
> 2. Using an registered data type: *dict.Set(maxon.Int32(5), “data”)*

**Parameters:**

- **key** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id) under which the data is stored.
- **value** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – Move reference to the data.
