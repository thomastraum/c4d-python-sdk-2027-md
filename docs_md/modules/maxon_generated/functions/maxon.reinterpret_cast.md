<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/functions/maxon.reinterpret_cast.html -->

# maxon.reinterpret_cast <a id="maxon-reinterpret-cast"></a>

## `maxon.reinterpret_cast(T, o)` <a id="maxon.reinterpret_cast"></a>

Cast(T, o) Cast the object *o* to the type *T*.

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.  
> Use [`maxon.MaxonConvert()`](maxon.MaxonConvert.md#maxon.MaxonConvert) instead.

**Parameters:**

- **T** (*type*) – The type to cast the object to.
- **o** ([`maxon.Data`](../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The Initial object

**Returns:** The casted object

**Return type:** T
