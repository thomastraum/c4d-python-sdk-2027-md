<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/core/maxon.RegistryInterface.html -->

# maxon.RegistryInterface <a id="maxon-registryinterface"></a>

## Description <a id="module-maxon.RegistryInterface"></a><a id="description"></a>

[`maxon.RegistryInterface`](#module-maxon.RegistryInterface) is used internally by [`maxon.Registry`](../../references/core/maxon.Registry.md#module-maxon.Registry).

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`CreateIterator`](#maxon.RegistryInterface.CreateIterator)(reg) | Returns an iterator over all entries registered at this registry. |
| [`EraseEntry`](#maxon.RegistryInterface.EraseEntry)(registry, eid) | Removes the entry identified by eid from registry. |
| [`Find`](#maxon.RegistryInterface.Find)(id) | Returns the registry entry registered at this registry under the given identifier |
| [`FindEntryValue`](#maxon.RegistryInterface.FindEntryValue)(registry, eid) | Returns the registry entry registered at the passed registry under the given identifier |
| [`GetDataType`](#maxon.RegistryInterface.GetDataType)() | Returns the [`maxon.DataType`](../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType). |
| [`GetId`](#maxon.RegistryInterface.GetId)() | Returns the [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id). |
| [`GetStamp`](#maxon.RegistryInterface.GetStamp)() | Returns the registry stamp. |
| [`InsertEntry`](#maxon.RegistryInterface.InsertEntry)(registry, eid, value) | Registers an entry at the registry under the given identifier. |

## Methods Definition <a id="methods-definition"></a>

### *static* `RegistryInterface.CreateIterator(reg)` <a id="maxon.RegistryInterface.CreateIterator"></a>

Returns an iterator over all entries registered at this registry.

**Parameters:** **reg** ([`maxon.Registry`](../../references/core/maxon.Registry.md#module-maxon.Registry)) – The registry.

**Returns:** An iterator.

### *static* `RegistryInterface.EraseEntry(registry, eid)` <a id="maxon.RegistryInterface.EraseEntry"></a>

Removes the entry identified by eid from registry.

> **Note:** If no such entry exists, nothing happens.

**Parameters:**

- **registry** ([`maxon.Registry`](../../references/core/maxon.Registry.md#module-maxon.Registry)) – The registry to add the data.
- **eid** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Identifier within this registry.

### *static* `RegistryInterface.Find(id)` <a id="maxon.RegistryInterface.Find"></a>

Returns the registry entry registered at this registry under the given identifier

> **Note:** If no entry exists for the given identifier, None is returned.

**Parameters:**

- **id** – Identifier within this registry.
- **id** – [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)

**Returns:** The value stored in the registry.

**Return type:** [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### *static* `RegistryInterface.FindEntryValue(registry, eid)` <a id="maxon.RegistryInterface.FindEntryValue"></a>

Returns the registry entry registered at the passed registry under the given identifier

**Parameters:**

- **registry** ([`maxon.Registry`](../../references/core/maxon.Registry.md#module-maxon.Registry)) – The registry to find the value from.
- **eid** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Identifier within this registry.

**Returns:** The value stored in the registry.

**Return type:** [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `RegistryInterface.GetDataType()` <a id="maxon.RegistryInterface.GetDataType"></a>

Returns the [`maxon.DataType`](../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType).

**Returns:** The data type.

**Return type:** [`maxon.DataType`](../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)

### `RegistryInterface.GetId()` <a id="maxon.RegistryInterface.GetId"></a>

Returns the [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id).

**Returns:** The id.

**Return type:** [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)

### `RegistryInterface.GetStamp()` <a id="maxon.RegistryInterface.GetStamp"></a>

Returns the registry stamp.

**Returns:** The registry stamp.

**Return type:** int

### *static* `RegistryInterface.InsertEntry(registry, eid, value)` <a id="maxon.RegistryInterface.InsertEntry"></a>

Registers an entry at the registry under the given identifier.

> **Note:** If an entry already exists for the identifier, nothing happens, and an error is raised.

**Parameters:**

- **registry** ([`maxon.Registry`](../../references/core/maxon.Registry.md#module-maxon.Registry)) – The registry to add the data.
- **eid** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Identifier within this registry.
- **value** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – Value to register.
