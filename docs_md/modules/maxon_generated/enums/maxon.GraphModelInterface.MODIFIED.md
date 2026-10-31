<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.html -->

# maxon.GraphModelInterface.MODIFIED <a id="maxon-graphmodelinterface-modified"></a>

## Description <a id="module-maxon.GraphModelInterface.MODIFIED"></a><a id="description"></a>

These flags are reported by `GraphModelInterface.GetModificationsSince()` to tell which properties of the node have changed.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.GraphModelInterface.MODIFIED.ALL_MASK`](maxon.GraphModelInterface.MODIFIED.ALL_MASK.md#maxon.GraphModelInterface.MODIFIED.ALL_MASK) |  |
| [`maxon.GraphModelInterface.MODIFIED.ATTRIBUTE_MASK`](maxon.GraphModelInterface.MODIFIED.ATTRIBUTE_MASK.md#maxon.GraphModelInterface.MODIFIED.ATTRIBUTE_MASK) | Mask to test for attribute changes. |
| [`maxon.GraphModelInterface.MODIFIED.CHILD_REMOVED`](maxon.GraphModelInterface.MODIFIED.CHILD_REMOVED.md#maxon.GraphModelInterface.MODIFIED.CHILD_REMOVED) | Children of the node have been removed. |
| [`maxon.GraphModelInterface.MODIFIED.COMPLETE`](maxon.GraphModelInterface.MODIFIED.COMPLETE.md#maxon.GraphModelInterface.MODIFIED.COMPLETE) | The graph has changed completely. |
| [`maxon.GraphModelInterface.MODIFIED.CONNECTION_MASK`](maxon.GraphModelInterface.MODIFIED.CONNECTION_MASK.md#maxon.GraphModelInterface.MODIFIED.CONNECTION_MASK) | Mask to test for connection changes of ports. |
| [`maxon.GraphModelInterface.MODIFIED.DATA_ATTRIBUTE_MASK`](maxon.GraphModelInterface.MODIFIED.DATA_ATTRIBUTE_MASK.md#maxon.GraphModelInterface.MODIFIED.DATA_ATTRIBUTE_MASK) | Mask to test for changes to attributes belonging to the data model of the graph (non-meta, non-user-state attributes). |
| [`maxon.GraphModelInterface.MODIFIED.DERIVED_ATTRIBUTE_MASK`](maxon.GraphModelInterface.MODIFIED.DERIVED_ATTRIBUTE_MASK.md#maxon.GraphModelInterface.MODIFIED.DERIVED_ATTRIBUTE_MASK) | Derived attributes of the node have changed. |
| [`maxon.GraphModelInterface.MODIFIED.DIRECT_ATTRIBUTE`](maxon.GraphModelInterface.MODIFIED.DIRECT_ATTRIBUTE.md#maxon.GraphModelInterface.MODIFIED.DIRECT_ATTRIBUTE) | Direct non-meta attributes of the node have changed. |
| [`maxon.GraphModelInterface.MODIFIED.DIRECT_ATTRIBUTE_MASK`](maxon.GraphModelInterface.MODIFIED.DIRECT_ATTRIBUTE_MASK.md#maxon.GraphModelInterface.MODIFIED.DIRECT_ATTRIBUTE_MASK) | Mask to test for changes to direct attributes (whether meta or non-meta). |
| [`maxon.GraphModelInterface.MODIFIED.DIRECT_META_ATTRIBUTE`](maxon.GraphModelInterface.MODIFIED.DIRECT_META_ATTRIBUTE.md#maxon.GraphModelInterface.MODIFIED.DIRECT_META_ATTRIBUTE) | Direct meta attributes of the node have changed (see [`maxon.GraphAttributeInterface.FLAGS.META`](maxon.GraphAttributeInterface.FLAGS.META.md#maxon.GraphAttributeInterface.FLAGS.META)). |
| [`maxon.GraphModelInterface.MODIFIED.INHERITED_ATTRIBUTE`](maxon.GraphModelInterface.MODIFIED.INHERITED_ATTRIBUTE.md#maxon.GraphModelInterface.MODIFIED.INHERITED_ATTRIBUTE) | Inherited attributes (derived from left to right) of the node have changed. |
| [`maxon.GraphModelInterface.MODIFIED.INPUT_CONNECTION`](maxon.GraphModelInterface.MODIFIED.INPUT_CONNECTION.md#maxon.GraphModelInterface.MODIFIED.INPUT_CONNECTION) | Input connections of the port have changed. |
| [`maxon.GraphModelInterface.MODIFIED.NODE_ADDED`](maxon.GraphModelInterface.MODIFIED.NODE_ADDED.md#maxon.GraphModelInterface.MODIFIED.NODE_ADDED) | The node has been added. |
| [`maxon.GraphModelInterface.MODIFIED.NODE_MASK`](maxon.GraphModelInterface.MODIFIED.NODE_MASK.md#maxon.GraphModelInterface.MODIFIED.NODE_MASK) | Mask to test for added or removed nodes. |
| [`maxon.GraphModelInterface.MODIFIED.NONE`](maxon.GraphModelInterface.MODIFIED.NONE.md#maxon.GraphModelInterface.MODIFIED.NONE) | No flag. |
| [`maxon.GraphModelInterface.MODIFIED.OUTPUT_CONNECTION`](maxon.GraphModelInterface.MODIFIED.OUTPUT_CONNECTION.md#maxon.GraphModelInterface.MODIFIED.OUTPUT_CONNECTION) | Output connections of the port have changed. |
| [`maxon.GraphModelInterface.MODIFIED.SPECIAL0`](maxon.GraphModelInterface.MODIFIED.SPECIAL0.md#maxon.GraphModelInterface.MODIFIED.SPECIAL0) | This is set to indicate a special change, the exact meaning is graph-specific. |
| [`maxon.GraphModelInterface.MODIFIED.SPECIAL1`](maxon.GraphModelInterface.MODIFIED.SPECIAL1.md#maxon.GraphModelInterface.MODIFIED.SPECIAL1) | This is set to indicate a special change, the exact meaning is graph-specific. |
| [`maxon.GraphModelInterface.MODIFIED.SPECIAL_NAME`](maxon.GraphModelInterface.MODIFIED.SPECIAL_NAME.md#maxon.GraphModelInterface.MODIFIED.SPECIAL_NAME) |  |
| [`maxon.GraphModelInterface.MODIFIED.STRUCTURE_MASK`](maxon.GraphModelInterface.MODIFIED.STRUCTURE_MASK.md#maxon.GraphModelInterface.MODIFIED.STRUCTURE_MASK) | Mask to test for any structural change (changed connections, added or removed nodes). |
| [`maxon.GraphModelInterface.MODIFIED.SYNTHESIZED_ATTRIBUTE`](maxon.GraphModelInterface.MODIFIED.SYNTHESIZED_ATTRIBUTE.md#maxon.GraphModelInterface.MODIFIED.SYNTHESIZED_ATTRIBUTE) | Synthesized attributes (derived from right to left) of the node have changed. |
| [`maxon.GraphModelInterface.MODIFIED.USER_STATE_ATTRIBUTE`](maxon.GraphModelInterface.MODIFIED.USER_STATE_ATTRIBUTE.md#maxon.GraphModelInterface.MODIFIED.USER_STATE_ATTRIBUTE) | User state attributes of the node have changed (see [`maxon.GraphAttributeInterface.FLAGS.USER_STATE`](maxon.GraphAttributeInterface.FLAGS.USER_STATE.md#maxon.GraphAttributeInterface.FLAGS.USER_STATE)). |
