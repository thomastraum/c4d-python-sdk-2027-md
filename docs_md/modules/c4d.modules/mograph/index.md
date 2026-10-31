<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/mograph/index.html -->

# c4d.modules.mograph <a id="c4d-modules-mograph"></a>

## *class* `c4d.modules.mograph` <a id="c4d.modules.mograph"></a>

> **Note:** By default, for legacy reason, an effector added programmatically to the scene will use the falloff option. To switch that effector to fields, the effector need to receive a message MSG_MENUPREPARE. This message can be sent with field.Message(c4d.MSG_MENUPREPARE, currentDoc);

**Attributes**

## `c4d.modules.mograph.FIELD_EXECUTION_BLOCK_SIZEf` <a id="c4d.modules.mograph.FIELD_EXECUTION_BLOCK_SIZEf"></a>

> The size of a block that’s executed in an MP environment.  
> For single depth execution a value closer to 1200 is actually more optimal, with one group 600 and from then on for each group depth you can expect a drop of a third.  
> For general usage on current architectures this gives the best balance.

**Type:** Float

> **See also:** [Scripting Elements](../../../manuals/manual_scripting_elements.md)

- [`c4d.modules.mograph.FieldCallerStack`](FieldCallerStack/index.md#c4d.modules.mograph.FieldCallerStack)
- [`c4d.modules.mograph.FieldInfo`](FieldInfo/index.md#c4d.modules.mograph.FieldInfo)
- [`c4d.modules.mograph.FieldInput`](FieldInput/index.md#c4d.modules.mograph.FieldInput)
- [`c4d.modules.mograph.FieldLayer`](FieldLayer/index.md#c4d.modules.mograph.FieldLayer)
- [`c4d.modules.mograph.FieldObject`](FieldObject/index.md#c4d.modules.mograph.FieldObject)
- [`c4d.modules.mograph.FieldOutput`](FieldOutput/index.md#c4d.modules.mograph.FieldOutput)
- [`c4d.modules.mograph.FieldOutputBlock`](FieldOutputBlock/index.md#c4d.modules.mograph.FieldOutputBlock)
- [`c4d.modules.mograph.MoData`](MoData/index.md#c4d.modules.mograph.MoData)

## Overview <a id="overview"></a>

**Clone Selection And Weights**

- [`c4d.modules.mograph.GeGetMoDataSelection()`](#c4d.modules.mograph.GeGetMoDataSelection): Retrieves the MoGraph clones selection.
- [`c4d.modules.mograph.GeGetMoDataWeights()`](#c4d.modules.mograph.GeGetMoDataWeights): Retrieves the MoGraph clones weights.
- [`c4d.modules.mograph.GeSetMoDataSelection()`](#c4d.modules.mograph.GeSetMoDataSelection): Sets the MoGraph clones selection.
- [`c4d.modules.mograph.GeSetMoDataWeights()`](#c4d.modules.mograph.GeSetMoDataWeights): Sets the MoGraph clones weights.

**Data Access And Defaults**

- [`c4d.modules.mograph.GeGetMoData()`](#c4d.modules.mograph.GeGetMoData): Returns the MoGraph data of an object.
- [`c4d.modules.mograph.GetMoDataDefault()`](#c4d.modules.mograph.GetMoDataDefault): Get the default value for the specified `MoData` ID.
- [`c4d.modules.mograph.GetMoDataDefaultType()`](#c4d.modules.mograph.GetMoDataDefaultType): Get the default value for the specified `MoData` ID.

## Members <a id="members"></a>

### Clone Selection And Weights <a id="c4d.modules.mograph-function-Clone-Selection-And-Weights"></a>

#### `c4d.modules.mograph.GeGetMoDataSelection(op)` <a id="c4d.modules.mograph.GeGetMoDataSelection"></a>

Retrieves the MoGraph clones selection.

*New in version R18.020.*

**Parameters:** **op** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – Can be either a MoGraph Selection tag *BaseTag(c4d.Tmgselection)* or an object with a MoGraph Selection tag.

**Return type:** [`c4d.BaseSelect`](../../c4d/BaseSelect/index.md#c4d.BaseSelect)

**Returns:** The clones selection.

#### `c4d.modules.mograph.GeGetMoDataWeights(op)` <a id="c4d.modules.mograph.GeGetMoDataWeights"></a>

Retrieves the MoGraph clones weights.

*New in version R18.020.*

**Parameters:** **op** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – Can be either a MoGraph Weightmap tag *BaseTag(c4d.Tmgweight)* or an object with a MoGraph Weightmap tag.

**Return type:** List[float]

**Returns:** The clones weights.

#### `c4d.modules.mograph.GeSetMoDataSelection(op, selection)` <a id="c4d.modules.mograph.GeSetMoDataSelection"></a>

Sets the MoGraph clones selection.

*New in version R18.039.*

> **Warning:**
>
> Before R21, makes sure to call `C4DAtom.SetDirty()` after any usage of this method to properly updates the mograph object.  
> In R21 this bug was fixed so the next code is no more needed.
>
> ```python
> # mographObject is the host mograph object of the MoGraph Selection tag: BaseTag(c4d.Tmgselection).
> mographObject.SetDirty(c4d.DIRTYFLAGS_DATA)
> mographObject.Message(c4d.MSG_UPDATE)
> ```

**Parameters:**

- **op** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – Can be either a MoGraph Selection tag *BaseTag(c4d.Tmgselection)* or an object with a MoGraph Selection tag.
- **selection** ([*c4d.BaseSelect*](../../c4d/BaseSelect/index.md#c4d.BaseSelect)) – The clones selection to set.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `c4d.modules.mograph.GeSetMoDataWeights(op, weights)` <a id="c4d.modules.mograph.GeSetMoDataWeights"></a>

Sets the MoGraph clones weights.

*New in version R18.039.*

> **Warning:** Before R21, makes sure to call `C4DAtom.SetDirty()` after any usage of this method to properly updates the mograph object. In R21 this bug was fixed so the next code is no more needed.
>
> ```python
> # mographObject is the host mograph object of the MoGraph Weight tag: BaseTag(c4d.Tmgweight).
> # moSelTag is a BaseTag(c4d.Tmgweight)
> moSelTag.SetDirty(c4d.DIRTYFLAGS_DATA)
> mographObject.SetDirty(c4d.DIRTYFLAGS_DATA)
> mographObject.Message(c4d.MSG_UPDATE)
> ```

**Parameters:**

- **op** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – Can be either a MoGraph Weight tag *BaseTag(c4d.Tmgweight)* or an object with a MoGraph Weight tag.
- **weights** (*List*[*float*]) – The clones weights to set.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Data Access And Defaults <a id="c4d.modules.mograph-function-Data-Access-And-Defaults"></a>

#### `c4d.modules.mograph.GeGetMoData(op)` <a id="c4d.modules.mograph.GeGetMoData"></a>

Returns the MoGraph data of an object.

**Parameters:** **op** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object.

**Return type:** [`MoData`](MoData/index.md#c4d.modules.mograph.MoData)

**Returns:** The MoGraph data.

#### `c4d.modules.mograph.GetMoDataDefault(id)` <a id="c4d.modules.mograph.GetMoDataDefault"></a>

Get the default value for the specified [`MoData`](MoData/index.md#c4d.modules.mograph.MoData) ID.

**Parameters:**

**id** (*int*) –

The [`MoData`](MoData/index.md#c4d.modules.mograph.MoData) ID:

|   |   |   |
|---|---|---|
| *MODATA_MATRIX* | [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) | Matrix of the clone. |
| *MODATA_COLOR* | [`Vector`](../../c4d/Vector/index.md#c4d.Vector) | Color of the clone. |
| *MODATA_SIZE* | [`Vector`](../../c4d/Vector/index.md#c4d.Vector) | Size of the clone. |
| *MODATA_UVW* | [`Vector`](../../c4d/Vector/index.md#c4d.Vector) | UV position of the clone. |
| *MODATA_FLAGS* | int | Flags: |
|  | *MOGENFLAG_CLONE_ON* | Particle is visible. |
|  | *MOGENFLAG_DISABLE* | Particle is permanently disabled. |
|  | *MOGENFLAG_BORN* | Particle is just generated (internal use only). |
|  | *MOGENFLAG_MODATASET* | The [`MoData`](MoData/index.md#c4d.modules.mograph.MoData) has been set and does not need the input of the transform panel. |
|  | *MOGENFLAG_COLORSET* | The [`MoData`](MoData/index.md#c4d.modules.mograph.MoData) color has been set and does not need to be updated. |
|  | *MOGENFLAG_TIMESET* | The [`MoData`](MoData/index.md#c4d.modules.mograph.MoData) time has been set and does not need to be updated. |
| *MODATA_WEIGHT* | float | Weight of the clone. |
| *MODATA_CLONE* | float | Clone Offset (picks which child of the Cloner gets cloned or the blending between those children). |
| *MODATA_TIME* | float | Time offset of the clone. |
| *MODATA_LASTMAT* | [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) | Previous frame particle matrix. |
| *MODATA_STARTMAT* | [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) | Matrix at the particle’s birth. |
| *MODATA_ALT_INDEX* | int | Alternative index value that can be used for instance by the Step Effector when cloned over a spline with an offset. |
| *MODATA_FALLOFF_WGT* | float | Falloff weight. |
| *MODATA_SPLINE_SEGMENT* | int | The segment index, mostly used with the MoSpline (currently unused). |
| *MODATA_GROWTH* | float | Offset of growth for the particle on the MoSpline (currently unused). |

**Return type:** Any

**Returns:** The default value.

#### `c4d.modules.mograph.GetMoDataDefaultType(id)` <a id="c4d.modules.mograph.GetMoDataDefaultType"></a>

Get the default value for the specified [`MoData`](MoData/index.md#c4d.modules.mograph.MoData) ID.

**Parameters:**

**id** (*int*) –

The [`MoData`](MoData/index.md#c4d.modules.mograph.MoData) ID:

|   |   |   |
|---|---|---|
| *MODATA_MATRIX* | [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) | Matrix of the clone. |
| *MODATA_COLOR* | [`Vector`](../../c4d/Vector/index.md#c4d.Vector) | Color of the clone. |
| *MODATA_SIZE* | [`Vector`](../../c4d/Vector/index.md#c4d.Vector) | Size of the clone. |
| *MODATA_UVW* | [`Vector`](../../c4d/Vector/index.md#c4d.Vector) | UV position of the clone. |
| *MODATA_FLAGS* | int | Flags: |
|  | *MOGENFLAG_CLONE_ON* | Particle is visible. |
|  | *MOGENFLAG_DISABLE* | Particle is permanently disabled. |
|  | *MOGENFLAG_BORN* | Particle is just generated (internal use only). |
|  | *MOGENFLAG_MODATASET* | The [`MoData`](MoData/index.md#c4d.modules.mograph.MoData) has been set and does not need the input of the transform panel. |
|  | *MOGENFLAG_COLORSET* | The [`MoData`](MoData/index.md#c4d.modules.mograph.MoData) color has been set and does not need to be updated. |
|  | *MOGENFLAG_TIMESET* | The [`MoData`](MoData/index.md#c4d.modules.mograph.MoData) time has been set and does not need to be updated. |
| *MODATA_WEIGHT* | float | Weight of the clone. |
| *MODATA_CLONE* | float | Clone Offset (picks which child of the Cloner gets cloned or the blending between those children). |
| *MODATA_TIME* | float | Time offset of the clone. |
| *MODATA_LASTMAT* | [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) | Previous frame particle matrix. |
| *MODATA_STARTMAT* | [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) | Matrix at the particle’s birth. |
| *MODATA_ALT_INDEX* | int | Alternative index value that can be used for instance by the Step Effector when cloned over a spline with an offset. |
| *MODATA_FALLOFF_WGT* | float | Falloff weight. |
| *MODATA_SPLINE_SEGMENT* | int | The segment index, mostly used with the MoSpline (currently unused). |
| *MODATA_GROWTH* | float | Offset of growth for the particle on the MoSpline (currently unused). |

**Return type:** int

**Returns:**

The default type:

| MD_TYPE_MD_NONE | None. |
|---|---|
| MD_TYPE_MD_CHAR | Char type. |
| MD_TYPE_MD_UCHAR | UChar type. |
| MD_TYPE_MD_LONG | Int32 type. |
| MD_TYPE_MD_ULONG | UInt32 type. |
| MD_TYPE_MD_LLONG | Int64 type. |
| MD_TYPE_MD_MATRIX | [`Matrix`](../../c4d/Matrix/index.md#c4d.Matrix) type. |
| MD_TYPE_MD_COLOR | [`Vector`](../../c4d/Vector/index.md#c4d.Vector) type. |
| MD_TYPE_MD_VECTOR | [`Vector`](../../c4d/Vector/index.md#c4d.Vector) type. |
| MD_TYPE_MD_NORMAL | Normal type. |
| MD_TYPE_MD_REAL | Float type. |
| MD_TYPE_MD_BOOL | Bool type. |
