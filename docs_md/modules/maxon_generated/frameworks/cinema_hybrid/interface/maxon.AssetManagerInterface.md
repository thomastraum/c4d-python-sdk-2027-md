<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/cinema_hybrid/interface/maxon.AssetManagerInterface.html -->

# maxon.AssetManagerInterface <a id="maxon-assetmanagerinterface"></a>

## Description <a id="module-maxon.AssetManagerInterface"></a><a id="description"></a>

Helper class to control the Asset Manager.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`CheckDownloadAssetWithModalProgressDialog`](#maxon.AssetManagerInterface.CheckDownloadAssetWithModalProgressDialog)(…) | Checks if an asset is already cached and if not it will download the asset with a modal progress dialog which can be canceled. |
| [`GetSelectedAssets`](#maxon.AssetManagerInterface.GetSelectedAssets)(*args) | Returns an array of asset descriptions for the selected assets of the active asset browser. |
| [`LoadAssets`](#maxon.AssetManagerInterface.LoadAssets)(searchRepository, …[, …]) | LoadAssets executes the load asset command from the asset browser (e.g. |
| [`OpenPopup`](#maxon.AssetManagerInterface.OpenPopup)(flags, masterFilter, filterString) | Opens an asset selection popup. |
| [`RevealAsset`](#maxon.AssetManagerInterface.RevealAsset)(assets) | Opens the asset browser to show the given assets in the browser. |
| [`SearchAssets`](#maxon.AssetManagerInterface.SearchAssets)(filterString, typeFilter, limit) | Runs an Asset Browser search without opening any UI and returns the matching assets. |
| [`SetActiveManager`](#maxon.AssetManagerInterface.SetActiveManager)(masterFilter[, presenter, …]) | Sets the active asset manager mode. |

## Methods Definition <a id="methods-definition"></a>

### *static* `AssetManagerInterface.CheckDownloadAssetWithModalProgressDialog(asset, lookupRepository)` <a id="maxon.AssetManagerInterface.CheckDownloadAssetWithModalProgressDialog"></a>

Checks if an asset is already cached and if not it will download the asset with a modal progress dialog which can be canceled.

Canceling the dialog will continue the download but returns **False**. Dependencies will be added to the download queue as well.

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – Asset to inspect/download.
- **lookupRepository** ([`maxon.AssetRepositoryRef`](../../asset/reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to check dependencies for.

**Returns:** **True** if done. **False** if cancelled.

**Return type:** bool

### *static* `AssetManagerInterface.GetSelectedAssets(*args)` <a id="maxon.AssetManagerInterface.GetSelectedAssets"></a>

Returns an array of asset descriptions for the selected assets of the active asset browser. :return: Array of selected asset descriptions. :rtype: [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)]

### *static* `AssetManagerInterface.LoadAssets(searchRepository, selectionAndFilterString, presenter=None, graphModelRef=None)` <a id="maxon.AssetManagerInterface.LoadAssets"></a>

LoadAssets executes the load asset command from the asset browser (e.g. double click or open).

**Parameters:**

- **searchRepository** ([`maxon.AssetRepositoryRef`](../../asset/reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Search repository.
- **selectionAndFilterString** (list[Union[Tuple[[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), str], list[[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), str]]]) – A list which contains the search terms to switch modes in the newly created node/object.
- **presenter** (*None*) – Not yet implemented, pass None.
- **graphModelRef** ([`maxon.NodesGraphModelRef`](../../nodes/reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)) – Optional parameter to pass the node graph where to insert nodes.

**Returns:** **True** if loaded. **False** indicates another error state.

**Return type:** bool

### *static* `AssetManagerInterface.OpenPopup(flags, masterFilter, filterString, smartFilter=None, presenter=None, model=None, title='', inSelection=(), outSelection=None)` <a id="maxon.AssetManagerInterface.OpenPopup"></a>

Opens an asset selection popup.

**Parameters:**

- **flags** ([`maxon.ASSETPOPUPOPTIONS`](../../../enums/maxon.ASSETPOPUPOPTIONS.md#module-maxon.ASSETPOPUPOPTIONS)) – see ASSETPOPUPOPTIONS.
- **masterFilter** ([`maxon.MASTERFILTER`](../../../enums/maxon.MASTERFILTER.md#module-maxon.MASTERFILTER)) – see MASTERFILTER.
- **filterString** (*str*) – see FilterString.
- **smartFilter** ([`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – SmartFilter to select.
- **presenter** (*None*) – Not yet implemented, pass None.
- **model** (*None*) – Not yet implemented, pass None.
- **title** (*str*) – Window Title.
- **inSelection** (list([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id))) – Define the selected elements and returns the selected elements (value being changed by the OpenPopup method).
- **outSelection** (Callable[[[`maxon.DragAndDropDataAssetArray`](../../asset/datatype/maxon.DragAndDropDataAssetArray.md#module-maxon.DragAndDropDataAssetArray)], None]) – Delegate.

### *static* `AssetManagerInterface.RevealAsset(assets)` <a id="maxon.AssetManagerInterface.RevealAsset"></a>

Opens the asset browser to show the given assets in the browser.

**Parameters:** **assets** (Union[[`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription), Collection[[`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)], [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)]]) – Assets to show.

### *static* `AssetManagerInterface.SearchAssets(filterString, typeFilter, limit)` <a id="maxon.AssetManagerInterface.SearchAssets"></a>

Runs an Asset Browser search without opening any UI and returns the matching assets.

The filter string is the Asset Browser’s own search syntax, so an *ai:* prefix performs a semantic search. The prefix takes no space after the colon and a multi-word query must be quoted - *ai:”a red leather armchair”* - because the parser splits on the first space. A semantic query returns nothing when the AI service is disabled in the preferences.

**Parameters:**

- **filterString** (*str*) – The search query in Asset Browser filter syntax.
- **typeFilter** (*str*) – Pipe-separated asset types, in the Asset Browser’s own vocabulary: `"model"`, `"scene"`, `"material"`, `"media"`, `"nodetemplate"`, `"operator"`. Use `"model|scene"` for geometry or `"media"` for textures. An empty string searches every type, which mixes textures in with models.
- **limit** (*int*) – Maximum number of assets to return, or 0 for no limit.

**Returns:** The matching assets, best match first for a semantic query.

**Return type:** [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.AssetDescription`](../../asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)]

### *static* `AssetManagerInterface.SetActiveManager(masterFilter, presenter=None, model=None)` <a id="maxon.AssetManagerInterface.SetActiveManager"></a>

Sets the active asset manager mode.

**Parameters:**

- **masterFilter** ([`maxon.MASTERFILTER`](../../../enums/maxon.MASTERFILTER.md#module-maxon.MASTERFILTER)) – see MASTERFILTER.
- **presenter** (*None*) – Optional parameter to pass a NodeGraph presenter.
- **model** ([`maxon.NodesGraphModelRef`](../../nodes/reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)) – Optional parameter to pass a NodeGraph.
