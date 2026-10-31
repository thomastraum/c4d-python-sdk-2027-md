<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/collection/maxon.Tuple.html -->

# maxon.Tuple <a id="maxon-tuple"></a>

## Description <a id="module-maxon.Tuple"></a><a id="description"></a>

[`maxon.Tuple`](#module-maxon.Tuple) provides in-place static storage for elements of arbitrary types.  
Represents an immutable list of items of identical type.  
Is similar to [`maxon.Pair`](maxon.Pair.md#module-maxon.Pair) but supports more than two elements.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Pair`](maxon.Pair.md#module-maxon.Pair)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`__init__`](#maxon.Tuple.__init__)(typename) | Initializes the appropriate C++ Data object and store it within the _data member. |

## Methods Definition <a id="methods-definition"></a>

### `Tuple.__init__(typename)` <a id="maxon.Tuple.__init__"></a>

Initializes the appropriate C++ Data object and store it within the _data member.

If C is a Data then _data store a copy the C++ Data is done and stored.  
If C is a C++ Data then _data store a reference of the C++ Data.  
If C is not defined the C++ data is created and stored in the _data member.

**Parameters:** **C** (Optional[[`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)]) – Input data from which the Data should be created.
