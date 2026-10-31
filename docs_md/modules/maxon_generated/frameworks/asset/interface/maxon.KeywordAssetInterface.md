<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.KeywordAssetInterface.html -->

# maxon.KeywordAssetInterface <a id="maxon-keywordassetinterface"></a>

## Description <a id="module-maxon.KeywordAssetInterface"></a><a id="description"></a>

An Asset represents digital content which can be managed by an [`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef) “asset repository”. The management includes versioning, meta data and automatic updates.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetInterface`](maxon.AssetInterface.md#module-maxon.AssetInterface)

Child Class:

- [`maxon.KeywordAsset`](../reference/maxon.KeywordAsset.md#module-maxon.KeywordAsset)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.KeywordAssetInterface.VIRTUAL`](maxon.KeywordAssetInterface.VIRTUAL.md#maxon.KeywordAssetInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`AddKeyword`](#maxon.KeywordAssetInterface.AddKeyword)(target, keywordId, userScope, …) | Adds a keyword to an asset. |
| [`Create`](#maxon.KeywordAssetInterface.Create)() | **return:** A new reference of [`maxon.KeywordAssetInterface`](#module-maxon.KeywordAssetInterface). |
| [`GetDefaultAsset`](#maxon.KeywordAssetInterface.GetDefaultAsset)(type, lookupRepository) | Returns the default preset for the given type. |
| [`GetDefaultAssetState`](#maxon.KeywordAssetInterface.GetDefaultAssetState)(ad) | Checks if the given asset is a preset. |
| [`HasKeyword`](#maxon.KeywordAssetInterface.HasKeyword)(target, keywordId) | Returns a populated id if the asset has a given keyword assigned. |
| [`IsFavouriteAsset`](#maxon.KeywordAssetInterface.IsFavouriteAsset)(ad) | Returns true if the given asset is a favourite. |
| [`RemoveKeyword`](#maxon.KeywordAssetInterface.RemoveKeyword)(target, keywordId, userScope) | Removes a keyword from an asset. |
| [`SetDefaultAsset`](#maxon.KeywordAssetInterface.SetDefaultAsset)(ad, on) | Sets the default state of the given preset asset. |

## Methods Definition <a id="methods-definition"></a>

### *static* `KeywordAssetInterface.AddKeyword(target, keywordId, userScope, updateUsageRepository)` <a id="maxon.KeywordAssetInterface.AddKeyword"></a>

Adds a keyword to an asset.

**Parameters:**

- **target** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to add keywords.
- **keywordId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Keyword Id to add.
- **userScope** (*bool*) – **True** to use [`maxon.ASSETMETADATA.UserKeywords`](../../../enums/maxon.ASSETMETADATA.UserKeywords.md#maxon.ASSETMETADATA.UserKeywords) otherwise [`maxon.ASSETMETADATA.Keywords`](../../../enums/maxon.ASSETMETADATA.Keywords.md#maxon.ASSETMETADATA.Keywords).
- **updateUsageRepository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – **True** to update the last used time and use count.

**Returns:** **True** if a keyword was added. **False** if the keyword was not added - that means it already exists.

**Return type:** bool

### *static* `KeywordAssetInterface.Create()` <a id="maxon.KeywordAssetInterface.Create"></a>

**Returns:** A new reference of [`maxon.KeywordAssetInterface`](#module-maxon.KeywordAssetInterface).

**Return type:** [`maxon.KeywordAsset`](../reference/maxon.KeywordAsset.md#module-maxon.KeywordAsset).

### *static* `KeywordAssetInterface.GetDefaultAsset(type, lookupRepository)` <a id="maxon.KeywordAssetInterface.GetDefaultAsset"></a>

Returns the default preset for the given type.

**Parameters:**

- **type** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Preset type.
- **lookupRepository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to search for.

**Returns:** AssetDescription on success.

**Return type:** [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### *static* `KeywordAssetInterface.GetDefaultAssetState(ad)` <a id="maxon.KeywordAssetInterface.GetDefaultAssetState"></a>

Checks if the given asset is a preset.

**Parameters:** **ad** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to look at.

**Returns:** First: **True** if it is an preset, Second: **True** if the asset is the default asset.

**Return type:** [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [bool, bool]

### *static* `KeywordAssetInterface.HasKeyword(target, keywordId)` <a id="maxon.KeywordAssetInterface.HasKeyword"></a>

Returns a populated id if the asset has a given keyword assigned.

**Parameters:**

- **target** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to search.
- **keywordId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Keyword Id to search.

**Returns:** Empty id if not found otherwise ASSETMETADATA::UserKeywords or ASSETMETADATA::Keywords if found.

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)

### *static* `KeywordAssetInterface.IsFavouriteAsset(ad)` <a id="maxon.KeywordAssetInterface.IsFavouriteAsset"></a>

Returns true if the given asset is a favourite.

**Parameters:** **ad** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to inspect.

**Returns:** **True** if favourite.

**Return type:** bool

### *static* `KeywordAssetInterface.RemoveKeyword(target, keywordId, userScope)` <a id="maxon.KeywordAssetInterface.RemoveKeyword"></a>

Removes a keyword from an asset.

**Parameters:**

- **target** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to remove keywords.
- **keywordId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Keyword Id to remove.
- **userScope** (*bool*) – **True** to use [`maxon.ASSETMETADATA.UserKeywords`](../../../enums/maxon.ASSETMETADATA.UserKeywords.md#maxon.ASSETMETADATA.UserKeywords) otherwise [`maxon.ASSETMETADATA.Keywords`](../../../enums/maxon.ASSETMETADATA.Keywords.md#maxon.ASSETMETADATA.Keywords).

**Returns:** **True** if a keyword was found and removed. **False** if the keyword was not found on the asset.

**Return type:** bool

### *static* `KeywordAssetInterface.SetDefaultAsset(ad, on)` <a id="maxon.KeywordAssetInterface.SetDefaultAsset"></a>

Sets the default state of the given preset asset. Every type can only have one preset as default.

**Parameters:**

- **ad** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to modify.
- **on** (*bool*) – **True** to make this preset the default. False to make it no longer the default.
