<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/functions/maxon.MaxonConvert.html -->

# maxon.MaxonConvert <a id="maxon-maxonconvert"></a>

## `maxon.MaxonConvert(*args)` <a id="maxon.MaxonConvert"></a>

Convert all passed objects to a maxon or Python object, depending on the passed type.

> **Note:** Latest arguments determine how the conversion is done by passing a `maxon.CONVERSIONMODE`.

```python
import maxon

# Returns a maxon.Int32 of value 10
print maxon.MaxonConvert(10)

# Returns a int of value 10
print maxon.MaxonConvert(maxon.Int(10))

# Forces a return value to Maxon API type, in this case a maxon.Int32 of value 10
print maxon.MaxonConvert(maxon.Int(10), maxon.CONVERSIONMODE.TOMAXON)

# Forces a return value to Python Builtin, in this case a int of value 10
print maxon.MaxonConvert(10, maxon.CONVERSIONMODE.TOBUILTIN)
```

**Parameters:** **args** (*Any*) – The object to converts.

**Returns:** The object converted

**Return type:** Any
