<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/graphview/GvNodeMaster/index.html -->

# c4d.modules.graphview.GvNodeMaster <a id="c4d-modules-graphview-gvnodemaster"></a>

## *class* `c4d.modules.graphview.GvNodeMaster` <a id="c4d.modules.graphview.GvNodeMaster"></a>

A [`GvNodeMaster`](#c4d.modules.graphview.GvNodeMaster) stores a collection of [`GvNode`](../GvNode/index.md#c4d.modules.graphview.GvNode).

Parent Class:

- [`c4d.BaseList2D`](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

## Overview <a id="overview"></a>

**Configuration And Availability**

- [`GvNodeMaster.GetPrefs()`](#c4d.modules.graphview.GvNodeMaster.GetPrefs): Returns the settings container.
- [`GvNodeMaster.IsEnabled()`](#c4d.modules.graphview.GvNodeMaster.IsEnabled): Checks if the node master is enabled.
- [`GvNodeMaster.SetPrefs()`](#c4d.modules.graphview.GvNodeMaster.SetPrefs): Set the settings container.

**Execution And Undo**

- [`GvNodeMaster.AddUndo()`](#c4d.modules.graphview.GvNodeMaster.AddUndo): Call this function if you manipulated something with a node master, and you want it to be undoable.
- [`GvNodeMaster.Execute()`](#c4d.modules.graphview.GvNodeMaster.Execute): Calculates the [`GvNodeMaster`](#c4d.modules.graphview.GvNodeMaster).

**Magic Methods**

- [`GvNodeMaster.__init__()`](#c4d.modules.graphview.GvNodeMaster.__init__): Normally not used, use `XPressoTag.__init__()` instead.

**Node Lifecycle And Hierarchy**

- [`GvNodeMaster.AllocNode()`](#c4d.modules.graphview.GvNodeMaster.AllocNode): Allocates a node without inserting it.
- [`GvNodeMaster.CreateNode()`](#c4d.modules.graphview.GvNodeMaster.CreateNode): Creates a node and inserts it.
- [`GvNodeMaster.InsertFirst()`](#c4d.modules.graphview.GvNodeMaster.InsertFirst): Inserts a node first in the node list of an Xgroup.
- [`GvNodeMaster.InsertLast()`](#c4d.modules.graphview.GvNodeMaster.InsertLast): Inserts a node last in the node list of an Xgroup.
- [`GvNodeMaster.SetHierarchy()`](#c4d.modules.graphview.GvNodeMaster.SetHierarchy): Perform a hierarchy operation.

**Ownership And Root Access**

- [`GvNodeMaster.GetOwner()`](#c4d.modules.graphview.GvNodeMaster.GetOwner): Retrieves the owner.
- [`GvNodeMaster.GetRoot()`](#c4d.modules.graphview.GvNodeMaster.GetRoot): Retrieves the root node.

## Members <a id="members"></a>

### Configuration And Availability <a id="c4d.modules.graphview.GvNodeMaster-method-Configuration-And-Availability"></a>

#### `GvNodeMaster.GetPrefs(self)` <a id="c4d.modules.graphview.GvNodeMaster.GetPrefs"></a>

Returns the settings container.

**Return type:** [c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** A copy of the settings container.

#### `GvNodeMaster.IsEnabled(self)` <a id="c4d.modules.graphview.GvNodeMaster.IsEnabled"></a>

Checks if the node master is enabled.

**Return type:** [c4d.modules.graphview.GvNodeMaster](#c4d.modules.graphview.GvNodeMaster)

**Returns:** **True** if the node master is enabled.

#### `GvNodeMaster.SetPrefs(self, bc)` <a id="c4d.modules.graphview.GvNodeMaster.SetPrefs"></a>

Set the settings container.

**Parameters:** **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The settings container.

### Execution And Undo <a id="c4d.modules.graphview.GvNodeMaster-method-Execution-And-Undo"></a>

#### `GvNodeMaster.AddUndo(self)` <a id="c4d.modules.graphview.GvNodeMaster.AddUndo"></a>

Call this function if you manipulated something with a node master, and you want it to be undoable.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `GvNodeMaster.Execute(self, thread=None)` <a id="c4d.modules.graphview.GvNodeMaster.Execute"></a>

Calculates the [`GvNodeMaster`](#c4d.modules.graphview.GvNodeMaster).

*Changed in version S22.*

**Parameters:** **thread** (*Optional*[[*c4d.threading.BaseThread*](../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)]) –

**Returns:**

| Symbol ID | Description |
|---|---|
| GV_IO_ERR_NONE | No I/O error. |
| GV_CALC_ERR_NONE | No calculation error. |
| GV_CALC_ERR_NO_MEMORY | Out of memory error. |
| GV_CALC_ERR_UNDEFINED | Undefined error. |
| GV_CALC_ERR_UNKNOWN_TYPE | Unknown type error. |
| GV_CALC_ERR_NOT_IMPLEMENTED | Not implemented error. |
| GV_CALC_ERR_NOT_INITIALIZED | Not initialized error. |
| GV_CALC_ERR_NOT_VALID | Not valid error. |
| GV_CALC_ERR_NO_OUTPORT | No output error. |
| GV_CALC_ERR_NOT_CONNECTED | Not connected error. |
| GV_CALC_ERR_NO_PORT | No port error. |
| GV_CALC_ERR_DIVISION_BY_ZERO | Division by zero error. |
| GV_CALC_ERR_TYPE_MISMATCH | Type mismatch error. |
| GV_CALC_ERR_INIT_FAILED | Init failed error. |
| GV_CALC_ERR_QUERY_FAILED | Query failed error. |
| GV_CALC_ERR_CALCULATION_FAILED | Calculation failed error. |
| GV_CALC_ERR_PARAMETER | Bad parameter error. |
| GV_IO_ERR_NO_MEMORY | No memory I/O error. |
| GV_IO_ERR_FILE_NOT_FOUND | File not found I/O error. |
| GV_IO_ERR_READ | Read I/O error. |
| GV_IO_ERR_WRITE | Write I/O error. |
| GV_IO_ERR_NOT_A_GROUPNODE | Not a group node I/O error. |
| GV_NR_OF_SYSTEM_ERRORS | Number of system errors. |
| GV_CALC_ERR_USER_DEFINED | All user defined errors will be above this ID. |

**Return type:** int

### Magic Methods <a id="c4d.modules.graphview.GvNodeMaster-method-Magic-Methods"></a>

#### `GvNodeMaster.__init__(self, host)` <a id="c4d.modules.graphview.GvNodeMaster.__init__"></a>

**Parameters:** **host** ([*BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – Attaches a [`GvNodeMaster`](#c4d.modules.graphview.GvNodeMaster) to a BaseList2D object.

### Node Lifecycle And Hierarchy <a id="c4d.modules.graphview.GvNodeMaster-method-Node-Lifecycle-And-Hierarchy"></a>

#### `GvNodeMaster.AllocNode(self, id)` <a id="c4d.modules.graphview.GvNodeMaster.AllocNode"></a>

Allocates a node without inserting it.

**Parameters:** **id** (*int*) – The id. See [Graph View Node Types](../../../../types/gvnodes.md).

**Return type:** [c4d.modules.graphview.GvNode](../GvNode/index.md#c4d.modules.graphview.GvNode)

**Returns:** The new node.

#### `GvNodeMaster.CreateNode(self, parent, id, insert=None, x=-1, y=-1)` <a id="c4d.modules.graphview.GvNodeMaster.CreateNode"></a>

Creates a node and inserts it.

**Parameters:**

- **parent** ([*c4d.modules.graphview.GvNode*](../GvNode/index.md#c4d.modules.graphview.GvNode)) – Parent node, can be [`GetRoot()`](#c4d.modules.graphview.GvNodeMaster.GetRoot).
- **id** (*int*) – The id. See [Graph View Node Types](../../../../types/gvnodes.md).
- **insert** (*Optional*[[*c4d.modules.graphview.GvNode*](../GvNode/index.md#c4d.modules.graphview.GvNode)]) – The insertion point.
- **x** (*int*) – X position
- **y** (*int*) – Y position.

**Return type:** [c4d.modules.graphview.GvNode](../GvNode/index.md#c4d.modules.graphview.GvNode)

**Returns:** The created node.

#### `GvNodeMaster.InsertFirst(self, parent, node)` <a id="c4d.modules.graphview.GvNodeMaster.InsertFirst"></a>

Inserts a node first in the node list of an Xgroup.

> **Note:** Equivalent to `GeListNode.InsertUnder()`, but with additional checks that parent is a group node, and that node is removed.

**Parameters:**

- **parent** ([*c4d.modules.graphview.GvNode*](../GvNode/index.md#c4d.modules.graphview.GvNode)) – Parent node. Must be in the same node master.
- **node** ([*c4d.modules.graphview.GvNode*](../GvNode/index.md#c4d.modules.graphview.GvNode)) – Node to insert.

**Return type:** bool

**Returns:** **True** if the node was inserted, otherwise **False**.

#### `GvNodeMaster.InsertLast(self, parent, node)` <a id="c4d.modules.graphview.GvNodeMaster.InsertLast"></a>

Inserts a node last in the node list of an Xgroup.

> **Note:** Equivalent to `GeListNode.InsertUnderLast()`, but with additional checks that parent is a group node, and that node is removed.

**Parameters:**

- **parent** ([*c4d.modules.graphview.GvNode*](../GvNode/index.md#c4d.modules.graphview.GvNode)) – Parent node. Must be in the same node master.
- **node** ([*c4d.modules.graphview.GvNode*](../GvNode/index.md#c4d.modules.graphview.GvNode)) – Node to insert.

**Return type:** bool

**Returns:** **True** if the node was inserted, otherwise **False**.

#### `GvNodeMaster.SetHierarchy(self, insert, node, mode=3)` <a id="c4d.modules.graphview.GvNodeMaster.SetHierarchy"></a>

Perform a hierarchy operation. Pass the arguments as a dictionary.

**Parameters:**

- **insert** ([*c4d.modules.graphview.GvNode*](../GvNode/index.md#c4d.modules.graphview.GvNode)) – Insertion point.

- **node** ([*c4d.modules.graphview.GvNode*](../GvNode/index.md#c4d.modules.graphview.GvNode)) – The node to perform the operation on.

- **mode** (*int*) –

  The insertion mode:

  |   |   |
  |---|---|
  | *GV_INSERT_UNDER* | Input port. |
  | *GV_INSERT_UNDER_LAST* | Insert under as last item. |
  | *GV_INSERT_BEFORE* | Insert before. |
  | *GV_INSERT_AFTER* | Insert after. |
  | *GV_INSERT_NONE* | Not used. |

**Return type:** bool

**Returns:** **True** if the hierarchy was set, otherwise **False**.

### Ownership And Root Access <a id="c4d.modules.graphview.GvNodeMaster-method-Ownership-And-Root-Access"></a>

#### `GvNodeMaster.GetOwner(self)` <a id="c4d.modules.graphview.GvNodeMaster.GetOwner"></a>

Retrieves the owner.

**Return type:** [c4d.BaseList2D](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

**Returns:** The owner of the [`GvNodeMaster`](#c4d.modules.graphview.GvNodeMaster)

#### `GvNodeMaster.GetRoot(self)` <a id="c4d.modules.graphview.GvNodeMaster.GetRoot"></a>

Retrieves the root node.

**Return type:** Optional[[c4d.modules.graphview.GvNode](../GvNode/index.md#c4d.modules.graphview.GvNode)]

**Returns:** The root node or **None**.
