<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/Quaternion/index.html -->

# c4d.Quaternion <a id="c4d-quaternion"></a>

## *class* `c4d.Quaternion` <a id="c4d.Quaternion"></a>

Has methods for conversion to and from a rotation matrix: `GetMatrix`/`SetMatrix`/`SetMatrixNorm`.

*New in version R17.048.*

**Attributes**

## `c4d.Quaternion.w` <a id="c4d.Quaternion.w"></a>

The rotation angle.

**Type:** float

## `c4d.Quaternion.v` <a id="c4d.Quaternion.v"></a>

The direction vector.

**Type:** [`Vector`](../Vector/index.md#c4d.Vector)

## Overview <a id="overview"></a>

**Magic Methods**

- [`Quaternion.__init__()`](#c4d.Quaternion.__init__): Returns a new [`Quaternion`](#c4d.Quaternion) instance.

**Matrix Conversion**

- [`Quaternion.GetMatrix()`](#c4d.Quaternion.GetMatrix): Derives a rotation matrix from the quaternion.
- [`Quaternion.SetMatrix()`](#c4d.Quaternion.SetMatrix): Derives quaternion values from a rotation matrix.
- [`Quaternion.SetMatrixNorm()`](#c4d.Quaternion.SetMatrixNorm): Derives quaternion values from a normalized rotation matrix.

**Rotation Representation**

- [`Quaternion.SetAxis()`](#c4d.Quaternion.SetAxis): Sets the quaternion values directly.
- [`Quaternion.SetHPB()`](#c4d.Quaternion.SetHPB): Derives quaternion values from a HPB rotation.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.Quaternion-method-Magic-Methods"></a>

#### `Quaternion.__init__(self)` <a id="c4d.Quaternion.__init__"></a>

Returns a new [`Quaternion`](#c4d.Quaternion) instance.

### Matrix Conversion <a id="c4d.Quaternion-method-Matrix-Conversion"></a>

#### `Quaternion.GetMatrix(self)` <a id="c4d.Quaternion.GetMatrix"></a>

Derives a rotation matrix from the quaternion.

**Return type:** [c4d.Matrix](../Matrix/index.md#c4d.Matrix)

**Returns:** The rotation matrix.

#### `Quaternion.SetMatrix(self, m)` <a id="c4d.Quaternion.SetMatrix"></a>

Derives quaternion values from a rotation matrix.

**Parameters:** **m** ([*c4d.Matrix*](../Matrix/index.md#c4d.Matrix)) – The rotation matrix to set.

#### `Quaternion.SetMatrixNorm(self, m)` <a id="c4d.Quaternion.SetMatrixNorm"></a>

Derives quaternion values from a normalized rotation matrix.

**Parameters:** **m** ([*c4d.Matrix*](../Matrix/index.md#c4d.Matrix)) – The normalized rotation matrix to set.

### Rotation Representation <a id="c4d.Quaternion-method-Rotation-Representation"></a>

#### `Quaternion.SetAxis(self, ax, ww)` <a id="c4d.Quaternion.SetAxis"></a>

Sets the quaternion values directly.

**Parameters:**

- **ax** ([*c4d.Vector*](../Vector/index.md#c4d.Vector)) – The direction vector.
- **ww** (*float*) – The rotation angle.

#### `Quaternion.SetHPB(self, hpb)` <a id="c4d.Quaternion.SetHPB"></a>

Derives quaternion values from a HPB rotation.

**Parameters:** **hpb** ([*c4d.Vector*](../Vector/index.md#c4d.Vector)) – The HPB rotation.
