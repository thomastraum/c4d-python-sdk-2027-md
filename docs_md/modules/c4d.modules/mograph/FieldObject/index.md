<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/mograph/FieldObject/index.html -->

# c4d.modules.mograph.FieldObject <a id="c4d-modules-mograph-fieldobject"></a>

## *class* `c4d.modules.mograph.FieldObject` <a id="c4d.modules.mograph.FieldObject"></a>

*New in version R20.*

Parent Class:

- [`c4d.BaseObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

## Overview <a id="overview"></a>

**Field Sampling**

- [`FieldObject.FreeSampling()`](#c4d.modules.mograph.FieldObject.FreeSampling): Frees any data allocated in `InitSampling()`.
- [`FieldObject.GetFieldFlags()`](#c4d.modules.mograph.FieldObject.GetFieldFlags): Returns the field flags.
- [`FieldObject.InitSampling()`](#c4d.modules.mograph.FieldObject.InitSampling): Initializes field sampling.
- [`FieldObject.Sample()`](#c4d.modules.mograph.FieldObject.Sample): Samples points within the field.

**Magic Methods**

- [`FieldObject.__init__()`](#c4d.modules.mograph.FieldObject.__init__): Creates a [`FieldObject`](#c4d.modules.mograph.FieldObject) instance.

## Members <a id="members"></a>

### Field Sampling <a id="c4d.modules.mograph.FieldObject-method-Field-Sampling"></a>

#### `FieldObject.FreeSampling(self, info)` <a id="c4d.modules.mograph.FieldObject.FreeSampling"></a>

Frees any data allocated in [`InitSampling()`](#c4d.modules.mograph.FieldObject.InitSampling).

> **Warning:** Must be called after sampling is finished.

> **Warning:**
>
> Due to core changes in 2024.0.0, this function is not working in Python 2024.0.0.  
> This is going to be fixed in an upcoming version.

**Parameters:** **info** ([*c4d.modules.mograph.FieldInfo*](../FieldInfo/index.md#c4d.modules.mograph.FieldInfo)) – The [`FieldInfo`](../FieldInfo/index.md#c4d.modules.mograph.FieldInfo) used for sampling.

#### `FieldObject.GetFieldFlags(self, doc)` <a id="c4d.modules.mograph.FieldObject.GetFieldFlags"></a>

Returns the field flags.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

**Return type:** int

**Returns:**

The field flags:

|   |   |
|---|---|
| *FIELDOBJECT_FLAG_NONE* | None. |
| *FIELDOBJECT_FLAG_INLINE* | The field calculates with the current values of the field stack. |
| *FIELDOBJECT_FLAG_GENERATINGCOLOR* | The field is currently outputting color. |
| *FIELDOBJECT_FLAG_PRESERVEALPHA* | The field does not modify alpha, any color it produces is directly applied to the existing color ignoring the alpha blending. |
| *FIELDOBJECT_FLAG_SKIP* | The field should be skipped. |
| *FIELDOBJECT_FLAG_ERRORSKIP* | The field is currently experiencing an error. |

#### `FieldObject.InitSampling(self, info)` <a id="c4d.modules.mograph.FieldObject.InitSampling"></a>

Initializes field sampling.

> **Warning:** Must be called before [`Sample()`](#c4d.modules.mograph.FieldObject.Sample) is invoked.

**Parameters:** **info** ([*c4d.modules.mograph.FieldInfo*](../FieldInfo/index.md#c4d.modules.mograph.FieldInfo)) – The [`FieldInfo`](../FieldInfo/index.md#c4d.modules.mograph.FieldInfo) to initialize sampling with.

#### `FieldObject.Sample(self, input, output, info, flags)` <a id="c4d.modules.mograph.FieldObject.Sample"></a>

Samples points within the field.

> **Warning:** [`InitSampling()`](#c4d.modules.mograph.FieldObject.InitSampling) must be called before. [`FreeSampling()`](#c4d.modules.mograph.FieldObject.FreeSampling) must be called once sampling is complete.

> **Warning:**
>
> Due to core changes in 2024.0.0, this function is not working in Python 2024.0.0.  
> This is going to be fixed in an upcoming version.

**Parameters:**

- **input** ([*c4d.modules.mograph.FieldInput*](../FieldInput/index.md#c4d.modules.mograph.FieldInput)) – The points to sample in global space.

- **output** ([*c4d.modules.mograph.FieldOutputBlock*](../FieldOutputBlock/index.md#c4d.modules.mograph.FieldOutputBlock)) – The output result values, should be allocated prior to usage.

- **info** ([*c4d.modules.mograph.FieldInfo*](../FieldInfo/index.md#c4d.modules.mograph.FieldInfo)) – The [`FieldInfo`](../FieldInfo/index.md#c4d.modules.mograph.FieldInfo) to sample with. It should match the info used with [`InitSampling()`](#c4d.modules.mograph.FieldObject.InitSampling).

- **flags** (*int*) –

  The field object sample flags:

  |   |   |
  |---|---|
  | *FIELDOBJECTSAMPLE_FLAG_NONE* | None. |
  | *FIELDOBJECTSAMPLE_FLAG_DISABLEDIRECTIONFALLOFF* | Private. |

### Magic Methods <a id="c4d.modules.mograph.FieldObject-method-Magic-Methods"></a>

#### `FieldObject.__init__(self, type)` <a id="c4d.modules.mograph.FieldObject.__init__"></a>

Creates a [`FieldObject`](#c4d.modules.mograph.FieldObject) instance.

**Parameters:** **type** (*int*) – The field type.
