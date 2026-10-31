<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/core/maxon.UuidInterface.html -->

# maxon.UuidInterface <a id="maxon-uuidinterface"></a>

## Description <a id="module-maxon.UuidInterface"></a><a id="description"></a>

## Inheritance diagram <a id="inheritance-diagram"></a>

Child Class:

- [`maxon.Uuid`](../../references/core/maxon.Uuid.md#module-maxon.Uuid)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Alloc`](#maxon.UuidInterface.Alloc)([obj]) | Create a new Uuid. |
| [`AllocEmpty`](#maxon.UuidInterface.AllocEmpty)() | Return a new Uuid. |
| [`AllocFromString`](#maxon.UuidInterface.AllocFromString)(uuidStr) | Create a new Uuid based on a string representing a valid Uuid. |
| [`AllocFromUuid`](#maxon.UuidInterface.AllocFromUuid)(uuid) | Return a copy of the passed Uuid. |
| [`Compare`](#maxon.UuidInterface.Compare)() | Compares the uuid against another uuid. |
| [`CreateId`](#maxon.UuidInterface.CreateId)() | Creates a new uuid. |
| [`CreateUuidString`](#maxon.UuidInterface.CreateUuidString)() | Creates a new uuid and returns the string of it. |
| [`DescribeIO`](#maxon.UuidInterface.DescribeIO)(stream) | Describes all elements of this class for I/O operations. |
| [`GetHashCode`](#maxon.UuidInterface.GetHashCode)() | Returns the hash code of the uuid. |
| [`IsEmpty`](#maxon.UuidInterface.IsEmpty)() | Returns whether the object is empty or not. |
| [`IsPopulated`](#maxon.UuidInterface.IsPopulated)() | Returns whether the object is populated or not. |
| [`Set`](#maxon.UuidInterface.Set)(uuid) | Sets a given uuid string. |
| [`ToString`](#maxon.UuidInterface.ToString)() | Converts the uuid into a string. |

## Methods Definition <a id="methods-definition"></a>

### *static* `UuidInterface.Alloc(obj=None)` <a id="maxon.UuidInterface.Alloc"></a>

Create a new Uuid.

**Parameters:** **uuid** (*Union*[*None*, *SourceLocation*, *String*, *str*, *Uuid*]) – None if a totally new Uuid should be returned otherwise a copy will be performed.

**Return type:** [`maxon.Uuid`](../../references/core/maxon.Uuid.md#module-maxon.Uuid)

**Returns:** The newly created Uuid.

### *static* `UuidInterface.AllocEmpty()` <a id="maxon.UuidInterface.AllocEmpty"></a>

Return a new Uuid.

**Return type:** [`maxon.Uuid`](../../references/core/maxon.Uuid.md#module-maxon.Uuid)

**Returns:** The newly created Uuid.

### *static* `UuidInterface.AllocFromString(uuidStr)` <a id="maxon.UuidInterface.AllocFromString"></a>

Create a new Uuid based on a string representing a valid Uuid.

**Parameters:** **uuid** (*str*) – The sting to copy to an Uuid.

**Return type:** [`maxon.Uuid`](../../references/core/maxon.Uuid.md#module-maxon.Uuid)

**Returns:** The newly created Uuid.

### *static* `UuidInterface.AllocFromUuid(uuid)` <a id="maxon.UuidInterface.AllocFromUuid"></a>

Return a copy of the passed Uuid.

**Parameters:** **uuid** ([`maxon.Uuid`](../../references/core/maxon.Uuid.md#module-maxon.Uuid)) – The uuid to copy.

**Return type:** [`maxon.Uuid`](../../references/core/maxon.Uuid.md#module-maxon.Uuid)

**Returns:** The newly created Uuid.

### `UuidInterface.Compare()` <a id="maxon.UuidInterface.Compare"></a>

Compares the uuid against another uuid.

**Parameters:** **uuid** ([`maxon.Uuid`](../../references/core/maxon.Uuid.md#module-maxon.Uuid)) – The uuid to compare with.

**Return type:** maxon.COMPARERESULT

**Returns:** See COMPARERESULT.

### `UuidInterface.CreateId()` <a id="maxon.UuidInterface.CreateId"></a>

Creates a new uuid.

**Return type:** [`maxon.Uuid`](../../references/core/maxon.Uuid.md#module-maxon.Uuid)

**Returns:** The newly created Uuid.

### *static* `UuidInterface.CreateUuidString()` <a id="maxon.UuidInterface.CreateUuidString"></a>

Creates a new uuid and returns the string of it.

**Return type:** [`maxon.Uuid`](../../references/core/maxon.Uuid.md#module-maxon.Uuid)

**Returns:** The newly created Uuid.

### *static* `UuidInterface.DescribeIO(stream)` <a id="maxon.UuidInterface.DescribeIO"></a>

Describes all elements of this class for I/O operations.

**Parameters:** **stream** (`maxon.DataSerializeInterface`) – The stream that is used to register the class members.

### `UuidInterface.GetHashCode()` <a id="maxon.UuidInterface.GetHashCode"></a>

Returns the hash code of the uuid.

> **Note:** The return value is 0 if the object IsEmpty().

**Return type:** int

### `UuidInterface.IsEmpty()` <a id="maxon.UuidInterface.IsEmpty"></a>

Returns whether the object is empty or not.  
A Uuid is empty if it hasn’t been constructed yet, or if a copy operation on the object failed, or if it just contains 0-values.

**Returns:** Returns whether the object is empty or not.

**Return type:** bool

### `UuidInterface.IsPopulated()` <a id="maxon.UuidInterface.IsPopulated"></a>

Returns whether the object is populated or not.  
Always the opposite of IsEmpty().

**Returns:** Returns whether the object is populated or not.

**Return type:** bool

### `UuidInterface.Set(uuid)` <a id="maxon.UuidInterface.Set"></a>

Sets a given uuid string. The id must be of the format “00000000-0000-0000-0000-000000000000”.

**Parameters:** **uuid** (*Union*[*str*, *StringInterface*]) – String with a valid uuid.

**Raises:** **IllegalArgumentError** – if the id could not be parsed.

### `UuidInterface.ToString()` <a id="maxon.UuidInterface.ToString"></a>

Converts the uuid into a string.  
The format will be “00000000-0000-0000-0000-000000000000” and the letters will be uppercase.

**Returns:** String representation of the uuid.

**Return type:** str
