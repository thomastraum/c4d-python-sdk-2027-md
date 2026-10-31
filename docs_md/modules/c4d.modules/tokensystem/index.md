<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/tokensystem/index.html -->

# c4d.modules.tokensystem <a id="c4d-modules-tokensystem"></a>

## *class* `c4d.modules.tokensystem` <a id="c4d.modules.tokensystem"></a>

The token system allows the use of expressions in file names. The API makes it is possible to handle these tokens.

*New in version R17.048.*

> **Note:** Since R21 it’s now possible to register your own custom token with [`c4d.plugins.RegisterToken()`](../../c4d.plugins/index.md#c4d.plugins.RegisterToken) and [`c4d.plugins.RegisterHiddenToken()`](../../c4d.plugins/index.md#c4d.plugins.RegisterHiddenToken).

<a id="renderpathdata-dictionary"></a>**RenderPathData Dictionary**

The *rpData* (RenderPathData) parameter of [`StringConvertTokens()`](#c4d.modules.tokensystem.StringConvertTokens), [`FilenameConvertTokens()`](#c4d.modules.tokensystem.FilenameConvertTokens), [`StringConvertTokensFilter()`](#c4d.modules.tokensystem.StringConvertTokensFilter) and [`FilenameConvertTokensFilter()`](#c4d.modules.tokensystem.FilenameConvertTokensFilter) accepts a dictionary with the data to convert tokens.

These are the keys that can be set in such dictionary:

- *_doc*: [`BaseDocument`](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)
- *_rData*: [`RenderData`](../../c4d.documents/RenderData/index.md#c4d.documents.RenderData)
- *_rBc*: [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer)
- *_take*: [`BaseTake`](../takesystem/BaseTake/index.md#c4d.modules.takesystem.BaseTake)
- *_frame*: int
- *_layerName*: str
- *_layerTypeName*: str
- *_layerType*: int
- *_isLight*: bool
- *_lightNumber*: int
- *_isMaterial*: bool
- *_nodeName*: str
- *_checkUnresolved*: bool

For instance the dictionary can be initialized like this:

```python
rpd = {'_doc': doc, '_rData': renderData, '_rBc': renderSettings, '_frame': 1}
```

## Overview <a id="overview"></a>

**Path Conversion**

- [`c4d.modules.tokensystem.FilenameConvertTokens()`](#c4d.modules.tokensystem.FilenameConvertTokens): Converts tokenized path string to standard string by replacing all Tokens with correct values if found.
- [`c4d.modules.tokensystem.FilenameConvertTokensFilter()`](#c4d.modules.tokensystem.FilenameConvertTokensFilter): Converts tokenized path string to standard string by replacing all Tokens with correct values if found.
- [`c4d.modules.tokensystem.StringConvertTokens()`](#c4d.modules.tokensystem.StringConvertTokens): Converts tokenized path string to standard string by replacing all Tokens with correct values if found.
- [`c4d.modules.tokensystem.StringConvertTokensFilter()`](#c4d.modules.tokensystem.StringConvertTokensFilter): Converts tokenized path string to standard String by replacing all Tokens with correct values if found.

**Path Inspection**

- [`c4d.modules.tokensystem.FilenameExtractRoot()`](#c4d.modules.tokensystem.FilenameExtractRoot): Searches for the first Token in *path*.
- [`c4d.modules.tokensystem.FilenameSlicePath()`](#c4d.modules.tokensystem.FilenameSlicePath): Splits *path* in two parts if a Token is found as sub-folders and extracts root and filename path starting at sub-folder.
- [`c4d.modules.tokensystem.GetAllTokenEntries()`](#c4d.modules.tokensystem.GetAllTokenEntries): Returns a list of all available Token entries.
- [`c4d.modules.tokensystem.StringExtractRoot()`](#c4d.modules.tokensystem.StringExtractRoot): Searches for the first Token in *path*.

## Members <a id="members"></a>

### Path Conversion <a id="c4d.modules.tokensystem-function-Path-Conversion"></a>

#### `c4d.modules.tokensystem.FilenameConvertTokens(path, rpData)` <a id="c4d.modules.tokensystem.FilenameConvertTokens"></a>

Converts tokenized path string to standard string by replacing all Tokens with correct values if found.

**Parameters:**

- **path** (*str*) – The original path filename.
- **rpData** (*dict*) – The data used to extract value for Tokens. See [RenderPathData Dictionary](#renderpathdata-dictionary).

**Return type:** bool

**Returns:** The converted filename, or the original path if any error.

#### `c4d.modules.tokensystem.FilenameConvertTokensFilter(path, rpData, exclude)` <a id="c4d.modules.tokensystem.FilenameConvertTokensFilter"></a>

Converts tokenized path string to standard string by replacing all Tokens with correct values if found.  
Tokens added to *exclude* array are ignored.

**Parameters:**

- **path** (*str*) – The original path filename.
- **rpData** (*Dict*[*str*, *object*]) – The data used to extract value for Tokens. See [RenderPathData Dictionary](#renderpathdata-dictionary).
- **exclude** (*List*[*str*]) – A list of Tokens strings to be ignored.

**Return type:** bool

**Returns:** The converted filename, or the original path if any error.

#### `c4d.modules.tokensystem.StringConvertTokens(path, rpData)` <a id="c4d.modules.tokensystem.StringConvertTokens"></a>

Converts tokenized path string to standard string by replacing all Tokens with correct values if found.

**Parameters:**

- **path** (*str*) – The original path string.
- **rpData** (*dict*) – The data used to extract value for Tokens. See [RenderPathData Dictionary](#renderpathdata-dictionary).

**Return type:** bool

**Returns:** The converted string, or the original path if any error.

#### `c4d.modules.tokensystem.StringConvertTokensFilter(path, rpData, exclude)` <a id="c4d.modules.tokensystem.StringConvertTokensFilter"></a>

Converts tokenized path string to standard String by replacing all Tokens with correct values if found.  
Tokens added to *exclude* array are ignored.

**Parameters:**

- **path** (*str*) – The original path string.
- **rpData** (*dict*) – The data used to extract value for Tokens. See [RenderPathData Dictionary](#renderpathdata-dictionary).
- **exclude** (*list*) – A list of Tokens strings to be ignored.

**Return type:** bool

**Returns:** The converted string, or the original path if any error.

### Path Inspection <a id="c4d.modules.tokensystem-function-Path-Inspection"></a>

#### `c4d.modules.tokensystem.FilenameExtractRoot(path)` <a id="c4d.modules.tokensystem.FilenameExtractRoot"></a>

Searches for the first Token in *path*.  
If it is found and it is in-between “/..” returns the preceeding directory path filename.

**Parameters:** **path** (*str*) – The original path filename.

**Return type:** bool

**Returns:** The root filename path, or the original filename if no Token is found.

#### `c4d.modules.tokensystem.FilenameSlicePath(path)` <a id="c4d.modules.tokensystem.FilenameSlicePath"></a>

Splits *path* in two parts if a Token is found as sub-folders and extracts root and filename path starting at sub-folder.

**Parameters:** **path** (*str*) – The original path filename.

**Return type:** Tuple[str, str]

**Returns:** The root and filename paths.

#### `c4d.modules.tokensystem.GetAllTokenEntries()` <a id="c4d.modules.tokensystem.GetAllTokenEntries"></a>

Returns a list of all available Token entries.

*New in version R17.053.*

For instance the following code prints all registered tokens

```python
import c4d

tokens = c4d.modules.tokensystem.GetAllTokenEntries()
for entry in tokens:
    print(entry)
```

**Return type:** Optional[List[Dict[**_token**: str, **_help**: str, **_example**: str]]]

**Returns:** All the registered Token information, or **None** if an error occurred.

#### `c4d.modules.tokensystem.StringExtractRoot(path)` <a id="c4d.modules.tokensystem.StringExtractRoot"></a>

Searches for the first Token in *path*.  
If it is found and it is in-between “/..” returns the preceeding directory path string.

**Parameters:** **path** (*str*) – The original path string.

**Return type:** bool

**Returns:** The root string path, or the original string if no Token is found.
