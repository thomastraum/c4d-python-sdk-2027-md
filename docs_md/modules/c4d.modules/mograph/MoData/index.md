<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/mograph/MoData/index.html -->

# c4d.modules.mograph.MoData <a id="c4d-modules-mograph-modata"></a>

## *class* `c4d.modules.mograph.MoData` <a id="c4d.modules.mograph.MoData"></a>

Represents a bundle of MoGraph particle data.

## Overview <a id="overview"></a>

**Array Management**

- [`MoData.AddArray()`](#c4d.modules.mograph.MoData.AddArray): Add the specified array.
- [`MoData.RemoveArray()`](#c4d.modules.mograph.MoData.RemoveArray): Remove the specified array.

**Array Metadata**

- [`MoData.GetArrayDescID()`](#c4d.modules.mograph.MoData.GetArrayDescID): Get the description ID for the specified array index.
- [`MoData.GetArrayID()`](#c4d.modules.mograph.MoData.GetArrayID): Get the ID for the specified array index.
- [`MoData.GetArrayIndex()`](#c4d.modules.mograph.MoData.GetArrayIndex): Get the array index for the specified description ID.
- [`MoData.GetArrayIndexType()`](#c4d.modules.mograph.MoData.GetArrayIndexType): Get the data type of the specified array.
- [`MoData.GetArrayType()`](#c4d.modules.mograph.MoData.GetArrayType): Get the data type of the specified array.
- [`MoData.GetIndexName()`](#c4d.modules.mograph.MoData.GetIndexName): Get the name of the specified array.
- [`MoData.GetName()`](#c4d.modules.mograph.MoData.GetName): Get the name of the specified array.
- [`MoData.SetIndexName()`](#c4d.modules.mograph.MoData.SetIndexName): Set the name for the specified array.
- [`MoData.SetName()`](#c4d.modules.mograph.MoData.SetName): Set the name for the specified array.

**Change Tracking**

- [`MoData.GetDirty()`](#c4d.modules.mograph.MoData.GetDirty): Get dirty count.
- [`MoData.SetDirty()`](#c4d.modules.mograph.MoData.SetDirty): Mark the data as dirty.

**Data Access**

- [`MoData.GetArray()`](#c4d.modules.mograph.MoData.GetArray): Get an array.
- [`MoData.GetArrayValue()`](#c4d.modules.mograph.MoData.GetArrayValue): Retrieves a value from a specific array in the MoData object.
- [`MoData.GetData()`](#c4d.modules.mograph.MoData.GetData): Get a copy of the array’s container.
- [`MoData.GetDataIndexInstance()`](#c4d.modules.mograph.MoData.GetDataIndexInstance): Get a pointer to the container for the specified array.
- [`MoData.GetDataInstance()`](#c4d.modules.mograph.MoData.GetDataInstance): Get a pointer to the container for the specified array.
- [`MoData.SetArray()`](#c4d.modules.mograph.MoData.SetArray): Set an array.

**Execution Context**

- [`MoData.GetBlendID()`](#c4d.modules.mograph.MoData.GetBlendID): Returns the current blend ID.
- [`MoData.GetCurrentIndex()`](#c4d.modules.mograph.MoData.GetCurrentIndex): Returns the current index.
- [`MoData.GetFalloffs()`](#c4d.modules.mograph.MoData.GetFalloffs): Returns the established falloffs.
- [`MoData.GetGenerator()`](#c4d.modules.mograph.MoData.GetGenerator): Returns the generator.

**Lifecycle Management**

- [`MoData.Clear()`](#c4d.modules.mograph.MoData.Clear): Clear the data in the arrays.
- [`MoData.Flush()`](#c4d.modules.mograph.MoData.Flush): Flushes the data.

**Persistence**

- [`MoData.Read()`](#c4d.modules.mograph.MoData.Read): Read the data from a hyper file.
- [`MoData.Write()`](#c4d.modules.mograph.MoData.Write): Write the data to a hyper file.

**Processing Bounds**

- [`MoData.SetLimit()`](#c4d.modules.mograph.MoData.SetLimit): Limits the array.
- [`MoData.SetOffset()`](#c4d.modules.mograph.MoData.SetOffset): Set an offset from the beginning of the arrays, for example array[0] becomes array[offset].

**Storage Dimensions**

- [`MoData.GetArrayCount()`](#c4d.modules.mograph.MoData.GetArrayCount): Get the number of arrays.
- [`MoData.GetCount()`](#c4d.modules.mograph.MoData.GetCount): Get the length of the arrays.
- [`MoData.GetMemorySize()`](#c4d.modules.mograph.MoData.GetMemorySize): Get the size of the data in bytes.
- [`MoData.SetCount()`](#c4d.modules.mograph.MoData.SetCount): Set the length of the arrays.

## Members <a id="members"></a>

### Array Management <a id="c4d.modules.mograph.MoData-method-Array-Management"></a>

#### `MoData.AddArray(self, id, name='', default_flags=0)` <a id="c4d.modules.mograph.MoData.AddArray"></a>

Add the specified array.

**Parameters:**

- **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The description ID of the array.

- **name** (*str*) – The name of the array.

- **default_flags** (*int*) –

  Default flags:

  |   |   |
  |---|---|
  | *MOGENFLAG_CLONE_ON* | Particle is visible. |
  | *MOGENFLAG_DISABLE* | Particle is permanently disabled. |
  | *MOGENFLAG_BORN* | Particle is just generated (internal use only). |
  | *MOGENFLAG_MODATASET* | The [`MoData`](#c4d.modules.mograph.MoData) has been set and does not need the input of the transform panel. |
  | *MOGENFLAG_COLORSET* | The [`MoData`](#c4d.modules.mograph.MoData) color has been set and does not need to be updated. |
  | *MOGENFLAG_TIMESET* | The [`MoData`](#c4d.modules.mograph.MoData) time has been set and does not need to be updated. |

**Return type:** int

**Returns:** The index of the added array or *NOTOK* if it failed.

#### `MoData.RemoveArray(self, id)` <a id="c4d.modules.mograph.MoData.RemoveArray"></a>

Remove the specified array.

**Parameters:** **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The description ID of the array.

**Return type:** bool

**Returns:** **True** if the array has been removed, otherwise **False**.

### Array Metadata <a id="c4d.modules.mograph.MoData-method-Array-Metadata"></a>

#### `MoData.GetArrayDescID(self, index)` <a id="c4d.modules.mograph.MoData.GetArrayDescID"></a>

Get the description ID for the specified array index.

**Parameters:** **index** (*int*) – The index of the array.

**Raises:** **IndexError** – If the array *index* is out of range : *0<=index<*[`GetArrayCount()`](#c4d.modules.mograph.MoData.GetArrayCount).

**Return type:** [c4d.DescID](../../../c4d/DescID/index.md#c4d.DescID)

**Returns:** The description ID.

#### `MoData.GetArrayID(self, index)` <a id="c4d.modules.mograph.MoData.GetArrayID"></a>

Get the ID for the specified array index.

**Parameters:** **index** (*int*) – The index of the array.

**Raises:** **IndexError** – If the array *index* is out of range : *0<=index<*[`GetArrayCount()`](#c4d.modules.mograph.MoData.GetArrayCount).

**Return type:** int

**Returns:**

The retrieved ID:

|   |   |   |
|---|---|---|
| *MODATA_MATRIX* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Matrix of the clone. |
| *MODATA_COLOR* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | Color of the clone. |
| *MODATA_SIZE* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | Size of the clone. |
| *MODATA_UVW* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | UV position of the clone. |
| *MODATA_FLAGS* | int | Flags: |
|  | *MOGENFLAG_CLONE_ON* | Particle is visible. |
|  | *MOGENFLAG_DISABLE* | Particle is permanently disabled. |
|  | *MOGENFLAG_BORN* | Particle is just generated (internal use only). |
|  | *MOGENFLAG_MODATASET* | The [`MoData`](#c4d.modules.mograph.MoData) has been set and does not need the input of the transform panel. |
|  | *MOGENFLAG_COLORSET* | The [`MoData`](#c4d.modules.mograph.MoData) color has been set and does not need to be updated. |
|  | *MOGENFLAG_TIMESET* | The [`MoData`](#c4d.modules.mograph.MoData) time has been set and does not need to be updated. |
| *MODATA_WEIGHT* | float | Weight of the clone. |
| *MODATA_CLONE* | float | Clone Offset (picks which child of the Cloner gets cloned or the blending between those children). |
| *MODATA_TIME* | float | Time offset of the clone. |
| *MODATA_LASTMAT* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Previous frame particle matrix. |
| *MODATA_STARTMAT* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Matrix at the particle’s birth. |
| *MODATA_ALT_INDEX* | int | Alternative index value that can be used for instance by the Step Effector when cloned over a spline with an offset. |
| *MODATA_FALLOFF_WGT* | float | Falloff weight. |
| *MODATA_SPLINE_SEGMENT* | int | The segment index, mostly used with the MoSpline (currently unused). |
| *MODATA_GROWTH* | float | Offset of growth for the particle on the MoSpline (currently unused). |

#### `MoData.GetArrayIndex(self, id)` <a id="c4d.modules.mograph.MoData.GetArrayIndex"></a>

Get the array index for the specified description ID.

**Parameters:** **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The description ID.

**Return type:** int

**Returns:** The retrieved array index.

#### `MoData.GetArrayIndexType(self, index)` <a id="c4d.modules.mograph.MoData.GetArrayIndexType"></a>

Get the data type of the specified array.

**Parameters:** **index** (*int*) – The index of the array.

**Raises:** **IndexError** – If the array *index* is out of range : *0<=index<*[`GetArrayCount()`](#c4d.modules.mograph.MoData.GetArrayCount).

**Return type:** int

**Returns:**

Type:

|   |   |
|---|---|
| *DTYPE_NONE* | None. |
| *DTYPE_CHILDREN* | Children. |
| *DTYPE_GROUP* | Group. |
| *DTYPE_COLOR* | Color. |
| *DTYPE_SUBCONTAINER* | [`BaseContainer`](../../../c4d/BaseContainer/index.md#c4d.BaseContainer). |
| *DTYPE_MULTIPLEDATA* | Multiple data entry. |
| *DTYPE_TEXTURE* | Texture name. |
| *DTYPE_BUTTON* | Button. |
| *DTYPE_DYNAMIC* | GV dynamic. |
| *DTYPE_SEPARATOR* | Separator. |
| *DTYPE_STATICTEXT* | Static text. |
| *DTYPE_POPUP* | Popup. |
| *DTYPE_LONG* | Integer. |
| *DTYPE_REAL* | Float. |
| *DTYPE_TIME* | [`BaseTime`](../../../c4d/BaseTime/index.md#c4d.BaseTime). |
| *DTYPE_VECTOR* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector). |
| *DTYPE_MATRIX* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix). |
| *DTYPE_STRING* | String. |
| *DTYPE_FILENAME* | String. |
| *DTYPE_BASELISTLINK* | [`BaseList2D`](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D). |
| *DTYPE_BOOL* | GV bool *ID_GV_DATA_TYPE_BOOL*. |
| *DTYPE_NORMAL* | GV normal *ID_GV_DATA_TYPE_NORMAL*. |
| *DTYPE_COLORA* | Color with Alpha. |
| *DTYPE_VECTOR4D* | Vector with 4 components. |

#### `MoData.GetArrayType(self, id)` <a id="c4d.modules.mograph.MoData.GetArrayType"></a>

Get the data type of the specified array.

**Parameters:**

**id** (*int*) –

The ID of the array:

|   |   |   |
|---|---|---|
| *MODATA_MATRIX* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Matrix of the clone. |
| *MODATA_COLOR* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | Color of the clone. |
| *MODATA_SIZE* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | Size of the clone. |
| *MODATA_UVW* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | UV position of the clone. |
| *MODATA_FLAGS* | int | Flags: |
|  | *MOGENFLAG_CLONE_ON* | Particle is visible. |
|  | *MOGENFLAG_DISABLE* | Particle is permanently disabled. |
|  | *MOGENFLAG_BORN* | Particle is just generated (internal use only). |
|  | *MOGENFLAG_MODATASET* | The [`MoData`](#c4d.modules.mograph.MoData) has been set and does not need the input of the transform panel. |
|  | *MOGENFLAG_COLORSET* | The [`MoData`](#c4d.modules.mograph.MoData) color has been set and does not need to be updated. |
|  | *MOGENFLAG_TIMESET* | The [`MoData`](#c4d.modules.mograph.MoData) time has been set and does not need to be updated. |
| *MODATA_WEIGHT* | float | Weight of the clone. |
| *MODATA_CLONE* | float | Clone Offset (picks which child of the Cloner gets cloned or the blending between those children). |
| *MODATA_TIME* | float | Time offset of the clone. |
| *MODATA_LASTMAT* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Previous frame particle matrix. |
| *MODATA_STARTMAT* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Matrix at the particle’s birth. |
| *MODATA_ALT_INDEX* | int | Alternative index value that can be used for instance by the Step Effector when cloned over a spline with an offset. |
| *MODATA_FALLOFF_WGT* | float | Falloff weight. |
| *MODATA_SPLINE_SEGMENT* | int | The segment index, mostly used with the MoSpline (currently unused). |
| *MODATA_GROWTH* | float | Offset of growth for the particle on the MoSpline (currently unused). |

#### `MoData.GetIndexName(self, index)` <a id="c4d.modules.mograph.MoData.GetIndexName"></a>

Get the name of the specified array.

**Parameters:** **index** (*int*) – Array index.

**Raises:** **IndexError** – If the array *index* is out of range : *0<=index<*[`GetArrayCount()`](#c4d.modules.mograph.MoData.GetArrayCount).

**Return type:** str

**Returns:** The name of the array.

#### `MoData.GetName(self, id)` <a id="c4d.modules.mograph.MoData.GetName"></a>

Get the name of the specified array.

**Parameters:** **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The description ID of the array.

**Return type:** str

**Returns:** The name of the array.

#### `MoData.SetIndexName(self, index, name)` <a id="c4d.modules.mograph.MoData.SetIndexName"></a>

Set the name for the specified array.

**Parameters:**

- **index** (*int*) – The index of the array.
- **name** (*str*) – The new name of the array.

**Raises:** **IndexError** – If the array *index* is out of range : *0<=index<*[`GetArrayCount()`](#c4d.modules.mograph.MoData.GetArrayCount).

#### `MoData.SetName(self, id, name)` <a id="c4d.modules.mograph.MoData.SetName"></a>

Set the name for the specified array.

**Parameters:**

- **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The description ID of the array.
- **name** (*str*) – The new name of the array.

### Change Tracking <a id="c4d.modules.mograph.MoData-method-Change-Tracking"></a>

#### `MoData.GetDirty(self, mask=0)` <a id="c4d.modules.mograph.MoData.GetDirty"></a>

Get dirty count. Can be used to check if something has changed.

**Parameters:**

**mask** (*int*) –

Flags:

|   |   |
|---|---|
| *MDDIRTY_NONE* | None. |
| *MDDIRTY_ALL* | Check all. |
| *MDDIRTY_ARRAYCOUNT* | Array count itself changed (number of different arrays rather than length of arrays). |
| *MDDIRTY_COUNT* | Length of the arrays changed. |
| *MDDIRTY_DATA* | Data in the arrays changed, must be manually set. |

**Return type:** int

**Returns:** Dirty count.

#### `MoData.SetDirty(self, mask=0)` <a id="c4d.modules.mograph.MoData.SetDirty"></a>

Mark the data as dirty.

**Parameters:**

**mask** (*int*) –

Flags:

|   |   |
|---|---|
| *MDDIRTY_NONE* | None. |
| *MDDIRTY_ALL* | Check all. |
| *MDDIRTY_ARRAYCOUNT* | Array count itself changed (number of different arrays rather than length of arrays). |
| *MDDIRTY_COUNT* | Length of the arrays changed. |
| *MDDIRTY_DATA* | Data in the arrays changed, must be manually set. |

### Data Access <a id="c4d.modules.mograph.MoData-method-Data-Access"></a>

#### `MoData.GetArray(self, id)` <a id="c4d.modules.mograph.MoData.GetArray"></a>

Get an array.

**Parameters:**

**id** (*int*) –

The ID of the array:

|   |   |   |
|---|---|---|
| *MODATA_MATRIX* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Matrix of the clone. |
| *MODATA_COLOR* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | Color of the clone. |
| *MODATA_SIZE* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | Size of the clone. |
| *MODATA_UVW* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | UV position of the clone. |
| *MODATA_FLAGS* | int | Flags: |
|  | *MOGENFLAG_CLONE_ON* | Particle is visible. |
|  | *MOGENFLAG_DISABLE* | Particle is permanently disabled. |
|  | *MOGENFLAG_BORN* | Particle is just generated (internal use only). |
|  | *MOGENFLAG_MODATASET* | The [`MoData`](#c4d.modules.mograph.MoData) has been set and does not need the input of the transform panel. |
|  | *MOGENFLAG_COLORSET* | The [`MoData`](#c4d.modules.mograph.MoData) color has been set and does not need to be updated. |
|  | *MOGENFLAG_TIMESET* | The [`MoData`](#c4d.modules.mograph.MoData) time has been set and does not need to be updated. |
| *MODATA_WEIGHT* | float | Weight of the clone. |
| *MODATA_CLONE* | float | Clone Offset (picks which child of the Cloner gets cloned or the blending between those children). |
| *MODATA_TIME* | float | Time offset of the clone. |
| *MODATA_LASTMAT* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Previous frame particle matrix. |
| *MODATA_STARTMAT* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Matrix at the particle’s birth. |
| *MODATA_ALT_INDEX* | int | Alternative index value that can be used for instance by the Step Effector when cloned over a spline with an offset. |
| *MODATA_FALLOFF_WGT* | float | Falloff weight. |
| *MODATA_SPLINE_SEGMENT* | int | The segment index, mostly used with the MoSpline (currently unused). |
| *MODATA_GROWTH* | float | Offset of growth for the particle on the MoSpline (currently unused). |

**Return type:** list

**Returns:** The array.

#### `MoData.GetArrayValue(self, arrayId, valueIndex)` <a id="c4d.modules.mograph.MoData.GetArrayValue"></a>

Retrieves a value from a specific array in the MoData object.

**Parameters:**

- **arrayId** (*int*) –

  The ID of the array from which to retrieve the value.

  |   |   |   |
  |---|---|---|
  | *MODATA_MATRIX* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Matrix of the clone. |
  | *MODATA_COLOR* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | Color of the clone. |
  | *MODATA_SIZE* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | Size of the clone. |
  | *MODATA_UVW* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | UV position of the clone. |
  | *MODATA_FLAGS* | int | Flags: |
  |  | *MOGENFLAG_CLONE_ON* | Particle is visible. |
  |  | *MOGENFLAG_DISABLE* | Particle is permanently disabled. |
  |  | *MOGENFLAG_BORN* | Particle is just generated (internal use only). |
  |  | *MOGENFLAG_MODATASET* | The [`MoData`](#c4d.modules.mograph.MoData) has been set and does not need the input of the transform panel. |
  |  | *MOGENFLAG_COLORSET* | The [`MoData`](#c4d.modules.mograph.MoData) color has been set and does not need to be updated. |
  |  | *MOGENFLAG_TIMESET* | The [`MoData`](#c4d.modules.mograph.MoData) time has been set and does not need to be updated. |
  | *MODATA_WEIGHT* | float | Weight of the clone. |
  | *MODATA_CLONE* | float | Clone Offset (picks which child of the Cloner gets cloned or the blending between those children). |
  | *MODATA_TIME* | float | Time offset of the clone. |
  | *MODATA_LASTMAT* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Previous frame particle matrix. |
  | *MODATA_STARTMAT* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Matrix at the particle’s birth. |
  | *MODATA_ALT_INDEX* | int | Alternative index value that can be used for instance by the Step Effector when cloned over a spline with an offset. |
  | *MODATA_FALLOFF_WGT* | float | Falloff weight. |
  | *MODATA_SPLINE_SEGMENT* | int | The segment index, mostly used with the MoSpline (currently unused). |
  | *MODATA_GROWTH* | float | Offset of growth for the particle on the MoSpline (currently unused). |

- **valueIndex** (*int*) – The index of the value to retrieve from the array.

**Returns:**

The value at the specified index in the specified array. The type of the returned value depends on the type of the array:

- If the array type is *DTYPE_MATRIX*, a [`c4d.Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) object is returned.
- If the array type is *DTYPE_NORMAL*, *DTYPE_COLOR*, or *DTYPE_VECTOR*, a [`c4d.Vector`](../../../c4d/Vector/index.md#c4d.Vector) object is returned.
- If the array type is *DTYPE_REAL*, a float is returned.
- If the array type is *DTYPE_BOOL*, a bool is returned.
- If the array type is *DTYPE_LONG*, an int is returned.

If the specified array ID or value index is invalid, *None* is returned.

**Return type:** [Matrix](../../../c4d/Matrix/index.md#c4d.Matrix), [Vector](../../../c4d/Vector/index.md#c4d.Vector), float, bool, int, or None

**Raises:** **ValueError** – If *valueIndex* is less than 0 or greater than the entry count of the MoData array.

#### `MoData.GetData(self, id=-1)` <a id="c4d.modules.mograph.MoData.GetData"></a>

Get a copy of the array’s container.

**Parameters:**

**id** (*int*) –

The ID of the array:

|   |   |   |
|---|---|---|
| *MODATA_MATRIX* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Matrix of the clone. |
| *MODATA_COLOR* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | Color of the clone. |
| *MODATA_SIZE* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | Size of the clone. |
| *MODATA_UVW* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | UV position of the clone. |
| *MODATA_FLAGS* | int | Flags: |
|  | *MOGENFLAG_CLONE_ON* | Particle is visible. |
|  | *MOGENFLAG_DISABLE* | Particle is permanently disabled. |
|  | *MOGENFLAG_BORN* | Particle is just generated (internal use only). |
|  | *MOGENFLAG_MODATASET* | The [`MoData`](#c4d.modules.mograph.MoData) has been set and does not need the input of the transform panel. |
|  | *MOGENFLAG_COLORSET* | The [`MoData`](#c4d.modules.mograph.MoData) color has been set and does not need to be updated. |
|  | *MOGENFLAG_TIMESET* | The [`MoData`](#c4d.modules.mograph.MoData) time has been set and does not need to be updated. |
| *MODATA_WEIGHT* | float | Weight of the clone. |
| *MODATA_CLONE* | float | Clone Offset (picks which child of the Cloner gets cloned or the blending between those children). |
| *MODATA_TIME* | float | Time offset of the clone. |
| *MODATA_LASTMAT* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Previous frame particle matrix. |
| *MODATA_STARTMAT* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Matrix at the particle’s birth. |
| *MODATA_ALT_INDEX* | int | Alternative index value that can be used for instance by the Step Effector when cloned over a spline with an offset. |
| *MODATA_FALLOFF_WGT* | float | Falloff weight. |
| *MODATA_SPLINE_SEGMENT* | int | The segment index, mostly used with the MoSpline (currently unused). |
| *MODATA_GROWTH* | float | Offset of growth for the particle on the MoSpline (currently unused). |

**Return type:** [c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The array’s container.

#### `MoData.GetDataIndexInstance(self, index)` <a id="c4d.modules.mograph.MoData.GetDataIndexInstance"></a>

Get a pointer to the container for the specified array.

**Parameters:** **index** (*int*) – The index of the array.

**Raises:** **IndexError** – If the array *index* is out of range : *0<=index<*[`GetArrayCount()`](#c4d.modules.mograph.MoData.GetArrayCount).

**Return type:** [c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The internal container.

#### `MoData.GetDataInstance(self, id)` <a id="c4d.modules.mograph.MoData.GetDataInstance"></a>

Get a pointer to the container for the specified array.

**Parameters:** **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The description ID of the array.

**Return type:** [c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The internal container.

#### `MoData.SetArray(self, id, arr, apply_strength)` <a id="c4d.modules.mograph.MoData.SetArray"></a>

Set an array.

**Parameters:**

- **id** (*int*) –

  The ID of the array:

  |   |   |   |
  |---|---|---|
  | *MODATA_MATRIX* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Matrix of the clone. |
  | *MODATA_COLOR* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | Color of the clone. |
  | *MODATA_SIZE* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | Size of the clone. |
  | *MODATA_UVW* | [`Vector`](../../../c4d/Vector/index.md#c4d.Vector) | UV position of the clone. |
  | *MODATA_FLAGS* | int | Flags: |
  |  | *MOGENFLAG_CLONE_ON* | Particle is visible. |
  |  | *MOGENFLAG_DISABLE* | Particle is permanently disabled. |
  |  | *MOGENFLAG_BORN* | Particle is just generated (internal use only). |
  |  | *MOGENFLAG_MODATASET* | The [`MoData`](#c4d.modules.mograph.MoData) has been set and does not need the input of the transform panel. |
  |  | *MOGENFLAG_COLORSET* | The [`MoData`](#c4d.modules.mograph.MoData) color has been set and does not need to be updated. |
  |  | *MOGENFLAG_TIMESET* | The [`MoData`](#c4d.modules.mograph.MoData) time has been set and does not need to be updated. |
  | *MODATA_WEIGHT* | float | Weight of the clone. |
  | *MODATA_CLONE* | float | Clone Offset (picks which child of the Cloner gets cloned or the blending between those children). |
  | *MODATA_TIME* | float | Time offset of the clone. |
  | *MODATA_LASTMAT* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Previous frame particle matrix. |
  | *MODATA_STARTMAT* | [`Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix) | Matrix at the particle’s birth. |
  | *MODATA_ALT_INDEX* | int | Alternative index value that can be used for instance by the Step Effector when cloned over a spline with an offset. |
  | *MODATA_FALLOFF_WGT* | float | Falloff weight. |
  | *MODATA_SPLINE_SEGMENT* | int | The segment index, mostly used with the MoSpline (currently unused). |
  | *MODATA_GROWTH* | float | Offset of growth for the particle on the MoSpline (currently unused). |

- **arr** (*list*) – The array.

- **apply_strength** (*bool*) – If **True**, a falloff must be present in the [`MoData`](#c4d.modules.mograph.MoData) instance

### Execution Context <a id="c4d.modules.mograph.MoData-method-Execution-Context"></a>

#### `MoData.GetBlendID(self)` <a id="c4d.modules.mograph.MoData.GetBlendID"></a>

Returns the current blend ID.

**Return type:** int

**Returns:** The current blend ID.

#### `MoData.GetCurrentIndex(self)` <a id="c4d.modules.mograph.MoData.GetCurrentIndex"></a>

Returns the current index.

**Return type:** int

**Returns:** The current index.

#### `MoData.GetFalloffs(self)` <a id="c4d.modules.mograph.MoData.GetFalloffs"></a>

Returns the established falloffs.

> **Note:** Before R20, the falloffs was returned in reverse order.

**Return type:** List[float]

**Returns:** The falloff samples.

#### `MoData.GetGenerator(self)` <a id="c4d.modules.mograph.MoData.GetGenerator"></a>

Returns the generator.

*New in version R14.014.*

> **Note:** In a Python Effector the variable *gen* is the generator.

**Return type:** [c4d.BaseList2D](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

**Returns:** The generator.

### Lifecycle Management <a id="c4d.modules.mograph.MoData-method-Lifecycle-Management"></a>

#### `MoData.Clear(self, reset)` <a id="c4d.modules.mograph.MoData.Clear"></a>

Clear the data in the arrays.

**Parameters:** **reset** (*bool*) – **True** will fill the arrays with their default values.

#### `MoData.Flush(self)` <a id="c4d.modules.mograph.MoData.Flush"></a>

Flushes the data.  
All data is cleared, the arrays are freed.

### Persistence <a id="c4d.modules.mograph.MoData-method-Persistence"></a>

#### `MoData.Read(self, hf)` <a id="c4d.modules.mograph.MoData.Read"></a>

Read the data from a hyper file.

**Parameters:** **hf** ([*c4d.storage.HyperFile*](../../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile)) – The hyper file to read from.

**Return type:** bool

**Returns:** **True** if the data was read, otherwise **False**.

#### `MoData.Write(self, hf)` <a id="c4d.modules.mograph.MoData.Write"></a>

Write the data to a hyper file.

**Parameters:** **hf** ([*c4d.storage.HyperFile*](../../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile)) – The hyper file to write to.

**Return type:** bool

**Returns:** **True** if the data was written, otherwise **False**.

### Processing Bounds <a id="c4d.modules.mograph.MoData-method-Processing-Bounds"></a>

#### `MoData.SetLimit(self, limit=-1)` <a id="c4d.modules.mograph.MoData.SetLimit"></a>

Limits the array. All data are kept internally.  
Can be useful for certain cases for instance merging.

**Parameters:** **limit** (*int*) – The array limit, 0 <= *limit* < [`GetCount()`](#c4d.modules.mograph.MoData.GetCount).

#### `MoData.SetOffset(self, offset=0)` <a id="c4d.modules.mograph.MoData.SetOffset"></a>

Set an offset from the beginning of the arrays, for example array[0] becomes array[offset].

**Parameters:** **offset** (*int*) – The array offset, 0 <= *offset* < [`GetCount()`](#c4d.modules.mograph.MoData.GetCount).

### Storage Dimensions <a id="c4d.modules.mograph.MoData-method-Storage-Dimensions"></a>

#### `MoData.GetArrayCount(self)` <a id="c4d.modules.mograph.MoData.GetArrayCount"></a>

Get the number of arrays.

**Return type:** int

**Returns:** The number of arrays.

#### `MoData.GetCount(self)` <a id="c4d.modules.mograph.MoData.GetCount"></a>

Get the length of the arrays.

**Return type:** int

**Returns:** The length of the arrays.

#### `MoData.GetMemorySize(self)` <a id="c4d.modules.mograph.MoData.GetMemorySize"></a>

Get the size of the data in bytes.

**Return type:** int

**Returns:** Size of the data.

#### `MoData.SetCount(self, cnt)` <a id="c4d.modules.mograph.MoData.SetCount"></a>

Set the length of the arrays.

**Parameters:** **cnt** (*int*) – The new length of the arrays.

**Return type:** bool

**Returns:** **True** if the length was set, otherwise **False**.
