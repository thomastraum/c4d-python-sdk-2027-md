<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/character/builder/Template/index.html -->

# c4d.modules.character.builder.Template <a id="c4d-modules-character-builder-template"></a>

## *class* `c4d.modules.character.builder.Template` <a id="c4d.modules.character.builder.Template"></a>

## Overview <a id="overview"></a>

- [`Template.FindComponent()`](#c4d.modules.character.builder.Template.FindComponent): Find component within template.
- [`Template.FindObject()`](#c4d.modules.character.builder.Template.FindObject): Find object within template.
- [`Template.GetDocument()`](#c4d.modules.character.builder.Template.GetDocument): Get the template BaseDocument.

## Members <a id="members"></a>

### Template Access <a id="c4d.modules.character.builder.Template-method-Template-Access"></a>

#### `Template.FindComponent(self, name, ident)` <a id="c4d.modules.character.builder.Template.FindComponent"></a>

Find component within template.

**Parameters:**

- **name** (*str*) – The component name to search for.
- **ident** (*bool*) – If **true**, matches name and unique id string.

**Return type:** Optional[[c4d.modules.character.builder.Component](../Component/index.md#c4d.modules.character.builder.Component)]

**Returns:** The found component or **None**.

#### `Template.FindObject(self, name)` <a id="c4d.modules.character.builder.Template.FindObject"></a>

Find object within template.

**Parameters:** **name** (*str*) – The component name to search for.

**Return type:** Optional[[c4d.BaseObject](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The found object or **None**.

#### `Template.GetDocument(self)` <a id="c4d.modules.character.builder.Template.GetDocument"></a>

Get the template BaseDocument.

**Return type:** [c4d.documents.BaseDocument](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)

**Returns:** The document.
