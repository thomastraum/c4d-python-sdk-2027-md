<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/mesh_misc/interface/maxon.MeshAttributeClassInterface.html -->

# maxon.MeshAttributeClassInterface <a id="maxon-meshattributeclassinterface"></a>

## Description <a id="module-maxon.MeshAttributeClassInterface"></a><a id="description"></a>

By implementing this interface, it is possible to define a new mesh attribute type.  
So that a data type can be attached to mesh vertices or to mesh polyvertices.  
The interface needs to be implemented with the data type description, which has to be registered using [`maxon.MAXON_MESHATTRIBUTE()`](../decorator/maxon.MAXON_MESHATTRIBUTE.md#maxon.MAXON_MESHATTRIBUTE) and `maxon.MAXON_DATATYPE`, and all arithmetic and comparison functions.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.CustomDataTagClassInterface`](maxon.CustomDataTagClassInterface.md#module-maxon.CustomDataTagClassInterface)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetDataType`](#maxon.MeshAttributeClassInterface.GetDataType)() | Returns the [`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType) this class manages, e.g. |
| [`InterpolateLinear`](#maxon.MeshAttributeClassInterface.InterpolateLinear)(data1, data2, blend) | Interpolates linearly between two values. |

## Methods Definition <a id="methods-definition"></a>

### `MeshAttributeClassInterface.GetDataType()` <a id="maxon.MeshAttributeClassInterface.GetDataType"></a>

Returns the [`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType) this class manages, e.g. `maxon.Vector2d32` for UV maps.

**Returns:** The DataType.

**Return type:** [`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType).

### `MeshAttributeClassInterface.InterpolateLinear(data1, data2, blend)` <a id="maxon.MeshAttributeClassInterface.InterpolateLinear"></a>

Interpolates linearly between two values. Both addresses need to be cast to the appropriate data type.

**Parameters:**

- **data1** (Same as [`maxon.MeshAttributeClassInterface.GetDataType()`](#maxon.MeshAttributeClassInterface.GetDataType)) – The first value.
- **data2** (Same as [`maxon.MeshAttributeClassInterface.GetDataType()`](#maxon.MeshAttributeClassInterface.GetDataType)) – The second value.
- **blend** (*float*) – The blend percentage [0.0..blend..1.0]
