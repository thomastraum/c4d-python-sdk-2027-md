<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.html -->

# c4d.BaseMaterial <a id="c4d-basematerial"></a>

## *class* `c4d.BaseMaterial` <a id="c4d.BaseMaterial"></a>

This is the material base class that all materials in Cinema 4D are derived from.

Parent Class:

- [`c4d.BaseList2D`](../index.md#c4d.BaseList2D)

Children Classes:

- [`c4d.Material`](Material/index.md#c4d.Material)
- [`c4d.NodeMaterial`](NodeMaterial/index.md#c4d.NodeMaterial)

## Overview <a id="overview"></a>

**Magic Methods**

- [`BaseMaterial.__init__()`](#c4d.BaseMaterial.__init__): Initialize a new [`BaseMaterial`](#c4d.BaseMaterial) in memory.

**Material Inspection**

- [`BaseMaterial.Compare()`](#c4d.BaseMaterial.Compare): Check if the materials are identical.
- [`BaseMaterial.GetNodeMaterialReference()`](#c4d.BaseMaterial.GetNodeMaterialReference): Returns a weak reference of the actual Material as a [`c4d.NodeMaterial`](NodeMaterial/index.md#c4d.NodeMaterial).
- [`BaseMaterial.GetRenderInfo()`](#c4d.BaseMaterial.GetRenderInfo): Retrieves information about what the material requires from the raytracer and what it will return.

**Preview Management**

- [`BaseMaterial.GetAverageColor()`](#c4d.BaseMaterial.GetAverageColor): Returns an average color for the material, based on the material preview.
- [`BaseMaterial.GetPreview()`](#c4d.BaseMaterial.GetPreview): Retrieves the preview picture of the material.
- [`BaseMaterial.Update()`](#c4d.BaseMaterial.Update): Recalculates the material’s thumbnail and updates internal values.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.BaseMaterial-method-Magic-Methods"></a>

#### `BaseMaterial.__init__(self, type)` <a id="c4d.BaseMaterial.__init__"></a>

Initialize a new [`BaseMaterial`](#c4d.BaseMaterial) in memory.

**Parameters:** **type** (*int*) – The material type : [Material Types](../../../../../../types/materials.md).

### Material Inspection <a id="c4d.BaseMaterial-method-Material-Inspection"></a>

#### `BaseMaterial.Compare(self, snd)` <a id="c4d.BaseMaterial.Compare"></a>

Check if the materials are identical.

> **Note:** Only the name of the compared materials can be different.

**Parameters:** **snd** ([*c4d.BaseMaterial*](#c4d.BaseMaterial)) – The material to compare with.

**Return type:** bool

**Returns:** **True** if the materials contents are the same, otherwise **False**.

#### `BaseMaterial.GetNodeMaterialReference(self)` <a id="c4d.BaseMaterial.GetNodeMaterialReference"></a>

Returns a weak reference of the actual Material as a [`c4d.NodeMaterial`](NodeMaterial/index.md#c4d.NodeMaterial).

**Returns:** The material as a [`c4d.NodeMaterial`](NodeMaterial/index.md#c4d.NodeMaterial).

**Return type:** [c4d.NodeMaterial](NodeMaterial/index.md#c4d.NodeMaterial)

#### `BaseMaterial.GetRenderInfo(self)` <a id="c4d.BaseMaterial.GetRenderInfo"></a>

Retrieves information about what the material requires from the raytracer and what it will return.

**Return type:** int

**Returns:**

The return values are:

|   |   |
|---|---|
| *VOLUMEINFO_NONE* | None. |
| *VOLUMEINFO_REFLECTION* | Calculates reflections. |
| *VOLUMEINFO_TRANSPARENCY* | Calculates transparency. |
| *VOLUMEINFO_ALPHA* | Calculates alpha. |
| *VOLUMEINFO_CHANGENORMAL* | Calculates bump mapping. |
| *VOLUMEINFO_DISPLACEMENT* | Calculates displacement mapping. |
| *VOLUMEINFO_ENVREQUIRED* | Needs environment reflection data. |
| *VOLUMEINFO_DUDVREQUIRED* | Needs du/dv bump mapping data. |
| *VOLUMEINFO_MIPSAT* | Requires MIP/SAT data. |
| *VOLUMEINFO_VOLUMETRIC* | Is volumetric. |
| *VOLUMEINFO_TRANSFORM* | Needs back-transformed data. |
| *VOLUMEINFO_EVALUATEPROJECTION* | Requires texture tag projections. |
| *VOLUMEINFO_PRIVATE_GLOW* | Calculates glow. Private. |
| *VOLUMEINFO_INITCALCULATION* | Needs *InitCalculation()* call. |
| *VOLUMEINFO_FINAL_ALPHA* | *New in version R18:* Writes final alpha value. |

### Preview Management <a id="c4d.BaseMaterial-method-Preview-Management"></a>

#### `BaseMaterial.GetAverageColor(self, channel=-1)` <a id="c4d.BaseMaterial.GetAverageColor"></a>

Returns an average color for the material, based on the material preview.

**Parameters:**

**channel** (*int*) –

An optional specific channel to get the average for.

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

**Return type:** [c4d.Vector](../../../../Vector/index.md#c4d.Vector)

**Returns:** Average color.

#### `BaseMaterial.GetPreview(self, flags=0)` <a id="c4d.BaseMaterial.GetPreview"></a>

Retrieves the preview picture of the material.

**Parameters:** **flags** (*int*) – Currently not used.

**Return type:** Optional[[c4d.bitmaps.BaseBitmap](../../../../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]

**Returns:** The preview picture or **None** if it has not been calculated.

#### `BaseMaterial.Update(self, preview, rttm)` <a id="c4d.BaseMaterial.Update"></a>

Recalculates the material’s thumbnail and updates internal values.

> **Note:**
>
> Recalculating the thumbnail/RTTM image is time intensive.  
> It only needs to be done if you want to let the user view the change.  
> The calculations are done asynchronously.

**Parameters:**

- **preview** (*bool*) – If this value is **True** then the preview thumbnail is updated.
- **rttm** (*bool*) – If this value is **True** then the real time texture map of the material will be recalculated.
