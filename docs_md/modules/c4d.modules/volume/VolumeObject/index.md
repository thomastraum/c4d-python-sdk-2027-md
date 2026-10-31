<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/volume/VolumeObject/index.html -->

# c4d.modules.volume.VolumeObject <a id="c4d-modules-volume-volumeobject"></a>

## *class* `c4d.modules.volume.VolumeObject` <a id="c4d.modules.volume.VolumeObject"></a>

The volume object class of type *Ovolume*.

*New in version R20.*

Parent Class:

- [`c4d.BaseObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

## Overview <a id="overview"></a>

**Grid Metadata**

- [`VolumeObject.GetGridClass()`](#c4d.modules.volume.VolumeObject.GetGridClass): Returns the grid class.
- [`VolumeObject.GetGridType()`](#c4d.modules.volume.VolumeObject.GetGridType): Returns the grid type.

**Magic Methods**

- [`VolumeObject.__init__()`](#c4d.modules.volume.VolumeObject.__init__): Creates a [`VolumeObject`](#c4d.modules.volume.VolumeObject).

**Volume Access**

- [`VolumeObject.GetVolume()`](#c4d.modules.volume.VolumeObject.GetVolume): Returns the core volume object.
- [`VolumeObject.SetVolume()`](#c4d.modules.volume.VolumeObject.SetVolume): Sets the core volume object.

## Members <a id="members"></a>

### Grid Metadata <a id="c4d.modules.volume.VolumeObject-method-Grid-Metadata"></a>

#### `VolumeObject.GetGridClass(self)` <a id="c4d.modules.volume.VolumeObject.GetGridClass"></a>

Returns the grid class.

**Return type:** int

**Returns:**

The grid class:

|   |   |
|---|---|
| *GRIDCLASS_NONE* | None. |
| *GRIDCLASS_SDF* | SDF. |
| *GRIDCLASS_FOG* | Fog. |
| *GRIDCLASS_STAGGERED* | Staggered. |
| *GRIDCLASS_UNKNOWN* | Unknow. |

#### `VolumeObject.GetGridType(self)` <a id="c4d.modules.volume.VolumeObject.GetGridType"></a>

Returns the grid type.

**Return type:** int

**Returns:**

The grid type:

|   |   |
|---|---|
| *GRIDTYPE_NONE* | None. |
| *GRIDTYPE_FLOAT* | 32-bit float. |
| *GRIDTYPE_DOUBLE* | 64-bit float. |
| *GRIDTYPE_INT32* | 32-bit integer. |
| *GRIDTYPE_INT64* | 64-bit integer. |
| *GRIDTYPE_INTVECTOR32* | 32-bit integer vector. |
| *GRIDTYPE_VECTOR32* | 32-bit vector. |
| *GRIDTYPE_VECTOR64* | 64-bit vector. |
| *GRIDTYPE_STRING* | String. |
| *GRIDTYPE_BOOLEAN* | Bool. |

### Magic Methods <a id="c4d.modules.volume.VolumeObject-method-Magic-Methods"></a>

#### `VolumeObject.__init__(self)` <a id="c4d.modules.volume.VolumeObject.__init__"></a>

Creates a [`VolumeObject`](#c4d.modules.volume.VolumeObject).

### Volume Access <a id="c4d.modules.volume.VolumeObject-method-Volume-Access"></a>

#### `VolumeObject.GetVolume(self)` <a id="c4d.modules.volume.VolumeObject.GetVolume"></a>

Returns the core volume object.

**Return type:** [`maxon.VolumeRef`](../../../maxon_generated/frameworks/volume/reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

**Returns:** The core volume object.

#### `VolumeObject.SetVolume(self, volume)` <a id="c4d.modules.volume.VolumeObject.SetVolume"></a>

Sets the core volume object.

**Parameters:** **volume** ([`maxon.VolumeRef`](../../../maxon_generated/frameworks/volume/reference/maxon.VolumeRef.md#module-maxon.VolumeRef)) – The core volume object to set.
