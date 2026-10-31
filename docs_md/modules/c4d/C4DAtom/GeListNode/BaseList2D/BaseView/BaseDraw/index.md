<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.html -->

# c4d.BaseDraw <a id="c4d-basedraw"></a>

## *class* `c4d.BaseDraw` <a id="c4d.BaseDraw"></a>

This class represents a Cinema 4D window.

> **Warning:** This type cannot be instantiated.

Parent Class:

- [`c4d.BaseView`](../index.md#c4d.BaseView)

## Overview <a id="overview"></a>

**Camera Management**

- [`BaseDraw.GetEditorCamera()`](#c4d.BaseDraw.GetEditorCamera): Returns the editor camera.
- [`BaseDraw.GetSceneCamera()`](#c4d.BaseDraw.GetSceneCamera): Returns the current scene camera from the passed document, or **None** if no scene camera is used.
- [`BaseDraw.HasCameraLink()`](#c4d.BaseDraw.HasCameraLink): Indicates if the camera link is enabled.
- [`BaseDraw.SetSceneCamera()`](#c4d.BaseDraw.SetSceneCamera): Sets a new scene camera.

**Color Management**

- [`BaseDraw.CheckColor()`](#c4d.BaseDraw.CheckColor): Makes sure that a color has at least 15% difference to the background color.
- [`BaseDraw.ConvertColor()`](#c4d.BaseDraw.ConvertColor): Converts colors from document color profile to viewport color profile.
- [`BaseDraw.ConvertColorReverse()`](#c4d.BaseDraw.ConvertColorReverse): Converts colors from viewport color profile to document color profile.
- [`BaseDraw.GetHighlightPassColor()`](#c4d.BaseDraw.GetHighlightPassColor): Returns the color in which the object has to be drawn in the highlight pass.
- [`BaseDraw.GetObjectColor()`](#c4d.BaseDraw.GetObjectColor): Returns the wireframe color in editor for the specified object.

**Coordinate Transforms**

- [`BaseDraw.GetViewMatrix()`](#c4d.BaseDraw.GetViewMatrix): Gets the view matrix.
- [`BaseDraw.SetMatrix_Camera()`](#c4d.BaseDraw.SetMatrix_Camera): Sets the transformation matrix to the camera system.
- [`BaseDraw.SetMatrix_Matrix()`](#c4d.BaseDraw.SetMatrix_Matrix): Sets the transformation matrix to the given matrix mg.
- [`BaseDraw.SetMatrix_Projection()`](#c4d.BaseDraw.SetMatrix_Projection): For internal use only.
- [`BaseDraw.SetMatrix_Screen()`](#c4d.BaseDraw.SetMatrix_Screen): Sets the transformation matrix to screen coordinates, i.e.

**Depth And Clipping**

- [`BaseDraw.LineZOffset()`](#c4d.BaseDraw.LineZOffset): Sets the current Z buffer offset.
- [`BaseDraw.SetClipPlaneOffset()`](#c4d.BaseDraw.SetClipPlaneOffset): Offsets the Viewport clipping planes by this offset.
- [`BaseDraw.SetDepth()`](#c4d.BaseDraw.SetDepth): Enables/disables writing to the depth buffer.

**Drawing Appearance**

- [`BaseDraw.SetPen()`](#c4d.BaseDraw.SetPen): Sets the pen color for following drawing operations.
- [`BaseDraw.SetPointSize()`](#c4d.BaseDraw.SetPointSize): Sets the drawn point size.
- [`BaseDraw.SimpleShade()`](#c4d.BaseDraw.SimpleShade): A quick shading algorithm that only takes the angle to the camera and a default light into account.

**HUD Text**

- [`BaseDraw.DrawHUDText()`](#c4d.BaseDraw.DrawHUDText): Draws 2D text into the viewport in the style of the HUD.
- [`BaseDraw.DrawMultipleHUDText()`](#c4d.BaseDraw.DrawMultipleHUDText): Draws many 2D text into the viewport at once.

**Line And Curve Drawing**

- [`BaseDraw.DrawArc()`](#c4d.BaseDraw.DrawArc): Draws an arc (section of a circle) in the current pen color at *pos*.
- [`BaseDraw.DrawCircle()`](#c4d.BaseDraw.DrawCircle): Draws an ellipse in the current pen color.
- [`BaseDraw.DrawCircle2D()`](#c4d.BaseDraw.DrawCircle2D): Draws a circle in the current pen color with a radius of *rad* and the center at (*mx*, *my*).
- [`BaseDraw.DrawLine()`](#c4d.BaseDraw.DrawLine): Draws a line in the current pen color between *p1* and *p2*.
- [`BaseDraw.DrawLine2D()`](#c4d.BaseDraw.DrawLine2D): Draws a line in the current pen color between *p1* and *p2*.

**Magic Methods**

- [`BaseDraw.__init__()`](#c4d.BaseDraw.__init__): Initialize a new base draw.

**Object And Batch Rendering**

- [`BaseDraw.AddToPostPass()`](#c4d.BaseDraw.AddToPostPass): Adds the object *op* to *DRAWPASS_XRAY*.
- [`BaseDraw.DrawArrayEnd()`](#c4d.BaseDraw.DrawArrayEnd): Each `DrawPolygon()` puts the polygon into an internal array and draws the polygons when the array is full or an Viewport state changes (e.g.
- [`BaseDraw.DrawObject()`](#c4d.BaseDraw.DrawObject): Draws a polygon object into the view.
- [`BaseDraw.DrawPolygonObject()`](#c4d.BaseDraw.DrawPolygonObject): Draws a polygon object into the view.

**Operation Control**

- [`BaseDraw.DoUndo()`](#c4d.BaseDraw.DoUndo): Performs an undo operation in the view.
- [`BaseDraw.InitUndo()`](#c4d.BaseDraw.InitUndo): Called before a change is made to the view to add the old setting to the undo buffer for the view.
- [`BaseDraw.TestBreak()`](#c4d.BaseDraw.TestBreak): Checks for thread breaks in the draw.

**Parameter Access**

- [`BaseDraw.GetDrawParam()`](#c4d.BaseDraw.GetDrawParam): Gets draw parameters.
- [`BaseDraw.GetParameterData()`](#c4d.BaseDraw.GetParameterData): Get a new parameter object.
- [`BaseDraw.SetDrawParam()`](#c4d.BaseDraw.SetDrawParam): Sets draw parameters.

**Point And Handle Drawing**

- [`BaseDraw.DrawHandle()`](#c4d.BaseDraw.DrawHandle): Draws a standard handle (orange dot) at *vp*.
- [`BaseDraw.DrawHandle2D()`](#c4d.BaseDraw.DrawHandle2D): Draws a standard handle (orange dot) at *p*.
- [`BaseDraw.DrawPoint2D()`](#c4d.BaseDraw.DrawPoint2D): Draws a one-pixel point in the current pen color at p.
- [`BaseDraw.DrawPoints()`](#c4d.BaseDraw.DrawPoints): Draws an array of points with individual colors.

**Shape Rendering**

- [`BaseDraw.DrawBox()`](#c4d.BaseDraw.DrawBox): Draws a box.
- [`BaseDraw.DrawPolygon()`](#c4d.BaseDraw.DrawPolygon): Draws a manually shaded triangle or quadrangle.
- [`BaseDraw.DrawSphere()`](#c4d.BaseDraw.DrawSphere): Draws a sphere at position off with size specified by the size vector in each direction and color specified by col.

**Texture And Lighting**

- [`BaseDraw.DrawTexture()`](#c4d.BaseDraw.DrawTexture): Draws a colored and shaded texture polygon using the points in *padr4*, the colors in *cadr*, the normals in *vnadr* and the UV coordinates in *uvadr*.
- [`BaseDraw.SetLightList()`](#c4d.BaseDraw.SetLightList): Sets the lighting used by the draw functions.
- [`BaseDraw.SetTexture()`](#c4d.BaseDraw.SetTexture): Set a texture used by the vertex buffer.

**Transparency Control**

- [`BaseDraw.GetTransparency()`](#c4d.BaseDraw.GetTransparency): Returns the current transparency value for polygons.
- [`BaseDraw.SetTransparency()`](#c4d.BaseDraw.SetTransparency): Sets the transparency value for following polygons.

**View Initialization**

- [`BaseDraw.InitClipbox()`](#c4d.BaseDraw.InitClipbox): Used to render into a framebuffer with different resolution than the editor view.
- [`BaseDraw.InitializeView()`](#c4d.BaseDraw.InitializeView): Used after rendering into a framebuffer with different resolution than the editor view.
- [`BaseDraw.InitView()`](#c4d.BaseDraw.InitView): Used to render into a framebuffer with different resolution than the editor view.

**Viewport State And Interaction**

- [`BaseDraw.GetDisplayFilter()`](#c4d.BaseDraw.GetDisplayFilter): Returns the current display filter.
- [`BaseDraw.GetDrawPass()`](#c4d.BaseDraw.GetDrawPass): Gets the current drawpass.
- [`BaseDraw.GetEditorWindow()`](#c4d.BaseDraw.GetEditorWindow): Get the editor window of the BaseDraw.
- [`BaseDraw.GetEditState()`](#c4d.BaseDraw.GetEditState): Get the edit state.
- [`BaseDraw.GetFrameScreen()`](#c4d.BaseDraw.GetFrameScreen): Used in the Extended GL mode.
- [`BaseDraw.GetGridStep()`](#c4d.BaseDraw.GetGridStep): Gets the grid spacing and the transparency value of the minor grid that fade when the user zoom in or out with dynamic grid.
- [`BaseDraw.GetReductionMode()`](#c4d.BaseDraw.GetReductionMode): Gets the reduction mode of the base draw.
- [`BaseDraw.IsViewOpen()`](#c4d.BaseDraw.IsViewOpen): Checks if the current tool can use the current SDS/Deformed editing state.
- [`BaseDraw.PointInRange()`](#c4d.BaseDraw.PointInRange): Returns **True** if the screen point (x,y) is within a hit range of the world point p, i.e.

## Members <a id="members"></a>

### Camera Management <a id="c4d.BaseDraw-method-Camera-Management"></a>

#### `BaseDraw.GetEditorCamera(self)` <a id="c4d.BaseDraw.GetEditorCamera"></a>

Returns the editor camera.

**Return type:** [c4d.BaseObject](../../BaseObject/index.md#c4d.BaseObject)

**Returns:** The editor camera. Guaranteed to never be **None**.

#### `BaseDraw.GetSceneCamera(self, doc)` <a id="c4d.BaseDraw.GetSceneCamera"></a>

Returns the current scene camera from the passed document, or **None** if no scene camera is used.

**Parameters:** **doc** (*Optional*[[*c4d.documents.BaseDocument*](../../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]) – The document to get the scene camera from.

**Return type:** [c4d.BaseObject](../../BaseObject/index.md#c4d.BaseObject)

**Returns:** The scene camera.

#### `BaseDraw.HasCameraLink(self)` <a id="c4d.BaseDraw.HasCameraLink"></a>

Indicates if the camera link is enabled.

**Return type:** bool

**Returns:** **True** if a scene camera is used, and **False** if the editor camera is used.

#### `BaseDraw.SetSceneCamera(self, op=None, animate=False)` <a id="c4d.BaseDraw.SetSceneCamera"></a>

Sets a new scene camera. If *op* is **None**, the editor camera is used.

**Parameters:**

- **op** (*Optional*[[*c4d.BaseObject*](../../BaseObject/index.md#c4d.BaseObject)]) – The new camera.
- **animate** (*bool*) – Private.

### Color Management <a id="c4d.BaseDraw-method-Color-Management"></a>

#### `BaseDraw.CheckColor(self, col)` <a id="c4d.BaseDraw.CheckColor"></a>

Makes sure that a color has at least 15% difference to the background color.

**Parameters:** **col** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The original vector.

**Return type:** [c4d.Vector](../../../../../Vector/index.md#c4d.Vector)

**Returns:** The new color, adjusted if needed.

#### `BaseDraw.ConvertColor(self, c)` <a id="c4d.BaseDraw.ConvertColor"></a>

Converts colors from document color profile to viewport color profile.

**Parameters:** **c** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The color to convert (document).

**Return type:** [c4d.Vector](../../../../../Vector/index.md#c4d.Vector)

**Returns:** The converted color (viewport).

#### `BaseDraw.ConvertColorReverse(self, c)` <a id="c4d.BaseDraw.ConvertColorReverse"></a>

Converts colors from viewport color profile to document color profile.

**Parameters:** **c** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The color to convert (viewport).

**Return type:** [c4d.Vector](../../../../../Vector/index.md#c4d.Vector)

**Returns:** The converted color (document).

#### `BaseDraw.GetHighlightPassColor(self, bh, lineObject)` <a id="c4d.BaseDraw.GetHighlightPassColor"></a>

Returns the color in which the object has to be drawn in the highlight pass.

*New in version R19.*

> **Note:** This function should only be called in the highlight pass.

**Parameters:**

- **bh** ([*c4d.plugins.BaseDrawHelp*](../../../../../../c4d.plugins/BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp)) – The base draw help.
- **lineObject** (*int*) – Must be set to **True** if the object is a line object.

**Return type:** Optional[[c4d.Vector](../../../../../Vector/index.md#c4d.Vector)]

**Returns:** The highlight color, or **None** if drawing the object can be skipped.

#### `BaseDraw.GetObjectColor(self, bh, op)` <a id="c4d.BaseDraw.GetObjectColor"></a>

Returns the wireframe color in editor for the specified object.  
Some types of objects have certain colors.

> **Note:** For polygon objects the main color is taken into account.

**Parameters:**

- **bh** ([*c4d.plugins.BaseDrawHelp*](../../../../../../c4d.plugins/BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp)) – The current base draw helper.
- **op** ([*c4d.BaseObject*](../../BaseObject/index.md#c4d.BaseObject)) – The object.

**Return type:** [c4d.Vector](../../../../../Vector/index.md#c4d.Vector)

**Returns:** The object color.

### Coordinate Transforms <a id="c4d.BaseDraw-method-Coordinate-Transforms"></a>

#### `BaseDraw.GetViewMatrix(self, n)` <a id="c4d.BaseDraw.GetViewMatrix"></a>

Gets the view matrix.

*New in version R14.014.*

**Parameters:**

**n** (*int*) –

View matrix to get:

|   |   |
|---|---|
| *DRAW_GET_VIEWMATRIX_PROJECTION* | Projection matrix. |
| *DRAW_GET_VIEWMATRIX_PROJECTION_LARGE_Z* | Projection matrix without consideration of the set clipping planes. The following values for near and far clipping are used instead: near=`1`, far=`100000` for perspective projection and near=`-1000000`, far=`1000000` for other projection types. |
| *DRAW_GET_VIEWMATRIX_INV_CAMERA* | Inverse camera matrix. |
| *DRAW_GET_VIEWMATRIX_MODELVIEW_PROJECTION* | Projection*View*Model matrix. Slow. |

**Return type:** Tuple[16*float]

**Returns:** The view matrix (4x4 matrix).

#### `BaseDraw.SetMatrix_Camera(self)` <a id="c4d.BaseDraw.SetMatrix_Camera"></a>

Sets the transformation matrix to the camera system.

> > **Note:** This function only affects the new draw functions below it, i.e. [`DrawHandle()`](#c4d.BaseDraw.DrawHandle), [`DrawTexture()`](#c4d.BaseDraw.DrawTexture), [`DrawCircle()`](#c4d.BaseDraw.DrawCircle), [`DrawBox()`](#c4d.BaseDraw.DrawBox), and [`DrawSphere()`](#c4d.BaseDraw.DrawSphere).

#### `BaseDraw.SetMatrix_Matrix(self, op, mg, zoffset=-1)` <a id="c4d.BaseDraw.SetMatrix_Matrix"></a>

Sets the transformation matrix to the given matrix mg.  
The matrix should transform coordinates passed to the draw functions into world coordinates.

**Parameters:**

- **op** (*Optional*[[*c4d.BaseObject*](../../BaseObject/index.md#c4d.BaseObject)]) – A scene object. If passed this is used to compare if the same object is still used.

- **mg** ([*c4d.Matrix*](../../../../../Matrix/index.md#c4d.Matrix)) – The new transformation matrix.

- **zoffset** (*int*) –

  Sets the current Z buffer offset.

  Use this to for example draw lines over shaded polygons in front of the screen.  
  A higher zoffset value means a higher draw priority in the Z buffer. For example:

  > - shaded polygon (level 0)
  > - unselected edges (level 2)
  > - selected edges (level 4)

#### `BaseDraw.SetMatrix_Projection(self)` <a id="c4d.BaseDraw.SetMatrix_Projection"></a>

For internal use only.

#### `BaseDraw.SetMatrix_Screen(self, offset=-1)` <a id="c4d.BaseDraw.SetMatrix_Screen"></a>

Sets the transformation matrix to screen coordinates, i.e. from (0, 0) to (width, height).

> > **Note:** This function only affects the new draw functions below it, i.e. [`DrawHandle()`](#c4d.BaseDraw.DrawHandle), [`DrawTexture()`](#c4d.BaseDraw.DrawTexture), [`DrawCircle()`](#c4d.BaseDraw.DrawCircle), [`DrawBox()`](#c4d.BaseDraw.DrawBox), and [`DrawSphere()`](#c4d.BaseDraw.DrawSphere).

**Parameters:**

**offset** (*int*) –

Sets the current Z buffer offset.  
Use this to for example draw lines over shaded polygons in front of the screen.  
A higher zoffset value means a higher draw priority in the Z buffer. For example:

- shaded polygon (level 0)
- unselected edges (level 2)
- selected edges (level 4)

### Depth And Clipping <a id="c4d.BaseDraw-method-Depth-And-Clipping"></a>

#### `BaseDraw.LineZOffset(self, offset)` <a id="c4d.BaseDraw.LineZOffset"></a>

Sets the current Z buffer offset.  
Use this to for example draw lines over shaded polygons in front of the screen.  
A higher *offset* value means a higher draw priority in the Z buffer. For example:

> - shaded polygon (level 0)
> - unselected edges (level 2)
> - selected edges (level 4)
>
> > **Note:** This function only affects the new draw functions below it, i.e. [`DrawHandle()`](#c4d.BaseDraw.DrawHandle), [`DrawTexture()`](#c4d.BaseDraw.DrawTexture), [`DrawCircle()`](#c4d.BaseDraw.DrawCircle), [`DrawBox()`](#c4d.BaseDraw.DrawBox), and [`DrawSphere()`](#c4d.BaseDraw.DrawSphere).

**Parameters:** **offset** (*int*) – The new Z buffer offset.

#### `BaseDraw.SetClipPlaneOffset(self, o)` <a id="c4d.BaseDraw.SetClipPlaneOffset"></a>

Offsets the Viewport clipping planes by this offset.

*New in version R14.014.*

**Parameters:** **o** (*float*) – The offset.

#### `BaseDraw.SetDepth(self, enable)` <a id="c4d.BaseDraw.SetDepth"></a>

Enables/disables writing to the depth buffer.

**Parameters:** **enable** (*bool*) – **True** to enable depth buffer writing, otherwise **False**.

### Drawing Appearance <a id="c4d.BaseDraw-method-Drawing-Appearance"></a>

#### `BaseDraw.SetPen(self, col, flags=0)` <a id="c4d.BaseDraw.SetPen"></a>

Sets the pen color for following drawing operations.

**Parameters:**

- **col** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The new color.

- **flags** (*Optional*[*int*]) –

  |   |   |
  |---|---|
  | *SET_PEN_USE_PROFILE_COLOR* | Set this flag if the color is already in the color space of the [`BaseDraw`](#c4d.BaseDraw). Otherwise the color will be converted. |

#### `BaseDraw.SetPointSize(self, pointsize)` <a id="c4d.BaseDraw.SetPointSize"></a>

Sets the drawn point size.

**Parameters:** **pointsize** (*float*) – The new point size.

#### `BaseDraw.SimpleShade(self, p, n)` <a id="c4d.BaseDraw.SimpleShade"></a>

A quick shading algorithm that only takes the angle to the camera and a default light into account.  
You pass a point and a normal in world space and get back the intensity.

> **Note:** Can be combined with [`DrawPolygon()`](#c4d.BaseDraw.DrawPolygon) to draw simple shaded polygons.

**Parameters:**

- **p** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – A point in world space.
- **n** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – A normal in world space.

**Return type:** float

**Returns:** The intensity of the light. Between 0 and 1.

### HUD Text <a id="c4d.BaseDraw-method-HUD-Text"></a>

#### `BaseDraw.DrawHUDText(self, x, y, txt)` <a id="c4d.BaseDraw.DrawHUDText"></a>

Draws 2D text into the viewport in the style of the HUD.

*New in version R18.020.*

**Parameters:**

- **x** (*int*) – The left X coordinate to draw the text at.
- **y** (*int*) – The upper Y coordinate to draw the text at.
- **txt** (*str*) – The text to draw.

#### `BaseDraw.DrawMultipleHUDText(self, texts)` <a id="c4d.BaseDraw.DrawMultipleHUDText"></a>

Draws many 2D text into the viewport at once.

*New in version R18.020.*

**Parameters:** **texts** (*List*[*Dict*[*'_txt': str*, *'_position': c4d.Vector*]]) – The list of text entries and their screen space positions to draw to the HUD.

### Line And Curve Drawing <a id="c4d.BaseDraw-method-Line-And-Curve-Drawing"></a>

#### `BaseDraw.DrawArc(self, pos, radius, angle_start, angle_end, subdiv=32, flags=0)` <a id="c4d.BaseDraw.DrawArc"></a>

Draws an arc (section of a circle) in the current pen color at *pos*.  
The coordinates must be in screen space.

*New in version R14.014.*

**Parameters:**

- **pos** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – Position of the rectangle that defines the arc.

- **radius** (*float*) – The radius.

- **angle_start** (*float*) – Start of the angle in radians.

- **angle_end** (*float*) – End of the angle in radians.

- **subdiv** (*int*) – The range between *angle_start* and *angle_end* is divided into *subdiv* line segments.

- **flags** (*int*) –

  *New in version R16.021.*

  Flags:

  |   |   |
  |---|---|
  | *NOCLIP_D* | Clip against the view border. |
  | *NOCLIP_Z* | Z clipping. |

#### `BaseDraw.DrawCircle(self, m)` <a id="c4d.BaseDraw.DrawCircle"></a>

Draws an ellipse in the current pen color.  
The ellipse is specified by the matrix m, where *m.v1* and *m.v2* are the axis vectors and m.off is the center position. (*m.v3* is not used.)  
The coordinates must be in world space.

> **Note:** The coordinates must be in the space defined by [`SetMatrix_Screen()`](#c4d.BaseDraw.SetMatrix_Screen), [`SetMatrix_Camera()`](#c4d.BaseDraw.SetMatrix_Camera) or [`SetMatrix_Matrix()`](#c4d.BaseDraw.SetMatrix_Matrix).

**Parameters:** **m** ([*c4d.Matrix*](../../../../../Matrix/index.md#c4d.Matrix)) – A matrix describing the circle.

#### `BaseDraw.DrawCircle2D(self, mx, my, rad)` <a id="c4d.BaseDraw.DrawCircle2D"></a>

Draws a circle in the current pen color with a radius of *rad* and the center at (*mx*, *my*).  
The coordinates must be in screen space.

> **Note:** Changes the matrix to screen with [`SetMatrix_Screen()`](#c4d.BaseDraw.SetMatrix_Screen) prior to drawing.

**Parameters:**

- **mx** (*int*) – Center x coordinate.
- **my** (*int*) – Center y coordinate.
- **rad** (*float*) – The radius.

#### `BaseDraw.DrawLine(self, p1, p2, flags)` <a id="c4d.BaseDraw.DrawLine"></a>

Draws a line in the current pen color between *p1* and *p2*.  
The coordinates must be in world space.

**Parameters:**

- **p1** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The start point.

- **p2** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The end point.

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *NOCLIP_D* | Clip against the view border. |
  | *NOCLIP_Z* | Z clipping. |

#### `BaseDraw.DrawLine2D(self, p1, p2)` <a id="c4d.BaseDraw.DrawLine2D"></a>

Draws a line in the current pen color between *p1* and *p2*.  
The coordinates must be in screen space.

> **Note:** Changes the matrix to screen with [`SetMatrix_Screen()`](#c4d.BaseDraw.SetMatrix_Screen) prior to drawing.

**Parameters:**

- **p1** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The start point.
- **p2** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The end point.

### Magic Methods <a id="c4d.BaseDraw-method-Magic-Methods"></a>

#### `BaseDraw.__init__(self)` <a id="c4d.BaseDraw.__init__"></a>

Initialize a new base draw.

*New in version R17.053.*

> **Note:** Useful for situations when there is no base draw available. It is used for instance in Mograph’s Camera shader.

### Object And Batch Rendering <a id="c4d.BaseDraw-method-Object-And-Batch-Rendering"></a>

#### `BaseDraw.AddToPostPass(self, op, bh)` <a id="c4d.BaseDraw.AddToPostPass"></a>

Adds the object *op* to *DRAWPASS_XRAY*.

```python
def Draw(self, op, drawpass, bd, bh):
    if drawpass == c4d.DRAWPASS_OBJECT:
        bd.AddToPostPass(op, bh)
        ok = True
    elif drawpass == c4d.DRAWPASS_XRAY:
        ok = True

    if not ok:
        return c4d.DRAWRESULT_OK
```

The object in this example is drawn both in regular and X-ray passes.

> **Note:** This example is only relevant to [`ObjectData`](../../../../../../c4d.plugins/BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData) plugins.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../BaseObject/index.md#c4d.BaseObject)) – The object to add to the X-ray pass.
- **bh** ([*c4d.plugins.BaseDrawHelp*](../../../../../../c4d.plugins/BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp)) – The current base draw helper.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `BaseDraw.DrawArrayEnd(self)` <a id="c4d.BaseDraw.DrawArrayEnd"></a>

Each [`DrawPolygon()`](#c4d.BaseDraw.DrawPolygon) puts the polygon into an internal array and draws the polygons when the array is full or an Viewport state changes (e.g. the matrix). With this method you can force this operation.

#### `BaseDraw.DrawObject(self, bh, op, flags, drawpass, parent, col=<_custom_c4d.Vector object at 0x0000012EC5D555E0>)` <a id="c4d.BaseDraw.DrawObject"></a>

Draws a polygon object into the view.

**Parameters:**

- **bh** ([*c4d.plugins.BaseDrawHelp*](../../../../../../c4d.plugins/BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp)) – Needs to be passed along.

- **op** ([*c4d.BaseObject*](../../BaseObject/index.md#c4d.BaseObject)) – The object.

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *DRAWOBJECT_NONE* | None. |
  | *DRAWOBJECT_FORCELINES* | Force wireframe display, independent of view settings. |
  | *DRAWOBJECT_NOBACKCULL* | Force no backface culling, independent of view settings. |
  | *DRAWOBJECT_LOCALMATRIX* | Object will be drawn relative to the currently processed object (used when called from the *Draw()* function in an object. |
  | *DRAWOBJECT_EDITMODE* | Object is drawn in edit-mode style. |
  | *DRAWOBJECT_FORCEBASE* | The draw call is only executed for the base class, and thus not for the instanciated object, if passed to `BaseDraw.DrawObject()` and the object type is an instance of either *Opoint* or *Opolygon*. This way, a draw call can be invoked from points/polygons derived object without running into a recursion. |
  | *DRAWOBJECT_FORCEPOINTS* | Force points display. |
  | *DRAWOBJECT_NO_EOGL* | No Extended OpenGL. |
  | *DRAWOBJECT_USE_OBJECT_COLOR* | Use the object’s color. |
  | *DRAWOBJECT_USE_CUSTOM_COLOR* | Use a custom color. |
  | *DRAWOBJECT_XRAY_ON* | Enables X-Ray mode. |
  | *DRAWOBJECT_XRAY_OFF* | Disables X-Ray mode. |
  | *DRAWOBJECT_IMMEDIATELY* | Draws an object immediately. Usually all objects are collected in a Z-depth sorted list before drawing. This flag is used for objects which are immediately deleted after drawing. |
  | *DRAWOBJECT_Z_OFFSET* | Do not change the Z offset. |
  | *DRAWOBJECT_PRIVATE_ANY* | Private. |

- **drawpass** (*int*) –

  Drawpass:

  |   |   |
  |---|---|
  | *DRAWPASS_OBJECT* | Object pass. |
  | *DRAWPASS_BOX* | Box pass. |
  | *DRAWPASS_HANDLES* | Handle pass. |
  | *DRAWPASS_HIGHLIGHTS* | Highlights pass. |
  | *DRAWPASS_XRAY* | X-Ray pass. |

- **parent** (*Optional*[[*c4d.BaseObject*](../../BaseObject/index.md#c4d.BaseObject)]) – The parent object, can be **None**.

- **col** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) –

  *New in version R21.*

  The object’s color.

#### `BaseDraw.DrawPolygonObject(self, bh, op, flags, parent=None, col=<_custom_c4d.Vector object at 0x0000012EC5D4FEE0>)` <a id="c4d.BaseDraw.DrawPolygonObject"></a>

Draws a polygon object into the view.

**Parameters:**

- **bh** ([*c4d.plugins.BaseDrawHelp*](../../../../../../c4d.plugins/BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp)) – Needs to be passed along.

- **op** ([*c4d.BaseObject*](../../BaseObject/index.md#c4d.BaseObject)) – The object.

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *DRAWOBJECT_NONE* | None. |
  | *DRAWOBJECT_FORCELINES* | Force wireframe display, independent of view settings. |
  | *DRAWOBJECT_NOBACKCULL* | Force no backface culling, independent of view settings. |
  | *DRAWOBJECT_LOCALMATRIX* | Object will be drawn relative to the currently processed object (used when called from the *Draw()* function in an object. |
  | *DRAWOBJECT_EDITMODE* | Object is drawn in edit-mode style. |
  | *DRAWOBJECT_FORCEBASE* | The draw call is only executed for the base class, and thus not for the instanciated object, if passed to `BaseDraw.DrawObject()` and the object type is an instance of either *Opoint* or *Opolygon*. This way, a draw call can be invoked from points/polygons derived object without running into a recursion. |
  | *DRAWOBJECT_FORCEPOINTS* | Force points display. |
  | *DRAWOBJECT_NO_EOGL* | No Extended OpenGL. |
  | *DRAWOBJECT_USE_OBJECT_COLOR* | Use the object’s color. |
  | *DRAWOBJECT_USE_CUSTOM_COLOR* | Use a custom color. |
  | *DRAWOBJECT_XRAY_ON* | Enables X-Ray mode. |
  | *DRAWOBJECT_XRAY_OFF* | Disables X-Ray mode. |
  | *DRAWOBJECT_IMMEDIATELY* | Draws an object immediately. Usually all objects are collected in a Z-depth sorted list before drawing. This flag is used for objects which are immediately deleted after drawing. |
  | *DRAWOBJECT_Z_OFFSET* | Do not change the Z offset. |
  | *DRAWOBJECT_PRIVATE_ANY* | Private. |

- **parent** (*Optional*[[*c4d.BaseObject*](../../BaseObject/index.md#c4d.BaseObject)]) –

  *New in version R21.*

  This is used for the viewport filter.  
  Take the Floor object for example, it displays a polygon object in the viewport. If parent is set to **None** the drawn polygon is considered by the viewport filter.  
  If the Floor object has been passed to parent the Floor object is considered by the viewport filter instead.

- **col** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) –

  *New in version R21.*

  The object’s color.

### Operation Control <a id="c4d.BaseDraw-method-Operation-Control"></a>

#### `BaseDraw.DoUndo(self, doc)` <a id="c4d.BaseDraw.DoUndo"></a>

Performs an undo operation in the view.

> **Note:** This is the same as the user selecting Undo View from within Cinema 4D.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The view’s document.

#### `BaseDraw.InitUndo(self, doc)` <a id="c4d.BaseDraw.InitUndo"></a>

Called before a change is made to the view to add the old setting to the undo buffer for the view.

> **Note:** This undo buffer is separate from the normal undo buffer.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The view’s document.

#### `BaseDraw.TestBreak(self)` <a id="c4d.BaseDraw.TestBreak"></a>

Checks for thread breaks in the draw.

**Return type:** bool

**Returns:** **True** if a stopping condition has occurred, otherwise *False*.

### Parameter Access <a id="c4d.BaseDraw-method-Parameter-Access"></a>

#### `BaseDraw.GetDrawParam(self, id)` <a id="c4d.BaseDraw.GetDrawParam"></a>

Gets draw parameters.

**Parameters:** **id** (*int*) – Parameter ID.

**Return type:** Any

**Returns:** Depends on the parameter ID.

#### `BaseDraw.GetParameterData(self, id)` <a id="c4d.BaseDraw.GetParameterData"></a>

Get a new parameter object.

**Parameters:** **id** (*int*) – A parameter ID. See the `dbasedraw.h` description file.

**Return type:** Any

**Returns:** The parameter data for *id*. The type depends on the *id*.

#### `BaseDraw.SetDrawParam(self, id, data)` <a id="c4d.BaseDraw.SetDrawParam"></a>

Sets draw parameters.

> **Note:** The coordinates must be in the space defined by [`SetMatrix_Screen()`](#c4d.BaseDraw.SetMatrix_Screen), [`SetMatrix_Camera()`](#c4d.BaseDraw.SetMatrix_Camera) or [`SetMatrix_Matrix()`](#c4d.BaseDraw.SetMatrix_Matrix).

**Parameters:**

- **id** (*int*) – Parameter ID.
- **data** (*any*) – Depends on the parameter ID.

### Point And Handle Drawing <a id="c4d.BaseDraw-method-Point-And-Handle-Drawing"></a>

#### `BaseDraw.DrawHandle(self, vp, type, flags)` <a id="c4d.BaseDraw.DrawHandle"></a>

Draws a standard handle (orange dot) at *vp*.  
The coordinates must be in world space.

**Parameters:**

- **vp** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – A point.

- **type** (*int*) –

  The handle type. Valid types are:

  |   |   |
  |---|---|
  | *DRAWHANDLE_MINI* | Tiny point. |
  | *DRAWHANDLE_SMALL* | Small point. |
  | *DRAWHANDLE_MIDDLE* | Medium point. |
  | *DRAWHANDLE_BIG* | Big point. Handle used by object generators and deformers. |
  | *DRAWHANDLE_CUSTOM* | Custom handle. |
  | *DRAWHANDLE_POINTSIZE* | Use the point size to draw the handle. |
  | *DRAWHANDLE_SELPOINTSIZE* | Use the size of selected points to draw the handle. |

- **flags** (*int*) – Private, set to *0*.

#### `BaseDraw.DrawHandle2D(self, p, type=1)` <a id="c4d.BaseDraw.DrawHandle2D"></a>

Draws a standard handle (orange dot) at *p*.  
The coordinates must be in screen space.

> **Note:** Changes the matrix to screen with [`SetMatrix_Screen()`](#c4d.BaseDraw.SetMatrix_Screen) prior to drawing.

**Parameters:**

- **p** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – A point.

- **type** (*int*) –

  The handle type. Possible values are:

  |   |   |
  |---|---|
  | *DRAWHANDLE_MINI* | Tiny point. |
  | *DRAWHANDLE_SMALL* | Small point. |
  | *DRAWHANDLE_MIDDLE* | Medium point. |
  | *DRAWHANDLE_BIG* | Big point. Handle used by object generators and deformers. |
  | *DRAWHANDLE_CUSTOM* | Custom handle. |
  | *DRAWHANDLE_POINTSIZE* | Use the point size to draw the handle. |
  | *DRAWHANDLE_SELPOINTSIZE* | Use the size of selected points to draw the handle. |

#### `BaseDraw.DrawPoint2D(self, p)` <a id="c4d.BaseDraw.DrawPoint2D"></a>

Draws a one-pixel point in the current pen color at p.  
The coordinates must be in screen space.

> **Note:** Changes the matrix to screen with [`SetMatrix_Screen()`](#c4d.BaseDraw.SetMatrix_Screen) prior to drawing.

**Parameters:** **p** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – A point.

#### `BaseDraw.DrawPoints(self, vp, vc, colcnt=0, vn=None)` <a id="c4d.BaseDraw.DrawPoints"></a>

Draws an array of points with individual colors.

> **Note:** The coordinates must be in the space defined by [`SetMatrix_Screen()`](#c4d.BaseDraw.SetMatrix_Screen), [`SetMatrix_Camera()`](#c4d.BaseDraw.SetMatrix_Camera) or [`SetMatrix_Matrix()`](#c4d.BaseDraw.SetMatrix_Matrix).

**Parameters:**

- **vp** (*any*) – An iteratable object with [`Vector`](../../../../../Vector/index.md#c4d.Vector) as elements for the point coordinates.

- **vc** (*Optional*[*any*]) –

  An iteratable object with floats as elements for the points color.

  *Changed in version R18.057.*

  Can be **None**.

- **colcnt** (*int*) – The number of color elements, for example 3 for RGB.

- **vn** (*Optional*[*any*]) –

  Reserved for future use.

  *Changed in version R18.057.*

  Can be **None**.

### Shape Rendering <a id="c4d.BaseDraw-method-Shape-Rendering"></a>

#### `BaseDraw.DrawBox(self, m, size, col, wire)` <a id="c4d.BaseDraw.DrawBox"></a>

Draws a box.  
The eight points of the box are defined as:

```python
p = [c4d.Vector() for x in range(8)]
p[0] = c4d.Vector(-size, -size, -size)
p[1] = c4d.Vector( size, -size, -size)
p[2] = c4d.Vector( size, -size,  size)
p[3] = c4d.Vector(-size, -size,  size)
p[4] = c4d.Vector(-size,  size, -size)
p[5] = c4d.Vector( size,  size, -size)
p[6] = c4d.Vector( size,  size,  size)
p[7] = c4d.Vector(-size,  size,  size)
```

To get arbitrary cubic forms, set size to 0.5 and multiply the vectors in the matrix by the length.

> **Note:** The coordinates must be in the space defined by [`SetMatrix_Screen()`](#c4d.BaseDraw.SetMatrix_Screen), [`SetMatrix_Camera()`](#c4d.BaseDraw.SetMatrix_Camera) or [`SetMatrix_Matrix()`](#c4d.BaseDraw.SetMatrix_Matrix).

**Parameters:**

- **m** ([*c4d.Matrix*](../../../../../Matrix/index.md#c4d.Matrix)) – A matrix describing the box.
- **size** (*float*) – The size of the box.
- **col** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The color of the box.
- **wire** (*bool*) – If this is **True** a wireframe is drawn.

#### `BaseDraw.DrawPolygon(self, p, f)` <a id="c4d.BaseDraw.DrawPolygon"></a>

Draws a manually shaded triangle or quadrangle.  
The corner points are given as a list of Vectors in *p*, and the corner colors as a corresponding list of Vectors in *f*.

```python
p = ( c4d.Vector(0,0,0), c4d.Vector(100,0,0), c4d.Vector(50,100,0) )
f = ( c4d.Vector(1,0,0), c4d.Vector(0,0,1), c4d.Vector(0,1,0) )
bd.DrawPolygon(p, f)
```

> **Note:** The coordinates must be in the space defined by [`SetMatrix_Screen()`](#c4d.BaseDraw.SetMatrix_Screen), [`SetMatrix_Camera()`](#c4d.BaseDraw.SetMatrix_Camera) or [`SetMatrix_Matrix()`](#c4d.BaseDraw.SetMatrix_Matrix).

**Parameters:**

- **p** (*List*[[*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)]) – A list of points.
- **f** (*List*[[*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)]) – A list of points.

#### `BaseDraw.DrawSphere(self, off, size, col, flags)` <a id="c4d.BaseDraw.DrawSphere"></a>

Draws a sphere at position off with size specified by the size vector in each direction and color specified by col.

> **Note:** The coordinates must be in the space defined by [`SetMatrix_Screen()`](#c4d.BaseDraw.SetMatrix_Screen), [`SetMatrix_Camera()`](#c4d.BaseDraw.SetMatrix_Camera) or [`SetMatrix_Matrix()`](#c4d.BaseDraw.SetMatrix_Matrix).

**Parameters:**

- **off** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – Position coordinate.

- **size** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – Sphere size.

- **col** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – The color.

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *NOCLIP_D* | Clip against the view border. |
  | *NOCLIP_Z* | Z clipping. |

### Texture And Lighting <a id="c4d.BaseDraw-method-Texture-And-Lighting"></a>

#### `BaseDraw.DrawTexture(self, bmp, padr4, cadr, vnadr, uvadr, pntcnt, alphamode, flags)` <a id="c4d.BaseDraw.DrawTexture"></a>

Draws a colored and shaded texture polygon using the points in *padr4*, the colors in *cadr*, the normals in *vnadr* and the UV coordinates in *uvadr*.  
Only a triangle or a quadrangle is accepted.  
The colors are interpolated between the points and mutiplied with the texture color.  
The shading is determined by [`SetLightList()`](#c4d.BaseDraw.SetLightList).

> **Note:** The coordinates must be in the space defined by [`SetMatrix_Screen()`](#c4d.BaseDraw.SetMatrix_Screen), [`SetMatrix_Camera()`](#c4d.BaseDraw.SetMatrix_Camera) or [`SetMatrix_Matrix()`](#c4d.BaseDraw.SetMatrix_Matrix).

> **Note:** Due to Python object live time limitation, the flags DRAW_TEXTUREFLAGS_TEMPORARY is always set.

**Parameters:**

- **bmp** ([*c4d.bitmaps.BaseBitmap*](../../../../../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The texture to draw.

- **padr4** (*List*[[*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)]) – An iteratable object with [`Vector`](../../../../../Vector/index.md#c4d.Vector) as elements for the points coordinates.

- **cadr** (*List*[[*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)]) – An iteratable object with [`Vector`](../../../../../Vector/index.md#c4d.Vector) as elements for the colors. Must have *4* items regardless of *pntcnt*.

- **vnadr** (*List*[[*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)]) – An iteratable object with [`Vector`](../../../../../Vector/index.md#c4d.Vector) as elements for the point normals. Must have *4* items regardless of *pntcnt*.

- **uvadr** (*List*[[*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)]) – An iteratable object with [`Vector`](../../../../../Vector/index.md#c4d.Vector) as elements for the UV coordinates. Must have *4* items regardless of *pntcnt*.

- **pntcnt** (*int*) – The number of points in *padr4*. Must be either *3* (triangle) or *4* (quadrangle).

- **alphamode** (*int*) –

  The alpha channel mode:

  |   |   |
  |---|---|
  | *DRAW_ALPHA_NONE* | No alpha. |
  | *DRAW_ALPHA_INVERTED* | Generates inverted alpha. |
  | *DRAW_ALPHA_NORMAL* | Generates alpha channel from the image’s alpha channel. If no alpha channel exists, the alpha value is set to *100%*. |
  | *DRAW_ALPHA_FROM_IMAGE* | Generates the alpha channel from the RGB image information. |
  | *DRAW_ALPHA_NORMAL_FROM_IMAGE* | Generates the alpha channel from the image’s alpha channel. If no alpha channel exists, the alpha value is generated from the RGB image. |

- **flags** (*int*) –

  A combination of these flags:

  |   |   |
  |---|---|
  | *DRAW_TEXTUREFLAGS_NONE* | None. |
  | *DRAW_TEXTUREFLAGS_COLOR_IMAGE_TO_LINEAR* | Converts the embedded color profile to linear color space. |
  | *DRAW_TEXTUREFLAGS_COLOR_SRGV_TO_LINEAR* | Converts from sRGB color space to linear color space. |
  | *DRAW_TEXTUREFLAGS_IMAGE_TO_SRGB* | Converts the embedded color profile to sRGB color space. |
  | *DRAW_TEXTUREFLAGS_COLOR_LINEAR_TO_SRGB* | Converts from linear color space to sRGB color space. |
  | *DRAW_TEXTUREFLAGS_COLOR_CORRECTION_MASK* | Color correction mask. |
  | *DRAW_TEXTUREFLAGS_USE_PROFILE_COLOR* | Use profile color. |
  | *DRAW_TEXTUREFLAGS_ALLOW_FLOATINGPOINT* | Allow floating point textures (if supported). |
  | *DRAW_TEXTUREFLAGS_TILE* | Allow tiling. |
  | *DRAW_TEXTUREFLAGS_TEMPORARY* | Texture is a temporary object. |
  | *DRAW_TEXTUREFLAGS_INTERPOLATION_NEAREST* | Nearest texture interpolation. |
  | *DRAW_TEXTUREFLAGS_INTERPOLATION_LINEAR* | Linear texture interpolation. |
  | *DRAW_TEXTUREFLAGS_INTERPOLATION_LINEAR_MIPMAP* | MIP map texture interpolation. |
  | *DRAW_TEXTUREFLAGS_INTERPOLATION_MASK* | Texture interpolation mask. |

#### `BaseDraw.SetLightList(self, mode)` <a id="c4d.BaseDraw.SetLightList"></a>

Sets the lighting used by the draw functions.

> **Note:** The coordinates must be in the space defined by [`SetMatrix_Screen()`](#c4d.BaseDraw.SetMatrix_Screen), [`SetMatrix_Camera()`](#c4d.BaseDraw.SetMatrix_Camera) or [`SetMatrix_Matrix()`](#c4d.BaseDraw.SetMatrix_Matrix).

> **Note:** This method only affects the new 3D drawing methods, i.e. [`DrawLine()`](#c4d.BaseDraw.DrawLine), [`DrawHandle()`](#c4d.BaseDraw.DrawHandle), [`DrawTexture()`](#c4d.BaseDraw.DrawTexture), [`DrawCircle()`](#c4d.BaseDraw.DrawCircle), [`DrawBox()`](#c4d.BaseDraw.DrawBox), [`DrawPolygon()`](#c4d.BaseDraw.DrawPolygon) and [`DrawSphere()`](#c4d.BaseDraw.DrawSphere).

**Parameters:**

**mode** (*int*) –

The lighting mode:

|   |   |
|---|---|
| *BDRAW_SETLIGHTLIST_NOLIGHTS* | No lights. |
| *BDRAW_SETLIGHTLIST_SCENELIGHTS* | Scene lights. |
| *BDRAW_SETLIGHTLIST_QUICKSHADING* | Quick shading. |

**Return type:** bool

**Returns:** **True** on success, otherwise **False**.

#### `BaseDraw.SetTexture(self, bm, tile, alphamode, flags)` <a id="c4d.BaseDraw.SetTexture"></a>

Set a texture used by the vertex buffer.

**Parameters:**

- **bm** ([*c4d.bitmaps.BaseBitmap*](../../../../../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)) – The texture’s bitmap.

- **tile** (*bool*) – Enable tiling.

- **alphamode** (*int*) –

  Alpha channel mode:

  |   |   |
  |---|---|
  | *DRAW_ALPHA_NONE* | No alpha. |
  | *DRAW_ALPHA_INVERTED* | Generates inverted alpha. |
  | *DRAW_ALPHA_NORMAL* | Generates alpha channel from the image’s alpha channel. If no alpha channel exists, the alpha value is set to *100%*. |
  | *DRAW_ALPHA_FROM_IMAGE* | Generates the alpha channel from the RGB image information. |
  | *DRAW_ALPHA_NORMAL_FROM_IMAGE* | Generates the alpha channel from the image’s alpha channel. If no alpha channel exists, the alpha value is generated from the RGB image. |

- **flags** (*int*) – Private, set to *0*.

### Transparency Control <a id="c4d.BaseDraw-method-Transparency-Control"></a>

#### `BaseDraw.GetTransparency(self)` <a id="c4d.BaseDraw.GetTransparency"></a>

Returns the current transparency value for polygons.  
The range is 0 to 255, where 255 is 100% transparent.

> **Note:** Negative values are true transparencies and positive values are ‘dotted’ transparencies.

**Return type:** int

**Returns:** The transparency.

#### `BaseDraw.SetTransparency(self, trans)` <a id="c4d.BaseDraw.SetTransparency"></a>

Sets the transparency value for following polygons.  
The range is 0 to 255, where 255 is 100% transparent.

> **Note:** Use negative values for true transparencies and positive values for ‘dotted’ transparencies.

**Parameters:** **trans** (*int*) – The transparency.

### View Initialization <a id="c4d.BaseDraw-method-View-Initialization"></a>

#### `BaseDraw.InitClipbox(self, left, top, right, bottom, flags)` <a id="c4d.BaseDraw.InitClipbox"></a>

Used to render into a framebuffer with different resolution than the editor view.

**Parameters:**

- **left** (*int*) – Left coordinate of the framebuffer.

- **top** (*int*) – Top coordinate of the framebuffer.

- **right** (*int*) – Right coordinate of the framebuffer.

- **bottom** (*int*) – Bottom coordinate of the framebuffer.

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *INIT_CLIPBOX_ADJUSTGLSIZE* | Adjust the size of the frame buffer. |

#### `BaseDraw.InitializeView(self, doc, cam, editorsv)` <a id="c4d.BaseDraw.InitializeView"></a>

Used after rendering into a framebuffer with different resolution than the editor view.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The view’s document.
- **cam** ([*c4d.BaseObject*](../../BaseObject/index.md#c4d.BaseObject)) – The view’s camera.
- **editorsv** (*bool*) – Set this **True** to retain the view’s ratio.

#### `BaseDraw.InitView(self, camera, op_m, sv, pix_x, pix_y, fitview)` <a id="c4d.BaseDraw.InitView"></a>

Used to render into a framebuffer with different resolution than the editor view.

**Parameters:**

- **camera** ([*c4d.BaseContainer*](../../../../../BaseContainer/index.md#c4d.BaseContainer)) – The camera’s container.
- **op_m** ([*c4d.Matrix*](../../../../../Matrix/index.md#c4d.Matrix)) – The camera’s matrix.
- **sv** (*float*) – The frame’s ratio.
- **pix_x** (*float*) – The frame’s X size.
- **pix_y** (*float*) – The frame’s Y size.
- **fitview** (*bool*) – Set this to True to fit the view.

### Viewport State And Interaction <a id="c4d.BaseDraw-method-Viewport-State-And-Interaction"></a>

#### `BaseDraw.GetDisplayFilter(self)` <a id="c4d.BaseDraw.GetDisplayFilter"></a>

Returns the current display filter.  
This is a bit field derived from the *DISPLAYFILTER* values.

> **Note:** To set the display filter use the description flags with `GeListNode.__setitem__()` or `C4DAtom.SetParameter()`.

For instance the following script switches the Filter “Subdivision Surface”.

```python
bd = doc.GetActiveBaseDraw()
displayFilter = bd.GetDisplayFilter()

if displayFilter & c4d.DISPLAYFILTER_HYPERNURBS:
    bd[c4d.DISPLAYFILTER_HYPERNURBS] = False
    print("Switched Off Subdivision Surface Display Filter")
else:
    bd[c4d.DISPLAYFILTER_HYPERNURBS] = True
    print("Switched On Subdivision Surface Display Filter")

bd.Message(c4d.MSG_CHANGE)
c4d.EventAdd()
```

Note the difference between the filters “Subdivision Surface” and “SDS Mesh”.

**Return type:** int

**Returns:**

A bit field with the following flags:

| DISPLAYFILTER_NONE | None. |
|---|---|
| DISPLAYFILTER_NULLOBJECT | Null. |
| DISPLAYFILTER_POLYGON | Polygon. |
| DISPLAYFILTER_SPLINE | Spline. |
| DISPLAYFILTER_GENERATOR | Generator. |
| DISPLAYFILTER_HYPERNURBS | Subdivision Surface. |
| DISPLAYFILTER_UNUSED1 | Unused. |
| DISPLAYFILTER_DEFORMER | Deformer. |
| DISPLAYFILTER_CAMERA | Camera. |
| DISPLAYFILTER_LIGHT | Light. |
| DISPLAYFILTER_SCENE | Scene. |
| DISPLAYFILTER_PARTICLE | Particle. |
| DISPLAYFILTER_OTHER | Other. |
| DISPLAYFILTER_UNUSED2 | *New in version S22:* Unused. |
| DISPLAYFILTER_GRID | Grid. |
| DISPLAYFILTER_HORIZON | Horizon. |
| DISPLAYFILTER_WORLDAXIS | World axis. |
| DISPLAYFILTER_BOUNDS | Bounding-box. |
| DISPLAYFILTER_HUD | HUD. |
| DISPLAYFILTER_SDS | HN mesh. |
| DISPLAYFILTER_HIGHLIGHTING | Highlighting. |
| DISPLAYFILTER_MULTIAXIS | Multi-select axis. |
| DISPLAYFILTER_OBJECTHANDLES | Highlight handles. |
| DISPLAYFILTER_HANDLEBANDS | Axis bands. |
| DISPLAYFILTER_SDSCAGE | HN cage. |
| DISPLAYFILTER_NGONLINES | N-gon lines. |
| DISPLAYFILTER_JOINT | Joint objects. |
| DISPLAYFILTER_OBJECTHIGHLIGHTING | Private. |
| DISPLAYFILTER_GUIDELINES | Axis Guidelines. |
| DISPLAYFILTER_POI | Navigation cross. |
| DISPLAYFILTER_GRADIENT | Gradient. |
| DISPLAYFILTER_BASEGRID | Base grid. |
| DISPLAYFILTER_HANDLES | Handles. |
| DISPLAYFILTER_HAIR | *New in version S22:* Hair. |
| DISPLAYFILTER_FIELD | *New in version S22:* Field. |

#### `BaseDraw.GetDrawPass(self)` <a id="c4d.BaseDraw.GetDrawPass"></a>

Gets the current drawpass.

*New in version R14.041.*

**Return type:** int

**Returns:**

One of the following flags:

|   |   |
|---|---|
| *DRAWPASS_OBJECT* | Object pass. |
| *DRAWPASS_BOX* | Box pass. |
| *DRAWPASS_HANDLES* | Handle pass. |
| *DRAWPASS_HIGHLIGHTS* | Highlights pass. |
| *DRAWPASS_XRAY* | X-Ray pass. |

#### `BaseDraw.GetEditorWindow(self)` <a id="c4d.BaseDraw.GetEditorWindow"></a>

Get the editor window of the BaseDraw.

**Return type:** [c4d.gui.EditorWindow](../../../../../../c4d.gui/EditorWindow/index.md#c4d.gui.EditorWindow)

**Returns:** The editor window of the base draw.

#### `BaseDraw.GetEditState(self)` <a id="c4d.BaseDraw.GetEditState"></a>

Get the edit state. This is a bit field derived from the edit state description flags in *dbasedraw.h*.

> **Note:** To set the display filter use the description flags with `GeListNode.__setitem__()` or `C4DAtom.SetParameter()`.

**Return type:** int

**Returns:**

A bit field with the following flags:

|   |   |
|---|---|
| *DISPLAYEDITSTATE_NONE* | None. |
| *DISPLAYEDITSTATE_SDS* | SDS edit state. |
| *DISPLAYEDITSTATE_DEFORM* | Deformed edit state. |
| *DISPLAYEDITSTATE_DOCUMENT* | Document edit state. |

#### `BaseDraw.GetFrameScreen(self)` <a id="c4d.BaseDraw.GetFrameScreen"></a>

Used in the Extended GL mode. This mode is not documented. See `c4d_gl.h` for definitions.

**Return type:** Optional[Dict[**cl**: int, **ct**: int, **cr**: int, **cb**: int, **windowScale**: float]]

**Returns:** A dict or **None**.

#### `BaseDraw.GetGridStep(self)` <a id="c4d.BaseDraw.GetGridStep"></a>

Gets the grid spacing and the transparency value of the minor grid that fade when the user zoom in or out with dynamic grid.

*New in version R14.014.*

**Return type:** Tuple[float, float]

**Returns:** The workplane grid spacing and the transparency value of the minor grid.

#### `BaseDraw.GetReductionMode(self)` <a id="c4d.BaseDraw.GetReductionMode"></a>

Gets the reduction mode of the base draw.

**Return type:** bool

**Returns:** **True** on success, otherwise **False**.

#### `BaseDraw.IsViewOpen(self, doc)` <a id="c4d.BaseDraw.IsViewOpen"></a>

Checks if the current tool can use the current SDS/Deformed editing state.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The current document.

**Return type:** bool

**Returns:** **True** if the view is open, otherwise **False**.

#### `BaseDraw.PointInRange(self, p, x, y)` <a id="c4d.BaseDraw.PointInRange"></a>

Returns **True** if the screen point (x,y) is within a hit range of the world point p, i.e. if the screen point is close to the world points projection on the screen.

**Parameters:**

- **p** ([*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)) – A point in world space.
- **x** (*int*) – Screen x coordinate.
- **y** (*int*) – Screen y coordinate.

**Return type:** bool

**Returns:** **True** if the point is within range, otherwise **True**.
