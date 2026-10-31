<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/mxutils/mxutils.SymbolTranslationCache.html -->

# mxutils.SymbolTranslationCache <a id="mxutils-symboltranslationcache"></a>

## Description <a id="module-mxutils.SymbolTranslationCache"></a><a id="description"></a>

Caches and provides access to string symbols over their integer values.

> **Note:**
>
> `mxutils.g_c4d_symbol_translation_cache` is a global instance of this class that caches the symbols of the `c4d` module. It is recommended to use this instance instead of creating a new one.

**Example:**

```python
import mxutils

# Access a symbol in the global cache for the c4d module.
print(mxutils.g_c4d_symbol_translation_cache[5159]) # prints: ['Ocube', 'OBJECT_CUBE']

# Symbols are not unambiguous and there can exist multiple symbols for the same value,
# as here for Ocube. While they are here semantically the same, this is not always the 
# case, and there can be full own collisions between symbols.
```

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Get`](#mxutils.SymbolTranslationCache.Get)(key[, filter]) | Returns the symbol translation for a given key with an optional filter. |
| [`Search`](#mxutils.SymbolTranslationCache.Search)(pattern) | Searches all cached symbols with a regular expression. |
| [`__build__`](#mxutils.SymbolTranslationCache.__build__)() | Builds the cache. |
| [`__getitem__`](#mxutils.SymbolTranslationCache.__getitem__)(key) | Retrieves the symbol translation for a given key. |
| [`__init__`](#mxutils.SymbolTranslationCache.__init__)(module[, buildDirectly]) | Initializes a cache instance. |

## Methods Definition <a id="methods-definition"></a>

### `SymbolTranslationCache.Get(key: int, filter: str = '') → list` <a id="mxutils.SymbolTranslationCache.Get"></a>

Returns the symbol translation for a given key with an optional filter.

**Parameters:**

- **key** (*int*) – The key to retrieve the translation for.
- **filter** (*str*, *optional*) – The filter to apply to the translation and is evaluated as a regular expression. Defaults to an empty string.

**Returns:** The symbol translations.

**Return type:** list[str]

### `SymbolTranslationCache.Search(pattern: str) → list` <a id="mxutils.SymbolTranslationCache.Search"></a>

Searches all cached symbols with a regular expression.

**Parameters:** **pattern** (*str*) – The regular expression to match against symbol names.

**Returns:** Matching symbol names and their integer values.

**Return type:** list[tuple[str, int]]

### `SymbolTranslationCache.__build__() → None` <a id="mxutils.SymbolTranslationCache.__build__"></a>

Builds the cache.

### `SymbolTranslationCache.__getitem__(key: int) → list[str] | None` <a id="mxutils.SymbolTranslationCache.__getitem__"></a>

Retrieves the symbol translation for a given key.

**Parameters:** **key** (*int*) – The key to retrieve the translation for.

**Returns:** The symbol translation.

**Return type:** str

**Raises:** **TypeError** – If the key is not an integer.

**Example:**

```python
import c4d
import mxutils

# Create a cache for the c4d package.
cache = mxutils.SymbolTranslationCache(c4d)

# Access a symbol in the cache.
print(cache[5159]) # ['Ocube', 'OBJECT_CUBE']

# Symbols are not unambiguous and there can exist multiple symbols for the same value,
# as here for Ocube. The cache will be built upon first access, unless the #buildDirectly
# argument was set to True.
```

### `SymbolTranslationCache.__init__(module: object, buildDirectly: bool = False) → None` <a id="mxutils.SymbolTranslationCache.__init__"></a>

Initializes a cache instance.

**Parameters:**

- **module** (*object*) – The module to cache symbols from. Submodules are not being unpacked.
- **buildDirectly** (*bool*) – If the cache should be built directly upon initialization.
