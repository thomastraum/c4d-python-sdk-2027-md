<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseData/BitmapLoaderData/index.html -->

# c4d.plugins.BitmapLoaderData <a id="c4d-plugins-bitmaploaderdata"></a>

## *class* `c4d.plugins.BitmapLoaderData` <a id="c4d.plugins.BitmapLoaderData"></a>

A data class for creating bitmap loaders.  
Use [`RegisterBitmapLoaderPlugin()`](../../index.md#c4d.plugins.RegisterBitmapLoaderPlugin) to register the plugin.

Parent Class:

- [`c4d.plugins.BaseData`](../index.md#c4d.plugins.BaseData)

## Overview <a id="overview"></a>

- [`BitmapLoaderData.GetInformation()`](#c4d.plugins.BitmapLoaderData.GetInformation): Implement this function if you want to support loading movies.
- [`BitmapLoaderData.GetSaver()`](#c4d.plugins.BitmapLoaderData.GetSaver): Return the ID of the corresponding bitmap saver, if there is one.
- [`BitmapLoaderData.Identify()`](#c4d.plugins.BitmapLoaderData.Identify): Override - Identify the file type as one that can be loaded using this plugin.
- [`BitmapLoaderData.Load()`](#c4d.plugins.BitmapLoaderData.Load): Override - Load the image file into the bitmap.

## Members <a id="members"></a>

### Bitmap File Handling <a id="c4d.plugins.BitmapLoaderData-method-Bitmap-File-Handling"></a>

#### `BitmapLoaderData.GetInformation(self, name)` <a id="c4d.plugins.BitmapLoaderData.GetInformation"></a>

Implement this function if you want to support loading movies.

**Parameters:** **name** (*str*) – The name of the file to check.

**Return type:** Tuple[int, int]

**Returns:** The *number of frames* and *fps* information for *name*.

#### `BitmapLoaderData.GetSaver(self)` <a id="c4d.plugins.BitmapLoaderData.GetSaver"></a>

Return the ID of the corresponding bitmap saver, if there is one.

**Return type:** Optional[int]

**Returns:** The plugin ID of the corresponding [`BitmapSaverData`](../BitmapSaverData/index.md#c4d.plugins.BitmapSaverData), or **None** if there is not one.

#### `BitmapLoaderData.Identify(self, name, probe, size)` <a id="c4d.plugins.BitmapLoaderData.Identify"></a>

Override - Identify the file type as one that can be loaded using this plugin. If possible, the file should not be identified through the suffix, but through the *probe* data.

**Parameters:**

- **name** (*str*) – The name of the file.
- **probe** (*memoryview*) – The start of a small chunk of data from the start of the file for testing this file type. Usually the *probe* size is 1024 bytes. The buffer is just accessible in this method.
- **size** (*int*) – The size of the chunk for testing this file type.

**Return type:** bool

**Returns:** **True** if your plugin recognises this file.

#### `BitmapLoaderData.Load(self, name, bm, frame)` <a id="c4d.plugins.BitmapLoaderData.Load"></a>

Override - Load the image file into the bitmap.

> **Warning:** **Never** call any GUI commands in this method. Use the return value to inform the user about the state of the rendering.

**Parameters:**

- **name** (*str*) – The filename of the file.
- **bm** ([*c4d.bitmaps.BaseBitmap*](../../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The bitmap. Please call `BaseBitmap.Init()` or `BaseBitmap.InitWith()` before, to initialize the size.
- **frame** (*int*) – The frame number for formats containing multiple images in a file such as Quicktime or AVI.

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
