<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseData/NodeData/ShaderData/index.html -->

# c4d.plugins.ShaderData <a id="c4d-plugins-shaderdata"></a>

## *class* `c4d.plugins.ShaderData` <a id="c4d.plugins.ShaderData"></a>

A data class for creating shader (channel shader) plugins.  
Use [`RegisterShaderPlugin()`](../../../index.md#c4d.plugins.RegisterShaderPlugin) to register the plugin.  
A registered shader will appear in the popup menu of the channels in the Materials Manager in Cinema 4D.

Here are some general comments on the shader API:

> - Coordinate Systems: if there is no further note all elements like points, normals etc. then they are always given in global coordinates.
> - Angle Systems: all angle values are always given in radians. Use [`Deg`](../../../../c4d.utils/index.md#c4d.utils.Deg) (angle) for conversion if needed.
> - Vectors: all normals and ray vectors must be normalized. Also, all normals and ray vectors you receive from Cinema 4D are normalized.

Parent Class:

- [`c4d.plugins.NodeData`](../index.md#c4d.plugins.NodeData)

## Overview <a id="overview"></a>

**Render Lifecycle**

- [`ShaderData.FreeRender()`](#c4d.plugins.ShaderData.FreeRender): Override - Free any resources used for the precalculated data from `InitRender()`.
- [`ShaderData.InitRender()`](#c4d.plugins.ShaderData.InitRender): Override - Pre-calculate any data for rendering.

**Surface Shading**

- [`ShaderData.Output()`](#c4d.plugins.ShaderData.Output): Override - Called for each point of the visible surface of a shaded object.
- [`ShaderData.SetExceptionColor()`](#c4d.plugins.ShaderData.SetExceptionColor): Set the exception color.

## Members <a id="members"></a>

### Render Lifecycle <a id="c4d.plugins.ShaderData-method-Render-Lifecycle"></a>

#### `ShaderData.FreeRender(self, sh)` <a id="c4d.plugins.ShaderData.FreeRender"></a>

Override - Free any resources used for the precalculated data from [`InitRender()`](#c4d.plugins.ShaderData.InitRender).

**Parameters:** **sh** ([*c4d.BaseShader*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseShader/index.md#c4d.BaseShader)) – The shader node connected with this instance.

#### `ShaderData.InitRender(self, sh, irs)` <a id="c4d.plugins.ShaderData.InitRender"></a>

Override - Pre-calculate any data for rendering.

**Parameters:**

- **sh** ([*c4d.BaseShader*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseShader/index.md#c4d.BaseShader)) – The shader node connected with this instance.
- **irs** ([*c4d.modules.render.InitRenderStruct*](../../../../c4d.modules/render/InitRenderStruct/index.md#c4d.modules.render.InitRenderStruct)) – Information about the upcoming rendering.

**Return type:** int

**Returns:**

Result of the initialisation:

|   |   |
|---|---|
| *INITRENDERRESULT_OK* | Everything is OK, there was no error. |
| *INITRENDERRESULT_OUTOFMEMORY* | Not enough memory. |
| *INITRENDERRESULT_ASSETMISSING* | Assets (textures etc.) are missing. |
| *INITRENDERRESULT_UNKNOWNERROR* | Unknown error. |
| *INITRENDERRESULT_USERBREAK* | *Changed in version R17.032:* Was *INITRENDERRESULT_THREADEDLOCK*. Thread has been canceled. |

### Surface Shading <a id="c4d.plugins.ShaderData-method-Surface-Shading"></a>

#### `ShaderData.Output(self, sh, cd)` <a id="c4d.plugins.ShaderData.Output"></a>

Override - Called for each point of the visible surface of a shaded object.  
Here you should calculate and return the channel color for the point *cd*.p.

**Important**:

> No OS calls are allowed during this function.  
> Doing so could cause a crash, since it can be called in a multi-processor context.

**Parameters:**

- **sh** ([*c4d.BaseShader*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseShader/index.md#c4d.BaseShader)) – The shader node connected with this instance.
- **cd** ([*c4d.modules.render.ChannelData*](../../../../c4d.modules/render/ChannelData/index.md#c4d.modules.render.ChannelData)) – Channel data to use and/or modify.

**Return type:** [c4d.Vector](../../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The calculated color.

#### `ShaderData.SetExceptionColor(self, col)` <a id="c4d.plugins.ShaderData.SetExceptionColor"></a>

Set the exception color.

**Parameters:** **col** ([*c4d.Vector*](../../../../c4d/Vector/index.md#c4d.Vector)) – The exception color.
