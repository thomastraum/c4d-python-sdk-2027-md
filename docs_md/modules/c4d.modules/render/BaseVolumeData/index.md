<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/render/BaseVolumeData/index.html -->

# c4d.modules.render.BaseVolumeData <a id="c4d-modules-render-basevolumedata"></a>

## *class* `c4d.modules.render.BaseVolumeData` <a id="c4d.modules.render.BaseVolumeData"></a>

**Attributes**

## `c4d.modules.render.BaseVolumeData.version` <a id="c4d.modules.render.BaseVolumeData.version"></a>

[Read-only]

The version number of this class.

**Type:** int

## `c4d.modules.render.BaseVolumeData.fps` <a id="c4d.modules.render.BaseVolumeData.fps"></a>

[Read-only]

Frames per second.

**Type:** int

## `c4d.modules.render.BaseVolumeData.ambient` <a id="c4d.modules.render.BaseVolumeData.ambient"></a>

Global ambient component.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.time` <a id="c4d.modules.render.BaseVolumeData.time"></a>

Current time in seconds.

**Type:** float

## `c4d.modules.render.BaseVolumeData.col` <a id="c4d.modules.render.BaseVolumeData.col"></a>

Set the calculated color within *BaseMaterial.CalcSurface()* and *BaseMaterial.CalcVolumetric()*.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.trans` <a id="c4d.modules.render.BaseVolumeData.trans"></a>

Set the calculated transparency within *BaseMaterial.CalcSurface()*, *BaseMaterial.CalcTransparency()* and *CalcVolumetric()*.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.refl` <a id="c4d.modules.render.BaseVolumeData.refl"></a>

Set the calculated reflection within *BaseMaterial.CalcSurface()*.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.alpha` <a id="c4d.modules.render.BaseVolumeData.alpha"></a>

Set the calculated alpha within *BaseMaterial.CalcAlpha()*.

**Type:** float

## `c4d.modules.render.BaseVolumeData.tray` <a id="c4d.modules.render.BaseVolumeData.tray"></a>

Transmitted vector (can be modified in *BaseMaterial.ChangeNormal()*), only valid if shader sets *VOLUMEINFO_TRANSPARENCY* and only during *BaseMaterial.CalcSurface()*.

> **Note:** Can be **None**, always check.

**Type:** Optional[c4d.modules.render.Ray]

## `c4d.modules.render.BaseVolumeData.rray` <a id="c4d.modules.render.BaseVolumeData.rray"></a>

Reflected vector (can be modified in *BaseMaterial.ChangeNormal()*), only valid if shader sets *VOLUMEINFO_TRANSPARENCY* and only during *BaseMaterial.CalcSurface()*.

