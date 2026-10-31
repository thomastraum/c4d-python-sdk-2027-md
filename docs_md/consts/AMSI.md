<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/AMSI.html -->

# AMSI <a id="amsi"></a>

|   |   |   |
|---|---|---|
| *AMSI_CREATE_MISSING_MATERIALS* | bool | Create materials and texture tags if they are missing. |
| *AMSI_CREATE_MISSING_CHANNELS* | bool | Create missing texture channels. |
| *AMSI_AUTOSELECT_MATERIALS* | bool | Autoselect materials from object selection. |
| *AMSI_AUTOSELECT_OBJECTS* | bool | Autoselect objects from material selection. |
| *AMSI_DELETE_BROKENMATERIALTAGS* | bool | Delete material tags with broken material links. |
| *AMSI_ENABLEMATERIALS* | bool | Enable all materials for painting. |
| *AMSI_SINGLEMATERIAL* | bool | Join UV’s in one single material. |
| *CREATE_CHANNEL* | bool | Create missing texture channels (*CREATE_CHANNEL + CHANNEL_ID*). |
| *CREATE_CHANNEL_C* | vector | Channel color (*CREATE_CHANNEL_C + CHANNEL_ID*). |
| *AMSI_ENABLED* | bool | Enable automatic mapsize interpolation, otherwise minimum *size == texsize*. |
| *AMSI_TEXW* | int | Fixed texture size width. |
| *AMSI_TEXH* | int | Fixed texture size height. |
| *AMSI_TEXMIN* | int | Minimum texture size (width and height). |
| *AMSI_TEXMAX* | int | Maximum texture size (width and height). |
| *AMSI_QUANTIZE* | int | Quantize texture size. |
| *AMSI_RESCALE_EXISTING* | bool | Rescale existing material channels. |
| *AMSI_USE_SAME_RES* | bool | Use the same texture size if one channel already exists. |
| *AMSI_UV_CALC_METHOD* | int | Calculation mode: |
|  | *UV_CALC_METHOD_OPTIMAL1* | Optimal Cube Mapping. |
|  | *UV_CALC_METHOD_OPTIMAL2* | Optimal Angle Mapping. |
|  | *UV_CALC_METHOD_REALIGN* | Realign. |
| *AMSI_UV_CALC_EXISTING* | bool | Calculate UVs. |
| *AMSI_UV_RELAXATION* | bool | Relax UVs. |
