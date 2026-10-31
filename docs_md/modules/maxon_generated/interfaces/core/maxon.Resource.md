<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/core/maxon.Resource.html -->

# maxon.Resource <a id="maxon-resource"></a>

## Description <a id="module-maxon.Resource"></a><a id="description"></a>

Class that handles resources.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`FindLanguage`](#maxon.Resource.FindLanguage)(identifier) | Finds for a given identifier (e.g. |
| [`GetAllLanguages`](#maxon.Resource.GetAllLanguages)() | Retrieves an array of all available languages. |
| [`GetCurrentLanguage`](#maxon.Resource.GetCurrentLanguage)() | Returns the language that is currently used. |
| [`GetDefaultLanguage`](#maxon.Resource.GetDefaultLanguage)() | Returns the default language (normally english). |
| [`LoadResourceString`](#maxon.Resource.LoadResourceString)(scope, keyValue) | Loads a string from the resource. |
| [`SetCurrentLanguage`](#maxon.Resource.SetCurrentLanguage)(language) | Sets the current language. |
| [`WriteLanguagePrf`](#maxon.Resource.WriteLanguagePrf)(language) | Writes the language preference file. |

## Methods Definition <a id="methods-definition"></a>

### *static* `Resource.FindLanguage(identifier)` <a id="maxon.Resource.FindLanguage"></a>

Finds for a given identifier (e.g. en-US) the language.

**Parameters:** **identifier** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The language Id.

**Return type:** [`maxon.LanguageRef`](../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)

**Returns:** The language.

### *static* `Resource.GetAllLanguages()` <a id="maxon.Resource.GetAllLanguages"></a>

Retrieves an array of all available languages.

**Return type:** [`maxon.BaseArray`](../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.LanguageRef`](../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)]

**Returns:** Array with all languages on success.

### *static* `Resource.GetCurrentLanguage()` <a id="maxon.Resource.GetCurrentLanguage"></a>

Returns the language that is currently used.

**Return type:** [`maxon.LanguageRef`](../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)

**Returns:** The language.

### *static* `Resource.GetDefaultLanguage()` <a id="maxon.Resource.GetDefaultLanguage"></a>

Returns the default language (normally english).

**Return type:** [`maxon.LanguageRef`](../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)

**Returns:** The language.

### *static* `Resource.LoadResourceString(scope, keyValue)` <a id="maxon.Resource.LoadResourceString"></a>

Loads a string from the resource.

Other than the member of LanguageRef this routine tries to load it from the current language first and -if that fails- from the default language.

**Parameters:**

- **scope** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The resource scope of a resource symbol.
- **keyValue** ([`maxon.InternedId`](../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The value of a resource symbol.

**Return type:** [`maxon.String`](../../references/core/maxon.String.md#module-maxon.String)

**Returns:** String.

### *static* `Resource.SetCurrentLanguage(language)` <a id="maxon.Resource.SetCurrentLanguage"></a>

Sets the current language.

**Return type:** [`maxon.LanguageRef`](../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)

**Returns:** The language.

### *static* `Resource.WriteLanguagePrf(language)` <a id="maxon.Resource.WriteLanguagePrf"></a>

Writes the language preference file.

**Parameters:** **language** ([`maxon.LanguageRef`](../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)) – The language.
