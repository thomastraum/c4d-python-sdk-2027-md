<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/io/maxon.UrlInterface.html -->

# maxon.UrlInterface <a id="maxon-urlinterface"></a>

## Description <a id="module-maxon.UrlInterface"></a><a id="description"></a>

Interface class for [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). | A [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) defines the location of a file or a similar resource. | The class allows to construct a file path and to handle files. | | Urls consist of three parts:

> 1. A scheme, an authority and a path. The readable text-representation is “scheme://authority/path”.  
>    The scheme defines which handler is used, e.g. “http” for web-based connections or “file” for the regular file system.
> 2. The authority defines the machine, which can be empty for “localhost”, a network drive or a webserver.  
>    It can also refer to an embedded file, e.g. a ZIP. To distinguish that case the readable text representation contains brackets: “scheme://[authority]/path”.  
>    Nesting is possible repeatedly.
> 3. Finally the path component defines the unique location of a file or directory on the target machine.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Append`](#maxon.UrlInterface.Append)(relativeUrl) | Appends a relative string or a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) to the current one. |
| [`CheckSuffix`](#maxon.UrlInterface.CheckSuffix)(suffix) | Checks whether the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) has the a given suffix. |
| [`ClearSuffix`](#maxon.UrlInterface.ClearSuffix)() | Deletes the suffix of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`Compare`](#maxon.UrlInterface.Compare)(self, name[, mode]) | Compares the object against ‘name’. |
| [`Get`](#maxon.UrlInterface.Get)(key[, defaultValue]) | Returns [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) attributes. |
| [`GetAuthority`](#maxon.UrlInterface.GetAuthority)() | Returns the authority of a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`GetComponents`](#maxon.UrlInterface.GetComponents)() | Returns all parts of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) system path as separated strings. |
| [`GetData`](#maxon.UrlInterface.GetData)(key) | Returns [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) attributes. |
| [`GetDirectory`](#maxon.UrlInterface.GetDirectory)() | Returns the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) of the directory. |
| [`GetEmbeddedUrl`](#maxon.UrlInterface.GetEmbeddedUrl)() | Returns an embedded [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`GetName`](#maxon.UrlInterface.GetName)() | Returns the name of the last component. |
| [`GetPath`](#maxon.UrlInterface.GetPath)() | Returns the path component of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`GetScheme`](#maxon.UrlInterface.GetScheme)() | Gets the UrlScheme of the Url. Is guaranteed to be lowercase (canonical form for urls) |
| [`GetSuffix`](#maxon.UrlInterface.GetSuffix)() | Returns the suffix of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`GetSystemPath`](#maxon.UrlInterface.GetSystemPath)() | Returns a path from the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) that the current operating system (or scheme handler) can understand. |
| [`GetUrl`](#maxon.UrlInterface.GetUrl)() | Returns the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) as a string. |
| [`IsEmpty`](#maxon.UrlInterface.IsEmpty)() | Returns if the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) has no content. |
| [`IsPopulated`](#maxon.UrlInterface.IsPopulated)() | Returns if the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) has any content. |
| [`RemoveName`](#maxon.UrlInterface.RemoveName)() | Removes the last part of a Url. |
| [`Set`](#maxon.UrlInterface.Set)(key, value) | Modifies or sets a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) attribute. |
| [`SetAuthority`](#maxon.UrlInterface.SetAuthority)(authority) | Sets the authority of a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`SetData`](#maxon.UrlInterface.SetData)(key, value) | Modifies or sets a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) attribute. |
| [`SetEmbeddedUrl`](#maxon.UrlInterface.SetEmbeddedUrl)(url) | Replaces and sets an embedded [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`SetName`](#maxon.UrlInterface.SetName)(name) | Replaces the last component of a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`SetPath`](#maxon.UrlInterface.SetPath)(path[, convertWindowsBackslashes]) | Replaces the path component of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`SetScheme`](#maxon.UrlInterface.SetScheme)(scheme) | Sets the scheme of the Url. |
| [`SetSuffix`](#maxon.UrlInterface.SetSuffix)(suffix) | Replaces the suffix of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`SetSystemPath`](#maxon.UrlInterface.SetSystemPath)(path) | Stores a system path in a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`SetUrl`](#maxon.UrlInterface.SetUrl)(urlString, enableDefaultFallbackScheme) | Sets the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |

## Methods Definition <a id="methods-definition"></a>

### `UrlInterface.Append(relativeUrl)` <a id="maxon.UrlInterface.Append"></a>

Appends a relative string or a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) to the current one.

> **Note:** If the Url is *file:///c:/directory* a call of
>
> ```python
> url.Append(maxon.Url("test/file.txt"))
> ```
>
> will result in *file:///c:/directory/test/file.txt*.

**Parameters:** **srelativeUrl** – The relative [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) to append.

### `UrlInterface.CheckSuffix(suffix)` <a id="maxon.UrlInterface.CheckSuffix"></a>

Checks whether the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) has the a given suffix.

> **Note:** If the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) is “[file:///c:/directory/file.txt](file:///c:/directory/file.txt)” a call of CheckSuffix(“txt”_s) will return true.

**Parameters:** **suffix** (*str*) – The suffix without dot to check against.

**Returns:** True if the suffix matches.

**Return type:** bool

### `UrlInterface.ClearSuffix()` <a id="maxon.UrlInterface.ClearSuffix"></a>

Deletes the suffix of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

> **Note:** If the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) was “[file:///c:/directory/file.txt](file:///c:/directory/file.txt)” a call will result in “[file:///c:/directory/file](file:///c:/directory/file)”.

### `UrlInterface.Compare(self, name, mode=enums.URLCOMPARE.DEFAULT)` <a id="maxon.UrlInterface.Compare"></a>

Compares the object against ‘name’.

> **Note:**
>
> By default the comparison is case-sensitive, so ‘./Test.tif’ and ‘./test.tif’ are not the same.  
> To check if Urls point to the identical item use `maxon.Url.IoNormalizeAndResolve()` instead.

**Parameters:**

- **name** ([`maxon.UrlInterface`](#module-maxon.UrlInterface)) – The [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) to be compared with.
- **mode** (`maxon.URLCOMPARE`) – The comparison mode.

**Returns:** The compared result.

**Return type:** maxon.COMPARERESULT

### `UrlInterface.Get(key, defaultValue=None)` <a id="maxon.UrlInterface.Get"></a>

Returns [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) attributes.

> **See also:**
>
> `maxon.URLFLAGS` for details.

**Parameters:**

- **key** (Union[`maxon.URLFLAGS`, [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)]) – The id of the property to get. The possible values for id depend on the scheme.
- **defaultValue** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The default value returned if the key was not found.

**Returns:** The attribute value or an error if there was none.

**Return type:** [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `UrlInterface.GetAuthority()` <a id="maxon.UrlInterface.GetAuthority"></a>

Returns the authority of a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). The authority can be a machine, server or embedded file.

**Returns:**

The authority of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

If the machine is localhost the returned [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) is empty.  
If it is a machine or server the scheme will be `maxon.URLSCHEME_AUTHORITY`.  
Otherwise it defines an embedded file.

**Return type:** [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

### `UrlInterface.GetComponents()` <a id="maxon.UrlInterface.GetComponents"></a>

Returns all parts of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) system path as separated strings.

> **Note:** If the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) was “[file:///c:/directory/file.txt](file:///c:/directory/file.txt)” a call of GetComponents will return: { “C:”, “directory”, “file.txt” }.

**Returns:** Array with all components as strings.

**Return type:** [`maxon.BaseArray`](../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.String`](../../references/core/maxon.String.md#module-maxon.String)]

### `UrlInterface.GetData(key)` <a id="maxon.UrlInterface.GetData"></a>

Returns [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) attributes. See `maxon.URLFLAGS` for details.

**Parameters:** **key** (Union[`maxon.URLFLAGS`, [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)]) – The id of the property to get. The possible values for id depend on the scheme.

**Returns:** The attribute value or an error if there was none.

**Return type:** [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `UrlInterface.GetDirectory()` <a id="maxon.UrlInterface.GetDirectory"></a>

Returns the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) of the directory.

> **Note:** If the Url was “[file:///c:/directory/file.txt](file:///c:/directory/file.txt)” a call of GetDirectory() will return “[file:///c:/directory](file:///c:/directory)”.

**Returns:** The directory.

**Return type:** [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

### `UrlInterface.GetEmbeddedUrl()` <a id="maxon.UrlInterface.GetEmbeddedUrl"></a>

Returns an embedded [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

> **Note:** If the Url is “zip://[file:///c:/images.zip]/image01.jpg” a call to GetEmbeddedUrl() will return “file:///c:/images.zip”.

**Returns:** The embedded [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) or if there was none, an empty [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

**Return type:** [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

### `UrlInterface.GetName()` <a id="maxon.UrlInterface.GetName"></a>

Returns the name of the last component.

> **Note:** if the Url is “[file:///c:/directory/file.txt](file:///c:/directory/file.txt)” a call to GetName() will return “file.txt”.

**Returns:** The name of the last path component.

**Return type:** str

### `UrlInterface.GetPath()` <a id="maxon.UrlInterface.GetPath"></a>

Returns the path component of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

> **Note:** This doesn’t contain scheme and authority. E.g. if the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) is “[file:///c:/directory/file.txt](file:///c:/directory/file.txt)” a call will return “c:/directory/file.txt”.

**Returns:** The path component of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) (with no authority and scheme).

**Return type:** str

### `UrlInterface.GetScheme()` <a id="maxon.UrlInterface.GetScheme"></a>

Gets the UrlScheme of the Url. Is guaranteed to be lowercase (canonical form for urls)  
if scheme was automatically determined through [`maxon.UrlInterface.SetUrl()`](#maxon.UrlInterface.SetUrl), otherwise as set.  
In most schemes paths are a combination of the directory path and file path, but the path could also be a network query or database entry. Path components are always separated by a forward slash and the forward slash is a reserved character that cannot be used for names.

**Returns:** The scheme name.

**Return type:** str

### `UrlInterface.GetSuffix()` <a id="maxon.UrlInterface.GetSuffix"></a>

Returns the suffix of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

> **Note:** If the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) was “[file:///c:/directory/file.txt](file:///c:/directory/file.txt)” a call of GetSuffix() will return “txt”.

**Returns:** The suffix without dot.

**Return type:** str

### `UrlInterface.GetSystemPath()` <a id="maxon.UrlInterface.GetSystemPath"></a>

Returns a path from the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) that the current operating system (or scheme handler) can understand.  
If the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) contains no valid scheme an error will be returned.  
An error will also be returned if the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) contains illegal characters for the scheme, e.g. backslashes on Windows in a file scheme.

**Returns:** The system path.

**Return type:** str

### `UrlInterface.GetUrl()` <a id="maxon.UrlInterface.GetUrl"></a>

Returns the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) as a string.

> **Note:** A [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) has the format scheme://authority/path.

**Returns:** The [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) as a string.

**Return type:** str

### `UrlInterface.IsEmpty()` <a id="maxon.UrlInterface.IsEmpty"></a>

Returns if the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) has no content.  
A [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) is considered empty if it has no path component and no authority (even if a scheme is set).

**Returns:** True if the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) is empty.

**Return type:** bool

### `UrlInterface.IsPopulated()` <a id="maxon.UrlInterface.IsPopulated"></a>

Returns if the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) has any content.  
A [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) is considered populated if it has a path component or authority set.

