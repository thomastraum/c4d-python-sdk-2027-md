<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/cinema_hybrid/interface/maxon.AssetCreationInterface.html -->

# maxon.AssetCreationInterface <a id="maxon-assetcreationinterface"></a>

## Description <a id="module-maxon.AssetCreationInterface"></a><a id="description"></a>

Helper interface for asset creation and drag&drop

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`AddPreviewRenderAsset`](#maxon.AssetCreationInterface.AddPreviewRenderAsset)(assetsToPreviewRender) | Adds the given assets to the background render queue. |
| [`BrowseDescriptionForDefaults`](#maxon.AssetCreationInterface.BrowseDescriptionForDefaults)(desc, add, …) | Helper function to browse through Descriptions to collect all attributes to be stored in a preset. |
| [`CheckObjectsOnDrop`](#maxon.AssetCreationInterface.CheckObjectsOnDrop)(doc, url, asset, …) | Helper function to add objects into the scene from the asset browser. |
| [`CreateMaterialAsset`](#maxon.AssetCreationInterface.CreateMaterialAsset)(activeDoc, mat, …) | Creates a material asset from the given BaseMaterial. |
| [`CreateMaterialsOnDrag`](#maxon.AssetCreationInterface.CreateMaterialsOnDrag)(doc, objectOrTag, url, …) | **param doc:** BaseDocument to insert the asset. |
| [`CreateObjectAsset`](#maxon.AssetCreationInterface.CreateObjectAsset)(op, activeDoc, …) | Creates an object asset from the given BaseObject. |
| [`CreateObjectsOnDrag`](#maxon.AssetCreationInterface.CreateObjectsOnDrag)(doc, url, asset, …[, …]) | Helper function to create assets when d&d into a scene/viewport. |
| [`CreateSceneAsset`](#maxon.AssetCreationInterface.CreateSceneAsset)(activeDoc, …) | Creates a scene asset from the given BaseDocument. |
| [`GenerateImagePreview`](#maxon.AssetCreationInterface.GenerateImagePreview)(imageUrl, previews, …) | Generates a preview image for a given texture. |
| [`GenerateScenePreviewImage`](#maxon.AssetCreationInterface.GenerateScenePreviewImage)(doc, preview, …) | Generates the preview image of the given BaseDocument. |
| [`GetAddDependencyDelegate`](#maxon.AssetCreationInterface.GetAddDependencyDelegate)(documentPath, …) | Helper function to generate the ResolveAssetDependenciesStruct.ResolveDelegate. |
| [`GetDefaultObject`](#maxon.AssetCreationInterface.GetDefaultObject)(asset[, doc]) | Returns a new default object for the given preset. |
| [`GetDefaultSettings`](#maxon.AssetCreationInterface.GetDefaultSettings)(asset, resId, resData) | Loads the settings for a preset |
| [`GetNewAssetIdFromIdAndVersion`](#maxon.AssetCreationInterface.GetNewAssetIdFromIdAndVersion)(prefix, …) | GetNewAssetIdFromIdAndVersion generates a standarized id from the given prefix and IdAndVersion for a new asset. |
| [`OpenSaveAssetDialog`](#maxon.AssetCreationInterface.OpenSaveAssetDialog)(flags, presetTypeName, …) | Opens the save asset dialog. |
| [`RenderDocumentAsset`](#maxon.AssetCreationInterface.RenderDocumentAsset)(renderDoc, progressRef, …) | Helper function to render a BaseDocument for preview rendering. |
| [`SaveActiveDocumentAsNewVersion`](#maxon.AssetCreationInterface.SaveActiveDocumentAsNewVersion)(activeDoc, …) | Writes the current BaseDocument as new version with asset dialog. |
| [`SaveBaseDocumentAsAsset`](#maxon.AssetCreationInterface.SaveBaseDocumentAsAsset)(doc, c4dRootPath, …) | Stores the given BaseDocument as a new scene to be saved as an asset. |
| [`SaveBrowserPreset`](#maxon.AssetCreationInterface.SaveBrowserPreset)(assetType, sourceData, …) | Stores the given data as preset asset. |
| [`SaveDefaultPresetFromObject`](#maxon.AssetCreationInterface.SaveDefaultPresetFromObject)(l, makeDefault) | Stores the default from the given object into the asset browser. |
| [`SaveDocumentAsset`](#maxon.AssetCreationInterface.SaveDocumentAsset)(assetDoc, subType, …) | Stores the given BaseDocument into the given repository. |
| [`SaveMemFileAsAsset`](#maxon.AssetCreationInterface.SaveMemFileAsAsset)(saveFileName, …) | Stores the given url as a asset into a temporary repository. |
| [`SaveMemFileAsAssetAlone`](#maxon.AssetCreationInterface.SaveMemFileAsAssetAlone)(saveFileName, …) | Stores the plain file into a temporary repository. |
| [`SaveMemFileAsAssetWithCopyAsset`](#maxon.AssetCreationInterface.SaveMemFileAsAssetWithCopyAsset)(…) | Stores the given url as a asset. |
| [`SaveMetaDataForAsset`](#maxon.AssetCreationInterface.SaveMetaDataForAsset)(asset, parentCategory, …) | Stores he given values into the asset description. |
| [`SaveTextureAsset`](#maxon.AssetCreationInterface.SaveTextureAsset)(imageUrl, assetName, …) | Stores the given image as media asset. |
| [`SetDefaultObject`](#maxon.AssetCreationInterface.SetDefaultObject)(defaultsType, partial, bc, …) | **param defaultsType:** Ids of the BaseObject. e.g. Ocube |
| [`SupportDefaultPresets`](#maxon.AssetCreationInterface.SupportDefaultPresets)(l) | Helper function to find if the given type supports the preset system. |
| [`UpdateMetaData`](#maxon.AssetCreationInterface.UpdateMetaData)(doc[, metaProperties, …]) | UpdateMetaData recalculates the asset metadata. |
| [`UpdateSubtypeAndMetaData`](#maxon.AssetCreationInterface.UpdateSubtypeAndMetaData)(list, force) | UpdateSubtypeAndMetaData determines subtype and calculates meta data for a list of assets. |

## Methods Definition <a id="methods-definition"></a>

### *static* `AssetCreationInterface.AddPreviewRenderAsset(assetsToPreviewRender)` <a id="maxon.AssetCreationInterface.AddPreviewRenderAsset"></a>

Adds the given assets to the background render queue.

**Parameters:** **assetsToPreviewRender** ([`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [[`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)]) – Assets to add to the render queue.

### *static* `AssetCreationInterface.BrowseDescriptionForDefaults(desc, add, isPartial)` <a id="maxon.AssetCreationInterface.BrowseDescriptionForDefaults"></a>

Helper function to browse through Descriptions to collect all attributes to be stored in a preset.

**Parameters:**

- **desc** ([`c4d.Description`](../../../../c4d/Description/index.md#c4d.Description)) – Description to browse.
- **add** (Callable[[`c4d.DescId`, [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [bool, [`c4d.BaseContainer`](../../../../c4d/BaseContainer/index.md#c4d.BaseContainer), [`c4d.DescID`](../../../../c4d/DescID/index.md#c4d.DescID), str], None]) – delegate which is triggered for each attribute.
- **isPartial** (*bool*) – **True** if this should be a partial preset. In that case DESC_UNIMPORTANTFORDEFAULTS will be ignored.

### *static* `AssetCreationInterface.CheckObjectsOnDrop(doc, url, asset, placementScale)` <a id="maxon.AssetCreationInterface.CheckObjectsOnDrop"></a>

Helper function to add objects into the scene from the asset browser.

This functions keeps a list of assets and remembers if they were added already.

**Parameters:**

- **doc** ([`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – BaseDocument to insert the asset.
- **url** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – Url of the d&d operation. This is typically an asset url “asset:///…”
- **asset** ([`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – AssetDescription of the asset.
- **placementScale** (*float*) – Additional scale factor.

### *static* `AssetCreationInterface.CreateMaterialAsset(activeDoc, mat, storeAssetStruct, assetId, assetName, assetVersion, copyMetaData, addAssetsIfNotInThisRepository)` <a id="maxon.AssetCreationInterface.CreateMaterialAsset"></a>

Creates a material asset from the given BaseMaterial.

**Parameters:**

- **activeDoc** ([`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – BaseDocument of the material to store. This document will be used to find dependencies.
- **mat** ([`c4d.BaseMaterial`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial)) – BaseMaterial to store.
- **storeAssetStruct** ([`maxon.StoreAssetStruct`](../../asset/datatype/maxon.StoreAssetStruct.md#module-maxon.StoreAssetStruct)) – Settings where to store the asset.
- **assetId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Optional asset Id. If empty the system calculates a new asset id.
- **assetName** (*str*) – Human readable name of the asset.
- **assetVersion** (*str*) – Human readable version string.
- **copyMetaData** ([`maxon.AssetMetaData`](../../asset/reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)) – Optional meta data to copy from another version.
- **addAssetsIfNotInThisRepository** (*bool*) – **True** to store the asset in the given saveRepository even if it’s already in any other repository. **False** would skip the writing.

**Returns:** The created AssetDescription.

**Return type:** [`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### *static* `AssetCreationInterface.CreateMaterialsOnDrag(doc, objectOrTag, url, allowMultiple, subType, noManagerUpdate, startUndo)` <a id="maxon.AssetCreationInterface.CreateMaterialsOnDrag"></a>

**Parameters:**

- **doc** ([`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – BaseDocument to insert the asset.
- **objectOrTag** ([`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – Drop destination.
- **url** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – Url of the d&d operation. This is typically an asset url “asset:///…”
- **allowMultiple** (*bool*) – **True** to insert multiple materials at the same time.
- **subType** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Subtype of the asset.
- **noManagerUpdate** (*bool*) – **True** to prevent attribute manager updates when activating the new objects.
- **startUndo** (*bool*) – **True** to call doc->StartUndo() and EndUndo().

**Returns:** Array with the newly created BaseMaterials on success.

**Return type:** tuple( [`c4d.BaseMaterial`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial))

### *static* `AssetCreationInterface.CreateObjectAsset(op, activeDoc, storeAssetStruct, assetId, assetName, assetVersion, copyMetaData, addAssetsIfNotInThisRepository)` <a id="maxon.AssetCreationInterface.CreateObjectAsset"></a>

Creates an object asset from the given BaseObject.

**Parameters:**

- **op** ([`c4d.BaseObject`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – BaseObject to store.
- **activeDoc** ([`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – BaseDocument of the material to store. This document will be used to find dependencies.
- **storeAssetStruct** ([`maxon.StoreAssetStruct`](../../asset/datatype/maxon.StoreAssetStruct.md#module-maxon.StoreAssetStruct)) – Settings where to store the asset.
- **assetId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Optional asset Id. If empty the system calculates a new asset id.
- **assetName** (*str*) – Human readable name of the asset.
- **assetVersion** (*str*) – Human readable version string.
- **copyMetaData** ([`maxon.AssetMetaData`](../../asset/reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)) – Optional meta data to copy from another version.
- **addAssetsIfNotInThisRepository** (*bool*) – **True** to store the asset in the given saveRepository even if it’s already in any other repository. **False** would skip the writing.

**Returns:** The created AssetDescription.

**Return type:** [`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### *static* `AssetCreationInterface.CreateObjectsOnDrag(doc, url, asset, filterString, allowPreviewCube, overwriteMatrix, overwriteMatrixMg, placementScale, parent=None, prev=None)` <a id="maxon.AssetCreationInterface.CreateObjectsOnDrag"></a>

Helper function to create assets when d&d into a scene/viewport.

**Parameters:**

- **doc** ([`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – BaseDocument to insert the asset.
- **url** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – Url of the d&d operation. This is typically an asset url “asset:///…”
- **asset** ([`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – AssetDescription of the asset.
- **filterString** (*str*) – Filter string of the d&d operation. This allows to switch the search term e.g. sphere / cube on a modeling node.
- **allowPreviewCube** (*bool*) – **True** to indicate that a preview cube should be inserted instead of the real geometry.
- **overwriteMatrix** (*bool*) – **True** to overwrite the overwriteMatrixMg.
- **overwriteMatrixMg** ([`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix)) – Overwrite the matrix with this value.
- **placementScale** (*float*) – Additional scale factor.
- **parent** (Optional[[`c4d.BaseObject`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – Parent object to insert.
- **prev** (Optional[[`c4d.BaseObject`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – Previous object to insert.

### *static* `AssetCreationInterface.CreateSceneAsset(activeDoc, storeAssetStruct, assetId, assetName, assetVersion, copyMetaData, addAssetsIfNotInThisRepository)` <a id="maxon.AssetCreationInterface.CreateSceneAsset"></a>

Creates a scene asset from the given BaseDocument.

**Parameters:**

- **activeDoc** ([`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – BaseDocument to store. This document will be used to find dependencies.
- **storeAssetStruct** ([`maxon.StoreAssetStruct`](../../asset/datatype/maxon.StoreAssetStruct.md#module-maxon.StoreAssetStruct)) – Settings where to store the asset.
- **assetId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Optional asset Id. If empty the system calculates a new asset id.
- **assetName** (*str*) – Human readable name of the asset.
- **assetVersion** (*str*) – Human readable version string.
- **copyMetaData** ([`maxon.AssetMetaData`](../../asset/reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)) – Optional meta data to copy from another version.
- **addAssetsIfNotInThisRepository** (*bool*) – **True** to store the asset in the given saveRepository even if it’s already in any other repository. **False** would skip the writing.

**Returns:** The created AssetDescription.

**Return type:** [`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### *static* `AssetCreationInterface.GenerateImagePreview(imageUrl, previews, previewW, previewH)` <a id="maxon.AssetCreationInterface.GenerateImagePreview"></a>

Generates a preview image for a given texture.

**Parameters:**

- **imageUrl** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – Url of the texture.
- **previews** (Callable[[[`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)], None]) – ValueReceiver which receives the preview.
- **previewW** (*int*) – Preview width.
- **previewH** (*int*) – Preview height.

### *static* `AssetCreationInterface.GenerateScenePreviewImage(doc, preview, flags, previewW, previewH)` <a id="maxon.AssetCreationInterface.GenerateScenePreviewImage"></a>

Generates the preview image of the given BaseDocument.

**Parameters:**

- **doc** ([`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – BaseDocument to preview.
- **preview** ([`c4d.bitmaps.BaseBitmap`](../../../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – BaseBitmap into which the preview should be rendered.
- **flags** ([`maxon.GENERATESCENEPREVIEWIMAGEFLAGS`](../../../enums/maxon.GENERATESCENEPREVIEWIMAGEFLAGS.md#module-maxon.GENERATESCENEPREVIEWIMAGEFLAGS)) – see GENERATESCENEPREVIEWIMAGEFLAGS.
- **previewW** (*int*) – Preview width.
- **previewH** (*int*) – Preview height.

### *static* `AssetCreationInterface.GetAddDependencyDelegate(documentPath, addAssetsIfNotInThisRepository)` <a id="maxon.AssetCreationInterface.GetAddDependencyDelegate"></a>

Helper function to generate the ResolveAssetDependenciesStruct.ResolveDelegate.

**Parameters:**

- **documentPath** (*str*) – Root Path of the document.
- **addAssetsIfNotInThisRepository** (*bool*) – **True** to store the asset in the given saveRepository even if it’s already in any other repository. **False** would skip the writing.

**Returns:** Delegate to be used in functions where it is required.

**Return type:** Callable[[[`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url), [`maxon.StoreAssetStruct`](../../asset/datatype/maxon.StoreAssetStruct.md#module-maxon.StoreAssetStruct), [`maxon.ResolveAssetDependenciesStruct`](../../asset/datatype/maxon.ResolveAssetDependenciesStruct.md#module-maxon.ResolveAssetDependenciesStruct)], [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]

### *static* `AssetCreationInterface.GetDefaultObject(asset, doc=None)` <a id="maxon.AssetCreationInterface.GetDefaultObject"></a>

Returns a new default object for the given preset.

Only next calls are allowed:

> - GetDefaultObject(asset: [`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription))
> - GetDefaultObject(asset: [`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [int], doc: [`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument))

**Parameters:**

- **asset** (Union[[`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [int], [`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)]) – Ids of the BaseObject. e.g. Ocube or Asset to load.
- **doc** (*Optional*[[*c4d.documents.BaseDocument*](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]) – BaseDocument to look for the scene repository. Pass a BaseDocument only if a [`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [int] is passed, otherwise ignored.

**Returns:** New BaseList2D to insert.

**Return type:** [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

### *static* `AssetCreationInterface.GetDefaultSettings(asset, resId, resData)` <a id="maxon.AssetCreationInterface.GetDefaultSettings"></a>

Loads the settings for a preset

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to load.
- **resId** ([`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [int]) – BaseList Ids of the preset.
- **resData** ([`c4d.BaseContainer`](../../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Settings Container.

**Returns:** **True** means a partial preset was loaded.

**Return type:** bool

### *static* `AssetCreationInterface.GetNewAssetIdFromIdAndVersion(prefix, idAndVersion)` <a id="maxon.AssetCreationInterface.GetNewAssetIdFromIdAndVersion"></a>

GetNewAssetIdFromIdAndVersion generates a standarized id from the given prefix and IdAndVersion for a new asset.

**Parameters:**

- **prefix** (*str*) – Prefix can be used for the type of the asset. e.g. “file” for file assets. preset for “presets”.
- **idAndVersion** ([`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]) – IdAndVersion of the asset to be created.

**Returns:** Id on success.

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)

### *static* `AssetCreationInterface.OpenSaveAssetDialog(flags, presetTypeName, id, name, version, lookupRepository, category, selectedRepository, setAsDefault)` <a id="maxon.AssetCreationInterface.OpenSaveAssetDialog"></a>

Opens the save asset dialog.

**Parameters:**

- **flags** ([`maxon.OPENSAVEASSETDIALOGFLAGS`](../../../enums/maxon.OPENSAVEASSETDIALOGFLAGS.md#module-maxon.OPENSAVEASSETDIALOGFLAGS)) – see OPENSAVEASSETDIALOGFLAGS.
- **presetTypeName** (*str*) – Asset Type name to create the dialog title.
- **id** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Id of the asset.
- **name** (*str*) – Asset name.
- **version** (*str*) – Version string.
- **lookupRepository** ([`maxon.AssetRepositoryRef`](../../asset/reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to search for assets.
- **category** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Category in which the asset should be stored.
- **selectedRepository** ([`maxon.AssetRepositoryRef`](../../asset/reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Selected repository where the asset should be stored.
- **setAsDefault** (*bool*) – True to set the preset as default.

**Returns:** **True** on success and dialog okay. **False** if user canceled.

**Return type:** bool

### *static* `AssetCreationInterface.RenderDocumentAsset(renderDoc, progressRef, progressIndex, polygonCount, previewW, previewH, flags)` <a id="maxon.AssetCreationInterface.RenderDocumentAsset"></a>

Helper function to render a BaseDocument for preview rendering.

**Parameters:**

- **renderDoc** ([`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – BaseDocument to render.
- **progressRef** (`maxon.MediaSessionProgressRef`) – progress class.
- **progressIndex** (*int*) – progress index to use.
- **polygonCount** (*int*) – Number of polygons in the scene. If -1 the count will be calculated. If the count == 0 and the scene has one first object the icon of the object is used as preview.
- **previewW** (*int*) – Preview width.
- **previewH** (*int*) – Preview height.
- **flags** ([`maxon.GENERATESCENEPREVIEWIMAGEFLAGS`](../../../enums/maxon.GENERATESCENEPREVIEWIMAGEFLAGS.md#module-maxon.GENERATESCENEPREVIEWIMAGEFLAGS)) – see GENERATESCENEPREVIEWIMAGEFLAGS.

**Returns:** Url of the rendered memory file.

**Return type:** [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)

### *static* `AssetCreationInterface.SaveActiveDocumentAsNewVersion(activeDoc, addAssetsIfNotInThisRepository)` <a id="maxon.AssetCreationInterface.SaveActiveDocumentAsNewVersion"></a>

Writes the current BaseDocument as new version with asset dialog.

**Parameters:**

- **activeDoc** ([`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – BaseDocument to store.
- **addAssetsIfNotInThisRepository** (*bool*) – **True** to store the asset in the given saveRepository even if it’s already in any other repository. **False** would skip the writing.

**Returns:** The created AssetDescription.

**Return type:** [`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### *static* `AssetCreationInterface.SaveBaseDocumentAsAsset(doc, c4dRootPath, saveFileName, addDependencyStruct, resolveAssets, metaProperties, calcBoundingBox, objectMatrix, subType)` <a id="maxon.AssetCreationInterface.SaveBaseDocumentAsAsset"></a>

Stores the given BaseDocument as a new scene to be saved as an asset. Dependencies will be calculated as well.

**Parameters:**

- **doc** ([`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – BaseDocument to store.
- **c4dRootPath** (*str*) – Root of the document. This path is used to search textures/dependencies.
- **saveFileName** (*str*) – Destination path where the BaseDocument will be stored (this can be a memory file).
- **addDependencyStruct** ([`maxon.AddAssetDepencendyStruct`](../../asset/datatype/maxon.AddAssetDepencendyStruct.md#module-maxon.AddAssetDepencendyStruct)) – AddAssetDepencendyStruct which is triggered on any dependency found.
- **resolveAssets** ([`maxon.ResolveAssetDependenciesStruct`](../../asset/datatype/maxon.ResolveAssetDependenciesStruct.md#module-maxon.ResolveAssetDependenciesStruct)) – ResolveAssetDependenciesStruct keeps temporary data to resolve dependencies.
- **metaProperties** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – DataDictionary to store the data.
- **calcBoundingBox** (*bool*) – True to calculate the bounding box of the scene.
- **objectMatrix** ([`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix)) – Optional matrix to add to the object.
- **subType** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – SubType of the asset, e.g. [`maxon.ASSETMETADATA.SubType_ENUM_Object`](../../../enums/maxon.ASSETMETADATA.SubType_ENUM_Object.md#maxon.ASSETMETADATA.SubType_ENUM_Object).

**Returns:** True on success.

**Return type:** bool

### *static* `AssetCreationInterface.SaveBrowserPreset(assetType, sourceData, presetTypeName, presetNameA, showMakeDefault, setAsDefault, allowSceneRepository)` <a id="maxon.AssetCreationInterface.SaveBrowserPreset"></a>

Stores the given data as preset asset.

**Parameters:**

- **assetType** ([`maxon.BasePresetAssetType`](../../asset/reference/maxon.BasePresetAssetType.md#module-maxon.BasePresetAssetType)) – PresetType.
- **sourceData** (`maxon.PresetSaveArgs`) – Data to store.
- **presetTypeName** (*str*) – Present Type name to generate the dialog title for.
- **presetNameA** (*str*) – Name of the Preset.
- **showMakeDefault** (*bool*) – **True** to enable the “Make as default” checkbox in the dialog.
- **setAsDefault** (*bool*) – **True** to make it the default.
- **allowSceneRepository** (*bool*) – **True** to allow to store the preset into the scene repository.

**Returns:** AssetDescription of the newly created asset on success.

**Return type:** [`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### *static* `AssetCreationInterface.SaveDefaultPresetFromObject(l, makeDefault, allowMakeDefault=True)` <a id="maxon.AssetCreationInterface.SaveDefaultPresetFromObject"></a>

Stores the default from the given object into the asset browser.

**Parameters:**

- **l** ([`c4d.GeListNode`](../../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – Object to store.
- **makeDefault** (*bool*) – **True** to make it the default.
- **allowMakeDefault** (*bool*) – **True** to enable the “Make as default” checkbox in the dialog.

### *static* `AssetCreationInterface.SaveDocumentAsset(assetDoc, subType, newAssetId, storeAssetStruct, assetName, versionString, createPreviewBitmapDelegate, copyMetaData, addAssetsIfNotInThisRepository)` <a id="maxon.AssetCreationInterface.SaveDocumentAsset"></a>

Stores the given BaseDocument into the given repository.

**Parameters:**

- **assetDoc** ([`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – BaseDocument to store.
- **subType** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – Optional value to set the subType of the asset.
- **newAssetId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Optional asset Id. If empty the system calculates a new asset id.
- **storeAssetStruct** ([`maxon.StoreAssetStruct`](../../asset/datatype/maxon.StoreAssetStruct.md#module-maxon.StoreAssetStruct)) – Settings where to store the asset.
- **assetName** (*str*) – User readable name of the asset.
- **versionString** (*str*) – User readable version string.
- **createPreviewBitmapDelegate** (Callable[[], `c4d.BaseBitmap`]) – Optional delegate to generate a preview preview bitmap when saving the asset.
- **copyMetaData** ([`maxon.AssetMetaData`](../../asset/reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)) – Optional meta data to copy from another version.
- **addAssetsIfNotInThisRepository** (*bool*) – **True** to store the asset in the given saveRepository even if it’s already in any other repository. **False** would skip the writing.

**Returns:** AssetDescription of the new asset on success.

**Return type:** [`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### *static* `AssetCreationInterface.SaveMemFileAsAsset(saveFileName, parentCategory, subType, calculateMetaData, metaProperties, dependencies, previews, animFps, assetName, localizedNames, localizedAnnotations, copyMetaData)` <a id="maxon.AssetCreationInterface.SaveMemFileAsAsset"></a>

Stores the given url as a asset into a temporary repository.

**Parameters:**

- **saveFileName** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – Url of the asset to be stored.
- **parentCategory** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Parent category in which the asset should be saved.
- **subType** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – SubType of the asset, e.g. [`maxon.ASSETMETADATA.SubType_ENUM_Object`](../../../enums/maxon.ASSETMETADATA.SubType_ENUM_Object.md#maxon.ASSETMETADATA.SubType_ENUM_Object).
- **calculateMetaData** (*bool*) – **True** to automatically calculate meta data when saving.
- **metaProperties** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – Additional metadata to store.
- **dependencies** (*tuple*[*AssetDependencyStruct*]) – Dependencies to store with the asset.
- **previews** ([`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)]) – Array images of Previews. If you pass more then one image it will be stored as animated mp4 with the given animFps frame rate.
- **animFps** (*float*) – If more than one image was given the preview will be stored as mp4 wih this frame rate.
- **assetName** (*str*) – User readable name of the asset.
- **localizedNames** (*tuple*[ *Id*, *String*]) – Optional translated names of the asset in other languages. Id is the languageid from LanguageInterface.
- **localizedAnnotations** (*tuple*[ *Id*, *String*]) – Optional translated descriptions of the asset in other languages. Id is the languageid from LanguageInterface.
- **copyMetaData** ([`maxon.AssetMetaData`](../../asset/reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)) – Metadata to copy.

**Returns:** AssetDescription of the new asset. UpdatableAssetRepositoryRef is a new temporary repository from which the asset can be moved into the target repository.

**Return type:** [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription), bool]

### *static* `AssetCreationInterface.SaveMemFileAsAssetAlone(saveFileName, copyMetaData)` <a id="maxon.AssetCreationInterface.SaveMemFileAsAssetAlone"></a>

Stores the plain file into a temporary repository.

**Parameters:**

- **saveFileName** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – Url of the asset to be stored.
- **copyMetaData** ([`maxon.AssetMetaData`](../../asset/reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)) – Optional meta data to copy.

**Returns:** AssetDescription of the new asset. UpdatableAssetRepositoryRef is a new temporary repository from which the asset can be moved into the target repository.

**Return type:** [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription), [`maxon.UpdatableAssetRepositoryRef`](../../asset/reference/maxon.UpdatableAssetRepositoryRef.md#module-maxon.UpdatableAssetRepositoryRef)]

### *static* `AssetCreationInterface.SaveMemFileAsAssetWithCopyAsset(depResultUrl, storeAssetStruct, subType, dependencies, assetName, addAssetsIfNotInThisRepository)` <a id="maxon.AssetCreationInterface.SaveMemFileAsAssetWithCopyAsset"></a>

Stores the given url as a asset.

**Parameters:**

- **depResultUrl** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – Url of the asset to store.
- **storeAssetStruct** ([`maxon.StoreAssetStruct`](../../asset/datatype/maxon.StoreAssetStruct.md#module-maxon.StoreAssetStruct)) – See StoreAssetStruct.
- **subType** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – SubType of the asset, e.g. [`maxon.ASSETMETADATA.SubType_ENUM_Object`](../../../enums/maxon.ASSETMETADATA.SubType_ENUM_Object.md#maxon.ASSETMETADATA.SubType_ENUM_Object).
- **dependencies** (tuple[[`maxon.AssetDependencyStruct`](../../asset/datatype/maxon.AssetDependencyStruct.md#module-maxon.AssetDependencyStruct)]) – Dependencies to store with the assets.
- **assetName** (Union[ [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), str]) – User readable name of the asset.
- **addAssetsIfNotInThisRepository** (*bool*) – **True** to store the asset in the given saveRepository even if it’s already in any other repository. **False** would skip the writing.

**Returns:** AssetDescription contains the new asset description, Bool is true if the asset is a new asset. False if the asset already existed.

**Return type:** [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription), bool]

### *static* `AssetCreationInterface.SaveMetaDataForAsset(asset, parentCategory, subType, calculateMetaData, metaProperties, dependencies, previews, animFps, assetName, localizedNames, localizedAnnotations)` <a id="maxon.AssetCreationInterface.SaveMetaDataForAsset"></a>

Stores he given values into the asset description.

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to be modified.
- **parentCategory** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Parent category in which the asset should be saved.
- **subType** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – SubType of the asset, e.g. [`maxon.ASSETMETADATA.SubType_ENUM_Object`](../../../enums/maxon.ASSETMETADATA.SubType_ENUM_Object.md#maxon.ASSETMETADATA.SubType_ENUM_Object).
- **calculateMetaData** (*bool*) – **True** to automatically calculate meta data when saving.
- **metaProperties** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – Additional metadata to store.
- **dependencies** (*tuple*[*AssetDependencyStruct*]) – Dependencies to store with the asset.
- **previews** ([`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)]) – Array images of Previews. If you pass more then one image it will be stored as animated mp4 with the given animFps frame rate.
- **animFps** (*float*) – If more than one image was given the preview will be stored as mp4 wih this frame rate.
- **assetName** (*str*) – User readable name of the asset.
- **localizedNames** (*tuple*[ *Id*, *String*]) – Optional translated names of the asset in other languages. Id is the languageid from LanguageInterface.
- **localizedAnnotations** (*tuple*[ *Id*, *String*]) – Optional translated descriptions of the asset in other languages. Id is the languageid from LanguageInterface.

**Returns:** AssetDescription of the new asset. UpdatableAssetRepositoryRef is a new temporary repository from which the asset can be moved into the target repository.

**Return type:** [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription), bool]

### *static* `AssetCreationInterface.SaveTextureAsset(imageUrl, assetName, storeAssetStruct, dependencies, addAssetsIfNotInThisRepository)` <a id="maxon.AssetCreationInterface.SaveTextureAsset"></a>

Stores the given image as media asset.

**Parameters:**

- **imageUrl** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – Url of the texture to store.
- **assetName** (*str*) – Human readable asset name.
- **storeAssetStruct** ([`maxon.StoreAssetStruct`](../../asset/datatype/maxon.StoreAssetStruct.md#module-maxon.StoreAssetStruct)) – Settings where to store the asset.
- **dependencies** (Tuple[ [`maxon.AssetDependencyStruct`](../../asset/datatype/maxon.AssetDependencyStruct.md#module-maxon.AssetDependencyStruct)]) – Optional dependencies to store along with the asset.
- **addAssetsIfNotInThisRepository** (*bool*) – **True** to store the asset in the given saveRepository even if it’s already in any other repository. **False** would skip the writing.

**Returns:**

AssetDescription of the new asset. Bool is **True** if the asset was saved. **False** if it was already in the repository.  
In that case the [`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription) is the one of the existing asset.

**Return type:** Tuple[[`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription), bool]

### *static* `AssetCreationInterface.SetDefaultObject(defaultsType, partial, bc, setAsDefault, allowMakeDefault)` <a id="maxon.AssetCreationInterface.SetDefaultObject"></a>

**Parameters:**

- **defaultsType** ([`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [int]) – Ids of the BaseObject. e.g. Ocube
- **partial** (*bool*) – **True** to signal that this preset contains only partial settings.
- **bc** ([`c4d.BaseContainer`](../../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – BaseContainer with the settings.
- **setAsDefault** (*bool*) – **True** to make this preset the default when creating new objects.
- **allowMakeDefault** (*bool*) – **True** to enable the “Make as default” checkbox in the dialog.

**Returns:** **True** on success.

**Return type:** bool

### *static* `AssetCreationInterface.SupportDefaultPresets(l)` <a id="maxon.AssetCreationInterface.SupportDefaultPresets"></a>

Helper function to find if the given type supports the preset system.

**Parameters:** **l** ([`c4d.C4DAtom`](../../../../c4d/C4DAtom/index.md#c4d.C4DAtom)) – Object to check

**Returns:** Tuple\<Bool, Bool>: first - support presets, second - support set as default

**Return type:** [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [bool, bool]

### *static* `AssetCreationInterface.UpdateMetaData(doc, metaProperties=None, calcBoundingBox=None, objectMatrix=None, subType=None)` <a id="maxon.AssetCreationInterface.UpdateMetaData"></a>

UpdateMetaData recalculates the asset metadata.

For scene files this might be the number of points, polygons. etc. for images the size, bitdepth etc.  
Only next calls are allowed:

> - UpdateMetaData(doc: [`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription))
> - UpdateMetaData(doc: [`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument), metaProperties: [`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary), calcBoundingBox: bool, objectMatrix: [`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix), subType: [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id))

**Parameters:**

- **doc** (Union[[`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription), [`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]) – Asset or BaseDocument to evaluate.
- **metaProperties** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – DataDictionary to store the data.
- **calcBoundingBox** (*bool*) – True to calculate the bounding box of the scene.
- **objectMatrix** ([`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix)) – Optional matrix to add to the object.
- **subType** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – SubType of the asset, e.g. [`maxon.ASSETMETADATA.SubType_ENUM_Object`](../../../enums/maxon.ASSETMETADATA.SubType_ENUM_Object.md#maxon.ASSETMETADATA.SubType_ENUM_Object).

### *static* `AssetCreationInterface.UpdateSubtypeAndMetaData(list, force)` <a id="maxon.AssetCreationInterface.UpdateSubtypeAndMetaData"></a>

UpdateSubtypeAndMetaData determines subtype and calculates meta data for a list of assets. Assets which already have a subtype are excluded unless force is True.

**Parameters:**

- **list** (Union[[`maxon.AssetRepositoryRef`](../../asset/reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef), [`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [[`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)]) – An AssetRepositoryRef or a block of AssetDescriptions.
- **force** (*bool*) – True to force the update of meta data even if a subtype already exists, False otherwise.
