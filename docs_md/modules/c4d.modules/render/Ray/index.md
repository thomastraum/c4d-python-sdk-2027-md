<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/render/Ray/index.html -->

# c4d.modules.render.Ray <a id="c4d-modules-render-ray"></a>

## *class* `c4d.modules.render.Ray` <a id="c4d.modules.render.Ray"></a>

**Attributes**

## `c4d.modules.render.Ray.p` <a id="c4d.modules.render.Ray.p"></a>

The rays position.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.Ray.v` <a id="c4d.modules.render.Ray.v"></a>

[Read-only]

The rays direction vector.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.Ray.ior` <a id="c4d.modules.render.Ray.ior"></a>

The current index of refraction.

**Type:** float

## `c4d.modules.render.Ray.pp` <a id="c4d.modules.render.Ray.pp"></a>

[Read-only]

3 additional ray points for MIP-Mapping.

**Type:** Tuple[c4d.Vector, c4d.Vector, c4d.Vector]

## `c4d.modules.render.Ray.vv` <a id="c4d.modules.render.Ray.vv"></a>

[Read-only]

3 additional ray vectors for MIP-Mapping.

**Type:** Tuple[c4d.Vector, c4d.Vector, c4d.Vector]

## `c4d.modules.render.Ray.transport` <a id="c4d.modules.render.Ray.transport"></a>

[Read-only]

The current ray intensity. A ray starts with intensity 1.0.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)
