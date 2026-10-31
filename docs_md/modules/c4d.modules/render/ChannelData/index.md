<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/render/ChannelData/index.html -->

# c4d.modules.render.ChannelData <a id="c4d-modules-render-channeldata"></a>

## *class* `c4d.modules.render.ChannelData` <a id="c4d.modules.render.ChannelData"></a>

**Attributes**

## `c4d.modules.render.ChannelData.p` <a id="c4d.modules.render.ChannelData.p"></a>

The texture position in UVW coordinates.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.ChannelData.n` <a id="c4d.modules.render.ChannelData.n"></a>

The surface normal.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.ChannelData.d` <a id="c4d.modules.render.ChannelData.d"></a>

The MIP sample radius in UVW coordinates.

**Type:** [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)

## `c4d.modules.render.ChannelData.t` <a id="c4d.modules.render.ChannelData.t"></a>

The current time in seconds.

**Type:** float

## `c4d.modules.render.ChannelData.texflag` <a id="c4d.modules.render.ChannelData.texflag"></a>

The texture flags, these values are:

|   |   |
|---|---|
| *TEX_TILE* | Texture tile enabled. |
| *TEX_MIRROR* | Texture mirroring enabled. |
| *TEX_ALPHA* | Texture uses alpha channel (for use within channel shaders). |
| *TEX_BUMP* | Bump calculation. |

## `c4d.modules.render.ChannelData.vd` <a id="c4d.modules.render.ChannelData.vd"></a>

[Read-only]

Volume information, this can be **None**.

**Type:** Optional[c4d.modules.render.VolumeData]

## `c4d.modules.render.ChannelData.off` <a id="c4d.modules.render.ChannelData.off"></a>

The MIP blur offset.

**Type:** float

## `c4d.modules.render.ChannelData.scale` <a id="c4d.modules.render.ChannelData.scale"></a>

The MIP blur scale.

**Type:** float

## Overview <a id="overview"></a>

- [`ChannelData.__init__()`](#c4d.modules.render.ChannelData.__init__): Initializes a new channel data, optionally from *t_vd* [`BaseVolumeData`](../BaseVolumeData/index.md#c4d.modules.render.BaseVolumeData) if passed.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.modules.render.ChannelData-method-Magic-Methods"></a>

#### `ChannelData.__init__(self, t_vd)` <a id="c4d.modules.render.ChannelData.__init__"></a>

Initializes a new channel data, optionally from *t_vd* [`BaseVolumeData`](../BaseVolumeData/index.md#c4d.modules.render.BaseVolumeData) if passed.

**Parameters:** **t_vd** ([*c4d.modules.render.BaseVolumeData*](../BaseVolumeData/index.md#c4d.modules.render.BaseVolumeData)) – The volume data to take [`p`](#c4d.modules.render.ChannelData.p), [`n`](#c4d.modules.render.ChannelData.n) and [`d`](#c4d.modules.render.ChannelData.d) from.
