<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.html -->

# maxon.GraphDescription <a id="maxon-graphdescription"></a>

## Description <a id="module-maxon.GraphDescription"></a><a id="description"></a>

Provides functions and constants to read and write node graphs from and into the graph description format.

A graph description is JSON-like format to describe complete or partial node graphs for arbitrary node spaces. Graph descriptions can describe node types and their attributes over their labels in a natural language, absolute and lazy node paths, and queries to select entities in a graph by their values.

> **See also:**
>
> - [`maxon.GraphDescription.PARSE_FLAGS`](../../../enums/maxon.GraphDescription.PARSE_FLAGS.md#module-maxon.GraphDescription.PARSE_FLAGS)
> - [`maxon.GraphDescription.QUERY_FLAGS`](../../../enums/maxon.GraphDescription.QUERY_FLAGS.md#module-maxon.GraphDescription.QUERY_FLAGS)

## Inheritance diagram <a id="inheritance-diagram"></a>

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.GraphDescription.ClearSoloNodeCommand`](maxon.GraphDescription.ClearSoloNodeCommand.md#maxon.GraphDescription.ClearSoloNodeCommand) | Returns the key for a clear solo node command field in a description. |
| [`maxon.GraphDescription.ClearStartNodeCommand`](maxon.GraphDescription.ClearStartNodeCommand.md#maxon.GraphDescription.ClearStartNodeCommand) | Returns the key for a clear start node command field in a description. |
| [`maxon.GraphDescription.Commands`](maxon.GraphDescription.Commands.md#maxon.GraphDescription.Commands) | Returns the key for a command field in a description. |
| [`maxon.GraphDescription.Default`](maxon.GraphDescription.Default.md#maxon.GraphDescription.Default) | Returns the key for an input-group default value. |
| [`maxon.GraphDescription.DefaultCommand`](maxon.GraphDescription.DefaultCommand.md#maxon.GraphDescription.DefaultCommand) | Returns the key for a default node command field in a description. |
| [`maxon.GraphDescription.Description`](maxon.GraphDescription.Description.md#maxon.GraphDescription.Description) | Returns the key for a description field in a description. |
| [`maxon.GraphDescription.DisconnectCommand`](maxon.GraphDescription.DisconnectCommand.md#maxon.GraphDescription.DisconnectCommand) | Returns the key for an isolate node command field in a description. |
| [`maxon.GraphDescription.Enum`](maxon.GraphDescription.Enum.md#maxon.GraphDescription.Enum) | Returns the key for input-group enumerations. |
| [`maxon.GraphDescription.Flags`](maxon.GraphDescription.Flags.md#maxon.GraphDescription.Flags) | Returns the key for a flags field in a description. |
| [`maxon.GraphDescription.GroupChildren`](maxon.GraphDescription.GroupChildren.md#maxon.GraphDescription.GroupChildren) | Returns the key for group children. |
| [`maxon.GraphDescription.HidePortsCommand`](maxon.GraphDescription.HidePortsCommand.md#maxon.GraphDescription.HidePortsCommand) | Returns the key for a hide ports command field in a description. |
| [`maxon.GraphDescription.Id`](maxon.GraphDescription.Id.md#maxon.GraphDescription.Id) | Returns the key for a node ID field in a description. |
| [`maxon.GraphDescription.InputGroup`](maxon.GraphDescription.InputGroup.md#maxon.GraphDescription.InputGroup) | Returns the key for an input-group scope. |
| [`maxon.GraphDescription.Language`](maxon.GraphDescription.Language.md#maxon.GraphDescription.Language) | Returns the key for a language ID field in a description. |
| [`maxon.GraphDescription.Max`](maxon.GraphDescription.Max.md#maxon.GraphDescription.Max) | Returns the key for an input-group maximum value. |
| [`maxon.GraphDescription.Min`](maxon.GraphDescription.Min.md#maxon.GraphDescription.Min) | Returns the key for an input-group minimum value. |
| [`maxon.GraphDescription.Ports`](maxon.GraphDescription.Ports.md#maxon.GraphDescription.Ports) | Returns the key for input-group ports. |
| [`maxon.GraphDescription.Query`](maxon.GraphDescription.Query.md#maxon.GraphDescription.Query) | Returns the key for a query field in a description. |
| [`maxon.GraphDescription.QueryComposition`](maxon.GraphDescription.QueryComposition.md#maxon.GraphDescription.QueryComposition) | Returns the key for a query composition field. |
| [`maxon.GraphDescription.QueryFlags`](maxon.GraphDescription.QueryFlags.md#maxon.GraphDescription.QueryFlags) | Returns the key for query flags. |
| [`maxon.GraphDescription.QueryMaxError`](maxon.GraphDescription.QueryMaxError.md#maxon.GraphDescription.QueryMaxError) | Returns the key for a query tolerance field. |
| [`maxon.GraphDescription.QueryMode`](maxon.GraphDescription.QueryMode.md#maxon.GraphDescription.QueryMode) | Returns the key for a query mode field in a description. |
| [`maxon.GraphDescription.QueryOpAnd`](maxon.GraphDescription.QueryOpAnd.md#maxon.GraphDescription.QueryOpAnd) | Returns the key for the and operator in a query. |
| [`maxon.GraphDescription.QueryOpEqual`](maxon.GraphDescription.QueryOpEqual.md#maxon.GraphDescription.QueryOpEqual) | Returns the key for the equal operator in a query. |
| [`maxon.GraphDescription.QueryOpGreater`](maxon.GraphDescription.QueryOpGreater.md#maxon.GraphDescription.QueryOpGreater) | Returns the key for the greater operator in a query. |
| [`maxon.GraphDescription.QueryOpGreaterEqual`](maxon.GraphDescription.QueryOpGreaterEqual.md#maxon.GraphDescription.QueryOpGreaterEqual) | Returns the key for the greater or equal operator in a query. |
| [`maxon.GraphDescription.QueryOpLess`](maxon.GraphDescription.QueryOpLess.md#maxon.GraphDescription.QueryOpLess) | Returns the key for the less operator in a query. |
| [`maxon.GraphDescription.QueryOpLessEqual`](maxon.GraphDescription.QueryOpLessEqual.md#maxon.GraphDescription.QueryOpLessEqual) | Returns the key for the less or equal operator in a query. |
| [`maxon.GraphDescription.QueryOpNotEqual`](maxon.GraphDescription.QueryOpNotEqual.md#maxon.GraphDescription.QueryOpNotEqual) | Returns the key for the not equal operator in a query. |
| [`maxon.GraphDescription.QueryOpOr`](maxon.GraphDescription.QueryOpOr.md#maxon.GraphDescription.QueryOpOr) | Returns the key for the or operator in a query. |
| [`maxon.GraphDescription.QueryOpRegexMatch`](maxon.GraphDescription.QueryOpRegexMatch.md#maxon.GraphDescription.QueryOpRegexMatch) | Returns the key for the regular expression match operator in a query. |
| [`maxon.GraphDescription.QueryOpRegexSearch`](maxon.GraphDescription.QueryOpRegexSearch.md#maxon.GraphDescription.QueryOpRegexSearch) | Returns the key for the regular expression search operator in a query. |
| [`maxon.GraphDescription.QueryOperator`](maxon.GraphDescription.QueryOperator.md#maxon.GraphDescription.QueryOperator) | Returns the key for a comparison operator field. |
| [`maxon.GraphDescription.QuerySelectPorts`](maxon.GraphDescription.QuerySelectPorts.md#maxon.GraphDescription.QuerySelectPorts) | Returns the key for a query select ports field. |
| [`maxon.GraphDescription.QueryValue`](maxon.GraphDescription.QueryValue.md#maxon.GraphDescription.QueryValue) | Returns the key for a comparison value field. |
| [`maxon.GraphDescription.RecursiveUngroupCommand`](maxon.GraphDescription.RecursiveUngroupCommand.md#maxon.GraphDescription.RecursiveUngroupCommand) | Returns the key for a recursive ungroup command field in a description. |
| [`maxon.GraphDescription.RemoveCommand`](maxon.GraphDescription.RemoveCommand.md#maxon.GraphDescription.RemoveCommand) | Returns the key for a remove node command field in a description. |
| [`maxon.GraphDescription.SetPortCountCommand`](maxon.GraphDescription.SetPortCountCommand.md#maxon.GraphDescription.SetPortCountCommand) | Returns the key for a change ports count command field in a description. |
| [`maxon.GraphDescription.ShowPortsCommand`](maxon.GraphDescription.ShowPortsCommand.md#maxon.GraphDescription.ShowPortsCommand) | Returns the key for a show ports command field in a description. |
| [`maxon.GraphDescription.SoloNodeCommand`](maxon.GraphDescription.SoloNodeCommand.md#maxon.GraphDescription.SoloNodeCommand) | Returns the key for a solo node command field in a description. |
| [`maxon.GraphDescription.Space`](maxon.GraphDescription.Space.md#maxon.GraphDescription.Space) | Returns the key for a node space ID field in a description. |
| [`maxon.GraphDescription.StartNodeCommand`](maxon.GraphDescription.StartNodeCommand.md#maxon.GraphDescription.StartNodeCommand) | Returns the key for a start node command field in a description. |
| [`maxon.GraphDescription.Step`](maxon.GraphDescription.Step.md#maxon.GraphDescription.Step) | Returns the key for an input-group step value. |
| [`maxon.GraphDescription.Type`](maxon.GraphDescription.Type.md#maxon.GraphDescription.Type) | Returns the key for a node type field in a description. |
| [`maxon.GraphDescription.TypeBool`](maxon.GraphDescription.TypeBool.md#maxon.GraphDescription.TypeBool) | Returns the input-group type string for boolean values. |
| [`maxon.GraphDescription.TypeColor`](maxon.GraphDescription.TypeColor.md#maxon.GraphDescription.TypeColor) | Returns the input-group type string for color values. |
| [`maxon.GraphDescription.TypeColorA`](maxon.GraphDescription.TypeColorA.md#maxon.GraphDescription.TypeColorA) | Returns the input-group type string for alpha color values. |
| [`maxon.GraphDescription.TypeFloat`](maxon.GraphDescription.TypeFloat.md#maxon.GraphDescription.TypeFloat) | Returns the input-group type string for float values. |
| [`maxon.GraphDescription.TypeId`](maxon.GraphDescription.TypeId.md#maxon.GraphDescription.TypeId) | Returns the input-group type string for ID values. |
| [`maxon.GraphDescription.TypeInt`](maxon.GraphDescription.TypeInt.md#maxon.GraphDescription.TypeInt) | Returns the input-group type string for integer values. |
| [`maxon.GraphDescription.TypeInternedId`](maxon.GraphDescription.TypeInternedId.md#maxon.GraphDescription.TypeInternedId) | Returns the input-group type string for interned ID values. |
| [`maxon.GraphDescription.TypeString`](maxon.GraphDescription.TypeString.md#maxon.GraphDescription.TypeString) | Returns the input-group type string for string values. |
| [`maxon.GraphDescription.TypeUrl`](maxon.GraphDescription.TypeUrl.md#maxon.GraphDescription.TypeUrl) | Returns the input-group type string for URL values. |
| [`maxon.GraphDescription.TypeVector`](maxon.GraphDescription.TypeVector.md#maxon.GraphDescription.TypeVector) | Returns the input-group type string for vector values. |
| [`maxon.GraphDescription.UngroupCommand`](maxon.GraphDescription.UngroupCommand.md#maxon.GraphDescription.UngroupCommand) | Returns the key for an ungroup command field in a description. |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`ApplyDescription`](#maxon.GraphDescription.ApplyDescription)(graph, description[, …]) | Applies the given graph *description* to the given nodes *graph*. |
| [`CreateGraph`](#maxon.GraphDescription.CreateGraph)([element, nodeSpaceId, …]) | Returns the nodes graph for the given scene #element and #nodeSpaceId. |
| [`EvaluateQuery`](#maxon.GraphDescription.EvaluateQuery)(graph, query[, nodeSpace, …]) | Evaluates a graph query and returns its matched nodes. |
| [`GetGraph`](#maxon.GraphDescription.GetGraph)([element, nodeSpaceId, …]) | Returns the nodes graph for the given scene *element* and *nodeSpaceId*. |
| [`GetMaterialGraphs`](#maxon.GraphDescription.GetMaterialGraphs)(nodeSpaceId) | Returns all material graphs in the given scene #doc which are in the given #nodeSpaceId. |

## Methods Definition <a id="methods-definition"></a>

### *static* `GraphDescription.ApplyDescription(graph: maxon.frameworks.nodes.NodesGraphModelRef, description: dict, nodeSpace: str = '', language: str = '', callback: callable = None, validateAbsolutePaths: bool = True) → dict` <a id="maxon.GraphDescription.ApplyDescription"></a>

Applies the given graph *description* to the given nodes *graph*.

**Parameters:**

- **graph** ([`maxon.NodesGraphModelRef`](../reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)) – The nodes graph to apply the *description* to.
- **description** (Union[*dict*, *list[dict]*]) – The description to apply to *graph*.
- **nodeSpace** (Union[*str*, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – The node space the given *description* is intended for. When the empty string or Id are passed, the space will be deduced from the passed *graph*. Apart from raising errors a bit earlier, this argument has only the function to make for more declarative code which clearly states for which node space a description is intended. Defaults to the empty string.
- **nodeSpace** – The natural language the given *description* is referencing. When the empty string or Id are passed, the currently active language of Cinema 4D is used to parse the *description*. Only relevant when using label references. Defaults to the empty string.
- **callback** (Union[*callable*, *None*]) – Will be called for each scope in the given *description* before it is parsed into the given *graph*. Defaults to *None*.
- **validateAbsolutePaths** – When *True*, absolute node paths in the given *description* will still be validated with the underlying graph description cache. When *False*, absolute node paths will invoked without checking the cache. This has the advantage that one can address ports and attributes that are not cacheable. The disadvantage is that one will get less precise error messages when a cacheable path is wrong. Should only be set to False for descriptions which raise the error ‘WARNING: Failed to cache child attributes for type ‘@’ in port bundle ‘@’. Referencing its children is only possible via absolute node paths.’. And then only when one actually wants to reference one of these children. This currently happens for example in the standard renderer node space for some color ports which decompose themselves into (r, g, b) child ports. Setting the color as a whole will work, but setting one of the child ports will not unless one uses an absolute node path and sets this flag to False, so that the path is being used without being validated. Defaults to *True*.

**Returns:** All nodes in the given graph as (ID, node) key-value pairs.

**Return type:** *dict*

### *static* `GraphDescription.CreateGraph(element: c4d.BaseList2D = None, nodeSpaceId: str = '', createEmpty: bool = True, name: str = '') → maxon.frameworks.nodes.NodesGraphModelRef` <a id="maxon.GraphDescription.CreateGraph"></a>

Returns the nodes graph for the given scene #element and #nodeSpaceId.

*Deprecated since version 2025.0:* Use [`GetGraph()`](#maxon.GraphDescription.GetGraph) instead.

### *static* `GraphDescription.EvaluateQuery(graph: maxon.frameworks.nodes.NodesGraphModelRef, query: dict, nodeSpace: str = '', language: str = '', validateAbsolutePaths: bool = True) → BaseArray[GraphNode]` <a id="maxon.GraphDescription.EvaluateQuery"></a>

Evaluates a graph query and returns its matched nodes.

A graph query allows you to search for nodes within a graph via a node attribute or port values, and the connections between nodes. Queries can also be embedded within [`ApplyDescription()`](#maxon.GraphDescription.ApplyDescription) calls, but then cannot return query results that represent ports.

**Parameters:**

- **graph** ([`maxon.NodesGraphModelRef`](../reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)) – The nodes graph to evaluate the query against.
- **query** (*dict*) – The query to evaluate.
- **nodeSpace** (*str*) – The node space in which to evaluate the query.
- **language** (*str*) – The language to use for the query.
- **validateAbsolutePaths** (*bool*) – Whether to validate absolute paths in the query.

**Returns:** The nodes that match the query. Other than for embedded queries, this can also contain nodes that represent ports.

**Return type:**

`BaseArray[GraphNode]`

### *static* `GraphDescription.GetGraph(element: c4d.BaseList2D = None, nodeSpaceId: str = '', createEmpty: bool = True, name: str = '') → maxon.frameworks.nodes.NodesGraphModelRef` <a id="maxon.GraphDescription.GetGraph"></a>

Returns the nodes graph for the given scene *element* and *nodeSpaceId*.

The element can be a *c4d.documents.BaseDocument* (for the document wide scene nodes graph), a *c4d.BaseObject* (for capsules), or a material (for material graphs), or *None* (to create a material in the active document). When the passed element does not yet have a graph in the requested node space, it will be created.

**Parameters:**

- **element** (Union[[`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument), [`c4d.BaseObject`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject), [`c4d.BaseMaterial`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial), *None*]) – The scene element to get the graph for. Can be *None* to create a material in the active document. Defaults to *None*.
- **nodeSpaceId** (Union[*str*, [`maxon.String`](../../../references/core/maxon.String.md#module-maxon.String), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – The node space to retrieve the graph for. When the empty ID is passed, it will default to the active node space for materials and the neutron node space for everything else. Defaults to the empty string.
- **createEmpty** (*bool*) – When *True*, new graphs will be created as an empty graph, when *False* the default graph will be created. Defaults to *True*.
- **name** (*str*) – The name to give the material which is created when #element is the *None*. Will be ignored when the empty string. Defaults to the empty string.

**Returns:** The retrieved graph.

**Return type:** [`maxon.NodesGraphModelRef`](../reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)

### `GraphDescription.GetMaterialGraphs(nodeSpaceId: str) → BaseArray[NodesGraphModelRef]` <a id="maxon.GraphDescription.GetMaterialGraphs"></a>

Returns all material graphs in the given scene #doc which are in the given #nodeSpaceId.

**Parameters:**

- **doc** ([`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to get the material graphs from.
- **nodeSpaceId** (*str*) – The node space to retrieve the graphs for. Cannot be the empty ID.

**Returns:** All material graphs in the given scene #doc which are of the given #nodeSpaceId.

**Return type:** [`maxon.BaseArray`](../../../datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) [[`maxon.NodesGraphModelRef`](../reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)]
