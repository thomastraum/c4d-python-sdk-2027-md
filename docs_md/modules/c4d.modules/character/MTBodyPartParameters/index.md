<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/character/MTBodyPartParameters/index.html -->

# c4d.modules.character.MTBodyPartParameters <a id="c4d-modules-character-mtbodypartparameters"></a>

## *class* `c4d.modules.character.MTBodyPartParameters` <a id="c4d.modules.character.MTBodyPartParameters"></a>

Represents the settings from a body part of a Character Definition.

Retrieved from `MTCharacterBodyPart.GetParameters()`.

*New in version R24.*

**Attributes**

## `c4d.modules.character.MTBodyPartParameters._identifier` <a id="c4d.modules.character.MTBodyPartParameters._identifier"></a>

Need to stay unique in hierarchy.

**Type:** [`maxon.InternedId`](../../../maxon_generated/datatypes/id/maxon.InternedId.md#module-maxon.InternedId)

## `c4d.modules.character.MTBodyPartParameters._name` <a id="c4d.modules.character.MTBodyPartParameters._name"></a>

Name of the Body Part.

**Type:** str

## `c4d.modules.character.MTBodyPartParameters._skeletonNodes` <a id="c4d.modules.character.MTBodyPartParameters._skeletonNodes"></a>

List of skeleton objects.

**Type:** List[c4d.BaseList2D]

## `c4d.modules.character.MTBodyPartParameters._controllerNodes` <a id="c4d.modules.character.MTBodyPartParameters._controllerNodes"></a>

List of controller objects.

**Type:** List[c4d.BaseList2D]

## `c4d.modules.character.MTBodyPartParameters._skeletonKeywords` <a id="c4d.modules.character.MTBodyPartParameters._skeletonKeywords"></a>

Automatic skeleton extraction keywords

**Type:** List[str]

## `c4d.modules.character.MTBodyPartParameters._skeletonDiscardKeywords` <a id="c4d.modules.character.MTBodyPartParameters._skeletonDiscardKeywords"></a>

Automatic skeleton discard extraction keywords

**Type:** List[str]

## `c4d.modules.character.MTBodyPartParameters._transferPosition` <a id="c4d.modules.character.MTBodyPartParameters._transferPosition"></a>

**True** if the position should be transferred.

**Type:** bool

## `c4d.modules.character.MTBodyPartParameters._transferRotation` <a id="c4d.modules.character.MTBodyPartParameters._transferRotation"></a>

**True** if the rotation should be transferred.

**Type:** bool

## `c4d.modules.character.MTBodyPartParameters._transferScale` <a id="c4d.modules.character.MTBodyPartParameters._transferScale"></a>

**True** if the scale should be transferred.

**Type:** bool

## `c4d.modules.character.MTBodyPartParameters._exposeInSolver` <a id="c4d.modules.character.MTBodyPartParameters._exposeInSolver"></a>

**True** if it should be exposed in the motion transfer solver.

**Type:** bool

## `c4d.modules.character.MTBodyPartParameters._transferUserData` <a id="c4d.modules.character.MTBodyPartParameters._transferUserData"></a>

**True** if user data should be transferred.

**Type:** bool

## `c4d.modules.character.MTBodyPartParameters._transferUserDataMode` <a id="c4d.modules.character.MTBodyPartParameters._transferUserDataMode"></a>

The method used to transfer user data

| Symbol ID | Description |
|---|---|
| BYID | Transfer using the ID. |
| BYNAME | Transfer using the Name. |
| BOTH | Transfer using both technique. |

**Type:** int

## Overview <a id="overview"></a>

- [`MTBodyPartParameters.CopyFrom()`](#c4d.modules.character.MTBodyPartParameters.CopyFrom): Copy all the data from **src** to the current [`c4d.modules.character.MTBodyPartParameters`](#c4d.modules.character.MTBodyPartParameters).

## Members <a id="members"></a>

### Data Copying <a id="c4d.modules.character.MTBodyPartParameters-method-Data-Copying"></a>

#### `MTBodyPartParameters.CopyFrom(self, src)` <a id="c4d.modules.character.MTBodyPartParameters.CopyFrom"></a>

Copy all the data from **src** to the current [`c4d.modules.character.MTBodyPartParameters`](#c4d.modules.character.MTBodyPartParameters).

**Parameters:** **src** ([`c4d.modules.character.MTBodyPartParameters`](#c4d.modules.character.MTBodyPartParameters)) – The other [`c4d.modules.character.MTBodyPartParameters`](#c4d.modules.character.MTBodyPartParameters) to copy.
