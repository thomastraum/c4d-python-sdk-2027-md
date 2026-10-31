<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/collection/maxon.Array.html -->

# maxon.Array <a id="maxon-array"></a>

## Description <a id="module-maxon.Array"></a><a id="description"></a>

An object of this class can store every type of data as long as that type has been registered (see [`maxon.DataType`](../base_core/maxon.DataType.md#module-maxon.DataType)).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Append`](#maxon.Array.Append)(value) |  |
| [`CopyFrom`](#maxon.Array.CopyFrom)(other) |  |
| [`Flush`](#maxon.Array.Flush)() | Deletes all elements, but doesn’t free memory (calls destructors though). |
| [`GetCount`](#maxon.Array.GetCount)() | Gets the number of array elements. |
| [`Insert`](#maxon.Array.Insert)(index, value) | Inserts a new element at index position. |
| [`Reset`](#maxon.Array.Reset)() | Deletes all elements (calls destructors and frees memory). |
| [`Resize`](#maxon.Array.Resize)(newCnt[, resizeFlags]) | Resizes the array to contain *newCnt* elements. |
| [`ToBlock`](#maxon.Array.ToBlock)() | Returns a [`maxon.Block`](maxon.Block.md#module-maxon.Block) which represents the elements of the array. |
| [`__getitem__`](#maxon.Array.__getitem__)(index) | Gets the item at the given index in the array. |
| [`__init__`](#maxon.Array.__init__)([ob, input, count]) | Initialize the Array in order to store a given type. At the moment only maxon Data Type are supported. |
| [`__iter__`](#maxon.Array.__iter__)() | Iterates over the values in the array. |
| [`__len__`](#maxon.Array.__len__)() | Returns the number of elements in array. |
| [`__maxon_init__`](#maxon.Array.__maxon_init__)(capsule) |  |
| [`__setitem__`](#maxon.Array.__setitem__)(index, item) | Sets the item for the given index in the array. |
| [`__str__`](#maxon.Array.__str__)() | Returns the string representation of a data. |

## Methods Definition <a id="methods-definition"></a>

### `Array.Append(value)` <a id="maxon.Array.Append"></a>

### `Array.CopyFrom(other)` <a id="maxon.Array.CopyFrom"></a>

### `Array.Flush()` <a id="maxon.Array.Flush"></a>

Deletes all elements, but doesn’t free memory (calls destructors though).

### `Array.GetCount()` <a id="maxon.Array.GetCount"></a>

Gets the number of array elements.

**Returns:** Number of array elements.

**Return type:** int

### `Array.Insert(index, value)` <a id="maxon.Array.Insert"></a>

Inserts a new element at index position.

**Parameters:**

- **index** (*int*) – position
- **value** ([`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)) – The value to be copied.

### `Array.Reset()` <a id="maxon.Array.Reset"></a>

Deletes all elements (calls destructors and frees memory).

### `Array.Resize(newCnt, resizeFlags=enums.COLLECTION_RESIZE_FLAGS.DEFAULT)` <a id="maxon.Array.Resize"></a>

Resizes the array to contain *newCnt* elements.  
If *newCnt* is smaller than [`BaseArray.GetCount()`](maxon.BaseArray.md#maxon.BaseArray.GetCount) all extra elements are being deleted.  
If it is greater the array is expanded and the default constructor is called for new elements.

**Parameters:**

- **newCnt** (*int*) – New array size.
- **resizeFlags** (`maxon.COLLECTION_RESIZE_FLAGS`) – How the resizing should be performed.

### `Array.ToBlock()` <a id="maxon.Array.ToBlock"></a>

Returns a [`maxon.Block`](maxon.Block.md#module-maxon.Block) which represents the elements of the array.

**Returns:** The content of this array as a block.

**Returns:** [`maxon.Block`](maxon.Block.md#module-maxon.Block)

### `Array.__getitem__(index)` <a id="maxon.Array.__getitem__"></a>

Gets the item at the given index in the array.

**Parameters:** **index** (*int*) – The index to retrieve the value for.

**Raises:** **IndexError** – When index is out of bounds.

**Returns:** The retrieved item.

**Return type:** [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

### `Array.__init__(ob=None, input=None, count=None)` <a id="maxon.Array.__init__"></a>

Initialize the Array in order to store a given type. At the moment only maxon Data Type are supported.  
If it is an iterable the items are copied over

**Parameters:**

- **ob** (*Union*[*str*, *datatype capsule*, *WrapperClass*] (*e.g. maxon.Int32* or *maxon.BaseTime*)) –

  If it’s a string:

  1. Example 1: “net.maxon.interface.string-C” creates an array of string objects
  2. Example 2: “net.maxon.interface.string-C[]” creates an array of string arrays

  If it’s a datatype capsule e.g [`maxon.Int32`](../simple/maxon.Int32.md#module-maxon.Int32) it will only accept this kind of datatype later.

- **input** (*Optional*(*Union*[*int*, *collections.Iterable*])) – If it’s an integer, resize the array with this number, if it’s an iterable the data are copied.

- **count** (*Optional*(*int*)) – Number of elements to fill/copy in case if input is passed.

### `Array.__iter__()` <a id="maxon.Array.__iter__"></a>

Iterates over the values in the array.

### `Array.__len__()` <a id="maxon.Array.__len__"></a>

Returns the number of elements in array.

**Returns:** Number of elements in the array.

**Return type:** int

### `Array.__maxon_init__(capsule)` <a id="maxon.Array.__maxon_init__"></a>

### `Array.__setitem__(index, item)` <a id="maxon.Array.__setitem__"></a>

Sets the item for the given index in the array.

It is only possible to modify existing items with this function, to add new values, use [`maxon.BaseArray.Append()`](maxon.BaseArray.md#maxon.BaseArray.Append).

**Parameters:**

- **index** (*int*) – The index of the value to set.
- **value** (Optional[[`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)]) – The value to set for *index*.

**Raises:** **IndexError** – When index is out of bounds.

### `Array.__str__()` <a id="maxon.Array.__str__"></a>

Returns the string representation of a data.

**Return type:** str
