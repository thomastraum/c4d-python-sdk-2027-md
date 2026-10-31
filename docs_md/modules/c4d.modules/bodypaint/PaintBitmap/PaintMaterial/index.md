<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/bodypaint/PaintBitmap/PaintMaterial/index.html -->

# c4d.modules.bodypaint.PaintMaterial <a id="c4d-modules-bodypaint-paintmaterial"></a>

## *class* `c4d.modules.bodypaint.PaintMaterial` <a id="c4d.modules.bodypaint.PaintMaterial"></a>

The abstract base class of all paint classes.  
Can be a texture, material, layer or mask.

Parent Class:

- [`c4d.modules.bodypaint.PaintBitmap`](../index.md#c4d.modules.bodypaint.PaintBitmap)

## Overview <a id="overview"></a>

- [`PaintMaterial.EnableMaterial()`](#c4d.modules.bodypaint.PaintMaterial.EnableMaterial): Enable material for painting.

## Members <a id="members"></a>

### Material Painting <a id="c4d.modules.bodypaint.PaintMaterial-method-Material-Painting"></a>

#### `PaintMaterial.EnableMaterial(self, doc, on, suppressevent=False, domaterialundo=True)` <a id="c4d.modules.bodypaint.PaintMaterial.EnableMaterial"></a>

Enable material for painting.

**Param:** The document the material belongs to.

**Parameters:**

- **on** (*bool*) – RUE to enable the material for painting, **False** to disable it.
- **suppressevent** (*bool*) – Private.
- **domaterialundo** (*bool*) – If **True** an undo is created on the undo stack.
