<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/LayerShaderLayer/index.html -->

# c4d.LayerShaderLayer <a id="c4d-layershaderlayer"></a>

## *class* `c4d.LayerShaderLayer` <a id="c4d.LayerShaderLayer"></a>

Represents a layer in a [`LayerShader`](../C4DAtom/GeListNode/BaseList2D/BaseShader/LayerShader/index.md#c4d.LayerShader).

*New in version R17.032.*

> **Warning:** This type cannot be instantiated.

## Overview <a id="overview"></a>

**Layer Inspection**

- [`LayerShaderLayer.GetName()`](#c4d.LayerShaderLayer.GetName): Gets the name of the layer.
- [`LayerShaderLayer.GetPreview()`](#c4d.LayerShaderLayer.GetPreview): Retrieves the preview bitmap.
- [`LayerShaderLayer.GetType()`](#c4d.LayerShaderLayer.GetType): Gets the layer type.

**Layer Navigation And Parameters**

- [`LayerShaderLayer.GetNext()`](#c4d.LayerShaderLayer.GetNext): Gets the next layer.
- [`LayerShaderLayer.GetParameter()`](#c4d.LayerShaderLayer.GetParameter): Retrieves layer parameters.
- [`LayerShaderLayer.SetParameter()`](#c4d.LayerShaderLayer.SetParameter): Sets layer parameters.

## Members <a id="members"></a>

### Layer Inspection <a id="c4d.LayerShaderLayer-method-Layer-Inspection"></a>

#### `LayerShaderLayer.GetName(self, doc)` <a id="c4d.LayerShaderLayer.GetName"></a>

Gets the name of the layer.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the operation.

**Return type:** str

**Returns:** The layer name.

#### `LayerShaderLayer.GetPreview(self)` <a id="c4d.LayerShaderLayer.GetPreview"></a>

Retrieves the preview bitmap.

**Return type:** [c4d.bitmaps.BaseBitmap](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)

**Returns:** The preview bitmap.

#### `LayerShaderLayer.GetType(self)` <a id="c4d.LayerShaderLayer.GetType"></a>

Gets the layer type.

**Return type:** int

**Returns:**

The layer type:

|   |   |
|---|---|
| *TypeUnknown* | Unknown layer. |
| *TypeFolder* | Folder. |
| *TypeShader* | Shader. |
| *TypeBrightnessContrast* | Brightness/Contrast. |
| *TypeHSL* | HSL. |
| *TypePosterize* | Posterize. |
| *TypeColorize* | Colorize. |
| *TypeClamp* | Clamp. |
| *TypeClip* | Clip. |
| *TypeDistorter* | Distorter. |
| *TypeTransform* | Transformation. |

### Layer Navigation And Parameters <a id="c4d.LayerShaderLayer-method-Layer-Navigation-And-Parameters"></a>

#### `LayerShaderLayer.GetNext(self)` <a id="c4d.LayerShaderLayer.GetNext"></a>

Gets the next layer.

> **Note:** Use this method to navigate trough the layers of a layer shader.

**Return type:** Optional[[c4d.LayerShaderLayer](#c4d.LayerShaderLayer)]

**Returns:** The next layer.

#### `LayerShaderLayer.GetParameter(self, id)` <a id="c4d.LayerShaderLayer.GetParameter"></a>

Retrieves layer parameters.

> > **Note:** See Layer Shader Library documentation in the C++ SDK for the information on the parameter IDs and types.

**Parameters:** **id** (*int*) – The ID of the parameter to get.

**Return type:** Any

**Returns:** The parameter value.

#### `LayerShaderLayer.SetParameter(self, id, data)` <a id="c4d.LayerShaderLayer.SetParameter"></a>

Sets layer parameters.

> > **Note:** See Layer Shader Library documentation in the C++ SDK for the information on the parameter IDs and types.

**Parameters:**

- **id** (*int*) – The ID of the parameter to set.
- **data** (*any*) – The new parameter value.

**Return type:** bool

**Returns:** **True** if the parameter could be set, otherwise **False**.
