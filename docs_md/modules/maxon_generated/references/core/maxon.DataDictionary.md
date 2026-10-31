<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/references/core/maxon.DataDictionary.html -->

# maxon.DataDictionary <a id="maxon-datadictionary"></a>

## Description <a id="module-maxon.DataDictionary"></a><a id="description"></a>

Reference class of [`maxon.DataDictionaryInterface`](../../interfaces/core/maxon.DataDictionaryInterface.md#module-maxon.DataDictionaryInterface).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.DataDictionaryInterface`](../../interfaces/core/maxon.DataDictionaryInterface.md#module-maxon.DataDictionaryInterface)
- [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`__contains__`](#maxon.DataDictionary.__contains__)(item) | Returns **True** if there is data stored under the #item# specific key. |
| [`__delitem__`](#maxon.DataDictionary.__delitem__)(key) | Erases the value stored under the given key. |
| [`__getitem__`](#maxon.DataDictionary.__getitem__)(item) | Gets the data stored under the given key. |
| [`__iter__`](#maxon.DataDictionary.__iter__)() | Iterates keys, values of the dictionary. |
| [`__len__`](#maxon.DataDictionary.__len__)() | Returns the number of entries in the dictionary. |
| [`__maxon_convert__`](#maxon.DataDictionary.__maxon_convert__)([expected]) | Converts a Python dictionary to a Maxon DataDictionary. |
| [`__setitem__`](#maxon.DataDictionary.__setitem__)(key, value) | Sets the value stored under the given key. |
| [`__str__`](#maxon.DataDictionary.__str__)() | Return str(self). |

## Methods Definition <a id="methods-definition"></a>

### `DataDictionary.__contains__(item)` <a id="maxon.DataDictionary.__contains__"></a>

Returns **True** if there is data stored under the #item# specific key.

**Parameters:** **item** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – Key under which the data should be stored.

**Returns:** **True** if existent.

**Return type:** bool

### `DataDictionary.__delitem__(key)` <a id="maxon.DataDictionary.__delitem__"></a>

Erases the value stored under the given key.  
Does not check if the dictionary contains the given key and values can be erased in two ways:

> 1. Using a FId: *dict.Erase(maxon.MAXCHINEINFO.COMPUTERNAME, “data”)*
> 2. Using a registered data type: *dict.Erase(maxon.Int32(5))*

**Parameters:** **key** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – Key under which the data is stored.

### `DataDictionary.__getitem__(item)` <a id="maxon.DataDictionary.__getitem__"></a>

Gets the data stored under the given key.  
Will return *None* when the given key does not exist.

**Parameters:** **item** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – Key under which the data is stored.

**Returns:** Data converted to the right type on success.

**Return type:** [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `DataDictionary.__iter__()` <a id="maxon.DataDictionary.__iter__"></a>

Iterates keys, values of the dictionary.

### `DataDictionary.__len__()` <a id="maxon.DataDictionary.__len__"></a>

Returns the number of entries in the dictionary.

**Returns:** Number of entries in the dictionary.

**Return type:** int

### `DataDictionary.__maxon_convert__(expected=None)` <a id="maxon.DataDictionary.__maxon_convert__"></a>

Converts a Python dictionary to a Maxon DataDictionary.

**Parameters:** **expected** (*Optional*[*type*]) – The expected output type, only dict is support for the moment.

**Returns:** A Python dictionary filled with data contained from the Maxon DataDictionary

**Return type:** dict

### `DataDictionary.__setitem__(key, value)` <a id="maxon.DataDictionary.__setitem__"></a>

Sets the value stored under the given key.  
Values can be set in two ways:

> 1. Using a FId: *dict.Set(maxon.MAXCHINEINFO.COMPUTERNAME, “data”)*
> 2. Using a registered data type: *dict.Set(maxon.Int32(5), “data”)*

**Parameters:**

- **key** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id) under which the data is stored.
- **value** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – Move reference to the data.

### `DataDictionary.__str__()` <a id="maxon.DataDictionary.__str__"></a>

Return str(self).
