<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.documents/BaseDocument/index.html -->

# c4d.documents.BaseDocument <a id="c4d-documents-basedocument"></a>

## *class* `c4d.documents.BaseDocument` <a id="c4d.documents.BaseDocument"></a>

This object contains the complete description of a scene.

> **Note:** Remember that you need to call [`StopAllThreads()`](../../c4d/index.md#c4d.StopAllThreads) before making modifications to a user scene.

Parent Class:

- [`c4d.BaseList2D`](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

## Overview <a id="overview"></a>

- [`BaseDocument.GetBasicColorConverter()`](#c4d.documents.BaseDocument.GetBasicColorConverter): Returns a fallback converter that can be used instead of a document specific OCIO converter in case of errors.
- [`BaseDocument.GetColorConverterForActiveDocument()`](#c4d.documents.BaseDocument.GetColorConverterForActiveDocument): Returns a converter to convert colors along the OCIO conversion paths defined by the currently active document.

**Animation Keying**

- [`BaseDocument.AutoKey()`](#c4d.documents.BaseDocument.AutoKey): Compares the object chain *op* to *undo* and sets keyframes for all the changes.
- [`BaseDocument.GetDefaultKey()`](#c4d.documents.BaseDocument.GetDefaultKey): Retrieves the document’s default keying settings.
- [`BaseDocument.GetTrackDefaultInterpolationMode()`](#c4d.documents.BaseDocument.GetTrackDefaultInterpolationMode): Gets the track default interpolation mode.
- [`BaseDocument.Record()`](#c4d.documents.BaseDocument.Record): Records the active objects in the document.
- [`BaseDocument.RecordKey()`](#c4d.documents.BaseDocument.RecordKey): Records a key for *op* at *time*.
- [`BaseDocument.SetDefaultKey()`](#c4d.documents.BaseDocument.SetDefaultKey): Sets the document’s default keying settings.
- [`BaseDocument.SetTrackDefaultInterpolationMode()`](#c4d.documents.BaseDocument.SetTrackDefaultInterpolationMode): Sets the track default interpolation mode.

**Color Conversion**

- [`BaseDocument.GetColorConverter()`](#c4d.documents.BaseDocument.GetColorConverter): Returns a converter to convert colors along the OCIO conversion paths defined by the settings of this document.
- [`BaseDocument.GetThumbnailColorConverter()`](#c4d.documents.BaseDocument.GetThumbnailColorConverter): Returns a converter to convert thumbnail colors along the OCIO conversion paths defined by the settings of this document.

**Color Management**

- [`BaseDocument.CopyLinearWorkflow()`](#c4d.documents.BaseDocument.CopyLinearWorkflow): Copies the settings for linear workflow and OCIO configurations to another document.
- [`BaseDocument.GetActiveOcioColorSpacesNames()`](#c4d.documents.BaseDocument.GetActiveOcioColorSpacesNames): Gets the name of the OCIO color spaces.
- [`BaseDocument.GetColorSpaceIdFromName()`](#c4d.documents.BaseDocument.GetColorSpaceIdFromName): Gets the index of a color space that is defined by category and its name.
- [`BaseDocument.GetNameFromColorSpaceId()`](#c4d.documents.BaseDocument.GetNameFromColorSpaceId): Gets the name of a color space that is defined by category and index.
- [`BaseDocument.GetOcioColorSpaceNames()`](#c4d.documents.BaseDocument.GetOcioColorSpaceNames): Gets the names of all color spaces that are defined by the current configuration.
- [`BaseDocument.GetOcioColorSpacesPopupMenu()`](#c4d.documents.BaseDocument.GetOcioColorSpacesPopupMenu): Gets the names of all color spaces as menu items to be used as a menu.
- [`BaseDocument.GetOcioConfigPath()`](#c4d.documents.BaseDocument.GetOcioConfigPath): Gets the path of the OCIO configuration file.
- [`BaseDocument.GetOcioDisplayColorSpaceNames()`](#c4d.documents.BaseDocument.GetOcioDisplayColorSpaceNames): Gets the names of all display color spaces that are defined by the current configuration.
- [`BaseDocument.GetOcioProfiles()`](#c4d.documents.BaseDocument.GetOcioProfiles): Gets the OCIO color profiles.
- [`BaseDocument.GetOcioRenderingColorSpaceNames()`](#c4d.documents.BaseDocument.GetOcioRenderingColorSpaceNames): Gets the names of all rendering color spaces that are defined by the current configuration.
- [`BaseDocument.GetOcioViewTransformNames()`](#c4d.documents.BaseDocument.GetOcioViewTransformNames): Gets the names of all view transforms that are defined by the current configuration.
- [`BaseDocument.UpdateOcioColorSpaces()`](#c4d.documents.BaseDocument.UpdateOcioColorSpaces): Updates the OCIO spaces that are stored internally in the document.

**Deprecated**

- [`BaseDocument.GetData()`](#c4d.documents.BaseDocument.GetData): Get the [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer) settings of the specified *type*.
- [`BaseDocument.GetOrderedActiveObjects()`](#c4d.documents.BaseDocument.GetOrderedActiveObjects): Use `GetActiveObjects()` with the corresponding flag instead.

**Document Lifecycle**

- [`BaseDocument.Flush()`](#c4d.documents.BaseDocument.Flush): Empties the document, deleting and freeing all resources used.
- [`BaseDocument.GetChanged()`](#c4d.documents.BaseDocument.GetChanged): Checks if the document has been changed since it was last saved.
- [`BaseDocument.IsBlank()`](#c4d.documents.BaseDocument.IsBlank): Checks if the scene contains any elements.
- [`BaseDocument.SetChanged()`](#c4d.documents.BaseDocument.SetChanged): Set the changed state of the document to reflect it has been modified.

**Document Settings**

- [`BaseDocument.GetDocumentData()`](#c4d.documents.BaseDocument.GetDocumentData): Get the [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer) settings of the specified *type*.
- [`BaseDocument.GetSettingsInstance()`](#c4d.documents.BaseDocument.GetSettingsInstance): Returns the internal settings object.
- [`BaseDocument.SetDocumentData()`](#c4d.documents.BaseDocument.SetDocumentData): Merges the [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer) for the settings of the specified *type*.

**Dynamics Cache**

- [`BaseDocument.HasUncachedDynamicMograph()`](#c4d.documents.BaseDocument.HasUncachedDynamicMograph): Checks if the scene contains uncached dynamic MoGraph effects.
- [`BaseDocument.HasUncachedDynamics()`](#c4d.documents.BaseDocument.HasUncachedDynamics): Checks if the scene contains uncached dynamics.

**Editor Configuration**

- [`BaseDocument.GetAction()`](#c4d.documents.BaseDocument.GetAction): Get the ID of the current active tool in the editor.
- [`BaseDocument.GetActiveToolData()`](#c4d.documents.BaseDocument.GetActiveToolData): Gets the original tool data container.
- [`BaseDocument.GetMode()`](#c4d.documents.BaseDocument.GetMode): Get the main mode of the editor.
- [`BaseDocument.GetSplinePlane()`](#c4d.documents.BaseDocument.GetSplinePlane): Get the plane in which the splines are created, such as XY plane.
- [`BaseDocument.IsAxisEnabled()`](#c4d.documents.BaseDocument.IsAxisEnabled): Returns the state of the object axis modifier.
- [`BaseDocument.IsEditMode()`](#c4d.documents.BaseDocument.IsEditMode): Check if the editor is in an editable mode.
- [`BaseDocument.SetAction()`](#c4d.documents.BaseDocument.SetAction): Set the current tool in the editor.
- [`BaseDocument.SetMode()`](#c4d.documents.BaseDocument.SetMode): Set the main mode of the editor.

**File Identity**

- [`BaseDocument.GetDocumentName()`](#c4d.documents.BaseDocument.GetDocumentName): Returns the file name of the document.
- [`BaseDocument.GetDocumentPath()`](#c4d.documents.BaseDocument.GetDocumentPath): Returns the path of the document.
- [`BaseDocument.SetDocumentName()`](#c4d.documents.BaseDocument.SetDocumentName): Set the file name of the document.
- [`BaseDocument.SetDocumentPath()`](#c4d.documents.BaseDocument.SetDocumentPath): Set the path of the document.

**Frame Rate**

- [`BaseDocument.GetFps()`](#c4d.documents.BaseDocument.GetFps): Returns the fps of the document.
- [`BaseDocument.SetFps()`](#c4d.documents.BaseDocument.SetFps): Set the frames per second.

**Level Of Detail**

- [`BaseDocument.GetLOD()`](#c4d.documents.BaseDocument.GetLOD): Get the Level of Detail for this document.
- [`BaseDocument.GetRenderLod()`](#c4d.documents.BaseDocument.GetRenderLod): Get if the level of detail for rendering should be used in the editor.
- [`BaseDocument.SetLOD()`](#c4d.documents.BaseDocument.SetLOD): Get the Level of Detail for this document.
- [`BaseDocument.SetRenderLod()`](#c4d.documents.BaseDocument.SetRenderLod): Set the level of detail for rendering.

**Magic Methods**

- [`BaseDocument.__init__()`](#c4d.documents.BaseDocument.__init__)

**Materials And Textures**

- [`BaseDocument.GetActiveMaterial()`](#c4d.documents.BaseDocument.GetActiveMaterial): Returns the active selected material.
- [`BaseDocument.GetAllTextures()`](#c4d.documents.BaseDocument.GetAllTextures): Returns a collection of all used textures in the document and optionally only for the objects in *ar*.
- [`BaseDocument.GetFirstMaterial()`](#c4d.documents.BaseDocument.GetFirstMaterial): Returns the first material.
- [`BaseDocument.GetMaterials()`](#c4d.documents.BaseDocument.GetMaterials): Returns all materials in a list.
- [`BaseDocument.InsertMaterial()`](#c4d.documents.BaseDocument.InsertMaterial): Inserts the material into the document’s material list.
- [`BaseDocument.SearchMaterial()`](#c4d.documents.BaseDocument.SearchMaterial): Search for a material with the same case sensitive name.
- [`BaseDocument.SetActiveMaterial()`](#c4d.documents.BaseDocument.SetActiveMaterial): Modifies the current multi selection with *op*, depending on *mode*.

**Object Processing**

- [`BaseDocument.AnimateObject()`](#c4d.documents.BaseDocument.AnimateObject): Animate a node in this document at the given time.
- [`BaseDocument.ExecutePasses()`](#c4d.documents.BaseDocument.ExecutePasses): Animate the current frame of the document.
- [`BaseDocument.Polygonize()`](#c4d.documents.BaseDocument.Polygonize): Make a clone of the document and turn all objects into polygon based objects.

**Pick Sessions**

- [`BaseDocument.GetPickSession()`](#c4d.documents.BaseDocument.GetPickSession): Returns information about the current pick session.
- [`BaseDocument.StartPickSession()`](#c4d.documents.BaseDocument.StartPickSession): Starts a pick session.
- [`BaseDocument.StopPickSession()`](#c4d.documents.BaseDocument.StopPickSession): Ends the pick session.

**Preview And Takes**

- [`BaseDocument.GetDocPreviewBitmap()`](#c4d.documents.BaseDocument.GetDocPreviewBitmap): Get the preview bitmap of the document.
- [`BaseDocument.GetTakeData()`](#c4d.documents.BaseDocument.GetTakeData): Gets the take data for the document.

**Render Settings**

- [`BaseDocument.GetActiveRenderData()`](#c4d.documents.BaseDocument.GetActiveRenderData): Returns the active selected render data.
- [`BaseDocument.GetFirstRenderData()`](#c4d.documents.BaseDocument.GetFirstRenderData): Gets the first render data or options of the document.
- [`BaseDocument.InsertRenderData()`](#c4d.documents.BaseDocument.InsertRenderData): Inserts the render data into the document’s render settings hierarchy.
- [`BaseDocument.InsertRenderDataLast()`](#c4d.documents.BaseDocument.InsertRenderDataLast): Inserts the render data as last child into the document’s render data list.
- [`BaseDocument.SetActiveRenderData()`](#c4d.documents.BaseDocument.SetActiveRenderData): Sets the active render settings for the document, these are the settings that are used for rendering.

**Scene Structure**

- [`BaseDocument.GetFirstObject()`](#c4d.documents.BaseDocument.GetFirstObject): Returns the first object.
- [`BaseDocument.GetHighest()`](#c4d.documents.BaseDocument.GetHighest): The first object in object manager hierarchy of type *type*.
- [`BaseDocument.GetLayerObjectRoot()`](#c4d.documents.BaseDocument.GetLayerObjectRoot): Returns the list of layers of the document.
- [`BaseDocument.GetObjects()`](#c4d.documents.BaseDocument.GetObjects): Returns the highest objects without children.
- [`BaseDocument.InsertObject()`](#c4d.documents.BaseDocument.InsertObject): Inserts the object into the document’s object hierarchy.
- [`BaseDocument.SearchObject()`](#c4d.documents.BaseDocument.SearchObject): Search for an object with the same case sensitive name.

**Scene Systems**

- [`BaseDocument.FindSceneHook()`](#c4d.documents.BaseDocument.FindSceneHook): Finds a scene hook by ID.
- [`BaseDocument.GetParticleSystem()`](#c4d.documents.BaseDocument.GetParticleSystem): Returns the particle master system of the document.
- [`BaseDocument.GetSceneRepository()`](#c4d.documents.BaseDocument.GetSceneRepository): Returns the SceneRepository description.
- [`BaseDocument.SendInfo()`](#c4d.documents.BaseDocument.SendInfo): Sends *MSG_DOCUMENTINFO* messages.

**Selection Management**

- [`BaseDocument.GetActiveMaterials()`](#c4d.documents.BaseDocument.GetActiveMaterials): Returns the material selection.
- [`BaseDocument.GetActiveObject()`](#c4d.documents.BaseDocument.GetActiveObject): Returns the active selected object.
- [`BaseDocument.GetActiveObjects()`](#c4d.documents.BaseDocument.GetActiveObjects): Returns the object selection.
- [`BaseDocument.GetActiveObjectsFilter()`](#c4d.documents.BaseDocument.GetActiveObjectsFilter): Returns the active object multi selection and removes objects that do not match the filter given by type and instanceof.
- [`BaseDocument.GetActiveTag()`](#c4d.documents.BaseDocument.GetActiveTag): Returns the active selected tag.
- [`BaseDocument.GetActiveTags()`](#c4d.documents.BaseDocument.GetActiveTags): Returns the tag selection.
- [`BaseDocument.GetHelperAxis()`](#c4d.documents.BaseDocument.GetHelperAxis): Get the helper axis for the current multi selection.
- [`BaseDocument.GetRealActiveObject()`](#c4d.documents.BaseDocument.GetRealActiveObject): Returns the active object or the dummy axis if multiple objects are selected.
- [`BaseDocument.GetSelection()`](#c4d.documents.BaseDocument.GetSelection): Returns the selection of materials, tags and objects in a list.
- [`BaseDocument.GetTargetObject()`](#c4d.documents.BaseDocument.GetTargetObject): Gets the target object within a multi-selection.
- [`BaseDocument.SetActiveObject()`](#c4d.documents.BaseDocument.SetActiveObject): Modifies the current multi selection with *op*, depending on *mode*.
- [`BaseDocument.SetActiveTag()`](#c4d.documents.BaseDocument.SetActiveTag): Sets a tag be the currently active one.
- [`BaseDocument.SetSelection()`](#c4d.documents.BaseDocument.SetSelection): Sets the active selection.
- [`BaseDocument.SetTargetObject()`](#c4d.documents.BaseDocument.SetTargetObject): Sets the target object within a multi-selection.

**Timeline Playback**

- [`BaseDocument.GetLoopMaxTime()`](#c4d.documents.BaseDocument.GetLoopMaxTime): Returns the time of the right boundary of the document’s preview range (loop range).
- [`BaseDocument.GetLoopMinTime()`](#c4d.documents.BaseDocument.GetLoopMinTime): Returns the time of the left boundary of the document’s preview range (loop range).
- [`BaseDocument.GetMaxTime()`](#c4d.documents.BaseDocument.GetMaxTime): Get the end time for the timeline of this document.
- [`BaseDocument.GetMinTime()`](#c4d.documents.BaseDocument.GetMinTime): Get the starting time for the timeline of this document.
- [`BaseDocument.GetTime()`](#c4d.documents.BaseDocument.GetTime): Returns the min time.
- [`BaseDocument.SetLoopMaxTime()`](#c4d.documents.BaseDocument.SetLoopMaxTime): Sets the right boundary of the document’s preview range (loop range) to the given time.
- [`BaseDocument.SetLoopMinTime()`](#c4d.documents.BaseDocument.SetLoopMinTime): Sets the left boundary of the document’s preview range (loop range) to the given time.
- [`BaseDocument.SetMaxTime()`](#c4d.documents.BaseDocument.SetMaxTime): Set the end time of the timeline for this document.
- [`BaseDocument.SetMinTime()`](#c4d.documents.BaseDocument.SetMinTime): Set the starting time for the timeline of this document.
- [`BaseDocument.SetRewind()`](#c4d.documents.BaseDocument.SetRewind): Rewinds the whole document (from time 0 to current time) when the next event *EVMSG_CHANGE* or [`DrawViews()`](../../c4d/index.md#c4d.DrawViews) is processed.
- [`BaseDocument.SetTime()`](#c4d.documents.BaseDocument.SetTime): Set the current time for this documents timeline.

**Undo Management**

- [`BaseDocument.AddUndo()`](#c4d.documents.BaseDocument.AddUndo): Adds an undo *type* to the list of undo operations started with `StartUndo()`.
- [`BaseDocument.DoRedo()`](#c4d.documents.BaseDocument.DoRedo): Perform a redo on this document (undo the last undo).
- [`BaseDocument.DoUndo()`](#c4d.documents.BaseDocument.DoUndo): Perform an undo operation, same as the user selecting Undo from within Cinema 4D.
- [`BaseDocument.EndUndo()`](#c4d.documents.BaseDocument.EndUndo): End the building of multiple undo actions into a single user undo.
- [`BaseDocument.FindUndoPtr()`](#c4d.documents.BaseDocument.FindUndoPtr): Returns the last undo state of the Cinema 4D element bl (object, tag, material, etc.) for the specified undo action type.
- [`BaseDocument.FlushUndoBuffer()`](#c4d.documents.BaseDocument.FlushUndoBuffer): Flushes the complete undo + redo buffer.
- [`BaseDocument.GetUndoPtr()`](#c4d.documents.BaseDocument.GetUndoPtr): Returns the element of the last undo action.
- [`BaseDocument.StartUndo()`](#c4d.documents.BaseDocument.StartUndo): Tells Cinema 4D to start building a list of undos into a single undo action for the user.

**Viewport Display**

- [`BaseDocument.ForceCreateBaseDraw()`](#c4d.documents.BaseDocument.ForceCreateBaseDraw): Makes sure that `GetBaseDraw()` (0) is accessible.
- [`BaseDocument.GetActiveBaseDraw()`](#c4d.documents.BaseDocument.GetActiveBaseDraw): Get the activate BaseDraw in the editor, this is where all drawing should be performed.
- [`BaseDocument.GetBaseDraw()`](#c4d.documents.BaseDocument.GetBaseDraw): Returns the BaseDraw hook of the editor *bd*.
- [`BaseDocument.GetBaseDrawCount()`](#c4d.documents.BaseDocument.GetBaseDrawCount): Get the [`BaseDraw`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw) count in the editor view.
- [`BaseDocument.GetDrawTime()`](#c4d.documents.BaseDocument.GetDrawTime): Get the editor redraw time.
- [`BaseDocument.GetRenderBaseDraw()`](#c4d.documents.BaseDocument.GetRenderBaseDraw): This is the BaseDraw belonging to the view that the user has chosen as ‘Render View’ (see View menu in Cinema 4D).

## Members <a id="members"></a>

### Color Conversion <a id="c4d.documents.BaseDocument-staticmethod-Color-Conversion"></a>

#### *static* `BaseDocument.GetBasicColorConverter()` <a id="c4d.documents.BaseDocument.GetBasicColorConverter"></a>

Returns a fallback converter that can be used instead of a document specific OCIO converter in case of errors.

*New in version 2025.2.0.*

**Returns:** The dummy color converter.

**Return type:** [c4d.modules.render.OcioConverter](../../c4d.modules/render/OcioConverter/index.md#c4d.modules.render.OcioConverter)

#### *static* `BaseDocument.GetColorConverterForActiveDocument()` <a id="c4d.documents.BaseDocument.GetColorConverterForActiveDocument"></a>

Returns a converter to convert colors along the OCIO conversion paths defined by the currently active document.

*New in version 2025.2.0.*

**Returns:** The converter for the active document or the dummy converter if there is no active document.

**Return type:** [c4d.modules.render.OcioConverter](../../c4d.modules/render/OcioConverter/index.md#c4d.modules.render.OcioConverter)

### Animation Keying <a id="c4d.documents.BaseDocument-method-Animation-Keying"></a>

#### `BaseDocument.AutoKey(self, op, undo, recursive, pos, scale, rot, param, pla)` <a id="c4d.documents.BaseDocument.AutoKey"></a>

Compares the object chain *op* to *undo* and sets keyframes for all the changes.

*New in version R16.021.*

**Parameters:**

- **op** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object chain to add the keys to.
- **undo** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The object chain to compare to. This is necessary e.g. for autokeyframing so that Cinema 4D can compare values. Usually this is the object from the undo buffer.
- **recursive** (*bool*) – If **True** then the function applies to all children of *op* as well. The hierarchy of *op* and *undo* must match.
- **pos** (*bool*) – If **True** keyframes are added for differences in position.
- **scale** (*bool*) – If **True** keyframes are added for differences in scale.
- **rot** (*bool*) – If **True** keyframes are added for differences in rotation.
- **param** (*bool*) – If **True** keyframes are added for differences in parameters.
- **pla** (*bool*) – If **True** keyframes are added as PLA for differences in point positions.

#### `BaseDocument.GetDefaultKey(self)` <a id="c4d.documents.BaseDocument.GetDefaultKey"></a>

Retrieves the document’s default keying settings.

*New in version R19.*

**Return type:** Optional[Tuple[[c4d.CKey](../../c4d/C4DAtom/CKey/index.md#c4d.CKey), bool]]

**Returns:**

A tuple containing a key with the document’s default settings and a bool giving the document’s default overdub state.  
**None** if the function failed.

#### `BaseDocument.GetTrackDefaultInterpolationMode(self)` <a id="c4d.documents.BaseDocument.GetTrackDefaultInterpolationMode"></a>

Gets the track default interpolation mode.

*New in version 24.*

**Returns:**

Interpolation mode.

| Symbol ID | Description |
|---|---|
| R23 | Hermite evaluation with some tangent issues. |
| CURRENT | Spline evaluation. |

**Return type:** int

#### `BaseDocument.Record(self)` <a id="c4d.documents.BaseDocument.Record"></a>

Records the active objects in the document.

*New in version R19.*

#### `BaseDocument.RecordKey(self, op, id, time, undo, autoKey, eval_attribmanager)` <a id="c4d.documents.BaseDocument.RecordKey"></a>

Records a key for *op* at *time*.

*New in version R16.021.*

**Parameters:**

- **op** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The object to record.

- **id** ([*c4d.DescID*](../../c4d/DescID/index.md#c4d.DescID)) – The description ID to record.

- **time** ([*c4d.BaseTime*](../../c4d/BaseTime/index.md#c4d.BaseTime)) – The time to record.

- **undo** (*Optional*[[*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]) –

  The object in the old state.  
  This is necessary e.g. for autokeyframing so that Cinema 4D can compare values  
  Usually this is the object from the undo buffer.  
  To record keys (no autokeying) **None** can be passed.

- **autoKey** (*bool*) – If **True** then autokeying is used and undo needs to be passed for comparison.

- **eval_attribmanager** (*bool*) – Evaluate attributes manager.

**Return type:** bool

**Returns:** **True** if successful, otherwise *False*.

#### `BaseDocument.SetDefaultKey(self, key, overdub)` <a id="c4d.documents.BaseDocument.SetDefaultKey"></a>

Sets the document’s default keying settings.

*New in version R19.*

**Parameters:**

- **key** ([*c4d.CKey*](../../c4d/C4DAtom/CKey/index.md#c4d.CKey)) – The key to set the new default document’s settings.

- **overdub** (*bool*) –

  The new document’s default overdub.  
  If a keyframe already exists, the existing keyframe’s interpolation type will be maintained when a new keyframe is recorded (only the value key will be overwritten).

#### `BaseDocument.SetTrackDefaultInterpolationMode(self, mode)` <a id="c4d.documents.BaseDocument.SetTrackDefaultInterpolationMode"></a>

Sets the track default interpolation mode.

*New in version 24.*

**Parameters:**

**mode** (*int*) –

Interpolation mode.

| Symbol ID | Description |
|---|---|
| R23 | Hermite evaluation with some tangent issues. |
| CURRENT | Spline evaluation. |

### Color Conversion <a id="c4d.documents.BaseDocument-method-Color-Conversion"></a>

#### `BaseDocument.GetColorConverter(self)` <a id="c4d.documents.BaseDocument.GetColorConverter"></a>

Returns a converter to convert colors along the OCIO conversion paths defined by the settings of this document.

*New in version 2025.2.0.*

**Returns:** The color converter that belongs to the document. If OCIO is not active or if there was an error to create the OCIO converter a dummy is returned.

**Return type:** [c4d.modules.render.OcioConverter](../../c4d.modules/render/OcioConverter/index.md#c4d.modules.render.OcioConverter)

#### `BaseDocument.GetThumbnailColorConverter(self)` <a id="c4d.documents.BaseDocument.GetThumbnailColorConverter"></a>

Returns a converter to convert thumbnail colors along the OCIO conversion paths defined by the settings of this document.

*New in version 2025.2.0.*

**Returns:** The color converter that belongs to the document for thumbnails. If OCIO is not active or if there was an error to create the OCIO converter a dummy is returned.

**Return type:** [c4d.modules.render.OcioConverter](../../c4d.modules/render/OcioConverter/index.md#c4d.modules.render.OcioConverter)

### Color Management <a id="c4d.documents.BaseDocument-method-Color-Management"></a>

#### `BaseDocument.CopyLinearWorkflow(self, src, dst, isMaterialPreview)` <a id="c4d.documents.BaseDocument.CopyLinearWorkflow"></a>

Copies the settings for linear workflow and OCIO configurations to another document.

*New in version 2025.2.0.*

**Parameters:**

- **src** ([*c4d.documents.BaseDocument*](#c4d.documents.BaseDocument)) – Document from where the settings are read.
- **dst** ([*c4d.documents.BaseDocument*](#c4d.documents.BaseDocument)) – Document in which the settings should be copied.
- **isMaterialPreview** (*bool*) – Must be set to True, if the document is a preview render document.

#### `BaseDocument.GetActiveOcioColorSpacesNames(self)` <a id="c4d.documents.BaseDocument.GetActiveOcioColorSpacesNames"></a>

Gets the name of the OCIO color spaces.

*New in version 2025.2.0.*

**Return type:** Tuple[str, str, str, str]

**Returns:**

A tuple with the following information:

str: Rendering color space name.  
str: Display color space name.  
str: View transform for rendering name.  
str: View transform for thumbnails name.

#### `BaseDocument.GetColorSpaceIdFromName(self, category, name)` <a id="c4d.documents.BaseDocument.GetColorSpaceIdFromName"></a>

Gets the index of a color space that is defined by category and its name.

*New in version 2025.2.0.*

**Parameters:**

- **category** (*int*) –

  One of these values:

  - DOCUMENT_OCIO_INPUT_COLORSPACE
  - DOCUMENT_OCIO_RENDER_COLORSPACE
  - DOCUMENT_OCIO_VIEW_TRANSFORM
  - DOCUMENT_OCIO_VIEW_TRANSFORM_THUMBNAILS
  - DOCUMENT_OCIO_DISPLAY_COLORSPACE

- **name** (*str*) – Name of a color space within the list that is specified by category.

**Returns:** The index of the corresponding colorspace.

**Return type:** int

#### `BaseDocument.GetNameFromColorSpaceId(self, category, index)` <a id="c4d.documents.BaseDocument.GetNameFromColorSpaceId"></a>

Gets the name of a color space that is defined by category and index. Returns an empty string if category or index are out of range.

*New in version 2025.2.0.*

**Parameters:**

- **category** (*int*) –

  One of these values:

  - DOCUMENT_OCIO_INPUT_COLORSPACE
  - DOCUMENT_OCIO_RENDER_COLORSPACE
  - DOCUMENT_OCIO_VIEW_TRANSFORM
  - DOCUMENT_OCIO_VIEW_TRANSFORM_THUMBNAILS
  - DOCUMENT_OCIO_DISPLAY_COLORSPACE

- **index** (*int*) – Index within the list that is specified by category.

**Returns:** The name of the corresponding colorspace.

**Return type:** str

#### `BaseDocument.GetOcioColorSpaceNames(self)` <a id="c4d.documents.BaseDocument.GetOcioColorSpaceNames"></a>

Gets the names of all color spaces that are defined by the current configuration.

*New in version 2025.2.0.*

**Returns:** A list containing the names of the color spaces.

**Return type:** list[str]

#### `BaseDocument.GetOcioColorSpacesPopupMenu(self)` <a id="c4d.documents.BaseDocument.GetOcioColorSpacesPopupMenu"></a>

Gets the names of all color spaces as menu items to be used as a menu.

*New in version 2025.2.0.*

**Returns:** A BaseContainer containing the names of all color spaces.

**Return type:** [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)

#### `BaseDocument.GetOcioConfigPath(self, fullPath=True)` <a id="c4d.documents.BaseDocument.GetOcioConfigPath"></a>

Gets the path of the OCIO configuration file.

*New in version 2025.2.0.*

> **Note:** If the path is set to “$OCIO” by the user, the path is taken from the environment variable “OCIO”.

**Parameters:** **fullPath** (*bool*) – If fullPath is set to True, the full path is returned, otherwise the string that is entered in the document settings.

**Returns:** OCIO config path.

**Return type:** str

#### `BaseDocument.GetOcioDisplayColorSpaceNames(self)` <a id="c4d.documents.BaseDocument.GetOcioDisplayColorSpaceNames"></a>

Gets the names of all display color spaces that are defined by the current configuration.

*New in version 2025.2.0.*

**Returns:** A list containing the names of the display color spaces.

**Return type:** list[str]

#### `BaseDocument.GetOcioProfiles(self)` <a id="c4d.documents.BaseDocument.GetOcioProfiles"></a>

Gets the OCIO color profiles.

*New in version 2025.2.0.*

**Return type:** Tuple[[c4d.bitmaps.ColorProfile](../../c4d.bitmaps/ColorProfile/index.md#c4d.bitmaps.ColorProfile), [c4d.bitmaps.ColorProfile](../../c4d.bitmaps/ColorProfile/index.md#c4d.bitmaps.ColorProfile), [c4d.bitmaps.ColorProfile](../../c4d.bitmaps/ColorProfile/index.md#c4d.bitmaps.ColorProfile), [c4d.bitmaps.ColorProfile](../../c4d.bitmaps/ColorProfile/index.md#c4d.bitmaps.ColorProfile)]

**Returns:**

A tuple with the following information:

c4d.bitmaps.ColorProfile: Rendering color space.  
c4d.bitmaps.ColorProfile: Display color space.  
c4d.bitmaps.ColorProfile: View transform for rendering.  
c4d.bitmaps.ColorProfile: View transform for thumbnails.

#### `BaseDocument.GetOcioRenderingColorSpaceNames(self)` <a id="c4d.documents.BaseDocument.GetOcioRenderingColorSpaceNames"></a>

Gets the names of all rendering color spaces that are defined by the current configuration.

*New in version 2025.2.0.*

**Returns:** A list containing the names of the rendering color spaces.

**Return type:** list[str]

#### `BaseDocument.GetOcioViewTransformNames(self)` <a id="c4d.documents.BaseDocument.GetOcioViewTransformNames"></a>

Gets the names of all view transforms that are defined by the current configuration.

*New in version 2025.2.0.*

**Returns:** A list containing the names of the view transforms.

**Return type:** list[str]

#### `BaseDocument.UpdateOcioColorSpaces(self)` <a id="c4d.documents.BaseDocument.UpdateOcioColorSpaces"></a>

Updates the OCIO spaces that are stored internally in the document. Should be called after CopyLinearWorkflow.

*New in version 2025.2.0.*

### Deprecated <a id="c4d.documents.BaseDocument-method-Deprecated"></a>

#### `BaseDocument.GetData(self, type)` <a id="c4d.documents.BaseDocument.GetData"></a>

*Deprecated since version R16:* [`GetDocumentData()`](#c4d.documents.BaseDocument.GetDocumentData) should be used instead.

Get the [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer) settings of the specified *type*.

**Parameters:** **type** (*int*) – The **DOCUMENTSETTINGS** type of the settings to get. See [DOCUMENTSETTINGS](../../../consts/DOCUMENTSETTINGS.md).

**Return type:** [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The settings for the document.

#### `BaseDocument.GetOrderedActiveObjects(self)` <a id="c4d.documents.BaseDocument.GetOrderedActiveObjects"></a>

*Deprecated since version R13.051:* Use [`GetActiveObjects()`](#c4d.documents.BaseDocument.GetActiveObjects) with the corresponding flag instead.

Returns the objects in an ordered list.

**Return type:** List[[c4d.BaseList2D](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The oredered list.

### Document Lifecycle <a id="c4d.documents.BaseDocument-method-Document-Lifecycle"></a>

#### `BaseDocument.Flush(self)` <a id="c4d.documents.BaseDocument.Flush"></a>

Empties the document, deleting and freeing all resources used.

#### `BaseDocument.GetChanged(self)` <a id="c4d.documents.BaseDocument.GetChanged"></a>

Checks if the document has been changed since it was last saved.

**Return type:** bool

**Returns:** **True** if the document has been changed.

#### `BaseDocument.IsBlank(self)` <a id="c4d.documents.BaseDocument.IsBlank"></a>

Checks if the scene contains any elements.

*New in version 2025.0.0.*

**Returns:** True if the scene is considered empty.

**Return type:** bool

#### `BaseDocument.SetChanged(self)` <a id="c4d.documents.BaseDocument.SetChanged"></a>

Set the changed state of the document to reflect it has been modified.

### Document Settings <a id="c4d.documents.BaseDocument-method-Document-Settings"></a>

#### `BaseDocument.GetDocumentData(self, type)` <a id="c4d.documents.BaseDocument.GetDocumentData"></a>

Get the [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer) settings of the specified *type*.

*New in version R16.021.*

> **Warning:**
>
> Use [`GetSettingsInstance()`](#c4d.documents.BaseDocument.GetSettingsInstance) to retrieve **DOCUMENTSETTINGS_TOOLS**.  
> [`GetDocumentData()`](#c4d.documents.BaseDocument.GetDocumentData) does not return these settings.

**Parameters:** **type** (*int*) – The **DOCUMENTSETTINGS** type of the settings to get. See [DOCUMENTSETTINGS](../../../consts/DOCUMENTSETTINGS.md).

**Return type:** [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The settings for the document.

#### `BaseDocument.GetSettingsInstance(self, type)` <a id="c4d.documents.BaseDocument.GetSettingsInstance"></a>

Returns the internal settings object.

> **Note:** Changes to the returned container are reflected in the document so it is not needed to call [`SetDocumentData()`](#c4d.documents.BaseDocument.SetDocumentData) manually.

> **Warning:**
>
> Use [`GetDocumentData()`](#c4d.documents.BaseDocument.GetDocumentData)/[`SetDocumentData()`](#c4d.documents.BaseDocument.SetDocumentData) to retrieve/change **DOCUMENTSETTINGS_GENERAL**.  
> [`GetSettingsInstance()`](#c4d.documents.BaseDocument.GetSettingsInstance) does not return these settings.

**Parameters:** **type** (*int*) – The **DOCUMENTSETTINGS** type of the settings to get. See [DOCUMENTSETTINGS](../../../consts/DOCUMENTSETTINGS.md).

**Return type:** [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The settings for the document.

#### `BaseDocument.SetDocumentData(self, type, bc)` <a id="c4d.documents.BaseDocument.SetDocumentData"></a>

Merges the [`BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer) for the settings of the specified *type*.

*New in version R16.021.*

> **Warning:**
>
> Use [`GetSettingsInstance()`](#c4d.documents.BaseDocument.GetSettingsInstance) to change **DOCUMENTSETTINGS_TOOLS**.  
> [`SetDocumentData()`](#c4d.documents.BaseDocument.SetDocumentData) does not affect these settings.

**Parameters:**

- **type** (*int*) – The **DOCUMENTSETTINGS** type of the settings to merge for the document. See [DOCUMENTSETTINGS](../../../consts/DOCUMENTSETTINGS.md).
- **bc** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The container to take the new settings from.

### Dynamics Cache <a id="c4d.documents.BaseDocument-method-Dynamics-Cache"></a>

#### `BaseDocument.HasUncachedDynamicMograph(self)` <a id="c4d.documents.BaseDocument.HasUncachedDynamicMograph"></a>

Checks if the scene contains uncached dynamic MoGraph effects.

*New in version 2025.0.0.*

This includes field lists in deformers and effectors. Function return False when all objects are cached or no dynamic MoGraph effects were found.

**Returns:** True if dynamic MoGraph elements that are not cached are present, otherwise False.

**Return type:** bool

#### `BaseDocument.HasUncachedDynamics(self)` <a id="c4d.documents.BaseDocument.HasUncachedDynamics"></a>

Checks if the scene contains uncached dynamics.

*New in version 2024.0.0.*

Even the scene contains i.e. cloth, rope or dynamics objects/tags this function still return False when all objects are cached. :return: True if dynamics that are not cached are present, otherwise False. :rtype: bool

### Editor Configuration <a id="c4d.documents.BaseDocument-method-Editor-Configuration"></a>

#### `BaseDocument.GetAction(self)` <a id="c4d.documents.BaseDocument.GetAction"></a>

Get the ID of the current active tool in the editor.

**Return type:** int

**Returns:** The ID.

#### `BaseDocument.GetActiveToolData(self)` <a id="c4d.documents.BaseDocument.GetActiveToolData"></a>

Gets the original tool data container.

> **Note:** The container is alive until the host object is freed.

**Return type:** [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** Tool data container.

#### `BaseDocument.GetMode(self)` <a id="c4d.documents.BaseDocument.GetMode"></a>

Get the main mode of the editor.

**Return type:** int

**Returns:**

The value:

|   |   |
|---|---|
| *Mcamera* | Camera mode. |
| *Mobject* | Object mode. |
| *Mtexture* | Texture mode. |
| *Mtextureaxis* | Texture axis mode. |
| *Mpoints* | Point edit mode. |
| *Medges* | Edge edit mode. |
| *Mpolygons* | Polygon edit mode. |
| *Manimation* | Animation mode. |
| *Mkinematic* | IK mode. |
| *Mmodel* | Model mode. |
| *Mpaint* | Paint mode. |
| *Muvpoints* | UV points mode. |
| *Muvpolygons* | UV polygons mode. |
| *Mdrag* | Drag mode. |
| *Mpolyedgepoint* | Combined poly/edge/point mode. Must only be used in [`ViewportSelect`](../../c4d.utils/ViewportSelect/index.md#c4d.utils.ViewportSelect). |
| *Medgepoint* | Combined edge/point mode. Must only be used in [`ViewportSelect`](../../c4d.utils/ViewportSelect/index.md#c4d.utils.ViewportSelect). |
| *Mworkplane* | Workplane mode. |
| *Mdrag* | Drag mode. |
| *Muvedges* | Uv Edge node is enabled. |
| *Muvon* | Uv mode is enabled. |

#### `BaseDocument.GetSplinePlane(self)` <a id="c4d.documents.BaseDocument.GetSplinePlane"></a>

Get the plane in which the splines are created, such as XY plane.

**Return type:** int

**Returns:**

Values for this are:

|   |   |
|---|---|
| *PRIM_PLANE_XY* | XY plane. |
| *PRIM_PLANE_ZY* | ZY plane. |
| *PRIM_PLANE_XZ* | XZ plane. |

#### `BaseDocument.IsAxisEnabled(self)` <a id="c4d.documents.BaseDocument.IsAxisEnabled"></a>

Returns the state of the object axis modifier.

*New in version R14.014.*

> **Note:** *c4d.CallCommand(12102)* toggles the tool.

**Return type:** bool

**Returns:** **True** if the object axis modifier is enabled, otherwise **False**.

#### `BaseDocument.IsEditMode(self)` <a id="c4d.documents.BaseDocument.IsEditMode"></a>

Check if the editor is in an editable mode.

> **Note:** This checks if [`GetMode()`](#c4d.documents.BaseDocument.GetMode) is *Mpoints*, *Medges* or *Mpolygons*.

**Return type:** bool

**Returns:** **True** if the editor is in point/poly editing mode.

#### `BaseDocument.SetAction(self, a)` <a id="c4d.documents.BaseDocument.SetAction"></a>

Set the current tool in the editor.

**Parameters:** **a** (*int*) – The values are *ID_MODELING_MOVE*, *ID_MODELING_SCALE*, *ID_MODELING_ROTATE* etc. The IDs are listed in *modelingids.h*.

#### `BaseDocument.SetMode(self, m)` <a id="c4d.documents.BaseDocument.SetMode"></a>

Set the main mode of the editor.

**Parameters:**

**m** (*int*) –

The value:

|   |   |
|---|---|
| *Mcamera* | Camera mode. |
| *Mobject* | Object mode. |
| *Mtexture* | Texture mode. |
| *Mtextureaxis* | Texture axis mode. |
| *Mpoints* | Point edit mode. |
| *Medges* | Edge edit mode. |
| *Mpolygons* | Polygon edit mode. |
| *Manimation* | Animation mode. |
| *Mkinematic* | IK mode. |
| *Mmodel* | Model mode. |
| *Mpaint* | Paint mode. |
| *Muvpoints* | UV points mode. |
| *Muvpolygons* | UV polygons mode. |
| *Mdrag* | Drag mode. |
| *Mpolyedgepoint* | Combined poly/edge/point mode. Must only be used in [`ViewportSelect`](../../c4d.utils/ViewportSelect/index.md#c4d.utils.ViewportSelect). |
| *Medgepoint* | Combined edge/point mode. Must only be used in [`ViewportSelect`](../../c4d.utils/ViewportSelect/index.md#c4d.utils.ViewportSelect). |
| *Mworkplane* | Workplane mode. |
| *Mdrag* | Drag mode. |
| *Muvedges* | Uv Edge node is enabled. |
| *Muvon* | Uv mode is enabled. |

### File Identity <a id="c4d.documents.BaseDocument-method-File-Identity"></a>

#### `BaseDocument.GetDocumentName(self)` <a id="c4d.documents.BaseDocument.GetDocumentName"></a>

Returns the file name of the document.

**Return type:** str

**Returns:**

The file name of the document.

> **Note:** If the document has not been saved then the name is in the form ‘Untitled 1’, for instance for the first unsaved document.

#### `BaseDocument.GetDocumentPath(self)` <a id="c4d.documents.BaseDocument.GetDocumentPath"></a>

Returns the path of the document.

**Return type:** str

**Returns:**

The path of the document.

> **Note:** If the document has not been saved then the path is empty.

#### `BaseDocument.SetDocumentName(self, name)` <a id="c4d.documents.BaseDocument.SetDocumentName"></a>

Set the file name of the document.

> **Note:** *name* must contain the filename part only.

**Parameters:** **name** (*str*) – The file name part of the document to set.

#### `BaseDocument.SetDocumentPath(self, path)` <a id="c4d.documents.BaseDocument.SetDocumentPath"></a>

Set the path of the document.

> **Note:** *path* must contain the path part only.

**Parameters:** **path** (*str*) – The path part of the document to set.

### Frame Rate <a id="c4d.documents.BaseDocument-method-Frame-Rate"></a>

#### `BaseDocument.GetFps(self)` <a id="c4d.documents.BaseDocument.GetFps"></a>

Returns the fps of the document.

**Return type:** int

**Returns:** The fps

#### `BaseDocument.SetFps(self, fps)` <a id="c4d.documents.BaseDocument.SetFps"></a>

Set the frames per second.

**Parameters:** **fps** (*int*) – The fps.

### Level Of Detail <a id="c4d.documents.BaseDocument-method-Level-Of-Detail"></a>

#### `BaseDocument.GetLOD(self)` <a id="c4d.documents.BaseDocument.GetLOD"></a>

Get the Level of Detail for this document.

**Return type:** float

**Returns:**

The default level of detail values are:

|   |   |
|---|---|
| Low | 0.25 |
| Medium | 0.5 |
| High | 1.0 |

#### `BaseDocument.GetRenderLod(self)` <a id="c4d.documents.BaseDocument.GetRenderLod"></a>

Get if the level of detail for rendering should be used in the editor.

**Return type:** bool

**Returns:** **True** if using the render lod.

#### `BaseDocument.SetLOD(self, lod)` <a id="c4d.documents.BaseDocument.SetLOD"></a>

Get the Level of Detail for this document.

**Parameters:**

**lod** (*float*) –

The default level of detail values are:

|   |   |
|---|---|
| Low | 0.25 |
| Medium | 0.5 |
| High | 1.0 |

#### `BaseDocument.SetRenderLod(self, lod)` <a id="c4d.documents.BaseDocument.SetRenderLod"></a>

Set the level of detail for rendering.

**Parameters:** **lod** (*bool*) – **True** if using the render lod.

### Magic Methods <a id="c4d.documents.BaseDocument-method-Magic-Methods"></a>

#### `BaseDocument.__init__(self)` <a id="c4d.documents.BaseDocument.__init__"></a>

### Materials And Textures <a id="c4d.documents.BaseDocument-method-Materials-And-Textures"></a>

#### `BaseDocument.GetActiveMaterial(self)` <a id="c4d.documents.BaseDocument.GetActiveMaterial"></a>

Returns the active selected material.

**Return type:** Optional[[c4d.BaseMaterial](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial)]

**Returns:** The active material, or **None**.

#### `BaseDocument.GetAllTextures(self, isNet=True, ar=None)` <a id="c4d.documents.BaseDocument.GetAllTextures"></a>

Returns a collection of all used textures in the document and optionally only for the objects in *ar*.

> **Note:**
>
> If *isNet* is passed **True** (default) then the function only delivers the textures of the current take.  
> Set the parameter to **False** to get all.

**Parameters:**

- **isNet** (*bool*) –

  *New in version R16.021:* Pass **True** (default) to retrieve the textures used in the current NET rendering.

- **ar** (*Optional*[*List*[[*c4d.C4DAtom*](../../c4d/C4DAtom/index.md#c4d.C4DAtom)]]) – An atom array to get the textures for. If **None** (default), all used textures in the document will be returned.

**Return type:** [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** A container with all filenames of used textures in the document.

#### `BaseDocument.GetFirstMaterial(self)` <a id="c4d.documents.BaseDocument.GetFirstMaterial"></a>

Returns the first material.

**Return type:** Optional[[c4d.BaseMaterial](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial)]

**Returns:** The active material, or **None**.

#### `BaseDocument.GetMaterials(self)` <a id="c4d.documents.BaseDocument.GetMaterials"></a>

Returns all materials in a list.

**Return type:** List[[c4d.BaseMaterial](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial)]

**Returns:** The list of all materials.

#### `BaseDocument.InsertMaterial(self, op, pred=None, checknames=True)` <a id="c4d.documents.BaseDocument.InsertMaterial"></a>

Inserts the material into the document’s material list.  
Optionally you can specify the insertion position with the pred parameter, giving the material before (just to the left of) the wanted position.  
Otherwise the material is inserted at the first position in the list.

**Parameters:**

- **op** ([*c4d.BaseMaterial*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial)) – Material to insert into the document.

- **pred** (*Optional*[[*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) –

  Optional insertion point for the material.

  > **Note:**
  >
  > Require condition *pred.GetDocument()==op.GetDocument()==op*.  
  > That means, the object has to be in the same document.

- **checknames** (*bool*) – Check for duplicate names and append .1, .2 etc.

#### `BaseDocument.SearchMaterial(self, name)` <a id="c4d.documents.BaseDocument.SearchMaterial"></a>

Search for a material with the same case sensitive name.

**Parameters:** **name** (*str*) – The name of the material to search for.

**Return type:** Optional[[c4d.BaseMaterial](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial)]

**Returns:** The material or **None** if nothing was found.

#### `BaseDocument.SetActiveMaterial(self, mp, mode=0)` <a id="c4d.documents.BaseDocument.SetActiveMaterial"></a>

Modifies the current multi selection with *op*, depending on *mode*.

> **Note:**
>
> `BaseDocument.GetActiveMaterial()` Should be called afterward to update the internal selection state.

**Parameters:**

- **mp** ([*c4d.BaseMaterial*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial)) – The material to set active.

- **mode** (*int*) –

  The selection flag:

  |   |   |
  |---|---|
  | *SELECTION_NEW* | Starts a new selection. |
  | *SELECTION_ADD* | Adds to the current selection |
  | *SELECTION_SUB* | Subtracts from the current selection. |

### Object Processing <a id="c4d.documents.BaseDocument-method-Object-Processing"></a>

#### `BaseDocument.AnimateObject(self, op, time, flags)` <a id="c4d.documents.BaseDocument.AnimateObject"></a>

Animate a node in this document at the given time.

> **Note:** Does not take expressions into account.

**Parameters:**

- **op** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – This is the node to animate.

- **time** ([*c4d.BaseTime*](../../c4d/BaseTime/index.md#c4d.BaseTime)) – The time at which it is being animated.

- **flags** (*int*) –

  Flags:

  | Key | Description |
  |---|---|
  | ANIMATEFLAGS_NONE | None. |
  | ANIMATEFLAGS_NO_PARTICLES | Ignore particles. |
  | ANIMATEFLAGS_NO_CHILDREN | Do not animate children. |
  | ANIMATEFLAGS_INRENDER | Prepare to render scene. |
  | ANIMATEFLAGS_NO_MINMAX | Private. |
  | ANIMATEFLAGS_NO_NLA | Private. |
  | ANIMATEFLAGS_NLA_SUM | Private. |
  | ANIMATEFLAGS_PARAMETER_TRACKS | *New in version 2024.5:* Private |

#### `BaseDocument.ExecutePasses(self, bt, animation, expressions, caches, flags)` <a id="c4d.documents.BaseDocument.ExecutePasses"></a>

Animate the current frame of the document.  
To update the editor you then need to send an update message using [`c4d.EventAdd()`](../../c4d/index.md#c4d.EventAdd).

**Parameters:**

- **bt** (*Optional*[ [*c4d.threading.BaseThread*](../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)]) – This thread can either be **None** (for the main Cinema 4D thread) or if you are within your own thread then you pass the thread.

- **animation** (*bool*) – Animations are evaluated.

- **expressions** (*bool*) – Expressions are evaluated.

- **caches** (*bool*) – Caches are evaluated.

- **flags** (*int*) –

  Flags:

  | Symbol ID | Description |
  |---|---|
  | BUILDFLAGS_NONE | The object is being built with no special context. This flag being set as the only flag is extremely rare and the actual ‘default’ flag is *BUILDFLAGS_INTERACTIVEEDITOR*. |
  | BUILDFLAGS_INTERNALRENDERER | The object is being built for the internal render event. |
  | BUILDFLAGS_EXTERNALRENDERER | The object is being built for an external render event. This covers the vast majority of render events these days. It is also common practice to check both render flags in tandem and treat them as one context. |
  | BUILDFLAGS_ISOPARM | The object is being built for its iso-parametric representation, you must return a [`c4d.LineObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/LineObject/index.md#c4d.LineObject) that is the iso-parametric representation of your object. |
  | BUILDFLAGS_EXPORTONLY | The object is being built for export by a scene exporter plugin such as Alembic, FBX, USD, etc. |
  | BUILDFLAGS_INTERACTIVEEDITOR | The object is being built for the viewport. This is the default context for building and what plugins will implicitly use when they do not explicitly check for build flags. |
  | BUILDFLAGS_PRIVATE_NO_CLEAR_PASS | Internal, do not use. |
  | BUILDFLAGS_PREROLL | The object is being built for a pre-roll event, e.g., a caching or rendering mechanism that is meant to start from a certain frame in the document and is now advancing through the timeline to reach that frame. |
  | BUILDFLAGS_MAKEEDITABLE | The object is being built for being made editable. This happens when the user presses the *C* key or invokes the *Make Editable* command from the context menu in the Object Manager to collapse the object to its cache. |

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `BaseDocument.Polygonize(self, keepanimation=False)` <a id="c4d.documents.BaseDocument.Polygonize"></a>

Make a clone of the document and turn all objects into polygon based objects.

**Parameters:** **keepanimation** (*bool*) – Keep animation.

**Return type:** Optional[[c4d.documents.BaseDocument](#c4d.documents.BaseDocument)]

**Returns:** The cloned polygon based document or **None** if failed.

### Pick Sessions <a id="c4d.documents.BaseDocument-method-Pick-Sessions"></a>

#### `BaseDocument.GetPickSession(self)` <a id="c4d.documents.BaseDocument.GetPickSession"></a>

Returns information about the current pick session.

*New in version R19.*

**Return type:** Optional[Tuple[List[[c4d.C4DAtom](../../c4d/C4DAtom/index.md#c4d.C4DAtom)], bool]]

**Returns:**

A tuple with the list of picked objects and the multi-pick state.  
**None** if there is no active pick session.

#### `BaseDocument.StartPickSession(self, callback, multi)` <a id="c4d.documents.BaseDocument.StartPickSession"></a>

Starts a pick session.

*New in version R19.*

**Parameters:**

- **callback** (function(*active*, *multi*)) –

  The pick session callback. The function does not need to return a value. The passed arguments are:

  > *active*: List[c4d.BaseObject]: The list of picked objects.  
  > *multi*: *bool*: The multi-pick state.

- **multi** (*bool*) – Pass **True** for multi-pick sessions. Usually a pick session ends when something is selected. With a multi-pick session it ends when the user terminates it (ESC key or double-click).

#### `BaseDocument.StopPickSession(self, cancel)` <a id="c4d.documents.BaseDocument.StopPickSession"></a>

Ends the pick session.  
For instance after filling the pick session array.

*New in version R19.*

**Parameters:** **cancel** (*bool*) – Pass **True** to cancel a pick session, for instance if an error occurred. Pass **False** if the pick session is ended regularly.

### Preview And Takes <a id="c4d.documents.BaseDocument-method-Preview-And-Takes"></a>

#### `BaseDocument.GetDocPreviewBitmap(self)` <a id="c4d.documents.BaseDocument.GetDocPreviewBitmap"></a>

Get the preview bitmap of the document.

*New in version R15.037.*

**Return type:** Optional[[c4d.bitmaps.BaseBitmap](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]

**Returns:** The preview bitmap of the document, or **None** if it could not be retrieved.

#### `BaseDocument.GetTakeData(self)` <a id="c4d.documents.BaseDocument.GetTakeData"></a>

Gets the take data for the document.

*New in version R17.032.*

**Return type:** [c4d.modules.takesystem.TakeData](../../c4d.modules/takesystem/TakeData/index.md#c4d.modules.takesystem.TakeData)

**Returns:** The take data.

### Render Settings <a id="c4d.documents.BaseDocument-method-Render-Settings"></a>

#### `BaseDocument.GetActiveRenderData(self)` <a id="c4d.documents.BaseDocument.GetActiveRenderData"></a>

Returns the active selected render data.

**Return type:** [c4d.documents.RenderData](../RenderData/index.md#c4d.documents.RenderData)

**Returns:**

The active render data.

> **Note:** Guaranteed to never be **None**.

#### `BaseDocument.GetFirstRenderData(self)` <a id="c4d.documents.BaseDocument.GetFirstRenderData"></a>

Gets the first render data or options of the document.

> **Note:** The other render settings in the document can be accessed by using the list functions `GetNext()`, `GetPred()`, `GetDown()` and `GetUp()`.

**Return type:** Optional[[c4d.documents.RenderData](../RenderData/index.md#c4d.documents.RenderData)]

**Returns:** The first render data of the document, or **None** if there are no render data associated with the document.

#### `BaseDocument.InsertRenderData(self, rd, parent=None, pred=None)` <a id="c4d.documents.BaseDocument.InsertRenderData"></a>

Inserts the render data into the document’s render settings hierarchy.  
Optionally the insertion position can either be specified by the *parent* parameter, inserting the render data as the first child of the specified *parent*, or by the *pred* parameter, inserting the render data below the specified *pred* render data.  
If neither is given, the render data is inserted at the top of the hierarchy.

**Parameters:**

- **rd** ([*c4d.documents.RenderData*](../RenderData/index.md#c4d.documents.RenderData)) – The render data to insert.
- **parent** (*Optional*[[*c4d.documents.RenderData*](../RenderData/index.md#c4d.documents.RenderData)]) – An optional parent to insert the render data as a child of.
- **pred** (*Optional*[[*c4d.documents.RenderData*](../RenderData/index.md#c4d.documents.RenderData)]) – An optional render data of the document to use as insertion point.

#### `BaseDocument.InsertRenderDataLast(self, rd)` <a id="c4d.documents.BaseDocument.InsertRenderDataLast"></a>

Inserts the render data as last child into the document’s render data list.

**Parameters:** **rd** ([*c4d.documents.RenderData*](../RenderData/index.md#c4d.documents.RenderData)) – The render data to insert.

#### `BaseDocument.SetActiveRenderData(self, rd)` <a id="c4d.documents.BaseDocument.SetActiveRenderData"></a>

Sets the active render settings for the document, these are the settings that are used for rendering.

**Parameters:** **rd** ([*c4d.documents.RenderData*](../RenderData/index.md#c4d.documents.RenderData)) – The render data that you want to make active.

### Scene Structure <a id="c4d.documents.BaseDocument-method-Scene-Structure"></a>

#### `BaseDocument.GetFirstObject(self)` <a id="c4d.documents.BaseDocument.GetFirstObject"></a>

Returns the first object.

**Return type:** Optional[[c4d.BaseObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The first object, or **None** if no objects are contained in this document.

#### `BaseDocument.GetHighest(self, type, editor)` <a id="c4d.documents.BaseDocument.GetHighest"></a>

The first object in object manager hierarchy of type *type*.  
It searches objects that are not deactivated in the object manager (set to red).

**Parameters:**

- **type** (*int*) – the object type
- **editor** (*bool*) – **True** will search using the ‘editor dot’ in the Object Manager, **False** will use the ‘render dot’.

**Return type:** Optional[[c4d.BaseObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The first requested object or **None** if nothing was found.

#### `BaseDocument.GetLayerObjectRoot(self)` <a id="c4d.documents.BaseDocument.GetLayerObjectRoot"></a>

Returns the list of layers of the document.

```python
def GetFirstLayer(doc):
    # Returns the first layer, if available, otherwise None

    return doc.GetLayerObjectRoot().GetDown()
```

> **Warning:** The hierarchy method `GeListNode.GetDown()` can only be called on the returned object.

**Return type:** Optional[[c4d.GeListHead](../../c4d/C4DAtom/GeListNode/GeListHead/index.md#c4d.GeListHead)]

**Returns:** The head of the list of the document’s layers.

#### `BaseDocument.GetObjects(self)` <a id="c4d.documents.BaseDocument.GetObjects"></a>

Returns the highest objects without children.

**Return type:** List[[c4d.BaseObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The objects.

#### `BaseDocument.InsertObject(self, op, parent=None, pred=None, checknames=False, sendNotification=True)` <a id="c4d.documents.BaseDocument.InsertObject"></a>

Inserts the object into the document’s object hierarchy.  
The insertion position can either be specified by the parent parameter, inserting the object as the first child of the specified parent, or by the *pred* parameter, inserting the object below the specified *prev* object.  
If neither is given, the object is inserted at the top of the hierarchy.

> **Note:** If both *pred* and *parent* are provided then pred has precedence.

**Raises:** **ReferenceError** – If the passed objects (*parent* and *pred*) are not in the same document.

**Parameters:**

- **op** (*Optional*[[*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – Object to insert into the document.

- **parent** (*Optional*[[*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – Optional parent to insert the object as a child of.

- **pred** (*Optional*[[*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – Optional insertion point.

- **checknames** (*bool*) – Check for duplicate names and append .1, .2 etc.

- **sendNotification** (*bool*) –

  *New in version 2024.0.0.0.*

  True to send MSG_DOCUMENTINFO_TYPE_OBJECT_INSERT notification to all scenehooks (default). False to prevent doing it.

#### `BaseDocument.SearchObject(self, name)` <a id="c4d.documents.BaseDocument.SearchObject"></a>

Search for an object with the same case sensitive name.

**Parameters:** **name** (*str*) – The name of the object to search for.

**Return type:** Optional[[c4d.BaseObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The object or **None** if nothing was found.

### Scene Systems <a id="c4d.documents.BaseDocument-method-Scene-Systems"></a>

#### `BaseDocument.FindSceneHook(self, id)` <a id="c4d.documents.BaseDocument.FindSceneHook"></a>

Finds a scene hook by ID.

**Parameters:** **id** (*int*) – The scene hook ID.

**Return type:** Optional[[c4d.BaseList2D](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The found scene hook, or **None**.

#### `BaseDocument.GetParticleSystem(self)` <a id="c4d.documents.BaseDocument.GetParticleSystem"></a>

Returns the particle master system of the document.

**Return type:** Optional[[c4d.modules.thinkingparticles.TP_MasterSystem](../../c4d.modules/thinkingparticles/TP_MasterSystem/index.md#c4d.modules.thinkingparticles.TP_MasterSystem)]

**Parameters:** **type** – The particle system of the document. Is useless when the document was deleted, **None** if Thinking Particles is not installed.

#### `BaseDocument.GetSceneRepository(self, create)` <a id="c4d.documents.BaseDocument.GetSceneRepository"></a>

Returns the SceneRepository description.

*New in version R26.*

**Parameters:** **create** (*bool*) – **True** to create if not existing.

**Returns:** Reference to a repository.

**Return type:** [`maxon.UpdatableAssetRepositoryRef`](../../maxon_generated/frameworks/asset/reference/maxon.UpdatableAssetRepositoryRef.md#module-maxon.UpdatableAssetRepositoryRef)

#### `BaseDocument.SendInfo(self, type, format, fn, bl, hooks_only)` <a id="c4d.documents.BaseDocument.SendInfo"></a>

Sends *MSG_DOCUMENTINFO* messages.

*New in version R14.014.*

**Parameters:**

- **type** (*int*) –

  The message type:

  |   |   |
  |---|---|
  | *MSG_DOCUMENTINFO_TYPE_SETACTIVE* | Document was set as active. |
  | *MSG_DOCUMENTINFO_TYPE_LOAD* | Document was loaded. |
  | *MSG_DOCUMENTINFO_TYPE_MERGE* | Document was merged. |
  | *MSG_DOCUMENTINFO_TYPE_BEFOREMERGE* | Document before merge. *data* is a [MSG_DOCUMENTINFO_TYPE_BEFOREMERGE_RESULT](../../../consts/MSG_DOCUMENTINFO_TYPE_BEFOREMERGE_RESULT.md). |
  | *MSG_DOCUMENTINFO_TYPE_SAVE_BEFORE* | Document is about to be written. |
  | *MSG_DOCUMENTINFO_TYPE_SAVE_AFTER* | Document was saved. |
  | *MSG_DOCUMENTINFO_TYPE_SAVEPROJECT_BEFORE* | Save Project with Assets is about to be executed. |
  | *MSG_DOCUMENTINFO_TYPE_SAVEPROJECT_AFTER* | Save Project with Assets was executed. |
  | *MSG_DOCUMENTINFO_TYPE_REMOVE* | The document is removed from the document list. All structures are still accessible. |
  | *MSG_DOCUMENTINFO_TYPE_TOOL_CHANGED* | Tool changed. |
  | *MSG_DOCUMENTINFO_TYPE_OBJECT_INSERT* | Objects got inserted into the document. |
  | *MSG_DOCUMENTINFO_TYPE_TAG_INSERT* | Tags got inserted into the document. |
  | *MSG_DOCUMENTINFO_TYPE_MATERIAL_INSERT* | Materials got inserted into the document. |
  | *MSG_DOCUMENTINFO_TYPE_UNDO* | Undo was called. |
  | *MSG_DOCUMENTINFO_TYPE_REDO* | Redo was called. |
  | *MSG_DOCUMENTINFO_TYPE_PASTE* | Paste was called. |
  | *MSG_DOCUMENTINFO_TYPE_COPY* | Copy was called. Private. |
  | *MSG_DOCUMENTINFO_TYPE_LOAD_XREFS* | Private. |
  | *MSG_DOCUMENTINFO_TYPE_MERGE_XREFS* | Private. |
  | *MSG_DOCUMENTINFO_TYPE_XREFS_IMPORTED* | Private. |
  | *MSG_DOCUMENTINFO_TYPE_MAKEPROJECT* | Sent around during “Save as Project” for each texture / asset it copies. The data contains the source and destination files. This message is only sent to scene hooks. |
  | *MSG_DOCUMENTINFO_TYPE_SWAP_XREF* | Private. |
  | *MSG_DOCUMENTINFO_TYPE_NODE_ASSETS_CHANGED* | *New in version R20.000:* Send around after node assets in a basedocument have been changed. |
  | *MSG_DOCUMENTINFO_TYPE_MODE_CHANGED* | *New in version R20.000:* Mode changed. |
  | *MSG_DOCUMENTINFO_TYPE_FLUSHCACHES* | *New in version R19.062:* Document caches are flushed. This message is only sent to scene hooks. |

- **format** (*int*) –

  The file format: (Set for load, merge and before/after save only. Otherwise *NOTOK*.)

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

- **fn** (*str*) –

  The document filename.

  > **Note:** This is not always the same as [`GetDocumentPath()`](#c4d.documents.BaseDocument.GetDocumentPath). E.g. for *MSG_DOCUMENTINFO_TYPE_SAVE_BEFORE* [`GetDocumentPath()`](#c4d.documents.BaseDocument.GetDocumentPath) still contains the old path whereas *fn* designates the real file.

- **bl** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) –

  The object/tag/material that got inserted. It is used if type is of one of the following types:

  *MSG_DOCUMENTINFO_TYPE_OBJECT_INSERT*  
  *MSG_DOCUMENTINFO_TYPE_TAG_INSERT*  
  *MSG_DOCUMENTINFO_TYPE_MATERIAL_INSERT*

- **hooks_only** (*bool*) – If **True** send only to scene hooks.

### Selection Management <a id="c4d.documents.BaseDocument-method-Selection-Management"></a>

#### `BaseDocument.GetActiveMaterials(self)` <a id="c4d.documents.BaseDocument.GetActiveMaterials"></a>

Returns the material selection.

**Return type:** List[[c4d.BaseMaterial](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial)]

**Returns:** The selected materials in a list.

#### `BaseDocument.GetActiveObject(self)` <a id="c4d.documents.BaseDocument.GetActiveObject"></a>

Returns the active selected object.

**Return type:** Optional[[c4d.BaseObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The active object, or **None**.

#### `BaseDocument.GetActiveObjects(self, flags)` <a id="c4d.documents.BaseDocument.GetActiveObjects"></a>

Returns the object selection.

**Parameters:**

**flags** (*int*) –

Flags:

|   |   |
|---|---|
| *GETACTIVEOBJECTFLAGS_NONE* | Only the topmost parent of each chain is added. |
| *GETACTIVEOBJECTFLAGS_CHILDREN* | Child objects are added to the selection too, provided they are selected. |
| *GETACTIVEOBJECTFLAGS_SELECTIONORDER* | The selection array is sorted in the selection order, e.g. the first selected object is the first element in the array. |

**Return type:** List[[c4d.BaseList2D](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The selected objects in a list.

#### `BaseDocument.GetActiveObjectsFilter(self, children, type, instanceof)` <a id="c4d.documents.BaseDocument.GetActiveObjectsFilter"></a>

Returns the active object multi selection and removes objects that do not match the filter given by type and instanceof.

**Parameters:**

- **children** (*bool*) – If **True** then children are also added to selection, provided that they are selected. Otherwise only the topmost parent in each chain is added.
- **type** (*int*) – Checked against `C4DAtom.GetType()`. Pass *NOTOK* to ignore this test.
- **instanceof** (*int*) – Checked against `C4DAtom.IsInstanceOf()`. Pass *NOTOK* to ignore this test.

**Return type:** List[[c4d.BaseList2D](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The selected objects in a list.

#### `BaseDocument.GetActiveTag(self)` <a id="c4d.documents.BaseDocument.GetActiveTag"></a>

Returns the active selected tag.

**Return type:** Optional[[c4d.BaseTag](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)]

**Returns:** The active tag, or **None**.

#### `BaseDocument.GetActiveTags(self)` <a id="c4d.documents.BaseDocument.GetActiveTags"></a>

Returns the tag selection.

**Return type:** List[[c4d.BaseTag](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)]

**Returns:** The selected tags in a list.

#### `BaseDocument.GetHelperAxis(self)` <a id="c4d.documents.BaseDocument.GetHelperAxis"></a>

Get the helper axis for the current multi selection.

**Return type:** [c4d.BaseObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

**Returns:** The axis object.

#### `BaseDocument.GetRealActiveObject(self, help)` <a id="c4d.documents.BaseDocument.GetRealActiveObject"></a>

Returns the active object or the dummy axis if multiple objects are selected.

*New in version R19.*

**Parameters:** **help** (*Optional*[*Iterable*[[*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]]) – Can be set to **None** or for speedup purposes pass a list/tuple of active objects.

**Return type:** Optional[Tuple[[c4d.BaseObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject), bool]]

**Returns:** A tuple with the real active object and a bool telling if multiple objects are selected. **None** if the method failed.

#### `BaseDocument.GetSelection(self)` <a id="c4d.documents.BaseDocument.GetSelection"></a>

Returns the selection of materials, tags and objects in a list.

**Return type:** List[[c4d.BaseList2D](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The selected objects in a list.

#### `BaseDocument.GetTargetObject(self)` <a id="c4d.documents.BaseDocument.GetTargetObject"></a>

Gets the target object within a multi-selection.

*New in version R17.048.*

> **Note:**
>
> This is the last object selected and is used by commands such as Spline Boolean in order to allow the user to control which object will be used as the target for the command.  
> The target object displays in the Object Manager as highlighted.

**Return type:** Optional[[c4d.BaseObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The target object, or **None** if it fails or there is no selection.

#### `BaseDocument.SetActiveObject(self, op, mode=0)` <a id="c4d.documents.BaseDocument.SetActiveObject"></a>

Modifies the current multi selection with *op*, depending on *mode*.

> **Note:**
>
> `BaseDocument.GetActiveObject()` Should be called afterward to update the internal selection state.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object.

- **mode** (*int*) –

  The selection flag:

  |   |   |
  |---|---|
  | *SELECTION_NEW* | Starts a new selection. |
  | *SELECTION_ADD* | Adds to the current selection |
  | *SELECTION_SUB* | Subtracts from the current selection. |

#### `BaseDocument.SetActiveTag(self, tag, mode=0)` <a id="c4d.documents.BaseDocument.SetActiveTag"></a>

Sets a tag be the currently active one.

> **Note:**
>
> `BaseDocument.GetActiveTag()` Should be called afterward to update the internal selection state.

**Parameters:**

- **tag** ([*c4d.BaseTag*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)) – The tag to set active.

- **mode** (*int*) –

  The selection flag:

  |   |   |
  |---|---|
  | *SELECTION_NEW* | Starts a new selection. |
  | *SELECTION_ADD* | Adds to the current selection |
  | *SELECTION_SUB* | Subtracts from the current selection. |

#### `BaseDocument.SetSelection(self, bl, mode=0)` <a id="c4d.documents.BaseDocument.SetSelection"></a>

Sets the active selection.  
This function deals with both objects, tags and materials.

**Parameters:**

- **bl** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The baselist object within this document that you want to make active. Must be in the document already.

- **mode** (*int*) –

  The selection mode:

  |   |   |
  |---|---|
  | *SELECTION_NEW* | Starts a new selection. |
  | *SELECTION_ADD* | Adds to the current selection |
  | *SELECTION_SUB* | Subtracts from the current selection. |

#### `BaseDocument.SetTargetObject(self, op)` <a id="c4d.documents.BaseDocument.SetTargetObject"></a>

Sets the target object within a multi-selection.

*New in version R17.048.*

> **Note:**
>
> This is the last object selected and is used by commands such as Spline Boolean in order to allow the user to control which object will be used as the target for the command.  
> The target object displays in the Object Manager as highlighted.

**Parameters:** **op** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object to set as the target.

### Timeline Playback <a id="c4d.documents.BaseDocument-method-Timeline-Playback"></a>

#### `BaseDocument.GetLoopMaxTime(self)` <a id="c4d.documents.BaseDocument.GetLoopMaxTime"></a>

Returns the time of the right boundary of the document’s preview range (loop range).

**Return type:** [c4d.BaseTime](../../c4d/BaseTime/index.md#c4d.BaseTime)

**Returns:** The time.

#### `BaseDocument.GetLoopMinTime(self)` <a id="c4d.documents.BaseDocument.GetLoopMinTime"></a>

Returns the time of the left boundary of the document’s preview range (loop range).

**Return type:** [c4d.BaseTime](../../c4d/BaseTime/index.md#c4d.BaseTime)

**Returns:** The time.

#### `BaseDocument.GetMaxTime(self)` <a id="c4d.documents.BaseDocument.GetMaxTime"></a>

Get the end time for the timeline of this document.

> **Note:**
>
> For conversion of FPS or other time units, see [`BaseTime`](../../c4d/BaseTime/index.md#c4d.BaseTime)  
> You may also find the [`GetFps()`](#c4d.documents.BaseDocument.GetFps) useful when using this method.

**Return type:** [c4d.BaseTime](../../c4d/BaseTime/index.md#c4d.BaseTime)

**Returns:** The time.

#### `BaseDocument.GetMinTime(self)` <a id="c4d.documents.BaseDocument.GetMinTime"></a>

Get the starting time for the timeline of this document.

> **Note:**
>
> For conversion of FPS or other time units, see [`BaseTime`](../../c4d/BaseTime/index.md#c4d.BaseTime)  
> You may also find the [`GetFps()`](#c4d.documents.BaseDocument.GetFps) useful when using this method.

**Return type:** [c4d.BaseTime](../../c4d/BaseTime/index.md#c4d.BaseTime)

**Returns:** The time.

#### `BaseDocument.GetTime(self)` <a id="c4d.documents.BaseDocument.GetTime"></a>

Returns the min time.

**Return type:** [c4d.BaseTime](../../c4d/BaseTime/index.md#c4d.BaseTime)

**Returns:** The current time.

#### `BaseDocument.SetLoopMaxTime(self, time)` <a id="c4d.documents.BaseDocument.SetLoopMaxTime"></a>

Sets the right boundary of the document’s preview range (loop range) to the given time.

**Parameters:** **type** ([*c4d.BaseTime*](../../c4d/BaseTime/index.md#c4d.BaseTime)) – The time.

#### `BaseDocument.SetLoopMinTime(self, time)` <a id="c4d.documents.BaseDocument.SetLoopMinTime"></a>

Sets the left boundary of the document’s preview range (loop range) to the given time.

**Parameters:** **type** ([*c4d.BaseTime*](../../c4d/BaseTime/index.md#c4d.BaseTime)) – The time.

#### `BaseDocument.SetMaxTime(self, time)` <a id="c4d.documents.BaseDocument.SetMaxTime"></a>

Set the end time of the timeline for this document.

> **Note:**
>
> For conversion of FPS or other time units, see [`BaseTime`](../../c4d/BaseTime/index.md#c4d.BaseTime)  
> You may also find the [`GetFps()`](#c4d.documents.BaseDocument.GetFps) useful when using this method.

**Parameters:** **type** ([*c4d.BaseTime*](../../c4d/BaseTime/index.md#c4d.BaseTime)) – The time.

#### `BaseDocument.SetMinTime(self, time)` <a id="c4d.documents.BaseDocument.SetMinTime"></a>

Set the starting time for the timeline of this document.

> **Note:**
>
> For conversion of FPS or other time units, see [`BaseTime`](../../c4d/BaseTime/index.md#c4d.BaseTime)  
> You may also find the [`GetFps()`](#c4d.documents.BaseDocument.GetFps) useful when using this method.

**Parameters:** **type** ([*c4d.BaseTime*](../../c4d/BaseTime/index.md#c4d.BaseTime)) – The time.

#### `BaseDocument.SetRewind(self, flags=0)` <a id="c4d.documents.BaseDocument.SetRewind"></a>

Rewinds the whole document (from time 0 to current time) when the next event *EVMSG_CHANGE* or [`DrawViews()`](../../c4d/index.md#c4d.DrawViews) is processed.

**Parameters:** **flags** (*int*) – Not used.

#### `BaseDocument.SetTime(self, time)` <a id="c4d.documents.BaseDocument.SetTime"></a>

Set the current time for this documents timeline.

> **Note:** This function only changes the document time, it does not start a redraw and/or animation/expressions.

**Parameters:** **type** ([*c4d.BaseTime*](../../c4d/BaseTime/index.md#c4d.BaseTime)) – The time.

### Undo Management <a id="c4d.documents.BaseDocument-method-Undo-Management"></a>

#### `BaseDocument.AddUndo(self, type, data, allowFromThread=False)` <a id="c4d.documents.BaseDocument.AddUndo"></a>

Adds an undo *type* to the list of undo operations started with [`StartUndo()`](#c4d.documents.BaseDocument.StartUndo).

> **Note:**
>
> Always has to be called before a change is made.  
> In the case of the creation of a new object the call is done afterwards, after insertion into the document/object/track/sequence but before calling subsequent functions like `BaseDocument.SetActiveObject()` which creates another undo:
>
> ```python
> tag = c4d.UVWTag(op.GetPointCount())
> op.InsertTag(tag)
> doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, tag)
> c4d.EventAdd()
> ```

**Parameters:**

- **type** (*int*) –

  The undo type:

  | Symbol ID | Description |
  |---|---|
  | UNDOTYPE_NONE | None. |
  | UNDOTYPE_CHANGE | Any change to an object, including hierarchy modifications; modification in positioning (object has been moved from A to B), substructures etc. (Needs to be called *before* the change.) |
  | UNDOTYPE_CHANGE_NOCHILDREN | Same as *UNDOTYPE_CHANGE*, but without child modifications. (Needs to be called *before* the change.) |
  | UNDOTYPE_CHANGE_SMALL | Change to local data only (e.g. data container), no substructures (e.g. no tags on an object) and no children. (Needs to be called *before* the change.) |
  | UNDOTYPE_CHANGE_SELECTION | Change to point/poly/edge selection only. (Needs to be called *before* the change.) |
  | UNDOTYPE_NEWOBJ | New object/node/tag etc. was created. (Needs to be called *after* the change.) |
  | UNDOTYPE_DELETEOBJ | Object/node/tag etc. to be deleted. (Needs to be called *before* the change.) |
  | UNDOTYPE_ACTIVATE | Automatically managed by `BaseDocument.SetActiveObject()`/`SetActiveTag()`/`SetActiveMaterial()` etc. No need to use manually. |
  | UNDOTYPE_DEACTIVATE | Automatically managed by `BaseDocument.SetActiveObject()`/`SetActiveTag()`/`SetActiveMaterial()` etc. No need to use manually. |
  | UNDOTYPE_BITS | Change to object bits, e.g. selection status. (Needs to be called *before* the change.) |
  | UNDOTYPE_HIERARCHY_PSR | Change in hierarchical placement and PSR values. (Needs to be called *before* the change.) |
  | UNDOTYPE_PRIVATE_STRING | Private |
  | UNDOTYPE_PRIVATE_MULTISELECTIONAXIS | Private. |
  | UNDOTYPE_START | Private. |
  | UNDOTYPE_END | Private. |

- **data** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The object the undo has been added for.

- **allowFromThread** (*Optional*[*bool*]) –

  *New in version R14.014:* If an undo is added from a thread this is not executed. (As a safety measure, because normally this doesn’t make any sense.)

  For explicit cases where a thread has to call [`AddUndo()`](#c4d.documents.BaseDocument.AddUndo) (the view redraw and everything else is blocked) this can be set to **True**.

**Return type:** bool

**Returns:** Success of adding the undo.

#### `BaseDocument.DoRedo(self)` <a id="c4d.documents.BaseDocument.DoRedo"></a>

Perform a redo on this document (undo the last undo).

**Return type:** bool

**Returns:** Success of the operation.

#### `BaseDocument.DoUndo(self, multiple=False)` <a id="c4d.documents.BaseDocument.DoUndo"></a>

Perform an undo operation, same as the user selecting Undo from within Cinema 4D.

**Parameters:** **multiple** (*bool*) – This parameter only matters if this method is called between [`AddUndo()`](#c4d.documents.BaseDocument.AddUndo) and [`EndUndo()`](#c4d.documents.BaseDocument.EndUndo). If *multiple* is **True** then all the [`AddUndo()`](#c4d.documents.BaseDocument.AddUndo) steps will be undone. Otherwise only the last [`AddUndo()`](#c4d.documents.BaseDocument.AddUndo) step will be undone. If [`EndUndo()`](#c4d.documents.BaseDocument.EndUndo) has been called then all steps are always undone.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `BaseDocument.EndUndo(self)` <a id="c4d.documents.BaseDocument.EndUndo"></a>

End the building of multiple undo actions into a single user undo.

> **Note:** This must be paired with [`StartUndo()`](#c4d.documents.BaseDocument.StartUndo).

**Return type:** bool

**Returns:** Success of finishing the undo list.

#### `BaseDocument.FindUndoPtr(self, bl, type)` <a id="c4d.documents.BaseDocument.FindUndoPtr"></a>

Returns the last undo state of the Cinema 4D element bl (object, tag, material, etc.) for the specified undo action type.

*New in version R14.014.*

Here is an how to retrieve the pre-undo object after a change has made

```python
preundo = doc.FindUndoPtr(obj, c4d.UNDOTYPE_CHANGE)
```

> **Note:** Always check the type of the returned object.

**Parameters:**

- **bl** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The element from which to obtain the last undo action.

- **type** (*int*) –

  The undo type to check:

  | Symbol ID | Description |
  |---|---|
  | UNDOTYPE_NONE | None. |
  | UNDOTYPE_CHANGE | Any change to an object, including hierarchy modifications; modification in positioning (object has been moved from A to B), substructures etc. (Needs to be called *before* the change.) |
  | UNDOTYPE_CHANGE_NOCHILDREN | Same as *UNDOTYPE_CHANGE*, but without child modifications. (Needs to be called *before* the change.) |
  | UNDOTYPE_CHANGE_SMALL | Change to local data only (e.g. data container), no substructures (e.g. no tags on an object) and no children. (Needs to be called *before* the change.) |
  | UNDOTYPE_CHANGE_SELECTION | Change to point/poly/edge selection only. (Needs to be called *before* the change.) |
  | UNDOTYPE_NEWOBJ | New object/node/tag etc. was created. (Needs to be called *after* the change.) |
  | UNDOTYPE_DELETEOBJ | Object/node/tag etc. to be deleted. (Needs to be called *before* the change.) |
  | UNDOTYPE_ACTIVATE | Automatically managed by `BaseDocument.SetActiveObject()`/`SetActiveTag()`/`SetActiveMaterial()` etc. No need to use manually. |
  | UNDOTYPE_DEACTIVATE | Automatically managed by `BaseDocument.SetActiveObject()`/`SetActiveTag()`/`SetActiveMaterial()` etc. No need to use manually. |
  | UNDOTYPE_BITS | Change to object bits, e.g. selection status. (Needs to be called *before* the change.) |
  | UNDOTYPE_HIERARCHY_PSR | Change in hierarchical placement and PSR values. (Needs to be called *before* the change.) |
  | UNDOTYPE_PRIVATE_STRING | Private |
  | UNDOTYPE_PRIVATE_MULTISELECTIONAXIS | Private. |
  | UNDOTYPE_START | Private. |
  | UNDOTYPE_END | Private. |

**Return type:** [c4d.BaseList2D](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

**Returns:** The last undo element.

#### `BaseDocument.FlushUndoBuffer(self)` <a id="c4d.documents.BaseDocument.FlushUndoBuffer"></a>

Flushes the complete undo + redo buffer.

*New in version R14.014.*

> **Warning:** Only call when absolutely needed.

#### `BaseDocument.GetUndoPtr(self)` <a id="c4d.documents.BaseDocument.GetUndoPtr"></a>

Returns the element of the last undo action. E.g. if you have added a [`BaseObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) undo you can retrieve the object by calling this method.

> **Note:** Always be sure to check the type of the result first.

**Return type:** [c4d.BaseList2D](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

**Returns:** The last undo element.

#### `BaseDocument.StartUndo(self)` <a id="c4d.documents.BaseDocument.StartUndo"></a>

Tells Cinema 4D to start building a list of undos into a single undo action for the user.

**Return type:** bool

**Returns:** Success of starting the undo list.

Here is a small example how to write a redo support for newly inserted objects.

```python
import c4d

doc.StartUndo()                     # Start undo support
cube = c4d.BaseObject(c4d.Ocube)

doc.InsertObject(cube)              # Insert the object
doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, cube) # Support redo the insert operation
doc.EndUndo()                       # Do not forget to close the undo support
```

### Viewport Display <a id="c4d.documents.BaseDocument-method-Viewport-Display"></a>

#### `BaseDocument.ForceCreateBaseDraw(self)` <a id="c4d.documents.BaseDocument.ForceCreateBaseDraw"></a>

Makes sure that [`GetBaseDraw()`](#c4d.documents.BaseDocument.GetBaseDraw) (0) is accessible.  
This is only important in import filters where, at the time, there are no valid base draws.

#### `BaseDocument.GetActiveBaseDraw(self)` <a id="c4d.documents.BaseDocument.GetActiveBaseDraw"></a>

Get the activate BaseDraw in the editor, this is where all drawing should be performed.

**Return type:** [c4d.BaseDraw](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)

**Returns:** The active view in the editor.

#### `BaseDocument.GetBaseDraw(self, bd)` <a id="c4d.documents.BaseDocument.GetBaseDraw"></a>

Returns the BaseDraw hook of the editor *bd*.

**Parameters:** **bd** (*int*) – If there are multiple views (multiple basedraws), this selects the view.

**Return type:** Optional[[c4d.BaseDraw](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)]

**Returns:** The requested view in the editor, or **None**

#### `BaseDocument.GetBaseDrawCount(self)` <a id="c4d.documents.BaseDocument.GetBaseDrawCount"></a>

Get the [`BaseDraw`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw) count in the editor view.

**Return type:** int

**Returns:** The count.

#### `BaseDocument.GetDrawTime(self)` <a id="c4d.documents.BaseDocument.GetDrawTime"></a>

Get the editor redraw time.

**Return type:** int

**Returns:** The editor redraw time.

#### `BaseDocument.GetRenderBaseDraw(self)` <a id="c4d.documents.BaseDocument.GetRenderBaseDraw"></a>

This is the BaseDraw belonging to the view that the user has chosen as ‘Render View’ (see View menu in Cinema 4D).

**Return type:** [c4d.BaseDraw](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)

**Returns:** The render view in the editor.
