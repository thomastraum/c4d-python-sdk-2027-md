<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/volume/VolumeBuilder/index.html -->

# c4d.modules.volume.VolumeBuilder <a id="c4d-modules-volume-volumebuilder"></a>

## *class* `c4d.modules.volume.VolumeBuilder` <a id="c4d.modules.volume.VolumeBuilder"></a>

The volume builder object class of type *Ovolumebuilder*.

*New in version R20.*

Parent Class:

- [`c4d.BaseObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

## Overview <a id="overview"></a>

**Input Object Management**

- [`VolumeBuilder.AddSceneObject()`](#c4d.modules.volume.VolumeBuilder.AddSceneObject): Adds a valid object from the document to the objects list.
- [`VolumeBuilder.ClearInputObjects()`](#c4d.modules.volume.VolumeBuilder.ClearInputObjects): Clears the objects list.
- [`VolumeBuilder.GetInputObject()`](#c4d.modules.volume.VolumeBuilder.GetInputObject): Retrieves the input object referenced at the given *index*.
- [`VolumeBuilder.GetInputObjectByType()`](#c4d.modules.volume.VolumeBuilder.GetInputObjectByType): Retrieves the input object with the given *type*.
- [`VolumeBuilder.GetInputObjectCount()`](#c4d.modules.volume.VolumeBuilder.GetInputObjectCount): Returns the number of objects in the list.
- [`VolumeBuilder.GetListEntryCount()`](#c4d.modules.volume.VolumeBuilder.GetListEntryCount): Returns the number of elements in the objects list containing folders.
- [`VolumeBuilder.InputObjectIsChild()`](#c4d.modules.volume.VolumeBuilder.InputObjectIsChild): Checks if object at *index* in the object list is a child of the generator.
- [`VolumeBuilder.RemoveObject()`](#c4d.modules.volume.VolumeBuilder.RemoveObject): Removes the object in the list at the given *index*.

**Input State**

- [`VolumeBuilder.GetEnable()`](#c4d.modules.volume.VolumeBuilder.GetEnable): Gets the enabled state for the input object at *index*.
- [`VolumeBuilder.GetSelected()`](#c4d.modules.volume.VolumeBuilder.GetSelected): Gets the selection state for the input object at *index*.
- [`VolumeBuilder.SetEnable()`](#c4d.modules.volume.VolumeBuilder.SetEnable): Sets the enabled state for the input object at *index*.
- [`VolumeBuilder.SetSelected()`](#c4d.modules.volume.VolumeBuilder.SetSelected): Sets the selection state for the input object at *index*.

**Magic Methods**

- [`VolumeBuilder.__init__()`](#c4d.modules.volume.VolumeBuilder.__init__): Creates a [`VolumeBuilder`](#c4d.modules.volume.VolumeBuilder).

**Operation Modes**

- [`VolumeBuilder.GetBoolMode()`](#c4d.modules.volume.VolumeBuilder.GetBoolMode): Gets the bool mode for the input object at *index*.
- [`VolumeBuilder.GetMixMode()`](#c4d.modules.volume.VolumeBuilder.GetMixMode): Gets the mix mode for the input object at *index*.
- [`VolumeBuilder.SetBoolMode()`](#c4d.modules.volume.VolumeBuilder.SetBoolMode): Sets the bool mode for the input object at *index*.
- [`VolumeBuilder.SetMixMode()`](#c4d.modules.volume.VolumeBuilder.SetMixMode): Sets the mix mode for the input object at *index*.

**Settings Access**

- [`VolumeBuilder.GetSettingsContainerForIndex()`](#c4d.modules.volume.VolumeBuilder.GetSettingsContainerForIndex): Returns the internal container for the settings of an input object at the given *index*.
- [`VolumeBuilder.GetSettingsContainerForObject()`](#c4d.modules.volume.VolumeBuilder.GetSettingsContainerForObject): Returns the internal container for the settings of an input object.

**Vector Mixing**

- [`VolumeBuilder.GetMixVectorMode()`](#c4d.modules.volume.VolumeBuilder.GetMixVectorMode): Gets the mix vector mode for the index.
- [`VolumeBuilder.SetMixVectorMode()`](#c4d.modules.volume.VolumeBuilder.SetMixVectorMode): Sets the mix vector mode for the index.

## Members <a id="members"></a>

### Input Object Management <a id="c4d.modules.volume.VolumeBuilder-method-Input-Object-Management"></a>

#### `VolumeBuilder.AddSceneObject(self, object, index=0)` <a id="c4d.modules.volume.VolumeBuilder.AddSceneObject"></a>

Adds a valid object from the document to the objects list.

> **Note:**
>
> Because the list is a tree, *index* depends on the position shown in the UI.  
> This means children are iterated first.

**Parameters:**

- **object** ([*c4d.BaseObject*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object that should be added to the objects list.
- **index** (*int*) – The index the object should be added to.

**Return type:** bool

**Returns:** **True** if the object was added successfully, otherwise **False**.

#### `VolumeBuilder.ClearInputObjects(self)` <a id="c4d.modules.volume.VolumeBuilder.ClearInputObjects"></a>

Clears the objects list.

#### `VolumeBuilder.GetInputObject(self, index)` <a id="c4d.modules.volume.VolumeBuilder.GetInputObject"></a>

Retrieves the input object referenced at the given *index*.

> **Note:**
>
> Because the list is a tree, *index* depends on the position shown in the UI.  
> This means children are iterated first.

**Parameters:** **index** (*int*) – The index of the object to access.

**Return type:** Optional[[c4d.BaseObject](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The input object at *index*. **None** if it is a folder or if the function failed.

#### `VolumeBuilder.GetInputObjectByType(self, type, startIndex)` <a id="c4d.modules.volume.VolumeBuilder.GetInputObjectByType"></a>

Retrieves the input object with the given *type*.

**Parameters:**

- **type** (*int*) – The type of object to access.
- **startIndex** (*int*) – The index to start the search.

**Return type:** Optional[Tuple[[c4d.BaseObject](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject), int]]

**Returns:** The input object and its index. **None** if the function failed.

#### `VolumeBuilder.GetInputObjectCount(self, countDouble=True)` <a id="c4d.modules.volume.VolumeBuilder.GetInputObjectCount"></a>

Returns the number of objects in the list.

> **Note:** The function does not count folders.

**Parameters:** **countDouble** (*bool*) – If **True** the objects that are present multiple times in the list are counted multiple times.

**Return type:** int

**Returns:** The number of objects in the object list.

#### `VolumeBuilder.GetListEntryCount(self)` <a id="c4d.modules.volume.VolumeBuilder.GetListEntryCount"></a>

Returns the number of elements in the objects list containing folders.

**Return type:** int

**Returns:** The number of elements in the object list.

#### `VolumeBuilder.InputObjectIsChild(self, index)` <a id="c4d.modules.volume.VolumeBuilder.InputObjectIsChild"></a>

Checks if object at *index* in the object list is a child of the generator.

> **Note:**
>
> Because the list is a tree, *index* depends on the position shown in the UI.  
> This means children are iterated first.

**Parameters:** **index** (*int*) – The index of the list object to check.

**Return type:** bool

**Returns:** **True** if the input object is a child, otherwise **False**.

#### `VolumeBuilder.RemoveObject(self, index)` <a id="c4d.modules.volume.VolumeBuilder.RemoveObject"></a>

Removes the object in the list at the given *index*.

> **Note:**
>
> Because the list is a tree, *index* depends on the position shown in the UI.  
> This means children are iterated first.  
> If the object is a child of the [`VolumeBuilder`](#c4d.modules.volume.VolumeBuilder), it will be automatically readded to the list.  
> Removing the object from the hierarchy would prevent that.

**Parameters:** **index** (*int*) – The index of the object to remove.

**Return type:** bool

**Returns:** **True** if the object was removed successfully, otherwise **False**.

### Input State <a id="c4d.modules.volume.VolumeBuilder-method-Input-State"></a>

#### `VolumeBuilder.GetEnable(self, index)` <a id="c4d.modules.volume.VolumeBuilder.GetEnable"></a>

Gets the enabled state for the input object at *index*.

> **Note:**
>
> Because the list is a tree, *index* depends on the position shown in the UI.  
> This means children are iterated first.

**Parameters:** **index** (*int*) – The index of the object in the list.

**Return type:** bool

**Returns:** **True** if the object is enabled, otherwise **False**.

#### `VolumeBuilder.GetSelected(self, index)` <a id="c4d.modules.volume.VolumeBuilder.GetSelected"></a>

Gets the selection state for the input object at *index*.

> **Note:**
>
> Because the list is a tree, *index* depends on the position shown in the UI.  
> This means children are iterated first.

**Parameters:** **index** (*int*) – The index of the object in the list.

**Return type:** bool

**Returns:** **True** if the object is selected, otherwise **False**.

#### `VolumeBuilder.SetEnable(self, index, enable)` <a id="c4d.modules.volume.VolumeBuilder.SetEnable"></a>

Sets the enabled state for the input object at *index*.

> **Note:**
>
> Because the list is a tree, *index* depends on the position shown in the UI.  
> This means children are iterated first.

**Parameters:**

- **index** (*int*) – The index of the object in the list.
- **enable** (*bool*) – The enabled state to set.

#### `VolumeBuilder.SetSelected(self, index, select)` <a id="c4d.modules.volume.VolumeBuilder.SetSelected"></a>

Sets the selection state for the input object at *index*.

> **Note:**
>
> Because the list is a tree, *index* depends on the position shown in the UI.  
> This means children are iterated first.

**Parameters:**

- **index** (*int*) – The index of the object in the list.
- **select** (*bool*) – The The selection state to set.

### Magic Methods <a id="c4d.modules.volume.VolumeBuilder-method-Magic-Methods"></a>

#### `VolumeBuilder.__init__(self)` <a id="c4d.modules.volume.VolumeBuilder.__init__"></a>

Creates a [`VolumeBuilder`](#c4d.modules.volume.VolumeBuilder).

### Operation Modes <a id="c4d.modules.volume.VolumeBuilder-method-Operation-Modes"></a>

#### `VolumeBuilder.GetBoolMode(self, index)` <a id="c4d.modules.volume.VolumeBuilder.GetBoolMode"></a>

Gets the bool mode for the input object at *index*.

> **Note:**
>
> Because the list is a tree, *index* depends on the position shown in the UI.  
> This means children are iterated first.

**Parameters:** **index** (*int*) – The index of the object in the list.

**Return type:** int

**Returns:**

The bool mode:

|   |   |
|---|---|
| *BOOLTYPE_NONE* | None. |
| *BOOLTYPE_UNION* | Union. |
| *BOOLTYPE_DIFF* | Difference. |
| *BOOLTYPE_INTERSECT* | Intersection. |

#### `VolumeBuilder.GetMixMode(self, index)` <a id="c4d.modules.volume.VolumeBuilder.GetMixMode"></a>

Gets the mix mode for the input object at *index*.

> **Note:**
>
> Because the list is a tree, *index* depends on the position shown in the UI.  
> This means children are iterated first.

**Parameters:** **index** (*int*) – The index of the object in the list.

**Return type:** int

**Returns:**

The mix mode:

|   |   |
|---|---|
| *MIXTYPE_NONE* | None. |
| *MIXTYPE_NORMAL* | Normal. |
| *MIXTYPE_MAX* | Maximum. |
| *MIXTYPE_MIN* | Minimum. |
| *MIXTYPE_ADD* | Addition. |
| *MIXTYPE_SUBTRACT* | Substract. |
| *MIXTYPE_MULTIPLY* | Multiply. |
| *MIXTYPE_DIVIDE* | Division. |

#### `VolumeBuilder.SetBoolMode(self, index, boolmode)` <a id="c4d.modules.volume.VolumeBuilder.SetBoolMode"></a>

Sets the bool mode for the input object at *index*.

> **Note:**
>
> Because the list is a tree, *index* depends on the position shown in the UI.  
> This means children are iterated first.

**Parameters:**

- **index** (*int*) – The index of the object in the list.

- **boolmode** (*int*) –

  The bool mode to set:

  |   |   |
  |---|---|
  | *BOOLTYPE_NONE* | None. |
  | *BOOLTYPE_UNION* | Union. |
  | *BOOLTYPE_DIFF* | Difference. |
  | *BOOLTYPE_INTERSECT* | Intersection. |

#### `VolumeBuilder.SetMixMode(self, index, mixmode)` <a id="c4d.modules.volume.VolumeBuilder.SetMixMode"></a>

Sets the mix mode for the input object at *index*.

> **Note:**
>
> Because the list is a tree, *index* depends on the position shown in the UI.  
> This means children are iterated first.

**Parameters:**

- **index** (*int*) – The index of the object in the list.

- **mixmode** (*int*) –

  The mix mode to set:

  |   |   |
  |---|---|
  | *MIXTYPE_NONE* | None. |
  | *MIXTYPE_NORMAL* | Normal. |
  | *MIXTYPE_MAX* | Maximum. |
  | *MIXTYPE_MIN* | Minimum. |
  | *MIXTYPE_ADD* | Addition. |
  | *MIXTYPE_SUBTRACT* | Substract. |
  | *MIXTYPE_MULTIPLY* | Multiply. |
  | *MIXTYPE_DIVIDE* | Division. |

### Settings Access <a id="c4d.modules.volume.VolumeBuilder-method-Settings-Access"></a>

#### `VolumeBuilder.GetSettingsContainerForIndex(self, index)` <a id="c4d.modules.volume.VolumeBuilder.GetSettingsContainerForIndex"></a>

Returns the internal container for the settings of an input object at the given *index*.

> **Note:**
>
> Because the list is a tree, *index* depends on the position shown in the UI.  
> This means children are iterated first.  
> Allows to change the settings that control the specific conversion of an input object.

**Parameters:** **index** (*int*) – The index of the object in the list.

**Return type:** Optional[[c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)]

**Returns:** The settings container for the object. **None** if it is a folder/filter or if the function failed.

#### `VolumeBuilder.GetSettingsContainerForObject(self, object)` <a id="c4d.modules.volume.VolumeBuilder.GetSettingsContainerForObject"></a>

Returns the internal container for the settings of an input object.

> **Note:** Allows to change the settings that control the specific conversion of an input object.

**Parameters:** **object** ([*c4d.BaseObject*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The input object in the objects list.

**Return type:** Optional[[c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)]

**Returns:** The settings container for the object. **None** if it is a folder/filter or if the function failed.

### Vector Mixing <a id="c4d.modules.volume.VolumeBuilder-method-Vector-Mixing"></a>

#### `VolumeBuilder.GetMixVectorMode(self, index)` <a id="c4d.modules.volume.VolumeBuilder.GetMixVectorMode"></a>

Gets the mix vector mode for the index.

**Parameters:** **index** (*int*) – The index of the object to get the mix vector mode for.

**Return type:** int

**Returns:**

The mix vector mode for the object at the given index.

| Value |
|---|
| MIXVECTORTYPE_NONE |
| MIXVECTORTYPE_NORMAL |
| MIXVECTORTYPE_ADD |
| MIXVECTORTYPE_SUBTRACT |
| MIXVECTORTYPE_CROSS |

#### `VolumeBuilder.SetMixVectorMode(self, index, mixmode)` <a id="c4d.modules.volume.VolumeBuilder.SetMixVectorMode"></a>

Sets the mix vector mode for the index.

**Parameters:**

- **index** (*int*) – The index of the object to set the mix vector mode for.

- **mixmode** (*int*) –

  The mix vector mode to set.

  | Value |
  |---|
  | MIXVECTORTYPE_NONE |
  | MIXVECTORTYPE_NORMAL |
  | MIXVECTORTYPE_ADD |
  | MIXVECTORTYPE_SUBTRACT |
  | MIXVECTORTYPE_CROSS |