**Returns:** True if the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) has content.

**Return type:** bool

### `UrlInterface.RemoveName()` <a id="maxon.UrlInterface.RemoveName"></a>

Removes the last part of a Url.

> **Note:** If the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) is “[file:///c:/directory/file.txt](file:///c:/directory/file.txt)” a call of RemoveName() will result in “[file:///c:/directory](file:///c:/directory)”.

### `UrlInterface.Set(key, value)` <a id="maxon.UrlInterface.Set"></a>

Modifies or sets a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) attribute.

> **See also:**
>
> `maxon.URLFLAGS` for details.

**Parameters:**

- **key** (Union[`maxon.URLFLAGS`, [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)]) – The id of the property to set. The possible values for id depend on the scheme.
- **value** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data) to be set.

### `UrlInterface.SetAuthority(authority)` <a id="maxon.UrlInterface.SetAuthority"></a>

Sets the authority of a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). This can be a machine or server.

> **Note:** Empty string can be passed for no authority / localhost. The authority scheme will be URLSCHEME_AUTHORITY.

**Parameters:** **authority** (Union[str, [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)]) – The new authority.

**Returns:**

### `UrlInterface.SetData(key, value)` <a id="maxon.UrlInterface.SetData"></a>

Modifies or sets a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) attribute. See `maxon.URLFLAGS` for details.

