<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/takesystem/BaseTake/index.html -->

# c4d.modules.takesystem.BaseTake <a id="c4d-modules-takesystem-basetake"></a>

## *class* `c4d.modules.takesystem.BaseTake` <a id="c4d.modules.takesystem.BaseTake"></a>

Represents a Take of the Take System.  
It stores [`BaseOverride`](../BaseOverride/index.md#c4d.modules.takesystem.BaseOverride) objects that define how a specific entity is changed in a Take.

> **Warning:** This type cannot be instantiated.

*New in version R17.032.*

Parent Class:

- [`c4d.BaseList2D`](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

## Overview <a id="overview"></a>

**Camera Assignment**

- [`BaseTake.GetCamera()`](#c4d.modules.takesystem.BaseTake.GetCamera): Gets the camera for the Take.
- [`BaseTake.SetCamera()`](#c4d.modules.takesystem.BaseTake.SetCamera): Sets the camera for the Take.

**Hierarchy And Inheritance**

- [`BaseTake.GetEffectiveCamera()`](#c4d.modules.takesystem.BaseTake.GetEffectiveCamera): Gets the camera used by the Take even if it comes from a parent Take.
- [`BaseTake.GetEffectiveRenderData()`](#c4d.modules.takesystem.BaseTake.GetEffectiveRenderData): Gets the render data used by the Take even if it comes from a parent Take.
- [`BaseTake.SearchHierarchy()`](#c4d.modules.takesystem.BaseTake.SearchHierarchy): Checks if the Take is a child of *op*.

**Override Access**

- [`BaseTake.FindOverride()`](#c4d.modules.takesystem.BaseTake.FindOverride): Searches if *node* is overridden in the Take.
- [`BaseTake.FindOverrideInHierarchy()`](#c4d.modules.takesystem.BaseTake.FindOverrideInHierarchy): Searches if *node* parameter with *descID* is overridden in the Take or in a parent.
- [`BaseTake.GetOverrideGroups()`](#c4d.modules.takesystem.BaseTake.GetOverrideGroups): Retrieves the Override Groups nodes owned by the Take.
- [`BaseTake.GetOverrides()`](#c4d.modules.takesystem.BaseTake.GetOverrides): Retrieves the Override nodes owned by the Take.

**Override Editing**

- [`BaseTake.AutoTake()`](#c4d.modules.takesystem.BaseTake.AutoTake): Compares nodes and automatically generates overrides for different parameters in the Take.
- [`BaseTake.DeleteOverride()`](#c4d.modules.takesystem.BaseTake.DeleteOverride): Deletes a single parameter Override for *node* with *descID*.
- [`BaseTake.FindOrAddOverrideParam()`](#c4d.modules.takesystem.BaseTake.FindOrAddOverrideParam): Searches if parameter with *descID* is Overridden.
- [`BaseTake.OverrideNode()`](#c4d.modules.takesystem.BaseTake.OverrideNode): Overrides all parameters of passed *node* in the Take.

**Override Groups**

- [`BaseTake.AddOverrideGroup()`](#c4d.modules.takesystem.BaseTake.AddOverrideGroup): Adds a new Override Group to the Take.
- [`BaseTake.DeleteOverrideGroup()`](#c4d.modules.takesystem.BaseTake.DeleteOverrideGroup): Deletes an Override Group from the Take.
- [`BaseTake.GetFirstOverrideGroup()`](#c4d.modules.takesystem.BaseTake.GetFirstOverrideGroup): Gets the first Override Group in the Take.

**Render Settings**

- [`BaseTake.GetRenderData()`](#c4d.modules.takesystem.BaseTake.GetRenderData): Gets the render data for the Take.
- [`BaseTake.SetRenderData()`](#c4d.modules.takesystem.BaseTake.SetRenderData): Sets the RenderData for the Take.

**Take State**

- [`BaseTake.IsChecked()`](#c4d.modules.takesystem.BaseTake.IsChecked): Gets the mark status of the Take used for rendering and export operations.
- [`BaseTake.IsMain()`](#c4d.modules.takesystem.BaseTake.IsMain): Checks if the Take is the Main Take.
- [`BaseTake.Reset()`](#c4d.modules.takesystem.BaseTake.Reset): Resets all sub-structures and Overrides for the Take.
- [`BaseTake.SetChecked()`](#c4d.modules.takesystem.BaseTake.SetChecked): Sets the mark status of the Take used for rendering and export operations.

## Members <a id="members"></a>

### Camera Assignment <a id="c4d.modules.takesystem.BaseTake-method-Camera-Assignment"></a>

#### `BaseTake.GetCamera(self, takeData)` <a id="c4d.modules.takesystem.BaseTake.GetCamera"></a>

Gets the camera for the Take.

> **Note:** Can return the default camera.

**Parameters:** **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.

**Return type:** Optional[[c4d.BaseObject](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The camera assigned to the Take, or **None** if the Take uses the camera from a parent Take.

#### `BaseTake.SetCamera(self, takeData, camera)` <a id="c4d.modules.takesystem.BaseTake.SetCamera"></a>

Sets the camera for the Take.

> **Note:** Can be the default camera.

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **camera** (*Optional*[[*c4d.BaseObject*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – The camera to set, or **None** to reset and use one from a parent Take.

### Hierarchy And Inheritance <a id="c4d.modules.takesystem.BaseTake-method-Hierarchy-And-Inheritance"></a>

#### `BaseTake.GetEffectiveCamera(self, takeData)` <a id="c4d.modules.takesystem.BaseTake.GetEffectiveCamera"></a>

Gets the camera used by the Take even if it comes from a parent Take.

> **Note:** Can return the default camera.

**Parameters:** **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.

**Return type:** Tuple[[c4d.BaseObject](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject), [c4d.modules.takesystem.BaseTake](#c4d.modules.takesystem.BaseTake)]

**Returns:** The camera used by the Take and the Take it comes from.

#### `BaseTake.GetEffectiveRenderData(self, takeData)` <a id="c4d.modules.takesystem.BaseTake.GetEffectiveRenderData"></a>

Gets the render data used by the Take even if it comes from a parent Take.

**Parameters:** **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.

**Return type:** Tuple[[c4d.documents.RenderData](../../../c4d.documents/RenderData/index.md#c4d.documents.RenderData), [c4d.modules.takesystem.BaseTake](#c4d.modules.takesystem.BaseTake)]

**Returns:** The render data used by the Take and the Take it comes from.

#### `BaseTake.SearchHierarchy(self, op)` <a id="c4d.modules.takesystem.BaseTake.SearchHierarchy"></a>

Checks if the Take is a child of *op*.

**Parameters:** **op** ([*c4d.modules.takesystem.BaseTake*](#c4d.modules.takesystem.BaseTake)) – The Take to search within his hierarchy.

**Return type:** bool

**Returns:** **True** if the Take is child of *op*, otherwise **False**.

### Override Access <a id="c4d.modules.takesystem.BaseTake-method-Override-Access"></a>

#### `BaseTake.FindOverride(self, takeData, node)` <a id="c4d.modules.takesystem.BaseTake.FindOverride"></a>

Searches if *node* is overridden in the Take.

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **node** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The scene node to search the Override for.

**Return type:** Optional[[c4d.modules.takesystem.BaseOverride](../BaseOverride/index.md#c4d.modules.takesystem.BaseOverride)]

**Returns:** The Override if found, otherwise **None**.

#### `BaseTake.FindOverrideInHierarchy(self, takeData, node, descID)` <a id="c4d.modules.takesystem.BaseTake.FindOverrideInHierarchy"></a>

Searches if *node* parameter with *descID* is overridden in the Take or in a parent.

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **node** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The node to search the Override for.
- **descID** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The parameter to search for.

**Return type:** Tuple[[c4d.modules.takesystem.BaseOverride](../BaseOverride/index.md#c4d.modules.takesystem.BaseOverride), [c4d.modules.takesystem.BaseTake](#c4d.modules.takesystem.BaseTake)]

**Returns:** The Override if found and the Take that owns it.

#### `BaseTake.GetOverrideGroups(self)` <a id="c4d.modules.takesystem.BaseTake.GetOverrideGroups"></a>

Retrieves the Override Groups nodes owned by the Take.

**Return type:** List[[c4d.modules.takesystem.BaseOverrideGroup](../BaseOverrideGroup/index.md#c4d.modules.takesystem.BaseOverrideGroup)]

**Returns:** The Override Groups nodes.

#### `BaseTake.GetOverrides(self)` <a id="c4d.modules.takesystem.BaseTake.GetOverrides"></a>

Retrieves the Override nodes owned by the Take.

**Return type:** List[[c4d.modules.takesystem.BaseOverride](../BaseOverride/index.md#c4d.modules.takesystem.BaseOverride)]

**Returns:** The Override nodes.

### Override Editing <a id="c4d.modules.takesystem.BaseTake-method-Override-Editing"></a>

#### `BaseTake.AutoTake(self, takeData, node, undo)` <a id="c4d.modules.takesystem.BaseTake.AutoTake"></a>

Compares nodes and automatically generates overrides for different parameters in the Take.

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **node** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The scene node to override.
- **undo** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The node to compare with.

#### `BaseTake.DeleteOverride(self, takeData, node, descID)` <a id="c4d.modules.takesystem.BaseTake.DeleteOverride"></a>

Deletes a single parameter Override for *node* with *descID*.  
If the Override results empty (no more overridden parameters) then it will be deleted too.

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **node** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The scene node to delete the parameter for.
- **descID** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The parameter Override to be deleted.

#### `BaseTake.FindOrAddOverrideParam(self, takeData, node, descID, overrideValue, backupValue=None, deleteAnim=False)` <a id="c4d.modules.takesystem.BaseTake.FindOrAddOverrideParam"></a>

Searches if parameter with *descID* is Overridden. If not adds a new Override with passed *overrideValue* for the Take.  
If the [`BaseOverride`](../BaseOverride/index.md#c4d.modules.takesystem.BaseOverride) node does not exist the function automatically allocates and inserts it, plus takes care to backup data properly in parent or Main Take.

> **Note:** An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see `TakeData.GetUndoState()`/`TakeData.SetUndoState()`).

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **node** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The scene node to override.
- **descID** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The parameter to override.
- **overrideValue** (*any*) – The initial value to set in the Overrides for the Take.
- **backupValue** (*Optional*[*any*]) – Optionally provide the backup value for the Main/parent Take. Mandatory to set this for parameters not from the GUI.
- **deleteAnim** (*bool*) – If **True** and original parameter in the scene is animated the animation will be removed in the resulting Override.

**Return type:** [c4d.modules.takesystem.BaseOverride](../BaseOverride/index.md#c4d.modules.takesystem.BaseOverride)

**Returns:** The found or newly created Override node.

#### `BaseTake.OverrideNode(self, takeData, node, deleteAnim)` <a id="c4d.modules.takesystem.BaseTake.OverrideNode"></a>

Overrides all parameters of passed *node* in the Take.

> **Note:** An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see `TakeData.GetUndoState()`/`TakeData.SetUndoState()`).

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **node** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The scene node to override.
- **deleteAnim** (*bool*) – If **True** and original parameter in the scene is animated the animation will be removed in the resulting Override.

**Return type:** [c4d.modules.takesystem.BaseOverride](../BaseOverride/index.md#c4d.modules.takesystem.BaseOverride)

**Returns:** The newly created Override node.

### Override Groups <a id="c4d.modules.takesystem.BaseTake-method-Override-Groups"></a>

#### `BaseTake.AddOverrideGroup(self)` <a id="c4d.modules.takesystem.BaseTake.AddOverrideGroup"></a>

Adds a new Override Group to the Take.

> **Note:** An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see `TakeData.GetUndoState()`/`TakeData.SetUndoState()`).

**Return type:** [c4d.modules.takesystem.BaseOverrideGroup](../BaseOverrideGroup/index.md#c4d.modules.takesystem.BaseOverrideGroup)

**Returns:** The added Override Group.

#### `BaseTake.DeleteOverrideGroup(self, takeData, og)` <a id="c4d.modules.takesystem.BaseTake.DeleteOverrideGroup"></a>

Deletes an Override Group from the Take.

> **Note:** An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see `TakeData.GetUndoState()`/`TakeData.SetUndoState()`).

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **og** ([*c4d.modules.takesystem.BaseOverrideGroup*](../BaseOverrideGroup/index.md#c4d.modules.takesystem.BaseOverrideGroup)) – The Override Group to be deleted.

#### `BaseTake.GetFirstOverrideGroup(self)` <a id="c4d.modules.takesystem.BaseTake.GetFirstOverrideGroup"></a>

Gets the first Override Group in the Take.

**Return type:** Optional[[c4d.modules.takesystem.BaseOverrideGroup](../BaseOverrideGroup/index.md#c4d.modules.takesystem.BaseOverrideGroup)]

**Returns:** The first Override Group, or **None** if there is none.

### Render Settings <a id="c4d.modules.takesystem.BaseTake-method-Render-Settings"></a>

#### `BaseTake.GetRenderData(self, takeData)` <a id="c4d.modules.takesystem.BaseTake.GetRenderData"></a>

Gets the render data for the Take.

**Parameters:** **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.

**Return type:** Optional[[c4d.documents.RenderData](../../../c4d.documents/RenderData/index.md#c4d.documents.RenderData)]

**Returns:** The RenderData assigned to the Take, or **None** if the Take uses the RenderData from a parent Take.

#### `BaseTake.SetRenderData(self, takeData, rData)` <a id="c4d.modules.takesystem.BaseTake.SetRenderData"></a>

Sets the RenderData for the Take.

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **rData** (*Optional*[[*c4d.documents.RenderData*](../../../c4d.documents/RenderData/index.md#c4d.documents.RenderData)]) – The render data to set, or **None** to reset and use one from a parent Take.

### Take State <a id="c4d.modules.takesystem.BaseTake-method-Take-State"></a>

#### `BaseTake.IsChecked(self)` <a id="c4d.modules.takesystem.BaseTake.IsChecked"></a>

Gets the mark status of the Take used for rendering and export operations.

**Return type:** Tuple[[c4d.documents.RenderData](../../../c4d.documents/RenderData/index.md#c4d.documents.RenderData), [c4d.modules.takesystem.BaseTake](#c4d.modules.takesystem.BaseTake)]

**Returns:** **True** if the Take is marked, otherwise **False**.

#### `BaseTake.IsMain(self)` <a id="c4d.modules.takesystem.BaseTake.IsMain"></a>

Checks if the Take is the Main Take.

**Return type:** bool

**Returns:** **True** if the Take is the Main Take, otherwise **False**.

#### `BaseTake.Reset(self)` <a id="c4d.modules.takesystem.BaseTake.Reset"></a>

Resets all sub-structures and Overrides for the Take.

> **Warning:** All data not in the current state of the document are deleted.

#### `BaseTake.SetChecked(self, status)` <a id="c4d.modules.takesystem.BaseTake.SetChecked"></a>

Sets the mark status of the Take used for rendering and export operations.

**Parameters:** **status** (*bool*) – If **True** the Take is marked, otherwise the mark is removed.
