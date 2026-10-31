<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/character/builder/ComponentObject/index.html -->

# c4d.modules.character.builder.ComponentObject <a id="c4d-modules-character-builder-componentobject"></a>

## *class* `c4d.modules.character.builder.ComponentObject` <a id="c4d.modules.character.builder.ComponentObject"></a>

## Overview <a id="overview"></a>

**Component Access**

- [`ComponentObject.GetComponent()`](#c4d.modules.character.builder.ComponentObject.GetComponent): Get the component.
- [`ComponentObject.GetName()`](#c4d.modules.character.builder.ComponentObject.GetName): Get the component’s name.
- [`ComponentObject.GetTag()`](#c4d.modules.character.builder.ComponentObject.GetTag): Get the component tag for this component.

**Component Search**

- [`ComponentObject.CountComponent()`](#c4d.modules.character.builder.ComponentObject.CountComponent): Count child components.
- [`ComponentObject.FindComponent()`](#c4d.modules.character.builder.ComponentObject.FindComponent): Find a specific child component by name.

**Hierarchy Navigation**

- [`ComponentObject.GetDown()`](#c4d.modules.character.builder.ComponentObject.GetDown): Get the main object of the first child component.
- [`ComponentObject.GetNext()`](#c4d.modules.character.builder.ComponentObject.GetNext): Get the main object of the next component.
- [`ComponentObject.GetPrev()`](#c4d.modules.character.builder.ComponentObject.GetPrev): Get the main object of the previous component.
- [`ComponentObject.GetUp()`](#c4d.modules.character.builder.ComponentObject.GetUp): Get the main object of the parent component.

**Object Access**

- [`ComponentObject.FindObject()`](#c4d.modules.character.builder.ComponentObject.FindObject): Find an object within the component by name.
- [`ComponentObject.GetObject()`](#c4d.modules.character.builder.ComponentObject.GetObject): Get the main object of the component.
- [`ComponentObject.GetObjects()`](#c4d.modules.character.builder.ComponentObject.GetObjects): Get a container with all the objects for this component.

## Members <a id="members"></a>

### Component Access <a id="c4d.modules.character.builder.ComponentObject-method-Component-Access"></a>

#### `ComponentObject.GetComponent(self)` <a id="c4d.modules.character.builder.ComponentObject.GetComponent"></a>

Get the component.

**Return type:** [c4d.modules.character.builder.Component](../Component/index.md#c4d.modules.character.builder.Component)

**Returns:** The related component.

#### `ComponentObject.GetName(self, ident)` <a id="c4d.modules.character.builder.ComponentObject.GetName"></a>

Get the component’s name.

**Parameters:** **ident** (*bool*) – If **true**, displays name and unique identifier.

**Return type:** str

**Returns:** The name.

#### `ComponentObject.GetTag(self)` <a id="c4d.modules.character.builder.ComponentObject.GetTag"></a>

Get the component tag for this component.

**Return type:** [c4d.BaseTag](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)

**Returns:** The component tag.

### Component Search <a id="c4d.modules.character.builder.ComponentObject-method-Component-Search"></a>

#### `ComponentObject.CountComponent(self, name, ident, mirrored, down)` <a id="c4d.modules.character.builder.ComponentObject.CountComponent"></a>

Count child components.

**Parameters:**

- **name** (*str*) – String to match.
- **ident** (*bool*) – If **true**, displays name and unique identifier.
- **mirrored** (*bool*) – If **true**, matches only mirrored components.
- **down** (*bool*) – If **true**, matches recursively (includes children).

**Return type:** int

**Returns:** Number of matches.

#### `ComponentObject.FindComponent(self, name, ident, mirrored, down)` <a id="c4d.modules.character.builder.ComponentObject.FindComponent"></a>

Find a specific child component by name.

**Parameters:**

- **name** (*str*) – String to match.
- **ident** (*bool*) – If **true**, displays name and unique identifier.
- **mirrored** (*bool*) – If **true**, matches only mirrored components.
- **down** (*bool*) – If **true**, matches recursively (includes children).

**Return type:** [c4d.modules.character.builder.ComponentObject](#c4d.modules.character.builder.ComponentObject)

**Returns:** The first matched object.

### Hierarchy Navigation <a id="c4d.modules.character.builder.ComponentObject-method-Hierarchy-Navigation"></a>

#### `ComponentObject.GetDown(self)` <a id="c4d.modules.character.builder.ComponentObject.GetDown"></a>

Get the main object of the first child component.

**Return type:** Optional[[c4d.BaseObject](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The main object of the first child component.

#### `ComponentObject.GetNext(self)` <a id="c4d.modules.character.builder.ComponentObject.GetNext"></a>

Get the main object of the next component.

**Return type:** Optional[[c4d.BaseObject](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The main object of the next component.

#### `ComponentObject.GetPrev(self)` <a id="c4d.modules.character.builder.ComponentObject.GetPrev"></a>

Get the main object of the previous component.

**Return type:** Optional[[c4d.BaseObject](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The main object of the previous component.

#### `ComponentObject.GetUp(self)` <a id="c4d.modules.character.builder.ComponentObject.GetUp"></a>

Get the main object of the parent component.

**Return type:** Optional[[c4d.BaseObject](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The main object of the parent component.

### Object Access <a id="c4d.modules.character.builder.ComponentObject-method-Object-Access"></a>

#### `ComponentObject.FindObject(self, name)` <a id="c4d.modules.character.builder.ComponentObject.FindObject"></a>

Find an object within the component by name.

**Parameters:** **name** (*str*) – String to match.

**Return type:** [c4d.BaseObject](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

**Returns:** The first matched object.

#### `ComponentObject.GetObject(self)` <a id="c4d.modules.character.builder.ComponentObject.GetObject"></a>

Get the main object of the component.

**Return type:** [c4d.BaseObject](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

**Returns:** The related object.

#### `ComponentObject.GetObjects(self, type)` <a id="c4d.modules.character.builder.ComponentObject.GetObjects"></a>

Get a container with all the objects for this component.

**Parameters:**

**type** (*int*) –

Indicates which objects to get:

> **Note:** These constants are defined in the c4d.modules.character.builder module so **c4d.modules.character.builder.COMPONENT_OBJECT_GETOBJECTS_TYPE_ALL** should be used and not **c4d.COMPONENT_OBJECT_GETOBJECTS_TYPE_ALL**.

| Symbol ID | Description |
|---|---|
| COMPONENT_OBJECT_GETOBJECTS_TYPE_ALL | All objects. |
| COMPONENT_OBJECT_GETOBJECTS_TYPE_INCLUDED | Included objects. |
| COMPONENT_OBJECT_GETOBJECTS_TYPE_MAIN | Direct Child objects. |
| COMPONENT_SELECTION_MODES_UVEDGES | *New in version S22:* UV Edges selection mode. |

**Return type:** [c4d.BaseContainer](../../../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The BaseContainer filled with object links.
