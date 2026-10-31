<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.utils/noise/C4DNoise/index.html -->

# c4d.utils.noise.C4DNoise <a id="c4d-utils-noise-c4dnoise"></a>

## *class* `c4d.utils.noise.C4DNoise` <a id="c4d.utils.noise.C4DNoise"></a>

An important technique for generating procedural textures is the use of fractal noise.

> **See also:** [Noise Types](../../../../types/noise.md).

## Overview <a id="overview"></a>

**Noise Setup**

- [`C4DNoise.CreateMenuContainer()`](#c4d.utils.noise.C4DNoise.CreateMenuContainer): Creates a menu container with the different noise options available:
- [`C4DNoise.EvaluateSampleOffset()`](#c4d.utils.noise.C4DNoise.EvaluateSampleOffset): Evaluates the sample offset.

**Parameter Support**

- [`C4DNoise.HasAbsolute()`](#c4d.utils.noise.C4DNoise.HasAbsolute): Checks if a certain noise type supports the absolute parameter.
- [`C4DNoise.HasCycles()`](#c4d.utils.noise.C4DNoise.HasCycles): Checks if a certain noise type supports the cycles parameter.
- [`C4DNoise.HasOctaves()`](#c4d.utils.noise.C4DNoise.HasOctaves): Checks if a certain noise type supports the octaves parameter.

**Magic Methods**

- [`C4DNoise.__init__()`](#c4d.utils.noise.C4DNoise.__init__)

**Noise Generation**

- [`C4DNoise.Fbm()`](#c4d.utils.noise.C4DNoise.Fbm): Generate a periodic Fractional Brownian Motion value.
- [`C4DNoise.Noise()`](#c4d.utils.noise.C4DNoise.Noise): Samples a 2D or 3D noise.
- [`C4DNoise.RidgedMultifractal()`](#c4d.utils.noise.C4DNoise.RidgedMultifractal): Generate a periodic fractal function used for such things as landscapes or mountain ranges.
- [`C4DNoise.SNoise()`](#c4d.utils.noise.C4DNoise.SNoise): Generate a periodic signed noise value.
- [`C4DNoise.Turbulence()`](#c4d.utils.noise.C4DNoise.Turbulence): Generate a turbulence value, this is a sum of multiple noises with different frequency.

**Noise Setup**

- [`C4DNoise.InitFbm()`](#c4d.utils.noise.C4DNoise.InitFbm): Initializes fractal brownian motion.

## Members <a id="members"></a>

### Noise Setup <a id="c4d.utils.noise.C4DNoise-staticmethod-Noise-Setup"></a>

#### *static* `C4DNoise.CreateMenuContainer(bIncludeNone=False)` <a id="c4d.utils.noise.C4DNoise.CreateMenuContainer"></a>

Creates a menu container with the different noise options available:

```python
import c4d

bc = c4d.utils.noise.C4DNoise.CreateMenuContainer(False)
for index, name in bc:
    print index, name
```

**Parameters:** **bIncludeNone** (*bool*) – Include the none option.

**Return type:** [c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** Generated noise menu.

#### *static* `C4DNoise.EvaluateSampleOffset(type, rOctaves, rDelta)` <a id="c4d.utils.noise.C4DNoise.EvaluateSampleOffset"></a>

Evaluates the sample offset.

**Parameters:**

- **type** (*int*) – Noise type.
- **rOctaves** (*float*) – Number of octaves.
- **rDelta** (*float*) – Delta.

**Return type:** float

**Returns:** The sample offset.

### Parameter Support <a id="c4d.utils.noise.C4DNoise-staticmethod-Parameter-Support"></a>

#### *static* `C4DNoise.HasAbsolute(t)` <a id="c4d.utils.noise.C4DNoise.HasAbsolute"></a>

Checks if a certain noise type supports the absolute parameter.

**Parameters:** **t** (*int*) – Noise type.

**Return type:** bool

**Returns:** **True** if absolute is supported, otherwise **False**.

#### *static* `C4DNoise.HasCycles(t)` <a id="c4d.utils.noise.C4DNoise.HasCycles"></a>

Checks if a certain noise type supports the cycles parameter.

**Parameters:** **t** (*int*) – Noise type.

**Return type:** bool

**Returns:** **True** if cycles is supported, otherwise **False**.

#### *static* `C4DNoise.HasOctaves(t)` <a id="c4d.utils.noise.C4DNoise.HasOctaves"></a>

Checks if a certain noise type supports the octaves parameter.

**Parameters:** **t** (*int*) – Noise type.

**Return type:** bool

**Returns:** **True** if octaves is supported, otherwise **False**.

### Magic Methods <a id="c4d.utils.noise.C4DNoise-method-Magic-Methods"></a>

#### `C4DNoise.__init__(self, seed=665)` <a id="c4d.utils.noise.C4DNoise.__init__"></a>

**Parameters:** **seed** (*int*) – Noise seed.

### Noise Generation <a id="c4d.utils.noise.C4DNoise-method-Noise-Generation"></a>

#### `C4DNoise.Fbm(self, p, rOctaves, lRepeat, t=0.0)` <a id="c4d.utils.noise.C4DNoise.Fbm"></a>

Generate a periodic Fractional Brownian Motion value.

> **Note:** Needs the call [`InitFbm()`](#c4d.utils.noise.C4DNoise.InitFbm) before.
>
> > **Warning:** The *rOctaves* value must not exceed the value passed to [`InitFbm()`](#c4d.utils.noise.C4DNoise.InitFbm) but can be lower.

**Parameters:**

- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The evaluation point.
- **rOctaves** (*float*) – The octaves
- **lRepeat** (*int*) – Must be *2^x - 1*, where x = [1..10], i.e. one of 1, 3, 7, 15, 31, 63, 127, 255, 511, and 1023. A noise repeats itself in time every 1024 units. Using a smaller repeat the noise will repeat at an earlier time.
- **t** (*float*) – The time

**Return type:** float

**Returns:** The fbm value.

#### `C4DNoise.Noise(self, t, two_d, p, time=0.0, octaves=4.0, absolute=False, sampleRad=0.25, detailAtt=0.25, t_repeat=0)` <a id="c4d.utils.noise.C4DNoise.Noise"></a>

Samples a 2D or 3D noise.

**Parameters:**

- **t** (*int*) –

  The noise **Type:** [Noise Types](../../../../types/noise.md)

  > **Note:** Please use [`InitFbm()`](#c4d.utils.noise.C4DNoise.InitFbm) before you use one of the following noise types: NOISE_ZADA, NOISE_DISPL_VORONOI, NOISE_OBER, NOISE_FBM, NOISE_BUYA.

- **two_d** (*bool*) – **True** for 2D Sampling, **False** for 3D Sampling

- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – Noise coordinate.

- **time** (*float*) – Time.

- **octaves** (*float*) – Octaves, if supported. See [`HasOctaves()`](#c4d.utils.noise.C4DNoise.HasOctaves)

- **absolute** (*bool*) – Absolute value, if supported. See [`HasAbsolute()`](#c4d.utils.noise.C4DNoise.HasAbsolute)

- **sampleRad** (*float*) – Sample radius.

- **detailAtt** (*float*) – Detail attenuation.

- **t_repeat** (*int*) – Must be *2^x - 1*, where x = [1..10], i.e. one of 1, 3, 7, 15, 31, 63, 127, 255, 511, and 1023. A noise repeats itself in time every 1024 units. Using a smaller repeat the noise will repeat at an earlier time.

**Return type:** float

**Returns:** Noise sample.

#### `C4DNoise.RidgedMultifractal(self, p, rOctaves, rOffset, rGain, lRepeat, t=0)` <a id="c4d.utils.noise.C4DNoise.RidgedMultifractal"></a>

Generate a periodic fractal function used for such things as landscapes or mountain ranges.

> > **Note:** Needs the call [`InitFbm()`](#c4d.utils.noise.C4DNoise.InitFbm) before.
>
> > **Warning:** The *rOctaves* value must not exceed the value passed to [`InitFbm()`](#c4d.utils.noise.C4DNoise.InitFbm) but can be lower.

**Parameters:**

- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The evaluation point.
- **rOctaves** (*float*) – The octave.
- **rOffset** (*float*) – The zero offset, this controls the multifractality.
- **rGain** (*float*) – The amplification of the fractal value.
- **lRepeat** (*float*) – Must be *2^x - 1*, where x = [1..10], i.e. one of 1, 3, 7, 15, 31, 63, 127, 255, 511, and 1023. A noise repeats itself in time every 1024 units. Using a smaller lrepeat the noise will repeat at an earlier time.
- **t** (*float*) – The time.

**Return type:** float

**Returns:** The fractal value.

#### `C4DNoise.SNoise(self, p, lRepeat, t=0.0)` <a id="c4d.utils.noise.C4DNoise.SNoise"></a>

Generate a periodic signed noise value.

**Parameters:**

- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – Noise coordinate.
- **lRepeat** (*int*) – Must be *2^x - 1*, where x = [1..10], i.e. one of 1, 3, 7, 15, 31, 63, 127, 255, 511, and 1023. A noise repeats itself in time every 1024 units. Using a smaller *lRepeat* the noise will repeat at an earlier time.
- **t** (*float*) – The time.

**Return type:** float

**Returns:** Signed noise value, this is between -1.0 and 1.0.

#### `C4DNoise.Turbulence(self, p, rOctaves, bAsolute, lRepeat, t=0.0)` <a id="c4d.utils.noise.C4DNoise.Turbulence"></a>

Generate a turbulence value, this is a sum of multiple noises with different frequency.

**Parameters:**

- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – Turbulence coordinate
- **rOctaves** (*float*) – The number of octaves.
- **bAbsolute** (*bool*) – **True** for absolute values.
- **lRepeat** (*int*) – Must be *2^x - 1*, where x = [1..10], i.e. one of 1, 3, 7, 15, 31, 63, 127, 255, 511, and 1023. A noise repeats itself in time every 1024 units. Using a smaller *lRepeat* the noise will repeat at an earlier time.
- **t** (*float*) – The time.

**Return type:** float

**Returns:** Noise sample.

### Noise Setup <a id="c4d.utils.noise.C4DNoise-method-Noise-Setup"></a>

#### `C4DNoise.InitFbm(self, lMaxOctaves, rLacunarity, h)` <a id="c4d.utils.noise.C4DNoise.InitFbm"></a>

Initializes fractal brownian motion.

**Parameters:**

- **lMaxOctaves** (*int*) – The maximum octave.
- **rLacunarity** (*float*) – This parameter controls the scale of each successive fractal overlay.
- **h** (*float*) – H-Parameter

**Return type:** bool

**Returns:** Initializes fractal brownian motion
