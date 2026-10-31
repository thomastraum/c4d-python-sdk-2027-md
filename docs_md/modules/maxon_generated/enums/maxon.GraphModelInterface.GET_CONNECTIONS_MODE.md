<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/enums/maxon.GraphModelInterface.GET_CONNECTIONS_MODE.html -->

# maxon.GraphModelInterface.GET_CONNECTIONS_MODE <a id="maxon-graphmodelinterface-get-connections-mode"></a>

## Description <a id="module-maxon.GraphModelInterface.GET_CONNECTIONS_MODE"></a><a id="description"></a>

Used with `GraphNode.GetConnections()` to control which connections shall be reported.  
Either CONNECTIONS or SHORTCUTS has to be set.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.GraphModelInterface.GET_CONNECTIONS_MODE.CONNECTIONS`](maxon.GraphModelInterface.GET_CONNECTIONS_MODE.CONNECTIONS.md#maxon.GraphModelInterface.GET_CONNECTIONS_MODE.CONNECTIONS) | Default Behavior for a class. |
| [`maxon.GraphModelInterface.GET_CONNECTIONS_MODE.DERIVATION_FILTER`](maxon.GraphModelInterface.GET_CONNECTIONS_MODE.DERIVATION_FILTER.md#maxon.GraphModelInterface.GET_CONNECTIONS_MODE.DERIVATION_FILTER) | Apply the derivation filter. |
| [`maxon.GraphModelInterface.GET_CONNECTIONS_MODE.EXTERNAL_CONNECTIONS`](maxon.GraphModelInterface.GET_CONNECTIONS_MODE.EXTERNAL_CONNECTIONS.md#maxon.GraphModelInterface.GET_CONNECTIONS_MODE.EXTERNAL_CONNECTIONS) | Only report connections which leave the node to which the port belongs (so they are external to the node). |
| [`maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INCLUDE_HIDDEN`](maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INCLUDE_HIDDEN.md#maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INCLUDE_HIDDEN) | Report connections where the hidden flag is set or which go to hidden ports. |
| [`maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INDUCED_DEPENDENCIES`](maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INDUCED_DEPENDENCIES.md#maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INDUCED_DEPENDENCIES) | Report induced dependencies (due to loop dependencies or sequencing). |
| [`maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INTERNAL_CONNECTIONS`](maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INTERNAL_CONNECTIONS.md#maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INTERNAL_CONNECTIONS) | Only report connections which don’t leave the node to which the port belongs (so they are internal to the node). |
| [`maxon.GraphModelInterface.GET_CONNECTIONS_MODE.NONE`](maxon.GraphModelInterface.GET_CONNECTIONS_MODE.NONE.md#maxon.GraphModelInterface.GET_CONNECTIONS_MODE.NONE) | Default Behavior for a class. |
| [`maxon.GraphModelInterface.GET_CONNECTIONS_MODE.SKIP_REROUTER`](maxon.GraphModelInterface.GET_CONNECTIONS_MODE.SKIP_REROUTER.md#maxon.GraphModelInterface.GET_CONNECTIONS_MODE.SKIP_REROUTER) | Hop over rerouter nodes. |
| [`maxon.GraphModelInterface.GET_CONNECTIONS_MODE.WITHOUT_INHIBITED`](maxon.GraphModelInterface.GET_CONNECTIONS_MODE.WITHOUT_INHIBITED.md#maxon.GraphModelInterface.GET_CONNECTIONS_MODE.WITHOUT_INHIBITED) | Don’t report inhibited connections (those where Wires::inhibit is present). |
