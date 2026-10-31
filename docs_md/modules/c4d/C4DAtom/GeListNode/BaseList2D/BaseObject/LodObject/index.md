<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/LodObject/index.html -->

# c4d.LodObject <a id="c4d-lodobject"></a>

## *class* `c4d.LodObject` <a id="c4d.LodObject"></a>

Represents the LOD object.

The instance object class of type *Olod*.

*New in version R19.*

Parent Class:

- [`c4d.BaseObject`](../index.md#c4d.BaseObject)

## Overview <a id="overview"></a>

**Display Modes**

- [`LodObject.GetDisplayBFCDescID()`](#c4d.LodObject.GetDisplayBFCDescID): Calculates the dynamic description ID of the Display Backface Culling control for the passed LOD *level*.
- [`LodObject.GetDisplayShModeDescID()`](#c4d.LodObject.GetDisplayShModeDescID): Calculates the dynamic description ID of the Display Shading Mode control for the passed LOD *level*.
- [`LodObject.GetDisplayStModeDescID()`](#c4d.LodObject.GetDisplayStModeDescID): Calculates the dynamic description ID of the Display Style Mode control for the passed LOD *level*.
- [`LodObject.GetDisplayTexDescID()`](#c4d.LodObject.GetDisplayTexDescID): Calculates the dynamic description ID of the Display Texture control for the passed LOD *level*.

**Level Controls**

- [`LodObject.GetDecimateStrengthDescID()`](#c4d.LodObject.GetDecimateStrengthDescID): Calculates the dynamic description ID of the decimation strength for the passed LOD *level*.
- [`LodObject.GetManualModeObjectListDescID()`](#c4d.LodObject.GetManualModeObjectListDescID): Calculates the dynamic description ID of the object list for the passed LOD *level*.
- [`LodObject.GetPerObjectControlDescID()`](#c4d.LodObject.GetPerObjectControlDescID): Calculates the dynamic description ID of the per object control for the passed LOD *level*.
- [`LodObject.GetShowControlDescID()`](#c4d.LodObject.GetShowControlDescID): Calculates the dynamic description ID of the show control for the passed LOD *level*.
- [`LodObject.GetSimplifyModeDescID()`](#c4d.LodObject.GetSimplifyModeDescID): Calculates the dynamic description ID of the simplify mode for the passed LOD *level*.

**Level Management**

- [`LodObject.GetCurrentLevel()`](#c4d.LodObject.GetCurrentLevel): Queries the current LOD level.
- [`LodObject.GetLevelCount()`](#c4d.LodObject.GetLevelCount): Queries the current number of LOD levels.

**Magic Methods**

- [`LodObject.__init__()`](#c4d.LodObject.__init__): Creates a LOD object.

**Null Display**

- [`LodObject.GetNullAspectRatioDescID()`](#c4d.LodObject.GetNullAspectRatioDescID): Calculates the dynamic description ID of the NullObject Aspect Ratio control for the passed LOD *level*.
- [`LodObject.GetNullDisplayDescID()`](#c4d.LodObject.GetNullDisplayDescID): Calculates the dynamic description ID of the NullObject Display control for the passed LOD *level*.
- [`LodObject.GetNullOrientationDescID()`](#c4d.LodObject.GetNullOrientationDescID): Calculates the dynamic description ID of the NullObject Orientation control for the passed LOD *level*.
- [`LodObject.GetNullRadiusDescID()`](#c4d.LodObject.GetNullRadiusDescID): Calculates the dynamic description ID of the NullObject Radius control for the passed LOD *level*.

## Members <a id="members"></a>

### Display Modes <a id="c4d.LodObject-method-Display-Modes"></a>

#### `LodObject.GetDisplayBFCDescID(self, level)` <a id="c4d.LodObject.GetDisplayBFCDescID"></a>

Calculates the dynamic description ID of the Display Backface Culling control for the passed LOD *level*.

**Parameters:** **level** (*int*) – The LOD level.

**Return type:** Optional[[c4d.DescID](../../../../../DescID/index.md#c4d.DescID)]

**Returns:** The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.

#### `LodObject.GetDisplayShModeDescID(self, level)` <a id="c4d.LodObject.GetDisplayShModeDescID"></a>

Calculates the dynamic description ID of the Display Shading Mode control for the passed LOD *level*.

**Parameters:** **level** (*int*) – The LOD level.

**Return type:** Optional[[c4d.DescID](../../../../../DescID/index.md#c4d.DescID)]

**Returns:** The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.

#### `LodObject.GetDisplayStModeDescID(self, level)` <a id="c4d.LodObject.GetDisplayStModeDescID"></a>

Calculates the dynamic description ID of the Display Style Mode control for the passed LOD *level*.

**Parameters:** **level** (*int*) – The LOD level.

**Return type:** Optional[[c4d.DescID](../../../../../DescID/index.md#c4d.DescID)]

**Returns:** The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.

#### `LodObject.GetDisplayTexDescID(self, level)` <a id="c4d.LodObject.GetDisplayTexDescID"></a>

Calculates the dynamic description ID of the Display Texture control for the passed LOD *level*.

**Parameters:** **level** (*int*) – The LOD level.

**Return type:** Optional[[c4d.DescID](../../../../../DescID/index.md#c4d.DescID)]

**Returns:** The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.

### Level Controls <a id="c4d.LodObject-method-Level-Controls"></a>

#### `LodObject.GetDecimateStrengthDescID(self, level)` <a id="c4d.LodObject.GetDecimateStrengthDescID"></a>

Calculates the dynamic description ID of the decimation strength for the passed LOD *level*.

**Parameters:** **level** (*int*) – The LOD level.

**Return type:** Optional[[c4d.DescID](../../../../../DescID/index.md#c4d.DescID)]

**Returns:** The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.

#### `LodObject.GetManualModeObjectListDescID(self, level)` <a id="c4d.LodObject.GetManualModeObjectListDescID"></a>

Calculates the dynamic description ID of the object list for the passed LOD *level*.

**Parameters:** **level** (*int*) – The LOD level.

**Return type:** Optional[[c4d.DescID](../../../../../DescID/index.md#c4d.DescID)]

**Returns:** The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.

#### `LodObject.GetPerObjectControlDescID(self, level)` <a id="c4d.LodObject.GetPerObjectControlDescID"></a>

Calculates the dynamic description ID of the per object control for the passed LOD *level*.

**Parameters:** **level** (*int*) – The LOD level.

**Return type:** Optional[[c4d.DescID](../../../../../DescID/index.md#c4d.DescID)]

**Returns:** The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.

#### `LodObject.GetShowControlDescID(self, level)` <a id="c4d.LodObject.GetShowControlDescID"></a>

Calculates the dynamic description ID of the show control for the passed LOD *level*.

**Parameters:** **level** (*int*) – The LOD level.

**Return type:** Optional[[c4d.DescID](../../../../../DescID/index.md#c4d.DescID)]

**Returns:** The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.

#### `LodObject.GetSimplifyModeDescID(self, level)` <a id="c4d.LodObject.GetSimplifyModeDescID"></a>

Calculates the dynamic description ID of the simplify mode for the passed LOD *level*.

**Parameters:** **level** (*int*) – The LOD level.

**Return type:** Optional[[c4d.DescID](../../../../../DescID/index.md#c4d.DescID)]

**Returns:** The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.

### Level Management <a id="c4d.LodObject-method-Level-Management"></a>

#### `LodObject.GetCurrentLevel(self)` <a id="c4d.LodObject.GetCurrentLevel"></a>

Queries the current LOD level.

**Return type:** int

**Returns:** The current LOD level index, or **NOTOK**/**-1** in error case.

#### `LodObject.GetLevelCount(self)` <a id="c4d.LodObject.GetLevelCount"></a>

Queries the current number of LOD levels.

**Return type:** int

**Returns:** The current LOD level count, or **NOTOK**/**-1** in error case.

### Magic Methods <a id="c4d.LodObject-method-Magic-Methods"></a>

#### `LodObject.__init__(self)` <a id="c4d.LodObject.__init__"></a>

Creates a LOD object.

### Null Display <a id="c4d.LodObject-method-Null-Display"></a>

#### `LodObject.GetNullAspectRatioDescID(self, level)` <a id="c4d.LodObject.GetNullAspectRatioDescID"></a>

Calculates the dynamic description ID of the NullObject Aspect Ratio control for the passed LOD *level*.

**Parameters:** **level** (*int*) – The LOD level.

**Return type:** Optional[[c4d.DescID](../../../../../DescID/index.md#c4d.DescID)]

**Returns:** The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.

#### `LodObject.GetNullDisplayDescID(self, level)` <a id="c4d.LodObject.GetNullDisplayDescID"></a>

Calculates the dynamic description ID of the NullObject Display control for the passed LOD *level*.

**Parameters:** **level** (*int*) – The LOD level.

**Return type:** Optional[[c4d.DescID](../../../../../DescID/index.md#c4d.DescID)]

**Returns:** The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.

#### `LodObject.GetNullOrientationDescID(self, level)` <a id="c4d.LodObject.GetNullOrientationDescID"></a>

Calculates the dynamic description ID of the NullObject Orientation control for the passed LOD *level*.

**Parameters:** **level** (*int*) – The LOD level.

**Return type:** Optional[[c4d.DescID](../../../../../DescID/index.md#c4d.DescID)]

**Returns:** The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.

#### `LodObject.GetNullRadiusDescID(self, level)` <a id="c4d.LodObject.GetNullRadiusDescID"></a>

Calculates the dynamic description ID of the NullObject Radius control for the passed LOD *level*.

**Parameters:** **level** (*int*) – The LOD level.

**Return type:** Optional[[c4d.DescID](../../../../../DescID/index.md#c4d.DescID)]

**Returns:** The resulting description ID, if mode and criteria are compatible with the requested parameter, otherwise **None**.
