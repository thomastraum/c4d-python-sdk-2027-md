<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.BasePresetAssetInterface.html -->

# maxon.BasePresetAssetInterface <a id="maxon-basepresetassetinterface"></a>

## Description <a id="module-maxon.BasePresetAssetInterface"></a><a id="description"></a>

[`maxon.BasePresetAssetInterface`](#module-maxon.BasePresetAssetInterface) allows to implement details for preset assets.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetInterface`](maxon.AssetInterface.md#module-maxon.AssetInterface)

Child Class:

- [`maxon.BasePresetAsset`](../reference/maxon.BasePresetAsset.md#module-maxon.BasePresetAsset)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.BasePresetAssetInterface.VIRTUAL`](maxon.BasePresetAssetInterface.VIRTUAL.md#maxon.BasePresetAssetInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Apply`](#maxon.BasePresetAssetInterface.Apply)() |  |
| [`GeneratePreview`](#maxon.BasePresetAssetInterface.GeneratePreview)(previewSize, progressRef, …) | **param previewSize:** |
| [`Serialize`](#maxon.BasePresetAssetInterface.Serialize)(outputStream) | **param outputStream:** |

## Methods Definition <a id="methods-definition"></a>

### `BasePresetAssetInterface.Apply()` <a id="maxon.BasePresetAssetInterface.Apply"></a>

### `BasePresetAssetInterface.GeneratePreview(previewSize, progressRef, progressIndex)` <a id="maxon.BasePresetAssetInterface.GeneratePreview"></a>

**Parameters:**

- **previewSize** (*int*) –
- **progressRef** (`maxon.MediaSessionProgressRef`) –
- **progressIndex** (*int*) –

**Returns:**

**Return type:** [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)

### `BasePresetAssetInterface.Serialize(outputStream)` <a id="maxon.BasePresetAssetInterface.Serialize"></a>

**Parameters:** **outputStream** ([`maxon.OutputStreamRef`](../../../references/io/maxon.OutputStreamRef.md#module-maxon.OutputStreamRef)) –
