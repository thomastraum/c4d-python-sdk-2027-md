<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/HyperLinkData/index.html -->

# c4d.HyperLinkData <a id="c4d-hyperlinkdata"></a>

## *class* `c4d.HyperLinkData` <a id="c4d.HyperLinkData"></a>

Hyper link data (*CUSTOMDATATYPE_HYPER_LINK_STATIC*) for use with [`HyperLinkCustomGui`](../../../c4d.gui/BaseCustomGui/HyperLinkCustomGui/index.md#c4d.gui.HyperLinkCustomGui).

*New in version R17.032.*

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Magic Methods**

- [`HyperLinkData.__init__()`](#c4d.HyperLinkData.__init__)

**String Access**

- [`HyperLinkData.GetStrings()`](#c4d.HyperLinkData.GetStrings): Gets the strings.
- [`HyperLinkData.SetStrings()`](#c4d.HyperLinkData.SetStrings): Sets the strings.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.HyperLinkData-method-Magic-Methods"></a>

#### `HyperLinkData.__init__(self, v)` <a id="c4d.HyperLinkData.__init__"></a>

**Parameters:** **v** ([*c4d.HyperLinkData*](#c4d.HyperLinkData)) – Copy constructor.

### String Access <a id="c4d.HyperLinkData-method-String-Access"></a>

#### `HyperLinkData.GetStrings(self)` <a id="c4d.HyperLinkData.GetStrings"></a>

Gets the strings.

**Return type:** Tuple[str, str]

**Returns:** The link and text strings.

#### `HyperLinkData.SetStrings(self, strLink, strText)` <a id="c4d.HyperLinkData.SetStrings"></a>

Sets the strings.

**Parameters:**

- **strLink** (*str*) – The new link string.
- **strText** (*str*) – The new text string.
