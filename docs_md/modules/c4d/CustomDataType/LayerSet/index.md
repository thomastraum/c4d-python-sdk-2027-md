<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/LayerSet/index.html -->

# c4d.LayerSet <a id="c4d-layerset"></a>

## *class* `c4d.LayerSet` <a id="c4d.LayerSet"></a>

This data type enables to access the layers of a bitmap shader.

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Display Modes**

- [`LayerSet.GetMode()`](#c4d.LayerSet.GetMode): Returns the layer set mode.
- [`LayerSet.GetPreviewMode()`](#c4d.LayerSet.GetPreviewMode): Return the preview mode.
- [`LayerSet.SetMode()`](#c4d.LayerSet.SetMode): Assign a new layer set mode.
- [`LayerSet.SetPreviewMode()`](#c4d.LayerSet.SetPreviewMode): Set the preview mode.

**Identity And Transfer**

- [`LayerSet.CopyTo()`](#c4d.LayerSet.CopyTo): Copies the content from *self* to *dst*.
- [`LayerSet.GetName()`](#c4d.LayerSet.GetName): Get the set’s name.

**Layer Membership**

- [`LayerSet.AddLayer()`](#c4d.LayerSet.AddLayer): Add a layer.
- [`LayerSet.Content()`](#c4d.LayerSet.Content): Check if the set is empty.
- [`LayerSet.FindLayerSet()`](#c4d.LayerSet.FindLayerSet): Check if a layer is in the set.
- [`LayerSet.FlushLayers()`](#c4d.LayerSet.FlushLayers): Flush all layers.
- [`LayerSet.IsLayerEnabled()`](#c4d.LayerSet.IsLayerEnabled): Check if a layer is enabled.
- [`LayerSet.RemoveLayer()`](#c4d.LayerSet.RemoveLayer): Remove a layer.

**Magic Methods**

- [`LayerSet.__init__()`](#c4d.LayerSet.__init__)

## Members <a id="members"></a>

### Display Modes <a id="c4d.LayerSet-method-Display-Modes"></a>

#### `LayerSet.GetMode(self)` <a id="c4d.LayerSet.GetMode"></a>

Returns the layer set mode.

**Return type:** int

**Returns:**

The mode:

|   |   |
|---|---|
| *LAYERSETMODE_LAYERS* | Layers / layer Sets. |
| *LAYERSETMODE_LAYERMASKS* | Layer masks. |
| *LAYERSETMODE_ALPHAS* | Alpha channels. |
| *LAYERSETMODE_LAYERALPHA* | Layer alpha. |
| *LAYERSETMODE_DISABLED* | Disabled. |

#### `LayerSet.GetPreviewMode(self)` <a id="c4d.LayerSet.GetPreviewMode"></a>

Return the preview mode.

**Return type:** int

**Returns:** The preview mode.

#### `LayerSet.SetMode(self, mode)` <a id="c4d.LayerSet.SetMode"></a>

Assign a new layer set mode.

**Parameters:**

**mode** (*int*) –

The mode:

|   |   |
|---|---|
| *LAYERSETMODE_LAYERS* | Layers / layer Sets. |
| *LAYERSETMODE_LAYERMASKS* | Layer masks. |
| *LAYERSETMODE_ALPHAS* | Alpha channels. |
| *LAYERSETMODE_LAYERALPHA* | Layer alpha. |
| *LAYERSETMODE_DISABLED* | Disabled. |

#### `LayerSet.SetPreviewMode(self, s)` <a id="c4d.LayerSet.SetPreviewMode"></a>

Set the preview mode.

**Parameters:** **s** (*int*) – The new preview mode.

### Identity And Transfer <a id="c4d.LayerSet-method-Identity-And-Transfer"></a>

#### `LayerSet.CopyTo(self, dst)` <a id="c4d.LayerSet.CopyTo"></a>

Copies the content from *self* to *dst*.

**Parameters:** **dst** ([*c4d.LayerSet*](#c4d.LayerSet)) – The destination layer set.

#### `LayerSet.GetName(self)` <a id="c4d.LayerSet.GetName"></a>

Get the set’s name.

**Return type:** str

**Returns:** The name of the set.

### Layer Membership <a id="c4d.LayerSet-method-Layer-Membership"></a>

#### `LayerSet.AddLayer(self, layer)` <a id="c4d.LayerSet.AddLayer"></a>

Add a layer.

**Parameters:** **layer** (*str*) – The layer to add.

#### `LayerSet.Content(self)` <a id="c4d.LayerSet.Content"></a>

Check if the set is empty.

**Return type:** bool

**Returns:** **True** if the set contains any layer, otherwise **False**.

#### `LayerSet.FindLayerSet(self, name)` <a id="c4d.LayerSet.FindLayerSet"></a>

Check if a layer is in the set.

**Parameters:** **name** (*str*) – The layer name to check for.

**Return type:** bool

**Returns:** **True** if the layer is in the set, otherwise **False**.

#### `LayerSet.FlushLayers(self)` <a id="c4d.LayerSet.FlushLayers"></a>

Flush all layers.

#### `LayerSet.IsLayerEnabled(self, name)` <a id="c4d.LayerSet.IsLayerEnabled"></a>

Check if a layer is enabled.

**Parameters:** **name** (*str*) – The layer name to check for.

**Return type:** bool

**Returns:** **True** if the layer is enabled, otherwise **False**.

#### `LayerSet.RemoveLayer(self, layer)` <a id="c4d.LayerSet.RemoveLayer"></a>

Remove a layer.

**Parameters:** **layer** (*str*) – The layer to remove.

### Magic Methods <a id="c4d.LayerSet-method-Magic-Methods"></a>

#### `LayerSet.__init__(self, v)` <a id="c4d.LayerSet.__init__"></a>

**Parameters:** **v** ([*c4d.LayerSet*](#c4d.LayerSet)) – Source layer set for copy constructor.