**Parameters:**

- **key** (Union[`maxon.URLFLAGS`, [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)]) – The id of the property to set. The possible values for id depend on the scheme.
- **value** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data) to be set.

### `UrlInterface.SetEmbeddedUrl(url)` <a id="maxon.UrlInterface.SetEmbeddedUrl"></a>

Replaces and sets an embedded [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

> **Note:** If the Url is “zip://[file:///c:/images.zip]/image01.jpg” a call to SetEmbeddedUrl(“file:///c:/otherimages.zip”_s) will result in “zip://[file:///c:/otherimages.zip]/image01.jpg”.

**Parameters:** **url** – The new embedded [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

### `UrlInterface.SetName(name)` <a id="maxon.UrlInterface.SetName"></a>

Replaces the last component of a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). The name must not contain a forward slashes and under Windows additionally no backslashes.

> **Note:** If the Url is “[file:///c:/directory/file.txt](file:///c:/directory/file.txt)” a call of SetName(“change.tif”_s) will result in “[file:///c:/directory/change.tif](file:///c:/directory/change.tif)”.

**Parameters:** **name** (*str*) – The new name.

### `UrlInterface.SetPath(path, convertWindowsBackslashes=True)` <a id="maxon.UrlInterface.SetPath"></a>

Replaces the path component of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

The path is stored unchanged with the exception that under Windows all backslashes will be changed into forward slashes unless *convertWindowsBackslashes* is set to False.

**Parameters:**

- **path** (*str*) – The new path.
- **convertWindowsBackslashes** (*bool*) – True to convert backslashes under windows (the default).

### `UrlInterface.SetScheme(scheme)` <a id="maxon.UrlInterface.SetScheme"></a>

Sets the scheme of the Url. Path and authority will stay unchanged.

**Parameters:** **scheme** (*str*) – The new scheme

### `UrlInterface.SetSuffix(suffix)` <a id="maxon.UrlInterface.SetSuffix"></a>

Replaces the suffix of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).  
If the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) had no suffix before a dot will be added together with the suffix string.

