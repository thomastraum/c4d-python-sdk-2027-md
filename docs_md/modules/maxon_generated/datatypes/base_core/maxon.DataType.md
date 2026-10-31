<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/base_core/maxon.DataType.html -->

# maxon.DataType <a id="maxon-datatype"></a>

## Description <a id="module-maxon.DataType"></a><a id="description"></a>

**[`maxon.DataType`](#module-maxon.DataType) provides a set of functions which allow to operate on values of arbitrary** types in a generic way.

Each type needs its own [`maxon.DataType`](#module-maxon.DataType) with specific implementations of the access functions. The [`maxon.Data`](maxon.Data.md#module-maxon.Data) class uses [`maxon.DataType`](#module-maxon.DataType) to be able to store values of arbitrary type.

There are primary data types and compound data types. A primary data type is registered at the DataTypes registry. A compound data type is for example:

> - a pointer or reference type of another type,
> - a block type of another type,
> - a result type of another type,
> - an array type of another type,
> - a tuple data type composed of a set of member types. Compound data types are typically created as instantiations of parametric types.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`CheckValueKind`](#maxon.DataType.CheckValueKind)(test) | Tests the value kind of this data type for the given flags (by using the bitwise and). |
| [`Create`](#maxon.DataType.Create)() | Creates a new instance of this type. |
| [`Get`](#maxon.DataType.Get)() | Retrieves a [`maxon.DataType`](#module-maxon.DataType) from its [`maxon.Id`](../id/maxon.Id.md#module-maxon.Id) |
| [`GetAlignment`](#maxon.DataType.GetAlignment)() | Returns the alignment of values of this data type. |
| [`GetArrayType`](#maxon.DataType.GetArrayType)() | Retrieves the kind of BaseArray used. |
| [`GetBaseArrayType`](#maxon.DataType.GetBaseArrayType)() | Retrieves the kind of BaseArray used. |
| [`GetConstType`](#maxon.DataType.GetConstType)() | Retrieves the constant type of the current type. |
| [`GetDataTypeType`](#maxon.DataType.GetDataTypeType)() |  |
| [`GetElementType`](#maxon.DataType.GetElementType)() | Returns the element type of this data type. |
| [`GetId`](#maxon.DataType.GetId)() | Returns the identifier of this data type. |
| [`GetNativeType`](#maxon.DataType.GetNativeType)() | Returns the initial DataType. |
| [`GetPointerType`](#maxon.DataType.GetPointerType)() | Retrieves the pointer type of the current type. |
| [`GetSize`](#maxon.DataType.GetSize)() | Returns the size of values of this data type. |
| [`GetType`](#maxon.DataType.GetType)() | Returns the DataType of the current object. |
| [`GetTypeArguments`](#maxon.DataType.GetTypeArguments)() | Returns the type arguments of this data type. |
| [`GetUnderlyingType`](#maxon.DataType.GetUnderlyingType)() | Returns the most atomic way for describing a parameter. |
| [`GetUnqualifiedType`](#maxon.DataType.GetUnqualifiedType)() | Returns the description of a parameter. |
| [`GetValueKind`](#maxon.DataType.GetValueKind)() | Returns the kind of values of this data type. |
| [`Is`](#maxon.DataType.Is)(dt) | Returns true if this type is the same as dt. |
| [`IsGeneric`](#maxon.DataType.IsGeneric)() | Checks if the DataType is a Generic one. |
| [`NullValue`](#maxon.DataType.NullValue)() |  |
| [`ToString`](#maxon.DataType.ToString)() | Returns the String representation of the datatype. |
| [`__eq__`](#maxon.DataType.__eq__)(other) | Checks if two datatypes are equal. |
| [`__init__`](#maxon.DataType.__init__)(dt) | Initializes a datatype with the data type retrieved from [`maxon.DataType.Get()`](#maxon.DataType.Get). |
| [`__repr__`](#maxon.DataType.__repr__)() | Returns the string representation of a data. |
| [`__str__`](#maxon.DataType.__str__)() | Return str(self). |

## Methods Definition <a id="methods-definition"></a>

### `DataType.CheckValueKind(test)` <a id="maxon.DataType.CheckValueKind"></a>

Tests the value kind of this data type for the given flags (by using the bitwise and).

**Parameters:** **test** (`maxon.VALUEKIND`) – The flags to test.

**Returns:** **True** if the value kind of this data type has one of the given flags, **False** otherwise.

**Return type:** bool

### `DataType.Create()` <a id="maxon.DataType.Create"></a>

Creates a new instance of this type.  
If this type is a non-virtual interface, the new instance will be created by NewObj.  
If this type is an array type TO BE DONE.  
If this type is a virtual interface type, an error is returned because only classes can be instantiated, not interfaces.  
Otherwise, the new instance will be initialized by the default constructor. For reference types, this means that the reference will point to nullptr.

**Returns:** New instance of this data type. The caller owns the new instance.

**Return type:** Any

### *static* `DataType.Get()` <a id="maxon.DataType.Get"></a>

Retrieves a [`maxon.DataType`](#module-maxon.DataType) from its [`maxon.Id`](../id/maxon.Id.md#module-maxon.Id)

**Parameters:**

- **id** (*str*) – The id of the datatype to search for.
- **lookupPythonTypes** (*bool*) – **True** to look also in the python built-in datatype.

**Returns:** The matched datatype.

**Type:** [`maxon.DataType`](#module-maxon.DataType)

**Raise:** TypeError: If the id is not a str.

### `DataType.GetAlignment()` <a id="maxon.DataType.GetAlignment"></a>

Returns the alignment of values of this data type. This might by an extended alignment.

**Returns:** Alignment of values.

**Return type:** int

### `DataType.GetArrayType()` <a id="maxon.DataType.GetArrayType"></a>

Retrieves the kind of BaseArray used.

**Returns:** The DataType of the BaseArray.

**Return type:** [`maxon.DataType`](#module-maxon.DataType)

### `DataType.GetBaseArrayType()` <a id="maxon.DataType.GetBaseArrayType"></a>

Retrieves the kind of BaseArray used.

**Returns:** The DataType of the BaseArray.

**Return type:** [`maxon.DataType`](#module-maxon.DataType)

### `DataType.GetConstType()` <a id="maxon.DataType.GetConstType"></a>

Retrieves the constant type of the current type.

**Returns:** The constant DataType.

**Return type:** [`maxon.DataType`](#module-maxon.DataType)

### *static* `DataType.GetDataTypeType()` <a id="maxon.DataType.GetDataTypeType"></a>

### `DataType.GetElementType()` <a id="maxon.DataType.GetElementType"></a>

Returns the element type of this data type. The element type is used for some parametric types such as pointers or references,

**Returns:** The DataType of the stored elements. Can be **None**.

**Return type:** [`maxon.DataType`](#module-maxon.DataType)

### `DataType.GetId()` <a id="maxon.DataType.GetId"></a>

Returns the identifier of this data type.  
Data type identifiers of primary types look like int32, pointer types are identified by a * suffix as in {float64*}, tuple types by a parenthesized list of its member types as in {(int32,float64*)}.

**Returns:** Unique identifier of this type.

**Return type:** [`maxon.Id`](../id/maxon.Id.md#module-maxon.Id)

### `DataType.GetNativeType()` <a id="maxon.DataType.GetNativeType"></a>

Returns the initial DataType.

**Returns:** The datatype.

**Return type:** [`maxon.DataType`](#module-maxon.DataType)

### `DataType.GetPointerType()` <a id="maxon.DataType.GetPointerType"></a>

Retrieves the pointer type of the current type.

**Returns:** The pointer DataType.

**Return type:** [`maxon.DataType`](#module-maxon.DataType)

### `DataType.GetSize()` <a id="maxon.DataType.GetSize"></a>

Returns the size of values of this data type.

**Returns:** Size of values.

**Return type:** int

### *classmethod* `DataType.GetType()` <a id="maxon.DataType.GetType"></a>

Returns the DataType of the current object.

**Returns:** The datatype.

**Return type:** [`maxon.DataType`](#module-maxon.DataType)

### `DataType.GetTypeArguments()` <a id="maxon.DataType.GetTypeArguments"></a>

Returns the type arguments of this data type.  
Type arguments are set for some instantiations of parametric types.  
For example, the 3-dimensional Vector is an instantiation of the parametric type Vec with the arguments (Float, 3).

**Returns:** The type arguments of this type.

**Return type:** list(tuple(type, name))

### `DataType.GetUnderlyingType()` <a id="maxon.DataType.GetUnderlyingType"></a>

Returns the most atomic way for describing a parameter.  
e.g: for a ColorA it’s “(float64 r,float64 g,float64 b,float64 a)”

**Returns:** The underlying DataType.

**Return type:** [`maxon.DataType`](#module-maxon.DataType)

### `DataType.GetUnqualifiedType()` <a id="maxon.DataType.GetUnqualifiedType"></a>

Returns the description of a parameter.  
e.g: for a ColorA it’s “net.maxon.parametrictype.col<4,float64>”

**Returns:** The unqualified DataType.

**Return type:** [`maxon.DataType`](#module-maxon.DataType)

### `DataType.GetValueKind()` <a id="maxon.DataType.GetValueKind"></a>

Returns the kind of values of this data type. This is a coarse classification to distinguish between e.g. value types, pointers, references, arrays and tuples.

**Returns:** Kind of values.

**Return type:**

`maxon.VALUEKIND`

### `DataType.Is(dt)` <a id="maxon.DataType.Is"></a>

Returns true if this type is the same as dt.

**Parameters:** **dt** ([`maxon.DataType`](#module-maxon.DataType)) – Type to compare.

**Returns:** **True** if this type is the same.

**Return type:** bool

### `DataType.IsGeneric()` <a id="maxon.DataType.IsGeneric"></a>

Checks if the DataType is a Generic one.

**Returns:** **True** if it’s a Generic.

**Return type:** bool

### *static* `DataType.NullValue()` <a id="maxon.DataType.NullValue"></a>

### `DataType.ToString()` <a id="maxon.DataType.ToString"></a>

Returns the String representation of the datatype.

**Returns:** The string representation of the DataType.

**Return type:** str

### `DataType.__eq__(other)` <a id="maxon.DataType.__eq__"></a>

Checks if two datatypes are equal.

**Parameters:** **other** (`maxon.Datatype`) – The other datatype.

**Return type:** bool

**Returns:** **True** if datatype are equal.

### `DataType.__init__(dt)` <a id="maxon.DataType.__init__"></a>

Initializes a datatype with the data type retrieved from [`maxon.DataType.Get()`](#maxon.DataType.Get).

**Parameters:** **dt** ([`maxon.DataType`](#module-maxon.DataType)) – The data type to store.

### `DataType.__repr__()` <a id="maxon.DataType.__repr__"></a>

Returns the string representation of a data.

**Return type:** str

### `DataType.__str__()` <a id="maxon.DataType.__str__"></a>

Return str(self).
