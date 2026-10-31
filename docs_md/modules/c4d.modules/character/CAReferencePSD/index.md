<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/character/CAReferencePSD/index.html -->

# c4d.modules.character.CAReferencePSD <a id="c4d-modules-character-careferencepsd"></a>

## *class* `c4d.modules.character.CAReferencePSD` <a id="c4d.modules.character.CAReferencePSD"></a>

Allows to access the PSD referential data and functions.  
Only used with a point pose in PSD Mode.

*New in version R19.*

## Overview <a id="overview"></a>

**Driver Overrides**

- [`CAReferencePSD.ClearAllForcedDrivers()`](#c4d.modules.character.CAReferencePSD.ClearAllForcedDrivers): Removes all user defined joint as driver and let the system manage it automatically.
- [`CAReferencePSD.ForceJointAsDriver()`](#c4d.modules.character.CAReferencePSD.ForceJointAsDriver): Forces the joint index to be a driver.
- [`CAReferencePSD.IsJointForcedAsDriver()`](#c4d.modules.character.CAReferencePSD.IsJointForcedAsDriver): Checks if the joint index is a user forced driver.

**External Controllers**

- [`CAReferencePSD.ClearAllExternalControllers()`](#c4d.modules.character.CAReferencePSD.ClearAllExternalControllers): Removes all external controllers assigned to the reference pose.
- [`CAReferencePSD.GetExternalController()`](#c4d.modules.character.CAReferencePSD.GetExternalController): Returns the controller assigned to the given index.
- [`CAReferencePSD.GetExternalControllerCount()`](#c4d.modules.character.CAReferencePSD.GetExternalControllerCount): Return the number of external controllers associated with the reference pose.
- [`CAReferencePSD.GetExternalControllerMatrix()`](#c4d.modules.character.CAReferencePSD.GetExternalControllerMatrix): Returns the matrix stored at the given index.
- [`CAReferencePSD.RemoveExternalController()`](#c4d.modules.character.CAReferencePSD.RemoveExternalController): Removes the external controller at the given index.
- [`CAReferencePSD.SetExternalControllerMatrix()`](#c4d.modules.character.CAReferencePSD.SetExternalControllerMatrix): Adds or adjusts the given controller global matrix to be part of the reference pose.

**Interpolation Mode**

- [`CAReferencePSD.GetInterpolationMode()`](#c4d.modules.character.CAReferencePSD.GetInterpolationMode): Returns the auto weighting interpolation mode.
- [`CAReferencePSD.SetInterpolationMode()`](#c4d.modules.character.CAReferencePSD.SetInterpolationMode): Sets the auto weighting interpolation mode.

**Reference Pose**

- [`CAReferencePSD.RestoreReferencePose()`](#c4d.modules.character.CAReferencePSD.RestoreReferencePose): Displays skeleton and user defined controller at the reference pose.
- [`CAReferencePSD.UpdateReferencePose()`](#c4d.modules.character.CAReferencePSD.UpdateReferencePose): Updates the current skeleton state as the PSD reference pose.

## Members <a id="members"></a>

### Driver Overrides <a id="c4d.modules.character.CAReferencePSD-method-Driver-Overrides"></a>

#### `CAReferencePSD.ClearAllForcedDrivers(self)` <a id="c4d.modules.character.CAReferencePSD.ClearAllForcedDrivers"></a>

Removes all user defined joint as driver and let the system manage it automatically.

#### `CAReferencePSD.ForceJointAsDriver(self, jointIndex, forceDriver)` <a id="c4d.modules.character.CAReferencePSD.ForceJointAsDriver"></a>

Forces the joint index to be a driver.

> **Note:** If any of the joints is marked as a forced driver, only those are considered in automatic weighting.

**Parameters:**

- **jointIndex** (*int*) – The weight tag joint index to use as driver.
- **forceDriver** (*bool*) – **True** if the joint is used as a driver, otherwise **False**.

#### `CAReferencePSD.IsJointForcedAsDriver(self, jointIndex)` <a id="c4d.modules.character.CAReferencePSD.IsJointForcedAsDriver"></a>

Checks if the joint index is a user forced driver.

> **Note:** If any of the joints is marked as a forced driver, only those are considered in automatic weighting.

**Parameters:** **jointIndex** (*int*) – The weight tag joint index to use as driver.

**Return type:** bool

**Returns:** **True** if the joint is forced as a driver, otherwise **False**.

### External Controllers <a id="c4d.modules.character.CAReferencePSD-method-External-Controllers"></a>

#### `CAReferencePSD.ClearAllExternalControllers(self)` <a id="c4d.modules.character.CAReferencePSD.ClearAllExternalControllers"></a>

Removes all external controllers assigned to the reference pose.

#### `CAReferencePSD.GetExternalController(self, controllerIndex)` <a id="c4d.modules.character.CAReferencePSD.GetExternalController"></a>

Returns the controller assigned to the given index.

**Parameters:** **controllerIndex** (*int*) – The controller index: *0* <= *controllerIndex* < [`GetExternalControllerCount()`](#c4d.modules.character.CAReferencePSD.GetExternalControllerCount).

**Return type:** Optional[[c4d.BaseObject](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The external controller, or **None** if the function failed.

#### `CAReferencePSD.GetExternalControllerCount(self)` <a id="c4d.modules.character.CAReferencePSD.GetExternalControllerCount"></a>

Return the number of external controllers associated with the reference pose.

**Return type:** int

**Returns:** The external controller count.

#### `CAReferencePSD.GetExternalControllerMatrix(self, controllerIndex)` <a id="c4d.modules.character.CAReferencePSD.GetExternalControllerMatrix"></a>

Returns the matrix stored at the given index.

**Parameters:** **controllerIndex** (*int*) – The controller index: *0* <= *controllerIndex* < [`GetExternalControllerCount()`](#c4d.modules.character.CAReferencePSD.GetExternalControllerCount).

**Return type:** [c4d.Matrix](../../../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The external controller global matrix, or a default [`c4d.Matrix()`](../../../c4d/Matrix/index.md#c4d.Matrix) if the function failed.

#### `CAReferencePSD.RemoveExternalController(self, controllerIndex)` <a id="c4d.modules.character.CAReferencePSD.RemoveExternalController"></a>

Removes the external controller at the given index.

**Parameters:** **controllerIndex** (*int*) – The controller index: *0* <= *controllerIndex* < [`GetExternalControllerCount()`](#c4d.modules.character.CAReferencePSD.GetExternalControllerCount).

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `CAReferencePSD.SetExternalControllerMatrix(self, controllerIndex, globalMatrix)` <a id="c4d.modules.character.CAReferencePSD.SetExternalControllerMatrix"></a>

Adds or adjusts the given controller global matrix to be part of the reference pose.

**Parameters:**

- **controllerIndex** (*int*) – The controller index: *0* <= *controllerIndex* < [`GetExternalControllerCount()`](#c4d.modules.character.CAReferencePSD.GetExternalControllerCount).
- **globalMatrix** ([*c4d.Matrix*](../../../c4d/Matrix/index.md#c4d.Matrix)) – The global matrix used as a reference.

**Return type:** int

**Returns:** The index of the controller, **NOTOK**/**-1** if invalid.

### Interpolation Mode <a id="c4d.modules.character.CAReferencePSD-method-Interpolation-Mode"></a>

#### `CAReferencePSD.GetInterpolationMode(self)` <a id="c4d.modules.character.CAReferencePSD.GetInterpolationMode"></a>

Returns the auto weighting interpolation mode.

**Return type:** int

**Returns:**

The interpolation mode:

|   |   |
|---|---|
| *CAMORPH_PSDINTERPOLATION_MODE_AXIS* | Per joint axis. |
| *CAMORPH_PSDINTERPOLATION_MODE_JOINT* | Per joint interpolation (joint axis average). |
| *CAMORPH_PSDINTERPOLATION_MODE_GLOBAL* | Use one global value (joint average). |
| *CAMORPH_PSDINTERPOLATION_MODE_DEFAULT* | Default. |

#### `CAReferencePSD.SetInterpolationMode(self, interpMode)` <a id="c4d.modules.character.CAReferencePSD.SetInterpolationMode"></a>

Sets the auto weighting interpolation mode.

**Parameters:**

**interpMode** (*int*) –

The interpolation mode to set:

|   |   |
|---|---|
| *CAMORPH_PSDINTERPOLATION_MODE_AXIS* | Per joint axis. |
| *CAMORPH_PSDINTERPOLATION_MODE_JOINT* | Per joint interpolation (joint axis average). |
| *CAMORPH_PSDINTERPOLATION_MODE_GLOBAL* | Use one global value (joint average). |
| *CAMORPH_PSDINTERPOLATION_MODE_DEFAULT* | Default. |

### Reference Pose <a id="c4d.modules.character.CAReferencePSD-method-Reference-Pose"></a>

#### `CAReferencePSD.RestoreReferencePose(self)` <a id="c4d.modules.character.CAReferencePSD.RestoreReferencePose"></a>

Displays skeleton and user defined controller at the reference pose.

#### `CAReferencePSD.UpdateReferencePose(self)` <a id="c4d.modules.character.CAReferencePSD.UpdateReferencePose"></a>

Updates the current skeleton state as the PSD reference pose.
