<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/nodespace/interface/maxon.NimbusBaseInterface.html -->

# maxon.NimbusBaseInterface <a id="maxon-nimbusbaseinterface"></a>

## Description <a id="module-maxon.NimbusBaseInterface"></a><a id="description"></a>

[`maxon.NimbusBaseRef`](../reference/maxon.NimbusBaseRef.md#module-maxon.NimbusBaseRef) manages a [`maxon.NodesGraphModelRef`](../../nodes/reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef) that is owned by a classic [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) object.  
A [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) object can own multiple graphs, one for each node space.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.NimbusBaseRef`](../reference/maxon.NimbusBaseRef.md#module-maxon.NimbusBaseRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`BaseList2DToUuid`](#maxon.NimbusBaseInterface.BaseList2DToUuid)(object) | Returns the uuid of the given BaseList2D object. |
| [`FindCorrespondingBaseList`](#maxon.NimbusBaseInterface.FindCorrespondingBaseList)(absolutePath) | Returns the corresponding [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) element for a [`maxon.GraphNode`](../../graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode) but will not create one if not already present. |
| [`FindOrCreateCorrespondingBaseList`](#maxon.NimbusBaseInterface.FindOrCreateCorrespondingBaseList)(absolutePath) | Returns the corresponding [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) element for a [`maxon.GraphNode`](../../graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode). |
| [`GetBaseListRoot`](#maxon.NimbusBaseInterface.GetBaseListRoot)() | Returns the C4D object that holds the [`maxon.NimbusBaseRef`](../reference/maxon.NimbusBaseRef.md#module-maxon.NimbusBaseRef). |
| [`GetDescID`](#maxon.NimbusBaseInterface.GetDescID)(port) | Sets up the [`c4d.DescID`](../../../../c4d/DescID/index.md#c4d.DescID) of the parameter which corresponds to the given port. |
| [`GetGraph`](#maxon.NimbusBaseInterface.GetGraph)() | Returns the node graph connected to this object. |
| [`GetGraphNodeFromBaseList`](#maxon.NimbusBaseInterface.GetGraphNodeFromBaseList)(bl) | Returns the node connected to the BaseList2D element. |
| [`GetNodePathFromBaseList`](#maxon.NimbusBaseInterface.GetNodePathFromBaseList)(bl) | Returns the path of the node connected to the BaseList2D element. |
| [`GetPath`](#maxon.NimbusBaseInterface.GetPath)(type) | Returns a path. |
| [`GetSpaceId`](#maxon.NimbusBaseInterface.GetSpaceId)() | Returns the identifier of the node space of the node graph. |
| [`OpenInEditor`](#maxon.NimbusBaseInterface.OpenInEditor)([path]) | Opens the node editor for the node graph held by this [`maxon.NimbusBaseRef`](../reference/maxon.NimbusBaseRef.md#module-maxon.NimbusBaseRef). |
| [`PrviateOpenInEditor`](#maxon.NimbusBaseInterface.PrviateOpenInEditor)(path) |  |
| [`SetPath`](#maxon.NimbusBaseInterface.SetPath)(type, path) | Sets a path. |
| [`UuidToBaseList2D`](#maxon.NimbusBaseInterface.UuidToBaseList2D)(uuid) | Returns the [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) element with the given uuid. |

## Methods Definition <a id="methods-definition"></a>

### `NimbusBaseInterface.BaseList2DToUuid(object)` <a id="maxon.NimbusBaseInterface.BaseList2DToUuid"></a>

Returns the uuid of the given BaseList2D object.

**Parameters:** **object** ([`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – BaseList2D object to find.

**Returns:** Uuid on success.

**Return type:** [`maxon.Uuid`](../../../references/core/maxon.Uuid.md#module-maxon.Uuid)

### `NimbusBaseInterface.FindCorrespondingBaseList(absolutePath)` <a id="maxon.NimbusBaseInterface.FindCorrespondingBaseList"></a>

Returns the corresponding [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) element for a [`maxon.GraphNode`](../../graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode) but will not create one if not already present.

**Parameters:** **absolutePath** ([`maxon.NodePath`](../../graph/datatype/maxon.NodePath.md#module-maxon.NodePath)) – Absolute Path to the Node.

**Returns:** [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) element, e.g. a Material.

**Return type:** [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

### `NimbusBaseInterface.FindOrCreateCorrespondingBaseList(absolutePath)` <a id="maxon.NimbusBaseInterface.FindOrCreateCorrespondingBaseList"></a>

Returns the corresponding [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) element for a [`maxon.GraphNode`](../../graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode). This function creates a new one if not already present.

**Parameters:** **absolutePath** ([`maxon.NodePath`](../../graph/datatype/maxon.NodePath.md#module-maxon.NodePath)) – Absolute Path to the Node.

**Returns:** [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) element. The return value can be None in case no element can be created for the given path, e.g. if it is invalid

**Return type:** [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

### `NimbusBaseInterface.GetBaseListRoot()` <a id="maxon.NimbusBaseInterface.GetBaseListRoot"></a>

Returns the C4D object that holds the [`maxon.NimbusBaseRef`](../reference/maxon.NimbusBaseRef.md#module-maxon.NimbusBaseRef).

**Returns:** [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) element, e.g. a Material.

**Return type:** [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

### `NimbusBaseInterface.GetDescID(port)` <a id="maxon.NimbusBaseInterface.GetDescID"></a>

Sets up the [`c4d.DescID`](../../../../c4d/DescID/index.md#c4d.DescID) of the parameter which corresponds to the given port.

**Parameters:** **port** ([`maxon.NodePath`](../../graph/datatype/maxon.NodePath.md#module-maxon.NodePath)) – A port path.

**Returns:** The DescID.

**Return type:** [`c4d.DescID`](../../../../c4d/DescID/index.md#c4d.DescID)

### `NimbusBaseInterface.GetGraph()` <a id="maxon.NimbusBaseInterface.GetGraph"></a>

Returns the node graph connected to this object.

**Returns:** NodesGraphModelRef on success.

**Return type:** [`maxon.NodesGraphModelRef`](../../nodes/reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)

### *static* `NimbusBaseInterface.GetGraphNodeFromBaseList(bl)` <a id="maxon.NimbusBaseInterface.GetGraphNodeFromBaseList"></a>

Returns the node connected to the BaseList2D element.

**Parameters:** **bl** ([`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The BaseList2D representing a GraphNode.

**Returns:** GraphNode on success.

**Return type:** [`maxon.GraphNode`](../../graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode)

### *static* `NimbusBaseInterface.GetNodePathFromBaseList(bl)` <a id="maxon.NimbusBaseInterface.GetNodePathFromBaseList"></a>

Returns the path of the node connected to the BaseList2D element.

**Parameters:** **bl** ([`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The BaseList2D representing a GraphNode.

**Returns:** NodePath on success.

**Return type:** [`maxon.NodePath`](../../graph/datatype/maxon.NodePath.md#module-maxon.NodePath)

### `NimbusBaseInterface.GetPath(type)` <a id="maxon.NimbusBaseInterface.GetPath"></a>

Returns a path.

> **Note:** The returned path can be invalid and point to a non-existing object.

**Parameters:** **type** ([`maxon.NIMBUS_PATH`](../../../enums/maxon.NIMBUS_PATH.md#module-maxon.NIMBUS_PATH)) – Path type.

**Returns:** Absolute Path to a Node or Port, depending on the given type.

**Return type:** [`maxon.NodePath`](../../graph/datatype/maxon.NodePath.md#module-maxon.NodePath)

### `NimbusBaseInterface.GetSpaceId()` <a id="maxon.NimbusBaseInterface.GetSpaceId"></a>

Returns the identifier of the node space of the node graph.

**Returns:** Node space identifier.

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)

### `NimbusBaseInterface.OpenInEditor(path=None)` <a id="maxon.NimbusBaseInterface.OpenInEditor"></a>

Opens the node editor for the node graph held by this [`maxon.NimbusBaseRef`](../reference/maxon.NimbusBaseRef.md#module-maxon.NimbusBaseRef).

**Parameters:** **path** ([`maxon.NodePath`](../../graph/datatype/maxon.NodePath.md#module-maxon.NodePath)) – An optional path pointing to a group of the node graph.

### `NimbusBaseInterface.PrviateOpenInEditor(path)` <a id="maxon.NimbusBaseInterface.PrviateOpenInEditor"></a>

### `NimbusBaseInterface.SetPath(type, path)` <a id="maxon.NimbusBaseInterface.SetPath"></a>

Sets a path.

**Parameters:**

- **type** ([`maxon.NIMBUS_PATH`](../../../enums/maxon.NIMBUS_PATH.md#module-maxon.NIMBUS_PATH)) – Path type.
- **path** ([`maxon.NodePath`](../../graph/datatype/maxon.NodePath.md#module-maxon.NodePath)) – Absolute Path to a Node or an empty path.

### `NimbusBaseInterface.UuidToBaseList2D(uuid)` <a id="maxon.NimbusBaseInterface.UuidToBaseList2D"></a>

Returns the [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) element with the given uuid.

**Parameters:** **uuid** ([`maxon.Uuid`](../../../references/core/maxon.Uuid.md#module-maxon.Uuid)) – Uuid to find.

**Returns:** BaseList2D object on success.

**Return type:** [`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)
