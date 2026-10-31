<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/io/maxon.BaseStreamInterface.html -->

# maxon.BaseStreamInterface <a id="maxon-basestreaminterface"></a>

## Description <a id="module-maxon.BaseStreamInterface"></a><a id="description"></a>

Interface is the base interface for all stream interfaces.  
It contains the general functions to work with streams (e.g. error handling).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.DataDictionaryObjectInterface`](../core/maxon.DataDictionaryObjectInterface.md#module-maxon.DataDictionaryObjectInterface)

Children Classes:

- [`maxon.InputStreamInterface`](maxon.InputStreamInterface.md#module-maxon.InputStreamInterface)
- [`maxon.OutputStreamInterface`](maxon.OutputStreamInterface.md#module-maxon.OutputStreamInterface)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.BaseStreamInterface.softspace`](maxon.BaseStreamInterface.softspace.md#maxon.BaseStreamInterface.softspace) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Close`](#maxon.BaseStreamInterface.Close)() | Closes the stream. |
| [`DisableBuffering`](#maxon.BaseStreamInterface.DisableBuffering)() | The stream may disable buffering when this routine is called (if it supports it). |
| [`GetPosition`](#maxon.BaseStreamInterface.GetPosition)() | Returns the current stream position. |
| [`GetStreamLength`](#maxon.BaseStreamInterface.GetStreamLength)() | Returns the length of the stream/file. |
| [`Seek`](#maxon.BaseStreamInterface.Seek)(position) | Sets the read/write position to this absolute position from the beginning of the stream. |
| [`SeekSupported`](#maxon.BaseStreamInterface.SeekSupported)() | Returns if the stream supports `BaseStreamInterface.Seek()`. |
| [`__enter__`](#maxon.BaseStreamInterface.__enter__)() |  |
| [`__exit__`](#maxon.BaseStreamInterface.__exit__)(exc_type, exc_value, traceback) |  |
| [`close`](#maxon.BaseStreamInterface.close)() |  |
| [`seek`](#maxon.BaseStreamInterface.seek)(offset[, whence]) |  |
| [`seekable`](#maxon.BaseStreamInterface.seekable)() |  |
| [`tell`](#maxon.BaseStreamInterface.tell)() |  |

## Methods Definition <a id="methods-definition"></a>

### `BaseStreamInterface.Close()` <a id="maxon.BaseStreamInterface.Close"></a>

Closes the stream.

### `BaseStreamInterface.DisableBuffering()` <a id="maxon.BaseStreamInterface.DisableBuffering"></a>

The stream may disable buffering when this routine is called (if it supports it).  
This method is typically used when the buffering is done from the outside.

### `BaseStreamInterface.GetPosition()` <a id="maxon.BaseStreamInterface.GetPosition"></a>

Returns the current stream position.  
This is the position where the next bytes will be read to or written from.

**Returns:** The current stream position.

**Return type:** int

### `BaseStreamInterface.GetStreamLength()` <a id="maxon.BaseStreamInterface.GetStreamLength"></a>

Returns the length of the stream/file.  
Be aware that some streams cannot return the file size (e.g. http streams with gzip+chunked transfer encoding).  
With this example code you can handle both cases correctly.  
In most cases it’s better to not use [`maxon.BaseStreamInterface.GetStreamLength()`](#maxon.BaseStreamInterface.GetStreamLength) and better use [`maxon.InputStreamInterface.ReadEOS()`](maxon.InputStreamInterface.md#maxon.InputStreamInterface.ReadEOS) to read as much as available.

**Return type:** Returns the length in bytes.

**Return type:** int

### `BaseStreamInterface.Seek(position)` <a id="maxon.BaseStreamInterface.Seek"></a>

Sets the read/write position to this absolute position from the beginning of the stream.

> **Note:** For [`maxon.InputStreamInterface`](maxon.InputStreamInterface.md#module-maxon.InputStreamInterface): If you want to [`BaseStreamInterface.Seek()`](#maxon.BaseStreamInterface.Seek) forward [`InputStreamInterface.Skip()`](maxon.InputStreamInterface.md#maxon.InputStreamInterface.Skip) is the preferred method to call from the performance perspective.

**Parameters:** **position** (*int*) – Position to jump to within the stream.

### `BaseStreamInterface.SeekSupported()` <a id="maxon.BaseStreamInterface.SeekSupported"></a>

Returns if the stream supports [`BaseStreamInterface.Seek()`](#maxon.BaseStreamInterface.Seek).

> **Note:** Seeking in stream may effect performance because the caches will be flushed.

**Returns:** True if the output stream supports [`BaseStreamInterface.Seek()`](#maxon.BaseStreamInterface.Seek).

**Return type:** bool

### `BaseStreamInterface.__enter__()` <a id="maxon.BaseStreamInterface.__enter__"></a>

### `BaseStreamInterface.__exit__(exc_type, exc_value, traceback)` <a id="maxon.BaseStreamInterface.__exit__"></a>

### `BaseStreamInterface.close()` <a id="maxon.BaseStreamInterface.close"></a>

### `BaseStreamInterface.seek(offset, whence=0)` <a id="maxon.BaseStreamInterface.seek"></a>

### `BaseStreamInterface.seekable()` <a id="maxon.BaseStreamInterface.seekable"></a>

### `BaseStreamInterface.tell()` <a id="maxon.BaseStreamInterface.tell"></a>
