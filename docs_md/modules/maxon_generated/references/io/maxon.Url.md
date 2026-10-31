<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/references/io/maxon.Url.html -->

# maxon.Url <a id="maxon-url"></a>

## Description <a id="module-maxon.Url"></a><a id="description"></a>

Reference class of [`maxon.UrlInterface`](../../interfaces/io/maxon.UrlInterface.md#module-maxon.UrlInterface).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.UrlInterface`](../../interfaces/io/maxon.UrlInterface.md#module-maxon.UrlInterface)
- [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetBrowseIterator`](#maxon.Url.GetBrowseIterator)(flags) | Returns a dedicated IoBrowseIterator with the browse iterator internally |
| [`GetBrowseRef`](#maxon.Url.GetBrowseRef)() | Returns the pure browse iterator |
| [`GetData`](#maxon.Url.GetData)(idValue[, default]) | Retrieves the data stored at the given url. |
| [`GetHashCode`](#maxon.Url.GetHashCode)() | Return the hashcode of an url. |
| [`IoCopyFile`](#maxon.Url.IoCopyFile)(dest, overwrite, removeReadOnly) | Copies a file to a different location, the path must exist otherwise the function returns an error. |
| [`IoCreateDirectory`](#maxon.Url.IoCreateDirectory)(createParents[, createdDirs]) | Creates a new directory. |
| [`IoDelete`](#maxon.Url.IoDelete)(force[, recursive]) | Deletes a file or directory physically on the medium. |
| [`IoDetect`](#maxon.Url.IoDetect)() | Detects the type of the object behind [`maxon.Url`](#module-maxon.Url). |
| [`IoGetAttributes`](#maxon.Url.IoGetAttributes)() | Returns the file attributes of the object behind [`maxon.Url`](#module-maxon.Url). |
| [`IoGetTime`](#maxon.Url.IoGetTime)(mode) | Returns the `maxon.DateTime` of the current file. |
| [`IoMove`](#maxon.Url.IoMove)(destName) | Moves a file or directory (including hierarchy) to a different location, the path must exist otherwise |
| [`IoNormalize`](#maxon.Url.IoNormalize)(self[, flags]) | Returns a normalized [`maxon.Url`](#module-maxon.Url). |
| [`IoRename`](#maxon.Url.IoRename)(newName) | Renames a file or directory. |
| [`Normalize`](#maxon.Url.Normalize)(self[, flags]) | Returns a normalized [`maxon.Url`](#module-maxon.Url). Does not involve any Io operation and is just syntax based. |
| [`OpenConnection`](#maxon.Url.OpenConnection)() | Returns a reference to a [`maxon.IoConnectionInterface`](../../interfaces/io/maxon.IoConnectionInterface.md#module-maxon.IoConnectionInterface) class of this [`maxon.Url`](#module-maxon.Url). |
| [`OpenInOutputStream`](#maxon.Url.OpenInOutputStream)([flags]) | Returns a reference to a [`maxon.InOutputStreamInterface`](../../interfaces/io/maxon.InOutputStreamInterface.md#module-maxon.InOutputStreamInterface) class of this [`maxon.Url`](#module-maxon.Url). |
| [`OpenInputStream`](#maxon.Url.OpenInputStream)([flags]) | Returns a reference to a [`maxon.InputStreamInterface`](../../interfaces/io/maxon.InputStreamInterface.md#module-maxon.InputStreamInterface) class of this [`maxon.Url`](#module-maxon.Url). |
| [`OpenOutputStream`](#maxon.Url.OpenOutputStream)([flags]) | Returns a reference to a [`maxon.OutputStreamInterface`](../../interfaces/io/maxon.OutputStreamInterface.md#module-maxon.OutputStreamInterface) class of this [`maxon.Url`](#module-maxon.Url). |
| [`__add__`](#maxon.Url.__add__)(s) | Appends a relative string or a [`maxon.Url`](#module-maxon.Url) to the current one. |
| [`__hash__`](#maxon.Url.__hash__)() | Returns the hash code of an Url. |
| [`__init__`](#maxon.Url.__init__)([urlOrScheme, scheme, authority, …]) | Creates and stores internally the reference of the C++ Data. |
| [`__radd__`](#maxon.Url.__radd__)(s) | Appends a relative string or a [`maxon.Url`](#module-maxon.Url) to the current one. |
| [`__str__`](#maxon.Url.__str__)() | Returns the string representation of an Url using the StringInterface.ToString method. |

## Methods Definition <a id="methods-definition"></a>

### `Url.GetBrowseIterator(flags)` <a id="maxon.Url.GetBrowseIterator"></a>

Returns a dedicated IoBrowseIterator with the browse iterator internally

### `Url.GetBrowseRef()` <a id="maxon.Url.GetBrowseRef"></a>

Returns the pure browse iterator

### `Url.GetData(idValue, default=None)` <a id="maxon.Url.GetData"></a>

Retrieves the data stored at the given url.

**Parameters:**

- **idValue** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The id where to find the data.
- **default** (*Any*) – The default value if the data is not found

**Returns:**

### `Url.GetHashCode()` <a id="maxon.Url.GetHashCode"></a>

Return the hashcode of an url.

**Returns:** The hashcode.

**Return type:** int

### `Url.IoCopyFile(dest, overwrite, removeReadOnly)` <a id="maxon.Url.IoCopyFile"></a>

Copies a file to a different location, the path must exist otherwise the function returns an error.

**Parameters:**

- **dest** ([`maxon.Url`](#module-maxon.Url)) – Destination name for the copy operation.
- **overwrite** (*bool*) – Set to **True** to allow overwriting destName file if it was already there.
- **removeReadOnly** (*bool*) – Set to **True** to remove the read only flag on the newly created copy.

### `Url.IoCreateDirectory(createParents, createdDirs=None)` <a id="maxon.Url.IoCreateDirectory"></a>

Creates a new directory. The function will return false if the directory already exists.

**Parameters:**

- **createParents** (*bool*) – Check if parent directory exists and if not create them recursively.

- **createdDirs** ([`maxon.BaseArray`](../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.Url`](#module-maxon.Url)]) –

  An array that will contain all newly created subdirectories in the order in which they were created.  
  If this parameter is **None** it will be ignored.

**Returns:**

### `Url.IoDelete(force, recursive=False)` <a id="maxon.Url.IoDelete"></a>

Deletes a file or directory physically on the medium.

**Parameters:**

- **force** (*bool*) – Set to **True** tries to deletes the file/directory even if the file/directory has read only flags set.
- **recursive** (*bool*) – Recursively deletes a directory and its content. If a file is specified this value is ignored.

### `Url.IoDetect()` <a id="maxon.Url.IoDetect"></a>

Detects the type of the object behind [`maxon.Url`](#module-maxon.Url). This allows to check if a file or directory exists.

**Returns:** IODETECT of the given [`maxon.Url`](#module-maxon.Url).

**Return type:**

`maxon.IODETECT`

### `Url.IoGetAttributes()` <a id="maxon.Url.IoGetAttributes"></a>

Returns the file attributes of the object behind [`maxon.Url`](#module-maxon.Url).

**Returns:** The file attribute.

**Return type:**

`maxon.IOATTRIBUTES`

### `Url.IoGetTime(mode)` <a id="maxon.Url.IoGetTime"></a>

Returns the `maxon.DateTime` of the current file. The time is in local time.

**Parameters:** **mode** (`maxon.IOTIMEMODE`) – IOTIMEMODE of the requested time.

**Returns:** Returns the DateTime or an error.

**Return type:** [`maxon.UniversalDateTime`](../../datatypes/time/maxon.UniversalDateTime.md#module-maxon.UniversalDateTime)

### `Url.IoMove(destName)` <a id="maxon.Url.IoMove"></a>

Moves a file or directory (including hierarchy) to a different location, the path must exist otherwise the function returns an error.  
If the destName file or directory does already exist the function returns with an error.  
Moving a file or directory on the same partition will perform without a temporary copy.

**Parameters:** **destName** ([`maxon.Url`](#module-maxon.Url)) – Destination name for the move operation.

### `Url.IoNormalize(self, flags=enums.NORMALIZEFLAGS.SCHEME_BASED)` <a id="maxon.Url.IoNormalize"></a>

Returns a normalized [`maxon.Url`](#module-maxon.Url). If the normalized [`maxon.Url`](#module-maxon.Url) is a link, the [`maxon.IoHandler`](maxon.IoHandler.md#module-maxon.IoHandler) can resolve it (if supported).

> **Note:** The [file:///](file:///) handler resolves symbolic links, where the [http://](http://) handler does not resolve links.

**Parameters:** **flags** (`maxon.NORMALIZEFLAGS`) – Flags to define type of normalization.

**Returns:** The normalized [`maxon.Url`](#module-maxon.Url).

**Return type:** [`maxon.Url`](#module-maxon.Url)

### `Url.IoRename(newName)` <a id="maxon.Url.IoRename"></a>

Renames a file or directory. The newName must not be the name of an existing file or directory.

**Parameters:** **newName** ([`maxon.Url`](#module-maxon.Url)) – New name for the rename operation.

### `Url.Normalize(self, flags=enums.NORMALIZEFLAGS.SCHEME_BASED)` <a id="maxon.Url.Normalize"></a>

**Returns a normalized [`maxon.Url`](#module-maxon.Url). Does not involve any Io operation and is just syntax based.** If nothing needs to be normalized the same path is returned.

**Parameters:** **flags** (`maxon.NORMALIZEFLAGS`) – Flags to define type of normalization.

**Returns:** The normalized [`maxon.Url`](#module-maxon.Url).

**Return type:** [`maxon.Url`](#module-maxon.Url)

### `Url.OpenConnection()` <a id="maxon.Url.OpenConnection"></a>

Returns a reference to a [`maxon.IoConnectionInterface`](../../interfaces/io/maxon.IoConnectionInterface.md#module-maxon.IoConnectionInterface) class of this [`maxon.Url`](#module-maxon.Url).

**Returns:** The pointer to the [`maxon.IoConnectionInterface`](../../interfaces/io/maxon.IoConnectionInterface.md#module-maxon.IoConnectionInterface). Can be **None**.

**Return type:** [`maxon.IoConnectionRef`](maxon.IoConnectionRef.md#module-maxon.IoConnectionRef)

### `Url.OpenInOutputStream(flags=0)` <a id="maxon.Url.OpenInOutputStream"></a>

Returns a reference to a [`maxon.InOutputStreamInterface`](../../interfaces/io/maxon.InOutputStreamInterface.md#module-maxon.InOutputStreamInterface) class of this [`maxon.Url`](#module-maxon.Url).

**Parameters:** **flags** (*See OPENSTREAMFLAGS for details.*) – `maxon.OPENSTREAMFLAGS`

**Returns:** The reference to the [`maxon.InOutputStreamInterface`](../../interfaces/io/maxon.InOutputStreamInterface.md#module-maxon.InOutputStreamInterface). Can be **None**.

**Return type:** [`maxon.InOutputStreamRef`](maxon.InOutputStreamRef.md#module-maxon.InOutputStreamRef)

### `Url.OpenInputStream(flags=0)` <a id="maxon.Url.OpenInputStream"></a>

Returns a reference to a [`maxon.InputStreamInterface`](../../interfaces/io/maxon.InputStreamInterface.md#module-maxon.InputStreamInterface) class of this [`maxon.Url`](#module-maxon.Url).

**Parameters:** **flags** (*See OPENSTREAMFLAGS for details.*) – `maxon.OPENSTREAMFLAGS`

**Returns:** The reference to the [`maxon.InputStreamInterface`](../../interfaces/io/maxon.InputStreamInterface.md#module-maxon.InputStreamInterface). Can be **None**.

**Return type:** [`maxon.InputStreamRef`](maxon.InputStreamRef.md#module-maxon.InputStreamRef)

### `Url.OpenOutputStream(flags=0)` <a id="maxon.Url.OpenOutputStream"></a>

Returns a reference to a [`maxon.OutputStreamInterface`](../../interfaces/io/maxon.OutputStreamInterface.md#module-maxon.OutputStreamInterface) class of this [`maxon.Url`](#module-maxon.Url).

**Parameters:** **flags** (*See OPENSTREAMFLAGS for details.*) – `maxon.OPENSTREAMFLAGS`

**Returns:** The reference to the [`maxon.OutputStreamInterface`](../../interfaces/io/maxon.OutputStreamInterface.md#module-maxon.OutputStreamInterface). Can be **None**.

**Return type:** [`maxon.OutputStreamRef`](maxon.OutputStreamRef.md#module-maxon.OutputStreamRef)

### `Url.__add__(s)` <a id="maxon.Url.__add__"></a>

Appends a relative string or a [`maxon.Url`](#module-maxon.Url) to the current one.

> **Note:** If the Url is *file:///c:/directory* a call of
>
> ```python
> url.Append(maxon.Url("test/file.txt"))
> ```
>
> will result in *file:///c:/directory/test/file.txt*.

**Parameters:** **s** (Union[str, [`maxon.Url`](#module-maxon.Url)]) – String or [`maxon.Url`](#module-maxon.Url) to add to the current url.

### `Url.__hash__()` <a id="maxon.Url.__hash__"></a>

Returns the hash code of an Url.

### `Url.__init__(urlOrScheme=None, scheme=None, authority=None, path=None, name=None)` <a id="maxon.Url.__init__"></a>

Creates and stores internally the reference of the C++ Data.  
When the passed data is None, an empty data is still allocated.

**Parameters:** **data** (*Optional*[*Data*]) – An optional c++ data used to hold the C++ reference alive during the whole lifetime of this python object.

### `Url.__radd__(s)` <a id="maxon.Url.__radd__"></a>

Appends a relative string or a [`maxon.Url`](#module-maxon.Url) to the current one.

> **Note:** If the Url is *file:///c:/directory* a call of
>
> ```python
> url.Append(maxon.Url("test/file.txt"))
> ```
>
> will result in *file:///c:/directory/test/file.txt*.

**Parameters:** **s** (Union[str, [`maxon.Url`](#module-maxon.Url)]) – String or [`maxon.Url`](#module-maxon.Url) to add to the current url.

### `Url.__str__()` <a id="maxon.Url.__str__"></a>

Returns the string representation of an Url using the StringInterface.ToString method.

**Return type:** str
