<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/collection/maxon.Pair.html -->

# maxon.Pair <a id="maxon-pair"></a>

## Description <a id="module-maxon.Pair"></a><a id="description"></a>

[`maxon.Pair`](#module-maxon.Pair) provides in-place static storage for elements of arbitrary types.  
It is similar to a [`maxon.Tuple`](maxon.Tuple.md#module-maxon.Tuple), but supports only 2 elements.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

Child Class:

- [`maxon.Tuple`](maxon.Tuple.md#module-maxon.Tuple)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Get`](#maxon.Pair.Get)(ELEMENTTYPE) | Returns an entry of the Pair. |
| [`GetFirst`](#maxon.Pair.GetFirst)() | Retrieves the first entry stored in the *maxon.Pair*. |
| [`GetSecond`](#maxon.Pair.GetSecond)() | Retrieves the second entry stored in the *maxon.Pair*. |
| [`GetTypeArguments`](#maxon.Pair.GetTypeArguments)() | Retrieves the [`maxon.DataType`](../base_core/maxon.DataType.md#module-maxon.DataType) from an argument |
| [`Set`](#maxon.Pair.Set)(ELEMENTTYPE, obj) | Defines a value of the Pair. |
| [`SetReturnType`](#maxon.Pair.SetReturnType)(type) | Defines the returned type. |
| [`__getitem__`](#maxon.Pair.__getitem__)(index) | Gets the item at the given index in the pair. |
| [`__init__`](#maxon.Pair.__init__)(typename) | Initializes the appropriate C++ Data object and store it within the _data member. |
| [`__iter__`](#maxon.Pair.__iter__)() | Iterates over the two elements of the pair. |
| [`__maxon_convert__`](#maxon.Pair.__maxon_convert__)([expected]) |  |
| [`__setitem__`](#maxon.Pair.__setitem__)(key, value) | Sets the item for the given index in the pair. |

## Methods Definition <a id="methods-definition"></a>

### `Pair.Get(ELEMENTTYPE)` <a id="maxon.Pair.Get"></a>

Returns an entry of the Pair.

**Parameters:** **ELEMENTTYPE** (*int*) – The index of the element to retrieve from the this *maxon.Pair*.

**Returns:** The data stored

**Return type:** [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

### `Pair.GetFirst()` <a id="maxon.Pair.GetFirst"></a>

Retrieves the first entry stored in the *maxon.Pair*.

**Returns:** The first entry of this *maxon.Pair*.

**Return type:** [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

### `Pair.GetSecond()` <a id="maxon.Pair.GetSecond"></a>

Retrieves the second entry stored in the *maxon.Pair*.

**Returns:** The second entry of this *maxon.Pair*.

**Return type:** [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

### `Pair.GetTypeArguments()` <a id="maxon.Pair.GetTypeArguments"></a>

Retrieves the [`maxon.DataType`](../base_core/maxon.DataType.md#module-maxon.DataType) from an argument

**Returns:** The list of argument and [`maxon.DataType`](../base_core/maxon.DataType.md#module-maxon.DataType).

**Return type:** list[[`maxon.DataType`](../base_core/maxon.DataType.md#module-maxon.DataType), type)

### `Pair.Set(ELEMENTTYPE, obj)` <a id="maxon.Pair.Set"></a>

Defines a value of the Pair.

**Parameters:**

- **ELEMENTTYPE** (*int*) – The index of the element to set the value from the this *maxon.Pair*.
- **obj** ([`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)) – The data to store stored

### `Pair.SetReturnType(type)` <a id="maxon.Pair.SetReturnType"></a>

Defines the returned type.

**Parameters:** **type** – The return type expected.

**Type:** type

### `Pair.__getitem__(index)` <a id="maxon.Pair.__getitem__"></a>

Gets the item at the given index in the pair.

**Parameters:** **index** (*int*) – The index to retrieve the value for.

**Raises:** **IndexError** – When index is out of bounds.

**Returns:** The retrieved item.

**Return type:** [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

### `Pair.__init__(typename)` <a id="maxon.Pair.__init__"></a>

Initializes the appropriate C++ Data object and store it within the _data member.

If C is a Data then _data store a copy the C++ Data is done and stored.  
If C is a C++ Data then _data store a reference of the C++ Data.  
If C is not defined the C++ data is created and stored in the _data member.

**Parameters:** **C** (Optional[[`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)]) – Input data from which the Data should be created.

### `Pair.__iter__()` <a id="maxon.Pair.__iter__"></a>

Iterates over the two elements of the pair.

### `Pair.__maxon_convert__(expected=None)` <a id="maxon.Pair.__maxon_convert__"></a>

### `Pair.__setitem__(key, value)` <a id="maxon.Pair.__setitem__"></a>

Sets the item for the given index in the pair.

**Parameters:**

- **index** (*int*) – The index of the value to set.
- **value** (Optional[[`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)]) – The value to set for *index*.

**Raises:** **IndexError** – When index is out of bounds.
