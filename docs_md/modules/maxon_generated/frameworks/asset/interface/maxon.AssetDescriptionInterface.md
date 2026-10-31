<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.AssetDescriptionInterface.html -->

# maxon.AssetDescriptionInterface <a id="maxon-assetdescriptioninterface"></a>

## Description <a id="module-maxon.AssetDescriptionInterface"></a><a id="description"></a>

Represents all meta information about an asset, namely its identifier and version, the [`maxon.AssetMetaData`](../reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData) and some further information. `AssetRepositoryInterface.FindAssets()` yields the found assets not as [`maxon.Asset`](../reference/maxon.Asset.md#module-maxon.Asset), but as [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription) to avoid unnecessary loading of the assets. When you really need the asset itself you have to call Load on the description.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetBaseInterface`](maxon.AssetBaseInterface.md#module-maxon.AssetBaseInterface)

Child Class:

- [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.AssetDescriptionInterface.VIRTUAL`](maxon.AssetDescriptionInterface.VIRTUAL.md#maxon.AssetDescriptionInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`EraseMetaData`](#maxon.AssetDescriptionInterface.EraseMetaData)(attr, kind) | EraseMetaData removes meta data from the asset. |
| [`GetMetaData`](#maxon.AssetDescriptionInterface.GetMetaData)() | Returns the meta data of this asset. |
| [`GetMetaString`](#maxon.AssetDescriptionInterface.GetMetaString)(key[, languageRef, fallback]) | Returns the translated string from a asset. |
| [`GetUrl`](#maxon.AssetDescriptionInterface.GetUrl)() | Returns the [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) where the asset is stored. |
| [`IsDeleted`](#maxon.AssetDescriptionInterface.IsDeleted)() | Returns **True** if this asset description is a delete marker. |
| [`Load`](#maxon.AssetDescriptionInterface.Load)([updateLinks]) | Loads the asset. |
| [`StoreDecryptionKey`](#maxon.AssetDescriptionInterface.StoreDecryptionKey)(license, licenseKey, …) | Stores the key for asset decryption in the asset’s meta data. |
| [`StoreMetaData`](#maxon.AssetDescriptionInterface.StoreMetaData)(attr, data, kind) | Stores *data* for the meta data attribute #attr of this asset. |
| [`StoreMetaString`](#maxon.AssetDescriptionInterface.StoreMetaString)(key, value, languageRef) | Stores the name of an asset for a language. |
| [`StoreUrlMetaData`](#maxon.AssetDescriptionInterface.StoreUrlMetaData)(metaId, source, kind) | Copies the file or directory #source as meta data for the meta data attribute #metaId of this *asset*. |

## Methods Definition <a id="methods-definition"></a>

### `AssetDescriptionInterface.EraseMetaData(attr, kind)` <a id="maxon.AssetDescriptionInterface.EraseMetaData"></a>

EraseMetaData removes meta data from the asset.

### `AssetDescriptionInterface.GetMetaData()` <a id="maxon.AssetDescriptionInterface.GetMetaData"></a>

Returns the meta data of this asset.

**Returns:** The meta data of this asset.

**Return type:** [`maxon.AssetMetaData`](../reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)

### `AssetDescriptionInterface.GetMetaString(key, languageRef=None, fallback='')` <a id="maxon.AssetDescriptionInterface.GetMetaString"></a>

Returns the translated string from a asset.

**Parameters:**

- **key** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – Attribute id to load. e.g. `maxon.OBJECT.BASE.NAME`.
- **languageRef** (Optional[[`maxon.LanguageRef`](../../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)]) – Optional language. By default the function uses the current language.
- **fallback** (*str*) – Fallback string if the asset has no name.

**Returns:** String on success.

**Return type:** str

### `AssetDescriptionInterface.GetUrl()` <a id="maxon.AssetDescriptionInterface.GetUrl"></a>

Returns the [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) where the asset is stored.

**Returns:** The [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) of this asset, may be empty if the asset isn’t accessible through a [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url).

**Return type:** [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)

### `AssetDescriptionInterface.IsDeleted()` <a id="maxon.AssetDescriptionInterface.IsDeleted"></a>

Returns **True** if this asset description is a delete marker. Delete markers are stored in repositories upon call of [`AssetRepositoryInterface.DeleteAsset()`](maxon.AssetRepositoryInterface.md#maxon.AssetRepositoryInterface.DeleteAsset) to indicate a deleted asset, but previous asset versions still exist in the repository.

**Returns:** **True** if this description represents a delete marker, **False** otherwise.

**Return type:** bool

### `AssetDescriptionInterface.Load(updateLinks=None)` <a id="maxon.AssetDescriptionInterface.Load"></a>

Loads the asset. The implementation may use caching to avoid repeated loading of the same asset.

**Parameters:** **updateLinks** (*Optional*[*bool*]) – **None** if the asset shall be loaded as is. A bool if asset links which use `maxon.ASSET_UPDATE_POLICY.IMPLICIT` shall be resolved to the latest version. The bool is set to **True** by this method whenever there is a link where the resolved version differs from the original version.

**Returns:** The loaded asset.

**Return type:** [`maxon.Asset`](../reference/maxon.Asset.md#module-maxon.Asset)

### `AssetDescriptionInterface.StoreDecryptionKey(license, licenseKey, assetDecryptionKey)` <a id="maxon.AssetDescriptionInterface.StoreDecryptionKey"></a>

Stores the key for asset decryption in the asset’s meta data. After copying an asset with encryption (see [`AssetRepositoryInterface.CopyAsset()`](maxon.AssetRepositoryInterface.md#maxon.AssetRepositoryInterface.CopyAsset)), you have to call this method once for each license with which decryption shall be possible.

**Parameters:**

- **license** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The license/license feature which allows access to the asset.
- **licenseKey** (`maxon.CryptoKey`) – The encryption key of the license.
- **assetDecryptionKey** (`maxon.CryptoKey`) – The key with which the encrypted asset can be decrypted.

### `AssetDescriptionInterface.StoreMetaData(attr, data, kind)` <a id="maxon.AssetDescriptionInterface.StoreMetaData"></a>

Stores *data* for the meta data attribute #attr of this asset. Observers of `AssetRepositoryInterface.ObservableMetaDataStored()` of the repository of the asset and its derived repositories are informed.

**Parameters:**

- **attr** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The meta data attribute.
- **data** ([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The value to set.
- **kind** ([`maxon.AssetMetaDataInterface.KIND`](../../../enums/maxon.AssetMetaDataInterface.KIND.md#module-maxon.AssetMetaDataInterface.KIND)) – The kind of the meta data.

### `AssetDescriptionInterface.StoreMetaString(key, value, languageRef)` <a id="maxon.AssetDescriptionInterface.StoreMetaString"></a>

Stores the name of an asset for a language.

**Parameters:**

- **key** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – Attribute id to save. e.g. maxon.OBJECT.BASE.NAME.
- **value** (*str*) – New String
- **languageRef** (Optional[[`maxon.LanguageRef`](../../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)]) – Optional language. By default the function uses the current language.

### `AssetDescriptionInterface.StoreUrlMetaData(metaId, source, kind)` <a id="maxon.AssetDescriptionInterface.StoreUrlMetaData"></a>

Copies the file or directory #source as meta data for the meta data attribute #metaId of this *asset*. The value of the meta data attribute will be a [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) which points to the local copy within the asset (i.e., not to *source*) of the form *{meta:///assetid/metaid.kind.extension}*, so the file name extension of *source* gets preserved.

Observers of ObservableMetaDataStored of this repository and its derived repositories are informed.

**Parameters:**

- **metaId** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The identifier of the meta data attribute.
- **source** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – The source which shall be copied as meta data to *asset*. Pass empty Url to erase meta data.
- **kind** ([`maxon.AssetMetaDataInterface.KIND`](../../../enums/maxon.AssetMetaDataInterface.KIND.md#module-maxon.AssetMetaDataInterface.KIND)) – The kind of the meta data.
