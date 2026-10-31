<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.AssetInterface.html -->

# maxon.AssetInterface <a id="maxon-assetinterface"></a>

## Description <a id="module-maxon.AssetInterface"></a><a id="description"></a>

An Asset represents digital content which can be managed by an [`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef) “asset repository”. The management includes versioning, meta data and automatic updates.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetBaseWithUpdateInterface`](maxon.AssetBaseWithUpdateInterface.md#module-maxon.AssetBaseWithUpdateInterface)

Children Classes:

- [`maxon.Asset`](../reference/maxon.Asset.md#module-maxon.Asset)
- [`maxon.UpdatableAssetInterface`](maxon.UpdatableAssetInterface.md#module-maxon.UpdatableAssetInterface)
- [`maxon.FileAssetInterface`](maxon.FileAssetInterface.md#module-maxon.FileAssetInterface)
- [`maxon.BasePresetAssetInterface`](maxon.BasePresetAssetInterface.md#module-maxon.BasePresetAssetInterface)
- [`maxon.CategoryAssetInterface`](maxon.CategoryAssetInterface.md#module-maxon.CategoryAssetInterface)
- [`maxon.KeywordAssetInterface`](maxon.KeywordAssetInterface.md#module-maxon.KeywordAssetInterface)
- [`maxon.ColorCategoryAssetInterface`](maxon.ColorCategoryAssetInterface.md#module-maxon.ColorCategoryAssetInterface)
- [`maxon.DatabaseAssetInterface`](maxon.DatabaseAssetInterface.md#module-maxon.DatabaseAssetInterface)
- [`maxon.NodeSpaceAssetInterface`](maxon.NodeSpaceAssetInterface.md#module-maxon.NodeSpaceAssetInterface)
- [`maxon.PluginAssetInterface`](maxon.PluginAssetInterface.md#module-maxon.PluginAssetInterface)
- [`maxon.SmartSearchAssetInterface`](maxon.SmartSearchAssetInterface.md#module-maxon.SmartSearchAssetInterface)
- [`maxon.SubTypeAssetInterface`](maxon.SubTypeAssetInterface.md#module-maxon.SubTypeAssetInterface)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.AssetInterface.VIRTUAL`](maxon.AssetInterface.VIRTUAL.md#maxon.AssetInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`AddRepositoryScope`](#maxon.AssetInterface.AddRepositoryScope)(url, repository) | Resolves the asset url and caching the assetdescription in the url. |
| [`CreateRepositoryFromUrl`](#maxon.AssetInterface.CreateRepositoryFromUrl)(rid, repoType, …) | Creates an asset repository for the given [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url). |
| [`GetApplicationRepository`](#maxon.AssetInterface.GetApplicationRepository)() | Returns the application repository. |
| [`GetAssetUrl`](#maxon.AssetInterface.GetAssetUrl)(*args) | Returns the url to access the asset data. |
| [`GetBuiltinRepository`](#maxon.AssetInterface.GetBuiltinRepository)() | Returns the built-in repository. |
| [`GetDescription`](#maxon.AssetInterface.GetDescription)() | Returns the AssetDescription of the given Asset. |
| [`GetLanguageMetaDataId`](#maxon.AssetInterface.GetLanguageMetaDataId)(languageId) | Returns the standardized InternedId for the given languageid. |
| [`GetMetaData`](#maxon.AssetInterface.GetMetaData)() | Returns the meta data of this asset. |
| [`GetPendingUpdates`](#maxon.AssetInterface.GetPendingUpdates)(updatedAssets[, receiver]) | Yields all possible AssetReference updates for this asset due to *updatedAssets* to *receiver*. |
| [`GetReferencedAssets`](#maxon.AssetInterface.GetReferencedAssets)(onlyUpdatable[, receiver]) | Yields all direct references which this asset makes to other assets. |
| [`GetType`](#maxon.AssetInterface.GetType)() | Returns the AssetType of this asset. |
| [`GetUserPrefsRepository`](#maxon.AssetInterface.GetUserPrefsRepository)() | Returns the asset repository in the user preferences folder. |
| [`GetVersionString`](#maxon.AssetInterface.GetVersionString)(asset) | Returns the version string for the given asset. |
| [`IsAssetValid`](#maxon.AssetInterface.IsAssetValid)(asset) | Checks if the asset is valid for the current license and program version. |
| [`IsAssetVisible`](#maxon.AssetInterface.IsAssetVisible)(asset) | Checks if the asset is visible for the current license and program version. |
| [`MakeUuid`](#maxon.AssetInterface.MakeUuid)(prefix, compact) | Creates a UUID (universally unique identifier). |
| [`ResolveAsset`](#maxon.AssetInterface.ResolveAsset)(url, repository) | Returns the asset description from a given url with the URLSCHEME_ASSET (Id: “asset”). |
| [`SetId`](#maxon.AssetInterface.SetId)(aid, update, repository[, url]) | Sets identifier, version and repository of this asset. |
| [`SetMetaData`](#maxon.AssetInterface.SetMetaData)(data) | Sets the meta data object to use for this asset. |

## Methods Definition <a id="methods-definition"></a>

### *static* `AssetInterface.AddRepositoryScope(url, repository)` <a id="maxon.AssetInterface.AddRepositoryScope"></a>

Resolves the asset url and caching the assetdescription in the url.

**Parameters:**

- **url** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – Url to investigate.
- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to search.

**Returns:** Modified url which contains the AssetDescription on success.

**Return type:** [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)

### *static* `AssetInterface.CreateRepositoryFromUrl(rid, repoType, bases, url, writable, derivedInPrefs, tempRepository)` <a id="maxon.AssetInterface.CreateRepositoryFromUrl"></a>

Creates an asset repository for the given [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url). If there already is a directory structure in the expected format it is read as far as needed to initialize the repository with the found assets, otherwise such a directory structure is created.

**Parameters:**

- **rid** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The repository identifier. There mustn’t be a base with the same identifier.
- **repoType** ([`maxon.Class`](../../../references/core_helper/maxon.Class.md#module-maxon.Class) [[`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)]) – See AssetRepositoryTypes registry.
- **bases** ([`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [[`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)]) – The base repositories for the new repository.
- **url** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – The root directory to use for the repository.
- **writable** (*bool*) – **True** if the repository shall be writable.
- **derivedInPrefs** (*bool*) – **True** if derived meta data shall be stored in the user preferences folder. This is mandatory if *url* is a read-only [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url).
- **tempRepository** (*bool*) – **True** if the repository should not be registered as a description database.

**Returns:** Reference to the repository in the user preferences folder.

**Return type:** [`maxon.UpdatableAssetRepositoryRef`](../reference/maxon.UpdatableAssetRepositoryRef.md#module-maxon.UpdatableAssetRepositoryRef)

### *static* `AssetInterface.GetApplicationRepository()` <a id="maxon.AssetInterface.GetApplicationRepository"></a>

Returns the application repository. The application repository uses the [`AssetInterface.GetBuiltinRepository()`](#maxon.AssetInterface.GetBuiltinRepository) “built-in repository” as base and adds the assets found in the resources of the asset.module.

**Returns:** Reference to the built-in repository.

**Return type:** [`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)

### *static* `AssetInterface.GetAssetUrl(*args)` <a id="maxon.AssetInterface.GetAssetUrl"></a>

Returns the url to access the asset data. e.g. asset:///file_634545662344

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – asset to convert.
- **isLatest** (*bool*) – **True** if the asset is the latest asset. In that case the version will not be added to the url.

**Returns:** The url to access the asset data.

**Return type:** [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)

### *static* `AssetInterface.GetBuiltinRepository()` <a id="maxon.AssetInterface.GetBuiltinRepository"></a>

Returns the built-in repository. This contains the built-in assets which are defined by program code (i.e., not by a data format to read them from a data stream).

**Returns:** Reference to the built-in repository.

**Return type:** [`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)

### `AssetInterface.GetDescription()` <a id="maxon.AssetInterface.GetDescription"></a>

Returns the AssetDescription of the given Asset.

**Returns:** AssetDescription on success.

**Return type:** [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### *static* `AssetInterface.GetLanguageMetaDataId(languageId)` <a id="maxon.AssetInterface.GetLanguageMetaDataId"></a>

Returns the standardized InternedId for the given languageid.

**Parameters:** **languageId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Language id.

**Returns:** InternedId on success.

**Return type:** [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)

### `AssetInterface.GetMetaData()` <a id="maxon.AssetInterface.GetMetaData"></a>

Returns the meta data of this asset.

**Returns:** The meta data of this asset.

**Return type:** [`maxon.AssetMetaData`](../reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)

### `AssetInterface.GetPendingUpdates(updatedAssets, receiver=None)` <a id="maxon.AssetInterface.GetPendingUpdates"></a>

Yields all possible AssetReference updates for this asset due to *updatedAssets* to *receiver*.

This method finds all direct references which this asset makes to other assets, and checks if they are affected by the list of *updatedAssets*. This check takes into account the update policy of the [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink) used for the reference. Whenever there is an updatable [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink) and *updatedAssets* contains a newer version for that link, this is reported by a call to *receiver* with the reference as first argument and the newer asset from *updatedAssets* as second argument.

**Parameters:**

- **updatedAssets** ([`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.AssetMetaData`](../reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)]) – An array of assets with (potentially) newer versions.
- **receiver** (Optional[list, Callable[[[`maxon.AssetReference`](../reference/maxon.AssetReference.md#module-maxon.AssetReference), [`maxon.AssetBase`](../reference/maxon.AssetBase.md#module-maxon.AssetBase)], bool]]) – Receiver to which all pending updates due to #updatedAssets are reported.

**Returns:** If *callback* is None or a list of [`maxon.AssetReference`](../reference/maxon.AssetReference.md#module-maxon.AssetReference) and [`maxon.AssetBase`](../reference/maxon.AssetBase.md#module-maxon.AssetBase) is returned. Otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.AssetReference`](../reference/maxon.AssetReference.md#module-maxon.AssetReference), [`maxon.AssetBase`](../reference/maxon.AssetBase.md#module-maxon.AssetBase)], bool]

### `AssetInterface.GetReferencedAssets(onlyUpdatable, receiver=None)` <a id="maxon.AssetInterface.GetReferencedAssets"></a>

Yields all direct references which this asset makes to other assets. The [`maxon.AssetReference`](../reference/maxon.AssetReference.md#module-maxon.AssetReference) objects are used later for the update mechanism: The method [`UpdatableAssetInterface.Update()`](maxon.UpdatableAssetInterface.md#maxon.UpdatableAssetInterface.Update) gets a block of tuples ([`maxon.AssetReference`](../reference/maxon.AssetReference.md#module-maxon.AssetReference), [`maxon.AssetBase`](../reference/maxon.AssetBase.md#module-maxon.AssetBase)) as input, and each tuple indicates to which asset an [`maxon.AssetReference`](../reference/maxon.AssetReference.md#module-maxon.AssetReference) shall be updated. So for example if an asset has two links to the same asset this has to be reported as two [`maxon.AssetReference`](../reference/maxon.AssetReference.md#module-maxon.AssetReference) objects, and when only the first one is passed to [`UpdatableAssetInterface.Update()`](maxon.UpdatableAssetInterface.md#maxon.UpdatableAssetInterface.Update) only the first link has to be updated, while the second has to remain unchanged.

**Parameters:**

- **onlyUpdatable** (*bool*) – **True** only references which use updatable links shall be reported (update policy different from *ASSET_UPDATE_POLICY.NEVER*), otherwise all references.
- **receiver** (Optional[list, Callable[[[`maxon.AssetReference`](../reference/maxon.AssetReference.md#module-maxon.AssetReference)], bool]) – Receiver to which references are reported.

**Returns:** If *callback* is None or a list of [`maxon.AssetReference`](../reference/maxon.AssetReference.md#module-maxon.AssetReference) is returned. Otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.AssetReference`](../reference/maxon.AssetReference.md#module-maxon.AssetReference)], bool]

### `AssetInterface.GetType()` <a id="maxon.AssetInterface.GetType"></a>

Returns the AssetType of this asset.

**Returns:** The asset’s type.

**Return type:** [`maxon.AssetType`](../reference/maxon.AssetType.md#module-maxon.AssetType)

### *static* `AssetInterface.GetUserPrefsRepository()` <a id="maxon.AssetInterface.GetUserPrefsRepository"></a>

Returns the asset repository in the user preferences folder. This repository is writable for the user.

**Returns:** Reference to the repository in the user preferences folder.

**Return type:** [`maxon.UpdatableAssetRepositoryRef`](../reference/maxon.UpdatableAssetRepositoryRef.md#module-maxon.UpdatableAssetRepositoryRef)

### *static* `AssetInterface.GetVersionString(asset)` <a id="maxon.AssetInterface.GetVersionString"></a>

Returns the version string for the given asset.

**Parameters:** **asset** (Union[[`maxon.Asset`](../reference/maxon.Asset.md#module-maxon.Asset)], [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)]) – Asset to look at.

**Returns:** Version string on success.

**Return type:** str

### *static* `AssetInterface.IsAssetValid(asset)` <a id="maxon.AssetInterface.IsAssetValid"></a>

Checks if the asset is valid for the current license and program version.

**Parameters:** **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to check

**Returns:** **True** on success

**Return type:** bool

### *static* `AssetInterface.IsAssetVisible(asset)` <a id="maxon.AssetInterface.IsAssetVisible"></a>

Checks if the asset is visible for the current license and program version.

**Parameters:** **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to check

**Returns:** **True** on success

**Return type:** bool

### *static* `AssetInterface.MakeUuid(prefix, compact)` <a id="maxon.AssetInterface.MakeUuid"></a>

Creates a UUID (universally unique identifier). If prefix is given, the returned identifier starts with prefix, followed by an @ sign, followed by the UUID such as *{base@5e75b5e319f64055ac5387490d7355c0}*, otherwise it is a UUID only. If prefix already contains an @ sign, only the part before that sign is used. If compact is **True**, a Base64-encoding with $ and _ as last characters is used for the UUID instead of the default Hex encoding, this results in shorter UUIDs like *{FR4pAc$UFR_jXb16rXadEB}*.

**Parameters:**

- **prefix** (*str*) – The prefix for the identifier, may be nullptr. Only the characters up to the first @ sign are used.
- **compact** (*bool*) – **True** if the shorter Base64-encoding shall be used, false for Hex encoding.

**Returns:** A new UUID. It is safe to assume that this UUID differs from any other UUID returned by this method.

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)

### *static* `AssetInterface.ResolveAsset(url, repository)` <a id="maxon.AssetInterface.ResolveAsset"></a>

Returns the asset description from a given url with the URLSCHEME_ASSET (Id: “asset”).

**Parameters:**

- **url** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – Url to search.
- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Lookup repository.

**Returns:** AssetDescription on success.

**Return type:** [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### `AssetInterface.SetId(aid, update, repository, url=None)` <a id="maxon.AssetInterface.SetId"></a>

Sets identifier, version and repository of this asset.

This method should only be called by the owning asset repository when it stores an asset to establish the link between asset and repository.

**Parameters:**

- **aid** ([`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]) – Identifier and version identifier of the asset.
- **update** (*int*) – Update counter, see [`AssetBaseWithUpdateInterface.GetUpdate()`](maxon.AssetBaseWithUpdateInterface.md#maxon.AssetBaseWithUpdateInterface.GetUpdate).
- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – The repository which stored the asset.
- **url** (Optional[[`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)]) – An optional Url where the repository stored the asset.

### `AssetInterface.SetMetaData(data)` <a id="maxon.AssetInterface.SetMetaData"></a>

Sets the meta data object to use for this asset. This method should only be called by the owning asset repository.

**Parameters:** **data** ([`maxon.AssetMetaData`](../reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)) – The meta data of the asset.
