<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/render/SceneColorConverter/index.html -->

# c4d.modules.render.SceneColorConverter <a id="c4d-modules-render-scenecolorconverter"></a>

## *class* `c4d.modules.render.SceneColorConverter` <a id="c4d.modules.render.SceneColorConverter"></a>

Translates colors stored in scenes and scene elements to new color spaces, preserving the visual identity of the stored colors.

*New in version 2025.2.0.*

Primarily meant to be used to convert legacy classic color management scenes to OCIO color management.

## Overview <a id="overview"></a>

**Conversion Operations**

- [`SceneColorConverter.ConvertData()`](#c4d.modules.render.SceneColorConverter.ConvertData): Converts colors in a custom data type.
- [`SceneColorConverter.ConvertObject()`](#c4d.modules.render.SceneColorConverter.ConvertObject): Converts the colors of a singular scene element.
- [`SceneColorConverter.ConvertObjects()`](#c4d.modules.render.SceneColorConverter.ConvertObjects): Converts the colors of multiple scene elements.
- [`SceneColorConverter.Init()`](#c4d.modules.render.SceneColorConverter.Init): Initializes the color converter.

**Magic Methods**

- [`SceneColorConverter.__init__()`](#c4d.modules.render.SceneColorConverter.__init__): Constructs an instance of *SceneColorConverter*.

## Members <a id="members"></a>

### Conversion Operations <a id="c4d.modules.render.SceneColorConverter-method-Conversion-Operations"></a>

#### `SceneColorConverter.ConvertData(self, data, treatVectorAsColor=False)` <a id="c4d.modules.render.SceneColorConverter.ConvertData"></a>

Converts colors in a custom data type.

**Parameters:**

- **data** (*any*) – The data object to convert.
- **treatVectorAsColor** (*bool*) – If to treat vectors as color data.

**Returns:** *True*, if the data was converted, *False* otherwise. Defaults to *False*. None if an error occurred.

**Return type:** Optional[bool]

#### `SceneColorConverter.ConvertObject(self, doc, op)` <a id="c4d.modules.render.SceneColorConverter.ConvertObject"></a>

Converts the colors of a singular scene element.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document from which the color settings are taken. Must be the same document which was used to initialize this instance.
- **op** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The scene element to convert.

**Returns:** The converted scene elements. Empty if the conversion failed.

**Return type:** Tuple[[c4d.BaseList2D](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

#### `SceneColorConverter.ConvertObjects(self, doc, objects)` <a id="c4d.modules.render.SceneColorConverter.ConvertObjects"></a>

Converts the colors of multiple scene elements.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document from which the color settings are taken. Must be the same document which was used to initialize this instance.
- **objects** (*Iterator*[[*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]) – The scene elements to convert.

**Returns:** The converted scene elements. Empty if the conversion failed.

**Return type:** Tuple[[c4d.BaseList2D](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

#### `SceneColorConverter.Init(self, config, inputColorSpaceLowName, inputColorSpaceHighName, renderColorSpaceName, flags=1)` <a id="c4d.modules.render.SceneColorConverter.Init"></a>

Initializes the color converter.

**Parameters:**

- **config** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) –

  The document from which the color settings are taken.

  > **Note:** Will be renamed *doc* in the next release.

- **inputColorSpaceLowName** (*str*) – The name of the new low input color space.

- **inputColorSpaceHighName** (*str*) – The name of the new high input color space.

- **renderColorSpaceName** (*str*) – The name of the new render color space.

- **flags** (*Optional*[*int*]) –

  The flags for the conversion. The values are:

  | Symbol ID | Description |
  |---|---|
  | NONE | No flags. |
  | ADD_UNDO | Create an undo step for all changes. This must not be set when the conversion is called from a thread. |
  | CLASSIC_LINEAR_TO_SRGB | The Scene is a classic scene and would have converted Linear to sRGB on color values. |
  | CLASSIC_SRGB_TO_LINEAR | The Scene is a classic scene and would have converted sRGB to Linear on color values. |
  | FORCE_LINEAR_LIGHTS | Forces the conversion from classic or to classic color management to interpret lights to have linear brightness. Otherwise lights will adjust their brightness. |

**Raises:** **RuntimeError** – When the initialization failed.

### Magic Methods <a id="c4d.modules.render.SceneColorConverter-method-Magic-Methods"></a>

#### `SceneColorConverter.__init__(self)` <a id="c4d.modules.render.SceneColorConverter.__init__"></a>

Constructs an instance of *SceneColorConverter*.

*New in version 2025.2.0.*
