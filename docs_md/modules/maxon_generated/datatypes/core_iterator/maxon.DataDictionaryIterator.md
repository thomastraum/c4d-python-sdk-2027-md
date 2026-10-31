<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/core_iterator/maxon.DataDictionaryIterator.html -->

# maxon.DataDictionaryIterator <a id="maxon-datadictionaryiterator"></a>

## Description <a id="module-maxon.DataDictionaryIterator"></a><a id="description"></a>

Iterator to iterate through all elements of a [`maxon.DataDictionaryIterator`](#module-maxon.DataDictionaryIterator).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetIterator`](#maxon.DataDictionaryIterator.GetIterator)() | Retrieves the [`maxon.DataDictionaryIterator`](#module-maxon.DataDictionaryIterator) attached to the current iterator. |
| [`__init__`](#maxon.DataDictionaryIterator.__init__)(dict, end) | Initializes a dictionary iterator. |
| [`__iter__`](#maxon.DataDictionaryIterator.__iter__)() | Iterates keys, values of the dictionary. |
| [`__next__`](#maxon.DataDictionaryIterator.__next__)() |  |

## Methods Definition <a id="methods-definition"></a>

### `DataDictionaryIterator.GetIterator()` <a id="maxon.DataDictionaryIterator.GetIterator"></a>

Retrieves the [`maxon.DataDictionaryIterator`](#module-maxon.DataDictionaryIterator) attached to the current iterator.

**Returns:** The attached [`maxon.DataDictionaryIterator`](#module-maxon.DataDictionaryIterator) iterator.

**Type:** [`maxon.DataDictionaryIterator`](#module-maxon.DataDictionaryIterator)

### `DataDictionaryIterator.__init__(dict, end)` <a id="maxon.DataDictionaryIterator.__init__"></a>

Initializes a dictionary iterator.

**Parameters:**

- **dict** ([`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – The dictionary to iterates.
- **end** ([`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)) – Last element to the datadictionary.

### `DataDictionaryIterator.__iter__()` <a id="maxon.DataDictionaryIterator.__iter__"></a>

Iterates keys, values of the dictionary.

### `DataDictionaryIterator.__next__()` <a id="maxon.DataDictionaryIterator.__next__"></a>
