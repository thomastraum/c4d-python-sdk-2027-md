<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/logger/maxon.LoggerInterface.html -->

# maxon.LoggerInterface <a id="maxon-loggerinterface"></a>

## Description <a id="module-maxon.LoggerInterface"></a><a id="description"></a>

The logger interface allows to create new custom loggers for specific tasks and to access existing loggers.  
Loggers are presented in the “Console” window in Cinema 4D and registered at the [`maxon.Loggers`](../../registries/maxon.Loggers.md#module-maxon.Loggers) registry.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.LoggerRef`](../../references/logger/maxon.LoggerRef.md#module-maxon.LoggerRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`AddLoggerType`](#maxon.LoggerInterface.AddLoggerType)(ta, loggerTypeCls[, cb]) | Adds a logger type to the logger. |
| [`AddNewLogger`](#maxon.LoggerInterface.AddNewLogger)(id, logger[, moduleInfo]) | Add a new logger to the system. |
| [`Enable`](#maxon.LoggerInterface.Enable)(enable) | Enable or disable the logger. |
| [`GetName`](#maxon.LoggerInterface.GetName)() | Returns the name of the logger. |
| [`IsEnabled`](#maxon.LoggerInterface.IsEnabled)() | Returns if the logger is enabled. |
| [`SetName`](#maxon.LoggerInterface.SetName)(name) | Sets the name of the logger. |
| [`Write`](#maxon.LoggerInterface.Write)([ta, str, loc, level]) | Sends a string to all added logger types. |

## Methods Definition <a id="methods-definition"></a>

### `LoggerInterface.AddLoggerType(ta, loggerTypeCls, cb=None)` <a id="maxon.LoggerInterface.AddLoggerType"></a>

Adds a logger type to the logger.

**Parameters:**

- **ta** (`maxon.TARGETAUDIENCE`) –

  Set the audience.

  The logger type will get the string if the target audience matches when [`LoggerInterface.Write()`](#maxon.LoggerInterface.Write) is used.

- **loggerTypeCls** ([`maxon.LoggerTypeRef`](../../references/logger/maxon.LoggerTypeRef.md#module-maxon.LoggerTypeRef)) – The logger type reference to add.

- **cb** (*function*) – Optional callback that is executed to initialize a logger type after added to the logger. E.g. the file logger needs to be initialized with a destination path.

### *static* `LoggerInterface.AddNewLogger(id, logger, moduleInfo=None)` <a id="maxon.LoggerInterface.AddNewLogger"></a>

Add a new logger to the system.  
Does the same as `Loggers.Insert()`, but also triggers the observers.

**Parameters:**

- **id** ([`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)) – The maxon Id corresponding to the logger.
- **logger** ([`maxon.LoggerRef`](../../references/logger/maxon.LoggerRef.md#module-maxon.LoggerRef)) – The logger reference to add.
- **moduleInfo** (`maxon.ModuleInfo`) – The module which initiates the call. When the module is freed, the logger will be freed too.

### `LoggerInterface.Enable(enable)` <a id="maxon.LoggerInterface.Enable"></a>

Enable or disable the logger.  
If disabled, the logger still consumes strings but discards them.

**Parameters:** **enable** (*bool*) – True or False to enable or disable the logger.

### `LoggerInterface.GetName()` <a id="maxon.LoggerInterface.GetName"></a>

Returns the name of the logger.

**Returns:** The name.

**Return type:** str

### `LoggerInterface.IsEnabled()` <a id="maxon.LoggerInterface.IsEnabled"></a>

Returns if the logger is enabled.

**Returns:** True or False.

**Return type:** bool

### `LoggerInterface.SetName(name)` <a id="maxon.LoggerInterface.SetName"></a>

Sets the name of the logger.

**Parameters:** **name** (*str*) – The name.

### `LoggerInterface.Write(ta=14, str='test', loc=None, level=1)` <a id="maxon.LoggerInterface.Write"></a>

Sends a string to all added logger types.

**Parameters:**

- **ta** (`maxon.TARGETAUDIENCE`) – All logger types which match the target audience will receive the string.
- **str** (*str*) – Text to print.
- **loc** ([`maxon.SourceLocation`](../../datatypes/core/maxon.SourceLocation.md#module-maxon.SourceLocation)) – Source location where the string was printed from.
- **level** (`maxon.WRITEMETA`) – Meta information for the current write operation.
