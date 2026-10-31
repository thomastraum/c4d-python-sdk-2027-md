<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/graphview/GvPort/index.html -->

# c4d.modules.graphview.GvPort <a id="c4d-modules-graphview-gvport"></a>

## *class* `c4d.modules.graphview.GvPort` <a id="c4d.modules.graphview.GvPort"></a>

A [`GvPort`](#c4d.modules.graphview.GvPort) is a port of a [`GvNode`](../GvNode/index.md#c4d.modules.graphview.GvNode)-object.

> **Note:**
>
> A [`GvPort`](#c4d.modules.graphview.GvPort) object cannot be alive without its owner.  
> Use `GvNode.AddPort()` to create a port.

## Overview <a id="overview"></a>

**Connection Management**

- [`GvPort.Connect()`](#c4d.modules.graphview.GvPort.Connect): Connects a port with another.
- [`GvPort.Remove()`](#c4d.modules.graphview.GvPort.Remove): Removes the connections of this port.

**Connection Routing**

- [`GvPort.GetDestination()`](#c4d.modules.graphview.GvPort.GetDestination): Returns the port where the port is linked with.
- [`GvPort.GetIncomingDestination()`](#c4d.modules.graphview.GvPort.GetIncomingDestination): Gets the destination of the incoming connection.
- [`GvPort.GetIncomingSource()`](#c4d.modules.graphview.GvPort.GetIncomingSource): Gets the source of the incoming connection.

**Connection Status**

- [`GvPort.GetNrOfConnections()`](#c4d.modules.graphview.GvPort.GetNrOfConnections): Get the number of connections, including both the incoming connection and outgoing connections.
- [`GvPort.IsIncomingConnected()`](#c4d.modules.graphview.GvPort.IsIncomingConnected): Check if there’s an incoming connection.

**Node Association**

- [`GvPort.GetNode()`](#c4d.modules.graphview.GvPort.GetNode): Returns the node of this port.

**Port Identity**

- [`GvPort.GetMainID()`](#c4d.modules.graphview.GvPort.GetMainID): Gets the main ID of the port.
- [`GvPort.GetSubID()`](#c4d.modules.graphview.GvPort.GetSubID): Gets the sub ID of the port.
- [`GvPort.SetMainID()`](#c4d.modules.graphview.GvPort.SetMainID): Sets the main ID of the port.

**Port Interface**

- [`GvPort.GetIO()`](#c4d.modules.graphview.GvPort.GetIO): Gets the IO mode for this port.
- [`GvPort.GetValueType()`](#c4d.modules.graphview.GvPort.GetValueType): Gets the value type of the port.

**Port Naming**

- [`GvPort.GetName()`](#c4d.modules.graphview.GvPort.GetName): Gets the name of this port.
- [`GvPort.SetName()`](#c4d.modules.graphview.GvPort.SetName): Sets the name of this port.

**User Data**

- [`GvPort.GetUserData()`](#c4d.modules.graphview.GvPort.GetUserData): Internal.
- [`GvPort.SetUserData()`](#c4d.modules.graphview.GvPort.SetUserData): Internal.

**User Identification**

- [`GvPort.GetUserID()`](#c4d.modules.graphview.GvPort.GetUserID): Gets the user ID of the port.
- [`GvPort.SetUserID()`](#c4d.modules.graphview.GvPort.SetUserID): Sets the user ID of the port.

**Visibility**

- [`GvPort.GetVisible()`](#c4d.modules.graphview.GvPort.GetVisible): Checks if this port is hidden or visible.
- [`GvPort.SetVisible()`](#c4d.modules.graphview.GvPort.SetVisible): Set the visibility of the port.

## Members <a id="members"></a>

### Connection Management <a id="c4d.modules.graphview.GvPort-method-Connection-Management"></a>

#### `GvPort.Connect(self, port)` <a id="c4d.modules.graphview.GvPort.Connect"></a>

Connects a port with another.

> **Note:** Remember, the nodes of the ports have to be in the same [`GvNodeMaster`](../GvNodeMaster/index.md#c4d.modules.graphview.GvNodeMaster), otherwise the connection fails.

**Parameters:** **port** ([*c4d.modules.graphview.GvPort*](#c4d.modules.graphview.GvPort)) – The port to connect to.

**Return type:** bool

**Returns:** **True** on succeeded connection, otherwise **False**.

#### `GvPort.Remove(self)` <a id="c4d.modules.graphview.GvPort.Remove"></a>

Removes the connections of this port.

**Return type:** bool

**Returns:** **True** if the connection was removed, otherwise **False**.

### Connection Routing <a id="c4d.modules.graphview.GvPort-method-Connection-Routing"></a>

#### `GvPort.GetDestination(self)` <a id="c4d.modules.graphview.GvPort.GetDestination"></a>

Returns the port where the port is linked with.

**Return type:** List[[c4d.modules.graphview.GvPort](#c4d.modules.graphview.GvPort)]

**Param:** A list with all destinations.

#### `GvPort.GetIncomingDestination(self, node, port)` <a id="c4d.modules.graphview.GvPort.GetIncomingDestination"></a>

Gets the destination of the incoming connection.

**Returns:** A tuple with the incoming destination node and the incoming destination port.

**Return type:** tuple[[c4d.modules.graphview.GvNode](../GvNode/index.md#c4d.modules.graphview.GvNode), [c4d.modules.graphview.GvPort](#c4d.modules.graphview.GvPort)]

#### `GvPort.GetIncomingSource(self, node, port)` <a id="c4d.modules.graphview.GvPort.GetIncomingSource"></a>

Gets the source of the incoming connection.

**Returns:** A tuple with the incoming source node and the incoming source port.

**Return type:** tuple[[c4d.modules.graphview.GvNode](../GvNode/index.md#c4d.modules.graphview.GvNode), [c4d.modules.graphview.GvPort](#c4d.modules.graphview.GvPort)]

### Connection Status <a id="c4d.modules.graphview.GvPort-method-Connection-Status"></a>

#### `GvPort.GetNrOfConnections(self)` <a id="c4d.modules.graphview.GvPort.GetNrOfConnections"></a>

Get the number of connections, including both the incoming connection and outgoing connections.

**Return type:** int

**Returns:** Number of connections.

#### `GvPort.IsIncomingConnected(self)` <a id="c4d.modules.graphview.GvPort.IsIncomingConnected"></a>

Check if there’s an incoming connection.

**Return type:** bool

**Returns:** **True** if there’s an incoming connection to the port, otherwise **False**.

### Node Association <a id="c4d.modules.graphview.GvPort-method-Node-Association"></a>

#### `GvPort.GetNode(self)` <a id="c4d.modules.graphview.GvPort.GetNode"></a>

Returns the node of this port.

**Return type:** [c4d.modules.graphview.GvNode](../GvNode/index.md#c4d.modules.graphview.GvNode)

**Param:** The container

### Port Identity <a id="c4d.modules.graphview.GvPort-method-Port-Identity"></a>

#### `GvPort.GetMainID(self)` <a id="c4d.modules.graphview.GvPort.GetMainID"></a>

Gets the main ID of the port.

**Return type:** int

**Returns:** Main ID.

#### `GvPort.GetSubID(self)` <a id="c4d.modules.graphview.GvPort.GetSubID"></a>

Gets the sub ID of the port.

**Return type:** int

**Returns:** Sub ID.

#### `GvPort.SetMainID(self, id)` <a id="c4d.modules.graphview.GvPort.SetMainID"></a>

Sets the main ID of the port.

**Parameters:** **id** (*int*) – New main ID.

### Port Interface <a id="c4d.modules.graphview.GvPort-method-Port-Interface"></a>

#### `GvPort.GetIO(self)` <a id="c4d.modules.graphview.GvPort.GetIO"></a>

Gets the IO mode for this port.

**Return type:** int

**Returns:**

IO mode:

|   |   |
|---|---|
| *GV_PORT_INVALID* | Invalid. |
| *GV_PORT_INPUT* | Input. |
| *GV_PORT_OUTPUT* | Output. |
| *GV_PORT_INPUT_OR_GEDATA* | Input or GeData. |

#### `GvPort.GetValueType(self)` <a id="c4d.modules.graphview.GvPort.GetValueType"></a>

Gets the value type of the port.

**Return type:** int

**Returns:** The value type.

### Port Naming <a id="c4d.modules.graphview.GvPort-method-Port-Naming"></a>

#### `GvPort.GetName(self, node)` <a id="c4d.modules.graphview.GvPort.GetName"></a>

Gets the name of this port.

**Parameters:** **node** ([*c4d.modules.graphview.GvNode*](../GvNode/index.md#c4d.modules.graphview.GvNode)) – The node the port belongs to

**Return type:** str

**Returns:** Port name.

#### `GvPort.SetName(self, name)` <a id="c4d.modules.graphview.GvPort.SetName"></a>

Sets the name of this port.

**Parameters:** **name** (*str*) – Port name.

### User Data <a id="c4d.modules.graphview.GvPort-method-User-Data"></a>

#### `GvPort.GetUserData(self)` <a id="c4d.modules.graphview.GvPort.GetUserData"></a>

Internal.

*New in version R17.048.*

#### `GvPort.SetUserData(self)` <a id="c4d.modules.graphview.GvPort.SetUserData"></a>

Internal.

*New in version R17.048.*

### User Identification <a id="c4d.modules.graphview.GvPort-method-User-Identification"></a>

#### `GvPort.GetUserID(self)` <a id="c4d.modules.graphview.GvPort.GetUserID"></a>

Gets the user ID of the port.

**Return type:** int

**Returns:** Sub ID.

#### `GvPort.SetUserID(self, id)` <a id="c4d.modules.graphview.GvPort.SetUserID"></a>

Sets the user ID of the port.

**Parameters:** **id** (*int*) – The user ID to set.

### Visibility <a id="c4d.modules.graphview.GvPort-method-Visibility"></a>

#### `GvPort.GetVisible(self)` <a id="c4d.modules.graphview.GvPort.GetVisible"></a>

Checks if this port is hidden or visible.

**Return type:** bool

**Returns:** **True** if visible, otherwise **False**.

#### `GvPort.SetVisible(self, v)` <a id="c4d.modules.graphview.GvPort.SetVisible"></a>

Set the visibility of the port.

**Parameters:** **v** (*bool*) – **False** for an invisible port.
