<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/sculpting/SculptBrushParams/index.html -->

# c4d.modules.sculpting.SculptBrushParams <a id="c4d-modules-sculpting-sculptbrushparams"></a>

## *class* `c4d.modules.sculpting.SculptBrushParams` <a id="c4d.modules.sculpting.SculptBrushParams"></a>

The parameters to pass in when registering a Sculpting Brush.

*New in version R16.021.*

## Overview <a id="overview"></a>

**Interaction Feedback**

- [`SculptBrushParams.EnableDrawDirection()`](#c4d.modules.sculpting.SculptBrushParams.EnableDrawDirection): When enabled the Draw Direction UI will appear in the settings tab.
- [`SculptBrushParams.EnableMouseData()`](#c4d.modules.sculpting.SculptBrushParams.EnableMouseData): Enables/disables the callback for the `SculptBrushToolData.MouseData()` method.
- [`SculptBrushParams.EnableNonModelPickMode()`](#c4d.modules.sculpting.SculptBrushParams.EnableNonModelPickMode): Does the brush do anything if the user clicks off of a model?
- [`SculptBrushParams.EnablePressureHUD()`](#c4d.modules.sculpting.SculptBrushParams.EnablePressureHUD): When enabled will display the pressure value in the sculpting size/pressure HUD.

**Operation Modes**

- [`SculptBrushParams.SetBrushMode()`](#c4d.modules.sculpting.SculptBrushParams.SetBrushMode): Specifies what type of brush this is (grab or normal).
- [`SculptBrushParams.SetFirstHitPointType()`](#c4d.modules.sculpting.SculptBrushParams.SetFirstHitPointType): Specifies what should happen when the user first clicks on model before dragging.
- [`SculptBrushParams.SetFloodType()`](#c4d.modules.sculpting.SculptBrushParams.SetFloodType): Specifies what kind of data the flood operation will change (points or mask).

**Selection And Surface**

- [`SculptBrushParams.EnableBackfaceSculpting()`](#c4d.modules.sculpting.SculptBrushParams.EnableBackfaceSculpting): Tells the system that this brush supports backface sculpting and that the backface option should be displayed in the brushes settings.
- [`SculptBrushParams.EnableFillToolIsolatedPointRemover()`](#c4d.modules.sculpting.SculptBrushParams.EnableFillToolIsolatedPointRemover): When this is enabled it will tell the Fill algorithm to remove any isolated points.
- [`SculptBrushParams.EnableRespectSelections()`](#c4d.modules.sculpting.SculptBrushParams.EnableRespectSelections): When enabled will tell the brush to respect Point and Polygon selections when in Point or Polygon mode respectively.

**State And Undo**

- [`SculptBrushParams.SetPolygonObjectDirtyFlags()`](#c4d.modules.sculpting.SculptBrushParams.SetPolygonObjectDirtyFlags): Sets which flags should be checked to do a rebuild of the collision structure for a [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject).
- [`SculptBrushParams.SetUndoType()`](#c4d.modules.sculpting.SculptBrushParams.SetUndoType): Specifies what kind of data the brush will be changing and storing in the undo system (point or mask).

**Tool Features**

- [`SculptBrushParams.EnableBuildup()`](#c4d.modules.sculpting.SculptBrushParams.EnableBuildup): Does the brush use the buildup slider?
- [`SculptBrushParams.EnableFlood()`](#c4d.modules.sculpting.SculptBrushParams.EnableFlood): Does the brush have a Flood function?
- [`SculptBrushParams.EnableInvertCheckbox()`](#c4d.modules.sculpting.SculptBrushParams.EnableInvertCheckbox): Does the brush use the invert checkbox?
- [`SculptBrushParams.EnableModifier()`](#c4d.modules.sculpting.SculptBrushParams.EnableModifier): Tells the system that this brush can use modifiers from other brushes (display the modifiers tab).
- [`SculptBrushParams.EnableStamp()`](#c4d.modules.sculpting.SculptBrushParams.EnableStamp): Does the brush use stamps?
- [`SculptBrushParams.EnableStencil()`](#c4d.modules.sculpting.SculptBrushParams.EnableStencil): Does the brush use stencils?
- [`SculptBrushParams.EnableToolSpecificSmooth()`](#c4d.modules.sculpting.SculptBrushParams.EnableToolSpecificSmooth): Does the brush have its own smooth operation that gets used when you press the shift key?

## Members <a id="members"></a>

### Interaction Feedback <a id="c4d.modules.sculpting.SculptBrushParams-method-Interaction-Feedback"></a>

#### `SculptBrushParams.EnableDrawDirection(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnableDrawDirection"></a>

When enabled the Draw Direction UI will appear in the settings tab.  
Calls can then be made to `BrushDabData.GetDrawDirectionNormal()` to get the direction of the normal based on the currently selected Draw Direction.

**Parameters:** **enable** (*bool*) – Set to **True** to display the Draw Direction UI. Disabled by default.

#### `SculptBrushParams.EnableMouseData(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnableMouseData"></a>

Enables/disables the callback for the `SculptBrushToolData.MouseData()` method.

*New in version R17.048.*

**Parameters:**

**enable** (*bool*) –

**True** if the brush needs the `SculptBrushToolData.MouseData()` callback, otherwise **False**.  
Default is **True**.

#### `SculptBrushParams.EnableNonModelPickMode(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnableNonModelPickMode"></a>

Does the brush do anything if the user clicks off of a model?  
I.e. have you implemented `SculptBrushToolData.HandleNonModelPickMode()` and `SculptBrushToolData.DrawNonModelPickMode()`?  
Private.

**Parameters:**

**enable** (*bool*) –

**True** if the brush has implemented `SculptBrushToolData.HandleNonModelPickMode()` and `SculptBrushToolData.DrawNonModelPickMode()`, otherwise **False**.  
Default is **False**.

#### `SculptBrushParams.EnablePressureHUD(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnablePressureHUD"></a>

When enabled will display the pressure value in the sculpting size/pressure HUD.

**Parameters:**

**enable** (*bool*) –

**True** if the brush should dispay the pressure value, otherwise **False**.  
Default is **True**.

### Operation Modes <a id="c4d.modules.sculpting.SculptBrushParams-method-Operation-Modes"></a>

#### `SculptBrushParams.SetBrushMode(self, mode)` <a id="c4d.modules.sculpting.SculptBrushParams.SetBrushMode"></a>

Specifies what type of brush this is (grab or normal).

**Parameters:** **mode** (*int*) – The brush mode. Default is *SCULPTBRUSHMODE_NORMAL*.

#### `SculptBrushParams.SetFirstHitPointType(self, type)` <a id="c4d.modules.sculpting.SculptBrushParams.SetFirstHitPointType"></a>

Specifies what should happen when the user first clicks on model before dragging.

**Parameters:** **type** (*int*) – The first hitpoint type. Default is *FIRSTHITPPOINTTYPE_SELECTED*.

#### `SculptBrushParams.SetFloodType(self, type)` <a id="c4d.modules.sculpting.SculptBrushParams.SetFloodType"></a>

Specifies what kind of data the flood operation will change (points or mask).

**Parameters:** **type** (*int*) – The flood data type. Default is *SCULPTBRUSHDATATYPE_POINT*.

### Selection And Surface <a id="c4d.modules.sculpting.SculptBrushParams-method-Selection-And-Surface"></a>

#### `SculptBrushParams.EnableBackfaceSculpting(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnableBackfaceSculpting"></a>

Tells the system that this brush supports backface sculpting and that the backface option should be displayed in the brushes settings.

*New in version R17.032.*

**Parameters:**

**enable** (*bool*) –

**True** if the brush supports backface sculpting, otherwise **False**.  
Default is **False**.

#### `SculptBrushParams.EnableFillToolIsolatedPointRemover(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnableFillToolIsolatedPointRemover"></a>

When this is enabled it will tell the Fill algorithm to remove any isolated points. That is any points that are selected but have no neighboring selections.  
This can happen on high resolution meshes due to the nature of the hit detection against screen space pixels defined by the fill tools.  
By setting this to **False** it will keep any isolated points that are selected.  
This is set to **True** by default so isolated points are removed before being sent to the `SculptBrushToolData.ApplyDab()` function.

**Parameters:**

**enable** (*bool*) –

**True** if the brush should remove isolated points, **False** if it should keep them.  
Default is **True**.

#### `SculptBrushParams.EnableRespectSelections(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnableRespectSelections"></a>

When enabled will tell the brush to respect Point and Polygon selections when in Point or Polygon mode respectively.

**Parameters:**

**enable** (*bool*) –

**True** if the brush should respect selections, otherwise **False**.  
Default is **False**.

### State And Undo <a id="c4d.modules.sculpting.SculptBrushParams-method-State-And-Undo"></a>

#### `SculptBrushParams.SetPolygonObjectDirtyFlags(self, type)` <a id="c4d.modules.sculpting.SculptBrushParams.SetPolygonObjectDirtyFlags"></a>

Sets which flags should be checked to do a rebuild of the collision structure for a [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject).  
These flags are used to check against the PolygonObjects dirty flags when a stroke is about to be done on a [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject).  
If the flags being checked are dirty since the last check then the collision cache structure for the object will be rebuilt.  
This can be used in cases such as the Select Brush where you are not directly moving the points of the model during a stroke.  
So you can set all the flags except the **DIRTYFLAGS_SELECT** - using something like **DIRTYFLAGS_ALL & ~DIRTYFLAGS_SELECT** - to ensure that the object is not recalculated when just the select flags are changed.  
In all other cases the object will be rebuilt.

*New in version R17.032.*

**Parameters:**

**type** (*int*) –

The dirty flags to check:

Expresses dirty state categories for a single scene element. Unlike `HDIRTYFLAGS`, these flags only track changes on the element itself.

|   |   |
|---|---|
| *DIRTYFLAGS_NONE* | Signals no state. |
| *DIRTYFLAGS_MATRIX* | Signals that the matrix of a [`BaseObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) has changed. |
| *DIRTYFLAGS_DATA* | Signals that container or parameter data of a scene element has changed. |
| *DIRTYFLAGS_SELECT* | Signals that a point, edge, or polygon selection of a [`BaseObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) has changed. |
| *DIRTYFLAGS_CACHE* | Signals that the cache of a [`BaseObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) has changed or been rebuilt. |
| *DIRTYFLAGS_CHILDREN* | Signals that owned child data of a scene element, such as animation keys, has changed. |
| *DIRTYFLAGS_DESCRIPTION* | Signals that the description of a scene element has changed. |
| *DIRTYFLAGS_VISIBILITY* | Signals that the visibility state of a scene element has changed. |
| *DIRTYFLAGS_SELECTION_OBJECTS* | Signals that the object selection of a [`BaseDocument`](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) has changed. |
| *DIRTYFLAGS_SELECTION_TAGS* | Signals that the tag selection of a [`BaseDocument`](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) has changed. |
| *DIRTYFLAGS_SELECTION_MATERIALS* | Signals that the material selection of a [`BaseDocument`](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) has changed. |
| *DIRTYFLAGS_ALL* | Signals all states. |

#### `SculptBrushParams.SetUndoType(self, type)` <a id="c4d.modules.sculpting.SculptBrushParams.SetUndoType"></a>

Specifies what kind of data the brush will be changing and storing in the undo system (point or mask).

**Parameters:** **type** (*int*) – The brush data type. Default is *SCULPTBRUSHDATATYPE_POINT*.

### Tool Features <a id="c4d.modules.sculpting.SculptBrushParams-method-Tool-Features"></a>

#### `SculptBrushParams.EnableBuildup(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnableBuildup"></a>

Does the brush use the buildup slider?  
Lets the system know if you are using the buildup slider or not.

Note that by default the buildup slider is not part of the base *.res* file so you will need to add it yourself to your own brushes *.res* file.  
To do this just add the following data to your .res file exactly as shown:

```cpp
GROUP MDATA_SCULPTBRUSH_SETTINGS_GROUP
{
    COLUMNS 3;
    REAL MDATA_SCULPTBRUSH_SETTINGS_BUILDUP { MIN 1; MAX 100; MINSLIDER 1; MAXSLIDER 100; CUSTOMGUI REALSLIDER; FIT_H; SCALE_H; }
    STATICTEXT { JOINENDSCALE; }
    STATICTEXT { JOINEND; }
}
```

**Parameters:**

**enable** (*bool*) –

**True** if the brush uses the buildup slider, otherwise **False**.  
Default is **False**.

#### `SculptBrushParams.EnableFlood(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnableFlood"></a>

Does the brush have a Flood function?  
I.e. have you implemented FloodSelectedLayer.

Note that by default the Flood button is not part of the base *.res* file so you will need to add it yourself to your own brushes *.res* file.  
To do this just add the following data to your .res file exactly as shown:

```cpp
GROUP MDATA_SCULPTBRUSH_SETTINGS_GROUP
{
    COLUMNS 3;
    BUTTON MDATA_SCULPTBRUSH_SETTINGS_FLOOD{ }
    STATICTEXT { JOINENDSCALE; }
    STATICTEXT { JOINEND; }
}
```

**Parameters:**

**enable** (*bool*) –

**True** if the brush has implemented a Flood function, otherwise **False**.  
Default is **False**.

#### `SculptBrushParams.EnableInvertCheckbox(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnableInvertCheckbox"></a>

Does the brush use the invert checkbox?  
Lets the system know if you are using the invert checkbox or not.

Note that by default the invert checkbox is not part of the base *.res* file so you will need to add it yourself to your own brushes *.res* file.  
To do this just add the following data to your .res file exactly as shown:

```cpp
GROUP MDATA_SCULPTBRUSH_SETTINGS_GROUP
{
    COLUMNS 3;
    BOOL MDATA_SCULPTBRUSH_SETTINGS_INVERT { }
    STATICTEXT { DUMMY; }
    STATICTEXT { DUMMY; }
}
```

**Parameters:**

**enable** (*bool*) –

**True** if the brush uses the invert checkbox, otherwise **False**.  
Default is **False**.

#### `SculptBrushParams.EnableModifier(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnableModifier"></a>

Tells the system that this brush can use modifiers from other brushes (display the modifiers tab).

**Parameters:** **enable** (*bool*) – Set to **True** if you want this brush to be able to use modifiers from other brushes.

#### `SculptBrushParams.EnableStamp(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnableStamp"></a>

Does the brush use stamps?  
Setting this to **False** will let the brush know that you are not going to be using stamps. This will free up some resource and computation time.  
Note that setting to **False** will also remove the tab from the brush interface.

**Parameters:** **enable** (*bool*) – **True** if the brush uses stamps, otherwise **False**. Default is **True**.

#### `SculptBrushParams.EnableStencil(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnableStencil"></a>

Does the brush use stencils?  
Settings this to **False** will let the brush know that you are not going to be using stencils. This will free up some resource and computation time.  
Note that setting to **False** will also remove the tab from the brush interface.

**Parameters:**

**enable** (*bool*) –

**True** if the brush uses stencils, otherwise **False**.  
Default is **True**.

#### `SculptBrushParams.EnableToolSpecificSmooth(self, enable)` <a id="c4d.modules.sculpting.SculptBrushParams.EnableToolSpecificSmooth"></a>

Does the brush have its own smooth operation that gets used when you press the shift key?  
You can check for this in the `SculptBrushToolData.ApplyDab()` method by checking if (GetBrushOverride() & *OVERRIDE_SMOOTHTOOL*) is **True** and then you can implement your own smooth method.  
Otherwise it will use the Smooth Brush for smoothing.

**Parameters:** **enable** (*bool*) – **True** if you are handling smoothing yourself, otherwise **False**. Default is **False**.
