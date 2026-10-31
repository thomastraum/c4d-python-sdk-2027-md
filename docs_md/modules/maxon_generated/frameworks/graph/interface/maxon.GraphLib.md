<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/graph/interface/maxon.GraphLib.html -->

# maxon.GraphLib <a id="maxon-graphlib"></a>

## Description <a id="module-maxon.GraphLib"></a><a id="description"></a>

GraphLib contains some static functions for graphs.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`CreateAttribute`](#maxon.GraphLib.CreateAttribute)(*args) | Creates a [`maxon.GraphAttribute`](../reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute) with the given name and flags. |
| [`CreateMessage`](#maxon.GraphLib.CreateMessage)(*args) | Creates a GraphMessage. |
| [`CreateSimpleGraphModel`](#maxon.GraphLib.CreateSimpleGraphModel)(*args) | Creates a new instance of a simple implementation of [`maxon.GraphModelInterface`](maxon.GraphModelInterface.md#module-maxon.GraphModelInterface). |
| [`WriteGml`](#maxon.GraphLib.WriteGml)(*args) | Writes a graph to a GML file (Graph Modeling Language). |

## Methods Definition <a id="methods-definition"></a>

### *static* `GraphLib.CreateAttribute(*args)` <a id="maxon.GraphLib.CreateAttribute"></a>

Creates a [`maxon.GraphAttribute`](../reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute) with the given name and flags.

**Parameters:**

- **attr** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The name of the attribute.
- **flags** ([`maxon.GraphAttributeInterface.FLAGS`](../../../enums/maxon.GraphAttributeInterface.FLAGS.md#module-maxon.GraphAttributeInterface.FLAGS)) – The flags of the attribute.

**Returns:** A new [`maxon.GraphAttribute`](../reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute) with the given name and flags.

**Return type:** [`maxon.GraphAttribute`](../reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute)

### *static* `GraphLib.CreateMessage(*args)` <a id="maxon.GraphLib.CreateMessage"></a>

Creates a GraphMessage.

**Parameters:**

- **flags** ([`maxon.GraphAttributeInterface.FLAGS`](../../../enums/maxon.GraphAttributeInterface.FLAGS.md#module-maxon.GraphAttributeInterface.FLAGS)) – The flags of the message.
- **origin** ([`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)) – The origin of the message.
- **value** ([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The ToString function of *value* will be called to implement GraphMessageInterface.Format.

**Returns:** A new [`maxon.GraphMessage`](../reference/maxon.GraphMessage.md#module-maxon.GraphMessage) for the given parameters.

**Return type:** [`maxon.GraphMessage`](../reference/maxon.GraphMessage.md#module-maxon.GraphMessage)

### *static* `GraphLib.CreateSimpleGraphModel(*args)` <a id="maxon.GraphLib.CreateSimpleGraphModel"></a>

Creates a new instance of a simple implementation of [`maxon.GraphModelInterface`](maxon.GraphModelInterface.md#module-maxon.GraphModelInterface).  
The simple graph model only manages plain nodes, ports and connections, but it doesn’t support advanced features like inheritance from base graphs, derived attributes, implicit connections, rollback of transactions or change lists.

**Returns:** A new [`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef) which uses a simple implementation of [`maxon.GraphModelInterface`](maxon.GraphModelInterface.md#module-maxon.GraphModelInterface).

**Return type:** [`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)

### *static* `GraphLib.WriteGml(*args)` <a id="maxon.GraphLib.WriteGml"></a>

Writes a graph to a GML file (Graph Modeling Language).

**Parameters:**

- **graph** ([`maxon.GraphModelRef`](../reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)) – The graph to write.
- **output** (Union[[`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url), [`maxon.OutputStreamInterface`](../../../interfaces/io/maxon.OutputStreamInterface.md#module-maxon.OutputStreamInterface)]) – The output stream to write to.

**Returns:**
