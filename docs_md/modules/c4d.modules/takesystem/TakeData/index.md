<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/takesystem/TakeData/index.html -->

# c4d.modules.takesystem.TakeData <a id="c4d-modules-takesystem-takedata"></a>

## *class* `c4d.modules.takesystem.TakeData` <a id="c4d.modules.takesystem.TakeData"></a>

## Overview <a id="overview"></a>

**Document And Asset Operations**

- [`TakeData.GetDocument()`](#c4d.modules.takesystem.TakeData.GetDocument): Retrieves the document for the [`TakeData`](#c4d.modules.takesystem.TakeData).
- [`TakeData.SaveTakesWithAssets()`](#c4d.modules.takesystem.TakeData.SaveTakesWithAssets): Executes a “Save Project With Assets” for Takes in the document, each saved file representing a Take.
- [`TakeData.TakeToDocument()`](#c4d.modules.takesystem.TakeData.TakeToDocument): Isolates a Take in a new document.

**Hierarchy Management**

- [`TakeData.AddTake()`](#c4d.modules.takesystem.TakeData.AddTake): Creates and inserts a new Take.
- [`TakeData.DeleteTake()`](#c4d.modules.takesystem.TakeData.DeleteTake): Deletes a Take and all connected overrides.
- [`TakeData.InsertTake()`](#c4d.modules.takesystem.TakeData.InsertTake): Moves a Take in the hierarchy in a safe way.

**Override Management**

- [`TakeData.CheckOverrideEnabling()`](#c4d.modules.takesystem.TakeData.CheckOverrideEnabling): Checks for a specific **OVERRIDEENABLING**.
- [`TakeData.FindOverrideCounterPart()`](#c4d.modules.takesystem.TakeData.FindOverrideCounterPart): Finds the backup node that fits with an Override (for example the backup node in the Main Take).
- [`TakeData.GetOverrideEnabling()`](#c4d.modules.takesystem.TakeData.GetOverrideEnabling): Retrieves the ability for the Take System to override a specific kind of node based on global switch.

**System State**

- [`TakeData.GetUndoState()`](#c4d.modules.takesystem.TakeData.GetUndoState): Gets the state of automatic Take undo.
- [`TakeData.ResetSystem()`](#c4d.modules.takesystem.TakeData.ResetSystem): Resets completely the Take System.
- [`TakeData.SetUndoState()`](#c4d.modules.takesystem.TakeData.SetUndoState): Activates or deactivates the state of automatic Take undo.

**Take Navigation**

- [`TakeData.GetCurrentTake()`](#c4d.modules.takesystem.TakeData.GetCurrentTake): Retrieves the current Take.
- [`TakeData.GetMainTake()`](#c4d.modules.takesystem.TakeData.GetMainTake): Retrieves the Main Take.
- [`TakeData.GetTakeMode()`](#c4d.modules.takesystem.TakeData.GetTakeMode): Retrieves the Take System global mode.
- [`TakeData.GetTakeSelection()`](#c4d.modules.takesystem.TakeData.GetTakeSelection): Retrieves the selected Takes.
- [`TakeData.SetCurrentTake()`](#c4d.modules.takesystem.TakeData.SetCurrentTake): Sets the current Take.

## Members <a id="members"></a>

### Document And Asset Operations <a id="c4d.modules.takesystem.TakeData-method-Document-And-Asset-Operations"></a>

#### `TakeData.GetDocument(self)` <a id="c4d.modules.takesystem.TakeData.GetDocument"></a>

Retrieves the document for the [`TakeData`](#c4d.modules.takesystem.TakeData).

**Return type:** Optional[[c4d.documents.BaseDocument](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]

**Returns:** The document, or **None** if the [`TakeData`](#c4d.modules.takesystem.TakeData) is not initialized.

#### `TakeData.SaveTakesWithAssets(self, selected)` <a id="c4d.modules.takesystem.TakeData.SaveTakesWithAssets"></a>

Executes a “Save Project With Assets” for Takes in the document, each saved file representing a Take.

**Parameters:** **selected** (*bool*) – If **True** only selected Takes are exported, otherwise all.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `TakeData.TakeToDocument(self, take)` <a id="c4d.modules.takesystem.TakeData.TakeToDocument"></a>

Isolates a Take in a new document. The new document is allocated and filled by the function.

> **Note:** The caller has to insert the document if necessary.

**Parameters:** **take** ([*c4d.modules.takesystem.BaseTake*](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)) – The Take to isolate.

**Return type:** [c4d.documents.BaseDocument](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)

**Returns:** The allocated document.

### Hierarchy Management <a id="c4d.modules.takesystem.TakeData-method-Hierarchy-Management"></a>

#### `TakeData.AddTake(self, name, parent, cloneFrom)` <a id="c4d.modules.takesystem.TakeData.AddTake"></a>

Creates and inserts a new Take.

> **Note:** An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see `TakeData.GetUndoState()`/`TakeData.SetUndoState()`).

> **Warning:** Selections have to be handled manually.

**Parameters:**

- **name** (*str*) – The name of the Take to add. If an empty string is passed the default Take name will be used.
- **parent** ([*c4d.modules.takesystem.BaseTake*](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)) – Optionally pass a parent Take, otherwise the new Take will be added at the end of the list under the Main Take.
- **cloneFrom** ([*c4d.modules.takesystem.BaseTake*](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)) – Optionally pass a Take the new Take will be cloned from.

**Return type:** [c4d.modules.takesystem.BaseTake](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)

**Returns:** The added Take.

#### `TakeData.DeleteTake(self, take)` <a id="c4d.modules.takesystem.TakeData.DeleteTake"></a>

Deletes a Take and all connected overrides. If Take is the current the Main Take will be set as current.

> **Note:** An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see `TakeData.GetUndoState()`/`TakeData.SetUndoState()`).

**Parameters:** **take** ([*c4d.modules.takesystem.BaseTake*](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)) – The Take to delete.

#### `TakeData.InsertTake(self, takeToMove, destTake, insertMode)` <a id="c4d.modules.takesystem.TakeData.InsertTake"></a>

Moves a Take in the hierarchy in a safe way.  
The Take system has several hierarchy dependencies.  
If a Take is moved while it is current or while it is a child of the Current Take then this would need to manually take care of all data sorting and handling.  
This function do all this work.

> **Note:** An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see `TakeData.GetUndoState()`/`TakeData.SetUndoState()`).

**Parameters:**

- **takeToMove** ([*c4d.modules.takesystem.BaseTake*](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)) – The Take to move.

- **destTake** (*Optional*[[*c4d.modules.takesystem.BaseTake*](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)]) – The parent destination Take. If **None** the Main Take is used. In this case c4d.NOTOK can be used as the insert mode to add the take as the last child of the main take

- **insertMode** (*int*) –

  The insertion mode:

  |   |   |
  |---|---|
  | *INSERT_BEFORE* | Insert before. |
  | *INSERT_AFTER* | Insert after. |
  | *INSERT_UNDER* | Insert under. |
  | *INSERT_REPLACE* | Replace the object. |

### Override Management <a id="c4d.modules.takesystem.TakeData-method-Override-Management"></a>

#### `TakeData.CheckOverrideEnabling(self, mask)` <a id="c4d.modules.takesystem.TakeData.CheckOverrideEnabling"></a>

Checks for a specific **OVERRIDEENABLING**.

**Parameters:**

**mask** (*int*) –

The Take System override enabling mask:

|   |   |
|---|---|
| *OVERRIDEENABLING_NONE* | None. |
| *OVERRIDEENABLING_OBJECT* | Object override enabled. |
| *OVERRIDEENABLING_TAG* | Tag override enabled. |
| *OVERRIDEENABLING_MATERIAL* | Material override enabled. |
| *OVERRIDEENABLING_SHADER* | Shader override enabled. |
| *OVERRIDEENABLING_LAYER* | Layer override enabled. |
| *OVERRIDEENABLING_OTHER* | Other types override enabled. |
| *OVERRIDEENABLING_GLOBAL* | Main switch types override enabled. |
| *OVERRIDEENABLING_ENABLING* | Object enabling and visibility override enabled. |
| *OVERRIDEENABLING_TRANSFOM* | Transformation override enabled. |
| *OVERRIDEENABLING_CAMERA* | Active camera override enabled. |
| *OVERRIDEENABLING_RS* | Active render settings override enabled. |
| *OVERRIDEENABLING_PARAM* | Generic parameter override enabled. |

**Return type:** bool

**Returns:** **True** if the OVERRIDEENABLING is set, otherwise **False**.

#### `TakeData.FindOverrideCounterPart(self, overrideNode, descID)` <a id="c4d.modules.takesystem.TakeData.FindOverrideCounterPart"></a>

Finds the backup node that fits with an Override (for example the backup node in the Main Take).

**Parameters:**

- **overrideNode** ([*c4d.modules.takesystem.BaseOverride*](../BaseOverride/index.md#c4d.modules.takesystem.BaseOverride)) – The original Override node.
- **descID** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The description ID to check.

**Return type:** Tuple[[c4d.modules.takesystem.BaseOverride](../BaseOverride/index.md#c4d.modules.takesystem.BaseOverride), [c4d.modules.takesystem.BaseTake](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)]

**Returns:** The counterpart node and the Take that owns it.

#### `TakeData.GetOverrideEnabling(self)` <a id="c4d.modules.takesystem.TakeData.GetOverrideEnabling"></a>

Retrieves the ability for the Take System to override a specific kind of node based on global switch.

**Return type:** int

**Returns:**

The Take System override enabling:

|   |   |
|---|---|
| *OVERRIDEENABLING_NONE* | None. |
| *OVERRIDEENABLING_OBJECT* | Object override enabled. |
| *OVERRIDEENABLING_TAG* | Tag override enabled. |
| *OVERRIDEENABLING_MATERIAL* | Material override enabled. |
| *OVERRIDEENABLING_SHADER* | Shader override enabled. |
| *OVERRIDEENABLING_LAYER* | Layer override enabled. |
| *OVERRIDEENABLING_OTHER* | Other types override enabled. |
| *OVERRIDEENABLING_GLOBAL* | Main switch types override enabled. |
| *OVERRIDEENABLING_ENABLING* | Object enabling and visibility override enabled. |
| *OVERRIDEENABLING_TRANSFOM* | Transformation override enabled. |
| *OVERRIDEENABLING_CAMERA* | Active camera override enabled. |
| *OVERRIDEENABLING_RS* | Active render settings override enabled. |
| *OVERRIDEENABLING_PARAM* | Generic parameter override enabled. |

### System State <a id="c4d.modules.takesystem.TakeData-method-System-State"></a>

#### `TakeData.GetUndoState(self)` <a id="c4d.modules.takesystem.TakeData.GetUndoState"></a>

Gets the state of automatic Take undo.

> **Note:** It is useful to deactivate undo when working on document clones in several situation like import/export operations where undo is not important.

**Return type:** bool

**Returns:** **True** if the automatic undo is active, otherwise **False**.

#### `TakeData.ResetSystem(self)` <a id="c4d.modules.takesystem.TakeData.ResetSystem"></a>

Resets completely the Take System. Usually not needed.

> **Warning:** All data not in the current state of the document is deleted.

#### `TakeData.SetUndoState(self, state)` <a id="c4d.modules.takesystem.TakeData.SetUndoState"></a>

Activates or deactivates the state of automatic Take undo.

> **Note:** It is useful to deactivate undo when working on document clones in several situation like import/export operations where undo is not important.

**Parameters:** **state** (*bool*) – **True** if the automatic undo has to be used, otherwise **False**.

### Take Navigation <a id="c4d.modules.takesystem.TakeData-method-Take-Navigation"></a>

#### `TakeData.GetCurrentTake(self)` <a id="c4d.modules.takesystem.TakeData.GetCurrentTake"></a>

Retrieves the current Take.

**Return type:** [c4d.modules.takesystem.BaseTake](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)

**Returns:** The current Take.

#### `TakeData.GetMainTake(self)` <a id="c4d.modules.takesystem.TakeData.GetMainTake"></a>

Retrieves the Main Take.

> **Note:** Main Take is always the first under the header.

**Return type:** [c4d.modules.takesystem.BaseTake](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)

**Returns:** The Main Take.

#### `TakeData.GetTakeMode(self)` <a id="c4d.modules.takesystem.TakeData.GetTakeMode"></a>

Retrieves the Take System global mode. Can be **TAKE_MODE_MANUAL** or **TAKE_MODE_AUTO**.

> **Note:** This mode affects how the user has to interact with GUI to override parameters.

**Return type:** int

**Returns:**

The Take System mode:

|   |   |
|---|---|
| *TAKE_MODE_MANUAL* | Manual override: the user has to explicitly override every single parameter. |
| *TAKE_MODE_AUTO* | Auto override: the system overrides any edited parameter (similar to Auto Key). |

#### `TakeData.GetTakeSelection(self, children)` <a id="c4d.modules.takesystem.TakeData.GetTakeSelection"></a>

Retrieves the selected Takes.

**Parameters:** **mask** (*bool*) – If **True** also selected Take children are collected.

**Return type:** List[[c4d.modules.takesystem.BaseTake](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)]

**Returns:** The selected Takes.

#### `TakeData.SetCurrentTake(self, take)` <a id="c4d.modules.takesystem.TakeData.SetCurrentTake"></a>

Sets the current Take.

> **Note:** An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see `TakeData.GetUndoState()`/`TakeData.SetUndoState()`).

**Parameters:** **take** ([*c4d.modules.takesystem.BaseTake*](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)) – The Take to set.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.
