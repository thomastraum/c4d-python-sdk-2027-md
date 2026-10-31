<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.bitmaps/BaseBitmap/MultipassBitmap/index.html -->

# c4d.bitmaps.MultipassBitmap <a id="c4d-bitmaps-multipassbitmap"></a>

## *class* `c4d.bitmaps.MultipassBitmap` <a id="c4d.bitmaps.MultipassBitmap"></a>

This is an extension of the [`BaseBitmap`](../index.md#c4d.bitmaps.BaseBitmap) class that  
supports higher bit depths, even floating point images, and multiple layers.  
The layers are stored hierarchically. There are three kinds of layers:

> |   |   |
> |---|---|
> | *Layer* | A regular layer, with full range of functionality. |
> | *Folder* | A collection of layers. This is a dummy element that has no image content, but other stuff like name, visibility etc. |
> | *Alpha* | An alpha channel, with full range of functionality. |

Parent Class:

- [`c4d.bitmaps.BaseBitmap`](../index.md#c4d.bitmaps.BaseBitmap)

## Overview <a id="overview"></a>

- [`MultipassBitmap.AllocWrapper()`](#c4d.bitmaps.MultipassBitmap.AllocWrapper): Allocates a multipass wrapper for bmp.

**Add Methods**

- [`MultipassBitmap.AddAlpha()`](#c4d.bitmaps.MultipassBitmap.AddAlpha): Adds an alpha layer with mode *colormode* after *insertafter* in the bitmap.
- [`MultipassBitmap.AddFolder()`](#c4d.bitmaps.MultipassBitmap.AddFolder): Adds a folder after *insertafter* in the bitmap.
- [`MultipassBitmap.AddLayer()`](#c4d.bitmaps.MultipassBitmap.AddLayer): Adds a layer after *insertafter* with mode *colormode* after *insertafter* in the bitmap.

**Deprecated**

- [`MultipassBitmap.GetHiddneLayerNum()`](#c4d.bitmaps.MultipassBitmap.GetHiddneLayerNum): Use `MultipassBitmap.GetHiddenLayerNum()` instead.

**General**

- [`MultipassBitmap.ClearImageData()`](#c4d.bitmaps.MultipassBitmap.ClearImageData): Clears the image data for all layers.
- [`MultipassBitmap.DeleteLayer()`](#c4d.bitmaps.MultipassBitmap.DeleteLayer): Deletes *layer* from the bitmap, freeing the memory.
- [`MultipassBitmap.FindUserID()`](#c4d.bitmaps.MultipassBitmap.FindUserID): Finds a layer in the bitmap by ID.
- [`MultipassBitmap.FreeHiddenLayers()`](#c4d.bitmaps.MultipassBitmap.FreeHiddenLayers): Free the hidden layers.
- [`MultipassBitmap.GetPaintBitmap()`](#c4d.bitmaps.MultipassBitmap.GetPaintBitmap): Gets a BodyPaint 3D paint bitmap for the multipass bitmap.

**Layer Methods**

- [`MultipassBitmap.GetAlphaLayerCount()`](#c4d.bitmaps.MultipassBitmap.GetAlphaLayerCount): Retrieves the number of alpha layers in the bitmap.
- [`MultipassBitmap.GetHiddenLayerCount()`](#c4d.bitmaps.MultipassBitmap.GetHiddenLayerCount): Retrieves the number of hidden layers in the bitmap.
- [`MultipassBitmap.GetLayerCount()`](#c4d.bitmaps.MultipassBitmap.GetLayerCount): Retrieves the number of layers in the bitmap.
- [`MultipassBitmap.GetLayers()`](#c4d.bitmaps.MultipassBitmap.GetLayers): Gets all the layers specified by *flags*.

**Magic Methods**

- [`MultipassBitmap.__init__()`](#c4d.bitmaps.MultipassBitmap.__init__): Allocates a multipass bitmap of size bx/by and bit depth given by mode.

**Parameter Methods**

- [`MultipassBitmap.GetAlphaLayerNum()`](#c4d.bitmaps.MultipassBitmap.GetAlphaLayerNum): Gets the alpha layer with number *num*.
- [`MultipassBitmap.GetHiddenLayerNum()`](#c4d.bitmaps.MultipassBitmap.GetHiddenLayerNum): Gets the hidden layer with number *num*.
- [`MultipassBitmap.GetLayerNum()`](#c4d.bitmaps.MultipassBitmap.GetLayerNum): Gets the layer with number *num*.
- [`MultipassBitmap.GetParameter()`](#c4d.bitmaps.MultipassBitmap.GetParameter): Gets a layer parameter.
- [`MultipassBitmap.SetParameter()`](#c4d.bitmaps.MultipassBitmap.SetParameter): Sets a layer parameter.

## Members <a id="members"></a>

### General <a id="c4d.bitmaps.MultipassBitmap-staticmethod-General"></a>

#### *static* `MultipassBitmap.AllocWrapper(bmp)` <a id="c4d.bitmaps.MultipassBitmap.AllocWrapper"></a>

Allocates a multipass wrapper for bmp.  
The returned multipass wrapper can be modified freely since the initial bmp is copied.

**Parameters:** **bmp** ([*c4d.bitmaps.BaseBitmap*](../index.md#c4d.bitmaps.BaseBitmap)) – The bitmap to wrap. The caller owns the pointed bitmap.

**Return type:** Optional[[MultipassBitmap](#c4d.bitmaps.MultipassBitmap)]

**Returns:** The allocated MultipassBitmap, or None if the allocation failed.

### Add Methods <a id="c4d.bitmaps.MultipassBitmap-method-Add-Methods"></a>

#### `MultipassBitmap.AddAlpha(self, insertafter, colormode)` <a id="c4d.bitmaps.MultipassBitmap.AddAlpha"></a>

Adds an alpha layer with mode *colormode* after *insertafter* in the bitmap.

**Parameters:**

- **insertafter** ([*c4d.bitmaps.MultipassBitmap*](#c4d.bitmaps.MultipassBitmap)) – The layer to insert after.

- **colormode** (*int*) –

  Color mode of the new alpha layer.

  |   |   |
  |---|---|
  | *COLORMODE_ILLEGAL* | Illegal 8-bit mode. |
  | *COLORMODE_ALPHA* | Only 8-bit alpha channel. |
  | *COLORMODE_GRAY* | 8-bit grayscale channel. |
  | *COLORMODE_AGRAY* | 8-bit grayscale channel with 8-bit alpha. |
  | *COLORMODE_RGB* | 8-bit RGB channels. |
  | *COLORMODE_ARGB* | 8-bit RGB channels with 8-bit alpha. |
  | *COLORMODE_CMYK* | 8-bit CMYK channel. |
  | *COLORMODE_ACMYK* | 8-bit CMYK channel with 8-bit alpha. |
  | *COLORMODE_MASK* | 8-bit grayscale map as mask. |
  | *COLORMODE_AMASK* | 8-bit grayscale map as mask with 8-bit alpha. |
  | *COLORMODE_ILLEGALw* | Illegal 16-bit mode. |
  | *COLORMODE_GRAYw* | 16-bit grayscale channel. |
  | *COLORMODE_AGRAYw* | 16-bit grayscale channel with 16-bit alpha. |
  | *COLORMODE_RGBw* | 16-bit RGB channels. |
  | *COLORMODE_ARGBw* | 16-bit RGB channels with 16-bit alpha. |
  | *COLORMODE_MASKw* | 16-bit grayscale map as mask with 16-bit alpha. |
  | *COLORMODE_ILLEGALf* | Illegal 32-bit mode. |
  | *COLORMODE_GRAYf* | 32-bit floating point grayscale channel. |
  | *COLORMODE_AGRAYf* | 32-bit floating point grayscale channel with floating point alpha. |
  | *COLORMODE_RGBf* | 32-bit floating point RGB channels. |
  | *COLORMODE_ARGBf* | 32-bit floating point RGB channels with floating point alpha. |
  | *COLORMODE_MASKf* | 32-bit floating point grayscale map as mask. |

**Return type:** Optional[[c4d.bitmaps.MultipassBitmap](#c4d.bitmaps.MultipassBitmap)]

**Returns:** The added alpha layer or **None**

#### `MultipassBitmap.AddFolder(self, insertafter, hidden=False)` <a id="c4d.bitmaps.MultipassBitmap.AddFolder"></a>

Adds a folder after *insertafter* in the bitmap.

**Parameters:**

- **insertafter** ([*c4d.bitmaps.MultipassBitmap*](#c4d.bitmaps.MultipassBitmap)) – The layer to insert after.
- **hidden** (*bool*) – If this is **True**, the layer is hidden.

**Return type:** Optional[[c4d.bitmaps.MultipassBitmap](#c4d.bitmaps.MultipassBitmap)]

**Returns:** The added folder or **None**.

#### `MultipassBitmap.AddLayer(self, insertafter, colormode, hidden=False)` <a id="c4d.bitmaps.MultipassBitmap.AddLayer"></a>

Adds a layer after *insertafter* with mode *colormode* after *insertafter* in the bitmap.

**Parameters:**

- **insertafter** ([*c4d.bitmaps.MultipassBitmap*](#c4d.bitmaps.MultipassBitmap)) – The layer to insert after.

- **colormode** (*int*) –

  Color mode of the new layer:

  |   |   |
  |---|---|
  | *COLORMODE_ILLEGAL* | Illegal 8-bit mode. |
  | *COLORMODE_ALPHA* | Only 8-bit alpha channel. |
  | *COLORMODE_GRAY* | 8-bit grayscale channel. |
  | *COLORMODE_AGRAY* | 8-bit grayscale channel with 8-bit alpha. |
  | *COLORMODE_RGB* | 8-bit RGB channels. |
  | *COLORMODE_ARGB* | 8-bit RGB channels with 8-bit alpha. |
  | *COLORMODE_CMYK* | 8-bit CMYK channel. |
  | *COLORMODE_ACMYK* | 8-bit CMYK channel with 8-bit alpha. |
  | *COLORMODE_MASK* | 8-bit grayscale map as mask. |
  | *COLORMODE_AMASK* | 8-bit grayscale map as mask with 8-bit alpha. |
  | *COLORMODE_ILLEGALw* | Illegal 16-bit mode. |
  | *COLORMODE_GRAYw* | 16-bit grayscale channel. |
  | *COLORMODE_AGRAYw* | 16-bit grayscale channel with 16-bit alpha. |
  | *COLORMODE_RGBw* | 16-bit RGB channels. |
  | *COLORMODE_ARGBw* | 16-bit RGB channels with 16-bit alpha. |
  | *COLORMODE_MASKw* | 16-bit grayscale map as mask with 16-bit alpha. |
  | *COLORMODE_ILLEGALf* | Illegal 32-bit mode. |
  | *COLORMODE_GRAYf* | 32-bit floating point grayscale channel. |
  | *COLORMODE_AGRAYf* | 32-bit floating point grayscale channel with floating point alpha. |
  | *COLORMODE_RGBf* | 32-bit floating point RGB channels. |
  | *COLORMODE_ARGBf* | 32-bit floating point RGB channels with floating point alpha. |
  | *COLORMODE_MASKf* | 32-bit floating point grayscale map as mask. |

- **hidden** (*bool*) – If this is **True**, the layer is hidden.

### Deprecated <a id="c4d.bitmaps.MultipassBitmap-method-Deprecated"></a>

#### `MultipassBitmap.GetHiddneLayerNum(self, num)` <a id="c4d.bitmaps.MultipassBitmap.GetHiddneLayerNum"></a>

*Deprecated since version R21.204:* Use `MultipassBitmap.GetHiddenLayerNum()` instead.

Gets the hidden layer with number *num*.

**Parameters:** **num** (*int*) – Hidden layer index, *0* <= *num* < [`GetHiddenLayerCount()`](#c4d.bitmaps.MultipassBitmap.GetHiddenLayerCount).

**Return type:** Optional[[c4d.bitmaps.MultipassBitmap](#c4d.bitmaps.MultipassBitmap)]

**Returns:** The retrieved layer, or **None** if the operation failed.

### General <a id="c4d.bitmaps.MultipassBitmap-method-General"></a>

#### `MultipassBitmap.ClearImageData(self)` <a id="c4d.bitmaps.MultipassBitmap.ClearImageData"></a>

Clears the image data for all layers.

> **Note:** The layers themselves are not removed or deleted.

#### `MultipassBitmap.DeleteLayer(self, layer)` <a id="c4d.bitmaps.MultipassBitmap.DeleteLayer"></a>

Deletes *layer* from the bitmap, freeing the memory.

**Parameters:** **layer** ([*c4d.bitmaps.MultipassBitmap*](#c4d.bitmaps.MultipassBitmap)) – The layer to delete. Never access this reference afterwards.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `MultipassBitmap.FindUserID(self, id, subid=0)` <a id="c4d.bitmaps.MultipassBitmap.FindUserID"></a>

Finds a layer in the bitmap by ID.

**Parameters:**

- **id** (*int*) – Main layer ID.
- **subid** (*int*) – Sub ID.

**Return type:** Optional[[c4d.bitmaps.MultipassBitmap](#c4d.bitmaps.MultipassBitmap)]

**Returns:** The found layer or **None**.

#### `MultipassBitmap.FreeHiddenLayers(self)` <a id="c4d.bitmaps.MultipassBitmap.FreeHiddenLayers"></a>

Free the hidden layers.

#### `MultipassBitmap.GetPaintBitmap(self)` <a id="c4d.bitmaps.MultipassBitmap.GetPaintBitmap"></a>

Gets a BodyPaint 3D paint bitmap for the multipass bitmap.

**Return type:** [c4d.modules.bodypaint.PaintBitmap](../../../c4d.modules/bodypaint/PaintBitmap/index.md#c4d.modules.bodypaint.PaintBitmap)

**Returns:** The paint bitmap.

### Layer Methods <a id="c4d.bitmaps.MultipassBitmap-method-Layer-Methods"></a>

#### `MultipassBitmap.GetAlphaLayerCount(self)` <a id="c4d.bitmaps.MultipassBitmap.GetAlphaLayerCount"></a>

Retrieves the number of alpha layers in the bitmap.

**Return type:** int

**Returns:** Alpha layer count.

#### `MultipassBitmap.GetHiddenLayerCount(self)` <a id="c4d.bitmaps.MultipassBitmap.GetHiddenLayerCount"></a>

Retrieves the number of hidden layers in the bitmap.

**Return type:** int

**Returns:** Hidden layer count.

#### `MultipassBitmap.GetLayerCount(self, num)` <a id="c4d.bitmaps.MultipassBitmap.GetLayerCount"></a>

Retrieves the number of layers in the bitmap.  
This is the sum of the number of layers, folders and alphas that are direct children of this bitmap.

**Parameters:** **num** (*int*) – Hidden layer index, *0* <= *num* < [`GetHiddenLayerCount()`](#c4d.bitmaps.MultipassBitmap.GetHiddenLayerCount).

**Return type:** int

**Returns:** Layer count.

#### `MultipassBitmap.GetLayers(self, flags=6)` <a id="c4d.bitmaps.MultipassBitmap.GetLayers"></a>

Gets all the layers specified by *flags*.

*New in version R14.014.*

**Parameters:**

**flags** (*int*) –

Flags:

|   |   |
|---|---|
| *MPB_GETLAYERS_NONE* | None. |
| *MPB_GETLAYERS_ALPHA* | Get alpha layers. |
| *MPB_GETLAYERS_IMAGE* | Get image layers. |

**Return type:** List[[c4d.bitmaps.BaseBitmap](../index.md#c4d.bitmaps.BaseBitmap)]

**Returns:** The layers.

### Magic Methods <a id="c4d.bitmaps.MultipassBitmap-method-Magic-Methods"></a>

#### `MultipassBitmap.__init__(self, bx, by, mode)` <a id="c4d.bitmaps.MultipassBitmap.__init__"></a>

Allocates a multipass bitmap of size bx/by and bit depth given by mode.  
The first RGBA layer is also created.

**Parameters:**

- **bx** (*int*) – Width in pixels.

- **bx** – Height in pixels.

- **mode** (*int*) –

  Main mode:

  |   |   |
  |---|---|
  | *COLORMODE_ILLEGAL* | Illegal 8-bit mode. |
  | *COLORMODE_ALPHA* | Only 8-bit alpha channel. |
  | *COLORMODE_GRAY* | 8-bit grayscale channel. |
  | *COLORMODE_AGRAY* | 8-bit grayscale channel with 8-bit alpha. |
  | *COLORMODE_RGB* | 8-bit RGB channels. |
  | *COLORMODE_ARGB* | 8-bit RGB channels with 8-bit alpha. |
  | *COLORMODE_CMYK* | 8-bit CMYK channel. |
  | *COLORMODE_ACMYK* | 8-bit CMYK channel with 8-bit alpha. |
  | *COLORMODE_MASK* | 8-bit grayscale map as mask. |
  | *COLORMODE_AMASK* | 8-bit grayscale map as mask with 8-bit alpha. |
  | *COLORMODE_ILLEGALw* | Illegal 16-bit mode. |
  | *COLORMODE_GRAYw* | 16-bit grayscale channel. |
  | *COLORMODE_AGRAYw* | 16-bit grayscale channel with 16-bit alpha. |
  | *COLORMODE_RGBw* | 16-bit RGB channels. |
  | *COLORMODE_ARGBw* | 16-bit RGB channels with 16-bit alpha. |
  | *COLORMODE_MASKw* | 16-bit grayscale map as mask with 16-bit alpha. |
  | *COLORMODE_ILLEGALf* | Illegal 32-bit mode. |
  | *COLORMODE_GRAYf* | 32-bit floating point grayscale channel. |
  | *COLORMODE_AGRAYf* | 32-bit floating point grayscale channel with floating point alpha. |
  | *COLORMODE_RGBf* | 32-bit floating point RGB channels. |
  | *COLORMODE_ARGBf* | 32-bit floating point RGB channels with floating point alpha. |
  | *COLORMODE_MASKf* | 32-bit floating point grayscale map as mask. |

### Parameter Methods <a id="c4d.bitmaps.MultipassBitmap-method-Parameter-Methods"></a>

#### `MultipassBitmap.GetAlphaLayerNum(self, num)` <a id="c4d.bitmaps.MultipassBitmap.GetAlphaLayerNum"></a>

Gets the alpha layer with number *num*.

**Parameters:** **num** (*int*) – Alpha layer index, *0* <= *num* < [`GetAlphaLayerCount()`](#c4d.bitmaps.MultipassBitmap.GetAlphaLayerCount).

**Return type:** Optional[[c4d.bitmaps.MultipassBitmap](#c4d.bitmaps.MultipassBitmap)]

**Returns:** The retrieved layer, or **None** if the operation failed.

#### `MultipassBitmap.GetHiddenLayerNum(self, num)` <a id="c4d.bitmaps.MultipassBitmap.GetHiddenLayerNum"></a>

Gets the hidden layer with number *num*.

**Parameters:** **num** (*int*) – Hidden layer index, *0* <= *num* < [`GetHiddenLayerCount()`](#c4d.bitmaps.MultipassBitmap.GetHiddenLayerCount).

**Return type:** Optional[[c4d.bitmaps.MultipassBitmap](#c4d.bitmaps.MultipassBitmap)]

**Returns:** The retrieved layer, or **None** if the operation failed.

#### `MultipassBitmap.GetLayerNum(self, num)` <a id="c4d.bitmaps.MultipassBitmap.GetLayerNum"></a>

Gets the layer with number *num*.

**Parameters:** **num** (*int*) – Layer index, *0* <= *num* < [`GetLayerCount()`](#c4d.bitmaps.MultipassBitmap.GetLayerCount).

**Return type:** Optional[[c4d.bitmaps.MultipassBitmap](#c4d.bitmaps.MultipassBitmap)]

**Returns:** The retrieved layer, or **None** if the operation failed.

#### `MultipassBitmap.GetParameter(self, id)` <a id="c4d.bitmaps.MultipassBitmap.GetParameter"></a>

Gets a layer parameter.

**Parameters:**

**id** (*int*) –

The layer parameter ID:

|   |   |   |
|---|---|---|
| *MPBTYPE_SHOW* | bool | Determines if the layer will be shown in the external render window. (The Cinema 4D renderer modifies this value itself.) |
| *MPBTYPE_SAVE* | bool | Determines if the layer is saved with the image or not if *SAVEBIT_USESELECTEDLAYERS* is used. |
| *MPBTYPE_PERCENT* | float | The blend parameter, between *0.0* and *1.0*. |
| *MPBTYPE_BLENDMODE* | int | The blend mode. (*LAYER_NORMAL*, *LAYER_DISSOLVE* etc. from from *bplayer.h.*) |
| *MPBTYPE_COLORMODE* | int | The color mode: See [COLORMODE](../../../../consts/COLORMODE.md). |
| *MPBTYPE_BITMAPTYPE* | int | The bitmap type. Cannot be set with `MultipassBitmap.SetParameter()`. |
| *MPBTYPE_NAME* | str | The layer name. Only a [`PaintLayerBmp`](../../../c4d.modules/bodypaint/PaintBitmap/PaintLayer/PaintLayerBmp/index.md#c4d.modules.bodypaint.PaintLayerBmp) or [`PaintLayerFolder`](../../../c4d.modules/bodypaint/PaintBitmap/PaintLayer/PaintLayerFolder/index.md#c4d.modules.bodypaint.PaintLayerFolder) can have a name. |
| *MPBTYPE_DPI* | int | The resolution in DPI. **Private.** |
| *MPBTYPE_USERID* | int | The user ID for the layer. In the renderer this is *VPBUFFER_xxx*. |
| *MPBTYPE_USERSUBID* | int | The user sub-ID for the layer. In the renderer this is used for blend channels for instance. |
| *MPBTYPE_FORCEBLEND* | int | The special mode used to force blend layers. |

**Return type:** Optional[Any]

**Returns:** The retrieved layer parameter data. Can be **None**.

#### `MultipassBitmap.SetParameter(self, id, t_data)` <a id="c4d.bitmaps.MultipassBitmap.SetParameter"></a>

Sets a layer parameter.

**Parameters:**

- **id** (*int*) –

  The layer parameter ID:

  |   |   |   |
  |---|---|---|
  | *MPBTYPE_SHOW* | bool | Determines if the layer will be shown in the external render window. (The Cinema 4D renderer modifies this value itself.) |
  | *MPBTYPE_SAVE* | bool | Determines if the layer is saved with the image or not if *SAVEBIT_USESELECTEDLAYERS* is used. |
  | *MPBTYPE_PERCENT* | float | The blend parameter, between *0.0* and *1.0*. |
  | *MPBTYPE_BLENDMODE* | int | The blend mode. (*LAYER_NORMAL*, *LAYER_DISSOLVE* etc. from from *bplayer.h.*) |
  | *MPBTYPE_COLORMODE* | int | The color mode: See [COLORMODE](../../../../consts/COLORMODE.md). |
  | *MPBTYPE_BITMAPTYPE* | int | The bitmap type. Cannot be set with `MultipassBitmap.SetParameter()`. |
  | *MPBTYPE_NAME* | str | The layer name. Only a [`PaintLayerBmp`](../../../c4d.modules/bodypaint/PaintBitmap/PaintLayer/PaintLayerBmp/index.md#c4d.modules.bodypaint.PaintLayerBmp) or [`PaintLayerFolder`](../../../c4d.modules/bodypaint/PaintBitmap/PaintLayer/PaintLayerFolder/index.md#c4d.modules.bodypaint.PaintLayerFolder) can have a name. |
  | *MPBTYPE_DPI* | int | The resolution in DPI. **Private.** |
  | *MPBTYPE_USERID* | int | The user ID for the layer. In the renderer this is *VPBUFFER_xxx*. |
  | *MPBTYPE_USERSUBID* | int | The user sub-ID for the layer. In the renderer this is used for blend channels for instance. |
  | *MPBTYPE_FORCEBLEND* | int | The special mode used to force blend layers. |

- **t_data** (*any*) – The new parameter data.

**Return type:** Any

**Returns:** **True** if the layer parameter was successfully set, otherwise **False**.
