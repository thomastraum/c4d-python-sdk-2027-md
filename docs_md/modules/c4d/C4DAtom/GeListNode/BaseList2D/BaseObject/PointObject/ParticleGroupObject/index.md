<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/ParticleGroupObject/index.html -->

# c4d.ParticleGroupObject <a id="c4d-particlegroupobject"></a>

## *class* `c4d.ParticleGroupObject` <a id="c4d.ParticleGroupObject"></a>

The particle group object.

The instance object class of type *Ofpgroup* or *Ofpmultigroup*.

Parent Class:

- [`c4d.PointObject`](../index.md#c4d.PointObject)

## Overview <a id="overview"></a>

**Attribute Channels**

- [`ParticleGroupObject.GetAttributeChannelData()`](#c4d.ParticleGroupObject.GetAttributeChannelData): Get a readable byte sequence object for the passed channel identifier.
- [`ParticleGroupObject.GetAttributeChannelDescriptions()`](#c4d.ParticleGroupObject.GetAttributeChannelDescriptions): Get a list of dictionaries describing all available particle properties with name, datatype and stride.

**Identity Data**

- [`ParticleGroupObject.GetParticleUniqueIdsR()`](#c4d.ParticleGroupObject.GetParticleUniqueIdsR): Get a readable byte sequence object to the unique Id data with dataType [`maxon.UInt32`](../../../../../../../maxon_generated/datatypes/simple/maxon.UInt32.md#module-maxon.UInt32).
- [`ParticleGroupObject.GetParticleUniqueIdsW()`](#c4d.ParticleGroupObject.GetParticleUniqueIdsW): Get a writeable byte sequence object to the unique Id data with dataType [`maxon.UInt32`](../../../../../../../maxon_generated/datatypes/simple/maxon.UInt32.md#module-maxon.UInt32).

**Kinematics**

- [`ParticleGroupObject.GetParticleAngularVelocitiesR()`](#c4d.ParticleGroupObject.GetParticleAngularVelocitiesR): Get a readable byte sequence object to the angular velocity data with dataType [`maxon.Vector4d32`](../../../../../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.md#module-maxon.Vector4d32).
- [`ParticleGroupObject.GetParticleAngularVelocitiesW()`](#c4d.ParticleGroupObject.GetParticleAngularVelocitiesW): Get a writeable byte sequence object to the angular velocity data with dataType [`maxon.Vector4d32`](../../../../../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.md#module-maxon.Vector4d32).
- [`ParticleGroupObject.GetParticleVelocitiesR()`](#c4d.ParticleGroupObject.GetParticleVelocitiesR): Get a readable byte sequence object to the velocity data with dataType [`maxon.Vector4d32`](../../../../../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.md#module-maxon.Vector4d32).
- [`ParticleGroupObject.GetParticleVelocitiesW()`](#c4d.ParticleGroupObject.GetParticleVelocitiesW): Get a writeable byte sequence object to the velocity data with dataType [`maxon.Vector4d32`](../../../../../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.md#module-maxon.Vector4d32).

**Lifecycle And Scale**

- [`ParticleGroupObject.GetParticleAgesR()`](#c4d.ParticleGroupObject.GetParticleAgesR): Get a readable byte sequence object to the age data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).
- [`ParticleGroupObject.GetParticleAgesW()`](#c4d.ParticleGroupObject.GetParticleAgesW): Get a writeable byte sequence object to the age data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).
- [`ParticleGroupObject.GetParticleDistancesTraversedR()`](#c4d.ParticleGroupObject.GetParticleDistancesTraversedR): Get a readable byte sequence object to the distance traversed data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).
- [`ParticleGroupObject.GetParticleDistancesTraversedW()`](#c4d.ParticleGroupObject.GetParticleDistancesTraversedW): Get a writeable byte sequence object to the distance traversed data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).
- [`ParticleGroupObject.GetParticleLifetimesR()`](#c4d.ParticleGroupObject.GetParticleLifetimesR): Get a readable byte sequence object to the lifetime data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).
- [`ParticleGroupObject.GetParticleLifetimesW()`](#c4d.ParticleGroupObject.GetParticleLifetimesW): Get a writeable byte sequence object to the lifetime data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).
- [`ParticleGroupObject.GetParticleRadiiR()`](#c4d.ParticleGroupObject.GetParticleRadiiR): Get a readable byte sequence object to the radius data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).
- [`ParticleGroupObject.GetParticleRadiiW()`](#c4d.ParticleGroupObject.GetParticleRadiiW): Get a writeable byte sequence object to the radius data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).

**Orientation**

- [`ParticleGroupObject.GetParticleAlignmentsR()`](#c4d.ParticleGroupObject.GetParticleAlignmentsR): Get a readable byte sequence object to the alignment data with dataType `` maxon.Quaternion`[:class:`maxon.Float32 ``].
- [`ParticleGroupObject.GetParticleAlignmentsW()`](#c4d.ParticleGroupObject.GetParticleAlignmentsW): Get a writeable byte sequence object to the alignment data with dataType `` maxon.Quaternion`[:class:`maxon.Float32 ``].

**Spatial And Visual Data**

- [`ParticleGroupObject.GetParticleColorsR()`](#c4d.ParticleGroupObject.GetParticleColorsR): Get a readable byte sequence object to the color data with dataType `maxon.Color32A`.
- [`ParticleGroupObject.GetParticleColorsW()`](#c4d.ParticleGroupObject.GetParticleColorsW): Get a writeable byte sequence object to the color data with dataType `maxon.Color32A`.
- [`ParticleGroupObject.GetParticlePositionsR()`](#c4d.ParticleGroupObject.GetParticlePositionsR): Get a readable byte sequence object to the position data with dataType [`maxon.Vector`](../../../../../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector) (64 bit or 32 bit - depending on the OS).
- [`ParticleGroupObject.GetParticlePositionsW()`](#c4d.ParticleGroupObject.GetParticlePositionsW): Get a writeable byte sequence object to the position data with dataType [`maxon.Vector`](../../../../../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector) (64 bit or 32 bit - depending on the OS).

## Members <a id="members"></a>

### Attribute Channels <a id="c4d.ParticleGroupObject-method-Attribute-Channels"></a>

#### `ParticleGroupObject.GetAttributeChannelData(self, channel)` <a id="c4d.ParticleGroupObject.GetAttributeChannelData"></a>

Get a readable byte sequence object for the passed channel identifier.

**Parameters:** **channel** (*str*) – The channel identifier

**Returns:** A readable byte sequence object for the passed channel identifier

**Return type:** memoryview

#### `ParticleGroupObject.GetAttributeChannelDescriptions(self)` <a id="c4d.ParticleGroupObject.GetAttributeChannelDescriptions"></a>

Get a list of dictionaries describing all available particle properties with name, datatype and stride.

**Returns:** A list of dictionaries describing all available particle properties

**Return type:** list[dict[“Name”: str, “Data Type”: str, “Data Size in bytes”: int, “Data Stride in bytes”: int]]

### Identity Data <a id="c4d.ParticleGroupObject-method-Identity-Data"></a>

#### `ParticleGroupObject.GetParticleUniqueIdsR(self)` <a id="c4d.ParticleGroupObject.GetParticleUniqueIdsR"></a>

Get a readable byte sequence object to the unique Id data with dataType [`maxon.UInt32`](../../../../../../../maxon_generated/datatypes/simple/maxon.UInt32.md#module-maxon.UInt32).

**Returns:** A readable byte sequence object to the unique Id data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticleUniqueIdsW(self)` <a id="c4d.ParticleGroupObject.GetParticleUniqueIdsW"></a>

Get a writeable byte sequence object to the unique Id data with dataType [`maxon.UInt32`](../../../../../../../maxon_generated/datatypes/simple/maxon.UInt32.md#module-maxon.UInt32).

**Returns:** A writeable byte sequence object to the unique Id data

**Return type:** memoryview

### Kinematics <a id="c4d.ParticleGroupObject-method-Kinematics"></a>

#### `ParticleGroupObject.GetParticleAngularVelocitiesR(self)` <a id="c4d.ParticleGroupObject.GetParticleAngularVelocitiesR"></a>

Get a readable byte sequence object to the angular velocity data with dataType [`maxon.Vector4d32`](../../../../../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.md#module-maxon.Vector4d32). Note that this vector’s w-component is unused.

**Returns:** A readable byte sequence object to the angular velocity data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticleAngularVelocitiesW(self)` <a id="c4d.ParticleGroupObject.GetParticleAngularVelocitiesW"></a>

Get a writeable byte sequence object to the angular velocity data with dataType [`maxon.Vector4d32`](../../../../../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.md#module-maxon.Vector4d32). Note that this vector’s w-component is unused.

**Returns:** A writeable byte sequence object to the angular velocity data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticleVelocitiesR(self)` <a id="c4d.ParticleGroupObject.GetParticleVelocitiesR"></a>

Get a readable byte sequence object to the velocity data with dataType [`maxon.Vector4d32`](../../../../../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.md#module-maxon.Vector4d32). Note that this vector’s w-component is unused.

**Returns:** A readable byte sequence object to the velocity data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticleVelocitiesW(self)` <a id="c4d.ParticleGroupObject.GetParticleVelocitiesW"></a>

Get a writeable byte sequence object to the velocity data with dataType [`maxon.Vector4d32`](../../../../../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.md#module-maxon.Vector4d32). Note that this vector’s w-component is unused.

**Returns:** A writeable byte sequence object to the velocity data

**Return type:** memoryview

### Lifecycle And Scale <a id="c4d.ParticleGroupObject-method-Lifecycle-And-Scale"></a>

#### `ParticleGroupObject.GetParticleAgesR(self)` <a id="c4d.ParticleGroupObject.GetParticleAgesR"></a>

Get a readable byte sequence object to the age data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).

**Returns:** A readable byte sequence object to the age data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticleAgesW(self)` <a id="c4d.ParticleGroupObject.GetParticleAgesW"></a>

Get a writeable byte sequence object to the age data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).

**Returns:** A writeable byte sequence object to the age data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticleDistancesTraversedR(self)` <a id="c4d.ParticleGroupObject.GetParticleDistancesTraversedR"></a>

Get a readable byte sequence object to the distance traversed data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).

**Returns:** A readable byte sequence object to the distance traversed data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticleDistancesTraversedW(self)` <a id="c4d.ParticleGroupObject.GetParticleDistancesTraversedW"></a>

Get a writeable byte sequence object to the distance traversed data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).

**Returns:** A writeable byte sequence object to the distance traversed data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticleLifetimesR(self)` <a id="c4d.ParticleGroupObject.GetParticleLifetimesR"></a>

Get a readable byte sequence object to the lifetime data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).

**Returns:** A readable byte sequence object to the lifetime data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticleLifetimesW(self)` <a id="c4d.ParticleGroupObject.GetParticleLifetimesW"></a>

Get a writeable byte sequence object to the lifetime data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).

**Returns:** A writeable byte sequence object to the lifetime data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticleRadiiR(self)` <a id="c4d.ParticleGroupObject.GetParticleRadiiR"></a>

Get a readable byte sequence object to the radius data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).

**Returns:** A readable byte sequence object to the radius data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticleRadiiW(self)` <a id="c4d.ParticleGroupObject.GetParticleRadiiW"></a>

Get a writeable byte sequence object to the radius data with dataType [`maxon.Float32`](../../../../../../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32).

**Returns:** A writeable byte sequence object to the radius data

**Return type:** memoryview

### Orientation <a id="c4d.ParticleGroupObject-method-Orientation"></a>

#### `ParticleGroupObject.GetParticleAlignmentsR(self)` <a id="c4d.ParticleGroupObject.GetParticleAlignmentsR"></a>

Get a readable byte sequence object to the alignment data with dataType `` maxon.Quaternion`[:class:`maxon.Float32 ``].

**Returns:** A readable byte sequence object to the alignment data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticleAlignmentsW(self)` <a id="c4d.ParticleGroupObject.GetParticleAlignmentsW"></a>

Get a writeable byte sequence object to the alignment data with dataType `` maxon.Quaternion`[:class:`maxon.Float32 ``].

**Returns:** A writeable byte sequence object to the alignment data

**Return type:** memoryview

### Spatial And Visual Data <a id="c4d.ParticleGroupObject-method-Spatial-And-Visual-Data"></a>

#### `ParticleGroupObject.GetParticleColorsR(self)` <a id="c4d.ParticleGroupObject.GetParticleColorsR"></a>

Get a readable byte sequence object to the color data with dataType `maxon.Color32A`.

**Returns:** A readable byte sequence object to the color data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticleColorsW(self)` <a id="c4d.ParticleGroupObject.GetParticleColorsW"></a>

Get a writeable byte sequence object to the color data with dataType `maxon.Color32A`.

**Returns:** A writeable byte sequence object to the color data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticlePositionsR(self)` <a id="c4d.ParticleGroupObject.GetParticlePositionsR"></a>

Get a readable byte sequence object to the position data with dataType [`maxon.Vector`](../../../../../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector) (64 bit or 32 bit - depending on the OS).

**Returns:** A readable byte sequence object to the position data

**Return type:** memoryview

#### `ParticleGroupObject.GetParticlePositionsW(self)` <a id="c4d.ParticleGroupObject.GetParticlePositionsW"></a>

Get a writeable byte sequence object to the position data with dataType [`maxon.Vector`](../../../../../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector) (64 bit or 32 bit - depending on the OS).

**Returns:** A writeable byte sequence object to the position data

**Return type:** memoryview
