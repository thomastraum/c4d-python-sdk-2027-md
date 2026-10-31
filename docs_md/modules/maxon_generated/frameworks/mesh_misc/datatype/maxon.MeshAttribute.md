<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/mesh_misc/datatype/maxon.MeshAttribute.html -->

# maxon.MeshAttribute <a id="maxon-meshattribute"></a>

## Description <a id="module-maxon.MeshAttribute"></a><a id="description"></a>

A simple wrapper class which contains a data pointer and a reference to the MeshAttribute implementation class.  
Implements all the arithmetic operators to simplify usage independently of the data type itself.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Struct`](../../../datatypes/base_core/maxon.Struct.md#module-maxon.Struct)
- [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`__init__`](#maxon.MeshAttribute.__init__)(cls[, valuePtr]) | Initialize a Mesh Attribute. |

## Methods Definition <a id="methods-definition"></a>

### `MeshAttribute.__init__(cls, valuePtr=None)` <a id="maxon.MeshAttribute.__init__"></a>

Initialize a Mesh Attribute.

**Parameters:**

- **cls** ([`maxon.MeshAttributeClassInterface`](../interface/maxon.MeshAttributeClassInterface.md#module-maxon.MeshAttributeClassInterface)) – The MeshAttributeClass to implement
- **valuePtr** ([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The data to holds.
