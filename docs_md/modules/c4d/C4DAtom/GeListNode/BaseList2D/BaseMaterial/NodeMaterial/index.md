<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/NodeMaterial/index.html -->

# c4d.NodeMaterial <a id="c4d-nodematerial"></a>

## *class* `c4d.NodeMaterial` <a id="c4d.NodeMaterial"></a>

The node-based material with the *Mbase* type.  
This class is a collection of accessors to node-related functionality that are grouped for clarity purposes.  
Note that any [`c4d.BaseMaterial`](../index.md#c4d.BaseMaterial) can be elevated to a [`c4d.NodeMaterial`](#c4d.NodeMaterial), no special construction is needed.

*New in version R24.*

Parent Class:

- [`c4d.BaseMaterial`](../index.md#c4d.BaseMaterial)

## Overview <a id="overview"></a>

**Identification And Mapping**

- [`NodeMaterial.GetMaterial()`](#c4d.NodeMaterial.GetMaterial): Returns the material owner of the provided graph.

**Path Resolution**

- [`NodeMaterial.GetTextureSearchPaths()`](#c4d.NodeMaterial.GetTextureSearchPaths): Determines the paths pointing to directories that are used to reference images by relative path in a particular [`c4d.documents.BaseDocument`](../../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument).

**Graph Management**

- [`NodeMaterial.AddGraph()`](#c4d.NodeMaterial.AddGraph): Creates a node graph for the provided node space identifier if a graph does not already exist.
- [`NodeMaterial.CreateDefaultGraph()`](#c4d.NodeMaterial.CreateDefaultGraph): Creates a node graph populated with default nodes for the provided node space identifier if a graph does not already exist.
- [`NodeMaterial.CreateEmptyGraph()`](#c4d.NodeMaterial.CreateEmptyGraph): Creates an empty node graph for the provided node space identifier if a graph does not already exist.
- [`NodeMaterial.GetGraph()`](#c4d.NodeMaterial.GetGraph): Returns the node graph for the provided node space id.
- [`NodeMaterial.HasSpace()`](#c4d.NodeMaterial.HasSpace): Checks whether the node space under the provided id was instantiated for the material.
- [`NodeMaterial.RemoveGraph()`](#c4d.NodeMaterial.RemoveGraph): Removes a node graph for the provided node space id if there is a graph.

**Identification And Mapping**

- [`NodeMaterial.BaseList2DToUuid()`](#c4d.NodeMaterial.BaseList2DToUuid): Returns the uuid of the given [`c4d.BaseList2D`](../../index.md#c4d.BaseList2D) object.
- [`NodeMaterial.GetBaseListForNode()`](#c4d.NodeMaterial.GetBaseListForNode): Returns the corresponding [`c4d.BaseList2D`](../../index.md#c4d.BaseList2D) element for a [`maxon.GraphNode`](../../../../../../maxon_generated/frameworks/graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode).
- [`NodeMaterial.GetDescIDForNodePort()`](#c4d.NodeMaterial.GetDescIDForNodePort): Calculates the [`c4d.DescID`](../../../../../DescID/index.md#c4d.DescID) for a given port.
- [`NodeMaterial.UuidToBaseList2D()`](#c4d.NodeMaterial.UuidToBaseList2D): Returns the [`c4d.BaseList2D`](../../index.md#c4d.BaseList2D) element with the given uuid.

**Path Resolution**

- [`NodeMaterial.GetMaterialNodePath()`](#c4d.NodeMaterial.GetMaterialNodePath): Returns the node path to the material end node.
- [`NodeMaterial.GetSoloNodePath()`](#c4d.NodeMaterial.GetSoloNodePath): Returns the node path to the solo node.

## Members <a id="members"></a>

### Identification And Mapping <a id="c4d.NodeMaterial-staticmethod-Identification-And-Mapping"></a>

#### *static* `NodeMaterial.GetMaterial(graph)` <a id="c4d.NodeMaterial.GetMaterial"></a>

Returns the material owner of the provided graph.

> **Note:**
>
> The returned BaseMaterial is only safe for access in the usual places of the API.  
> You must avoid to perform read or write access to it in an arbitrary worker thread.

**Parameters:** **graph** ([`maxon.NodesGraphModelRef`](../../../../../../maxon_generated/frameworks/nodes/reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)) – The node graph of the owner.

**Returns:** Returns the owner of the node graph, **None** if unknown or on failure to retrieve.

**Return type:** Optional[[c4d.BaseMaterial](../index.md#c4d.BaseMaterial)]

### Path Resolution <a id="c4d.NodeMaterial-staticmethod-Path-Resolution"></a>

#### *static* `NodeMaterial.GetTextureSearchPaths(secondaryPath, documentPath)` <a id="c4d.NodeMaterial.GetTextureSearchPaths"></a>

Determines the paths pointing to directories that are used to reference images by relative path in a particular [`c4d.documents.BaseDocument`](../../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument).

```python
>>> doc = c4d.documents.GetActiveDocument()
>>> secondaryPath = maxon.Url(doc.GetDataInstance()[c4d.DOCUMENT_SECONDARYPATH])
>>> docPath = maxon.Url(doc.GetDocumentPath())
>>> docPath
file:///C:/Users/m_adam/Documents

>>> textureSearchPaths = c4d.NodeMaterial.GetTextureSearchPaths(secondaryPath, docPath)
>>> for path in textureSearchPaths:
...     print(path)

file:///C:/Users/m_adam/Documents
file:///C:/Users/m_adam/Documents/tex
file:///C:/Users/m_adam/Documents/MAXON/Build/24.029
file:///C:/Users/m_adam/Documents/MAXON/Build/24.029_/tex
file:///C:/Users/m_adam/AppData/Roaming/Maxon/24.029_0F21F86A
file:///C:/Users/m_adam/AppData/Roaming/Maxon/24.029_0F21F86A/tex
```

**Parameters:**

- **secondaryPath** ([`maxon.Url`](../../../../../../maxon_generated/references/io/maxon.Url.md#module-maxon.Url)) – Allows to provide the DOCUMENT_SECONDARYPATH
- **documentPath** ([`maxon.Url`](../../../../../../maxon_generated/references/io/maxon.Url.md#module-maxon.Url)) – The path of the BaseDocument.

**Return type:** [`maxon.BaseArray`](../../../../../../maxon_generated/datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray) ([`maxon.Url`](../../../../../../maxon_generated/references/io/maxon.Url.md#module-maxon.Url))

**Returns:** The set of paths in which the images may be located.

### Graph Management <a id="c4d.NodeMaterial-method-Graph-Management"></a>

#### `NodeMaterial.AddGraph(self, spaceId)` <a id="c4d.NodeMaterial.AddGraph"></a>

Creates a node graph for the provided node space identifier if a graph does not already exist.

*Deprecated since version 2023.1.0:* Use `NodeMaterial.CreateDefaultGraph()` or `NodeMaterial.CreateEmptyGraph()`.

**Parameters:** **spaceId** ([`maxon.Id`](../../../../../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id)) – The id of the node space.

**Returns:** The added graph.

**Return type:** [`maxon.NodesGraphModelRef`](../../../../../../maxon_generated/frameworks/nodes/reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)

#### `NodeMaterial.CreateDefaultGraph(self, spaceId)` <a id="c4d.NodeMaterial.CreateDefaultGraph"></a>

Creates a node graph populated with default nodes for the provided node space identifier if a graph does not already exist.

**Parameters:** **spaceId** ([`maxon.Id`](../../../../../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id)) – The id of the node space.

**Returns:** The added graph.

**Return type:** [`maxon.NodesGraphModelRef`](../../../../../../maxon_generated/frameworks/nodes/reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)

#### `NodeMaterial.CreateEmptyGraph(self, spaceId)` <a id="c4d.NodeMaterial.CreateEmptyGraph"></a>

Creates an empty node graph for the provided node space identifier if a graph does not already exist.

**Parameters:** **spaceId** ([`maxon.Id`](../../../../../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id)) – The id of the node space.

**Returns:** The added graph.

**Return type:** [`maxon.NodesGraphModelRef`](../../../../../../maxon_generated/frameworks/nodes/reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)

#### `NodeMaterial.GetGraph(self, spaceId)` <a id="c4d.NodeMaterial.GetGraph"></a>

Returns the node graph for the provided node space id.

**Parameters:** **spaceId** ([`maxon.Id`](../../../../../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id)) – The id of the node space.

**Raises:** **SystemError** – If the material does not have this space.

**Returns:** Returns the node graph.

**Return type:** [`maxon.NodesGraphModelRef`](../../../../../../maxon_generated/frameworks/nodes/reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)

#### `NodeMaterial.HasSpace(self, spaceId)` <a id="c4d.NodeMaterial.HasSpace"></a>

Checks whether the node space under the provided id was instantiated for the material.

**Parameters:** **spaceId** ([`maxon.Id`](../../../../../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id)) – The id of the node space.

**Returns:** Returns **True** if the node space exists, **False** otherwise.

**Return type:** bool

#### `NodeMaterial.RemoveGraph(self, spaceId)` <a id="c4d.NodeMaterial.RemoveGraph"></a>

Removes a node graph for the provided node space id if there is a graph.

**Parameters:** **spaceId** ([`maxon.Id`](../../../../../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id)) – The id of the node space.

### Identification And Mapping <a id="c4d.NodeMaterial-method-Identification-And-Mapping"></a>

#### `NodeMaterial.BaseList2DToUuid(self, spaceId, object)` <a id="c4d.NodeMaterial.BaseList2DToUuid"></a>

Returns the uuid of the given [`c4d.BaseList2D`](../../index.md#c4d.BaseList2D) object.

**Parameters:**

- **spaceId** ([`maxon.Id`](../../../../../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id)) – The id of the node space.
- **object** ([*c4d.BaseList2D*](../../index.md#c4d.BaseList2D)) – [`c4d.BaseList2D`](../../index.md#c4d.BaseList2D) object to find.

**Return type:** [`maxon.Uuid`](../../../../../../maxon_generated/references/core/maxon.Uuid.md#module-maxon.Uuid)

**Returns:** The uuid

#### `NodeMaterial.GetBaseListForNode(self, spaceId, nodePath)` <a id="c4d.NodeMaterial.GetBaseListForNode"></a>

Returns the corresponding [`c4d.BaseList2D`](../../index.md#c4d.BaseList2D) element for a [`maxon.GraphNode`](../../../../../../maxon_generated/frameworks/graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode).

**Parameters:**

- **spaceId** ([`maxon.Id`](../../../../../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id)) – The id of the node space.
- **nodePath** ([`maxon.NodePath`](../../../../../../maxon_generated/frameworks/graph/datatype/maxon.NodePath.md#module-maxon.NodePath)) – Absolute Path to the Node.

**Returns:** BaseList2D element. The return value can be **None** if there’s no corresponding element, or if it refers to an inner node.

**Return type:** Optional[[c4d.BaseList2D](../../index.md#c4d.BaseList2D)]

#### `NodeMaterial.GetDescIDForNodePort(self, spaceId, node, port)` <a id="c4d.NodeMaterial.GetDescIDForNodePort"></a>

Calculates the [`c4d.DescID`](../../../../../DescID/index.md#c4d.DescID) for a given port.

**Parameters:**

- **spaceId** ([`maxon.Id`](../../../../../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id)) – The id of the node space.
- **node** (`maxon.node`) – The node that owns the port.
- **port** (`maxon.node`) – The port.

**Returns:** The description ID of the port.

**Return type:** [c4d.DescID](../../../../../DescID/index.md#c4d.DescID)

#### `NodeMaterial.UuidToBaseList2D(self, spaceId, uuid)` <a id="c4d.NodeMaterial.UuidToBaseList2D"></a>

Returns the [`c4d.BaseList2D`](../../index.md#c4d.BaseList2D) element with the given uuid.

**Parameters:**

- **spaceId** ([`maxon.Id`](../../../../../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id)) – The id of the node space.
- **uuid** ([`maxon.Uuid`](../../../../../../maxon_generated/references/core/maxon.Uuid.md#module-maxon.Uuid)) – Uuid to find.

**Returns:** BaseList2D object.

**Return type:** [c4d.BaseList2D](../../index.md#c4d.BaseList2D)

### Path Resolution <a id="c4d.NodeMaterial-method-Path-Resolution"></a>

#### `NodeMaterial.GetMaterialNodePath(self, spaceId)` <a id="c4d.NodeMaterial.GetMaterialNodePath"></a>

Returns the node path to the material end node.

**Parameters:** **spaceId** ([`maxon.Id`](../../../../../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id)) – The id of the node space.

**Returns:** The path to the material end node.

**Return type:** [`maxon.NodePath`](../../../../../../maxon_generated/frameworks/graph/datatype/maxon.NodePath.md#module-maxon.NodePath)

#### `NodeMaterial.GetSoloNodePath(self, spaceId)` <a id="c4d.NodeMaterial.GetSoloNodePath"></a>

Returns the node path to the solo node.

**Parameters:** **spaceId** ([`maxon.Id`](../../../../../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id)) – The id of the node space.

**Returns:** The path to the solo node, empty if nothing was soloed.

**Return type:** [`maxon.NodePath`](../../../../../../maxon_generated/frameworks/graph/datatype/maxon.NodePath.md#module-maxon.NodePath)
