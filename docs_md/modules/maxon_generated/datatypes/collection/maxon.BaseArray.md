<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/collection/maxon.BaseArray.html -->

# maxon.BaseArray <a id="maxon-basearray"></a>

## Description <a id="module-maxon.BaseArray"></a><a id="description"></a>

A generic array class template used to stored any kind of data. It is based on `maxon.BaseCollection` and `maxon.Collection`.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Append`](#maxon.BaseArray.Append)(value) |  |
| [`CopyFrom`](#maxon.BaseArray.CopyFrom)(other) |  |
| [`Flush`](#maxon.BaseArray.Flush)() | Deletes all elements, but doesn’t free memory (calls destructors though). |
| [`GetCount`](#maxon.BaseArray.GetCount)() | Gets the number of array elements. |
| [`Insert`](#maxon.BaseArray.Insert)(index, value) | Inserts a new element at index position. |
| [`Reset`](#maxon.BaseArray.Reset)() | Deletes all elements (calls destructors and frees memory). |
| [`Resize`](#maxon.BaseArray.Resize)(newCnt[, resizeFlags]) | Resizes the array to contain *newCnt* elements. |
| [`ToBlock`](#maxon.BaseArray.ToBlock)() | Returns a [`maxon.Block`](maxon.Block.md#module-maxon.Block) which represents the elements of the array. |
| [`__getitem__`](#maxon.BaseArray.__getitem__)(index) | Gets the item at the given index in the array. |
| [`__init__`](#maxon.BaseArray.__init__)([ob, input, count]) | Initialize the BaseContainer in order to store a given type. At the moment only maxon Data Type are supported. |
| [`__iter__`](#maxon.BaseArray.__iter__)() | Iterates over the values in the array. |
| [`__len__`](#maxon.BaseArray.__len__)() | Returns the number of elements in array. |
| [`__maxon_init__`](#maxon.BaseArray.__maxon_init__)(capsule) |  |
| [`__setitem__`](#maxon.BaseArray.__setitem__)(index, item) | Sets the item for the given index in the array. |
| [`__str__`](#maxon.BaseArray.__str__)() | Returns the string representation of a data. |

## Methods Definition <a id="methods-definition"></a>

### `BaseArray.Append(value)` <a id="maxon.BaseArray.Append"></a>

### `BaseArray.CopyFrom(other)` <a id="maxon.BaseArray.CopyFrom"></a>

### `BaseArray.Flush()` <a id="maxon.BaseArray.Flush"></a>

Deletes all elements, but doesn’t free memory (calls destructors though).

### `BaseArray.GetCount()` <a id="maxon.BaseArray.GetCount"></a>

Gets the number of array elements.

**Returns:** Number of array elements.

**Return type:** int

### `BaseArray.Insert(index, value)` <a id="maxon.BaseArray.Insert"></a>

Inserts a new element at index position.

**Parameters:**

- **index** (*int*) – position
- **value** ([`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)) – The value to be copied.

### `BaseArray.Reset()` <a id="maxon.BaseArray.Reset"></a>

Deletes all elements (calls destructors and frees memory).

### `BaseArray.Resize(newCnt, resizeFlags=enums.COLLECTION_RESIZE_FLAGS.DEFAULT)` <a id="maxon.BaseArray.Resize"></a>

Resizes the array to contain *newCnt* elements.  
If *newCnt* is smaller than [`BaseArray.GetCount()`](#maxon.BaseArray.GetCount) all extra elements are being deleted.  
If it is greater the array is expanded and the default constructor is called for new elements.

**Parameters:**

- **newCnt** (*int*) – New array size.
- **resizeFlags** (`maxon.COLLECTION_RESIZE_FLAGS`) – How the resizing should be performed.

### `BaseArray.ToBlock()` <a id="maxon.BaseArray.ToBlock"></a>

Returns a [`maxon.Block`](maxon.Block.md#module-maxon.Block) which represents the elements of the array.

**Returns:** The content of this array as a block.

**Returns:** [`maxon.Block`](maxon.Block.md#module-maxon.Block)

### `BaseArray.__getitem__(index)` <a id="maxon.BaseArray.__getitem__"></a>

Gets the item at the given index in the array.

**Parameters:** **index** (*int*) – The index to retrieve the value for.

**Raises:** **IndexError** – When index is out of bounds.

**Returns:** The retrieved item.

**Return type:** [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

### `BaseArray.__init__(ob=None, input=None, count=None)` <a id="maxon.BaseArray.__init__"></a>

Initialize the BaseContainer in order to store a given type. At the moment only maxon Data Type are supported.  
If it is an iterable the items are copied over

**Parameters:**

- **ob** (*Union*[*str*, *datatype capsule*, *WrapperClass*] (*e.g. maxon.Int32* or *maxon.BaseTime*)) –

  If it’s a string:

  1. Example 1: “net.maxon.interface.string-C” creates an array of string objects
  2. Example 2: “net.maxon.interface.string-C[A]” creates an array of string arrays

  If it’s a datatype capsule e.g [`maxon.Int32`](../simple/maxon.Int32.md#module-maxon.Int32) it will only accept this kind of datatype later.

- **input** (*Optional*(*Union*[*int*, *collections.Iterable*])) – If it’s an integer, resize the array with this number, if it’s an iterable the data are copied.

- **count** (*Optional*(*int*)) – Number of elements to fill/copy in case if input is passed.

### `BaseArray.__iter__()` <a id="maxon.BaseArray.__iter__"></a>

Iterates over the values in the array.

### `BaseArray.__len__()` <a id="maxon.BaseArray.__len__"></a>

Returns the number of elements in array.

**Returns:** Number of elements in the array.

**Return type:** int

### `BaseArray.__maxon_init__(capsule)` <a id="maxon.BaseArray.__maxon_init__"></a>

### `BaseArray.__setitem__(index, item)` <a id="maxon.BaseArray.__setitem__"></a>

Sets the item for the given index in the array.  
It is only possible to modify existing items with this function, to add new values, use  
[`maxon.BaseArray.Append()`](#maxon.BaseArray.Append).

**Parameters:**

- **index** (*int*) – The index of the value to set.
- **value** (Optional[[`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)]) – The value to set for *index*.

**Raises:** **IndexError** – When index is out of bounds.

### `BaseArray.__str__()` <a id="maxon.BaseArray.__str__"></a>

Returns the string representation of a data.

**Return type:** str
