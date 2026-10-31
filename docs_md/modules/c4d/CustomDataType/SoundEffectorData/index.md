<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/SoundEffectorData/index.html -->

# c4d.SoundEffectorData <a id="c4d-soundeffectordata"></a>

## *class* `c4d.SoundEffectorData` <a id="c4d.SoundEffectorData"></a>

Sound effector data type (*CUSTOMDATATYPE_SOUNDEFFECTOR*) for [`SoundEffectorCustomGui`](../../../c4d.gui/BaseCustomGui/SoundEffectorCustomGui/index.md#c4d.gui.SoundEffectorCustomGui).

*New in version R19.*

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Magic Methods**

- [`SoundEffectorData.__init__()`](#c4d.SoundEffectorData.__init__): Creates a [`c4d.SoundEffectorData`](#c4d.SoundEffectorData).

**Probe Management**

- [`SoundEffectorData.CreateProbe()`](#c4d.SoundEffectorData.CreateProbe): Creates a probe.
- [`SoundEffectorData.DeleteProbe()`](#c4d.SoundEffectorData.DeleteProbe): Deletes the probe at the specified *index*.
- [`SoundEffectorData.GetProbe()`](#c4d.SoundEffectorData.GetProbe): Retrieves the probe at the specified *index*.
- [`SoundEffectorData.GetProbeCount()`](#c4d.SoundEffectorData.GetProbeCount): Retrieves the number of probes owned by the sound effector data.
- [`SoundEffectorData.SetProbe()`](#c4d.SoundEffectorData.SetProbe): Sets the probe at the specified *index*.
- [`SoundEffectorData.UpdateProbeOrder()`](#c4d.SoundEffectorData.UpdateProbeOrder): Updates the probes.

**Range And Blending**

- [`SoundEffectorData.GetLinLog()`](#c4d.SoundEffectorData.GetLinLog): Retrieves the blend value for the linear/logarithmic slider.
- [`SoundEffectorData.GetRange()`](#c4d.SoundEffectorData.GetRange): Retrieves the range of the sound effector data.
- [`SoundEffectorData.SetLinLog()`](#c4d.SoundEffectorData.SetLinLog): Sets the blend value for the linear/logarithmic slider.
- [`SoundEffectorData.SetRange()`](#c4d.SoundEffectorData.SetRange): Sets the range of the sound effector data.

**Sampling And Data Operations**

- [`SoundEffectorData.CopyTo()`](#c4d.SoundEffectorData.CopyTo): Copies the sound effector data.
- [`SoundEffectorData.FreeSampling()`](#c4d.SoundEffectorData.FreeSampling): Frees the memory used for sampling.
- [`SoundEffectorData.InitSampling()`](#c4d.SoundEffectorData.InitSampling): Initializes the sampling functionality of the sound effector data.
- [`SoundEffectorData.Sample()`](#c4d.SoundEffectorData.Sample): Samples the sound file using the probes.

**Soundtrack Selection**

- [`SoundEffectorData.GetActiveSoundTrack()`](#c4d.SoundEffectorData.GetActiveSoundTrack): Retrieves the active sound track.
- [`SoundEffectorData.SetActiveSoundTrack()`](#c4d.SoundEffectorData.SetActiveSoundTrack): Sets the active sound track.

**State And Gradient**

- [`SoundEffectorData.GetFreeze()`](#c4d.SoundEffectorData.GetFreeze): Retrieves the freeze state.
- [`SoundEffectorData.GetGradient()`](#c4d.SoundEffectorData.GetGradient): Retrieves the global gradient.
- [`SoundEffectorData.GetGradientDirection()`](#c4d.SoundEffectorData.GetGradientDirection): Retrieves the global gradient direction.
- [`SoundEffectorData.SetFreeze()`](#c4d.SoundEffectorData.SetFreeze): Sets the freeze state.
- [`SoundEffectorData.SetGradientDirection()`](#c4d.SoundEffectorData.SetGradientDirection): Sets the global gradient direction.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.SoundEffectorData-method-Magic-Methods"></a>

#### `SoundEffectorData.__init__(self, v)` <a id="c4d.SoundEffectorData.__init__"></a>

Creates a [`c4d.SoundEffectorData`](#c4d.SoundEffectorData).

**Parameters:** **v** ([*c4d.SoundEffectorData*](#c4d.SoundEffectorData)) – An optional [`c4d.SoundEffectorData`](#c4d.SoundEffectorData) to copy.

### Probe Management <a id="c4d.SoundEffectorData-method-Probe-Management"></a>

#### `SoundEffectorData.CreateProbe(self, left, right, top, bottom, selected=False)` <a id="c4d.SoundEffectorData.CreateProbe"></a>

Creates a probe.

**Parameters:**

- **left** (*float*) – The left side of the probe in Hertz *[1,22050]*.
- **right** (*float*) – The right side of the probe in Hertz *[1,22050]*.
- **top** (*float*) – The top edge of the probe in the range *[0,1]*.
- **bottom** (*float*) – The bottom edge of the probe in the range *[0,1]*.
- **selected** (*bool*) – **True** to select the created probe. Other probes are not deselected in the operation.

**Return type:** int

**Returns:** The created probe’s index.

#### `SoundEffectorData.DeleteProbe(self, index)` <a id="c4d.SoundEffectorData.DeleteProbe"></a>

Deletes the probe at the specified *index*.

**Parameters:** **index** (*int*) – The index of the probe to delete.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SoundEffectorData.GetProbe(self, index)` <a id="c4d.SoundEffectorData.GetProbe"></a>

Retrieves the probe at the specified *index*.

**Parameters:** **index** (*int*) – The probe index.

**Return type:** Optional[dict]

**Returns:**

The probe, or **None** if the function fails. The dictionary contains the following data:

|   |   |   |
|---|---|---|
| *left* | float | The left value of probe in Hertz. |
| *right* | float | The right value of probe in Hertz. |
| *top* | float | The top value of probe in Hertz. |
| *bottom* | float | The bottom value of probe in Hertz. |
| *strength* | float | The overall strength multiplier for the probe. |
| *clamp* | bool | **True** limits the output of the probe from *0.0* to *1.0* and ignores values outside of the range. |
| *samplingMode* | int | The probe mode. |
| *colorMode* | int | The color mode. |
| *color* | [`c4d.Vector`](../../Vector/index.md#c4d.Vector) | The color of the probe used when *colorMode* is Custom Color. |
| *gradient* | [`c4d.Gradient`](../Gradient/index.md#c4d.Gradient) | The gradient of the probe used when *colorMode* is Custom Gradient. |

#### `SoundEffectorData.GetProbeCount(self)` <a id="c4d.SoundEffectorData.GetProbeCount"></a>

Retrieves the number of probes owned by the sound effector data.

**Return type:** int

**Returns:** The probe count.

#### `SoundEffectorData.SetProbe(self, index, probe)` <a id="c4d.SoundEffectorData.SetProbe"></a>

Sets the probe at the specified *index*.

**Parameters:**

- **index** (*int*) – The index of the probe to set.

- **probe** (*dict*) –

  The probe data to set:

  |   |   |   |
  |---|---|---|
  | *left* | float | The left value of probe in Hertz. |
  | *right* | float | The right value of probe in Hertz. |
  | *top* | float | The top value of probe in Hertz. |
  | *bottom* | float | The bottom value of probe in Hertz. |
  | *strength* | float | The overall strength multiplier for the probe. |
  | *clamp* | bool | Set to **True** to limit the output of the probe from *0.0* to *1.0* and to ignore values outside of the range. |
  | *samplingMode* | int | The probe mode. |
  | *colorMode* | int | The color mode. |
  | *color* | [`c4d.Vector`](../../Vector/index.md#c4d.Vector) | The color of the probe used when *colorMode* is Custom Color. |
  | *gradient* | [`c4d.Gradient`](../Gradient/index.md#c4d.Gradient) | The gradient of the probe used when *colorMode* is Custom Gradient. |

#### `SoundEffectorData.UpdateProbeOrder(self)` <a id="c4d.SoundEffectorData.UpdateProbeOrder"></a>

Updates the probes.

> **Note:** Must be called after adjusting any probes left or right values to update the order that the probes are calculated in.

### Range And Blending <a id="c4d.SoundEffectorData-method-Range-And-Blending"></a>

#### `SoundEffectorData.GetLinLog(self)` <a id="c4d.SoundEffectorData.GetLinLog"></a>

Retrieves the blend value for the linear/logarithmic slider.

**Return type:** float

**Returns:** The blend percentage: *0%* = linear, *100%* = log10.

#### `SoundEffectorData.GetRange(self)` <a id="c4d.SoundEffectorData.GetRange"></a>

Retrieves the range of the sound effector data.

> **Warning:** Only valid if the data is shown in the sound sound effector GUI.

**Return type:** Tuple[float, float, float, float]

**Returns:** A tuple with the left, right, top and bottom values.

#### `SoundEffectorData.SetLinLog(self, value)` <a id="c4d.SoundEffectorData.SetLinLog"></a>

Sets the blend value for the linear/logarithmic slider.

**Parameters:** **value** (*float*) – The blend percentage to set: *0%* = linear, *100%* = log10.

#### `SoundEffectorData.SetRange(self, left, right, top, bottom)` <a id="c4d.SoundEffectorData.SetRange"></a>

Sets the range of the sound effector data.

> **Warning:** Only valid if the data is shown in the sound effector GUI.

**Parameters:**

- **left** (*float*) – The left value to set.
- **right** (*float*) – The right value to set.
- **top** (*float*) – The top value to set.
- **bottom** (*float*) – The bottom value to set.

### Sampling And Data Operations <a id="c4d.SoundEffectorData-method-Sampling-And-Data-Operations"></a>

#### `SoundEffectorData.CopyTo(self, dest)` <a id="c4d.SoundEffectorData.CopyTo"></a>

Copies the sound effector data.

**Parameters:** **dest** ([*c4d.SoundEffectorData*](#c4d.SoundEffectorData)) – The destination sound effector data.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**

#### `SoundEffectorData.FreeSampling(self)` <a id="c4d.SoundEffectorData.FreeSampling"></a>

Frees the memory used for sampling.

> **Note:** Must be invoked after [`InitSampling()`](#c4d.SoundEffectorData.InitSampling) has been called.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SoundEffectorData.InitSampling(self, doc)` <a id="c4d.SoundEffectorData.InitSampling"></a>

Initializes the sampling functionality of the sound effector data.

> **Note:** Must be called before [`Sample()`](#c4d.SoundEffectorData.Sample). [`FreeSampling()`](#c4d.SoundEffectorData.FreeSampling) must be invoked afterwards.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the operation.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SoundEffectorData.Sample(self, index, count)` <a id="c4d.SoundEffectorData.Sample"></a>

Samples the sound file using the probes.

**Parameters:**

- **index** (*int*) – The index of the element to sample.
- **count** (*int*) – The number of elements in the array being sampled.

**Return type:** Tuple[Optional[float], Optional[[c4d.Vector](../../Vector/index.md#c4d.Vector)]]

**Returns:** A tuple with the output value and color (both **None** if the function failed).

### Soundtrack Selection <a id="c4d.SoundEffectorData-method-Soundtrack-Selection"></a>

#### `SoundEffectorData.GetActiveSoundTrack(self, doc)` <a id="c4d.SoundEffectorData.GetActiveSoundTrack"></a>

Retrieves the active sound track.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the operation.

**Return type:** Optional[[c4d.CTrack](../../C4DAtom/GeListNode/BaseList2D/CTrack/index.md#c4d.CTrack)]

**Returns:** The active sound track, or **None** if the function fails.

#### `SoundEffectorData.SetActiveSoundTrack(self, track, doc)` <a id="c4d.SoundEffectorData.SetActiveSoundTrack"></a>

Sets the active sound track.

**Parameters:**

- **track** ([*c4d.CTrack*](../../C4DAtom/GeListNode/BaseList2D/CTrack/index.md#c4d.CTrack)) – The sound track to set.
- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the operation.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### State And Gradient <a id="c4d.SoundEffectorData-method-State-And-Gradient"></a>

#### `SoundEffectorData.GetFreeze(self)` <a id="c4d.SoundEffectorData.GetFreeze"></a>

Retrieves the freeze state.

**Return type:** bool

**Returns:** **True** if freeze is enabled, otherwise **False**.

#### `SoundEffectorData.GetGradient(self)` <a id="c4d.SoundEffectorData.GetGradient"></a>

Retrieves the global gradient.

**Return type:** Optional[[c4d.Gradient](../Gradient/index.md#c4d.Gradient)]

**Returns:** The global gradient, or **None** if the function fails.

#### `SoundEffectorData.GetGradientDirection(self)` <a id="c4d.SoundEffectorData.GetGradientDirection"></a>

Retrieves the global gradient direction.

**Return type:** int

**Returns:** The global gradient direction: *0* for vertical (volume), *1* for horizontal (frequency).

#### `SoundEffectorData.SetFreeze(self, freeze)` <a id="c4d.SoundEffectorData.SetFreeze"></a>

Sets the freeze state.

**Parameters:** **freeze** (*bool*) – **True** to enable freeze, otherwise **False**.

#### `SoundEffectorData.SetGradientDirection(self, direction)` <a id="c4d.SoundEffectorData.SetGradientDirection"></a>

Sets the global gradient direction.

**Parameters:** **direction** (*int*) – The global gradient direction to set: *0* for vertical (volume), *1* for horizontal (frequency).
