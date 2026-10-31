<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/graph/interface/maxon.GraphModelHelper.html -->

# maxon.GraphModelHelper <a id="maxon-graphmodelhelper"></a>

## Description <a id="module-maxon.GraphModelHelper"></a><a id="description"></a>

Regroups functions to simplify the usage of the node API. Those functions help developers retrieving and manipulate information about a node system. Those functions mainly use internal function from the GraphModelInterface and do not offer more functionalities than what can be already done.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`CreateInputPort`](#maxon.GraphModelHelper.CreateInputPort)(node, id, name) | Creates and returns a new InputPort. |
| [`CreateOutputPort`](#maxon.GraphModelHelper.CreateOutputPort)(node, id, name) | Creates and returns a new OutputPort. |
| [`DeselectAll`](#maxon.GraphModelHelper.DeselectAll)(graphModel, kind) | Deselect all True Nodes and ports based on the NODE_KIND passed as parameter. |
| [`DeselectConnection`](#maxon.GraphModelHelper.DeselectConnection)(srcPort, dstPort) | Deselects the connection between two ports. A connection hold a Wire object, itself holding 8 wires. |
| [`DeselectNode`](#maxon.GraphModelHelper.DeselectNode)(node) | Deselects a node or a port. |
| [`FindNodesByAssetId`](#maxon.GraphModelHelper.FindNodesByAssetId)(graphModel, assetId, exactId) | Find all true nodes that have the same AssetId as the passed argument. Only nodes have assetId. |
| [`FindNodesById`](#maxon.GraphModelHelper.FindNodesById)(graphModel, nodeId, kind, …) | Find all true nodes that have the same AssetId as the passed argument. Only nodes have assetId. |
| [`FindNodesByName`](#maxon.GraphModelHelper.FindNodesByName)(graphModel, nodeName, kind, …) | Find all GraphNode (true nodes or ports) that have the same name as the passed argument. |
| [`GetAllPredecessors`](#maxon.GraphModelHelper.GetAllPredecessors)(node, filter[, callback]) | Retrieves all nodes or ports connected to the passed port or node. |
| [`GetAllSuccessors`](#maxon.GraphModelHelper.GetAllSuccessors)(node, filter[, callback]) | Retrieves all nodes or ports connected to the passed port or node. |
| [`GetDirectPredecessors`](#maxon.GraphModelHelper.GetDirectPredecessors)(node, filter[, callback]) | Retrieves the first level of nodes or ports connected to the passed port or node. |
| [`GetDirectSuccessors`](#maxon.GraphModelHelper.GetDirectSuccessors)(node, filter[, callback]) | Retrieves the first level of nodes or ports connected to the passed port or node. |
| [`GetSelectedConnections`](#maxon.GraphModelHelper.GetSelectedConnections)(graphModel[, callback]) | Retrieves all the selected connections on the graph. |
| [`GetSelectedNodes`](#maxon.GraphModelHelper.GetSelectedNodes)(graphModel, kind[, callback]) | Retrieves all selected ports and/or true node on the graph depending on the NODE_KIND passed as argument. |
| [`IsConnected`](#maxon.GraphModelHelper.IsConnected)(node, port) | Checks if this node or port is connected to another port. |
| [`IsConnectionSelected`](#maxon.GraphModelHelper.IsConnectionSelected)(srcPort, dstPort) | Checks if a connection between two port is selected. A connection hold a Wire object. |
| [`IsNodeSelected`](#maxon.GraphModelHelper.IsNodeSelected)(node) | Returns if the node or the port is selected or not. |
| [`ListAllNodes`](#maxon.GraphModelHelper.ListAllNodes)(graphModel, matchingData[, …]) | Retrieves all nodes having their stored data equals the ones in the passed DataDictionary. |
| [`MuteAllConnections`](#maxon.GraphModelHelper.MuteAllConnections)(node, direction) | Mutes all incoming or outgoing connections of a node depending on the specified direction |
| [`MuteConnection`](#maxon.GraphModelHelper.MuteConnection)(srcNode, dstPort) | Mutes the connection between a node or port and another port. |
| [`RemoveAllConnections`](#maxon.GraphModelHelper.RemoveAllConnections)(node) | Removes all the connection a true node have. The node should be a true node. |
| [`RemoveConnection`](#maxon.GraphModelHelper.RemoveConnection)(srcPort, dstPort) | Removes the connections between two port. |
| [`SelectConnection`](#maxon.GraphModelHelper.SelectConnection)(srcPort, dstPort) | Selects the connection between two ports. |
| [`SelectNode`](#maxon.GraphModelHelper.SelectNode)(node) | Selects a node or a port. |
| [`UnmuteAllConnections`](#maxon.GraphModelHelper.UnmuteAllConnections)(node, direction) | Unmutes all the connections in one direction. |
| [`UnmuteConnection`](#maxon.GraphModelHelper.UnmuteConnection)(srcNode, dstPort) | Unmutes the connection between a node or port and another port. |

## Methods Definition <a id="methods-definition"></a>

### *static* `GraphModelHelper.CreateInputPort(node, id, name)` <a id="maxon.GraphModelHelper.CreateInputPort"></a>

Creates and returns a new InputPort.  
The port will be identified by the passed id and will be renamed with the passed string.  
This new port can only be created on the root or any group node.

**Parameters:**

- **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The node where to create the input port.
- **id** (*Union*[*maxon.Id*, *str*, *maxon.String*]) – The id of the port that need to be created.
- **name** (*Union*[*maxon.Id*, *str*, *maxon.String*]) – The name of the port that need to be created.

**Returns:** The created port.

**Return type:** [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)

### *static* `GraphModelHelper.CreateOutputPort(node, id, name)` <a id="maxon.GraphModelHelper.CreateOutputPort"></a>

Creates and returns a new OutputPort.  
The port will be identified by the passed id and will be renamed with the passed string.  
This new port can only be created on the root or any group node.

**Parameters:**

- **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The node where to create the output port.
- **id** (*Union*[*maxon.Id*, *str*, *maxon.String*]) – The id of the port that need to be created.
- **name** (*Union*[*maxon.Id*, *str*, *maxon.String*]) – The name of the port that need to be created.

**Returns:** The created port.

**Return type:** [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)

### *static* `GraphModelHelper.DeselectAll(graphModel, kind)` <a id="maxon.GraphModelHelper.DeselectAll"></a>

Deselect all True Nodes and ports based on the NODE_KIND passed as parameter.

**Parameters:**

- **graphModel** ([`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)) – The GraphModelRef to deselect elements.
- **kind** ([`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)) – The GraphNode’s kind that will be deselected.

### *static* `GraphModelHelper.DeselectConnection(srcPort, dstPort)` <a id="maxon.GraphModelHelper.DeselectConnection"></a>

Deselects the connection between two ports. A connection hold a Wire object, itself holding 8 wires.  
There is at most one connection between two ports.

**Parameters:**

- **srcPort** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The connection’s source port.
- **dstPort** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The connection’s destination port.

### *static* `GraphModelHelper.DeselectNode(node)` <a id="maxon.GraphModelHelper.DeselectNode"></a>

Deselects a node or a port.

**Parameters:** **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The node or the port that have to be Deselected.

### *static* `GraphModelHelper.FindNodesByAssetId(graphModel, assetId, exactId, callback=None)` <a id="maxon.GraphModelHelper.FindNodesByAssetId"></a>

Find all true nodes that have the same AssetId as the passed argument. Only nodes have assetId.  
This function will return several nodes if they share the same assetId.

**Parameters:**

- **graphModel** ([`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)) – The GraphModelRef to search for the nodes.
- **assetId** (*Union*[*str*, *maxon.String*, *maxon.Id*]) – The AssetId of the true node or the port to look for. This has the form of a reversed domain string. e.g “net.maxon.asset.utility.color”
- **exactId** (*bool*) – Set **True** if the exact id should be search. If this is set to **False**, check if the passed id is contained in the node assetID.
- **callback** (Union[None, list, Callable[[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]]) – This callback will receive all ports and/or True Node that have the same name.

**Returns:** If *callback* is None or a list then a list of [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]

### *static* `GraphModelHelper.FindNodesById(graphModel, nodeId, kind, direction, exactId, callback=None)` <a id="maxon.GraphModelHelper.FindNodesById"></a>

Find all true nodes that have the same AssetId as the passed argument. Only nodes have assetId.  
This function will return several nodes if they share the same assetId.

**Parameters:**

- **graphModel** ([`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)) – The GraphModelRef to search for the nodes.
- **nodeId** (*Union*[*str*, *maxon.String*, *maxon.Id*]) – The id of the true node or the port to look for.
- **kind** ([`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)) – Filter that will be applied to the kind of GraphNode we are looking for. By default, All type (true node/ports)
- **direction** ([`maxon.PORT_DIR`](../../../enums/maxon.PORT_DIR.md#module-maxon.PORT_DIR)) – Filter the GraphNode by direction. Input or Output.
- **exactId** (*bool*) – Set true if the exact id should be search. If this is set to false, check if the passed id is contained in the GraphNode’s id.
- **callback** (Union[None, list, Callable[[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]]) – This callback will receive all ports and/or True Node that have the same name.

**Returns:** If *callback* is None or a list then a list of [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]

### *static* `GraphModelHelper.FindNodesByName(graphModel, nodeName, kind, direction, exactName, callback)` <a id="maxon.GraphModelHelper.FindNodesByName"></a>

Find all GraphNode (true nodes or ports) that have the same name as the passed argument.  
This function will return several nodes/port if they share the same name.

> **Warning:**
>
> Name of true nodes or port can change depending on the language of Cinema4D.  
> Search based on name should be avoided as mush as possible, unless you are sure the name will not be different on any setup.

**Parameters:**

- **graphModel** ([`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)) – The GraphModelRef to search for the nodes.
- **nodeName** (*Union*[*str*, *maxon.String*]) – The name of the true node or the port to look for.
- **kind** ([`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)) – Filter that will be applied to the kind of GraphNode we are looking for. By default, All type (true node/ports)
- **direction** ([`maxon.PORT_DIR`](../../../enums/maxon.PORT_DIR.md#module-maxon.PORT_DIR)) – Filter the GraphNode by direction. Input or Output.
- **exactName** (*bool*) – Set true if the exact name should be search. If this is set to false, check if the passed name is contained in the GraphNode’s name.
- **callback** (Union[None, list, Callable[[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]]) – This callback will receive all ports and/or true node that have the same name.

**Returns:** If *callback* is None or a list then a list of [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]

### *static* `GraphModelHelper.GetAllPredecessors(node, filter, callback=None)` <a id="maxon.GraphModelHelper.GetAllPredecessors"></a>

Retrieves all nodes or ports connected to the passed port or node. This will only retrieve nodes or ports that are connected to the inputs.

**Parameters:**

- **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The starting point to retrieve all the predecessor. A node or a port can be used. If a port is used, an input port must be used.

- **filter** ([`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)) – The NODE_KIND that will be included. The function search for all possible nodes or ports and will include them or not based on this filter.

- **callback** (Union[None, list, Callable[[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]]) –

  If a callable, this will be called with all the connected nodes.  
  If a list is passed, connected nodes will be added to it.  
  If a None is passed, a list containing connected nodes will be returned.

**Returns:** If *callback* is None or a list then a list of [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]

### *static* `GraphModelHelper.GetAllSuccessors(node, filter, callback=None)` <a id="maxon.GraphModelHelper.GetAllSuccessors"></a>

Retrieves all nodes or ports connected to the passed port or node. This will only retrieve nodes or ports that are connected to the outputs.

**Parameters:**

- **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The starting point to retrieve all the successors. A node or a port can be used. If a port is used, an output port must be used.

- **filter** ([`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)) – The NODE_KIND that will be included. The function search for all possible nodes or ports and will include them or not based on this filter.

- **callback** (Union[None, list, Callable[[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]]) –

  If a callable, this will be called with all the connected nodes.  
  If a list is passed, connected nodes will be added to it.  
  If a None is passed, a list containing connected nodes will be returned.

**Returns:** If *callback* is None or a list then a list of [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]

### *static* `GraphModelHelper.GetDirectPredecessors(node, filter, callback=None)` <a id="maxon.GraphModelHelper.GetDirectPredecessors"></a>

Retrieves the first level of nodes or ports connected to the passed port or node. This will only retrieve nodes or ports that are connected to the inputs.

**Parameters:**

- **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The starting point to retrieve the direct predecessors. A node or a port can be used. If a port is used, an input port must be used.

- **filter** ([`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)) – The NODE_KIND that will be included. The function search for all possible nodes or ports and will include them or not based on this filter.

- **callback** (Union[None, list, Callable[[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]]) –

  If a callable, this will be called with all the connected nodes.  
  If a list is passed, connected nodes will be added to it.  
  If a None is passed, a list containing connected nodes will be returned.

**Returns:** If *callback* is None or a list then a list of [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]

### *static* `GraphModelHelper.GetDirectSuccessors(node, filter, callback=None)` <a id="maxon.GraphModelHelper.GetDirectSuccessors"></a>

Retrieves the first level of nodes or ports connected to the passed port or node. This will only retrieve nodes or ports that are connected to the outputs.

**Parameters:**

- **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The starting point to retrieve the direct successors. A node or a port can be used. If a port is used, an output port must be used.

- **filter** ([`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)) – The NODE_KIND that will be included. The function search for all possible nodes or ports and will include them or not based on this filter.

- **callback** (Union[None, list, Callable[[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]]) –

  If a callable, this will be called with all the connected nodes.  
  If a list is passed, connected nodes will be added to it.  
  If a None is passed, a list containing connected nodes will be returned.

**Returns:** If *callback* is None or a list then a list of [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]

### *static* `GraphModelHelper.GetSelectedConnections(graphModel, callback=None)` <a id="maxon.GraphModelHelper.GetSelectedConnections"></a>

Retrieves all the selected connections on the graph. A connection hold a Wire object. There is none or only one connection between two ports, and this connection is composed by multiple wires.

**Parameters:**

- **graphModel** ([`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)) – The GraphModelRef to retrieve the GraphNode from the path.
- **callback** (Union[None, list, Callable[[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode), [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode), [`maxon.Wires`](../datatype/maxon.Wires.md#module-maxon.Wires)], bool]]) – This callback will receive the source and destination ports and the wire itself

**Returns:** If *callback* is None or a list then a list of [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]

### *static* `GraphModelHelper.GetSelectedNodes(graphModel, kind, callback=None)` <a id="maxon.GraphModelHelper.GetSelectedNodes"></a>

Retrieves all selected ports and/or true node on the graph depending on the NODE_KIND passed as argument.

**Parameters:**

- **graphModel** ([`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)) – The GraphModelRef to retrieve the selected elements.
- **kind** ([`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)) – The GraphNode kind to check.
- **callback** (Union[None, list, Callable[[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]]) – The list or callable to pass the found nodes to.

**Returns:** If *callback* is None or a list then a list of [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]

### *static* `GraphModelHelper.IsConnected(node, port)` <a id="maxon.GraphModelHelper.IsConnected"></a>

Checks if this node or port is connected to another port.  
If a true node is passed, every port on the node will be tested. If a port is passed, only the passed port will be tested.

**Parameters:**

- **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The node to check the connection with.
- **port** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The port to check the connection with.

**Returns:** **True** if ports are connected, otherwise **False**.

**Return type:** bool

### *static* `GraphModelHelper.IsConnectionSelected(srcPort, dstPort)` <a id="maxon.GraphModelHelper.IsConnectionSelected"></a>

Checks if a connection between two port is selected. A connection hold a Wire object.  
There is at most one connection between two port, but this connection is composed by 8 wires.  
If a GraphNode is passed instead a NodePath, the GraphNode will be converted to NodePath.

**Parameters:**

- **srcPort** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The connection’s source port.
- **dstPort** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The connection’s destination port.

**Returns:** **True** if the connection is selected, otherwise **False**.

**Return type:** bool

### *static* `GraphModelHelper.IsNodeSelected(node)` <a id="maxon.GraphModelHelper.IsNodeSelected"></a>

Returns if the node or the port is selected or not.

**Parameters:** **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The Node or the Port to check.

**Returns:** **True** if the node or the port is selected, otherwise **False**.

**Return type:** bool

### *static* `GraphModelHelper.ListAllNodes(graphModel, matchingData, callback=None)` <a id="maxon.GraphModelHelper.ListAllNodes"></a>

Retrieves all nodes having their stored data equals the ones in the passed DataDictionary.  
The passed DataDictionary can have one or multiple data defined.  
The function will compare all the value inside the DataDictionary, if they all match, the node will be returned.

```python
# Retrieve all nodes with a defined name
nodeProperties = maxon.DataDictionary();
nodeProperties.Set(maxon.NODE.BASE.NAME, groupName)

for child in maxon.GraphModelHelper.ListAllNodes(nodeGraph, nodeProperties):
    print(f"node that have this name {child}")
```

**Parameters:**

- **graphModel** ([`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)) – The GraphModelRef to list the node.

- **matchingData** ([`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)) –

  The Dictionary filled with the data we want to compare the GraphNode with.  
  All node founded that have the same data values than those passed within the Dictionary.

- **callback** (Union[None, list, Callable[[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]]) – This callback will receive all nodes founded that have the same data values than those passed within the Dictionary

**Returns:** If *callback* is None or a list then a list of [`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)], bool]

### *static* `GraphModelHelper.MuteAllConnections(node, direction)` <a id="maxon.GraphModelHelper.MuteAllConnections"></a>

Mutes all incoming or outgoing connections of a node depending on the specified direction

**Parameters:**

- **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The true node to mute all the connections.
- **direction** ([`maxon.PORT_DIR`](../../../enums/maxon.PORT_DIR.md#module-maxon.PORT_DIR)) – The direction where all connection will be muted.

### *static* `GraphModelHelper.MuteConnection(srcNode, dstPort)` <a id="maxon.GraphModelHelper.MuteConnection"></a>

Mutes the connection between a node or port and another port.  
If a true node is passed, and the port is connected to one or several input port, all the connections will be muted between the port and the node.  
For example, a constant port is connected to several input port of another node.

**Parameters:**

- **srcNode** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The node to mute the connection with.
- **dstPort** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The other port the connection must be muted.

### *static* `GraphModelHelper.RemoveAllConnections(node)` <a id="maxon.GraphModelHelper.RemoveAllConnections"></a>

Removes all the connection a true node have. The node should be a true node.  
To remove connection for a port, use `GraphNodeFunctions.RemoveConnections()`

**Parameters:** **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The node to remove all the connections to.

### *static* `GraphModelHelper.RemoveConnection(srcPort, dstPort)` <a id="maxon.GraphModelHelper.RemoveConnection"></a>

Removes the connections between two port.

**Parameters:**

- **srcPort** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The source’s port.
- **dstPort** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The destination’s port.

### *static* `GraphModelHelper.SelectConnection(srcPort, dstPort)` <a id="maxon.GraphModelHelper.SelectConnection"></a>

Selects the connection between two ports.

**Parameters:**

- **srcPort** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The connection’s source port.
- **dstPort** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The connection’s destination port.

### *static* `GraphModelHelper.SelectNode(node)` <a id="maxon.GraphModelHelper.SelectNode"></a>

Selects a node or a port.

**Parameters:** **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The node or the port that have to be selected.

### *static* `GraphModelHelper.UnmuteAllConnections(node, direction)` <a id="maxon.GraphModelHelper.UnmuteAllConnections"></a>

Unmutes all the connections in one direction.

**Parameters:**

- **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The node to unmute the connection.
- **direction** ([`maxon.PORT_DIR`](../../../enums/maxon.PORT_DIR.md#module-maxon.PORT_DIR)) – The direction where all connection will be Unmuted

### *static* `GraphModelHelper.UnmuteConnection(srcNode, dstPort)` <a id="maxon.GraphModelHelper.UnmuteConnection"></a>

Unmutes the connection between a node or port and another port.  
If a true node is passed, depending of the port passed direction, every output or every input will be unmuted.

**Parameters:**

- **srcNode** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The node to unmute the connection with.
- **dstPort** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – The other port that the connection must be Unmuted.
