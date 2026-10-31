<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/ILLUMINATEFLAGS.html -->

# ILLUMINATEFLAGS <a id="illuminateflags"></a>

|   |   |
|---|---|
| *ILLUMINATEFLAGS_NONE* | None. |
| *ILLUMINATEFLAGS_SHADOW* | Full shadow calculations. |
| *ILLUMINATEFLAGS_NOENVIRONMENT* | Shadow calculations are enabled but no environment shading will be calculated. |
| *ILLUMINATEFLAGS_DISABLESHADOWMAP_CORRECTION* | Shadow maps evaluate the normal at a surface point, to avoid the problem of self-shadowing (that is otherwise inherent due to the way the algorithm works). If a free point is sampled in space (where no surface is) this correction has to be disabled though, otherwise wrong results will be returned. |
| *ILLUMINATEFLAGS_DISABLESHADOWCASTERMP_CORRECTION* | Private. |
| *ILLUMINATEFLAGS_LIGHTDIRNORMALS* | Private. |
| *ILLUMINATEFLAGS_NODISTANCEFALLOFF* | Do not take distance falloff into account. |
| *ILLUMINATEFLAGS_NOGRAIN* | Do not take grain into account. |
| *ILLUMINATEFLAGS_BACKLIGHT* | Take backlight into account. |
