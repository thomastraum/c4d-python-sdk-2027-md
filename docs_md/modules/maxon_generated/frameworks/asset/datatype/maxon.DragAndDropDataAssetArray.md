<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/datatype/maxon.DragAndDropDataAssetArray.html -->

# maxon.DragAndDropDataAssetArray <a id="maxon-draganddropdataassetarray"></a>

## Description <a id="module-maxon.DragAndDropDataAssetArray"></a><a id="description"></a>

Message data for *DRAGTYPE_ASSET*

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)
- [`maxon.Struct`](../../../datatypes/base_core/maxon.Struct.md#module-maxon.Struct)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetAssetDescriptions`](#maxon.DragAndDropDataAssetArray.GetAssetDescriptions)() | Getter to access the asset description. |
| [`GetLookupRepository`](#maxon.DragAndDropDataAssetArray.GetLookupRepository)() | GetLookupRepository getter function. |
| [`SetAssetDescriptions`](#maxon.DragAndDropDataAssetArray.SetAssetDescriptions)(assetDescriptions) | Setter for DndAsset data. |
| [`SetLookupRepository`](#maxon.DragAndDropDataAssetArray.SetLookupRepository)(lookupRepository) | Setter to set the lookup repository. |
| [`__init__`](#maxon.DragAndDropDataAssetArray.__init__)([other]) | Initializes the appropriate C++ Data object and store it within the _data member. |

## Methods Definition <a id="methods-definition"></a>

### `DragAndDropDataAssetArray.GetAssetDescriptions()` <a id="maxon.DragAndDropDataAssetArray.GetAssetDescriptions"></a>

Getter to access the asset description.

**Return type:** tuple[tuple[[`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription), [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url), [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String)]]

### `DragAndDropDataAssetArray.GetLookupRepository()` <a id="maxon.DragAndDropDataAssetArray.GetLookupRepository"></a>

GetLookupRepository getter function.

**Returns:** AssetRepositoryRef where to search for assets.

**Return type:** [`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)

### `DragAndDropDataAssetArray.SetAssetDescriptions(assetDescriptions)` <a id="maxon.DragAndDropDataAssetArray.SetAssetDescriptions"></a>

Setter for DndAsset data.

**Parameters:** **assetDescriptions** (Union[list[tuple[[`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription), [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url), [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String)]], tuple[tuple[[`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription), [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url), [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String)]]]) – Array with assets to drag around.

### `DragAndDropDataAssetArray.SetLookupRepository(lookupRepository)` <a id="maxon.DragAndDropDataAssetArray.SetLookupRepository"></a>

Setter to set the lookup repository.

**Parameters:** **lookupRepository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to search in.

### `DragAndDropDataAssetArray.__init__(other=None)` <a id="maxon.DragAndDropDataAssetArray.__init__"></a>

Initializes the appropriate C++ Data object and store it within the _data member.

If C is a Data then _data store a copy the C++ Data is done and stored.  
If C is a C++ Data then _data store a reference of the C++ Data.  
If C is not defined the C++ data is created and stored in the _data member.

**Parameters:** **C** (Optional[[`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)]) – Input data from which the Data should be created.
