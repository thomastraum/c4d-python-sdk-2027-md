<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/io/maxon.InputStreamInterface.html -->

# maxon.InputStreamInterface <a id="maxon-inputstreaminterface"></a>

## Description <a id="module-maxon.InputStreamInterface"></a><a id="description"></a>

Interface for input streams. It allows to read data from streams.  
This interface needs to be implemented for each protocol.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.BaseStreamInterface`](maxon.BaseStreamInterface.md#module-maxon.BaseStreamInterface)

Children Classes:

- [`maxon.InOutputStreamInterface`](maxon.InOutputStreamInterface.md#module-maxon.InOutputStreamInterface)
- [`maxon.InputStreamRef`](../../references/io/maxon.InputStreamRef.md#module-maxon.InputStreamRef)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.InputStreamInterface.FromBlock`](maxon.InputStreamInterface.FromBlock.md#maxon.InputStreamInterface.FromBlock) |  |
| [`maxon.InputStreamInterface.softspace`](maxon.InputStreamInterface.softspace.md#maxon.InputStreamInterface.softspace) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`BytesAvailable`](#maxon.InputStreamInterface.BytesAvailable)() | Returns an estimate of the number of bytes that can be read (or skipped over) from this input stream without blocking by the next invocation of a method for this input stream. |
| [`Read`](#maxon.InputStreamInterface.Read)([len, chunk]) | Reads all bytes up to len bytes of data from the input stream into an array of bytes. |
| [`ReadEOS`](#maxon.InputStreamInterface.ReadEOS)(data) | Reads up to len bytes of data from the input stream into an array of bytes. |
| [`Skip`](#maxon.InputStreamInterface.Skip)(bytes) | Skips over and discards n bytes of data from this input stream. |
| [`read`](#maxon.InputStreamInterface.read)([n]) |  |

## Methods Definition <a id="methods-definition"></a>

### `InputStreamInterface.BytesAvailable()` <a id="maxon.InputStreamInterface.BytesAvailable"></a>

Returns an estimate of the number of bytes that can be read (or skipped over) from this input stream without blocking by the next invocation of a method for this input stream.

**Returns:** Available number of bytes to read/skip.

**Return type:** int

### `InputStreamInterface.Read(len=None, chunk=8192)` <a id="maxon.InputStreamInterface.Read"></a>

Reads all bytes up to len bytes of data from the input stream into an array of bytes. ‘bytes’ and the result are of type Int (not Int64) as ‘buffer’ can never hold more bytes on a 32-bit system.

**Parameters:**

- **len** (*int*) – size of buffer to read.
- **chunk** – The type of the data to read

**Returns:** The buffer with the data.

**Return type:** bytes

### `InputStreamInterface.ReadEOS(data)` <a id="maxon.InputStreamInterface.ReadEOS"></a>

Reads up to len bytes of data from the input stream into an array of bytes. ‘bytes’ and the result are of type Int (not Int64) as ‘buffer’ can never hold more bytes on a 32-bit system.

**Parameters:** **data** ([`maxon.Block`](../../datatypes/collection/maxon.Block.md#module-maxon.Block)) – Buffer which receives the read bytes.

**Returns:**

Number of bytes that has been read. If less bytes read than requested the end of

the stream has been reached.

**Return type:** int

### `InputStreamInterface.Skip(bytes)` <a id="maxon.InputStreamInterface.Skip"></a>

Skips over and discards n bytes of data from this input stream.  
If you want to [`BaseStreamInterface.Seek()`](maxon.BaseStreamInterface.md#maxon.BaseStreamInterface.Seek) forward [`InputStreamInterface.Skip()`](#maxon.InputStreamInterface.Skip) is the preferred method to call from the performance perspective.

**Parameters:** **bytes** (*bytes*) – Number of bytes to skip from the current position.

### `InputStreamInterface.read(n=- 1)` <a id="maxon.InputStreamInterface.read"></a>
