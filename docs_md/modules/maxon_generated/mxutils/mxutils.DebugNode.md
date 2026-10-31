<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/mxutils/mxutils.DebugNode.html -->

# mxutils.DebugNode <a id="mxutils-debugnode"></a>

## Description <a id="module-mxutils.DebugNode"></a><a id="description"></a>

Realizes a simple tree structure used in printing debug information.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`mxutils.DebugNode.Children`](mxutils.DebugNode.Children.md#mxutils.DebugNode.Children) | Gets an immutable tuple of the child nodes of the node. |
| [`mxutils.DebugNode.Depth`](mxutils.DebugNode.Depth.md#mxutils.DebugNode.Depth) | Gets the depth of the node in the tree. |
| [`mxutils.DebugNode.Label`](mxutils.DebugNode.Label.md#mxutils.DebugNode.Label) | Gets the label of the node, i.e., what is printed in a debug tree. |
| [`mxutils.DebugNode.Nid`](mxutils.DebugNode.Nid.md#mxutils.DebugNode.Nid) | Gets the ID of the node. |
| [`mxutils.DebugNode.Parent`](mxutils.DebugNode.Parent.md#mxutils.DebugNode.Parent) | Gets the pointed parent node of the node. |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Add`](#mxutils.DebugNode.Add)(child) | Adds a child node to the node. |
| [`Find`](#mxutils.DebugNode.Find)(nid) | Finds a node by its ID. |
| [`FromString`](#mxutils.DebugNode.FromString)(input[, indentation]) | Builds a tree structure from a string representation. |
| [`Remove`](#mxutils.DebugNode.Remove)() | Removes the node from its parent. |
| [`ToString`](#mxutils.DebugNode.ToString)() | Returns the string representation of the current node and its subtree. |
| [`__init__`](#mxutils.DebugNode.__init__)(name[, nid]) | Initializes a DebugNode instance. |
| [`__repr__`](#mxutils.DebugNode.__repr__)() | Returns the label of the node. |
| [`__str__`](#mxutils.DebugNode.__str__)() | Returns the label of the node. |

## Methods Definition <a id="methods-definition"></a>

### `DebugNode.Add(child: mxutils.mxu_scene.DebugNode) → None` <a id="mxutils.DebugNode.Add"></a>

Adds a child node to the node.

**Parameters:** **child** – The child node to add.

**Raises:** **ValueError** – If the child already has a parent.

### `DebugNode.Find(nid: tuple) → mxutils.mxu_scene.DebugNode | None` <a id="mxutils.DebugNode.Find"></a>

Finds a node by its ID.

**Parameters:** **nid** – The ID of the node to find.

**Returns:** The node with the specified ID, or None if not found.

**Return type:** DebugNode | None

### *static* `DebugNode.FromString(input: str, indentation: int = 4) → mxutils.mxu_scene.DebugNode` <a id="mxutils.DebugNode.FromString"></a>

Builds a tree structure from a string representation.

**Parameters:**

- **input** – The string representation of the tree structure.
- **indentation** – The number of spaces used for indentation.

**Returns:** The root node of the constructed tree.

**Return type:** DebugNode

### `DebugNode.Remove() → None` <a id="mxutils.DebugNode.Remove"></a>

Removes the node from its parent.

### `DebugNode.ToString() → str` <a id="mxutils.DebugNode.ToString"></a>

Returns the string representation of the current node and its subtree.

**Returns:** The string representation of the current node and its subtree.

**Return type:** str

### `DebugNode.__init__(name: str, nid: tuple[int] | None = None) → None` <a id="mxutils.DebugNode.__init__"></a>

Initializes a DebugNode instance.

**Parameters:**

- **name** – The label of the node.
- **nid** – The ID of the node as a tuple of integers.

### `DebugNode.__repr__() → str` <a id="mxutils.DebugNode.__repr__"></a>

Returns the label of the node.

### `DebugNode.__str__()` <a id="mxutils.DebugNode.__str__"></a>

Returns the label of the node.
