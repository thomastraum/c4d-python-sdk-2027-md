<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.documents/BaseVideoPost/index.html -->

# c4d.documents.BaseVideoPost <a id="c4d-documents-basevideopost"></a>

## *class* `c4d.documents.BaseVideoPost` <a id="c4d.documents.BaseVideoPost"></a>

Parent Class:

- [`c4d.BaseList2D`](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

## Overview <a id="overview"></a>

**Magic Methods**

- [`BaseVideoPost.__init__()`](#c4d.documents.BaseVideoPost.__init__): Initializes a new [`BaseVideoPost`](#c4d.documents.BaseVideoPost).

**Render Engine And Image Processing**

- [`BaseVideoPost.RenderEngineCheck()`](#c4d.documents.BaseVideoPost.RenderEngineCheck): Checks if a videopost is available for a certain render engine.
- [`BaseVideoPost.StereoMergeImages()`](#c4d.documents.BaseVideoPost.StereoMergeImages): Merges stereoscopic images for rendering.

**Stereo Camera Management**

- [`BaseVideoPost.StereoGetCameraCountEditor()`](#c4d.documents.BaseVideoPost.StereoGetCameraCountEditor): Returns the number of stereoscopic editor cameras.
- [`BaseVideoPost.StereoGetCameraCountRenderer()`](#c4d.documents.BaseVideoPost.StereoGetCameraCountRenderer): Returns the number of stereoscopic cameras used for rendering.
- [`BaseVideoPost.StereoGetCameraInfo()`](#c4d.documents.BaseVideoPost.StereoGetCameraInfo): Retrieves the information for a stereoscopic camera.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.documents.BaseVideoPost-method-Magic-Methods"></a>

#### `BaseVideoPost.__init__(self, type)` <a id="c4d.documents.BaseVideoPost.__init__"></a>

Initializes a new [`BaseVideoPost`](#c4d.documents.BaseVideoPost).

**Parameters:** **type** (*int*) – The videopost type: [VideoPost Types](../../../types/videoposts.md).

### Render Engine And Image Processing <a id="c4d.documents.BaseVideoPost-method-Render-Engine-And-Image-Processing"></a>

#### `BaseVideoPost.RenderEngineCheck(self, type)` <a id="c4d.documents.BaseVideoPost.RenderEngineCheck"></a>

Checks if a videopost is available for a certain render engine.

**Parameters:** **type** (*int*) – The ID of the render engine.

**Return type:** bool

**Returns:** **True** if the videopost is available for the specified render engine, otherwise **False**.

#### `BaseVideoPost.StereoMergeImages(self, dest, source, settings, transform)` <a id="c4d.documents.BaseVideoPost.StereoMergeImages"></a>

Merges stereoscopic images for rendering.

**Parameters:**

- **dest** ([*c4d.bitmaps.BaseBitmap*](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The destination bitmap to be filled with the merged stereoscopic image.

- **source** (*List*[[*c4d.bitmaps.BaseBitmap*](../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]) – A list containing the stereoscopic images.

- **settings** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The stereoscopic render settings: See *RDATA_STEREO* in *drendersettings.h*.

- **transform** (*int*) –

  The color space transformation mode:

  | Symbol ID | Description |
  |---|---|
  | NONE | None. |
  | COLORSPACETRANSFORMATION_LINEAR_TO_SRGB | Linear to sRGB color space transformation. |
  | COLORSPACETRANSFORMATION_SRGB_TO_LINEAR | sRGB to linear color space transformation. |
  | COLORSPACETRANSFORMATION_LINEAR_TO_VIEW | Linear to display color space transformation. |
  | COLORSPACETRANSFORMATION_SRGB_TO_VIEW | sRGB to display color space transformation. |

**Return type:** bool

**Returns:** **True** if the stereo images were merged, otherwise **False**.

### Stereo Camera Management <a id="c4d.documents.BaseVideoPost-method-Stereo-Camera-Management"></a>

#### `BaseVideoPost.StereoGetCameraCountEditor(self, doc, bd)` <a id="c4d.documents.BaseVideoPost.StereoGetCameraCountEditor"></a>

Returns the number of stereoscopic editor cameras.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document.
- **bd** ([*c4d.BaseDraw*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The active view.

**Return type:** int

**Returns:** The number of stereoscopic cameras.

#### `BaseVideoPost.StereoGetCameraCountRenderer(self, doc, rd)` <a id="c4d.documents.BaseVideoPost.StereoGetCameraCountRenderer"></a>

Returns the number of stereoscopic cameras used for rendering.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document.
- **rd** ([*c4d.documents.RenderData*](../RenderData/index.md#c4d.documents.RenderData)) – The active render settings.

**Return type:** int

**Returns:** The number of stereoscopic cameras.

#### `BaseVideoPost.StereoGetCameraInfo(self, doc, bd, rd, index)` <a id="c4d.documents.BaseVideoPost.StereoGetCameraInfo"></a>

Retrieves the information for a stereoscopic camera.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../BaseDocument/index.md#c4d.documents.BaseDocument)) – The active document.
- **bd** ([*c4d.BaseDraw*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The active view.
- **rd** ([*c4d.documents.RenderData*](../RenderData/index.md#c4d.documents.RenderData)) – The active render settings.
- **index** (*int*) – The index of the stereoscopic camera.

**Return type:** Optional[Dict[[c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix), float, float, str]]

**Returns:**

A dictionary (**None** if the function failed) with the following information for the stereoscopic camera:

*m*: [`c4d.Matrix`](../../c4d/Matrix/index.md#c4d.Matrix): Matrix of the stereoscopic camera.  
*off_x*: *float*: Stereoscopic camera film X offset.  
*off_y*: *float*: Stereoscopic camera film Y offset.  
*name*: *str*: Name of the stereoscopic camera.
