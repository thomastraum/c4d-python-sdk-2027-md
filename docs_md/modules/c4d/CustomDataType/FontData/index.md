<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/FontData/index.html -->

# c4d.FontData <a id="c4d-fontdata"></a>

## *class* `c4d.FontData` <a id="c4d.FontData"></a>

Data type (*FONTCHOOSER_DATA*) for the font chooser GUI ([`FontChooserCustomGui`](../../../c4d.gui/BaseCustomGui/FontChooserCustomGui/index.md#c4d.gui.FontChooserCustomGui)).

This type is called by value.

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Font Container Access**

- [`FontData.GetFont()`](#c4d.FontData.GetFont): Gets the font container.
- [`FontData.SetFont()`](#c4d.FontData.SetFont): Sets the font container.

**Magic Methods**

- [`FontData.__init__()`](#c4d.FontData.__init__)

## Members <a id="members"></a>

### Font Container Access <a id="c4d.FontData-method-Font-Container-Access"></a>

#### `FontData.GetFont(self)` <a id="c4d.FontData.GetFont"></a>

Gets the font container.

**Return type:** [c4d.BaseContainer](../../BaseContainer/index.md#c4d.BaseContainer)

**Returns:** Font container.

#### `FontData.SetFont(self, bc)` <a id="c4d.FontData.SetFont"></a>

Sets the font container.

**Parameters:** **bc** ([*c4d.BaseContainer*](../../BaseContainer/index.md#c4d.BaseContainer)) – The font container.

### Magic Methods <a id="c4d.FontData-method-Magic-Methods"></a>

#### `FontData.__init__(self, v)` <a id="c4d.FontData.__init__"></a>

**Parameters:** **v** ([*c4d.FontData*](#c4d.FontData)) – Copy constructor.
