<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseShader/index.html -->

# c4d.BaseShader <a id="c4d-baseshader"></a>

## *class* `c4d.BaseShader` <a id="c4d.BaseShader"></a>

Represents a shader in the shader tree of a channel.

Parent Class:

- [`c4d.BaseList2D`](../index.md#c4d.BaseList2D)

Child Class:

- [`c4d.LayerShader`](LayerShader/index.md#c4d.LayerShader)

## Overview <a id="overview"></a>

**Magic Methods**

- [`BaseShader.__init__()`](#c4d.BaseShader.__init__): Initialize a new [`BaseShader`](#c4d.BaseShader) in memory.

**Rendering Lifecycle**

- [`BaseShader.FreeRender()`](#c4d.BaseShader.FreeRender): Frees all resources used by this shader, allocated by calling `InitRender()`.
- [`BaseShader.GetRenderInfo()`](#c4d.BaseShader.GetRenderInfo): Calls *ShaderData.GetRenderInfo()* for the corresponding shader plugin.
- [`BaseShader.InitRender()`](#c4d.BaseShader.InitRender): Calls `ShaderData.InitRender()` for the corresponding shader plugin.

**Shader Evaluation**

- [`BaseShader.IsColorManagementOff()`](#c4d.BaseShader.IsColorManagementOff): It checks if color management is disabled for shaders within bump, alpha, displacement or normal channels when linear workflow is enabled.
- [`BaseShader.Sample()`](#c4d.BaseShader.Sample): Calls `ShaderData.Output()` for the corresponding shader plugin.
- [`BaseShader.SampleBump()`](#c4d.BaseShader.SampleBump): Calculates the bump mapping for a shader (and its children) with the same algorithm as Cinema 4D does.

**Shader Properties And Comparison**

- [`BaseShader.Compare()`](#c4d.BaseShader.Compare): Checks if this shader is similar to *dst*.
- [`BaseShader.GetBitmap()`](#c4d.BaseShader.GetBitmap): Returns the bitmap of shaders of type *Xbitmap*, otherwise None.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.BaseShader-method-Magic-Methods"></a>

#### `BaseShader.__init__(self, type)` <a id="c4d.BaseShader.__init__"></a>

Initialize a new [`BaseShader`](#c4d.BaseShader) in memory.

**Parameters:** **type** (*int*) – The shader type : [Shader Types](../../../../../../types/shaders.md).

### Rendering Lifecycle <a id="c4d.BaseShader-method-Rendering-Lifecycle"></a>

#### `BaseShader.FreeRender(self)` <a id="c4d.BaseShader.FreeRender"></a>

Frees all resources used by this shader, allocated by calling [`InitRender()`](#c4d.BaseShader.InitRender).

#### `BaseShader.GetRenderInfo(self)` <a id="c4d.BaseShader.GetRenderInfo"></a>

Calls *ShaderData.GetRenderInfo()* for the corresponding shader plugin.  
This retrieves information about what the plugin requires from the raytracer and what it will return.

**Return type:** int

**Returns:**

The return values are:

|   |   |
|---|---|
| *SHADERINFO_NONE* | None. |
| *SHADERINFO_TRANSFORM* | Channel needs back-transformed data. (Required for `BaseVolumeData.back_p`.) |
| *SHADERINFO_BUMP_SUPPORT* | Channel shader supports bump. This is strongly recommended for all shaders except simple 2D (UV) samplers. |
| *SHADERINFO_ALPHA_SUPPORT* | Channel shader supports alpha output. |
| *SHADERINFO_REFLECTIONS* | Channel shader computes reflections. |
| *SHADERINFO_DUDVREQUIRED* | Channel shader needs du/dv bump mapping data. See `BaseVolumeData.ddu` and `BaseVolumeData.ddv`. |
| *SHADERINFO_DYNAMICSUBSHADERS* | Channel shader has a dynamic list of sub-shaders in its description. |

#### `BaseShader.InitRender(self, is_)` <a id="c4d.BaseShader.InitRender"></a>

Calls `ShaderData.InitRender()` for the corresponding shader plugin.  
You have to do this before you can use the [`Sample()`](#c4d.BaseShader.Sample), [`SampleBump()`](#c4d.BaseShader.SampleBump) or [`GetBitmap()`](#c4d.BaseShader.GetBitmap) functions.

> **Note:**
>
> Remember to call [`FreeRender()`](#c4d.BaseShader.FreeRender) afterwards.  
> You aren’t allowed to call [`InitRender()`](#c4d.BaseShader.InitRender) multiple times without calling [`FreeRender()`](#c4d.BaseShader.FreeRender) in between, even from multiple threads!

**Parameters:** **is** ([*c4d.modules.render.InitRenderStruct*](../../../../../c4d.modules/render/InitRenderStruct/index.md#c4d.modules.render.InitRenderStruct)) – Information about the upcoming rendering.

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

### Shader Evaluation <a id="c4d.BaseShader-method-Shader-Evaluation"></a>

#### `BaseShader.IsColorManagementOff(self, doc)` <a id="c4d.BaseShader.IsColorManagementOff"></a>

It checks if color management is disabled for shaders within bump, alpha, displacement or normal channels when linear workflow is enabled.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document containing the shader to check if linear workflow is disabled in it.

**Return type:** bool

**Returns:** **True** if color managment is disabled, otherwise **False**.

#### `BaseShader.Sample(self, cd)` <a id="c4d.BaseShader.Sample"></a>

Calls `ShaderData.Output()` for the corresponding shader plugin.  
The channel color for the point cd.p is calculated.

> **Note:** This has to be done within a pair of [`InitRender()`](#c4d.BaseShader.InitRender) / [`FreeRender()`](#c4d.BaseShader.FreeRender) calls.

**Parameters:** **cd** ([*c4d.modules.render.ChannelData*](../../../../../c4d.modules/render/ChannelData/index.md#c4d.modules.render.ChannelData)) – The channel data to use.

**Return type:** [c4d.Vector](../../../../Vector/index.md#c4d.Vector)

**Returns:** The calculated color.

#### `BaseShader.SampleBump(self, cd, bumpflags)` <a id="c4d.BaseShader.SampleBump"></a>

Calculates the bump mapping for a shader (and its children) with the same algorithm as Cinema 4D does.  
The function returns the delta vector that is added to the normal.  
The resulting normal is calculated by:

```python
n_dst =  not(n_src + SampleBump(SAMPLEBUMP_NONE))
```

where **n_src** is the original normal and **n_dst** is the bumped normal.

> **Note:**
>
> This has to be done within a pair of [`InitRender()`](#c4d.BaseShader.InitRender) / [`FreeRender()`](#c4d.BaseShader.FreeRender) calls.  
> Also the `BaseVolumeData.ddu` and `BaseVolumeData.ddv` vectors have to be initialized.

**Parameters:**

- **cd** ([*c4d.modules.render.ChannelData*](../../../../../c4d.modules/render/ChannelData/index.md#c4d.modules.render.ChannelData)) – The channel data to use.

- **bumpflags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *SAMPLEBUMP_NONE* | None. |
  | *SAMPLEBUMP_MIPFALLOFF* | Additional bump change over distance is considered. |

**Return type:** [c4d.Vector](../../../../Vector/index.md#c4d.Vector)

**Returns:** The delta normal.

### Shader Properties And Comparison <a id="c4d.BaseShader-method-Shader-Properties-And-Comparison"></a>

#### `BaseShader.Compare(self, dst)` <a id="c4d.BaseShader.Compare"></a>

Checks if this shader is similar to *dst*.

**Parameters:** **dst** ([*c4d.BaseShader*](#c4d.BaseShader)) – The shader to compare to.

**Return type:** bool

**Returns:** **True** if the plugin shaders are the same, otherwise **False**.

#### `BaseShader.GetBitmap(self)` <a id="c4d.BaseShader.GetBitmap"></a>

Returns the bitmap of shaders of type *Xbitmap*, otherwise None.

> **Note:** This has to be done within a pair of [`InitRender()`](#c4d.BaseShader.InitRender) / [`FreeRender()`](#c4d.BaseShader.FreeRender) calls.

Here is an example.

```python
# Get the first material in the document.
material = doc.GetFirstMaterial()
if material is None:
    raise RuntimeError("Could not find material.")

# Retrieve the shader linked in the color channel.
shader = material[c4d.MATERIAL_COLOR_SHADER]
if shader is None:
    raise RuntimeError("Material has no shader.")

# Initialize an InitRenderStruct.
irs = render.InitRenderStruct()
if irs and shader.InitRender(irs) == c4d.INITRENDERRESULT_OK:
    # Get the bitmap.
    bitmap = shader.GetBitmap()
    # Free the renderer so that that its memory can be freed.
    shader.FreeRender()
    # Show the bitmap in the Picture Viewer.
    if bitmap is not None:
        bitmaps.ShowBitmap(bitmap)
```

**Return type:** Optional[[c4d.bitmaps.BaseBitmap](../../../../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]

**Returns:**

The bitmap.

> **Note:** The returned bitmap must be accessed as read-only.
