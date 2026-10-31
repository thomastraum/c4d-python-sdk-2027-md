<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/MPBTYPE.html -->

# MPBTYPE <a id="mpbtype"></a>

|   |   |   |
|---|---|---|
| *MPBTYPE_SHOW* | bool | Determines if the layer will be shown in the external render window. (The Cinema 4D renderer modifies this value itself.) |
| *MPBTYPE_SAVE* | bool | Determines if the layer is saved with the image or not if *SAVEBIT_USESELECTEDLAYERS* is used. |
| *MPBTYPE_PERCENT* | float | The blend parameter, between *0.0* and *1.0*. |
| *MPBTYPE_BLENDMODE* | int | The blend mode. (*LAYER_NORMAL*, *LAYER_DISSOLVE* etc. from from *bplayer.h.*) |
| *MPBTYPE_COLORMODE* | int | The color mode: See [COLORMODE](COLORMODE.md). |
| *MPBTYPE_BITMAPTYPE* | int | The bitmap type. Cannot be set with `MultipassBitmap.SetParameter()`. |
| *MPBTYPE_NAME* | str | The layer name. Only a [`PaintLayerBmp`](../modules/c4d.modules/bodypaint/PaintBitmap/PaintLayer/PaintLayerBmp/index.md#c4d.modules.bodypaint.PaintLayerBmp) or [`PaintLayerFolder`](../modules/c4d.modules/bodypaint/PaintBitmap/PaintLayer/PaintLayerFolder/index.md#c4d.modules.bodypaint.PaintLayerFolder) can have a name. |
| *MPBTYPE_DPI* | int | The resolution in DPI. **Private.** |
| *MPBTYPE_USERID* | int | The user ID for the layer. In the renderer this is *VPBUFFER_xxx*. |
| *MPBTYPE_USERSUBID* | int | The user sub-ID for the layer. In the renderer this is used for blend channels for instance. |
| *MPBTYPE_FORCEBLEND* | int | The special mode used to force blend layers. |
