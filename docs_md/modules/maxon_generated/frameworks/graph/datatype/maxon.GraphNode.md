<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/graph/datatype/maxon.GraphNode.html -->

# maxon.GraphNode <a id="maxon-graphnode"></a>

## Description <a id="module-maxon.GraphNode"></a><a id="description"></a>

A [`maxon.GraphNode`](#module-maxon.GraphNode) represents a general node (g-node for short) in the hierarchy of a [`maxon.GraphModelInterface`](../interface/maxon.GraphModelInterface.md#module-maxon.GraphModelInterface). There are five different kinds of such a node: It may be a true node, an input or output port or an input port list or output port list. A node may have attributes, and if it is a port, it may be connected to other ports. For a general overview, see [`maxon.GraphModelInterface`](../interface/maxon.GraphModelInterface.md#module-maxon.GraphModelInterface).

Most functions of [`maxon.GraphNode`](#module-maxon.GraphNode) can be used for all node kinds, some functions are specific for certain kinds (such as `GraphNode.Connect()` which is only supported for ports).

[`maxon.GraphNode`](#module-maxon.GraphNode) holds a strong [`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef) reference on the graph, see `GraphNode.GetGraph()`. The node within the graph is referenced symbolically by a [`maxon.NodePath`](maxon.NodePath.md#module-maxon.NodePath), see `GraphNode.GetPath()`. Therefore it is guaranteed for the referenced graph that it exists as long as the [`maxon.GraphNode`](#module-maxon.GraphNode), but not for the referenced node. Namely, a [`maxon.GraphNode`](#module-maxon.GraphNode) can be in one of three states:

- It may be a null value, then it doesn’t represent any node. `GraphNode.IsNull()` returns true in this state.
- It may be a valid node in a graph (`GraphNode.IsValid()` returns true). `GraphNode.GetGraph()` returns the graph, `GraphNode.GetPath()` the path of the node, and all supported functions can be called.
- It represents a node which doesn’t exist any longer. `GraphNode.IsValid()` returns false, but `GraphNode.IsPopulated()` still returns true. Also `GraphNode.GetGraph()` and `GraphNode.GetPath()` return valid values, but you can’t call any functions which would require access to the node. Such a state can be used to identify deleted nodes. A transition between the cases 2 and 3 can happen without this [`maxon.GraphNode`](#module-maxon.GraphNode) being directly involved, namely when the graph is modified through another [`maxon.GraphNode`](#module-maxon.GraphNode) and a node with the path of this [`maxon.GraphNode`](#module-maxon.GraphNode) is added or removed.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Struct`](../../../datatypes/base_core/maxon.Struct.md#module-maxon.Struct)
- [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`AddPort`](#maxon.GraphNode.AddPort)(name) | Adds a port to this node with the given id. |
| [`AddPorts`](#maxon.GraphNode.AddPorts)(index, count) | Adds a number of variadic port instances to this variadic port. |
| [`BeginTransactionImpl`](#maxon.GraphNode.BeginTransactionImpl)([userData]) |  |
| [`ChangeValue`](#maxon.GraphNode.ChangeValue)(attr, op, path, value) | Sets a part of the value of #attr to #value for this node. |
| [`Connect`](#maxon.GraphNode.Connect)(target, *args, **kwargs) | Connect this node with another node port. |
| [`CopyConnectionsFrom`](#maxon.GraphNode.CopyConnectionsFrom)(source, direction, …) | Copies all connections of *source* to the port given by this [`maxon.GraphNode`](#module-maxon.GraphNode). |
| [`CopyValuesFrom`](#maxon.GraphNode.CopyValuesFrom)(source, includeInner) | Copies all directly set attribute values of *source* to this node. |
| [`FindChild`](#maxon.GraphNode.FindChild)(idOrNodeKind) | Finds the child of this node whose kind matches the given *mask*. |
| [`FindInnerNode`](#maxon.GraphNode.FindInnerNode)(relativePath) | Finds the inner child of this node with the given relative path. |
| [`GetAncestor`](#maxon.GraphNode.GetAncestor)(mask) | Returns the closest ancestor node of this node (possibly this node itself) whose kind matches the given *mask*. |
| [`GetAttributeModificationsSince`](#maxon.GraphNode.GetAttributeModificationsSince)(stamp, receiver) | Reports all attribute modifications which have been made for this node since the given stamp to the receiver. |
| [`GetAttributeStamp`](#maxon.GraphNode.GetAttributeStamp)(attr) | Returns the modification stamp of the given attribute for this node. |
| [`GetBaseValues`](#maxon.GraphNode.GetBaseValues)(attr, expectedType[, receiver]) | Gets the values of the given attribute for this node and its inherited parents. |
| [`GetChildren`](#maxon.GraphNode.GetChildren)([callback, mask]) | Gets all children of this node. |
| [`GetConnectionStamp`](#maxon.GraphNode.GetConnectionStamp)(direction) | Returns the modification stamp of incoming/outgoing connections for this port. |
| [`GetConnectionValue`](#maxon.GraphNode.GetConnectionValue)(target, position, attr[, …]) | Gets the value of the given attribute for the connection from this port to target. |
| [`GetConnectionValues`](#maxon.GraphNode.GetConnectionValues)(target, receiver) | Gets all attribute values of the connection from this port to target. |
| [`GetConnections`](#maxon.GraphNode.GetConnections)(pDir[, conns, mask, mode]) | Yields all connections of this port for the given direction *dir*. |
| [`GetConstantValue`](#maxon.GraphNode.GetConstantValue)() | *Deprecated since version 2024.4.* |
| [`GetDefaultValue`](#maxon.GraphNode.GetDefaultValue)() | *Deprecated since version 2024.4.* |
| [`GetEffectivePortValue`](#maxon.GraphNode.GetEffectivePortValue)() | Returns the effective value of this port. |
| [`GetGraph`](#maxon.GraphNode.GetGraph)() | Returns the graph to which this node belongs. |
| [`GetHashCode`](#maxon.GraphNode.GetHashCode)() | Returns the hash code of [`maxon.GraphNode`](#module-maxon.GraphNode). |
| [`GetId`](#maxon.GraphNode.GetId)() | Returns the identifier of this node. |
| [`GetInnerNodes`](#maxon.GraphNode.GetInnerNodes)(mask, includeThis[, receiver]) | Yields all inner nodes of this node matching #mask in pre-order. |
| [`GetInputs`](#maxon.GraphNode.GetInputs)() | Returns the input port list of this node. |
| [`GetKind`](#maxon.GraphNode.GetKind)() | Returns the kind of this node. |
| [`GetMessageFlags`](#maxon.GraphNode.GetMessageFlags)(attr) | Returns the message flags of the given attribute at this node. |
| [`GetMessages`](#maxon.GraphNode.GetMessages)(attr, receiver) | Yields the error or warning messages (if any) of the given attribute at this node to *receiver*. |
| [`GetOutputs`](#maxon.GraphNode.GetOutputs)() | Returns the output port list of this node. |
| [`GetParent`](#maxon.GraphNode.GetParent)() | Returns the parent of this node. |
| [`GetPath`](#maxon.GraphNode.GetPath)() | Returns the path of this node. |
| [`GetPortList`](#maxon.GraphNode.GetPortList)(dir) | Returns the input or output port list of this node, depending on dir. |
| [`GetPortValue`](#maxon.GraphNode.GetPortValue)() | Returns the value of this port (ignoring upstream overrides). |
| [`GetStoredValue`](#maxon.GraphNode.GetStoredValue)(attr[, expectedType]) | Gets the current value of the given attribute for this node, REGARDLESS of whether it is valid or not. |
| [`GetValue`](#maxon.GraphNode.GetValue)(attr[, expectedType]) | Gets the value of the given attribute *attr* for this node. |
| [`GetValues`](#maxon.GraphNode.GetValues)(mask) | Gets all attribute values of this node. |
| [`GetWires`](#maxon.GraphNode.GetWires)(target) | Returns the Wires from this node to #target. |
| [`InheritValue`](#maxon.GraphNode.InheritValue)(attr) | Restores the inherited state of the value for *attr*. |
| [`IsConnectable`](#maxon.GraphNode.IsConnectable)(target) | Checks if a connection from this port to target can be made. |
| [`IsInner`](#maxon.GraphNode.IsInner)() | Checks if this [`maxon.GraphNode`](#module-maxon.GraphNode) belongs to an inner node of the graph. |
| [`IsPopulated`](#maxon.GraphNode.IsPopulated)() | Checks whether this [`maxon.GraphNode`](#module-maxon.GraphNode) has graph and path references. |
| [`IsRoot`](#maxon.GraphNode.IsRoot)() | Checks if this GraphNode is the root node of the graph. |
| [`IsValid`](#maxon.GraphNode.IsValid)() | Checks whether this GraphNode points to a valid node. |
| [`Remove`](#maxon.GraphNode.Remove)() | Removes this node from the graph. |
| [`RemoveConnections`](#maxon.GraphNode.RemoveConnections)(pDir, mask) | Removes all connections of this port in the given direction which match the given *mask*. |
| [`RemovePorts`](#maxon.GraphNode.RemovePorts)(ports) | Removes a number of variadic port instances from this variadic port. |
| [`RemoveValue`](#maxon.GraphNode.RemoveValue)(attr) | Removes an attribute value from this node. |
| [`Reset`](#maxon.GraphNode.Reset)() | Resets this [`maxon.GraphNode`](#module-maxon.GraphNode) to the state it has right after default construction. |
| [`SetConnectionValue`](#maxon.GraphNode.SetConnectionValue)(target, position, attr, value) | Sets the value of *attr* to *value* for the connection from this port to *target*. |
| [`SetDefaultValue`](#maxon.GraphNode.SetDefaultValue)(value) | *Deprecated since version 2024.4.* |
| [`SetPortValue`](#maxon.GraphNode.SetPortValue)(value) | Sets the value of the attribute *maxon.DESCRIPTION.DATA.BASE.DEFAULTVALUE* to #value for this port. |
| [`SetValue`](#maxon.GraphNode.SetValue)(attr, value[, checkAndInvalidate]) | Sets the value of *attr* to *value* for this node. |
| [`TouchValue`](#maxon.GraphNode.TouchValue)(attr) | Marks the value of *attr* as modified without actually modifying it. |
| [`__eq__`](#maxon.GraphNode.__eq__)(other) | Checks if two nodes are representing the same node in a graph. |
| [`__hash__`](#maxon.GraphNode.__hash__)() | Return hash(self). |
| [`__init__`](#maxon.GraphNode.__init__)([src]) | Initializes a node from a graph. |
| [`__ne__`](#maxon.GraphNode.__ne__)(other) | Checks if two nodes are not representing the same node in a graph. |

## Methods Definition <a id="methods-definition"></a>

### `GraphNode.AddPort(name)` <a id="maxon.GraphNode.AddPort"></a>

Adds a port to this node with the given id.  
This node has to be a port list or a port itself.

**Parameters:** **name** (Union[str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]) – The identifier for the new port.

**Returns:** The added port.

**Return type:** [`maxon.GraphNode`](#module-maxon.GraphNode)

### `GraphNode.AddPorts(index, count)` <a id="maxon.GraphNode.AddPorts"></a>

Adds a number of variadic port instances to this variadic port.  
This is more efficient than a repeated call to [`GraphNode.AddPort()`](#maxon.GraphNode.AddPort).

> **Warning:** It is an error if this GraphNode is no variadic port.

**Parameters:**

- **index** (*int*) – The index within the current list of variadic port instances where the new instances shall be added.
- **count** (*int*) – The number of instances to add.

**Returns:** The newly added port instances as an array.

**Return type:** [`maxon.GraphNode`](#module-maxon.GraphNode)

### `GraphNode.BeginTransactionImpl(userData=None)` <a id="maxon.GraphNode.BeginTransactionImpl"></a>

### `GraphNode.ChangeValue(attr, op, path, value)` <a id="maxon.GraphNode.ChangeValue"></a>

Sets a part of the value of #attr to #value for this node.

**Parameters:**

- **attr** (Union[str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – The attribute whose value shall be set.
- **op** (`maxon.SubDataOperation`) – The SubDataOperation to use.
- **path** (`maxon.SubDataPathBlock`) – The path to the part of the attribute value which shall be changed.
- **value** ([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The new value for the part.

### `GraphNode.Connect(target, *args, **kwargs)` <a id="maxon.GraphNode.Connect"></a>

Connect this node with another node port.

Only one of this calls is allowed:

> - Connect(target, modes=WIRE_MODE.NORMAL, reverse=False)
> - Connect(target, portId)

**Parameters:**

- **target** ([`maxon.GraphNode`](#module-maxon.GraphNode)) – The node to connect to
- **modes** (Union[[`maxon.Wires`](maxon.Wires.md#module-maxon.Wires), [`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)]) – The type to use for the connection.
- **reverse** (*bool*) – If true the direction is reversed (from target to this port).
- **portId** (Union[[`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]) – The port’s id to be found.

### `GraphNode.CopyConnectionsFrom(source, direction, includeInner)` <a id="maxon.GraphNode.CopyConnectionsFrom"></a>

Copies all connections of *source* to the port given by this [`maxon.GraphNode`](#module-maxon.GraphNode).  
For each connection of *source* to a port in the given *direction*, a corresponding port in this graph is searched (based on the relative path) and, if it exists, a connection to that port is created.

**Parameters:**

- **source** ([`maxon.GraphNode`](#module-maxon.GraphNode)) – Another [`maxon.GraphNode`](#module-maxon.GraphNode) port, may stem from a different graph.
- **direction** ([`maxon.PORT_DIR`](../../../enums/maxon.PORT_DIR.md#module-maxon.PORT_DIR)) – The direction of connections to copy.
- **includeInner** (*bool*) – If **True**, copies connections for all inner nodes, too.

### `GraphNode.CopyValuesFrom(source, includeInner)` <a id="maxon.GraphNode.CopyValuesFrom"></a>

Copies all directly set attribute values of *source* to this node.  
This excludes derived attribute values as well as attribute values which are inherited from a base.

**Parameters:**

- **source** ([`maxon.GraphNode`](#module-maxon.GraphNode)) – Another [`maxon.GraphNode`](#module-maxon.GraphNode), may stem from a different graph.
- **includeInner** (*bool*) – If **True**, copies attribute values for all inner nodes, too.

### `GraphNode.FindChild(idOrNodeKind)` <a id="maxon.GraphNode.FindChild"></a>

Finds the child of this node whose kind matches the given *mask*.  
If no such child can be found, a null node is returned.  
If there is more than one matching child, an error is returned.

**Parameters:** **idOrNodeKind** (Union[str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.NodePath`](maxon.NodePath.md#module-maxon.NodePath), [`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)]) – A particual Id of a node or mask kind to look for.

**Returns:** A direct child of this node which matches the given *mask*, or a null node if no such child exists.

**Return type:** [`maxon.GraphNode`](#module-maxon.GraphNode)

### `GraphNode.FindInnerNode(relativePath)` <a id="maxon.GraphNode.FindInnerNode"></a>

Finds the inner child of this node with the given relative path.

> **Note:** If no such child can be found, a null node is returned.

**Parameters:** **relativePath** (Union[`` maxon.Block`[:class:`maxon.InternedId ``], `` maxon.BaseArray`[:class:`maxon.InternedId ``], list[Union[[`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), str]], [`maxon.NodePath`](maxon.NodePath.md#module-maxon.NodePath), str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String)]) – The relative path of the child to find, starting at this node.

**Returns:** The inner child of this node with the given relativePath, or a null node if no such child exists.

**Return type:** [`maxon.GraphNode`](#module-maxon.GraphNode)

### `GraphNode.GetAncestor(mask)` <a id="maxon.GraphNode.GetAncestor"></a>

Returns the closest ancestor node of this node (possibly this node itself) whose kind matches the given *mask*.  
i.e., the function goes upwards in the hierarchy until it finds a matching node.

**Parameters:** **mask** ([`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)) – Mask for the kind of node to look for.

**Returns:** Closest ancestor of this node matching the given *mask*, may be this node itself or a null node.

**Return type:** [`maxon.GraphNode`](#module-maxon.GraphNode)

### `GraphNode.GetAttributeModificationsSince(stamp, receiver)` <a id="maxon.GraphNode.GetAttributeModificationsSince"></a>

Reports all attribute modifications which have been made for this node since the given stamp to the receiver.  
Only stored attributes will be reported, so to also check for new values of computed attributes you should use [`GraphAttributeInterface.IsComputedFrom()`](../interface/maxon.GraphAttributeInterface.md#maxon.GraphAttributeInterface.IsComputedFrom).

> > **See also:** [`GraphModelInterface.GetModificationsSince()`](../interface/maxon.GraphModelInterface.md#maxon.GraphModelInterface.GetModificationsSince)

**Parameters:**

- **stamp** (`maxon.TimeStamp`) – A reference time stamp. Only modifications newer than this stamp are reported.
- **receiver** (Callable[[[`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)], bool]) – Modifications are reported to this receiver as a pair of the attribute identifier and the current value.

**Returns:** **False** if the receiver cancelled further evaluation, **True** otherwise.

**Return type:** bool

### `GraphNode.GetAttributeStamp(attr)` <a id="maxon.GraphNode.GetAttributeStamp"></a>

Returns the modification stamp of the given attribute for this node.  
This is the value of the graph’s time stamp (see [`GraphModelInterface.GetModificationStamp()`](../interface/maxon.GraphModelInterface.md#maxon.GraphModelInterface.GetModificationStamp)) at the time when the attribute value has been set last for this node, or a null value if it hasn’t been set at all.

**Parameters:** **attr** (Union[str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – An attribute.

**Returns:** The modification stamp of the last change of the attribute value.

**Return type:**

`maxon.TimeStamp`

### `GraphNode.GetBaseValues(attr, expectedType, receiver=None)` <a id="maxon.GraphNode.GetBaseValues"></a>

Gets the values of the given attribute for this node and its inherited parents.  
If this node doesn’t have a value for the attribute or the value doesn’t have the expected type,  
GetBaseValues will keep iterating the inherited nodes and call #valueReceiver each time the attribute is found on an a base.

**Parameters:**

- **attr** (Union[str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – The attribute whose value shall be obtained.
- **expectedType** (Optional[[`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)]) – The expected type of the attribute value, may be None if no check shall be done.
- **receiver** (Union[None, list, Callable[[[`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data), int], bool]]) – A callback which receives the attribute values and their nesting levels.

**Returns:** If *callback* is None or a list then a list of tuple([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data), int) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data), int], bool]

### `GraphNode.GetChildren(callback=None, mask=31)` <a id="maxon.GraphNode.GetChildren"></a>

Gets all children of this node.  
For a true node this will be its child nodes as well as a single input port list and a single output port list.  
Otherwise, the children are ports.

**Parameters:**

- **callback** (Union[None, list, Callable[[[`maxon.GraphNode`](#module-maxon.GraphNode)], bool]]) – This callback will receive all children.
- **mask** ([`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)) – Mask to filter the kind of node to look for.

**Returns:** If *callback* is None or a list then a list of [`maxon.GraphNode`](#module-maxon.GraphNode) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.GraphNode`](#module-maxon.GraphNode)], bool]

### `GraphNode.GetConnectionStamp(direction)` <a id="maxon.GraphNode.GetConnectionStamp"></a>

Returns the modification stamp of incoming/outgoing connections for this port.  
This is the value of the graph’s time stamp (see [`GraphModelInterface.GetModificationStamp()`](../interface/maxon.GraphModelInterface.md#maxon.GraphModelInterface.GetModificationStamp)) at the time when connections in the given direction have been modified last for this port.

**Parameters:** **direction** ([`maxon.PORT_DIR`](../../../enums/maxon.PORT_DIR.md#module-maxon.PORT_DIR)) – The connection direction.

**Returns:** The modification stamp of the last connection change of the port.

**Return type:**

`maxon.TimeStamp`

### `GraphNode.GetConnectionValue(target, position, attr, expectedType=None, reverse=False)` <a id="maxon.GraphNode.GetConnectionValue"></a>

Gets the value of the given attribute for the connection from this port to target.  
If there is no such connection, the connection has no value for the attribute or the value doesn’t have the expected type, an empty [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data) is returned.

**Parameters:**

- **target** ([`maxon.GraphNode`](#module-maxon.GraphNode)) – The other end of the connection.
- **position** ([`maxon.CONNECTION_POSITION`](../../../enums/maxon.CONNECTION_POSITION.md#module-maxon.CONNECTION_POSITION)) – The connection position at which the attribute’s value shall be obtained.
- **attr** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The attribute whose value shall be obtained.
- **expectedType** ([`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)) – The expected type of the attribute value, may be nullptr if no check shall be done.
- **reverse** (*bool*) – **True** if the connection shall be from target to this port (also *position* is reversed in this case), **False** otherwise (the default).

**Returns:** The attribute value of the connection, or a null [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data).

**Return type:** [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `GraphNode.GetConnectionValues(target, receiver)` <a id="maxon.GraphNode.GetConnectionValues"></a>

Gets all attribute values of the connection from this port to target.

**Parameters:**

- **target** – The other end of the connection.
- **receiver** (Callable[[[`maxon.CONNECTION_POSITION`](../../../enums/maxon.CONNECTION_POSITION.md#module-maxon.CONNECTION_POSITION), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)], bool]) – All attribute values of the connection will be reported to the receiver.

**Returns:** **False** if *receiver* cancelled further evaluation, **True** otherwise.

**Return type:** bool

### `GraphNode.GetConnections(pDir, conns=None, mask=maxon.Wires object at 0x12e9b874620 with the data: Wires - Value:63, Event:63, Dependency:63, Context:63, Hidden:63, Inhibit:63, Slink:63, Tlink:63, mode=1)` <a id="maxon.GraphNode.GetConnections"></a>

Yields all connections of this port for the given direction *dir*.  
Depending on the graph model implementation, this may include implicit wires due to connections between enclosing ports.  
The latter are marked with [`maxon.WIRE_MODE.IMPLICIT`](../../../enums/maxon.WIRE_MODE.IMPLICIT.md#maxon.WIRE_MODE.IMPLICIT).

**Parameters:**

- **pDir** ([`maxon.PORT_DIR`](../../../enums/maxon.PORT_DIR.md#module-maxon.PORT_DIR)) – Whether to yield incoming or outgoing connections.
- **conns** (Union[None, list, Callable[[[`maxon.GraphNode`](#module-maxon.GraphNode), [`maxon.Wires`](maxon.Wires.md#module-maxon.Wires)], bool]]) – The receiver for the found connections.
- **mask** ([`maxon.Wires`](maxon.Wires.md#module-maxon.Wires)) – Only yield connections whose wires match this mask.
- **mode** ([`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)) – Mode for GetConnections.

**Returns:** A list if *conns* is None or a list otherwise **False** if *conns* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[tuple[[`maxon.GraphNode`](#module-maxon.GraphNode), [`maxon.Wires`](maxon.Wires.md#module-maxon.Wires)]], bool]

### `GraphNode.GetConstantValue()` <a id="maxon.GraphNode.GetConstantValue"></a>

*Deprecated since version 2024.4:* Use [`maxon.GraphNode.GetEffectivePortValue()`](#maxon.GraphNode.GetEffectivePortValue) instead.

Returns the constant value of this port.  
The constant value is set whenever the graph implementation is able to determine a constant value for the port, either because the default value has been set directly at the port, or because it is possible to compute the value from connected ports and nodes.

**Returns:** The default value of this port.

**Returns:** [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `GraphNode.GetDefaultValue()` <a id="maxon.GraphNode.GetDefaultValue"></a>

*Deprecated since version 2024.4:* Use [`maxon.GraphNode.GetPortValue()`](#maxon.GraphNode.GetPortValue) instead.

Returns the default value of this port.  
This is the value of the DefaultValue attribute,which in turn is synthesized from `maxon.DESCRIPTION.DATA.BASE.DEFAULTVALUE`: (maxon.Id(“default”))  
Default values are derived from right to left along connections.

**Returns:** The default value of this port.

**Returns:** [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `GraphNode.GetEffectivePortValue()` <a id="maxon.GraphNode.GetEffectivePortValue"></a>

Returns the effective value of this port.

The effective value is set whenever the graph implementation is able to determine a constant value for the port either because the value has been set directly at the port, or because it is possible to compute the value from connected ports and nodes.

**Returns:** The effective value of this port, or an empty data if the port has no value.

**Return type:** [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `GraphNode.GetGraph()` <a id="maxon.GraphNode.GetGraph"></a>

Returns the graph to which this node belongs.

**Returns:** Owning graph of this node.

**Return type:** [`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)

### `GraphNode.GetHashCode()` <a id="maxon.GraphNode.GetHashCode"></a>

Returns the hash code of [`maxon.GraphNode`](#module-maxon.GraphNode).

**Returns:** Hash code.

**Return type:** int

### `GraphNode.GetId()` <a id="maxon.GraphNode.GetId"></a>

Returns the identifier of this node.  
This is the last part of the [`GraphNode.GetPath()`](#maxon.GraphNode.GetPath) “path”, so it’s unique within the siblings of this node, but not within the whole graph.

**Returns:** Identifier of this node.

**Return type:** [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)

### `GraphNode.GetInnerNodes(mask, includeThis, receiver=None)` <a id="maxon.GraphNode.GetInnerNodes"></a>

Yields all inner nodes of this node matching #mask in pre-order. The recursive traversal stops at nodes which don’t match *mask*.

**Parameters:**

- **mask** ([`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)) –

  Mask to filter the tree traversal.  
  Only nodes matching this mask are considered.  
  The node on which GetInnerNodes is called isn’t checked for mask.

- **includeThis** (*bool*) – If **True**, the node on which GetInnerNodes is called is yielded to *receiver* too.

- **receiver** (Union[Callable[[[`maxon.GraphNode`](#module-maxon.GraphNode)], bool], list, None]) – Inner nodes are reported to this value receiver.

**Returns:**

If None or a list, a list with all the inner [`maxon.GraphNode`](#module-maxon.GraphNode)  
*False** if *receiver* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.GraphNode`](#module-maxon.GraphNode)], bool]

### `GraphNode.GetInputs()` <a id="maxon.GraphNode.GetInputs"></a>

Returns the input port list of this node.  
All top-level input ports of a node can be found as children of its input port list.

**Returns:** Input port list of this node.

**Return type:** [`maxon.GraphNode`](#module-maxon.GraphNode)

### `GraphNode.GetKind()` <a id="maxon.GraphNode.GetKind"></a>

Returns the kind of this node.  
This can be used to check whether this node is a true node, a port or a port list, see [`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND) and [`maxon.GraphModelInterface`](../interface/maxon.GraphModelInterface.md#module-maxon.GraphModelInterface).

**Returns:** [`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)

### `GraphNode.GetMessageFlags(attr)` <a id="maxon.GraphNode.GetMessageFlags"></a>

Returns the message flags of the given attribute at this node.  
You have to call this method if you want to check if an attribute has a message (an error or a warning) for this node.

**Parameters:** **attr** (Union[str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – The attribute which shall be asked.

**Returns:** Message flags (GraphAttribute.FLAGS.WARNING, GraphAttribute.FLAGS.ERROR) of *attr* at this node.

**Return type:**

`maxon.GraphAttribute.FLAGS`

### `GraphNode.GetMessages(attr, receiver)` <a id="maxon.GraphNode.GetMessages"></a>

Yields the error or warning messages (if any) of the given attribute at this node to *receiver*.

**Parameters:**

- **attr** (Union[str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – The attribute which shall be asked.
- **receiver** (Callable[[[`maxon.GraphMessage`](../reference/maxon.GraphMessage.md#module-maxon.GraphMessage)], bool]) – All messages are reported to this receiver.

**Returns:** **False** if the receiver cancelled further evaluation, **True** otherwise.

**Return type:** bool

### `GraphNode.GetOutputs()` <a id="maxon.GraphNode.GetOutputs"></a>

Returns the output port list of this node.  
All top-level output ports of a node can be found as children of its output port list.

**Returns:** Output port list of this node.

**Return type:** [`maxon.GraphNode`](#module-maxon.GraphNode)

### `GraphNode.GetParent()` <a id="maxon.GraphNode.GetParent"></a>

Returns the parent of this node.

**Returns:** Parent node of this node, or a null node if this node is the root node.

**Return type:** [`maxon.GraphNode`](#module-maxon.GraphNode)

### `GraphNode.GetPath()` <a id="maxon.GraphNode.GetPath"></a>

Returns the path of this node.

> **Note:** It is not guaranteed that a node with that path still exists in the graph, to check this use `NodePath.IsValid()`.

**Returns:** Path of this node.

**Return type:** [`maxon.NodePath`](maxon.NodePath.md#module-maxon.NodePath)

### `GraphNode.GetPortList(dir)` <a id="maxon.GraphNode.GetPortList"></a>

Returns the input or output port list of this node, depending on dir.

**Parameters:** **dir** ([`maxon.PORT_DIR.INPUT`](../../../enums/maxon.PORT_DIR.INPUT.md#maxon.PORT_DIR.INPUT) or [`maxon.PORT_DIR.OUTPUT`](../../../enums/maxon.PORT_DIR.OUTPUT.md#maxon.PORT_DIR.OUTPUT).) – PORT_DIR.INPUT to return the input port list, PORT_DIR.OUTPUT to return the output port list.

**Returns:** Port list of this node.

**Return type:** [`maxon.GraphNode`](#module-maxon.GraphNode)

### `GraphNode.GetPortValue()` <a id="maxon.GraphNode.GetPortValue"></a>

Returns the value of this port (ignoring upstream overrides).

This is the value of the PortValue attribute, which in turn is synthesized from *maxon.DESCRIPTION.DATA.BASE.DEFAULTVALUE*. Port values are derived from right to left along connections.

**..note** Port values may be overridden by upstream values from incoming connections, you have to use GetEffectivePortValue to ask for the final port value.

**Returns:** The value of this port (ignoring upstream overrides), or an empty data if the port has no value.

**Return type:** [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `GraphNode.GetStoredValue(attr, expectedType=None)` <a id="maxon.GraphNode.GetStoredValue"></a>

Gets the current value of the given attribute for this node, REGARDLESS of whether it is valid or not.  
If using lazy updates then this may be out of date.  
If NOT using lazy updates then this should always match GetValue().  
If this node doesn’t have a value for the attribute of the correct type, an empty Opt is returned.

**Parameters:**

- **attr** (Union[str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – The attribute whose value shall be obtained.
- **expectedType** ([`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)) – The expected type of the attribute value, may be **None** if no check shall be done.

**Returns:** The attribute value of this node.

**Return type:** [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `GraphNode.GetValue(attr, expectedType=None)` <a id="maxon.GraphNode.GetValue"></a>

Gets the value of the given attribute *attr* for this node.  
If this node doesn’t have a value for the attribute of the correct type, an empty [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data) is returned.

**Parameters:**

- **attr** (Union[str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – The attribute whose value shall be obtained.
- **expectedType** ([`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)) – The expected type of the attribute value, may be **None** if no check shall be done.

**Returns:** The attribute value of this node

**Return type:** [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `GraphNode.GetValues(mask)` <a id="maxon.GraphNode.GetValues"></a>

Gets all attribute values of this node.

**Parameters:** **mask** ([`maxon.GraphAttributeInterface.FLAGS`](../../../enums/maxon.GraphAttributeInterface.FLAGS.md#module-maxon.GraphAttributeInterface.FLAGS)) – Specify which attributes kind to return.

**Returns:** All attribute values of this node.

**Return type:** list[[`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)]

### `GraphNode.GetWires(target)` <a id="maxon.GraphNode.GetWires"></a>

Returns the Wires from this node to #target.  
Depending on the graph model implementation, this may include implicit wires due to connections between enclosing nodes.  
The latter are marked with [`maxon.WIRE_MODE.IMPLICIT`](../../../enums/maxon.WIRE_MODE.IMPLICIT.md#maxon.WIRE_MODE.IMPLICIT).

**Parameters:** **target** ([`maxon.GraphNode`](#module-maxon.GraphNode)) – Another graph node.

**Returns:** Wires between from this node to *target*.

**Return type:** [`maxon.Wires`](maxon.Wires.md#module-maxon.Wires)

### `GraphNode.InheritValue(attr)` <a id="maxon.GraphNode.InheritValue"></a>

Restores the inherited state of the value for *attr*.  
This removes any value which has been set directly in this graph.

**Parameters:** **attr** (Union[str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – The attribute whose value shall be removed from this node.

**Returns:** True if the value has been inherited.

**Return type:** bool

### `GraphNode.IsConnectable(target)` <a id="maxon.GraphNode.IsConnectable"></a>

Checks if a connection from this port to target can be made.

**Parameters:** **target** ([`maxon.GraphNode`](#module-maxon.GraphNode)) – Target port of the (hypothetical) connection.

**Returns:** True if a connection is allowed, False otherwise.

**Return type:** bool

### `GraphNode.IsInner()` <a id="maxon.GraphNode.IsInner"></a>

Checks if this [`maxon.GraphNode`](#module-maxon.GraphNode) belongs to an inner node of the graph.  
The root node and its port lists and ports aren’t inner nodes, all other nodes are.

**Returns:** **True** if this [`maxon.GraphNode`](#module-maxon.GraphNode) is an inner node of the graph.

**Return type:** bool

### `GraphNode.IsPopulated()` <a id="maxon.GraphNode.IsPopulated"></a>

Checks whether this [`maxon.GraphNode`](#module-maxon.GraphNode) has graph and path references.  
This is not the same as [`GraphNode.IsValid()`](#maxon.GraphNode.IsValid), because [`GraphNode.IsPopulated()`](#maxon.GraphNode.IsPopulated) just checks if graph and path are set, but not if the graph really contains a node with the path, see [`GraphNode.IsValid()`](#maxon.GraphNode.IsValid).  
Therefore we also don’t have an `GraphNode.IsEmpty()` counterpart, because it would hide that there are two different functions to check the content of a [`maxon.GraphNode`](#module-maxon.GraphNode).

**Returns:** **True** if this GraphNode has graph and path set, **False** otherwise.

**Return type:** bool

### `GraphNode.IsRoot()` <a id="maxon.GraphNode.IsRoot"></a>

Checks if this GraphNode is the root node of the graph.

maxon.GraphNode() is not considered a root node, because it doesn’t belong to any graph.

**Returns:** True if this GraphNode is a valid root node.

**Return type:** bool

### `GraphNode.IsValid()` <a id="maxon.GraphNode.IsValid"></a>

Checks whether this GraphNode points to a valid node.  
This is not the same as [`GraphNode.IsPopulated()`](#maxon.GraphNode.IsPopulated):

- [`GraphNode.IsValid()`](#maxon.GraphNode.IsValid) return true if the node is a valid, existing node in the graph.
- [`GraphNode.IsPopulated()`](#maxon.GraphNode.IsPopulated) also returns true for graph nodes which point to non-existing (deleted) nodes.  
  They have a valid graph and path to identify the node, but you can’t call any function  
  which would require access to the node.

**Returns:**

**True** if this [`maxon.GraphNode`](#module-maxon.GraphNode) points to a valid node,  
**False** if it is a null node or a reference to a deleted node.

**Return type:** bool

### `GraphNode.Remove()` <a id="maxon.GraphNode.Remove"></a>

Removes this node from the graph.  
This will also remove all nested nodes as well as connections of this node and its nested ports.

### `GraphNode.RemoveConnections(pDir, mask)` <a id="maxon.GraphNode.RemoveConnections"></a>

Removes all connections of this port in the given direction which match the given *mask*.

**Parameters:**

- **pDir** ([`maxon.PORT_DIR`](../../../enums/maxon.PORT_DIR.md#module-maxon.PORT_DIR)) – Connection direction.
- **mask** ([`maxon.Wires`](maxon.Wires.md#module-maxon.Wires)) – Mask for the connections to remove.

### `GraphNode.RemovePorts(ports)` <a id="maxon.GraphNode.RemovePorts"></a>

Removes a number of variadic port instances from this variadic port.  
This is more efficient than a repeated call to [`GraphNode.Remove()`](#maxon.GraphNode.Remove) on each of the instances.

> **Warning:** It is an error if this GraphNode is no variadic port.

**Parameters:** **ports** (Union[list[str, [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]]) – The identifiers of the port instances which shall be removed.

**Returns:**

### `GraphNode.RemoveValue(attr)` <a id="maxon.GraphNode.RemoveValue"></a>

Removes an attribute value from this node.  
Nothing happens if this node doesn’t have a value for the given attribute.

**Parameters:** **attr** (Union[str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – The attribute whose value shall be removed from this node.

**Returns:** **True** if the value has been changed.

**Return type:** bool

### `GraphNode.Reset()` <a id="maxon.GraphNode.Reset"></a>

Resets this [`maxon.GraphNode`](#module-maxon.GraphNode) to the state it has right after default construction.  
This includes freeing all resources held by this [`maxon.GraphNode`](#module-maxon.GraphNode).

### `GraphNode.SetConnectionValue(target, position, attr, value)` <a id="maxon.GraphNode.SetConnectionValue"></a>

Sets the value of *attr* to *value* for the connection from this port to *target*.  
This will override any previously existing value.

**Parameters:**

- **target** ([`maxon.GraphNode`](#module-maxon.GraphNode)) – The other end of the connection.
- **position** ([`maxon.CONNECTION_POSITION`](../../../enums/maxon.CONNECTION_POSITION.md#module-maxon.CONNECTION_POSITION)) – The connection position at which the attribute’s value shall be set.
- **attr** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The attribute whose value shall be set.
- **value** ([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The value for the attribute.

**Returns:** **True** if the value has been changed.

**Return type:** bool

### `GraphNode.SetDefaultValue(value)` <a id="maxon.GraphNode.SetDefaultValue"></a>

*Deprecated since version 2024.4:* Use [`maxon.GraphNode.SetPortValue()`](#maxon.GraphNode.SetPortValue) instead.

Sets the value of the attribute `maxon.DESCRIPTION.DATA.BASE.DEFAULTVALUE` (maxon.Id(“default”)) to *value* for this port.  
This will override any values which would otherwise be inherited from a base port.

**Parameters:** **value** ([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The value for the DefaultValue attribute.

**Returns:** **True** if the value has been changed.

**Return type:** bool

### `GraphNode.SetPortValue(value)` <a id="maxon.GraphNode.SetPortValue"></a>

Sets the value of the attribute *maxon.DESCRIPTION.DATA.BASE.DEFAULTVALUE* to #value for this port.

This will override any values which would otherwise be inherited from a base or downstream port.

**Parameters:** **value** ([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – New value for the port.

**Returns:** True if the value has been changed, False otherwise.

**Return type:** bool

### `GraphNode.SetValue(attr, value, checkAndInvalidate=True)` <a id="maxon.GraphNode.SetValue"></a>

Sets the value of *attr* to *value* for this node.

> **Note:** This will override any previously existing value.

**Parameters:**

- **attr** (Union[str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – The attribute whose value shall be set.
- **value** ([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The value for the attribute.
- **checkAndInvalidate** (*bool*) – Validate the node once the value is set.

**Returns:** True if the value has been changed.

**Return type:** bool

### `GraphNode.TouchValue(attr)` <a id="maxon.GraphNode.TouchValue"></a>

Marks the value of *attr* as modified without actually modifying it.  
Use this if the value points to some external data which has changed without knowledge of the graph (for example a [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) for a file which has been modified).  
If there is no value yet for attr, an IllegalStateError is returned.

**Parameters:** **attr** (Union[str, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – The attribute whose value shall be set.

### `GraphNode.__eq__(other)` <a id="maxon.GraphNode.__eq__"></a>

Checks if two nodes are representing the same node in a graph.

**Parameters:** **other** ([`maxon.GraphNode`](#module-maxon.GraphNode)) – The other node.

**Return type:** bool

**Returns:** **True** if both node are equal.

### `GraphNode.__hash__()` <a id="maxon.GraphNode.__hash__"></a>

Return hash(self).

### `GraphNode.__init__(src=None)` <a id="maxon.GraphNode.__init__"></a>

Initializes a node from a graph.

**Parameters:** **src** (Optional[[`maxon.GraphNode`](#module-maxon.GraphNode)]) – Another node to re-use.

### `GraphNode.__ne__(other)` <a id="maxon.GraphNode.__ne__"></a>

Checks if two nodes are not representing the same node in a graph.

**Parameters:** **other** ([`maxon.GraphNode`](#module-maxon.GraphNode)) – The other node.

**Return type:** bool

**Returns:** **True** if both node are not equal.
