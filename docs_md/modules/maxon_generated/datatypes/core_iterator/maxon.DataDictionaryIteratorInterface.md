<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/core_iterator/maxon.DataDictionaryIteratorInterface.html -->

# maxon.DataDictionaryIteratorInterface <a id="maxon-datadictionaryiteratorinterface"></a>

## Description <a id="module-maxon.DataDictionaryIteratorInterface"></a><a id="description"></a>

[`maxon.DataDictionaryIteratorInterface`](#module-maxon.DataDictionaryIteratorInterface) is used internally by `DataDictionary.Iterator()`.

> **Warning:** It should not be used directly.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.PlainIterator`](maxon.PlainIterator.md#module-maxon.PlainIterator)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Destruct`](#maxon.DataDictionaryIteratorInterface.Destruct)() | Destructs the current iterator |
| [`GetKeyAndData`](#maxon.DataDictionaryIteratorInterface.GetKeyAndData)(res) | Retrieves the key and value for the current entry of the iterator. |
| [`HasValue`](#maxon.DataDictionaryIteratorInterface.HasValue)() | Checks if there is still value to iterate. |
| [`MoveToNext`](#maxon.DataDictionaryIteratorInterface.MoveToNext)() | Moves to the next entry from the [`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary). |
| [`__init__`](#maxon.DataDictionaryIteratorInterface.__init__)(memory) | **param memory:** |

## Methods Definition <a id="methods-definition"></a>

### `DataDictionaryIteratorInterface.Destruct()` <a id="maxon.DataDictionaryIteratorInterface.Destruct"></a>

Destructs the current iterator

### `DataDictionaryIteratorInterface.GetKeyAndData(res)` <a id="maxon.DataDictionaryIteratorInterface.GetKeyAndData"></a>

Retrieves the key and value for the current entry of the iterator.

**Parameters:** **res** (tuple([`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data), [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data))) – The key and the value stored for this key.

**Returns:**

### `DataDictionaryIteratorInterface.HasValue()` <a id="maxon.DataDictionaryIteratorInterface.HasValue"></a>

Checks if there is still value to iterate.

**Returns:** Returns True if this object contains a value.

**Return type:** bool

### `DataDictionaryIteratorInterface.MoveToNext()` <a id="maxon.DataDictionaryIteratorInterface.MoveToNext"></a>

Moves to the next entry from the [`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary).

### `DataDictionaryIteratorInterface.__init__(memory)` <a id="maxon.DataDictionaryIteratorInterface.__init__"></a>

**Parameters:** **memory** –
