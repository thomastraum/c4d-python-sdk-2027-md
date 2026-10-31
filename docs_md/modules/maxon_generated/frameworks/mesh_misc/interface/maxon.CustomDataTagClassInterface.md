<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/mesh_misc/interface/maxon.CustomDataTagClassInterface.html -->

# maxon.CustomDataTagClassInterface <a id="maxon-customdatatagclassinterface"></a>

## Description <a id="module-maxon.CustomDataTagClassInterface"></a><a id="description"></a>

[`maxon.CustomDataTagClassInterface`](#module-maxon.CustomDataTagClassInterface) uses [`maxon.MeshAttributeClassInterface`](maxon.MeshAttributeClassInterface.md#module-maxon.MeshAttributeClassInterface) as a base interface and allows to add information and functionality to the mesh attribute to be used as tag.  
It mainly contains the information about the `c4d.CustomDataTag` registration, read/write, icons and the optional display implementation.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.MeshAttributeClassInterface`](maxon.MeshAttributeClassInterface.md#module-maxon.MeshAttributeClassInterface)

Child Class:

- [`maxon.CustomDataTagClass`](../reference/maxon.CustomDataTagClass.md#module-maxon.CustomDataTagClass)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetDefaultResourceId`](#maxon.CustomDataTagClassInterface.GetDefaultResourceId)() | By default, all implementations provide a standard UI. |
| [`GetDisplayClassId`](#maxon.CustomDataTagClassInterface.GetDisplayClassId)() | Get [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id) Id of the display implementation or an empty [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id) if display is not implemented. |
| [`GetIcon`](#maxon.CustomDataTagClassInterface.GetIcon)(perPolyVertex) | Gets the icon id according to the data location (per vertex vs. |
| [`GetResourceId`](#maxon.CustomDataTagClassInterface.GetResourceId)() | Returns the resource id for the Tag. |
| [`GetTagPluginId`](#maxon.CustomDataTagClassInterface.GetTagPluginId)() | Returns the Tag plugin ID to be registered with this implementation. |
| [`GetTagPluginLevel`](#maxon.CustomDataTagClassInterface.GetTagPluginLevel)() | Returns the Tag level to be used as data versioning system. |
| [`GetTagPluginName`](#maxon.CustomDataTagClassInterface.GetTagPluginName)() | Returns the Tag string name to be registered with this implementation. |
| [`IsSdsCompatible`](#maxon.CustomDataTagClassInterface.IsSdsCompatible)(floatSize) | Returns if the [`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType) is compatible with the SDS interpolation. |
| [`Read`](#maxon.CustomDataTagClassInterface.Read)(data, hf, level) | Reads a single data entry from a file. |
| [`Write`](#maxon.CustomDataTagClassInterface.Write)(data, hf) | **param data:** The data pointer. |

## Methods Definition <a id="methods-definition"></a>

### *static* `CustomDataTagClassInterface.GetDefaultResourceId()` <a id="maxon.CustomDataTagClassInterface.GetDefaultResourceId"></a>

By default, all implementations provide a standard UI. Gets the default resource id in case a custom AM UI is not needed.

**Returns:** The description string identifier.

**Return type:** str

### `CustomDataTagClassInterface.GetDisplayClassId()` <a id="maxon.CustomDataTagClassInterface.GetDisplayClassId"></a>

Get [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id) Id of the display implementation or an empty [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id) if display is not implemented.

**Returns:** The id of the associated display implementation.

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)

### `CustomDataTagClassInterface.GetIcon(perPolyVertex)` <a id="maxon.CustomDataTagClassInterface.GetIcon"></a>

Gets the icon id according to the data location (per vertex vs. per polyvertex).

**Parameters:** **perPolyVertex** (*bool*) – If True the polyvertex icon id is returned.

**Returns:** The icon id or c4d.NOTOK if there is no icon.

### `CustomDataTagClassInterface.GetResourceId()` <a id="maxon.CustomDataTagClassInterface.GetResourceId"></a>

Returns the resource id for the Tag.

**Returns:** A string that represent the tag res ID.

**Return type:** str

### `CustomDataTagClassInterface.GetTagPluginId()` <a id="maxon.CustomDataTagClassInterface.GetTagPluginId"></a>

Returns the Tag plugin ID to be registered with this implementation.

**Returns:** A unique plugin ID.

**Return type:** int

### `CustomDataTagClassInterface.GetTagPluginLevel()` <a id="maxon.CustomDataTagClassInterface.GetTagPluginLevel"></a>

Returns the Tag level to be used as data versioning system.

**Returns:** The disk level.

**Return type:** int

### `CustomDataTagClassInterface.GetTagPluginName()` <a id="maxon.CustomDataTagClassInterface.GetTagPluginName"></a>

Returns the Tag string name to be registered with this implementation.

**Returns:** A string that represent the tag in the interface.

**Return type:** str

### `CustomDataTagClassInterface.IsSdsCompatible(floatSize)` <a id="maxon.CustomDataTagClassInterface.IsSdsCompatible"></a>

Returns if the [`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType) is compatible with the SDS interpolation.  
SDS implementations, both internal and OSD, are only able to interpolate float values.  
The floatSize allows to define how many values are used for each entry, for example a vector will have a floatSize = 3.

**Parameters:** **floatSize** (*int*) – The number of float values that the datatype contains.

**Returns:** True if this interface can be processed for SDS interpolations.

**Return type:** bool

### `CustomDataTagClassInterface.Read(data, hf, level)` <a id="maxon.CustomDataTagClassInterface.Read"></a>

Reads a single data entry from a file.

**Parameters:**

- **data** (*Any*) – The data pointer.
- **hf** (`c4d.HyperFile`) – The file handle to read.
- **level** (*int*) – The disk level.

### `CustomDataTagClassInterface.Write(data, hf)` <a id="maxon.CustomDataTagClassInterface.Write"></a>

**Parameters:**

- **data** (*Any*) – The data pointer.
- **hf** (`c4d.HyperFile`) – The file handle to write on.
