<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/base_core/maxon.UnknownDataType.html -->

# maxon.UnknownDataType <a id="maxon-unknowndatatype"></a>

## Description <a id="module-maxon.UnknownDataType"></a><a id="description"></a>

Class for all data objects, that have no proper wrapper class in Python. This can happen, if a function returns an instance of an object, that is unknown to Python. To still be able to receive the object, an instance of this class is returned instead. It’s use is limited, since Python doesn’t know, how the underlying object looks like, or which functions it has on the C++ side. However, it can be automatically passed to a function, which accepts an object which matches the data type of it. If the data type of the object got registered via MAXON_DATATYPE_REGISTER_STRUCT on the C++ side, you can use UnknownDataType.MaxonConvert() to convert its members to a dict. The dict can alternatively be used then to pass to a function that expects a type of this object.

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](maxon.Data.md#module-maxon.Data)
- [`maxon.Struct`](maxon.Struct.md#module-maxon.Struct)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetId`](#maxon.UnknownDataType.GetId)() | Retrieves the [`maxon.Id`](../id/maxon.Id.md#module-maxon.Id) of the current Data. |
| [`GetType`](#maxon.UnknownDataType.GetType)() | Returns the data type of the underlying data object. |
| [`MaxonConvert`](#maxon.UnknownDataType.MaxonConvert)([expected]) | If the data type of the underlying object is a ‘known’ struct, the object will be converted |
| [`__str__`](#maxon.UnknownDataType.__str__)() | Returns the string representation of a data. |

## Methods Definition <a id="methods-definition"></a>

### `UnknownDataType.GetId()` <a id="maxon.UnknownDataType.GetId"></a>

Retrieves the [`maxon.Id`](../id/maxon.Id.md#module-maxon.Id) of the current Data.

**Returns:** The [`maxon.Id`](../id/maxon.Id.md#module-maxon.Id) of the current Data holds by the current [`maxon.UnknownDataType`](#module-maxon.UnknownDataType) instance.

**Return type:** [`maxon.Id`](../id/maxon.Id.md#module-maxon.Id)

### `UnknownDataType.GetType()` <a id="maxon.UnknownDataType.GetType"></a>

Returns the data type of the underlying data object. This function overwrites maxon.Data.GetType() because the data type of UnknownDataType would be returned instead.

**Returns:** Data type of the underlying data type.

**Return type:** [`maxon.DataType`](maxon.DataType.md#module-maxon.DataType)

### `UnknownDataType.MaxonConvert(expected=dict)` <a id="maxon.UnknownDataType.MaxonConvert"></a>

If the data type of the underlying object is a ‘known’ struct, the object will be converted to a dict, where each key and value matches the name and values of the C++ struct.  
A ‘known struct’ is a data type, that got registered via MAXON_DATATYPE_REGISTER_STRUCT in the originated C++ module. If no proper conversion can be found, self will be returned.

**Returns:** Converted object or self if the datatype is not registered internally as a struct via MAXON_DATATYPE_REGISTER_STRUCT.

**Return type:** Union[Self, dict]

### `UnknownDataType.__str__()` <a id="maxon.UnknownDataType.__str__"></a>

Returns the string representation of a data.

**Return type:** str
