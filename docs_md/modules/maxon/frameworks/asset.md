<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon/frameworks/asset.html -->

# maxon.frameworks.asset <a id="maxon-frameworks-asset"></a><a id="framework-asset"></a>

> **Note:** Members documented here are defined in `maxon.frameworks.asset` module and are also exposed to the global `maxon` module. See the [Maxon API](../../../manuals/manual_api_overview.md#maxon-api-introduction) section of the API Overview for more information about the special conventions of this API.

## Description <a id="description"></a>

Module for interacting with assets.

## Interfaces <a id="interfaces"></a>

|   |   |
|---|---|
| [`AssetBaseInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetBaseInterface.md#module-maxon.AssetBaseInterface)(*args) | The base interface of [`maxon.AssetBaseWithUpdateInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetBaseWithUpdateInterface.md#module-maxon.AssetBaseWithUpdateInterface) and [`maxon.AssetDescriptionInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetDescriptionInterface.md#module-maxon.AssetDescriptionInterface). |
| [`AssetBaseWithUpdateInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetBaseWithUpdateInterface.md#module-maxon.AssetBaseWithUpdateInterface)(*args) | The base interface of [`maxon.AssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetInterface.md#module-maxon.AssetInterface) and [`maxon.AssetReferenceInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetReferenceInterface.md#module-maxon.AssetReferenceInterface). |
| [`AssetDataBasesInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetDataBasesInterface.md#module-maxon.AssetDataBasesInterface)(*args) | This interface provides helper functions to register asset repositories. |
| [`AssetDescriptionInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetDescriptionInterface.md#module-maxon.AssetDescriptionInterface)(*args) | Represents all meta information about an asset, namely its identifier and version, the [`maxon.AssetMetaData`](../../maxon_generated/frameworks/asset/reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData) and some further information. |
| [`AssetIdentifierInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetIdentifierInterface.md#module-maxon.AssetIdentifierInterface)(*args) | The base interface of [`maxon.AssetBaseInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetBaseInterface.md#module-maxon.AssetBaseInterface) and [`maxon.AssetLinkInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetLinkInterface.md#module-maxon.AssetLinkInterface). |
| [`AssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetInterface.md#module-maxon.AssetInterface)(*args) | An Asset represents digital content which can be managed by an [`maxon.AssetRepositoryRef`](../../maxon_generated/frameworks/asset/reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef) “asset repository”. |
| [`AssetLinkInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetLinkInterface.md#module-maxon.AssetLinkInterface)(*args) | An AssetLink is a symbolic link to an asset identified by its id and version. |
| [`AssetMetaDataInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetMetaDataInterface.md#module-maxon.AssetMetaDataInterface)(*args) | [`maxon.AssetMetaData`](../../maxon_generated/frameworks/asset/reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData) allows to query the meta data of an asset. |
| [`AssetReferenceInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetReferenceInterface.md#module-maxon.AssetReferenceInterface)(*args) | [`maxon.AssetReference`](../../maxon_generated/frameworks/asset/reference/maxon.AssetReference.md#module-maxon.AssetReference) is needed for the asset update mechanism and represents a specific updatable [`maxon.AssetLink`](../../maxon_generated/frameworks/asset/reference/maxon.AssetLink.md#module-maxon.AssetLink) within an asset, see [`AssetInterface.GetReferencedAssets()`](../../maxon_generated/frameworks/asset/interface/maxon.AssetInterface.md#maxon.AssetInterface.GetReferencedAssets). |
| [`AssetRepositoryInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetRepositoryInterface.md#module-maxon.AssetRepositoryInterface)(*args) | An AssetRepositoryInterface manages a set of assets: - Assets can be looked up using their identifier and version. |
| [`AssetTypeInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetTypeInterface.md#module-maxon.AssetTypeInterface)(*args) | Creates and stores internally the reference of the C++ Data. |
| [`AssetUtilitiesInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetUtilitiesInterface.md#module-maxon.AssetUtilitiesInterface)() | Helper Interface for Asset functions. |
| [`BasePresetAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.BasePresetAssetInterface.md#module-maxon.BasePresetAssetInterface)(*args) | [`maxon.BasePresetAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.BasePresetAssetInterface.md#module-maxon.BasePresetAssetInterface) allows to implement details for preset assets. |
| [`BasePresetAssetTypeInterface`](../../maxon_generated/frameworks/asset/interface/maxon.BasePresetAssetTypeInterface.md#module-maxon.BasePresetAssetTypeInterface)(*args) | Defines a new preset type and is the connector to BasePresetAssetInterface |
| [`CategoryAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.CategoryAssetInterface.md#module-maxon.CategoryAssetInterface)(*args) | Implementation of category assets |
| [`ColorCategoryAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.ColorCategoryAssetInterface.md#module-maxon.ColorCategoryAssetInterface)(*args) | Implementation of a color category asset. |
| [`CompactableAssetRepositoryInterface`](../../maxon_generated/frameworks/asset/interface/maxon.CompactableAssetRepositoryInterface.md#module-maxon.CompactableAssetRepositoryInterface)(*args) | Repository which allows to write an index. |
| [`DatabaseAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.DatabaseAssetInterface.md#module-maxon.DatabaseAssetInterface)(*args) | Implementation of DatabaseAsset. |
| [`DataDescriptionPresetStorageInterface`](../../maxon_generated/frameworks/asset/interface/maxon.DataDescriptionPresetStorageInterface.md#module-maxon.DataDescriptionPresetStorageInterface)() | Helper class to handle loading and saving of presets. |
| [`DerivedAssetRepositoryDataInterface`](../../maxon_generated/frameworks/asset/interface/maxon.DerivedAssetRepositoryDataInterface.md#module-maxon.DerivedAssetRepositoryDataInterface)(*args) | Creates and stores internally the reference of the C++ Data. |
| [`FileAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.FileAssetInterface.md#module-maxon.FileAssetInterface)(*args) | Creates and stores internally the reference of the C++ Data. |
| [`KeywordAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.KeywordAssetInterface.md#module-maxon.KeywordAssetInterface)(*args) | Creates and stores internally the reference of the C++ Data. |
| [`LazyLanguageDictionaryInterface`](../../maxon_generated/frameworks/asset/interface/maxon.LazyLanguageDictionaryInterface.md#module-maxon.LazyLanguageDictionaryInterface)(*args) | Interface to manage lazy loading of `maxon.LanguageDictionary` for description strings. |
| [`LazyLanguageStringDataDescriptionDefinitionInterface`](../../maxon_generated/frameworks/asset/interface/maxon.LazyLanguageStringDataDescriptionDefinitionInterface.md#module-maxon.LazyLanguageStringDataDescriptionDefinitionInterface)(*args) | Interface to manage lazy loading of `maxon.LanguageStringDataDescriptionDefinition` for description strings. |
| [`NodeSpaceAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.NodeSpaceAssetInterface.md#module-maxon.NodeSpaceAssetInterface)(*args) | Implementation of NodeSpaceAssets |
| [`PluginAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.PluginAssetInterface.md#module-maxon.PluginAssetInterface)(*args) | Implements the PluginAsset type |
| [`SmartSearchAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.SmartSearchAssetInterface.md#module-maxon.SmartSearchAssetInterface)(*args) | Implements the smartsearch asset type. |
| [`SubTypeAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.SubTypeAssetInterface.md#module-maxon.SubTypeAssetInterface)(*args) | Implements the SubTypeAsset. |
| [`UpdatableAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.UpdatableAssetInterface.md#module-maxon.UpdatableAssetInterface)(*args) | An [`maxon.UpdatableAsset`](../../maxon_generated/frameworks/asset/reference/maxon.UpdatableAsset.md#module-maxon.UpdatableAsset) is an [`maxon.Asset`](../../maxon_generated/frameworks/asset/reference/maxon.Asset.md#module-maxon.Asset) which supports the update of its updatable references to other assets to newer versions. |
| [`UpdatableAssetRepositoryInterface`](../../maxon_generated/frameworks/asset/interface/maxon.UpdatableAssetRepositoryInterface.md#module-maxon.UpdatableAssetRepositoryInterface)(*args) | Asset repository which allows to update assets. |
| [`UrlAssetRepositoryInterface`](../../maxon_generated/frameworks/asset/interface/maxon.UrlAssetRepositoryInterface.md#module-maxon.UrlAssetRepositoryInterface)(*args) | Creates and stores internally the reference of the C++ Data. |

## References <a id="references"></a>

|   |   |
|---|---|
| [`Asset`](../../maxon_generated/frameworks/asset/reference/maxon.Asset.md#module-maxon.Asset)(*args) | Represents a reference of a [`maxon.AssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetInterface.md#module-maxon.AssetInterface) |
| [`AssetBase`](../../maxon_generated/frameworks/asset/reference/maxon.AssetBase.md#module-maxon.AssetBase)(*args) | Represents a reference of a [`maxon.AssetBaseInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetBaseInterface.md#module-maxon.AssetBaseInterface) |
| [`AssetBaseWithUpdate`](../../maxon_generated/frameworks/asset/reference/maxon.AssetBaseWithUpdate.md#module-maxon.AssetBaseWithUpdate)(*args) | Represents a reference of a [`maxon.AssetBaseWithUpdateInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetBaseWithUpdateInterface.md#module-maxon.AssetBaseWithUpdateInterface) |
| [`AssetDescription`](../../maxon_generated/frameworks/asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)(*args) | Represents a reference of a [`maxon.AssetDescriptionInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetDescriptionInterface.md#module-maxon.AssetDescriptionInterface) |
| [`AssetIdentifier`](../../maxon_generated/frameworks/asset/reference/maxon.AssetIdentifier.md#module-maxon.AssetIdentifier)(*args) | Represents a reference of a [`maxon.AssetIdentifierInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetIdentifierInterface.md#module-maxon.AssetIdentifierInterface) |
| [`AssetLink`](../../maxon_generated/frameworks/asset/reference/maxon.AssetLink.md#module-maxon.AssetLink)(*args) | Represents a reference of a [`maxon.AssetLinkInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetLinkInterface.md#module-maxon.AssetLinkInterface) |
| [`AssetMetaData`](../../maxon_generated/frameworks/asset/reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)(*args) | Represents a reference of a [`maxon.AssetMetaDataInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetMetaDataInterface.md#module-maxon.AssetMetaDataInterface) |
| [`AssetReference`](../../maxon_generated/frameworks/asset/reference/maxon.AssetReference.md#module-maxon.AssetReference)(*args) | Represents a reference of a [`maxon.AssetReferenceInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetReferenceInterface.md#module-maxon.AssetReferenceInterface) |
| [`AssetRepositoryRef`](../../maxon_generated/frameworks/asset/reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)(*args) | Represents a reference of a [`maxon.AssetRepositoryInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetRepositoryInterface.md#module-maxon.AssetRepositoryInterface) |
| [`AssetType`](../../maxon_generated/frameworks/asset/reference/maxon.AssetType.md#module-maxon.AssetType)(*args) | Represents a reference of a [`maxon.AssetTypeInterface`](../../maxon_generated/frameworks/asset/interface/maxon.AssetTypeInterface.md#module-maxon.AssetTypeInterface) |
| [`BasePresetAsset`](../../maxon_generated/frameworks/asset/reference/maxon.BasePresetAsset.md#module-maxon.BasePresetAsset)(*args) | Represents a reference of a [`maxon.BasePresetAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.BasePresetAssetInterface.md#module-maxon.BasePresetAssetInterface) |
| [`BasePresetAssetType`](../../maxon_generated/frameworks/asset/reference/maxon.BasePresetAssetType.md#module-maxon.BasePresetAssetType)(*args) | Represents a reference of a [`maxon.BasePresetAssetTypeInterface`](../../maxon_generated/frameworks/asset/interface/maxon.BasePresetAssetTypeInterface.md#module-maxon.BasePresetAssetTypeInterface) |
| [`CategoryAsset`](../../maxon_generated/frameworks/asset/reference/maxon.CategoryAsset.md#module-maxon.CategoryAsset)(*args) | Represents a reference of a [`maxon.CategoryAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.CategoryAssetInterface.md#module-maxon.CategoryAssetInterface) |
| [`ColorCategoryAsset`](../../maxon_generated/frameworks/asset/reference/maxon.ColorCategoryAsset.md#module-maxon.ColorCategoryAsset)(*args) | Represents a reference of a [`maxon.ColorCategoryAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.ColorCategoryAssetInterface.md#module-maxon.ColorCategoryAssetInterface) |
| [`CompactableAssetRepositoryRef`](../../maxon_generated/frameworks/asset/reference/maxon.CompactableAssetRepositoryRef.md#module-maxon.CompactableAssetRepositoryRef)(*args) | Represents a reference of a [`maxon.CompactableAssetRepositoryInterface`](../../maxon_generated/frameworks/asset/interface/maxon.CompactableAssetRepositoryInterface.md#module-maxon.CompactableAssetRepositoryInterface) |
| [`DatabaseAsset`](../../maxon_generated/frameworks/asset/reference/maxon.DatabaseAsset.md#module-maxon.DatabaseAsset)(*args) | Represents a reference of a [`maxon.DatabaseAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.DatabaseAssetInterface.md#module-maxon.DatabaseAssetInterface) |
| [`DerivedAssetRepositoryDataRef`](../../maxon_generated/frameworks/asset/reference/maxon.DerivedAssetRepositoryDataRef.md#module-maxon.DerivedAssetRepositoryDataRef)(*args) | Represents a reference of a [`maxon.DerivedAssetRepositoryDataInterface`](../../maxon_generated/frameworks/asset/interface/maxon.DerivedAssetRepositoryDataInterface.md#module-maxon.DerivedAssetRepositoryDataInterface) |
| [`FileAsset`](../../maxon_generated/frameworks/asset/reference/maxon.FileAsset.md#module-maxon.FileAsset)(*args) | Represents a reference of a [`maxon.FileAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.FileAssetInterface.md#module-maxon.FileAssetInterface) |
| [`KeywordAsset`](../../maxon_generated/frameworks/asset/reference/maxon.KeywordAsset.md#module-maxon.KeywordAsset)(*args) | Represents a reference of a [`maxon.KeywordAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.KeywordAssetInterface.md#module-maxon.KeywordAssetInterface) |
| [`LazyLanguageDictionary`](../../maxon_generated/frameworks/asset/reference/maxon.LazyLanguageDictionary.md#module-maxon.LazyLanguageDictionary)(*args) | Represents a reference of a [`maxon.LazyLanguageDictionaryInterface`](../../maxon_generated/frameworks/asset/interface/maxon.LazyLanguageDictionaryInterface.md#module-maxon.LazyLanguageDictionaryInterface) |
| [`LazyLanguageStringDataDescriptionDefinition`](../../maxon_generated/frameworks/asset/reference/maxon.LazyLanguageStringDataDescriptionDefinition.md#module-maxon.LazyLanguageStringDataDescriptionDefinition)(*args) | Represents a reference of a [`maxon.LazyLanguageStringDataDescriptionDefinitionInterface`](../../maxon_generated/frameworks/asset/interface/maxon.LazyLanguageStringDataDescriptionDefinitionInterface.md#module-maxon.LazyLanguageStringDataDescriptionDefinitionInterface) |
| [`NodeSpaceAsset`](../../maxon_generated/frameworks/asset/reference/maxon.NodeSpaceAsset.md#module-maxon.NodeSpaceAsset)(*args) | Represents a reference of a [`maxon.NodeSpaceAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.NodeSpaceAssetInterface.md#module-maxon.NodeSpaceAssetInterface) |
| [`PluginAsset`](../../maxon_generated/frameworks/asset/reference/maxon.PluginAsset.md#module-maxon.PluginAsset)(*args) | Represents a reference of a [`maxon.PluginAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.PluginAssetInterface.md#module-maxon.PluginAssetInterface) |
| [`SmartSearchAsset`](../../maxon_generated/frameworks/asset/reference/maxon.SmartSearchAsset.md#module-maxon.SmartSearchAsset)(*args) | Represents a reference of a [`maxon.SmartSearchAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.SmartSearchAssetInterface.md#module-maxon.SmartSearchAssetInterface) |
| [`SubTypeAsset`](../../maxon_generated/frameworks/asset/reference/maxon.SubTypeAsset.md#module-maxon.SubTypeAsset)(*args) | Represents a reference of a [`maxon.SubTypeAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.SubTypeAssetInterface.md#module-maxon.SubTypeAssetInterface) |
| [`UpdatableAsset`](../../maxon_generated/frameworks/asset/reference/maxon.UpdatableAsset.md#module-maxon.UpdatableAsset)(*args) | Represents a reference of a [`maxon.UpdatableAssetInterface`](../../maxon_generated/frameworks/asset/interface/maxon.UpdatableAssetInterface.md#module-maxon.UpdatableAssetInterface) |
| [`UpdatableAssetRepositoryRef`](../../maxon_generated/frameworks/asset/reference/maxon.UpdatableAssetRepositoryRef.md#module-maxon.UpdatableAssetRepositoryRef)(*args) | Represents a reference of a [`maxon.UpdatableAssetRepositoryInterface`](../../maxon_generated/frameworks/asset/interface/maxon.UpdatableAssetRepositoryInterface.md#module-maxon.UpdatableAssetRepositoryInterface) |
| [`UrlAssetRepositoryRef`](../../maxon_generated/frameworks/asset/reference/maxon.UrlAssetRepositoryRef.md#module-maxon.UrlAssetRepositoryRef)(*args) | Represents a reference of a [`maxon.UrlAssetRepositoryInterface`](../../maxon_generated/frameworks/asset/interface/maxon.UrlAssetRepositoryInterface.md#module-maxon.UrlAssetRepositoryInterface) |

## Data Types <a id="data-types"></a>

|   |   |
|---|---|
| [`AddAssetDepencendyStruct`](../../maxon_generated/frameworks/asset/datatype/maxon.AddAssetDepencendyStruct.md#module-maxon.AddAssetDepencendyStruct)(parentCategory[, …]) | Initializes the appropriate C++ Data object and store it within the _data member. |
| [`AssetDatabaseStruct`](../../maxon_generated/frameworks/asset/datatype/maxon.AssetDatabaseStruct.md#module-maxon.AssetDatabaseStruct)(otherOrDbUrl[, active, …]) | Initializes the appropriate C++ Data object and store it within the _data member. |
| [`AssetDependencyStruct`](../../maxon_generated/frameworks/asset/datatype/maxon.AssetDependencyStruct.md#module-maxon.AssetDependencyStruct)([other]) | Helper class to pass several arguments into asset creation functions. |
| [`DragAndDropDataAssetArray`](../../maxon_generated/frameworks/asset/datatype/maxon.DragAndDropDataAssetArray.md#module-maxon.DragAndDropDataAssetArray)([other]) | Message data for *DRAGTYPE_ASSET* |
| [`ResolveAssetDependenciesStruct`](../../maxon_generated/frameworks/asset/datatype/maxon.ResolveAssetDependenciesStruct.md#module-maxon.ResolveAssetDependenciesStruct)([C]) | Initializes the appropriate C++ Data object and store it within the _data member. |
| [`StoreAssetStruct`](../../maxon_generated/frameworks/asset/datatype/maxon.StoreAssetStruct.md#module-maxon.StoreAssetStruct)(parentCategory[, …]) | Initializes the appropriate C++ Data object and store it within the _data member. |

## Functions <a id="functions"></a>

|   |   |
|---|---|
| [`GetAssetUrl`](../../maxon_generated/frameworks/asset/functions/maxon.GetAssetUrl.md#maxon.GetAssetUrl)(asset) | Returns the url of a DndAsset. |
| [`UpdateAssetUsage`](../../maxon_generated/frameworks/asset/functions/maxon.UpdateAssetUsage.md#maxon.UpdateAssetUsage)(asset[, incCount, updateDate]) | Mark the asset as used and increment the usage counter. |
| [`IdToIdAndVersion`](../../maxon_generated/frameworks/asset/functions/maxon.IdToIdAndVersion.md#maxon.IdToIdAndVersion)(id) | Convert a compacted id back to an id and version. |
| [`IdAndVersionToId`](../../maxon_generated/frameworks/asset/functions/maxon.IdAndVersionToId.md#maxon.IdAndVersionToId)(assetId) | Compacts an IdAndVersion into a id. |
| [`IdToIdAndVersionWithRepository`](../../maxon_generated/frameworks/asset/functions/maxon.IdToIdAndVersionWithRepository.md#maxon.IdToIdAndVersionWithRepository)(id, …) | Calls IdToIdAndVersion and adds the repository on top. |
| [`IdAndVersionToIdWithRepository`](../../maxon_generated/frameworks/asset/functions/maxon.IdAndVersionToIdWithRepository.md#maxon.IdAndVersionToIdWithRepository)(assetId, …) | Inverse of IdToIdAndVersionWithRepository. |

## Registries <a id="registries"></a>

|   |   |
|---|---|
| [`AssetTypes`](../../maxon_generated/frameworks/asset/registry/maxon.AssetTypes.md#module-maxon.AssetTypes)() |  |
| [`PresetAssetImplementations`](../../maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.md#module-maxon.PresetAssetImplementations)() |  |

## Enums <a id="enums"></a>

|   |   |
|---|---|
| [`APPSETTINGS.ASSETS`](../../maxon_generated/enums/maxon.APPSETTINGS.ASSETS.md#module-maxon.APPSETTINGS.ASSETS)() |  |
| [`ASSET_FIND_MODE`](../../maxon_generated/enums/maxon.ASSET_FIND_MODE.md#module-maxon.ASSET_FIND_MODE)() | The flags of ASSET_FIND_MODE control the behavior of [`AssetRepositoryInterface.FindAssets()`](../../maxon_generated/frameworks/asset/interface/maxon.AssetRepositoryInterface.md#maxon.AssetRepositoryInterface.FindAssets). |
| [`ASSETMETADATA`](../../maxon_generated/enums/maxon.ASSETMETADATA.md#module-maxon.ASSETMETADATA)() |  |
| [`AssetMetaDataInterface.KIND`](../../maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.md#module-maxon.AssetMetaDataInterface.KIND)() |  |
| [`ASSETREPOSITORYPROPERTIES`](../../maxon_generated/enums/maxon.ASSETREPOSITORYPROPERTIES.md#module-maxon.ASSETREPOSITORYPROPERTIES)() |  |
| [`ASSETLICENSETYPE`](../../maxon_generated/enums/maxon.ASSETLICENSETYPE.md#module-maxon.ASSETLICENSETYPE)() |  |
| [`ASSET.INFO`](../../maxon_generated/enums/maxon.ASSET.INFO.md#module-maxon.ASSET.INFO)() |  |
| [`ASSET.METAPROPERTIES`](../../maxon_generated/enums/maxon.ASSET.METAPROPERTIES.md#module-maxon.ASSET.METAPROPERTIES)() |  |
| [`ASSETTYPEPROPERTIES`](../../maxon_generated/enums/maxon.ASSETTYPEPROPERTIES.md#module-maxon.ASSETTYPEPROPERTIES)() |  |
