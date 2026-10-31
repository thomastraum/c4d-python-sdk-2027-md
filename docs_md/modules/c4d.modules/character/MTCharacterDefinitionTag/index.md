<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/character/MTCharacterDefinitionTag/index.html -->

# c4d.modules.character.MTCharacterDefinitionTag <a id="c4d-modules-character-mtcharacterdefinitiontag"></a>

## *class* `c4d.modules.character.MTCharacterDefinitionTag` <a id="c4d.modules.character.MTCharacterDefinitionTag"></a>

Represents the Character Definition tag.

*New in version R24.*

Parent Class:

- [`c4d.BaseTag`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)

## Overview <a id="overview"></a>

**Rest Pose Management**

- [`MTCharacterDefinitionTag.ApplyRestPose()`](#c4d.modules.character.MTCharacterDefinitionTag.ApplyRestPose): Applies the current rest pose.
- [`MTCharacterDefinitionTag.ClearRestPose()`](#c4d.modules.character.MTCharacterDefinitionTag.ClearRestPose): Clears the current rest pose.
- [`MTCharacterDefinitionTag.ExtractRestPose()`](#c4d.modules.character.MTCharacterDefinitionTag.ExtractRestPose): Gets current skeleton pose and set it as rest pose.

**Rig Structure**

- [`MTCharacterDefinitionTag.CreateSolver()`](#c4d.modules.character.MTCharacterDefinitionTag.CreateSolver): Creates a solver and assign to the object owner.
- [`MTCharacterDefinitionTag.ExtractSkeleton()`](#c4d.modules.character.MTCharacterDefinitionTag.ExtractSkeleton): Automatic body part extraction for the skeleton.
- [`MTCharacterDefinitionTag.GetRootBodyPart()`](#c4d.modules.character.MTCharacterDefinitionTag.GetRootBodyPart): Returns a copy of the body part hierarchy.
- [`MTCharacterDefinitionTag.SetRootBodyPart()`](#c4d.modules.character.MTCharacterDefinitionTag.SetRootBodyPart): Sets the body part hierarchy.

## Members <a id="members"></a>

### Rest Pose Management <a id="c4d.modules.character.MTCharacterDefinitionTag-method-Rest-Pose-Management"></a>

#### `MTCharacterDefinitionTag.ApplyRestPose(self, undo)` <a id="c4d.modules.character.MTCharacterDefinitionTag.ApplyRestPose"></a>

Applies the current rest pose.

> **Warning:** This should be called only in the main thread.

**Parameters:** **undo** (*bool*) – Add Character definition to the undo stack before any changes.

**Returns:** **True** if successful, otherwise **False**.

**Return type:** bool

#### `MTCharacterDefinitionTag.ClearRestPose(self, undo)` <a id="c4d.modules.character.MTCharacterDefinitionTag.ClearRestPose"></a>

Clears the current rest pose.

> **Warning:** This should be called only in the main thread.

**Parameters:** **undo** (*bool*) – Add Character definition to the undo stack before any changes.

**Returns:** **True** if successful, otherwise **False**.

**Return type:** bool

#### `MTCharacterDefinitionTag.ExtractRestPose(self, undo)` <a id="c4d.modules.character.MTCharacterDefinitionTag.ExtractRestPose"></a>

Gets current skeleton pose and set it as rest pose.

> **Warning:** This should be called only in the main thread.

**Parameters:** **undo** (*bool*) – Add Character definition to the undo stack before any changes.

**Returns:** **True** if successful, otherwise **False**.

**Return type:** bool

### Rig Structure <a id="c4d.modules.character.MTCharacterDefinitionTag-method-Rig-Structure"></a>

#### `MTCharacterDefinitionTag.CreateSolver(self, undo)` <a id="c4d.modules.character.MTCharacterDefinitionTag.CreateSolver"></a>

Creates a solver and assign to the object owner.

> **Warning:** This should be called only in the main thread.

**Parameters:** **undo** (*bool*) – Add Character definition to the undo stack before any changes.

**Returns:** The new created MTCharacterMotionTransferTag.

**Return type:** [`c4d.modules.character.MTCharacterMotionTransferTag`](../MTCharacterMotionTransferTag/index.md#c4d.modules.character.MTCharacterMotionTransferTag)

#### `MTCharacterDefinitionTag.ExtractSkeleton(self, undo)` <a id="c4d.modules.character.MTCharacterDefinitionTag.ExtractSkeleton"></a>

Automatic body part extraction for the skeleton.

> **Warning:** This should be called only in the main thread.

**Parameters:** **undo** (*bool*) – Add Character definition to the undo stack before any changes.

**Returns:** **True** if successful, otherwise **False**.

**Return type:** bool

#### `MTCharacterDefinitionTag.GetRootBodyPart(self)` <a id="c4d.modules.character.MTCharacterDefinitionTag.GetRootBodyPart"></a>

Returns a copy of the body part hierarchy.

**Returns:** The MTCharacterBodyPart.

**Return type:** [`c4d.modules.character.MTCharacterBodyPart`](../MTCharacterBodyPart/index.md#c4d.modules.character.MTCharacterBodyPart)

#### `MTCharacterDefinitionTag.SetRootBodyPart(self, rootBodyPart)` <a id="c4d.modules.character.MTCharacterDefinitionTag.SetRootBodyPart"></a>

Sets the body part hierarchy.

**Parameters:** **rootBodyPart** ([`c4d.modules.character.MTCharacterBodyPart`](../MTCharacterBodyPart/index.md#c4d.modules.character.MTCharacterBodyPart)) – Represent the BodyPart hierarchy.

**Returns:** **True** if successful, otherwise **False**.

**Return type:** bool
