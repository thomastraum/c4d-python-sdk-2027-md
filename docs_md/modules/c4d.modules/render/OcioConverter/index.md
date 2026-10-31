<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/render/OcioConverter/index.html -->

# c4d.modules.render.OcioConverter <a id="c4d-modules-render-ocioconverter"></a>

## *class* `c4d.modules.render.OcioConverter` <a id="c4d.modules.render.OcioConverter"></a>

Transforms colors from one OCIO color space to another.

*New in version 2025.2.0.*

## Overview <a id="overview"></a>

**Color Conversion**

- [`OcioConverter.IsOcioConverter()`](#c4d.modules.render.OcioConverter.IsOcioConverter): Checks if the converter is an OCIO converter.
- [`OcioConverter.TransformColor()`](#c4d.modules.render.OcioConverter.TransformColor): Transforms a color.
- [`OcioConverter.TransformColors()`](#c4d.modules.render.OcioConverter.TransformColors): Transforms multiple colors.

**Magic Methods**

- [`OcioConverter.__init__()`](#c4d.modules.render.OcioConverter.__init__): Creates a new converter and Initializes it with the document settings.

## Members <a id="members"></a>

### Color Conversion <a id="c4d.modules.render.OcioConverter-method-Color-Conversion"></a>

#### `OcioConverter.IsOcioConverter(self)` <a id="c4d.modules.render.OcioConverter.IsOcioConverter"></a>

Checks if the converter is an OCIO converter.

**Returns:** True if the converter is an OCIO converter, False if the converter is a legacy converter.

**Return type:** bool

#### `OcioConverter.TransformColor(self, v, colorSpaceTransformation)` <a id="c4d.modules.render.OcioConverter.TransformColor"></a>

Transforms a color.

**Parameters:**

- **v** (Union[c4d.Vector, [`maxon.Vector`](../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector)]) – Input color.

- **colorSpaceTransformation** (*int.*) –

  The values are:

  | Symbol ID | Description |
  |---|---|
  | NONE | None. |
  | COLORSPACETRANSFORMATION_LINEAR_TO_SRGB | Linear to sRGB color space transformation. |
  | COLORSPACETRANSFORMATION_SRGB_TO_LINEAR | sRGB to linear color space transformation. |
  | COLORSPACETRANSFORMATION_LINEAR_TO_VIEW | Linear to display color space transformation. |
  | COLORSPACETRANSFORMATION_SRGB_TO_VIEW | sRGB to display color space transformation. |

**Returns:** The transformed color.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

#### `OcioConverter.TransformColors(self, v, colorSpaceTransformation)` <a id="c4d.modules.render.OcioConverter.TransformColors"></a>

Transforms multiple colors.

**Parameters:**

- **v** (Iterator[Union[c4d.Vector, [`maxon.Vector`](../../../maxon_generated/datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector)]]) – Input color.

- **colorSpaceTransformation** (*int.*) –

  The values are:

  | Symbol ID | Description |
  |---|---|
  | NONE | None. |
  | COLORSPACETRANSFORMATION_LINEAR_TO_SRGB | Linear to sRGB color space transformation. |
  | COLORSPACETRANSFORMATION_SRGB_TO_LINEAR | sRGB to linear color space transformation. |
  | COLORSPACETRANSFORMATION_LINEAR_TO_VIEW | Linear to display color space transformation. |
  | COLORSPACETRANSFORMATION_SRGB_TO_VIEW | sRGB to display color space transformation. |

**Returns:** The transformed colors.

**Return type:** list[[c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)]

### Magic Methods <a id="c4d.modules.render.OcioConverter-method-Magic-Methods"></a>

#### `OcioConverter.__init__(self, doc, overrideViewTransform=-1)` <a id="c4d.modules.render.OcioConverter.__init__"></a>

Creates a new converter and Initializes it with the document settings.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The optional document to initialize with.
- **overrideViewTransform** (*int*) – Index within the viewtransform array to override the view transform. Ignored, if the value is not a valid index.
