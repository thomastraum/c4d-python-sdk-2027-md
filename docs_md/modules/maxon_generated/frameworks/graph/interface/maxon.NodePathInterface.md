<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/graph/interface/maxon.NodePathInterface.html -->

# maxon.NodePathInterface <a id="maxon-nodepathinterface"></a>

## Description <a id="module-maxon.NodePathInterface"></a><a id="description"></a>

A [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath) identifies a graph node (a true node, port or port list) within a node graph.  
It consists of a list of identifiers (one for each hierarchy level) just like the path of a file in a file system. In the textual notation of a path we use */* as separator character (except around *<* or *>*, see below).

The root node has an empty path, and port lists use the special identifiers *<* (input port list) and *>* (output port list).  
For example in the graph there are the following paths:

- The empty path identifies the root node.
- *<* is the path of the input port list of the root node (containing the object port), *>* of the output port list (containing the center port).
- *\<object*, *\<object/geometry*, *\<object/bounds* are the paths of the input ports of the root node.
- *>center* is the path of the output port of the root node.
- *x* is the path of the child node x.
- x has the input port *x\<bounds* and the output port *x>c*.
- x has the inner node *x/n* with ports *x/n\<in* and *x/n>out*.

A path cannot contain more than one of the port list identifiers *<* or *>*.  
All methods which initialize or modify a path return an error if the result was such an invalid path.

To make the string representation shorter and more readable, the separator character */* is only used between regular identifiers, but not around the port list identifiers *<* or *>*.  
Therefore we write e.g. *x/n>out* instead of *x/n/>/out*.

## Inheritance diagram <a id="inheritance-diagram"></a>

Child Class:

