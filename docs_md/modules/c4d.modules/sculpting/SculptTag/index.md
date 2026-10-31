<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/sculpting/SculptTag/index.html -->

# c4d.modules.sculpting.SculptTag <a id="c4d-modules-sculpting-sculpttag"></a>

## *class* `c4d.modules.sculpting.SculptTag` <a id="c4d.modules.sculpting.SculptTag"></a>

When a [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) is made sculptable it will contain a [`SculptTag`](#c4d.modules.sculpting.SculptTag).  
Each [`SculptTag`](#c4d.modules.sculpting.SculptTag) references a [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject) in the Document.  
This [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject) contains all the layers and offsets used by the sculpt tools.

*New in version R15.037.*

> **Warning:**
>
> The class [`SculptTag`](#c4d.modules.sculpting.SculptTag) cannot be instantiated.  
> [`MakeSculptObject()`](../index.md#c4d.modules.sculpting.MakeSculptObject) function should be used instead.

Parent Class:

- [`c4d.BaseTag`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)

## Overview <a id="overview"></a>

- [`SculptTag.GetSculptObject()`](#c4d.modules.sculpting.SculptTag.GetSculptObject): Get the [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject) for this [`SculptTag`](#c4d.modules.sculpting.SculptTag).

## Members <a id="members"></a>

### Sculpt Object Access <a id="c4d.modules.sculpting.SculptTag-method-Sculpt-Object-Access"></a>

#### `SculptTag.GetSculptObject(self)` <a id="c4d.modules.sculpting.SculptTag.GetSculptObject"></a>

Get the [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject) for this [`SculptTag`](#c4d.modules.sculpting.SculptTag).

**Return type:** [c4d.modules.sculpting.SculptObject](../SculptObject/index.md#c4d.modules.sculpting.SculptObject)

**Returns:** The [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject) that this tag references.
