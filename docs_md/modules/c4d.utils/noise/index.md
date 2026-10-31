<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.utils/noise/index.html -->

# c4d.utils.noise <a id="c4d-utils-noise"></a>

## *class* `c4d.utils.noise` <a id="c4d.utils.noise"></a>

- [c4d.utils.noise.C4DNoise](C4DNoise/index.md)

## Overview <a id="overview"></a>

**Noise Generation**

- [`c4d.utils.noise.Noise()`](#c4d.utils.noise.Noise): Generates a noise value.
- [`c4d.utils.noise.PNoise()`](#c4d.utils.noise.PNoise): Generates a periodical noise value.
- [`c4d.utils.noise.SNoise()`](#c4d.utils.noise.SNoise): Generates a signed noise value.

**Turbulence**

- [`c4d.utils.noise.Turbulence()`](#c4d.utils.noise.Turbulence): Generates a turbulence value, this is a sum of multiple noises with different frequency.
- [`c4d.utils.noise.WavyTurbulence()`](#c4d.utils.noise.WavyTurbulence): Generates a wavy turbulence value, this is a sum of multiple noises with different frequency.

## Members <a id="members"></a>

### Noise Generation <a id="c4d.utils.noise-function-Noise-Generation"></a>

#### `c4d.utils.noise.Noise(p, t=0.0)` <a id="c4d.utils.noise.Noise"></a>

Generates a noise value.

**Parameters:**

- **p** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The noise coordinate.
- **t** (*float*) – The time.

**Return type:** float

**Returns:** The noise value, between *0.0* and *1.0*.

#### `c4d.utils.noise.PNoise(p, d, dt, t=0.0)` <a id="c4d.utils.noise.PNoise"></a>

Generates a periodical noise value.

[`PNoise()`](#c4d.utils.noise.PNoise) is based on [`SNoise()`](#c4d.utils.noise.SNoise):

> ```python
> import c4d
>
> NOISERES = 1024
> pnoise = c4d.utils.noise.SNoise(c4d.Vector(p.x * NOISERES / d.x, p.y * NOISERES / d.y, p.z * NOISERES / d.z))
> ```

**Parameters:**

- **p** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The noise coordinate.
- **d** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The period.
- **dt** (*float*) – The time period.
- **t** (*float*) – The time.

**Return type:** float

**Returns:** The periodical noise value.

#### `c4d.utils.noise.SNoise(p, t=0.0)` <a id="c4d.utils.noise.SNoise"></a>

Generates a signed noise value.

**Parameters:**

- **p** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The noise coordinate.
- **t** (*float*) – The time.

**Return type:** float

**Returns:** The signed noise value, this is between *-1.0* and *1.0*.

### Turbulence <a id="c4d.utils.noise-function-Turbulence"></a>

#### `c4d.utils.noise.Turbulence(p, oct, abs, t=0.0)` <a id="c4d.utils.noise.Turbulence"></a>

Generates a turbulence value, this is a sum of multiple noises with different frequency.

**Parameters:**

- **p** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The turbulence coordinate.
- **oct** (*int*) – The number of octaves.
- **abs** (*bool*) – **True** for the absolute value.
- **t** (*int*) – The time.

**Return type:** float

**Returns:** The turbulence value, between *-1.0* and *1.0* unless *abs* is true, in which case it will be between *0.0* to *1.0*.

#### `c4d.utils.noise.WavyTurbulence(p, t, oct, start)` <a id="c4d.utils.noise.WavyTurbulence"></a>

Generates a wavy turbulence value, this is a sum of multiple noises with different frequency.

**Parameters:**

- **p** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The turbulence coordinate.
- **t** (*float*) – The time.
- **oct** (*int*) – The number of octaves.
- **start** (*int*) – The start value.

**Return type:** float

**Returns:** Turbulence value, this is between *-1.0* and *1.0*.
