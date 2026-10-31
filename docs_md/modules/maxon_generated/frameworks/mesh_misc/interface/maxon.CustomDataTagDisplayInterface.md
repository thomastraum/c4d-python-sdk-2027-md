<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/mesh_misc/interface/maxon.CustomDataTagDisplayInterface.html -->

# maxon.CustomDataTagDisplayInterface <a id="maxon-customdatatagdisplayinterface"></a>

## Description <a id="module-maxon.CustomDataTagDisplayInterface"></a><a id="description"></a>

[`maxon.CustomDataTagDisplayInterface`](#module-maxon.CustomDataTagDisplayInterface) can be optionally implemented for each [`maxon.CustomDataTagClassInterface`](maxon.CustomDataTagClassInterface.md#module-maxon.CustomDataTagClassInterface) implementation and defines if and how a `c4d.CustomDataTag` should be displayed in the viewport.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.CustomDataTagDisplayRef`](../reference/maxon.CustomDataTagDisplayRef.md#module-maxon.CustomDataTagDisplayRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Draw`](#maxon.CustomDataTagDisplayInterface.Draw)(tag, op, bd, bh) | Draws the visual representation of the tag data in 3D views. |
| [`FreeDisplayControl`](#maxon.CustomDataTagDisplayInterface.FreeDisplayControl)(tag) | Frees resources allocated by `maxon.CustomDataTagDisplayInterface.InitDisplayControl()`. |
| [`Init`](#maxon.CustomDataTagDisplayInterface.Init)(tag) | Initializes the class after creation. |
| [`Reset`](#maxon.CustomDataTagDisplayInterface.Reset)() | Resets any local data before destroying the class instance. |

## Methods Definition <a id="methods-definition"></a>

### `CustomDataTagDisplayInterface.Draw(tag, op, bd, bh)` <a id="maxon.CustomDataTagDisplayInterface.Draw"></a>

Draws the visual representation of the tag data in 3D views.

> **Note:**
>
> This function is called in a thread context. See the important information about threading.  
> To get the current drawpass call `BaseDraw.GetDrawPass()`.

**Parameters:**

- **tag** ([`c4d.BaseTag`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)) – The BaseTag connected with the TagData instance.
- **op** ([`c4d.BaseObject`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The host object of the tag. Cinema 4D owns the pointed object.
- **bd** ([`c4d.BaseDraw`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The editor’s view. The caller owns the pointed view.
- **bh** (`c4d.BaseDrawHelp`) – The helper for the editor’s view. The caller owns the pointed view helper.

### `CustomDataTagDisplayInterface.FreeDisplayControl(tag)` <a id="maxon.CustomDataTagDisplayInterface.FreeDisplayControl"></a>

Frees resources allocated by `maxon.CustomDataTagDisplayInterface.InitDisplayControl()`.

**Parameters:** **tag** ([`c4d.BaseTag`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)) – The BaseTag connected with the TagData instance.

### `CustomDataTagDisplayInterface.Init(tag)` <a id="maxon.CustomDataTagDisplayInterface.Init"></a>

Initializes the class after creation.

**Parameters:** **tag** ([`c4d.BaseTag`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)) – The tag that owns the attributes.

### `CustomDataTagDisplayInterface.Reset()` <a id="maxon.CustomDataTagDisplayInterface.Reset"></a>

Resets any local data before destroying the class instance.
