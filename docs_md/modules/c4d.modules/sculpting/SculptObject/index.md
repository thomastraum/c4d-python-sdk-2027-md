<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/sculpting/SculptObject/index.html -->

# c4d.modules.sculpting.SculptObject <a id="c4d-modules-sculpting-sculptobject"></a>

## *class* `c4d.modules.sculpting.SculptObject` <a id="c4d.modules.sculpting.SculptObject"></a>

A [`SculptObject`](#c4d.modules.sculpting.SculptObject) is what you use to interact with the data referenced by a [`SculptTag`](../SculptTag/index.md#c4d.modules.sculpting.SculptTag) (`SculptTag.GetSculptObject()`).  
The [`SculptTag`](../SculptTag/index.md#c4d.modules.sculpting.SculptTag) on a [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) references a [`SculptObject`](#c4d.modules.sculpting.SculptObject) that is stored in a scene hook within the document.  
When the [`SculptTag`](../SculptTag/index.md#c4d.modules.sculpting.SculptTag) is deleted this [`SculptObject`](#c4d.modules.sculpting.SculptObject) is also deleted.

*New in version R15.037.*

Parent Class:

- [`c4d.BaseObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

## Overview <a id="overview"></a>

**Collision And Raycasting**

- [`SculptObject.HitObject()`](#c4d.modules.sculpting.SculptObject.HitObject): Given a ray in object space do a hit intersection against the sculpt object and return any data if the ray hits the object.
- [`SculptObject.HitScreen()`](#c4d.modules.sculpting.SculptObject.HitScreen): From a viewport cast a ray, in screen space, onto the sculpt object and return any data if the ray hits the object.
- [`SculptObject.NeedCollisionUpdate()`](#c4d.modules.sculpting.SculptObject.NeedCollisionUpdate): Tells the sculpt object that it requires a collision update before the user tries to use any of the sculpt tools.
- [`SculptObject.UpdateCollision()`](#c4d.modules.sculpting.SculptObject.UpdateCollision): Updates any collision data after any changes to the sculpt layer offsets have been made.

**Geometry Access**

- [`SculptObject.GetDisplayPolygonObject()`](#c4d.modules.sculpting.SculptObject.GetDisplayPolygonObject): Retrieves the Polygon Object that is currently being displayed in the viewport.
- [`SculptObject.GetFaceNormal()`](#c4d.modules.sculpting.SculptObject.GetFaceNormal): Gets the face normal for the polygon object at *index* and at the current subdivision level.
- [`SculptObject.GetOriginalObject()`](#c4d.modules.sculpting.SculptObject.GetOriginalObject): Get the original [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) that the [`SculptTag`](../SculptTag/index.md#c4d.modules.sculpting.SculptTag) is applied to.
- [`SculptObject.GetPoint()`](#c4d.modules.sculpting.SculptObject.GetPoint): Get read-only access to the point at *index* that will be used for the polygon object at the current subdivision level.
- [`SculptObject.GetPolygon()`](#c4d.modules.sculpting.SculptObject.GetPolygon): Gets the Polygon at the given *index*.
- [`SculptObject.GetVertexNormal()`](#c4d.modules.sculpting.SculptObject.GetVertexNormal): Get the vertex normal for the polygon object at *index* and at the current subdivision level.

**Layer Management**

- [`SculptObject.AddFolder()`](#c4d.modules.sculpting.SculptObject.AddFolder): Create a new folder for the sculpt object.
- [`SculptObject.AddLayer()`](#c4d.modules.sculpting.SculptObject.AddLayer): Create a new layer on the sculpt object at the current subdivision level.
- [`SculptObject.DeleteSelectedLayer()`](#c4d.modules.sculpting.SculptObject.DeleteSelectedLayer): Deletes the currently selected layer (or folder) on the sculpt object (as specified in the Sculpting Layer Manager UI).
- [`SculptObject.GetBaseLayer()`](#c4d.modules.sculpting.SculptObject.GetBaseLayer): Get the Base Object layer, which is the special layer that has multiple [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) children, one for each subdivison level, that allows the user to sculpt on while at any subdivision level.
- [`SculptObject.GetCurrentLayer()`](#c4d.modules.sculpting.SculptObject.GetCurrentLayer): Get the currently layer, or folder, selected for this sculpt object.
- [`SculptObject.GetFirstLayer()`](#c4d.modules.sculpting.SculptObject.GetFirstLayer): Get the first layer.

**Masks And Selection**

- [`SculptObject.GetMaskCachePoint()`](#c4d.modules.sculpting.SculptObject.GetMaskCachePoint): Gets the mask value from the mask cache.
- [`SculptObject.IsPointSelected()`](#c4d.modules.sculpting.SculptObject.IsPointSelected): For use in the `SculptBrushToolData.FloodSelectedLayer()` method to determine if a point should be moved or not.
- [`SculptObject.IsPolygonSelected()`](#c4d.modules.sculpting.SculptObject.IsPolygonSelected): For use in the `SculptBrushToolData.FloodSelectedLayer()` method to determine if a point should be moved or not.
- [`SculptObject.UpdateMask()`](#c4d.modules.sculpting.SculptObject.UpdateMask): Updates the mask on the sculpt object.

**Processing And Resources**

- [`SculptObject.GetMemoryUsage()`](#c4d.modules.sculpting.SculptObject.GetMemoryUsage): Get the amount of memory currently used for this sculpt object.
- [`SculptObject.InitOpenGL()`](#c4d.modules.sculpting.SculptObject.InitOpenGL): Initializes the sculpt object for the given viewport for OpenGL use.
- [`SculptObject.Smooth()`](#c4d.modules.sculpting.SculptObject.Smooth): Smooth the sculpt object and apply the offsets to the currently selected layer.
- [`SculptObject.Update()`](#c4d.modules.sculpting.SculptObject.Update): Recomposites all the layers and updates the sculpt object.

**State Controls**

- [`SculptObject.GetAllowDeformations()`](#c4d.modules.sculpting.SculptObject.GetAllowDeformations): Check if the object allows to be deformed by any deformers.
- [`SculptObject.IsFrozen()`](#c4d.modules.sculpting.SculptObject.IsFrozen): Check if the sculpt object is frozen.
- [`SculptObject.SetAllowDeformations()`](#c4d.modules.sculpting.SculptObject.SetAllowDeformations): Set the *Allow Deformations* checkbox thereby allowing any deformers to have an effect on the display of the sculpt object, as long as it is also frozen.
- [`SculptObject.SetFrozen()`](#c4d.modules.sculpting.SculptObject.SetFrozen): Sets the frozen state of the sculpt object.

**Subdivision Management**

- [`SculptObject.DecreaseSubdivisionLevel()`](#c4d.modules.sculpting.SculptObject.DecreaseSubdivisionLevel): Decrease the subdivision level to the down one level.
- [`SculptObject.GetCurrentLevel()`](#c4d.modules.sculpting.SculptObject.GetCurrentLevel): Gets the current subdivision level that the sculpt object is currently at.
- [`SculptObject.GetPointCount()`](#c4d.modules.sculpting.SculptObject.GetPointCount): Get the number of points at the current subdivision level.
- [`SculptObject.GetPolygonCopy()`](#c4d.modules.sculpting.SculptObject.GetPolygonCopy): Get a copy of the sculpt object at a specific subdivision level.
- [`SculptObject.GetPolygonCount()`](#c4d.modules.sculpting.SculptObject.GetPolygonCount): Get the number of polygons at the current subdivision level.
- [`SculptObject.GetSubdivisionCount()`](#c4d.modules.sculpting.SculptObject.GetSubdivisionCount): Get the number of subdivisions that this sculpt object currently has; i.e.
- [`SculptObject.IncreaseSubdivisionLevel()`](#c4d.modules.sculpting.SculptObject.IncreaseSubdivisionLevel): Increase the subdivision level to the next highest level.
- [`SculptObject.Subdivide()`](#c4d.modules.sculpting.SculptObject.Subdivide): Subdivide the sculpt object to the next level.

**Undo Management**

- [`SculptObject.EndUndo()`](#c4d.modules.sculpting.SculptObject.EndUndo): Must be called after `StartUndo()` once all the points and masks have been changed on the layers.
- [`SculptObject.StartUndo()`](#c4d.modules.sculpting.SculptObject.StartUndo): Call before any calls to `AddOffset()`, `SetOffset()`, `AddToMask()` or `SetMask()` if you wish it to be undone.

## Members <a id="members"></a>

### Collision And Raycasting <a id="c4d.modules.sculpting.SculptObject-method-Collision-And-Raycasting"></a>

#### `SculptObject.HitObject(self, rayp, rayv, backfaces)` <a id="c4d.modules.sculpting.SculptObject.HitObject"></a>

Given a ray in object space do a hit intersection against the sculpt object and return any data if the ray hits the object.

> **Note:** This will return the closest hit point if multiple intersections are found.

> **Note:** To use the *Hit* functions the mesh must be unfrozen and both `NeedCollisionUpdate(True)` and [`UpdateCollision()`](#c4d.modules.sculpting.SculptObject.UpdateCollision) should be called to initialize the collision data.

**Parameters:**

- **rayp** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The starting position of the ray in object space.
- **rayv** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The direction the ray is pointing.
- **backfaces** (*bool*) – Allow back facing polygons to be hit tested.

**Return type:** dict{**distance**: float, **normal**: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector), **point**: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector), **polygon**: int}

**Returns:**

The intersection data will be returned if the object was hit:

distance: The distance from the ray point. normal: The normal of the hitpoint on the surface of the object in its local coordinate system. point: Location of the hit point on the surface of the object in its local coordinate system. polygon: The polygon that was hit.

#### `SculptObject.HitScreen(self, bd, mx, my, backfaces)` <a id="c4d.modules.sculpting.SculptObject.HitScreen"></a>

From a viewport cast a ray, in screen space, onto the sculpt object and return any data if the ray hits the object.

> **Note:** This will return the closest hit point if multiple intersections are found.

> **Note:** To use the *Hit* functions the mesh must be unfrozen and both `NeedCollisionUpdate(True)` and [`UpdateCollision()`](#c4d.modules.sculpting.SculptObject.UpdateCollision) should be called to initialize the collision data.

**Parameters:**

- **bd** ([*c4d.BaseDraw*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The [`BaseDraw`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw) that the user is casting the ray from.
- **mx** (*float*) – The X coordinate (i.e. mouse coordinate) in screen space.
- **my** (*float*) – The Y coordinate (i.e mouse coordinate) in screen space.
- **backfaces** (*bool*) – Allow back facing polygons to be hit tested.

**Return type:** dict{**distance**: float, **normal**: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector), **point**: [`Vector`](../../../c4d/Vector/index.md#c4d.Vector), **polygon**: int}

**Returns:**

The intersection data will be returned if the object was hit:

distance: The distance from the ray point. normal: The normal of the hitpoint on the surface of the object in its local coordinate system. point: Location of the hit point on the surface of the object in its local coordinate system. polygon: The polygon that was hit.

#### `SculptObject.NeedCollisionUpdate(self, fullUpdate)` <a id="c4d.modules.sculpting.SculptObject.NeedCollisionUpdate"></a>

Tells the sculpt object that it requires a collision update before the user tries to use any of the sculpt tools. Then next time a user tries to use a tool it will first call [`UpdateCollision()`](#c4d.modules.sculpting.SculptObject.UpdateCollision) to ensure that the [`HitScreen()`](#c4d.modules.sculpting.SculptObject.HitScreen)/[`HitObject()`](#c4d.modules.sculpting.SculptObject.HitObject) calls will be correct.

**Parameters:** **fullUpdate** (*bool*) – Set to **True** to update the full mesh. This is not always required.

#### `SculptObject.UpdateCollision(self)` <a id="c4d.modules.sculpting.SculptObject.UpdateCollision"></a>

Updates any collision data after any changes to the sculpt layer offsets have been made. This is required before you call the [`HitScreen()`](#c4d.modules.sculpting.SculptObject.HitScreen)/[`HitObject()`](#c4d.modules.sculpting.SculptObject.HitObject) methods.

### Geometry Access <a id="c4d.modules.sculpting.SculptObject-method-Geometry-Access"></a>

#### `SculptObject.GetDisplayPolygonObject(self)` <a id="c4d.modules.sculpting.SculptObject.GetDisplayPolygonObject"></a>

Retrieves the Polygon Object that is currently being displayed in the viewport.  
This is the internal Polygon Object and should never be changed.

*New in version R16.021.*

> **Note:** In `SculptBrushToolData.FloodSelectedLayer()` calls it returns the same as [`GetOriginalObject()`](#c4d.modules.sculpting.SculptObject.GetOriginalObject) when sculpting on a Polygon Object that have no [`SculptTag`](../SculptTag/index.md#c4d.modules.sculpting.SculptTag).

**Return type:** [c4d.PolygonObject](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject)

**Returns:** The Polygon Object displayed in the viewport.

#### `SculptObject.GetFaceNormal(self, index)` <a id="c4d.modules.sculpting.SculptObject.GetFaceNormal"></a>

Gets the face normal for the polygon object at *index* and at the current subdivision level.

*New in version R17.032.*

**Parameters:** **index** (*int*) – The index of the face.

**Raises:** **IndexError** – If the face *index* is out of range : *0<=index<*[`GetPolygonCount()`](#c4d.modules.sculpting.SculptObject.GetPolygonCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The face normal.

#### `SculptObject.GetOriginalObject(self)` <a id="c4d.modules.sculpting.SculptObject.GetOriginalObject"></a>

Get the original [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) that the [`SculptTag`](../SculptTag/index.md#c4d.modules.sculpting.SculptTag) is applied to.

**Return type:** [c4d.PolygonObject](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject)

**Returns:** The original [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject).

#### `SculptObject.GetPoint(self, index)` <a id="c4d.modules.sculpting.SculptObject.GetPoint"></a>

Get read-only access to the point at *index* that will be used for the polygon object at the current subdivision level.

**Parameters:** **index** (*int*) – The index of the point.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptObject.GetPointCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The point.

#### `SculptObject.GetPolygon(self, index)` <a id="c4d.modules.sculpting.SculptObject.GetPolygon"></a>

Gets the Polygon at the given *index*.

*New in version R16.021.*

**Parameters:** **index** (*int*) – The index of the polygon.

**Raises:** **IndexError** – If the polygon *index* is out of range : *0<=index<*[`GetPolygonCount()`](#c4d.modules.sculpting.SculptObject.GetPolygonCount).

**Return type:** Optional[[c4d.CPolygon](../../../c4d/CPolygon/index.md#c4d.CPolygon)]

**Returns:** The Polygon if it was found, otherwise **None**.

#### `SculptObject.GetVertexNormal(self, index)` <a id="c4d.modules.sculpting.SculptObject.GetVertexNormal"></a>

Get the vertex normal for the polygon object at *index* and at the current subdivision level.

**Parameters:** **index** (*int*) – The index of the vertex.

**Raises:** **IndexError** – If the vertex *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptObject.GetPointCount).

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The vertex normal.

### Layer Management <a id="c4d.modules.sculpting.SculptObject-method-Layer-Management"></a>

#### `SculptObject.AddFolder(self)` <a id="c4d.modules.sculpting.SculptObject.AddFolder"></a>

Create a new folder for the sculpt object.

**Return type:** [c4d.modules.sculpting.SculptFolder](../SculptFolder/index.md#c4d.modules.sculpting.SculptFolder)

**Returns:** The sculpt folder added.

#### `SculptObject.AddLayer(self)` <a id="c4d.modules.sculpting.SculptObject.AddLayer"></a>

Create a new layer on the sculpt object at the current subdivision level.

**Return type:** [c4d.modules.sculpting.SculptLayer](../SculptLayer/index.md#c4d.modules.sculpting.SculptLayer)

**Returns:** The sculpt layer added.

#### `SculptObject.DeleteSelectedLayer(self)` <a id="c4d.modules.sculpting.SculptObject.DeleteSelectedLayer"></a>

Deletes the currently selected layer (or folder) on the sculpt object (as specified in the Sculpting Layer Manager UI).

> **Note:** If the currently selected layer is a folder then it will only delete the folder if all the layers that are contained in that folder are at the same subdivision level as the current subdivion level.

**Return type:** bool

**Returns:** **True** if the layer was deleted, otherwise **False**.

#### `SculptObject.GetBaseLayer(self)` <a id="c4d.modules.sculpting.SculptObject.GetBaseLayer"></a>

Get the Base Object layer, which is the special layer that has multiple [`SculptLayerData`](../SculptLayerData/index.md#c4d.modules.sculpting.SculptLayerData) children, one for each subdivison level, that allows the user to sculpt on while at any subdivision level.

**Return type:** [c4d.modules.sculpting.SculptLayerBase](../SculptLayerBase/index.md#c4d.modules.sculpting.SculptLayerBase)

**Returns:** The Base Object layer.

#### `SculptObject.GetCurrentLayer(self)` <a id="c4d.modules.sculpting.SculptObject.GetCurrentLayer"></a>

Get the currently layer, or folder, selected for this sculpt object.

**Return type:** [c4d.modules.sculpting.SculptLayerBase](../SculptLayerBase/index.md#c4d.modules.sculpting.SculptLayerBase)

**Returns:** The current sculpt layer or folder.

#### `SculptObject.GetFirstLayer(self)` <a id="c4d.modules.sculpting.SculptObject.GetFirstLayer"></a>

Get the first layer. This is usually the Base Object layer.

**Return type:** [c4d.modules.sculpting.SculptLayerBase](../SculptLayerBase/index.md#c4d.modules.sculpting.SculptLayerBase)

**Returns:** The first layer.

### Masks And Selection <a id="c4d.modules.sculpting.SculptObject-method-Masks-And-Selection"></a>

#### `SculptObject.GetMaskCachePoint(self, id)` <a id="c4d.modules.sculpting.SculptObject.GetMaskCachePoint"></a>

Gets the mask value from the mask cache.

*New in version R16.021.*

**Parameters:** **id** (*int*) – The index of the point.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptObject.GetPointCount).

**Return type:** float

**Returns:** The mask cache value.

#### `SculptObject.IsPointSelected(self, index)` <a id="c4d.modules.sculpting.SculptObject.IsPointSelected"></a>

For use in the `SculptBrushToolData.FloodSelectedLayer()` method to determine if a point should be moved or not.  
When in Point Mode, and there is a selection, it returns **True** if a point is selected or **False** if the point is not selected. If there are no points selected it returns **True**.  
When in Polygon Mode, and there is a selection, it returns **True** if a point on any of the selected polygons is selected or **False** if there is no point selected. If there are no polygons selected it returns **True**.  
It returns **False** in all other cases.

*New in version R16.021.*

> **Note:** This method only works when the selected object being sculpted on is by a tool and is a Polygon Object without a [`SculptTag`](../SculptTag/index.md#c4d.modules.sculpting.SculptTag).

**Parameters:** **index** (*int*) – The index of the point.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=index<*[`GetPointCount()`](#c4d.modules.sculpting.SculptObject.GetPointCount).

**Return type:** bool

**Returns:** **True** if the point was selected, **False** if not.

#### `SculptObject.IsPolygonSelected(self, index)` <a id="c4d.modules.sculpting.SculptObject.IsPolygonSelected"></a>

For use in the `SculptBrushToolData.FloodSelectedLayer()` method to determine if a point should be moved or not.  
When in Polygon Mode, and there is a selection, it returns **True** if a point on any of the selected polygons is selected or **False** if there is no point selected.  
If there are no polygons selected it returns **True**. It returns **False** in all other cases.

*New in version R16.021.*

> **Note:** This method only works when the selected object being sculpted on is by a tool and is a Polygon Object without a [`SculptTag`](../SculptTag/index.md#c4d.modules.sculpting.SculptTag).

**Parameters:** **index** (*int*) – The index of the polygon.

**Raises:** **IndexError** – If the polygon *index* is out of range : *0<=index<*[`GetPolygonCount()`](#c4d.modules.sculpting.SculptObject.GetPolygonCount).

**Return type:** bool

**Returns:** **True** if the polygon was selected, **False** if not.

#### `SculptObject.UpdateMask(self, fullUpdate)` <a id="c4d.modules.sculpting.SculptObject.UpdateMask"></a>

Updates the mask on the sculpt object.

*New in version R16.021.*

**Parameters:** **fullUpdate** (*bool*) – Pass **True** to force a full update of the mask.

### Processing And Resources <a id="c4d.modules.sculpting.SculptObject-method-Processing-And-Resources"></a>

#### `SculptObject.GetMemoryUsage(self)` <a id="c4d.modules.sculpting.SculptObject.GetMemoryUsage"></a>

Get the amount of memory currently used for this sculpt object. This does not include any memory used by the Viewport.

**Return type:** int

**Returns:** The memory used in bytes.

#### `SculptObject.InitOpenGL(self, bd)` <a id="c4d.modules.sculpting.SculptObject.InitOpenGL"></a>

Initializes the sculpt object for the given viewport for OpenGL use. Private.

*New in version R16.021.*

**Parameters:** **bd** (*Optional*[[*c4d.BaseDraw*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)]) – The viewport that is being updated. If **None** then the currently active view will be used.

#### `SculptObject.Smooth(self, count, respectMask)` <a id="c4d.modules.sculpting.SculptObject.Smooth"></a>

Smooth the sculpt object and apply the offsets to the currently selected layer.

**Parameters:**

- **count** (*int*) – The number of times to run the smooth algorithm.
- **respectMask** (*bool*) – **True** to not smooth any masked out points, **False** to apply it to every point.

#### `SculptObject.Update(self)` <a id="c4d.modules.sculpting.SculptObject.Update"></a>

Recomposites all the layers and updates the sculpt object.

### State Controls <a id="c4d.modules.sculpting.SculptObject-method-State-Controls"></a>

#### `SculptObject.GetAllowDeformations(self)` <a id="c4d.modules.sculpting.SculptObject.GetAllowDeformations"></a>

Check if the object allows to be deformed by any deformers. This is also able to be set on the [`SculptTag`](../SculptTag/index.md#c4d.modules.sculpting.SculptTag) in Cinema 4D’s UI.

> **Note:**
>
> This option only works if the object is also frozen.  
> When both these options are enabled, any deformers that are children of the polygon object that the sculpt tag is applied to, will be able to deform the object in the viewport.

**Return type:** bool

**Returns:** **True** if the sculpt object allows deformations, otherwise **False**.

#### `SculptObject.IsFrozen(self)` <a id="c4d.modules.sculpting.SculptObject.IsFrozen"></a>

Check if the sculpt object is frozen.  
This is also able to be set on the [`SculptTag`](../SculptTag/index.md#c4d.modules.sculpting.SculptTag) in Cinema 4D’s UI.

**Return type:** bool

**Returns:** **True** if the object is frozen, otherwise **False**.

#### `SculptObject.SetAllowDeformations(self, allowDef)` <a id="c4d.modules.sculpting.SculptObject.SetAllowDeformations"></a>

Set the *Allow Deformations* checkbox thereby allowing any deformers to have an effect on the display of the sculpt object, as long as it is also frozen.  
This option can also be found in the [`SculptTag`](../SculptTag/index.md#c4d.modules.sculpting.SculptTag)’s UI.

**Parameters:** **allowDef** (*bool*) – **True** to allow deformations, otherwise **False**.

#### `SculptObject.SetFrozen(self, frozen)` <a id="c4d.modules.sculpting.SculptObject.SetFrozen"></a>

Sets the frozen state of the sculpt object. In Cinema 4D UI this is shown in the [`SculptTag`](../SculptTag/index.md#c4d.modules.sculpting.SculptTag). When the object is frozen no changes to the sculpt object or any of its layers are allowed.

> **Note:**
>
> If the polygon object has a *Phong* tag it will also become active when the sculpt object is frozen.  
> When not Frozen then the sculpt object uses its own internal vertex normals and disables the *Phong* tag on the polygonobject.

**Parameters:** **frozen** (*bool*) – The frozen state.

### Subdivision Management <a id="c4d.modules.sculpting.SculptObject-method-Subdivision-Management"></a>

#### `SculptObject.DecreaseSubdivisionLevel(self)` <a id="c4d.modules.sculpting.SculptObject.DecreaseSubdivisionLevel"></a>

Decrease the subdivision level to the down one level.  
If it is already at level 0 then it will do nothing.

**Return type:** bool

**Returns:** **True** if it was able go down a level, otherwise **False**.

#### `SculptObject.GetCurrentLevel(self)` <a id="c4d.modules.sculpting.SculptObject.GetCurrentLevel"></a>

Gets the current subdivision level that the sculpt object is currently at.

**Return type:** int

**Returns:** The current subdivision level.

#### `SculptObject.GetPointCount(self)` <a id="c4d.modules.sculpting.SculptObject.GetPointCount"></a>

Get the number of points at the current subdivision level.

**Return type:** int

**Returns:** The number of points.

#### `SculptObject.GetPolygonCopy(self, level, includeTopLevels)` <a id="c4d.modules.sculpting.SculptObject.GetPolygonCopy"></a>

Get a copy of the sculpt object at a specific subdivision level.

**Parameters:**

- **level** (*int*) – The subdivision level to copy the [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) at.

- **includeTopLevels** (*bool*) –

  If True includes all the detail from any layers that are above subdivisionLevel.  
  If false includes only the sculpting data for all layers up to and including the subdivisionLevel specified.

**Return type:** [c4d.PolygonObject](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject)

**Returns:** The [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) for the subdivision *level*.

#### `SculptObject.GetPolygonCount(self)` <a id="c4d.modules.sculpting.SculptObject.GetPolygonCount"></a>

Get the number of polygons at the current subdivision level.

**Return type:** int

**Returns:** The number of polygons.

#### `SculptObject.GetSubdivisionCount(self)` <a id="c4d.modules.sculpting.SculptObject.GetSubdivisionCount"></a>

Get the number of subdivisions that this sculpt object currently has; i.e. how many times it has been subdivided by the user.

**Return type:** int

**Returns:** The number of subdivision levels.

#### `SculptObject.IncreaseSubdivisionLevel(self)` <a id="c4d.modules.sculpting.SculptObject.IncreaseSubdivisionLevel"></a>

Increase the subdivision level to the next highest level.  
If it is already at the top subdivision level then it will do nothing.

**Return type:** bool

**Returns:** **True** if it was able go up a level, otherwise **False**.

#### `SculptObject.Subdivide(self)` <a id="c4d.modules.sculpting.SculptObject.Subdivide"></a>

Subdivide the sculpt object to the next level.

> **Note:** This method will only work if the sculpt object is already at the top most level and the memory limit (as specified in the preferences) has not been exceeded and also only if there is enough memory on the user’s computer to successfully do the subdivision.

**Return type:** bool

**Returns:** **True** if the object was successfully subdivided, otherwise **False**.

### Undo Management <a id="c4d.modules.sculpting.SculptObject-method-Undo-Management"></a>

#### `SculptObject.EndUndo(self)` <a id="c4d.modules.sculpting.SculptObject.EndUndo"></a>

Must be called after [`StartUndo()`](#c4d.modules.sculpting.SculptObject.StartUndo) once all the points and masks have been changed on the layers.

#### `SculptObject.StartUndo(self)` <a id="c4d.modules.sculpting.SculptObject.StartUndo"></a>

Call before any calls to `AddOffset()`, `SetOffset()`, `AddToMask()` or `SetMask()` if you wish it to be undone.

> **Warning:**
>
> This will only work if you are only making changes to a single layer.  
> Changes to multiple layers or layers at different levels is not allowed.

> **Note:** The method [`EndUndo()`](#c4d.modules.sculpting.SculptObject.EndUndo) must be called after all calls to the above functions have been done.
