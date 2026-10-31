<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.html -->

# c4d.BaseTag <a id="c4d-basetag"></a>

## *class* `c4d.BaseTag` <a id="c4d.BaseTag"></a>

A variety of properties can be added to objects using tags.  
For example, adding smoothing (Phong tag) or preventing an object from being edited accidentally (Protection tag).

Parent Class:

- [`c4d.BaseList2D`](../index.md#c4d.BaseList2D)

Children Classes:

- [`c4d.SelectionTag`](SelectionTag/index.md#c4d.SelectionTag)
- `c4d.CustomDataTag`
- [`c4d.TextureTag`](TextureTag/index.md#c4d.TextureTag)
- [`c4d.VariableTag`](VariableTag/index.md#c4d.VariableTag)
- [`c4d.HNWeightTag`](HNWeightTag/index.md#c4d.HNWeightTag)
- [`c4d.modules.character.CAWeightTag`](../../../../../c4d.modules/character/CAWeightTag/index.md#c4d.modules.character.CAWeightTag)
- [`c4d.modules.character.CAPoseMorphTag`](../../../../../c4d.modules/character/CAPoseMorphTag/index.md#c4d.modules.character.CAPoseMorphTag)
- [`c4d.modules.character.MTCharacterDefinitionTag`](../../../../../c4d.modules/character/MTCharacterDefinitionTag/index.md#c4d.modules.character.MTCharacterDefinitionTag)
- [`c4d.modules.character.MTCharacterMotionTransferTag`](../../../../../c4d.modules/character/MTCharacterMotionTransferTag/index.md#c4d.modules.character.MTCharacterMotionTransferTag)
- [`c4d.modules.hair.HairSelectionTag`](../../../../../c4d.modules/hair/HairSelectionTag/index.md#c4d.modules.hair.HairSelectionTag)
- [`c4d.modules.hair.HairVertexMapTag`](../../../../../c4d.modules/hair/HairVertexMapTag/index.md#c4d.modules.hair.HairVertexMapTag)
- [`c4d.modules.hair.HairTangentTag`](../../../../../c4d.modules/hair/HairTangentTag/index.md#c4d.modules.hair.HairTangentTag)
- [`c4d.modules.sculpting.SculptTag`](../../../../../c4d.modules/sculpting/SculptTag/index.md#c4d.modules.sculpting.SculptTag)
- [`c4d.modules.graphview.XPressoTag`](../../../../../c4d.modules/graphview/XPressoTag/index.md#c4d.modules.graphview.XPressoTag)

## Overview <a id="overview"></a>

**Magic Methods**

- [`BaseTag.__init__()`](#c4d.BaseTag.__init__): Initialize a new [`BaseTag`](#c4d.BaseTag) in memory.

**Object Context**

- [`BaseTag.GetObject()`](#c4d.BaseTag.GetObject): Returns the object where the object is attached.
- [`BaseTag.GetOrigin()`](#c4d.BaseTag.GetOrigin): Returns where the tag was cloned from.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.BaseTag-method-Magic-Methods"></a>

#### `BaseTag.__init__(self, type)` <a id="c4d.BaseTag.__init__"></a>

Initialize a new [`BaseTag`](#c4d.BaseTag) in memory.

**Parameters:** **type** (*int*) – The type of tag. See [Tag Types](../../../../../../types/tags.md).

### Object Context <a id="c4d.BaseTag-method-Object-Context"></a>

#### `BaseTag.GetObject(self)` <a id="c4d.BaseTag.GetObject"></a>

Returns the object where the object is attached.

**Return type:** Optional[[c4d.BaseObject](../BaseObject/index.md#c4d.BaseObject)]

**Returns:** The object or **None** if it is not attached.

#### `BaseTag.GetOrigin(self)` <a id="c4d.BaseTag.GetOrigin"></a>

Returns where the tag was cloned from.

> **Note:** For example, if the tag is on a cache object, it tells you what the original tag was from the original document.

**Return type:** Optional[[c4d.BaseTag](#c4d.BaseTag)]

**Returns:** The origin tag or **None**.
