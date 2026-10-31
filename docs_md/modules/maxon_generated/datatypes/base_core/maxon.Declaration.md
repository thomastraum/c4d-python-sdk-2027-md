<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/base_core/maxon.Declaration.html -->

# maxon.Declaration <a id="maxon-declaration"></a>

## Description <a id="module-maxon.Declaration"></a><a id="description"></a>

Maxon API rely on object that are declared. Such object are stored under a [`maxon.Declaration`](#module-maxon.Declaration) object.

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetId`](#maxon.Declaration.GetId)() | Retrieves the Id of the declaration |
| [`__call__`](#maxon.Declaration.__call__)() | Call self as a function. |
| [`__init__`](#maxon.Declaration.__init__)(ids[, entityBaseType, returnType]) | Initialize self. |

## Methods Definition <a id="methods-definition"></a>

### `Declaration.GetId()` <a id="maxon.Declaration.GetId"></a>

Retrieves the Id of the declaration

**Returns:** The declaration id

**Return type:** [`maxon.InternedId`](../id/maxon.InternedId.md#module-maxon.InternedId)

### `Declaration.__call__()` <a id="maxon.Declaration.__call__"></a>

Call self as a function.

### `Declaration.__init__(ids, entityBaseType=None, returnType=None)` <a id="maxon.Declaration.__init__"></a>

Initialize self. See help(type(self)) for accurate signature.
