<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/id/maxon.InternedId.html -->

# maxon.InternedId <a id="maxon-internedid"></a>

## Description <a id="module-maxon.InternedId"></a><a id="description"></a>

**[`maxon.InternedId`](#module-maxon.InternedId) represents an [`maxon.Id`](maxon.Id.md#module-maxon.Id) which has been interned into a pool of unique** [`maxon.Id`](maxon.Id.md#module-maxon.Id) objects.

I.e., there are no two different Id objects with an equal id string, so for equality comparison you can compare pointers instead of whole strings.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Builtin`](../base_core/maxon.Builtin.md#module-maxon.Builtin)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`__eq__`](#maxon.InternedId.__eq__)(other) | Checks if other interned string value is equal to the current value`. |
| [`__hash__`](#maxon.InternedId.__hash__)() | Returns the hash code of a data. |
| [`__init__`](#maxon.InternedId.__init__)([C]) | Initializes an [`maxon.InternedId`](#module-maxon.InternedId) with the passed data, if a maxon.Data is passed a copy is done. |
| [`__ne__`](#maxon.InternedId.__ne__)(other) | Checks if other interned string value is unequal to the current value`. |

## Methods Definition <a id="methods-definition"></a>

### `InternedId.__eq__(other)` <a id="maxon.InternedId.__eq__"></a>

Checks if other interned string value is equal to the current value`.

**Parameters:** **other** (Union[str, [`maxon.String`](../../references/core/maxon.String.md#module-maxon.String) [`maxon.Id`](maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](#module-maxon.InternedId)]) – The other identifier to compare.

**Returns:** **True** if other is equal to the current value, otherwise **False**.

**Return type:** bool

### `InternedId.__hash__()` <a id="maxon.InternedId.__hash__"></a>

Returns the hash code of a data.

### `InternedId.__init__(C=None)` <a id="maxon.InternedId.__init__"></a>

Initializes an [`maxon.InternedId`](#module-maxon.InternedId) with the passed data, if a maxon.Data is passed a copy is done.

**Parameters:** **C** (Optional[[`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)]) – The input data to derive the [`maxon.InternedId`](#module-maxon.InternedId).

### `InternedId.__ne__(other)` <a id="maxon.InternedId.__ne__"></a>

Checks if other interned string value is unequal to the current value`.

**Parameters:** **other** (Union[str, [`maxon.String`](../../references/core/maxon.String.md#module-maxon.String) [`maxon.Id`](maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](#module-maxon.InternedId)]) – The other identifier to compare.

**Returns:** **True** if other is unequal to the current value, otherwise **False**.

**Return type:** bool
