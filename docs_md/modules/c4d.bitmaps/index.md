<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.bitmaps/index.html -->

# c4d.bitmaps <a id="c4d-bitmaps"></a>

## *class* `c4d.bitmaps` <a id="c4d.bitmaps"></a>

- [`c4d.bitmaps.BaseBitmap`](BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)

  - [`c4d.bitmaps.MultipassBitmap`](BaseBitmap/MultipassBitmap/index.md#c4d.bitmaps.MultipassBitmap)

- [`c4d.bitmaps.ColorProfile`](ColorProfile/index.md#c4d.bitmaps.ColorProfile)

- [`c4d.bitmaps.ColorProfileConvert`](ColorProfileConvert/index.md#c4d.bitmaps.ColorProfileConvert)

- [`c4d.bitmaps.GeClipMap`](GeClipMap/index.md#c4d.bitmaps.GeClipMap)

- [`c4d.bitmaps.MovieLoader`](MovieLoader/index.md#c4d.bitmaps.MovieLoader)

- [`c4d.bitmaps.MovieSaver`](MovieSaver/index.md#c4d.bitmaps.MovieSaver)

## Overview <a id="overview"></a>

**Display And Rendering**

- [`c4d.bitmaps.AllocateRenderBitmap()`](#c4d.bitmaps.AllocateRenderBitmap): Allocates a bitmap for rendering a document according to the passed render data container.
- [`c4d.bitmaps.ShowBitmap()`](#c4d.bitmaps.ShowBitmap): Shows a bitmap in the picture viewer.

**Resource And Configuration**

- [`c4d.bitmaps.GetImageSettingsDictionary()`](#c4d.bitmaps.GetImageSettingsDictionary): Extracts the image format settings from *data*.
- [`c4d.bitmaps.InitResourceBitmap()`](#c4d.bitmaps.InitResourceBitmap): Loads the global icon with ID *resource_id*.
- [`c4d.bitmaps.SetImageSettingsDictionary()`](#c4d.bitmaps.SetImageSettingsDictionary): Replaces the image format settings in *data*.

## Members <a id="members"></a>

### Display And Rendering <a id="c4d.bitmaps-function-Display-And-Rendering"></a>

#### `c4d.bitmaps.AllocateRenderBitmap(renderData)` <a id="c4d.bitmaps.AllocateRenderBitmap"></a>

Allocates a bitmap for rendering a document according to the passed render data container.

*New in version 2026.2.0.*

**Parameters:** **renderData** ([*c4d.BaseContainer*](../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The render settings to use for allocating the bitmap.

**Return type:** Optional[[c4d.bitmaps.MultipassBitmap](BaseBitmap/MultipassBitmap/index.md#c4d.bitmaps.MultipassBitmap)]

**Returns:** The allocated bitmap or **None**.

#### `c4d.bitmaps.ShowBitmap(bmp, name=None)` <a id="c4d.bitmaps.ShowBitmap"></a>

Shows a bitmap in the picture viewer.

**Parameters:**

- **bmp** ([*c4d.bitmaps.BaseBitmap*](BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The bitmap. Will be copied.

- **name** (*Optional*[*str*]) –

  Optional name to be displayed in the Picture Viewer.

  *New in version 2025.2.0.*

### Resource And Configuration <a id="c4d.bitmaps-function-Resource-And-Configuration"></a>

#### `c4d.bitmaps.GetImageSettingsDictionary(data, filterId)` <a id="c4d.bitmaps.GetImageSettingsDictionary"></a>

Extracts the image format settings from *data*.

*New in version R20.*

**Parameters:**

- **data** ([*c4d.BaseContainer*](../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The container to extract.
- **filterId** (*int*) – The filter Id.

**Return type:** maxon.DataDictionary

**Returns:** The extracted image format settings.

#### `c4d.bitmaps.InitResourceBitmap(resource_id)` <a id="c4d.bitmaps.InitResourceBitmap"></a>

Loads the global icon with ID *resource_id*.  
Cinema 4D registers hundreds of its icons at program start and this way you can access them, for example *RESOURCEIMAGE_MOVE* is the move symbol. You can also resource your own icons via [`RegisterIcon()`](../c4d.gui/index.md#c4d.gui.RegisterIcon).

> **Note:** Also you can access the icons for commands.
>
> ```python
> import c4d
>
> icon = c4d.bitmaps.InitResourceBitmap(c4d.RESOURCEIMAGE_MOVE) # Returns the 'move' bitmap from the list below
> ```

**Parameters:** **resource_id** (*int*) – Resource ID to load.

**Return type:** Optional[[c4d.bitmaps.BaseBitmap](BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]

**Returns:** The loaded bitmap or **None**. Find a list of all icons ID in [Resource Index](../../indexes/resource_index.md).

#### `c4d.bitmaps.SetImageSettingsDictionary(settings, data, filterId)` <a id="c4d.bitmaps.SetImageSettingsDictionary"></a>

Replaces the image format settings in *data*.

*New in version R20.*

**Parameters:**

- **settings** (*maxon.DataDictionary*) – The image format settings to replace.
- **data** ([*c4d.BaseContainer*](../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The container to modify.
- **filterId** (*int*) – The filter Id.
