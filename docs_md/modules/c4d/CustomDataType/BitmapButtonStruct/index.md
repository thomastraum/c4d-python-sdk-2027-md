<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/BitmapButtonStruct/index.html -->

# c4d.BitmapButtonStruct <a id="c4d-bitmapbuttonstruct"></a>

## *class* `c4d.BitmapButtonStruct` <a id="c4d.BitmapButtonStruct"></a>

Bitmap button data type (*CUSTOMDATATYPE_BITMAPBUTTON*) for [`BitmapButtonCustomGui`](../../../c4d.gui/BaseCustomGui/BitmapButtonCustomGui/index.md#c4d.gui.BitmapButtonCustomGui).

*New in version R17.032.*

> **Note:**
>
> Used to get a bitmap button in the Attribute Manager.  
> Specify an object, `BitmapButtonStruct.op`, that provides an icon through the *MSG_DESCRIPTION_GETBITMAP* message.

**Attributes**

## `c4d.BitmapButtonStruct.op` <a id="c4d.BitmapButtonStruct.op"></a>

[Read/Write]

The object to send *MSG_DESCRIPTION_GETBITMAP* to.

**Type:** [`BaseList2D`](../../C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

## `c4d.BitmapButtonStruct.id` <a id="c4d.BitmapButtonStruct.id"></a>

[Read/Write]

The ID of the bitmap button.

**Type:** [`DescID`](../../DescID/index.md#c4d.DescID)

## `c4d.BitmapButtonStruct.dirty` <a id="c4d.BitmapButtonStruct.dirty"></a>

[Read/Write]

The dirty flag. Internally used to detect changes. If this flag changes on parameter set, a new *MSG_DESCRIPTION_GETBITMAP* will be emitted.

**Type:** int

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

- [`BitmapButtonStruct.__init__()`](#c4d.BitmapButtonStruct.__init__): Constructor.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.BitmapButtonStruct-method-Magic-Methods"></a>

#### `BitmapButtonStruct.__init__(self, op, id, dirty)` <a id="c4d.BitmapButtonStruct.__init__"></a>

Constructor.

**Parameters:**

- **op** ([*c4d.BaseList2D*](../../C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The object to send *MSG_DESCRIPTION_GETBITMAP* to.
- **id** ([*c4d.DescID*](../../DescID/index.md#c4d.DescID)) – The ID of the bitmap button.
- **dirty** (*int*) – The dirty flag. Internally used to detect changes. If this flag changes on parameter set, a new *MSG_DESCRIPTION_GETBITMAP* will be emitted.
