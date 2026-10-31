<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.storage/MemoryFileStruct/index.html -->

# c4d.storage.MemoryFileStruct <a id="c4d-storage-memoryfilestruct"></a>

## *class* `c4d.storage.MemoryFileStruct` <a id="c4d.storage.MemoryFileStruct"></a>

This class is used to write to memory instead of to a file.

## Overview <a id="overview"></a>

**Magic Methods**

- [`MemoryFileStruct.__init__()`](#c4d.storage.MemoryFileStruct.__init__)

**Memory Buffer Operations**

- [`MemoryFileStruct.GetData()`](#c4d.storage.MemoryFileStruct.GetData): Retrieves all data written to the memory file.
- [`MemoryFileStruct.SetMemoryReadMode()`](#c4d.storage.MemoryFileStruct.SetMemoryReadMode): Sets the buffer read from a memory block instead of from a file.
- [`MemoryFileStruct.SetMemoryWriteMode()`](#c4d.storage.MemoryFileStruct.SetMemoryWriteMode): Sets the buffer ready to be written to.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.storage.MemoryFileStruct-method-Magic-Methods"></a>

#### `MemoryFileStruct.__init__(self)` <a id="c4d.storage.MemoryFileStruct.__init__"></a>

### Memory Buffer Operations <a id="c4d.storage.MemoryFileStruct-method-Memory-Buffer-Operations"></a>

#### `MemoryFileStruct.GetData(self)` <a id="c4d.storage.MemoryFileStruct.GetData"></a>

Retrieves all data written to the memory file.

**Return type:** Tuple[bytearray, int]

**Returns:** A tuple with the buffer data and size.

#### `MemoryFileStruct.SetMemoryReadMode(self, adr, size)` <a id="c4d.storage.MemoryFileStruct.SetMemoryReadMode"></a>

Sets the buffer read from a memory block instead of from a file.

**Parameters:**

- **adr** (*Union*[*bytearray*, *memoryview*]) – The memory address to read from.
- **size** (*int*) – The size of the memory block, or -1 if the buffer is “big enough”.

#### `MemoryFileStruct.SetMemoryWriteMode(self)` <a id="c4d.storage.MemoryFileStruct.SetMemoryWriteMode"></a>

Sets the buffer ready to be written to.
