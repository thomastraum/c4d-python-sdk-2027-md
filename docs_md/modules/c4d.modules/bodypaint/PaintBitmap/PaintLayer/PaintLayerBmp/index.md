<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/bodypaint/PaintBitmap/PaintLayer/PaintLayerBmp/index.html -->

# c4d.modules.bodypaint.PaintLayerBmp <a id="c4d-modules-bodypaint-paintlayerbmp"></a>

## *class* `c4d.modules.bodypaint.PaintLayerBmp` <a id="c4d.modules.bodypaint.PaintLayerBmp"></a>

The abstract base class of all paint classes.  
Can be a texture, material, layer or mask.

Parent Class:

- [`c4d.modules.bodypaint.PaintLayer`](../index.md#c4d.modules.bodypaint.PaintLayer)

## Overview <a id="overview"></a>

**Bitmap Access**

- [`PaintLayerBmp.GetBoundingBox()`](#c4d.modules.bodypaint.PaintLayerBmp.GetBoundingBox): Get the bounding box of the bitmap layer.
- [`PaintLayerBmp.GetPixelCnt()`](#c4d.modules.bodypaint.PaintLayerBmp.GetPixelCnt): Reads *cnt* pixels from (*x*, *y*) in the bitmap to the *buffer* with mode *dstmode*.
- [`PaintLayerBmp.SetPixelCnt()`](#c4d.modules.bodypaint.PaintLayerBmp.SetPixelCnt): Sets *cnt* pixels at (*x*, *y*) in the bitmap from *buffer* with mode *srcmode*, incrementing *inc* bytes for each pixel.

**Bitmap Import**

- [`PaintLayerBmp.ImportFromBaseBitmap()`](#c4d.modules.bodypaint.PaintLayerBmp.ImportFromBaseBitmap): Fill the layer bitmap with an imported bitmap.
- [`PaintLayerBmp.ImportFromBaseBitmapAlpha()`](#c4d.modules.bodypaint.PaintLayerBmp.ImportFromBaseBitmapAlpha): Fill the layer bitmap with an imported bitmap.

## Members <a id="members"></a>

### Bitmap Access <a id="c4d.modules.bodypaint.PaintLayerBmp-method-Bitmap-Access"></a>

#### `PaintLayerBmp.GetBoundingBox(self)` <a id="c4d.modules.bodypaint.PaintLayerBmp.GetBoundingBox"></a>

Get the bounding box of the bitmap layer.

```python
d = layer_bmp.GetBoundingBox()
d["x1"], d["y1"], d["y1"], d["y2"]
```

**Return type:** dict

**Returns:** The coordinates.

#### `PaintLayerBmp.GetPixelCnt(self, x, y, cnt, buffer, dstmode, flags)` <a id="c4d.modules.bodypaint.PaintLayerBmp.GetPixelCnt"></a>

Reads *cnt* pixels from (*x*, *y*) in the bitmap to the *buffer* with mode *dstmode*.

*New in version R16.021.*

**Parameters:**

- **x** (*int*) – The starting X coordinate.

- **y** (*int*) – The starting Y coordinate.

- **cnt** (*int*) – The number of pixels to get.

- **buffer** (*Union*[*bytearray*, *memoryview*]) – The destination buffer.

- **dstmode** (*int*) –

  The destination color mode:

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

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *PIXELCNT_NONE* | None. |
  | *PIXELCNT_DITHERING* | Allow dithering. |
  | *PIXELCNT_B3DLAYERS* | Merge BodyPaint 3D layers ([`MultipassBitmap`](../../../../../c4d.bitmaps/BaseBitmap/MultipassBitmap/index.md#c4d.bitmaps.MultipassBitmap)). |
  | *PIXELCNT_APPLYALPHA* | Apply alpha layers to the result ([`PaintLayerBmp`](#c4d.modules.bodypaint.PaintLayerBmp)). |
  | *PIXELCNT_INTERNAL_SETLINE* | Internal SetLine indicator. Private. |
  | *PIXELCNT_INTERNAL_ALPHAVALUE* | Get also the alpha value (RGBA *32*-bit). Private. |

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `PaintLayerBmp.SetPixelCnt(self, x, y, cnt, buffer, inc, srcmode, flags)` <a id="c4d.modules.bodypaint.PaintLayerBmp.SetPixelCnt"></a>

Sets *cnt* pixels at (*x*, *y*) in the bitmap from *buffer* with mode *srcmode*, incrementing *inc* bytes for each pixel.

*New in version R16.021.*

**Parameters:**

- **x** (*int*) – X coordinate of the first pixel to set.

- **y** (*int*) – Y coordinate of the first pixel to set.

- **cnt** (*int*) – Number of pixels to set.

- **buffer** (*Union*[*bytearray*, *memoryview*]) – The source buffer.

- **inc** (*int*) – The byte increment per pixel in the buffer.

- **srcmode** (*int*) –

  The source mode.

  > **Note:** None of the alpha modes are supported.

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

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *PIXELCNT_NONE* | None. |
  | *PIXELCNT_DITHERING* | Allow dithering. |
  | *PIXELCNT_B3DLAYERS* | Merge BodyPaint 3D layers ([`MultipassBitmap`](../../../../../c4d.bitmaps/BaseBitmap/MultipassBitmap/index.md#c4d.bitmaps.MultipassBitmap)). |
  | *PIXELCNT_APPLYALPHA* | Apply alpha layers to the result ([`PaintLayerBmp`](#c4d.modules.bodypaint.PaintLayerBmp)). |
  | *PIXELCNT_INTERNAL_SETLINE* | Internal SetLine indicator. Private. |
  | *PIXELCNT_INTERNAL_ALPHAVALUE* | Get also the alpha value (RGBA *32*-bit). Private. |

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Bitmap Import <a id="c4d.modules.bodypaint.PaintLayerBmp-method-Bitmap-Import"></a>

#### `PaintLayerBmp.ImportFromBaseBitmap(self, bmp, usealpha)` <a id="c4d.modules.bodypaint.PaintLayerBmp.ImportFromBaseBitmap"></a>

Fill the layer bitmap with an imported bitmap.

**Parameters:**

- **bm** ([*c4d.bitmaps.BaseBitmap*](../../../../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The bitmap to import.
- **usealpha** (*bool*) – If **True** the alpha channel of the bitmap is used, otherwise **False**.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `PaintLayerBmp.ImportFromBaseBitmapAlpha(self, bmp, channel)` <a id="c4d.modules.bodypaint.PaintLayerBmp.ImportFromBaseBitmapAlpha"></a>

Fill the layer bitmap with an imported bitmap.

**Parameters:**

- **bm** ([*c4d.bitmaps.BaseBitmap*](../../../../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The bitmap to import.
- **channel** ([*c4d.bitmaps.BaseBitmap*](../../../../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The separate alpha channel bitmap to import.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.
