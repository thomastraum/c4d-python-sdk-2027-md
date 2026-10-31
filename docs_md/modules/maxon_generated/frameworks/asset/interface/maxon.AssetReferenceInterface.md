<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.AssetReferenceInterface.html -->

# maxon.AssetReferenceInterface <a id="maxon-assetreferenceinterface"></a>

## Description <a id="module-maxon.AssetReferenceInterface"></a><a id="description"></a>

[`maxon.AssetReference`](../reference/maxon.AssetReference.md#module-maxon.AssetReference) is needed for the asset update mechanism and represents a specific updatable [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink) within an asset, see `AssetInterface.GetReferencedAssets()`.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetBaseWithUpdateInterface`](maxon.AssetBaseWithUpdateInterface.md#module-maxon.AssetBaseWithUpdateInterface)

Child Class:

- [`maxon.AssetReference`](../reference/maxon.AssetReference.md#module-maxon.AssetReference)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.AssetReferenceInterface.VIRTUAL`](maxon.AssetReferenceInterface.VIRTUAL.md#maxon.AssetReferenceInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetLink`](#maxon.AssetReferenceInterface.GetLink)() | Returns the link which this AssetReference uses. |

## Methods Definition <a id="methods-definition"></a>

### `AssetReferenceInterface.GetLink()` <a id="maxon.AssetReferenceInterface.GetLink"></a>

Returns the link which this AssetReference uses.

**Returns:** The AssetLink of this reference.

**Return type:** [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink)
