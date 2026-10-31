<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.bitmaps/ColorProfileConvert/index.html -->

# c4d.bitmaps.ColorProfileConvert <a id="c4d-bitmaps-colorprofileconvert"></a>

## *class* `c4d.bitmaps.ColorProfileConvert` <a id="c4d.bitmaps.ColorProfileConvert"></a>

A helper class to convert the [`ColorProfile`](../ColorProfile/index.md#c4d.bitmaps.ColorProfile) of [`bitmaps`](../BaseBitmap/index.md#c4d.bitmaps.BaseBitmap).  
See also `BaseBitmap.GetPixelCnt()`.

*New in version R17.032.*

## Overview <a id="overview"></a>

**Color Conversion**

- [`ColorProfileConvert.Convert()`](#c4d.bitmaps.ColorProfileConvert.Convert): Converts the color profiles of the pixel data.
- [`ColorProfileConvert.PrepareTransform()`](#c4d.bitmaps.ColorProfileConvert.PrepareTransform): Prepares the color conversion i.e.

**Magic Methods**

- [`ColorProfileConvert.__init__()`](#c4d.bitmaps.ColorProfileConvert.__init__)

## Members <a id="members"></a>

### Color Conversion <a id="c4d.bitmaps.ColorProfileConvert-method-Color-Conversion"></a>

#### `ColorProfileConvert.Convert(self, src, dst, cnt, skipInputComponents, skipOutputComponents)` <a id="c4d.bitmaps.ColorProfileConvert.Convert"></a>

Converts the color profiles of the pixel data.

**Parameters:**

- **src** (*bytes*) – The source pixel buffer.

- **dst** (*bytes*) – The destination pixel buffer.

- **cnt** (*int*) – The number of pixels to convert.

- **skipInputComponents** (*int*) –

  The number of bytes to skip in the source buffer after each converted pixel. For instance a RGB pixel contains 3 bytes.  
  After conversion the number of *skipInputComponents* bytes is added to the source pointer.

- **skipOutputComponents** (*int*) –

  The number of bytes to skip in the destination buffer after each converted pixel. For instance a RGB pixel contains 3 bytes.  
  After conversion the number of SkipOutputComponents bytes is added to the destination pointer.

#### `ColorProfileConvert.PrepareTransform(self, srccolormode, srcprofile, dstcolormode, dstprofile, bgr)` <a id="c4d.bitmaps.ColorProfileConvert.PrepareTransform"></a>

Prepares the color conversion i.e. checks if a conversion is needed.  
A conversion is only necessary if **True** is returned. Two identical color spaces will return **False**.

**Parameters:**

- **srccolormode** (*int*) –

  The source color mode:

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

- **srcprofile** ([*c4d.bitmaps.ColorProfile*](../ColorProfile/index.md#c4d.bitmaps.ColorProfile)) – The source color profile.

- **dstcolormode** ([*c4d.bitmaps.ColorProfile*](../ColorProfile/index.md#c4d.bitmaps.ColorProfile)) –

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

- **dstprofile** ([*c4d.bitmaps.ColorProfile*](../ColorProfile/index.md#c4d.bitmaps.ColorProfile)) – The destination color profile.

- **bgr** (*bool*) – **True** to swap the RGB channels. Only necessary when working directly with Windows bitmaps.

**Return type:** bool

**Returns:** **True** a conversion is necessary, otherwise **False**.

### Magic Methods <a id="c4d.bitmaps.ColorProfileConvert-method-Magic-Methods"></a>

#### `ColorProfileConvert.__init__(self)` <a id="c4d.bitmaps.ColorProfileConvert.__init__"></a>
