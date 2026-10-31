<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/enums/maxon.NODE_KIND.html -->

# maxon.NODE_KIND <a id="maxon-node-kind"></a>

## Description <a id="module-maxon.NODE_KIND"></a><a id="description"></a>

NODE_KIND allows to determine whether a general node (g-node for short) is a true node, a port or a port list.  
Because nodes, ports and port lists can be represented in a single hierarchy, classes such as GraphNode and GNode make use of this and need NODE_KIND to determine the actual kind of a g-node.  
NODE stands for true nodes. They may contain nested nodes and two port lists, one for the input ports and one for the output ports.

- INPUTS and OUTPUTS stand for port lists. They occur in the hierarchy as direct children of true nodes. Each true node may have at most one input list and one output list.
- INPORT and OUTPORT stand for ports. When a port is actually a port bundle, it may contain nested ports. A port is a child of either a port bundle or a port list.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.NODE_KIND.ALL_MASK`](maxon.NODE_KIND.ALL_MASK.md#maxon.NODE_KIND.ALL_MASK) | Mask which matches all node kinds. |
| [`maxon.NODE_KIND.INPORT`](maxon.NODE_KIND.INPORT.md#maxon.NODE_KIND.INPORT) | Indicates that the g-node is an input port. |
| [`maxon.NODE_KIND.INPUTS`](maxon.NODE_KIND.INPUTS.md#maxon.NODE_KIND.INPUTS) | Indicates that the g-node is an input port list. |
| [`maxon.NODE_KIND.IN_MASK`](maxon.NODE_KIND.IN_MASK.md#maxon.NODE_KIND.IN_MASK) | Mask to check a NODE_KIND if it stands for an input port or an input port list. |
| [`maxon.NODE_KIND.NODE`](maxon.NODE_KIND.NODE.md#maxon.NODE_KIND.NODE) | Indicates that the g-node is a true node. |
| [`maxon.NODE_KIND.NONE`](maxon.NODE_KIND.NONE.md#maxon.NODE_KIND.NONE) | Special value used e.g. |
| [`maxon.NODE_KIND.OUTPORT`](maxon.NODE_KIND.OUTPORT.md#maxon.NODE_KIND.OUTPORT) | Indicates that the g-node is an output port. |
| [`maxon.NODE_KIND.OUTPUTS`](maxon.NODE_KIND.OUTPUTS.md#maxon.NODE_KIND.OUTPUTS) | Indicates that the g-node is an output port list. |
| [`maxon.NODE_KIND.OUT_MASK`](maxon.NODE_KIND.OUT_MASK.md#maxon.NODE_KIND.OUT_MASK) |  |
| [`maxon.NODE_KIND.PORTLIST_MASK`](maxon.NODE_KIND.PORTLIST_MASK.md#maxon.NODE_KIND.PORTLIST_MASK) | Mask to check a NODE_KIND if it stands for a port list. |
| [`maxon.NODE_KIND.PORT_MASK`](maxon.NODE_KIND.PORT_MASK.md#maxon.NODE_KIND.PORT_MASK) | Mask to check a NODE_KIND if it stands for a port. |
