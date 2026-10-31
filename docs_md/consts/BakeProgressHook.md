<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/BakeProgressHook.html -->

# BakeProgressHook <a id="bakeprogresshook"></a>

|   |   |   |
|---|---|---|
| ‘version’ | int | Bake version. |
| ‘state’ | int | Bake state: |
|  | *BAKE_STATE_NONE* | None. |
|  | *BAKE_STATE_PREPARE* | Prepare. |
|  | *BAKE_STATE_GI_PREPASS* | GI prepass. |
|  | *BAKE_STATE_FILL_IMAGE* | Fill image. |
|  | *BAKE_STATE_COMPLETE* | Complete. |
|  | *BAKE_STATE_INITIALIZE* | Initialize. |
|  | *BAKE_STATE_RESIZENOTIFY* | Resize notify. |
| ‘data’ | tuple(int, int, [`BaseBitmap`](../modules/c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) | Only used in case of *BAKE_STATE_RESIZENOTIFY* state. Tuple data is resize width, resize height and cake bitmap. |
| ‘timedelta’ | int | Time. |
| ‘r’ | float | Progress, between *0* and *1*. |
| ‘starttime’ | int | Start time in milliseconds. |
