<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon/frameworks/nodes.html -->

# maxon.frameworks.nodes <a id="maxon-frameworks-nodes"></a><a id="framework-nodes"></a>

> **Note:** Members documented here are defined in `maxon.frameworks.nodes` module and are also exposed to the global `maxon` module. See the [Maxon API](../../../manuals/manual_api_overview.md#maxon-api-introduction) section of the API Overview for more information about the special conventions of this API.

## Description <a id="description"></a>

Module for node systems.

## Interfaces <a id="interfaces"></a>

|   |   |
|---|---|
| [`NodesGraphModelInterface`](../../maxon_generated/frameworks/nodes/interface/maxon.NodesGraphModelInterface.md#module-maxon.NodesGraphModelInterface)(*args) | A [`maxon.NodesGraphModelRef`](../../maxon_generated/frameworks/nodes/reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef) is an implementation of [`maxon.GraphModelInterface`](../../maxon_generated/frameworks/graph/interface/maxon.GraphModelInterface.md#module-maxon.GraphModelInterface) which wraps a `maxon.NodeSystem`. |
| [`NodeSystemManagerInterface`](../../maxon_generated/frameworks/nodes/interface/maxon.NodeSystemManagerInterface.md#module-maxon.NodeSystemManagerInterface)(*args) | A node system manager manages a `maxon.NodeSystem` and several views on that |
| [`GraphDescription`](../../maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.md#module-maxon.GraphDescription)() | Provides functions and constants to read and write node graphs from and into the graph description format. |

## References <a id="references"></a>

|   |   |
|---|---|
| [`NodesGraphModelRef`](../../maxon_generated/frameworks/nodes/reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)(*args) | Reference class for [`maxon.GraphModelInterface`](../../maxon_generated/frameworks/graph/interface/maxon.GraphModelInterface.md#module-maxon.GraphModelInterface). |

## Enums <a id="enums"></a>

|   |   |
|---|---|
| [`NodeSystemManagerInterface.FILTER`](../../maxon_generated/enums/maxon.NodeSystemManagerInterface.FILTER.md#module-maxon.NodeSystemManagerInterface.FILTER)() | Filter flags for views. |
| [`GraphDescription.PARSE_FLAGS`](../../maxon_generated/enums/maxon.GraphDescription.PARSE_FLAGS.md#module-maxon.GraphDescription.PARSE_FLAGS)() | Expresses options when parsing graph descriptions. |
| [`GraphDescription.QUERY_FLAGS`](../../maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.md#module-maxon.GraphDescription.QUERY_FLAGS)() | Expresses options when querying a graph for nodes. |
| [`NodeSpaceIdentifiers`](../../maxon_generated/enums/maxon.NodeSpaceIdentifiers.md#module-maxon.NodeSpaceIdentifiers)() | Holds the identifiers for all node spaces shipped with Cinema 4D. |
