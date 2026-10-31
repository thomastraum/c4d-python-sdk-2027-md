<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/motiontracker/MtData/index.html -->

# c4d.modules.motiontracker.MtData <a id="c4d-modules-motiontracker-mtdata"></a>

## *class* `c4d.modules.motiontracker.MtData` <a id="c4d.modules.motiontracker.MtData"></a>

*New in version R18.020.*

## Overview <a id="overview"></a>

**Track Position Retrieval**

- [`MtData.GetNormalisedPosition()`](#c4d.modules.motiontracker.MtData.GetNormalisedPosition): Retrieves the track position in normalized coordinates.
- [`MtData.GetPixelPosition()`](#c4d.modules.motiontracker.MtData.GetPixelPosition): Retrieves the track position in pixel coordinates.

**Track Spatial Direction**

- [`MtData.GetCameraSpaceDirection()`](#c4d.modules.motiontracker.MtData.GetCameraSpaceDirection): Retrieves the camera space ray corresponding to track position.

## Members <a id="members"></a>

### Track Position Retrieval <a id="c4d.modules.motiontracker.MtData-method-Track-Position-Retrieval"></a>

#### `MtData.GetNormalisedPosition(self)` <a id="c4d.modules.motiontracker.MtData.GetNormalisedPosition"></a>

Retrieves the track position in normalized coordinates.

> **Note:**
>
> x is in range *-0.5* to *+0.5* from left to right of image.  
> y is in range *-0.5/aspect* to *+0.5/aspect* from top to bottom of image, where *aspect* is the image aspect ratio.

**Return type:** [`c4d.Vector`](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The track position in normalized coordinates.

#### `MtData.GetPixelPosition(self, footageData, originalRes)` <a id="c4d.modules.motiontracker.MtData.GetPixelPosition"></a>

Retrieves the track position in pixel coordinates.

**Parameters:**

- **footageData** ([*c4d.modules.motiontracker.MtFootageData*](../MtFootageData/index.md#c4d.modules.motiontracker.MtFootageData)) – The footage object (used to define resolution and aspect ratio).

- **originalRes** (*int*) –

  If **True**, returns pixel coordinates for the original footage.  
  If **False**, returns pixel coordinates for the downsampled footage.

**Return type:** [`c4d.Vector`](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The track position in pixel coordinates.

### Track Spatial Direction <a id="c4d.modules.motiontracker.MtData-method-Track-Spatial-Direction"></a>

#### `MtData.GetCameraSpaceDirection(self, focalLength, sensorWidth)` <a id="c4d.modules.motiontracker.MtData.GetCameraSpaceDirection"></a>

Retrieves the camera space ray corresponding to track position.

**Parameters:**

- **focalLength** (*float*) – The focal length to use for the camera (mm).
- **sensorWidth** (*float*) – The sensor width to use for the camera (mm).

**Return type:** [`c4d.Vector`](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The ray in camera space corresponding to the position of the track.