> **Note:** If the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) is “[file:///c:/directory/file.txt](file:///c:/directory/file.txt)” a call of SetSuffix(“jpg”_s) will result in “[file:///c:/directory/file.jpg](file:///c:/directory/file.jpg)”.

**Parameters:** **suffix** (*str*) – The new suffix of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) without dot.

### `UrlInterface.SetSystemPath(path)` <a id="maxon.UrlInterface.SetSystemPath"></a>

Stores a system path in a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).  
This call needs to be done after the appropriate scheme has been set.  
If no scheme is set `maxon.URLSCHEME_FILESYSTEM` will be automatically set.  
The system path may be converted to a different internal representation,  
e.g. split into authority and path components.

> **Note:** Under Windows all backslashes will be changed into forward slashes.

**Parameters:** **path** (*str*) – The system path

### `UrlInterface.SetUrl(urlString, enableDefaultFallbackScheme)` <a id="maxon.UrlInterface.SetUrl"></a>

Sets the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).  
The scheme is detected automatically and converted to the canonical lowercase version (as described in rfc3986#3.1).  
If a scheme isn’t found and enableDefaultFallbackScheme is False the function returns an IllegalArgumentError,  
otherwise `maxon.URLSCHEME_FILESYSTEM` will be assumed (or `maxon.URLSCHEME_RELATIVE` if ‘urlString’ starts with no drive letter).  
Please note that Urls only use forward slashes as delimiter,  
backslashes are considered to be a part of names and not a delimiter.  
‘?’ will be considered as the start of `maxon.URLFLAGS.QUERY` parameters.  
Everything behind the ‘?’ will be placed in that property.  
Use url.Get(`maxon.URLFLAGS.QUERY`) to get the query parameters.

**Parameters:**

- **urlString** (*str*) – The new [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) to be set.
- **enableDefaultFallbackScheme** (*bool*) – If False and no scheme is set an error will be returned.
