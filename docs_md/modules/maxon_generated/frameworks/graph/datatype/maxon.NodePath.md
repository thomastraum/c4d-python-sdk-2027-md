<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/graph/datatype/maxon.NodePath.html -->

# maxon.NodePath <a id="maxon-nodepath"></a>

## Description <a id="module-maxon.NodePath"></a><a id="description"></a>

Reference class for [`maxon.NodePathInterface`](../interface/maxon.NodePathInterface.md#module-maxon.NodePathInterface).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.NodePathInterface`](../interface/maxon.NodePathInterface.md#module-maxon.NodePathInterface)
- [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.NodePath.INPUTS`](maxon.NodePath.INPUTS.md#maxon.NodePath.INPUTS) |  |
| [`maxon.NodePath.OUTPUTS`](maxon.NodePath.OUTPUTS.md#maxon.NodePath.OUTPUTS) |  |
| [`maxon.NodePath.TEMPLATE`](maxon.NodePath.TEMPLATE.md#maxon.NodePath.TEMPLATE) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetPortPath`](#maxon.NodePath.GetPortPath)() | Returns only the relative port path without the true node of this node path. |
| [`ToBlock`](#maxon.NodePath.ToBlock)() | Returns the internally stored path as a [`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block). |
| [`__init__`](#maxon.NodePath.__init__)([obj]) | Initializes a new node path object. |

## Methods Definition <a id="methods-definition"></a>

### `NodePath.GetPortPath()` <a id="maxon.NodePath.GetPortPath"></a>

Returns only the relative port path without the true node of this node path.

**Returns:** The port path of this node path.

**Return type:** [`maxon.NodePath`](#module-maxon.NodePath)

### `NodePath.ToBlock()` <a id="maxon.NodePath.ToBlock"></a>

Returns the internally stored path as a [`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block).

The returned block references the internal storage of this path, so it keeps this [`maxon.NodePath`](#module-maxon.NodePath) alive as long as the block exists.

**Returns:** This path as a block of identifiers.

**Return type:** [`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [[`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]

### `NodePath.__init__(obj=None)` <a id="maxon.NodePath.__init__"></a>

Initializes a new node path object.

**Parameters:**

**obj** (Optional[[`maxon.NodePath`](#module-maxon.NodePath), str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String)]) –

If *obj* is None, an empty `maxon.Nodepath` is initialized.  
If *obj* is a `maxon.Nodepath` this node path is copied.  
If *obj* is a string a `maxon.Nodepath` is built from it.
