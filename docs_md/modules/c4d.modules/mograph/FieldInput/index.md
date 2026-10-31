<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/mograph/FieldInput/index.html -->

# c4d.modules.mograph.FieldInput <a id="c4d-modules-mograph-fieldinput"></a>

## *class* `c4d.modules.mograph.FieldInput` <a id="c4d.modules.mograph.FieldInput"></a>

*New in version R20.*

**Attributes**

## `c4d.modules.mograph.FieldInput._blockCount` <a id="c4d.modules.mograph.FieldInput._blockCount"></a>

[Read-only]

The number of elements to be processed. The count to use when iterating over elements in [`FieldObject`](../FieldObject/index.md#c4d.modules.mograph.FieldObject) and [`FieldLayer`](../FieldLayer/index.md#c4d.modules.mograph.FieldLayer).

**Type:** int

## `c4d.modules.mograph.FieldInput._blockOffset` <a id="c4d.modules.mograph.FieldInput._blockOffset"></a>

[Read-only]

The offset (starting point) of the elements if a portion of a larger array. Used for example to get the actual index in the list: *actualIndex = index - points._blockOffset*.

**Type:** int

## `c4d.modules.mograph.FieldInput._fullArraySize` <a id="c4d.modules.mograph.FieldInput._fullArraySize"></a>

[Read-only]

The full size of the source data. May be larger than `_blockCount` and also might be larger than the size of the allocated block within the [`c4d.modules.mograph.FieldInput`](#c4d.modules.mograph.FieldInput).

> **Warning:** Do no use `_fullArraySize` to browse the arrays.

**Type:** int

## `c4d.modules.mograph.FieldInput._transform` <a id="c4d.modules.mograph.FieldInput._transform"></a>

[Read-only]

The transform matrix for the points in the input block. Use to bring the position and direction lists into world space or the local space of a [`FieldObject`](../FieldObject/index.md#c4d.modules.mograph.FieldObject).

**Type:** [`c4d.Matrix`](../../../c4d/Matrix/index.md#c4d.Matrix)

## `c4d.modules.mograph.FieldInput._position` <a id="c4d.modules.mograph.FieldInput._position"></a>

[Read-only]

The position values for the array of points. If it is a sub-block then element *0* is at `_blockOffset` within the larger block.

**Type:** List[c4d.Vector]

## `c4d.modules.mograph.FieldInput._direction` <a id="c4d.modules.mograph.FieldInput._direction"></a>

[Read-only]

The direction values for the array of points. If it is a sub-block then element *0* is at `_blockOffset` within the larger block.

**Type:** List[c4d.Vector]

## `c4d.modules.mograph.FieldInput._uvw` <a id="c4d.modules.mograph.FieldInput._uvw"></a>

[Read-only]

The uvw values for the array of points. If it is a sub-block then element *0* is at `_blockOffset` within the larger block.

**Type:** List[c4d.Vector]

## Overview <a id="overview"></a>

**Data Slicing And Layout**

- [`FieldInput.GetCount()`](#c4d.modules.mograph.FieldInput.GetCount): Returns the number of elements in the [`FieldInput`](#c4d.modules.mograph.FieldInput).
- [`FieldInput.GetOffset()`](#c4d.modules.mograph.FieldInput.GetOffset): Returns the offset of the first element in full arrays.
- [`FieldInput.GetSubBlock()`](#c4d.modules.mograph.FieldInput.GetSubBlock): Retrieves a [`FieldInput`](#c4d.modules.mograph.FieldInput) for a subset of the original block.

**Magic Methods**

- [`FieldInput.__init__()`](#c4d.modules.mograph.FieldInput.__init__): Creates a [`FieldInput`](#c4d.modules.mograph.FieldInput) instance.

**State Validation**

- [`FieldInput.IsPopulated()`](#c4d.modules.mograph.FieldInput.IsPopulated): Checks if the [`FieldInput`](#c4d.modules.mograph.FieldInput) is valid and non-empty.
- [`FieldInput.IsValid()`](#c4d.modules.mograph.FieldInput.IsValid): Checks if the [`FieldInput`](#c4d.modules.mograph.FieldInput) allocations and sizes are valid.

## Members <a id="members"></a>

### Data Slicing And Layout <a id="c4d.modules.mograph.FieldInput-method-Data-Slicing-And-Layout"></a>

#### `FieldInput.GetCount(self)` <a id="c4d.modules.mograph.FieldInput.GetCount"></a>

Returns the number of elements in the [`FieldInput`](#c4d.modules.mograph.FieldInput).

**Return type:** int

**Returns:** The number of elements.

#### `FieldInput.GetOffset(self)` <a id="c4d.modules.mograph.FieldInput.GetOffset"></a>

Returns the offset of the first element in full arrays.

**Return type:** int

**Returns:** The offset.

#### `FieldInput.GetSubBlock(self, offset, blockSize)` <a id="c4d.modules.mograph.FieldInput.GetSubBlock"></a>

Retrieves a [`FieldInput`](#c4d.modules.mograph.FieldInput) for a subset of the original block.

> **Note:** Useful to pass smaller blocks to the field processing threads.

**Parameters:**

- **offset** (*int*) – The sub-block start offset.
- **blockSize** (*int*) – The size of the desired sub-block. *400* is the recommended size.

**Return type:** [c4d.modules.mograph.FieldInput](#c4d.modules.mograph.FieldInput)

**Returns:** The sub-block [`FieldInput`](#c4d.modules.mograph.FieldInput).

### Magic Methods <a id="c4d.modules.mograph.FieldInput-method-Magic-Methods"></a>

#### `FieldInput.__init__(self, position, allocatedCount, transform=None, fullCount=-1, direction=None, uvw=None)` <a id="c4d.modules.mograph.FieldInput.__init__"></a>

Creates a [`FieldInput`](#c4d.modules.mograph.FieldInput) instance.

**Parameters:**

- **position** (*List*[[*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)]) – The position list to sample.
- **allocatedCount** (*int*) – The length of the *position* list.
- **transform** (*Optional*[[*c4d.Matrix*](../../../c4d/Matrix/index.md#c4d.Matrix)]) – The transform matrix required to convert the position and direction inputs to global space.
- **fullCount** (*Optional*[*int*]) – The full position count if *allocatedCount* is too big to allocate *position* list. If not set *allocatedCount* is used instead.
- **direction** (*Optional*[*List*[[*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)]]) – The direction list to sample.
- **uvw** (*Optional*[*List*[[*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)]]) – The uvw list to sample.

### State Validation <a id="c4d.modules.mograph.FieldInput-method-State-Validation"></a>

#### `FieldInput.IsPopulated(self)` <a id="c4d.modules.mograph.FieldInput.IsPopulated"></a>

Checks if the [`FieldInput`](#c4d.modules.mograph.FieldInput) is valid and non-empty.

**Return type:** bool

**Returns:** **True** if the [`FieldInput`](#c4d.modules.mograph.FieldInput) is populated, otherwise **False**.

#### `FieldInput.IsValid(self)` <a id="c4d.modules.mograph.FieldInput.IsValid"></a>

Checks if the [`FieldInput`](#c4d.modules.mograph.FieldInput) allocations and sizes are valid.

> **Note:** Default empty [`FieldInput`](#c4d.modules.mograph.FieldInput) is considered valid.

**Return type:** bool

**Returns:** **True** if the [`FieldInput`](#c4d.modules.mograph.FieldInput) is valid, otherwise **False**.