- [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.NodePathInterface.INPUTS`](maxon.NodePathInterface.INPUTS.md#maxon.NodePathInterface.INPUTS) |  |
| [`maxon.NodePathInterface.OUTPUTS`](maxon.NodePathInterface.OUTPUTS.md#maxon.NodePathInterface.OUTPUTS) |  |
| [`maxon.NodePathInterface.TEMPLATE`](maxon.NodePathInterface.TEMPLATE.md#maxon.NodePathInterface.TEMPLATE) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Compare`](#maxon.NodePathInterface.Compare)(other) | Compares this and *other*. |
| [`DescribeIO`](#maxon.NodePathInterface.DescribeIO)(*args) |  |
| [`FromCString`](#maxon.NodePathInterface.FromCString)(path) | Parses a node path given as a character block into a NodePath object. |
| [`GetCount`](#maxon.NodePathInterface.GetCount)() | Returns the length of this path. |
| [`GetHashCode`](#maxon.NodePathInterface.GetHashCode)() | Returns the hash code of [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath). |
| [`GetKind`](#maxon.NodePathInterface.GetKind)() | Returns the node kind of the graph node which is identified by this path: - A path without path list identifiers *<* or *>* is a true node ([`maxon.NODE_KIND.NODE`](../../../enums/maxon.NODE_KIND.NODE.md#maxon.NODE_KIND.NODE)), for example *node/child*. |
| [`GetLastId`](#maxon.NodePathInterface.GetLastId)() | Returns the last element of this path. |
| [`GetNode`](#maxon.NodePathInterface.GetNode)() | Returns only the path of the node without ports. |
| [`GetNodeDepth`](#maxon.NodePathInterface.GetNodeDepth)() | Returns the hierarchy depth of the true node which is identified by this path. |
| [`GetParent`](#maxon.NodePathInterface.GetParent)() | Returns the path of the parent of this path. |
| [`GetPart`](#maxon.NodePathInterface.GetPart)(src, count) | Returns a part of this node path as a new NodePath. |
| [`GetPortPart`](#maxon.NodePathInterface.GetPortPart)() | Returns the port part of this path as a new NodePath. |
| [`GetPortPath`](#maxon.NodePathInterface.GetPortPath)() | Returns only the relative port path without the node path. |
| [`GetTopLevelPort`](#maxon.NodePathInterface.GetTopLevelPort)() | Returns the path to the @ref Port “top-level port” of this path. |
| [`IsEmpty`](#maxon.NodePathInterface.IsEmpty)() | Checks if this path is an empty path. |
| [`IsInputsOrOutputs`](#maxon.NodePathInterface.IsInputsOrOutputs)(i) | Checks if the identifier i stands for the input or output port list of a node, so if it is either ‘<’ or ‘>’. |
| [`IsPopulated`](#maxon.NodePathInterface.IsPopulated)() | Checks if this path contains anything. |
| [`IsPortOfRoot`](#maxon.NodePathInterface.IsPortOfRoot)() | Checks if this path identifies a port of the root node of a node system. |
| [`IsTopLevelPort`](#maxon.NodePathInterface.IsTopLevelPort)() | Checks if this path identifies a “top-level port”. |
| [`LessThan`](#maxon.NodePathInterface.LessThan)(other) |  |
| [`LessThanOrEqual`](#maxon.NodePathInterface.LessThanOrEqual)(other) |  |
| [`Prepend`](#maxon.NodePathInterface.Prepend)(prefix) | Prepends a node prefix at the beginning of this path. |
| [`PrivateGetKind`](#maxon.NodePathInterface.PrivateGetKind)() |  |
| [`StartsWith`](#maxon.NodePathInterface.StartsWith)(other) | Checks whether this path starts with *other*. |
| [`ToBlock`](#maxon.NodePathInterface.ToBlock)() | Returns the internally stored path as a [`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block). |
| [`ToString`](#maxon.NodePathInterface.ToString)() |  |
| [`__add__`](#maxon.NodePathInterface.__add__)(other) | Appends a node subpath at the end of this path. |
| [`__eq__`](#maxon.NodePathInterface.__eq__)(other) | Checks if *self* equals to *other*. |
| [`__getitem__`](#maxon.NodePathInterface.__getitem__)(index) | Returns the path element at the given #index. |
| [`__hash__`](#maxon.NodePathInterface.__hash__)() | Return hash(self). |
| [`__iter__`](#maxon.NodePathInterface.__iter__)() | Returns an iterator pointing to the first identifier of this path. |
| [`__le__`](#maxon.NodePathInterface.__le__)(other) | Return self<=value. |
| [`__lt__`](#maxon.NodePathInterface.__lt__)(other) | Return self\<value. |
| [`__ne__`](#maxon.NodePathInterface.__ne__)(other) | Checks if *self* is not equals to *other*. |

## Methods Definition <a id="methods-definition"></a>

### `NodePathInterface.Compare(other)` <a id="maxon.NodePathInterface.Compare"></a>

Compares this and *other*.

**Parameters:** **other** – Another [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

**Return type:**

`maxon.COMPARERESULT`

**Returns:** Result of the comparison

### *static* `NodePathInterface.DescribeIO(*args)` <a id="maxon.NodePathInterface.DescribeIO"></a>

### *static* `NodePathInterface.FromCString(path)` <a id="maxon.NodePathInterface.FromCString"></a>

Parses a node path given as a character block into a NodePath object.

The given #path has to match the format returned by ToCString, otherwise an error is returned.

**Parameters:** **path** ([`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [[`maxon.Char`](../../../datatypes/simple/maxon.Char.md#module-maxon.Char)]) – The path to parse.

**Returns:** The parsed NodePath.

**Return type:** [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

### `NodePathInterface.GetCount()` <a id="maxon.NodePathInterface.GetCount"></a>

Returns the length of this path.

> **Note:** The path elements have indices from 0 up to length-1.

**Returns:** Number of elements of this path.

**Return type:** int

### `NodePathInterface.GetHashCode()` <a id="maxon.NodePathInterface.GetHashCode"></a>

Returns the hash code of [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath).

**Returns:** Hash code.

**Return type:** int

### `NodePathInterface.GetKind()` <a id="maxon.NodePathInterface.GetKind"></a>

Returns the node kind of the graph node which is identified by this path: - A path without path list identifiers *<* or *>* is a true node ([`maxon.NODE_KIND.NODE`](../../../enums/maxon.NODE_KIND.NODE.md#maxon.NODE_KIND.NODE)), for example *node/child*. - A path which ends with *<* or *>* is a port list ([`maxon.NODE_KIND.INPUTS`](../../../enums/maxon.NODE_KIND.INPUTS.md#maxon.NODE_KIND.INPUTS) or [`maxon.NODE_KIND.OUTPUTS`](../../../enums/maxon.NODE_KIND.OUTPUTS.md#maxon.NODE_KIND.OUTPUTS)), for example *node/child/<*. - A path which contains *<* or *>*, but does not end with such an identifier is a port ([`maxon.NODE_KIND.INPORT`](../../../enums/maxon.NODE_KIND.INPORT.md#maxon.NODE_KIND.INPORT) or [`maxon.NODE_KIND.OUTPORT`](../../../enums/maxon.NODE_KIND.OUTPORT.md#maxon.NODE_KIND.OUTPORT)), for example *node/child/\</in*.

**Returns:** The node kind of the graph node identified by this path.

**Return type:** [`maxon.NODE_KIND`](../../../enums/maxon.NODE_KIND.md#module-maxon.NODE_KIND)

### `NodePathInterface.GetLastId()` <a id="maxon.NodePathInterface.GetLastId"></a>

Returns the last element of this path.

**Returns:** Last element of this path, or an empty identifier if the path is empty.

**Return type:** [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)

### `NodePathInterface.GetNode()` <a id="maxon.NodePathInterface.GetNode"></a>

Returns only the path of the node without ports.

**Returns:** [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath) with the node path on success.

**Return type:** [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

### `NodePathInterface.GetNodeDepth()` <a id="maxon.NodePathInterface.GetNodeDepth"></a>

Returns the hierarchy depth of the true node which is identified by this path.  
If this path identifies a true node directly, the depth is the number of path elements. Otherwise, if this path identifies a port or port list, the depth is the depth of the innermost enclosing true node, i.e., the number of path elements up to but excluding the port list identifier.  
For example all of the paths *node/child*, *node/child/<* and *node/child/\</in* have a node depth of 2 because for all those paths *node/child* is the innermost true node.

**Returns:** The depth of the true node given by this path.

**Return type:** int

### `NodePathInterface.GetParent()` <a id="maxon.NodePathInterface.GetParent"></a>

Returns the path of the parent of this path.

**Return type:** [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

**Returns:** The parent of this path, or an empty path if this path is already the root path.

### `NodePathInterface.GetPart(src, count)` <a id="maxon.NodePathInterface.GetPart"></a>

Returns a part of this node path as a new NodePath.

**Parameters:**

- **src** (*int*) – Position where the new partial path will start. This has to be within the bounds, otherwise an error is returned.
- **count** (*int*) – Number of identifiers for the partial path. If it is larger than the number of available identifiers an error is returned.

**Returns:** The partial path.

**Return type:** [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

### `NodePathInterface.GetPortPart()` <a id="maxon.NodePathInterface.GetPortPart"></a>

Returns the port part of this path as a new NodePath.  
The port parts starts at the input/output list identifier.

**Returns:** The port part of this path.

**Return type:** [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

### `NodePathInterface.GetPortPath()` <a id="maxon.NodePathInterface.GetPortPath"></a>

Returns only the relative port path without the node path.

**Returns:** PathBlock with the ports on success.

**Return type:** [`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [[`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]

### `NodePathInterface.GetTopLevelPort()` <a id="maxon.NodePathInterface.GetTopLevelPort"></a>

Returns the path to the @ref Port “top-level port” of this path.  
The top-level port of a port is the outermost enclosing port, i.e., an enclosing port which is a direct child of a port list, or the port itself it this is already a direct child of a port list.

**Returns:** The path to the top-level port of the port given by this path. If this path doesn’t represent a port, an error is returned.

**Return type:** [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

### `NodePathInterface.IsEmpty()` <a id="maxon.NodePathInterface.IsEmpty"></a>

Checks if this path is an empty path. The root node of a node system is identified by an empty path.

**Returns:** **True** if this is an empty path (of length 0), **False** otherwise.

**Return type:** bool

### `NodePathInterface.IsInputsOrOutputs(i)` <a id="maxon.NodePathInterface.IsInputsOrOutputs"></a>

Checks if the identifier i stands for the input or output port list of a node, so if it is either ‘<’ or ‘>’.

**Parameters:** **i** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – An identifier for a general node.

**Returns:** **True** if the identifier stands for the input or output port list.

**Return type:** bool

### `NodePathInterface.IsPopulated()` <a id="maxon.NodePathInterface.IsPopulated"></a>

Checks if this path contains anything.

**Returns:** **True** if this is not an empty path (of length 0), **False** otherwise.

**Return type:** bool

### `NodePathInterface.IsPortOfRoot()` <a id="maxon.NodePathInterface.IsPortOfRoot"></a>

Checks if this path identifies a port of the root node of a node system.  
This includes not only top-level ports, but also nested ports.

**Returns:** **True** if this path stands for a port of the root node, **False** otherwise.

**Return type:** bool

### `NodePathInterface.IsTopLevelPort()` <a id="maxon.NodePathInterface.IsTopLevelPort"></a>

Checks if this path identifies a “top-level port”.  
A top-level port is a port which is not nested within another port, but a direct child of the input or output port list of a node.

**Return type:** bool

**Returns:** **True** if this path stands for a top-level port, **False** otherwise.

### `NodePathInterface.LessThan(other)` <a id="maxon.NodePathInterface.LessThan"></a>

### `NodePathInterface.LessThanOrEqual(other)` <a id="maxon.NodePathInterface.LessThanOrEqual"></a>

### `NodePathInterface.Prepend(prefix)` <a id="maxon.NodePathInterface.Prepend"></a>

Prepends a node prefix at the beginning of this path.

**Parameters:** **prefix** ([`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [[`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – The prefix to insert.

**Returns:** The newly [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

**Return type:** [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

### `NodePathInterface.PrivateGetKind()` <a id="maxon.NodePathInterface.PrivateGetKind"></a>

### `NodePathInterface.StartsWith(other)` <a id="maxon.NodePathInterface.StartsWith"></a>

Checks whether this path starts with *other*.

**Parameters:** **other** ([`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [[`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]) – Another path.

**Returns:** **True** if this path starts with the given path or in case of error, otherwise **False**.

**Return type:** bool

### `NodePathInterface.ToBlock()` <a id="maxon.NodePathInterface.ToBlock"></a>

Returns the internally stored path as a [`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block).

> **Note:** The returned block references the internal storage of this path and is only valid as long as this [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath) is alive.

**Returns:** This path as a block of identifiers.

**Return type:** [`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [[`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]

### `NodePathInterface.ToString()` <a id="maxon.NodePathInterface.ToString"></a>

### `NodePathInterface.__add__(other)` <a id="maxon.NodePathInterface.__add__"></a>

Appends a node subpath at the end of this path.

**Parameters:** **other** (Union[[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), str, [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)]) – The subpath to append.

**Returns:** The operation result.

**Return type:** [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)

### `NodePathInterface.__eq__(other)` <a id="maxon.NodePathInterface.__eq__"></a>

Checks if *self* equals to *other*.

**Parameters:** **other** (Union[[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), str, [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)]) – The *other* to check against self.

**Returns:** **True** if this equals *other*, **False** otherwise.

### `NodePathInterface.__getitem__(index)` <a id="maxon.NodePathInterface.__getitem__"></a>

Returns the path element at the given #index.

> **Note:** The index is zero-based, i.e., from 0 up to length-1.

**Parameters:** **index** (*int*) – The index of the element to return. It has to be within the bounds, otherwise the behaviour is undefined.

**Returns:** The path element at *index*.

**Return type:** [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)

### `NodePathInterface.__hash__()` <a id="maxon.NodePathInterface.__hash__"></a>

Return hash(self).

### `NodePathInterface.__iter__()` <a id="maxon.NodePathInterface.__iter__"></a>

Returns an iterator pointing to the first identifier of this path.

**Returns:** Generator pointing to first identifier.

**Return type:** Generator[[`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)]

### `NodePathInterface.__le__(other)` <a id="maxon.NodePathInterface.__le__"></a>

Return self<=value.

### `NodePathInterface.__lt__(other)` <a id="maxon.NodePathInterface.__lt__"></a>

Return self\<value.

### `NodePathInterface.__ne__(other)` <a id="maxon.NodePathInterface.__ne__"></a>

Checks if *self* is not equals to *other*.

**Parameters:** **other** (Union[[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), str, [`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId), [`maxon.NodePath`](../datatype/maxon.NodePath.md#module-maxon.NodePath)]) – The *other* to check against self.

**Returns:** **True** if this is not equals *other*, **False** otherwise.
