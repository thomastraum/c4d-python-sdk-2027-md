<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.gui/BaseCustomGui/HyperLinkCustomGui/index.html -->

# c4d.gui.HyperLinkCustomGui <a id="c4d-gui-hyperlinkcustomgui"></a>

## *class* `c4d.gui.HyperLinkCustomGui` <a id="c4d.gui.HyperLinkCustomGui"></a>

Hyper link custom GUI (*CUSTOMGUI_HYPER_LINK_STATIC*). Here are the settings:

|   |   |   |
|---|---|---|
| *HYPERLINK_LINK_TEXT* | str | The static text. |
| *HYPERLINK_LINK_DEST* | str | Link destination. |
| *HYPERLINK_IS_LINK* | bool | **True** if this is a real hyperlink, static text otherwise. |
| *HYPERLINK_ALIGN_LEFT* | bool | Align left. |
| *HYPERLINK_ALIGN_RIGHT* | bool | Align right. |
| *HYPERLINK_NO_UNDERLINE* | bool | No underline. |

*New in version R17.032.*

Parent Class:

- [`c4d.gui.BaseCustomGui`](../index.md#c4d.gui.BaseCustomGui)

## Overview <a id="overview"></a>

- [`HyperLinkCustomGui.GetLinkString()`](#c4d.gui.HyperLinkCustomGui.GetLinkString): Gets the strings.
- [`HyperLinkCustomGui.SetLinkString()`](#c4d.gui.HyperLinkCustomGui.SetLinkString): Sets the strings.

## Members <a id="members"></a>

### Link String Management <a id="c4d.gui.HyperLinkCustomGui-method-Link-String-Management"></a>

#### `HyperLinkCustomGui.GetLinkString(self)` <a id="c4d.gui.HyperLinkCustomGui.GetLinkString"></a>

Gets the strings.

**Return type:** Tuple[str, str]

**Returns:** The link and text strings.

#### `HyperLinkCustomGui.SetLinkString(self, strLink='', strText='')` <a id="c4d.gui.HyperLinkCustomGui.SetLinkString"></a>

Sets the strings.

**Parameters:**

- **strLink** (*str*) – The new link string.
- **strText** (*str*) – The new text string.
