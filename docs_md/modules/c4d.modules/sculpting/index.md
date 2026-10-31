<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/sculpting/index.html -->

# c4d.modules.sculpting <a id="c4d-modules-sculpting"></a>

## *class* `c4d.modules.sculpting` <a id="c4d.modules.sculpting"></a>

*New in version R15.037.*

- [`c4d.modules.sculpting.BrushDabData`](BrushDabData/index.md#c4d.modules.sculpting.BrushDabData)

- [`c4d.modules.sculpting.SculptBrushParams`](SculptBrushParams/index.md#c4d.modules.sculpting.SculptBrushParams)

- [`c4d.modules.sculpting.SculptLayerBase`](SculptLayerBase/index.md#c4d.modules.sculpting.SculptLayerBase)

  - [`c4d.modules.sculpting.SculptFolder`](SculptFolder/index.md#c4d.modules.sculpting.SculptFolder)
  - [`c4d.modules.sculpting.SculptLayer`](SculptLayer/index.md#c4d.modules.sculpting.SculptLayer)

- [`c4d.modules.sculpting.SculptLayerData`](SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData)

- [`c4d.modules.sculpting.SculptModifierInterface`](SculptModifierInterface/index.md#c4d.modules.sculpting.SculptModifierInterface)

- [`c4d.modules.sculpting.SculptObject`](SculptObject/index.md#c4d.modules.sculpting.SculptObject)

- [`c4d.modules.sculpting.SculptTag`](SculptTag/index.md#c4d.modules.sculpting.SculptTag)

- [`c4d.plugins.SculptBrushToolData`](../../c4d.plugins/BaseData/SculptBrushToolData/index.md#c4d.plugins.SculptBrushToolData)

## Overview <a id="overview"></a>

- [`c4d.modules.sculpting.GetSelectedSculptObject()`](#c4d.modules.sculpting.GetSelectedSculptObject): Gets the currently selected `SculptObject` in the document.
- [`c4d.modules.sculpting.MakeSculptObject()`](#c4d.modules.sculpting.MakeSculptObject): Adds a `SculptTag` to the [`PolygonObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) *obj*.

## Members <a id="members"></a>

### Object Management <a id="c4d.modules.sculpting-function-Object-Management"></a>

#### `c4d.modules.sculpting.GetSelectedSculptObject(doc)` <a id="c4d.modules.sculpting.GetSelectedSculptObject"></a>

Gets the currently selected [`SculptObject`](SculptObject/index.md#c4d.modules.sculpting.SculptObject) in the document.

> **Note:** This will be the first selected [`PolygonObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) that has a [`SculptTag`](SculptTag/index.md#c4d.modules.sculpting.SculptTag).

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to search.

**Return type:** Optional[[`SculptObject`](SculptObject/index.md#c4d.modules.sculpting.SculptObject)]

**Returns:** The currently selected [`SculptObject`](SculptObject/index.md#c4d.modules.sculpting.SculptObject), or **None** if none is selected.

#### `c4d.modules.sculpting.MakeSculptObject(obj, doc)` <a id="c4d.modules.sculpting.MakeSculptObject"></a>

Adds a [`SculptTag`](SculptTag/index.md#c4d.modules.sculpting.SculptTag) to the [`PolygonObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) *obj*.

> **Note:** If one does not exist then return the [`SculptObject`](SculptObject/index.md#c4d.modules.sculpting.SculptObject) that the newly created [`SculptTag`](SculptTag/index.md#c4d.modules.sculpting.SculptTag) references.

**Parameters:**

- **obj** ([*c4d.PolygonObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject)) – The [`PolygonObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) to add the [`SculptTag`](SculptTag/index.md#c4d.modules.sculpting.SculptTag) to.
- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document that *obj* belongs to.

**Return type:** [`SculptObject`](SculptObject/index.md#c4d.modules.sculpting.SculptObject)

**Returns:** The [`SculptObject`](SculptObject/index.md#c4d.modules.sculpting.SculptObject) that the [`SculptTag`](SculptTag/index.md#c4d.modules.sculpting.SculptTag) is referencing.
