<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseData/BitmapSaverData/index.html -->

# c4d.plugins.BitmapSaverData <a id="c4d-plugins-bitmapsaverdata"></a>

## *class* `c4d.plugins.BitmapSaverData` <a id="c4d.plugins.BitmapSaverData"></a>

A data class for creating bitmap savers.  
Use [`RegisterBitmapSaverPlugin()`](../../index.md#c4d.plugins.RegisterBitmapSaverPlugin) to register the plugin.

Parent Class:

- [`c4d.plugins.BaseData`](../index.md#c4d.plugins.BaseData)

## Overview <a id="overview"></a>

**Configuration And Output**

- [`BitmapSaverData.Edit()`](#c4d.plugins.BitmapSaverData.Edit): Override - Open the settings dialog for this import/export filter.
- [`BitmapSaverData.Save()`](#c4d.plugins.BitmapSaverData.Save): Override - Save the bitmap to a file.

**Format Capabilities**

- [`BitmapSaverData.GetMaxAlphas()`](#c4d.plugins.BitmapSaverData.GetMaxAlphas): Get the maximum number of alpha channels this format supports with the current settings.
- [`BitmapSaverData.GetMaxResolution()`](#c4d.plugins.BitmapSaverData.GetMaxResolution): Overload this to return the maximum resolution of the image format.

## Members <a id="members"></a>

### Configuration And Output <a id="c4d.plugins.BitmapSaverData-method-Configuration-And-Output"></a>

#### `BitmapSaverData.Edit(self, data)` <a id="c4d.plugins.BitmapSaverData.Edit"></a>

Override - Open the settings dialog for this import/export filter.

**Parameters:** **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The settings for your plugin.

**Return type:** bool

**Returns:** **True** if the dialog opened successfully.

#### `BitmapSaverData.Save(self, fn, bmp, data, savebits)` <a id="c4d.plugins.BitmapSaverData.Save"></a>

Override - Save the bitmap to a file.

> **Warning:** **Never** call any GUI commands in this method. Use the return value to inform the user about the state of the rendering.

**Parameters:**

- **fn** (*str*) – The filename of the file to save.

- **bmp** ([*c4d.bitmaps.BaseBitmap*](../../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The bitmap to save the image from.

- **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The settings for your plugin. These settings are stored with the general preferences.

- **savebits** (*int*) –

  Flags for the save:

  | Symbol ID | Description |
  |---|---|
  | SAVEBIT_NONE | None. |
  | SAVEBIT_ALPHA | Save the alpha channel(s) in the file. (For filter plugins, do not save an alpha channel if this is not set.) |
  | SAVEBIT_MULTILAYER | Save multiple layers. |
  | SAVEBIT_USESELECTEDLAYERS | Use selected layers. |
  | SAVEBIT_USE16BITCHANNELS | Use *16*-bit channels. |
  | SAVEBIT_GREYSCALE | Save in grayscale mode. |
  | SAVEBIT_INTERNALNET | Private. |
  | SAVEBIT_DONTMERGE | Avoid merging of layers in BodyPaint 3D files. |
  | SAVEBIT_USE32BITCHANNELS | Use *32*-bit channels. |
  | SAVEBIT_SAVERENDERRESULT | Private. |
  | SAVEBIT_FIRSTALPHA_ONLY | Private. |
  | SAVEBIT_KEEP_COLOR_MODE | Private. |

**Return type:** int

**Returns:**

The return values:

|   |   |
|---|---|
| *IMAGERESULT_OK* | Image loaded/created. |
| *IMAGERESULT_NOTEXISTING* | Image does not exist. |
| *IMAGERESULT_WRONGTYPE* | Image has the wrong type. |
| *IMAGERESULT_OUTOFMEMORY* | Not enough memory. |
| *IMAGERESULT_FILEERROR* | File error. |
| *IMAGERESULT_FILESTRUCTURE* | Invalid file structure. |
| *IMAGERESULT_MISC_ERROR* | Unknown error. |
| *IMAGERESULT_PARAM_ERROR* | Parameter error. |
| *IMAGERESULT_THREADCANCELED* | Thread canceled while working. |

### Format Capabilities <a id="c4d.plugins.BitmapSaverData-method-Format-Capabilities"></a>

#### `BitmapSaverData.GetMaxAlphas(self, data)` <a id="c4d.plugins.BitmapSaverData.GetMaxAlphas"></a>

Get the maximum number of alpha channels this format supports with the current settings.

**Parameters:** **data** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The settings for your plugin. These settings are stored with the general preferences.

**Return type:** int

**Returns:** The number of alpha channels.

#### `BitmapSaverData.GetMaxResolution(self, layers)` <a id="c4d.plugins.BitmapSaverData.GetMaxResolution"></a>

Overload this to return the maximum resolution of the image format.

**Parameters:** **layers** (*bool*) – **True** if layers are to be saved, otherwise **False**.

**Return type:** int

**Returns:** The maximum resolution supported by the image format.
