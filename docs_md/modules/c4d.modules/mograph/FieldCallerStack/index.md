<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/mograph/FieldCallerStack/index.html -->

# c4d.modules.mograph.FieldCallerStack <a id="c4d-modules-mograph-fieldcallerstack"></a>

## *class* `c4d.modules.mograph.FieldCallerStack` <a id="c4d.modules.mograph.FieldCallerStack"></a>

*New in version R20.*

**Attributes**

## `c4d.modules.mograph.FieldCallerStack._value` <a id="c4d.modules.mograph.FieldCallerStack._value"></a>

Caller stack id.

**Type:** int

## Overview <a id="overview"></a>

**Data Management**

- [`FieldCallerStack.Add()`](#c4d.modules.mograph.FieldCallerStack.Add): Adds a caller to the stack and updates the stack ID.
- [`FieldCallerStack.CopyFrom()`](#c4d.modules.mograph.FieldCallerStack.CopyFrom): Copies from the supplied [`FieldCallerStack`](#c4d.modules.mograph.FieldCallerStack) *src*.
- [`FieldCallerStack.GetCount()`](#c4d.modules.mograph.FieldCallerStack.GetCount): Returns the number of callers involved in the stack.
- [`FieldCallerStack.GetValue()`](#c4d.modules.mograph.FieldCallerStack.GetValue): Returns the caller stack ID.
- [`FieldCallerStack.IsValid()`](#c4d.modules.mograph.FieldCallerStack.IsValid): Checks if the caller stack is valid.

**Magic Methods**

- [`FieldCallerStack.__getitem__()`](#c4d.modules.mograph.FieldCallerStack.__getitem__): Retrieves a caller from the stack by index.
- [`FieldCallerStack.__init__()`](#c4d.modules.mograph.FieldCallerStack.__init__): Creates a [`c4d.modules.mograph.FieldCallerStack`](#c4d.modules.mograph.FieldCallerStack) instance.

**Value Calculation**

- [`FieldCallerStack.RecalcValue()`](#c4d.modules.mograph.FieldCallerStack.RecalcValue): Calculates the ID of the caller stack from scratch.
- [`FieldCallerStack.UpdateValue()`](#c4d.modules.mograph.FieldCallerStack.UpdateValue): Recalculates the ID of the caller stack from scratch and updates the internal stack ID value.

## Members <a id="members"></a>

### Data Management <a id="c4d.modules.mograph.FieldCallerStack-method-Data-Management"></a>

#### `FieldCallerStack.Add(self, caller)` <a id="c4d.modules.mograph.FieldCallerStack.Add"></a>

Adds a caller to the stack and updates the stack ID.

**Parameters:** **caller** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The caller object to add to the stack.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `FieldCallerStack.CopyFrom(self, src)` <a id="c4d.modules.mograph.FieldCallerStack.CopyFrom"></a>

Copies from the supplied [`FieldCallerStack`](#c4d.modules.mograph.FieldCallerStack) *src*.

**Parameters:** **src** ([*c4d.modules.mograph.FieldCallerStack*](#c4d.modules.mograph.FieldCallerStack)) – The source.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `FieldCallerStack.GetCount(self)` <a id="c4d.modules.mograph.FieldCallerStack.GetCount"></a>

Returns the number of callers involved in the stack.

**Return type:** int

**Returns:** The number of callers.

#### `FieldCallerStack.GetValue(self)` <a id="c4d.modules.mograph.FieldCallerStack.GetValue"></a>

Returns the caller stack ID.

**Return type:** int

**Returns:** The caller stack ID.

#### `FieldCallerStack.IsValid(self)` <a id="c4d.modules.mograph.FieldCallerStack.IsValid"></a>

Checks if the caller stack is valid.

> **Note:**
>
> An empty stack is valid.  
> A stack with broken links to callers is not valid.

> **Warning:** A non empty stack with no stack ID value is not valid.

**Return type:** bool

**Returns:** **True** if the caller stack is valid, otherwise **False**.

### Magic Methods <a id="c4d.modules.mograph.FieldCallerStack-method-Magic-Methods"></a>

#### `FieldCallerStack.__getitem__(self, key)` <a id="c4d.modules.mograph.FieldCallerStack.__getitem__"></a>

Retrieves a caller from the stack by index.

**Parameters:** **key** (*int*) – The caller index.

**Raises:** **IndexError** – If the index *key* is out of range : *0<=key<*[`GetCount()`](#c4d.modules.mograph.FieldCallerStack.GetCount).

**Return type:** [c4d.BaseList2D](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

**Returns:** The caller.

#### `FieldCallerStack.__init__(self)` <a id="c4d.modules.mograph.FieldCallerStack.__init__"></a>

Creates a [`c4d.modules.mograph.FieldCallerStack`](#c4d.modules.mograph.FieldCallerStack) instance.

### Value Calculation <a id="c4d.modules.mograph.FieldCallerStack-method-Value-Calculation"></a>

#### `FieldCallerStack.RecalcValue(self)` <a id="c4d.modules.mograph.FieldCallerStack.RecalcValue"></a>

Calculates the ID of the caller stack from scratch. Does not update stored ID value.

**Return type:** int

**Returns:** The new caller stack ID.

#### `FieldCallerStack.UpdateValue(self)` <a id="c4d.modules.mograph.FieldCallerStack.UpdateValue"></a>

Recalculates the ID of the caller stack from scratch and updates the internal stack ID value.
