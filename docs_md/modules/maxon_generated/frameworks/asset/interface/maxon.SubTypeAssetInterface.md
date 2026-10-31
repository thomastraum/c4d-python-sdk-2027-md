<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.SubTypeAssetInterface.html -->

# maxon.SubTypeAssetInterface <a id="maxon-subtypeassetinterface"></a>

## Description <a id="module-maxon.SubTypeAssetInterface"></a><a id="description"></a>

Implements the SubTypeAsset. This subtype specializes for example FileAssets.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetInterface`](maxon.AssetInterface.md#module-maxon.AssetInterface)

Child Class:

- [`maxon.SubTypeAsset`](../reference/maxon.SubTypeAsset.md#module-maxon.SubTypeAsset)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.SubTypeAssetInterface.VIRTUAL`](maxon.SubTypeAssetInterface.VIRTUAL.md#maxon.SubTypeAssetInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Create`](#maxon.SubTypeAssetInterface.Create)() | Creates a new SubtypeAsset. |
| [`SetSubType`](#maxon.SubTypeAssetInterface.SetSubType)(target, subtype) | Stores the subtype of an asset. |

## Methods Definition <a id="methods-definition"></a>

### *static* `SubTypeAssetInterface.Create()` <a id="maxon.SubTypeAssetInterface.Create"></a>

Creates a new SubtypeAsset.

**Returns:**

**Return type:** [`maxon.SubTypeAsset`](../reference/maxon.SubTypeAsset.md#module-maxon.SubTypeAsset)

### *static* `SubTypeAssetInterface.SetSubType(target, subtype)` <a id="maxon.SubTypeAssetInterface.SetSubType"></a>

Stores the subtype of an asset.

**Parameters:**

- **target** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to modify.
- **subtype** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Subtype to store.
