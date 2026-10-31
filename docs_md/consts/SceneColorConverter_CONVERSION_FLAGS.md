<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/SceneColorConverter_CONVERSION_FLAGS.html -->

# SceneColorConverter_CONVERSION_FLAGS <a id="scenecolorconverter-conversion-flags"></a>

| Symbol ID | Description |
|---|---|
| NONE | No flags. |
| ADD_UNDO | Create an undo step for all changes. This must not be set when the conversion is called from a thread. |
| CLASSIC_LINEAR_TO_SRGB | The Scene is a classic scene and would have converted Linear to sRGB on color values. |
| CLASSIC_SRGB_TO_LINEAR | The Scene is a classic scene and would have converted sRGB to Linear on color values. |
| FORCE_LINEAR_LIGHTS | Forces the conversion from classic or to classic color management to interpret lights to have linear brightness. Otherwise lights will adjust their brightness. |
