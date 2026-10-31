<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/DateTimeData/index.html -->

# c4d.DateTimeData <a id="c4d-datetimedata"></a>

## *class* `c4d.DateTimeData` <a id="c4d.DateTimeData"></a>

DateTime data type (*DATETIME_DATA*) for the [`DateTimeControl`](../../../c4d.gui/BaseCustomGui/DateTimeControlData/index.md#c4d.gui.DateTimeControl) GUI.

This type is called by value.

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Date And Time**

- [`DateTimeData.GetDateTime()`](#c4d.DateTimeData.GetDateTime): Return the time.
- [`DateTimeData.SetDateTime()`](#c4d.DateTimeData.SetDateTime): Set the time.

**Magic Methods**

- [`DateTimeData.__init__()`](#c4d.DateTimeData.__init__)

## Members <a id="members"></a>

### Date And Time <a id="c4d.DateTimeData-method-Date-And-Time"></a>

#### `DateTimeData.GetDateTime(self)` <a id="c4d.DateTimeData.GetDateTime"></a>

Return the time.

**Return type:** [time.struct_time](https://docs.python.org/3.9/library/time.html#time.struct_time)

**Returns:** The time.

#### `DateTimeData.SetDateTime(self, d, bSetData=True, bSetTime=True)` <a id="c4d.DateTimeData.SetDateTime"></a>

Set the time.

**Parameters:**

- **d** – The new time.
- **bSetData** (*bool*) – If this is **False** the date part of *d* is disregarded.
- **bSetTime** (*bool*) – If this is **False** the time part of *d* is disregarded.

Here is a sample code that shows how to parse a string into a [`DateTimeData`](#c4d.DateTimeData) object.

```python
import c4d
from datetime import datetime

# Parse the time string
dt = datetime.strptime('16.07.2011 03:37:12',"%d.%m.%Y %H:%M:%S")
dtd = c4d.DateTimeData()
# Fills the Data object with the DateTime object
dtd.SetDateTime(dt)

t = dtd.GetDateTime()
print(t.day)
print(t.month)
print(t.year)
```

### Magic Methods <a id="c4d.DateTimeData-method-Magic-Methods"></a>

#### `DateTimeData.__init__(self, v)` <a id="c4d.DateTimeData.__init__"></a>

**Parameters:** **v** ([*c4d.DateTimeData*](#c4d.DateTimeData)) – Copy constructor.