**Type:** [`Ray`](../Ray/index.md#c4d.modules.render.Ray)

## `c4d.modules.render.BaseVolumeData.p` <a id="c4d.modules.render.BaseVolumeData.p"></a>

The surface point, this can **only** be modified by *BaseMaterial.Displace()*.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.ray` <a id="c4d.modules.render.BaseVolumeData.ray"></a>

The current eye ray.

> **Note:** Is always valid.

**Type:** [`Ray`](../Ray/index.md#c4d.modules.render.Ray)

## `c4d.modules.render.BaseVolumeData.bumpn` <a id="c4d.modules.render.BaseVolumeData.bumpn"></a>

Surface phong and bump normal.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.orign` <a id="c4d.modules.render.BaseVolumeData.orign"></a>

The original surface normal.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.n` <a id="c4d.modules.render.BaseVolumeData.n"></a>

The surface phong normal.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.dispn` <a id="c4d.modules.render.BaseVolumeData.dispn"></a>

The suggested displacement direction.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.dist` <a id="c4d.modules.render.BaseVolumeData.dist"></a>

Distance between `p` and `Ray.p`, i.e. the ray length.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.cosc` <a id="c4d.modules.render.BaseVolumeData.cosc"></a>

The angle beween ray vector and unbumped normal.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.uvw` <a id="c4d.modules.render.BaseVolumeData.uvw"></a>

The surface uvw coordinates, this is invalid for volumetric shaders.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.delta` <a id="c4d.modules.render.BaseVolumeData.delta"></a>

This defines the radius for the area around ‘uvw’ that needs to be sampled.

> **Note:** If you ignore this value your shader will work, but produce aliasing artefacts.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.lhit` <a id="c4d.modules.render.BaseVolumeData.lhit"></a>

Surface identity.

**Type:** ptr

## `c4d.modules.render.BaseVolumeData.ddu` <a id="c4d.modules.render.BaseVolumeData.ddu"></a>

U direction vector perpendicular to `n`; can be used for bump mapping if *VOLUMEINFO_DUDVREQUIRED* is set.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.ddv` <a id="c4d.modules.render.BaseVolumeData.ddv"></a>

V direction vector perpendicular to `n`; can be used for bump mapping if *VOLUMEINFO_DUDVREQUIRED* is set.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.raydepth` <a id="c4d.modules.render.BaseVolumeData.raydepth"></a>

The depth of the actual ray.

**Type:** int

## `c4d.modules.render.BaseVolumeData.calc_trans` <a id="c4d.modules.render.BaseVolumeData.calc_trans"></a>

Specifies, if transparency will be rendered.

These values are:

> |   |   |
> |---|---|
> | *0* | No transparency. |
> | *1* | No refractions. |
> | *2* | Full calculation. |

## `c4d.modules.render.BaseVolumeData.calc_refl` <a id="c4d.modules.render.BaseVolumeData.calc_refl"></a>

Specifies, if reflections will be rendered.

These values are:

> |   |   |
> |---|---|
> | *0* | No reflection. |
> | *1* | Only sky/floor. |
> | *2* | Full calculation. |

## `c4d.modules.render.BaseVolumeData.calc_shadow` <a id="c4d.modules.render.BaseVolumeData.calc_shadow"></a>

Specifies, if shadows will be rendered.

**Type:** bool

## `c4d.modules.render.BaseVolumeData.calc_illum` <a id="c4d.modules.render.BaseVolumeData.calc_illum"></a>

Specifies, if illumination will be rendered. If this value is ‘0’ then *BaseMaterial.CalcSurface()* should directly return the surface color without illumination (also, no bump mapping is needed in ChangeNormal etc.). this technique is used for some types of objects like the sky. Illuminance1 automatically takes care of `calc_illum`.

**Type:** int

## `c4d.modules.render.BaseVolumeData.calc_mip` <a id="c4d.modules.render.BaseVolumeData.calc_mip"></a>

Specifies, if mip calculations will be done. If this value is ‘0’ then no mip mapping needs to be calculated. ‘calc_mip’ can in some cases be **False** - even if the shader sets *VOLUMEINFO_MIPSAT*. If calc_mip == **False** you should not access MIP/SAT variables such as `delta` etc.

**Type:** int

## `c4d.modules.render.BaseVolumeData.pp` <a id="c4d.modules.render.BaseVolumeData.pp"></a>

MIP corner points in global space.

> **Note:** Only valid if *VOLUMEINFO_MIPSAT* is set.

**Type:** Tuple[c4d.Vector, c4d.Vector, c4d.Vector]

## `c4d.modules.render.BaseVolumeData.nn` <a id="c4d.modules.render.BaseVolumeData.nn"></a>

MIP normals of the three other corner points.

> **Note:** Only valid if *VOLUMEINFO_MIPSAT* is set.

**Type:** Tuple[c4d.Vector, c4d.Vector, c4d.Vector]

## `c4d.modules.render.BaseVolumeData.raybits` <a id="c4d.modules.render.BaseVolumeData.raybits"></a>

Ray information, these values are:

|   |   |
|---|---|
| *RAYBIT_NONE* | None. |
| *RAYBIT_REFLECTION* | Ray chain contains a reflection ray. |
| *RAYBIT_TRANSPARENCY* | Ray chain contains a transparency ray (refractions are not contained). |
| *RAYBIT_REFRACTION* | Ray chain contains a refraction ray. |
| *RAYBIT_CUSTOM* | Ray chain contains a custom ray. |
| *RAYBIT_CURR_REFLECTION* | Current ray is a reflection ray. |
| *RAYBIT_CURR_TRANSPARENCY* | Current ray is a transparency ray. |
| *RAYBIT_CURR_REFRACTION* | Current ray is a refraction ray. |
| *RAYBIT_CURR_CUSTOM* | Current ray is a custom ray. |
| *RAYBIT_VOLUMETRICLIGHT* | Current ray is used to calculate a volumetric light. |
| *RAYBIT_ALLOWVLMIX* | Custom mixing of visible light sources allowed for the ray; bit must be deleted by shader if used. |
| *RAYBIT_GI* | Current ray is a Global Illumination ray. |
| *RAYBIT_BLURRY* | Current ray is a blurry ray. |
| *RAYBIT_SSS* | Current ray is a subsurface scattering ray. |
| *RAYBIT_AO* | Current ray is an Ambient Occlusion ray. |
| *RAYBIT_COMPOSITING* | Current ray is a compositing ray. |

**Type:** int

## `c4d.modules.render.BaseVolumeData.recursion_id` <a id="c4d.modules.render.BaseVolumeData.recursion_id"></a>

The plugin ID of data passed through recursion.

**Type:** int

## `c4d.modules.render.BaseVolumeData.back_p` <a id="c4d.modules.render.BaseVolumeData.back_p"></a>

The backprojected point (*StickTextureTag*) will be generated if the shader sets the flag *VOLUMEINFO_TRANSFORM* or *SHADERINFO_TRANSFORM* if it is a channel shader.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.back_delta` <a id="c4d.modules.render.BaseVolumeData.back_delta"></a>

This the ‘spot size’ (MIP mapping value) for the backprojected point. The backprojected point (*StickTextureTag*) will be generated if the shader sets the flag *VOLUMEINFO_TRANSFORM* or *SHADERINFO_TRANSFORM* if it is a channel shader.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.BaseVolumeData.global_mip` <a id="c4d.modules.render.BaseVolumeData.global_mip"></a>

The global MIP scale.

**Type:** float

## `c4d.modules.render.BaseVolumeData.sid` <a id="c4d.modules.render.BaseVolumeData.sid"></a>

Sub polygon ID (only used for SPD).

**Type:** int

## `c4d.modules.render.BaseVolumeData.par_u` <a id="c4d.modules.render.BaseVolumeData.par_u"></a>

Barycentric U coordinate (only used for SPD).

**Type:** float

## `c4d.modules.render.BaseVolumeData.par_v` <a id="c4d.modules.render.BaseVolumeData.par_v"></a>

Barycentric V coordinate (only used for SPD).

**Type:** float

Child Class:

- [`c4d.modules.render.VolumeData`](../VolumeData/index.md#c4d.modules.render.VolumeData)
