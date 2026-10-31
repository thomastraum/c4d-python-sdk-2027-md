<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.documents/index.html -->

# c4d.documents <a id="c4d-documents"></a>

## *class* `c4d.documents` <a id="c4d.documents"></a>

- [`c4d.documents.BaseDocument`](BaseDocument/index.md#c4d.documents.BaseDocument)
- [`c4d.documents.BaseVideoPost`](BaseVideoPost/index.md#c4d.documents.BaseVideoPost)
- [`c4d.documents.BatchRender`](BatchRender/index.md#c4d.documents.BatchRender)
- [`c4d.documents.LayerObject`](LayerObject/index.md#c4d.documents.LayerObject)
- [`c4d.documents.RenderData`](RenderData/index.md#c4d.documents.RenderData)

## Overview <a id="overview"></a>

**Animation Timeline**

- [`c4d.documents.AddMarker()`](#c4d.documents.AddMarker): Inserts a timeline marker into the document at a given time.
- [`c4d.documents.GetFirstMarker()`](#c4d.documents.GetFirstMarker): Returns the first timeline marker of the document.
- [`c4d.documents.RunAnimation()`](#c4d.documents.RunAnimation): Controls the animation in the active document *doc*.
- [`c4d.documents.SetDocumentTime()`](#c4d.documents.SetDocumentTime): Controls the time of the active document doc.

**Asset Management**

- [`c4d.documents.GetAllAssets()`](#c4d.documents.GetAllAssets): Use [`c4d.documents.GetAllAssetsNew()`](#c4d.documents.GetAllAssetsNew).
- [`c4d.documents.GetAllAssetsNew()`](#c4d.documents.GetAllAssetsNew): Get all assets from a document.
- [`c4d.documents.SaveProject()`](#c4d.documents.SaveProject): Save the document as a project (menu *“Save Project with Assets”*).

**Document Lifecycle**

- [`c4d.documents.CloseAllDocuments()`](#c4d.documents.CloseAllDocuments): Closes all open documents in Cinema 4D.
- [`c4d.documents.InsertBaseDocument()`](#c4d.documents.InsertBaseDocument): Inserts a document into the Cinema 4D editor list of documents.
- [`c4d.documents.KillDocument()`](#c4d.documents.KillDocument): Removes and free all resources of this document.

**Document Navigation**

- [`c4d.documents.GetActiveDocument()`](#c4d.documents.GetActiveDocument): Returns the active document of Cinema 4D.
- [`c4d.documents.GetFirstDocument()`](#c4d.documents.GetFirstDocument): Returns the first document in the list of documents within Cinema 4D.
- [`c4d.documents.GetRecentDocumentsList()`](#c4d.documents.GetRecentDocumentsList): Retrieves the recent documents list.
- [`c4d.documents.SetActiveDocument()`](#c4d.documents.SetActiveDocument): Sets *doc* in the editor that the user is editing, this is the active document.

**File Operations**

- [`c4d.documents.LoadDocument()`](#c4d.documents.LoadDocument): Similar to `LoadFile()` but this time the document is not put into the editors list of documents and it gives control over the loaded document.
- [`c4d.documents.LoadFile()`](#c4d.documents.LoadFile): Loads a file into Cinema 4D and opens it.
- [`c4d.documents.MergeDocument()`](#c4d.documents.MergeDocument): Merges the file *name* into the document *doc*.
- [`c4d.documents.SaveDocument()`](#c4d.documents.SaveDocument): Saves the document to a file.

**Modeling And Framing**

- [`c4d.documents.FrameScene()`](#c4d.documents.FrameScene): Change the active camera framing of the passed document.
- [`c4d.documents.InteractiveModeling_Restart()`](#c4d.documents.InteractiveModeling_Restart): Used for modeling tools with GUI input.
- [`c4d.documents.IsolateObjects()`](#c4d.documents.IsolateObjects): A helper routine to copy the objects *t_objects* of document *doc* to a new document (returned).

**Rendering**

- [`c4d.documents.BakeOcioViewToBitmap()`](#c4d.documents.BakeOcioViewToBitmap): Bakes the OCIO transforms associated with *bmp* into the image.
- [`c4d.documents.GetBatchRender()`](#c4d.documents.GetBatchRender): Get the batch render instance.
- [`c4d.documents.RenderDocument()`](#c4d.documents.RenderDocument): Renders the document to a bitmap.
- [`c4d.documents.StopExternalRenderer()`](#c4d.documents.StopExternalRenderer): Stop the external renderer.

## Members <a id="members"></a>

### Animation Timeline <a id="c4d.documents-function-Animation-Timeline"></a>

#### `c4d.documents.AddMarker(doc, pPred, time, name)` <a id="c4d.documents.AddMarker"></a>

Inserts a timeline marker into the document at a given time. Optionally an insertion point *pPred* in the timeline marker list can be specified, giving the marker before the wanted insertion point.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document in which to insert.
- **pPred** (*Optional*[ [*c4d.BaseList2D*](../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]) – The optional timeline marker to use as list insertion point.
- **time** ([*c4d.BaseTime*](../c4d/BaseTime/index.md#c4d.BaseTime)) – The time position of the timeline marker.
- **name** (*str*) – The name of the timeline marker.

**Return type:** Optional[[c4d.BaseList2D](../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The added timeline marker, or **None** if insertion failed.

#### `c4d.documents.GetFirstMarker(doc)` <a id="c4d.documents.GetFirstMarker"></a>

Returns the first timeline marker of the document.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

**Return type:** [c4d.BaseList2D](../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

**Returns:** The first timeline marker.

#### `c4d.documents.RunAnimation(doc, stop, forward)` <a id="c4d.documents.RunAnimation"></a>

Controls the animation in the active document *doc*.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to control. Usually [`GetActiveDocument()`](#c4d.documents.GetActiveDocument)
- **stop** (*bool*) – If this is **True** the animation is stopped, otherwise it is running.
- **forward** (*bool*) – If this is **True** the direction is set to forward, otherwise it is set to backward.

**Return type:** bool

**Returns:** **True** on success, otherwise **False**

#### `c4d.documents.SetDocumentTime(doc, time)` <a id="c4d.documents.SetDocumentTime"></a>

Controls the time of the active document doc.

> **Note:** Unlike [`BaseDocument.SetTime()`](BaseDocument/index.md#c4d.documents.BaseDocument.SetTime) it handles running animation.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to control.
- **time** ([*c4d.BaseTime*](../c4d/BaseTime/index.md#c4d.BaseTime)) – The time to set.

**Return type:** bool

**Returns:** **True** on success, otherwise **False**

### Asset Management <a id="c4d.documents-function-Asset-Management"></a>

#### `c4d.documents.GetAllAssets(doc, allowDialogs, lastPath, flags=0)` <a id="c4d.documents.GetAllAssets"></a>

*Deprecated since version S22:* Use [`c4d.documents.GetAllAssetsNew()`](#c4d.documents.GetAllAssetsNew).

Get all assets from a document.  
It is e.g. used by *“Save Project with Assets”* menu and [`SaveProject()`](#c4d.documents.SaveProject).

*New in version R15.057.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to save as project.

- **allowDialogs** (*bool*) – If **True** the function can open dialogs. For example a file select dialog is opened if a node of the scene points to a file which does not exist anymore.

- **lastPath** (*str*) –

  Pass an empty string, that will be filled with the last path used.  
  If a file dialog is opened and the user selects the missing file on the harddisk, the folder of this asset is assigned to *lastPath*.  
  The developer can store this value somewhere and pass it next time so Cinema 4D knows where to look first before asking the user again.

- **flags** (*int*) –

  *New in version R20:* The flags to decide which assets should be collected:

  |   |   |
  |---|---|
  | *ASSETDATA_FLAG_NONE* | None. |
  | *ASSETDATA_FLAG_COLLECT_NODES_ASSETS* | Set to collect node asset infos as well. |
  | *ASSETDATA_FLAG_CURRENTFRAMEONLY* | Only return current frame assets. |
  | *ASSETDATA_FLAG_CURRENTTAKEONLY* | Only return current take assets. |
  | *ASSETDATA_FLAG_DONOTRESOLVE* | Set to get the original name, not resolved to the folder. |
  | *ASSETDATA_FLAG_MULTIPLEUSE* | Adds the same asset again for every usage. |
  | *ASSETDATA_FLAG_NET* | Set if NET is collecting assets to distribute them to the clients. |
  | *ASSETDATA_FLAG_NODOCUMENT* | Exclude the document itself from the asset list. |
  | *ASSETDATA_FLAG_NOMISSING* | Only existing assets will be included. |
  | *ASSETDATA_FLAG_NOSUBSTANCES* | Normally Substance assets are included with *ASSETDATA_FLAG_TEXTURESONLY* but with this flag they are not. |
  | *ASSETDATA_FLAG_TEXTURESONLY* | Only return texture assets. |
  | *ASSETDATA_FLAG_WITHCACHES* | Also return caches (Global Illumination / Ambient Occlusion). |
  | *ASSETDATA_FLAG_WITHFONTS* | Also return fonts. |

**Return type:** Optional[List[Dict]]

**Returns:**

The assets in the document, or **None** if there was an error.

The dictionary for each returned asset is:

> - *filename*: str: The asset filename.
> - *assetname*: str: The asset name.
> - *channelId*: int: The asset channel ID.
> - *netRequestOnDemand*: bool: NET request on demand.
> - *owner*: [`c4d.BaseList2D`](../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D): The owner object. Since R20.
> - *exists*: bool: Tells if the asset could be found. Since R20.
> - *paramId*: int: The parameter ID. Since R20.
> - *nodePath*: str: The node path of the port the asset is assigned to in case of a nimbus material. Since R20.
> - *nodeSpace*: str: The node space id in case of a nimbus material. Since R21.

#### `c4d.documents.GetAllAssetsNew(doc, allowDialogs, lastPath, flags=0, assetList=[])` <a id="c4d.documents.GetAllAssetsNew"></a>

Get all assets from a document.  
It is e.g. used by *“Save Project with Assets”* menu and [`SaveProject()`](#c4d.documents.SaveProject).

*New in version S22.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to get the assets from.

- **allowDialogs** (*bool*) – If **True** the function can open dialogs. For example a file select dialog is opened if a node of the scene points to a file which does not exist anymore.

- **lastPath** (*str*) –

  Pass an empty string, that will be filled with the last path used.  
  If a file dialog is opened and the user selects the missing file on the harddisk, the folder of this asset is assigned to *lastPath*.  
  The developer can store this value somewhere and pass it next time so Cinema 4D knows where to look first before asking the user again.

- **flags** (*int*) –

  The flags to decide which assets should be collected:

  |   |   |
  |---|---|
  | *ASSETDATA_FLAG_NONE* | None. |
  | *ASSETDATA_FLAG_COLLECT_NODES_ASSETS* | Set to collect node asset infos as well. |
  | *ASSETDATA_FLAG_CURRENTFRAMEONLY* | Only return current frame assets. |
  | *ASSETDATA_FLAG_CURRENTTAKEONLY* | Only return current take assets. |
  | *ASSETDATA_FLAG_DONOTRESOLVE* | Set to get the original name, not resolved to the folder. |
  | *ASSETDATA_FLAG_MULTIPLEUSE* | Adds the same asset again for every usage. |
  | *ASSETDATA_FLAG_NET* | Set if NET is collecting assets to distribute them to the clients. |
  | *ASSETDATA_FLAG_NODOCUMENT* | Exclude the document itself from the asset list. |
  | *ASSETDATA_FLAG_NOMISSING* | Only existing assets will be included. |
  | *ASSETDATA_FLAG_NOSUBSTANCES* | Normally Substance assets are included with *ASSETDATA_FLAG_TEXTURESONLY* but with this flag they are not. |
  | *ASSETDATA_FLAG_TEXTURESONLY* | Only return texture assets. |
  | *ASSETDATA_FLAG_WITHCACHES* | Also return caches (Global Illumination / Ambient Occlusion). |
  | *ASSETDATA_FLAG_WITHFONTS* | Also return fonts. |

- **assetList** (*List*[*Dict*]) –

  A list filled with assets in the document.

  The dictionary for each returned asset is:

  > - *filename*: str: The asset filename.
  > - *assetname*: str: The asset name.
  > - *channelId*: int: The asset channel ID.
  > - *netRequestOnDemand*: bool: NET request on demand.
  > - *owner*: [`c4d.BaseList2D`](../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D): The owner object. Since R20.
  > - *exists*: bool: Tells if the asset could be found. Since R20.
  > - *paramId*: int: The parameter ID. Since R20.
  > - *nodePath*: str: The node path of the port the asset is assigned to in case of a nimbus material. Since R20.
  > - *nodeSpace*: str: The node space id in case of a nimbus material. Since R21.

**Return type:** int

**Returns:**

The success state.

*New in version S22.*

| Symbol ID | Description |
|---|---|
| GETALLASSETSRESULT_FAILED | Function call went wrong. |
| GETALLASSETSRESULT_OK | Function succeeded and all assets exists. |
| GETALLASSETSRESULT_MISSING | Function succeeded but some assets cannot be found. |

#### `c4d.documents.SaveProject(doc, flags, targetPath, assets, missingAssets)` <a id="c4d.documents.SaveProject"></a>

Save the document as a project (menu *“Save Project with Assets”*).

*New in version R15.057.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to save as project.

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *SAVEPROJECT_NONE* | None. |
  | *SAVEPROJECT_ASSETS* | Pass if the assets will be taken into account. |
  | *SAVEPROJECT_SCENEFILE* | Pass if the scene will be taken into account. |
  | *SAVEPROJECT_DIALOGSALLOWED* | Show dialogs like error messages, a file selection for missing assets or alerts if necessary. |
  | *SAVEPROJECT_SHOWMISSINGASSETDIALOG* | If an asset is missing show a warning dialog. Flag can be set without *SAVEPROJECT_DIALOGSALLOWED*. |
  | *SAVEPROJECT_ADDTORECENTLIST* | Add document to the recent list. |
  | *SAVEPROJECT_DONTCOPYFILES* | Does the same as without this flag but does not copy the files to the destination. Flag used to simulate the function. |
  | *SAVEPROJECT_PROGRESSALLOWED* | Show the progress bar in the main window. |
  | *SAVEPROJECT_DONTTOUCHDOCUMENT* | Document will be in the same state as before the call was made. |
  | *SAVEPROJECT_DONTFAILONMISSINGASSETS* | If this flag is passed, the function does not fail anymore when assets are missing. |
  | *SAVEPROJECT_ISNET* | Private. Set only if NET module is collecting assets. |
  | *SAVEPROJECT_USEDOCUMENTNAMEASFILENAME* | Use the document name as the file name to save as project. |
  | *SAVEPROJECT_DONTCLEARSUGGESTEDFOLDER* | Do not change asset paths of nodes. |
  | *SAVEPROJECT_WITHCACHES* | *New in version R17.048:* Save the project assets with Global Illumination / Ambient Occlusion caches. See also *ASSETDATA_FLAG_WITHCACHES*. |
  | *SAVEPROJECT_DONTGENERATEPAINTTEX* | *New in version R17.053:* Does the same as without this flag but does not generate the textures from painted materials. |
  | *SAVEPROJECT_ASSETLINKS_COPY_FILEASSETS* | *New in version R24:* Copy file assets (assets://) to the tex folder. |
  | *SAVEPROJECT_ASSETLINKS_COPY_NODEASSETS* | *New in version R24:* Copy node assets to the scene repository. |

- **targetPath** (*str*) – The path to save the project to.

- **assets** (List[Dict[**filename**: str, **assetname**: str, **channelId**: int, **netRequestOnDemand**: bool]]) – Pass an empty list that will be filled with the found assets.

- **missingAssets** (List[Dict[**filename**: str, **assetname**: str, **channelId**: int, **netRequestOnDemand**: bool]) – Pass an empty list that will be filled with the missing assets.

**Return type:** bool

**Returns:** **True** if the document was successfully saved as a project, otherwise **False**.

```python
missingAssets = []
assets = []
targetPath = "some path"
res = c4d.documents.SaveProject(doc, c4d.SAVEPROJECT_ASSETS | c4d.SAVEPROJECT_SCENEFILE, targetPath, assets, missingAssets)
```

### Document Lifecycle <a id="c4d.documents-function-Document-Lifecycle"></a>

#### `c4d.documents.CloseAllDocuments()` <a id="c4d.documents.CloseAllDocuments"></a>

Closes all open documents in Cinema 4D.

#### `c4d.documents.InsertBaseDocument(doc)` <a id="c4d.documents.InsertBaseDocument"></a>

Inserts a document into the Cinema 4D editor list of documents.

> **Note:** [`SetActiveDocument()`](#c4d.documents.SetActiveDocument) is called implicitly.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to insert.

#### `c4d.documents.KillDocument(doc)` <a id="c4d.documents.KillDocument"></a>

Removes and free all resources of this document.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to free.

### Document Navigation <a id="c4d.documents-function-Document-Navigation"></a>

#### `c4d.documents.GetActiveDocument()` <a id="c4d.documents.GetActiveDocument"></a>

Returns the active document of Cinema 4D.

**Return type:** [c4d.documents.BaseDocument](BaseDocument/index.md#c4d.documents.BaseDocument)

**Returns:** The active document.

#### `c4d.documents.GetFirstDocument()` <a id="c4d.documents.GetFirstDocument"></a>

Returns the first document in the list of documents within Cinema 4D.

**Return type:** [c4d.documents.BaseDocument](BaseDocument/index.md#c4d.documents.BaseDocument)

**Returns:** The first document.

#### `c4d.documents.GetRecentDocumentsList(isBodyPaint=False)` <a id="c4d.documents.GetRecentDocumentsList"></a>

Retrieves the recent documents list.

*New in version R21.*

**Parameters:** **isBodyPaint** (*bool*) – **True** to retrieve BodyPaint’s list.

**Return type:** [`maxon.BaseArray`](../maxon_generated/datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) ([`maxon.Url`](../maxon_generated/references/io/maxon.Url.md#module-maxon.Url))

**Returns:** The recent documents list.

#### `c4d.documents.SetActiveDocument(doc)` <a id="c4d.documents.SetActiveDocument"></a>

Sets *doc* in the editor that the user is editing, this is the active document.

> **Warning:**
>
> It’s mandatory for *doc* to be already inserted into the Cinema 4D list of documents.  
> This can be done with [`InsertBaseDocument()`](#c4d.documents.InsertBaseDocument).

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

### File Operations <a id="c4d.documents-function-File-Operations"></a>

#### `c4d.documents.LoadDocument(name, loadflags, thread=None)` <a id="c4d.documents.LoadDocument"></a>

Similar to [`LoadFile()`](#c4d.documents.LoadFile) but this time the document is not put into the editors list of documents and it gives control over the loaded document.

**Parameters:**

- **name** (*Union*[*str*, [*c4d.storage.MemoryFileStruct*](../c4d.storage/MemoryFileStruct/index.md#c4d.storage.MemoryFileStruct)]) – The name of the file to load the document from.

- **loadflags** (*int*) –

  The scene filter flags for the loader:

  |   |   |
  |---|---|
  | *SCENEFILTER_NONE* | None. |
  | *SCENEFILTER_OBJECTS* | Load/save objects. |
  | *SCENEFILTER_MATERIALS* | Load/save materials. |
  | *SCENEFILTER_DIALOGSALLOWED* | Flag to inform a plugin that a dialog can be displayed. If this flag is not set then no dialogs must be opened. |
  | *SCENEFILTER_PROGRESSALLOWED* | Flag to inform a plugin that a progress bar can be displayed. The progress bar can be set by calling [`StatusSetBar()`](../c4d/index.md#c4d.StatusSetBar). |
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

- **thread** (*Optional*[[*c4d.threading.BaseThread*](../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)]) – The current thread, or **None** for the main Cinema 4D thread.

**Return type:** Optional[[c4d.documents.BaseDocument](BaseDocument/index.md#c4d.documents.BaseDocument)]

**Returns:** The document that was loaded, or **None** if it failed.

#### `c4d.documents.LoadFile(name)` <a id="c4d.documents.LoadFile"></a>

Loads a file into Cinema 4D and opens it.

<a id="loadfile-note"></a>

> **Note:** This function can be used to open any kind of file Cinema 4D handles i.e. a document, an image, a layout or a lib4d/cat4d file.

**Parameters:** **name** (*str*) – The file to load.

#### `c4d.documents.MergeDocument(doc, name, loadflags, thread)` <a id="c4d.documents.MergeDocument"></a>

Merges the file *name* into the document *doc*.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to merge the loaded document *name* into.

- **name** (*Union*[*str*, [*c4d.storage.MemoryFileStruct*](../c4d.storage/MemoryFileStruct/index.md#c4d.storage.MemoryFileStruct)]) – The file to merge into *doc*.

- **loadflags** (*int*) –

  The scene filter flags for the loader:

  |   |   |
  |---|---|
  | *SCENEFILTER_NONE* | None. |
  | *SCENEFILTER_OBJECTS* | Load/save objects. |
  | *SCENEFILTER_MATERIALS* | Load/save materials. |
  | *SCENEFILTER_DIALOGSALLOWED* | Flag to inform a plugin that a dialog can be displayed. If this flag is not set then no dialogs must be opened. |
  | *SCENEFILTER_PROGRESSALLOWED* | Flag to inform a plugin that a progress bar can be displayed. The progress bar can be set by calling [`StatusSetBar()`](../c4d/index.md#c4d.StatusSetBar). |
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

- **thread** (*Optional*[[*c4d.threading.BaseThread*](../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)]) – The current thread, or **None** for the main Cinema 4D thread.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `c4d.documents.SaveDocument(doc, name, saveflags, format)` <a id="c4d.documents.SaveDocument"></a>

Saves the document to a file.

> **See also:** Warning note in `SceneSaverData.Save()`.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – Command ID

- **name** (*Union*[*str*, [*c4d.storage.MemoryFileStruct*](../c4d.storage/MemoryFileStruct/index.md#c4d.storage.MemoryFileStruct)]) – File to save the document to.

- **saveflags** (*int*) –

  The flags

  |   |   |
  |---|---|
  | *SAVEDOCUMENTFLAGS_NONE* | None. |
  | *SAVEDOCUMENTFLAGS_DIALOGSALLOWED* | Flag to inform that a dialog can be displayed. If this flag is not set then no dialogs must be opened. |
  | *SAVEDOCUMENTFLAGS_SAVEAS* | Forces a “Save As” and opens the file dialog. |
  | *SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST* | Do not add the saved document to the recent file list. |
  | *SAVEDOCUMENTFLAGS_AUTOSAVE* | Sets the “Auto Save” mode. Is usually used in conjunction with *DONTADDTORECENTLIST*. |
  | *SAVEDOCUMENTFLAGS_SAVECACHES* | For *melange* export only. Caches of objects will also be written (only supported by Cinema 4D file format). |
  | *SAVEDOCUMENTFLAGS_EXPORTDIALOG* | Opens the Export dialog. |
  | *SAVEDOCUMENTFLAGS_CRASHSITUATION* | This flag is passed to Cinema 4D if a crash occurred. |
  | *SAVEDOCUMENTFLAGS_NO_SHADERCACHE* | Disables the *SCENEFILTER_SAVE_BINARYCACHE* flag. |

- **format** (*int*) –

  The file format to save the document as.

  |   |   |
  |---|---|
  | *FORMAT_PREF* | Preferences. |
  | *FORMAT_WAV* | WAV sound. |
  | *FORMAT_L4D* | Layout. |
  | *FORMAT_P4D* | Layout. |
  | *FORMAT_C4DIMPORT* | *Cinema 4D* import. |
  | *FORMAT_C4DEXPORT* | *Cinema 4D* export. |
  | *FORMAT_VRML1IMPORT* | VRML 1 import. |
  | *FORMAT_VRML1EXPORT* | VRML 1 export. |
  | *FORMAT_VRML2IMPORT* | VRML 2 import. |
  | *FORMAT_VRML2EXPORT* | VRML 2 export. |
  | *FORMAT_DXFIMPORT* | DXF import. |
  | *FORMAT_DXFEXPORT* | DXF export. |
  | *FORMAT_3DSIMPORT* | 3DS import. |
  | *FORMAT_3DSEXPORT* | 3DS export. |
  | *FORMAT_OBJIMPORT* | Old OBJ import (R16 and older). |
  | *FORMAT_OBJEXPORT* | Old OBJ export (R16 and older). |
  | *FORMAT_Q3DIMPORT* | QuickDraw 3D import. |
  | *FORMAT_Q3DEXPORT* | QuickDraw 3D export. |
  | *FORMAT_AIIMPORT* | AI import. |
  | *FORMAT_DEMIMPORT* | DEM import. |
  | *FORMAT_D3DEXPORT* | *Direct3D* export. |
  | *FORMAT_OBJ2IMPORT* | *New in version R17.048:* New OBJ import (R17 and newer). |
  | *FORMAT_OBJ2EXPORT* | *New in version R17.048:* New OBJ export (R17 and newer). |
  | *FORMAT_SKPIMPORT* | *New in version R17.048:* SketchUp import. |
  | *FORMAT_STEPIMPORT* | *New in version R20.026:* Step import. |
  | *FORMAT_CATIAIMPORT* | *New in version R20.026:* Catia V5 import. |
  | *FORMAT_IGESIMPORT* | *New in version R20.026:* Iges import. |
  | *FORMAT_JTIMPORT* | *New in version R20.026:* Jt import. |
  | *FORMAT_SOLIDWORKSIMPORT* | *New in version R20.026:* Solidworks import. |
  | *FORMAT_ABCIMPORT* | *New in version R20.041:* Alembic import (R20.041 and newer). |
  | *FORMAT_ABCEXPORT* | *New in version R20.041:* Alembic export (R20.041 and newer). |
  | *FORMAT_DAE14IMPORT* | *New in version R20.041:* Collada 14 import (R20.041 and newer). |
  | *FORMAT_DAE14EXPORT* | *New in version R20.041:* Collada 14 export (R20.041 and newer). |
  | *FORMAT_DAE15IMPORT* | *New in version R20.041:* Collada 15 import (R20.041 and newer). |
  | *FORMAT_DAE15EXPORT* | *New in version R20.041:* Collada 15 export (R20.041 and newer). |
  | *FORMAT_AI_EXPORT* | *New in version S22:* Adobe Illustrator AI export. |
  | *FORMAT_ALLPLAN_EXPORT* | *New in version S22:* Allplan XML export. |
  | *FORMAT_BVH_IMPORT* | *New in version S22:* BVH import. |
  | *FORMAT_FBX_EXPORT* | *New in version S22:* FBX export. |
  | *FORMAT_FBX_IMPORT* | *New in version S22:* FBX import. |
  | *FORMAT_GLTFEXPORT* | *New in version S22:* glTF export. |
  | *FORMAT_DWG_IMPORT* | *New in version S22:* AutoCAD DWG import. |
  | *FORMAT_STL_EXPORT* | *New in version S22:* STL export. |
  | *FORMAT_STL_IMPORT* | *New in version S22:* STL import. |
  | *FORMAT_VDB_EXPORT* | *New in version S22:* Volume VDB export. |
  | *FORMAT_VDB_IMPORT* | *New in version S22:* Volume VDB import. |

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Modeling And Framing <a id="c4d.documents-function-Modeling-And-Framing"></a>

#### `c4d.documents.FrameScene(doc, mode)` <a id="c4d.documents.FrameScene"></a>

Change the active camera framing of the passed document.

*New in version 2026.0.0.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to frame.

- **mode** (*int*) –

  The framing mode.

  | Key | Description |
  |---|---|
  | OVERVIEW_DEFAULT | Frame Default. |
  | OVERVIEW_AKTU | Frame Selected Objects |
  | OVERVIEW_SCENE | Frame Geometry. |
  | OVERVIEW_COMPLETE | Frame All. |
  | OVERVIEW_SELECTED | Frame Selected Elements. |
  | OVERVIEW_COMPLETE_SQUARE | Emulates a square view and then does. |

#### `c4d.documents.InteractiveModeling_Restart(doc)` <a id="c4d.documents.InteractiveModeling_Restart"></a>

Used for modeling tools with GUI input.  
Applies the last modeling undo so that new values of the modeling tool can be applied.

An example from the edge cut code.

```python
import c4d

class TestTool(c4d.plugins.ToolData):

    def MouseInput(self, doc, data, draw, win, msg):
        if not doc: return False

        if doc.GetMode() == c4d.Medges:
            active = p.GetActiveObjects(True)

        # Undo step before
        c4d.documents.InteractiveModeling_Restart(doc)

        self.ModelingEdgeCut(active, c4d.MODELINGCOMMANDMODE_EDGESELECTION, data, doc, win, msg, True)
        c4d.EventAdd()

        return True
```

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `c4d.documents.IsolateObjects(doc, t_objects)` <a id="c4d.documents.IsolateObjects"></a>

A helper routine to copy the objects *t_objects* of document *doc* to a new document (returned).

> **Note:** All materials associated are also copied over and the links are corrected.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document that contains the objects in *t_objects*.
- **t_objects** (*List*[[*c4d.BaseObject*](../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – The objects to isolate.

**Return type:** [c4d.documents.BaseDocument](BaseDocument/index.md#c4d.documents.BaseDocument)

**Returns:** The document containing the isolated objects.

### Rendering <a id="c4d.documents-function-Rendering"></a>

#### `c4d.documents.BakeOcioViewToBitmap(bmp, renderData, flags)` <a id="c4d.documents.BakeOcioViewToBitmap"></a>

Bakes the OCIO transforms associated with *bmp* into the image.

*New in version 2025.2.0.*

This primarily intended for baking OCIO data to sRGB for displaying purposes within Cinema 4D, as for example baking RenderDocument images for the Picture Viewer.

**Parameters:**

- **bmp** ([*c4d.bitmaps.BaseBitmap*](../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – Bitmap to bake. This should be the result of [`c4d.documents.RenderDocument()`](#c4d.documents.RenderDocument).

- **renderData** ([*c4d.documents.RenderData*](RenderData/index.md#c4d.documents.RenderData)) – Render data that was used to render the document.

- **flags** (*int*) –

  Save bits.

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

**Returns:** Baked bitmap or *None* if the bitmap does not need to be baked

**Return type:** [c4d.bitmaps.BaseBitmap](../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)

#### `c4d.documents.GetBatchRender()` <a id="c4d.documents.GetBatchRender"></a>

Get the batch render instance.

**Return type:** [c4d.documents.BatchRender](BatchRender/index.md#c4d.documents.BatchRender)

**Returns:** The batch render.

#### `c4d.documents.RenderDocument(doc, rdata, bmp, renderflags=0, th=None, prog=None, wprog=None)` <a id="c4d.documents.RenderDocument"></a>

Renders the document to a bitmap. You need to initialize the image with the size of the render data

> **Note:** A [`MultipassBitmap`](../c4d.bitmaps/BaseBitmap/MultipassBitmap/index.md#c4d.bitmaps.MultipassBitmap) must be passed to render the image with an alpha channel.

See the [rendering examples](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/rendering) for details on how to use this function.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](BaseDocument/index.md#c4d.documents.BaseDocument)) – The document you want to render.

- **rdata** ([*c4d.BaseContainer*](../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The render data.

- **bmp** ([*c4d.bitmaps.BaseBitmap*](../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The bitmap where the rendered picture will be saved in. Initialize the image with the size of the render data.

- **renderflags** (*int*) –

  Some renderflags.

  |   |   |
  |---|---|
  | *RENDERFLAGS_NONE* | Default flag which can lead to unexpected results. See *RENDERFLAGS_EXTERNAL*. |
  | *RENDERFLAGS_EXTERNAL* | Enables using render engines other than the standard renderer. When this flag is not set, Cinema 4D will fall back to what it considers the “standard” engine in its context (either Standard or Redshift when it is installed). So, when you render data set for example the Hardware Preview renderer or a third party render engine, Cinema 4D will ignore that engine choice and use the standard engine instead; unless you set this flag. Setting this flag will also entail a ‘full fidelity’ render, in the sense that caches are being busted and rebuilt with full render quality. |
  | *RENDERFLAGS_NODOCUMENTCLONE* | Suppresses the document being cloned for rendering, even when *RENDERFLAGS_EXTERNAL* is set. This is a performance optimization but not recommended for final renderings. |
  | *RENDERFLAGS_SHOWERRORS* | If to show error messages of the renderer. |
  | *RENDERFLAGS_PREVIEWRENDER* | Many subsystems check for this flag to produce lower quality results, as used in material previews or the asset browser. Is not related to the hardware preview renderer. |
  | *RENDERFLAGS_IRR* | An interactive render region render. |
  | *RENDERFLAGS_CREATE_PICTUREVIEWER* | Returns the rendering in a new Picture Viewer instance. |
  | *RENDERFLAGS_OPEN_PICTUREVIEWER* | Opens the rendering in the Picture Viewer. |
  | *RENDERFLAGS_KEEP_CONTEXT* | Private. |
  | *RENDERFLAGS_BATCHRENDER* | Private. |
  | *RENDERFLAGS_NET* | Use NET for rendering. |
  | *RENDERFLAGS_DONTANIMATE* | Do not animate document before rendering. This should only be used in combination with *RENDERFLAGS_PREVIEWRENDER*. |
  | *RENDERFLAGS_PREVIEWSETTINGS* | Use preview settings. |
  | *RENDERFLAGS_RENDERQUEUEERRORS* | Cancel Render Queue rendering if scene has missing assets. |
  | *RENDERFLAGS_FORCE_LINEAR_COLOR_PROFILE* | Forces a linear color profile on the render bitmap in some settings. |
  | *RENDERFLAGS_OCIO_RAW_RENDERING* | Shorthand for setting *RDATA_BAKE_OCIO_VIEW_TRANSFORM_RENDER* according to the color management settings of the document. This will cause OCIO documents to return render results in raw render space, instead of having data baked down. Will have no effect on documents which are not using OCIO color management. |
  | *RENDERFLAGS_OCIO_BAKE_RENDERING* | Shorthand for calling [`BakeOcioViewToBitmap`](#c4d.documents.BakeOcioViewToBitmap) on the render result bitmap, baking down all OCIO transforms as if Cinema 4D would when saving the rendering to disk, depending on the passed render settings. This only affects the returned render bitmap. .. warning:: Setting this flag will cause the bake result to be copied into the render result bitmap. Using [`BakeOcioViewToBitmap`](#c4d.documents.BakeOcioViewToBitmap) manually is faster as it does not copy data and should be preferred in performance critical code paths. |
  | *RENDERFLAGS_AUTO_SETUP* | Alias for *EXTERNAL \| OCIO_RAW_RENDERING*. This is the recommended flags combination to use as a base for most rendering tasks. |
  | *RENDERFLAGS_INTERNAL_USE_CURRENT_QUEUE* | Internal. |
  | *RENDERFLAGS_INTERNAL_SPECIAL_PREVIEW* | Internal. |

  > **Note:** If you are in a safe context you might use *RENDERFLAG_NODOCUMENTCLONE* to speed up the render process especially on big scenes.

- **th** (*Optional*[[*c4d.threading.BaseThread*](../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)]) – The thread to test for a break or **None**.

- **prog** (*Optional*[*Callable*[[*float*, *int*], *None*]]) –

  *New in version R21.*

  A function that will be called during the rendering with information about the current progress.

  The expected function signature is *functionName(p, progress_type)* and parameters correspond to:

  > - p (float): The progress, between 0.0 and 1.0.
  >
  > - progress_type: The render Progress type:
  >
  >   > *New in version R21.*
  >   >
  >   > | Symbol ID | Description |
  >   > |---|---|
  >   > | RENDERPROGRESSTYPE_BEFORERENDERING | Before rendering. |
  >   > | RENDERPROGRESSTYPE_DURINGRENDERING | During rendering. |
  >   > | RENDERPROGRESSTYPE_AFTERRENDERING | After rendering. |
  >   > | RENDERPROGRESSTYPE_GLOBALILLUMINATION | GI prepass. |
  >   > | RENDERPROGRESSTYPE_QUICK_PREVIEW | Quick Preview rendering. |
  >   > | RENDERPROGRESSTYPE_AMBIENTOCCLUSION | AO prepass. |

- **wprog** (*Optional*[*Callable*[[*int*, *Optional*[[*c4d.bitmaps.BaseBitmap*](../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)], *str*, *bool*, *int*, *int*, *int*, *str*], *None*]]) –

  *New in version R21.*

  The write progress hook for the render operation.

  The expected function signature is *functionName(mode, bmp, fn, mainImage, frame, renderTime, streamnum, streamname)* and parameters correspond to:

  > - mode: the write mode type:
  >
  >   > | Symbol ID | Description |
  >   > |---|---|
  >   > | WRITEMODE_STANDARD | Standard. |
  >   > | WRITEMODE_ASSEMBLE_MOVIE | Assemble movie. |
  >   > | WRITEMODE_ASSEMBLE_SINGLEIMAGE | Assemble single image. |
  >
  > - bmp ([`c4d.bitmaps.BaseBitmap`](../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)): The bitmap written to. Can be **None**.
  >
  > - fn (str): The filename where the file is going to be written to.
  >
  > - mainImage (bool): **True** for main image, otherwise **False**.
  >
  > - frame (int): The frame number.
  >
  > - renderTime (int): The bitmap frame time.
  >
  > - streamnum (int): The stream number.
  >
  > - streamname (str): The stream name.

**Return type:** int

**Returns:**

|   |   |
|---|---|
| *RENDERRESULT_OK* | Function was successful. |
| *RENDERRESULT_OUTOFMEMORY* | Not enough memory. |
| *RENDERRESULT_ASSETMISSING* | Assets (textures etc.) are missing. |
| *RENDERRESULT_SAVINGFAILED* | Failed to save. |
| *RENDERRESULT_USERBREAK* | User stopped the processing. |
| *RENDERRESULT_GICACHEMISSING* | GI cache is missing. |
| *RENDERRESULT_NOMACHINE* | Machine was not found. Can only happen during Team Rendering. |
| *RENDERRESULT_PROJECTNOTFOUND* | Project was not found. Can only be returned by Cinema 4D during command line rendering. |
| *RENDERRESULT_ERRORLOADINGPROJECT* | There was an error while loading the project. Can only be returned by Cinema 4D during command line rendering. |
| *RENDERRESULT_NOOUTPUTSPECIFIED* | Output was not specified. Can only be returned by Cinema 4D during command line rendering. |

#### `c4d.documents.StopExternalRenderer()` <a id="c4d.documents.StopExternalRenderer"></a>

Stop the external renderer.

**Return type:** bool

**Returns:** **True** if the rendering has been canceled, otherwise **False**.
