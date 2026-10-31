<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/SHADERINFO.html -->

# SHADERINFO <a id="shaderinfo"></a>

|   |   |
|---|---|
| *SHADERINFO_NONE* | None. |
| *SHADERINFO_TRANSFORM* | Channel needs back-transformed data. (Required for `BaseVolumeData.back_p`.) |
| *SHADERINFO_BUMP_SUPPORT* | Channel shader supports bump. This is strongly recommended for all shaders except simple 2D (UV) samplers. |
| *SHADERINFO_ALPHA_SUPPORT* | Channel shader supports alpha output. |
| *SHADERINFO_REFLECTIONS* | Channel shader computes reflections. |
| *SHADERINFO_DUDVREQUIRED* | Channel shader needs du/dv bump mapping data. See `BaseVolumeData.ddu` and `BaseVolumeData.ddv`. |
| *SHADERINFO_DYNAMICSUBSHADERS* | Channel shader has a dynamic list of sub-shaders in its description. |
