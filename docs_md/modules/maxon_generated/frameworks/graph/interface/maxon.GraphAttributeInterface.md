<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/graph/interface/maxon.GraphAttributeInterface.html -->

# maxon.GraphAttributeInterface <a id="maxon-graphattributeinterface"></a>

## Description <a id="module-maxon.GraphAttributeInterface"></a><a id="description"></a>

A graph attribute provides extra information about an attribute of nodes and ports.  
Attributes are identified and accessed only by an InternedId which carries no extra information about the attribute.  
If a GraphModelInterface wants to provide additional information for an attribute, its `GraphModelInterface.GetGraphAttribute()` returns a graph attribute to get that information (such as the attribute :[`maxon.GraphAttributeInterface.FLAGS`](../../../enums/maxon.GraphAttributeInterface.FLAGS.md#module-maxon.GraphAttributeInterface.FLAGS)).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.GraphAttribute`](../reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetFlags`](#maxon.GraphAttributeInterface.GetFlags)() | Returns the flags of this attribute. |
| [`GetId`](#maxon.GraphAttributeInterface.GetId)() | Returns the id of this attribute. |
| [`GetMessageFlags`](#maxon.GraphAttributeInterface.GetMessageFlags)(node) | Returns the message flags of the attribute value at *node*. |
| [`GetMessages`](#maxon.GraphAttributeInterface.GetMessages)(node, receiver) | Yields the messages of this attribute at *node* to *receiver*. |
| [`IsComputedFrom`](#maxon.GraphAttributeInterface.IsComputedFrom)(other) | Checks for a FLAGS.DERIVED “derived” attribute if its value is computed |

## Methods Definition <a id="methods-definition"></a>

### `GraphAttributeInterface.GetFlags()` <a id="maxon.GraphAttributeInterface.GetFlags"></a>

Returns the flags of this attribute.

> **Note:** If FLAGS.ERROR or FLAGS.WARNING is set, this means that the attribute can contain an error or warning, however a check for a concrete node using [`GraphAttributeInterface.GetMessageFlags()`](#maxon.GraphAttributeInterface.GetMessageFlags) has to be done to test if the value of the attribute at that node really contains an error or warning.

> **Note:** Usually you shouldn’t call this method directly, but use `GraphNode.GetGraphAttributeFlags()`.

**Return type:** [`maxon.GraphAttributeInterface.FLAGS`](../../../enums/maxon.GraphAttributeInterface.FLAGS.md#module-maxon.GraphAttributeInterface.FLAGS)

**Returns:** Flags of this attribute.

### `GraphAttributeInterface.GetId()` <a id="maxon.GraphAttributeInterface.GetId"></a>

Returns the id of this attribute.

**Return type:** [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)

**Returns:** Id of this attribute.

### `GraphAttributeInterface.GetMessageFlags(node)` <a id="maxon.GraphAttributeInterface.GetMessageFlags"></a>

Returns the message flags of the attribute value at *node*.  
An attribute which may contain an error or warning according to [`GraphAttributeInterface.GetFlags()`](#maxon.GraphAttributeInterface.GetFlags) doesn’t necessarily have to do so, you have to test for a concrete node if the value of the attribute at that node really contains an error or warning.

> **Note:** Usually you shouldn’t call this method directly, but use `GraphNode.GetGraphAttributeFlags()`.

**Parameters:** **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – A node or port where the message flags of this attribute shall be checked.

**Returns:** Message flags ([`maxon.GraphAttributeInterface.FLAGS.WARNING`](../../../enums/maxon.GraphAttributeInterface.FLAGS.WARNING.md#maxon.GraphAttributeInterface.FLAGS.WARNING), [`maxon.GraphAttributeInterface.FLAGS.ERROR`](../../../enums/maxon.GraphAttributeInterface.FLAGS.ERROR.md#maxon.GraphAttributeInterface.FLAGS.ERROR)) of this attribute at *node*.

**Return type:** [`maxon.GraphAttributeInterface.FLAGS`](../../../enums/maxon.GraphAttributeInterface.FLAGS.md#module-maxon.GraphAttributeInterface.FLAGS)

### `GraphAttributeInterface.GetMessages(node, receiver)` <a id="maxon.GraphAttributeInterface.GetMessages"></a>

Yields the messages of this attribute at *node* to *receiver*.

> **Note:** Usually you shouldn’t call this method directly, but use [`GraphNode.GetMessages()`](../datatype/maxon.GraphNode.md#maxon.GraphNode.GetMessages).

**Parameters:**

- **node** ([`maxon.GraphNode`](../datatype/maxon.GraphNode.md#module-maxon.GraphNode)) – A node or port at which the messages shall be obtained.
- **receiver** (Callable[[[`maxon.GraphMessage`](../reference/maxon.GraphMessage.md#module-maxon.GraphMessage)], bool]) – All messages are reported to this receiver.

**Returns:** **False** if the receiver cancelled further evaluation, **True** otherwise.

### `GraphAttributeInterface.IsComputedFrom(other)` <a id="maxon.GraphAttributeInterface.IsComputedFrom"></a>

Checks for a FLAGS.DERIVED “derived” attribute if its value is computed on-the-fly and needs the value of #other for that computation.  
A derived attribute may store its value in the graph, or it may compute it on-the-fly.  
In the latter case you can check the required attributes with this method.

> **Note:**
>
> This is important e.g. when you check for attribute modifications using `GraphNodeFunctions.GetAttributeModificationsSince()`  
> You only get notified about changes of stored attribute values.

**Parameters:** **other** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – Another attribute.

**Returns:** **True** if *other* is the same as #this, or if *this* is a computed attribute which needs #other to compute its value.
