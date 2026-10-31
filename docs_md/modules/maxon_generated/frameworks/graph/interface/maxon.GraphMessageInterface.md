<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/graph/interface/maxon.GraphMessageInterface.html -->

# maxon.GraphMessageInterface <a id="maxon-graphmessageinterface"></a>

## Description <a id="module-maxon.GraphMessageInterface"></a><a id="description"></a>

A graph message is an error or warning message to tell the user about issues found in the graph.  
A graph attribute which has one of [`maxon.GraphAttributeInterface.FLAGS.ERROR`](../../../enums/maxon.GraphAttributeInterface.FLAGS.ERROR.md#maxon.GraphAttributeInterface.FLAGS.ERROR), [`maxon.GraphAttributeInterface.FLAGS.WARNING`](../../../enums/maxon.GraphAttributeInterface.FLAGS.WARNING.md#maxon.GraphAttributeInterface.FLAGS.WARNING) set can produce such messages via the method `GraphAttributeInterface.GetMessages()`.  
To query for messages use `GraphNode.GetMessages()`.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.GraphMessage`](../reference/maxon.GraphMessage.md#module-maxon.GraphMessage)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Format`](#maxon.GraphMessageInterface.Format)() | Formats this message in a user-friendly way. |
| [`GetFlags`](#maxon.GraphMessageInterface.GetFlags)() | Returns the flags of this message, either [`maxon.GraphAttributeInterface.FLAGS.ERROR`](../../../enums/maxon.GraphAttributeInterface.FLAGS.ERROR.md#maxon.GraphAttributeInterface.FLAGS.ERROR) , [`maxon.GraphAttributeInterface.FLAGS.WARNING`](../../../enums/maxon.GraphAttributeInterface.FLAGS.WARNING.md#maxon.GraphAttributeInterface.FLAGS.WARNING) or both. |
| [`GetOrigin`](#maxon.GraphMessageInterface.GetOrigin)() | Returns the origin of the message. |

## Methods Definition <a id="methods-definition"></a>

### `GraphMessageInterface.Format()` <a id="maxon.GraphMessageInterface.Format"></a>

Formats this message in a user-friendly way.

**Returns:** A human-readable message.

**Return type:** str

### `GraphMessageInterface.GetFlags()` <a id="maxon.GraphMessageInterface.GetFlags"></a>

Returns the flags of this message, either [`maxon.GraphAttributeInterface.FLAGS.ERROR`](../../../enums/maxon.GraphAttributeInterface.FLAGS.ERROR.md#maxon.GraphAttributeInterface.FLAGS.ERROR) , [`maxon.GraphAttributeInterface.FLAGS.WARNING`](../../../enums/maxon.GraphAttributeInterface.FLAGS.WARNING.md#maxon.GraphAttributeInterface.FLAGS.WARNING) or both.

**Returns:** Message flags.

**Return type:** [`maxon.GraphAttributeInterface.FLAGS`](../../../enums/maxon.GraphAttributeInterface.FLAGS.md#module-maxon.GraphAttributeInterface.FLAGS)

### `GraphMessageInterface.GetOrigin()` <a id="maxon.GraphMessageInterface.GetOrigin"></a>

Returns the origin of the message.  
The graph model implementation may propagate a message along connections, for example to make a message for a nested node visible at the outside of a group. In such cases the origin tells where the message originates.

**Return type:** [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

**Returns:** The origin of the message.
