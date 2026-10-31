<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/mograph/FieldLayer/index.html -->

# c4d.modules.mograph.FieldLayer <a id="c4d-modules-mograph-fieldlayer"></a>

## *class* `c4d.modules.mograph.FieldLayer` <a id="c4d.modules.mograph.FieldLayer"></a>

*New in version R20.*

> **Warning:**
>
> Due to core changes in 2024.0.0, sampling of FieldLayer is not working in Python 2024.0.0.  
> This is going to be fixed in an upcoming version meanwhile you can sample a FieldList.

Parent Class:

- [`c4d.BaseList2D`](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

## Overview <a id="overview"></a>

**Channel Flags**

- [`FieldLayer.GetChannelFlag()`](#c4d.modules.mograph.FieldLayer.GetChannelFlag): Checks a specific channel *flag* enabled state.
- [`FieldLayer.GetChannelFlags()`](#c4d.modules.mograph.FieldLayer.GetChannelFlags): Gets the enabled flags for the layer.
- [`FieldLayer.SetChannelFlag()`](#c4d.modules.mograph.FieldLayer.SetChannelFlag): Sets a specific channel *flag* enabled *state*.
- [`FieldLayer.SetChannelFlags()`](#c4d.modules.mograph.FieldLayer.SetChannelFlags): Sets the enabled flags for the layer.

**Identity**

- [`FieldLayer.GetUniqueID()`](#c4d.modules.mograph.FieldLayer.GetUniqueID): Private.
- [`FieldLayer.SetUniqueID()`](#c4d.modules.mograph.FieldLayer.SetUniqueID): Private.

**Layer Flags**

- [`FieldLayer.GetLayerFlags()`](#c4d.modules.mograph.FieldLayer.GetLayerFlags): Gets the layer’s execution and display *flags*.
- [`FieldLayer.SetLayerFlags()`](#c4d.modules.mograph.FieldLayer.SetLayerFlags): Sets the layer’s execution and display *flags*.

**Linked Object**

- [`FieldLayer.GetLinkedObject()`](#c4d.modules.mograph.FieldLayer.GetLinkedObject): Gets the linked object.
- [`FieldLayer.SetLinkedObject()`](#c4d.modules.mograph.FieldLayer.SetLinkedObject): Sets the linked object.

**Magic Methods**

- [`FieldLayer.__init__()`](#c4d.modules.mograph.FieldLayer.__init__): Creates a [`FieldLayer`](#c4d.modules.mograph.FieldLayer) instance.

**Masks**

- [`FieldLayer.AddMask()`](#c4d.modules.mograph.FieldLayer.AddMask): Adds a mask to the `c4d.FieldLayer`, if a mask already exists then this will do nothing.
- [`FieldLayer.GetMaskHead()`](#c4d.modules.mograph.FieldLayer.GetMaskHead): If the `c4d.FieldLayer` has a mask then this retrieve the list head containing the mask layers.
- [`FieldLayer.RemoveMask()`](#c4d.modules.mograph.FieldLayer.RemoveMask): Removes the mask on the `c4d.FieldLayer`, if no mask exists then this will do nothing.

**Sampling**

- [`FieldLayer.Aggregate()`](#c4d.modules.mograph.FieldLayer.Aggregate): Private
- [`FieldLayer.FreeSampling()`](#c4d.modules.mograph.FieldLayer.FreeSampling): Frees any data allocated in `InitSampling()`.
- [`FieldLayer.InitSampling()`](#c4d.modules.mograph.FieldLayer.InitSampling): Initializes field sampling.
- [`FieldLayer.Sample()`](#c4d.modules.mograph.FieldLayer.Sample): Samples the field layer.

**Strength And Blending**

- [`FieldLayer.GetBlendingMode()`](#c4d.modules.mograph.FieldLayer.GetBlendingMode): Gets the field layer’s blending mode.
- [`FieldLayer.GetStrength()`](#c4d.modules.mograph.FieldLayer.GetStrength): Gets the field layer’s strength in percent.
- [`FieldLayer.SetBlendingMode()`](#c4d.modules.mograph.FieldLayer.SetBlendingMode): Sets field layer’s blending mode.
- [`FieldLayer.SetStrength()`](#c4d.modules.mograph.FieldLayer.SetStrength): Sets the field layer’s strength in percent.

## Members <a id="members"></a>

### Channel Flags <a id="c4d.modules.mograph.FieldLayer-method-Channel-Flags"></a>

#### `FieldLayer.GetChannelFlag(self, flag)` <a id="c4d.modules.mograph.FieldLayer.GetChannelFlag"></a>

Checks a specific channel *flag* enabled state.

**Parameters:**

**flag** (*int*) –

The flag to check:

|   |   |
|---|---|
| *FIELDLAYER_CHANNELFLAG_NONE* | None. |
| *FIELDLAYER_CHANNELFLAG_ENABLE* | Layer is enabled and sampled. |
| *FIELDLAYER_CHANNELFLAG_VALUE* | Value sampling is enabled. |
| *FIELDLAYER_CHANNELFLAG_COLOR* | Color sampling is enabled. |
| *FIELDLAYER_CHANNELFLAG_DIRECTION* | Direction sampling is enabled. |
| *FIELDLAYER_CHANNELFLAG_ROTATION* | Rotation sampling is enabled. |

**Return type:** bool

**Returns:** **True** if channel *flag* is set, otherwise **False**.

#### `FieldLayer.GetChannelFlags(self)` <a id="c4d.modules.mograph.FieldLayer.GetChannelFlags"></a>

Gets the enabled flags for the layer.

**Return type:** int

**Returns:**

The channel flags:

|   |   |
|---|---|
| *FIELDLAYER_CHANNELFLAG_NONE* | None. |
| *FIELDLAYER_CHANNELFLAG_ENABLE* | Layer is enabled and sampled. |
| *FIELDLAYER_CHANNELFLAG_VALUE* | Value sampling is enabled. |
| *FIELDLAYER_CHANNELFLAG_COLOR* | Color sampling is enabled. |
| *FIELDLAYER_CHANNELFLAG_DIRECTION* | Direction sampling is enabled. |
| *FIELDLAYER_CHANNELFLAG_ROTATION* | Rotation sampling is enabled. |

#### `FieldLayer.SetChannelFlag(self, flag, state=True)` <a id="c4d.modules.mograph.FieldLayer.SetChannelFlag"></a>

Sets a specific channel *flag* enabled *state*.

**Parameters:**

- **flags** (*int*) –

  The flag to set:

  |   |   |
  |---|---|
  | *FIELDLAYER_CHANNELFLAG_NONE* | None. |
  | *FIELDLAYER_CHANNELFLAG_ENABLE* | Layer is enabled and sampled. |
  | *FIELDLAYER_CHANNELFLAG_VALUE* | Value sampling is enabled. |
  | *FIELDLAYER_CHANNELFLAG_COLOR* | Color sampling is enabled. |
  | *FIELDLAYER_CHANNELFLAG_DIRECTION* | Direction sampling is enabled. |
  | *FIELDLAYER_CHANNELFLAG_ROTATION* | Rotation sampling is enabled. |

- **state** (*bool*) – **True** to enable the flag, **False** to disable.

#### `FieldLayer.SetChannelFlags(self, flags)` <a id="c4d.modules.mograph.FieldLayer.SetChannelFlags"></a>

Sets the enabled flags for the layer.

**Parameters:**

**flags** (*int*) –

The channel flags to set:

|   |   |
|---|---|
| *FIELDLAYER_CHANNELFLAG_NONE* | None. |
| *FIELDLAYER_CHANNELFLAG_ENABLE* | Layer is enabled and sampled. |
| *FIELDLAYER_CHANNELFLAG_VALUE* | Value sampling is enabled. |
| *FIELDLAYER_CHANNELFLAG_COLOR* | Color sampling is enabled. |
| *FIELDLAYER_CHANNELFLAG_DIRECTION* | Direction sampling is enabled. |
| *FIELDLAYER_CHANNELFLAG_ROTATION* | Rotation sampling is enabled. |

### Identity <a id="c4d.modules.mograph.FieldLayer-method-Identity"></a>

#### `FieldLayer.GetUniqueID(self)` <a id="c4d.modules.mograph.FieldLayer.GetUniqueID"></a>

Private.

#### `FieldLayer.SetUniqueID(self, id)` <a id="c4d.modules.mograph.FieldLayer.SetUniqueID"></a>

Private.

### Layer Flags <a id="c4d.modules.mograph.FieldLayer-method-Layer-Flags"></a>

#### `FieldLayer.GetLayerFlags(self)` <a id="c4d.modules.mograph.FieldLayer.GetLayerFlags"></a>

Gets the layer’s execution and display *flags*.

**Return type:** int

**Returns:**

The layer flags:

|   |   |
|---|---|
| *FIELDLAYER_FLAG_NONE* | None. |
| *FIELDLAYER_FLAG_SKIP* | Layer calculation is disabled, e.g. the linked object on a standard layer’s deform mode is false. |
| *FIELDLAYER_FLAG_ERRORSKIP* | Layer calculation is disabled due to a non critical error in [`InitSampling()`](#c4d.modules.mograph.FieldLayer.InitSampling) or as user specified. |
| *FIELDLAYER_FLAG_HIDE* | Layer should be completely ignored from both calculation and GUI display, e.g. the linked object has been deleted. |
| *FIELDLAYER_FLAG_MODIFYDATA* | The layer modifies existing data and needs the values from layers beneath it in the layer list. |
| *FIELDLAYER_FLAG_PRESERVEALPHA* | The layer does not adjust the existing alpha and its color changes should be applied ignoring any alpha values. |
| *FIELDLAYER_FLAG_NOCHILDVALUE* | Children of the layer do not output their value. |
| *FIELDLAYER_FLAG_NOCHILDCOLOR* | Children of the layer do not output their color. |
| *FIELDLAYER_FLAG_NOCHILDDIRECTION* | Children of the layer do not output their direction. |
| *FIELDLAYER_FLAG_NOCHILDROTATION* | Children of the layer do not output their rotation. |
| *FIELDLAYER_FLAG_TEMPORARY* | Do not save the layer with the list or duplicate it (outside of undo). |

#### `FieldLayer.SetLayerFlags(self, flags, state=True)` <a id="c4d.modules.mograph.FieldLayer.SetLayerFlags"></a>

Sets the layer’s execution and display *flags*.

**Parameters:**

- **flags** (*int*) –

  The layer flag to set:

  |   |   |
  |---|---|
  | *FIELDLAYER_FLAG_NONE* | None. |
  | *FIELDLAYER_FLAG_SKIP* | Layer calculation is disabled, e.g. the linked object on a standard layer’s deform mode is false. |
  | *FIELDLAYER_FLAG_ERRORSKIP* | Layer calculation is disabled due to a non critical error in [`InitSampling()`](#c4d.modules.mograph.FieldLayer.InitSampling) or as user specified. |
  | *FIELDLAYER_FLAG_HIDE* | Layer should be completely ignored from both calculation and GUI display, e.g. the linked object has been deleted. |
  | *FIELDLAYER_FLAG_MODIFYDATA* | The layer modifies existing data and needs the values from layers beneath it in the layer list. |
  | *FIELDLAYER_FLAG_PRESERVEALPHA* | The layer does not adjust the existing alpha and its color changes should be applied ignoring any alpha values. |
  | *FIELDLAYER_FLAG_NOCHILDVALUE* | Children of the layer do not output their value. |
  | *FIELDLAYER_FLAG_NOCHILDCOLOR* | Children of the layer do not output their color. |
  | *FIELDLAYER_FLAG_NOCHILDDIRECTION* | Children of the layer do not output their direction. |
  | *FIELDLAYER_FLAG_NOCHILDROTATION* | Children of the layer do not output their rotation. |
  | *FIELDLAYER_FLAG_TEMPORARY* | Do not save the layer with the list or duplicate it (outside of undo). |

- **state** (*bool*) – **True** to set, **False** to clear.

### Linked Object <a id="c4d.modules.mograph.FieldLayer-method-Linked-Object"></a>

#### `FieldLayer.GetLinkedObject(self, doc)` <a id="c4d.modules.mograph.FieldLayer.GetLinkedObject"></a>

Gets the linked object.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document the [`FieldLayer`](#c4d.modules.mograph.FieldLayer) belongs to.

**Return type:** [c4d.BaseList2D](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

**Returns:** The linked object.

#### `FieldLayer.SetLinkedObject(self, link)` <a id="c4d.modules.mograph.FieldLayer.SetLinkedObject"></a>

Sets the linked object.

**Parameters:** **link** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The object to link.

### Magic Methods <a id="c4d.modules.mograph.FieldLayer-method-Magic-Methods"></a>

#### `FieldLayer.__init__(self, type)` <a id="c4d.modules.mograph.FieldLayer.__init__"></a>

Creates a [`FieldLayer`](#c4d.modules.mograph.FieldLayer) instance.

**Parameters:** **type** (*int*) – The layer type.

### Masks <a id="c4d.modules.mograph.FieldLayer-method-Masks"></a>

#### `FieldLayer.AddMask(self)` <a id="c4d.modules.mograph.FieldLayer.AddMask"></a>

Adds a mask to the `c4d.FieldLayer`, if a mask already exists then this will do nothing.

**Return type:** bool

**Returns:** **True** on success.

#### `FieldLayer.GetMaskHead(self)` <a id="c4d.modules.mograph.FieldLayer.GetMaskHead"></a>

If the `c4d.FieldLayer` has a mask then this retrieve the list head containing the mask layers.

**Return type:** Optional[[c4d.GeListHead](../../../c4d/C4DAtom/GeListNode/GeListHead/index.md#c4d.GeListHead)]

**Returns:** The GeListHead containing the mask layers, **None** if masks aren’t active on this layer.

#### `FieldLayer.RemoveMask(self, link)` <a id="c4d.modules.mograph.FieldLayer.RemoveMask"></a>

Removes the mask on the `c4d.FieldLayer`, if no mask exists then this will do nothing.

> **Note:** In c++ the parameter *link* is named *deleteLayers*, it’s probable that it will change as well in Python.

**Parameters:** **link** (*bool*) – **True** to delete the layers in the mask, **False** to retain them so that when enabled again via `c4d.AddMask()` the layers will reappear.

### Sampling <a id="c4d.modules.mograph.FieldLayer-method-Sampling"></a>

#### `FieldLayer.Aggregate(self, input, output, info)` <a id="c4d.modules.mograph.FieldLayer.Aggregate"></a>

Private

#### `FieldLayer.FreeSampling(self, info)` <a id="c4d.modules.mograph.FieldLayer.FreeSampling"></a>

Frees any data allocated in [`InitSampling()`](#c4d.modules.mograph.FieldLayer.InitSampling).

> **Warning:** Must be called after sampling is finished.

> **Warning:**
>
> Due to core changes in 2024.0.0, this function is not working in Python 2024.0.0.  
> This is going to be fixed in an upcoming version.

**Parameters:** **info** ([*c4d.modules.mograph.FieldInfo*](../FieldInfo/index.md#c4d.modules.mograph.FieldInfo)) – The [`FieldInfo`](../FieldInfo/index.md#c4d.modules.mograph.FieldInfo) instance used for sampling.

#### `FieldLayer.InitSampling(self, info)` <a id="c4d.modules.mograph.FieldLayer.InitSampling"></a>

Initializes field sampling.

> **Warning:** Must be called before [`Sample()`](#c4d.modules.mograph.FieldLayer.Sample) is invoked.

**Parameters:** **info** ([*c4d.modules.mograph.FieldInfo*](../FieldInfo/index.md#c4d.modules.mograph.FieldInfo)) – The [`FieldInfo`](../FieldInfo/index.md#c4d.modules.mograph.FieldInfo) to initialize sampling with.

#### `FieldLayer.Sample(self, input, output, info)` <a id="c4d.modules.mograph.FieldLayer.Sample"></a>

Samples the field layer.

> **Warning:** [`InitSampling()`](#c4d.modules.mograph.FieldLayer.InitSampling) must be called before. [`FreeSampling()`](#c4d.modules.mograph.FieldLayer.FreeSampling) must be called once sampling is complete.

> **Warning:**
>
> Due to core changes in 2024.0.0, this function is not working in Python 2024.0.0.  
> This is going to be fixed in an upcoming version.

**Parameters:**

- **input** ([*c4d.modules.mograph.FieldInput*](../FieldInput/index.md#c4d.modules.mograph.FieldInput)) – The points to sample in global space.
- **output** (*c4d..modules.mograph.FieldOutputBlock*) – The output result values, should be allocated prior to usage.
- **info** ([*c4d.modules.mograph.FieldInfo*](../FieldInfo/index.md#c4d.modules.mograph.FieldInfo)) – The [`FieldInfo`](../FieldInfo/index.md#c4d.modules.mograph.FieldInfo) to sample with. It should match the info used with [`InitSampling()`](#c4d.modules.mograph.FieldLayer.InitSampling).

### Strength And Blending <a id="c4d.modules.mograph.FieldLayer-method-Strength-And-Blending"></a>

#### `FieldLayer.GetBlendingMode(self)` <a id="c4d.modules.mograph.FieldLayer.GetBlendingMode"></a>

Gets the field layer’s blending mode.

**Return type:** int

**Returns:** The blending mode. See *flbase.h/res* for values.

#### `FieldLayer.GetStrength(self)` <a id="c4d.modules.mograph.FieldLayer.GetStrength"></a>

Gets the field layer’s strength in percent.

**Return type:** float

**Returns:** The strength.

#### `FieldLayer.SetBlendingMode(self, blendingMode)` <a id="c4d.modules.mograph.FieldLayer.SetBlendingMode"></a>

Sets field layer’s blending mode.

**Parameters:** **blendingMode** (*int*) – The blending mode to set. See *flbase.h/res* for values.

#### `FieldLayer.SetStrength(self, strength)` <a id="c4d.modules.mograph.FieldLayer.SetStrength"></a>

Sets the field layer’s strength in percent.

**Parameters:** **strength** (*float*) – The strength to set.
