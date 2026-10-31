<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/Material/index.html -->

# c4d.Material <a id="c4d-material"></a>

## *class* `c4d.Material` <a id="c4d.Material"></a>

The material with the Mmaterial type.

See *Mmaterial.h* for container IDs.

Parent Class:

- [`c4d.BaseMaterial`](../index.md#c4d.BaseMaterial)

## Overview <a id="overview"></a>

**Channel State**

- [`Material.GetChannelState()`](#c4d.Material.GetChannelState): Get the state of a channel (if it is enabled or disabled).
- [`Material.SetChannelState()`](#c4d.Material.SetChannelState): Set the state of a channel (if it is enabled or disabled).

**Layer Inspection**

- [`Material.GetAllReflectionShaders()`](#c4d.Material.GetAllReflectionShaders): Retrieves all the reflection/specular shaders.
- [`Material.GetReflectionLayerCount()`](#c4d.Material.GetReflectionLayerCount): Retrieves the number of reflection/specular layers.
- [`Material.GetReflectionLayerID()`](#c4d.Material.GetReflectionLayerID): Retrieves a reflection/specular layer by ID.
- [`Material.GetReflectionLayerIndex()`](#c4d.Material.GetReflectionLayerIndex): Retrieves a reflection/specular layer by index.
- [`Material.GetReflectionLayerTrans()`](#c4d.Material.GetReflectionLayerTrans): Retrieves the transparency layer.
- [`Material.GetReflectionPrimaryLayers()`](#c4d.Material.GetReflectionPrimaryLayers): Retrieves the indices to the primary reflection and specular layers (can be -1 for empty).

**Layer Management**

- [`Material.AddReflectionLayer()`](#c4d.Material.AddReflectionLayer): Adds a reflection/specular layer.
- [`Material.RemoveReflectionAllLayers()`](#c4d.Material.RemoveReflectionAllLayers): Deletes all reflection/specular layers.
- [`Material.RemoveReflectionLayerID()`](#c4d.Material.RemoveReflectionLayerID): Removes a reflection/specular layer by ID.
- [`Material.RemoveReflectionLayerIndex()`](#c4d.Material.RemoveReflectionLayerIndex): Removes a reflection/specular layer by index.

**Magic Methods**

- [`Material.__init__()`](#c4d.Material.__init__)

## Members <a id="members"></a>

### Channel State <a id="c4d.Material-method-Channel-State"></a>

#### `Material.GetChannelState(self, channel)` <a id="c4d.Material.GetChannelState"></a>

Get the state of a channel (if it is enabled or disabled).

**Parameters:**

**channel** (*int*) –

The type of channel:

|   |   |
|---|---|
| *CHANNEL_COLOR* | The color channel of a material. |
| *CHANNEL_LUMINANCE* | The luminance channel of a material. |
| *CHANNEL_TRANSPARENCY* | The transparency channel of a material. |
| *CHANNEL_REFLECTION* | The reflection channel of a material. |
| *CHANNEL_ENVIRONMENT* | The environment channel of a material. |
| *CHANNEL_FOG* | The fog channel of a material. |
| *CHANNEL_BUMP* | The bump channel of a material. |
| *CHANNEL_ALPHA* | The alpha channel of a material. |
| *CHANNEL_SPECULAR* | The specular channel of a material. |
| *CHANNEL_SPECULARCOLOR* | The specular color channel of a material. |
| *CHANNEL_GLOW* | The glow channel of a material. |
| *CHANNEL_DISPLACEMENT* | The displacement channel of a material. |
| *CHANNEL_DIFFUSION* | The diffusion channel of a material. |
| *CHANNEL_NORMAL* | The normal channel of a material. |
| *CHANNEL_ANY* | An unlabeled plugin channel. |

**Return type:** bool

**Returns:** **True** if the channel is enabled.

#### `Material.SetChannelState(self, channel, state)` <a id="c4d.Material.SetChannelState"></a>

Set the state of a channel (if it is enabled or disabled).

**Parameters:**

- **channel** (*int*) –

  The type of channel to change:

  |   |   |
  |---|---|
  | *CHANNEL_COLOR* | The color channel of a material. |
  | *CHANNEL_LUMINANCE* | The luminance channel of a material. |
  | *CHANNEL_TRANSPARENCY* | The transparency channel of a material. |
  | *CHANNEL_REFLECTION* | The reflection channel of a material. |
  | *CHANNEL_ENVIRONMENT* | The environment channel of a material. |
  | *CHANNEL_FOG* | The fog channel of a material. |
  | *CHANNEL_BUMP* | The bump channel of a material. |
  | *CHANNEL_ALPHA* | The alpha channel of a material. |
  | *CHANNEL_SPECULAR* | The specular channel of a material. |
  | *CHANNEL_SPECULARCOLOR* | The specular color channel of a material. |
  | *CHANNEL_GLOW* | The glow channel of a material. |
  | *CHANNEL_DISPLACEMENT* | The displacement channel of a material. |
  | *CHANNEL_DIFFUSION* | The diffusion channel of a material. |
  | *CHANNEL_NORMAL* | The normal channel of a material. |
  | *CHANNEL_ANY* | An unlabeled plugin channel. |

- **state** (*bool*) – **True** to enable the channel.

### Layer Inspection <a id="c4d.Material-method-Layer-Inspection"></a>

#### `Material.GetAllReflectionShaders(self)` <a id="c4d.Material.GetAllReflectionShaders"></a>

Retrieves all the reflection/specular shaders.

*New in version R17.032.*

**Return type:** List[[c4d.BaseShader](../../BaseShader/index.md#c4d.BaseShader)]

**Returns:** The reflection/specular shaders.

#### `Material.GetReflectionLayerCount(self)` <a id="c4d.Material.GetReflectionLayerCount"></a>

Retrieves the number of reflection/specular layers.

*New in version R17.032.*

**Return type:** int

**Returns:** The reflection/specular layers’ count.

#### `Material.GetReflectionLayerID(self, id)` <a id="c4d.Material.GetReflectionLayerID"></a>

Retrieves a reflection/specular layer by ID.

*New in version R17.032.*

**Parameters:** **id** (*int*) – The layer ID.

**Return type:** [c4d.ReflectionLayer](../../../../../ReflectionLayer/index.md#c4d.ReflectionLayer)

**Returns:** The reflection/specular layer.

#### `Material.GetReflectionLayerIndex(self, index)` <a id="c4d.Material.GetReflectionLayerIndex"></a>

Retrieves a reflection/specular layer by index.

*New in version R17.032.*

**Parameters:** **index** (*int*) – The layer index.

**Return type:** [c4d.ReflectionLayer](../../../../../ReflectionLayer/index.md#c4d.ReflectionLayer)

**Returns:** The reflection/specular layer.

#### `Material.GetReflectionLayerTrans(self)` <a id="c4d.Material.GetReflectionLayerTrans"></a>

Retrieves the transparency layer.

*New in version R17.032.*

**Return type:** Optional[[c4d.ReflectionLayer](../../../../../ReflectionLayer/index.md#c4d.ReflectionLayer)]

**Returns:** The transparency layer, or **None** if not available.

#### `Material.GetReflectionPrimaryLayers(self)` <a id="c4d.Material.GetReflectionPrimaryLayers"></a>

Retrieves the indices to the primary reflection and specular layers (can be -1 for empty).

*New in version R17.032.*

**Return type:** Tuple[int, int]

**Returns:** The most significant reflection and specular layers.

### Layer Management <a id="c4d.Material-method-Layer-Management"></a>

#### `Material.AddReflectionLayer(self)` <a id="c4d.Material.AddReflectionLayer"></a>

Adds a reflection/specular layer.

*New in version R17.032.*

**Return type:** [c4d.ReflectionLayer](../../../../../ReflectionLayer/index.md#c4d.ReflectionLayer)

**Returns:** The added reflection/specular layer.

#### `Material.RemoveReflectionAllLayers(self)` <a id="c4d.Material.RemoveReflectionAllLayers"></a>

Deletes all reflection/specular layers.

*New in version R17.032.*

#### `Material.RemoveReflectionLayerID(self, id)` <a id="c4d.Material.RemoveReflectionLayerID"></a>

Removes a reflection/specular layer by ID.

*New in version R17.032.*

**Parameters:** **id** (*int*) – The layer ID.

#### `Material.RemoveReflectionLayerIndex(self, index)` <a id="c4d.Material.RemoveReflectionLayerIndex"></a>

Removes a reflection/specular layer by index.

*New in version R17.032.*

**Parameters:** **index** (*int*) – The layer index.

### Magic Methods <a id="c4d.Material-method-Magic-Methods"></a>

#### `Material.__init__(self)` <a id="c4d.Material.__init__"></a>
