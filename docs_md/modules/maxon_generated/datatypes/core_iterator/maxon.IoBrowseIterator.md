<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/core_iterator/maxon.IoBrowseIterator.html -->

# maxon.IoBrowseIterator <a id="maxon-iobrowseiterator"></a>

## Description <a id="module-maxon.IoBrowseIterator"></a><a id="description"></a>

Represents a python iterator for an [`maxon.IoBrowseInterface`](../../interfaces/io/maxon.IoBrowseInterface.md#module-maxon.IoBrowseInterface)

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetIoBrowse`](#maxon.IoBrowseIterator.GetIoBrowse)() | Retrieves the internal iterator object. |
| [`Init`](#maxon.IoBrowseIterator.Init)(cls, iteratorObject) | Initializes the passed cls object with the iterator. |
| [`__init__`](#maxon.IoBrowseIterator.__init__)(iteratorObject) | Initialize self. |
| [`__iter__`](#maxon.IoBrowseIterator.__iter__)() | Iterates all values from the current url. |

## Methods Definition <a id="methods-definition"></a>

### `IoBrowseIterator.GetIoBrowse()` <a id="maxon.IoBrowseIterator.GetIoBrowse"></a>

Retrieves the internal iterator object. :return:

### *classmethod* `IoBrowseIterator.Init(cls, iteratorObject)` <a id="maxon.IoBrowseIterator.Init"></a>

Initializes the passed cls object with the iterator.

**Parameters:** **iteratorObject** ([`maxon.IoBrowseRef`](../../references/io/maxon.IoBrowseRef.md#module-maxon.IoBrowseRef)) – an IteratorObject

**Returns:** The initialized Iterator

**Return type:** [`maxon.IoBrowseRef`](../../references/io/maxon.IoBrowseRef.md#module-maxon.IoBrowseRef)

### `IoBrowseIterator.__init__(iteratorObject)` <a id="maxon.IoBrowseIterator.__init__"></a>

Initialize self. See help(type(self)) for accurate signature.

### `IoBrowseIterator.__iter__()` <a id="maxon.IoBrowseIterator.__iter__"></a>

Iterates all values from the current url.
