<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.AssetTypeInterface.html -->

# maxon.AssetTypeInterface <a id="maxon-assettypeinterface"></a>

## Description <a id="module-maxon.AssetTypeInterface"></a><a id="description"></a>

Class to store and find any [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data) type under any type of key.

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.DataDictionaryObjectInterface`](../../../interfaces/core/maxon.DataDictionaryObjectInterface.md#module-maxon.DataDictionaryObjectInterface)

Children Classes:

- [`maxon.AssetType`](../reference/maxon.AssetType.md#module-maxon.AssetType)
- [`maxon.BasePresetAssetTypeInterface`](maxon.BasePresetAssetTypeInterface.md#module-maxon.BasePresetAssetTypeInterface)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`ComputeMetaData`](#maxon.AssetTypeInterface.ComputeMetaData)(repository, asset, meta, metaId) | ComputeMetaData to specialize the loading of meta data. |
| [`CopyWithEncryption`](#maxon.AssetTypeInterface.CopyWithEncryption)(source, urlFrom, urlTo) | Copies the asset with encryption to the new url. |
| [`GetAssetDataType`](#maxon.AssetTypeInterface.GetAssetDataType)() | Returns the DataType of assets handled by this [`maxon.AssetType`](../reference/maxon.AssetType.md#module-maxon.AssetType). |
| [`GetDefaultIcon`](#maxon.AssetTypeInterface.GetDefaultIcon)(repository, asset, meta) | Returns the default icon of this asset type. |
| [`GetId`](#maxon.AssetTypeInterface.GetId)() | Returns the identifier of this asset type. |
| [`GetMetaString`](#maxon.AssetTypeInterface.GetMetaString)(asset, key, languageRef, fallback) | Returns the translated string from a asset. |
| [`GetRepositoryId`](#maxon.AssetTypeInterface.GetRepositoryId)(id, fromTo) | Returns the default id of the asset. |
| [`GetUrlSuffix`](#maxon.AssetTypeInterface.GetUrlSuffix)(asset) | Returns the [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) suffix (file name ending without the dot) to use for the given asset. |
| [`Load`](#maxon.AssetTypeInterface.Load)(repo, assetDescription, url[, updateLinks]) | Loads an asset from a Url. |
| [`LoadDescriptionDefinition`](#maxon.AssetTypeInterface.LoadDescriptionDefinition)(asset, mode, …) | Loads the data description of the given asset. |
| [`StoreDescriptionDefinition`](#maxon.AssetTypeInterface.StoreDescriptionDefinition)(asset, category, …) | **param asset:** Asset to store. |
| [`StoreMetaString`](#maxon.AssetTypeInterface.StoreMetaString)(asset, key, value, languageRef) | Stores the name of an asset for a language. |

## Methods Definition <a id="methods-definition"></a>

### `AssetTypeInterface.ComputeMetaData(repository, asset, meta, metaId)` <a id="maxon.AssetTypeInterface.ComputeMetaData"></a>

ComputeMetaData to specialize the loading of meta data.

**Parameters:**

- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository where the asset is stored.
- **asset** ([`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]) – Asset id and version.
- **meta** ([`maxon.AssetMetaData`](../reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)) – Meta data of the asset.
- **metaId** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – MetaId to load.

**Returns:** Data contains the data. Bool if the value should be cached.

