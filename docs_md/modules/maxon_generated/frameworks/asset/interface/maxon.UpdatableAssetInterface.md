<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.UpdatableAssetInterface.html -->

# maxon.UpdatableAssetInterface <a id="maxon-updatableassetinterface"></a>

## Description <a id="module-maxon.UpdatableAssetInterface"></a><a id="description"></a>

An [`maxon.UpdatableAsset`](../reference/maxon.UpdatableAsset.md#module-maxon.UpdatableAsset) is an [`maxon.Asset`](../reference/maxon.Asset.md#module-maxon.Asset) which supports the update of its updatable references to other assets to newer versions. Such an update doesn’t create a new repository version of the asset because the asset definition itself isn’t changed, only the references (represented by [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink)) point to newer assets.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetInterface`](maxon.AssetInterface.md#module-maxon.AssetInterface)

Child Class:

- [`maxon.UpdatableAsset`](../reference/maxon.UpdatableAsset.md#module-maxon.UpdatableAsset)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.UpdatableAssetInterface.VIRTUAL`](maxon.UpdatableAssetInterface.VIRTUAL.md#maxon.UpdatableAssetInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Update`](#maxon.UpdatableAssetInterface.Update)(updates, repository) | Updates the given references of this asset to point to the corresponding assets. |

## Methods Definition <a id="methods-definition"></a>

### `UpdatableAssetInterface.Update(updates, repository)` <a id="maxon.UpdatableAssetInterface.Update"></a>

Updates the given references of this asset to point to the corresponding assets.

The references have to use updatable [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink) objects (their update policy must not be *ASSET_UPDATE_POLICY.NEVER*). Afterwards the [`AssetBaseWithUpdateInterface.GetUpdate()`](maxon.AssetBaseWithUpdateInterface.md#maxon.AssetBaseWithUpdateInterface.GetUpdate) “update counter” is incremented.

**Parameters:**

- **updates** ([`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.AssetReference`](../reference/maxon.AssetReference.md#module-maxon.AssetReference), [`maxon.AssetBase`](../reference/maxon.AssetBase.md#module-maxon.AssetBase)]]) – The updates to apply as a block of the references and their new targets.
- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – The repository to which this asset belongs. [`AssetBaseInterface.GetRepository()`](maxon.AssetBaseInterface.md#maxon.AssetBaseInterface.GetRepository) will be **None** during the update because the asset is in mutable state.
