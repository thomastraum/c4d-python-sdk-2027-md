<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/character/builder/index.html -->

# c4d.modules.character.builder <a id="c4d-modules-character-builder"></a>

## *class* `c4d.modules.character.builder` <a id="c4d.modules.character.builder"></a>

## Constants <a id="constants"></a>

> **Note:** These constants are defined in the c4d.modules.character.builder module so **c4d.modules.character.builder.COMPONENT_OBJECT_GETOBJECTS_TYPE_ALL** should be used and not **c4d.COMPONENT_OBJECT_GETOBJECTS_TYPE_ALL**.

| Symbol ID | Description |
|---|---|
| ID_CA_CHARACTER_MODE_BUILD | Build Mode. |
| ID_CA_CHARACTER_MODE_ADJUST | Adjust Mode. |
| ID_CA_CHARACTER_MODE_BIND | Bind Mode. |
| ID_CA_CHARACTER_MODE_ANIMATE | Animate Mode. |

> **Note:** These constants are defined in the c4d.modules.character.builder module so **c4d.modules.character.builder.COMPONENT_OBJECT_GETOBJECTS_TYPE_ALL** should be used and not **c4d.COMPONENT_OBJECT_GETOBJECTS_TYPE_ALL**.

| Symbol ID | Description |
|---|---|
| COMPONENT_OBJECT_GETOBJECTS_TYPE_ALL | All objects. |
| COMPONENT_OBJECT_GETOBJECTS_TYPE_INCLUDED | Included objects. |
| COMPONENT_OBJECT_GETOBJECTS_TYPE_MAIN | Direct Child objects. |
| COMPONENT_SELECTION_MODES_UVEDGES | *New in version S22:* UV Edges selection mode. |

- [`c4d.modules.character.builder.CharacterObject`](CharacterObject/index.md#c4d.modules.character.builder.CharacterObject)
- [`c4d.modules.character.builder.Component`](Component/index.md#c4d.modules.character.builder.Component)
- [`c4d.modules.character.builder.ComponentObject`](ComponentObject/index.md#c4d.modules.character.builder.ComponentObject)
- [`c4d.modules.character.builder.Template`](Template/index.md#c4d.modules.character.builder.Template)

## Overview <a id="overview"></a>

**Builder Component Management**

- [`c4d.modules.character.builder.GetComponentFlags()`](#c4d.modules.character.builder.GetComponentFlags): Get component flags from an object/tag.

**Include Container Management**

- [`c4d.modules.character.builder.AddIncludeObject()`](#c4d.modules.character.builder.AddIncludeObject): Add object to include container.
- [`c4d.modules.character.builder.FindIncludeObject()`](#c4d.modules.character.builder.FindIncludeObject): Find object in include container.
- [`c4d.modules.character.builder.RemoveIncludeObject()`](#c4d.modules.character.builder.RemoveIncludeObject): Remove object from include container

## Members <a id="members"></a>

### Builder Component Management <a id="c4d.modules.character.builder-function-Builder-Component-Management"></a>

#### `c4d.modules.character.builder.GetComponentFlags(bl)` <a id="c4d.modules.character.builder.GetComponentFlags"></a>

Get component flags from an object/tag.

**Parameters:** **bl** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The Component.

**Return type:** int

**Returns:**

Type of object:

| Value | Description |
|---|---|
| 0 | None. |
| 1 | A Component. |
| 2 | An Object. |
| 4 | A Node Object. |
| 8 | A Root. |
| 16 | A Template. |
| 32 | A Controller. |
| 64 | A Character. |
| 128 | A Group. |
| 256 | A main component. |

### Include Container Management <a id="c4d.modules.character.builder-function-Include-Container-Management"></a>

#### `c4d.modules.character.builder.AddIncludeObject(iincdata, op, flags)` <a id="c4d.modules.character.builder.AddIncludeObject"></a>

Add object to include container.

**Parameters:**

- **iincdata** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) –

  All objects that will be included where each entry is a BaseLink to the object and the index is an integer corresponding to the InExcludeData flags:

  | Value | Description |
  |---|---|
  | 1 | Hierarchy. |
  | 2 | Sharing. |
  | 4 | Self-Sharing. |

- **op** ([*c4d.BaseObject*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object where need to be inserted.

- **flags** (*int*) – The bitmap. Will be copied.

**Return type:** int

**Returns:** **1** if success, otherwise **0**.

#### `c4d.modules.character.builder.FindIncludeObject(incdata, name)` <a id="c4d.modules.character.builder.FindIncludeObject"></a>

Find object in include container.

**Parameters:**

- **iincdata** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) –

  All objects that will be included where each entry is a BaseLink to the object and the index is an integer corresponding to the InExcludeData flags:

  | Value | Description |
  |---|---|
  | 1 | Hierarchy. |
  | 2 | Sharing. |
  | 4 | Self-Sharing. |

- **name** (*string*) – The name to match .

**Return type:** int

**Returns:** **1** if a match is found, otherwise **0**.

#### `c4d.modules.character.builder.RemoveIncludeObject(incdata, name)` <a id="c4d.modules.character.builder.RemoveIncludeObject"></a>

Remove object from include container

**Parameters:**

- **iincdata** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – All objects that are included.
- **name** (*string*) – The object name to remove.

**Return type:** int

**Returns:** **1** if the matching object found is deleted, otherwise **0**.
