<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/particles/index.html -->

# c4d.modules.particles <a id="c4d-modules-particles"></a>

## *class* `c4d.modules.particles` <a id="c4d.modules.particles"></a>

- [`c4d.modules.particles.BaseParticle`](BaseParticle/index.md#c4d.modules.particles.BaseParticle)
- [`c4d.modules.particles.Particle`](Particle/index.md#c4d.modules.particles.Particle)

## Overview <a id="overview"></a>

- [`c4d.modules.particles.CalcParticleMatrix()`](#c4d.modules.particles.CalcParticleMatrix): Calculate the particles matrix, this represents the position and direction of the particle as used when the objects are aligned with a particle using the emitter Tangential option.

## Members <a id="members"></a>

### Particle Transformations <a id="c4d.modules.particles-function-Particle-Transformations"></a>

#### `c4d.modules.particles.CalcParticleMatrix(cp)` <a id="c4d.modules.particles.CalcParticleMatrix"></a>

Calculate the particles matrix, this represents the position and direction of the particle as used when the objects are aligned with a particle using the emitter Tangential option.

**Parameters:** **cp** ([*c4d.modules.particles.Particle*](Particle/index.md#c4d.modules.particles.Particle)) – The particle you wish to get the matrix for.

**Return type:** [c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** Details of the particles position and rotation.
