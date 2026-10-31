<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseData/NodeData/ObjectData/index.html -->

# c4d.plugins.ObjectData <a id="c4d-plugins-objectdata"></a>

## *class* `c4d.plugins.ObjectData` <a id="c4d.plugins.ObjectData"></a>

An object plugin class to be registered with [`RegisterObjectPlugin()`](../../../index.md#c4d.plugins.RegisterObjectPlugin).

Parent Class:

- [`c4d.plugins.NodeData`](../index.md#c4d.plugins.NodeData)

## Overview <a id="overview"></a>

**Generic Methods**

- [`ObjectData.AddToExecution()`](#c4d.plugins.ObjectData.AddToExecution): Override - By default this function returns *False*.
- [`ObjectData.Draw()`](#c4d.plugins.ObjectData.Draw): Override - Called when the display is updated for you to display some visual element of your op in the 3D view.
- [`ObjectData.DrawShadow()`](#c4d.plugins.ObjectData.DrawShadow): Called during the shadow pass instead of the `Draw()` method.
- [`ObjectData.Execute()`](#c4d.plugins.ObjectData.Execute): Override - Called at the point in the priority pipeline specified by `AddToExecution()`, or the lack thereof.
- [`ObjectData.GetContour()`](#c4d.plugins.ObjectData.GetContour): Override - Return a spline contour.
- [`ObjectData.GetDimension()`](#c4d.plugins.ObjectData.GetDimension): Override - Return the boundaries of your object.
- [`ObjectData.GetVirtualObjects()`](#c4d.plugins.ObjectData.GetVirtualObjects): Override - Return an object chain of a generator object (e.g.
- [`ObjectData.SetOptimizeCache()`](#c4d.plugins.ObjectData.SetOptimizeCache): Sets the cache optimization for the node.

**Handle Methods**

- [`ObjectData.DetectHandle()`](#c4d.plugins.ObjectData.DetectHandle): Override - Manually detect a click on a handle.
- [`ObjectData.GetHandle()`](#c4d.plugins.ObjectData.GetHandle): Called to get the information for handle at index *i*. Part of the automated handle interface.
- [`ObjectData.GetHandleCount()`](#c4d.plugins.ObjectData.GetHandleCount): Called to get the number of handles the object has.
- [`ObjectData.MoveHandle()`](#c4d.plugins.ObjectData.MoveHandle): Override - Move a handle manually.
- [`ObjectData.SetHandle()`](#c4d.plugins.ObjectData.SetHandle): Called to set the information for handle at index *i*. Part of the automated handle interface.

**Modifier Specific Methods**

- [`ObjectData.CheckDirty()`](#c4d.plugins.ObjectData.CheckDirty): Override - Called to check for a change manually.
- [`ObjectData.ModifyObject()`](#c4d.plugins.ObjectData.ModifyObject): Override - Called when an object plugin should modify the passed object.

**Particle Specific Methods**

- [`ObjectData.ModifyParticles()`](#c4d.plugins.ObjectData.ModifyParticles): Override - Called for modifying particles.

## Members <a id="members"></a>

### Generic Methods <a id="c4d.plugins.ObjectData-method-Generic-Methods"></a>

#### `ObjectData.AddToExecution(self, op, list)` <a id="c4d.plugins.ObjectData.AddToExecution"></a>

Override - By default this function returns *False*.  
Then Cinema 4D will call [`Execute()`](#c4d.plugins.ObjectData.Execute) at the priority specified by the user in the *EXPRESSION_PRIORITY* parameter of the container.

If you override this function and return *True*, then you can insert your own points of execution in the list by calling for example.

```python
list.Add(op, c4d.EXECUTIONPRIORITY_ANIMATION, 0)
list.Add(op, c4d.EXECUTIONPRIORITY_GENERATOR, 0)
```

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.
- **list** ([*c4d.plugins.PriorityList*](../../../PriorityList/index.md#c4d.plugins.PriorityList)) – The priority list to add your object’s execution points to.

**Return type:** bool

**Returns:** **True** if you override this function and has added stuff to list.

#### `ObjectData.Draw(self, op, drawpass, bd, bh)` <a id="c4d.plugins.ObjectData.Draw"></a>

Override - Called when the display is updated for you to display some visual element of your op in the 3D view.

> **Note:** This function is called in a threaded context. Please see the [important information](../../../../../manuals/manual_scene_execution.md#threading-information) about threading.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.

- **drawpass** (*int*) –

  One of the following flags:

  |   |   |
  |---|---|
  | *DRAWPASS_OBJECT* | Object pass. |
  | *DRAWPASS_BOX* | Box pass. |
  | *DRAWPASS_HANDLES* | Handle pass. |
  | *DRAWPASS_HIGHLIGHTS* | Highlights pass. |
  | *DRAWPASS_XRAY* | X-Ray pass. |

  > **Warning:**
  >
  > Only draw in *DRAWPASS_HIGHLIGHTS* if you **really** know what you are doing.  
  > Otherwise **always** check the *drawpass* and then **do not** draw if it is *DRAWPASS_HIGHLIGHTS*.

  Here is an example.

  ```python
  def Draw(self, op, drawpass, bd, bh):

      if drawpass==c4d.DRAWPASS_HIGHLIGHTS:
          return c4d.DRAWRESULT_SKIP

      # Put here your drawing operations

      return c4d.DRAWRESULT_OK
  ```

  > **Warning:**
  >
  > Only draw the object in one pass : *DRAWPASS_OBJECT*.  
  > The object’s appearance may change if you draw the same object in multiple passes.

- **bd** ([*c4d.BaseDraw*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The editor’s view.

- **bh** ([*c4d.plugins.BaseDrawHelp*](../../../BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp)) – The [`BaseDrawHelp`](../../../BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp) editor’s view.

**Return type:** int

**Returns:**

Success of drawing into the editor view:

| Symbol ID | Description |
|---|---|
| DRAWRESULT_FAILURE | There was an error while drawing. |
| DRAWRESULT_OK | Something was drawn. |
| DRAWRESULT_SKIP | There was nothing to draw in the pass. |

#### `ObjectData.DrawShadow(self, op, bd, bh)` <a id="c4d.plugins.ObjectData.DrawShadow"></a>

Called during the shadow pass instead of the [`Draw()`](#c4d.plugins.ObjectData.Draw) method.

*New in version R14.014.*

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.
- **bd** ([*c4d.BaseDraw*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The editor’s view.
- **bh** ([*c4d.plugins.BaseDrawHelp*](../../../BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp)) – The [`BaseDrawHelp`](../../../BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp) editor’s view.

**Return type:** int

**Returns:**

Success of drawing into the editor view:

| Symbol ID | Description |
|---|---|
| DRAWRESULT_FAILURE | There was an error while drawing. |
| DRAWRESULT_OK | Something was drawn. |
| DRAWRESULT_SKIP | There was nothing to draw in the pass. |

#### `ObjectData.Execute(self, op, doc, bt, priority, flags)` <a id="c4d.plugins.ObjectData.Execute"></a>

Override - Called at the point in the priority pipeline specified by [`AddToExecution()`](#c4d.plugins.ObjectData.AddToExecution), or the lack thereof.

> **Note:**
>
> This function is called in a thread context.  
> Please see the [important information](../../../../../manuals/manual_scene_execution.md#threading-information) about threading.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.

- **doc** ([*c4d.documents.BaseDocument*](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The host document of the object.

- **bt** (*Optional*[*c4d.BaseThread*]) – Currently not used.

- **priority** (*int*) –

  The priority of this call to [`Execute()`](#c4d.plugins.ObjectData.Execute) in the pipeline. Standard values are:

  |   |   |
  |---|---|
  | *EXECUTIONPRIORITY_INITIAL* | Initial. |
  | *EXECUTIONPRIORITY_ANIMATION* | Animation. |
  | *EXECUTIONPRIORITY_ANIMATION_NLA* | NLA. |
  | *EXECUTIONPRIORITY_EXPRESSION* | Expression. |
  | *EXECUTIONPRIORITY_DYNAMICS* | Dynamics. |
  | *EXECUTIONPRIORITY_GENERATOR* | Generators. |
  | *EXECUTIONPRIORITY_SCENENODE* | Scene nodes. |
  | *EXECUTIONPRIORITY_FORCE* | Highest priority that will ensure execution even if the execution pipeline is cancelled before. Only use this to e.g. release locks or do super-fast non-blocking operations. |

- **flags** (*int*) –

  A combination of the following flags:

  |   |   |
  |---|---|
  | *EXECUTIONFLAGS_NONE* | None. |
  | *EXECUTIONFLAGS_ANIMATION* | Animation is calculated. |
  | *EXECUTIONFLAGS_EXPRESSION* | Expressions are calculated. |
  | *EXECUTIONFLAGS_CACHEBUILDING* | Cache building is done. |
  | *EXECUTIONFLAGS_CAMERAONLY* | Only camera dependent expressions shall be executed. |
  | *EXECUTIONFLAGS_INDRAG* | Pipeline is done within scrubbing. |
  | *EXECUTIONFLAGS_INMOVE* | Pipeline is done within moving. |
  | *EXECUTIONFLAGS_RENDER* | The external renderer (Picture Viewer) is running. |
  | *EXECUTIONFLAGS_ALLOW_PRIORITYSHIFT* | *New in version R18:* Allow to shift the priority with the priority shift tag. Private. |

**Return type:** int

**Returns:**

The result:

|   |   |
|---|---|
| *EXECUTIONRESULT_OK* | OK. |
| *EXECUTIONRESULT_USERBREAK* | User break. |
| *EXECUTIONRESULT_MEMORYERROR* | Not enough memory. |

#### `ObjectData.GetContour(self, op, doc, lod, bt)` <a id="c4d.plugins.ObjectData.GetContour"></a>

Override - Return a spline contour. For spline objects only.

> **Note:**
>
> This function is called in a thread context.  
> Please see the [important information](../../../../../manuals/manual_scene_execution.md#threading-information) about threading.

> **Note:**
>
> Splines created through [`GetContour()`](#c4d.plugins.ObjectData.GetContour) are cached. So if the generator does not produce any output (e.g. when the user chose wrong settings).  
> It must at least return an (empty) Ospline object, otherwise Cinema 4D will try to rebuild the cache again and again.  
> To make this frame dependent, [`CheckDirty()`](#c4d.plugins.ObjectData.CheckDirty) can be overloaded to set the object dirty if a certain condition has changed.  
> Only return **None** in the case of a memory error.

> **Warning:** Must not be overridden for non-spline objects.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.
- **doc** ([*c4d.documents.BaseDocument*](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document containing the plugin object.
- **lod** (*int*) – The level of detail.
- **bt** ([*c4d.threading.BaseThread*](../../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)) – The calling thread.

**Return type:** Optional[[c4d.SplineObject](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/SplineObject/index.md#c4d.SplineObject)]

**Returns:** The newly allocated spline or **None** only in the case of a memory error.

#### `ObjectData.GetDimension(self, op, mp, rad)` <a id="c4d.plugins.ObjectData.GetDimension"></a>

Override - Return the boundaries of your object.

```python
def GetDimension(self, op, mp, rad):
    '''
    (i) When the method runs without a raised exception
    mp and rad will be internally copied, otherwise they
    are ignored.
    '''

    mp.x = self.x_size   # correct
    mp.y = self.y_size   # correct
    mp.z = self.z_size   # correct

    mp = c4d.Vector(x_size, y_size, z_size)    #!!! wrong !!! do not rebind mp!
    #this assign applies for 'rad' as well
    return
```

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.
- **mp** ([*c4d.Vector*](../../../../c4d/Vector/index.md#c4d.Vector)) – Assign the center point of the bounding box to this vector.
- **rad** ([*c4d.Vector*](../../../../c4d/Vector/index.md#c4d.Vector)) – Assign the XYZ bounding box radius to this vector.

#### `ObjectData.GetVirtualObjects(self, op, hh)` <a id="c4d.plugins.ObjectData.GetVirtualObjects"></a>

Override - Return an object chain of a generator object (e.g. a polygonal object).

> **Note:**
>
> This function is called in a thread context.  
> Please see the [important information](../../../../../manuals/manual_scene_execution.md#threading-information) about threading.

> **Warning:** Must not be overridden for non-generator objects.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.

- **hh** ([*c4d.plugins.HierarchyHelp*](../../../HierarchyHelp/index.md#c4d.plugins.HierarchyHelp)) –

  A hierarchy helper for the operation.  
  Pass this to virtual objects hierarchy methods `BaseObject.GetCache()`, `BaseObject.CheckCache()`, `BaseObject.GetAndCheckHierarchyClone()`, `BaseObject.GetHierarchyClone()`.

**Return type:** Optional[[c4d.BaseObject](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:**

The newly allocated object chain, or **None** if a memory error occured.

> **Note:**
>
> Only return **None** in the case of a memory error.  
> If the generator does not produce any output (e.g. when the user chooses wrong settings) it must at least return an (empty) **Onull** object, otherwise Cinema 4D will try to rebuild the cache again and again.

#### `ObjectData.SetOptimizeCache(self, cache)` <a id="c4d.plugins.ObjectData.SetOptimizeCache"></a>

Sets the cache optimization for the node.  
If **True**, the cache of the object will only be rebuilt, have its *GetVirtualObjects* method called, when its  
data container changed, i.e., the node is *DIRTYFLAGS_DATA*. Otherwise, *GetVirtualObjects* will be called on each  
scene update and it is up to the plugin to decide if it needs to rebuild its cache or not. See the *py-rounded_tube_r13*  
for a practical example of both approaches.

**Parameters:**

**cache** (*bool*) –

If **True**, the cache of the node will only be rebuilt when its data container changed.  
If *False*, it will be rebuilt on each scene update.

### Handle Methods <a id="c4d.plugins.ObjectData-method-Handle-Methods"></a>

#### `ObjectData.DetectHandle(self, op, bd, x, y, qualifier)` <a id="c4d.plugins.ObjectData.DetectHandle"></a>

Override - Manually detect a click on a handle.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.

- **bd** ([*c4d.BaseDraw*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The editor’s view.

- **x** (*int*) – The mouse X coordinate.

- **y** (*int*) – The mouse Y coordinate.

- **qualifier** (*int*) –

  Any qualifier keys that were pressed. These are defined in [`c4d.gui`](../../../../c4d.gui/index.md#c4d.gui):

  |   |   |
  |---|---|
  | *QUALIFIER_SHIFT* | *SHIFT* key. |
  | *QUALIFIER_CTRL* | CTRL key. |
  | *QUALIFIER_MOUSEHIT* | Indication in `ObjectData.DetectHandle()` that the user pressed the mouse (`ObjectData.DetectHandle()` is also called for cursor information, when hovering over a handle). For instance if *QUALIFIER_MOUSEHIT* and *QUALIFIER_CTRL* are set, `ObjectData.DetectHandle()` could create a new element. |

**Return type:** int

**Returns:** The handle ID that is to be passed to [`MoveHandle()`](#c4d.plugins.ObjectData.MoveHandle)

#### `ObjectData.GetHandle(self, op, i, info)` <a id="c4d.plugins.ObjectData.GetHandle"></a>

Called to get the information for handle at index *i*. Part of the automated handle interface.

*New in version R18.011.*

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.
- **i** (*int*) – The handle index.
- **info** ([*c4d.HandleInfo*](../../../../c4d/HandleInfo/index.md#c4d.HandleInfo)) – Fill with the handle information.

#### `ObjectData.GetHandleCount(self, op)` <a id="c4d.plugins.ObjectData.GetHandleCount"></a>

Called to get the number of handles the object has. Part of the automated handle interface.

*New in version R18.011.*

**Parameters:** **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.

**Return type:** int

**Returns:** The number of handles for the object.

#### `ObjectData.MoveHandle(self, op, undo, mouse_pos, hit_id, qualifier, bd)` <a id="c4d.plugins.ObjectData.MoveHandle"></a>

Override - Move a handle manually.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.

- **undo** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – This is a copy of the object that must not be modified during the move handle.

- **mouse_pos** ([*c4d.Vector*](../../../../c4d/Vector/index.md#c4d.Vector)) – The current mouse position.

- **hit_id** (*int*) – The handle ID returned from [`DetectHandle()`](#c4d.plugins.ObjectData.DetectHandle)

- **qualifier** (*int*) –

  Any qualifier keys that were pressed.  
  These are defined in [`c4d.gui`](../../../../c4d.gui/index.md#c4d.gui):

  |   |   |
  |---|---|
  | *QUALIFIER_SHIFT* | *SHIFT* key. |
  | *QUALIFIER_CTRL* | CTRL key. |
  | *QUALIFIER_MOUSEHIT* | Indication in `ObjectData.DetectHandle()` that the user pressed the mouse (`ObjectData.DetectHandle()` is also called for cursor information, when hovering over a handle). For instance if *QUALIFIER_MOUSEHIT* and *QUALIFIER_CTRL* are set, `ObjectData.DetectHandle()` could create a new element. |

- **bd** ([*c4d.BaseDraw*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The editor’s view.

**Return type:** bool

**Returns:** Success of modifying the handle.

#### `ObjectData.SetHandle(self, op, i, p, info)` <a id="c4d.plugins.ObjectData.SetHandle"></a>

Called to set the information for handle at index *i*. Part of the automated handle interface.  
Called when the user has moved handle *i* to position *p*. Update the object’s internal data accordingly (e.g. parameter values etc).

*New in version R18.011.*

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.
- **i** (*int*) – The handle index.
- **p** ([*c4d.Vector*](../../../../c4d/Vector/index.md#c4d.Vector)) – The new handle position.
- **info** ([*c4d.HandleInfo*](../../../../c4d/HandleInfo/index.md#c4d.HandleInfo)) – The handle information.

### Modifier Specific Methods <a id="c4d.plugins.ObjectData-method-Modifier-Specific-Methods"></a>

#### `ObjectData.CheckDirty(self, op, doc)` <a id="c4d.plugins.ObjectData.CheckDirty"></a>

Override - Called to check for a change manually.  
For example this will update every frame:

```python
def CheckDirty(self, op, doc):

    frame = doc.GetTime().GetFrame(doc.GetFps())
    if frame != lastFrame:
        lastFrame = frame
        op.SetDirty(c4d.DIRTYFLAGS_DATA)
```

> **Note:**
>
> This function is called in a thread context.  
> Please see the [important information](../../../../../manuals/manual_scene_execution.md#threading-information) about threading.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.
- **doc** ([*c4d.documents.BaseDocument*](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document containing the plugin object.

#### `ObjectData.ModifyObject(self, mod, doc, op, op_mg, mod_mg, lod, flags, thread)` <a id="c4d.plugins.ObjectData.ModifyObject"></a>

Override - Called when an object plugin should modify the passed object.

> **Note:**
>
> This function is called in a thread context.  
> Please see the [important information](../../../../../manuals/manual_scene_execution.md#threading-information) about threading.

> **Warning:** Must not be overridden for non-modifier objects.

**Parameters:**

- **mod** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The modifier object.
- **doc** ([*c4d.documents.BaseDocument*](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document containing the plugin object.
- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object to modify.
- **op_mg** ([*c4d.Matrix*](../../../../c4d/Matrix/index.md#c4d.Matrix)) – The object’s world matrix.
- **mod_mg** ([*c4d.Matrix*](../../../../c4d/Matrix/index.md#c4d.Matrix)) – The modifier object’s world matrix.
- **lod** (*float*) – The level of detail.
- **flags** (*int*) – Currently unused.
- **thread** ([*c4d.threading.BaseThread*](../../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)) – The calling thread.

**Return type:** bool

**Returns:** Success of modifying the object.

### Particle Specific Methods <a id="c4d.plugins.ObjectData-method-Particle-Specific-Methods"></a>

#### `ObjectData.ModifyParticles(self, op, pp, ss, pcnt, diff)` <a id="c4d.plugins.ObjectData.ModifyParticles"></a>

Override - Called for modifying particles. This is for particle modifiers only.

> **Note:**
>
> This function is called in a thread context.  
> Please see the [important information](../../../../../manuals/manual_scene_execution.md#threading-information) about threading.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The established base object.

- **pp** (*List*[[*c4d.modules.particles.Particle*](../../../../c4d.modules/particles/Particle/index.md#c4d.modules.particles.Particle)]) –

  The initial element of the Particle list.

  > **Note:** This list is used to read the particles information only, the particles should not be modified.

- **ss** (*List*[[*c4d.modules.particles.BaseParticle*](../../../../c4d.modules/particles/BaseParticle/index.md#c4d.modules.particles.BaseParticle)]) – The initial element of the [`BaseParticle`](../../../../c4d.modules/particles/BaseParticle/index.md#c4d.modules.particles.BaseParticle) list. Modify the elements in this list to change the velocity of the particle.

- **pcnt** (*int*) – The number of particles in the [`Particle`](../../../../c4d.modules/particles/Particle/index.md#c4d.modules.particles.Particle) and [`BaseParticle`](../../../../c4d.modules/particles/BaseParticle/index.md#c4d.modules.particles.BaseParticle) list.

- **diff** (*float*) – The time delta for the particles movement in seconds. Usually the difference in time between two frames, but this can be different for such functions as motion blur.
