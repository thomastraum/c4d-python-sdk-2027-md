<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/bodypaint/PaintBitmap/PaintLayer/index.html -->

# c4d.modules.bodypaint.PaintLayer <a id="c4d-modules-bodypaint-paintlayer"></a>

## *class* `c4d.modules.bodypaint.PaintLayer` <a id="c4d.modules.bodypaint.PaintLayer"></a>

The abstract base class of all paint classes.  
Can be a texture, material, layer or mask.

Parent Class:

- [`c4d.modules.bodypaint.PaintBitmap`](../index.md#c4d.modules.bodypaint.PaintBitmap)

Children Classes:

- [`c4d.modules.bodypaint.PaintLayerBmp`](PaintLayerBmp/index.md#c4d.modules.bodypaint.PaintLayerBmp)
- [`c4d.modules.bodypaint.PaintLayerFolder`](PaintLayerFolder/index.md#c4d.modules.bodypaint.PaintLayerFolder)
- [`c4d.modules.bodypaint.PaintLayerMask`](PaintLayerMask/index.md#c4d.modules.bodypaint.PaintLayerMask)

## Overview <a id="overview"></a>

**Layer Conversion**

- [`PaintLayer.ToPaintLayerBmp()`](#c4d.modules.bodypaint.PaintLayer.ToPaintLayerBmp): Casts the PaintLayer to a PaintLayerBmp.

**Visibility Control**

- [`PaintLayer.GetShowBit()`](#c4d.modules.bodypaint.PaintLayer.GetShowBit): Get the visibility of the layer.
- [`PaintLayer.SetShowBit()`](#c4d.modules.bodypaint.PaintLayer.SetShowBit): Set the visibility of the layer.

## Members <a id="members"></a>

### Layer Conversion <a id="c4d.modules.bodypaint.PaintLayer-method-Layer-Conversion"></a>

#### `PaintLayer.ToPaintLayerBmp(self)` <a id="c4d.modules.bodypaint.PaintLayer.ToPaintLayerBmp"></a>

Casts the PaintLayer to a PaintLayerBmp.

*New in version R16.021.*

**Return type:** [c4d.modules.bodypaint.PaintLayerBmp](PaintLayerBmp/index.md#c4d.modules.bodypaint.PaintLayerBmp)

**Returns:** The [`PaintLayer`](#c4d.modules.bodypaint.PaintLayer) casted to a [`PaintLayerBmp`](PaintLayerBmp/index.md#c4d.modules.bodypaint.PaintLayerBmp).

### Visibility Control <a id="c4d.modules.bodypaint.PaintLayer-method-Visibility-Control"></a>

#### `PaintLayer.GetShowBit(self, hierarchy, bit)` <a id="c4d.modules.bodypaint.PaintLayer.GetShowBit"></a>

Get the visibility of the layer.

**Parameters:**

- **hierarchy** (*bool*) – If **True** the visiblity of the parents is taken into account (think of layer sets).
- **bit** (*int*) – Must be set to 0.

**Return type:** bool

**Returns:** **True** if visible, otherwise **False**.

#### `PaintLayer.SetShowBit(self, onoff, bit)` <a id="c4d.modules.bodypaint.PaintLayer.SetShowBit"></a>

Set the visibility of the layer.

**Parameters:**

- **onoff** (*bool*) – **True** if visible, otherwise **False**.
- **bit** (*int*) – Must be set to 0.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.
