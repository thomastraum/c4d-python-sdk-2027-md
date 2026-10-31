<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.ColorCategoryAssetInterface.html -->

# maxon.ColorCategoryAssetInterface <a id="maxon-colorcategoryassetinterface"></a>

## Description <a id="module-maxon.ColorCategoryAssetInterface"></a><a id="description"></a>

Implementation of a color category asset.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetInterface`](maxon.AssetInterface.md#module-maxon.AssetInterface)

Child Class:

- [`maxon.ColorCategoryAsset`](../reference/maxon.ColorCategoryAsset.md#module-maxon.ColorCategoryAsset)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.ColorCategoryAssetInterface.VIRTUAL`](maxon.ColorCategoryAssetInterface.VIRTUAL.md#maxon.ColorCategoryAssetInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Create`](#maxon.ColorCategoryAssetInterface.Create)() | Returns a new color category asset. |
| [`GetColorCategory`](#maxon.ColorCategoryAssetInterface.GetColorCategory)(asset, lookupRepository) | Returns the color category of an asset. |
| [`SetColorCategory`](#maxon.ColorCategoryAssetInterface.SetColorCategory)(*args) | Stores a color category for an asset. |

## Methods Definition <a id="methods-definition"></a>

### *static* `ColorCategoryAssetInterface.Create()` <a id="maxon.ColorCategoryAssetInterface.Create"></a>

Returns a new color category asset.

**Returns:** A new reference of [`maxon.ColorCategoryAssetInterface`](#module-maxon.ColorCategoryAssetInterface).

**Return type:** [`maxon.ColorCategoryAsset`](../reference/maxon.ColorCategoryAsset.md#module-maxon.ColorCategoryAsset).

### *static* `ColorCategoryAssetInterface.GetColorCategory(asset, lookupRepository)` <a id="maxon.ColorCategoryAssetInterface.GetColorCategory"></a>

Returns the color category of an asset.

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to use.
- **lookupRepository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to look up for dependencies.

**Returns:** Tuple\<Id, Color>.

**Return type:** [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.Color`](../../../datatypes/vec_col_mat/maxon.Color.md#module-maxon.Color)]

### *static* `ColorCategoryAssetInterface.SetColorCategory(*args)` <a id="maxon.ColorCategoryAssetInterface.SetColorCategory"></a>

Stores a color category for an asset.

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to modify
- **category** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Category to use.
