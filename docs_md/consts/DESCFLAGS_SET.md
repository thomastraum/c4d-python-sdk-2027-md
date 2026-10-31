<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/DESCFLAGS_SET.html -->

# DESCFLAGS_SET <a id="descflags-set"></a>

|   |   |
|---|---|
| *DESCFLAGS_SET_NONE* | None. |
| *DESCFLAGS_SET_PARAM_SET* | Parameter set. |
| *DESCFLAGS_SET_USERINTERACTION* | Set when the GUI is calling `SetParameter()`. This is the only time when `SetParameter()` is allowed to use user interaction elements (e.g. open dialogs, display messages etc.). |
| *DESCFLAGS_SET_DONTCHECKMINMAX* | No check is internally done if the parameter passed is within the [min/max] range of the description, to save some time. |
| *DESCFLAGS_SET_DONTAFFECTINHERITANCE* | No parameter inheritance, for render settings and post effects only. |
| *DESCFLAGS_SET_FORCESET* | Forces the set value without `GetParameter()`/Compare. Use only for calls where for sure the value was changed! |
| *DESCFLAGS_SET_DONTFREESPLINECACHE* | **Private.** *New in version R16.038.* |
| *DESCFLAGS_SET_INDRAG* | **Gadget (e.g. Slider) in dragging mode (not finished). Only used when *DESCFLAGS_SET_USERINTERACTION* is set.** *New in version R17.053.* |
