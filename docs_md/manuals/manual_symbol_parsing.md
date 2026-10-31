<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_symbol_parsing.html -->

# Symbol Parsing <a id="symbol-parsing"></a><a id="manual-py-symbols"></a>

Explains resource symbols and mxutils.ImportSymbols.

## Introduction <a id="introduction"></a>

A symbol represents the name of a constant value in the Cinema 4D SDK.

Symbols should always be used rather than the direct constant value, as a value may change between two Cinema 4D releases.  
As an example Ocube is a symbols representing the constant value 5159. This symbol represent the Plugin ID used to register the Cube Object.  
Other built-in symbols are listed in the [Types and Symbols List](../indexes/type_index.md) documents.

> **See also:** [`mxutils.ImportSymbols()`](../modules/mxutils_api.md#mxutils.ImportSymbols)

## Internal Creation Process <a id="internal-creation-process"></a>

During the compilation of Cinema 4D, symbols and their associated constants values are extracted from the Cinema 4D C++ SDK. They are saved to a file shipped with Cinema 4D.  
During the first Cinema 4D startup, this file and all descriptions resource files are loaded by Python. Python will then parse theses files to expose symbols and their value to you, 3rd party plugin developers.  
This parsing is cached within the “symbolcache” file to speedup next Cinema 4D startup and this file is updated only when a resource files is added, removed or modified.

The symbolcache file is located in :

> (Mac) e.g: ‘/Users/UserName/Library/Preferences/MAXON/Maxon Cinema 4D R25_C333CB6C/prefs/symbolcache’
>
> (Windows) e.g: ‘C:\Users\UserName\AppData\Roaming\Maxon\Maxon Cinema 4D R25_C333CB6C\prefs\symbolcache’

## Symbols Parser Usage <a id="symbols-parser-usage"></a>

### `mxutils.ImportSymbols(path: str, output: Type = None) → dict[str, float | int | str] | None`

Parses elements of all resource files contained in the given `path` into the global scope of the caller or into a dictionary.

> **See also:** [Symbol Parsing](#manual-py-symbols)

**Parameters:**

- **path** (*str*) – The path within which header files should be discovered and parsed.
- **output** (*typing.Type*) – If the parsed symbols should be placed in the global scope or be returned as a dictionary. Pass `None` to let them be placed in the global scope and `dict` to have the function return them as a dictionary. Defaults to `None`.

**Returns:** The parsed symbol value pairs as or nothing when the `output` was `None`

**Return type:** dict[str, float | int | str] | None

**Example:**

The following header file `c:\data\c4d_symbols.h`,

```cpp
enum
{
    ID_FOO = 1000,
    ID_BAR = 1001,
    _DUMMY_ELEMENT_
};
```

can be imported as follows:

```python
import os
import mxutils

# Recursively parse header files in "c:\data" into this scope.
mxutils.ImportSymbols("c:\data")

# This would also work when only a singular file should be parsed.
mxutils.ImportSymbols("c:\data\c4d_symbols.h")

# The parsed symbols are now exposed in the global scope.
print(ID_FOO) # Will print 1000
print(ID_BAR) # Will print 1001

# Alternatively, symbols can also be parsed into a dictionary.
data: dict[str, int] = mxutils.ImportSymbols("c:\data\c4d_symbols.h", output=dict)

print(data["ID_FOO"]) # Will print 1000
print(data["ID_BAR"]) # Will print 1001
```

## Symbols Parser Features <a id="symbols-parser-features"></a>

### Supported Values <a id="supported-values"></a>

For the moment Cinema 4D, can only ingest Int32 value when reading the cached symbolcache files. However, the parser, understand and parse correctly all POD including string.

#### Integer Values <a id="integer-values"></a>

Integer values are parsed, all bit operations are supported, including simple arithmetic.

| C++ Input | Python Output |
|---|---|
| #define LEGACY_DRAW_FLAGS_DEPTH_TEST_ALWAYS (1 << 10) | LEGACY_DRAW_FLAGS_DEPTH_TEST_ALWAYS == 1024 |
| #define COLORMODE_MAXCOLOR ((1 << 6) - 1) | COLORMODE_MAXCOLOR == 63 |
| #define HUDCONTROL_FLAG_KEYVALUE_CHANGED (1ULL << 32ULL)<br>> **Note:** UL/LL/ULL are removed only if the previous char is a number, otherwise it’s kept to not break symbols like BASEDRAW_DISPLAYFILTER_NULL. | HUDCONTROL_FLAG_KEYVALUE_CHANGED == 4294967296 |

#### Hexadecimal Values <a id="hexadecimal-values"></a>

Hexadecimal values are parsed.

| C++ Input | Python Output |
|---|---|
| #define ZIP_FILE_FLAG_OWNER_R 0x01000000 | ZIP_FILE_FLAG_OWNER_R == 16777216 |

#### Float Values <a id="float-values"></a>

Float32 values are parsed, supporting scientific notation.

| C++ Input | Python Output |
|---|---|
| #define MAXRANGE 1.0e20 | ZIP_FILE_FLAG_OWNER_R == 1e+20 |
| #define MIN_EPSILON 0.001 | MIN_EPSILON == 0.001 |

#### Single Quote Strings <a id="single-quote-strings"></a>

Single quote string values are converted to their corresponding integer value if they have length of 3 or 4. Otherwise they are treated as regular string.

| C++ Input | Python Output |
|---|---|
| #define QUICKTAB_BARTITLE ‘btit’ | QUICKTAB_BARTITLE == 1651796340 |

#### CHAR_CONST32 Values <a id="char-const32-values"></a>

CHAR_CONST32 values are converted to their corresponding integer value.

| C++ Input | Python Output |
|---|---|
| #define FLAT_SETTINGS_MAGIC CHAR_CONST32(‘fflt’) | FLAT_SETTINGS_MAGIC == 1717988468 |

#### C4D_FOUR_BYTE Values <a id="c4d-four-byte-values"></a>

C4D_FOUR_BYTE values are converted to their corresponding integer value.

| C++ Input | Python Output |
|---|---|
| #define QUICKTAB_BAR C4D_FOUR_BYTE(0,’b’,’a’,’r’) | QUICKTAB_BAR == 6447474 |

#### Double Quote String Values <a id="double-quote-string-values"></a>

Double quote string values are parsed.

| C++ Input | Python Output |
|---|---|
| #define MENUCOMMAND “CMD” | MENUCOMMAND == “CMD” |

#### Values Referencing Other Values <a id="values-referencing-other-values"></a>

Values referencing other values are resolved.

| C++ Input | Python Output |
|---|---|
| `#define POLY_TRIANG_NGON 32`<br>`#define POLY_TRIANG_FORCE_NGON (128 \| POLY_TRIANG_NGON)` | POLY_TRIANG_NGON == 32 POLY_TRIANG_FORCE_NGON == 160<br>> **Note:** The system is able to resolve any numbers of references. |
| `enum class HDIRTY_ID {RENDERSETTINGS = 7}`<br>`enum class HDIRTYFLAGS {RENDERSETTINGS = (1 << (UInt32)HDIRTY_ID::RENDERSETTINGS)}` | HDIRTY_ID_RENDERSETTINGS == 7 HDIRTYFLAGS_RENDERSETTINGS == 128 |

### Supported Types <a id="supported-types"></a>

#### Defines <a id="defines"></a>

Defines expressing a value are parsed. Define expressing an expression/macro are not parsed.

| C++ Input | Python Output |
|---|---|
| #define CUSTOMGUI_TEXTURENAME 1000484 | CUSTOMGUI_TEXTURENAME == 1000484 |
| #define COLORBYTES_GRAYw (COLORBYTES_GRAY * sizeof(PIX_W)) // COLORBYTES_GRAY == 1, sizeof(PIX_W) == 2 | COLORBYTES_GRAYw == 2 |

#### static const Int32 <a id="static-const-int32"></a>

static const Int32 and only Int32 value are parsed and outputs using the current namespace/class.

| C++ Input | Python Output |
|---|---|
| static const Int32 ID_CUSTOMDATA_TAG_LIB = 431000187; | ID_CUSTOMDATA_TAG_LIB == 431000187 |

#### Enums <a id="enums"></a>

Enums value are incremented, starting from 0 if no value is defined otherwise, it take the previous enum value.

#### Unnamed Enums <a id="unnamed-enums"></a>

Enums without name are expressed in Python with the current C++ namespace or class.

| C++ Input | Python Output |
|---|---|
| enum {Mcamera, Xyz, Mdrag} | Mcamera == 0 Xyz == 1 Mdrag = 2 |
| enum {Mcamera = 5, Xyz, Mdrag = 1000} | Mcamera == 5 Xyz == 6 Mdrag = 1000 |

#### Named Enums <a id="named-enums"></a>

Enums with name are expressed in Python with the current C++ namespace or class, so their names are not took into consideration.

| C++ Input | Python Output |
|---|---|
| enum DA {DA_NIL= 0, DA_VOID = 14}; | DA_NIL == 0 DA_VOID == 14<br>> **Note:** DA.DA_NIL does not exist |

#### Enums Struct/Class and MAXON_ENUM_LIST/MAXON_ENUM_FLAGS <a id="enums-struct-class-and-maxon-enum-list-maxon-enum-flags"></a>

Enums struct, class, MAXON_ENUM_LIST and MAXON_ENUM_FLAGS are expressed in Python with their scope name. Given a enum class XYZ with the value ABC will output XYZ_ABC.

| C++ Input | Python Output |
|---|---|
| `enum class MDDIRTY`<br>`{`<br>`NONE = 0,`<br>`ARRAYCOUNT = (1 << 0)`<br>`} MAXON_ENUM_FLAGS(MDDIRTY);` | MDDIRTY_NONE MDDIRTY_0 == 0 MDDIRTY_ARRAYCOUNT == 1<br>> **Note:** The MDDIRTY_0 value is added to Python, each time there is a NONE entry to not break API compatibility as older version of the API may still use it. |
| `enum class MD_TYPE`<br>`{`<br>`MD_NONE = DA_NIL,`<br>`MD_CHAR = 40000000,`<br>`} MAXON_ENUM_LIST(MD_TYPE);` | MD_TYPE_MD_NONE = 0 MD_TYPE_MD_CHAR = 40000000 |

## See Also <a id="see-also"></a>

- [Dialog and Description Resources](manual_resource_files.md): Explains how to define dialogs and node parameters with resource files, and how to use them from Python.
- [Implementing Plugins](manual_implementing_plugins.md): Explains the basic concepts of implementing plugins.
- [Example mxutils_symboltranslationcache.py](../examples/misc/mxutils_symboltranslationcache.py.md): Demonstrates translating Cinema 4D symbols with SymbolTranslationCache.
- [Example py_cmd_gui_resources.pyp](../examples/plugins/py_cmd_gui_resources/py_cmd_gui_resources.pyp.md): Demonstrates a plugin that uses resources to define its dialog layout and string translations.
