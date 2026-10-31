<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.gui/BaseCustomGui/DateTimeControlData/index.html -->

# c4d.gui.DateTimeControl <a id="c4d-gui-datetimecontrol"></a>

## *class* `c4d.gui.DateTimeControl` <a id="c4d.gui.DateTimeControl"></a>

Spline GUI(**DATETIME_GUI**) for [`DateTimeData`](../../../c4d/CustomDataType/DateTimeData/index.md#c4d.DateTimeData) data type. These are the settings:

|   |   |
|---|---|
| *DATETIME_TIME_CONTROL* | **True**, if it is a clock. |
| *DATETIME_DATE_CONTROL* | **True**, if it is a calendar. |
| *DATETIME_NOW_BUTTON* | **True**, to add “Now” button. |
| *DATETIME_NO_SECONDS* | **True**, to not show seconds. |
| *DATETIME_SHOW_LABELS* | **True**, to show the *“Date”* and *“Time”* labels if the GUI is collapsed. |

This is how it looks like:

![../../../../_images/datetimecontrol_datetime.png](../../../../_images/datetimecontrol_datetime.png)

Parent Class:

- [`c4d.gui.BaseCustomGui`](../index.md#c4d.gui.BaseCustomGui)

## Overview <a id="overview"></a>

- [`DateTimeControl.GetDateTime()`](#c4d.gui.DateTimeControl.GetDateTime): Get the time.
- [`DateTimeControl.SetDateTime()`](#c4d.gui.DateTimeControl.SetDateTime): Sets the time.

## Members <a id="members"></a>

### Date And Time <a id="c4d.gui.DateTimeControl-method-Date-And-Time"></a>

#### `DateTimeControl.GetDateTime(self)` <a id="c4d.gui.DateTimeControl.GetDateTime"></a>

Get the time.

**Return type:** [c4d.DateTimeData](../../../c4d/CustomDataType/DateTimeData/index.md#c4d.DateTimeData)

**Returns:** The new spline data object.

#### `DateTimeControl.SetDateTime(self, d, bSetData=True, bSetTime=True)` <a id="c4d.gui.DateTimeControl.SetDateTime"></a>

Sets the time.

**Parameters:**

- **d** ([*c4d.DateTimeData*](../../../c4d/CustomDataType/DateTimeData/index.md#c4d.DateTimeData)) – The new time.
- **bSetData** (*bool*) – If this is **False** the date part of *d* is disregarded.
- **bSetTime** (*bool*) – If this is **False** the time part of *d* is disregarded.
