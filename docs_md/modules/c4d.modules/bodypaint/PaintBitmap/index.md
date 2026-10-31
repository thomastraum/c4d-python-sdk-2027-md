<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/bodypaint/PaintBitmap/index.html -->

# c4d.modules.bodypaint.PaintBitmap <a id="c4d-modules-bodypaint-paintbitmap"></a>

## *class* `c4d.modules.bodypaint.PaintBitmap` <a id="c4d.modules.bodypaint.PaintBitmap"></a>

The abstract base class of all paint classes.  
Can be a texture, material, layer or mask.

Parent Class:

- [`c4d.BaseList2D`](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

Children Classes:

- [`c4d.modules.bodypaint.PaintMaterial`](PaintMaterial/index.md#c4d.modules.bodypaint.PaintMaterial)
- [`c4d.modules.bodypaint.PaintTexture`](PaintTexture/index.md#c4d.modules.bodypaint.PaintTexture)
- [`c4d.modules.bodypaint.PaintLayer`](PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)

## Overview <a id="overview"></a>

**Alpha Channel Editing**

- [`PaintBitmap.AddAlphaChannel()`](#c4d.modules.bodypaint.PaintBitmap.AddAlphaChannel): Add an alpha channel to the layer.
- [`PaintBitmap.AskApplyAlphaMask()`](#c4d.modules.bodypaint.PaintBitmap.AskApplyAlphaMask): Check if an alpha mask can be applied.

**Bitmap Properties**

- [`PaintBitmap.GetBh()`](#c4d.modules.bodypaint.PaintBitmap.GetBh): Get the height of the paint bitmap.
- [`PaintBitmap.GetBw()`](#c4d.modules.bodypaint.PaintBitmap.GetBw): Get the width of the paint bitmap.
- [`PaintBitmap.GetColorMode()`](#c4d.modules.bodypaint.PaintBitmap.GetColorMode): Get the color mode of the paint bitmap.
- [`PaintBitmap.GetPaintTexture()`](#c4d.modules.bodypaint.PaintBitmap.GetPaintTexture): Get the paint texture if possible.

**Layer Structure**

- [`PaintBitmap.GetAlphaFirst()`](#c4d.modules.bodypaint.PaintBitmap.GetAlphaFirst): Get the first alpha channel layer.
- [`PaintBitmap.GetAlphaLast()`](#c4d.modules.bodypaint.PaintBitmap.GetAlphaLast): Get the last alpha channel layer.
- [`PaintBitmap.GetLayerDownFirst()`](#c4d.modules.bodypaint.PaintBitmap.GetLayerDownFirst): Get the first alpha channel layer.
- [`PaintBitmap.GetLayerDownLast()`](#c4d.modules.bodypaint.PaintBitmap.GetLayerDownLast): Get the last child layer.
- [`PaintBitmap.GetParent()`](#c4d.modules.bodypaint.PaintBitmap.GetParent): Get the parent.

**Refresh And Change Tracking**

- [`PaintBitmap.GetDirty()`](#c4d.modules.bodypaint.PaintBitmap.GetDirty): Get dirty count.
- [`PaintBitmap.UpdateRefresh()`](#c4d.modules.bodypaint.PaintBitmap.UpdateRefresh): Refresh an area of the paint bitmap.
- [`PaintBitmap.UpdateRefreshAll()`](#c4d.modules.bodypaint.PaintBitmap.UpdateRefreshAll): Refresh the complete paint bitmap.

## Members <a id="members"></a>

### Alpha Channel Editing <a id="c4d.modules.bodypaint.PaintBitmap-method-Alpha-Channel-Editing"></a>

#### `PaintBitmap.AddAlphaChannel(self, bitdepth, prev=None, undo=True, activate=True)` <a id="c4d.modules.bodypaint.PaintBitmap.AddAlphaChannel"></a>

Add an alpha channel to the layer.

**Parameters:**

- **bitdepth** (*int*) –

  The bit depth of the alpha channel:

  |   |   |
  |---|---|
  | *BITDEPTH_SHIFT* |  |
  | *BITDEPTH_MAXMODES* |  |
  | *BITDEPTH_UCHAR* |  |
  | *BITDEPTH_UWORD* |  |
  | *BITDEPTH_FLOAT* |  |

- **prev** (*Optional*[[*c4d.modules.bodypaint.PaintLayer*](PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)]) – Optional point to insert the alpha channel.

- **undo** (*bool*) – **True** to create an undo on the undo stack, otherwise **False**.

- **activate** (*bool*) – If **True** alpha channel will be activated.

**Return type:** Optional[[c4d.modules.bodypaint.PaintLayerBmp](PaintLayer/PaintLayerBmp/index.md#c4d.modules.bodypaint.PaintLayerBmp)]

**Returns:** The added alpha channel, or **None** if it failed.

#### `PaintBitmap.AskApplyAlphaMask(self)` <a id="c4d.modules.bodypaint.PaintBitmap.AskApplyAlphaMask"></a>

Check if an alpha mask can be applied.

**Return type:** bool

**Returns:** **True** if an alpha mask can be applied, otherwise **False**.

### Bitmap Properties <a id="c4d.modules.bodypaint.PaintBitmap-method-Bitmap-Properties"></a>

#### `PaintBitmap.GetBh(self)` <a id="c4d.modules.bodypaint.PaintBitmap.GetBh"></a>

Get the height of the paint bitmap.

**Return type:** int

**Returns:** The height of the paint bitmap.

#### `PaintBitmap.GetBw(self)` <a id="c4d.modules.bodypaint.PaintBitmap.GetBw"></a>

Get the width of the paint bitmap.

**Return type:** int

**Returns:** The width of the paint bitmap.

#### `PaintBitmap.GetColorMode(self)` <a id="c4d.modules.bodypaint.PaintBitmap.GetColorMode"></a>

Get the color mode of the paint bitmap.

**Return type:** int

**Returns:**

The color mode:

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

#### `PaintBitmap.GetPaintTexture(self)` <a id="c4d.modules.bodypaint.PaintBitmap.GetPaintTexture"></a>

Get the paint texture if possible.

**Return type:** Optional[[c4d.modules.bodypaint.PaintTexture](PaintTexture/index.md#c4d.modules.bodypaint.PaintTexture)]

**Returns:** The paint texture if possible, otherwise **None**.

### Layer Structure <a id="c4d.modules.bodypaint.PaintBitmap-method-Layer-Structure"></a>

#### `PaintBitmap.GetAlphaFirst(self)` <a id="c4d.modules.bodypaint.PaintBitmap.GetAlphaFirst"></a>

Get the first alpha channel layer.

**Return type:** Optional[[c4d.modules.bodypaint.PaintLayer](PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)]

**Returns:** The first alpha channel layer, or **None** if there is none.

#### `PaintBitmap.GetAlphaLast(self)` <a id="c4d.modules.bodypaint.PaintBitmap.GetAlphaLast"></a>

Get the last alpha channel layer.

**Return type:** Optional[[c4d.modules.bodypaint.PaintLayer](PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)]

**Returns:** The last alpha channel layer, or **None** if there is none.

#### `PaintBitmap.GetLayerDownFirst(self)` <a id="c4d.modules.bodypaint.PaintBitmap.GetLayerDownFirst"></a>

Get the first alpha channel layer.

**Return type:** Optional[[c4d.modules.bodypaint.PaintLayer](PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)]

**Returns:** The first alpha channel layer, or **None** if there is none.

#### `PaintBitmap.GetLayerDownLast(self)` <a id="c4d.modules.bodypaint.PaintBitmap.GetLayerDownLast"></a>

Get the last child layer.

**Return type:** Optional[[c4d.modules.bodypaint.PaintLayer](PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)]

**Returns:** The last child layer, or **None** if there is none.

#### `PaintBitmap.GetParent(self)` <a id="c4d.modules.bodypaint.PaintBitmap.GetParent"></a>

Get the parent.

> **Note:** This can be a layer or a texture for instance.

**Return type:** Optional[[c4d.modules.bodypaint.PaintBitmap](#c4d.modules.bodypaint.PaintBitmap)]

**Returns:** The paint texture if possible, otherwise **None**.

### Refresh And Change Tracking <a id="c4d.modules.bodypaint.PaintBitmap-method-Refresh-And-Change-Tracking"></a>

#### `PaintBitmap.GetDirty(self, flags)` <a id="c4d.modules.bodypaint.PaintBitmap.GetDirty"></a>

Get dirty count.

**Parameters:** **flags** (*int*) – Reserved, must be 0.

**Return type:** int

**Returns:** Dirty count, incremented when the paint bitmap changes.

#### `PaintBitmap.UpdateRefresh(self, xmin, ymin, xmax, ymax, flags)` <a id="c4d.modules.bodypaint.PaintBitmap.UpdateRefresh"></a>

Refresh an area of the paint bitmap.

> **Note:** Must be done after modifying the paint bitmap.

**Parameters:**

- **xmin** (*int*) – Left coordinate of the refreshed area.

- **ymin** (*int*) – Top coordinate of the refreshed area.

- **xmax** (*int*) – Right coordinate of the refreshed area.

- **ymax** (*int*) – Bottom coordinate of the refreshed area.

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *UPDATE_CHILDREN* | Private. |
  | *UPDATE_PARENTS* | Private. |
  | *UPDATE_PREVIEW* | Private. |
  | *UPDATE_REFRESH2D* | Private. |
  | *UPDATE_RECALC* | Private. |
  | *UPDATE_NOSAVECHG* | Private. |
  | *UPDATE_NOOFFSET* | Private. |
  | *UPDATE_REFRESH3D* | Private. |
  | *UPDATE_REFRESHCURSOR* | Private. |
  | *UPDATE_NOSTOPTHREADS* | Private. |
  | *UPDATE_STD* | Standard refresh. |

#### `PaintBitmap.UpdateRefreshAll(self, flags, reallyall)` <a id="c4d.modules.bodypaint.PaintBitmap.UpdateRefreshAll"></a>

Refresh the complete paint bitmap. Has to be done after modifying the paint bitmap.

**Parameters:**

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *UPDATE_CHILDREN* | Private. |
  | *UPDATE_PARENTS* | Private. |
  | *UPDATE_PREVIEW* | Private. |
  | *UPDATE_REFRESH2D* | Private. |
  | *UPDATE_RECALC* | Private. |
  | *UPDATE_NOSAVECHG* | Private. |
  | *UPDATE_NOOFFSET* | Private. |
  | *UPDATE_REFRESH3D* | Private. |
  | *UPDATE_REFRESHCURSOR* | Private. |
  | *UPDATE_NOSTOPTHREADS* | Private. |
  | *UPDATE_STD* | Standard refresh. |

- **reallyall** (*bool*) –

  If **True** an infinite bounding box is used for the refresh.  
  If **False** the bounding box of the layer is used, this is much faster.
