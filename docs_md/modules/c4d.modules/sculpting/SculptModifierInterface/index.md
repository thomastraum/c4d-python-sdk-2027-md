<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/sculpting/SculptModifierInterface/index.html -->

# c4d.modules.sculpting.SculptModifierInterface <a id="c4d-modules-sculpting-sculptmodifierinterface"></a>

## *class* `c4d.modules.sculpting.SculptModifierInterface` <a id="c4d.modules.sculpting.SculptModifierInterface"></a>

This interface lets apply the affects of a sculpting modifier to any Polygon Object.

It allows to use the same algorithms outside of the sculpting system itself and deform a Polygon Object using the same brush algorithms that the sculpt brushes use.

*New in version R16.021.*

## Overview <a id="overview"></a>

**Initialization And Brush Configuration**

- [`SculptModifierInterface.Clear()`](#c4d.modules.sculpting.SculptModifierInterface.Clear): Clears the interface.
- [`SculptModifierInterface.GetDefaultData()`](#c4d.modules.sculpting.SculptModifierInterface.GetDefaultData): Gets the default brush data setting.
- [`SculptModifierInterface.Init()`](#c4d.modules.sculpting.SculptModifierInterface.Init): Initializes the interface so that you can apply modifiers to the given Polygon Object.
- [`SculptModifierInterface.SetData()`](#c4d.modules.sculpting.SculptModifierInterface.SetData): Sets the brush data and modifier data for the next dab to be drawn.

**Modifier Discovery And Application**

- [`SculptModifierInterface.ApplyModifier()`](#c4d.modules.sculpting.SculptModifierInterface.ApplyModifier): Applies a modifier to the Polygon Object near the specified *vertex*.
- [`SculptModifierInterface.ApplyModifierExact()`](#c4d.modules.sculpting.SculptModifierInterface.ApplyModifierExact): Exactly applies a modifier to the Polygon Object near the specified *vertex* using the given *hitpoint*.
- [`SculptModifierInterface.GetModifierCount()`](#c4d.modules.sculpting.SculptModifierInterface.GetModifierCount): Gets the number of available modifiers that are currently registered and able to be used.
- [`SculptModifierInterface.GetModifierInfo()`](#c4d.modules.sculpting.SculptModifierInterface.GetModifierInfo): Gets the information about a modifier given its *index*.

## Members <a id="members"></a>

### Initialization And Brush Configuration <a id="c4d.modules.sculpting.SculptModifierInterface-method-Initialization-And-Brush-Configuration"></a>

#### `SculptModifierInterface.Clear(self)` <a id="c4d.modules.sculpting.SculptModifierInterface.Clear"></a>

Clears the interface.  
This will free up any internal data that was required to apply modifiers to the initialized [`PolygonObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) in [`Init()`](#c4d.modules.sculpting.SculptModifierInterface.Init).

#### `SculptModifierInterface.GetDefaultData(self)` <a id="c4d.modules.sculpting.SculptModifierInterface.GetDefaultData"></a>

Gets the default brush data setting. These settings can be found in *toolsculptbrushbase.h*.

**Return type:** [c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The container containing all the default brush settings.

#### `SculptModifierInterface.Init(self, poly)` <a id="c4d.modules.sculpting.SculptModifierInterface.Init"></a>

Initializes the interface so that you can apply modifiers to the given Polygon Object.

**Parameters:** **poly** ([*c4d.PolygonObject*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject)) – The Polygon Object that you wish to apply modifiers to.

**Return type:** bool

**Returns:** **True** if successfully initialized.

#### `SculptModifierInterface.SetData(self, brushData, modifierData)` <a id="c4d.modules.sculpting.SculptModifierInterface.SetData"></a>

Sets the brush data and modifier data for the next dab to be drawn.  
This must be called before [`ApplyModifier()`](#c4d.modules.sculpting.SculptModifierInterface.ApplyModifier). This will initialize any time consuming data before you make repeated calls to [`ApplyModifier()`](#c4d.modules.sculpting.SculptModifierInterface.ApplyModifier).  
Operations that take time are things such as enabling stamps, changing a stamps texture, calculation of the falloff values etc…

**Parameters:**

- **brushData** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The brush data settings. By default you can just use the container returned by [`GetDefaultData()`](#c4d.modules.sculpting.SculptModifierInterface.GetDefaultData).

- **modifierData** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) –

  The settings for the modifier itself. Each modifier is a [`BaseList2D`](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) node and could have its own settings.  
  Refer to each modifiers BM file (*BMknife.h* as an example).

**Return type:** bool

**Returns:** **True** if the data was correctly set.

### Modifier Discovery And Application <a id="c4d.modules.sculpting.SculptModifierInterface-method-Modifier-Discovery-And-Application"></a>

#### `SculptModifierInterface.ApplyModifier(self, modifierId, vertex, brushData, modifierData, respectselections=False)` <a id="c4d.modules.sculpting.SculptModifierInterface.ApplyModifier"></a>

Applies a modifier to the Polygon Object near the specified *vertex*.

**Parameters:**

- **modifierId** (*int*) – The ID of the modifier to apply. This is retrieved from a call to [`GetModifierInfo()`](#c4d.modules.sculpting.SculptModifierInterface.GetModifierInfo).

- **vertex** (*int*) – The index of the vertex on the PolygonObject where you want to apply the modifier to.

- **brushData** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The brush data settings. By default you can just use the container returned by [`GetDefaultData()`](#c4d.modules.sculpting.SculptModifierInterface.GetDefaultData).

- **modifierData** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) –

  The settings for the modifier itself. Each modifier is a [`BaseList2D`](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) node and could have its own settings.  
  Refer to each modifiers BM file (*BMknife.h* as an example).

- **respectselections** (*bool*) – Pass **True** for the modifier to respect any polygon or point selections on the Polygon Object. Default to **False**.

**Return type:** bool

**Returns:** **True** if the modifier was successfully applied.

#### `SculptModifierInterface.ApplyModifierExact(self, modifierId, vertex, brushData, modifierData, hitpoint, lasthitpoint, respectselections=False)` <a id="c4d.modules.sculpting.SculptModifierInterface.ApplyModifierExact"></a>

Exactly applies a modifier to the Polygon Object near the specified *vertex* using the given *hitpoint*.

**Parameters:**

- **modifierId** (*int*) – The ID of the modifier to apply. This is retrieved from a call to [`GetModifierInfo()`](#c4d.modules.sculpting.SculptModifierInterface.GetModifierInfo).

- **vertex** (*int*) – The index of the vertex on the PolygonObject where you want to apply the modifier to.

- **brushData** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The brush data settings. By default you can just use the container returned by [`GetDefaultData()`](#c4d.modules.sculpting.SculptModifierInterface.GetDefaultData).

- **modifierData** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) –

  The settings for the modifier itself. Each modifier is a [`BaseList2D`](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) node and could have its own settings.  
  Refer to each modifiers BM file (*BMknife.h* as an example).

- **respectselections** (*bool*) – Pass **True** for the modifier to respect any polygon or point selections on the Polygon Object. Default to **False**.

- **hitpoint** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The exact hitpoint on the surface of a polygon that is connected to the passed *vertex*.

- **lasthitpoint** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) –

  The last hitpoint from the previous call to [`ApplyModifier()`](#c4d.modules.sculpting.SculptModifierInterface.ApplyModifier).  
  This is used to determine the direction of the dab for modifiers such as the knife and pinch modifier.

**Return type:** bool

**Returns:** **True** if the modifier was successfully applied.

#### `SculptModifierInterface.GetModifierCount(self)` <a id="c4d.modules.sculpting.SculptModifierInterface.GetModifierCount"></a>

Gets the number of available modifiers that are currently registered and able to be used.

**Return type:** int

**Returns:** The number of Modifiers.

#### `SculptModifierInterface.GetModifierInfo(self, index)` <a id="c4d.modules.sculpting.SculptModifierInterface.GetModifierInfo"></a>

Gets the information about a modifier given its *index*.

**Parameters:** **index** (*int*) – The index into the list of available modifiers. [`GetModifierCount()`](#c4d.modules.sculpting.SculptModifierInterface.GetModifierCount) returns the number of modifiers.

**Return type:** dict{**id**: int, **name**: str}

**Returns:** The modifier information.
