<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/colorchooser/index.html -->

# c4d.modules.colorchooser <a id="c4d-modules-colorchooser"></a>

## *class* `c4d.modules.colorchooser` <a id="c4d.modules.colorchooser"></a>

*New in version R18.011.*

- [`c4d.modules.colorchooser.ColorSwatchData`](ColorSwatchData/index.md#c4d.modules.colorchooser.ColorSwatchData)
- [`c4d.modules.colorchooser.ColorSwatchGroup`](ColorSwatchGroup/index.md#c4d.modules.colorchooser.ColorSwatchGroup)

## Overview <a id="overview"></a>

**Color Bit Depth Conversion**

- [`c4d.modules.colorchooser.Color16BitToFloat()`](#c4d.modules.colorchooser.Color16BitToFloat): Converts a RGB 16-bit color (range [0, 65535]) to float color in range [0.0, 1.0].
- [`c4d.modules.colorchooser.Color8BitToFloat()`](#c4d.modules.colorchooser.Color8BitToFloat): Converts a RGB 8-bit color (range [0, 255]) to float color in range [0.0, 1.0].
- [`c4d.modules.colorchooser.ColorFloatTo16Bit()`](#c4d.modules.colorchooser.ColorFloatTo16Bit): Converts a RGB float color in range [0.0, 1.0] to 16-bit color (range [0, 65535]).
- [`c4d.modules.colorchooser.ColorFloatTo8Bit()`](#c4d.modules.colorchooser.ColorFloatTo8Bit): Converts a RGB float color in range [0.0, 1.0] to 8-bit color (range [0, 255]).

**Color Conversion**

- [`c4d.modules.colorchooser.ColorHSVToString()`](#c4d.modules.colorchooser.ColorHSVToString): Converts a HSV *color* to string based on the color range defined in Cinema 4D preferences (See *WPREF_COLOR_RGBRANGE*).
- [`c4d.modules.colorchooser.ColorKelvinTemperatureToRGB()`](#c4d.modules.colorchooser.ColorKelvinTemperatureToRGB): Converts color Kelvin temperature to RGB value.
- [`c4d.modules.colorchooser.ColorRGBToString()`](#c4d.modules.colorchooser.ColorRGBToString): Converts a RGB *color* to string based on the color range defined in Cinema 4D preferences (See *WPREF_COLOR_RGBRANGE*).

**Component Bit Depth Conversion**

- [`c4d.modules.colorchooser.ColorComponent16BitToFloat()`](#c4d.modules.colorchooser.ColorComponent16BitToFloat): Converts a RGB 16-bit color component (range [0, 65535]) to float in range [0.0, 1.0].
- [`c4d.modules.colorchooser.ColorComponent8BitToFloat()`](#c4d.modules.colorchooser.ColorComponent8BitToFloat): Converts a RGB 8-bit color component (range [0, 255]) to float in range [0.0, 1.0].
- [`c4d.modules.colorchooser.ColorComponentFloatTo16Bit()`](#c4d.modules.colorchooser.ColorComponentFloatTo16Bit): Converts a RGB float color component in range [0.0, 1.0] to 16-bit (range [0, 65535]).
- [`c4d.modules.colorchooser.ColorComponentFloatTo8Bit()`](#c4d.modules.colorchooser.ColorComponentFloatTo8Bit): Converts a RGB float color component in range [0.0, 1.0] to 8-bit (range [0, 255]).

**Harmony Palette Generation**

- [`c4d.modules.colorchooser.ColorHarmonyGetAnalogous()`](#c4d.modules.colorchooser.ColorHarmonyGetAnalogous): Generates an Analogous Color Harmony palette.
- [`c4d.modules.colorchooser.ColorHarmonyGetComplementary()`](#c4d.modules.colorchooser.ColorHarmonyGetComplementary): Generates a complementary color harmony palette from *color*. Contains the input color and its opposite color in a color wheel.
- [`c4d.modules.colorchooser.ColorHarmonyGetEquiangular()`](#c4d.modules.colorchooser.ColorHarmonyGetEquiangular): Generates an Equiangular Color Harmony palette.
- [`c4d.modules.colorchooser.ColorHarmonyGetSplitComplementary()`](#c4d.modules.colorchooser.ColorHarmonyGetSplitComplementary): Generates a split complementary color harmony palette from *color*. Contains the input color and the 2 analogous colors to its complementary color.
- [`c4d.modules.colorchooser.ColorHarmonyGetTetradic()`](#c4d.modules.colorchooser.ColorHarmonyGetTetradic): Generates a tetradric color harmony palette.
- [`c4d.modules.colorchooser.ColorHarmonyInterpolateColors()`](#c4d.modules.colorchooser.ColorHarmonyInterpolateColors): Generates a palette composed by a defined amount of colors interpolated between *color1* and *color2* in HSV color space.
- [`c4d.modules.colorchooser.ColorHarmonyRotateColor()`](#c4d.modules.colorchooser.ColorHarmonyRotateColor): Generates a palette composed by a defined amount of colors whose hue is separated by a defined angle in HSV color space.

## Members <a id="members"></a>

### Color Bit Depth Conversion <a id="c4d.modules.colorchooser-function-Color-Bit-Depth-Conversion"></a>

#### `c4d.modules.colorchooser.Color16BitToFloat(red, green, blue)` <a id="c4d.modules.colorchooser.Color16BitToFloat"></a>

Converts a RGB 16-bit color (range [0, 65535]) to float color in range [0.0, 1.0].

**Parameters:**

- **red** (*int*) – The 16-bit color component to be converted. Must be in range [0, 65535].
- **green** (*int*) – The 16-bit color component to be converted. Must be in range [0, 65535].
- **blue** (*int*) – The 16-bit color component to be converted. Must be in range [0, 65535].

**Return type:** [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The converted float color in range [0.0, 1.0].

#### `c4d.modules.colorchooser.Color8BitToFloat(red, green, blue)` <a id="c4d.modules.colorchooser.Color8BitToFloat"></a>

Converts a RGB 8-bit color (range [0, 255]) to float color in range [0.0, 1.0].

**Parameters:**

- **red** (*int*) – The 8-bit color component to be converted. Must be in range [0, 255].
- **green** (*int*) – The 8-bit color component to be converted. Must be in range [0, 255].
- **blue** (*int*) – The 8-bit color component to be converted. Must be in range [0, 255].

**Return type:** [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The converted float color in range [0.0, 1.0].

#### `c4d.modules.colorchooser.ColorFloatTo16Bit(floatColor)` <a id="c4d.modules.colorchooser.ColorFloatTo16Bit"></a>

Converts a RGB float color in range [0.0, 1.0] to 16-bit color (range [0, 65535]).

**Parameters:** **floatColor** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The color to be converted. Must be in range [0.0, 1.0].

**Return type:** List[int, int, int]

**Returns:** The converted 16-bit red, green and blue color components.

#### `c4d.modules.colorchooser.ColorFloatTo8Bit(floatColor)` <a id="c4d.modules.colorchooser.ColorFloatTo8Bit"></a>

Converts a RGB float color in range [0.0, 1.0] to 8-bit color (range [0, 255]).

**Parameters:** **floatColor** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The color to be converted. Must be in range [0.0, 1.0].

**Return type:** List[int, int, int]

**Returns:** The converted 8-bit red, green and blue color components.

### Color Conversion <a id="c4d.modules.colorchooser-function-Color-Conversion"></a>

#### `c4d.modules.colorchooser.ColorHSVToString(color)` <a id="c4d.modules.colorchooser.ColorHSVToString"></a>

Converts a HSV *color* to string based on the color range defined in Cinema 4D preferences (See *WPREF_COLOR_RGBRANGE*).  
Example: The string result for the color *Vector(0.45, 0.32, 1.0)* will be “251.471 deg , 68 %, 100 %”.

**Parameters:** **color** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The HSV color to convert to string. Its components must be in range [0.0, 1.0]. See [`RGBToHSV()`](../../c4d.utils/index.md#c4d.utils.RGBToHSV) / [`HSVToRGB()`](../../c4d.utils/index.md#c4d.utils.HSVToRGB).

**Return type:** str

**Returns:** The string representation of the color.

#### `c4d.modules.colorchooser.ColorKelvinTemperatureToRGB(kelvinDegree, tint=0.0)` <a id="c4d.modules.colorchooser.ColorKelvinTemperatureToRGB"></a>

Converts color Kelvin temperature to RGB value.

**Parameters:**

- **kelvinDegree** (*float*) – The Kelvin temperature value in Kelvin degrees. Useful range: [1000.0, 10000.0] deg K
- **tint** (*float*) – Offsets the color temperature from green (negative value) to magenta (positive value). Set to 0.0 to disable tinting. Value will be clamped to range [-1.0, 1.0].

**Return type:** [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The converted RGB color value.

#### `c4d.modules.colorchooser.ColorRGBToString(color)` <a id="c4d.modules.colorchooser.ColorRGBToString"></a>

Converts a RGB *color* to string based on the color range defined in Cinema 4D preferences (See *WPREF_COLOR_RGBRANGE*).  
Example: The string result for the color *Vector(0.45, 0.32, 1.0)* will be “115, 82, 255” if *WPREF_COLOR_RGBRANGE* is configured to *COLORSYSTEM_RANGE_255*.

**Parameters:** **color** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The RGB color to convert to string. Its components must be in range [0.0, 1.0].

**Return type:** str

**Returns:** The string representation of the color.

### Component Bit Depth Conversion <a id="c4d.modules.colorchooser-function-Component-Bit-Depth-Conversion"></a>

#### `c4d.modules.colorchooser.ColorComponent16BitToFloat(colorComponentInput)` <a id="c4d.modules.colorchooser.ColorComponent16BitToFloat"></a>

Converts a RGB 16-bit color component (range [0, 65535]) to float in range [0.0, 1.0].

**Parameters:** **colorComponentInput** (*int*) – The 16-bit color component to be converted. Must be in range [0, 65535].

**Return type:** float

**Returns:** The converted color component in range [0.0, 1.0].

#### `c4d.modules.colorchooser.ColorComponent8BitToFloat(colorComponentInput)` <a id="c4d.modules.colorchooser.ColorComponent8BitToFloat"></a>

Converts a RGB 8-bit color component (range [0, 255]) to float in range [0.0, 1.0].

**Parameters:** **colorComponentInput** (*int*) – The 8-bit color component to be converted. Must be in range [0, 255].

**Return type:** float

**Returns:** The converted color component in range [0.0, 1.0].

#### `c4d.modules.colorchooser.ColorComponentFloatTo16Bit(colorComponentInput)` <a id="c4d.modules.colorchooser.ColorComponentFloatTo16Bit"></a>

Converts a RGB float color component in range [0.0, 1.0] to 16-bit (range [0, 65535]).

**Parameters:** **colorComponentInput** (*float*) – The color component to be converted. Must be in range [0.0, 1.0].

**Return type:** int

**Returns:** The converted 16-bit color component in range [0, 65535].

#### `c4d.modules.colorchooser.ColorComponentFloatTo8Bit(colorComponentInput)` <a id="c4d.modules.colorchooser.ColorComponentFloatTo8Bit"></a>

Converts a RGB float color component in range [0.0, 1.0] to 8-bit (range [0, 255]).

**Parameters:** **colorComponentInput** (*float*) – The color component to be converted. Must be in range [0.0, 1.0].

**Return type:** int

**Returns:** The converted 8-bit color component in range [0, 255].

### Harmony Palette Generation <a id="c4d.modules.colorchooser-function-Harmony-Palette-Generation"></a>

#### `c4d.modules.colorchooser.ColorHarmonyGetAnalogous(color, colorCount, ryb)` <a id="c4d.modules.colorchooser.ColorHarmonyGetAnalogous"></a>

Generates an Analogous Color Harmony palette. Analogous color schemes use colors that are next to each other on the color wheel, i.e. 30 deg far away.

**Parameters:**

- **color** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The color to generate the palette. This color will be added to the resulting palette as well, and converted to RYB space if enabled.

- **colorCount** (*int*) – Number of colors to generate. Because input color is added as well, the resulting palette will have *colorCount* + 1 colors.

- **ryb** (*bool*) –

  Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.  
  RYB generates visually nicer palettes, but is less accurate and smaller than RGB space.  
  This means different RGB values could be converted to the same RYB value.

**Return type:** List[[c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The analogous color harmony palette.

#### `c4d.modules.colorchooser.ColorHarmonyGetComplementary(color, ryb)` <a id="c4d.modules.colorchooser.ColorHarmonyGetComplementary"></a>

Generates a complementary color harmony palette from *color*. Contains the input color and its opposite color in a color wheel.

**Parameters:**

- **color** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The color to generate the palette. This color will be added to the resulting palette as well, and converted to RYB space if enabled.

- **ryb** (*bool*) –

  Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.  
  RYB generates visually nicer palettes, but is less accurate because it is smaller than RGB space.  
  This means different RGB values could be converted to the same RYB value.

**Return type:** List[[c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The complementary color harmony palette.

#### `c4d.modules.colorchooser.ColorHarmonyGetEquiangular(color, colorCount, ryb)` <a id="c4d.modules.colorchooser.ColorHarmonyGetEquiangular"></a>

Generates an Equiangular Color Harmony palette. All colors are evenly arranged around the color wheel.

**Parameters:**

- **color** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The color to generate the palette. This color will be added to the resulting palette as well, and converted to RYB space if enabled.

- **colorCount** (*int*) – Number of colors to generate. Because input color is added as well, the resulting palette will have *colorCount* + 1 colors.

- **ryb** (*bool*) –

  Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.  
  RYB generates visually nicer palettes, but is less accurate because it is smaller than RGB space.  
  This means different RGB values could be converted to the same RYB value.

**Return type:** List[[c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The equiangular color harmony palette.

#### `c4d.modules.colorchooser.ColorHarmonyGetSplitComplementary(color, ryb)` <a id="c4d.modules.colorchooser.ColorHarmonyGetSplitComplementary"></a>

Generates a split complementary color harmony palette from *color*. Contains the input color and the 2 analogous colors to its complementary color.  
The complementary color is calculated rotating 180 deg the hue of the original color in HSV space.

**Parameters:**

- **color** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The color to generate the palette. This color will be added to the resulting palette as well, and converted to RYB space if enabled.

- **ryb** (*bool*) –

  Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.  
  RYB generates visually nicer palettes, but is less accurate because it is smaller than RGB space.  
  This means different RGB values could be converted to the same RYB value.

**Return type:** List[[c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The split complementary color harmony palette.

#### `c4d.modules.colorchooser.ColorHarmonyGetTetradic(color, ryb)` <a id="c4d.modules.colorchooser.ColorHarmonyGetTetradic"></a>

Generates a tetradric color harmony palette. The rectangle or Tetradic color scheme uses four colors arranged into 2 complementary pairs.

**Parameters:**

- **color** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The color to generate the palette. This color will be added to the resulting palette as well, and converted to RYB space if enabled.

- **ryb** (*bool*) –

  Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.  
  RYB generates visually nicer palettes, but is less accurate because it is smaller than RGB space.  
  This means different RGB values could be converted to the same RYB value.

**Return type:** List[[c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The tetradric color harmony palette.

#### `c4d.modules.colorchooser.ColorHarmonyInterpolateColors(color1, color2, colorCount, ryb)` <a id="c4d.modules.colorchooser.ColorHarmonyInterpolateColors"></a>

Generates a palette composed by a defined amount of colors interpolated between *color1* and *color2* in HSV color space. All 3 HSV values will be interpolated.

**Parameters:**

- **color1** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The first generator color. This color will be added to the resulting palette as well, and converted to RYB space if enabled.

- **color2** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The second generator color. This color will be added to the resulting palette as well, and converted to RYB space if enabled.

- **colorCount** (*int*) – Number of colors to generate. Because the 2 input colors are added as well, the resulting palette will have *colorCount* + 2 colors.

- **ryb** (*bool*) –

  Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.  
  RYB generates visually nicer palettes, but is less accurate because it is smaller than RGB space.  
  This means different RGB values could be converted to the same RYB value.

**Return type:** List[[c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The palette.

#### `c4d.modules.colorchooser.ColorHarmonyRotateColor(color, colorCount, angle, ryb)` <a id="c4d.modules.colorchooser.ColorHarmonyRotateColor"></a>

Generates a palette composed by a defined amount of colors whose hue is separated by a defined angle in HSV color space.

**Parameters:**

- **color** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The color to generate the palette. This color will be added to the resulting palette as well, and converted to RYB space if enabled.

- **colorCount** (*int*) – Number of colors to generate. Because input color is added as well, the resulting palette will have *colorCount* + 1 colors.

- **angle** (*int*) – Rotation angle in radians. See [`c4d.utils.Deg()`](../../c4d.utils/index.md#c4d.utils.Deg)

- **ryb** (*bool*) –

  Set to **True** to use RYB (red-yellow-blue) HSV space, set to **False** to use RGB (red-green-blue) HSV space.  
  RYB generates visually nicer palettes, but is less accurate because it is smaller than RGB space.  
  This means different RGB values could be converted to the same RYB value.

**Return type:** List[[c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The palette.
