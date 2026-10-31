<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/thinkingparticles/TP_PGroup/index.html -->

# c4d.modules.thinkingparticles.TP_PGroup <a id="c4d-modules-thinkingparticles-tp-pgroup"></a>

## *class* `c4d.modules.thinkingparticles.TP_PGroup` <a id="c4d.modules.thinkingparticles.TP_PGroup"></a>

Represents a Thinking Particle group.

Parent Class:

- [`c4d.BaseList2D`](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

## Overview <a id="overview"></a>

**Display Settings**

- [`TP_PGroup.GetColor()`](#c4d.modules.thinkingparticles.TP_PGroup.GetColor): Returns the color of the group.
- [`TP_PGroup.GetShowObjects()`](#c4d.modules.thinkingparticles.TP_PGroup.GetShowObjects): Returns the show-objects flag of the group.
- [`TP_PGroup.GetUseColor()`](#c4d.modules.thinkingparticles.TP_PGroup.GetUseColor): Gets the use color state of the group.
- [`TP_PGroup.GetViewType()`](#c4d.modules.thinkingparticles.TP_PGroup.GetViewType): Returns the group view type.
- [`TP_PGroup.SetColor()`](#c4d.modules.thinkingparticles.TP_PGroup.SetColor): Sets the color of the group.
- [`TP_PGroup.SetShowObjects()`](#c4d.modules.thinkingparticles.TP_PGroup.SetShowObjects): Sets the show-objects flag of the group.
- [`TP_PGroup.SetUseColor()`](#c4d.modules.thinkingparticles.TP_PGroup.SetUseColor): Sets the use color state of the group.
- [`TP_PGroup.SetViewType()`](#c4d.modules.thinkingparticles.TP_PGroup.SetViewType): Sets the group view type.

**Group Metadata**

- [`TP_PGroup.GetTitle()`](#c4d.modules.thinkingparticles.TP_PGroup.GetTitle): Returns the group title.
- [`TP_PGroup.SetTitle()`](#c4d.modules.thinkingparticles.TP_PGroup.SetTitle): Sets the group title.

**Hierarchy And Membership**

- [`TP_PGroup.GetGroupID()`](#c4d.modules.thinkingparticles.TP_PGroup.GetGroupID): Returns the ID of the group.
- [`TP_PGroup.GetLevel()`](#c4d.modules.thinkingparticles.TP_PGroup.GetLevel): Calculates the level of this group.
- [`TP_PGroup.GetParticles()`](#c4d.modules.thinkingparticles.TP_PGroup.GetParticles): Returns the particles which belong to this group.
- [`TP_PGroup.IsSubGroup()`](#c4d.modules.thinkingparticles.TP_PGroup.IsSubGroup): Checks if *group* is a subgroup of the group.
- [`TP_PGroup.NumParticles()`](#c4d.modules.thinkingparticles.TP_PGroup.NumParticles): Returns the count of particles which belong to this group.

**List Interaction**

- [`TP_PGroup.EditSettings()`](#c4d.modules.thinkingparticles.TP_PGroup.EditSettings): Opens the edit dialog for the group.
- [`TP_PGroup.IsOpened()`](#c4d.modules.thinkingparticles.TP_PGroup.IsOpened): Checks if the group is opened in the group list.
- [`TP_PGroup.IsSelected()`](#c4d.modules.thinkingparticles.TP_PGroup.IsSelected): Checks if the group is selected in the group list.
- [`TP_PGroup.Open()`](#c4d.modules.thinkingparticles.TP_PGroup.Open): Opens or closes the group in the group list.
- [`TP_PGroup.Select()`](#c4d.modules.thinkingparticles.TP_PGroup.Select): Sets the selection mode of the group in the group list.

**Particle Caching**

- [`TP_PGroup.Cache()`](#c4d.modules.thinkingparticles.TP_PGroup.Cache): Sets the group to contain only cached data.
- [`TP_PGroup.IsCache()`](#c4d.modules.thinkingparticles.TP_PGroup.IsCache): Checks if the group is used to represent cached particle data only.

## Members <a id="members"></a>

### Display Settings <a id="c4d.modules.thinkingparticles.TP_PGroup-method-Display-Settings"></a>

#### `TP_PGroup.GetColor(self)` <a id="c4d.modules.thinkingparticles.TP_PGroup.GetColor"></a>

Returns the color of the group.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The group color.

#### `TP_PGroup.GetShowObjects(self)` <a id="c4d.modules.thinkingparticles.TP_PGroup.GetShowObjects"></a>

Returns the show-objects flag of the group.

**Return type:** int

**Returns:** The show-objects flag.

#### `TP_PGroup.GetUseColor(self)` <a id="c4d.modules.thinkingparticles.TP_PGroup.GetUseColor"></a>

Gets the use color state of the group.

*New in version R16.038.*

**Return type:** bool

**Returns:** **True** if use color is enabled, otherwise **False**.

#### `TP_PGroup.GetViewType(self)` <a id="c4d.modules.thinkingparticles.TP_PGroup.GetViewType"></a>

Returns the group view type.

**Return type:** int

**Returns:** The group view type.

#### `TP_PGroup.SetColor(self, col)` <a id="c4d.modules.thinkingparticles.TP_PGroup.SetColor"></a>

Sets the color of the group.

**Parameters:** **col** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The new group color.

#### `TP_PGroup.SetShowObjects(self, bool)` <a id="c4d.modules.thinkingparticles.TP_PGroup.SetShowObjects"></a>

Sets the show-objects flag of the group.

**Parameters:** **show** (*bool*) – The new show-objects flag.

#### `TP_PGroup.SetUseColor(self, use)` <a id="c4d.modules.thinkingparticles.TP_PGroup.SetUseColor"></a>

Sets the use color state of the group.

*New in version R16.038.*

**Parameters:** **use** (*bool*) – **True** if use color should be enabled, otherwise **False**.

#### `TP_PGroup.SetViewType(self, type)` <a id="c4d.modules.thinkingparticles.TP_PGroup.SetViewType"></a>

Sets the group view type.

**Parameters:** **title** (*int*) – The new view type. See *PGROUP_VIEWTYPE* in *description/tp_group.h*

### Group Metadata <a id="c4d.modules.thinkingparticles.TP_PGroup-method-Group-Metadata"></a>

#### `TP_PGroup.GetTitle(self)` <a id="c4d.modules.thinkingparticles.TP_PGroup.GetTitle"></a>

Returns the group title.

**Return type:** str

**Returns:** The group title.

#### `TP_PGroup.SetTitle(self, title)` <a id="c4d.modules.thinkingparticles.TP_PGroup.SetTitle"></a>

Sets the group title.

**Parameters:** **title** (*str*) – The new group title.

### Hierarchy And Membership <a id="c4d.modules.thinkingparticles.TP_PGroup-method-Hierarchy-And-Membership"></a>

#### `TP_PGroup.GetGroupID(self)` <a id="c4d.modules.thinkingparticles.TP_PGroup.GetGroupID"></a>

Returns the ID of the group. This is only based on the order in the group list, so it can change when the user reorders the groups.

**Return type:** int

**Returns:** The group ID.

#### `TP_PGroup.GetLevel(self)` <a id="c4d.modules.thinkingparticles.TP_PGroup.GetLevel"></a>

Calculates the level of this group. This is the number of parents that the group has.

**Return type:** int

**Returns:** The group level.

#### `TP_PGroup.GetParticles(self)` <a id="c4d.modules.thinkingparticles.TP_PGroup.GetParticles"></a>

Returns the particles which belong to this group.

**Return type:** List[int]

**Returns:** The particles.

#### `TP_PGroup.IsSubGroup(self, group)` <a id="c4d.modules.thinkingparticles.TP_PGroup.IsSubGroup"></a>

Checks if *group* is a subgroup of the group.

**Parameters:** **group** ([*c4d.modules.thinkingparticles.TP_PGroup*](#c4d.modules.thinkingparticles.TP_PGroup)) – A TP particle group.

**Return type:** bool

**Returns:** **True** if *group* is a subgroup of the group, otherwise **False**.

#### `TP_PGroup.NumParticles(self)` <a id="c4d.modules.thinkingparticles.TP_PGroup.NumParticles"></a>

Returns the count of particles which belong to this group.

**Return type:** int

**Returns:** The number of particles.

### List Interaction <a id="c4d.modules.thinkingparticles.TP_PGroup-method-List-Interaction"></a>

#### `TP_PGroup.EditSettings(self)` <a id="c4d.modules.thinkingparticles.TP_PGroup.EditSettings"></a>

Opens the edit dialog for the group.

**Return type:** bool

**Returns:** **True** if the user clicked *OK*, otherwise **False**.

#### `TP_PGroup.IsOpened(self)` <a id="c4d.modules.thinkingparticles.TP_PGroup.IsOpened"></a>

Checks if the group is opened in the group list.

**Return type:** bool

**Returns:** **True** if the group is opened, otherwise **False** if it is closed.

#### `TP_PGroup.IsSelected(self)` <a id="c4d.modules.thinkingparticles.TP_PGroup.IsSelected"></a>

Checks if the group is selected in the group list.

**Return type:** bool

**Returns:** **True** if the group is selected, otherwise **False**.

#### `TP_PGroup.Open(self, onoff)` <a id="c4d.modules.thinkingparticles.TP_PGroup.Open"></a>

Opens or closes the group in the group list.

**Parameters:** **onoff** (*bool*) – **True** if the group should be opened, otherwise **False** if it should be closed.

#### `TP_PGroup.Select(self, mode)` <a id="c4d.modules.thinkingparticles.TP_PGroup.Select"></a>

Sets the selection mode of the group in the group list.

**Parameters:**

**mode** (*int*) –

The selection mode:

|   |   |
|---|---|
| *SELECTION_NEW* | Starts a new selection. |
| *SELECTION_ADD* | Adds to the current selection |
| *SELECTION_SUB* | Subtracts from the current selection. |

### Particle Caching <a id="c4d.modules.thinkingparticles.TP_PGroup-method-Particle-Caching"></a>

#### `TP_PGroup.Cache(self, onoff)` <a id="c4d.modules.thinkingparticles.TP_PGroup.Cache"></a>

Sets the group to contain only cached data. This will prevent the particle system from doing simulation calculations for the group.

*New in version R16.050.*

**Parameters:** **onoff** (*bool*) – **True** if cached data is used, otherwise **False**.

#### `TP_PGroup.IsCache(self)` <a id="c4d.modules.thinkingparticles.TP_PGroup.IsCache"></a>

Checks if the group is used to represent cached particle data only.

*New in version R16.050.*

**Return type:** bool

**Returns:** **True** if the group represents cached data, otherwise **False**.
