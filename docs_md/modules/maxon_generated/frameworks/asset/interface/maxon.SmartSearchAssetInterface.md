<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.SmartSearchAssetInterface.html -->

# maxon.SmartSearchAssetInterface <a id="maxon-smartsearchassetinterface"></a>

## Description <a id="module-maxon.SmartSearchAssetInterface"></a><a id="description"></a>

Implements the smartsearch asset type.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetInterface`](maxon.AssetInterface.md#module-maxon.AssetInterface)

Child Class:

- [`maxon.SmartSearchAsset`](../reference/maxon.SmartSearchAsset.md#module-maxon.SmartSearchAsset)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.SmartSearchAssetInterface.VIRTUAL`](maxon.SmartSearchAssetInterface.VIRTUAL.md#maxon.SmartSearchAssetInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Create`](#maxon.SmartSearchAssetInterface.Create)() | Creates an new SmartSearchAsset. |
| [`GetFilterString`](#maxon.SmartSearchAssetInterface.GetFilterString)() | Returns the filter string stored in the smart search asset. |
| [`SetFilterString`](#maxon.SmartSearchAssetInterface.SetFilterString)(asset, filter) | Stores a new smartsearch in a SmartSearchAsset. |

## Methods Definition <a id="methods-definition"></a>

### *static* `SmartSearchAssetInterface.Create()` <a id="maxon.SmartSearchAssetInterface.Create"></a>

Creates an new SmartSearchAsset.

**Returns:** SmartSearchAsset

**Return type:** [`maxon.SmartSearchAsset`](../reference/maxon.SmartSearchAsset.md#module-maxon.SmartSearchAsset)

### `SmartSearchAssetInterface.GetFilterString()` <a id="maxon.SmartSearchAssetInterface.GetFilterString"></a>

Returns the filter string stored in the smart search asset.

**Returns:**

**Return type:** [`maxon.SmartSearchAsset`](../reference/maxon.SmartSearchAsset.md#module-maxon.SmartSearchAsset)

### *static* `SmartSearchAssetInterface.SetFilterString(asset, filter)` <a id="maxon.SmartSearchAssetInterface.SetFilterString"></a>

Stores a new smartsearch in a SmartSearchAsset.

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – SmartSearchAsset to modify.
- **filter** (*str*) – Fitler string to store.
