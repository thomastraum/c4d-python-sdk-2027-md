<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/particles/BaseParticle/index.html -->

# c4d.modules.particles.BaseParticle <a id="c4d-modules-particles-baseparticle"></a>

## *class* `c4d.modules.particles.BaseParticle` <a id="c4d.modules.particles.BaseParticle"></a>

Used to change the particle path by the particle modifiers.

**Attributes**

## `c4d.modules.particles.BaseParticle.v` <a id="c4d.modules.particles.BaseParticle.v"></a>

The velocity sum of the modifications to the particle, the current velocity of the particle is found from [`Particle`](../Particle/index.md#c4d.modules.particles.Particle). The new velocity is found using this velocity sum and dividing by the sum `count`.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.particles.BaseParticle.count` <a id="c4d.modules.particles.BaseParticle.count"></a>

This is the sum count of the velocities added to the velocity vector `v`.

**Type:** int
