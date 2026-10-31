<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.bitmaps/ColorProfile/index.html -->

# c4d.bitmaps.ColorProfile <a id="c4d-bitmaps-colorprofile"></a>

## *class* `c4d.bitmaps.ColorProfile` <a id="c4d.bitmaps.ColorProfile"></a>

Represents a Color Profile.

## Overview <a id="overview"></a>

- [`ColorProfile.GetDefaultLinearGray()`](#c4d.bitmaps.ColorProfile.GetDefaultLinearGray): Returns the default gray linear color.
- [`ColorProfile.GetDefaultLinearRGB()`](#c4d.bitmaps.ColorProfile.GetDefaultLinearRGB): Returns the default linear final.
- [`ColorProfile.GetDefaultSGray()`](#c4d.bitmaps.ColorProfile.GetDefaultSGray): Returns the default SGray linear color.
- [`ColorProfile.GetDefaultSRGB()`](#c4d.bitmaps.ColorProfile.GetDefaultSRGB): Returns the default SRGB final.

**Color Modes And Defaults**

- [`ColorProfile.CheckColorMode()`](#c4d.bitmaps.ColorProfile.CheckColorMode): Check the color mode of the color profile.

**File Operations**

- [`ColorProfile.OpenProfileFromFile()`](#c4d.bitmaps.ColorProfile.OpenProfileFromFile): Open a profile from a file.
- [`ColorProfile.WriteProfileToFile()`](#c4d.bitmaps.ColorProfile.WriteProfileToFile): Write a profile to a file

**Magic Methods**

- [`ColorProfile.__init__()`](#c4d.bitmaps.ColorProfile.__init__)

**Profile Metadata And State**

- [`ColorProfile.GetHashCode()`](#c4d.bitmaps.ColorProfile.GetHashCode): Gets the hash code of the color profile.
- [`ColorProfile.GetInfo()`](#c4d.bitmaps.ColorProfile.GetInfo): Returns the profile info.
- [`ColorProfile.HasProfile()`](#c4d.bitmaps.ColorProfile.HasProfile): Check if a profile is set.
- [`ColorProfile.IsMonitorProfileMode()`](#c4d.bitmaps.ColorProfile.IsMonitorProfileMode): Check if the current profile is the monitor profile.
- [`ColorProfile.SetMonitorProfileMode()`](#c4d.bitmaps.ColorProfile.SetMonitorProfileMode): Link this color profile to the monitor color profile.

## Static Methods <a id="static_methods"></a>

### Color Modes And Defaults <a id="c4d.bitmaps.ColorProfile-staticmethod-Color-Modes-And-Defaults"></a>

#### *static* `ColorProfile.GetDefaultLinearGray()` <a id="c4d.bitmaps.ColorProfile.GetDefaultLinearGray"></a>

Returns the default gray linear color.

**Return type:** [c4d.bitmaps.ColorProfile](#c4d.bitmaps.ColorProfile)

**Returns:** The profile.

#### *static* `ColorProfile.GetDefaultLinearRGB()` <a id="c4d.bitmaps.ColorProfile.GetDefaultLinearRGB"></a>

Returns the default linear final.

**Return type:** [c4d.bitmaps.ColorProfile](#c4d.bitmaps.ColorProfile)

**Returns:** The profile.

#### *static* `ColorProfile.GetDefaultSGray()` <a id="c4d.bitmaps.ColorProfile.GetDefaultSGray"></a>

Returns the default SGray linear color.

**Return type:** [c4d.bitmaps.ColorProfile](#c4d.bitmaps.ColorProfile)

**Returns:** The profile.

#### *static* `ColorProfile.GetDefaultSRGB()` <a id="c4d.bitmaps.ColorProfile.GetDefaultSRGB"></a>

Returns the default SRGB final.

**Return type:** [c4d.bitmaps.ColorProfile](#c4d.bitmaps.ColorProfile)

**Returns:** The profile.

## Methods <a id="methods"></a>

### Color Modes And Defaults <a id="c4d.bitmaps.ColorProfile-method-Color-Modes-And-Defaults"></a>

#### `ColorProfile.CheckColorMode(self, colormode)` <a id="c4d.bitmaps.ColorProfile.CheckColorMode"></a>

Check the color mode of the color profile.

**Parameters:**

**colormode** (*int*) –

The mode:

|   |   |
|---|---|
| *COLORMODE_ILLEGAL* | Illegal 8-bit mode. |
| *COLORMODE_ALPHA* | Only 8-bit alpha channel. |
| *COLORMODE_GRAY* | 8-bit grayscale channel. |
| *COLORMODE_AGRAY* | 8-bit grayscale channel with 8-bit alpha. |
| *COLORMODE_RGB* | 8-bit RGB channels. |
| *COLORMODE_ARGB* | 8-bit RGB channels with 8-bit alpha. |
| *COLORMODE_CMYK* | 8-bit CMYK channel. |
| *COLORMODE_ACMYK* | 8-bit CMYK channel with 8-bit alpha. |
| *COLORMODE_MASK* | 8-bit grayscale map as mask. |
| *COLORMODE_AMASK* | 8-bit grayscale map as mask with 8-bit alpha. |
| *COLORMODE_ILLEGALw* | Illegal 16-bit mode. |
| *COLORMODE_GRAYw* | 16-bit grayscale channel. |
| *COLORMODE_AGRAYw* | 16-bit grayscale channel with 16-bit alpha. |
| *COLORMODE_RGBw* | 16-bit RGB channels. |
| *COLORMODE_ARGBw* | 16-bit RGB channels with 16-bit alpha. |
| *COLORMODE_MASKw* | 16-bit grayscale map as mask with 16-bit alpha. |
| *COLORMODE_ILLEGALf* | Illegal 32-bit mode. |
| *COLORMODE_GRAYf* | 32-bit floating point grayscale channel. |
| *COLORMODE_AGRAYf* | 32-bit floating point grayscale channel with floating point alpha. |
| *COLORMODE_RGBf* | 32-bit floating point RGB channels. |
| *COLORMODE_ARGBf* | 32-bit floating point RGB channels with floating point alpha. |
| *COLORMODE_MASKf* | 32-bit floating point grayscale map as mask. |

**Return type:** bool

**Returns:** **True** if set, otherwise **False**.

### File Operations <a id="c4d.bitmaps.ColorProfile-method-File-Operations"></a>

#### `ColorProfile.OpenProfileFromFile(self, fn)` <a id="c4d.bitmaps.ColorProfile.OpenProfileFromFile"></a>

Open a profile from a file.

**Parameters:** **fn** (*Union*[*str*, [*c4d.storage.MemoryFileStruct*](../../c4d.storage/MemoryFileStruct/index.md#c4d.storage.MemoryFileStruct)]) – The file.

#### `ColorProfile.WriteProfileToFile(self, fn)` <a id="c4d.bitmaps.ColorProfile.WriteProfileToFile"></a>

Write a profile to a file

**Parameters:** **fn** (*Union*[*str*, [*c4d.storage.MemoryFileStruct*](../../c4d.storage/MemoryFileStruct/index.md#c4d.storage.MemoryFileStruct)]) – The file.

**Return type:** bool

**Returns:** Is **True** on success, otherwise **False**.

### Magic Methods <a id="c4d.bitmaps.ColorProfile-method-Magic-Methods"></a>

#### `ColorProfile.__init__(self)` <a id="c4d.bitmaps.ColorProfile.__init__"></a>

### Profile Metadata And State <a id="c4d.bitmaps.ColorProfile-method-Profile-Metadata-And-State"></a>

#### `ColorProfile.GetHashCode(self)` <a id="c4d.bitmaps.ColorProfile.GetHashCode"></a>

Gets the hash code of the color profile.

*New in version 2025.2.0.*

**Returns:** The hash code of the color profile.

**Return type:** int

#### `ColorProfile.GetInfo(self)` <a id="c4d.bitmaps.ColorProfile.GetInfo"></a>

Returns the profile info.

**Return type:** str

**Returns:** The profile info

#### `ColorProfile.HasProfile(self)` <a id="c4d.bitmaps.ColorProfile.HasProfile"></a>

Check if a profile is set.

**Return type:** bool

**Returns:** **True** on success, otherwise **False**.

#### `ColorProfile.IsMonitorProfileMode(self)` <a id="c4d.bitmaps.ColorProfile.IsMonitorProfileMode"></a>

Check if the current profile is the monitor profile.

**Return type:** bool

**Returns:** **True** if the monitor profile is set, otherwise **False**.

#### `ColorProfile.SetMonitorProfileMode(self, on)` <a id="c4d.bitmaps.ColorProfile.SetMonitorProfileMode"></a>

Link this color profile to the monitor color profile.

**Parameters:** **on** (*bool*) – Set **True** to link the color profile to the monitor profile.

**Return type:** bool

**Returns:** **True** if set, otherwise **False**.
