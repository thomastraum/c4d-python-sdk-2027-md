<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/bodypaint/PaintBitmap/PaintTexture/index.html -->

# c4d.modules.bodypaint.PaintTexture <a id="c4d-modules-bodypaint-painttexture"></a>

## *class* `c4d.modules.bodypaint.PaintTexture` <a id="c4d.modules.bodypaint.PaintTexture"></a>

A class for paint textures, can contain layers and may represent channel of a material.

Parent Class:

- [`c4d.modules.bodypaint.PaintBitmap`](../index.md#c4d.modules.bodypaint.PaintBitmap)

## Overview <a id="overview"></a>

**Selection**

- [`PaintTexture.GetSelectedTexture()`](#c4d.modules.bodypaint.PaintTexture.GetSelectedTexture): Gets the selected paint texture.
- [`PaintTexture.SetSelected_Texture()`](#c4d.modules.bodypaint.PaintTexture.SetSelected_Texture): Selects a paint texture.

**Texture Setup**

- [`PaintTexture.CreateNewTexture()`](#c4d.modules.bodypaint.PaintTexture.CreateNewTexture): Creates a new paint texture.
- [`PaintTexture.GetTextureDefaults()`](#c4d.modules.bodypaint.PaintTexture.GetTextureDefaults): Gets the default texture settings for the passed material *channel* ID.

**Asset Information**

- [`PaintTexture.GetAlphaCount()`](#c4d.modules.bodypaint.PaintTexture.GetAlphaCount): Get the number of alpha channels of the paint texture.
- [`PaintTexture.GetFilename()`](#c4d.modules.bodypaint.PaintTexture.GetFilename): Get the filename of the paint texture.

**Color Configuration**

- [`PaintTexture.GetColorProfile()`](#c4d.modules.bodypaint.PaintTexture.GetColorProfile): Gets the color profile for the paint texture.
- [`PaintTexture.SetColorMode()`](#c4d.modules.bodypaint.PaintTexture.SetColorMode): Change the color mode of the paint texture.
- [`PaintTexture.SetColorProfile()`](#c4d.modules.bodypaint.PaintTexture.SetColorProfile): Sets the color profile for the paint texture.

**Layer Creation**

- [`PaintTexture.AddLayerBmp()`](#c4d.modules.bodypaint.PaintTexture.AddLayerBmp): Add a bitmap layer.
- [`PaintTexture.AddLayerFolder()`](#c4d.modules.bodypaint.PaintTexture.AddLayerFolder): Add a layer folder.

**Layer Navigation**

- [`PaintTexture.GetActive()`](#c4d.modules.bodypaint.PaintTexture.GetActive): Get the selected layer, or **None** if there is none.
- [`PaintTexture.GetFirstLayer()`](#c4d.modules.bodypaint.PaintTexture.GetFirstLayer): Get the first layer of the paint texture.
- [`PaintTexture.GetLastLayer()`](#c4d.modules.bodypaint.PaintTexture.GetLastLayer): Get the last layer of the paint texture.
- [`PaintTexture.GetLayerCount()`](#c4d.modules.bodypaint.PaintTexture.GetLayerCount): Get the number of layers of the paint texture.
- [`PaintTexture.GetLinkLayers()`](#c4d.modules.bodypaint.PaintTexture.GetLinkLayers): Get linked layers.

**Selection**

- [`PaintTexture.SetActiveLayer()`](#c4d.modules.bodypaint.PaintTexture.SetActiveLayer): Select a layer.

## Members <a id="members"></a>

### Selection <a id="c4d.modules.bodypaint.PaintTexture-staticmethod-Selection"></a>

#### *static* `PaintTexture.GetSelectedTexture()` <a id="c4d.modules.bodypaint.PaintTexture.GetSelectedTexture"></a>

Gets the selected paint texture.

**Return type:** Optional[[c4d.modules.bodypaint.PaintTexture](#c4d.modules.bodypaint.PaintTexture)]

**Returns:** The selected paint texture or **None** if no paint is selected.

#### *static* `PaintTexture.SetSelected_Texture(bmp, preferred)` <a id="c4d.modules.bodypaint.PaintTexture.SetSelected_Texture"></a>

Selects a paint texture.

**Parameters:**

- **bmp** ([*c4d.modules.bodypaint.PaintBitmap*](../index.md#c4d.modules.bodypaint.PaintBitmap)) – The paint texture to select.
- **preferred** (*Optional*[[*c4d.modules.bodypaint.PaintMaterial*](../PaintMaterial/index.md#c4d.modules.bodypaint.PaintMaterial)]) – The prefered paint material, usually **None**.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Texture Setup <a id="c4d.modules.bodypaint.PaintTexture-staticmethod-Texture-Setup"></a>

#### *static* `PaintTexture.CreateNewTexture(path, settings)` <a id="c4d.modules.bodypaint.PaintTexture.CreateNewTexture"></a>

Creates a new paint texture.

**Parameters:**

- **path** (*str*) – The filename for the paint texture.

- **settings** ([*c4d.BaseContainer*](../../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) –

  The settings for the texture creation:

  | Key | Value Type | Description |
  |---|---|---|
  | *TEXTURE_FILEFORMAT* | int | *FILTER_TIF*: TIFF.<br>*FILTER_TGA*: TGA.<br>*FILTER_BMP*: BMP.<br>*FILTER_IFF*: IFF.<br>*FILTER_JPG*: JPEG.<br>*FILTER_PICT*: PICT.<br>*FILTER_PSD*: PSD.<br>*FILTER_RLA*: RLA.<br>*FILTER_RPF*: RPF.<br>*FILTER_B3D*: *BodyPaint 3D*.<br>*FILTER_TIF_B3D*: TIFF *BodyPaint 3D*.<br>*FILTER_PSB*: PSB.<br>*FILTER_AVI*: AVI Movie.<br>*FILTER_MOVIE*: Quicktime Movie.<br>*FILTER_QTVRSAVER_PANORAMA*: QTVR Panorama.<br>*FILTER_QTVRSAVER_OBJECT*: QTVR Object.<br>*FILTER_HDR*: HDR.<br>*FILTER_EXR_LOAD*: EXR (Load).<br>*FILTER_EXR*: EXR.<br>*FILTER_PNG*: PNG.<br>*FILTER_IES*: IES.<br>*FILTER_B3DNET*: *BodyPaint 3D* NET. Private.<br>*FILTER_DPX*: DPX.<br>*FILTER_DDS*: *New in version R19:* DDS. |
  | *TEXTURE_WIDTH* | int | Texture width. |
  | *TEXTURE_HEIGHT* | int | Texture height. |
  | *TEXTURE_MODE* | int | Texture mode (only non-alpha channel modes): [COLORMODE](../../../../../consts/COLORMODE.md). |
  | *TEXTURE_COLOR* | [`Vector`](../../../../c4d/Vector/index.md#c4d.Vector) | Texture color. |
  | *TEXTURE_SAVE_IMMEDIATLY* | bool | Flag to save immediately, otherwise texture is only created in memory. |

**Return type:** Optional[[c4d.modules.bodypaint.PaintTexture](#c4d.modules.bodypaint.PaintTexture)]

**Returns:** The created paint texture if successful, otherwise **None**.

#### *static* `PaintTexture.GetTextureDefaults(channel)` <a id="c4d.modules.bodypaint.PaintTexture.GetTextureDefaults"></a>

Gets the default texture settings for the passed material *channel* ID.

**Parameters:**

**path** (*int*) –

The material channel ID:

|   |   |
|---|---|
| *CHANNEL_COLOR* | The color channel of a material. |
| *CHANNEL_LUMINANCE* | The luminance channel of a material. |
| *CHANNEL_TRANSPARENCY* | The transparency channel of a material. |
| *CHANNEL_REFLECTION* | The reflection channel of a material. |
| *CHANNEL_ENVIRONMENT* | The environment channel of a material. |
| *CHANNEL_FOG* | The fog channel of a material. |
| *CHANNEL_BUMP* | The bump channel of a material. |
| *CHANNEL_ALPHA* | The alpha channel of a material. |
| *CHANNEL_SPECULAR* | The specular channel of a material. |
| *CHANNEL_SPECULARCOLOR* | The specular color channel of a material. |
| *CHANNEL_GLOW* | The glow channel of a material. |
| *CHANNEL_DISPLACEMENT* | The displacement channel of a material. |
| *CHANNEL_DIFFUSION* | The diffusion channel of a material. |
| *CHANNEL_NORMAL* | The normal channel of a material. |
| *CHANNEL_ANY* | An unlabeled plugin channel. |

**Return type:** [c4d.BaseContainer](../../../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:**

The default texture settings:

| Key | Value Type | Description |
|---|---|---|
| *TEXTURE_FILEFORMAT* | int | *FILTER_TIF*: TIFF.<br>*FILTER_TGA*: TGA.<br>*FILTER_BMP*: BMP.<br>*FILTER_IFF*: IFF.<br>*FILTER_JPG*: JPEG.<br>*FILTER_PICT*: PICT.<br>*FILTER_PSD*: PSD.<br>*FILTER_RLA*: RLA.<br>*FILTER_RPF*: RPF.<br>*FILTER_B3D*: *BodyPaint 3D*.<br>*FILTER_TIF_B3D*: TIFF *BodyPaint 3D*.<br>*FILTER_PSB*: PSB.<br>*FILTER_AVI*: AVI Movie.<br>*FILTER_MOVIE*: Quicktime Movie.<br>*FILTER_QTVRSAVER_PANORAMA*: QTVR Panorama.<br>*FILTER_QTVRSAVER_OBJECT*: QTVR Object.<br>*FILTER_HDR*: HDR.<br>*FILTER_EXR_LOAD*: EXR (Load).<br>*FILTER_EXR*: EXR.<br>*FILTER_PNG*: PNG.<br>*FILTER_IES*: IES.<br>*FILTER_B3DNET*: *BodyPaint 3D* NET. Private.<br>*FILTER_DPX*: DPX.<br>*FILTER_DDS*: *New in version R19:* DDS. |
| *TEXTURE_WIDTH* | int | Texture width. |
| *TEXTURE_HEIGHT* | int | Texture height. |
| *TEXTURE_MODE* | int | Texture mode (only non-alpha channel modes): [COLORMODE](../../../../../consts/COLORMODE.md). |
| *TEXTURE_COLOR* | [`Vector`](../../../../c4d/Vector/index.md#c4d.Vector) | Texture color. |
| *TEXTURE_SAVE_IMMEDIATLY* | bool | Flag to save immediately, otherwise texture is only created in memory. |

### Asset Information <a id="c4d.modules.bodypaint.PaintTexture-method-Asset-Information"></a>

#### `PaintTexture.GetAlphaCount(self)` <a id="c4d.modules.bodypaint.PaintTexture.GetAlphaCount"></a>

Get the number of alpha channels of the paint texture.

**Return type:** int

**Returns:** The number of alpha channels.

#### `PaintTexture.GetFilename(self)` <a id="c4d.modules.bodypaint.PaintTexture.GetFilename"></a>

Get the filename of the paint texture.

**Return type:** str

**Returns:** The filename of the paint texture.

### Color Configuration <a id="c4d.modules.bodypaint.PaintTexture-method-Color-Configuration"></a>

#### `PaintTexture.GetColorProfile(self, index=0)` <a id="c4d.modules.bodypaint.PaintTexture.GetColorProfile"></a>

Gets the color profile for the paint texture.

*New in version R17.048.*

**Parameters:**

**index** (*int*) –

Index of the colorprofile to retrieve.

*New in version 2025.2.0.*

| Symbol ID | Description |
|---|---|
| COLORPROFILE_INDEX_IMAGE | Index of the image color profile. |
| COLORPROFILE_INDEX_RENDERSPACE | Index of the renderspace color profile. |
| COLORPROFILE_INDEX_VIEW_TRANSFORM | Index of the view transform. |
| COLORPROFILE_INDEX_DISPLAYSPACE | Index of the displayspace color profile. |

**Return type:** [c4d.bitmaps.ColorProfile](../../../../c4d.bitmaps/ColorProfile/index.md#c4d.bitmaps.ColorProfile)

**Returns:** The color profile.

#### `PaintTexture.SetColorMode(self, newcolormode, doundo)` <a id="c4d.modules.bodypaint.PaintTexture.SetColorMode"></a>

Change the color mode of the paint texture.

**Parameters:**

- **newcolormode** (*int*) –

  The new color mode:

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

- **doundo** (*bool*) – **True** to create an undo for changing the color mode, otherwise **False**.

#### `PaintTexture.SetColorProfile(self, profile, index=0)` <a id="c4d.modules.bodypaint.PaintTexture.SetColorProfile"></a>

Sets the color profile for the paint texture.

*New in version R17.048.*

**Parameters:**

- **index** (*int*) –

  Index of the colorprofile to set.

  *New in version 2025.2.0.*

  | Symbol ID | Description |
  |---|---|
  | COLORPROFILE_INDEX_IMAGE | Index of the image color profile. |
  | COLORPROFILE_INDEX_RENDERSPACE | Index of the renderspace color profile. |
  | COLORPROFILE_INDEX_VIEW_TRANSFORM | Index of the view transform. |
  | COLORPROFILE_INDEX_DISPLAYSPACE | Index of the displayspace color profile. |

- **profile** ([*c4d.bitmaps.ColorProfile*](../../../../c4d.bitmaps/ColorProfile/index.md#c4d.bitmaps.ColorProfile)) – The color profile to set.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Layer Creation <a id="c4d.modules.bodypaint.PaintTexture-method-Layer-Creation"></a>

#### `PaintTexture.AddLayerBmp(self, insertafter=None, layerset=None, mode=5, useundo=True, activate=True)` <a id="c4d.modules.bodypaint.PaintTexture.AddLayerBmp"></a>

Add a bitmap layer.

**Parameters:**

- **insertafter** (*Optional*[[*c4d.modules.bodypaint.PaintLayer*](../PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)]) – The layer insertion point.

- **layerset** (*Optional*[[*c4d.modules.bodypaint.PaintLayer*](../PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)]) – The parent layer folder.

- **mode** (*int*) –

  Mode (should be the same as the paint texture):

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

- **useundo** (*bool*) – **True** to create an undo on the undo stack, otherwise **False**.

- **activate** (*bool*) – **True** to select the layer.

**Return type:** [c4d.modules.bodypaint.PaintLayerBmp](../PaintLayer/PaintLayerBmp/index.md#c4d.modules.bodypaint.PaintLayerBmp)

**Returns:** The added bitmap layer.

#### `PaintTexture.AddLayerFolder(self, insertafter=None, insertunder=None, useundo=True, activate=True)` <a id="c4d.modules.bodypaint.PaintTexture.AddLayerFolder"></a>

Add a layer folder.

**Parameters:**

- **insertafter** (*Optional*[[*c4d.modules.bodypaint.PaintLayer*](../PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)]) – The layer insertion point.
- **insertunder** (*Optional*[[*c4d.modules.bodypaint.PaintLayer*](../PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)]) – Parent layer folder.
- **useundo** (*bool*) – **True** to create an undo on the undo stack, otherwise **False**.
- **activate** (*bool*) – **True** to select the layer.

**Return type:** [c4d.modules.bodypaint.PaintLayerBmp](../PaintLayer/PaintLayerBmp/index.md#c4d.modules.bodypaint.PaintLayerBmp)

**Returns:** The added layer folder.

### Layer Navigation <a id="c4d.modules.bodypaint.PaintTexture-method-Layer-Navigation"></a>

#### `PaintTexture.GetActive(self)` <a id="c4d.modules.bodypaint.PaintTexture.GetActive"></a>

Get the selected layer, or **None** if there is none.

**Return type:** Optional[[c4d.modules.bodypaint.PaintLayer](../PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)]

**Returns:** The selected layer.

#### `PaintTexture.GetFirstLayer(self)` <a id="c4d.modules.bodypaint.PaintTexture.GetFirstLayer"></a>

Get the first layer of the paint texture.

**Return type:** Optional[[c4d.modules.bodypaint.PaintLayer](../PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)]

**Returns:** The first layer of the paint texture, or **None** if there is none.

#### `PaintTexture.GetLastLayer(self)` <a id="c4d.modules.bodypaint.PaintTexture.GetLastLayer"></a>

Get the last layer of the paint texture.

**Return type:** Optional[[c4d.modules.bodypaint.PaintLayer](../PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)]

**Returns:** The last layer of the paint texture, or **None** if there is none.

#### `PaintTexture.GetLayerCount(self)` <a id="c4d.modules.bodypaint.PaintTexture.GetLayerCount"></a>

Get the number of layers of the paint texture.

**Return type:** int

**Returns:** The number of layers.

#### `PaintTexture.GetLinkLayers(self, addfolders)` <a id="c4d.modules.bodypaint.PaintTexture.GetLinkLayers"></a>

Get linked layers.

**Parameters:** **addfolders** (*bool*) – If **True** the layer hierarchy is taken into account (see layer folders), otherwise **False**.

**Return type:** List[[c4d.modules.bodypaint.PaintLayer](../PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)]

**Returns:** The list containing the linked layers.

### Selection <a id="c4d.modules.bodypaint.PaintTexture-method-Selection"></a>

#### `PaintTexture.SetActiveLayer(self, layer, activatetexture, show=True)` <a id="c4d.modules.bodypaint.PaintTexture.SetActiveLayer"></a>

Select a layer.

**Parameters:**

- **layer** ([*c4d.modules.bodypaint.PaintLayer*](../PaintLayer/index.md#c4d.modules.bodypaint.PaintLayer)) – The layer to select.
- **activatetexture** (*bool*) – Select the texture.
- **show** (*True*) – Show the texture.
