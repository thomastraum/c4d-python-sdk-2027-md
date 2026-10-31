<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/io/maxon.IoConnectionInterface.html -->

# maxon.IoConnectionInterface <a id="maxon-ioconnectioninterface"></a>

## Description <a id="module-maxon.IoConnectionInterface"></a><a id="description"></a>

The connection interface a given [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).  
This connection needs to be implemented for each protocol.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.DataDictionaryObjectInterface`](../core/maxon.DataDictionaryObjectInterface.md#module-maxon.DataDictionaryObjectInterface)

Child Class:

- [`maxon.IoConnectionRef`](../../references/io/maxon.IoConnectionRef.md#module-maxon.IoConnectionRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetBrowseIterator`](#maxon.IoConnectionInterface.GetBrowseIterator)(flags) | Returns a [`maxon.IoBrowseInterface`](maxon.IoBrowseInterface.md#module-maxon.IoBrowseInterface) class to browse through all children of an Url. |
| [`GetContentLength`](#maxon.IoConnectionInterface.GetContentLength)() | Returns length of the content. |
| [`GetUrl`](#maxon.IoConnectionInterface.GetUrl)() | Returns the corresponding [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) connected to the [`maxon.IoConnectionRef`](../../references/io/maxon.IoConnectionRef.md#module-maxon.IoConnectionRef). |
| [`IoCopyFile`](#maxon.IoConnectionInterface.IoCopyFile)(destName, overwrite, removeReadOnly) | Copies a file to a different location, the path must exist otherwise the function returns an error. |
| [`IoCreateDirectory`](#maxon.IoConnectionInterface.IoCreateDirectory)(createParents[, createDirs]) | Creates a new directory. |
| [`IoDelete`](#maxon.IoConnectionInterface.IoDelete)(force) | Deletes the file physically on the medium. |
| [`IoDetect`](#maxon.IoConnectionInterface.IoDetect)() | Detects the type of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`IoGetAttributes`](#maxon.IoConnectionInterface.IoGetAttributes)() | Returns the file attributes. |
| [`IoGetFreeVolumeSpace`](#maxon.IoConnectionInterface.IoGetFreeVolumeSpace)() | Calculates the free space on a volume. |
| [`IoGetTime`](#maxon.IoConnectionInterface.IoGetTime)(mode) | Returns the `maxon.DateTime` of the current file. |
| [`IoMove`](#maxon.IoConnectionInterface.IoMove)(destName) | Moves a file or directory (including hierarchy) to a different location. |
| [`IoRename`](#maxon.IoConnectionInterface.IoRename)(newName) | Renames a file or directory. |
| [`IoSetAttributes`](#maxon.IoConnectionInterface.IoSetAttributes)(flags, mask) | Modify the file attributes. |
| [`IoSetTime`](#maxon.IoConnectionInterface.IoSetTime)(mode, dateTime) | Modifies the `maxon.DateTime` of the current file. |
| [`IoShowInOS`](#maxon.IoConnectionInterface.IoShowInOS)(flags) | Opens or shows the file in the systems explorer (desktop/finder). |
| [`OpenInOutputStream`](#maxon.IoConnectionInterface.OpenInOutputStream)(self[, flags]) | Opens an [`maxon.InOutputStreamRef`](../../references/io/maxon.InOutputStreamRef.md#module-maxon.InOutputStreamRef) for the given connection. |
| [`OpenInputStream`](#maxon.IoConnectionInterface.OpenInputStream)(self[, flags]) | Opens an [`maxon.InputStreamRef`](../../references/io/maxon.InputStreamRef.md#module-maxon.InputStreamRef) for the given connection. |
| [`OpenOutputStream`](#maxon.IoConnectionInterface.OpenOutputStream)(self[, flags]) | Opens an [`maxon.OutputStreamRef`](../../references/io/maxon.OutputStreamRef.md#module-maxon.OutputStreamRef) for the given connection. |

## Methods Definition <a id="methods-definition"></a>

### `IoConnectionInterface.GetBrowseIterator(flags)` <a id="maxon.IoConnectionInterface.GetBrowseIterator"></a>

Returns a [`maxon.IoBrowseInterface`](maxon.IoBrowseInterface.md#module-maxon.IoBrowseInterface) class to browse through all children of an Url.  
The return value needs to be checked against None.

**Parameters:** **flags** (`maxon.GETBROWSEITERATORFLAGS`) – Defines how the iterator resolve data.

**Returns:** The iterator.

**Return type:** [`maxon.IoBrowseInterface`](maxon.IoBrowseInterface.md#module-maxon.IoBrowseInterface)

### `IoConnectionInterface.GetContentLength()` <a id="maxon.IoConnectionInterface.GetContentLength"></a>

Returns length of the content.

**Returns:** The effective size in bytes of the [`maxon.IoConnectionInterface`](#module-maxon.IoConnectionInterface) (e.g. filesize).

**Return type:** int

### `IoConnectionInterface.GetUrl()` <a id="maxon.IoConnectionInterface.GetUrl"></a>

Returns the corresponding [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) connected to the [`maxon.IoConnectionRef`](../../references/io/maxon.IoConnectionRef.md#module-maxon.IoConnectionRef). :return: Returns the name of the connection. :rtype: [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

### `IoConnectionInterface.IoCopyFile(destName, overwrite, removeReadOnly)` <a id="maxon.IoConnectionInterface.IoCopyFile"></a>

Copies a file to a different location, the path must exist otherwise the function returns an error.

**Parameters:**

- **destName** ([`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)) – Destination name for the copy operation.
- **overwrite** (*bool*) – True to allow overwriting destName file if it was already there.
- **removeReadOnly** (*bool*) – True to remove the read only flag on the newly created copy.

### `IoConnectionInterface.IoCreateDirectory(createParents, createDirs=None)` <a id="maxon.IoConnectionInterface.IoCreateDirectory"></a>

Creates a new directory.

> **Note:** The function returns false if the directory already exists.

**Parameters:**

- **createParents** (*bool*) – Check if parent directory exists and if not create them recursively.

- **createDirs** ([`maxon.BaseArray`](../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)]) –

  An array that will contain all newly created subdirectories in the order in which they were created.  
  If this parameter is None it will be ignored.

### `IoConnectionInterface.IoDelete(force)` <a id="maxon.IoConnectionInterface.IoDelete"></a>

Deletes the file physically on the medium.

**Parameters:** **force** – True tries to deletes the file/directory even if the file/directory has read only flags set.

**Returns:** True if the file/directory could be removed successfully.

**Return type:** bool

### `IoConnectionInterface.IoDetect()` <a id="maxon.IoConnectionInterface.IoDetect"></a>

Detects the type of the [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).  
This allows to check if a file or directory exists.

**Returns:** Flags defining the detection state.

**Return type:**

`maxon.IODETECT`

### `IoConnectionInterface.IoGetAttributes()` <a id="maxon.IoConnectionInterface.IoGetAttributes"></a>

Returns the file attributes.

**Returns:** IOATTRIBUTES of the files.

**Return type:**

`maxon.IOATTRIBUTES`

### `IoConnectionInterface.IoGetFreeVolumeSpace()` <a id="maxon.IoConnectionInterface.IoGetFreeVolumeSpace"></a>

Calculates the free space on a volume.

> **Note:** The [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) can point to a volume or directory.

**Returns:**

In the next order:

1. The number of available bytes on the volume.
2. The total size of the volume in bytes.

**Return type:** tuple(int, int)

### `IoConnectionInterface.IoGetTime(mode)` <a id="maxon.IoConnectionInterface.IoGetTime"></a>

Returns the `maxon.DateTime` of the current file.  
The time is in local time.

**Parameters:** **mode** (`maxon.IOTIMEMODE`) – IOTIMEMODE of the requested time.

**Returns:** Returns the `maxon.DateTime` or an error.

**Return type:** [`maxon.UniversalDateTime`](../../datatypes/time/maxon.UniversalDateTime.md#module-maxon.UniversalDateTime)

### `IoConnectionInterface.IoMove(destName)` <a id="maxon.IoConnectionInterface.IoMove"></a>

Moves a file or directory (including hierarchy) to a different location.  
The path must exist otherwise the function returns an error.  
If the destName file or directory does already exist the function returns with an error.  
Moving a file or directory on the same partition will perform without a temporary copy.

**Parameters:** **destName** ([`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)) – Destination name for the move operation.

### `IoConnectionInterface.IoRename(newName)` <a id="maxon.IoConnectionInterface.IoRename"></a>

Renames a file or directory.

> **Warning:** The newName must not be the name of an existing file or directory.

**Parameters:**

- **newName** – New name for the rename operation.
- **newName** – [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

**Returns:**

### `IoConnectionInterface.IoSetAttributes(flags, mask)` <a id="maxon.IoConnectionInterface.IoSetAttributes"></a>

Modify the file attributes.

**Parameters:**

- **flags** – Flags to set/clear.
- **flags** – `maxon.IOATTRIBUTES`
- **mask** – Mask with all flags to be changed.
- **mask** – `maxon.IOATTRIBUTES`

### `IoConnectionInterface.IoSetTime(mode, dateTime)` <a id="maxon.IoConnectionInterface.IoSetTime"></a>

Modifies the `maxon.DateTime` of the current file. the time is in local time.

**Parameters:**

- **mode** (`maxon.IOTIMEMODE`) – IOTIMEMODE of the requested time.
- **dateTime** ([`maxon.UniversalDateTime`](../../datatypes/time/maxon.UniversalDateTime.md#module-maxon.UniversalDateTime)) – New datetime for the file.

### `IoConnectionInterface.IoShowInOS(flags)` <a id="maxon.IoConnectionInterface.IoShowInOS"></a>

Opens or shows the file in the systems explorer (desktop/finder).  
Under windows that would be on the desktop/explorer.  
Under OSX this would be the Finder.  
Depending on the url scheme this could also open another browser.

**Parameters:** **flags** (`maxon.IOSHOWINOSFLAGS`) – Flags to define how to show/open that file.

### `IoConnectionInterface.OpenInOutputStream(self, flags=enums.OPENSTREAMFLAGS.NONE)` <a id="maxon.IoConnectionInterface.OpenInOutputStream"></a>

Opens an [`maxon.InOutputStreamRef`](../../references/io/maxon.InOutputStreamRef.md#module-maxon.InOutputStreamRef) for the given connection.  
With this kind of streams it’s possible to read/write to it.

**Parameters:** **flags** (`maxon.OPENSTREAMFLAGS`) – Defines how the stream will be handled.

**Returns:** An input stream, should be free with `ObjectInterface.Free()`.

**Return type:** [`maxon.InOutputStreamRef`](../../references/io/maxon.InOutputStreamRef.md#module-maxon.InOutputStreamRef)

### `IoConnectionInterface.OpenInputStream(self, flags=enums.OPENSTREAMFLAGS.NONE)` <a id="maxon.IoConnectionInterface.OpenInputStream"></a>

Opens an [`maxon.InputStreamRef`](../../references/io/maxon.InputStreamRef.md#module-maxon.InputStreamRef) for the given connection.  
With this kind of streams it’s only possible to read from it.

**Parameters:** **flags** (`maxon.OPENSTREAMFLAGS`) – Defines how the stream will be handled.

**Returns:** An input stream, should be free with `ObjectInterface.Free()`.

**Return type:** [`maxon.InputStreamRef`](../../references/io/maxon.InputStreamRef.md#module-maxon.InputStreamRef)

### `IoConnectionInterface.OpenOutputStream(self, flags=enums.OPENSTREAMFLAGS.NONE)` <a id="maxon.IoConnectionInterface.OpenOutputStream"></a>

Opens an [`maxon.OutputStreamRef`](../../references/io/maxon.OutputStreamRef.md#module-maxon.OutputStreamRef) for the given connection.  
With this kind of streams it’s only possible to write to it.

**Parameters:** **flags** (`maxon.OPENSTREAMFLAGS`) – Defines how the stream will be handled.

**Returns:** An input stream, should be free with `ObjectInterface.Free()`.

**Return type:** [`maxon.OutputStreamRef`](../../references/io/maxon.OutputStreamRef.md#module-maxon.OutputStreamRef)
