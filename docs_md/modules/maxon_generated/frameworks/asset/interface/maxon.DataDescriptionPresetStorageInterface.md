<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.DataDescriptionPresetStorageInterface.html -->

# maxon.DataDescriptionPresetStorageInterface <a id="maxon-datadescriptionpresetstorageinterface"></a>

## Description <a id="module-maxon.DataDescriptionPresetStorageInterface"></a><a id="description"></a>

Helper class to handle loading and saving of presets.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`DeletePreset`](#maxon.DataDescriptionPresetStorageInterface.DeletePreset)(repository, presetIdentifier, …) | Deletes a preset from the database. |
| [`GetPresetAttributes`](#maxon.DataDescriptionPresetStorageInterface.GetPresetAttributes)(repository, presetIdentifier) | Returns all stored attribute ids of a given preset identifier database. |
| [`GetPresetIdentifiers`](#maxon.DataDescriptionPresetStorageInterface.GetPresetIdentifiers)(repository) | Returns all preset identifiers registered under the given scope. |
| [`GetPresetName`](#maxon.DataDescriptionPresetStorageInterface.GetPresetName)(repository, presetIdentifier, …) | Returns the localized string of the preset name. |
| [`GetPresets`](#maxon.DataDescriptionPresetStorageInterface.GetPresets)(repository, presetIdentifier) | Returns all stored preset ids. |
| [`LoadPreset`](#maxon.DataDescriptionPresetStorageInterface.LoadPreset)(repository, presetIdentifier, …) | Reads a preset from the database. |
| [`SetPresetName`](#maxon.DataDescriptionPresetStorageInterface.SetPresetName)(assetDescription, …) | Sets the localized string of the preset name. |
| [`StorePreset`](#maxon.DataDescriptionPresetStorageInterface.StorePreset)(repository, presetIdentifier, …) | Stores a preset under the given scope and id in the database. |

## Methods Definition <a id="methods-definition"></a>

### *static* `DataDescriptionPresetStorageInterface.DeletePreset(repository, presetIdentifier, presetName)` <a id="maxon.DataDescriptionPresetStorageInterface.DeletePreset"></a>

Deletes a preset from the database.

**Parameters:**

- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to search for presets (including it’s bases).
- **presetIdentifier** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Identifier to check.
- **presetName** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Name of the preset.

**Returns:** **True** if the preset could be deleted. **False** if the repository which stores the asset is write protected.

**Return type:** bool

### *static* `DataDescriptionPresetStorageInterface.GetPresetAttributes(repository, presetIdentifier)` <a id="maxon.DataDescriptionPresetStorageInterface.GetPresetAttributes"></a>

Returns all stored attribute ids of a given preset identifier database.

**Parameters:**

- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to search for presets (including it’s bases).
- **presetIdentifier** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Identifier to check.

**Returns:** Array of attribute ids on success.

**Return type:** tuple( [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id))

### *static* `DataDescriptionPresetStorageInterface.GetPresetIdentifiers(repository)` <a id="maxon.DataDescriptionPresetStorageInterface.GetPresetIdentifiers"></a>

Returns all preset identifiers registered under the given scope.

**Parameters:** **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to search for presets (including it’s bases).

**Returns:** Array of [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id) on success.

**Return type:** [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]

### *static* `DataDescriptionPresetStorageInterface.GetPresetName(repository, presetIdentifier, presetName, language)` <a id="maxon.DataDescriptionPresetStorageInterface.GetPresetName"></a>

Returns the localized string of the preset name.

**Parameters:**

- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to search for presets (including it’s bases).
- **presetIdentifier** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Identifier to check.
- **presetName** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Name of the preset.
- **language** ([`maxon.LanguageRef`](../../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)) – Language to find.

**Returns:** Localized String on success.

**Return type:** str

### *static* `DataDescriptionPresetStorageInterface.GetPresets(repository, presetIdentifier)` <a id="maxon.DataDescriptionPresetStorageInterface.GetPresets"></a>

Returns all stored preset ids.

**Parameters:**

- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to search for presets (including it’s bases).
- **presetIdentifier** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Identifier to check.

**Returns:** Array of [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id) on success.

**Return type:** [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]

### *static* `DataDescriptionPresetStorageInterface.LoadPreset(repository, presetIdentifier, presetName)` <a id="maxon.DataDescriptionPresetStorageInterface.LoadPreset"></a>

Reads a preset from the database.

**Parameters:**

- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to search for presets (including it’s bases).
- **presetIdentifier** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Identifier to check.
- **presetName** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Name of the preset.

**Returns:** [`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary) on success.

**Return type:** [`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)

### *static* `DataDescriptionPresetStorageInterface.SetPresetName(assetDescription, presetIdentifier, presetName, language)` <a id="maxon.DataDescriptionPresetStorageInterface.SetPresetName"></a>

Sets the localized string of the preset name.

**Parameters:**

- **assetDescription** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to modify.
- **presetIdentifier** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Name of the preset.
- **presetName** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Localized String for the given language.
- **language** ([`maxon.LanguageRef`](../../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)) – Language to find.

### *static* `DataDescriptionPresetStorageInterface.StorePreset(repository, presetIdentifier, presetName, presetData)` <a id="maxon.DataDescriptionPresetStorageInterface.StorePreset"></a>

Stores a preset under the given scope and id in the database.

**Parameters:**

- **repository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to search for presets (including it’s bases).
- **presetIdentifier** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Identifier to check.
- **presetName** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Name of the preset.
- **presetData** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – Data to store.

**Returns:** [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription) on success.

**Return type:** [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)
