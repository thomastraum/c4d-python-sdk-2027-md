<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/takesystem/BaseOverride/index.html -->

# c4d.modules.takesystem.BaseOverride <a id="c4d-modules-takesystem-baseoverride"></a>

## *class* `c4d.modules.takesystem.BaseOverride` <a id="c4d.modules.takesystem.BaseOverride"></a>

An Override holds the settings for a specific object in a Take.

> **Warning:** This type cannot be instantiated.

*New in version R17.032.*

Parent Class:

- [`c4d.BaseList2D`](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

## Overview <a id="overview"></a>

**Ownership And Grouping**

- [`BaseOverride.GetOwnerTake()`](#c4d.modules.takesystem.BaseOverride.GetOwnerTake): Gets the Take that owns the Override.
- [`BaseOverride.GetSceneNode()`](#c4d.modules.takesystem.BaseOverride.GetSceneNode): Retrieves the original scene node connected to the Override node.
- [`BaseOverride.IsInGroup()`](#c4d.modules.takesystem.BaseOverride.IsInGroup): Checks if the Override is also part of an Override Group, and if yes returns the group.

**Parameter Management**

- [`BaseOverride.GetAllOverrideDescID()`](#c4d.modules.takesystem.BaseOverride.GetAllOverrideDescID): Retrieves the DescID of all parameters in the Override.
- [`BaseOverride.IsOverriddenParam()`](#c4d.modules.takesystem.BaseOverride.IsOverriddenParam): Checks if the parameter at *descID* is overridden.
- [`BaseOverride.UpdateSceneNode()`](#c4d.modules.takesystem.BaseOverride.UpdateSceneNode): Updates the scene node whenever data is directly changed on the base Override (for example with `C4DAtom.SetParameter()`).

## Members <a id="members"></a>

### Ownership And Grouping <a id="c4d.modules.takesystem.BaseOverride-method-Ownership-And-Grouping"></a>

#### `BaseOverride.GetOwnerTake(self, takeData)` <a id="c4d.modules.takesystem.BaseOverride.GetOwnerTake"></a>

Gets the Take that owns the Override.

**Parameters:** **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.

**Return type:** [c4d.modules.takesystem.BaseTake](../BaseTake/index.md#c4d.modules.takesystem.BaseTake)

**Returns:** The Take for the Override.

#### `BaseOverride.GetSceneNode(self)` <a id="c4d.modules.takesystem.BaseOverride.GetSceneNode"></a>

Retrieves the original scene node connected to the Override node.

**Return type:** [c4d.BaseList2D](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

**Returns:** The original scene node.

#### `BaseOverride.IsInGroup(self, takeData)` <a id="c4d.modules.takesystem.BaseOverride.IsInGroup"></a>

Checks if the Override is also part of an Override Group, and if yes returns the group.

**Parameters:** **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.

**Return type:** Tuple[bool, [c4d.modules.takesystem.BaseOverrideGroup](../BaseOverrideGroup/index.md#c4d.modules.takesystem.BaseOverrideGroup)]

**Returns:** **True** if the Override is part of an Override Group, otherwise **False**.

### Parameter Management <a id="c4d.modules.takesystem.BaseOverride-method-Parameter-Management"></a>

#### `BaseOverride.GetAllOverrideDescID(self)` <a id="c4d.modules.takesystem.BaseOverride.GetAllOverrideDescID"></a>

Retrieves the DescID of all parameters in the Override.

> **Note:** Sub-descriptions are included if overridden.

**Return type:** List[[c4d.DescID](../../../c4d/DescID/index.md#c4d.DescID)]

**Returns:** The DescID of all overridden parameters.

#### `BaseOverride.IsOverriddenParam(self, descID)` <a id="c4d.modules.takesystem.BaseOverride.IsOverriddenParam"></a>

Checks if the parameter at *descID* is overridden.

**Parameters:** **descID** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The parameter to be checked.

**Return type:** bool

**Returns:** **True** if parameter is overridden, otherwise **False**.

#### `BaseOverride.UpdateSceneNode(self, takeData, descID)` <a id="c4d.modules.takesystem.BaseOverride.UpdateSceneNode"></a>

Updates the scene node whenever data is directly changed on the base Override (for example with `C4DAtom.SetParameter()`).  
This ensures the scene node is properly updated if the Override affects the current document state.

> **Note:** An undo step is added automatically if the call is added from the main (GUI) thread and global undo is allowed (see `TakeData.GetUndoState()`/`TakeData.SetUndoState()`).

**Parameters:**

- **takeData** ([*c4d.modules.takesystem.TakeData*](../TakeData/index.md#c4d.modules.takesystem.TakeData)) – The Take System context.
- **descID** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The edited parameter.
