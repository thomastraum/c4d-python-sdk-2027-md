<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/TextureTag/index.html -->

# c4d.TextureTag <a id="c4d-texturetag"></a>

## *class* `c4d.TextureTag` <a id="c4d.TextureTag"></a>

Represents the Texture Tag.  
Holds the texture information associated with an object.

Parent Class:

- [`c4d.BaseTag`](../index.md#c4d.BaseTag)

## Overview <a id="overview"></a>

**Get Methods**

- [`TextureTag.GetMaterial()`](#c4d.TextureTag.GetMaterial): Get the current material associated with this tag.
- [`TextureTag.GetMl()`](#c4d.TextureTag.GetMl): Get the texture projection’s coordinate system as a matrix.
- [`TextureTag.GetPos()`](#c4d.TextureTag.GetPos): Get the position of the texture project.
- [`TextureTag.GetRot()`](#c4d.TextureTag.GetRot): Get the rotation of the texture project.
- [`TextureTag.GetScale()`](#c4d.TextureTag.GetScale): Get the scale of the texture project.

**Magic Methods**

- [`TextureTag.__init__()`](#c4d.TextureTag.__init__)

**Set Methods**

- [`TextureTag.SetMaterial()`](#c4d.TextureTag.SetMaterial): Set the material associated with this tag.
- [`TextureTag.SetMl()`](#c4d.TextureTag.SetMl): Sets the texture projection’s coordinate system matrix.
- [`TextureTag.SetPos()`](#c4d.TextureTag.SetPos): Sets the position of the texture projection.
- [`TextureTag.SetRot()`](#c4d.TextureTag.SetRot): Sets the rotation of the texture projection.
- [`TextureTag.SetScale()`](#c4d.TextureTag.SetScale): Sets the scale of the texture projection.

## Members <a id="members"></a>

### Get Methods <a id="c4d.TextureTag-method-Get-Methods"></a>

#### `TextureTag.GetMaterial(self, ignoredoc=False)` <a id="c4d.TextureTag.GetMaterial"></a>

Get the current material associated with this tag.

**Parameters:**

**ignoredoc** (*bool*) –

*New in version R18.020.*

**True** to ignore the tag’s document (default), otherwise **False**.  
**True** by default to keep backward compatibility.

*Changed in version R21.204.*

Changed default value to **False** to match C++.

**Return type:** Optional[[c4d.BaseMaterial](../../BaseMaterial/index.md#c4d.BaseMaterial)]

**Returns:** The material or **None**.

#### `TextureTag.GetMl(self)` <a id="c4d.TextureTag.GetMl"></a>

Get the texture projection’s coordinate system as a matrix.

**Return type:** [c4d.Vector](../../../../../Vector/index.md#c4d.Vector)

**Returns:** The texture projection’s coordinate system.

#### `TextureTag.GetPos(self)` <a id="c4d.TextureTag.GetPos"></a>

Get the position of the texture project.

**Return type:** [c4d.Vector](../../../../../Vector/index.md#c4d.Vector)

**Returns:** The texture XYZ position.

#### `TextureTag.GetRot(self)` <a id="c4d.TextureTag.GetRot"></a>

Get the rotation of the texture project.

**Return type:** [c4d.Vector](../../../../../Vector/index.md#c4d.Vector)

**Returns:** The rot of the texture.

#### `TextureTag.GetScale(self)` <a id="c4d.TextureTag.GetScale"></a>

Get the scale of the texture project.

**Return type:** [c4d.Vector](../../../../../Vector/index.md#c4d.Vector)

**Returns:** The scale of the texture.

### Magic Methods <a id="c4d.TextureTag-method-Magic-Methods"></a>

#### `TextureTag.__init__(self)` <a id="c4d.TextureTag.__init__"></a>

### Set Methods <a id="c4d.TextureTag-method-Set-Methods"></a>

#### `TextureTag.SetMaterial(self, mat)` <a id="c4d.TextureTag.SetMaterial"></a>

Set the material associated with this tag.

**Parameters:** **mat** ([*c4d.BaseMaterial*](../../BaseMaterial/index.md#c4d.BaseMaterial)) – The material for this tag.

#### `TextureTag.SetMl(self, m)` <a id="c4d.TextureTag.SetMl"></a>

Sets the texture projection’s coordinate system matrix.

**Parameters:** **v** ([*c4d.Matrix*](../../../../../Matrix/index.md#c4d.Matrix)) – The texture projection’s coordinate system.

#### `TextureTag.SetPos(self, v)` <a id="c4d.TextureTag.SetPos"></a>

Sets the position of the texture projection.

**Parameters:** **v** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The position of the texture.

#### `TextureTag.SetRot(self, v)` <a id="c4d.TextureTag.SetRot"></a>

Sets the rotation of the texture projection.

**Parameters:** **v** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The rotation of the texture.

#### `TextureTag.SetScale(self, v)` <a id="c4d.TextureTag.SetScale"></a>

Sets the scale of the texture projection.

**Parameters:** **v** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The scale of the texture.
