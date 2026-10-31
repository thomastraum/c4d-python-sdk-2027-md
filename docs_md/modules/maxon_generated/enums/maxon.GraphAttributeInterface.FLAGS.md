<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.html -->

# maxon.GraphAttributeInterface.FLAGS <a id="maxon-graphattributeinterface-flags"></a>

## Description <a id="module-maxon.GraphAttributeInterface.FLAGS"></a><a id="description"></a>

FLAGS provide information about the nature of the attribute. Exactly one of DIRECT, DERIVED, USER_STATE or DERIVED|USER_STATE has to be set in the flags returned by `GraphAttributeInterface.GetFlags()`.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.GraphAttributeInterface.FLAGS.DERIVED`](maxon.GraphAttributeInterface.FLAGS.DERIVED.md#maxon.GraphAttributeInterface.FLAGS.DERIVED) | The attribute is a derived attribute which can’t be set by program code. |
| [`maxon.GraphAttributeInterface.FLAGS.DIRECT`](maxon.GraphAttributeInterface.FLAGS.DIRECT.md#maxon.GraphAttributeInterface.FLAGS.DIRECT) | The attribute is an attribute which can be set directly by program code. |
| [`maxon.GraphAttributeInterface.FLAGS.ERROR`](maxon.GraphAttributeInterface.FLAGS.ERROR.md#maxon.GraphAttributeInterface.FLAGS.ERROR) | The attribute represents an error message. |
| [`maxon.GraphAttributeInterface.FLAGS.IMMUTABLE`](maxon.GraphAttributeInterface.FLAGS.IMMUTABLE.md#maxon.GraphAttributeInterface.FLAGS.IMMUTABLE) | The attribute value can only be set once on creation of the node or port. |
| [`maxon.GraphAttributeInterface.FLAGS.MESSAGE_MASK`](maxon.GraphAttributeInterface.FLAGS.MESSAGE_MASK.md#maxon.GraphAttributeInterface.FLAGS.MESSAGE_MASK) | Mask to test for changes to direct attributes (whether meta or non-meta). |
| [`maxon.GraphAttributeInterface.FLAGS.META`](maxon.GraphAttributeInterface.FLAGS.META.md#maxon.GraphAttributeInterface.FLAGS.META) | The attribute is a meta attribute whose value is irrelevant for the data model and runtime behaviour of the graph. |
| [`maxon.GraphAttributeInterface.FLAGS.NONE`](maxon.GraphAttributeInterface.FLAGS.NONE.md#maxon.GraphAttributeInterface.FLAGS.NONE) | No flag set. |
| [`maxon.GraphAttributeInterface.FLAGS.ROOT`](maxon.GraphAttributeInterface.FLAGS.ROOT.md#maxon.GraphAttributeInterface.FLAGS.ROOT) | The attribute is a graph-global attribute which is stored at the root. |
| [`maxon.GraphAttributeInterface.FLAGS.TRANSIENT`](maxon.GraphAttributeInterface.FLAGS.TRANSIENT.md#maxon.GraphAttributeInterface.FLAGS.TRANSIENT) | The attribute is transient (non-persistent, i.e., not stored by serialization). |
| [`maxon.GraphAttributeInterface.FLAGS.TYPE_MASK`](maxon.GraphAttributeInterface.FLAGS.TYPE_MASK.md#maxon.GraphAttributeInterface.FLAGS.TYPE_MASK) | Use this mask to test for the type (one of DIRECT, DERIVED, USER_STATE or DERIVED\|USER_STATE). |
| [`maxon.GraphAttributeInterface.FLAGS.USER_STATE`](maxon.GraphAttributeInterface.FLAGS.USER_STATE.md#maxon.GraphAttributeInterface.FLAGS.USER_STATE) | The attribute is a user-state attribute which can be set by program code and doesn’t belong to the persistent state of the graph. |
| [`maxon.GraphAttributeInterface.FLAGS.WARNING`](maxon.GraphAttributeInterface.FLAGS.WARNING.md#maxon.GraphAttributeInterface.FLAGS.WARNING) | The attribute represents a warning message. |
