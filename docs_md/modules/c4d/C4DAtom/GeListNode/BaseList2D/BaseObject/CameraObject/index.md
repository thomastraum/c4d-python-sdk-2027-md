<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/CameraObject/index.html -->

# c4d.CameraObject <a id="c4d-cameraobject"></a>

## *class* `c4d.CameraObject` <a id="c4d.CameraObject"></a>

Represents a Camera object.

The instance object class of type *Ocamera*.

Parent Class:

- [`c4d.BaseObject`](../index.md#c4d.BaseObject)

## Overview <a id="overview"></a>

**Camera Settings**

- [`CameraObject.GetAperture()`](#c4d.CameraObject.GetAperture): Return the aperture width.
- [`CameraObject.GetFocus()`](#c4d.CameraObject.GetFocus): Get the focus of the camera.
- [`CameraObject.GetOffset()`](#c4d.CameraObject.GetOffset): Return the offset.
- [`CameraObject.GetProjection()`](#c4d.CameraObject.GetProjection): Get the camera projection.
- [`CameraObject.GetZoom()`](#c4d.CameraObject.GetZoom): Get the zoom of the camera.
- [`CameraObject.SetAperture()`](#c4d.CameraObject.SetAperture): Set the aperture width.
- [`CameraObject.SetFocus()`](#c4d.CameraObject.SetFocus): Set the focus of the camera.
- [`CameraObject.SetOffset()`](#c4d.CameraObject.SetOffset): Set the offset.
- [`CameraObject.SetProjection()`](#c4d.CameraObject.SetProjection): Set the camera projection.
- [`CameraObject.SetZoom()`](#c4d.CameraObject.SetZoom): Set the zoom of the camera.

**Magic Methods**

- [`CameraObject.__init__()`](#c4d.CameraObject.__init__)

**Stereo Camera**

- [`CameraObject.StereoGetCameraCount()`](#c4d.CameraObject.StereoGetCameraCount): Returns the number of stereoscopic cameras.
- [`CameraObject.StereoGetCameraInfo()`](#c4d.CameraObject.StereoGetCameraInfo): Returns the information for a stereoscopic camera.

## Members <a id="members"></a>

### Camera Settings <a id="c4d.CameraObject-method-Camera-Settings"></a>

#### `CameraObject.GetAperture(self)` <a id="c4d.CameraObject.GetAperture"></a>

Return the aperture width.

**Return type:** float

**Returns:** The camera’s aperture.

#### `CameraObject.GetFocus(self)` <a id="c4d.CameraObject.GetFocus"></a>

Get the focus of the camera.

**Return type:** float

**Returns:** The focus.

#### `CameraObject.GetOffset(self)` <a id="c4d.CameraObject.GetOffset"></a>

Return the offset.

**Return type:** [c4d.Vector](../../../../../Vector/index.md#c4d.Vector)

**Returns:** The offset.

#### `CameraObject.GetProjection(self)` <a id="c4d.CameraObject.GetProjection"></a>

Get the camera projection.

**Return type:** int

**Returns:** The projection. See `Ocamera.h` for values.

#### `CameraObject.GetZoom(self)` <a id="c4d.CameraObject.GetZoom"></a>

Get the zoom of the camera.

**Return type:** float

**Returns:** The zoom.

#### `CameraObject.SetAperture(self, v)` <a id="c4d.CameraObject.SetAperture"></a>

Set the aperture width.

**Parameters:** **v** (*float*) – The camera’s aperture.

#### `CameraObject.SetFocus(self, v)` <a id="c4d.CameraObject.SetFocus"></a>

Set the focus of the camera.

**Parameters:** **v** (*float*) – The focus.

#### `CameraObject.SetOffset(self, offset)` <a id="c4d.CameraObject.SetOffset"></a>

Set the offset.

**Parameters:** **offset** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The offset.

#### `CameraObject.SetProjection(self, projection)` <a id="c4d.CameraObject.SetProjection"></a>

Set the camera projection.

**Parameters:** **projection** (*int*) – The projection. See `Ocamera.h` for values.

#### `CameraObject.SetZoom(self, zoom)` <a id="c4d.CameraObject.SetZoom"></a>

Set the zoom of the camera.

**Parameters:** **zoom** (*float*) – The zoom.

### Magic Methods <a id="c4d.CameraObject-method-Magic-Methods"></a>

#### `CameraObject.__init__(self)` <a id="c4d.CameraObject.__init__"></a>

### Stereo Camera <a id="c4d.CameraObject-method-Stereo-Camera"></a>

#### `CameraObject.StereoGetCameraCount(self, doc, bd, rd, flags=0)` <a id="c4d.CameraObject.StereoGetCameraCount"></a>

Returns the number of stereoscopic cameras.

*New in version R19.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the operation.
- **bd** ([*c4d.BaseDraw*](../../BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The stereoscopic view.
- **rd** ([*c4d.documents.RenderData*](../../../../../../c4d.documents/RenderData/index.md#c4d.documents.RenderData)) – The stereoscopic render settings.
- **flags** (*int*) – Optional. Currently unused. Set to *0*.

**Return type:** int

**Returns:** The number of stereoscopic cameras.

#### `CameraObject.StereoGetCameraInfo(self, doc, bd, rd, n, flags=0)` <a id="c4d.CameraObject.StereoGetCameraInfo"></a>

Returns the information for a stereoscopic camera.

*New in version R19.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the operation.
- **bd** ([*c4d.BaseDraw*](../../BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The stereoscopic view.
- **rd** ([*c4d.documents.RenderData*](../../../../../../c4d.documents/RenderData/index.md#c4d.documents.RenderData)) – The stereoscopic render settings.
- **n** (*int*) – The stereoscopic camera index: *0* <= *n* < [`StereoGetCameraCount()`](#c4d.CameraObject.StereoGetCameraCount)
- **flags** (*int*) – Optional. Currently unused. Set to *0*.

**Return type:** Optional[Dict[[c4d.Matrix](../../../../../Matrix/index.md#c4d.Matrix), float, float, str]]

**Returns:**

A dictionary (**None** if the function failed) with the stereo camera information:

’m’: Stereoscopic camera matrix.  
’off_x’: Stereoscopic camera film X offset.  
’off_y’: Stereoscopic camera film Y offset.  
’name’: Stereoscopic camera name.
