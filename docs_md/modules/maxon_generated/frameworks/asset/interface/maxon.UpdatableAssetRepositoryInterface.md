<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.UpdatableAssetRepositoryInterface.html -->

# maxon.UpdatableAssetRepositoryInterface <a id="maxon-updatableassetrepositoryinterface"></a>

## Description <a id="module-maxon.UpdatableAssetRepositoryInterface"></a><a id="description"></a>

Asset repository which allows to update assets.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetRepositoryInterface`](maxon.AssetRepositoryInterface.md#module-maxon.AssetRepositoryInterface)

Children Classes:

- [`maxon.UpdatableAssetRepositoryRef`](../reference/maxon.UpdatableAssetRepositoryRef.md#module-maxon.UpdatableAssetRepositoryRef)
- [`maxon.UrlAssetRepositoryInterface`](maxon.UrlAssetRepositoryInterface.md#module-maxon.UrlAssetRepositoryInterface)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetPendingUpdates`](#maxon.UpdatableAssetRepositoryInterface.GetPendingUpdates)(reset) | Returns an array with a list of unsaved changes. |
| [`Update`](#maxon.UpdatableAssetRepositoryInterface.Update)(updates) | Update applies the updates to the repository. |

## Methods Definition <a id="methods-definition"></a>

### `UpdatableAssetRepositoryInterface.GetPendingUpdates(reset)` <a id="maxon.UpdatableAssetRepositoryInterface.GetPendingUpdates"></a>

Returns an array with a list of unsaved changes.

**Parameters:** **reset** (*bool*) – True to reset the changes.

**Returns:** Array on success.

**Return type:** [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription), [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.AssetBase`](../reference/maxon.AssetBase.md#module-maxon.AssetBase)]]]

### `UpdatableAssetRepositoryInterface.Update(updates)` <a id="maxon.UpdatableAssetRepositoryInterface.Update"></a>

Update applies the updates to the repository.

**Parameters:** **updates** ([`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription), [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.AssetBase`](../reference/maxon.AssetBase.md#module-maxon.AssetBase)]]]) – Updates to process
