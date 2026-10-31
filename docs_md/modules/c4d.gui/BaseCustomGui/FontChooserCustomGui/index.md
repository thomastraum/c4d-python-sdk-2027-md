<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.gui/BaseCustomGui/FontChooserCustomGui/index.html -->

# c4d.gui.FontChooserCustomGui <a id="c4d-gui-fontchoosercustomgui"></a>

## *class* `c4d.gui.FontChooserCustomGui` <a id="c4d.gui.FontChooserCustomGui"></a>

Font chooser custom GUI (*CUSTOMGUI_FONTCHOOSER*). Here are the settings:

|   |   |   |
|---|---|---|
| *FONTCHOOSER_ENABLE_SIZE* | bool | **True** if the size popup should be displayed. |
| *FONTCHOOSER_ENABLE_FILTER* | bool | **True** Whether font filter field should be displayed. |

*New in version R17.032.*

Parent Class:

- [`c4d.gui.BaseCustomGui`](../index.md#c4d.gui.BaseCustomGui)

## Overview <a id="overview"></a>

- [`FontChooserCustomGui.GetFont()`](#c4d.gui.FontChooserCustomGui.GetFont): Retrieves the font container.
- [`FontChooserCustomGui.SetFont()`](#c4d.gui.FontChooserCustomGui.SetFont): Sets the font container.

## Members <a id="members"></a>

### Font Selection <a id="c4d.gui.FontChooserCustomGui-method-Font-Selection"></a>

#### `FontChooserCustomGui.GetFont(self)` <a id="c4d.gui.FontChooserCustomGui.GetFont"></a>

Retrieves the font container.

**Return type:** [c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The font container.

#### `FontChooserCustomGui.SetFont(self, bc)` <a id="c4d.gui.FontChooserCustomGui.SetFont"></a>

Sets the font container.

> **Note:** Use `GeClipMap.GetFontDescription()` or `GeClipMap.EnumerateFonts()` to get a font description container.

**Parameters:** **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The font container.
