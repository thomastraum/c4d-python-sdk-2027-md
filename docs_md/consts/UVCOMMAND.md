<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/UVCOMMAND.html -->

# UVCOMMAND <a id="uvcommand"></a>

| Symbols | Description / Sub Symbols | Type | Description |
|---|---|---|---|
| *UVCOMMAND_OPTIMALMAPPING* | Optimal Angle UV Mapping. |  |  |
| *UVCOMMAND_OPTIMALCUBICMAPPING* | Optimal Cubic UV Mapping. |  |  |
| *UVCOMMAND_REALIGN* | Realign UV Mapping: |  |  |
|  | *OPTIMALMAPPING_PRESERVEORIENTATION* | bool | Preserve Orientation (Cubic, Angle, Realign). |
|  | *OPTIMALMAPPING_STRETCHTOFIT* | bool | Stretch To Fit (Cubic, Angle, Realign). |
|  | *OPTIMALMAPPING_DISTORTION* | float | Maximum Distortion (Angle). |
|  | *OPTIMALMAPPING_SPACING* | float | Spacing (Cubic, Angle, Realign). |
|  | *OPTIMALMAPPING_AREAFAK* | float | Maximum Area Factor (Cubic). |
|  | *OPTIMALMAPPING_TWOD* | bool | 2D (Cubic). |
|  | *OPTIMALMAPPING_PROGRESSBAR* | bool | Progress bar (Cubic, Angle, Realign). |
|  | *OPTIMALMAPPING_RELAXCOUNT* | int | Relaxation Steps (Cubic, Angle). |
|  | *OPTIMALMAPPING_EQUALIZEAREA* | bool | Equalize Island Size (Realign). |
| *UVCOMMAND_RELAX* | Relax UV: |  |  |
|  | *RELAXUV_KEEP_BORDER* | bool | Pin Border Points. |
|  | *RELAXUV_KEEP_NEIGHBORS* | bool | Pin To Neighbors. |
|  | *RELAXUV_KEEP_POINTSEL* | bool | Pin Point Selection. |
|  | *RELAXUV_CUT_EDGESEL* | bool | Cut Selected Edges. |
|  | *RELAXUV_EDGESEL_POINTER* | [`c4d.BaseSelect`](../modules/c4d/BaseSelect/index.md#c4d.BaseSelect) | Pointer to the edge selection. |
|  | *RELAXUV_MAX_ITERATIONS* | int | Maximum Iteration Steps. |
|  | *RELAXUV_MODE* | int | Relaxation Mode: |
|  |  | *RELAXUV_MODE_LSCM* | LSCM relaxation. |
|  |  | *RELAXUV_MODE_ABF* | ABF relaxation. |
| *UVCOMMAND_COPY_UV* | Copy UV Points. |  |  |
| *UVCOMMAND_PASTE_UV* | Paste UV Points. |  |  |
| *UVCOMMAND_MAX_UV* | Max UV. |  |  |
| *UVCOMMAND_FLIP_SEQUENCE* | Flip Sequence. |  |  |
| *UVCOMMAND_CYCLE_CW_UV*<br>Previously UVCOMMAND_MOVE_DOWN_SEQUENCE | Move Down Sequence. |  |  |
|  |  |  |  |
| *UVCOMMAND_CYCLE_CCW_UV*<br>Previously UVCOMMAND_MOVE_UP_SEQUENCE | Move Up Sequence. |  |  |
|  |  |  |  |
| *UVCOMMAND_TERRACE* | UV Terrace. |  |  |
| *UVCOMMAND_FIT_TO_CANVAS* | Fit UV To Canvas. |  |  |
| *UVCOMMAND_TRANSFORM* | Transform UV: |  |  |
|  | *UVCOMMAND_TRANSFORM_MOVE_X* | float | Move X (U). |
|  | *UVCOMMAND_TRANSFORM_MOVE_Y* | float | Move Y (V). |
|  | *UVCOMMAND_TRANSFORM_SCALE_X* | float | Scale X (U). |
|  | *UVCOMMAND_TRANSFORM_SCALE_Y* | float | Scale Y (V). |
|  | *UVCOMMAND_TRANSFORM_ANGLE* | float | Rotation angle in radians. |
| *UVCOMMAND_LINEUP* | Line Up UV. |  |  |
| *UVCOMMAND_UNSTITCH* | Unstitch UV. |  |  |
| *UVCOMMAND_BOUNDARY2SHAPE* | UV Boundary To Shape: |  |  |
|  | *UVCOMMAND_BOUNDARY2SHAPE_MODE* | int | UV boundary shape: |
|  |  | *UVCOMMAND_BOUNDARY2SHAPE_CIRCLE* | UV boundary to circle. |
|  |  | *UVCOMMAND_BOUNDARY2SHAPE_QUAD* | UV boundary to square. |
