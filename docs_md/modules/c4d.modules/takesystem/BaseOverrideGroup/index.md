<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/takesystem/BaseOverrideGroup/index.html -->

# c4d.modules.takesystem.BaseOverrideGroup <a id="c4d-modules-takesystem-baseoverridegroup"></a>

## *class* `c4d.modules.takesystem.BaseOverrideGroup` <a id="c4d.modules.takesystem.BaseOverrideGroup"></a>

An Override Group manages the values of multiple objects in a Take.

> **Warning:** This type cannot be instantiated.

*New in version R17.032.*

Parent Class:

- [`c4d.BaseList2D`](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

## Overview <a id="overview"></a>

**Membership And Ownership**

- [`BaseOverrideGroup.AddToGroup()`](#c4d.modules.takesystem.BaseOverrideGroup.AddToGroup): Adds *node* to the Override Group.
- [`BaseOverrideGroup.Find()`](#c4d.modules.takesystem.BaseOverrideGroup.Find): Checks if an object is included in the Override Group.
- [`BaseOverrideGroup.GetObjectsInGroup()`](#c4d.modules.takesystem.BaseOverrideGroup.GetObjectsInGroup): Retrieves all the objects in the group.
- [`BaseOverrideGroup.GetTake()`](#c4d.modules.takesystem.BaseOverrideGroup.GetTake): Returns the Take that owns the Override Group.
- [`BaseOverrideGroup.RemoveFromGroup()`](#c4d.modules.takesystem.BaseOverrideGroup.RemoveFromGroup): Removes *node* from the Override Group.

**Tag Management**

- [`BaseOverrideGroup.AddTag()`](#c4d.modules.takesystem.BaseOverrideGroup.AddTag): Adds a new tag of the given *type* to the Override Group if it is not already there.
- [`BaseOverrideGroup.GetTag()`](#c4d.modules.takesystem.BaseOverrideGroup.GetTag): Searches for a tag of the given *type* attached to the Override Group.
- [`BaseOverrideGroup.RemoveTag()`](#c4d.modules.takesystem.BaseOverrideGroup.RemoveTag): Removes the tag of the given *type* from the Override Group.

**Visibility Modes**

- [`BaseOverrideGroup.GetEditorMode()`](#c4d.modules.takesystem.BaseOverrideGroup.GetEditorMode): Returns the editor visibility mode for the Override Group.
- [`BaseOverrideGroup.GetRenderMode()`](#c4d.modules.takesystem.BaseOverrideGroup.GetRenderMode): Returns the render visibility mode for the Override Group.
- [`BaseOverrideGroup.SetEditorMode()`](#c4d.modules.takesystem.BaseOverrideGroup.SetEditorMode): Sets the editor visibility mode for the Override Group.
- [`BaseOverrideGroup.SetRenderMode()`](#c4d.modules.takesystem.BaseOverrideGroup.SetRenderMode): Sets the render visibility mode for the Override Group.

## Members <a id="members"></a>

### Membership And Ownership <a id="c4d.modules.takesystem.BaseOverrideGroup-method-Membership-And-Ownership"></a>

#### `BaseOverrideGroup.AddToGroup(self, takeData, node)` <a id="c4d.modules.takesystem.BaseOverrideGroup.AddToGroup"></a>

Adds *node* to the Override Group. If *node* is already part of another group it will be automatically removed first.

> **Warning:** The node to add must be a real scene node. Adding BaseOverride nodes is forbidden.

> **Note:** An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see `TakeData.GetUndoState()`/`TakeData.SetUndoState()`).

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **node** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The node to add.

#### `BaseOverrideGroup.Find(self, takeData, op)` <a id="c4d.modules.takesystem.BaseOverrideGroup.Find"></a>

Checks if an object is included in the Override Group.

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **op** ([*c4d.BaseObject*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object to check.

**Return type:** bool

**Returns:** **True** if the object is included in the Override Group, otherwise **False**.

#### `BaseOverrideGroup.GetObjectsInGroup(self)` <a id="c4d.modules.takesystem.BaseOverrideGroup.GetObjectsInGroup"></a>

Retrieves all the objects in the group.

**Return type:** List[[c4d.BaseList2D](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The objects in the group.

#### `BaseOverrideGroup.GetTake(self)` <a id="c4d.modules.takesystem.BaseOverrideGroup.GetTake"></a>

Returns the Take that owns the Override Group.

**Return type:** [c4d.modules.takesystem.BaseTake](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)

**Returns:** The Take for the Override Group.

#### `BaseOverrideGroup.RemoveFromGroup(self, takeData, node)` <a id="c4d.modules.takesystem.BaseOverrideGroup.RemoveFromGroup"></a>

Removes *node* from the Override Group.

> **Note:** An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see `TakeData.GetUndoState()`/`TakeData.SetUndoState()`).

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **node** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The node to remove. If it is not part of the group the function returns.

### Tag Management <a id="c4d.modules.takesystem.BaseOverrideGroup-method-Tag-Management"></a>

#### `BaseOverrideGroup.AddTag(self, takeData, type, mat)` <a id="c4d.modules.takesystem.BaseOverrideGroup.AddTag"></a>

Adds a new tag of the given *type* to the Override Group if it is not already there.

> **Warning:** Only tags registered with the flag **TAG_ADDTOTAKEGROUP** are accepted by the group.

> **Note:** An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see `TakeData.GetUndoState()`/`TakeData.SetUndoState()`).

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.

- **type** (*int*) –

  The tag type to be added. If the tag is already in the group the function returns.  
  If **Ttexture** the material can be assigned to *mat*.

- **mat** (*Optional*[[*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)]) – The optional material (can be **None**) if passed type is **Ttexture**.

**Return type:** [c4d.BaseTag](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)

**Returns:** The tag. The added one if created by the function or the one already in the group.

#### `BaseOverrideGroup.GetTag(self, type)` <a id="c4d.modules.takesystem.BaseOverrideGroup.GetTag"></a>

Searches for a tag of the given *type* attached to the Override Group.

**Parameters:** **type** (*int*) – The tag type to search for.

**Return type:** Optional[[c4d.BaseTag](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)]

**Returns:** The tag if found, otherwise **None**.

#### `BaseOverrideGroup.RemoveTag(self, takeData, type)` <a id="c4d.modules.takesystem.BaseOverrideGroup.RemoveTag"></a>

Removes the tag of the given *type* from the Override Group.

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **type** (*int*) – The tag type to be removed. If it is not in the Group the function returns.

### Visibility Modes <a id="c4d.modules.takesystem.BaseOverrideGroup-method-Visibility-Modes"></a>

#### `BaseOverrideGroup.GetEditorMode(self)` <a id="c4d.modules.takesystem.BaseOverrideGroup.GetEditorMode"></a>

Returns the editor visibility mode for the Override Group.

**Return type:** int

**Returns:**

The editor mode:

|   |   |
|---|---|
| *MODE_ON* | The object is enabled regardless of the state of any parent object. |
| *MODE_OFF* | The object is disabled regardless of the state of any parent object. |
| *MODE_UNDEF* | The object is enabled by default, but the state of any parent object is used if it is enabled or disabled. |

#### `BaseOverrideGroup.GetRenderMode(self)` <a id="c4d.modules.takesystem.BaseOverrideGroup.GetRenderMode"></a>

Returns the render visibility mode for the Override Group.

**Return type:** int

**Returns:**

The render mode:

|   |   |
|---|---|
| *MODE_ON* | The object is enabled regardless of the state of any parent object. |
| *MODE_OFF* | The object is disabled regardless of the state of any parent object. |
| *MODE_UNDEF* | The object is enabled by default, but the state of any parent object is used if it is enabled or disabled. |

#### `BaseOverrideGroup.SetEditorMode(self, mode)` <a id="c4d.modules.takesystem.BaseOverrideGroup.SetEditorMode"></a>

Sets the editor visibility mode for the Override Group.

**Parameters:**

**type** (*int*) –

The editor mode to set:

|   |   |
|---|---|
| *MODE_ON* | The object is enabled regardless of the state of any parent object. |
| *MODE_OFF* | The object is disabled regardless of the state of any parent object. |
| *MODE_UNDEF* | The object is enabled by default, but the state of any parent object is used if it is enabled or disabled. |

#### `BaseOverrideGroup.SetRenderMode(self, mode)` <a id="c4d.modules.takesystem.BaseOverrideGroup.SetRenderMode"></a>

Sets the render visibility mode for the Override Group.

**Parameters:**

**type** (*int*) –

The render mode to set:

|   |   |
|---|---|
| *MODE_ON* | The object is enabled regardless of the state of any parent object. |
| *MODE_OFF* | The object is disabled regardless of the state of any parent object. |
| *MODE_UNDEF* | The object is enabled by default, but the state of any parent object is used if it is enabled or disabled. |
