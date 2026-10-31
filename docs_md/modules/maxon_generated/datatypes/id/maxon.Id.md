<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/id/maxon.Id.html -->

# maxon.Id <a id="maxon-id"></a>

## Description <a id="module-maxon.Id"></a><a id="description"></a>

[`maxon.Id`](#module-maxon.Id) represents an identifier consisting of a c-string.

Such identifiers are used mainly to identify entities such as interfaces, components, classes, registries, entries, modules or published objects.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Builtin`](../base_core/maxon.Builtin.md#module-maxon.Builtin)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`__add__`](#maxon.Id.__add__)(other) | Returns a new string by adding *other* string representation to the current string value. |
| [`__eq__`](#maxon.Id.__eq__)(other) | Checks if other string value is equal to the current value`. |
| [`__hash__`](#maxon.Id.__hash__)() | Returns the hash code of a data. |
| [`__init__`](#maxon.Id.__init__)([C]) | Initializes an [`maxon.Id`](#module-maxon.Id) with the passed data, if a maxon.Data is passed a copy is done. |
| [`__iter__`](#maxon.Id.__iter__)() | Iterates the string representation. |
| [`__len__`](#maxon.Id.__len__)() | Returns the string length of the [`maxon.Id`](#module-maxon.Id). |
| [`__ne__`](#maxon.Id.__ne__)(other) | Checks if other string value is unequal to the current value`. |
| [`__radd__`](#maxon.Id.__radd__)(other) | Returns a new string by adding *other* string representation to the current string value. |

## Methods Definition <a id="methods-definition"></a>

### `Id.__add__(other)` <a id="maxon.Id.__add__"></a>

Returns a new string by adding *other* string representation to the current string value.

**Parameters:** **other** (Union[str, [`maxon.Id`](#module-maxon.Id), [`maxon.InternedId`](maxon.InternedId.md#module-maxon.InternedId)]) – The other string value to add to the current id.

**Returns:** The new concatenated string.

**Return type:** str

### `Id.__eq__(other)` <a id="maxon.Id.__eq__"></a>

Checks if other string value is equal to the current value`.

**Parameters:** **other** (Union[str, [`maxon.String`](../../references/core/maxon.String.md#module-maxon.String) [`maxon.Id`](#module-maxon.Id), [`maxon.InternedId`](maxon.InternedId.md#module-maxon.InternedId)]) – The other identifier to compare.

**Returns:** **True** if other is equal to the current value, otherwise **False**.

**Return type:** bool

### `Id.__hash__()` <a id="maxon.Id.__hash__"></a>

Returns the hash code of a data.

### `Id.__init__(C=None)` <a id="maxon.Id.__init__"></a>

Initializes an [`maxon.Id`](#module-maxon.Id) with the passed data, if a maxon.Data is passed a copy is done.

**Parameters:** **C** (Optional[[`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)]) – The input data to derive the [`maxon.Id`](#module-maxon.Id).

### `Id.__iter__()` <a id="maxon.Id.__iter__"></a>

Iterates the string representation.

### `Id.__len__()` <a id="maxon.Id.__len__"></a>

Returns the string length of the [`maxon.Id`](#module-maxon.Id).

**Returns:** String length of the current [`maxon.Id`](#module-maxon.Id).

**Return type:** int

### `Id.__ne__(other)` <a id="maxon.Id.__ne__"></a>

Checks if other string value is unequal to the current value`.

**Parameters:** **other** (Union[str, [`maxon.String`](../../references/core/maxon.String.md#module-maxon.String) [`maxon.Id`](#module-maxon.Id), [`maxon.InternedId`](maxon.InternedId.md#module-maxon.InternedId)]) – The other identifier to compare.

**Returns:** **True** if other is unequal to the current value, otherwise **False**.

**Return type:** bool

### `Id.__radd__(other)` <a id="maxon.Id.__radd__"></a>

Returns a new string by adding *other* string representation to the current string value.

**Parameters:** **other** (Union[str, [`maxon.Id`](#module-maxon.Id), [`maxon.InternedId`](maxon.InternedId.md#module-maxon.InternedId)]) – The other string value to add to the current id.

**Returns:** The new concatenated string.

**Return type:** str
