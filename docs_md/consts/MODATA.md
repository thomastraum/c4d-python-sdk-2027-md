<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/MODATA.html -->

# MODATA <a id="modata"></a>

|   |   |   |
|---|---|---|
| *MODATA_MATRIX* | [`Matrix`](../modules/c4d/Matrix/index.md#c4d.Matrix) | Matrix of the clone. |
| *MODATA_COLOR* | [`Vector`](../modules/c4d/Vector/index.md#c4d.Vector) | Color of the clone. |
| *MODATA_SIZE* | [`Vector`](../modules/c4d/Vector/index.md#c4d.Vector) | Size of the clone. |
| *MODATA_UVW* | [`Vector`](../modules/c4d/Vector/index.md#c4d.Vector) | UV position of the clone. |
| *MODATA_FLAGS* | int | Flags: |
|  | *MOGENFLAG_CLONE_ON* | Particle is visible. |
|  | *MOGENFLAG_DISABLE* | Particle is permanently disabled. |
|  | *MOGENFLAG_BORN* | Particle is just generated (internal use only). |
|  | *MOGENFLAG_MODATASET* | The [`MoData`](../modules/c4d.modules/mograph/MoData/index.md#c4d.modules.mograph.MoData) has been set and does not need the input of the transform panel. |
|  | *MOGENFLAG_COLORSET* | The [`MoData`](../modules/c4d.modules/mograph/MoData/index.md#c4d.modules.mograph.MoData) color has been set and does not need to be updated. |
|  | *MOGENFLAG_TIMESET* | The [`MoData`](../modules/c4d.modules/mograph/MoData/index.md#c4d.modules.mograph.MoData) time has been set and does not need to be updated. |
| *MODATA_WEIGHT* | float | Weight of the clone. |
| *MODATA_CLONE* | float | Clone Offset (picks which child of the Cloner gets cloned or the blending between those children). |
| *MODATA_TIME* | float | Time offset of the clone. |
| *MODATA_LASTMAT* | [`Matrix`](../modules/c4d/Matrix/index.md#c4d.Matrix) | Previous frame particle matrix. |
| *MODATA_STARTMAT* | [`Matrix`](../modules/c4d/Matrix/index.md#c4d.Matrix) | Matrix at the particle’s birth. |
| *MODATA_ALT_INDEX* | int | Alternative index value that can be used for instance by the Step Effector when cloned over a spline with an offset. |
| *MODATA_FALLOFF_WGT* | float | Falloff weight. |
| *MODATA_SPLINE_SEGMENT* | int | The segment index, mostly used with the MoSpline (currently unused). |
| *MODATA_GROWTH* | float | Offset of growth for the particle on the MoSpline (currently unused). |
