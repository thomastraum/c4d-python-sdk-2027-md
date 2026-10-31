<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/graphview/index.html -->

# c4d.modules.graphview <a id="c4d-modules-graphview"></a>

## *class* `c4d.modules.graphview` <a id="c4d.modules.graphview"></a>

- [`c4d.modules.graphview.GvNode`](GvNode/index.md#c4d.modules.graphview.GvNode)
- [`c4d.modules.graphview.GvNodeMaster`](GvNodeMaster/index.md#c4d.modules.graphview.GvNodeMaster)
- [`c4d.modules.graphview.GvPort`](GvPort/index.md#c4d.modules.graphview.GvPort)
- [`c4d.modules.graphview.XPressoTag`](XPressoTag/index.md#c4d.modules.graphview.XPressoTag)

## Overview <a id="overview"></a>

**Dialog Management**

- [`c4d.modules.graphview.CloseDialog()`](#c4d.modules.graphview.CloseDialog): Closes a dialog opened with `OpenDialog()`.
- [`c4d.modules.graphview.OpenDialog()`](#c4d.modules.graphview.OpenDialog): Opens the Xpresso dialog for a specific node master.

**Graph View Operations**

- [`c4d.modules.graphview.GetDefaultOperatorIcon()`](#c4d.modules.graphview.GetDefaultOperatorIcon): Gets the default operator icon for an operator *type*.
- [`c4d.modules.graphview.GetMaster()`](#c4d.modules.graphview.GetMaster): Get one of the current active master nodes.
- [`c4d.modules.graphview.RedrawMaster()`](#c4d.modules.graphview.RedrawMaster): Redraws the [`GvNodeMaster`](GvNodeMaster/index.md#c4d.modules.graphview.GvNodeMaster).

**Preferences**

- [`c4d.modules.graphview.GetPrefs()`](#c4d.modules.graphview.GetPrefs): Gets the preferences for this world.
- [`c4d.modules.graphview.SetPrefs()`](#c4d.modules.graphview.SetPrefs): The new preferences.

## Members <a id="members"></a>

### Dialog Management <a id="c4d.modules.graphview-function-Dialog-Management"></a>

#### `c4d.modules.graphview.CloseDialog(id)` <a id="c4d.modules.graphview.CloseDialog"></a>

Closes a dialog opened with [`OpenDialog()`](#c4d.modules.graphview.OpenDialog).

**Parameters:** **id** (*int*) – The ID that the dialog was opened with.

#### `c4d.modules.graphview.OpenDialog(id, master)` <a id="c4d.modules.graphview.OpenDialog"></a>

Opens the Xpresso dialog for a specific node master.

**Parameters:**

- **id** (*int*) – Plugin ID.
- **master** ([*c4d.modules.graphview.GvNodeMaster*](GvNodeMaster/index.md#c4d.modules.graphview.GvNodeMaster)) – Node master to open the dialog for.

**Return type:** bool

**Returns:** **True** if the dialog was opened, otherwise **False**.

### Graph View Operations <a id="c4d.modules.graphview-function-Graph-View-Operations"></a>

#### `c4d.modules.graphview.GetDefaultOperatorIcon(type)` <a id="c4d.modules.graphview.GetDefaultOperatorIcon"></a>

Gets the default operator icon for an operator *type*.

**Parameters:**

**type** (*int*) –

Operator type:

|   |   |
|---|---|
| *GV_OPERATOR_TYPE_INVALID* | Invalid. |
| *GV_OPERATOR_TYPE_GROUP* | Group. |
| *GV_OPERATOR_TYPE_NODE* | Node. |
| *GV_OPERATOR_TYPE_DUMMY* | Dummy. |
| *GV_OPERATOR_TYPE_GENERAL* | General. |
| *GV_OPERATOR_TYPE_CALCULATE* | Calculate. |
| *GV_OPERATOR_TYPE_ITERATOR* | Iterator. |
| *GV_OPERATOR_TYPE_BOOL* | Bool. |
| *GV_OPERATOR_TYPE_LOGICAL* | Logical. |
| *GV_OPERATOR_TYPE_ADAPTER* | Adapter. |
| *GV_OPERATOR_TYPE_THINKINGPARTICLES* | Thinking particles. |

**Return type:** [c4d.bitmaps.BaseBitmap](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)

**Returns:** The default operator icon.

#### `c4d.modules.graphview.GetMaster(id)` <a id="c4d.modules.graphview.GetMaster"></a>

Get one of the current active master nodes.

**Parameters:** **id** (*int*) – The ID of the master node.

**Return type:** [c4d.modules.graphview.GvNodeMaster](GvNodeMaster/index.md#c4d.modules.graphview.GvNodeMaster)

**Returns:** The master node identified by *id*.

#### `c4d.modules.graphview.RedrawMaster(master)` <a id="c4d.modules.graphview.RedrawMaster"></a>

Redraws the [`GvNodeMaster`](GvNodeMaster/index.md#c4d.modules.graphview.GvNodeMaster).

**Parameters:** **master** ([*c4d.modules.graphview.GvNodeMaster*](GvNodeMaster/index.md#c4d.modules.graphview.GvNodeMaster)) – The nodemaster to redraw.

### Preferences <a id="c4d.modules.graphview-function-Preferences"></a>

#### `c4d.modules.graphview.GetPrefs()` <a id="c4d.modules.graphview.GetPrefs"></a>

Gets the preferences for this world.

**Return type:** [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:**

A copy of the preferences.

|   |   |   |
|---|---|---|
| *GV_WORLD_CONFIG_UNDO_DEPTH* | int | GraphView undo depth preference. |

#### `c4d.modules.graphview.SetPrefs(bc)` <a id="c4d.modules.graphview.SetPrefs"></a>

The new preferences. Use these container IDs:

**Parameters:**

**bc** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) –

The new preferences.

|   |   |   |
|---|---|---|
| *GV_WORLD_CONFIG_UNDO_DEPTH* | int | GraphView undo depth preference. |
