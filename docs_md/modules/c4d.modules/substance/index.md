<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/substance/index.html -->

# c4d.modules.substance <a id="c4d-modules-substance"></a>

## *class* `c4d.modules.substance` <a id="c4d.modules.substance"></a>

*New in version R18.020.*

## Overview <a id="overview"></a>

**Asset Management**

- [`c4d.modules.substance.GetFirstSubstance()`](#c4d.modules.substance.GetFirstSubstance): Retrieves the first Substance asset in *doc*.
- [`c4d.modules.substance.GetSubstances()`](#c4d.modules.substance.GetSubstances): Retrieves all (or only selected) Substance assets in *doc*.
- [`c4d.modules.substance.ImportSubstance()`](#c4d.modules.substance.ImportSubstance): Imports a Substance asset file (.sbsar) into *doc*.
- [`c4d.modules.substance.InsertLastSubstance()`](#c4d.modules.substance.InsertLastSubstance): Inserts *asset* into *doc* as last element.

**Graph And Channel Data**

- [`c4d.modules.substance.GetSubstanceGraph()`](#c4d.modules.substance.GetSubstanceGraph): Retrieves the Substance graph.
- [`c4d.modules.substance.GetSubstanceInput()`](#c4d.modules.substance.GetSubstanceInput): Retrieves the Substance input of an asset.
- [`c4d.modules.substance.GetSubstanceMosaicPreview()`](#c4d.modules.substance.GetSubstanceMosaicPreview): Returns an image with previews of the output channels of *asset*.
- [`c4d.modules.substance.GetSubstanceOutput()`](#c4d.modules.substance.GetSubstanceOutput): Retrieves the Substance output of an asset.

**Material And Shader Setup**

- [`c4d.modules.substance.AssignChannelToMaterial()`](#c4d.modules.substance.AssignChannelToMaterial)
- [`c4d.modules.substance.CreateMaterial()`](#c4d.modules.substance.CreateMaterial): Creates a Cinema 4D standard material from *asset*.
- [`c4d.modules.substance.CreateSubstanceShader()`](#c4d.modules.substance.CreateSubstanceShader): Creates a Substance shader linked to *asset*.
- [`c4d.modules.substance.MaterialUsesSubstance()`](#c4d.modules.substance.MaterialUsesSubstance): Checks if *mat* contains any Substance shaders.

**Preferences**

- [`c4d.modules.substance.PrefsGetMaterialModeSetting()`](#c4d.modules.substance.PrefsGetMaterialModeSetting): Convenience function to get the material creation mode set in Substance preferences.
- [`c4d.modules.substance.PrefsGetPreviewSetting()`](#c4d.modules.substance.PrefsGetPreviewSetting): Convenience function to get the preview mode for Content Browser set in Substance preferences.

## Members <a id="members"></a>

### Asset Management <a id="c4d.modules.substance-function-Asset-Management"></a>

#### `c4d.modules.substance.GetFirstSubstance(doc)` <a id="c4d.modules.substance.GetFirstSubstance"></a>

Retrieves the first Substance asset in *doc*.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

**Return type:** Optional[[c4d.BaseList2D](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The first Substance asset, or **None** if none exists.

#### `c4d.modules.substance.GetSubstances(doc, onlySelected)` <a id="c4d.modules.substance.GetSubstances"></a>

Retrieves all (or only selected) Substance assets in *doc*.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.
- **onlySelected** (*bool*) – Set to **True** to get only selected Substance assets.

**Return type:** List[[c4d.C4DAtom](../../c4d/C4DAtom/index.md#c4d.C4DAtom)]

**Returns:** The retrieved Substance assets.

#### `c4d.modules.substance.ImportSubstance(doc, fn, copyFile, errPopup, addUndo, createMaterial)` <a id="c4d.modules.substance.ImportSubstance"></a>

Imports a Substance asset file (.sbsar) into *doc*.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to import into.

- **fn** (*str*) – The Substance asset file.

- **copyFile** (*int*) –

  The copy file flag:

  |   |   |
  |---|---|
  | *SUBSTANCE_IMPORT_COPY_YES* | Automatically copy file to project directory (relative file path). |
  | *SUBSTANCE_IMPORT_COPY_NO* | Do not copy file to project directory (absolute file path). |
  | *SUBSTANCE_IMPORT_COPY_ASK* | Ask user. |

  If set to *ASK*, user’s choice will be returned.  
  Note: When set to *ASK*, the function obviously has to be called in a context where user interaction is allowed.

- **errPopup** (*bool*) –

  If set to **True**, problems will be communicated to the user with a message requester.  
  Note: When set to **True**, the function obviously has to be called in a context where user interaction is allowed.

- **addUndo** (*bool*) – If set to **True**, an undo step will be added for the import. Caller has to care for the surrounding `BaseDocument.StartUndo()` and `BaseDocument.EndUndo()` calls.

- **createMaterial** (*bool*) – Set to **True**, to have a material created based on the configuration in preferences. Set to **False**, to suppress any creation of materials.

**Return type:** Tuple[int, [c4d.BaseList2D](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D), int]

**Returns:**

A tuple with the following information:

int: The result for the import:

|   |   |
|---|---|
| *SUBSTANCE_IMPORT_RESULT_SUCCESS* | Success. |
| *SUBSTANCE_IMPORT_RESULT_DOESNOTEXIST* | File not found. |
| *SUBSTANCE_IMPORT_RESULT_NOTANASSET* | Wrong file format. |
| *SUBSTANCE_IMPORT_RESULT_UNKNOWNERROR* | On memory error or when invalid parameters were passed. |

[`c4d.BaseList2D`](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D): The imported Substance asset.  
int: User’s choice if *copyFile* was *ASK*. Otherwise same as passed to *copyFile*.

#### `c4d.modules.substance.InsertLastSubstance(doc, asset)` <a id="c4d.modules.substance.InsertLastSubstance"></a>

Inserts *asset* into *doc* as last element.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.
- **asset** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The Substance asset.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Graph And Channel Data <a id="c4d.modules.substance-function-Graph-And-Channel-Data"></a>

#### `c4d.modules.substance.GetSubstanceGraph(asset, prevGraph=None)` <a id="c4d.modules.substance.GetSubstanceGraph"></a>

Retrieves the Substance graph. This function may be used to iterate over the graphs of *asset*.

**Parameters:**

- **asset** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The Substance asset.
- **prevGraph** (*Optional*[*PyCObject*]) – Pass **None** (default) to get the first graph, pass a graph object to get the following graph.

**Return type:** Tuple[PyCObject, str]

**Returns:** The Substance graph and its name.

#### `c4d.modules.substance.GetSubstanceInput(asset, graph, prevInput=None)` <a id="c4d.modules.substance.GetSubstanceInput"></a>

Retrieves the Substance input of an asset. This function may be used to iterate over the inputs of *graph* for *asset*.

**Parameters:**

- **asset** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The Substance asset.
- **graph** (*PyCObject*) – The graph.
- **prevInput** (*Optional*[*PyCObject*]) – Pass **None** (default) to get the first input, pass an input object to get the following input.

**Return type:** Tuple[Optional[PyCObject], int, int, int, int, str]

**Returns:**

A tuple with the following information:

The Substance input, or **None** if input is not available.  
The unique ID of the input. Only valid if the function does not return **None**.  
The ID of the first component of the input parameter in Cinema 4D. This ID can be used to create a [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID) for `C4DAtom.SetParameter()`. Only valid if the function does not return **None**.  
The number of description elements used in Cinema 4D to represent the Substance input parameter. Only valid if the function does not return **None**.  
The data type of the input. Only valid if the function does not return **None**.

|   |   |
|---|---|
| *SUBSTANCE_INPUT_TYPE_INTEGER* | int Integer, one [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID). |
| *SUBSTANCE_INPUT_TYPE_INTEGER_2* | int Two component integer vector, two [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID). |
| *SUBSTANCE_INPUT_TYPE_INTEGER_3* | int Three component integer vector, three [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID). |
| *SUBSTANCE_INPUT_TYPE_INTEGER_4* | int Four component integer vector, four [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID). |
| *SUBSTANCE_INPUT_TYPE_BOOL* | bool Boolean, one [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID). |
| *SUBSTANCE_INPUT_TYPE_FLOAT* | float Float, one [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID). |
| *SUBSTANCE_INPUT_TYPE_FLOAT_2* | float Two component float vector, two [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID). |
| *SUBSTANCE_INPUT_TYPE_FLOAT_3* | float Three component float vector, three [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID). |
| *SUBSTANCE_INPUT_TYPE_FLOAT_4* | float Four component float vector, four [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID). |
| *SUBSTANCE_INPUT_TYPE_IMAGE* | str Image input, one [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID). |
| *SUBSTANCE_INPUT_TYPE_STRING* | str String, one [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID). |
| *SUBSTANCE_INPUT_TYPE_COLOR_RGB* | [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector) RGB color vector, one [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID). |
| *SUBSTANCE_INPUT_TYPE_COLOR_RGBA* | [`c4d.Vector`](../../c4d/Vector/index.md#c4d.Vector) and float RGBA color vector, two [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID). |
| *SUBSTANCE_INPUT_TYPE_RESOLUTION* | int Substance output resolution, two [`c4d.DescID`](../../c4d/DescID/index.md#c4d.DescID), integer, range *4* to *11*, *2^n* pixels (*16* pixels to *2048* pixels). |

Name of the returned input. Only valid if the function does not return **None** as Substance input.

#### `c4d.modules.substance.GetSubstanceMosaicPreview(asset, w, h)` <a id="c4d.modules.substance.GetSubstanceMosaicPreview"></a>

Returns an image with previews of the output channels of *asset*.

> **Note:** While the Substance asset won’t have to be re-rendered, this operation still involves downscaling of all Substance outputs.

**Parameters:**

- **asset** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The Substance asset.
- **w** (*int*) – The width of the preview image.
- **h** (*int*) – The height of the preview image.

**Return type:** [`c4d.bitmaps.BaseBitmap`](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)

**Returns:** The resulting preview bitmap.

#### `c4d.modules.substance.GetSubstanceOutput(asset, graph, getBitmap, prevOutput=None)` <a id="c4d.modules.substance.GetSubstanceOutput"></a>

Retrieves the Substance output of an asset. This function may be used to iterate over the outputs of *graph* for *asset*.

**Parameters:**

- **asset** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The Substance asset.
- **graph** (*PyCObject*) – The graph.
- **getBitmap** (*bool*) – Set to **True**, to get a clone of the output channel bitmap.
- **prevOutput** (*Optional*[*PyCObject*]) – Pass **None** (default) to get the first output, pass an output object to get the following output.

**Return type:** Tuple[Optional[PyCObject], int, int, str, [c4d.bitmaps.BaseBitmap](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]

**Returns:**

A tuple with the following information:

The Substance output, or **None** if output is not available.  
The unique ID of the output. Only valid if the function does not return **None**.  
The output type ID. Only valid if the function does not return **None** as Substance output.

> |   |   |
> |---|---|
> | *SUBSTANCE_OUTPUT_TYPE_DIFFUSE* |  |
> | *SUBSTANCE_OUTPUT_TYPE_BASECOLOR* |  |
> | *SUBSTANCE_OUTPUT_TYPE_OPACITY* |  |
> | *SUBSTANCE_OUTPUT_TYPE_EMISSIVE* |  |
> | *SUBSTANCE_OUTPUT_TYPE_AMBIENT* |  |
> | *SUBSTANCE_OUTPUT_TYPE_AMBIENTOCCLUSION* |  |
> | *SUBSTANCE_OUTPUT_TYPE_MASK* |  |
> | *SUBSTANCE_OUTPUT_TYPE_NORMAL* |  |
> | *SUBSTANCE_OUTPUT_TYPE_BUMP* |  |
> | *SUBSTANCE_OUTPUT_TYPE_HEIGHT* |  |
> | *SUBSTANCE_OUTPUT_TYPE_DISPLACEMENT* |  |
> | *SUBSTANCE_OUTPUT_TYPE_SPECULAR* |  |
> | *SUBSTANCE_OUTPUT_TYPE_SPECULARLEVEL* |  |
> | *SUBSTANCE_OUTPUT_TYPE_SPECULARCOLOR* |  |
> | *SUBSTANCE_OUTPUT_TYPE_GLOSSINESS* |  |
> | *SUBSTANCE_OUTPUT_TYPE_ROUGHNESS* |  |
> | *SUBSTANCE_OUTPUT_TYPE_ANISOTROPYLEVEL* |  |
> | *SUBSTANCE_OUTPUT_TYPE_ANISOTROPYANGLE* |  |
> | *SUBSTANCE_OUTPUT_TYPE_TRANSMISSIVE* |  |
> | *SUBSTANCE_OUTPUT_TYPE_REFLECTION* |  |
> | *SUBSTANCE_OUTPUT_TYPE_REFRACTION* |  |
> | *SUBSTANCE_OUTPUT_TYPE_ENVIRONMENT* |  |
> | *SUBSTANCE_OUTPUT_TYPE_IOR* |  |
> | *SUBSTANCE_OUTPUT_TYPE_SCATTERING0* |  |
> | *SUBSTANCE_OUTPUT_TYPE_SCATTERING1* |  |
> | *SUBSTANCE_OUTPUT_TYPE_SCATTERING2* |  |
> | *SUBSTANCE_OUTPUT_TYPE_SCATTERING3* |  |
> | *SUBSTANCE_OUTPUT_TYPE_METALLIC* |  |
> | *SUBSTANCE_OUTPUT_TYPE_ANY* |  |
> | *SUBSTANCE_OUTPUT_TYPE_UNKNOWN* |  |
> | *SUBSTANCE_OUTPUT_TYPE_INTERNAL_COUNT* |  |

The name of the returned output. Only valid if the function does not return **None**.  
The clone of the output channel bitmap. Only valid if the function does not return **None** and *getBitmap* was passed **True**.

### Material And Shader Setup <a id="c4d.modules.substance-function-Material-And-Shader-Setup"></a>

#### `c4d.modules.substance.AssignChannelToMaterial(asset, mat, channelId, outputUid, addUndo)` <a id="c4d.modules.substance.AssignChannelToMaterial"></a>

**Parameters:**

- **asset** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The Substance asset. Needs to be part of the document.

- **mat** ([*c4d.Material*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/Material/index.md#c4d.Material)) – The material.

- **channelId** (*int*) –

  The channel ID:

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

- **outputUid** (*int*) – The unique ID of the Substance output to use.

- **addUndo** (*bool*) – If set to **True**, an undo step will be added for the import. Caller has to care for the surrounding `BaseDocument.StartUndo()` and `BaseDocument.EndUndo()` calls.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `c4d.modules.substance.CreateMaterial(asset, graphIndex, mode)` <a id="c4d.modules.substance.CreateMaterial"></a>

Creates a Cinema 4D standard material from *asset*.

**Parameters:**

- **asset** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The Substance asset.

- **graphIndex** (*int*) – The index of the graph to use (for multi-graph Substances).

- **mode** (*int*) –

  The material creation mode

  |   |   |
  |---|---|
  | *SUBSTANCE_MATERIAL_MODE_STANDARD* | Create standard material. |
  | *SUBSTANCE_MATERIAL_MODE_METALLIC* | Create metallic material. |
  | *SUBSTANCE_MATERIAL_MODE_GLOSSY* | Create glossy material. |
  | *SUBSTANCE_MATERIAL_MODE_AUTO* | Use heuristic to choose one of the three above (see Cinema 4D’s user manual). |
  | *SUBSTANCE_MATERIAL_MODE_NONE* | Do not create material. |

**Return type:** [`c4d.BaseMaterial`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial)

**Returns:** The created material.

#### `c4d.modules.substance.CreateSubstanceShader(asset)` <a id="c4d.modules.substance.CreateSubstanceShader"></a>

Creates a Substance shader linked to *asset*.

**Parameters:** **asset** (*Optional*[[*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]) – The Substance asset. Can be **None** (since R18.039).

**Return type:** [`c4d.BaseShader`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseShader/index.md#c4d.BaseShader)

**Returns:** The created Substance shader.

#### `c4d.modules.substance.MaterialUsesSubstance(mat)` <a id="c4d.modules.substance.MaterialUsesSubstance"></a>

Checks if *mat* contains any Substance shaders.

**Parameters:** **mat** ([*c4d.BaseMaterial*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial)) – The material to check for Substance shaders.

**Return type:** bool

**Returns:** **True** if the material uses a Substance shader, otherwise **False**.

### Preferences <a id="c4d.modules.substance-function-Preferences"></a>

#### `c4d.modules.substance.PrefsGetMaterialModeSetting()` <a id="c4d.modules.substance.PrefsGetMaterialModeSetting"></a>

Convenience function to get the material creation mode set in Substance preferences.

**Return type:** int

**Returns:**

The material creation mode:

|   |   |
|---|---|
| *SUBSTANCE_MATERIAL_MODE_STANDARD* | Create standard material. |
| *SUBSTANCE_MATERIAL_MODE_METALLIC* | Create metallic material. |
| *SUBSTANCE_MATERIAL_MODE_GLOSSY* | Create glossy material. |
| *SUBSTANCE_MATERIAL_MODE_AUTO* | Use heuristic to choose one of the three above (see Cinema 4D’s user manual). |
| *SUBSTANCE_MATERIAL_MODE_NONE* | Do not create material. |

#### `c4d.modules.substance.PrefsGetPreviewSetting()` <a id="c4d.modules.substance.PrefsGetPreviewSetting"></a>

Convenience function to get the preview mode for Content Browser set in Substance preferences.

**Return type:** int

**Returns:** *0* for mosaic preview, otherwise rendered preview scene.
