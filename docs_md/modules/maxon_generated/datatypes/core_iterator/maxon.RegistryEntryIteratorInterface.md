<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/core_iterator/maxon.RegistryEntryIteratorInterface.html -->

# maxon.RegistryEntryIteratorInterface <a id="maxon-registryentryiteratorinterface"></a>

## Description <a id="module-maxon.RegistryEntryIteratorInterface"></a><a id="description"></a>

RegistryEntryIteratorInterface is used internally by `Registry.Iterator()`.

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Free`](#maxon.RegistryEntryIteratorInterface.Free)() | Free the resource used by the iterator. |
| [`GetEntry`](#maxon.RegistryEntryIteratorInterface.GetEntry)() | Retrieve the current entry |
| [`GetId`](#maxon.RegistryEntryIteratorInterface.GetId)() | Returns the [`maxon.Id`](../id/maxon.Id.md#module-maxon.Id). |
| [`HasValue`](#maxon.RegistryEntryIteratorInterface.HasValue)() | True if the object still contains value to iterate. |
| [`MoveToNext`](#maxon.RegistryEntryIteratorInterface.MoveToNext)() | Move to the next entry from the [`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary). |
| [`SetReturnType`](#maxon.RegistryEntryIteratorInterface.SetReturnType)(returnType) |  |
| [`__del__`](#maxon.RegistryEntryIteratorInterface.__del__)() |  |
| [`__iter__`](#maxon.RegistryEntryIteratorInterface.__iter__)() | Iterates over all elements available in the registry. |

## Methods Definition <a id="methods-definition"></a>

### *static* `RegistryEntryIteratorInterface.Free()` <a id="maxon.RegistryEntryIteratorInterface.Free"></a>

Free the resource used by the iterator.

### `RegistryEntryIteratorInterface.GetEntry()` <a id="maxon.RegistryEntryIteratorInterface.GetEntry"></a>

Retrieve the current entry

**Returns:** The value for the current entry.

**Return type:** Any

### `RegistryEntryIteratorInterface.GetId()` <a id="maxon.RegistryEntryIteratorInterface.GetId"></a>

Returns the [`maxon.Id`](../id/maxon.Id.md#module-maxon.Id).

**Returns:** The id

**Return type:** [`maxon.Id`](../id/maxon.Id.md#module-maxon.Id)

### `RegistryEntryIteratorInterface.HasValue()` <a id="maxon.RegistryEntryIteratorInterface.HasValue"></a>

True if the object still contains value to iterate.

**Returns:** True if the object still contains value to iterate.

**Return type:** bool

### `RegistryEntryIteratorInterface.MoveToNext()` <a id="maxon.RegistryEntryIteratorInterface.MoveToNext"></a>

Move to the next entry from the [`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary).

### `RegistryEntryIteratorInterface.SetReturnType(returnType)` <a id="maxon.RegistryEntryIteratorInterface.SetReturnType"></a>

### `RegistryEntryIteratorInterface.__del__()` <a id="maxon.RegistryEntryIteratorInterface.__del__"></a>

### `RegistryEntryIteratorInterface.__iter__()` <a id="maxon.RegistryEntryIteratorInterface.__iter__"></a>

Iterates over all elements available in the registry.
