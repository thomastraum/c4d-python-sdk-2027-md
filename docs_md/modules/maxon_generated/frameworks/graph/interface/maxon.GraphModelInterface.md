<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/graph/interface/maxon.GraphModelInterface.html -->

# maxon.GraphModelInterface <a id="maxon-graphmodelinterface"></a>

## Description <a id="module-maxon.GraphModelInterface"></a><a id="description"></a>

GraphModelInterface is an abstraction of a hierarchical graph.  
A [`maxon.GraphModelInterface`](#module-maxon.GraphModelInterface) has a single root node (see [`maxon.GraphModelInterface.GetViewRoot()`](#maxon.GraphModelInterface.GetViewRoot)).  
The root node and any other node may have an arbitrary number of child nodes.  
Each node may have a number of input ports and output ports.  
Those ports may have nested ports, too.  
Nodes and ports of a graph can be arranged in a single tree, for example:

- **Root (maxon.NODE_KIND.NODE)**

  - **N1 (maxon.NODE_KIND.NODE)**

    - **N2 (maxon.NODE_KIND.NODE)**

      - **Inputs (maxon.NODE_KIND.INPUTS)**

        - **PortA (maxon.NODE_KIND.INPORT)**

          - PortB (maxon.NODE_KIND.INPORT)

        - PortC (maxon.NODE_KIND.INPORT)

      - **Outputs (maxon.NODE_KIND.OUTPUTS)**

        - PortD (maxon.NODE_KIND.OUTPORT)

    - **Inputs (maxon.NODE_KIND.INPUTS)**

      - PortE (maxon.NODE_KIND.INPORT)g

    - **Outputs (maxon.NODE_KIND.OUTPUTS)**

      - **PortF (maxon.NODE_KIND.OUTPORT)**

        - PortG (maxon.NODE_KIND.OUTPORT)

  - **N3 (maxon.NODE_KIND.NODE)**

    - **Inputs (maxon.NODE_KIND.INPUTS)**

      - PortH (maxon.NODE_KIND.INPORT)

    - **Outputs (maxon.NODE_KIND.OUTPUTS)**

      - PortI (maxon.NODE_KIND.OUTPORT)

[`maxon.GraphModelInterface`](#module-maxon.GraphModelInterface) represents nodes and ports by the same class [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode).  
To distinguish between the different kinds of a [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode), a value of type [`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND) is returned by [`maxon.GraphNode.GetKind()`](../datatype/maxon.GraphNode.md#maxon.GraphNode.GetKind).  
The example tree shows the possible kinds in parentheses:

- [`maxon.NODE_KIND.NODE`](../../../enums/maxon.NODE_KIND.NODE.md#maxon.NODE_KIND.NODE) stands for true nodes.
- [`maxon.NODE_KIND.INPUTS`](../../../enums/maxon.NODE_KIND.INPUTS.md#maxon.NODE_KIND.INPUTS) /[`maxon.NODE_KIND.OUTPUTS`](../../../enums/maxon.NODE_KIND.OUTPUTS.md#maxon.NODE_KIND.OUTPUTS) represent the lists of top-level input/output ports of a node.
- [`maxon.NODE_KIND.INPORT`](../../../enums/maxon.NODE_KIND.INPORT.md#maxon.NODE_KIND.INPORT) / [`maxon.NODE_KIND.OUTPORT`](../../../enums/maxon.NODE_KIND.OUTPORT.md#maxon.NODE_KIND.OUTPORT) represent input/output ports.

It is not required for an implementation of [`maxon.GraphModelInterface`](#module-maxon.GraphModelInterface) to support arbitrary nestings.  
For example, the implementation for nodes supports arbitrarily nested ports, but depending on its filter settings it doesn’t support nodes nested within other nodes.

In addition to the tree of nodes and ports, a hierarchical graph also has a number of connections between ports.  
They are represented by `maxon.GraphConnection`.  
Typically a connection goes from an output port to an input port, but this is not always the case.  
The following connections are allowed:

- An output port of a node may have a connection to an input port of a sibling node (so both nodes must have the same direct parent).
- An input port of a child node may have a connection from an input port of its direct parent node.
- An output port of a child node may have a connection to an output port of its direct parent node.
- An input port of a node may have a connection to an output port of that same node (so the connections just tunnels the value through the node).

In all cases it doesn’t matter if the ports are top-level ports or nested ports.  
Each node may have attributes.  
An attribute is identified by an [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), typically this id is defined together with the type of the attribute value by [`maxon.MAXON_ATTRIBUTE()`](../../../functions/maxon.MAXON_ATTRIBUTE.md#maxon.MAXON_ATTRIBUTE).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObserverObjectInterface`](../../../interfaces/core_helper/maxon.ObserverObjectInterface.md#module-maxon.ObserverObjectInterface)

Children Classes:

- [`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)
- [`maxon.NodesGraphModelInterface`](../../nodes/interface/maxon.NodesGraphModelInterface.md#module-maxon.NodesGraphModelInterface)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`AddChild`](#maxon.GraphModelInterface.AddChild)(childId, nodeId[, args]) | Adds an instance of the node given by the identifier nodeId as child of the root node to this graph. |
| [`AddPorts`](#maxon.GraphModelInterface.AddPorts)() |  |
| [`Apply`](#maxon.GraphModelInterface.Apply)(list, inverse) | Applies the given change list to the node system of this manager. |
| [`BeginTransaction`](#maxon.GraphModelInterface.BeginTransaction)([userData]) | Begins a new transaction within which modifications can be made. |
| [`BeginTransactionImpl`](#maxon.GraphModelInterface.BeginTransactionImpl)() |  |
| [`CommitImpl`](#maxon.GraphModelInterface.CommitImpl)(userData, nesting[, validate]) |  |
| [`CreateCopyOfSelection`](#maxon.GraphModelInterface.CreateCopyOfSelection)(selection) | Returns a new graph model which is a copy of the subgraph given by the selection. |
| [`GetChangeList`](#maxon.GraphModelInterface.GetChangeList)() | Returns the change list to which this graph model currently logs its modifications. |
| [`GetGraphAttribute`](#maxon.GraphModelInterface.GetGraphAttribute)(attr) | Returns the [`maxon.GraphAttribute`](../reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute) which this graph model uses for the attribute identified by attr. |
| [`GetGraphAttributeFlags`](#maxon.GraphModelInterface.GetGraphAttributeFlags)(attr) | Returns the [`maxon.GraphAttributeInterface.FLAGS`](../../../enums/maxon.GraphAttributeInterface.FLAGS.md#module-maxon.GraphAttributeInterface.FLAGS) to use for the attribute identified by attr. |
| [`GetModificationStamp`](#maxon.GraphModelInterface.GetModificationStamp)() | Returns a time stamp of this graph which can be used to test for modifications. |
| [`GetModificationsSince`](#maxon.GraphModelInterface.GetModificationsSince)(stamp[, receiver, …]) | Reports all modifications which have been made since the given stamp to **receiver**. |
| [`GetNode`](#maxon.GraphModelInterface.GetNode)(path[, filtered]) | Returns the [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) corresponding to path. |
| [`GetRoot`](#maxon.GraphModelInterface.GetRoot)() | *Deprecated since version 2025.0.* |
| [`GetRootPath`](#maxon.GraphModelInterface.GetRootPath)() | *Deprecated since version 2025.0.* |
| [`GetTransactionCount`](#maxon.GraphModelInterface.GetTransactionCount)() |  |
| [`GetUserState`](#maxon.GraphModelInterface.GetUserState)() |  |
| [`GetViewRoot`](#maxon.GraphModelInterface.GetViewRoot)() | Returns the root node of this graph. |
| [`GetViewRootPath`](#maxon.GraphModelInterface.GetViewRootPath)() | Returns the path of the root node of this graph. |
| [`IsConnectable`](#maxon.GraphModelInterface.IsConnectable)() |  |
| [`IsReadOnly`](#maxon.GraphModelInterface.IsReadOnly)() | Checks if this graph is read-only. |
| [`IsRoot`](#maxon.GraphModelInterface.IsRoot)() |  |
| [`Merge`](#maxon.GraphModelInterface.Merge)(other) | Merges the other graph into this graph. |
| [`RemovePorts`](#maxon.GraphModelInterface.RemovePorts)() |  |
| [`ResetUserState`](#maxon.GraphModelInterface.ResetUserState)(attr) | Removes all values for the given user state attribute attr from this graph (so from all of its nodes). |
| [`StartNewChangeList`](#maxon.GraphModelInterface.StartNewChangeList)() | Starts a new change list and returns the previous one. |
| [`Validate`](#maxon.GraphModelInterface.Validate)() | Validates the graph. |

## Methods Definition <a id="methods-definition"></a>

### `GraphModelInterface.AddChild(childId, nodeId, args=maxon.DataDictionary object at 0x12e9af6a4a0 with the data: DataDictionary{})` <a id="maxon.GraphModelInterface.AddChild"></a>

Adds an instance of the node given by the identifier nodeId as child of the root node to this graph.

> If *childId* is empty, a `maxon.UUID` will be chosen as identifier of the child, otherwise *childId*.  
> In the latter case it is an error if this root node already has a child with that identifier.

**Parameters:**

- **childId** (Union[str, [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]) – Identifier for the child node (if empty, a UUID is chosen).
- **nodeId** (Union[str, [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]) – Identifier for the type of the node to add. How this is resolved to an actual node type is model-specific.
- **args** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) – Arguments to use for the node creation. The exact meaning is model-specific.

**Returns:** A [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) referencing the added child.

**Return type:** [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)

### `GraphModelInterface.AddPorts()` <a id="maxon.GraphModelInterface.AddPorts"></a>

### `GraphModelInterface.Apply(list, inverse)` <a id="maxon.GraphModelInterface.Apply"></a>

Applies the given change list to the node system of this manager.

**Parameters:**

- **list** (`maxon.ChangeList`) – Change list to apply.
- **inverse** (*bool*) – **True** if the inverse of the change list shall be applied (for an undo), **False** otherwise.

**Returns:** A new change list which contains those changes of list which couldn’t be applied, for example the change of an attribute value at a node which doesn’t exist in the node system.

**Return type:**

`maxon.ChangeList`

### `GraphModelInterface.BeginTransaction(userData=None)` <a id="maxon.GraphModelInterface.BeginTransaction"></a>

Begins a new transaction within which modifications can be made.  
This is mandatory in order to modify the graph, modifications outside of transactions are not allowed (with the exception of changing user state attributes).  
If there already is an active transaction, this will create a nested transaction.  
Otherwise a non-nested transaction starts, only then the observable

> **Warning:** It’s mandatory to use the *with* statement as unclosed Transaction could lead to a freeze.
>
> ```python
> # This will start a new transaction and RollBack the transaction once the scope is left
> with graph.BeginTransaction() as transaction:
>     # Do some modification like connecting two ports
>     graph.Connect()
>
>     # This will commit and perform the change to the graph
>     transaction.Commit()
>
> # transaction is not anymore accessible and it has been Rolled out to the previous Commit.
> ```

**Parameters:**

**userData** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) –

User data to pass to the observers of `GraphModelInterface.ObservableTransactionStarted()`.  
Because nested transactions don’t trigger the observable, the user data of them is ignored.

**Returns:** A [`maxon.GraphTransaction`](../datatype/maxon.GraphTransaction.md#module-maxon.GraphTransaction) object to commit or rollback the transaction at a later point of time.

**Return type:** [`maxon.GraphTransaction`](../datatype/maxon.GraphTransaction.md#module-maxon.GraphTransaction)

### `GraphModelInterface.BeginTransactionImpl()` <a id="maxon.GraphModelInterface.BeginTransactionImpl"></a>

### `GraphModelInterface.CommitImpl(userData, nesting, validate=True)` <a id="maxon.GraphModelInterface.CommitImpl"></a>

### `GraphModelInterface.CreateCopyOfSelection(selection)` <a id="maxon.GraphModelInterface.CreateCopyOfSelection"></a>

Returns a new graph model which is a copy of the subgraph given by the selection.

**Parameters:** **selection** (list[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)]) – A selection of nodes. Nodes which aren’t direct children of this graph are ignored.

**Returns:** A copy of the subgraph given by the selection.

**Return type:** [`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)

### `GraphModelInterface.GetChangeList()` <a id="maxon.GraphModelInterface.GetChangeList"></a>

Returns the change list to which this graph model currently logs its modifications.  
A newly created graph model doesn’t automatically create a change list, so to start logging you need to call [`GraphModelInterface.StartNewChangeList()`](#maxon.GraphModelInterface.StartNewChangeList) once.  
The change list can be used to undo or redo the changes or even to apply them to a different graph, see [`GraphModelInterface.Apply()`](#maxon.GraphModelInterface.Apply).

**Returns:** Current change list, may be a null reference.

**Return type:**

`maxon.ChangeList`

### `GraphModelInterface.GetGraphAttribute(attr)` <a id="maxon.GraphModelInterface.GetGraphAttribute"></a>

Returns the [`maxon.GraphAttribute`](../reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute) which this graph model uses for the attribute identified by attr.  
The model may return a null reference if it doesn’t provide a [`maxon.GraphAttribute`](../reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute) for attr.  
This doesn’t mean that the attribute is unsupported, it just means that there is no need for special handling of the attribute (which would require a [`maxon.GraphAttribute`](../reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute)).

**Parameters:** **attr** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The identifier of the attribute

**Returns:** The corresponding [`maxon.GraphAttribute`](../reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute), or a null reference if the graph model has no [`maxon.GraphAttribute`](../reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute) for attr.

**Return type:** [`maxon.GraphAttribute`](../reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute)

### `GraphModelInterface.GetGraphAttributeFlags(attr)` <a id="maxon.GraphModelInterface.GetGraphAttributeFlags"></a>

Returns the [`maxon.GraphAttributeInterface.FLAGS`](../../../enums/maxon.GraphAttributeInterface.FLAGS.md#module-maxon.GraphAttributeInterface.FLAGS) to use for the attribute identified by attr.  
This allows the graph model to override the default flags of the attribute, for example to mark an attribute as meta attribute.

**Parameters:** **attr** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The identifier of the attribute.

**Returns:** The flags which this graph model uses for the attribute.

**Return type:** [`maxon.GraphAttributeInterface.FLAGS`](../../../enums/maxon.GraphAttributeInterface.FLAGS.md#module-maxon.GraphAttributeInterface.FLAGS)

### `GraphModelInterface.GetModificationStamp()` <a id="maxon.GraphModelInterface.GetModificationStamp"></a>

Returns a time stamp of this graph which can be used to test for modifications.  
Each transaction or change of user state increments the stamp.  
The time stamp is also needed for [`GraphModelInterface.GetModificationsSince()`](#maxon.GraphModelInterface.GetModificationsSince) and [`GraphNode.GetAttributeModificationsSince()`](../datatype/maxon.GraphNode.md#maxon.GraphNode.GetAttributeModificationsSince) to get all modifications which have happened since then.

**Returns:** Modification time stamp of the graph.

**Return type:**

`maxon.TimeStamp`

### `GraphModelInterface.GetModificationsSince(stamp, receiver=None, filtered=True)` <a id="maxon.GraphModelInterface.GetModificationsSince"></a>

Reports all modifications which have been made since the given stamp to **receiver**.  
If **receiver** is None only flags will be returned.

**Parameters:**

- **stamp** (`maxon.Timestamp`) – A reference time stamp. Only modifications newer than this stamp are reported.
- **receiver** (Union[None, list, Callable[[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode), [`maxon.GraphModelInterface.MODIFIED`](../../../enums/maxon.GraphModelInterface.MODIFIED.md#module-maxon.GraphModelInterface.MODIFIED)], bool]) – Modifications are reported to this receiver.
- **filtered** (*bool*) – With the default value of True the filter settings (if any) of this graph will be used, so modifications to nodes which don’t pass the filter aren’t reported.

**Returns:** Combination of flags to indicate the kinds of changes that have happened.

### `GraphModelInterface.GetNode(path, filtered=True)` <a id="maxon.GraphModelInterface.GetNode"></a>

Returns the [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) corresponding to path.

> **Note:** If no such node exists in the graph, an empty node is returned.

**Parameters:**

- **path** ([`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)) –

  A node path.  
  This has to be an absolute path, so if the current graph is view of a nested part of an enclosing graph.  
  The path has to be the full path starting at the root of the enclosing graph.

- **filtered** –

  With the default value of **True** the filter settings (if any) of this graph will be used.  
  When **False** this is disabled, then you’ll get a valid [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) even for paths which don’t belong to this graph, but e.g. to nested graphs which are hidden by the filter settings.

**Return type:** [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)

**Returns:**

The [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) corresponding to the path.  
This is empty when there is no such node in the graph.

### `GraphModelInterface.GetRoot()` <a id="maxon.GraphModelInterface.GetRoot"></a>

*Deprecated since version 2025.0:* Use `maxon.GraphNode.GetViewRoot()` instead.

Returns the root node of this graph.  
The whole graph can be traversed starting from the root node.

**Return type:** [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)

**Returns:** The root node of this graph.

### `GraphModelInterface.GetRootPath()` <a id="maxon.GraphModelInterface.GetRootPath"></a>

*Deprecated since version 2025.0:* Use `maxon.GraphNode.GetViewRootPath()` instead.

Returns the path of the root node of this graph.  
Usually this is an empty path, but a graph model may be a view of a nested part of an enclosing graph.  
In the latter case the path points to the root node of the nested part.

**Return type:** [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

**Returns:** The path of the root node of this graph.

### `GraphModelInterface.GetTransactionCount()` <a id="maxon.GraphModelInterface.GetTransactionCount"></a>

### `GraphModelInterface.GetUserState()` <a id="maxon.GraphModelInterface.GetUserState"></a>

### `GraphModelInterface.GetViewRoot()` <a id="maxon.GraphModelInterface.GetViewRoot"></a>

Returns the root node of this graph.  
The whole graph can be traversed starting from the root node.

**Return type:** [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)

**Returns:** The root node of this graph.

### `GraphModelInterface.GetViewRootPath()` <a id="maxon.GraphModelInterface.GetViewRootPath"></a>

Returns the path of the root node of this graph.  
Usually this is an empty path, but a graph model may be a view of a nested part of an enclosing graph.  
In the latter case the path points to the root node of the nested part.

**Return type:** [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

**Returns:** The path of the root node of this graph.

### `GraphModelInterface.IsConnectable()` <a id="maxon.GraphModelInterface.IsConnectable"></a>

### `GraphModelInterface.IsReadOnly()` <a id="maxon.GraphModelInterface.IsReadOnly"></a>

Checks if this graph is read-only.

> **Note:** You can’t modify read-only graphs.

**Return type:** bool

**Returns:** **True** if this graph is read-only otherwise **False**.

### `GraphModelInterface.IsRoot()` <a id="maxon.GraphModelInterface.IsRoot"></a>

### `GraphModelInterface.Merge(other)` <a id="maxon.GraphModelInterface.Merge"></a>

Merges the other graph into this graph.  
Top-level nodes and ports are added into this graph using new unique identifiers to prevent naming conflicts.  
The mapping from the original identifiers of other to the new ones is returned.

**Parameters:** **other** ([`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)) – Another graph to merge into this graph.

**Returns:** The mapping from original identifiers of other to the identifiers used for the merge: | - first entry contains the mapping of top-level nodes. | - second entry contains the mapping of top-level input ports. | - third entry contains the mapping of top-level output ports.

**Return type:** tuple[`maxon.HashMap` [[`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]]

### `GraphModelInterface.RemovePorts()` <a id="maxon.GraphModelInterface.RemovePorts"></a>

### `GraphModelInterface.ResetUserState(attr)` <a id="maxon.GraphModelInterface.ResetUserState"></a>

Removes all values for the given user state attribute attr from this graph (so from all of its nodes).

**Parameters:** **attr** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – A user state attribute

### `GraphModelInterface.StartNewChangeList()` <a id="maxon.GraphModelInterface.StartNewChangeList"></a>

Starts a new change list and returns the previous one.  
Afterwards this manager will log all modifications to the newly created change list.  
The new change list can be obtained with [`GraphModelInterface.GetChangeList()`](#maxon.GraphModelInterface.GetChangeList) or as the result of the next call to [`GraphModelInterface.StartNewChangeList()`](#maxon.GraphModelInterface.StartNewChangeList).  
The returned change list contains all modifications which have been made since the previous call to [`GraphModelInterface.StartNewChangeList()`](#maxon.GraphModelInterface.StartNewChangeList).  
You can pass it to [`GraphModelInterface.Apply()`](#maxon.GraphModelInterface.Apply) to undo or redo the changes.

**Returns:** Change list which contains the modifications since the previous call to *GraphModelInterface.StartNewChangeList*.

**Return type:**

`maxon.ChangeList`

### `GraphModelInterface.Validate()` <a id="maxon.GraphModelInterface.Validate"></a>

Validates the graph.

> **Note:** This is an implementation-specific operation and should be invoked when a batch of changes has been applied to the graph and the graph should be brought into a valid state again.

For example, the implementation of [`maxon.GraphModelInterface`](#module-maxon.GraphModelInterface) for nodes may update the type of an output port of a polymorphic node based on the types of the input ports.
