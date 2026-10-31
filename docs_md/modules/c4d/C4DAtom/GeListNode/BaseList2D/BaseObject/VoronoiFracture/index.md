<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/VoronoiFracture/index.html -->

# c4d.VoronoiFracture <a id="c4d-voronoifracture"></a>

## *class* `c4d.VoronoiFracture` <a id="c4d.VoronoiFracture"></a>

A VoronoiFracture object represents a Voronoi Fracture MoGraph generator.  
The class provides safe access to the point sources referenced, owned and used by the generator.

*New in version R18.039.*

Parent Class:

- [`c4d.BaseObject`](../index.md#c4d.BaseObject)

## Overview <a id="overview"></a>

**Magic Methods**

- [`VoronoiFracture.__init__()`](#c4d.VoronoiFracture.__init__)

**Source Management**

- [`VoronoiFracture.AddPointGenerator()`](#c4d.VoronoiFracture.AddPointGenerator): Adds a new point generator.
- [`VoronoiFracture.AddSceneObject()`](#c4d.VoronoiFracture.AddSceneObject): Adds a valid object from the scene to the Sources list.
- [`VoronoiFracture.ClearSources()`](#c4d.VoronoiFracture.ClearSources): Clears the Sources list and deletes all point generators.
- [`VoronoiFracture.RemoveSource()`](#c4d.VoronoiFracture.RemoveSource): Removes the source element in the list at the given index.

**Source Retrieval**

- [`VoronoiFracture.GetSource()`](#c4d.VoronoiFracture.GetSource): Retrieves the object referenced at the given *index*.
- [`VoronoiFracture.GetSourceByType()`](#c4d.VoronoiFracture.GetSourceByType): Retrieves the object referenced in the Sources list with the given type.
- [`VoronoiFracture.GetSourcesCount()`](#c4d.VoronoiFracture.GetSourcesCount): Returns the number of elements in the Sources list, including point generators.

**Source Settings**

- [`VoronoiFracture.GetSourceSettingsContainerForIndex()`](#c4d.VoronoiFracture.GetSourceSettingsContainerForIndex): Returns the internal container for the settings of an external source input, like a polygon object as point source.
- [`VoronoiFracture.GetSourceSettingsContainerForObject()`](#c4d.VoronoiFracture.GetSourceSettingsContainerForObject): Returns the internal container for the settings of an external source input, like a polygon object as point source.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.VoronoiFracture-method-Magic-Methods"></a>

#### `VoronoiFracture.__init__(self)` <a id="c4d.VoronoiFracture.__init__"></a>

### Source Management <a id="c4d.VoronoiFracture-method-Source-Management"></a>

#### `VoronoiFracture.AddPointGenerator(self, type, shaderType=-1)` <a id="c4d.VoronoiFracture.AddPointGenerator"></a>

Adds a new point generator.

**Parameters:**

- **type** (*int*) – The type of point generator, either **ID_POINTCREATOR_CREATORTYPE_DISTRIBUTION** or **ID_POINTCREATOR_CREATORTYPE_SHADER**.
- **shaderType** (*int*) – If a Shader generator is created a shader of this type is automatically added to it.

**Return type:** Optional[Tuple[[c4d.BaseObject](../index.md#c4d.BaseObject), int]]

**Returns:** A tuple with the added point generator and its index, or **None** if the method failed.

#### `VoronoiFracture.AddSceneObject(self, object)` <a id="c4d.VoronoiFracture.AddSceneObject"></a>

Adds a valid object from the scene to the Sources list.

**Parameters:** **object** ([*c4d.BaseObject*](../index.md#c4d.BaseObject)) – The scene object that should be added.

**Return type:** Optional[Tuple[bool, int]]

**Returns:** A tuple with the scene object addition state and its index, or **None** if the method failed.

#### `VoronoiFracture.ClearSources(self)` <a id="c4d.VoronoiFracture.ClearSources"></a>

Clears the Sources list and deletes all point generators.

#### `VoronoiFracture.RemoveSource(self, index)` <a id="c4d.VoronoiFracture.RemoveSource"></a>

Removes the source element in the list at the given index.

> **Note:** If the index references a point generator it is also deleted from the internal list.

**Parameters:** **index** (*int*) – The index of the source element to remove.

**Return type:** bool

**Returns:** **True** if the element was removed successfully, otherwise **False**.

### Source Retrieval <a id="c4d.VoronoiFracture-method-Source-Retrieval"></a>

#### `VoronoiFracture.GetSource(self, index)` <a id="c4d.VoronoiFracture.GetSource"></a>

Retrieves the object referenced at the given *index*.

> **Note:** If *index* references a point generator that point generator object is returned.

**Parameters:** **index** (*int*) – The index of the source element to access.

**Return type:** Optional[[c4d.BaseObject](../index.md#c4d.BaseObject)]

**Returns:** The object at the given *index*, or **None** if the method failed.

#### `VoronoiFracture.GetSourceByType(self, type, startIndex=-1)` <a id="c4d.VoronoiFracture.GetSourceByType"></a>

Retrieves the object referenced in the Sources list with the given type.

> **Note:** If multiple objects with the given *type* exist the first is returned.

**Parameters:**

- **type** (*int*) – The type of object to access.
- **startIndex** (*int*) – The index to start the search.

**Return type:** Optional[Tuple[[c4d.BaseObject](../index.md#c4d.BaseObject), int]]

**Returns:** A tuple with the found source object and its index, or **None** if the method failed.

#### `VoronoiFracture.GetSourcesCount(self)` <a id="c4d.VoronoiFracture.GetSourcesCount"></a>

Returns the number of elements in the Sources list, including point generators.

**Return type:** int

**Returns:** The number of elements in the Sources list.

### Source Settings <a id="c4d.VoronoiFracture-method-Source-Settings"></a>

#### `VoronoiFracture.GetSourceSettingsContainerForIndex(self, index)` <a id="c4d.VoronoiFracture.GetSourceSettingsContainerForIndex"></a>

Returns the internal container for the settings of an external source input, like a polygon object as point source.

*New in version R19.*

> **Note:** Allows to change the settings that control for example the distribution of points in the object and the point count.

**Parameters:** **index** (*int*) – The index of the object in the Sources list.

**Return type:** Optional[[c4d.BaseContainer](../../../../../BaseContainer/index.md#c4d.BaseContainer)]

**Returns:** The container for the source settings if the index fits to an external Source input, otherwise **None**.

#### `VoronoiFracture.GetSourceSettingsContainerForObject(self, object)` <a id="c4d.VoronoiFracture.GetSourceSettingsContainerForObject"></a>

Returns the internal container for the settings of an external source input, like a polygon object as point source.

*New in version R19.*

> **Note:** Allows to change the settings that control for example the distribution of points in the object and the point count.

**Parameters:** **object** ([*c4d.BaseObject*](../index.md#c4d.BaseObject)) – The external source object in the Sources list.

**Return type:** Optional[[c4d.BaseContainer](../../../../../BaseContainer/index.md#c4d.BaseContainer)]

**Returns:** The container for the source settings if the object is in the Sources list, otherwise **None**.
