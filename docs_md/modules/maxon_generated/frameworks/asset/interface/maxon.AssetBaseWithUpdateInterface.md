<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.AssetBaseWithUpdateInterface.html -->

# maxon.AssetBaseWithUpdateInterface <a id="maxon-assetbasewithupdateinterface"></a>

## Description <a id="module-maxon.AssetBaseWithUpdateInterface"></a><a id="description"></a>

The base interface of [`maxon.AssetInterface`](maxon.AssetInterface.md#module-maxon.AssetInterface) and [`maxon.AssetReferenceInterface`](maxon.AssetReferenceInterface.md#module-maxon.AssetReferenceInterface). It inherits from [`maxon.AssetBaseInterface`](maxon.AssetBaseInterface.md#module-maxon.AssetBaseInterface) and adds a methods to obtain the update counter.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetBaseInterface`](maxon.AssetBaseInterface.md#module-maxon.AssetBaseInterface)

Children Classes:

- [`maxon.AssetBaseWithUpdate`](../reference/maxon.AssetBaseWithUpdate.md#module-maxon.AssetBaseWithUpdate)
- [`maxon.AssetReferenceInterface`](maxon.AssetReferenceInterface.md#module-maxon.AssetReferenceInterface)
- [`maxon.AssetInterface`](maxon.AssetInterface.md#module-maxon.AssetInterface)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.AssetBaseWithUpdateInterface.VIRTUAL`](maxon.AssetBaseWithUpdateInterface.VIRTUAL.md#maxon.AssetBaseWithUpdateInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetUpdate`](#maxon.AssetBaseWithUpdateInterface.GetUpdate)() | Returns the update counter of the asset. |

## Methods Definition <a id="methods-definition"></a>

### `AssetBaseWithUpdateInterface.GetUpdate()` <a id="maxon.AssetBaseWithUpdateInterface.GetUpdate"></a>

Returns the update counter of the asset. The update counter is incremented whenever an asset is updated because one of its references to other assets is updated to a newer version of the referenced asset. This does not lead to a newer repository version of the asset itself because the asset definition isn’t changed. Therefore the version identifier stays the same, just the update counter changes.

The update counter is 0 for the asset which exacly matches the original version (returned by [`AssetDescriptionInterface.Load()`](maxon.AssetDescriptionInterface.md#maxon.AssetDescriptionInterface.Load) when it is called with a None argument).

**Returns:** Update counter of the asset.

**Return type:** int
