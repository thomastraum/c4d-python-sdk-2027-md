<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/time/maxon.UniversalDateTime.html -->

# maxon.UniversalDateTime <a id="maxon-universaldatetime"></a>

## Description <a id="module-maxon.UniversalDateTime"></a><a id="description"></a>

Class that represents the Universal date-time (UTC+0000).  
This class should be used whenever you store date and time data and should be converted to the [`maxon.LocalDateTime`](maxon.LocalDateTime.md#module-maxon.LocalDateTime) for a local output as late as possible.  
The internal representation is an unsigned 64-Bit integer and contains the standard Unix date-time starting with 01/01/1970-00:00 UTC+0000.  
The resolution of this date-time class is 1-second.

> **See also:** [`maxon.LocalDateTime`](maxon.LocalDateTime.md#module-maxon.LocalDateTime)

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`ConvertToLocalDateTime`](#maxon.UniversalDateTime.ConvertToLocalDateTime)() | Converts the universal date-time to a local date-time object in the current timezone. |
| [`FromUnixTimestamp`](#maxon.UniversalDateTime.FromUnixTimestamp)(timestamp) | Create a universal date-time object by passing a Unix time stamp. |

## Methods Definition <a id="methods-definition"></a>

### `UniversalDateTime.ConvertToLocalDateTime()` <a id="maxon.UniversalDateTime.ConvertToLocalDateTime"></a>

Converts the universal date-time to a local date-time object in the current timezone.

**Returns:** The local date-time object.

**Return type:** [`maxon.LocalDateTime`](maxon.LocalDateTime.md#module-maxon.LocalDateTime)

### *static* `UniversalDateTime.FromUnixTimestamp(timestamp)` <a id="maxon.UniversalDateTime.FromUnixTimestamp"></a>

Create a universal date-time object by passing a Unix time stamp.

**Parameters:** **timestamp** (*int*) – The unix time stamp to be converted.

**Returns:** The universal date-time representation.

**Return type:** [`maxon.UniversalDateTime`](#module-maxon.UniversalDateTime)
