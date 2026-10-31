<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon/frameworks/graph.html -->

# maxon.frameworks.graph <a id="maxon-frameworks-graph"></a><a id="framework-graph"></a>

> **Note:** Members documented here are defined in `maxon.frameworks.graph` module and are also exposed to the global `maxon` module. See the [Maxon API](../../../manuals/manual_api_overview.md#maxon-api-introduction) section of the API Overview for more information about the special conventions of this API.

## Description <a id="description"></a>

Module for graph structures.

## Interfaces <a id="interfaces"></a>

|   |   |
|---|---|
| [`GraphModelHelper`](../../maxon_generated/frameworks/graph/interface/maxon.GraphModelHelper.md#module-maxon.GraphModelHelper)() | Regroups functions to simplify the usage of the node API. |
| [`GraphAttributeInterface`](../../maxon_generated/frameworks/graph/interface/maxon.GraphAttributeInterface.md#module-maxon.GraphAttributeInterface)(*args) | A graph attribute provides extra information about an attribute of nodes and ports. |
| [`GraphMessageInterface`](../../maxon_generated/frameworks/graph/interface/maxon.GraphMessageInterface.md#module-maxon.GraphMessageInterface)(*args) | A graph message is an error or warning message to tell the user about issues found in the graph. |
| [`GraphModelInterface`](../../maxon_generated/frameworks/graph/interface/maxon.GraphModelInterface.md#module-maxon.GraphModelInterface)(*args) | GraphModelInterface is an abstraction of a hierarchical graph. |
| [`NodePathInterface`](../../maxon_generated/frameworks/graph/interface/maxon.NodePathInterface.md#module-maxon.NodePathInterface)() | A [`maxon.NodePath`](../../maxon_generated/frameworks/graph/datatype/maxon.NodePath.md#module-maxon.NodePath) identifies a graph node (a true node, port or port list) within a node graph. |
| [`GraphLib`](../../maxon_generated/frameworks/graph/interface/maxon.GraphLib.md#module-maxon.GraphLib)() | GraphLib contains some static functions for graphs. |

## References <a id="references"></a>

|   |   |
|---|---|
| [`GraphAttribute`](../../maxon_generated/frameworks/graph/reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute)(*args) | Reference class for [`maxon.GraphAttributeInterface`](../../maxon_generated/frameworks/graph/interface/maxon.GraphAttributeInterface.md#module-maxon.GraphAttributeInterface). |
| [`GraphModelRef`](../../maxon_generated/frameworks/graph/reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)(*args) | Reference class for [`maxon.GraphModelInterface`](../../maxon_generated/frameworks/graph/interface/maxon.GraphModelInterface.md#module-maxon.GraphModelInterface). |
| [`GraphMessage`](../../maxon_generated/frameworks/graph/reference/maxon.GraphMessage.md#module-maxon.GraphMessage)(*args) | Reference class for [`maxon.GraphMessageInterface`](../../maxon_generated/frameworks/graph/interface/maxon.GraphMessageInterface.md#module-maxon.GraphMessageInterface). |

## Data Types <a id="data-types"></a>

|   |   |
|---|---|
| [`GraphNode`](../../maxon_generated/frameworks/graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode)([src]) | A [`maxon.GraphNode`](../../maxon_generated/frameworks/graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode) represents a general node (g-node for short) in the hierarchy of a [`maxon.GraphModelInterface`](../../maxon_generated/frameworks/graph/interface/maxon.GraphModelInterface.md#module-maxon.GraphModelInterface). |
| [`GraphTransaction`](../../maxon_generated/frameworks/graph/datatype/maxon.GraphTransaction.md#module-maxon.GraphTransaction)([src]) | Modifications to a GraphModelInterface may only be done when there is an active GraphTransaction. |
| [`NodePath`](../../maxon_generated/frameworks/graph/datatype/maxon.NodePath.md#module-maxon.NodePath)(*args) | Reference class for [`maxon.NodePathInterface`](../../maxon_generated/frameworks/graph/interface/maxon.NodePathInterface.md#module-maxon.NodePathInterface). |
| [`Wires`](../../maxon_generated/frameworks/graph/datatype/maxon.Wires.md#module-maxon.Wires)([value, event, dependency, context, …]) | A port connection consists of up to eight independent wires: |

## Enums <a id="enums"></a>

|   |   |
|---|---|
| [`GraphModelInterface.GET_CONNECTIONS_MODE`](../../maxon_generated/enums/maxon.GraphModelInterface.GET_CONNECTIONS_MODE.md#module-maxon.GraphModelInterface.GET_CONNECTIONS_MODE)() | Used with [`GraphNode.GetConnections()`](../../maxon_generated/frameworks/graph/datatype/maxon.GraphNode.md#maxon.GraphNode.GetConnections) to control which connections shall be reported. |
| [`GraphModelInterface.MODIFIED`](../../maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.md#module-maxon.GraphModelInterface.MODIFIED)() | These flags are reported by [`GraphModelInterface.GetModificationsSince()`](../../maxon_generated/frameworks/graph/interface/maxon.GraphModelInterface.md#maxon.GraphModelInterface.GetModificationsSince) to tell which properties of the node have changed. |
| [`GraphAttributeInterface.FLAGS`](../../maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.md#module-maxon.GraphAttributeInterface.FLAGS)() | FLAGS provide information about the nature of the attribute. |
| [`CONNECTION_POSITION`](../../maxon_generated/enums/maxon.CONNECTION_POSITION.md#module-maxon.CONNECTION_POSITION)() | Graph connections can “store attribute values” [`GraphNode.GetConnectionValue()`](../../maxon_generated/frameworks/graph/datatype/maxon.GraphNode.md#maxon.GraphNode.GetConnectionValue) at three different positions: |
| [`NODE_KIND`](../../maxon_generated/enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)() | NODE_KIND allows to determine whether a general node (g-node for short) is a true node, a port or a port list. |
| [`WIRE_MODE`](../../maxon_generated/enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)() | WIRE_MODE is used for the wires in a Wires object to control whether a wire is set, inherited or hidden. |
