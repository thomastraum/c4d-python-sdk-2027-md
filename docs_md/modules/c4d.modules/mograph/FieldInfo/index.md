<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/mograph/FieldInfo/index.html -->

# c4d.modules.mograph.FieldInfo <a id="c4d-modules-mograph-fieldinfo"></a>

## *class* `c4d.modules.mograph.FieldInfo` <a id="c4d.modules.mograph.FieldInfo"></a>

*New in version R20.*

**Attributes**

## `c4d.modules.mograph.FieldInfo._flags` <a id="c4d.modules.mograph.FieldInfo._flags"></a>

The channels that should be sampled.

**Type:** int

## `c4d.modules.mograph.FieldInfo._threadIndex` <a id="c4d.modules.mograph.FieldInfo._threadIndex"></a>

The current thread index.

**Type:** int

## `c4d.modules.mograph.FieldInfo._totalThreadCount` <a id="c4d.modules.mograph.FieldInfo._totalThreadCount"></a>

The number of threads active for the current execution.

**Type:** int

## `c4d.modules.mograph.FieldInfo._callerThread` <a id="c4d.modules.mograph.FieldInfo._callerThread"></a>

The calling thread. Required.

**Type:** [`c4d.threading.BaseThread`](../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)

## `c4d.modules.mograph.FieldInfo._doc` <a id="c4d.modules.mograph.FieldInfo._doc"></a>

The calling document. Required.

**Type:** [`c4d.documents.BaseDocument`](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)

## `c4d.modules.mograph.FieldInfo._callerStack` <a id="c4d.modules.mograph.FieldInfo._callerStack"></a>

A list of objects for the calculation as well as an ID for the invocation chain. Required.

> **Note:** The caller stack ID is especially useful to hash data to a specific caller.

> **Warning:** The ID uses the memory addresses of the callers so the value can change on undo/redo and on document load.

**Type:** [`c4d.modules.mograph.FieldCallerStack`](../FieldCallerStack/index.md#c4d.modules.mograph.FieldCallerStack)

## `c4d.modules.mograph.FieldInfo._inputData` <a id="c4d.modules.mograph.FieldInfo._inputData"></a>

The input data to be sampled.

**Type:** [`c4d.modules.mograph.FieldInput`](../FieldInput/index.md#c4d.modules.mograph.FieldInput)

## Overview <a id="overview"></a>

- [`FieldInfo.Create()`](#c4d.modules.mograph.FieldInfo.Create): Creates a [`c4d.modules.mograph.FieldInfo`](#c4d.modules.mograph.FieldInfo) while relaying potential allocation errors.

**Creation And Validation**

- [`FieldInfo.IsPopulated()`](#c4d.modules.mograph.FieldInfo.IsPopulated): Checks if the [`FieldInfo`](#c4d.modules.mograph.FieldInfo) data is valid and non-empty.
- [`FieldInfo.IsValid()`](#c4d.modules.mograph.FieldInfo.IsValid): Checks if the [`FieldInfo`](#c4d.modules.mograph.FieldInfo) data is valid.

**Magic Methods**

- [`FieldInfo.__init__()`](#c4d.modules.mograph.FieldInfo.__init__): Creates a [`FieldInfo`](#c4d.modules.mograph.FieldInfo) instance.

## Members <a id="members"></a>

### Creation And Validation <a id="c4d.modules.mograph.FieldInfo-staticmethod-Creation-And-Validation"></a>

#### *static* `FieldInfo.Create(flags, thread, doc, currentThreadIndex, threadCount, inputs, callers)` <a id="c4d.modules.mograph.FieldInfo.Create"></a>

Creates a [`c4d.modules.mograph.FieldInfo`](#c4d.modules.mograph.FieldInfo) while relaying potential allocation errors.

**Parameters:**

- **flags** (*int*) –

  The channels to sample.

  |   |   |
  |---|---|
  | *FIELDSAMPLE_FLAG_VALUE* | Sample only the value. |
  | *FIELDSAMPLE_FLAG_DIRECTION* | Sample the velocity. |
  | *FIELDSAMPLE_FLAG_COLOR* | Sample the color. |
  | *FIELDSAMPLE_FLAG_ROTATION* | Sample the rotational velocity. |

- **thread** ([*c4d.threading.BaseThread*](../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)) – The caller thread.

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to sample.

- **currentThreadIndex** (*int*) – The thread index that will sample those points.

- **threadCount** (*int*) – The total thread count.

- **inputs** (*Optional*[[*c4d.modules.mograph.FieldInput*](../FieldInput/index.md#c4d.modules.mograph.FieldInput)]) – The full point list.

- **callers** (*Optional*[*List*[[*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]]) – An initializer list to build the stack, first item is base of stack.

**Return type:** *c4d.modules.mograph.FieldInfo*

**Returns:** The created FieldInfo

### Creation And Validation <a id="c4d.modules.mograph.FieldInfo-method-Creation-And-Validation"></a>

#### `FieldInfo.IsPopulated(self)` <a id="c4d.modules.mograph.FieldInfo.IsPopulated"></a>

Checks if the [`FieldInfo`](#c4d.modules.mograph.FieldInfo) data is valid and non-empty.

> **Note:** Required [`FieldInfo`](#c4d.modules.mograph.FieldInfo) content should be set and ready for sampling.

**Return type:** bool

**Returns:** **True** if the [`FieldInfo`](#c4d.modules.mograph.FieldInfo) is populated, otherwise **False**.

#### `FieldInfo.IsValid(self)` <a id="c4d.modules.mograph.FieldInfo.IsValid"></a>

Checks if the [`FieldInfo`](#c4d.modules.mograph.FieldInfo) data is valid.

> **Note:** Default empty [`FieldInfo`](#c4d.modules.mograph.FieldInfo) is considered valid.

**Return type:** bool

**Returns:** **True** if the [`FieldInfo`](#c4d.modules.mograph.FieldInfo) is valid, otherwise **False**.

### Magic Methods <a id="c4d.modules.mograph.FieldInfo-method-Magic-Methods"></a>

#### `FieldInfo.__init__(self)` <a id="c4d.modules.mograph.FieldInfo.__init__"></a>

Creates a [`FieldInfo`](#c4d.modules.mograph.FieldInfo) instance.
