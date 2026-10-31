<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/references/core/maxon.Registry.html -->

# maxon.Registry <a id="maxon-registry"></a>

## Description <a id="module-maxon.Registry"></a><a id="description"></a>

Registries are used to register specific implementations of a given interface.  
An implementation that is registered in such a registry can then be accessed with a specific ID from anywhere in the application.

## Inheritance diagram <a id="inheritance-diagram"></a>

Children Classes:

- [`maxon.Classes`](../../registries/maxon.Classes.md#module-maxon.Classes)
- [`maxon.DataTypes`](../../registries/maxon.DataTypes.md#module-maxon.DataTypes)
- [`maxon.Loggers`](../../registries/maxon.Loggers.md#module-maxon.Loggers)
- [`maxon.LoggerTypes`](../../registries/maxon.LoggerTypes.md#module-maxon.LoggerTypes)
- [`maxon.IoHandlers`](../../registries/maxon.IoHandlers.md#module-maxon.IoHandlers)
- [`maxon.FileFormats`](../../registries/maxon.FileFormats.md#module-maxon.FileFormats)
- [`maxon.FileFormatHandlers`](../../registries/maxon.FileFormatHandlers.md#module-maxon.FileFormatHandlers)
- [`maxon.ParametricTypes`](../../registries/maxon.ParametricTypes.md#module-maxon.ParametricTypes)
- [`maxon.AssetTypes`](../../frameworks/asset/registry/maxon.AssetTypes.md#module-maxon.AssetTypes)
- `maxon.AssetRepositoryTypes`
- [`maxon.CustomDataTagDisplayClasses`](../../frameworks/mesh_misc/registry/maxon.CustomDataTagDisplayClasses.md#module-maxon.CustomDataTagDisplayClasses)
- [`maxon.FilterClasses`](../../frameworks/render_filter/registry/maxon.FilterClasses.md#module-maxon.FilterClasses)
- [`maxon.FilterCommandQueueClasses`](../../frameworks/render_filter/registry/maxon.FilterCommandQueueClasses.md#module-maxon.FilterCommandQueueClasses)
- [`maxon.FilterContextClasses`](../../frameworks/render_filter/registry/maxon.FilterContextClasses.md#module-maxon.FilterContextClasses)
- [`maxon.FilterImageClasses`](../../frameworks/render_filter/registry/maxon.FilterImageClasses.md#module-maxon.FilterImageClasses)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Get`](#maxon.Registry.Get)(eid) | Retrieves the object stored with the given [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id) within the current registry. |
| [`GetEntries`](#maxon.Registry.GetEntries)() | Retrieve a RegistryIterator that can be iterate with a for loop. |
| [`GetId`](#maxon.Registry.GetId)() | Return the identifier of this registry. |
| [`Insert`](#maxon.Registry.Insert)(eid, object) | Inserts a new entry into the current registry. |
| [`__getitem__`](#maxon.Registry.__getitem__)(item) | Retrieves an entry in the registry. |
| [`__iter__`](#maxon.Registry.__iter__)() | Iterates over all elements available in the registry. |
| [`__len__`](#maxon.Registry.__len__)() | Returns the number of entries in the registry. |

## Methods Definition <a id="methods-definition"></a>

### *classmethod* `Registry.Get(eid)` <a id="maxon.Registry.Get"></a>

Retrieves the object stored with the given [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id) within the current registry.

**Parameters:** **eid** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The object identifier to access into the registry.

**Returns:** The object stored in the current registry matching the [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id).

**Return type:** Any

**Raises:** **LookupError** – If value not inside the registry.

### *classmethod* `Registry.GetEntries()` <a id="maxon.Registry.GetEntries"></a>

Retrieve a RegistryIterator that can be iterate with a for loop.

**Returns:** an iterator.

### *classmethod* `Registry.GetId()` <a id="maxon.Registry.GetId"></a>

Return the identifier of this registry.

**Returns:** The identifier of this registry.

**Return type:** [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)

### *classmethod* `Registry.Insert(eid, object)` <a id="maxon.Registry.Insert"></a>

Inserts a new entry into the current registry.

**Parameters:**

- **eid** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The identifier of the object.
- **object** (*Any*) – The object to store into the registry.

**Returns:**

### `Registry.__getitem__(item)` <a id="maxon.Registry.__getitem__"></a>

Retrieves an entry in the registry.

**Parameters:** **item** ([`maxon.InternedId`](../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The identifier of the registry entry you want to retrieve.

### `Registry.__iter__()` <a id="maxon.Registry.__iter__"></a>

Iterates over all elements available in the registry.

### `Registry.__len__()` <a id="maxon.Registry.__len__"></a>

Returns the number of entries in the registry.

**Returns:** Number of entries in the registry.

**Return type:** int