**Return type:** [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data), [`maxon.Bool`](../../../datatypes/simple/maxon.Bool.md#module-maxon.Bool)]

### `AssetTypeInterface.CopyWithEncryption(source, urlFrom, urlTo)` <a id="maxon.AssetTypeInterface.CopyWithEncryption"></a>

Copies the asset with encryption to the new url.

**Parameters:**

- **source** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to copy.
- **urlFrom** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – source url.
- **urlTo** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – destination url.

### `AssetTypeInterface.GetAssetDataType()` <a id="maxon.AssetTypeInterface.GetAssetDataType"></a>

Returns the DataType of assets handled by this [`maxon.AssetType`](../reference/maxon.AssetType.md#module-maxon.AssetType). The data type has to be a reference type derived from [`maxon.Asset`](../reference/maxon.Asset.md#module-maxon.Asset).

**Returns:** The data type of assets of this [`maxon.AssetType`](../reference/maxon.AssetType.md#module-maxon.AssetType).

**Return type:** [`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)

### `AssetTypeInterface.GetDefaultIcon(repository, asset, meta)` <a id="maxon.AssetTypeInterface.GetDefaultIcon"></a>

Returns the default icon of this asset type.

**Parameters:**

- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to search for.
- **asset** ([`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]) – Asset id and version.
- **meta** ([`maxon.AssetMetaData`](../reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)) – meta data of the asset to store.

**Returns:**

**Return type:** [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)

### `AssetTypeInterface.GetId()` <a id="maxon.AssetTypeInterface.GetId"></a>

Returns the identifier of this asset type. This has to be the same as used for the [`maxon.AssetTypes`](../registry/maxon.AssetTypes.md#module-maxon.AssetTypes) registry.

**Returns:** Asset type identifier.

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)

### `AssetTypeInterface.GetMetaString(asset, key, languageRef, fallback)` <a id="maxon.AssetTypeInterface.GetMetaString"></a>

Returns the translated string from a asset.

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to load.
- **key** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – Attribute id to load. e.g. maxon.OBJECT.BASE.NAME
- **languageRef** ([`maxon.LanguageRef`](../../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)) – Optional language. By default the function uses the current language.
- **fallback** (*str*) – Fallback string if the asset has no name.

**Returns:** String on success.

**Return type:** str

### `AssetTypeInterface.GetRepositoryId(id, fromTo)` <a id="maxon.AssetTypeInterface.GetRepositoryId"></a>

Returns the default id of the asset.

**Parameters:**

- **id** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Id of the asset.
- **fromTo** (*bool*) – **True** to add the full id. **False** to cut the hash code and append it.

**Returns:** New id on success.

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)

### `AssetTypeInterface.GetUrlSuffix(asset)` <a id="maxon.AssetTypeInterface.GetUrlSuffix"></a>

Returns the [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) suffix (file name ending without the dot) to use for the given asset.

**Parameters:** **asset** ([`maxon.Asset`](../reference/maxon.Asset.md#module-maxon.Asset)) – An asset, has to match the expected data type of this [`maxon.AssetType`](../reference/maxon.AssetType.md#module-maxon.AssetType).

**Returns:** The Url suffix to use, may be empty.

**Return type:** [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)

### `AssetTypeInterface.Load(repo, assetDescription, url, updateLinks=None)` <a id="maxon.AssetTypeInterface.Load"></a>

Loads an asset from a Url.

**Parameters:**

- **repo** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – The repository to which the asset belongs.

- **assetDescription** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – The asset description.

- **url** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – The [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) from which the asset shall be loaded.

- **updateLinks** (*Optional*[*bool*]) –

  None if the asset shall be loaded as is.  
  A boolean if asset links which use ASSET_UPDATE_POLICY.IMPLICIT shall be resolved to the latest version.

**Returns:** The loaded asset and a boolean sets to **True** whenever there is a link where the resolved version differs from the original version.

**Return type:** Tuple[[`maxon.Asset`](../reference/maxon.Asset.md#module-maxon.Asset), bool]

### `AssetTypeInterface.LoadDescriptionDefinition(asset, mode, category, language)` <a id="maxon.AssetTypeInterface.LoadDescriptionDefinition"></a>

Loads the data description of the given asset.

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to load.
- **mode** (`maxon.LOADDESCRIPTIONMODE`) – see LOADDESCRIPTIONMODE.
- **category** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – DATADESCRIPTION_CATEGORY_xxx
- **language** ([`maxon.LanguageRef`](../../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)) – Language id in case of DATADESCRIPTION_CATEGORY_STRING.

**Returns:** ataDescriptionDefinition on success.

**Return type:**

`maxon.DataDescriptionDefinition`

### `AssetTypeInterface.StoreDescriptionDefinition(asset, category, language, overwrittenDescription, storeRepository)` <a id="maxon.AssetTypeInterface.StoreDescriptionDefinition"></a>

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to store.
- **category** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – DATADESCRIPTION_CATEGORY_xxx
- **language** ([`maxon.LanguageRef`](../../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)) – Language id in case of DATADESCRIPTION_CATEGORY_STRING.
- **overwrittenDescription** (`maxon.DataDescriptionDefinition`) – Additional description with overwritten parameters.
- **storeRepository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to store the asset.

**Returns:** AssetDescription with the new asset on success.

**Return type:** [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### `AssetTypeInterface.StoreMetaString(asset, key, value, languageRef)` <a id="maxon.AssetTypeInterface.StoreMetaString"></a>

Stores the name of an asset for a language.

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to modify.
- **key** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – Attribute id to save. e.g. maxon.OBJECT.BASE.NAME
- **value** (*str*) – New string.
- **languageRef** ([`maxon.LanguageRef`](../../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)) – Optional language. By default the function uses the current language.
