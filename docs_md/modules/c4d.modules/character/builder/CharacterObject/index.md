<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/character/builder/CharacterObject/index.html -->

# c4d.modules.character.builder.CharacterObject <a id="c4d-modules-character-builder-characterobject"></a>

## *class* `c4d.modules.character.builder.CharacterObject` <a id="c4d.modules.character.builder.CharacterObject"></a>

## Overview <a id="overview"></a>

- [`CharacterObject.FindObject()`](#c4d.modules.character.builder.CharacterObject.FindObject): Find an object by template name.
- [`CharacterObject.GetFirst()`](#c4d.modules.character.builder.CharacterObject.GetFirst): Returns the first character component.
- [`CharacterObject.GetObject()`](#c4d.modules.character.builder.CharacterObject.GetObject): Get the character object.

## Members <a id="members"></a>

### Component Access <a id="c4d.modules.character.builder.CharacterObject-method-Component-Access"></a>

#### `CharacterObject.FindObject(self, name)` <a id="c4d.modules.character.builder.CharacterObject.FindObject"></a>

Find an object by template name.

**Parameters:** **name** (*str*) – The object name to search for.

**Return type:** Optional[[c4d.BaseObject](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The found object or **None**.

#### `CharacterObject.GetFirst(self)` <a id="c4d.modules.character.builder.CharacterObject.GetFirst"></a>

Returns the first character component.

**Return type:** Optional[[c4d.modules.character.builder.ComponentObject](../ComponentObject/index.md#c4d.modules.character.builder.ComponentObject)]

**Returns:** The first component or **None**.

#### `CharacterObject.GetObject(self)` <a id="c4d.modules.character.builder.CharacterObject.GetObject"></a>

Get the character object.

**Return type:** [c4d.BaseObject](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

**Returns:** The character BaseObject.
