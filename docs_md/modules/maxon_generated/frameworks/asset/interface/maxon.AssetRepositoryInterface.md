<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.AssetRepositoryInterface.html -->

# maxon.AssetRepositoryInterface <a id="maxon-assetrepositoryinterface"></a>

## Description <a id="module-maxon.AssetRepositoryInterface"></a><a id="description"></a>

An AssetRepositoryInterface manages a set of assets: - Assets can be looked up using their identifier and version. - New assets or new asset versions can be stored. - Each asset can have associated meta data which can be read and written. - Observers for changes to the repository can be added.

An asset repository can have several base repositories which are used for the lookup after lookup in the repository itself has finished. Cycles aren’t allowed, so asset repositories form a directed acyclic graph.

A repository which has another repository as (direct or indirect) base is said to be *derived* from that repository. Whenever an observable of a repository is triggered, this is done for all derived repositories too.

The methods of [`maxon.AssetRepositoryInterface`](#module-maxon.AssetRepositoryInterface) are thread-safe. This allows for concurrent modifications and queries.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObserverObjectInterface`](../../../interfaces/core_helper/maxon.ObserverObjectInterface.md#module-maxon.ObserverObjectInterface)
- [`maxon.DataDictionaryObjectInterface`](../../../interfaces/core/maxon.DataDictionaryObjectInterface.md#module-maxon.DataDictionaryObjectInterface)

Children Classes:

- [`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)
- [`maxon.UpdatableAssetRepositoryInterface`](maxon.UpdatableAssetRepositoryInterface.md#module-maxon.UpdatableAssetRepositoryInterface)
- [`maxon.CompactableAssetRepositoryInterface`](maxon.CompactableAssetRepositoryInterface.md#module-maxon.CompactableAssetRepositoryInterface)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`AddBase`](#maxon.AssetRepositoryInterface.AddBase)(base) | Adds *base* to the list of base repositories of this repository. |
| [`CompareVersions`](#maxon.AssetRepositoryInterface.CompareVersions)(first, second) | Compares the versions of assets of this repository: |
| [`CopyAsset`](#maxon.AssetRepositoryInterface.CopyAsset)(aid, source[, addProtection, …]) | Copies an asset including meta data to this repository using the identifier *aid* for the copy. |
| [`DeleteAsset`](#maxon.AssetRepositoryInterface.DeleteAsset)(aid) | Deletes the asset given by the identifier *aid*. |
| [`EraseAsset`](#maxon.AssetRepositoryInterface.EraseAsset)(asset) | Permanently erases an asset version. |
| [`FindAssets`](#maxon.AssetRepositoryInterface.FindAssets)(assetType[, aid, version, …]) | Finds all assets matching the parameters: |
| [`FindLatestAsset`](#maxon.AssetRepositoryInterface.FindLatestAsset)(type, aid, version, findMode) | Finds the asset with the given identifier in this repository and its base repositories. |
| [`FindRepository`](#maxon.AssetRepositoryInterface.FindRepository)(repoId) | Finds the repository with the given identifier among this repository and its direct and indirect bases. |
| [`GetBases`](#maxon.AssetRepositoryInterface.GetBases)() | Returns an array holding all current base repositories of this repository. |
| [`GetDerived`](#maxon.AssetRepositoryInterface.GetDerived)([receiver]) | Yields all derived repositories of this repository to #receiver (those which have this repository as direct base). |
| [`GetDescription`](#maxon.AssetRepositoryInterface.GetDescription)(asset) | returns the AssetDescription of the given asset. |
| [`GetDescriptionDatabaseId`](#maxon.AssetRepositoryInterface.GetDescriptionDatabaseId)() | **return:** |
| [`GetId`](#maxon.AssetRepositoryInterface.GetId)() | Returns the identifier of this repository. |
| [`GetRepositoryName`](#maxon.AssetRepositoryInterface.GetRepositoryName)(language[, addDetails]) | Returns the name of the repository in the requested language. |
| [`HandleDownloadStateChanged`](#maxon.AssetRepositoryInterface.HandleDownloadStateChanged)(repository, finished) | Informs all observers of ObservableDownloadStateChanged and calls HandleDownloadStateChanged on all derived repositories. |
| [`InitBases`](#maxon.AssetRepositoryInterface.InitBases)(bases) | Initializes the base repositories of this repository. |
| [`IsBasedOnOrSame`](#maxon.AssetRepositoryInterface.IsBasedOnOrSame)(other) | Returns **True** if this repository is based on *other* or *other* itself, **False** otherwise. |
| [`IsWritable`](#maxon.AssetRepositoryInterface.IsWritable)() | Tells if this repository is writable or not. |
| [`LoadDescriptionAssetId`](#maxon.AssetRepositoryInterface.LoadDescriptionAssetId)(category, language, …) |  |
| [`LoadDescriptionDefinition`](#maxon.AssetRepositoryInterface.LoadDescriptionDefinition)(mode, category, …) | **param mode:** |
| [`OverwriteAsset`](#maxon.AssetRepositoryInterface.OverwriteAsset)(aid, asset[, metaData]) | Stores asset as a new version using the identifier *aid*. |
| [`RemoveBase`](#maxon.AssetRepositoryInterface.RemoveBase)(base) | Removes *base* from the list of base repositories of this repository. |
| [`SetRepositoryName`](#maxon.AssetRepositoryInterface.SetRepositoryName)(name, language) | Sets the name of the repository in the given language. |
| [`StoreAsset`](#maxon.AssetRepositoryInterface.StoreAsset)(aid, asset[, metaData]) | Stores asset as a new version using the identifier *aid*. |
| [`StoreMetaData`](#maxon.AssetRepositoryInterface.StoreMetaData)(asset, metaId, data, kind) | Stores *data* for the meta data attribute *metaId* of the given *asset*. |
| [`StoreUrlMetaData`](#maxon.AssetRepositoryInterface.StoreUrlMetaData)(asset, metaId, data, kind) | Stores *data* for the meta data attribute *metaId* of the given *asset*. |

## Methods Definition <a id="methods-definition"></a>

### `AssetRepositoryInterface.AddBase(base)` <a id="maxon.AssetRepositoryInterface.AddBase"></a>

Adds *base* to the list of base repositories of this repository. The observers for ObservableBaseChanged of this repository and its derived repositories are informed.

**Parameters:** **base** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – The base repository to add.

### `AssetRepositoryInterface.CompareVersions(first, second)` <a id="maxon.AssetRepositoryInterface.CompareVersions"></a>

Compares the versions of assets of this repository:

- If #first is newer, returns `maxon.COMPARERESULT.GREATER`.
- If #second is newer, returns `maxon.COMPARERESULT.LESS`.
- If both denote the same asset version, returns `maxon.COMPARERESULT.EQUAL`.

Being newer isn’t based on the time stamp, but on the order in which assets are stored. It also takes into account the update counter ([`AssetBaseWithUpdateInterface.GetUpdate()`](maxon.AssetBaseWithUpdateInterface.md#maxon.AssetBaseWithUpdateInterface.GetUpdate)) when both assets have the same version identifier.

If both assets have different asset identifiers the method returns `maxon.COMPARERESULT.INCOMPARABLE`. If the assets don’t belong to this repository, the result is unspecified.

**Parameters:**

- **first** ([`maxon.AssetBase`](../reference/maxon.AssetBase.md#module-maxon.AssetBase)) – The first asset.
- **second** ([`maxon.AssetBase`](../reference/maxon.AssetBase.md#module-maxon.AssetBase)) – The second asset.

**Returns:** The result of the comparison of the versions.

**Return type:**

`maxon.COMPARERESULT`

### `AssetRepositoryInterface.CopyAsset(aid, source, addProtection=False, overwrite=False, encryption=maxon.CryptoKey object at 0x12e9af29aa0 with the data: nullptr)` <a id="maxon.AssetRepositoryInterface.CopyAsset"></a>

Copies an asset including meta data to this repository using the identifier *aid* for the copy.

*source* has to be an asset already stored in some repository.  
The version identifier of *source* will be used for the copy even if this repository would normally derive a different identifier from the asset content.

> **Note:** Observers of ObservableAssetStored of this repository and its derived repositories are informed.

**Parameters:**

- **aid** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The asset identifier to use.
- **source** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – The source asset to copy.
- **addProtection** (*bool*) – **True** if the copy shall be stored in a protected way such that a user can’t see the asset contents (e.g., the node graph of a node asset). The protection has to be handled by the [`maxon.AssetType`](../reference/maxon.AssetType.md#module-maxon.AssetType).
- **overwrite** (*bool*) – **True** to overwrite the existing asset.
- **encryption** (`maxon.CryptoKey`) – An optional encryption key with which the asset will be encrypted. Make sure to store that key in the meta data afterwards, see [`AssetDescriptionInterface.StoreDecryptionKey()`](maxon.AssetDescriptionInterface.md#maxon.AssetDescriptionInterface.StoreDecryptionKey).

**Returns:** The [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription) of the copy.

**Return type:** [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### `AssetRepositoryInterface.DeleteAsset(aid)` <a id="maxon.AssetRepositoryInterface.DeleteAsset"></a>

Deletes the asset given by the identifier *aid*.

The previous versions still exist in the repository, this method just stores a delete marker so that [`AssetRepositoryInterface.FindAssets()`](#maxon.AssetRepositoryInterface.FindAssets) doesn’t take those versions into account unless the *ASSET_FIND_MODE.WITH_DELETED* flag is given.

For a complete removal of a specific version use `AssetRepositoryInterface.EraseAsset.()`.

> **Note:** Observers of ObservableAssetStored of this repository and its derived repositories are informed.

**Parameters:** **aid** (`maxon.aid`) – The asset to delete.

**Returns:** The [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription) which represents the delete marker.

**Return type:** [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### `AssetRepositoryInterface.EraseAsset(asset)` <a id="maxon.AssetRepositoryInterface.EraseAsset"></a>

Permanently erases an asset version.

Unlike [`AssetRepositoryInterface.DeleteAsset()`](#maxon.AssetRepositoryInterface.DeleteAsset) which marks an asset as deleted but keeps all previous versions this method completely removes any data of the given asset version.

> **Note:** Observers of ObservableAssetErased of this repository and its derived repositories are informed.

**Parameters:** **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – The asset version to erase from this repository.

### `AssetRepositoryInterface.FindAssets(assetType, aid=None, version=None, findMode=1, receiver=None)` <a id="maxon.AssetRepositoryInterface.FindAssets"></a>

Finds all assets matching the parameters:

- If *aid* is set, only assets with that identifier are found (or which have the aid as prefix when [`maxon.ASSET_FIND_MODE.PREFIX`](../../../enums/maxon.ASSET_FIND_MODE.PREFIX.md#maxon.ASSET_FIND_MODE.PREFIX) is set), otherwise all assets.
- If *version* is set, only assets with that version are found, otherwise
- if [`maxon.ASSET_FIND_MODE.LATEST`](../../../enums/maxon.ASSET_FIND_MODE.LATEST.md#maxon.ASSET_FIND_MODE.LATEST) is set in *findMode*, only the latest asset version is found
- if [`maxon.ASSET_FIND_MODE.ALL`](../../../enums/maxon.ASSET_FIND_MODE.ALL.md#maxon.ASSET_FIND_MODE.ALL) is set in *findMode*, all asset versions are found.
- If [`maxon.ASSET_FIND_MODE.WITHOUT_BASES`](../../../enums/maxon.ASSET_FIND_MODE.WITHOUT_BASES.md#maxon.ASSET_FIND_MODE.WITHOUT_BASES) is set in *findMode*, then base repositories aren’t taken into account. Otherwise, they are considered after this repository.
- If [`maxon.ASSET_FIND_MODE.WITH_DELETED`](../../../enums/maxon.ASSET_FIND_MODE.WITH_DELETED.md#maxon.ASSET_FIND_MODE.WITH_DELETED) is set in *findMode*, then also deleted assets are reported.

When version is given or [`maxon.ASSET_FIND_MODE.LATEST`](../../../enums/maxon.ASSET_FIND_MODE.LATEST.md#maxon.ASSET_FIND_MODE.LATEST) is used and a matching asset is found in a repository, assets in base repositories thereof aren’t reported even if they are newer. So then an asset in a repository hides assets with the same identifier in base repositories. Assets with another identifier are still reported.

**Parameters:**

- **assetType** (Union[Collection[[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)], [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.AssetType`](../reference/maxon.AssetType.md#module-maxon.AssetType), [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]]) – The allowed asset type.
- **aid** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The asset identifier to lookup, use an empty identifier to find all assets.
- **version** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The version identifier to find, use an empty identifier to find all versions.
- **findMode** ([`maxon.ASSET_FIND_MODE`](../../../enums/maxon.ASSET_FIND_MODE.md#module-maxon.ASSET_FIND_MODE)) – Flags for the lookup.
- **receiver** (Union[None, list, Callable[[[`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)], bool]]) – All found assets are reported to this receiver.

**Returns:** If *callback* is None or a list then a list of [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)], bool]

### `AssetRepositoryInterface.FindLatestAsset(type, aid, version, findMode)` <a id="maxon.AssetRepositoryInterface.FindLatestAsset"></a>

Finds the asset with the given identifier in this repository and its base repositories. If version is set, this finds the asset with that version, otherwise it finds the latest asset. When a matching asset is found in a repository, assets in base repositories thereof aren’t considered even if they are newer

**Parameters:**

- **type** (Union[[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.AssetType`](../reference/maxon.AssetType.md#module-maxon.AssetType), [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]) – The allowed asset type.
- **aid** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The asset identifier to lookup, use an empty identifier to find all assets.
- **version** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The version identifier to find, use an empty identifier to find all versions.
- **findMode** ([`maxon.ASSET_FIND_MODE`](../../../enums/maxon.ASSET_FIND_MODE.md#module-maxon.ASSET_FIND_MODE)) – Flags for the lookup.

**Returns:** The found asset, or a null reference.

**Return type:** [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### `AssetRepositoryInterface.FindRepository(repoId)` <a id="maxon.AssetRepositoryInterface.FindRepository"></a>

Finds the repository with the given identifier among this repository and its direct and indirect bases. If no such repository exists, a null reference is returned, use [`Data.IsNullValue()`](../../../datatypes/base_core/maxon.Data.md#maxon.Data.IsNullValue) to test it.

**Parameters:** **repoId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The identifier of the repository to find.

**Returns:** The found repository, or a null reference.

**Return type:** [`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)

### `AssetRepositoryInterface.GetBases()` <a id="maxon.AssetRepositoryInterface.GetBases"></a>

Returns an array holding all current base repositories of this repository.

> **Note:** A repository must not have the same identifier as one of its (direct or indirect) bases.

**Returns:** The identifier of this repository.

**Return type:**

`` maxon.BaseArray`[:class:`maxon.AssetRepositoryRef ``]

### `AssetRepositoryInterface.GetDerived(receiver=None)` <a id="maxon.AssetRepositoryInterface.GetDerived"></a>

Yields all derived repositories of this repository to #receiver (those which have this repository as direct base).

**Parameters:** **receiver** (Union[None, list, Callable[[[`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)], bool]]) – The receiver for derived repositories., return **False** to cancel further evaluation.

**Returns:** If *receiver* is None or a list then a list of [`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)], bool]

### `AssetRepositoryInterface.GetDescription(asset)` <a id="maxon.AssetRepositoryInterface.GetDescription"></a>

returns the AssetDescription of the given asset.

**Parameters:** **asset** ([`maxon.Asset`](../reference/maxon.Asset.md#module-maxon.Asset)) – Asset to query.

**Returns:** AssetDescription on success.

**Return type:** [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### `AssetRepositoryInterface.GetDescriptionDatabaseId()` <a id="maxon.AssetRepositoryInterface.GetDescriptionDatabaseId"></a>

**Returns:**

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)

### `AssetRepositoryInterface.GetId()` <a id="maxon.AssetRepositoryInterface.GetId"></a>

Returns the identifier of this repository. Repository identifiers needn’t be unique, but a repository must not have the same identifier as one of its (direct or indirect) bases.

**Returns:** The identifier of this repository.

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)

### `AssetRepositoryInterface.GetRepositoryName(language, addDetails=True)` <a id="maxon.AssetRepositoryInterface.GetRepositoryName"></a>

Returns the name of the repository in the requested language.

**Parameters:**

- **language** (*bool*) – Language to query.
- **addDetails** – True if detail should be added.

**Returns:** Name on success.

**Return type:** str

### `AssetRepositoryInterface.HandleDownloadStateChanged(repository, finished)` <a id="maxon.AssetRepositoryInterface.HandleDownloadStateChanged"></a>

Informs all observers of ObservableDownloadStateChanged and calls HandleDownloadStateChanged on all derived repositories.

**Parameters:**

- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – The repository.
- **finished** (*bool*) – **True** if finished.

### `AssetRepositoryInterface.InitBases(bases)` <a id="maxon.AssetRepositoryInterface.InitBases"></a>

Initializes the base repositories of this repository. This function may only be called once right after the [`maxon.AssetRepositoryInterface`](#module-maxon.AssetRepositoryInterface) instance has been created.

> **Note:** It doesn’t inform any observers.

**Parameters:** **bases** ([`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [[`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)]) – The bases of this repository.

### `AssetRepositoryInterface.IsBasedOnOrSame(other)` <a id="maxon.AssetRepositoryInterface.IsBasedOnOrSame"></a>

Returns **True** if this repository is based on *other* or *other* itself, **False** otherwise.

**Parameters:** **other** (Union[[`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef), str, [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String)]) – A repository or a repository identifier.

**Returns:** **True** if *other* is a direct or indirect base of this repository or this repository itself.

**Return type:** bool

### `AssetRepositoryInterface.IsWritable()` <a id="maxon.AssetRepositoryInterface.IsWritable"></a>

Tells if this repository is writable or not.

**Returns:** **True** if this repository is writable, **False** otherwise.

**Return type:** bool

### `AssetRepositoryInterface.LoadDescriptionAssetId(category, language, dataType)` <a id="maxon.AssetRepositoryInterface.LoadDescriptionAssetId"></a>

### `AssetRepositoryInterface.LoadDescriptionDefinition(mode, category, language, asset)` <a id="maxon.AssetRepositoryInterface.LoadDescriptionDefinition"></a>

**Parameters:**

- **mode** (`maxon.LOADDESCRIPTIONMODE`) –
- **category** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) –
- **language** ([`maxon.LanguageRef`](../../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)) –
- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) –

**Returns:**

**Return type:** DataDescriptionDefinition

### `AssetRepositoryInterface.OverwriteAsset(aid, asset, metaData=None)` <a id="maxon.AssetRepositoryInterface.OverwriteAsset"></a>

Stores asset as a new version using the identifier *aid*.

Identifier, version and repository are set correspondingly at #asset, so *asset* may point to a copy of the original object afterwards (Asset is a copy-on-write reference).

> **Note:** Observers of ObservableAssetStored of this repository and its derived repositories are informed.

**Parameters:**

- **aid** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The asset identifier to use.
- **asset** ([`maxon.Asset`](../reference/maxon.Asset.md#module-maxon.Asset)) – The asset object to store. This method sets identifier, version and repository of *asset*.
- **metaData** (Optional[[`maxon.AssetMetaData`](../reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)]) – Initial meta data to use for the asset.

**Returns:** The [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription) for the added asset.

**Return type:** [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### `AssetRepositoryInterface.RemoveBase(base)` <a id="maxon.AssetRepositoryInterface.RemoveBase"></a>

Removes *base* from the list of base repositories of this repository. The observers for ObservableBaseChanged of this repository and its derived repositories are informed. Nothing happens if this repository doesn’t have #base as one of its bases.

**Parameters:** **base** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – The base repository to remove.

### `AssetRepositoryInterface.SetRepositoryName(name, language)` <a id="maxon.AssetRepositoryInterface.SetRepositoryName"></a>

Sets the name of the repository in the given language.

**Parameters:**

- **name** (*str*) – Name to set.
- **language** ([`maxon.LanguageRef`](../../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)) – Language

### `AssetRepositoryInterface.StoreAsset(aid, asset, metaData=None)` <a id="maxon.AssetRepositoryInterface.StoreAsset"></a>

Stores asset as a new version using the identifier *aid*.

Identifier, version and repository are set correspondingly at #asset, so *asset* may point to a copy of the original object afterwards (Asset is a copy-on-write reference).

> **Note:** Observers of ObservableAssetStored of this repository and its derived repositories are informed.

**Parameters:**

- **aid** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The asset identifier to use.
- **asset** ([`maxon.Asset`](../reference/maxon.Asset.md#module-maxon.Asset)) – The asset object to store. This method sets identifier, version and repository of *asset*.
- **metaData** (Optional[[`maxon.AssetMetaData`](../reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)]) – Initial meta data to use for the asset.

**Returns:** The [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription) for the added asset.

**Return type:** [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### `AssetRepositoryInterface.StoreMetaData(asset, metaId, data, kind)` <a id="maxon.AssetRepositoryInterface.StoreMetaData"></a>

Stores *data* for the meta data attribute *metaId* of the given *asset*.

> **Note:** Observers of ObservableMetaDataStored of this repository and its derived repositories are informed.

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – The asset for which a meta data value shall be set.
- **metaId** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The identifier of the meta data attribute.
- **data** ([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The value to set.
- **kind** ([`maxon.AssetMetaDataInterface.KIND`](../../../enums/maxon.AssetMetaDataInterface.KIND.md#module-maxon.AssetMetaDataInterface.KIND)) – The kind of the meta data.

### `AssetRepositoryInterface.StoreUrlMetaData(asset, metaId, data, kind)` <a id="maxon.AssetRepositoryInterface.StoreUrlMetaData"></a>

Stores *data* for the meta data attribute *metaId* of the given *asset*.

> **Note:** Observers of ObservableMetaDataStored of this repository and its derived repositories are informed.

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – The asset for which a meta data value shall be set.
- **metaId** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The identifier of the meta data attribute.
- **data** ([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The value to set.
- **kind** ([`maxon.AssetMetaDataInterface.KIND`](../../../enums/maxon.AssetMetaDataInterface.KIND.md#module-maxon.AssetMetaDataInterface.KIND)) – The kind of the meta data.
