<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.AssetMetaDataInterface.html -->

# maxon.AssetMetaDataInterface <a id="maxon-assetmetadatainterface"></a>

## Description <a id="module-maxon.AssetMetaDataInterface"></a><a id="description"></a>

[`maxon.AssetMetaData`](../reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData) allows to query the meta data of an asset. It is returned by [`maxon.AssetDescriptionInterface.GetMetaData()`](maxon.AssetDescriptionInterface.md#maxon.AssetDescriptionInterface.GetMetaData). The methods of this interface are thread-safe, but the meta data of an asset may be hanged concurrently, so the returned values may differ from call to call even when the calling thread made no modification inbetween.

You can’t modify the meta data of an asset through this interface, you have to use [`maxon.AssetDescriptionInterface.StoreMetaData()`](maxon.AssetDescriptionInterface.md#maxon.AssetDescriptionInterface.StoreMetaData) instead.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.AssetMetaData`](../reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Get`](#maxon.AssetMetaDataInterface.Get)(metaId[, defaultValue]) | Returns the current value of the meta data entry for the meta data attribute #metaId. |
| [`GetExistingEntries`](#maxon.AssetMetaDataInterface.GetExistingEntries)() | Returns an array with the current set of meta data entries. |
| [`GetTimeStamp`](#maxon.AssetMetaDataInterface.GetTimeStamp)(metaId) | Returns the time stamp for the meta data attribute #metaId. |

## Methods Definition <a id="methods-definition"></a>

### `AssetMetaDataInterface.Get(metaId, defaultValue=None)` <a id="maxon.AssetMetaDataInterface.Get"></a>

Returns the current value of the meta data entry for the meta data attribute #metaId.

**Parameters:**

- **metaId** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The identifier of the meta data attribute.
- **defaultValue** (*Any*) – The default value to use when there is no entry.

**Returns:**

The current value for the id, or the defaultValue if there is no entry.  
An error is returned if there is an entry, but loading the entry value fails.

> **Note:** The returned value may differ from call to call because another thread could have modified the meta data inbetween.

**Return type:** [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `AssetMetaDataInterface.GetExistingEntries()` <a id="maxon.AssetMetaDataInterface.GetExistingEntries"></a>

Returns an array with the current set of meta data entries.

**Returns:**

The current set of meta data entries given by the meta data attribute id and kind.

> **Note:** The returned value may differ from call to call because another thread could have modified the meta data inbetween.

**Return type:** [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), [`maxon.AssetMetaDataInterface.KIND`](../../../enums/maxon.AssetMetaDataInterface.KIND.md#module-maxon.AssetMetaDataInterface.KIND)]]

### `AssetMetaDataInterface.GetTimeStamp(metaId)` <a id="maxon.AssetMetaDataInterface.GetTimeStamp"></a>

Returns the time stamp for the meta data attribute #metaId. The time stamp is increased each time the value changes.

**Parameters:** **metaId** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The identifier of the meta data attribute.

**Returns:**

The time stamp for the attribute, or 0 if there is no entry for the attribute.

> **Note:** The returned value may differ from call to call because another thread could have modified the meta data inbetween.

**Return type:** int
