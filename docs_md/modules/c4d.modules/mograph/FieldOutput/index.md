<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/mograph/FieldOutput/index.html -->

# c4d.modules.mograph.FieldOutput <a id="c4d-modules-mograph-fieldoutput"></a>

## *class* `c4d.modules.mograph.FieldOutput` <a id="c4d.modules.mograph.FieldOutput"></a>

*New in version R20.*

**Attributes**

## `c4d.modules.mograph.FieldOutput._value` <a id="c4d.modules.mograph.FieldOutput._value"></a>

The weight value array.

**Type:** List[float]

## `c4d.modules.mograph.FieldOutput._alpha` <a id="c4d.modules.mograph.FieldOutput._alpha"></a>

The alpha array for color and direction. Only available when color or direction are allocated.

**Type:** List[float]

## `c4d.modules.mograph.FieldOutput._color` <a id="c4d.modules.mograph.FieldOutput._color"></a>

The color array.

**Type:** List[c4d.Vector]

## `c4d.modules.mograph.FieldOutput._direction` <a id="c4d.modules.mograph.FieldOutput._direction"></a>

The slope direction array.

**Type:** List[c4d.Vector]

## `c4d.modules.mograph.FieldOutput._rotation` <a id="c4d.modules.mograph.FieldOutput._rotation"></a>

The rotational velocity array.

**Type:** List[c4d.Vector]

## `c4d.modules.mograph.FieldOutput._pivot` <a id="c4d.modules.mograph.FieldOutput._pivot"></a>

The rotational velocity (axe + magnitude)

**Type:** List[c4d.Vector]

## `c4d.modules.mograph.FieldOutput._deactivated` <a id="c4d.modules.mograph.FieldOutput._deactivated"></a>

The deactivated state array.

**Type:** List[bool]

## Overview <a id="overview"></a>

