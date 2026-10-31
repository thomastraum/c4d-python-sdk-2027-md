<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/render/VolumeData/index.html -->

# c4d.modules.render.VolumeData <a id="c4d-modules-render-volumedata"></a>

## *class* `c4d.modules.render.VolumeData` <a id="c4d.modules.render.VolumeData"></a>

Parent Class:

- [`c4d.modules.render.BaseVolumeData`](../BaseVolumeData/index.md#c4d.modules.render.BaseVolumeData)

## Overview <a id="overview"></a>

**Camera And Ray Mapping**

- [`VolumeData.CameraToScreen()`](#c4d.modules.render.VolumeData.CameraToScreen): Transform camera to screen coordinates.
- [`VolumeData.GetRay()`](#c4d.modules.render.VolumeData.GetRay): Generate the view ray for a position.
- [`VolumeData.ScreenToCamera()`](#c4d.modules.render.VolumeData.ScreenToCamera): Transform screen to camera coordinates.

**CPU Resources**

- [`VolumeData.GetCPUCount()`](#c4d.modules.render.VolumeData.GetCPUCount): Returns the CPU count the renderer is utilizing.
- [`VolumeData.GetCurrentCPU()`](#c4d.modules.render.VolumeData.GetCurrentCPU): Returns the current CPU on which the shader is executed.

**Lifecycle And Copying**

- [`VolumeData.CopyTo()`](#c4d.modules.render.VolumeData.CopyTo): Copy this to another [`VolumeData`](#c4d.modules.render.VolumeData).
- [`VolumeData.Init()`](#c4d.modules.render.VolumeData.Init): Initializes this [`VolumeData`](#c4d.modules.render.VolumeData) object with the data from the *from* object.

**Lighting And Illumination**

- [`VolumeData.CalcArea()`](#c4d.modules.render.VolumeData.CalcArea): If you code custom illumination models (e.g.
- [`VolumeData.CalcShadow()`](#c4d.modules.render.VolumeData.CalcShadow): Compute a shadow.
- [`VolumeData.CalcVisibleLight()`](#c4d.modules.render.VolumeData.CalcVisibleLight): Returns the mixed color of all visible lights on a given ray span.
- [`VolumeData.GetLight()`](#c4d.modules.render.VolumeData.GetLight): Get the given light source.
- [`VolumeData.GetLightFalloff()`](#c4d.modules.render.VolumeData.GetLightFalloff): Calculate the light falloff function (light intensity for a distance).
- [`VolumeData.IlluminanceAnyPoint()`](#c4d.modules.render.VolumeData.IlluminanceAnyPoint): Calculates the light intensity for a given point *p*.
- [`VolumeData.IlluminateSurfacePoint()`](#c4d.modules.render.VolumeData.IlluminateSurfacePoint): Calculates the intensity of incoming light for a given light and surface point.

**Pixel Rendering**

- [`VolumeData.CalcFgBg()`](#c4d.modules.render.VolumeData.CalcFgBg): Calculates the foreground or background color and alpha at (*x*, *y*).
- [`VolumeData.GetXY()`](#c4d.modules.render.VolumeData.GetXY): Returns the current X/Y pixel position in render resolution.
- [`VolumeData.SetXY()`](#c4d.modules.render.VolumeData.SetXY): Sets the current X/Y pixel position in render resolution.

**Progress Feedback**

- [`VolumeData.StatusSetBar()`](#c4d.modules.render.VolumeData.StatusSetBar): Set the progress bar during initialization of your shader or videopost effect.
- [`VolumeData.StatusSetSpinMode()`](#c4d.modules.render.VolumeData.StatusSetSpinMode): Set the render progress bar spinning.
- [`VolumeData.StatusSetText()`](#c4d.modules.render.VolumeData.StatusSetText): Set the status bar text during initialization of your shader or videopost effect.

**Render Process Control**

- [`VolumeData.OutOfMemory()`](#c4d.modules.render.VolumeData.OutOfMemory): Notify Cinema 4D that a (severe) out-of-memory condition occurred.
- [`VolumeData.SkipRenderProcess()`](#c4d.modules.render.VolumeData.SkipRenderProcess): Skips the render process.

**Scene Element Counts**

- [`VolumeData.GetLightCount()`](#c4d.modules.render.VolumeData.GetLightCount): Returns the overall number of lights.
- [`VolumeData.GetObjCount()`](#c4d.modules.render.VolumeData.GetObjCount): Returns the overall number of objects.
- [`VolumeData.GetSkyCount()`](#c4d.modules.render.VolumeData.GetSkyCount): Returns the number of skies.

**Surface Geometry**

- [`VolumeData.GetRS()`](#c4d.modules.render.VolumeData.GetRS): Calculates the R/S parameters for a point.
- [`VolumeData.GetSmoothedNormal()`](#c4d.modules.render.VolumeData.GetSmoothedNormal): Returns the phong normal for a point.
- [`VolumeData.GetWeights()`](#c4d.modules.render.VolumeData.GetWeights): Returns barycentric coordinates for a point on the surface of a polygon.

**Video Post Effects**

- [`VolumeData.FindVideoPost()`](#c4d.modules.render.VolumeData.FindVideoPost): Returns a video post effect for this render process by ID.
- [`VolumeData.GetVideoPost()`](#c4d.modules.render.VolumeData.GetVideoPost): Returns the n-th video post effect for this render process.

## Members <a id="members"></a>

### Camera And Ray Mapping <a id="c4d.modules.render.VolumeData-method-Camera-And-Ray-Mapping"></a>

#### `VolumeData.CameraToScreen(self, p)` <a id="c4d.modules.render.VolumeData.CameraToScreen"></a>

Transform camera to screen coordinates. During QTVR rendering same point is returned.

**Parameters:** **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The camera coordinate.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The screen coordinate.

#### `VolumeData.GetRay(self, x, y, ray)` <a id="c4d.modules.render.VolumeData.GetRay"></a>

Generate the view ray for a position.

> **Note:** This function does not set `Ray.pp` [0..2], `Ray.vv` [0..2], `Ray.transport` and `Ray.ior`.

**Parameters:**

- **x** (*float*) – The X position for the view ray in screen space coordinates.
- **y** (*float*) – The Y position for the view ray in screen space coordinates.
- **ray** ([*c4d.modules.render.Ray*](../Ray/index.md#c4d.modules.render.Ray)) – The view ray.

#### `VolumeData.ScreenToCamera(self, p)` <a id="c4d.modules.render.VolumeData.ScreenToCamera"></a>

Transform screen to camera coordinates. During QTVR rendering same point is returned.

**Parameters:** **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The screen coordinate.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The camera coordinate.

### CPU Resources <a id="c4d.modules.render.VolumeData-method-CPU-Resources"></a>

#### `VolumeData.GetCPUCount(self)` <a id="c4d.modules.render.VolumeData.GetCPUCount"></a>

Returns the CPU count the renderer is utilizing.

**Return type:** int

**Returns:** The number of CPUs.

#### `VolumeData.GetCurrentCPU(self)` <a id="c4d.modules.render.VolumeData.GetCurrentCPU"></a>

Returns the current CPU on which the shader is executed.

**Return type:** int

**Returns:** The running CPU id.

### Lifecycle And Copying <a id="c4d.modules.render.VolumeData-method-Lifecycle-And-Copying"></a>

#### `VolumeData.CopyTo(self, dst)` <a id="c4d.modules.render.VolumeData.CopyTo"></a>

Copy this to another [`VolumeData`](#c4d.modules.render.VolumeData).

**Parameters:** **dst** ([*c4d.modules.render.VolumeData*](#c4d.modules.render.VolumeData)) – The destination VolumeData.

#### `VolumeData.Init(self, from_)` <a id="c4d.modules.render.VolumeData.Init"></a>

Initializes this [`VolumeData`](#c4d.modules.render.VolumeData) object with the data from the *from* object.

> **Note:** Only the most essential parts are copied over, including the render instance.

**Parameters:** **from** ([*c4d.modules.render.VolumeData*](#c4d.modules.render.VolumeData)) – Source object.

### Lighting And Illumination <a id="c4d.modules.render.VolumeData-method-Lighting-And-Illumination"></a>

#### `VolumeData.CalcArea(self, light, nodiffuse, nospecular, specular_exponent, ray_vector, p, bumpn, orign, raybits, ignoreLightColor)` <a id="c4d.modules.render.VolumeData.CalcArea"></a>

If you code custom illumination models (e.g. different specular function) you can do this for standard lightsources easily.  
For area lights you’ll usually want to fall back to the default illumination model though, as otherwise you’d have to rebuild the sample code of area lights!

**Parameters:**

- **light** (*ptr*) – The area light to calculate.

- **nodiffuse** (*bool*) – **True** if the diffuse value should not be calculated, otherwise **False**.

- **nospecular** (*bool*) – **True** if the specular value should not be calculated, otherwise **False**.

- **specular_exponent** (*float*) – Specular exponent to use.

- **ray_vector** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – Ray vector.

- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The surface point.

- **bumpn** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The bump normal.

- **orign** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The original normal.

- **raybits** (*int*) –

  The ray bits:

  |   |   |
  |---|---|
  | *RAYBIT_NONE* | None. |
  | *RAYBIT_REFLECTION* | Ray chain contains a reflection ray. |
  | *RAYBIT_TRANSPARENCY* | Ray chain contains a transparency ray (refractions are not contained). |
  | *RAYBIT_REFRACTION* | Ray chain contains a refraction ray. |
  | *RAYBIT_CUSTOM* | Ray chain contains a custom ray. |
  | *RAYBIT_CURR_REFLECTION* | Current ray is a reflection ray. |
  | *RAYBIT_CURR_TRANSPARENCY* | Current ray is a transparency ray. |
  | *RAYBIT_CURR_REFRACTION* | Current ray is a refraction ray. |
  | *RAYBIT_CURR_CUSTOM* | Current ray is a custom ray. |
  | *RAYBIT_VOLUMETRICLIGHT* | Current ray is used to calculate a volumetric light. |
  | *RAYBIT_ALLOWVLMIX* | Custom mixing of visible light sources allowed for the ray; bit must be deleted by shader if used. |
  | *RAYBIT_GI* | Current ray is a Global Illumination ray. |
  | *RAYBIT_BLURRY* | Current ray is a blurry ray. |
  | *RAYBIT_SSS* | Current ray is a subsurface scattering ray. |
  | *RAYBIT_AO* | Current ray is an Ambient Occlusion ray. |
  | *RAYBIT_COMPOSITING* | Current ray is a compositing ray. |

- **ignoreLightColor** (*bool*) –

*New in version R20:* **True** to ignore the light color into the result, otherwise **False**.

**Return type:** Tuple[[c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector), [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The diffuse and specular components.

#### `VolumeData.CalcShadow(self, l, p, bumpn, phongn, orign, rayv, transparency, hitid, raybits)` <a id="c4d.modules.render.VolumeData.CalcShadow"></a>

Compute a shadow.

**Parameters:**

- **l** (*ptr*) – The illuminating light source.

- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The point in global coordinates.

- **bumpn** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The bump normal.

- **phongn** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The phong normal.

- **orign** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The original normal.

- **rayv** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The ray vector.

- **transparency** (*bool*) – **True** if transparencies/alphas for inbetween objects should be evaluated.

- **hitid** (*ptr*) – The global RayHitID for the surface intersection (to avoid self shadowing), or RayHitID() if you are not on a surface or do not wish to make use of this avoidance.

- **raybits** (*int*) –

  The ray bits:

  |   |   |
  |---|---|
  | *RAYBIT_NONE* | None. |
  | *RAYBIT_REFLECTION* | Ray chain contains a reflection ray. |
  | *RAYBIT_TRANSPARENCY* | Ray chain contains a transparency ray (refractions are not contained). |
  | *RAYBIT_REFRACTION* | Ray chain contains a refraction ray. |
  | *RAYBIT_CUSTOM* | Ray chain contains a custom ray. |
  | *RAYBIT_CURR_REFLECTION* | Current ray is a reflection ray. |
  | *RAYBIT_CURR_TRANSPARENCY* | Current ray is a transparency ray. |
  | *RAYBIT_CURR_REFRACTION* | Current ray is a refraction ray. |
  | *RAYBIT_CURR_CUSTOM* | Current ray is a custom ray. |
  | *RAYBIT_VOLUMETRICLIGHT* | Current ray is used to calculate a volumetric light. |
  | *RAYBIT_ALLOWVLMIX* | Custom mixing of visible light sources allowed for the ray; bit must be deleted by shader if used. |
  | *RAYBIT_GI* | Current ray is a Global Illumination ray. |
  | *RAYBIT_BLURRY* | Current ray is a blurry ray. |
  | *RAYBIT_SSS* | Current ray is a subsurface scattering ray. |
  | *RAYBIT_AO* | Current ray is an Ambient Occlusion ray. |
  | *RAYBIT_COMPOSITING* | Current ray is a compositing ray. |

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The returned shadow value. If there is no shadow, 0.0 will be returned. 1.0 is the maximum shadow value for each component.

#### `VolumeData.CalcVisibleLight(self, ray, maxdist)` <a id="c4d.modules.render.VolumeData.CalcVisibleLight"></a>

Returns the mixed color of all visible lights on a given ray span.

**Parameters:**

- **ray** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The ray span.
- **maxdist** (*float*) – The maximum distance for the lights.

**Return type:** Tuple[[c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector), [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** The mixed color of the lights and a value indicating if some light sources have a dust effect (!= 0 in this case).

#### `VolumeData.GetLight(self, index)` <a id="c4d.modules.render.VolumeData.GetLight"></a>

Get the given light source.

**Parameters:** **index** (*int*) – The index of the light source to return.

**Return type:** ptr

**Returns:** The light source.

#### `VolumeData.GetLightFalloff(self)` <a id="c4d.modules.render.VolumeData.GetLightFalloff"></a>

Calculate the light falloff function (light intensity for a distance).

#### `VolumeData.IlluminanceAnyPoint(self, p, flags, raybits)` <a id="c4d.modules.render.VolumeData.IlluminanceAnyPoint"></a>

Calculates the light intensity for a given point *p*.  
This routine can calculate the illumination for any point in space and is widely used for transparent volumetric shaders (gases, clouds etc.).

**Parameters:**

- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The point in global coordinates.

- **raybits** (*int*) – The global coordinate point to calculate the illumination for.

- **flags** (*int*) –

  The illuminate flags:

  |   |   |
  |---|---|
  | *ILLUMINATEFLAGS_NONE* | None. |
  | *ILLUMINATEFLAGS_SHADOW* | Full shadow calculations. |
  | *ILLUMINATEFLAGS_NOENVIRONMENT* | Shadow calculations are enabled but no environment shading will be calculated. |
  | *ILLUMINATEFLAGS_DISABLESHADOWMAP_CORRECTION* | Shadow maps evaluate the normal at a surface point, to avoid the problem of self-shadowing (that is otherwise inherent due to the way the algorithm works). If a free point is sampled in space (where no surface is) this correction has to be disabled though, otherwise wrong results will be returned. |
  | *ILLUMINATEFLAGS_DISABLESHADOWCASTERMP_CORRECTION* | Private. |
  | *ILLUMINATEFLAGS_LIGHTDIRNORMALS* | Private. |
  | *ILLUMINATEFLAGS_NODISTANCEFALLOFF* | Do not take distance falloff into account. |
  | *ILLUMINATEFLAGS_NOGRAIN* | Do not take grain into account. |
  | *ILLUMINATEFLAGS_BACKLIGHT* | Take backlight into account. |

- **raybits** –

  The ray bits:

  |   |   |
  |---|---|
  | *RAYBIT_NONE* | None. |
  | *RAYBIT_REFLECTION* | Ray chain contains a reflection ray. |
  | *RAYBIT_TRANSPARENCY* | Ray chain contains a transparency ray (refractions are not contained). |
  | *RAYBIT_REFRACTION* | Ray chain contains a refraction ray. |
  | *RAYBIT_CUSTOM* | Ray chain contains a custom ray. |
  | *RAYBIT_CURR_REFLECTION* | Current ray is a reflection ray. |
  | *RAYBIT_CURR_TRANSPARENCY* | Current ray is a transparency ray. |
  | *RAYBIT_CURR_REFRACTION* | Current ray is a refraction ray. |
  | *RAYBIT_CURR_CUSTOM* | Current ray is a custom ray. |
  | *RAYBIT_VOLUMETRICLIGHT* | Current ray is used to calculate a volumetric light. |
  | *RAYBIT_ALLOWVLMIX* | Custom mixing of visible light sources allowed for the ray; bit must be deleted by shader if used. |
  | *RAYBIT_GI* | Current ray is a Global Illumination ray. |
  | *RAYBIT_BLURRY* | Current ray is a blurry ray. |
  | *RAYBIT_SSS* | Current ray is a subsurface scattering ray. |
  | *RAYBIT_AO* | Current ray is an Ambient Occlusion ray. |
  | *RAYBIT_COMPOSITING* | Current ray is a compositing ray. |

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:**

The returned color.

> **Note:** The returned color components can exceed values of 1.0!

#### `VolumeData.IlluminateSurfacePoint(self, rl, p, bumpn, phongn, orign, ray_vector, flags, hitid, raybits, cosine_cutoff)` <a id="c4d.modules.render.VolumeData.IlluminateSurfacePoint"></a>

Calculates the intensity of incoming light for a given light and surface point.

> **Note:** Used for custom illumination models.

**Parameters:**

- **rl** (*PyCObject*) – The illuminating light.

- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The surface point.

- **bumpn** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The bump normal.

- **phongn** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The phong normal.

- **orign** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The original normal.

- **ray_vector** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The ray vector.

- **flags** (*int*) –

  The illuminate flags:

  |   |   |
  |---|---|
  | *ILLUMINATEFLAGS_NONE* | None. |
  | *ILLUMINATEFLAGS_SHADOW* | Full shadow calculations. |
  | *ILLUMINATEFLAGS_NOENVIRONMENT* | Shadow calculations are enabled but no environment shading will be calculated. |
  | *ILLUMINATEFLAGS_DISABLESHADOWMAP_CORRECTION* | Shadow maps evaluate the normal at a surface point, to avoid the problem of self-shadowing (that is otherwise inherent due to the way the algorithm works). If a free point is sampled in space (where no surface is) this correction has to be disabled though, otherwise wrong results will be returned. |
  | *ILLUMINATEFLAGS_DISABLESHADOWCASTERMP_CORRECTION* | Private. |
  | *ILLUMINATEFLAGS_LIGHTDIRNORMALS* | Private. |
  | *ILLUMINATEFLAGS_NODISTANCEFALLOFF* | Do not take distance falloff into account. |
  | *ILLUMINATEFLAGS_NOGRAIN* | Do not take grain into account. |
  | *ILLUMINATEFLAGS_BACKLIGHT* | Take backlight into account. |

- **hitid** (*PyCObject*) – The global RayHitID.

- **raybits** (*int*) –

  The ray bits:

  |   |   |
  |---|---|
  | *RAYBIT_NONE* | None. |
  | *RAYBIT_REFLECTION* | Ray chain contains a reflection ray. |
  | *RAYBIT_TRANSPARENCY* | Ray chain contains a transparency ray (refractions are not contained). |
  | *RAYBIT_REFRACTION* | Ray chain contains a refraction ray. |
  | *RAYBIT_CUSTOM* | Ray chain contains a custom ray. |
  | *RAYBIT_CURR_REFLECTION* | Current ray is a reflection ray. |
  | *RAYBIT_CURR_TRANSPARENCY* | Current ray is a transparency ray. |
  | *RAYBIT_CURR_REFRACTION* | Current ray is a refraction ray. |
  | *RAYBIT_CURR_CUSTOM* | Current ray is a custom ray. |
  | *RAYBIT_VOLUMETRICLIGHT* | Current ray is used to calculate a volumetric light. |
  | *RAYBIT_ALLOWVLMIX* | Custom mixing of visible light sources allowed for the ray; bit must be deleted by shader if used. |
  | *RAYBIT_GI* | Current ray is a Global Illumination ray. |
  | *RAYBIT_BLURRY* | Current ray is a blurry ray. |
  | *RAYBIT_SSS* | Current ray is a subsurface scattering ray. |
  | *RAYBIT_AO* | Current ray is an Ambient Occlusion ray. |
  | *RAYBIT_COMPOSITING* | Current ray is a compositing ray. |

- **cosine_cutoff** (*bool*) – **True** if cosine cut-off should be used, otherwise **False**.

**Return type:** Tuple[[c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector), [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** A tuple with the color result for the calculation and the light to point vector.

### Pixel Rendering <a id="c4d.modules.render.VolumeData-method-Pixel-Rendering"></a>

#### `VolumeData.CalcFgBg(self, foreground, x, y, subx, suby)` <a id="c4d.modules.render.VolumeData.CalcFgBg"></a>

Calculates the foreground or background color and alpha at (*x*, *y*).

**Parameters:**

- **foreground** (*bool*) – **True** to calculate the foreground color. Otherwise the background color is calculated.
- **x** (*int*) – X coordinate.
- **y** (*int*) – Y coordinate.
- **subx** (*int*) – Sub pixel X position. (0 <= subx <= 15)
- **suby** (*int*) – Sub pixel Y position. (0 <= suby <= 15)

**Return type:** Tuple[ [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector), float]

**Returns:** The background/foreground color and alpha.

#### `VolumeData.GetXY(self)` <a id="c4d.modules.render.VolumeData.GetXY"></a>

Returns the current X/Y pixel position in render resolution. Render resolution is the screen resolution multiplied by ‘scale’.

**Return type:** Tuple[int, int, int]

**Returns:**

The X, Y pixel positions and render scale.

> **Note:** X/scale and Y/scale is the screen position.

#### `VolumeData.SetXY(self, x, y)` <a id="c4d.modules.render.VolumeData.SetXY"></a>

Sets the current X/Y pixel position in render resolution. Render resolution is the screen resolution multiplied by ‘scale’.

> **Note:** X/scale and Y/scale is the screen position.

> **Note:** Some Shaders use the screen pixel position. Plugins (like the Baker for instance) can change this position without having to render an image.

**Parameters:**

- **x** (*float*) – The X pixel position to set.
- **y** (*float*) – The Y pixel position to set.

### Progress Feedback <a id="c4d.modules.render.VolumeData-method-Progress-Feedback"></a>

#### `VolumeData.StatusSetBar(self)` <a id="c4d.modules.render.VolumeData.StatusSetBar"></a>

Set the progress bar during initialization of your shader or videopost effect.

> **Note:** The value passed will only be displayed if it is bigger than the previous one. To reset the bar call *StatusSetText* (“”).

#### `VolumeData.StatusSetSpinMode(self, on)` <a id="c4d.modules.render.VolumeData.StatusSetSpinMode"></a>

Set the render progress bar spinning. Use this to indicate that your plugin is still processing even if the progress bar is not increasing.

**Parameters:** **on** (*bool*) – **True** to set the progress bar spinning, **False** to stop it.

#### `VolumeData.StatusSetText(self, str)` <a id="c4d.modules.render.VolumeData.StatusSetText"></a>

Set the status bar text during initialization of your shader or videopost effect.

> **Note:** If an empty string is passed the status bar will be cleared.

**Parameters:** **str** (*str*) – The status text to display.

### Render Process Control <a id="c4d.modules.render.VolumeData-method-Render-Process-Control"></a>

#### `VolumeData.OutOfMemory(self)` <a id="c4d.modules.render.VolumeData.OutOfMemory"></a>

Notify Cinema 4D that a (severe) out-of-memory condition occurred.  
Cinema 4D will stop as soon as possible, but there is no guarantee when exactly.  
It is possible that your shader could still be called several times, so it has to be programmed to handle this and to be crash-proof.

#### `VolumeData.SkipRenderProcess(self)` <a id="c4d.modules.render.VolumeData.SkipRenderProcess"></a>

Skips the render process. (Useful for custom renderers.)

### Scene Element Counts <a id="c4d.modules.render.VolumeData-method-Scene-Element-Counts"></a>

#### `VolumeData.GetLightCount(self)` <a id="c4d.modules.render.VolumeData.GetLightCount"></a>

Returns the overall number of lights.

**Return type:** int

**Returns:** The number of lights.

#### `VolumeData.GetObjCount(self)` <a id="c4d.modules.render.VolumeData.GetObjCount"></a>

Returns the overall number of objects.

**Return type:** int

**Returns:** The total number of objects.

#### `VolumeData.GetSkyCount(self)` <a id="c4d.modules.render.VolumeData.GetSkyCount"></a>

Returns the number of skies.

**Return type:** int

**Returns:** The number of skies.

### Surface Geometry <a id="c4d.modules.render.VolumeData-method-Surface-Geometry"></a>

#### `VolumeData.GetRS(self, hitid, p)` <a id="c4d.modules.render.VolumeData.GetRS"></a>

Calculates the R/S parameters for a point.  
If you want to calculate weighted data (e.g. based upon a color for each polygon point) you can do this the following way:

```python
r, s = GetRS(hitid, p)
result = [color a] * (1.0-r-s) + [color d]*r + [color c]*s
```

**Parameters:**

- **hitid** (*ptr*) – The global RayHitID.
- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The point.

**Return type:** Tuple[bool, float, float]

**Returns:**

If the polygon is a quadrangle then the first value holds True for the second part (a-c-d) of the quadrangle or False for the first part (a-b-c). If the polygon is a triangle then this is the same as the first part of a quadrangle (a-b-c).  
The 2nd and 3rd values are the R and S parameters for point *p*.

#### `VolumeData.GetSmoothedNormal(self, hitid, p)` <a id="c4d.modules.render.VolumeData.GetSmoothedNormal"></a>

Returns the phong normal for a point.

**Parameters:**

- **hitid** (*ptr*) –

  The global RayHitID.

  > **Note:** Must be a valid RayHitID.

- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) –

  The point for the phong normal.

  > **Note:** The point must be within the surface boundaries of the polygon.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The phong normal.

#### `VolumeData.GetWeights(self, hitid, p)` <a id="c4d.modules.render.VolumeData.GetWeights"></a>

Returns barycentric coordinates for a point on the surface of a polygon.  
Cinema 4D uses enhanced interpolation routines for quadrangles, so you’ll get a higher quality using it instead of considering a quadrangle as two triangles.  
The routine works for any type of polygon, including triangles and non-coplanar quadrangles.

> **Note:**
>
> The function returns a tuple with the weight factors for the global polygon with ID *hitid* at *p*.  
> Works similar to [`GetRS()`](#c4d.modules.render.VolumeData.GetRS), but has a higher quality.

**Parameters:**

- **hitid** (*ptr*) – The global RayHitID.
- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – Point on polygon.

**Return type:** Tuple[float, float, float, float]

**Returns:** A tuple with the respective weight factors for points A, B, C and D.

### Video Post Effects <a id="c4d.modules.render.VolumeData-method-Video-Post-Effects"></a>

#### `VolumeData.FindVideoPost(self, id)` <a id="c4d.modules.render.VolumeData.FindVideoPost"></a>

Returns a video post effect for this render process by ID.

**Parameters:** **id** (*int*) – The video post effect ID.

**Return type:** Optional[[c4d.BaseList2D](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The found video post, or **None** if it doesn’t exist.

#### `VolumeData.GetVideoPost(self, nth)` <a id="c4d.modules.render.VolumeData.GetVideoPost"></a>

Returns the n-th video post effect for this render process.

**Parameters:** **nth** (*int*) – nth The nth index of the videopost effect.

**Return type:** Optional[[c4d.BaseList2D](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The video post, or **None** if the index is too large.
