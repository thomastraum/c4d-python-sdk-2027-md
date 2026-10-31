<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/sculpting/BrushDabData/index.html -->

# c4d.modules.sculpting.BrushDabData <a id="c4d-modules-sculpting-brushdabdata"></a>

## *class* `c4d.modules.sculpting.BrushDabData` <a id="c4d.modules.sculpting.BrushDabData"></a>

The brush data for an individual dab.

*New in version R16.021.*

## Overview <a id="overview"></a>

**Affected Geometry**

- [`BrushDabData.GetNeighbor()`](#c4d.modules.sculpting.BrushDabData.GetNeighbor): Gets the neighbor information for the Sculpt Object if it is currently at level *0*.
- [`BrushDabData.GetPointCount()`](#c4d.modules.sculpting.BrushDabData.GetPointCount): Gets the number of points that are touched by the dab.
- [`BrushDabData.GetPointData()`](#c4d.modules.sculpting.BrushDabData.GetPointData): Gets the point at *index* affected by the brush.
- [`BrushDabData.GetPolyCount()`](#c4d.modules.sculpting.BrushDabData.GetPolyCount): Gets the number of polygons that are touched by the dab.
- [`BrushDabData.GetPolyData()`](#c4d.modules.sculpting.BrushDabData.GetPolyData): Gets the polygon at *index* affected by the brush.

**Brush Influence**

- [`BrushDabData.GetAutoScaleValue()`](#c4d.modules.sculpting.BrushDabData.GetAutoScaleValue): Returns a value which represents the scale of the Sculpt Object.
- [`BrushDabData.GetBrushFalloff()`](#c4d.modules.sculpting.BrushDabData.GetBrushFalloff): Returns the brush falloff for the point specified by the *index* value.
- [`BrushDabData.GetBrushFalloffFromPos()`](#c4d.modules.sculpting.BrushDabData.GetBrushFalloffFromPos): Returns the falloff value, defined by the falloff curve, based on the distance from *pos* to the hitpoint for the dab.
- [`BrushDabData.GetBrushRadius()`](#c4d.modules.sculpting.BrushDabData.GetBrushRadius): Gets the brush radius for the dab.
- [`BrushDabData.GetBrushStrength()`](#c4d.modules.sculpting.BrushDabData.GetBrushStrength): Gets the brush strength for the dab.

**Dab State**

- [`BrushDabData.GetBrushOverride()`](#c4d.modules.sculpting.BrushDabData.GetBrushOverride): Gets the override flags.
- [`BrushDabData.GetStrokeInstanceID()`](#c4d.modules.sculpting.BrushDabData.GetStrokeInstanceID): Gets the ID of the stroke instance that this dab is being drawn for.
- [`BrushDabData.IsBackface()`](#c4d.modules.sculpting.BrushDabData.IsBackface): Returns **True** if the dab is being applied backfacing polygons.
- [`BrushDabData.IsFillTool()`](#c4d.modules.sculpting.BrushDabData.IsFillTool): Checks if the current draw mode is fill.
- [`BrushDabData.IsPreviewDab()`](#c4d.modules.sculpting.BrushDabData.IsPreviewDab): Checks if this is a preview dab.

**Drawing Context**

- [`BrushDabData.GetBaseDraw()`](#c4d.modules.sculpting.BrushDabData.GetBaseDraw): Gets the [`BaseDraw`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw) that the user is currently drawing in.
- [`BrushDabData.GetData()`](#c4d.modules.sculpting.BrushDabData.GetData): Gets the settings data for the tool.

**Hit And Cursor Position**

- [`BrushDabData.GetEyePoint()`](#c4d.modules.sculpting.BrushDabData.GetEyePoint): Gets the location of the mouse in local space above the model.
- [`BrushDabData.GetHitPoint()`](#c4d.modules.sculpting.BrushDabData.GetHitPoint): Gets the point on the surface of the SculptObject where the dab is going to be placed.
- [`BrushDabData.GetHitPolygon()`](#c4d.modules.sculpting.BrushDabData.GetHitPolygon): Gets the index of the polygon on the surface of the SculptObject where the dab is going to be placed.
- [`BrushDabData.GetLastHitPoint()`](#c4d.modules.sculpting.BrushDabData.GetLastHitPoint): Gets the hit point for the previous dab during the stroke.
- [`BrushDabData.GetMousePos3D()`](#c4d.modules.sculpting.BrushDabData.GetMousePos3D): If the brush mode is *SCULPTBRUSHMODE_GRAB* then this method can be used to get the location of the mouse pointer in world space in the scene.

**Layer And Point Access**

- [`BrushDabData.GetLayer()`](#c4d.modules.sculpting.BrushDabData.GetLayer): Retrieves the currently selected Layer for a subdivided [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject).
- [`BrushDabData.GetOriginalPoint()`](#c4d.modules.sculpting.BrushDabData.GetOriginalPoint): Retrieves a copy of the point at *index* in its state before the brush stroke started.
- [`BrushDabData.GetPoint()`](#c4d.modules.sculpting.BrushDabData.GetPoint): Retrieves the live point at *index* that is modified on the surface during a brush stroke.
- [`BrushDabData.OffsetPoint()`](#c4d.modules.sculpting.BrushDabData.OffsetPoint): Offsets the point on the layer by the given *offset* amount.
- [`BrushDabData.OffsetPreviewPoint()`](#c4d.modules.sculpting.BrushDabData.OffsetPreviewPoint): If `IsPreviewDab()` returns **True** then you should apply your offset using this method.

**Object Context**

- [`BrushDabData.GetBaseObject()`](#c4d.modules.sculpting.BrushDabData.GetBaseObject): Gets the original object that the Sculpt Tag is applied to.
- [`BrushDabData.GetObject()`](#c4d.modules.sculpting.BrushDabData.GetObject): Gets the Sculpt Object that the dab is for.
- [`BrushDabData.GetPolygonObject()`](#c4d.modules.sculpting.BrushDabData.GetPolygonObject): Gets the Polygon Object for the Sculpt Object that is currently being displayed in the viewport.
- [`BrushDabData.IsSculptObject()`](#c4d.modules.sculpting.BrushDabData.IsSculptObject): Checks if the object being touched is a [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject) (i.e.

**Point Editing**

- [`BrushDabData.ApplySmooth()`](#c4d.modules.sculpting.BrushDabData.ApplySmooth): Applies an effect of the smooth brush to the current dab.
- [`BrushDabData.DirtyAllPoints()`](#c4d.modules.sculpting.BrushDabData.DirtyAllPoints): Dirty all the points for this dab according to the flags.
- [`BrushDabData.IsPointModified()`](#c4d.modules.sculpting.BrushDabData.IsPointModified): When using symmetry another mirrored brush may change the point.

**Stencil And Stamp**

- [`BrushDabData.GetStamp()`](#c4d.modules.sculpting.BrushDabData.GetStamp): Retreves the stamp bitmap used for this dab.
- [`BrushDabData.GetStampColor()`](#c4d.modules.sculpting.BrushDabData.GetStampColor): Retrieves the grey value, color and coordinates of the stamp for a point in the Sculpt Object local space.
- [`BrushDabData.GetStencil()`](#c4d.modules.sculpting.BrushDabData.GetStencil): Retrieves the stencil bitmap used for this dab.
- [`BrushDabData.GetStencilColor()`](#c4d.modules.sculpting.BrushDabData.GetStencilColor): Retrieves the grey value, color and coordinates of the stencil for a point in the Sculpt Object local space.

**Surface Normals**

- [`BrushDabData.GetAveragePointAndNormal()`](#c4d.modules.sculpting.BrushDabData.GetAveragePointAndNormal): Gets the average point and normal.
- [`BrushDabData.GetFaceNormal()`](#c4d.modules.sculpting.BrushDabData.GetFaceNormal): Gets the face normal at *index* for the SculptObject.
- [`BrushDabData.GetNormal()`](#c4d.modules.sculpting.BrushDabData.GetNormal): Gets the normal at the current hitpoint for the dab.
- [`BrushDabData.GetOriginalVertexNormal()`](#c4d.modules.sculpting.BrushDabData.GetOriginalVertexNormal): Gets the state of a vertex normal before the user started a brush stroke.
- [`BrushDabData.GetVertexNormal()`](#c4d.modules.sculpting.BrushDabData.GetVertexNormal): Gets the vertex normal at *index* for the Sculpt Object.

**Symmetry And Direction**

- [`BrushDabData.GetDrawDirectionNormal()`](#c4d.modules.sculpting.BrushDabData.GetDrawDirectionNormal): If the brush supports the Draw Direction, i.e.
- [`BrushDabData.GetMirrorPoint()`](#c4d.modules.sculpting.BrushDabData.GetMirrorPoint): Mirror the point (or Normal) from the objects space to the correct location for the current dab.
- [`BrushDabData.IsMirroredDab()`](#c4d.modules.sculpting.BrushDabData.IsMirroredDab): Checks if this dab is for a mirrored brush stroke.

## Members <a id="members"></a>

### Affected Geometry <a id="c4d.modules.sculpting.BrushDabData-method-Affected-Geometry"></a>

#### `BrushDabData.GetNeighbor(self)` <a id="c4d.modules.sculpting.BrushDabData.GetNeighbor"></a>

Gets the neighbor information for the Sculpt Object if it is currently at level *0*.

> **Note:** If the user is sculpting a regular unsubdivided Polygon Object then this will also return a neighbor information.

**Return type:** Optional[[c4d.utils.Neighbor](../../../c4d.utils/Neighbor/index.md#c4d.utils.Neighbor)]

**Returns:** The Neighbor information if Sculpt Object is at level *0* (or if the user is sculpting on a regular [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject)), otherwise **None**.

#### `BrushDabData.GetPointCount(self)` <a id="c4d.modules.sculpting.BrushDabData.GetPointCount"></a>

Gets the number of points that are touched by the dab.

**Return type:** int

**Returns:** The number of points.

#### `BrushDabData.GetPointData(self, index)` <a id="c4d.modules.sculpting.BrushDabData.GetPointData"></a>

Gets the point at *index* affected by the brush.

**Parameters:** **index** (*int*) – The index of the point.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.BrushDabData.GetPointCount).

**Return type:** dict{**pointIndex**: int, **distance**: float}

**Returns:** The point data index and distance.

#### `BrushDabData.GetPolyCount(self)` <a id="c4d.modules.sculpting.BrushDabData.GetPolyCount"></a>

Gets the number of polygons that are touched by the dab.

**Return type:** int

**Returns:** The number of polygons.

#### `BrushDabData.GetPolyData(self, index)` <a id="c4d.modules.sculpting.BrushDabData.GetPolyData"></a>

Gets the polygon at *index* affected by the brush.

**Parameters:** **index** (*int*) – The index of the polygon.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPolyCount()`](#c4d.modules.sculpting.BrushDabData.GetPolyCount).

**Return type:** dict{**polyIndex**: int, **distance**: float}

**Returns:** The polygon data index.

### Brush Influence <a id="c4d.modules.sculpting.BrushDabData-method-Brush-Influence"></a>

#### `BrushDabData.GetAutoScaleValue(self, noRadius)` <a id="c4d.modules.sculpting.BrushDabData.GetAutoScaleValue"></a>

Returns a value which represents the scale of the Sculpt Object.

> **Note:**
>
> This can be used to convert a distance in object space with the value returned from [`GetBrushRadius()`](#c4d.modules.sculpting.BrushDabData.GetBrushRadius) to help adjust  
> the algorithm for your brush since the value returned from [`GetBrushRadius()`](#c4d.modules.sculpting.BrushDabData.GetBrushRadius) is also already adjusted using the same value.

**Parameters:** **noRadius** (*bool*) – **True** means it will not take into account the radius of the object in its calculation and will only use the scale.

**Return type:** float

**Returns:** The scale value with which to adjust your local space vector or distance value.

#### `BrushDabData.GetBrushFalloff(self, index, customDistance=-1.0)` <a id="c4d.modules.sculpting.BrushDabData.GetBrushFalloff"></a>

Returns the brush falloff for the point specified by the *index* value.  
The falloff is already adjusted by using the values from the stamp and stencil so it can be used directly to adjust the strength of an offset that you wish to add to the layer.  
Internally this method will use the distance that this point is from the hitpoint in its calculation. Pass in a value to *customDistance* to use a different distance.

**Parameters:**

- **index** (*int*) – The point data index returned from [`GetPointData()`](#c4d.modules.sculpting.BrushDabData.GetPointData).
- **customDistance** (*float*) – The custom distance to use instead of the points actual distance from the hitpoint.

**Return type:** float

**Returns:** The final falloff value that can be used to adjust the offset value.

#### `BrushDabData.GetBrushFalloffFromPos(self, pos)` <a id="c4d.modules.sculpting.BrushDabData.GetBrushFalloffFromPos"></a>

Returns the falloff value, defined by the falloff curve, based on the distance from *pos* to the hitpoint for the dab.

**Parameters:** **pos** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – A point in 3D space to get the falloff for.

**Return type:** float

**Returns:** The falloff value.

#### `BrushDabData.GetBrushRadius(self)` <a id="c4d.modules.sculpting.BrushDabData.GetBrushRadius"></a>

Gets the brush radius for the dab. The size of the radius is in the Sculpt Object local space.

> **Warning:**
>
> This is not the same as the brush size in the [`BaseContainer`](../../../c4d/BaseContainer/index.md#c4d.BaseContainer) data.  
> This also takes into account other factors such as the distance from the camera and scale of the object and tablet values to determine the correct brush radius.

**Return type:** float

**Returns:** The radius of the brush.

#### `BrushDabData.GetBrushStrength(self)` <a id="c4d.modules.sculpting.BrushDabData.GetBrushStrength"></a>

Gets the brush strength for the dab.

> **Warning:**
>
> This strength is not the same as the strength in the [`BaseContainer`](../../../c4d/BaseContainer/index.md#c4d.BaseContainer) data.  
> This also takes into account many other variables including tablet pressure to create the value.

**Return type:** float

**Returns:** The strength of the brush.

### Dab State <a id="c4d.modules.sculpting.BrushDabData-method-Dab-State"></a>

#### `BrushDabData.GetBrushOverride(self)` <a id="c4d.modules.sculpting.BrushDabData.GetBrushOverride"></a>

Gets the override flags. This could be any combination of the *OVERRIDE* flags.

**Return type:** int

**Returns:** The overrides if there are any or *0* if there are none.

#### `BrushDabData.GetStrokeInstanceID(self)` <a id="c4d.modules.sculpting.BrushDabData.GetStrokeInstanceID"></a>

Gets the ID of the stroke instance that this dab is being drawn for.

**Return type:** int

**Returns:** The stroke instance ID.

#### `BrushDabData.IsBackface(self)` <a id="c4d.modules.sculpting.BrushDabData.IsBackface"></a>

Returns **True** if the dab is being applied backfacing polygons.

*New in version R17.032.*

> **Note:** Backface polygons will only be sculpted on if the brush has its BackFaceSculpting option enabled and the Backface option is also checked by the user.

**Return type:** bool

**Returns:** **True** if the dab is on backfacing polygons, otherwise **False**.

#### `BrushDabData.IsFillTool(self)` <a id="c4d.modules.sculpting.BrushDabData.IsFillTool"></a>

Checks if the current draw mode is fill.  
Basically checks if the dab *MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE* setting is:  
*MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_LASSO_FILL* or  
*MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_POLY_FILL* or  
*MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_RECTANGLE_FILL*

**Return type:** bool

**Returns:** **True** if the current draw mode is fill, otherwise **False**.

#### `BrushDabData.IsPreviewDab(self)` <a id="c4d.modules.sculpting.BrushDabData.IsPreviewDab"></a>

Checks if this is a preview dab. Currently only DragDab and DragRect draw modes support preview brushes.

**Return type:** bool

**Returns:** **True** if it is a preview dab, otherwise **False**.

### Drawing Context <a id="c4d.modules.sculpting.BrushDabData-method-Drawing-Context"></a>

#### `BrushDabData.GetBaseDraw(self)` <a id="c4d.modules.sculpting.BrushDabData.GetBaseDraw"></a>

Gets the [`BaseDraw`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw) that the user is currently drawing in.

**Return type:** int

**Returns:** The [`BaseDraw`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw).

#### `BrushDabData.GetData(self)` <a id="c4d.modules.sculpting.BrushDabData.GetData"></a>

Gets the settings data for the tool.

**Return type:** [c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The data.

### Hit And Cursor Position <a id="c4d.modules.sculpting.BrushDabData-method-Hit-And-Cursor-Position"></a>

#### `BrushDabData.GetEyePoint(self)` <a id="c4d.modules.sculpting.BrushDabData.GetEyePoint"></a>

Gets the location of the mouse in local space above the model.  
This point is created by interpolating between previous and next real mouse hitpoint on the surface of the Sculpt Object.  
It is then projected down onto the surface of the model to get the real hitpoint for this interpolated value.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The virtual mouse location in local space above the surface of the [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject).

#### `BrushDabData.GetHitPoint(self)` <a id="c4d.modules.sculpting.BrushDabData.GetHitPoint"></a>

Gets the point on the surface of the SculptObject where the dab is going to be placed. This is the center of the dab.

> **Note:** If the mode is set to *SCULPTBRUSHMODE_GRAB* then this always returns the initial hit point that occurred when the user first pressed the left mouse button down.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The hitpoint on the surface.

#### `BrushDabData.GetHitPolygon(self)` <a id="c4d.modules.sculpting.BrushDabData.GetHitPolygon"></a>

Gets the index of the polygon on the surface of the SculptObject where the dab is going to be placed.  
This is the center of the dab.

*New in version R17.032.*

**Return type:** int

**Returns:** The index of the polygon on hit the surface.

#### `BrushDabData.GetLastHitPoint(self)` <a id="c4d.modules.sculpting.BrushDabData.GetLastHitPoint"></a>

Gets the hit point for the previous dab during the stroke.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The last hitpoint on the surface.

#### `BrushDabData.GetMousePos3D(self)` <a id="c4d.modules.sculpting.BrushDabData.GetMousePos3D"></a>

If the brush mode is *SCULPTBRUSHMODE_GRAB* then this method can be used to get the location of the mouse pointer in world space in the scene.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The position of the mouse in world space if the brush mode is *SCULPTBRUSHMODE_GRAB*, otherwise it returns [`c4d.Vector(0,0,0)`](../../../c4d/Vector/index.md#c4d.Vector).

### Layer And Point Access <a id="c4d.modules.sculpting.BrushDabData-method-Layer-And-Point-Access"></a>

#### `BrushDabData.GetLayer(self)` <a id="c4d.modules.sculpting.BrushDabData.GetLayer"></a>

Retrieves the currently selected Layer for a subdivided [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject).

> **Note:** If the user is sculpting a regular [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject)) then this will return **None**.

**Return type:** Optional[[c4d.modules.sculpting.SculptLayer](../SculptLayer/index.md#c4d.modules.sculpting.SculptLayer)]

**Returns:** The currently selected layer in the LayerManager if it is a subdivided [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject), otherwise **None**.

#### `BrushDabData.GetOriginalPoint(self, index)` <a id="c4d.modules.sculpting.BrushDabData.GetOriginalPoint"></a>

Retrieves a copy of the point at *index* in its state before the brush stroke started.

> **Note:**
>
> You can use this point to compare where the surface was before the user started sculpting.  
> As an example this data is used by the grab tool to correctly offset the points based on their original location on the surface at the first mouse click.

**Parameters:** **index** (*int*) – The index of the point.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.BrushDabData.GetPointCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The point at *index* of the PolygonObject at the state it was in when the user first pressed the left mouse button down.

#### `BrushDabData.GetPoint(self, index)` <a id="c4d.modules.sculpting.BrushDabData.GetPoint"></a>

Retrieves the live point at *index* that is modified on the surface during a brush stroke.  
This point may already have been modified by previous brush dabs during the current brush stroke.

**Parameters:** **index** (*int*) – The index of the point.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.BrushDabData.GetPointCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The point at *index* on the [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) that is currently displayed in the viewport.

#### `BrushDabData.OffsetPoint(self, index, offset, respectStrength=0)` <a id="c4d.modules.sculpting.BrushDabData.OffsetPoint"></a>

Offsets the point on the layer by the given *offset* amount.

> **Note:** This method should be used if [`IsPreviewDab()`](#c4d.modules.sculpting.BrushDabData.IsPreviewDab) returns **False**, otherwise use [`OffsetPreviewPoint()`](#c4d.modules.sculpting.BrushDabData.OffsetPreviewPoint) instead.

**Parameters:**

- **index** (*int*) – The index of the point.

- **offset** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The vector to offset the point by.

- **respectStrength** (*int*) –

  Let you use or ignore settings such as the layers mask or strength when offsetting the point. See *SCULPTOFFSETFLAGS*.  
  By setting the *SCULPTOFFSETFLAGS_IGNOREMASK* flag it will ignore whatever the mask checkbox state is for the layer.  
  Otherwise it uses this state to determine if it should use the mask.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.BrushDabData.GetPointCount).

#### `BrushDabData.OffsetPreviewPoint(self, index, offset)` <a id="c4d.modules.sculpting.BrushDabData.OffsetPreviewPoint"></a>

If [`IsPreviewDab()`](#c4d.modules.sculpting.BrushDabData.IsPreviewDab) returns **True** then you should apply your offset using this method.  
If it returns **False** then you should use [`OffsetPreviewPoint()`](#c4d.modules.sculpting.BrushDabData.OffsetPreviewPoint) instead.  
This adds the offset to a temporary preview layer that is created when using the DragDab and DragRect draw modes.

**Parameters:**

- **index** (*int*) – The index of the point.
- **offset** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The vector to offset the point by.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.BrushDabData.GetPointCount).

### Object Context <a id="c4d.modules.sculpting.BrushDabData-method-Object-Context"></a>

#### `BrushDabData.GetBaseObject(self)` <a id="c4d.modules.sculpting.BrushDabData.GetBaseObject"></a>

Gets the original object that the Sculpt Tag is applied to.

> **Note:** In the case where this there is no Sculpt Tag on then this will return the same as the call to [`GetPolygonObject()`](#c4d.modules.sculpting.BrushDabData.GetPolygonObject).

**Return type:** [c4d.PolygonObject](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject)

**Returns:** The original object.

#### `BrushDabData.GetObject(self)` <a id="c4d.modules.sculpting.BrushDabData.GetObject"></a>

Gets the Sculpt Object that the dab is for.

**Return type:** [c4d.modules.sculpting.SculptObject](../SculptObject/index.md#c4d.modules.sculpting.SculptObject)

**Returns:** The sculpt object.

#### `BrushDabData.GetPolygonObject(self)` <a id="c4d.modules.sculpting.BrushDabData.GetPolygonObject"></a>

Gets the Polygon Object for the Sculpt Object that is currently being displayed in the viewport.

**Return type:** [c4d.PolygonObject](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject)

**Returns:** The Polygon Object.

#### `BrushDabData.IsSculptObject(self)` <a id="c4d.modules.sculpting.BrushDabData.IsSculptObject"></a>

Checks if the object being touched is a [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject) (i.e. has a [`SculptTag`](../SculptTag/index.md#c4d.modules.sculpting.SculptTag)).

**Return type:** bool

**Returns:** **True** if the object being touched is a [`SculptObject`](../SculptObject/index.md#c4d.modules.sculpting.SculptObject), otherwise **False**.

### Point Editing <a id="c4d.modules.sculpting.BrushDabData-method-Point-Editing"></a>

#### `BrushDabData.ApplySmooth(self)` <a id="c4d.modules.sculpting.BrushDabData.ApplySmooth"></a>

Applies an effect of the smooth brush to the current dab.

> **Note:** Call this after you have modified the dab to smooth it out if needed.

#### `BrushDabData.DirtyAllPoints(self, flags)` <a id="c4d.modules.sculpting.BrushDabData.DirtyAllPoints"></a>

Dirty all the points for this dab according to the flags.

**Parameters:** **flags** (*int*) – See *SCULPTBRUSHDATATYPE*.

#### `BrushDabData.IsPointModified(self, index)` <a id="c4d.modules.sculpting.BrushDabData.IsPointModified"></a>

When using symmetry another mirrored brush may change the point.  
You can use this to check if another brush stroke has changed a point and if so then you can do something different for this current stroke.

**Parameters:** **index** (*int*) – The index of the point.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.BrushDabData.GetPointCount).

**Return type:** bool

**Returns:** **True** if the point was modified, otherwise **False**.

### Stencil And Stamp <a id="c4d.modules.sculpting.BrushDabData-method-Stencil-And-Stamp"></a>

#### `BrushDabData.GetStamp(self)` <a id="c4d.modules.sculpting.BrushDabData.GetStamp"></a>

Retreves the stamp bitmap used for this dab.

**Return type:** [c4d.bitmaps.BaseBitmap](../../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)

**Returns:** The bitmap for the stamp.

#### `BrushDabData.GetStampColor(self, point, distance, mode)` <a id="c4d.modules.sculpting.BrushDabData.GetStampColor"></a>

Retrieves the grey value, color and coordinates of the stamp for a point in the Sculpt Object local space.

**Parameters:**

- **point** (*int*) – The index of the point.

- **distance** (*float*) –

  Can be either the point data distance value (returned by :[`GetPointData()`](#c4d.modules.sculpting.BrushDabData.GetPointData)), the length of the vector (hitpoint - point) or a custom distance value.  
  This is used to get the correct falloff for the point.

- **mode** (*int*) – The mode used to sample the stamp texture. See *SAMPLEMODE*.

**Raises:** **IndexError** – If the *point* index is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.BrushDabData.GetPointCount).

**Return type:** dict{**grey**: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector), **color**: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector), **coords**: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)}

**Returns:** The grey value (adjusted by the stamps Gray Value), color and coordinates of the stamp.

#### `BrushDabData.GetStencil(self)` <a id="c4d.modules.sculpting.BrushDabData.GetStencil"></a>

Retrieves the stencil bitmap used for this dab.

**Return type:** [c4d.bitmaps.BaseBitmap](../../../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)

**Returns:** The bitmap for the stencil.

#### `BrushDabData.GetStencilColor(self, point, mode=0)` <a id="c4d.modules.sculpting.BrushDabData.GetStencilColor"></a>

Retrieves the grey value, color and coordinates of the stencil for a point in the Sculpt Object local space.

**Parameters:**

- **point** (*int*) – The index of the point.
- **mode** (*Optional*[*int*]) – The mode used to sample the stencil texture. See *SAMPLEMODE*.

**Raises:** **IndexError** – If the *point* index is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.BrushDabData.GetPointCount).

**Return type:** dict{**grey**: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector), **color**: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector), **coords**: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)}

**Returns:** The grey value, color and coords of the stencil.

### Surface Normals <a id="c4d.modules.sculpting.BrushDabData-method-Surface-Normals"></a>

#### `BrushDabData.GetAveragePointAndNormal(self)` <a id="c4d.modules.sculpting.BrushDabData.GetAveragePointAndNormal"></a>

Gets the average point and normal.  
Depending on what the Fixed Plane (*MDATA_SCULPTBRUSH_SETTINGS_FIXEDPLANE*) setting is for the brush this will return one of *3* things:

- ***MDATA_SCULPTBRUSH_SETTINGS_FIXEDPLANE_OFF***

  - averagePoint = The average location of all the points that are touched by the dab.
  - normal = The normal at the hitpoint on the surface of the Sculpt Object.

- ***MDATA_SCULPTBRUSH_SETTINGS_FIXEDPLANE_MOUSEDOWN***

  - averagePoint = The average location of all the points under the dab area when the mouse was mouse button was first pressed.
  - normal = The average normal of all the points under the dab area when the mouse was mouse button was first pressed.

- ***MDATA_SCULPTBRUSH_SETTINGS_FIXEDPLANE_WORKPLANE***

  - averagePoint = The point on the workplane that is above the hitpoint on the surface of the Sculpt Object.
  - normal = The normal of the workplane.

**Return type:** dict{**averagePoint**: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector), **normal**: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector)}

**Returns:** The average point and normal based on the Fixed Plane setting.

#### `BrushDabData.GetFaceNormal(self, index)` <a id="c4d.modules.sculpting.BrushDabData.GetFaceNormal"></a>

Gets the face normal at *index* for the SculptObject.

*New in version R17.032.*

**Parameters:** **index** (*int*) – The index of the face.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The face normal.

#### `BrushDabData.GetNormal(self)` <a id="c4d.modules.sculpting.BrushDabData.GetNormal"></a>

Gets the normal at the current hitpoint for the dab.  
This is the average vertex normal of all the points that are affected by the dab.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The normal at the current hitpoint.

#### `BrushDabData.GetOriginalVertexNormal(self, index)` <a id="c4d.modules.sculpting.BrushDabData.GetOriginalVertexNormal"></a>

Gets the state of a vertex normal before the user started a brush stroke.

*New in version R17.048.*

**Parameters:** **index** (*int*) – The index of the vertex.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The original vertex normal.

#### `BrushDabData.GetVertexNormal(self, index)` <a id="c4d.modules.sculpting.BrushDabData.GetVertexNormal"></a>

Gets the vertex normal at *index* for the Sculpt Object.

**Parameters:** **index** (*int*) – The index of the vertex.

**Raises:** **IndexError** – If the vertex *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.BrushDabData.GetPointCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The vertex normal.

### Symmetry And Direction <a id="c4d.modules.sculpting.BrushDabData-method-Symmetry-And-Direction"></a>

#### `BrushDabData.GetDrawDirectionNormal(self)` <a id="c4d.modules.sculpting.BrushDabData.GetDrawDirectionNormal"></a>

If the brush supports the Draw Direction, i.e. the user has set `SculptBrushParams.EnableDrawDirection()` to **True**, then this returns the direction selected by the user.  
Otherwise it just returns the same vector as [`GetNormal()`](#c4d.modules.sculpting.BrushDabData.GetNormal).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The Draw Direction normal.

#### `BrushDabData.GetMirrorPoint(self, point, isNormal)` <a id="c4d.modules.sculpting.BrushDabData.GetMirrorPoint"></a>

Mirror the point (or Normal) from the objects space to the correct location for the current dab.  
This should only be used if you need to get the symmetrically mirrored point for a point that you specifically need.  
In most cases this method would never be used because the brush system automatically handles symmetrical points for you.

**Parameters:**

- **point** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The input point, or normal to mirror.
- **isNormal** (*bool*) – Set to **True** if *point* is a normal, so that it will then only be rotated and will not be offset.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The mirrored point.

#### `BrushDabData.IsMirroredDab(self)` <a id="c4d.modules.sculpting.BrushDabData.IsMirroredDab"></a>

Checks if this dab is for a mirrored brush stroke.

**Return type:** bool

**Returns:** **True** if it’s a mirrored dab or **False** if it’s the main brush stroke.
