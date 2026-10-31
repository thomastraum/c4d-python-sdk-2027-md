<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/mograph/FieldOutputBlock/index.html -->

# c4d.modules.mograph.FieldOutputBlock <a id="c4d-modules-mograph-fieldoutputblock"></a>

## *class* `c4d.modules.mograph.FieldOutputBlock` <a id="c4d.modules.mograph.FieldOutputBlock"></a>

*New in version R20.*

**Attributes**

## `c4d.modules.mograph.FieldOutputBlock._value` <a id="c4d.modules.mograph.FieldOutputBlock._value"></a>

The weight value array.

**Type:** List[float]

## `c4d.modules.mograph.FieldOutputBlock._alpha` <a id="c4d.modules.mograph.FieldOutputBlock._alpha"></a>

The alpha array for color and direction. Only available when color or direction are allocated.

**Type:** List[float]

## `c4d.modules.mograph.FieldOutputBlock._color` <a id="c4d.modules.mograph.FieldOutputBlock._color"></a>

The color array.

**Type:** List[c4d.Vector]

## `c4d.modules.mograph.FieldOutputBlock._direction` <a id="c4d.modules.mograph.FieldOutputBlock._direction"></a>

The slope direction array.

**Type:** List[c4d.Vector]

## `c4d.modules.mograph.FieldOutputBlock._rotation` <a id="c4d.modules.mograph.FieldOutputBlock._rotation"></a>

The rotational velocity array.

**Type:** List[c4d.Vector]

## `c4d.modules.mograph.FieldOutputBlock._pivot` <a id="c4d.modules.mograph.FieldOutputBlock._pivot"></a>

The rotational velocity (axe + magnitude)

**Type:** List[c4d.Vector]

## `c4d.modules.mograph.FieldOutputBlock._deactivated` <a id="c4d.modules.mograph.FieldOutputBlock._deactivated"></a>

The deactivated state array.

**Type:** List[bool]

## Overview <a id="overview"></a>

**Copying And Integrity**

