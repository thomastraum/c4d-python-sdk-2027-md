<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/character/MTCharacterMotionTransferTag/index.html -->

# c4d.modules.character.MTCharacterMotionTransferTag <a id="c4d-modules-character-mtcharactermotiontransfertag"></a>

## *class* `c4d.modules.character.MTCharacterMotionTransferTag` <a id="c4d.modules.character.MTCharacterMotionTransferTag"></a>

Represents the Motion Transfer tag.

*New in version R24.*

Parent Class:

- [`c4d.BaseTag`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)

## Overview <a id="overview"></a>

- [`MTCharacterMotionTransferTag.GetExposedBodyPartSettings()`](#c4d.modules.character.MTCharacterMotionTransferTag.GetExposedBodyPartSettings): Returns BaseContainer containing the solver settings for the given identifier.
- [`MTCharacterMotionTransferTag.SetExposedBodyPartSettings()`](#c4d.modules.character.MTCharacterMotionTransferTag.SetExposedBodyPartSettings): Sets body part solver settings for an exposed body part.

## Members <a id="members"></a>

### Body Part Solver Settings <a id="c4d.modules.character.MTCharacterMotionTransferTag-method-Body-Part-Solver-Settings"></a>

#### `MTCharacterMotionTransferTag.GetExposedBodyPartSettings(self, bodyPartIdentifier)` <a id="c4d.modules.character.MTCharacterMotionTransferTag.GetExposedBodyPartSettings"></a>

Returns BaseContainer containing the solver settings for the given identifier.  
See next IDs for value stored in the returned container.

| Symbol ID | Symbol Type |
|---|---|
| CS_BPSS_IDENT_ID | String |
| CS_BPSS_WEIGHT_ID | Float |
| CS_BPSS_ACTIVE_ID | Bool |
| CS_BPSS_POSITIONWEIGHT_ID | Float |
| CS_BPSS_ROTATIONWEIGHT_ID | Float |
| CS_BPSS_SCALEWEIGHT_ID | Float |
| CS_BPSS_POSITIONACTIVE_ID | Bool |
| CS_BPSS_ROTATIONACTIVE_ID | Bool |
| CS_BPSS_SCALEACTIVE_ID | Bool |

**Parameters:** **bodyPartIdentifier** ([`maxon.InternedId`](../../../maxon_generated/datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – Identifier used to get the body part settings.

**Returns:**

**Return type:** [c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)

#### `MTCharacterMotionTransferTag.SetExposedBodyPartSettings(self, bodyPartSettings)` <a id="c4d.modules.character.MTCharacterMotionTransferTag.SetExposedBodyPartSettings"></a>

Sets body part solver settings for an exposed body part.  
See next IDs to configure the container.

| Symbol ID | Symbol Type |
|---|---|
| CS_BPSS_IDENT_ID | String |
| CS_BPSS_WEIGHT_ID | Float |
| CS_BPSS_ACTIVE_ID | Bool |
| CS_BPSS_POSITIONWEIGHT_ID | Float |
| CS_BPSS_ROTATIONWEIGHT_ID | Float |
| CS_BPSS_SCALEWEIGHT_ID | Float |
| CS_BPSS_POSITIONACTIVE_ID | Bool |
| CS_BPSS_ROTATIONACTIVE_ID | Bool |
| CS_BPSS_SCALEACTIVE_ID | Bool |

**Parameters:** **bodyPartSettings** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The BaseContainer with the data to set
