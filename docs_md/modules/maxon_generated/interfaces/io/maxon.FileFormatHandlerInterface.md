<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/io/maxon.FileFormatHandlerInterface.html -->

# maxon.FileFormatHandlerInterface <a id="maxon-fileformathandlerinterface"></a>

## Description <a id="module-maxon.FileFormatHandlerInterface"></a><a id="description"></a>

FileFormatHandlerInterface implements a handler for a specific FileFormat.

> **Note:**
>
> Two different implementations could offer different loaders for one and the same FileFormat.  
> `maxon.FileFormat.Zip` implements one handler for Directory Browsing ([`maxon.IoBrowseRef`](../../references/io/maxon.IoBrowseRef.md#module-maxon.IoBrowseRef)) and one for `maxon.ReadArchiveRef`.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.FileFormatHandler`](../../references/io/maxon.FileFormatHandler.md#module-maxon.FileFormatHandler)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`CreateHandler`](#maxon.FileFormatHandlerInterface.CreateHandler)(HANDLER, url) | Creates an [`maxon.ObjectRef`](../../references/core_helper/maxon.ObjectRef.md#module-maxon.ObjectRef) which handles the given url with the specific interface. |
| [`GetDependends`](#maxon.FileFormatHandlerInterface.GetDependends)(url) | Returns the dependencies of this [`maxon.FileFormatHandler`](../../references/io/maxon.FileFormatHandler.md#module-maxon.FileFormatHandler). |
| [`GetFileFormat`](#maxon.FileFormatHandlerInterface.GetFileFormat)() | Returns the [`maxon.FileFormat`](../../references/io/maxon.FileFormat.md#module-maxon.FileFormat) which is handled by this [`maxon.FileFormatHandler`](../../references/io/maxon.FileFormatHandler.md#module-maxon.FileFormatHandler). |
| [`GetHandlerType`](#maxon.FileFormatHandlerInterface.GetHandlerType)() | Returns the [`maxon.DataType`](../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType) of the reference class of the handler returned by `FileFormatHandlerInterface.CreateHandler()`. |

## Methods Definition <a id="methods-definition"></a>

### `FileFormatHandlerInterface.CreateHandler(HANDLER, url)` <a id="maxon.FileFormatHandlerInterface.CreateHandler"></a>

Creates an [`maxon.ObjectRef`](../../references/core_helper/maxon.ObjectRef.md#module-maxon.ObjectRef) which handles the given url with the specific interface.

> **Note:**
>
> `maxon.FileFormat.Zip` implements one handler for Directory Browsing “[`maxon.IoBrowseRef`](../../references/io/maxon.IoBrowseRef.md#module-maxon.IoBrowseRef)” and one for workign with archives “`maxon.ReadArchiveRef`”.

**Parameters:**

- **HANDLER** (Union[[`maxon.UrlInterface`](maxon.UrlInterface.md#module-maxon.UrlInterface), [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data), type]) – Reference class to be expected with the result of CreateHandler.
- **url** ([`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)) – [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) to be used with this handler.

**Returns:** Reference class to be expected with the result of CreateHandler.

**Return type:** same as HANDLER

### `FileFormatHandlerInterface.GetDependends(url)` <a id="maxon.FileFormatHandlerInterface.GetDependends"></a>

Returns the dependencies of this [`maxon.FileFormatHandler`](../../references/io/maxon.FileFormatHandler.md#module-maxon.FileFormatHandler).  
This allows to give an priority order for a implementation.

> **Warning:** This function should not be called except from `FileFormatDetectionInterface.DetectAll()`.

**Returns:** Defines the priority order of file formats. The lower the value the later it will be called.

**Return type:**

`maxon.FILEFORMAT_PRIORITY`

### `FileFormatHandlerInterface.GetFileFormat()` <a id="maxon.FileFormatHandlerInterface.GetFileFormat"></a>

Returns the [`maxon.FileFormat`](../../references/io/maxon.FileFormat.md#module-maxon.FileFormat) which is handled by this [`maxon.FileFormatHandler`](../../references/io/maxon.FileFormatHandler.md#module-maxon.FileFormatHandler).

**Returns:** The file format.

**Return type:** [`maxon.FileFormat`](../../references/io/maxon.FileFormat.md#module-maxon.FileFormat)

### `FileFormatHandlerInterface.GetHandlerType()` <a id="maxon.FileFormatHandlerInterface.GetHandlerType"></a>

Returns the [`maxon.DataType`](../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType) of the reference class of the handler returned by [`FileFormatHandlerInterface.CreateHandler()`](#maxon.FileFormatHandlerInterface.CreateHandler).

**Returns:** The data type of the reference class.

**Return type:** [`maxon.DataType`](../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)
