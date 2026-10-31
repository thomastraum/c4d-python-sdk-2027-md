<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/core/maxon.DataDescriptionInterface.html -->

# maxon.DataDescriptionInterface <a id="maxon-datadescriptioninterface"></a>

## Description <a id="module-maxon.DataDescriptionInterface"></a><a id="description"></a>

## Inheritance diagram <a id="inheritance-diagram"></a>

Child Class:

- [`maxon.DataDescription`](../../references/core/maxon.DataDescription.md#module-maxon.DataDescription)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Compare`](#maxon.DataDescriptionInterface.Compare)(other) | Compares the 2 values. |
| [`DescribeIO`](#maxon.DataDescriptionInterface.DescribeIO)(*args) | Describes all elements of this class for I/O operations. |
| [`EraseEntry`](#maxon.DataDescriptionInterface.EraseEntry)(id) | Deletes a attribute from the description. |
| [`GetEntries`](#maxon.DataDescriptionInterface.GetEntries)() | Returns a array with all entries. |
| [`GetEntry`](#maxon.DataDescriptionInterface.GetEntry)(id) | Returns a specific entry with the given id. |
| [`GetEntryCount`](#maxon.DataDescriptionInterface.GetEntryCount)() | Returns the number of entries in the description. |
| [`GetHashCode`](#maxon.DataDescriptionInterface.GetHashCode)() | Returns the hashcode of the description. |
| [`GetInfo`](#maxon.DataDescriptionInterface.GetInfo)() | Returns the info dictionary. |
| [`IsEqual`](#maxon.DataDescriptionInterface.IsEqual)(other, equality) | Compares two descriptions. |
| [`Reset`](#maxon.DataDescriptionInterface.Reset)() | Resets the description and clear all attributes. |
| [`SetEntry`](#maxon.DataDescriptionInterface.SetEntry)(props[, merge]) | SetEntry description. |
| [`SetInfo`](#maxon.DataDescriptionInterface.SetInfo)(info) | The info dictionary of the description. |
| [`ToString`](#maxon.DataDescriptionInterface.ToString)() | Returns a readable string of the content. |

## Methods Definition <a id="methods-definition"></a>

### `DataDescriptionInterface.Compare(other)` <a id="maxon.DataDescriptionInterface.Compare"></a>

Compares the 2 values.

**Parameters:** **other** ([`maxon.DataDescriptionInterface`](#module-maxon.DataDescriptionInterface)) – Other description to compare.

### *static* `DataDescriptionInterface.DescribeIO(*args)` <a id="maxon.DataDescriptionInterface.DescribeIO"></a>

Describes all elements of this class for I/O operations.

**Parameters:** **stream** (`maxon.DataSerializeInterface`) – The stream that is used to register the class members.

### `DataDescriptionInterface.EraseEntry(id)` <a id="maxon.DataDescriptionInterface.EraseEntry"></a>

Deletes a attribute from the description.

**Parameters:** **id** ([`maxon.InternedId`](../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id) of the attribute to delete.

### `DataDescriptionInterface.GetEntries()` <a id="maxon.DataDescriptionInterface.GetEntries"></a>

Returns a array with all entries.

**Returns:** A array with all entries.

**Return type:** [`maxon.BaseArray`](../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)]

### `DataDescriptionInterface.GetEntry(id)` <a id="maxon.DataDescriptionInterface.GetEntry"></a>

Returns a specific entry with the given id.

**Parameters:** **id** ([`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Id to find.

**Returns:** DataDictionary on success. Error if the requested attribute was not in the description-

**Return type:** [`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)

### `DataDescriptionInterface.GetEntryCount()` <a id="maxon.DataDescriptionInterface.GetEntryCount"></a>

Returns the number of entries in the description.

**Returns:** The number of entries in the description.

**Return type:** int

### `DataDescriptionInterface.GetHashCode()` <a id="maxon.DataDescriptionInterface.GetHashCode"></a>

Returns the hashcode of the description.

**Returns:** The hashcode.

**Return type:** int

### `DataDescriptionInterface.GetInfo()` <a id="maxon.DataDescriptionInterface.GetInfo"></a>

Returns the info dictionary.

**Returns:** The info dictionary.

**Return type:** [`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary).

### `DataDescriptionInterface.IsEqual(other, equality)` <a id="maxon.DataDescriptionInterface.IsEqual"></a>

Compares two descriptions.

**Parameters:**

- **other** ([`maxon.DataDescriptionInterface`](#module-maxon.DataDescriptionInterface)) – Other description to compare.
- **equality** (`maxon.EQUALITY`) – See @EQUALITY.

**Returns:** True in equality.

**Return type:** bool

### `DataDescriptionInterface.Reset()` <a id="maxon.DataDescriptionInterface.Reset"></a>

Resets the description and clear all attributes.

### `DataDescriptionInterface.SetEntry(props, merge=False)` <a id="maxon.DataDescriptionInterface.SetEntry"></a>

SetEntry description.

**Parameters:**

- **props** ([`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – Properties to set. The DESCRIPTION.BASE.IDENTIFIER will be used as key for the hashmap.
- **merge** (*bool*) – **True** if the container should be merged with the existing props im the description. The given props will have priority over the existing.

**Returns:** **True** if properties has been changed.

**Return type:** bool

### `DataDescriptionInterface.SetInfo(info)` <a id="maxon.DataDescriptionInterface.SetInfo"></a>

The info dictionary of the description.

**Parameters:** **info** ([`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – Dictionary with infos.

### `DataDescriptionInterface.ToString()` <a id="maxon.DataDescriptionInterface.ToString"></a>

Returns a readable string of the content.

**Returns:** A readable string of the content.

**Return type:** str
