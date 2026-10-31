<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.AssetUtilitiesInterface.html -->

# maxon.AssetUtilitiesInterface <a id="maxon-assetutilitiesinterface"></a>

## Description <a id="module-maxon.AssetUtilitiesInterface"></a><a id="description"></a>

Helper Interface for Asset functions.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`AssetSetMetaData`](#maxon.AssetUtilitiesInterface.AssetSetMetaData)(asset, assetName, …) | Sets the asset meta data for the given asset. |
| [`GetAssetIcon`](#maxon.AssetUtilitiesInterface.GetAssetIcon)(asset) | Returns the asset icon. |
| [`IncreaseAssetVersion`](#maxon.AssetUtilitiesInterface.IncreaseAssetVersion)(currentVersion) | IncreaseAssetVersion description. |

## Methods Definition <a id="methods-definition"></a>

### *static* `AssetUtilitiesInterface.AssetSetMetaData(asset, assetName, assetVersion, assetCategory)` <a id="maxon.AssetUtilitiesInterface.AssetSetMetaData"></a>

Sets the asset meta data for the given asset.

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to modify
- **assetName** (*str*) – Human readable asset name.
- **assetVersion** (*str*) – Asset version to set.
- **assetCategory** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Asset category to set.

### *static* `AssetUtilitiesInterface.GetAssetIcon(asset)` <a id="maxon.AssetUtilitiesInterface.GetAssetIcon"></a>

Returns the asset icon.

It returns the preview stored under ASSETMETADATA.ASSET_PREVIEWIMAGEURL

**Parameters:** **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to use.

**Returns:** Url to the preview icon on success.

**Return type:** [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)

### *static* `AssetUtilitiesInterface.IncreaseAssetVersion(currentVersion)` <a id="maxon.AssetUtilitiesInterface.IncreaseAssetVersion"></a>

IncreaseAssetVersion description.

**Parameters:** **currentVersion** (*str*) – Increases the version string by one. e.g. “1.0” -> “1.1” or “1.0.99” -> “1.1.00”

**Returns:** New Version String on success.

**Return type:** str
