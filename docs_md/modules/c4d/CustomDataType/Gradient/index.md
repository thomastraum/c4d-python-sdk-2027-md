<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/Gradient/index.html -->

# c4d.Gradient <a id="c4d-gradient"></a>

## *class* `c4d.Gradient` <a id="c4d.Gradient"></a>

Gradient data type (*CUSTOMDATATYPE_GRADIENT*) for the [`GradientCustomGui`](../../../c4d.gui/BaseCustomGui/GradientCustomGui/index.md#c4d.gui.GradientCustomGui) GUI.

This type is called by value.

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Alpha Processing**

- [`Gradient.AllocAlphaGradient()`](#c4d.Gradient.AllocAlphaGradient): Create a alpha of the gradient.
- [`Gradient.ConvertToAlphaGradient()`](#c4d.Gradient.ConvertToAlphaGradient): Converts this gradient to an alpha gradient.
- [`Gradient.GetAlphaGradient()`](#c4d.Gradient.GetAlphaGradient): Gets a copy of the alpha gradient.
- [`Gradient.SetAlphaGradient()`](#c4d.Gradient.SetAlphaGradient): Sets the alpha gradient.

**Container Access**

- [`Gradient.GetData()`](#c4d.Gradient.GetData): Gets a data item from the gradient container.
- [`Gradient.SetData()`](#c4d.Gradient.SetData): Sets a data item from the gradient container.

**Knot Editing**

- [`Gradient.DistributeKnots()`](#c4d.Gradient.DistributeKnots): Distributes the knots evenly.
- [`Gradient.DoubleKnots()`](#c4d.Gradient.DoubleKnots): Doubles the knots.
- [`Gradient.FlushKnots()`](#c4d.Gradient.FlushKnots): Flushes all knots.
- [`Gradient.GetKnot()`](#c4d.Gradient.GetKnot): Returns the information about a knot.
- [`Gradient.GetKnotCount()`](#c4d.Gradient.GetKnotCount): Gets the knot count.
- [`Gradient.InsertKnot()`](#c4d.Gradient.InsertKnot): Insert a knot.
- [`Gradient.InvertKnots()`](#c4d.Gradient.InvertKnots): Inverts the knots.
- [`Gradient.RemoveKnot()`](#c4d.Gradient.RemoveKnot): Delete a knot.
- [`Gradient.SetKnot()`](#c4d.Gradient.SetKnot): Set the values of a knot.

**Magic Methods**

- [`Gradient.__hash__()`](#c4d.Gradient.__hash__): Returns a hash of the whole gradient state, including the needles, colors and interpolation type.
- [`Gradient.__init__()`](#c4d.Gradient.__init__)

**Render Preparation**

- [`Gradient.PrepareRenderData()`](#c4d.Gradient.PrepareRenderData): Initializes the gradient data for render.
- [`Gradient.PrepareRenderDataWithAlpha()`](#c4d.Gradient.PrepareRenderDataWithAlpha): Initializes the gradient data for render.

**Representation Access**

- [`Gradient.GetGradient()`](#c4d.Gradient.GetGradient): Gets the internal gradient.
- [`Gradient.SetGradient()`](#c4d.Gradient.SetGradient): Sets the internal gradient.

**State Transfer And Validation**

- [`Gradient.CopyFrom()`](#c4d.Gradient.CopyFrom): Copies all gradient data from the source gradient.
- [`Gradient.GetChecksum()`](#c4d.Gradient.GetChecksum): Gets a checksum of the whole gradient state, including the knots, colors and interpolation type.

## Members <a id="members"></a>

### Alpha Processing <a id="c4d.Gradient-method-Alpha-Processing"></a>

#### `Gradient.AllocAlphaGradient(self)` <a id="c4d.Gradient.AllocAlphaGradient"></a>

Create a alpha of the gradient. Similar to `Gradient.GetAlphaGradient()`.

> **Note:**
>
> It is a copy of the original gradient.  
> Can be changed, but has no effect to the original alpha-gradient.

**Return type:** [c4d.Gradient](#c4d.Gradient)

**Returns:** Alpha gradient.

#### `Gradient.ConvertToAlphaGradient(self, bc=None, id=0)` <a id="c4d.Gradient.ConvertToAlphaGradient"></a>

Converts this gradient to an alpha gradient.

**Parameters:**

- **bc** (*Optional*[[*c4d.BaseContainer*](../../BaseContainer/index.md#c4d.BaseContainer)]) – The container holding the gradient.
- **id** (*Optional*[*int*]) – The ID of the gradient within the container.

**Return type:** int

**Returns:** Knot count.

#### `Gradient.GetAlphaGradient(self)` <a id="c4d.Gradient.GetAlphaGradient"></a>

Gets a copy of the alpha gradient.

> **Note:**
>
> It is just a copy of the original gradient.  
> Can be changed, but has no effect to the original alpha-gradient.  
> Use `Gradient.SetAlphaGradient()` to set the alpha-gradient.

**Return type:** [c4d.Gradient](#c4d.Gradient)

**Returns:** Alpha gradient.

#### `Gradient.SetAlphaGradient(self, alphaGradient)` <a id="c4d.Gradient.SetAlphaGradient"></a>

Sets the alpha gradient.

**Parameters:** **alphaGradient** ([*c4d.Gradient*](#c4d.Gradient)) – Alpha gradient.

### Container Access <a id="c4d.Gradient-method-Container-Access"></a>

#### `Gradient.GetData(self, id)` <a id="c4d.Gradient.GetData"></a>

Gets a data item from the gradient container.

**Parameters:**

**id** (*int*) –

Data ID:

|   |   |   |   |
|---|---|---|---|
| *GRADIENT_KNOT* | [`BaseContainer`](../../BaseContainer/index.md#c4d.BaseContainer) | Holds the knots as sub-containers: |  |
|  | *GRADIENTKNOT_COLOR* | [`Vector`](../../Vector/index.md#c4d.Vector) | Color. |
|  | *GRADIENTKNOT_BRIGHTNESS* | float | Brightness. |
|  | *GRADIENTKNOT_POSITION* | float | Position. |
|  | *GRADIENTKNOT_BIAS* | float | Bias. |
|  | *GRADIENTKNOT_ID* | int | Index. |
|  | *GRADIENTKNOT_INTERPOLATION* | int |  |
|  |  | *GRADIENT_INTERPOLATION_CUBICKNOT* | Cubic knot. |
|  |  | *GRADIENT_INTERPOLATION_SMOOTHKNOT* | Smooth knot. |
|  |  | *GRADIENT_INTERPOLATION_LINEARKNOT* | Linear knot. |
|  |  | *GRADIENT_INTERPOLATION_NONE* | None. |
|  |  | *GRADIENT_INTERPOLATION_EXP_UP* | Exponential up. |
|  |  | *GRADIENT_INTERPOLATION_EXP_DOWN* | Exponential down. |
|  |  | *GRADIENT_INTERPOLATION_BLEND* | *New in version R20:* Blend. |
| *GRADIENT_MODE* | int | Mode: |  |
|  | *GRADIENTMODE_COLOR* | Color only. |  |
|  | *GRADIENTMODE_ALPHA* | Alpha only. |  |
|  | *GRADIENTMODE_COLORALPHA* | Color and alpha. |  |
| *GRADIENT_UNCLAMPED* | bool | Unclamped |  |

**Return type:** object

**Returns:** The data.

#### `Gradient.SetData(self, id, data)` <a id="c4d.Gradient.SetData"></a>

Sets a data item from the gradient container.

**Parameters:**

- **id** (*int*) –

  Data ID:

  |   |   |   |   |
  |---|---|---|---|
  | *GRADIENT_KNOT* | [`BaseContainer`](../../BaseContainer/index.md#c4d.BaseContainer) | Holds the knots as sub-containers: |  |
  |  | *GRADIENTKNOT_COLOR* | [`Vector`](../../Vector/index.md#c4d.Vector) | Color. |
  |  | *GRADIENTKNOT_BRIGHTNESS* | float | Brightness. |
  |  | *GRADIENTKNOT_POSITION* | float | Position. |
  |  | *GRADIENTKNOT_BIAS* | float | Bias. |
  |  | *GRADIENTKNOT_ID* | int | Index. |
  |  | *GRADIENTKNOT_INTERPOLATION* | int |  |
  |  |  | *GRADIENT_INTERPOLATION_CUBICKNOT* | Cubic knot. |
  |  |  | *GRADIENT_INTERPOLATION_SMOOTHKNOT* | Smooth knot. |
  |  |  | *GRADIENT_INTERPOLATION_LINEARKNOT* | Linear knot. |
  |  |  | *GRADIENT_INTERPOLATION_NONE* | None. |
  |  |  | *GRADIENT_INTERPOLATION_EXP_UP* | Exponential up. |
  |  |  | *GRADIENT_INTERPOLATION_EXP_DOWN* | Exponential down. |
  |  |  | *GRADIENT_INTERPOLATION_BLEND* | *New in version R20:* Blend. |
  | *GRADIENT_MODE* | int | Mode: |  |
  |  | *GRADIENTMODE_COLOR* | Color only. |  |
  |  | *GRADIENTMODE_ALPHA* | Alpha only. |  |
  |  | *GRADIENTMODE_COLORALPHA* | Color and alpha. |  |
  | *GRADIENT_UNCLAMPED* | bool | Unclamped |  |

- **data** (*object*) – The data.

### Knot Editing <a id="c4d.Gradient-method-Knot-Editing"></a>

#### `Gradient.DistributeKnots(self)` <a id="c4d.Gradient.DistributeKnots"></a>

Distributes the knots evenly.

*New in version R20.*

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `Gradient.DoubleKnots(self)` <a id="c4d.Gradient.DoubleKnots"></a>

Doubles the knots.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `Gradient.FlushKnots(self)` <a id="c4d.Gradient.FlushKnots"></a>

Flushes all knots.

#### `Gradient.GetKnot(self, index)` <a id="c4d.Gradient.GetKnot"></a>

Returns the information about a knot.

**Parameters:**

**index** (*int*) –

The index.

> **Note:** The new knot index has to be 0 <= index < `Gradient.GetKnotCount()`

Check out this small example.

```python
col, brightness, pos, bias, index = gradient.GetKnot(index)
```

**Return type:** Dict[int, [c4d.Vector](../../Vector/index.md#c4d.Vector), float, float, float]

**Returns:** A dictionary with the knot information.

#### `Gradient.GetKnotCount(self)` <a id="c4d.Gradient.GetKnotCount"></a>

Gets the knot count.

**Return type:** int

**Returns:** Knot count.

#### `Gradient.InsertKnot(self, col, brightness, pos, bias, index)` <a id="c4d.Gradient.InsertKnot"></a>

Insert a knot. Not passed arguments will be set with default values.

**Parameters:**

- **col** ([*c4d.Vector*](../../Vector/index.md#c4d.Vector)) – The color.
- **brightness** (*float*) – The brightness.
- **pos** (*float*) – The position.
- **bias** (*float*) – The bias.
- **index** (*int*) – The index.

**Return type:** int

**Returns:**

The new knot

> **Note:** The new knot index is [`GetKnotCount()`](#c4d.Gradient.GetKnotCount) - 1

#### `Gradient.InvertKnots(self)` <a id="c4d.Gradient.InvertKnots"></a>

Inverts the knots.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `Gradient.RemoveKnot(self, index)` <a id="c4d.Gradient.RemoveKnot"></a>

Delete a knot.

**Parameters:**

**index** (*int*) –

index knot.

> **Note:** 0 <= index < [`GetKnotCount()`](#c4d.Gradient.GetKnotCount)

#### `Gradient.SetKnot(self, index, col, brightness, pos, bias)` <a id="c4d.Gradient.SetKnot"></a>

Set the values of a knot.

> **Note:** Just the passed arguments will be set, the other will be discarded.

**Parameters:**

- **index** (*int*) –

  The knot index.

  > **Note:** The new knot index has to be 0 <= index < `Gradient.GetKnotCount()`

- **col** ([*c4d.Vector*](../../Vector/index.md#c4d.Vector)) – The color.

- **brightness** (*float*) – The brightness.

- **pos** (*float*) – The position.

- **bias** (*float*) – The bias.

### Magic Methods <a id="c4d.Gradient-method-Magic-Methods"></a>

#### `Gradient.__hash__(self)` <a id="c4d.Gradient.__hash__"></a>

Returns a hash of the whole gradient state, including the needles, colors and interpolation type.

```python
print(hash(obj) #hash calls obj.__hash__())
```

**Return type:** int

**Returns:** Hash value

#### `Gradient.__init__(self, v)` <a id="c4d.Gradient.__init__"></a>

**Parameters:** **v** ([*c4d.Gradient*](#c4d.Gradient)) – Copy constructor.

### Render Preparation <a id="c4d.Gradient-method-Render-Preparation"></a>

#### `Gradient.PrepareRenderData(self, irs)` <a id="c4d.Gradient.PrepareRenderData"></a>

Initializes the gradient data for render.

*New in version 2024.0.0.*

> **Note:** Call before `CalcGradientPixel()`.

**Parameters:** **irs** ([*c4d.modules.render.InitRenderStruct*](../../../c4d.modules/render/InitRenderStruct/index.md#c4d.modules.render.InitRenderStruct)) – Information about the upcoming rendering.

**Return type:** [`maxon.GradientRenderData`](../../../maxon_generated/interfaces/misc/maxon.GradientRenderData.md#module-maxon.GradientRenderData)

**Returns:** RenderData on success.

#### `Gradient.PrepareRenderDataWithAlpha(self, irs)` <a id="c4d.Gradient.PrepareRenderDataWithAlpha"></a>

Initializes the gradient data for render.

*New in version 2024.0.0.*

> **Note:** Call before `CalcGradientPixel()`.

**Parameters:** **irs** ([*c4d.modules.render.InitRenderStruct*](../../../c4d.modules/render/InitRenderStruct/index.md#c4d.modules.render.InitRenderStruct)) – Information about the upcoming rendering.

**Return type:** tuple[[`maxon.GradientRenderData`](../../../maxon_generated/interfaces/misc/maxon.GradientRenderData.md#module-maxon.GradientRenderData), [`maxon.GradientRenderData`](../../../maxon_generated/interfaces/misc/maxon.GradientRenderData.md#module-maxon.GradientRenderData)]

**Returns:** RenderData for the colors and the Alpha on success.

### Representation Access <a id="c4d.Gradient-method-Representation-Access"></a>

#### `Gradient.GetGradient(self)` <a id="c4d.Gradient.GetGradient"></a>

Gets the internal gradient.

*New in version 2024.0.0.*

**Returns:** The internal gradient.

**Return type:** [`maxon.Gradient`](../../../maxon_generated/interfaces/misc/maxon.Gradient.md#module-maxon.Gradient)

#### `Gradient.SetGradient(self, gradient)` <a id="c4d.Gradient.SetGradient"></a>

Sets the internal gradient.

*New in version 2024.0.0.*

**Parameters:** **gradient** ([`maxon.Gradient`](../../../maxon_generated/interfaces/misc/maxon.Gradient.md#module-maxon.Gradient)) – The internal gradient to set.

### State Transfer And Validation <a id="c4d.Gradient-method-State-Transfer-And-Validation"></a>

#### `Gradient.CopyFrom(self, src)` <a id="c4d.Gradient.CopyFrom"></a>

Copies all gradient data from the source gradient.

*New in version 2024.0.0.*

**Parameters:** **src** ([*c4d.Gradient*](#c4d.Gradient)) – The source gradient.

**Returns:** True if the copy succeeded otherwise False.

**Return type:** bool

#### `Gradient.GetChecksum(self)` <a id="c4d.Gradient.GetChecksum"></a>

Gets a checksum of the whole gradient state, including the knots, colors and interpolation type.

*New in version 2024.0.0.*

**Returns:** The checksum.

**Return type:** int
