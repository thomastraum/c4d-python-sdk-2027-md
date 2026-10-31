<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/FieldList/index.html -->

# c4d.FieldList <a id="c4d-fieldlist"></a>

## *class* `c4d.FieldList` <a id="c4d.FieldList"></a>

Field list data type (*CUSTOMDATATYPE_FIELDLIST*).

*New in version R20.*

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Content State**

- [`FieldList.Flush()`](#c4d.FieldList.Flush): Empties the list of all entries, frees any used memory and resets the [`FieldList`](#c4d.FieldList) instance back to its default state.
- [`FieldList.GetCount()`](#c4d.FieldList.GetCount): Retrieves the total number of fields and groups in the list.
- [`FieldList.GetDirty()`](#c4d.FieldList.GetDirty): Checks the dirtiness of the field list and its objects.
- [`FieldList.HasContent()`](#c4d.FieldList.HasContent): Checks if the list has content.

**Direct Sampling**

- [`FieldList.DirectFreeSampling()`](#c4d.FieldList.DirectFreeSampling): Frees any data allocated in `DirectInitSampling()`.
- [`FieldList.DirectInitSampling()`](#c4d.FieldList.DirectInitSampling): Initializes sampling in direct mode.
- [`FieldList.DirectSample()`](#c4d.FieldList.DirectSample): Samples in direct mode.

**Flag Management**

- [`FieldList.CheckFlag()`](#c4d.FieldList.CheckFlag): Checks a specific *flag* or combination to see if set.
- [`FieldList.GetFlags()`](#c4d.FieldList.GetFlags): Gets the flags for the list.
- [`FieldList.SetFlags()`](#c4d.FieldList.SetFlags): Sets the flags for the list.

**Layer Management**

- [`FieldList.GetLayersRoot()`](#c4d.FieldList.GetLayersRoot): Retrieves the root [`GeListHead`](../../C4DAtom/GeListNode/GeListHead/index.md#c4d.GeListHead) that owns the layers.
- [`FieldList.GetSelected()`](#c4d.FieldList.GetSelected): Retrieves a list of all the selected layers in the list.
- [`FieldList.InsertLayer()`](#c4d.FieldList.InsertLayer): Inserts a pre-existing layer into the list.

**Magic Methods**

- [`FieldList.__init__()`](#c4d.FieldList.__init__): Initializes a [`FieldList`](#c4d.FieldList) instance.

**Sampling**

- [`FieldList.SampleList()`](#c4d.FieldList.SampleList): Samples the list with full parameter control.
- [`FieldList.SampleListSimple()`](#c4d.FieldList.SampleListSimple): Samples the list.

## Members <a id="members"></a>

### Content State <a id="c4d.FieldList-method-Content-State"></a>

#### `FieldList.Flush(self)` <a id="c4d.FieldList.Flush"></a>

Empties the list of all entries, frees any used memory and resets the [`FieldList`](#c4d.FieldList) instance back to its default state.

#### `FieldList.GetCount(self)` <a id="c4d.FieldList.GetCount"></a>

Retrieves the total number of fields and groups in the list.

**Return type:** int

**Returns:** The number of elements in the list.

#### `FieldList.GetDirty(self, doc)` <a id="c4d.FieldList.GetDirty"></a>

Checks the dirtiness of the field list and its objects.

**Parameters:** **doc** (*Optional*[[*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]) – The document. Can be **None**.

**Return type:** int

**Returns:** The dirty count.

#### `FieldList.HasContent(self)` <a id="c4d.FieldList.HasContent"></a>

Checks if the list has content.

**Return type:** bool

**Returns:** **True** if there is any field layer in the list, otherwise **False**.

### Direct Sampling <a id="c4d.FieldList-method-Direct-Sampling"></a>

#### `FieldList.DirectFreeSampling(self, info)` <a id="c4d.FieldList.DirectFreeSampling"></a>

Frees any data allocated in [`DirectInitSampling()`](#c4d.FieldList.DirectInitSampling).

> **Warning:** Must be called after direct sampling is finished.

> **Warning:**
>
> Due to core changes in 2024.0.0, this function is not working in Python 2024.0.0.  
> This is going to be fixed in an upcoming version.

**Parameters:** **info** ([*c4d.modules.mograph.FieldInfo*](../../../c4d.modules/mograph/FieldInfo/index.md#c4d.modules.mograph.FieldInfo)) – The [`FieldInfo`](../../../c4d.modules/mograph/FieldInfo/index.md#c4d.modules.mograph.FieldInfo) used for sampling.

#### `FieldList.DirectInitSampling(self, info)` <a id="c4d.FieldList.DirectInitSampling"></a>

Initializes sampling in direct mode.

> **Warning:** Must be called before [`DirectSample()`](#c4d.FieldList.DirectSample) is invoked.

**Parameters:** **info** ([*c4d.modules.mograph.FieldInfo*](../../../c4d.modules/mograph/FieldInfo/index.md#c4d.modules.mograph.FieldInfo)) – The [`FieldInfo`](../../../c4d.modules/mograph/FieldInfo/index.md#c4d.modules.mograph.FieldInfo) to initialize sampling with.

**Return type:** bool

**Returns:** **True** if successful otherwise **False**.

#### `FieldList.DirectSample(self, inputs, outputs, info)` <a id="c4d.FieldList.DirectSample"></a>

Samples in direct mode.

> **Warning:**
>
> Due to core changes in 2024.0.0, this function is not working in Python 2024.0.0.  
> This is going to be fixed in an upcoming version.

**Parameters:**

- **inputs** ([*c4d.modules.mograph.FieldInput*](../../../c4d.modules/mograph/FieldInput/index.md#c4d.modules.mograph.FieldInput)) – The inputs to sample from.
- **outputs** ([*c4d.modules.mograph.FieldOutput*](../../../c4d.modules/mograph/FieldOutput/index.md#c4d.modules.mograph.FieldOutput)) – The sample data result.
- **info** ([*c4d.modules.mograph.FieldInfo*](../../../c4d.modules/mograph/FieldInfo/index.md#c4d.modules.mograph.FieldInfo)) – The [`FieldInfo`](../../../c4d.modules/mograph/FieldInfo/index.md#c4d.modules.mograph.FieldInfo) to sample with.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Flag Management <a id="c4d.FieldList-method-Flag-Management"></a>

#### `FieldList.CheckFlag(self, flag)` <a id="c4d.FieldList.CheckFlag"></a>

Checks a specific *flag* or combination to see if set.

**Parameters:**

**flag** (*int*) –

The flag to check:

|   |   |
|---|---|
| *FIELDLIST_FLAGS_NONE* | None. |
| *FIELDLIST_FLAGS_CLAMPOUTPUT* | Clamp the output values from the field list. |
| *FIELDLIST_FLAGS_ENABLEDIRECTIONBYDEFAULT* | Direction enabled by default on new layers. |
| *FIELDLIST_FLAGS_ENABLECOLORBYDEFAULT* | Color enabled by default on new layers. |
| *FIELDLIST_FLAGS_ENABLEROTATIONBYDEFAULT* | Direction enabled by default on new layers |
| *FIELDLIST_FLAGS_DISABLEVALUEBYDEFAULT* | Disable the value channel by default on new layers |
| *FIELDLIST_FLAGS_SIMPLEGUI* | Use simple GUI. Only possible if there is only a single standard field layer in the list. |

**Return type:** bool

**Returns:** **True** if *flag* is set, otherwise **False**.

#### `FieldList.GetFlags(self)` <a id="c4d.FieldList.GetFlags"></a>

Gets the flags for the list.

**Return type:** int

**Returns:**

The flags:

|   |   |
|---|---|
| *FIELDLIST_FLAGS_NONE* | None. |
| *FIELDLIST_FLAGS_CLAMPOUTPUT* | Clamp the output values from the field list. |
| *FIELDLIST_FLAGS_ENABLEDIRECTIONBYDEFAULT* | Direction enabled by default on new layers. |
| *FIELDLIST_FLAGS_ENABLECOLORBYDEFAULT* | Color enabled by default on new layers. |
| *FIELDLIST_FLAGS_ENABLEROTATIONBYDEFAULT* | Direction enabled by default on new layers |
| *FIELDLIST_FLAGS_DISABLEVALUEBYDEFAULT* | Disable the value channel by default on new layers |
| *FIELDLIST_FLAGS_SIMPLEGUI* | Use simple GUI. Only possible if there is only a single standard field layer in the list. |

#### `FieldList.SetFlags(self, flag, state)` <a id="c4d.FieldList.SetFlags"></a>

Sets the flags for the list.

**Parameters:**

- **flag** (*int*) –

  The flags to set:

  |   |   |
  |---|---|
  | *FIELDLIST_FLAGS_NONE* | None. |
  | *FIELDLIST_FLAGS_CLAMPOUTPUT* | Clamp the output values from the field list. |
  | *FIELDLIST_FLAGS_ENABLEDIRECTIONBYDEFAULT* | Direction enabled by default on new layers. |
  | *FIELDLIST_FLAGS_ENABLECOLORBYDEFAULT* | Color enabled by default on new layers. |
  | *FIELDLIST_FLAGS_ENABLEROTATIONBYDEFAULT* | Direction enabled by default on new layers |
  | *FIELDLIST_FLAGS_DISABLEVALUEBYDEFAULT* | Disable the value channel by default on new layers |
  | *FIELDLIST_FLAGS_SIMPLEGUI* | Use simple GUI. Only possible if there is only a single standard field layer in the list. |

- **state** (*bool*) – **True** to set the flag, **False** to clear it.

### Layer Management <a id="c4d.FieldList-method-Layer-Management"></a>

#### `FieldList.GetLayersRoot(self, create=True)` <a id="c4d.FieldList.GetLayersRoot"></a>

Retrieves the root [`GeListHead`](../../C4DAtom/GeListNode/GeListHead/index.md#c4d.GeListHead) that owns the layers.

**Parameters:**

**create** (*bool*) –

*New in version 2024.0.0.*

True if the root should be created if it does not exist.

**Return type:** Optional[[c4d.GeListHead](../../C4DAtom/GeListNode/GeListHead/index.md#c4d.GeListHead)]

**Returns:** The layers root, or **None** if the function failed.

#### `FieldList.GetSelected(self, selected, includeChildren=True)` <a id="c4d.FieldList.GetSelected"></a>

Retrieves a list of all the selected layers in the list.

> **Note:** This may include the background layer.

**Parameters:**

- **selected** (*List*[[*c4d.modules.mograph.FieldLayer*](../../../c4d.modules/mograph/FieldLayer/index.md#c4d.modules.mograph.FieldLayer)]) – The selected layers in the list.
- **includeChildren** (*Optional*[*bool*]) – **True** to include children layers, **False** to exclude.

#### `FieldList.InsertLayer(self, layer, parent=None, prev=None)` <a id="c4d.FieldList.InsertLayer"></a>

Inserts a pre-existing layer into the list.

**Parameters:**

- **layer** ([*c4d.modules.mograph.FieldLayer*](../../../c4d.modules/mograph/FieldLayer/index.md#c4d.modules.mograph.FieldLayer)) – The layer to insert. Must not be already inserted in any other list or in the current list in another location.
- **parent** (*Optional*[[*c4d.modules.mograph.FieldLayer*](../../../c4d.modules/mograph/FieldLayer/index.md#c4d.modules.mograph.FieldLayer)]) – The parent layer to insert the layer as a child of.
- **prev** (*Optional*[[*c4d.modules.mograph.FieldLayer*](../../../c4d.modules/mograph/FieldLayer/index.md#c4d.modules.mograph.FieldLayer)]) – The previous layer to the one being inserted.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Magic Methods <a id="c4d.FieldList-method-Magic-Methods"></a>

#### `FieldList.__init__(self)` <a id="c4d.FieldList.__init__"></a>

Initializes a [`FieldList`](#c4d.FieldList) instance.

### Sampling <a id="c4d.FieldList-method-Sampling"></a>

#### `FieldList.SampleList(self, info, inputs, outputs)` <a id="c4d.FieldList.SampleList"></a>

Samples the list with full parameter control.

**Parameters:**

- **info** ([*c4d.modules.mograph.FieldInfo*](../../../c4d.modules/mograph/FieldInfo/index.md#c4d.modules.mograph.FieldInfo)) – The [`FieldInfo`](../../../c4d.modules/mograph/FieldInfo/index.md#c4d.modules.mograph.FieldInfo) to sample with.
- **inputs** ([*c4d.modules.mograph.FieldInput*](../../../c4d.modules/mograph/FieldInput/index.md#c4d.modules.mograph.FieldInput)) – The inputs to sample. A [`FieldInput`](../../../c4d.modules/mograph/FieldInput/index.md#c4d.modules.mograph.FieldInput) with a single position can be passed to sample just one point.
- **outputs** ([*c4d.modules.mograph.FieldOutput*](../../../c4d.modules/mograph/FieldOutput/index.md#c4d.modules.mograph.FieldOutput)) – The sample data result.

#### `FieldList.SampleListSimple(self, caller, inputs, flags)` <a id="c4d.FieldList.SampleListSimple"></a>

Samples the list.

> **Note:** Use [`SampleListSimple()`](#c4d.FieldList.SampleListSimple) to avoid pre-creating [`FieldInfo`](../../../c4d.modules/mograph/FieldInfo/index.md#c4d.modules.mograph.FieldInfo) and [`FieldOutput`](../../../c4d.modules/mograph/FieldOutput/index.md#c4d.modules.mograph.FieldOutput).

**Parameters:**

- **caller** ([*c4d.BaseList2D*](../../C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The caller object. Pass the [`BaseList2D`](../../C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) to invoke the sampling from.

- **inputs** ([*c4d.modules.mograph.FieldInput*](../../../c4d.modules/mograph/FieldInput/index.md#c4d.modules.mograph.FieldInput)) – The inputs to sample from.

- **flags** (*int*) –

  The channels to sample:

  |   |   |
  |---|---|
  | *FIELDSAMPLE_FLAG_VALUE* | Sample only the value. |
  | *FIELDSAMPLE_FLAG_DIRECTION* | Sample the velocity. |
  | *FIELDSAMPLE_FLAG_COLOR* | Sample the color. |
  | *FIELDSAMPLE_FLAG_ROTATION* | Sample the rotational velocity. |

**Return type:** [c4d.modules.mograph.FieldOutput](../../../c4d.modules/mograph/FieldOutput/index.md#c4d.modules.mograph.FieldOutput)

**Returns:** The sampling result.
