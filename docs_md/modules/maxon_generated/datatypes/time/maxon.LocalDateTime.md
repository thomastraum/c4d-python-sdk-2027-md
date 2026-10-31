<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/time/maxon.LocalDateTime.html -->

# maxon.LocalDateTime <a id="maxon-localdatetime"></a>

## Description <a id="module-maxon.LocalDateTime"></a><a id="description"></a>

At some point developers have to deal with times, dates and timezones.  
This topic can promote headaches because it can be quite complex.  
In general you have to be aware of differences in timezones, especially when your software runs on mobile devices are you let the user share data across countries (or even within the same country).  
The implementation and definition of the classes rely on the ISO 8601.  
Use the [`maxon.UniversalDateTime`](maxon.UniversalDateTime.md#module-maxon.UniversalDateTime) whenever possible to store normalized time and date values and convert them to a [`maxon.LocalDateTime`](#module-maxon.LocalDateTime) instance as late as possible (e.g. for a local string output).  
An object representing a local ‘time and date’ of the current system time.  
All members are public and are allowed to be modified for custom needs.  
Keep in mind that you have to ensure that the values are correct and valid when converting an object back to [`maxon.UniversalDateTime`](maxon.UniversalDateTime.md#module-maxon.UniversalDateTime), otherwise the behavior is undefined.

> **See also:** [`maxon.UniversalDateTime`](maxon.UniversalDateTime.md#module-maxon.UniversalDateTime)

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`ConvertUniversalDateTime`](#maxon.LocalDateTime.ConvertUniversalDateTime)() | Converts the stored time to a Universal Date Time. |
| [`FromUnixTimestamp`](#maxon.LocalDateTime.FromUnixTimestamp)(timestamp) | Create a local date-time object by passing a Unix time stamp. |

## Methods Definition <a id="methods-definition"></a>

### `LocalDateTime.ConvertUniversalDateTime()` <a id="maxon.LocalDateTime.ConvertUniversalDateTime"></a>

Converts the stored time to a Universal Date Time.

**Returns:** The universal date-time object.

**Return type:** [`maxon.UniversalDateTime`](maxon.UniversalDateTime.md#module-maxon.UniversalDateTime)

### *static* `LocalDateTime.FromUnixTimestamp(timestamp)` <a id="maxon.LocalDateTime.FromUnixTimestamp"></a>

Create a local date-time object by passing a Unix time stamp.

**Parameters:** **timestamp** (*int*) – The unix time stamp to be converted.

**Returns:** The local date-time representation.

**Return type:** [`maxon.LocalDateTime`](#module-maxon.LocalDateTime)
