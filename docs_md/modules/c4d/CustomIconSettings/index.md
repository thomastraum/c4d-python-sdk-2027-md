<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomIconSettings/index.html -->

# c4d.CustomIconSettings <a id="c4d-customiconsettings"></a>

## *class* `c4d.CustomIconSettings` <a id="c4d.CustomIconSettings"></a>

Represents the data passed in the MSG_GETCUSTOMICON_SETTINGS.

*New in version R21.*

**Attributes**

## `c4d.CustomIconSettings._iconFileId` <a id="c4d.CustomIconSettings._iconFileId"></a>

Custom bitmap file path or icon ID.

**Type:** str

## `c4d.CustomIconSettings._colorMode` <a id="c4d.CustomIconSettings._colorMode"></a>

Color mode: 0: None, 1: custom, 2: special cases.

**Type:** int

## `c4d.CustomIconSettings._customColor` <a id="c4d.CustomIconSettings._customColor"></a>

Custom color used if _colorMode == 1.

**Type:** [`maxon.Color`](../../maxon_generated/datatypes/vec_col_mat/maxon.Color.md#module-maxon.Color)

## `c4d.CustomIconSettings._specialColors` <a id="c4d.CustomIconSettings._specialColors"></a>

Special colors (e.g. Light Color for light object).

**Type:** [`maxon.BaseArray`](../../maxon_generated/datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) ([`maxon.Color`](../../maxon_generated/datatypes/vec_col_mat/maxon.Color.md#module-maxon.Color))

## `c4d.CustomIconSettings._defaultIconId` <a id="c4d.CustomIconSettings._defaultIconId"></a>

Icon ID used if no custom bitmap path / icon ID.

**Type:** int

## `c4d.CustomIconSettings._customIcon` <a id="c4d.CustomIconSettings._customIcon"></a>

Custom icon used as default (more priority than _defaultIconId).

**Type:** [`c4d.IconData`](../IconData/index.md#c4d.IconData)

## `c4d.CustomIconSettings._fillDefault` <a id="c4d.CustomIconSettings._fillDefault"></a>

If **True**, CustomIconData will be filled always. Set to **True** only if you provide a _customIcon [`c4d.IconData`](../IconData/index.md#c4d.IconData) or and icon ID different than default, otherwise just leave it **False**.

**Type:** bool

## `c4d.CustomIconSettings._colorizeContrastMode` <a id="c4d.CustomIconSettings._colorizeContrastMode"></a>

If **True**, icon bitmap will be inverted with dark colors for better readability.

**Type:** bool

## `c4d.CustomIconSettings._colorizeContrastModeMaxBrightnessThreshold` <a id="c4d.CustomIconSettings._colorizeContrastModeMaxBrightnessThreshold"></a>

Brightness values greater than this value will be considered as full brightness (1.0)

**Type:** float

## Overview <a id="overview"></a>

- [`CustomIconSettings.FillCustomIconSettingsFromBaseList2D()`](#c4d.CustomIconSettings.FillCustomIconSettingsFromBaseList2D): Fills the passed [`c4d.CustomIconSettings`](#c4d.CustomIconSettings) *settings* with the data from a BaseList2D BaseContainer.
- [`CustomIconSettings.GetCustomIcon()`](#c4d.CustomIconSettings.GetCustomIcon): Fill the dictionary *cid* with the passed CustomIconSettings

## Members <a id="members"></a>

### Icon Settings <a id="c4d.CustomIconSettings-staticmethod-Icon-Settings"></a>

#### *static* `CustomIconSettings.FillCustomIconSettingsFromBaseList2D(settings, data, defaultIconId, bcFillDefault)` <a id="c4d.CustomIconSettings.FillCustomIconSettingsFromBaseList2D"></a>

Fills the passed [`c4d.CustomIconSettings`](#c4d.CustomIconSettings) *settings* with the data from a BaseList2D BaseContainer.

> **Note:** This is mostly used in plugin development. See py-custom-icon example in github.

**Parameters:**

- **settings** ([*c4d.CustomIconSettings*](#c4d.CustomIconSettings)) – The Custom Icon Settings to fill.
- **data** ([*c4d.BaseContainer*](../BaseContainer/index.md#c4d.BaseContainer)) – The BaseContainer of a BaseList2D (retrieved with BaseList2D.GetData()).
- **defaultIconId** (*int*) – The default IconId the CustomIconSettings should use (usually node.GetType()).
- **bcFillDefault** (*bool*) – True if default should be filled

#### *static* `CustomIconSettings.GetCustomIcon(cid, settings, drawBeforeColoring=False)` <a id="c4d.CustomIconSettings.GetCustomIcon"></a>

Fill the dictionary *cid* with the passed CustomIconSettings

> **Note:** This is mostly used in plugin development. See py-custom-icon example in github.

**Parameters:**

- **cid** (*dict*) – A dictionary with the structure of [MSG_GETCUSTOMICON](../../../consts/MSG_C4DATOM_PLUGINS.md#msg-getcustomicon).
- **settings** ([*c4d.CustomIconSettings*](#c4d.CustomIconSettings)) – The Custom Icon Settings to fill *cid* with.
- **drawBeforeColoring** (*bool*) – True if the icon should be drawn before color change.
