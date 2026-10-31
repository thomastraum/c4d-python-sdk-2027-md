<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/motiontracker/MtFootageData/index.html -->

# c4d.modules.motiontracker.MtFootageData <a id="c4d-modules-motiontracker-mtfootagedata"></a>

## *class* `c4d.modules.motiontracker.MtFootageData` <a id="c4d.modules.motiontracker.MtFootageData"></a>

*New in version R18.020.*

## Overview <a id="overview"></a>

**Aspect Ratios**

- [`MtFootageData.GetImageAspectRatio()`](#c4d.modules.motiontracker.MtFootageData.GetImageAspectRatio): Retrieves the aspect ratio of the footage including effects of pixel aspect ratio.
- [`MtFootageData.GetPixelAspectRatio()`](#c4d.modules.motiontracker.MtFootageData.GetPixelAspectRatio): Retrieves the pixel aspect ratio of the footage.
- [`MtFootageData.GetResolutionAspectRatio()`](#c4d.modules.motiontracker.MtFootageData.GetResolutionAspectRatio): Retrieves the ratio of the horizontal to vertical resolution.

**Footage Identity And Timing**

- [`MtFootageData.GetFirstFrameNumber()`](#c4d.modules.motiontracker.MtFootageData.GetFirstFrameNumber): Retrieves the frame number of the first frame in the footage.
- [`MtFootageData.GetFootageName()`](#c4d.modules.motiontracker.MtFootageData.GetFootageName): Retrieves the filename of the footage (the first frame if an image sequence).
- [`MtFootageData.GetLastFrameNumber()`](#c4d.modules.motiontracker.MtFootageData.GetLastFrameNumber): Retrieves the last number of the first frame in the footage.

**Image Dimensions And Scaling**

- [`MtFootageData.GetDownsamplingFactor()`](#c4d.modules.motiontracker.MtFootageData.GetDownsamplingFactor): Retrieves the downsampling factor used for the footage.
- [`MtFootageData.GetResolutionHeightPix()`](#c4d.modules.motiontracker.MtFootageData.GetResolutionHeightPix): Retrieves the height in pixels of the footage.
- [`MtFootageData.GetResolutionWidthPix()`](#c4d.modules.motiontracker.MtFootageData.GetResolutionWidthPix): Retrieves the width in pixels of the footage.

## Members <a id="members"></a>

### Aspect Ratios <a id="c4d.modules.motiontracker.MtFootageData-method-Aspect-Ratios"></a>

#### `MtFootageData.GetImageAspectRatio(self)` <a id="c4d.modules.motiontracker.MtFootageData.GetImageAspectRatio"></a>

Retrieves the aspect ratio of the footage including effects of pixel aspect ratio.

> **Note:** [`GetImageAspectRatio()`](#c4d.modules.motiontracker.MtFootageData.GetImageAspectRatio) == [`GetResolutionAspectRatio()`](#c4d.modules.motiontracker.MtFootageData.GetResolutionAspectRatio) * [`GetPixelAspectRatio()`](#c4d.modules.motiontracker.MtFootageData.GetPixelAspectRatio)

**Return type:** float

**Returns:** The image aspect ratio.

#### `MtFootageData.GetPixelAspectRatio(self)` <a id="c4d.modules.motiontracker.MtFootageData.GetPixelAspectRatio"></a>

Retrieves the pixel aspect ratio of the footage.

**Return type:** float

**Returns:** The pixel aspect ratio.

#### `MtFootageData.GetResolutionAspectRatio(self)` <a id="c4d.modules.motiontracker.MtFootageData.GetResolutionAspectRatio"></a>

Retrieves the ratio of the horizontal to vertical resolution. Ignores pixel aspect ratio.

**Return type:** float

**Returns:** The aspect ratio from resolution.

### Footage Identity And Timing <a id="c4d.modules.motiontracker.MtFootageData-method-Footage-Identity-And-Timing"></a>

#### `MtFootageData.GetFirstFrameNumber(self)` <a id="c4d.modules.motiontracker.MtFootageData.GetFirstFrameNumber"></a>

Retrieves the frame number of the first frame in the footage. *-1* if no footage loaded.

**Return type:** int

**Returns:** The first frame number.

#### `MtFootageData.GetFootageName(self)` <a id="c4d.modules.motiontracker.MtFootageData.GetFootageName"></a>

Retrieves the filename of the footage (the first frame if an image sequence).

**Return type:** str

**Returns:** The filename.

#### `MtFootageData.GetLastFrameNumber(self)` <a id="c4d.modules.motiontracker.MtFootageData.GetLastFrameNumber"></a>

Retrieves the last number of the first frame in the footage. *-1* if no footage loaded.

**Return type:** int

**Returns:** The last frame number.

### Image Dimensions And Scaling <a id="c4d.modules.motiontracker.MtFootageData-method-Image-Dimensions-And-Scaling"></a>

#### `MtFootageData.GetDownsamplingFactor(self)` <a id="c4d.modules.motiontracker.MtFootageData.GetDownsamplingFactor"></a>

Retrieves the downsampling factor used for the footage.

**Return type:** float

**Returns:** The downsampling factor.

#### `MtFootageData.GetResolutionHeightPix(self, originalRes)` <a id="c4d.modules.motiontracker.MtFootageData.GetResolutionHeightPix"></a>

Retrieves the height in pixels of the footage.

**Parameters:**

**originalRes** (*int*) –

If **True**, returns the original resolution of the footage.  
If **False**, returns the downsampled resolution.

**Return type:** int

**Returns:** The height of footage in pixels.

#### `MtFootageData.GetResolutionWidthPix(self, originalRes)` <a id="c4d.modules.motiontracker.MtFootageData.GetResolutionWidthPix"></a>

Retrieves the width in pixels of the footage.

**Parameters:**

**originalRes** (*int*) –

If **True**, returns the original resolution of the footage.  
If **False**, returns the downsampled resolution.

**Return type:** int

**Returns:** The width of footage in pixels.
