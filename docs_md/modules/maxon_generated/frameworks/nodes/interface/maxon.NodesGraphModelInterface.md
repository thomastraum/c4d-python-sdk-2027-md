<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/nodes/interface/maxon.NodesGraphModelInterface.html -->

# maxon.NodesGraphModelInterface <a id="maxon-nodesgraphmodelinterface"></a>

## Description <a id="module-maxon.NodesGraphModelInterface"></a><a id="description"></a>

A [`maxon.NodesGraphModelRef`](../reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef) is an implementation of [`maxon.GraphModelInterface`](../../graph/interface/maxon.GraphModelInterface.md#module-maxon.GraphModelInterface) which wraps a `maxon.NodeSystem`.  
There may be more than one model working on the same `maxon.NodeSystem` reference, this is handled by a shared `maxon.NodeSystemManagerRef`.  
Each [`maxon.NodesGraphModelRef`](../reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef) is a certain CreateView “view” on the NodeSystem with individual filter settings and root paths.  
The manager ([`maxon.NodeSystemManagerInterface`](maxon.NodeSystemManagerInterface.md#module-maxon.NodeSystemManagerInterface)) coordinates the accesses of the views.  
`maxon.NodesGraphModelClass` is the base implementation of this interface.  
It has to be used as base class for custom implementations.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.GraphModelInterface`](../../graph/interface/maxon.GraphModelInterface.md#module-maxon.GraphModelInterface)

Child Class:

- [`maxon.NodesGraphModelRef`](../reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`CreateView`](#maxon.NodesGraphModelInterface.CreateView)(filter, rootPath) | Creates a new view for the node system of this view. |
| [`GetBase`](#maxon.NodesGraphModelInterface.GetBase)(node) | Return the original base node. |
| [`MoveToGroup`](#maxon.NodesGraphModelInterface.MoveToGroup)(groupRoot, groupId, selection) | Groups the selection of nodes of this graph into a new group node. |
| [`ReplaceChild`](#maxon.NodesGraphModelInterface.ReplaceChild)(child, nodeId, portMap) | Replaces the given child node with an instance of a node system. |
| [`Ungroup`](#maxon.NodesGraphModelInterface.Ungroup)(group) | Dissolves the given group into its children. |

## Methods Definition <a id="methods-definition"></a>

### `NodesGraphModelInterface.CreateView(filter, rootPath)` <a id="maxon.NodesGraphModelInterface.CreateView"></a>

Creates a new view for the node system of this view.  
The returned view will be managed by the same `maxon.NodeSystemManagerRef` as this view.

**Parameters:**

- **filter** ([`maxon.NodeSystemManagerInterface.FILTER`](../../../enums/maxon.NodeSystemManagerInterface.FILTER.md#module-maxon.NodeSystemManagerInterface.FILTER)) –

  The filter to use for the view.  
  If this view is read-only, the FILTER.READ_ONLY flag will be set implicitly.

- **rootPath** ([`maxon.NodePath`](../../graph/datatype/maxon.NodePath.md#module-maxon.NodePath)) –

  The absolute path to the root node of the new view.  
  Use this if the new view shall not represent the whole graph, but only a node and its inner parts.  
  Note that this is an absolute path, so the path of the current view is always ignored.

**Returns:** A new [`maxon.NodesGraphModelRef`](../reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef) view for the same node system.

**Return type:** [`maxon.NodesGraphModelRef`](../reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)

### `NodesGraphModelInterface.GetBase(node)` <a id="maxon.NodesGraphModelInterface.GetBase"></a>

Return the original base node.

**Parameters:** **node** ([`maxon.GraphNode`](../../graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The node to retrieve the NodeSystem from.

**Returns:** The base NodeSystem of the node.

**Return type:**

`maxon.NodeSystem`

### `NodesGraphModelInterface.MoveToGroup(groupRoot, groupId, selection)` <a id="maxon.NodesGraphModelInterface.MoveToGroup"></a>

Groups the selection of nodes of this graph into a new group node.  
*groupRoot* is used to set up the new group node.  
You can leave this empty, then a new node system will be created as an instance of a group asset which fits to the selection (group assets already used by the selection are considered).  
But you can also provide a valid node system.  
All selected nodes are moved to the group using their original identifiers, including inner connections.  
Afterwards the group is :`MutableRoot.EndModification()` “finalized” and an instance of the group is added to this graph using the given groupId.  
Connections which leave the group are kept by adding ports to the group node as needed, and connecting them correspondingly.  
If the used group node already has ports, these will be used where identifiers mach.

**Parameters:**

- **groupRoot** ([`maxon.GraphNode`](../../graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The GraphNode of another (usually empty) node system which will become the group, can be empty.
- **groupId** (Union[str, [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), [`maxon.StringInterface`](../../../interfaces/core/maxon.StringInterface.md#module-maxon.StringInterface)]) – Identifier for the new group within this node system (if empty, a UUID is chosen).
- **selection** ([`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.GraphNode`](../../graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode)]) – A selection of nodes. Only nodes which are direct children of the root node of this view are considered.

**Returns:** A GraphNode referencing the added child.

**Return type:** [`maxon.GraphNode`](../../graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode)

### `NodesGraphModelInterface.ReplaceChild(child, nodeId, portMap)` <a id="maxon.NodesGraphModelInterface.ReplaceChild"></a>

Replaces the given child node with an instance of a node system.  
This removes the original child, adds an instance of nodeId as new child (with the same identifier),  
and finally tries to re-establish connections and attribute values of the original node at the new node.

**Parameters:**

- **child** ([`maxon.GraphNode`](../../graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The child node to replace.
- **nodeId** (Union[str, [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]) – Identifier for the type of the node to add.
- **portMap** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – The port mapping from old port paths to new port paths. You can use NodePath or string.

### `NodesGraphModelInterface.Ungroup(group)` <a id="maxon.NodesGraphModelInterface.Ungroup"></a>

Dissolves the given group into its children.  
This moves all children of group including their inner connections to the parent of group.  
External connections (from the group to other nodes) are moved to the inner nodes as well.

**Parameters:** **group** ([`maxon.GraphNode`](../../graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The group node to dissolve.

**Returns:** The mapping from original identifiers within the group to the new identifiers used at parent level.

**Return type:** list[tuple[[`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]]