- [`FieldOutputBlock.CalculateCrc()`](#c4d.modules.mograph.FieldOutputBlock.CalculateCrc): Calculates a Crc on all internal data.
- [`FieldOutputBlock.CopyArrayContentFrom()`](#c4d.modules.mograph.FieldOutputBlock.CopyArrayContentFrom): Copies from *src* array content.
- [`FieldOutputBlock.CopyFrom()`](#c4d.modules.mograph.FieldOutputBlock.CopyFrom): Copies from [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) *src*.

**Layout And Ownership**

- [`FieldOutputBlock.GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount): Returns the number of elements in the sub-block.
- [`FieldOutputBlock.GetFullCount()`](#c4d.modules.mograph.FieldOutputBlock.GetFullCount): Returns the number of elements in the parent [`FieldOutput`](../FieldOutput/index.md#c4d.modules.mograph.FieldOutput).
- [`FieldOutputBlock.GetOffset()`](#c4d.modules.mograph.FieldOutputBlock.GetOffset): Returns the offset of the sub-block in the parent [`FieldOutput`](../FieldOutput/index.md#c4d.modules.mograph.FieldOutput).
- [`FieldOutputBlock.GetOwner()`](#c4d.modules.mograph.FieldOutputBlock.GetOwner): Returns the parent or owner [`FieldOutput`](../FieldOutput/index.md#c4d.modules.mograph.FieldOutput).
- [`FieldOutputBlock.GetSubBlock()`](#c4d.modules.mograph.FieldOutputBlock.GetSubBlock): Gets a sub-section of the sampling arrays.

**Magic Methods**

- [`FieldOutputBlock.__init__()`](#c4d.modules.mograph.FieldOutputBlock.__init__): Creates a [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) instance.

**Sample Values**

- [`FieldOutputBlock.GetAlpha()`](#c4d.modules.mograph.FieldOutputBlock.GetAlpha): Reads alpha at specified *index*.
- [`FieldOutputBlock.GetColor()`](#c4d.modules.mograph.FieldOutputBlock.GetColor): Reads color at specified *index*.
- [`FieldOutputBlock.GetValue()`](#c4d.modules.mograph.FieldOutputBlock.GetValue): Reads value at specified *index*.
- [`FieldOutputBlock.SetAlpha()`](#c4d.modules.mograph.FieldOutputBlock.SetAlpha): Writes alpha at specified *index*.
- [`FieldOutputBlock.SetColor()`](#c4d.modules.mograph.FieldOutputBlock.SetColor): Writes color at specified *index*.
- [`FieldOutputBlock.SetValue()`](#c4d.modules.mograph.FieldOutputBlock.SetValue): Writes value at specified *index*.

**Spatial Attributes**

- [`FieldOutputBlock.GetDirection()`](#c4d.modules.mograph.FieldOutputBlock.GetDirection): Reads direction at specified *index*.
- [`FieldOutputBlock.GetPivot()`](#c4d.modules.mograph.FieldOutputBlock.GetPivot): Retrieve the rotational velocity (axe + magnitude) at specified *index*.
- [`FieldOutputBlock.GetRotation()`](#c4d.modules.mograph.FieldOutputBlock.GetRotation): Reads rotation at specified *index*.
- [`FieldOutputBlock.SetDirection()`](#c4d.modules.mograph.FieldOutputBlock.SetDirection): Writes direction at specified *index*.
- [`FieldOutputBlock.SetRotation()`](#c4d.modules.mograph.FieldOutputBlock.SetRotation): Writes rotation at specified *index*.

**State Management**

- [`FieldOutputBlock.ClearDeactivated()`](#c4d.modules.mograph.FieldOutputBlock.ClearDeactivated): Clears the deactivated array.
- [`FieldOutputBlock.ClearMemory()`](#c4d.modules.mograph.FieldOutputBlock.ClearMemory): Resets the sampling data to default values.
- [`FieldOutputBlock.GetDeactivated()`](#c4d.modules.mograph.FieldOutputBlock.GetDeactivated): Reads deactivated state at specified *index*.
- [`FieldOutputBlock.IsPopulated()`](#c4d.modules.mograph.FieldOutputBlock.IsPopulated): Checks if the [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) is valid and non-empty.
- [`FieldOutputBlock.IsValid()`](#c4d.modules.mograph.FieldOutputBlock.IsValid): Checks if the [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) instance allocations and sizes are valid.
- [`FieldOutputBlock.Reset()`](#c4d.modules.mograph.FieldOutputBlock.Reset): Resets the [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) instance to an empty state.
- [`FieldOutputBlock.SetDeactivated()`](#c4d.modules.mograph.FieldOutputBlock.SetDeactivated): Writes deactivated state at specified *index*.

## Members <a id="members"></a>

### Copying And Integrity <a id="c4d.modules.mograph.FieldOutputBlock-method-Copying-And-Integrity"></a>

#### `FieldOutputBlock.CalculateCrc(self)` <a id="c4d.modules.mograph.FieldOutputBlock.CalculateCrc"></a>

Calculates a Crc on all internal data.

> **Note:** Crc is not kept internally and is calculated from scratch on each [`CalculateCrc()`](#c4d.modules.mograph.FieldOutputBlock.CalculateCrc) call.

**Return type:** int

**Returns:** The calculated Crc.

#### `FieldOutputBlock.CopyArrayContentFrom(self, src)` <a id="c4d.modules.mograph.FieldOutputBlock.CopyArrayContentFrom"></a>

Copies from *src* array content.

> **Note:**
>
> Size and flags are not affected by [`CopyArrayContentFrom()`](#c4d.modules.mograph.FieldOutputBlock.CopyArrayContentFrom).  
> The destination [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) must be big enough to accept the full content of *src*.

**Parameters:** **src** ([*c4d.modules.mograph.FieldOutputBlock*](#c4d.modules.mograph.FieldOutputBlock)) – The source [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock).

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `FieldOutputBlock.CopyFrom(self, src)` <a id="c4d.modules.mograph.FieldOutputBlock.CopyFrom"></a>

Copies from [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) *src*.

**Parameters:** **src** ([*c4d.modules.mograph.FieldOutputBlock*](#c4d.modules.mograph.FieldOutputBlock)) – The source [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock).

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Layout And Ownership <a id="c4d.modules.mograph.FieldOutputBlock-method-Layout-And-Ownership"></a>

#### `FieldOutputBlock.GetCount(self)` <a id="c4d.modules.mograph.FieldOutputBlock.GetCount"></a>

Returns the number of elements in the sub-block.

**Return type:** int

**Returns:** The number of elements.

#### `FieldOutputBlock.GetFullCount(self)` <a id="c4d.modules.mograph.FieldOutputBlock.GetFullCount"></a>

Returns the number of elements in the parent [`FieldOutput`](../FieldOutput/index.md#c4d.modules.mograph.FieldOutput).

**Return type:** int

**Returns:** The full number of elements.

#### `FieldOutputBlock.GetOffset(self)` <a id="c4d.modules.mograph.FieldOutputBlock.GetOffset"></a>

Returns the offset of the sub-block in the parent [`FieldOutput`](../FieldOutput/index.md#c4d.modules.mograph.FieldOutput).

**Return type:** int

**Returns:** The offset.

#### `FieldOutputBlock.GetOwner(self)` <a id="c4d.modules.mograph.FieldOutputBlock.GetOwner"></a>

Returns the parent or owner [`FieldOutput`](../FieldOutput/index.md#c4d.modules.mograph.FieldOutput).

**Return type:** [c4d.modules.mograph.FieldOutput](../FieldOutput/index.md#c4d.modules.mograph.FieldOutput)

**Returns:** The owner.

#### `FieldOutputBlock.GetSubBlock(self)` <a id="c4d.modules.mograph.FieldOutputBlock.GetSubBlock"></a>

Gets a sub-section of the sampling arrays.

**Parameters:**

- **offset** (*int*) – The offset index to retrieve a sub-block starting at.
- **size** (*int*) – The suggested size of the block. Note the function clamps the size against the maximum number of entries.

**Return type:** [c4d.modules.mograph.FieldOutputBlock](#c4d.modules.mograph.FieldOutputBlock)

**Returns:** The requested sub-block.

### Magic Methods <a id="c4d.modules.mograph.FieldOutputBlock-method-Magic-Methods"></a>

#### `FieldOutputBlock.__init__(self)` <a id="c4d.modules.mograph.FieldOutputBlock.__init__"></a>

Creates a [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) instance.

### Sample Values <a id="c4d.modules.mograph.FieldOutputBlock-method-Sample-Values"></a>

#### `FieldOutputBlock.GetAlpha(self, index)` <a id="c4d.modules.mograph.FieldOutputBlock.GetAlpha"></a>

Reads alpha at specified *index*.

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount).

**Return type:** float

**Returns:** The alpha.

#### `FieldOutputBlock.GetColor(self, index)` <a id="c4d.modules.mograph.FieldOutputBlock.GetColor"></a>

Reads color at specified *index*.

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The color.

#### `FieldOutputBlock.GetValue(self, index)` <a id="c4d.modules.mograph.FieldOutputBlock.GetValue"></a>

Reads value at specified *index*.

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount).

**Return type:** float

**Returns:** The value.

#### `FieldOutputBlock.SetAlpha(self, index, alpha)` <a id="c4d.modules.mograph.FieldOutputBlock.SetAlpha"></a>

Writes alpha at specified *index*.

**Parameters:**

- **index** (*int*) – The index in the array.
- **alpha** (*float*) – The alpha to set.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount).

#### `FieldOutputBlock.SetColor(self, index, color)` <a id="c4d.modules.mograph.FieldOutputBlock.SetColor"></a>

Writes color at specified *index*.

**Parameters:**

- **index** (*int*) – The index in the array.
- **color** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The color to set.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount).

#### `FieldOutputBlock.SetValue(self, index, value)` <a id="c4d.modules.mograph.FieldOutputBlock.SetValue"></a>

Writes value at specified *index*.

**Parameters:**

- **index** (*int*) – The index in the array.
- **value** (*float*) – The value to set.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount).

### Spatial Attributes <a id="c4d.modules.mograph.FieldOutputBlock-method-Spatial-Attributes"></a>

#### `FieldOutputBlock.GetDirection(self, index)` <a id="c4d.modules.mograph.FieldOutputBlock.GetDirection"></a>

Reads direction at specified *index*.

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The direction.

#### `FieldOutputBlock.GetPivot(self, index)` <a id="c4d.modules.mograph.FieldOutputBlock.GetPivot"></a>

Retrieve the rotational velocity (axe + magnitude) at specified *index*.

*New in version R21.*

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The rotational velocity (axe + magnitude).

#### `FieldOutputBlock.GetRotation(self, index)` <a id="c4d.modules.mograph.FieldOutputBlock.GetRotation"></a>

Reads rotation at specified *index*.

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The rotation.

#### `FieldOutputBlock.SetDirection(self, index, direction)` <a id="c4d.modules.mograph.FieldOutputBlock.SetDirection"></a>

Writes direction at specified *index*.

**Parameters:**

- **index** (*int*) – The index in the array.
- **direction** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The direction to set.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount).

#### `FieldOutputBlock.SetRotation(self, index, rotation, pivot)` <a id="c4d.modules.mograph.FieldOutputBlock.SetRotation"></a>

Writes rotation at specified *index*.

*Changed in version R21.*

**Parameters:**

- **index** (*int*) – The index in the array.
- **rotation** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The rotation to set.
- **pivot** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The rotational velocity.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount).

### State Management <a id="c4d.modules.mograph.FieldOutputBlock-method-State-Management"></a>

#### `FieldOutputBlock.ClearDeactivated(self, state=False)` <a id="c4d.modules.mograph.FieldOutputBlock.ClearDeactivated"></a>

Clears the deactivated array.

**Parameters:** **state** (*bool*) – The state the deactivated array should be cleared to.

#### `FieldOutputBlock.ClearMemory(self, startIdx=0, count=<function FieldOutputBlock.GetCount at 0x0000012ED4B15750>, deactivatedOnly=False, deactivatedState=False)` <a id="c4d.modules.mograph.FieldOutputBlock.ClearMemory"></a>

Resets the sampling data to default values.

> **Note:** Values are reset to *0*, colors to *1.0*, direction to *0*, deactivated to *0*.

**Parameters:**

- **startIdx** (*int*) – The index to start at.
- **count** (*int*) – The number of array elements to reset to default value.
- **deactivatedOnly** (*bool*) – **True** to clear deactivated only, otherwise **False**.
- **deactivatedState** (*bool*) – The state the deactivated array should be cleared to.

#### `FieldOutputBlock.GetDeactivated(self, index)` <a id="c4d.modules.mograph.FieldOutputBlock.GetDeactivated"></a>

Reads deactivated state at specified *index*.

**Parameters:** **index** (*int*) – The index in the array.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount).

**Return type:** bool

**Returns:** The deactivated state.

#### `FieldOutputBlock.IsPopulated(self)` <a id="c4d.modules.mograph.FieldOutputBlock.IsPopulated"></a>

Checks if the [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) is valid and non-empty.

**Return type:** bool

**Returns:** **True** if the [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) instance is populated, otherwise **False**.

#### `FieldOutputBlock.IsValid(self)` <a id="c4d.modules.mograph.FieldOutputBlock.IsValid"></a>

Checks if the [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) instance allocations and sizes are valid.

> **Note:** An empty [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) instance is considered valid.

**Return type:** bool

**Returns:** **True** if the [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) instance is valid, otherwise **False**.

#### `FieldOutputBlock.Reset(self)` <a id="c4d.modules.mograph.FieldOutputBlock.Reset"></a>

Resets the [`FieldOutputBlock`](#c4d.modules.mograph.FieldOutputBlock) instance to an empty state. All memory is deallocated.

#### `FieldOutputBlock.SetDeactivated(self, index, deact)` <a id="c4d.modules.mograph.FieldOutputBlock.SetDeactivated"></a>

Writes deactivated state at specified *index*.

**Parameters:**

- **index** (*int*) – The index in the array.
- **deact** (*bool*) – The deactivated state to set.

**Raises:** **IndexError** – If the *index* is out of range : *0<=index<*[`GetCount()`](#c4d.modules.mograph.FieldOutputBlock.GetCount).
