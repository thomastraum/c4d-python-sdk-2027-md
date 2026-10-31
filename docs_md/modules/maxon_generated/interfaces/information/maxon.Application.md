<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/information/maxon.Application.html -->

# maxon.Application <a id="maxon-application"></a>

## Description <a id="module-maxon.Application"></a><a id="description"></a>

Application wide functions.  
Implement this interface to be able to link against the kernel library.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetApplicationMode`](#maxon.Application.GetApplicationMode)() | Retrieves the current application mode. |
| [`GetCommandLineArg`](#maxon.Application.GetCommandLineArg)(idx) | Returns a command line argument. |
| [`GetCommandLineArgCount`](#maxon.Application.GetCommandLineArgCount)() | Returns the number of command line arguments delivered to the app on startup. |
| [`GetMachineInfo`](#maxon.Application.GetMachineInfo)() | Returns information about the system and processor. |
| [`GetModulePaths`](#maxon.Application.GetModulePaths)() | Returns all module paths configured through g_modulePath, g_additionalModulePath and user preferences. |
| [`GetTempUrl`](#maxon.Application.GetTempUrl)(directory) | Returns a new unique [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) for a temporary file. |
| [`GetUrl`](#maxon.Application.GetUrl)() | Returns the requested [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`GetWindowsSubsystem`](#maxon.Application.GetWindowsSubsystem)() | Returns information about the subsystem of the application. |
| [`SetApplicationMode`](#maxon.Application.SetApplicationMode)(mode) | Sets a new application mode. This mode defines the behavior after the startup is done. |

## Methods Definition <a id="methods-definition"></a>

### *static* `Application.GetApplicationMode()` <a id="maxon.Application.GetApplicationMode"></a>

Retrieves the current application mode.  
This mode defines the behavior after after the startup is done.

**Returns:** The current application mode.

**Return type:**

`maxon.APPLICATIONMODE`

### *static* `Application.GetCommandLineArg(idx)` <a id="maxon.Application.GetCommandLineArg"></a>

Returns a command line argument.

**Parameters:** **idx** (*int*) – The index of the argument. (0 >= idx < GetCommandLineArgCount()).

**Returns:** The requested argument.

**Return type:** str

### *static* `Application.GetCommandLineArgCount()` <a id="maxon.Application.GetCommandLineArgCount"></a>

Returns the number of command line arguments delivered to the app on startup.

**Returns:** Number of arguments to request via [`Application.GetCommandLineArg()`](#maxon.Application.GetCommandLineArg).

**Return type:** int

### *static* `Application.GetMachineInfo()` <a id="maxon.Application.GetMachineInfo"></a>

Returns information about the system and processor.  
See `maxon.MACHINEINFO` for [`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary) properties.

**Returns:** System and processor information.

**Return type:** [`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)

### *static* `Application.GetModulePaths()` <a id="maxon.Application.GetModulePaths"></a>

Returns all module paths configured through g_modulePath, g_additionalModulePath and user preferences.

**Returns:** Array containing all paths that are searched for modules.

**Return type:** [`maxon.BaseArray`](../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray)

### *static* `Application.GetTempUrl(directory)` <a id="maxon.Application.GetTempUrl"></a>

Returns a new unique [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) for a temporary file.  
A typical use for this is

```python
tempfile = maxon.Application.GetTempUrl(maxon.Application.GetUrl(maxon.APPLICATION_URLTYPE.TEMP_DIR))
```

**Parameters:** **directory** ([`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)) – Directory url where the temporary file should be created in.

**Returns:** [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) pointing to the temporary file.

**Return type:** [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

### *static* `Application.GetUrl()` <a id="maxon.Application.GetUrl"></a>

Returns the requested [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

```python
tempfile = maxon.Application.GetUrl(maxon.APPLICATION_URLTYPE.TEMP_DIR))
```

**Parameters:** **urlType** (`maxon.APPLICATION_URLTYPE`) – Type of the url.

**Returns:** [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) containing the requested.

**Return type:** [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

### *static* `Application.GetWindowsSubsystem()` <a id="maxon.Application.GetWindowsSubsystem"></a>

Returns information about the subsystem of the application.

> **Warning:** This method is only available on Windows.

**Returns:** The current subsystem of the current process.

**Return type:**

`maxon.SUBSYSTEM`

### *static* `Application.SetApplicationMode(mode)` <a id="maxon.Application.SetApplicationMode"></a>

Sets a new application mode. This mode defines the behavior after the startup is done.  
Please note that it’s only possible to raise the mode from `maxon.APPLICATIONMODE.DONTWAIT` to `maxon.APPLICATIONMODE.KEEPRUNNING`.

**Parameters:** **mode** (`maxon.APPLICATIONMODE`) – The new mode to be set.

**Returns:** True if the function changed the mode successfully.

**Return type:** bool
