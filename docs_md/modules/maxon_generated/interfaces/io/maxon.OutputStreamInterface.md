<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/io/maxon.OutputStreamInterface.html -->

# maxon.OutputStreamInterface <a id="maxon-outputstreaminterface"></a>

## Description <a id="module-maxon.OutputStreamInterface"></a><a id="description"></a>

Creates an [`maxon.OutputStreamInterface`](#module-maxon.OutputStreamInterface) class to write bytes into streams.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.BaseStreamInterface`](maxon.BaseStreamInterface.md#module-maxon.BaseStreamInterface)

Children Classes:

- [`maxon.InOutputStreamInterface`](maxon.InOutputStreamInterface.md#module-maxon.InOutputStreamInterface)
- [`maxon.OutputStreamRef`](../../references/io/maxon.OutputStreamRef.md#module-maxon.OutputStreamRef)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.OutputStreamInterface.softspace`](maxon.OutputStreamInterface.softspace.md#maxon.OutputStreamInterface.softspace) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Flush`](#maxon.OutputStreamInterface.Flush)() | Flushes the output stream and forces any buffered output bytes to be written. |
| [`Write`](#maxon.OutputStreamInterface.Write)(data) | Write bytes to the stream. |
| [`flush`](#maxon.OutputStreamInterface.flush)() | Flushes the output stream and forces any buffered output bytes to be written. |
| [`write`](#maxon.OutputStreamInterface.write)(data) | Write bytes to the stream. |

## Methods Definition <a id="methods-definition"></a>

### `OutputStreamInterface.Flush()` <a id="maxon.OutputStreamInterface.Flush"></a>

Flushes the output stream and forces any buffered output bytes to be written.

### `OutputStreamInterface.Write(data)` <a id="maxon.OutputStreamInterface.Write"></a>

Write bytes to the stream. ‘bytes’ is of type Int (not Int64) as ‘buffer’ can never hold more bytes on a 32-bit system.

**Parameters:** **data** (Union[bytes, bytearray, memoryview, [`maxon.BaseArray`](../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray), [`maxon.Block`](../../datatypes/collection/maxon.Block.md#module-maxon.Block)]) – Data that should be written to the stream.

### `OutputStreamInterface.flush()` <a id="maxon.OutputStreamInterface.flush"></a>

Flushes the output stream and forces any buffered output bytes to be written.

### `OutputStreamInterface.write(data)` <a id="maxon.OutputStreamInterface.write"></a>

Write bytes to the stream. ‘bytes’ is of type Int (not Int64) as ‘buffer’ can never hold more bytes on a 32-bit system.

**Parameters:** **data** ([`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data) that should be written to the stream.
