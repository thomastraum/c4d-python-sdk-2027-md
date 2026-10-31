<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/decorators/registry/maxon.MAXON_COMPONENT.html -->

# maxon.MAXON_COMPONENT <a id="maxon-maxon-component"></a>

## `maxon.MAXON_COMPONENT(kind=ClassInterface.KIND.NORMAL, *ARGS)` <a id="maxon.MAXON_COMPONENT"></a>

Decorator to mark an element as a Maxon API component (available from a registry)

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

**Parameters:**

- **kind** (`maxon.ClassInterface.KIND`) – The kind of interface to be exposed
- **ARGS** – [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data).

**Returns:** The component object
