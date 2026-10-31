<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseData/NodeData/SceneLoaderData/index.html -->

# c4d.plugins.SceneLoaderData <a id="c4d-plugins-sceneloaderdata"></a>

## *class* `c4d.plugins.SceneLoaderData` <a id="c4d.plugins.SceneLoaderData"></a>

A data class for creating scene loaders.  
Use [`RegisterSceneLoaderPlugin()`](../../../index.md#c4d.plugins.RegisterSceneLoaderPlugin) to register the plugin.

Parent Class:

- [`c4d.plugins.NodeData`](../index.md#c4d.plugins.NodeData)

## Overview <a id="overview"></a>

- [`SceneLoaderData.Identify()`](#c4d.plugins.SceneLoaderData.Identify): Override - Identify the file type as one that can be loaded using this plugin.
- [`SceneLoaderData.Load()`](#c4d.plugins.SceneLoaderData.Load): Override - Load the file into the document.

## Members <a id="members"></a>

### File Loading <a id="c4d.plugins.SceneLoaderData-method-File-Loading"></a>

#### `SceneLoaderData.Identify(self, node, name, probe, size)` <a id="c4d.plugins.SceneLoaderData.Identify"></a>

Override - Identify the file type as one that can be loaded using this plugin.  
If possible, the file should not be identified through the suffix, but through the *probe* data.

**Parameters:**

- **node** ([*c4d.BaseList2D*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The node object.
- **name** (*str*) – The name of the loader.
- **probe** (*memoryview*) – The start of a small chunk of data from the start of the file for testing this file type. Usually the probe size is 1024 bytes. Never call the buffer outside this method!
- **size** (*int*) – The size of the chunk for testing this file type.

**Return type:** bool

**Returns:** **True** if your plugin recognises this file.

#### `SceneLoaderData.Load(self, node, name, doc, filterflags, error, bt)` <a id="c4d.plugins.SceneLoaderData.Load"></a>

Override - Load the file into the document.

**Parameters:**

- **node** ([*c4d.BaseList2D*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The node object.

- **name** (*str*) – The filename of the file to load.

- **doc** ([*c4d.documents.BaseDocument*](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document that the selected objects should be loaded into.

- **filterflags** (*int*) –

  Information about what can be done during this load call:

  |   |   |
  |---|---|
  | *SCENEFILTER_NONE* | None. |
  | *SCENEFILTER_OBJECTS* | Load/save objects. |
  | *SCENEFILTER_MATERIALS* | Load/save materials. |
  | *SCENEFILTER_DIALOGSALLOWED* | Flag to inform a plugin that a dialog can be displayed. If this flag is not set then no dialogs must be opened. |
  | *SCENEFILTER_PROGRESSALLOWED* | Flag to inform a plugin that a progress bar can be displayed. The progress bar can be set by calling [`StatusSetBar()`](../../../../c4d/index.md#c4d.StatusSetBar). |
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

- **error** (*None*) – Not supported.

- **bt** ([*c4d.threading.BaseThread*](../../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)) – The calling thread.

**Return type:** int

**Returns:**

The return values:

| Symbol ID | Description |
|---|---|
| FILEERROR_NONE | No error. |
| FILEERROR_OPEN | Problems opening the file. |
| FILEERROR_CLOSE | Problems closing the file. |
| FILEERROR_READ | Problems reading the file. |
| FILEERROR_WRITE | Problems writing the file. |
| FILEERROR_SEEK | Problems seeking the file. |
| FILEERROR_INVALID | Invalid parameter or operation (e.g. writing in read-mode). |
| FILEERROR_OUTOFMEMORY | Not enough memory. |
| FILEERROR_USERBREAK | User break. |
| FILEERROR_WRONG_VALUE | Other value detected than expected. |
| FILEERROR_CHUNK_NUMBER | Wrong number of chunks or sub-chunks detected. |
| FILEERROR_VALUE_NO_CHUNK | There was a value without any enclosing start/stop chunks. |
| FILEERROR_FILEEND | The file end was reached without finishing reading. |
| FILEERROR_UNKNOWN_VALUE | Unknown value detected. |
