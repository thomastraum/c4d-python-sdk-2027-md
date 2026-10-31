<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.LazyLanguageStringDataDescriptionDefinitionInterface.html -->

# maxon.LazyLanguageStringDataDescriptionDefinitionInterface <a id="maxon-lazylanguagestringdatadescriptiondefinitioninterface"></a>

## Description <a id="module-maxon.LazyLanguageStringDataDescriptionDefinitionInterface"></a><a id="description"></a>

Interface to manage lazy loading of `maxon.LanguageStringDataDescriptionDefinition` for description strings.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.LazyLanguageStringDataDescriptionDefinition`](../reference/maxon.LazyLanguageStringDataDescriptionDefinition.md#module-maxon.LazyLanguageStringDataDescriptionDefinition)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`DefaultValuePtr`](#maxon.LazyLanguageStringDataDescriptionDefinitionInterface.DefaultValuePtr)(*args) | NullValuePtr(self) Helper function to return the default value for an empty cow object. |
| [`Get`](#maxon.LazyLanguageStringDataDescriptionDefinitionInterface.Get)(languageId) | Returns the description of the given language. |
| [`GetMetaData`](#maxon.LazyLanguageStringDataDescriptionDefinitionInterface.GetMetaData)() | Returns all descriptions to export. |
| [`LoadAll`](#maxon.LazyLanguageStringDataDescriptionDefinitionInterface.LoadAll)() | Loads all string resources from the meta data into memory (e.g. |
| [`Set`](#maxon.LazyLanguageStringDataDescriptionDefinitionInterface.Set)(languageId, description) | Stores the description for the given language. |
| [`SetMetaData`](#maxon.LazyLanguageStringDataDescriptionDefinitionInterface.SetMetaData)(meta, path) | Sets the asset from which the definition shall be loaded lazily. |

## Methods Definition <a id="methods-definition"></a>

### *static* `LazyLanguageStringDataDescriptionDefinitionInterface.DefaultValuePtr(*args)` <a id="maxon.LazyLanguageStringDataDescriptionDefinitionInterface.DefaultValuePtr"></a>

NullValuePtr(self) Helper function to return the default value for an empty cow object.

**Returns:** An empty [`maxon.LazyLanguageStringDataDescriptionDefinition`](../reference/maxon.LazyLanguageStringDataDescriptionDefinition.md#module-maxon.LazyLanguageStringDataDescriptionDefinition).

**Return type:** [`maxon.LazyLanguageStringDataDescriptionDefinition`](../reference/maxon.LazyLanguageStringDataDescriptionDefinition.md#module-maxon.LazyLanguageStringDataDescriptionDefinition)

### `LazyLanguageStringDataDescriptionDefinitionInterface.Get(languageId)` <a id="maxon.LazyLanguageStringDataDescriptionDefinitionInterface.Get"></a>

Returns the description of the given language.

**Parameters:** **languageId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Id of the language to load.

**Returns:**

`maxon.DataDescriptionDefinition` on success.

**Return type:**

`maxon.DataDescriptionDefinition`

### `LazyLanguageStringDataDescriptionDefinitionInterface.GetMetaData()` <a id="maxon.LazyLanguageStringDataDescriptionDefinitionInterface.GetMetaData"></a>

Returns all descriptions to export.

**Returns:**

`maxon.LanguageStringDataDescriptionDefinition` on success.

**Return type:**

`maxon.LanguageStringDataDescriptionDefinition`

### `LazyLanguageStringDataDescriptionDefinitionInterface.LoadAll()` <a id="maxon.LazyLanguageStringDataDescriptionDefinitionInterface.LoadAll"></a>

Loads all string resources from the meta data into memory (e.g. for copying data).

### `LazyLanguageStringDataDescriptionDefinitionInterface.Set(languageId, description)` <a id="maxon.LazyLanguageStringDataDescriptionDefinitionInterface.Set"></a>

Stores the description for the given language.

**Parameters:**

- **languageId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Id of the language to load.
- **description** (`maxon.DataDescriptionDefinition`) – Description to store.

### `LazyLanguageStringDataDescriptionDefinitionInterface.SetMetaData(meta, path)` <a id="maxon.LazyLanguageStringDataDescriptionDefinitionInterface.SetMetaData"></a>

Sets the asset from which the definition shall be loaded lazily.

**Parameters:**

- **meta** ([`maxon.AssetMetaData`](../reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)) – Asset meta data to use for loading the strings.
- **path** (*str*) – Relative path of the description within the asset.
