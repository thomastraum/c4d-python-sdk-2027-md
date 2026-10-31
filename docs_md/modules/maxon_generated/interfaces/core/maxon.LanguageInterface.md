<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/core/maxon.LanguageInterface.html -->

# maxon.LanguageInterface <a id="maxon-languageinterface"></a>

## Description <a id="module-maxon.LanguageInterface"></a><a id="description"></a>

## Inheritance diagram <a id="inheritance-diagram"></a>

Child Class:

- [`maxon.LanguageRef`](../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Alloc`](#maxon.LanguageInterface.Alloc)([source_location]) |  |
| [`GetFallbackLanguage`](#maxon.LanguageInterface.GetFallbackLanguage)() | Returns the fallback language of this language. |
| [`GetIdentifier`](#maxon.LanguageInterface.GetIdentifier)() | Returns the identifier of a language. |
| [`GetName`](#maxon.LanguageInterface.GetName)() | Returns the real (country-specific) name of a language. |
| [`LoadResourceString`](#maxon.LanguageInterface.LoadResourceString)(scope, keyValue) | Loads a string from the resource. |
| [`ToString`](#maxon.LanguageInterface.ToString)() |  |

## Methods Definition <a id="methods-definition"></a>

### *static* `LanguageInterface.Alloc(source_location=None)` <a id="maxon.LanguageInterface.Alloc"></a>

### `LanguageInterface.GetFallbackLanguage()` <a id="maxon.LanguageInterface.GetFallbackLanguage"></a>

Returns the fallback language of this language.

**Returns:** **None** if the language has no fallback language (e.g. “en-US” has none because it’s the root of all languages).

**Return type:** [`maxon.LanguageRef`](../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)

### `LanguageInterface.GetIdentifier()` <a id="maxon.LanguageInterface.GetIdentifier"></a>

Returns the identifier of a language.

**Returns:** The name.

**Return type:** [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)

### `LanguageInterface.GetName()` <a id="maxon.LanguageInterface.GetName"></a>

Returns the real (country-specific) name of a language.

**Returns:** The name.

**Return type:** str

### `LanguageInterface.LoadResourceString(scope, keyValue)` <a id="maxon.LanguageInterface.LoadResourceString"></a>

Loads a string from the resource.

**Parameters:**

- **scope** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The resource scope of a resource symbol.
- **keyValue** ([`maxon.InternedId`](../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The value of a resource symbol.

**Returns:** String.

**Return type:** str

### `LanguageInterface.ToString()` <a id="maxon.LanguageInterface.ToString"></a>
