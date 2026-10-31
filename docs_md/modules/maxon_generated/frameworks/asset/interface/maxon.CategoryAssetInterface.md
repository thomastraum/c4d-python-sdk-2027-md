<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.CategoryAssetInterface.html -->

# maxon.CategoryAssetInterface <a id="maxon-categoryassetinterface"></a>

## Description <a id="module-maxon.CategoryAssetInterface"></a><a id="description"></a>

Implementation of category assets

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetInterface`](maxon.AssetInterface.md#module-maxon.AssetInterface)

Child Class:

- [`maxon.CategoryAsset`](../reference/maxon.CategoryAsset.md#module-maxon.CategoryAsset)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.CategoryAssetInterface.VIRTUAL`](maxon.CategoryAssetInterface.VIRTUAL.md#maxon.CategoryAssetInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Create`](#maxon.CategoryAssetInterface.Create)() | Create creates a new category asset. |
| [`GetParentCategory`](#maxon.CategoryAssetInterface.GetParentCategory)(asset) | Returns the category id of the given asset. |
| [`SetAssetCategory`](#maxon.CategoryAssetInterface.SetAssetCategory)(asset, category) | Allows to move an asset into a category. |

## Methods Definition <a id="methods-definition"></a>

### *static* `CategoryAssetInterface.Create()` <a id="maxon.CategoryAssetInterface.Create"></a>

Create creates a new category asset.

**Returns:** CategoryAsset on success.

**Return type:** [`maxon.CategoryAsset`](../reference/maxon.CategoryAsset.md#module-maxon.CategoryAsset)

### *static* `CategoryAssetInterface.GetParentCategory(asset)` <a id="maxon.CategoryAssetInterface.GetParentCategory"></a>

Returns the category id of the given asset.

**Parameters:** **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to investigate.

**Returns:** Category id on success.

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)

### *static* `CategoryAssetInterface.SetAssetCategory(asset, category)` <a id="maxon.CategoryAssetInterface.SetAssetCategory"></a>

Allows to move an asset into a category.

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to move.
- **category** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Category to use.
