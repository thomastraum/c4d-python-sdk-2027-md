<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/references/core/maxon.Uuid.html -->

# maxon.Uuid <a id="maxon-uuid"></a>

## Description <a id="module-maxon.Uuid"></a><a id="description"></a>

Reference class of [`maxon.UuidInterface`](../../interfaces/core/maxon.UuidInterface.md#module-maxon.UuidInterface).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.UuidInterface`](../../interfaces/core/maxon.UuidInterface.md#module-maxon.UuidInterface)
- [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Create`](#maxon.Uuid.Create)([uuid]) | Create a new Uuid. |
| [`__init__`](#maxon.Uuid.__init__)([obj]) | Initialize self. |

## Methods Definition <a id="methods-definition"></a>

### *classmethod* `Uuid.Create(uuid=None)` <a id="maxon.Uuid.Create"></a>

Create a new Uuid.

**Parameters:** **uuid** (*Union*[*None*, *SourceLocation*, *String*, *str*, *Uuid*]) – None if a totally new Uuid should be returned otherwise a copy will be performed.

**Return type:** [`maxon.Uuid`](#module-maxon.Uuid)

**Returns:** The newly created Uuid.

### `Uuid.__init__(obj=None)` <a id="maxon.Uuid.__init__"></a>

Initialize self. See help(type(self)) for accurate signature.
