<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/character/MTCharacterBodyPart/index.html -->

# c4d.modules.character.MTCharacterBodyPart <a id="c4d-modules-character-mtcharacterbodypart"></a>

## *class* `c4d.modules.character.MTCharacterBodyPart` <a id="c4d.modules.character.MTCharacterBodyPart"></a>

Represents a body part from a Character Definition.

Retrieved from `MTCharacterDefinitionTag.GetRootBodyPart()`.

*New in version R24.*

## Overview <a id="overview"></a>

**Hierarchy Management**

- [`MTCharacterBodyPart.DeleteChild()`](#c4d.modules.character.MTCharacterBodyPart.DeleteChild): Deletes the child at the given index.
- [`MTCharacterBodyPart.GetChild()`](#c4d.modules.character.MTCharacterBodyPart.GetChild): Gets the child at the given index.
- [`MTCharacterBodyPart.GetChildCount()`](#c4d.modules.character.MTCharacterBodyPart.GetChildCount): Gets the child count.
- [`MTCharacterBodyPart.GetParent()`](#c4d.modules.character.MTCharacterBodyPart.GetParent): Gets the parent if any.
- [`MTCharacterBodyPart.InsertChild()`](#c4d.modules.character.MTCharacterBodyPart.InsertChild): Inserts the given child.

**Parameter Management**

- [`MTCharacterBodyPart.GetParameters()`](#c4d.modules.character.MTCharacterBodyPart.GetParameters): Gets the parameters structure.
- [`MTCharacterBodyPart.SetParameters()`](#c4d.modules.character.MTCharacterBodyPart.SetParameters): Sets the parameter for the body part.

## Members <a id="members"></a>

### Hierarchy Management <a id="c4d.modules.character.MTCharacterBodyPart-method-Hierarchy-Management"></a>

#### `MTCharacterBodyPart.DeleteChild(self, index)` <a id="c4d.modules.character.MTCharacterBodyPart.DeleteChild"></a>

Deletes the child at the given index.

**Parameters:** **index** (*int*) – Child index.

**Returns:** **True** if successful, otherwise **False**.

**Return type:** bool

#### `MTCharacterBodyPart.GetChild(self, index)` <a id="c4d.modules.character.MTCharacterBodyPart.GetChild"></a>

Gets the child at the given index.

**Parameters:** **index** (*int*) – Child index.

**Returns:** The child body part

**Return type:** [`c4d.modules.character.MTCharacterBodyPart`](#c4d.modules.character.MTCharacterBodyPart)

#### `MTCharacterBodyPart.GetChildCount(self)` <a id="c4d.modules.character.MTCharacterBodyPart.GetChildCount"></a>

Gets the child count.

**Returns:** The child count.

**Return type:** int

#### `MTCharacterBodyPart.GetParent(self)` <a id="c4d.modules.character.MTCharacterBodyPart.GetParent"></a>

Gets the parent if any.

**Returns:** Parent.

**Return type:** [`c4d.modules.character.MTCharacterBodyPart`](#c4d.modules.character.MTCharacterBodyPart)

#### `MTCharacterBodyPart.InsertChild(self, child)` <a id="c4d.modules.character.MTCharacterBodyPart.InsertChild"></a>

Inserts the given child.

**Parameters:** **child** ([`c4d.modules.character.MTCharacterBodyPart`](#c4d.modules.character.MTCharacterBodyPart)) – Child to insert.

**Returns:** **True** if successful, otherwise **False**.

**Return type:** bool

### Parameter Management <a id="c4d.modules.character.MTCharacterBodyPart-method-Parameter-Management"></a>

#### `MTCharacterBodyPart.GetParameters(self)` <a id="c4d.modules.character.MTCharacterBodyPart.GetParameters"></a>

Gets the parameters structure.

**Returns:** The body part parameters.

**Return type:** [`c4d.modules.character.MTBodyPartParameters`](../MTBodyPartParameters/index.md#c4d.modules.character.MTBodyPartParameters)

#### `MTCharacterBodyPart.SetParameters(self, param)` <a id="c4d.modules.character.MTCharacterBodyPart.SetParameters"></a>

Sets the parameter for the body part.

**Parameters:** **param** ([`c4d.modules.character.MTBodyPartParameters`](../MTBodyPartParameters/index.md#c4d.modules.character.MTBodyPartParameters)) – Parameters.
