<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/core/maxon.ConfigInit.html -->

# maxon.ConfigInit <a id="maxon-configinit"></a>

## Description <a id="module-maxon.ConfigInit"></a><a id="description"></a>

Represents an config entry value.

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

To access configuration, please use config.XXXX to access the configuration value.

```python
# Display the default preference path
tempFile = maxon.config.g_prefsPath
```

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)
- [`maxon.Struct`](../base_core/maxon.Struct.md#module-maxon.Struct)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.ConfigInit.CONFIGURATION_DATATYPE_BOOL`](maxon.ConfigInit.CONFIGURATION_DATATYPE_BOOL.md#maxon.ConfigInit.CONFIGURATION_DATATYPE_BOOL) | Defines a boolean type. |
| [`maxon.ConfigInit.CONFIGURATION_DATATYPE_FLOAT`](maxon.ConfigInit.CONFIGURATION_DATATYPE_FLOAT.md#maxon.ConfigInit.CONFIGURATION_DATATYPE_FLOAT) | Defines a float type. |
| [`maxon.ConfigInit.CONFIGURATION_DATATYPE_INT`](maxon.ConfigInit.CONFIGURATION_DATATYPE_INT.md#maxon.ConfigInit.CONFIGURATION_DATATYPE_INT) | Defines an integer type. |
| [`maxon.ConfigInit.CONFIGURATION_DATATYPE_STRING`](maxon.ConfigInit.CONFIGURATION_DATATYPE_STRING.md#maxon.ConfigInit.CONFIGURATION_DATATYPE_STRING) | Defines a string type. |
| [`maxon.ConfigInit.CONFIGURATION_DATATYPE_STRING_C`](maxon.ConfigInit.CONFIGURATION_DATATYPE_STRING_C.md#maxon.ConfigInit.CONFIGURATION_DATATYPE_STRING_C) | Defines a pointer type. |
| [`maxon.ConfigInit.default`](maxon.ConfigInit.default.md#maxon.ConfigInit.default) | Stores the default value. |
| [`maxon.ConfigInit.helpText`](maxon.ConfigInit.helpText.md#maxon.ConfigInit.helpText) | A help text to know why this config is used for. |
| [`maxon.ConfigInit.key`](maxon.ConfigInit.key.md#maxon.ConfigInit.key) | The key representing the value into the maxon.config dict. |
| [`maxon.ConfigInit.maxValue`](maxon.ConfigInit.maxValue.md#maxon.ConfigInit.maxValue) | Stores the maximum value possible. |
| [`maxon.ConfigInit.minValue`](maxon.ConfigInit.minValue.md#maxon.ConfigInit.minValue) | Stores the minimal value possible. |
| [`maxon.ConfigInit.type`](maxon.ConfigInit.type.md#maxon.ConfigInit.type) | Stores the type of the entry (bool, int, float, string). |
| [`maxon.ConfigInit.value`](maxon.ConfigInit.value.md#maxon.ConfigInit.value) | The value stored for the key into the the maxon.config dict. |