- [`FieldOutput.Create()`](#c4d.modules.mograph.FieldOutput.Create): Creates a [`FieldOutput`](#c4d.modules.mograph.FieldOutput) with the specified sampling arrays.

**Construction And Access**

- [`FieldOutput.GetBlock()`](#c4d.modules.mograph.FieldOutput.GetBlock): Retrieves all arrays in a [`FieldOutputBlock`](../FieldOutputBlock/index.md#c4d.modules.mograph.FieldOutputBlock).
- [`FieldOutput.GetSubBlock()`](#c4d.modules.mograph.FieldOutput.GetSubBlock): Gets a sub-section of the sampling arrays.

**Copying**

- [`FieldOutput.CopyArrayContentFrom()`](#c4d.modules.mograph.FieldOutput.CopyArrayContentFrom): Copies from *src* array content.
- [`FieldOutput.CopyFrom()`](#c4d.modules.mograph.FieldOutput.CopyFrom): Copies from [`FieldOutput`](#c4d.modules.mograph.FieldOutput) *src*. Performs a deep copy.

**Magic Methods**

- [`FieldOutput.__init__()`](#c4d.modules.mograph.FieldOutput.__init__): Creates a [`FieldOutput`](#c4d.modules.mograph.FieldOutput) instance.

**Memory Management**

- [`FieldOutput.ClearDeactivated()`](#c4d.modules.mograph.FieldOutput.ClearDeactivated): Clears the deactivated array.
- [`FieldOutput.ClearMemory()`](#c4d.modules.mograph.FieldOutput.ClearMemory): Resets the sampling data to default values.
- [`FieldOutput.Flush()`](#c4d.modules.mograph.FieldOutput.Flush): Flushes the [`FieldOutput`](#c4d.modules.mograph.FieldOutput) instance, keeping the arrays allocated for future resize.
- [`FieldOutput.Reset()`](#c4d.modules.mograph.FieldOutput.Reset): Resets the [`FieldOutput`](#c4d.modules.mograph.FieldOutput) instance to an empty state.
- [`FieldOutput.Resize()`](#c4d.modules.mograph.FieldOutput.Resize): Resizes the arrays held in the FieldOutput.

**Sample Channels**

- [`FieldOutput.GetAlpha()`](#c4d.modules.mograph.FieldOutput.GetAlpha): Reads alpha at specified *index*.
- [`FieldOutput.GetColor()`](#c4d.modules.mograph.FieldOutput.GetColor): Reads color at specified *index*.
- [`FieldOutput.GetDeactivated()`](#c4d.modules.mograph.FieldOutput.GetDeactivated): Reads deactivated state at specified *index*.
- [`FieldOutput.GetDirection()`](#c4d.modules.mograph.FieldOutput.GetDirection): Reads direction at specified *index*.
- [`FieldOutput.GetPivot()`](#c4d.modules.mograph.FieldOutput.GetPivot): Retrieve the rotational velocity (axe + magnitude) at specified *index*.
- [`FieldOutput.GetRotation()`](#c4d.modules.mograph.FieldOutput.GetRotation): Reads rotation at specified *index*.
- [`FieldOutput.GetValue()`](#c4d.modules.mograph.FieldOutput.GetValue): Reads value at specified *index*.
- [`FieldOutput.SetAlpha()`](#c4d.modules.mograph.FieldOutput.SetAlpha): Writes alpha at specified *index*.
- [`FieldOutput.SetColor()`](#c4d.modules.mograph.FieldOutput.SetColor): Writes color at specified *index*.
- [`FieldOutput.SetDeactivated()`](#c4d.modules.mograph.FieldOutput.SetDeactivated): Writes deactivated state at specified *index*.
- [`FieldOutput.SetDirection()`](#c4d.modules.mograph.FieldOutput.SetDirection): Writes direction at specified *index*.
- [`FieldOutput.SetRotation()`](#c4d.modules.mograph.FieldOutput.SetRotation): Writes rotation at specified *index*.
- [`FieldOutput.SetValue()`](#c4d.modules.mograph.FieldOutput.SetValue): Writes value at specified *index*.

**State And Validation**

- [`FieldOutput.CalculateCrc()`](#c4d.modules.mograph.FieldOutput.CalculateCrc): Calculates a Crc on all internal data.
- [`FieldOutput.GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount): Returns the number of elements in the sample arrays.
- [`FieldOutput.IsPopulated()`](#c4d.modules.mograph.FieldOutput.IsPopulated): Checks if the [`FieldOutput`](#c4d.modules.mograph.FieldOutput) is valid and non-empty.
- [`FieldOutput.IsValid()`](#c4d.modules.mograph.FieldOutput.IsValid): Checks if the [`FieldOutput`](#c4d.modules.mograph.FieldOutput) instance allocations and sizes are valid.

## Members <a id="members"></a>

### Construction And Access <a id="c4d.modules.mograph.FieldOutput-staticmethod-Construction-And-Access"></a>

#### *static* `FieldOutput.Create(size, flags=3, src=None)` <a id="c4d.modules.mograph.FieldOutput.Create"></a>

Creates a [`FieldOutput`](#c4d.modules.mograph.FieldOutput) with the specified sampling arrays.

**Parameters:**

- **size** (*int*) – The size.

- **flags** (*int*) –

  The flags:

  |   |   |
  |---|---|
  | *FIELDSAMPLE_FLAG_VALUE* | Sample only the value. |
  | *FIELDSAMPLE_FLAG_DIRECTION* | Sample the velocity. |
  | *FIELDSAMPLE_FLAG_COLOR* | Sample the color. |
  | *FIELDSAMPLE_FLAG_ROTATION* | Sample the rotational velocity. |

- **src** (*Optional*[[*c4d.modules.mograph.FieldOutputBlock*](../FieldOutputBlock/index.md#c4d.modules.mograph.FieldOutputBlock)]) – Alternatively pass only a source [`FieldOutputBlock`](../FieldOutputBlock/index.md#c4d.modules.mograph.FieldOutputBlock) to copy its size and arrays.

**Return type:** [c4d.modules.mograph.FieldOutput](#c4d.modules.mograph.FieldOutput)

**Returns:** The created [`FieldOutput`](#c4d.modules.mograph.FieldOutput) instance.

### Construction And Access <a id="c4d.modules.mograph.FieldOutput-method-Construction-And-Access"></a>

#### `FieldOutput.GetBlock(self)` <a id="c4d.modules.mograph.FieldOutput.GetBlock"></a>

Retrieves all arrays in a [`FieldOutputBlock`](../FieldOutputBlock/index.md#c4d.modules.mograph.FieldOutputBlock).

**Return type:** [c4d.modules.mograph.FieldOutputBlock](../FieldOutputBlock/index.md#c4d.modules.mograph.FieldOutputBlock)

**Returns:** A sub-block for the whole [`FieldOutput`](#c4d.modules.mograph.FieldOutput).

#### `FieldOutput.GetSubBlock(self, offset, size)` <a id="c4d.modules.mograph.FieldOutput.GetSubBlock"></a>

Gets a sub-section of the sampling arrays.

**Parameters:**

- **offset** (*int*) – The offset index to retrieve a sub-block starting at.
- **size** (*int*) – The suggested size of the block. Note the function clamps the size against the maximum number of entries.

**Return type:** [c4d.modules.mograph.FieldOutputBlock](../FieldOutputBlock/index.md#c4d.modules.mograph.FieldOutputBlock)

**Returns:** The requested sub-block.

### Copying <a id="c4d.modules.mograph.FieldOutput-method-Copying"></a>

#### `FieldOutput.CopyArrayContentFrom(self, src)` <a id="c4d.modules.mograph.FieldOutput.CopyArrayContentFrom"></a>

Copies from *src* array content.

> **Note:**
>
> Size and flags are not affected by [`CopyArrayContentFrom()`](#c4d.modules.mograph.FieldOutput.CopyArrayContentFrom).  
> Source data is copied into target up to current size. If target is bigger than source, the remaining items are cleared.

**Parameters:** **src** (*Union*[[*c4d.modules.mograph.FieldOutput*](#c4d.modules.mograph.FieldOutput), [*c4d.modules.mograph.FieldOutputBlock*](../FieldOutputBlock/index.md#c4d.modules.mograph.FieldOutputBlock)]) – The source [`FieldOutput`](#c4d.modules.mograph.FieldOutput) or [`FieldOutputBlock`](../FieldOutputBlock/index.md#c4d.modules.mograph.FieldOutputBlock).

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `FieldOutput.CopyFrom(self, src)` <a id="c4d.modules.mograph.FieldOutput.CopyFrom"></a>

Copies from [`FieldOutput`](#c4d.modules.mograph.FieldOutput) *src*. Performs a deep copy.

**Parameters:** **src** ([*c4d.modules.mograph.FieldOutput*](#c4d.modules.mograph.FieldOutput)) – The source [`FieldOutput`](#c4d.modules.mograph.FieldOutput).

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Magic Methods <a id="c4d.modules.mograph.FieldOutput-method-Magic-Methods"></a>

#### `FieldOutput.__init__(self)` <a id="c4d.modules.mograph.FieldOutput.__init__"></a>

Creates a [`FieldOutput`](#c4d.modules.mograph.FieldOutput) instance.

### Memory Management <a id="c4d.modules.mograph.FieldOutput-method-Memory-Management"></a>

#### `FieldOutput.ClearDeactivated(self, state=False)` <a id="c4d.modules.mograph.FieldOutput.ClearDeactivated"></a>

Clears the deactivated array.

**Parameters:** **state** (*bool*) – The state the deactivated array should be cleared to.

#### `FieldOutput.ClearMemory(self, startIdx=0, count=<function FieldOutput.GetCount at 0x0000012ECE95E250>, deactivatedOnly=False, deactivatedState=False)` <a id="c4d.modules.mograph.FieldOutput.ClearMemory"></a>

Resets the sampling data to default values.

> **Note:** Values are reset to *0*, colors to *1.0*, direction to *0*, deactivated to *0*.

**Parameters:**

- **startIdx** (*int*) – The index to start at.
- **count** (*int*) – The number of array elements to reset to default value.
- **deactivatedOnly** (*bool*) – **True** to clear deactivated only, otherwise **False**.
- **deactivatedState** (*bool*) – The state the deactivated array should be cleared to.

#### `FieldOutput.Flush(self)` <a id="c4d.modules.mograph.FieldOutput.Flush"></a>

Flushes the [`FieldOutput`](#c4d.modules.mograph.FieldOutput) instance, keeping the arrays allocated for future resize.

#### `FieldOutput.Reset(self)` <a id="c4d.modules.mograph.FieldOutput.Reset"></a>

Resets the [`FieldOutput`](#c4d.modules.mograph.FieldOutput) instance to an empty state.

> **Note:** All memory is deallocated.

#### `FieldOutput.Resize(self, newSize, sampleFlags=0, resizeFlags=2)` <a id="c4d.modules.mograph.FieldOutput.Resize"></a>

Resizes the arrays held in the FieldOutput.

> > **Note:** Unspecified channel arrays are resized to *0* length according to *resizeFlags*.

**Parameters:**

- **newSize** (*int*) – The new size for the arrays.

- **sampleFlags** (*int*) –

  The channels to sample:

- **resizeFlags** (*int*) – The flags for the resize.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Sample Channels <a id="c4d.modules.mograph.FieldOutput-method-Sample-Channels"></a>

#### `FieldOutput.GetAlpha(self, index)` <a id="c4d.modules.mograph.FieldOutput.GetAlpha"></a>

Reads alpha at specified *index*.

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount).

**Return type:** float

**Returns:** The alpha.

#### `FieldOutput.GetColor(self, index)` <a id="c4d.modules.mograph.FieldOutput.GetColor"></a>

Reads color at specified *index*.

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The color.

#### `FieldOutput.GetDeactivated(self, index)` <a id="c4d.modules.mograph.FieldOutput.GetDeactivated"></a>

Reads deactivated state at specified *index*.

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount).

**Return type:** bool

**Returns:** The deactivated state.

#### `FieldOutput.GetDirection(self, index)` <a id="c4d.modules.mograph.FieldOutput.GetDirection"></a>

Reads direction at specified *index*.

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The direction.

#### `FieldOutput.GetPivot(self, index)` <a id="c4d.modules.mograph.FieldOutput.GetPivot"></a>

Retrieve the rotational velocity (axe + magnitude) at specified *index*.

*New in version R21.*

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The rotational velocity (axe + magnitude).

#### `FieldOutput.GetRotation(self, index)` <a id="c4d.modules.mograph.FieldOutput.GetRotation"></a>

Reads rotation at specified *index*.

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The rotation.

#### `FieldOutput.GetValue(self, index)` <a id="c4d.modules.mograph.FieldOutput.GetValue"></a>

Reads value at specified *index*.

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount).

**Return type:** float

**Returns:** The value.

#### `FieldOutput.SetAlpha(self, index, alpha)` <a id="c4d.modules.mograph.FieldOutput.SetAlpha"></a>

Writes alpha at specified *index*.

**Parameters:**

- **index** (*int*) – The index in the array.
- **alpha** (*float*) – The alpha to set.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount).

#### `FieldOutput.SetColor(self, index, color)` <a id="c4d.modules.mograph.FieldOutput.SetColor"></a>

Writes color at specified *index*.

**Parameters:**

- **index** (*int*) – The index in the array.
- **color** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The color to set.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount).

#### `FieldOutput.SetDeactivated(self, index, deact)` <a id="c4d.modules.mograph.FieldOutput.SetDeactivated"></a>

Writes deactivated state at specified *index*.

**Parameters:**

- **index** (*int*) – The index in the array.
- **deact** (*bool*) – The deactivated state to set.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount).

#### `FieldOutput.SetDirection(self, index, direction)` <a id="c4d.modules.mograph.FieldOutput.SetDirection"></a>

Writes direction at specified *index*.

**Parameters:**

- **index** (*int*) – The index in the array.
- **direction** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The direction to set.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount).

#### `FieldOutput.SetRotation(self, index, rotation, pivot)` <a id="c4d.modules.mograph.FieldOutput.SetRotation"></a>

Writes rotation at specified *index*.

*Changed in version R21.*

**Parameters:**

- **index** (*int*) – The index in the array.
- **rotation** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The rotation to set.
- **pivot** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The rotational velocity.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount).

#### `FieldOutput.SetValue(self, index, value)` <a id="c4d.modules.mograph.FieldOutput.SetValue"></a>

Writes value at specified *index*.

**Parameters:**

- **index** (*int*) – The index in the array.
- **value** (*float*) – The value to set.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutput.GetCount).

### State And Validation <a id="c4d.modules.mograph.FieldOutput-method-State-And-Validation"></a>

#### `FieldOutput.CalculateCrc(self)` <a id="c4d.modules.mograph.FieldOutput.CalculateCrc"></a>

Calculates a Crc on all internal data.

> **Note:** Crc is not kept internally and is calculated from scratch on each [`CalculateCrc()`](#c4d.modules.mograph.FieldOutput.CalculateCrc) call.

**Return type:** int

**Returns:** The calculated Crc.

#### `FieldOutput.GetCount(self)` <a id="c4d.modules.mograph.FieldOutput.GetCount"></a>

Returns the number of elements in the sample arrays.

**Return type:** int

**Returns:** The number of elements.

#### `FieldOutput.IsPopulated(self)` <a id="c4d.modules.mograph.FieldOutput.IsPopulated"></a>

Checks if the [`FieldOutput`](#c4d.modules.mograph.FieldOutput) is valid and non-empty.

**Return type:** bool

**Returns:** **True** if the [`FieldOutput`](#c4d.modules.mograph.FieldOutput) instance is populated, otherwise **False**.

#### `FieldOutput.IsValid(self)` <a id="c4d.modules.mograph.FieldOutput.IsValid"></a>

Checks if the [`FieldOutput`](#c4d.modules.mograph.FieldOutput) instance allocations and sizes are valid.

> **Note:** An empty [`FieldOutput`](#c4d.modules.mograph.FieldOutput) instance is considered valid.

**Return type:** bool

**Returns:** **True** if the [`FieldOutput`](#c4d.modules.mograph.FieldOutput) instance is valid, otherwise **False**.
