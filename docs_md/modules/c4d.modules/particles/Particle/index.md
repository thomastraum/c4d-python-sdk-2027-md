<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/particles/Particle/index.html -->

# c4d.modules.particles.Particle <a id="c4d-modules-particles-particle"></a>

## *class* `c4d.modules.particles.Particle` <a id="c4d.modules.particles.Particle"></a>

The information for each particle detailing its located, movement and life.

**Attributes**

## `c4d.modules.particles.Particle.off` <a id="c4d.modules.particles.Particle.off"></a>

The current position of the particle.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.particles.Particle.v1` <a id="c4d.modules.particles.Particle.v1"></a>

This vector is usually calculated by Cinema 4D when using the Tangential option in the particle emitter. The vectors `v1` and `v3` are used to form the axes to align the direction in which the objects attached to the particles are aligned.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.particles.Particle.v3` <a id="c4d.modules.particles.Particle.v3"></a>

The current velocity of the particle (speed and direction).

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

> **See also:** [`CalcParticleMatrix()`](../index.md#c4d.modules.particles.CalcParticleMatrix)

## `c4d.modules.particles.Particle.t` <a id="c4d.modules.particles.Particle.t"></a>

The current time from the particles birth, this is the age of the particle.

**Type:** float

## `c4d.modules.particles.Particle.bits` <a id="c4d.modules.particles.Particle.bits"></a>

The flags for the particles state:

|   |   |
|---|---|
| *PARTICLEFLAGS_NONE* | None. |
| *PARTICLEFLAGS_VISIBLE* | Particle is visible. |
| *PARTICLEFLAGS_ALIVE* | Particle is alive. |
