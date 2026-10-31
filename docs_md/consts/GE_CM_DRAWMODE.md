<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/GE_CM_DRAWMODE.html -->

# GE_CM_DRAWMODE <a id="ge-cm-drawmode"></a>

|   |   |
|---|---|
| *GE_CM_DRAWMODE_COPY* | New pixels overwrite old ones. |
| *GE_CM_DRAWMODE_BLEND* | New pixels blend with old ones, taking the alpha value of the new pixels in account as well as the blend factor specified by the parameter. The value specified by the parameter is the opacity of the source (bitmap). It ranges from *0* to *256*, where *256* equals *1.0* and means opaque. |
| *GE_CM_DRAWMODE_MASK* | New pixels overwrite the old ones at the bits where the mask specified by the parameter equals *1*. |
