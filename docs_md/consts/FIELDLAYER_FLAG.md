<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/FIELDLAYER_FLAG.html -->

# FIELDLAYER_FLAG <a id="fieldlayer-flag"></a>

|   |   |
|---|---|
| *FIELDLAYER_FLAG_NONE* | None. |
| *FIELDLAYER_FLAG_SKIP* | Layer calculation is disabled, e.g. the linked object on a standard layer’s deform mode is false. |
| *FIELDLAYER_FLAG_ERRORSKIP* | Layer calculation is disabled due to a non critical error in `InitSampling()` or as user specified. |
| *FIELDLAYER_FLAG_HIDE* | Layer should be completely ignored from both calculation and GUI display, e.g. the linked object has been deleted. |
| *FIELDLAYER_FLAG_MODIFYDATA* | The layer modifies existing data and needs the values from layers beneath it in the layer list. |
| *FIELDLAYER_FLAG_PRESERVEALPHA* | The layer does not adjust the existing alpha and its color changes should be applied ignoring any alpha values. |
| *FIELDLAYER_FLAG_NOCHILDVALUE* | Children of the layer do not output their value. |
| *FIELDLAYER_FLAG_NOCHILDCOLOR* | Children of the layer do not output their color. |
| *FIELDLAYER_FLAG_NOCHILDDIRECTION* | Children of the layer do not output their direction. |
| *FIELDLAYER_FLAG_NOCHILDROTATION* | Children of the layer do not output their rotation. |
| *FIELDLAYER_FLAG_TEMPORARY* | Do not save the layer with the list or duplicate it (outside of undo). |
