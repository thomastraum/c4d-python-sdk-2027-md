<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.storage/HyperFile/index.html -->

# c4d.storage.HyperFile <a id="c4d-storage-hyperfile"></a>

## *class* `c4d.storage.HyperFile` <a id="c4d.storage.HyperFile"></a>

Hyper files are used to store data in a file.  
The HyperFile works with the ‘FIFO’ concept.  
The values will be written and read in the same order.  
The following source code is a simple example showing how to use the [`HyperFile`](#c4d.storage.HyperFile) class.

```python
import c4d, os
YOUR_IDENT = 49545 # Choose a custom ident
path = os.path.join("/Users", "Dev", "Desktop", "test.file")
print(path)

def Write(path, key):
    #write
    print(path)
    hf = c4d.storage.HyperFile()
    if hf.Open(ident=key, filename=path, mode=c4d.FILEOPEN_WRITE, error_dialog=c4d.FILEDIALOG_NONE):
        bc = c4d.BaseContainer()
        bc[0] = "test"
        bc[1] = "3"
        hf.WriteContainer(bc)
        hf.Close()
    else:
        c4d.gui.MessageDialog("Cannot open file to write.")

def Read(path, key):
    #read
    hf = c4d.storage.HyperFile()
    if hf.Open(ident=key, filename=path, mode=c4d.FILEOPEN_READ, error_dialog=c4d.FILEDIALOG_NONE):
        bc = hf.ReadContainer()
        hf.Close()
        print(bc[0], bc[1]) #output: test 3
    else:
        c4d.gui.MessageDialog("Cannot open file to read.")

Write(path, YOUR_IDENT)
Read(path, YOUR_IDENT)
```

## Overview <a id="overview"></a>

**Chunk Reading**

- [`HyperFile.ReadChunkEnd()`](#c4d.storage.HyperFile.ReadChunkEnd): Read a chunks end marker from the file.
- [`HyperFile.ReadChunkStart()`](#c4d.storage.HyperFile.ReadChunkStart): Read a chunks identification from the file.
- [`HyperFile.SkipToEndChunk()`](#c4d.storage.HyperFile.SkipToEndChunk): Move the file pointer to the end of the chunk.

**Chunk Writing**

- [`HyperFile.WriteChunkEnd()`](#c4d.storage.HyperFile.WriteChunkEnd): Write a chunk ending marker into the file.
- [`HyperFile.WriteChunkStart()`](#c4d.storage.HyperFile.WriteChunkStart): Write a chunk marker into the file indicating the beginning of a new chunk of data.

**Error Handling**

- [`HyperFile.GetError()`](#c4d.storage.HyperFile.GetError): Get the error from the last hyperfile operation.
- [`HyperFile.SetError()`](#c4d.storage.HyperFile.SetError): Set the error value for this hyperfile.

**File Context**

- [`HyperFile.GetDocument()`](#c4d.storage.HyperFile.GetDocument): Gets the active document for the hyper file operation.
- [`HyperFile.GetFileVersion()`](#c4d.storage.HyperFile.GetFileVersion): Get the version of Cinema 4D that wrote the file.
- [`HyperFile.GetFilterFlags()`](#c4d.storage.HyperFile.GetFilterFlags): Gets the filter flags, the value is valid only during a Load or a Merge.

**File Lifecycle**

- [`HyperFile.Close()`](#c4d.storage.HyperFile.Close): Closes the hyper file.
- [`HyperFile.Open()`](#c4d.storage.HyperFile.Open): Opens the hyper file.

**Geometric Reading**

- [`HyperFile.ReadMatrix()`](#c4d.storage.HyperFile.ReadMatrix): Read a [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) from the hyperfile.
- [`HyperFile.ReadMatrix32()`](#c4d.storage.HyperFile.ReadMatrix32): Read a [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) from the hyperfile.
- [`HyperFile.ReadMatrix64()`](#c4d.storage.HyperFile.ReadMatrix64): Read a double precision [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) from the hyperfile.
- [`HyperFile.ReadVector()`](#c4d.storage.HyperFile.ReadVector): Read a [`Vector`](../../c4d/Vector/index.md#c4d.Vector) from the hyperfile.
- [`HyperFile.ReadVector32()`](#c4d.storage.HyperFile.ReadVector32): Read a [`Vector`](../../c4d/Vector/index.md#c4d.Vector) from the hyperfile.
- [`HyperFile.ReadVector64()`](#c4d.storage.HyperFile.ReadVector64): Read a double precision [`Vector`](../../c4d/Vector/index.md#c4d.Vector) from the hyperfile.

**Geometric Writing**

- [`HyperFile.WriteMatrix()`](#c4d.storage.HyperFile.WriteMatrix): Write a [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) to the hyperfile.
- [`HyperFile.WriteMatrix32()`](#c4d.storage.HyperFile.WriteMatrix32): Write a [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) to the hyperfile.
- [`HyperFile.WriteMatrix64()`](#c4d.storage.HyperFile.WriteMatrix64): Write a double precision [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) to the hyperfile.
- [`HyperFile.WriteVector()`](#c4d.storage.HyperFile.WriteVector): Write a [`Vector`](../../c4d/Vector/index.md#c4d.Vector) to the hyperfile.
- [`HyperFile.WriteVector32()`](#c4d.storage.HyperFile.WriteVector32): Write a [`Vector`](../../c4d/Vector/index.md#c4d.Vector) to the hyperfile.
- [`HyperFile.WriteVector64()`](#c4d.storage.HyperFile.WriteVector64): Write a double precision [`Vector`](../../c4d/Vector/index.md#c4d.Vector) to the hyperfile.

**Magic Methods**

- [`HyperFile.__init__()`](#c4d.storage.HyperFile.__init__): Allocates a hyper file.

**Numeric Reading**

- [`HyperFile.ReadChar()`](#c4d.storage.HyperFile.ReadChar): Read a character from the hyperfile.
- [`HyperFile.ReadFloat()`](#c4d.storage.HyperFile.ReadFloat): Read a float from the hyperfile.
- [`HyperFile.ReadFloat32()`](#c4d.storage.HyperFile.ReadFloat32): Read a float from the hyperfile.
- [`HyperFile.ReadFloat64()`](#c4d.storage.HyperFile.ReadFloat64): Read a double precision float from the hyperfile.
- [`HyperFile.ReadInt16()`](#c4d.storage.HyperFile.ReadInt16): Read a signed word from the hyperfile.
- [`HyperFile.ReadInt32()`](#c4d.storage.HyperFile.ReadInt32): Read an int from the hyperfile.
- [`HyperFile.ReadInt64()`](#c4d.storage.HyperFile.ReadInt64): Read a double precision int from the hyperfile.
- [`HyperFile.ReadUChar()`](#c4d.storage.HyperFile.ReadUChar): Read an unsigned character from the hyperfile.
- [`HyperFile.ReadUInt16()`](#c4d.storage.HyperFile.ReadUInt16): Read an unsigned word from the hyperfile.
- [`HyperFile.ReadUInt32()`](#c4d.storage.HyperFile.ReadUInt32): Read an unsigned int from the hyperfile.
- [`HyperFile.ReadUInt64()`](#c4d.storage.HyperFile.ReadUInt64): Read a double precision unsigned int from the hyperfile.

**Numeric Writing**

- [`HyperFile.WriteChar()`](#c4d.storage.HyperFile.WriteChar): Write a character to the hyperfile.
- [`HyperFile.WriteFloat32()`](#c4d.storage.HyperFile.WriteFloat32): Write a float value to the hyperfile.
- [`HyperFile.WriteFloat64()`](#c4d.storage.HyperFile.WriteFloat64): Write a double precision float value to the hyperfile.
- [`HyperFile.WriteInt16()`](#c4d.storage.HyperFile.WriteInt16): Write a signed short int to the hyperfile.
- [`HyperFile.WriteInt32()`](#c4d.storage.HyperFile.WriteInt32): Write an int to the hyperfile.
- [`HyperFile.WriteInt64()`](#c4d.storage.HyperFile.WriteInt64): Write a double precision int value to the hyperfile.
- [`HyperFile.WriteUChar()`](#c4d.storage.HyperFile.WriteUChar): Write a very short int to the hyperfile.
- [`HyperFile.WriteUInt16()`](#c4d.storage.HyperFile.WriteUInt16): Write an unsigned short int to the hyperfile.
- [`HyperFile.WriteUInt32()`](#c4d.storage.HyperFile.WriteUInt32): Write an unsigned int to the hyperfile.
- [`HyperFile.WriteUInt64()`](#c4d.storage.HyperFile.WriteUInt64): Write a double precision unsigned int value to the hyperfile.

**Scalar And Text Reading**

- [`HyperFile.ReadBool()`](#c4d.storage.HyperFile.ReadBool): Read a bool from the hyperfile.
- [`HyperFile.ReadFilename()`](#c4d.storage.HyperFile.ReadFilename): Read a path from the hyperfile.
- [`HyperFile.ReadString()`](#c4d.storage.HyperFile.ReadString): Read a string from the hyperfile.
- [`HyperFile.ReadTime()`](#c4d.storage.HyperFile.ReadTime): Read a [`BaseTime`](../../c4d/BaseTime/index.md#c4d.BaseTime) from the hyperfile.

**Scalar And Text Writing**

- [`HyperFile.WriteBool()`](#c4d.storage.HyperFile.WriteBool): Write a bool to the hyperfile.
- [`HyperFile.WriteFilename()`](#c4d.storage.HyperFile.WriteFilename): Write a path to the hyperfile.
- [`HyperFile.WriteString()`](#c4d.storage.HyperFile.WriteString): Write a string to the hyperfile.
- [`HyperFile.WriteTime()`](#c4d.storage.HyperFile.WriteTime): Write a [`BaseTime`](../../c4d/BaseTime/index.md#c4d.BaseTime) to the hyperfile.

**Structured Data Reading**

- [`HyperFile.ReadContainer()`](#c4d.storage.HyperFile.ReadContainer): Read a container from the hyperfile.
- [`HyperFile.ReadData()`](#c4d.storage.HyperFile.ReadData): Read a data from the hyperfile.
- [`HyperFile.ReadImage()`](#c4d.storage.HyperFile.ReadImage): Read a bitmap from the hyperfile.
- [`HyperFile.ReadMemory()`](#c4d.storage.HyperFile.ReadMemory): Read a block of memory from the hyperfile.

**Structured Data Writing**

- [`HyperFile.WriteContainer()`](#c4d.storage.HyperFile.WriteContainer): Write the settings in a [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer) to the hyperfile.
- [`HyperFile.WriteData()`](#c4d.storage.HyperFile.WriteData): Write data to the container.
- [`HyperFile.WriteImage()`](#c4d.storage.HyperFile.WriteImage): Write an image to the hyperfile.
- [`HyperFile.WriteMemory()`](#c4d.storage.HyperFile.WriteMemory): Write a block of memory to the hyperfile.

**Value Navigation**

- [`HyperFile.ReadValueHeader()`](#c4d.storage.HyperFile.ReadValueHeader): Read the value header from the file.
- [`HyperFile.SkipValue()`](#c4d.storage.HyperFile.SkipValue): Skip a given type of value.

## Members <a id="members"></a>

### Chunk Reading <a id="c4d.storage.HyperFile-method-Chunk-Reading"></a>

#### `HyperFile.ReadChunkEnd(self)` <a id="c4d.storage.HyperFile.ReadChunkEnd"></a>

Read a chunks end marker from the file.

**Return type:** bool

**Returns:** Success of reading the chunk end.

#### `HyperFile.ReadChunkStart(self)` <a id="c4d.storage.HyperFile.ReadChunkStart"></a>

Read a chunks identification from the file.

```python
import c4d

hf = c4d.storage.HyperFile()

chunk = hf.ReadChunkStart()
if chunk is None:
    return

id = chunk["id"]  # Chunk ID, int
level = chunk["level"]  # Chunk Level, int
```

**Return type:** Optional[Dict[**id**: int, **level**: int]]

**Returns:** The identification or **None** on failure.

#### `HyperFile.SkipToEndChunk(self)` <a id="c4d.storage.HyperFile.SkipToEndChunk"></a>

Move the file pointer to the end of the chunk.

> **Note:** This should always be called after finishing reading your values from this chunk.

**Return type:** bool

**Returns:** Success of finding the end of the chunk.

### Chunk Writing <a id="c4d.storage.HyperFile-method-Chunk-Writing"></a>

#### `HyperFile.WriteChunkEnd(self)` <a id="c4d.storage.HyperFile.WriteChunkEnd"></a>

Write a chunk ending marker into the file.

**Return type:** bool

**Returns:** Success of writing the chunk end.

#### `HyperFile.WriteChunkStart(self, id, level)` <a id="c4d.storage.HyperFile.WriteChunkStart"></a>

Write a chunk marker into the file indicating the beginning of a new chunk of data.

> **Note:**
>
> Chunks should only be used if absolutely necessary.  
> If a plugin uses chunks badly then the file structure can become corrupted.

**Parameters:**

- **id** (*int*) – The ID for the chunk.
- **level** (*int*) – If you want to write additional information you can increase the level this allows you to easily save/read new values.

**Return type:** bool

**Returns:** Success of writing the chunk identification.

### Error Handling <a id="c4d.storage.HyperFile-method-Error-Handling"></a>

#### `HyperFile.GetError(self)` <a id="c4d.storage.HyperFile.GetError"></a>

Get the error from the last hyperfile operation.

**Return type:** int

**Returns:** The error number.

#### `HyperFile.SetError(self, err)` <a id="c4d.storage.HyperFile.SetError"></a>

Set the error value for this hyperfile.

**Parameters:** **err** (*int*) – The error number.

### File Context <a id="c4d.storage.HyperFile-method-File-Context"></a>

#### `HyperFile.GetDocument(self)` <a id="c4d.storage.HyperFile.GetDocument"></a>

Gets the active document for the hyper file operation.

> **Note:** Can be **None**, for example when saving layouts.

**Return type:** Optional[[c4d.documents.BaseDocument](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]

**Returns:** The document or **None**.

#### `HyperFile.GetFileVersion(self)` <a id="c4d.storage.HyperFile.GetFileVersion"></a>

Get the version of Cinema 4D that wrote the file.

> **Note:** Only valid during reading a Cinema 4D scene, object, material etc.

**Return type:** int

**Returns:** The file version.

#### `HyperFile.GetFilterFlags(self)` <a id="c4d.storage.HyperFile.GetFilterFlags"></a>

Gets the filter flags, the value is valid only during a Load or a Merge.

*New in version R21.108.*

**Return type:** int

**Returns:**

The filter flags:

|   |   |
|---|---|
| *SCENEFILTER_NONE* | None. |
| *SCENEFILTER_OBJECTS* | Load/save objects. |
| *SCENEFILTER_MATERIALS* | Load/save materials. |
| *SCENEFILTER_DIALOGSALLOWED* | Flag to inform a plugin that a dialog can be displayed. If this flag is not set then no dialogs must be opened. |
| *SCENEFILTER_PROGRESSALLOWED* | Flag to inform a plugin that a progress bar can be displayed. The progress bar can be set by calling [`StatusSetBar()`](../../c4d/index.md#c4d.StatusSetBar). |
| *SCENEFILTER_MERGESCENE* | Flag to inform a plugin that this is a merge operation, i.e. the document that is inserted to is an existing scene. |
| *SCENEFILTER_NONEWMARKERS* | Objects loaded from disk will keep their markers. |
| *SCENEFILTER_SAVECACHES* | For *melange* export only. Caches of objects will also be written (only supported by Cinema 4D format). This is the same as the global option “Save Polygon Objects for Melange Exchange”. |
| *SCENEFILTER_NOUNDO* | Use together with *SCENEFILTER_MERGESCENE* to avoid that undos are created for the merge operation. |
| *SCENEFILTER_SAVE_BINARYCACHE* | Save the binary compiled shaders with the scene (only for Cinema 4D format). |
| *SCENEFILTER_IDENTIFY_ONLY* | Do not load the whole document, identify it only. |
| *SCENEFILTER_ONLY_RENDERDATA* | Only load render settings. If this flag is set, *SCENEFILTER_OBJECTS* and *SCENEFILTER_MATERIALS* are ignored. |
| *SCENEFILTER_IGNOREMISSINGPLUGINSINNONACTIVERENDERDATA* | Ignore all missing plugins which are part of a non-active render data. |
| *SCENEFILTER_IGNOREXREFS* | *New in version R16.038:* Avoid that included X-Refs will be loaded. |
| *SCENEFILTER_DONTCORRECTOUTPUTFORMAT* | Do not change unknown output formats in render settings. |

### File Lifecycle <a id="c4d.storage.HyperFile-method-File-Lifecycle"></a>

#### `HyperFile.Close(self)` <a id="c4d.storage.HyperFile.Close"></a>

Closes the hyper file.

**Return type:** bool

**Returns:** **True** on success.

#### `HyperFile.Open(self, ident, filename, mode, error_dialog)` <a id="c4d.storage.HyperFile.Open"></a>

Opens the hyper file.

**Parameters:**

- **ident** (*int*) – File identification.

- **filename** (*Union*[*str*, [*c4d.storage.MemoryFileStruct*](../MemoryFileStruct/index.md#c4d.storage.MemoryFileStruct)]) – File to open.

- **mode** (*int*) –

  File mode:

  |   |   |
  |---|---|
  | *FILEOPEN_APPEND* | Open an existing file for writing and set the position to the end of that file. |
  | *FILEOPEN_READ* | Open the file for reading. |
  | *FILEOPEN_WRITE* | Create a new file for writing. **Warning:** If the file name points to an existing file, it will be overwritten. |
  | *FILEOPEN_READWRITE* | Open the file for both reading and writing. |
  | *FILEOPEN_READ_NOCACHE* | Private. |
  | *FILEOPEN_SHAREDREAD* | Private. |
  | *FILEOPEN_SHAREDWRITE* | Private. |

- **error_dialog** (*int*) –

  File error dialog:

  |   |   |
  |---|---|
  | *FILEDIALOG_NONE* | Never show an error dialog. |
  | *FILEDIALOG_ANY* | Show an error dialog for any error. |
  | *FILEDIALOG_IGNOREOPEN* | Do not show an error dialog if the file does not exist, otherwise like *FILEDIALOG_ANY*. |

**Return type:** bool

**Returns:** **True** if the hyper file could be opened, otherwise **False**.

### Geometric Reading <a id="c4d.storage.HyperFile-method-Geometric-Reading"></a>

#### `HyperFile.ReadMatrix(self)` <a id="c4d.storage.HyperFile.ReadMatrix"></a>

Read a [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) from the hyperfile.

**Return type:** Optional[[c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix)]

**Returns:** The matrix or **None** if reading failed.

#### `HyperFile.ReadMatrix32(self)` <a id="c4d.storage.HyperFile.ReadMatrix32"></a>

Read a [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) from the hyperfile.

*New in version R16.021.*

**Return type:** Optional[[c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix)]

**Returns:** The matrix or **None** if reading failed.

#### `HyperFile.ReadMatrix64(self)` <a id="c4d.storage.HyperFile.ReadMatrix64"></a>

Read a double precision [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) from the hyperfile.

*New in version R15.037.*

**Return type:** Optional[[c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix)]

**Returns:** The matrix or **None** if reading failed.

#### `HyperFile.ReadVector(self)` <a id="c4d.storage.HyperFile.ReadVector"></a>

Read a [`Vector`](../../c4d/Vector/index.md#c4d.Vector) from the hyperfile.

**Return type:** Optional[[c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The vector or **None** if reading failed.

#### `HyperFile.ReadVector32(self)` <a id="c4d.storage.HyperFile.ReadVector32"></a>

Read a [`Vector`](../../c4d/Vector/index.md#c4d.Vector) from the hyperfile.

*New in version R16.021.*

**Return type:** Optional[[c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The vector or **None** if reading failed.

#### `HyperFile.ReadVector64(self)` <a id="c4d.storage.HyperFile.ReadVector64"></a>

Read a double precision [`Vector`](../../c4d/Vector/index.md#c4d.Vector) from the hyperfile.

*New in version R15.037.*

**Return type:** Optional[[c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The vector or **None** if reading failed.

### Geometric Writing <a id="c4d.storage.HyperFile-method-Geometric-Writing"></a>

#### `HyperFile.WriteMatrix(self, v)` <a id="c4d.storage.HyperFile.WriteMatrix"></a>

Write a [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) to the hyperfile.

**Parameters:** **v** ([*c4d.Matrix*](../../c4d/Matrix/index.md#c4d.Matrix)) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteMatrix32(self, v)` <a id="c4d.storage.HyperFile.WriteMatrix32"></a>

Write a [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) to the hyperfile.

*New in version R16.021.*

**Parameters:** **v** ([*c4d.Matrix*](../../c4d/Matrix/index.md#c4d.Matrix)) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteMatrix64(self, v)` <a id="c4d.storage.HyperFile.WriteMatrix64"></a>

Write a double precision [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) to the hyperfile.

*New in version R15.037.*

**Parameters:** **v** ([*c4d.Matrix*](../../c4d/Matrix/index.md#c4d.Matrix)) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteVector(self, v)` <a id="c4d.storage.HyperFile.WriteVector"></a>

Write a [`Vector`](../../c4d/Vector/index.md#c4d.Vector) to the hyperfile.

**Parameters:** **v** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteVector32(self, v)` <a id="c4d.storage.HyperFile.WriteVector32"></a>

Write a [`Vector`](../../c4d/Vector/index.md#c4d.Vector) to the hyperfile.

*New in version R16.021.*

**Parameters:** **v** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteVector64(self, v)` <a id="c4d.storage.HyperFile.WriteVector64"></a>

Write a double precision [`Vector`](../../c4d/Vector/index.md#c4d.Vector) to the hyperfile.

*New in version R15.037.*

**Parameters:** **v** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

### Magic Methods <a id="c4d.storage.HyperFile-method-Magic-Methods"></a>

#### `HyperFile.__init__(self)` <a id="c4d.storage.HyperFile.__init__"></a>

Allocates a hyper file.

### Numeric Reading <a id="c4d.storage.HyperFile-method-Numeric-Reading"></a>

#### `HyperFile.ReadChar(self)` <a id="c4d.storage.HyperFile.ReadChar"></a>

Read a character from the hyperfile.

**Return type:** Optional[int]

**Returns:** The character or **None** if reading failed.

#### `HyperFile.ReadFloat(self)` <a id="c4d.storage.HyperFile.ReadFloat"></a>

Read a float from the hyperfile.

*New in version R15.037.*

**Return type:** Optional[float]

**Returns:** The float or **None** if reading failed.

#### `HyperFile.ReadFloat32(self)` <a id="c4d.storage.HyperFile.ReadFloat32"></a>

Read a float from the hyperfile.

*New in version R16.021.*

**Return type:** Optional[float]

**Returns:** The float or **None** if reading failed.

#### `HyperFile.ReadFloat64(self)` <a id="c4d.storage.HyperFile.ReadFloat64"></a>

Read a double precision float from the hyperfile.

*New in version R15.037.*

**Return type:** Optional[float]

**Returns:** The float or **None** if reading failed.

#### `HyperFile.ReadInt16(self)` <a id="c4d.storage.HyperFile.ReadInt16"></a>

Read a signed word from the hyperfile.

*New in version R15.037.*

**Return type:** Optional[int]

**Returns:** The unsigned word or **None** if reading failed.

#### `HyperFile.ReadInt32(self)` <a id="c4d.storage.HyperFile.ReadInt32"></a>

Read an int from the hyperfile.

*New in version R15.037.*

**Return type:** Optional[int]

**Returns:** The unsigned int or **None** if reading failed.

#### `HyperFile.ReadInt64(self)` <a id="c4d.storage.HyperFile.ReadInt64"></a>

Read a double precision int from the hyperfile.

*New in version R15.037.*

**Return type:** Optional[int]

**Returns:** The value or **None** if reading failed.

#### `HyperFile.ReadUChar(self)` <a id="c4d.storage.HyperFile.ReadUChar"></a>

Read an unsigned character from the hyperfile.

**Return type:** Optional[int]

**Returns:** The unsigned character or **None** if reading failed.

#### `HyperFile.ReadUInt16(self)` <a id="c4d.storage.HyperFile.ReadUInt16"></a>

Read an unsigned word from the hyperfile.

*New in version R15.037.*

**Return type:** Optional[int]

**Returns:** The unsigned word or **None** if reading failed.

#### `HyperFile.ReadUInt32(self)` <a id="c4d.storage.HyperFile.ReadUInt32"></a>

Read an unsigned int from the hyperfile.

*New in version R15.037.*

**Return type:** Optional[int]

**Returns:** The unsigned int or **None** if reading failed.

#### `HyperFile.ReadUInt64(self)` <a id="c4d.storage.HyperFile.ReadUInt64"></a>

Read a double precision unsigned int from the hyperfile.

*New in version R16.021.*

**Return type:** Optional[int]

**Returns:** The value or **None** if reading failed.

### Numeric Writing <a id="c4d.storage.HyperFile-method-Numeric-Writing"></a>

#### `HyperFile.WriteChar(self, v)` <a id="c4d.storage.HyperFile.WriteChar"></a>

Write a character to the hyperfile.

**Parameters:** **v** (*int*) – A char to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteFloat32(self, v)` <a id="c4d.storage.HyperFile.WriteFloat32"></a>

Write a float value to the hyperfile.

*New in version R16.021.*

**Parameters:** **v** (*float*) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteFloat64(self, v)` <a id="c4d.storage.HyperFile.WriteFloat64"></a>

Write a double precision float value to the hyperfile.

*New in version R15.037.*

**Parameters:** **v** (*float*) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteInt16(self, v)` <a id="c4d.storage.HyperFile.WriteInt16"></a>

Write a signed short int to the hyperfile.

*New in version R15.037.*

**Parameters:** **v** (*int*) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteInt32(self, v)` <a id="c4d.storage.HyperFile.WriteInt32"></a>

Write an int to the hyperfile.

*New in version R15.037.*

**Parameters:** **v** (*int*) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteInt64(self, v)` <a id="c4d.storage.HyperFile.WriteInt64"></a>

Write a double precision int value to the hyperfile.

*New in version R15.037.*

**Parameters:** **v** (*int*) – The integer to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteUChar(self, v)` <a id="c4d.storage.HyperFile.WriteUChar"></a>

Write a very short int to the hyperfile.

**Parameters:** **v** (*int*) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteUInt16(self, v)` <a id="c4d.storage.HyperFile.WriteUInt16"></a>

Write an unsigned short int to the hyperfile.

*New in version R15.037.*

**Parameters:** **v** (*int*) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteUInt32(self, v)` <a id="c4d.storage.HyperFile.WriteUInt32"></a>

Write an unsigned int to the hyperfile.

*New in version R15.037.*

**Parameters:** **v** (*int*) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteUInt64(self, v)` <a id="c4d.storage.HyperFile.WriteUInt64"></a>

Write a double precision unsigned int value to the hyperfile.

*New in version R15.037.*

**Parameters:** **v** (*int*) – The integer to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

### Scalar And Text Reading <a id="c4d.storage.HyperFile-method-Scalar-And-Text-Reading"></a>

#### `HyperFile.ReadBool(self)` <a id="c4d.storage.HyperFile.ReadBool"></a>

Read a bool from the hyperfile.

**Return type:** Optional[bool]

**Returns:** The bool or **None** if reading failed.

#### `HyperFile.ReadFilename(self)` <a id="c4d.storage.HyperFile.ReadFilename"></a>

Read a path from the hyperfile.

**Return type:** Optional[str]

**Returns:** The path or **None** if reading failed.

#### `HyperFile.ReadString(self)` <a id="c4d.storage.HyperFile.ReadString"></a>

Read a string from the hyperfile.

**Return type:** Optional[str]

**Returns:** The string or **None** if reading failed.

#### `HyperFile.ReadTime(self)` <a id="c4d.storage.HyperFile.ReadTime"></a>

Read a [`BaseTime`](../../c4d/BaseTime/index.md#c4d.BaseTime) from the hyperfile.

**Return type:** Optional[[c4d.BaseTime](../../c4d/BaseTime/index.md#c4d.BaseTime)]

**Returns:** The time or **None** if reading failed.

### Scalar And Text Writing <a id="c4d.storage.HyperFile-method-Scalar-And-Text-Writing"></a>

#### `HyperFile.WriteBool(self, v)` <a id="c4d.storage.HyperFile.WriteBool"></a>

Write a bool to the hyperfile.

**Parameters:** **v** (*bool*) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteFilename(self, v)` <a id="c4d.storage.HyperFile.WriteFilename"></a>

Write a path to the hyperfile.

**Parameters:** **v** (*str*) – The path to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteString(self, v)` <a id="c4d.storage.HyperFile.WriteString"></a>

Write a string to the hyperfile.

**Parameters:** **v** (*str*) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteTime(self, v)` <a id="c4d.storage.HyperFile.WriteTime"></a>

Write a [`BaseTime`](../../c4d/BaseTime/index.md#c4d.BaseTime) to the hyperfile.

**Parameters:** **v** ([*c4d.BaseTime*](../../c4d/BaseTime/index.md#c4d.BaseTime)) – The value to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

### Structured Data Reading <a id="c4d.storage.HyperFile-method-Structured-Data-Reading"></a>

#### `HyperFile.ReadContainer(self)` <a id="c4d.storage.HyperFile.ReadContainer"></a>

Read a container from the hyperfile.

**Return type:** Optional[[c4d.bitmaps.BaseBitmap](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]

**Returns:** The container or **None** if reading failed.

#### `HyperFile.ReadData(self)` <a id="c4d.storage.HyperFile.ReadData"></a>

Read a data from the hyperfile.

> **Note:** Please check the constructor of **GeData** in the C++ SDK to see what type this method accepts.

**Return type:** Optional[Any]

**Returns:** The value or **None** if reading failed.

#### `HyperFile.ReadImage(self)` <a id="c4d.storage.HyperFile.ReadImage"></a>

Read a bitmap from the hyperfile.

**Return type:** Optional[[c4d.bitmaps.BaseBitmap](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]

**Returns:** The bitmap or **None** if reading failed.

#### `HyperFile.ReadMemory(self)` <a id="c4d.storage.HyperFile.ReadMemory"></a>

Read a block of memory from the hyperfile.

> **Note:** Only use this when you need to, be aware that the byte sequences will not be platform independent.

**Return type:** Optional[bytes]

**Returns:** The value or **None** if reading failed.

### Structured Data Writing <a id="c4d.storage.HyperFile-method-Structured-Data-Writing"></a>

#### `HyperFile.WriteContainer(self, v)` <a id="c4d.storage.HyperFile.WriteContainer"></a>

Write the settings in a [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer) to the hyperfile.

**Parameters:** **v** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The container to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteData(self, v)` <a id="c4d.storage.HyperFile.WriteData"></a>

Write data to the container.

> **Note:** Please check the constructor of **GeData** in the C++ SDK to see what type this method accepts.

**Parameters:** **v** (*any*) – The data.

**Return type:** bool

**Returns:** Success of writing the value.

#### `HyperFile.WriteImage(self, v, format, data, savebits=1)` <a id="c4d.storage.HyperFile.WriteImage"></a>

Write an image to the hyperfile.

**Parameters:**

- **v** ([*c4d.bitmaps.BaseBitmap*](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The bitmap to write to the hyperfile.

- **format** (*int*) –

  The image format:

  |   |   |
  |---|---|
  | *FILTER_TIF* | TIFF. |
  | *FILTER_TGA* | TGA. |
  | *FILTER_BMP* | BMP. |
  | *FILTER_IFF* | IFF. |
  | *FILTER_JPG* | JPEG. |
  | *FILTER_PICT* | PICT. |
  | *FILTER_PSD* | PSD. |
  | *FILTER_RLA* | RLA. |
  | *FILTER_RPF* | RPF. |
  | *FILTER_B3D* | *BodyPaint 3D*. |
  | *FILTER_TIF_B3D* | TIFF *BodyPaint 3D*. |
  | *FILTER_PSB* | PSB. |
  | *FILTER_AVI* | AVI Movie. |
  | *FILTER_MOVIE* | Quicktime Movie. |
  | *FILTER_QTVRSAVER_PANORAMA* | QTVR Panorama. |
  | *FILTER_QTVRSAVER_OBJECT* | QTVR Object. |
  | *FILTER_HDR* | HDR. |
  | *FILTER_EXR_LOAD* | EXR (Load). |
  | *FILTER_EXR* | EXR. |
  | *FILTER_PNG* | PNG. |
  | *FILTER_IES* | IES. |
  | *FILTER_B3DNET* | *BodyPaint 3D* NET. Private. |
  | *FILTER_DPX* | DPX. |
  | *FILTER_DDS* | *New in version R19:* DDS. |

- **data** (*Optional*[[*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)]) –

  A container with additional format settings, or **None**.

  | Symbol ID | Description |
  |---|---|
  | SAVEBIT_NONE | None. |
  | SAVEBIT_ALPHA | Save the alpha channel(s) in the file. (For filter plugins, do not save an alpha channel if this is not set.) |
  | SAVEBIT_MULTILAYER | Save multiple layers. |
  | SAVEBIT_USESELECTEDLAYERS | Use selected layers. |
  | SAVEBIT_USE16BITCHANNELS | Use *16*-bit channels. |
  | SAVEBIT_GREYSCALE | Save in grayscale mode. |
  | SAVEBIT_INTERNALNET | Private. |
  | SAVEBIT_DONTMERGE | Avoid merging of layers in BodyPaint 3D files. |
  | SAVEBIT_USE32BITCHANNELS | Use *32*-bit channels. |
  | SAVEBIT_SAVERENDERRESULT | Private. |
  | SAVEBIT_FIRSTALPHA_ONLY | Private. |
  | SAVEBIT_KEEP_COLOR_MODE | Private. |

- **savebits** (*int*) –

  The save bits:

  | Symbol ID | Description |
  |---|---|
  | SAVEBIT_NONE | None. |
  | SAVEBIT_ALPHA | Save the alpha channel(s) in the file. (For filter plugins, do not save an alpha channel if this is not set.) |
  | SAVEBIT_MULTILAYER | Save multiple layers. |
  | SAVEBIT_USESELECTEDLAYERS | Use selected layers. |
  | SAVEBIT_USE16BITCHANNELS | Use *16*-bit channels. |
  | SAVEBIT_GREYSCALE | Save in grayscale mode. |
  | SAVEBIT_INTERNALNET | Private. |
  | SAVEBIT_DONTMERGE | Avoid merging of layers in BodyPaint 3D files. |
  | SAVEBIT_USE32BITCHANNELS | Use *32*-bit channels. |
  | SAVEBIT_SAVERENDERRESULT | Private. |
  | SAVEBIT_FIRSTALPHA_ONLY | Private. |
  | SAVEBIT_KEEP_COLOR_MODE | Private. |

**Return type:** bool

**Returns:** Success of writing the image.

#### `HyperFile.WriteMemory(self, data)` <a id="c4d.storage.HyperFile.WriteMemory"></a>

Write a block of memory to the hyperfile.

> **Note:** Only use this when you need to, be aware that the byte sequences will not be platform independent.

**Parameters:** **data** (*bytearray*) – The data to write to the hyperfile.

**Return type:** bool

**Returns:** Success of writing the data.

### Value Navigation <a id="c4d.storage.HyperFile-method-Value-Navigation"></a>

#### `HyperFile.ReadValueHeader(self)` <a id="c4d.storage.HyperFile.ReadValueHeader"></a>

Read the value header from the file. This is only necessary in combination with loops.

Example:

```python
import c4d

def ReadSettings(op, hf, level):
    while hf.ReadValueHeader() == c4d.HYPERFILEVALUE_START:
        chunk = hf.ReadChunkStart()
        if not chunk:
            return False

        id = chunk["id"]
        if id == 2:
            i1 = hf.ReadInt32()
            i2 = hf.ReadInt32()
            # do_here
        elif id == 3:
            i1 = hf.ReadInt32()
            i2 = hf.ReadInt32()
            i3 = hf.ReadInt32()
            # do_here

        hf.SkipToEndChunk()  # never forget this at the end
        if id == 0:
            break

    test = hf.ReadString()
    # do here
    return True
```

**Return type:** Optional[int]

**Returns:**

The header value or **None**:

|   |   |
|---|---|
| *HYPERFILEVALUE_NONE* | None. |
| *HYPERFILEVALUE_START* | Marks the start of a chunk. |
| *HYPERFILEVALUE_STOP* | Marks the end of a chunk. |
| *HYPERFILEVALUE_CSTOP* | Marks the end of a container. Internal. |
| *HYPERFILEVALUE_CHAR* | Integer. |
| *HYPERFILEVALUE_UCHAR* | Integer. |
| *HYPERFILEVALUE_INT16* | Integer. |
| *HYPERFILEVALUE_UINT16* | Integer. |
| *HYPERFILEVALUE_INT32* | Integer. |
| *HYPERFILEVALUE_UINT32* | Integer. |
| *HYPERFILEVALUE_INT64* | Integer. |
| *HYPERFILEVALUE_UINT64* | Integer. |
| *HYPERFILEVALUE_FLOAT* | Float. |
| *HYPERFILEVALUE_FLOAT32* | Float. |
| *HYPERFILEVALUE_FLOAT64* | Float. |
| *HYPERFILEVALUE_TIME* | [`BaseTime`](../../c4d/BaseTime/index.md#c4d.BaseTime). |
| *HYPERFILEVALUE_VECTOR* | [`Vector`](../../c4d/Vector/index.md#c4d.Vector). |
| *HYPERFILEVALUE_VECTOR32* | [`Vector`](../../c4d/Vector/index.md#c4d.Vector). |
| *HYPERFILEVALUE_VECTOR64* | [`Vector`](../../c4d/Vector/index.md#c4d.Vector). |
| *HYPERFILEVALUE_MATRIX* | [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix). |
| *HYPERFILEVALUE_MATRIX32* | [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix). |
| *HYPERFILEVALUE_MATRIX64* | [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix). |
| *HYPERFILEVALUE_MEMORY* | Memory. |
| *HYPERFILEVALUE_IMAGE* | Image. |
| *HYPERFILEVALUE_STRING* | String. |
| *HYPERFILEVALUE_FILENAME* | String. |
| *HYPERFILEVALUE_CONTAINER* | [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer). |
| *HYPERFILEVALUE_ALIASLINK* | [`BaseList2D`](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D). |

#### `HyperFile.SkipValue(self, h)` <a id="c4d.storage.HyperFile.SkipValue"></a>

Skip a given type of value.

**Parameters:**

**h** (*int*) –

The hyper file value to skip:

|   |   |
|---|---|
| *HYPERFILEVALUE_NONE* | None. |
| *HYPERFILEVALUE_START* | Marks the start of a chunk. |
| *HYPERFILEVALUE_STOP* | Marks the end of a chunk. |
| *HYPERFILEVALUE_CSTOP* | Marks the end of a container. Internal. |
| *HYPERFILEVALUE_CHAR* | Integer. |
| *HYPERFILEVALUE_UCHAR* | Integer. |
| *HYPERFILEVALUE_INT16* | Integer. |
| *HYPERFILEVALUE_UINT16* | Integer. |
| *HYPERFILEVALUE_INT32* | Integer. |
| *HYPERFILEVALUE_UINT32* | Integer. |
| *HYPERFILEVALUE_INT64* | Integer. |
| *HYPERFILEVALUE_UINT64* | Integer. |
| *HYPERFILEVALUE_FLOAT* | Float. |
| *HYPERFILEVALUE_FLOAT32* | Float. |
| *HYPERFILEVALUE_FLOAT64* | Float. |
| *HYPERFILEVALUE_TIME* | [`BaseTime`](../../c4d/BaseTime/index.md#c4d.BaseTime). |
| *HYPERFILEVALUE_VECTOR* | [`Vector`](../../c4d/Vector/index.md#c4d.Vector). |
| *HYPERFILEVALUE_VECTOR32* | [`Vector`](../../c4d/Vector/index.md#c4d.Vector). |
| *HYPERFILEVALUE_VECTOR64* | [`Vector`](../../c4d/Vector/index.md#c4d.Vector). |
| *HYPERFILEVALUE_MATRIX* | [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix). |
| *HYPERFILEVALUE_MATRIX32* | [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix). |
| *HYPERFILEVALUE_MATRIX64* | [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix). |
| *HYPERFILEVALUE_MEMORY* | Memory. |
| *HYPERFILEVALUE_IMAGE* | Image. |
| *HYPERFILEVALUE_STRING* | String. |
| *HYPERFILEVALUE_FILENAME* | String. |
| *HYPERFILEVALUE_CONTAINER* | [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer). |
| *HYPERFILEVALUE_ALIASLINK* | [`BaseList2D`](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D). |

**Return type:** bool

**Returns:** **True** if the value was of the given header type and it was skipped, otherwise **False**.
