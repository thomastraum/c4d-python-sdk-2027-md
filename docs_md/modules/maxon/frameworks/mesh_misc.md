<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon/frameworks/mesh_misc.html -->

# maxon.frameworks.mesh_misc <a id="maxon-frameworks-mesh-misc"></a><a id="framework-mesh-misc"></a>

> **Note:** Members documented here are defined in `maxon.frameworks.mesh_misc` module and are also exposed to the global `maxon` module. See the [Maxon API](../../../manuals/manual_api_overview.md#maxon-api-introduction) section of the API Overview for more information about the special conventions of this API.

## Description <a id="description"></a>

Module for mesh attributes.

## Interfaces <a id="interfaces"></a>

|   |   |
|---|---|
| [`MeshAttributeClassInterface`](../../maxon_generated/frameworks/mesh_misc/interface/maxon.MeshAttributeClassInterface.md#module-maxon.MeshAttributeClassInterface)(*args) | By implementing this interface, it is possible to define a new mesh attribute type. |
| [`CustomDataTagDisplayInterface`](../../maxon_generated/frameworks/mesh_misc/interface/maxon.CustomDataTagDisplayInterface.md#module-maxon.CustomDataTagDisplayInterface)(*args) | [`maxon.CustomDataTagDisplayInterface`](../../maxon_generated/frameworks/mesh_misc/interface/maxon.CustomDataTagDisplayInterface.md#module-maxon.CustomDataTagDisplayInterface) can be optionally implemented for each [`maxon.CustomDataTagClassInterface`](../../maxon_generated/frameworks/mesh_misc/interface/maxon.CustomDataTagClassInterface.md#module-maxon.CustomDataTagClassInterface) implementation and defines if and how a `c4d.CustomDataTag` should be displayed in the viewport. |
| [`CustomDataTagClassInterface`](../../maxon_generated/frameworks/mesh_misc/interface/maxon.CustomDataTagClassInterface.md#module-maxon.CustomDataTagClassInterface)(*args) | [`maxon.CustomDataTagClassInterface`](../../maxon_generated/frameworks/mesh_misc/interface/maxon.CustomDataTagClassInterface.md#module-maxon.CustomDataTagClassInterface) uses |

## References <a id="references"></a>

|   |   |
|---|---|
| [`CustomDataTagDisplayRef`](../../maxon_generated/frameworks/mesh_misc/reference/maxon.CustomDataTagDisplayRef.md#module-maxon.CustomDataTagDisplayRef)(*args) | Represents a reference of a [`maxon.CustomDataTagDisplayInterface`](../../maxon_generated/frameworks/mesh_misc/interface/maxon.CustomDataTagDisplayInterface.md#module-maxon.CustomDataTagDisplayInterface) |
| [`CustomDataTagClass`](../../maxon_generated/frameworks/mesh_misc/reference/maxon.CustomDataTagClass.md#module-maxon.CustomDataTagClass)(*args) | Represents a reference of a [`maxon.CustomDataTagClassInterface`](../../maxon_generated/frameworks/mesh_misc/interface/maxon.CustomDataTagClassInterface.md#module-maxon.CustomDataTagClassInterface) |

## Data Types <a id="data-types"></a>

|   |   |
|---|---|
| [`MeshAttribute`](../../maxon_generated/frameworks/mesh_misc/datatype/maxon.MeshAttribute.md#module-maxon.MeshAttribute)(cls[, valuePtr]) | A simple wrapper class which contains a data pointer and a reference to the MeshAttribute implementation class. |

## Registries <a id="registries"></a>

|   |   |
|---|---|
| [`CustomDataTagDisplayClasses`](../../maxon_generated/frameworks/mesh_misc/registry/maxon.CustomDataTagDisplayClasses.md#module-maxon.CustomDataTagDisplayClasses)() | Registry storing all [`maxon.CustomDataTagDisplayInterface`](../../maxon_generated/frameworks/mesh_misc/interface/maxon.CustomDataTagDisplayInterface.md#module-maxon.CustomDataTagDisplayInterface). |

## Decorators <a id="decorators"></a>

|   |   |
|---|---|
| [`MAXON_MESHATTRIBUTE`](../../maxon_generated/frameworks/mesh_misc/decorator/maxon.MAXON_MESHATTRIBUTE.md#maxon.MAXON_MESHATTRIBUTE)(T) | A compatible [`maxon.DataType`](../../maxon_generated/datatypes/base_core/maxon.DataType.md#module-maxon.DataType) must be defined for each |
