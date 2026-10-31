<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/registries/maxon.LoggerTypes.html -->

# maxon.LoggerTypes <a id="maxon-loggertypes"></a>

## Description <a id="module-maxon.LoggerTypes"></a><a id="description"></a>

Registries are used to register specific implementations of a given interface.  
An implementation that is registered in such a registry can then be accessed with a specific ID from anywhere in the application.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Registry`](../references/core/maxon.Registry.md#module-maxon.Registry)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.LoggerTypes.Application`](maxon.LoggerTypes.Application.md#maxon.LoggerTypes.Application) | Logger type which writes output to the built-in UI console of the host application. |
| [`maxon.LoggerTypes.File`](maxon.LoggerTypes.File.md#maxon.LoggerTypes.File) | Logger type which writes output to a file. |
| [`maxon.LoggerTypes.MultiFile`](maxon.LoggerTypes.MultiFile.md#maxon.LoggerTypes.MultiFile) | Logger type which writes output to a file in a ring buffer mode. |
| [`maxon.LoggerTypes.Process`](maxon.LoggerTypes.Process.md#maxon.LoggerTypes.Process) | Logger type which writes output to the process console (and on Windows to the debugger console). |
