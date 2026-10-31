<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/character/CAWeightMgr/index.html -->

# c4d.modules.character.CAWeightMgr <a id="c4d-modules-character-caweightmgr"></a>

## *class* `c4d.modules.character.CAWeightMgr` <a id="c4d.modules.character.CAWeightMgr"></a>

Represents the Weight Manager.

*New in version R19.*

> **Note:**
>
> Weight Manager data and settings are per document.  
> Any change on a document does not affect other open documents.

## Overview <a id="overview"></a>

**List Access**

- [`CAWeightMgr.GetJointCount()`](#c4d.modules.character.CAWeightMgr.GetJointCount): Queries the number of joints bound to a weight tag.
- [`CAWeightMgr.GetJointId()`](#c4d.modules.character.CAWeightMgr.GetJointId): Returns the unique Id of a joint.
- [`CAWeightMgr.GetJointIndex()`](#c4d.modules.character.CAWeightMgr.GetJointIndex): Finds a joint’s main (tag) and sub (joint) indices in the joint list.
- [`CAWeightMgr.GetJointObject()`](#c4d.modules.character.CAWeightMgr.GetJointObject): Finds a joint object from its indices or Id in the joint list.
- [`CAWeightMgr.GetMeshObject()`](#c4d.modules.character.CAWeightMgr.GetMeshObject): Finds the object owning the weight tag from a tag index in the joint list.
- [`CAWeightMgr.GetTagCount()`](#c4d.modules.character.CAWeightMgr.GetTagCount): Queries the number of weight tags for the passed document *doc*.
- [`CAWeightMgr.GetTagIndex()`](#c4d.modules.character.CAWeightMgr.GetTagIndex): Finds a tag’s index in the joint list.
- [`CAWeightMgr.GetWeightTag()`](#c4d.modules.character.CAWeightMgr.GetWeightTag): Finds a weight tag from its index in the joint list.
- [`CAWeightMgr.ValidateJointIndex()`](#c4d.modules.character.CAWeightMgr.ValidateJointIndex): Validates tag and joint indices before access.

**Locks**

- [`CAWeightMgr.IsJointLocked()`](#c4d.modules.character.CAWeightMgr.IsJointLocked): Checks if a joint of the Weight Manager list is locked.
- [`CAWeightMgr.LockAllJoints()`](#c4d.modules.character.CAWeightMgr.LockAllJoints): Locks all joints of all tags in the Weight Manager list.
- [`CAWeightMgr.LockSelectedJoints()`](#c4d.modules.character.CAWeightMgr.LockSelectedJoints): Locks selected joints in the Weight Manager list.
- [`CAWeightMgr.UnlockAllJoints()`](#c4d.modules.character.CAWeightMgr.UnlockAllJoints): Unlocks all joints of all tags in the Weight Manager list.
- [`CAWeightMgr.UnlockSelectedJoints()`](#c4d.modules.character.CAWeightMgr.UnlockSelectedJoints): Unlocks selected joints in the Weight Manager list.

**Manager Update**

- [`CAWeightMgr.GetAutoWeightAlgoId()`](#c4d.modules.character.CAWeightMgr.GetAutoWeightAlgoId): Get the AutoWeightRef algorithm’s id associated with the given index.
- [`CAWeightMgr.GetAutoWeightAlgoIndex()`](#c4d.modules.character.CAWeightMgr.GetAutoWeightAlgoIndex): Get the AutoWeightRef algorithm’s index associated with the given id.
- [`CAWeightMgr.GetAutoWeightDictionary()`](#c4d.modules.character.CAWeightMgr.GetAutoWeightDictionary): Get autoweight dictionary of the Weight Manager.
- [`CAWeightMgr.GetParameter()`](#c4d.modules.character.CAWeightMgr.GetParameter): Retrieves a parameter of the Weight Manager.
- [`CAWeightMgr.SetAutoWeightDictionary()`](#c4d.modules.character.CAWeightMgr.SetAutoWeightDictionary): Get autoweight dictionary of the Weight Manager.
- [`CAWeightMgr.SetDirty()`](#c4d.modules.character.CAWeightMgr.SetDirty): Sets the Weight Manager dirty to force an update on the next call to `Update()`.
- [`CAWeightMgr.SetParameter()`](#c4d.modules.character.CAWeightMgr.SetParameter): Sets a parameters of the Weight Manager.
- [`CAWeightMgr.Update()`](#c4d.modules.character.CAWeightMgr.Update): Updates the internal weighted object list.

**Selection**

- [`CAWeightMgr.IsJointSelected()`](#c4d.modules.character.CAWeightMgr.IsJointSelected): Checks if a joint of the Weight Manager list is selected.
- [`CAWeightMgr.SelectAllJoints()`](#c4d.modules.character.CAWeightMgr.SelectAllJoints): Selects all joints of all tags in the Weight Manager list.
- [`CAWeightMgr.SelectJoint()`](#c4d.modules.character.CAWeightMgr.SelectJoint): Selects a joint of the Weight Manager list.
- [`CAWeightMgr.UnselectAllJointListNodes()`](#c4d.modules.character.CAWeightMgr.UnselectAllJointListNodes): Deselects all of the nodes in the Weight Manager joint list.
- [`CAWeightMgr.UnselectAllJoints()`](#c4d.modules.character.CAWeightMgr.UnselectAllJoints): Deselects all joints of all tags in the Weight Manager list.
- [`CAWeightMgr.UnselectJoint()`](#c4d.modules.character.CAWeightMgr.UnselectJoint): Deselects a joint of the Weight Manager list.

**Weighting Functions**

- [`CAWeightMgr.ApplyWeightFunction()`](#c4d.modules.character.CAWeightMgr.ApplyWeightFunction): Applies the currently selected weighting function to the selected joints (add, smooth, remap etc.).
- [`CAWeightMgr.AutoWeight()`](#c4d.modules.character.CAWeightMgr.AutoWeight): Runs an auto weight algorithm on the selected joints.
- [`CAWeightMgr.BakeWeights()`](#c4d.modules.character.CAWeightMgr.BakeWeights): Bakes the effector weights.
- [`CAWeightMgr.ClearWeights()`](#c4d.modules.character.CAWeightMgr.ClearWeights): Clears all weights on the selected joints.
- [`CAWeightMgr.CopyWeights()`](#c4d.modules.character.CAWeightMgr.CopyWeights): Copies the weights of the selected joints into the weights clipboard.
- [`CAWeightMgr.FlipWeights()`](#c4d.modules.character.CAWeightMgr.FlipWeights): Flips the weights of the selected joints.
- [`CAWeightMgr.MirrorWeights()`](#c4d.modules.character.CAWeightMgr.MirrorWeights): Mirrors the weights for the selected joints.
- [`CAWeightMgr.NormalizeWeights()`](#c4d.modules.character.CAWeightMgr.NormalizeWeights): Applies a normalization on the selected joints.
- [`CAWeightMgr.PasteWeights()`](#c4d.modules.character.CAWeightMgr.PasteWeights): Pastes the copied weights on the selected joints.
- [`CAWeightMgr.SmoothWeights()`](#c4d.modules.character.CAWeightMgr.SmoothWeights): Smooths the weights of the selected joints.

## Members <a id="members"></a>

### List Access <a id="c4d.modules.character.CAWeightMgr-staticmethod-List-Access"></a>

#### *static* `CAWeightMgr.GetJointCount(doc, tagIdx)` <a id="c4d.modules.character.CAWeightMgr.GetJointCount"></a>

Queries the number of joints bound to a weight tag.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **tagIdx** (*int*) – The tag index in the list: *0* <= *tagIdx* < [`GetTagCount()`](#c4d.modules.character.CAWeightMgr.GetTagCount).

**Return type:** int

**Returns:** The joints count.

#### *static* `CAWeightMgr.GetJointId(doc, tag, joint)` <a id="c4d.modules.character.CAWeightMgr.GetJointId"></a>

Returns the unique Id of a joint.

> **Note:** This Id remains valid even if the joint list changes or if undo/redo is used.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **tag** ([*c4d.modules.character.CAWeightTag*](../CAWeightTag/index.md#c4d.modules.character.CAWeightTag)) – The weight tag to search for.
- **joint** ([*c4d.modules.character.CAJointObject*](../CAJointObject/index.md#c4d.modules.character.CAJointObject)) – The joint to search for.

**Return type:** int

**Returns:** The joint unique Id, or **sys.maxsize** if not found.

#### *static* `CAWeightMgr.GetJointIndex(doc, tag, joint)` <a id="c4d.modules.character.CAWeightMgr.GetJointIndex"></a>

Finds a joint’s main (tag) and sub (joint) indices in the joint list.

> **Note:**
>
> The joint index might not match the joint index on the tag.  
> It is not recommended to keep indices over time, some operations might change the list ordering or length.  
> Only the Ids to reference joints can be kept over time.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **tag** ([*c4d.modules.character.CAWeightTag*](../CAWeightTag/index.md#c4d.modules.character.CAWeightTag)) – The weight tag to search for.
- **joint** ([*c4d.modules.character.CAJointObject*](../CAJointObject/index.md#c4d.modules.character.CAJointObject)) – The joint to search for.

**Return type:** Tuple[int, int]

**Returns:** The tag’s index in the joint list, or **NOTOK**/**-1** if not found, and the joint’s index in the joint list, or **NOTOK**/**-1** if not found.

#### *static* `CAWeightMgr.GetJointObject(doc, tagIdx, jointIdx)` <a id="c4d.modules.character.CAWeightMgr.GetJointObject"></a>

Finds a joint object from its indices or Id in the joint list.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **tagIdx** (*int*) – The tag’s index in the joint list.
- **jointIdx** (*int*) – The joint’s index in the joint list.

**Return type:** Optional[[c4d.modules.character.CAJointObject](../CAJointObject/index.md#c4d.modules.character.CAJointObject)]

**Returns:** The joint object, or **None** if not found.

#### *static* `CAWeightMgr.GetMeshObject(doc, tagIdx)` <a id="c4d.modules.character.CAWeightMgr.GetMeshObject"></a>

Finds the object owning the weight tag from a tag index in the joint list.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **tagIdx** (*int*) – The tag’s index in the joint list.

**Return type:** Optional[[c4d.BaseObject](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The mesh object, or **None** if not found.

#### *static* `CAWeightMgr.GetTagCount(doc)` <a id="c4d.modules.character.CAWeightMgr.GetTagCount"></a>

Queries the number of weight tags for the passed document *doc*.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** int

**Returns:** The weight tags count.

#### *static* `CAWeightMgr.GetTagIndex(doc, tag)` <a id="c4d.modules.character.CAWeightMgr.GetTagIndex"></a>

Finds a tag’s index in the joint list.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **tag** ([*c4d.modules.character.CAWeightTag*](../CAWeightTag/index.md#c4d.modules.character.CAWeightTag)) – The weight tag to search for.

**Return type:** int

**Returns:** The tag’s index in the list, or **NOTOK**/**-1** if not found.

#### *static* `CAWeightMgr.GetWeightTag(doc, tagIdx)` <a id="c4d.modules.character.CAWeightMgr.GetWeightTag"></a>

Finds a weight tag from its index in the joint list.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **tagIdx** (*int*) – The tag’s index in the joint list.

**Return type:** Optional[[c4d.modules.character.CAWeightTag](../CAWeightTag/index.md#c4d.modules.character.CAWeightTag)]

**Returns:** The weight tag, or **None** if not found.

#### *static* `CAWeightMgr.ValidateJointIndex(doc, tagIdx, jointIdx)` <a id="c4d.modules.character.CAWeightMgr.ValidateJointIndex"></a>

Validates tag and joint indices before access.

> **Warning:** Call before functions that require tag and joint indices to avoid crashes.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **tagIdx** (*int*) – The tag’s index in the joint list.
- **jointIdx** (*int*) – The joint’s index in the joint list.

**Return type:** bool

**Returns:** **True** if tag and joint indices are valid, otherwise **False**.

### Locks <a id="c4d.modules.character.CAWeightMgr-staticmethod-Locks"></a>

#### *static* `CAWeightMgr.IsJointLocked(doc, tagIdx, jointIdx)` <a id="c4d.modules.character.CAWeightMgr.IsJointLocked"></a>

Checks if a joint of the Weight Manager list is locked.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **tagIdx** (*int*) – The tag’s index in the joint list.
- **jointIdx** (*int*) – The joint’s index in the joint list.

**Return type:** bool

**Returns:** **True** if the joint was found and is locked, otherwise **False**.

#### *static* `CAWeightMgr.LockAllJoints(doc)` <a id="c4d.modules.character.CAWeightMgr.LockAllJoints"></a>

Locks all joints of all tags in the Weight Manager list.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** bool

**Returns:** **True** if all joints got locked, otherwise **False**.

#### *static* `CAWeightMgr.LockSelectedJoints(doc)` <a id="c4d.modules.character.CAWeightMgr.LockSelectedJoints"></a>

Locks selected joints in the Weight Manager list.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### *static* `CAWeightMgr.UnlockAllJoints(doc)` <a id="c4d.modules.character.CAWeightMgr.UnlockAllJoints"></a>

Unlocks all joints of all tags in the Weight Manager list.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### *static* `CAWeightMgr.UnlockSelectedJoints(doc)` <a id="c4d.modules.character.CAWeightMgr.UnlockSelectedJoints"></a>

Unlocks selected joints in the Weight Manager list.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Manager Update <a id="c4d.modules.character.CAWeightMgr-staticmethod-Manager-Update"></a>

#### *static* `CAWeightMgr.GetAutoWeightAlgoId(doc, index)` <a id="c4d.modules.character.CAWeightMgr.GetAutoWeightAlgoId"></a>

Get the AutoWeightRef algorithm’s id associated with the given index.

*New in version R21.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **index** (*int*) – The autoweight int.

**Return type:** maxon.Id

**Returns:** The index of the autoweight id.

#### *static* `CAWeightMgr.GetAutoWeightAlgoIndex(doc, stringId)` <a id="c4d.modules.character.CAWeightMgr.GetAutoWeightAlgoIndex"></a>

Get the AutoWeightRef algorithm’s index associated with the given id.

*New in version R21.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **stringId** (*maxon.Id*) – The autoweight id.

**Return type:** int

**Returns:** The index of the autoweight id.

#### *static* `CAWeightMgr.GetAutoWeightDictionary(doc, stringId)` <a id="c4d.modules.character.CAWeightMgr.GetAutoWeightDictionary"></a>

Get autoweight dictionary of the Weight Manager.

*New in version R21.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **stringId** (*maxon.Id*) – The maxon id of the autoweight algorithm.

**Return type:** maxon.DataDictionary

**Returns:** The data dictionary with the autoweight parameters inside.

#### *static* `CAWeightMgr.GetParameter(doc, id)` <a id="c4d.modules.character.CAWeightMgr.GetParameter"></a>

Retrieves a parameter of the Weight Manager.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **id** (*int*) – The ID of the parameter to set.

**Return type:** Optional[Any]

**Returns:** The parameter data, otherwise **None** if the function failed.

#### *static* `CAWeightMgr.SetAutoWeightDictionary(doc, dataDictionary, stringId)` <a id="c4d.modules.character.CAWeightMgr.SetAutoWeightDictionary"></a>

Get autoweight dictionary of the Weight Manager.

*New in version R21.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **dataDictionary** (*maxon.The data dictionary with the autoweight parameters inside.*) – The data dictionary with the autoweight parameters inside.
- **stringId** (*maxon.Id*) – The maxon id of the autoweight algorithm.

**Return type:** bool

**Returns:** **True** if it worked.

#### *static* `CAWeightMgr.SetDirty(doc)` <a id="c4d.modules.character.CAWeightMgr.SetDirty"></a>

Sets the Weight Manager dirty to force an update on the next call to [`Update()`](#c4d.modules.character.CAWeightMgr.Update).  
If the Weight Manager dialog is open or if the Weight Manager is active, the update happens automatically at the next frame.  
To force an update after a parameter change, use [`SetDirty()`](#c4d.modules.character.CAWeightMgr.SetDirty), then call [`Update()`](#c4d.modules.character.CAWeightMgr.Update). Call [`SetDirty()`](#c4d.modules.character.CAWeightMgr.SetDirty) if a Weight Manager’s parameter was directly modified in its container.

> **Note:** Call [`c4d.EventAdd()`](../../../c4d/index.md#c4d.EventAdd) to refresh the Weight Manager UI to show the updated changes.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### *static* `CAWeightMgr.SetParameter(doc, id, newValue)` <a id="c4d.modules.character.CAWeightMgr.SetParameter"></a>

Sets a parameters of the Weight Manager.  
Result is the same as setting a parameter on the Weight Manager’s container directly except that [`SetParameter()`](#c4d.modules.character.CAWeightMgr.SetParameter) allows to specify the document in which to set the parameter.

> **Warning:**
>
> Setting parameters directly into the Weight Manager’s container is not recommended.  
> Doing so requires to make the Weight Manager dirty and to update it manually.

> **Note:** Call [`c4d.EventAdd()`](../../../c4d/index.md#c4d.EventAdd) to refresh the Weight Manager UI to show the updated changes.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **id** (*int*) – The ID of the parameter to set.
- **newValue** (*any*) – The parameter data to set.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### *static* `CAWeightMgr.Update(doc)` <a id="c4d.modules.character.CAWeightMgr.Update"></a>

Updates the internal weighted object list.  
Call before using other methods of CAWeightMgr if the Weight Manager dialog is closed and if the weight tool is inactive. Any of the two condition is enough to have the update run automatically each frame.  
Also call if the weighted object list was changed programmatically. For instance after adding a new tag, performing undo redo, or any reason where an update is needed immediately.

> **Note:**
>
> Update has no effect if nothing dirty is detected.  
> Call [`c4d.EventAdd()`](../../../c4d/index.md#c4d.EventAdd) to refresh the Weight Manager UI to show the updated changes.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Selection <a id="c4d.modules.character.CAWeightMgr-staticmethod-Selection"></a>

#### *static* `CAWeightMgr.IsJointSelected(doc, tagIdx, jointIdx)` <a id="c4d.modules.character.CAWeightMgr.IsJointSelected"></a>

Checks if a joint of the Weight Manager list is selected.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **tagIdx** (*int*) – The tag’s index in the joint list.
- **jointIdx** (*int*) – The joint’s index in the joint list.

**Return type:** bool

**Returns:** **True** if the joint was found and is selected, otherwise **False**.

#### *static* `CAWeightMgr.SelectAllJoints(doc)` <a id="c4d.modules.character.CAWeightMgr.SelectAllJoints"></a>

Selects all joints of all tags in the Weight Manager list.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

#### *static* `CAWeightMgr.SelectJoint(doc, tagIdx, jointIdx)` <a id="c4d.modules.character.CAWeightMgr.SelectJoint"></a>

Selects a joint of the Weight Manager list.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **tagIdx** (*int*) – The tag’s index in the joint list.
- **jointIdx** (*int*) – The joint’s index in the joint list.

**Return type:** bool

**Returns:** **True** if the joint was selected, otherwise **False**.

#### *static* `CAWeightMgr.UnselectAllJointListNodes(doc)` <a id="c4d.modules.character.CAWeightMgr.UnselectAllJointListNodes"></a>

Deselects all of the nodes in the Weight Manager joint list. This includes all type of nodes (mesh/tag/folder/joint).

> **Note:**
>
> The CAWeightMgr API does not allow selecting/deselecting mesh and tags at the moment.  
> As a parent mesh, tag, or folder activates the child joints for painting, call this function to get rid of any mesh/tag that could have been already selected.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

#### *static* `CAWeightMgr.UnselectAllJoints(doc)` <a id="c4d.modules.character.CAWeightMgr.UnselectAllJoints"></a>

Deselects all joints of all tags in the Weight Manager list.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

#### *static* `CAWeightMgr.UnselectJoint(doc, tagIdx, jointIdx)` <a id="c4d.modules.character.CAWeightMgr.UnselectJoint"></a>

Deselects a joint of the Weight Manager list.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **tagIdx** (*int*) – The tag’s index in the joint list.
- **jointIdx** (*int*) – The joint’s index in the joint list.

**Return type:** bool

**Returns:** **True** if the joint was deselected, otherwise **False**.

### Weighting Functions <a id="c4d.modules.character.CAWeightMgr-staticmethod-Weighting-Functions"></a>

#### *static* `CAWeightMgr.ApplyWeightFunction(doc, allPoints=False)` <a id="c4d.modules.character.CAWeightMgr.ApplyWeightFunction"></a>

Applies the currently selected weighting function to the selected joints (add, smooth, remap etc.).  
Uses the parameters currently set in the Weight Manager’s container for the document.

> **Note:** The point selection is fetched from the actual component mode or from point mode if the document is not in component mode.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **allPoints** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – **True** to apply on all the points of the mesh, **False** to apply on point selection.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### *static* `CAWeightMgr.AutoWeight(doc)` <a id="c4d.modules.character.CAWeightMgr.AutoWeight"></a>

Runs an auto weight algorithm on the selected joints.  
Uses the parameters currently set in the Weight Manager’s container for the document.

*Changed in version R21:* *allowNull* parameter no more there.

> **Note:** Adds an undo.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### *static* `CAWeightMgr.BakeWeights(doc, normalize)` <a id="c4d.modules.character.CAWeightMgr.BakeWeights"></a>

Bakes the effector weights.  
Uses the parameters currently set in the Weight Manager’s container for the document.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.
- **normalize** (*bool*) – **True** to normalize after bake operation, otherwise **False**.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### *static* `CAWeightMgr.ClearWeights(doc)` <a id="c4d.modules.character.CAWeightMgr.ClearWeights"></a>

Clears all weights on the selected joints.

> **Note:** Adds an undo.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### *static* `CAWeightMgr.CopyWeights(doc)` <a id="c4d.modules.character.CAWeightMgr.CopyWeights"></a>

Copies the weights of the selected joints into the weights clipboard.

> **Note:**
>
> Document must be in either point, edge or polygon edit mode.  
> If no selection is present on the mesh, all the point are copied, otherwise only the selected points are copied.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### *static* `CAWeightMgr.FlipWeights(doc)` <a id="c4d.modules.character.CAWeightMgr.FlipWeights"></a>

Flips the weights of the selected joints. Each joint is flipped on itself using the local axis specified in Weight Manager container.

> **Note:** Both zero and non zero weights are flipped.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### *static* `CAWeightMgr.MirrorWeights(doc)` <a id="c4d.modules.character.CAWeightMgr.MirrorWeights"></a>

Mirrors the weights for the selected joints.  
Uses the parameters currently set in the Weight Manager’s container for the document.

> **Note:** Adds an undo.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### *static* `CAWeightMgr.NormalizeWeights(doc)` <a id="c4d.modules.character.CAWeightMgr.NormalizeWeights"></a>

Applies a normalization on the selected joints.

> **Note:** Some joints can be locked prior to normalization to avoid touching some joints.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### *static* `CAWeightMgr.PasteWeights(doc, merge)` <a id="c4d.modules.character.CAWeightMgr.PasteWeights"></a>

Pastes the copied weights on the selected joints.  
Uses the parameters currently set in the Weight Manager’s container for the document.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

- **merge** (*bool*) –

  **True** to merge with target weights, **False** to replace target weights:  
  **True** adds the source weights to the target weights. For instance, source point with null weight does not affect the final result.  
  **False** replaces all the target weights with the source weights including null source weights. For instance, all target weights are lost and replaced with source weights.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### *static* `CAWeightMgr.SmoothWeights(doc)` <a id="c4d.modules.character.CAWeightMgr.SmoothWeights"></a>

Smooths the weights of the selected joints.  
Uses the parameters currently set in the Weight Manager’s container for the document.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the Weight Manager.

**Return type:** bool

**Returns:** **True** if successful, otherwise **True**.
