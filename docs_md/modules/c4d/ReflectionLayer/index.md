<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/ReflectionLayer/index.html -->

# c4d.ReflectionLayer <a id="c4d-reflectionlayer"></a>

## *class* `c4d.ReflectionLayer` <a id="c4d.ReflectionLayer"></a>

Represents a layer in a [`c4d.Material`](../C4DAtom/GeListNode/BaseList2D/BaseMaterial/Material/index.md#c4d.Material).

*New in version R17.032.*

> **Warning:** This type cannot be instantiated.

## Overview <a id="overview"></a>

**Flags**

- [`ReflectionLayer.GetFlags()`](#c4d.ReflectionLayer.GetFlags): Retrieves the flags for the layer.
- [`ReflectionLayer.SetFlags()`](#c4d.ReflectionLayer.SetFlags): Sets the flags for the layer.

**Identification**

- [`ReflectionLayer.GetDataID()`](#c4d.ReflectionLayer.GetDataID): Retrieves the layer base data ID to get/set its data.
- [`ReflectionLayer.GetLayerID()`](#c4d.ReflectionLayer.GetLayerID): Retrieves the layer ID.

**Naming**

- [`ReflectionLayer.GetName()`](#c4d.ReflectionLayer.GetName): Retrieves the layer name.
- [`ReflectionLayer.SetName()`](#c4d.ReflectionLayer.SetName): Sets the layer name.

## Members <a id="members"></a>

### Flags <a id="c4d.ReflectionLayer-method-Flags"></a>

#### `ReflectionLayer.GetFlags(self)` <a id="c4d.ReflectionLayer.GetFlags"></a>

Retrieves the flags for the layer.

*New in version R18.020.*

**Return type:** int

**Returns:**

The layer flags:

|   |   |
|---|---|
| *REFLECTION_FLAG_NONE* | None. |
| *REFLECTION_FLAG_SELECTED* | Selected. |
| *REFLECTION_FLAG_ACTIVE* | Active. |
| *REFLECTION_FLAG_TAB* | Tab. |
| *REFLECTION_FLAG_TRANSPARENCY* | Transparency. |
| *REFLECTION_FLAG_SEPARATE* | Separate pass. |
| *REFLECTION_FLAG_READY* | Ready. |

#### `ReflectionLayer.SetFlags(self, flags)` <a id="c4d.ReflectionLayer.SetFlags"></a>

Sets the flags for the layer.

*New in version R18.020.*

**Parameters:**

**flags** (*int*) –

The layer flags to set:

|   |   |
|---|---|
| *REFLECTION_FLAG_NONE* | None. |
| *REFLECTION_FLAG_SELECTED* | Selected. |
| *REFLECTION_FLAG_ACTIVE* | Active. |
| *REFLECTION_FLAG_TAB* | Tab. |
| *REFLECTION_FLAG_TRANSPARENCY* | Transparency. |
| *REFLECTION_FLAG_SEPARATE* | Separate pass. |
| *REFLECTION_FLAG_READY* | Ready. |

### Identification <a id="c4d.ReflectionLayer-method-Identification"></a>

#### `ReflectionLayer.GetDataID(self)` <a id="c4d.ReflectionLayer.GetDataID"></a>

Retrieves the layer base data ID to get/set its data.

**Return type:** int

**Returns:** The layer base data ID.

#### `ReflectionLayer.GetLayerID(self)` <a id="c4d.ReflectionLayer.GetLayerID"></a>

Retrieves the layer ID.

*New in version R18.020.*

**Return type:** int

**Returns:** The layer ID. Must be a value greater or equal than *3*, otherwise it failed.

### Naming <a id="c4d.ReflectionLayer-method-Naming"></a>

#### `ReflectionLayer.GetName(self)` <a id="c4d.ReflectionLayer.GetName"></a>

Retrieves the layer name.

*New in version R18.020.*

**Return type:** str

**Returns:** The layer name.

#### `ReflectionLayer.SetName(self, name)` <a id="c4d.ReflectionLayer.SetName"></a>

Sets the layer name.

*New in version R18.020.*

**Parameters:**

**name** (*str*) –

The layer name to set.  
If not valid (e.g. empty or all chars are whitespace characters) a default layer name will be used.
