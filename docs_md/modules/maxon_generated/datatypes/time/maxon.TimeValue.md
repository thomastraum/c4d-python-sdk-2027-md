<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/time/maxon.TimeValue.html -->

# maxon.TimeValue <a id="maxon-timevalue"></a>

## Description <a id="module-maxon.TimeValue"></a><a id="description"></a>

The [`maxon.TimeValue`](#module-maxon.TimeValue) class encapsulates a timer value.

## Inheritance diagram <a id="inheritance-diagram"></a>

Child Class:

- [`maxon.Seconds`](maxon.Seconds.md#module-maxon.Seconds)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetSeconds`](#maxon.TimeValue.GetSeconds)() | Gets the time value in seconds from the instance. |
| [`SetSeconds`](#maxon.TimeValue.SetSeconds)(seconds) | Set the time value in seconds for the instance. |
| [`__add__`](#maxon.TimeValue.__add__)(b) | Adds a time value in seconds to the current time. |
| [`__init__`](#maxon.TimeValue.__init__)(seconds) | Initializes the time object with a values in seconds. |
| [`__radd__`](#maxon.TimeValue.__radd__)(b) | Adds a time in seconds to the current time. |
| [`__rsub__`](#maxon.TimeValue.__rsub__)(b) |  |
| [`__str__`](#maxon.TimeValue.__str__)() | Return str(self). |
| [`__sub__`](#maxon.TimeValue.__sub__)(b) | Subtracts a time value in seconds from the current time. |

## Methods Definition <a id="methods-definition"></a>

### `TimeValue.GetSeconds()` <a id="maxon.TimeValue.GetSeconds"></a>

Gets the time value in seconds from the instance.

**Returns:** The time value in seconds.

**Return type:** int

### `TimeValue.SetSeconds(seconds)` <a id="maxon.TimeValue.SetSeconds"></a>

Set the time value in seconds for the instance.

**Parameters:** **seconds** (*float*) – The value to set.

### `TimeValue.__add__(b)` <a id="maxon.TimeValue.__add__"></a>

Adds a time value in seconds to the current time.

**Parameters:** **b** ([`maxon.TimeValue`](#module-maxon.TimeValue)) – The other time.

### `TimeValue.__init__(seconds)` <a id="maxon.TimeValue.__init__"></a>

Initializes the time object with a values in seconds.

**Parameters:** **seconds** (*float*) – The number of seconds to initalize the time object with.

### `TimeValue.__radd__(b)` <a id="maxon.TimeValue.__radd__"></a>

Adds a time in seconds to the current time.

**Parameters:** **b** ([`maxon.TimeValue`](#module-maxon.TimeValue)) – The other time.

### `TimeValue.__rsub__(b)` <a id="maxon.TimeValue.__rsub__"></a>

### `TimeValue.__str__()` <a id="maxon.TimeValue.__str__"></a>

Return str(self).

### `TimeValue.__sub__(b)` <a id="maxon.TimeValue.__sub__"></a>

Subtracts a time value in seconds from the current time.

**Parameters:** **b** ([`maxon.TimeValue`](#module-maxon.TimeValue)) – The other time.
