<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/information/maxon.System.html -->

# maxon.System <a id="maxon-system"></a>

## Description <a id="module-maxon.System"></a><a id="description"></a>

Application wide system functions.  
Do not use any of those functions directly.  
Implement this interface to link against the kernel library.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`FindDefinitionGetData`](#maxon.System.FindDefinitionGetData)(type, id[, expected]) | Returns the definition of the given entity type. |
| [`GetConfiguration`](#maxon.System.GetConfiguration)(index, config) | Gets the configuration value by a given index. |
| [`GetConfigurationCount`](#maxon.System.GetConfigurationCount)() | Returns the number of configuration values registered with ConfigurationRegister. |
| [`GetConsoleOutputType`](#maxon.System.GetConsoleOutputType)() | Retrieves which types of output shall be supported. |
| [`GetCustomTimer`](#maxon.System.GetCustomTimer)() | Returns the current system time which is being used by the Timer class. |
| [`GetDefinitionCount`](#maxon.System.GetDefinitionCount)(type) | Returns the total number of definitions for the given entity type. |
| [`PrivateGetInternedId`](#maxon.System.PrivateGetInternedId)(value) | Retrieve a `maxon.Componenent` from a [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id). |

## Methods Definition <a id="methods-definition"></a>

### *static* `System.FindDefinitionGetData(type, id, expected=None)` <a id="maxon.System.FindDefinitionGetData"></a>

Returns the definition of the given entity type.

**Parameters:**

- **type** (`maxon.EntityBase.TYPE`) –

  Entity type.

  Use `maxon.EntityBase.TYPE.COUNT` for the total number of methods of all (virtual and non-virtual) interfaces.

- **id** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Entity id.

- **expected** ([`maxon.DataType`](../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)) – The expected [`maxon.DataType`](../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType) of the return value

**Returns:** The definition of the given entity type.

**Return type:** [`maxon.DataType`](../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType) specified for *expected*

### *classmethod* `System.GetConfiguration(index, config)` <a id="maxon.System.GetConfiguration"></a>

Gets the configuration value by a given index.

**Parameters:**

- **index** (*int*) – index Index of the configuration value. 0 <= index < [`System.GetConfigurationCount()`](#maxon.System.GetConfigurationCount)
- **config** ([`maxon.ConfigInit`](../../datatypes/core/maxon.ConfigInit.md#module-maxon.ConfigInit)) – The config that will be filled with the data.

**Returns:** True on success or false if the index is out of range.

**Return type:** bool

### *static* `System.GetConfigurationCount()` <a id="maxon.System.GetConfigurationCount"></a>

Returns the number of configuration values registered with ConfigurationRegister.

**Returns:** Number of configuration values.

**Return type:** int

### *static* `System.GetConsoleOutputType()` <a id="maxon.System.GetConsoleOutputType"></a>

Retrieves which types of output shall be supported.

**Returns:** Diagnostic, warning and/or critical output.

**Return type:**

`maxon.OUTPUT`

### *static* `System.GetCustomTimer()` <a id="maxon.System.GetCustomTimer"></a>

Returns the current system time which is being used by the Timer class.

**Returns:** [`maxon.Seconds`](../../datatypes/time/maxon.Seconds.md#module-maxon.Seconds) of the system time.

**Return type:** float

### *static* `System.GetDefinitionCount(type)` <a id="maxon.System.GetDefinitionCount"></a>

Returns the total number of definitions for the given entity type.  
This is used for statistics about the complexity of the whole application.

**Parameters:**

**type** (`maxon.EntityBase.TYPE`) –

Entity type.

Use `maxon.EntityBase.TYPE.COUNT` for the total number of methods of all (virtual and non-virtual) interfaces.

**Returns:** Number of definitions of the given type.

**Return type:** int

### *static* `System.PrivateGetInternedId(value)` <a id="maxon.System.PrivateGetInternedId"></a>

Retrieve a `maxon.Componenent` from a [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id).

**Parameters:** **value** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id) of the registered maxon component you want to retrieve.

**Returns:** The maxon component

**Return type:** [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)
