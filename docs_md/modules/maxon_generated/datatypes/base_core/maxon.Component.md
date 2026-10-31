<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/base_core/maxon.Component.html -->

# maxon.Component <a id="maxon-component"></a>

## `maxon.Component(*INTERFACES)` <a id="maxon.Component"></a>

A component implements the functions of a given interface.  
Different implementations of the same interface define different components.  
Since these different implementations implement the functionality of the same interface they may have a lot of code in common.  
To reduce redundant code it is possible to define a base component that can be reused in different implementations.

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

**Parameters:** **INTERFACES** – [`maxon.Data`](maxon.Data.md#module-maxon.Data).
