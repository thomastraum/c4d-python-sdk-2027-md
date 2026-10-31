<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/IconData/index.html -->

# c4d.IconData <a id="c4d-icondata"></a>

## *class* `c4d.IconData` <a id="c4d.IconData"></a>

Represents a single icon in a large bitmap array.

*New in version R21.*

**Attributes**

## `c4d.IconData.bmp` <a id="c4d.IconData.bmp"></a>

The bitmap. Can be **None**.

**Type:** Optional[[`c4d.bitmaps.BaseBitmap`](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]

## `c4d.IconData.x` <a id="c4d.IconData.x"></a>

The X coordinate of the upper-left corner of the icon.

**Type:** int

## `c4d.IconData.y` <a id="c4d.IconData.y"></a>

The Y coordinate of the upper-left corner of the icon.

**Type:** int

## `c4d.IconData.w` <a id="c4d.IconData.w"></a>

The width of the icon.

**Type:** int

## `c4d.IconData.h` <a id="c4d.IconData.h"></a>

The height of the icon.

**Type:** int

## `c4d.IconData.flags` <a id="c4d.IconData.flags"></a>

The flags

**Type:**

|   |   |
|---|---|
| *ICONDATAFLAGS_NONE* | None. |
| *ICONDATAFLAGS_APPLYCOLORPROFILE* | Applies color profile. |
| *ICONDATAFLAGS_DISABLED* | Disabled icon. |

## Overview <a id="overview"></a>

**Bitmap Parts**

- [`IconData.GetClonePart()`](#c4d.IconData.GetClonePart): Gets a copy of the bitmap’s part for the icon data.
- [`IconData.GetGuiScalePart()`](#c4d.IconData.GetGuiScalePart): Gets a copy of the scaled bitmap’s part for the icon data with the size `IconData.GetGuiW()`/`IconData.GetGuiH()`.

**Display Dimensions**

- [`IconData.GetGuiH()`](#c4d.IconData.GetGuiH): Gets the GUI scaled height of the icon data.
- [`IconData.GetGuiW()`](#c4d.IconData.GetGuiW): Gets the GUI scaled width of the icon data.

**Magic Methods**

- [`IconData.__init__()`](#c4d.IconData.__init__): Initializes a new [`Vector`](#c4d.IconData).

## Members <a id="members"></a>

### Bitmap Parts <a id="c4d.IconData-method-Bitmap-Parts"></a>

#### `IconData.GetClonePart(self)` <a id="c4d.IconData.GetClonePart"></a>

Gets a copy of the bitmap’s part for the icon data.

**Return type:** [`c4d.bitmaps.BaseBitmap`](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)

**Returns:** The copy of the icon part.

#### `IconData.GetGuiScalePart(self)` <a id="c4d.IconData.GetGuiScalePart"></a>

Gets a copy of the scaled bitmap’s part for the icon data with the size `IconData.GetGuiW()`/`IconData.GetGuiH()`.

**Return type:** [`c4d.bitmaps.BaseBitmap`](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)

**Returns:** The copy of the scaled icon part.

### Display Dimensions <a id="c4d.IconData-method-Display-Dimensions"></a>

#### `IconData.GetGuiH(self)` <a id="c4d.IconData.GetGuiH"></a>

Gets the GUI scaled height of the icon data.

**Return type:** int

**Returns:** The GUI scaled height.

#### `IconData.GetGuiW(self)` <a id="c4d.IconData.GetGuiW"></a>

Gets the GUI scaled width of the icon data.

**Parameters:** **value** (*int*) – The GUI scaled width.

### Magic Methods <a id="c4d.IconData-method-Magic-Methods"></a>

#### `IconData.__init__(self)` <a id="c4d.IconData.__init__"></a>

Initializes a new [`Vector`](#c4d.IconData).
