<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/core_helper/maxon.AutoIterator.html -->

# maxon.AutoIterator <a id="maxon-autoiterator"></a>

## Description <a id="module-maxon.AutoIterator"></a><a id="description"></a>

AutoIterator implements a foreach iterator for a BaseArray

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`__init__`](#maxon.AutoIterator.__init__)(array[, beginIndex]) | Initializes the Iterator with the given BaseArray optionally with an offset. |
| [`__next__`](#maxon.AutoIterator.__next__)() | Retrieves the next element in the array. |

## Methods Definition <a id="methods-definition"></a>

### `AutoIterator.__init__(array, beginIndex=None)` <a id="maxon.AutoIterator.__init__"></a>

Initializes the Iterator with the given BaseArray optionally with an offset.

**Parameters:**

- **array** (Union[[`maxon.BaseArray`](../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray), [`maxon.Array`](../../datatypes/collection/maxon.Array.md#module-maxon.Array)]) – The Array to iterates.
- **beginIndex** (*Optional*[*int*]) – Optional offset for the start of the array iteration.

### `AutoIterator.__next__()` <a id="maxon.AutoIterator.__next__"></a>

Retrieves the next element in the array.

**Returns:** The next element of the array.

**Return type:** [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)
