<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/DRAW_GET_VIEWMATRIX.html -->

# DRAW_GET_VIEWMATRIX <a id="draw-get-viewmatrix"></a>

|   |   |
|---|---|
| *DRAW_GET_VIEWMATRIX_PROJECTION* | Projection matrix. |
| *DRAW_GET_VIEWMATRIX_PROJECTION_LARGE_Z* | Projection matrix without consideration of the set clipping planes. The following values for near and far clipping are used instead: near=`1`, far=`100000` for perspective projection and near=`-1000000`, far=`1000000` for other projection types. |
| *DRAW_GET_VIEWMATRIX_INV_CAMERA* | Inverse camera matrix. |
| *DRAW_GET_VIEWMATRIX_MODELVIEW_PROJECTION* | Projection*View*Model matrix. Slow. |
