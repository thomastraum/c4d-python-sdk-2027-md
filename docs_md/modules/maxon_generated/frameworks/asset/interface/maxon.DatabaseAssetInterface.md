<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.DatabaseAssetInterface.html -->

# maxon.DatabaseAssetInterface <a id="maxon-databaseassetinterface"></a>

## Description <a id="module-maxon.DatabaseAssetInterface"></a><a id="description"></a>

Implementation of DatabaseAsset.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetInterface`](maxon.AssetInterface.md#module-maxon.AssetInterface)

Child Class:

- [`maxon.DatabaseAsset`](../reference/maxon.DatabaseAsset.md#module-maxon.DatabaseAsset)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.DatabaseAssetInterface.VIRTUAL`](maxon.DatabaseAssetInterface.VIRTUAL.md#maxon.DatabaseAssetInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Create`](#maxon.DatabaseAssetInterface.Create)() | Creates a new database asset. |
| [`GetRepositoryName`](#maxon.DatabaseAssetInterface.GetRepositoryName)(repository, language, …) | Returns the database name. |
| [`SetRepositoryName`](#maxon.DatabaseAssetInterface.SetRepositoryName)(repository, name, language) | Stores a asset database name. |

## Methods Definition <a id="methods-definition"></a>

### *static* `DatabaseAssetInterface.Create()` <a id="maxon.DatabaseAssetInterface.Create"></a>

Creates a new database asset.

**Returns:** A new reference of [`maxon.ColorCategoryAssetInterface`](maxon.ColorCategoryAssetInterface.md#module-maxon.ColorCategoryAssetInterface).

**Return type:** [`maxon.DatabaseAsset`](../reference/maxon.DatabaseAsset.md#module-maxon.DatabaseAsset).

### *static* `DatabaseAssetInterface.GetRepositoryName(repository, language, fallbackName)` <a id="maxon.DatabaseAssetInterface.GetRepositoryName"></a>

Returns the database name.

**Parameters:**

- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Asset repository to use.
- **language** ([`maxon.LanguageRef`](../../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)) – Optional Language. Default is the program language.
- **fallbackName** (*str*) – Fall back string of no name was found.

**Returns:** String on success.

**Return type:** str

### *static* `DatabaseAssetInterface.SetRepositoryName(repository, name, language)` <a id="maxon.DatabaseAssetInterface.SetRepositoryName"></a>

Stores a asset database name.

**Parameters:**

- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Asset repository to modify.
- **name** (*str*) – Name to store.
- **language** ([`maxon.LanguageRef`](../../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)) – Optional Language. Default is the program language.
