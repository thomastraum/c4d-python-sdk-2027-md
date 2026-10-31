<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.gui/BaseCustomGui/RangeCustomGui/index.html -->

# c4d.gui.RangeCustomGui <a id="c4d-gui-rangecustomgui"></a>

## *class* `c4d.gui.RangeCustomGui` <a id="c4d.gui.RangeCustomGui"></a>

Range custom GUI (*CUSTOMGUI_RANGE*) for [`c4d.RangeData`](../../../c4d/CustomDataType/RangeData/index.md#c4d.RangeData). Here are the settings:

|   |   |   |
|---|---|---|
| *RANGE_ALLOWRANGEEDIT* | bool | **True** allows user to add or remove ranges. |
| *RANGE_ALLOWVALUEEDIT* | bool | **True** allows the user to edit the LOD value. |
| *RANGE_ALLOWVALUEEDIT_NONUMERICAL* | bool | **True** allows value editing for the slider only, not for numerical entry. |
| *RANGE_ALLOWRANGESLELECION* | bool | **True** to select ranges by clicking on the range. |
| *RANGE_SHOWVALUE* | bool | **True** to show numerical value. |
| *RANGE_SHOWVALUEPOINTER* | bool | **True** to show value indicator. |
| *RANGE_ALLOWCOLOREDIT* | bool | The color control is visible and the color can be changed by the user. |
| *RANGE_REVERSEVALUE* | bool | If **True** the value on the lod bar will be reversed, *100%* on left and *0%* on the right. |
| *RANGE_SHOWNUMBERONBAR* | bool | If **True** the range index is displayed on the bar. |
| *RANGE_REMAPVALUE* | bool | If **True** the value will be remapped using defined units, min and max. |
| *RANGE_REMAPUNIT* | int | The unit to be used for remapping: *DESC_UNIT_METER*, *DESC_UNIT_PERCENT*, *DESC_UNIT_DEGREE*, *DESC_UNIT_FLOAT*. |
| *RANGE_REMAPMIN* | float | The minimum remapping value. |
| *RANGE_REMAPMAX* | float | The maximum remapping value. |
| *RANGE_VALUESTRING* | str | The string value to be used inside the GUI to decode the current value (e.g. “lod Value” for lod object). |
| *RANGE_CURSORICON* | int | The icon ID for custom cursor. |

The container sub-IDs for *MSG_DESCRIPTION_CUSTOMGUI_NOTIFICATION* are:

|   |   |   |   |
|---|---|---|---|
| *MSG_DESCRIPTION_RANGEGUI_KNOTDELETED* | Selection was changed. |  |  |
|  | *MSG_DESCRIPTION_RANGEGUI_KNOTSELECTED_INDEX* | int | Selected index. |
| *MSG_DESCRIPTION_RANGEGUI_KNOTDELETED* | Knot was deleted. |  |  |
|  | *MSG_DESCRIPTION_RANGEGUI_KNOTDELETED_INDEX* | int | Deleted knot index. |
| *MSG_DESCRIPTION_RANGEGUI_KNOTADDED* | Knot was added. |  |  |
|  | *MSG_DESCRIPTION_RANGEGUI_KNOTADDED_INDEX* | int | Added knot index. |
| *MSG_DESCRIPTION_RANGEGUI_RANGESINVERTED* | Ranges were inverted. |  |  |
| *MSG_DESCRIPTION_RANGEGUI_USERCURRENTVALUECHANGED* | User changed current value. |  |  |
|  | *MSG_DESCRIPTION_RANGEGUI_USERCURRENTVALUECHANGED_MODE* | int | Current value mode: |
|  |  | *MSG_DESCRIPTION_RANGEGUI_USERCURRENTVALUECHANGED_START* | Start. |
|  |  | *MSG_DESCRIPTION_RANGEGUI_USERCURRENTVALUECHANGED_DRAG* | Drag. |
|  |  | *MSG_DESCRIPTION_RANGEGUI_USERCURRENTVALUECHANGED_END* | End. |
|  | *MSG_DESCRIPTION_RANGEGUI_USERCURRENTVALUECHANGED_VALUE* | float | Current value value. |

*New in version R19.*

Parent Class:

- [`c4d.gui.BaseCustomGui`](../index.md#c4d.gui.BaseCustomGui)
