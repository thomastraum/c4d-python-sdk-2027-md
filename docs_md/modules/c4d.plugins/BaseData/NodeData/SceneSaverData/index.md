<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseData/NodeData/SceneSaverData/index.html -->

# c4d.plugins.SceneSaverData <a id="c4d-plugins-scenesaverdata"></a>

## *class* `c4d.plugins.SceneSaverData` <a id="c4d.plugins.SceneSaverData"></a>

A data class for creating scene savers.  
Use [`RegisterSceneSaverPlugin()`](../../../index.md#c4d.plugins.RegisterSceneSaverPlugin) to register the plugin.

Parent Class:

- [`c4d.plugins.NodeData`](../index.md#c4d.plugins.NodeData)

## Overview <a id="overview"></a>

- [`SceneSaverData.Save()`](#c4d.plugins.SceneSaverData.Save): Override - Save the document.

## Members <a id="members"></a>

### Document Saving <a id="c4d.plugins.SceneSaverData-method-Document-Saving"></a>

#### `SceneSaverData.Save(self, node, name, doc, filterflags)` <a id="c4d.plugins.SceneSaverData.Save"></a>

Override - Save the document.

*Changed in version R15.057.*

> **Warning:**
>
> Calling `BaseDocument.GetDocumentPath()` from a scene saver invoked by [`SaveDocument()`](../../../../c4d.documents/index.md#c4d.documents.SaveDocument) is now consistent with the GUI behavior of the export.  
> `BaseDocument.GetDocumentPath()` now always returns the current path of the document instead of the target path of the file to save for all formats (except *Cinema 4D (*.c4d)* and *Cinema 4D XML (*.xml)*).  
> A new document flag **DOCUMENT_SAVEDOC_DESTINATIONPATH** (only set when saving) can be used in scene savers to get the destination path of the exported file.

**Parameters:**

- **node** ([*c4d.BaseList2D*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The node object.

- **name** (*str*) – The filename of the file to save.

- **doc** ([*c4d.documents.BaseDocument*](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document that the selected objects should be saved from.

- **filterflags** (*int*) –

  The possible flags are:

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
