<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/DescLevel/index.html -->

# c4d.DescLevel <a id="c4d-desclevel"></a>

## *class* `c4d.DescLevel` <a id="c4d.DescLevel"></a>

Represents a level within a [`DescID`](../DescID/index.md#c4d.DescID).

**Attributes**

## `c4d.DescLevel.id` <a id="c4d.DescLevel.id"></a>

ID of this level.

**Type:** int

## `c4d.DescLevel.dtype` <a id="c4d.DescLevel.dtype"></a>

Datatype. Either a custom ID or one of these:

|   |   |
|---|---|
| *DTYPE_NONE* | None. |
| *DTYPE_CHILDREN* | Children. |
| *DTYPE_GROUP* | Group. |
| *DTYPE_COLOR* | Color. |
| *DTYPE_SUBCONTAINER* | [`BaseContainer`](../BaseContainer/index.md#c4d.BaseContainer). |
| *DTYPE_MULTIPLEDATA* | Multiple data entry. |
| *DTYPE_TEXTURE* | Texture name. |
| *DTYPE_BUTTON* | Button. |
| *DTYPE_DYNAMIC* | GV dynamic. |
| *DTYPE_SEPARATOR* | Separator. |
| *DTYPE_STATICTEXT* | Static text. |
| *DTYPE_POPUP* | Popup. |
| *DTYPE_LONG* | Integer. |
| *DTYPE_REAL* | Float. |
| *DTYPE_TIME* | [`BaseTime`](../BaseTime/index.md#c4d.BaseTime). |
| *DTYPE_VECTOR* | [`Vector`](../Vector/index.md#c4d.Vector). |
| *DTYPE_MATRIX* | [`Matrix`](../Matrix/index.md#c4d.Matrix). |
| *DTYPE_STRING* | String. |
| *DTYPE_FILENAME* | String. |
| *DTYPE_BASELISTLINK* | [`BaseList2D`](../C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D). |
| *DTYPE_BOOL* | GV bool *ID_GV_DATA_TYPE_BOOL*. |
| *DTYPE_NORMAL* | GV normal *ID_GV_DATA_TYPE_NORMAL*. |
| *DTYPE_COLORA* | Color with Alpha. |
| *DTYPE_VECTOR4D* | Vector with 4 components. |

## `c4d.DescLevel.creator` <a id="c4d.DescLevel.creator"></a>

Creator ID.

**Type:** int

## Overview <a id="overview"></a>

- [`DescLevel.__eq__()`](#c4d.DescLevel.__eq__): Checks if all specified values are equal to the values in *other*.
- [`DescLevel.__init__()`](#c4d.DescLevel.__init__): Constructor, specifying the values.
- [`DescLevel.__ne__()`](#c4d.DescLevel.__ne__): The reverse of `__eq__()`.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.DescLevel-method-Magic-Methods"></a>

#### `DescLevel.__eq__(self, other)` <a id="c4d.DescLevel.__eq__"></a>

Checks if all specified values are equal to the values in *other*.

#### `DescLevel.__init__(self, t_id, t_datatype=None, t_creator=None)` <a id="c4d.DescLevel.__init__"></a>

Constructor, specifying the values.

**Parameters:**

- **t_id** (*int*) – Initial value for *id*.
- **t_datatype** (*Optional*[*int*]) – Initial value for *dtype*.
- **t_creator** (*Optional*[*int*]) – Initial value for *creator*.

#### `DescLevel.__ne__(self, other)` <a id="c4d.DescLevel.__ne__"></a>

The reverse of [`__eq__()`](#c4d.DescLevel.__eq__).
