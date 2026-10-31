<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.LazyLanguageDictionaryInterface.html -->

# maxon.LazyLanguageDictionaryInterface <a id="maxon-lazylanguagedictionaryinterface"></a>

## Description <a id="module-maxon.LazyLanguageDictionaryInterface"></a><a id="description"></a>

Interface to manage lazy loading of `maxon.LanguageDictionary` for description strings.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.LazyLanguageDictionary`](../reference/maxon.LazyLanguageDictionary.md#module-maxon.LazyLanguageDictionary)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`DefaultValuePtr`](#maxon.LazyLanguageDictionaryInterface.DefaultValuePtr)(*args) | Helper function to return the default value for an empty cow object. |
| [`Get`](#maxon.LazyLanguageDictionaryInterface.Get)(languageId) | Returns the description of the given language. |
| [`GetMetaData`](#maxon.LazyLanguageDictionaryInterface.GetMetaData)() | Returns all descriptions to export. |
| [`LoadAll`](#maxon.LazyLanguageDictionaryInterface.LoadAll)() | Loads all string resources from the meta data into memory (e.g. |
| [`Set`](#maxon.LazyLanguageDictionaryInterface.Set)(languageId, description) | Stores the description for the given language. |
| [`SetMetaData`](#maxon.LazyLanguageDictionaryInterface.SetMetaData)(meta, path) | Sets the asset from which the definition shall be loaded lazily. |

## Methods Definition <a id="methods-definition"></a>

### *static* `LazyLanguageDictionaryInterface.DefaultValuePtr(*args)` <a id="maxon.LazyLanguageDictionaryInterface.DefaultValuePtr"></a>

Helper function to return the default value for an empty cow object.

**Returns:** An empty [`maxon.LazyLanguageDictionary`](../reference/maxon.LazyLanguageDictionary.md#module-maxon.LazyLanguageDictionary).

**Return type:** [`maxon.LazyLanguageDictionary`](../reference/maxon.LazyLanguageDictionary.md#module-maxon.LazyLanguageDictionary)

### `LazyLanguageDictionaryInterface.Get(languageId)` <a id="maxon.LazyLanguageDictionaryInterface.Get"></a>

Returns the description of the given language.

**Parameters:** **languageId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Id of the language to load.

**Returns:** [`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary) on success.

**Return type:** [`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)

### `LazyLanguageDictionaryInterface.GetMetaData()` <a id="maxon.LazyLanguageDictionaryInterface.GetMetaData"></a>

Returns all descriptions to export.

**Returns:** [`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary) on success.

**Return type:** [`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)

### `LazyLanguageDictionaryInterface.LoadAll()` <a id="maxon.LazyLanguageDictionaryInterface.LoadAll"></a>

Loads all string resources from the meta data into memory (e.g. for copying data).

### `LazyLanguageDictionaryInterface.Set(languageId, description)` <a id="maxon.LazyLanguageDictionaryInterface.Set"></a>

Stores the description for the given language.

**Parameters:**

- **languageId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Id of the language to load.
- **description** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – [`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary) to store.

### `LazyLanguageDictionaryInterface.SetMetaData(meta, path)` <a id="maxon.LazyLanguageDictionaryInterface.SetMetaData"></a>

Sets the asset from which the definition shall be loaded lazily.

**Parameters:**

- **meta** ([`maxon.AssetMetaData`](../reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)) – Asset meta data to use for loading the strings.
- **path** (*str*) – Relative path of the description within the asset.
