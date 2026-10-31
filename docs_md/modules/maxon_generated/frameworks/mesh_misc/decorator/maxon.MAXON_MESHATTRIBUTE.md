<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/mesh_misc/decorator/maxon.MAXON_MESHATTRIBUTE.html -->

# maxon.MAXON_MESHATTRIBUTE <a id="maxon-maxon-meshattribute"></a>

## `maxon.MAXON_MESHATTRIBUTE(T)` <a id="maxon.MAXON_MESHATTRIBUTE"></a>

A compatible [`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType) must be defined for each [`maxon.MeshAttributeClassInterface`](../interface/maxon.MeshAttributeClassInterface.md#module-maxon.MeshAttributeClassInterface).  
This Generator automatically generates a compatible data type out of the passed *T*.  
After this macro call, it is also necessary to declare and register the resulting DataType using MAXON_DATATYPE

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to use this decorator directly.

**Parameters:** **T** ([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The type to register.
