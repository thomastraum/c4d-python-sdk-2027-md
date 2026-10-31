<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/InstanceObject/index.html -->

# c4d.InstanceObject <a id="c4d-instanceobject"></a>

## *class* `c4d.InstanceObject` <a id="c4d.InstanceObject"></a>

Class that contains the minimal data to represent one or multiple instances of an object.  
This InstanceObject has two modes : single-instance mode or multi-instance mode.

The instance object class of type *Oinstance*.

*New in version R20.*

Parent Class:

- [`c4d.BaseObject`](../index.md#c4d.BaseObject)

## Overview <a id="overview"></a>

**Color Data**

- [`InstanceObject.GetInstanceColor()`](#c4d.InstanceObject.GetInstanceColor): Returns the color of the instance at the specified *index*.
- [`InstanceObject.GetInstanceColors()`](#c4d.InstanceObject.GetInstanceColors): Returns the instance colors.
- [`InstanceObject.SetInstanceColors()`](#c4d.InstanceObject.SetInstanceColors): Sets the instance colors.

**Configuration**

- [`InstanceObject.GetReferenceObject()`](#c4d.InstanceObject.GetReferenceObject): Return the instantiated object.
- [`InstanceObject.IsMultiInstance()`](#c4d.InstanceObject.IsMultiInstance): Checks if the instance object is in multi-instance mode.
- [`InstanceObject.SetReferenceObject()`](#c4d.InstanceObject.SetReferenceObject): Sets the instantiated object used for the multiple instances.

**Magic Methods**

- [`InstanceObject.__init__()`](#c4d.InstanceObject.__init__): Creates an [`InstanceObject`](#c4d.InstanceObject).

**Transform Data**

- [`InstanceObject.GetInstanceCount()`](#c4d.InstanceObject.GetInstanceCount): Returns the instance count (number of instances and matrices).
- [`InstanceObject.GetInstanceMatrices()`](#c4d.InstanceObject.GetInstanceMatrices): Returns the instance matrices.
- [`InstanceObject.GetInstanceMatrix()`](#c4d.InstanceObject.GetInstanceMatrix): Returns the global matrix of the instance at the specified *index*.
- [`InstanceObject.SetInstanceMatrices()`](#c4d.InstanceObject.SetInstanceMatrices): Sets the instance matrices.

## Members <a id="members"></a>

### Color Data <a id="c4d.InstanceObject-method-Color-Data"></a>

#### `InstanceObject.GetInstanceColor(self, index)` <a id="c4d.InstanceObject.GetInstanceColor"></a>

Returns the color of the instance at the specified *index*.

**Parameters:** **index** (*int*) – The instance index.

**Return type:** [c4d.Vector](../../../../../Vector/index.md#c4d.Vector)

**Returns:** The instance color.

#### `InstanceObject.GetInstanceColors(self)` <a id="c4d.InstanceObject.GetInstanceColors"></a>

Returns the instance colors.

**Return type:** List[[c4d.Vector](../../../../../Vector/index.md#c4d.Vector)]

**Returns:** The list of instance colors.

#### `InstanceObject.SetInstanceColors(self, colors)` <a id="c4d.InstanceObject.SetInstanceColors"></a>

Sets the instance colors.

**Parameters:** **colors** (*Union*[*List*[[*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)], *Tuple*[[*c4d.Vector*](../../../../../Vector/index.md#c4d.Vector)]]) – The iterable (list or tuple) for the instance colors to set.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Configuration <a id="c4d.InstanceObject-method-Configuration"></a>

#### `InstanceObject.GetReferenceObject(self, doc)` <a id="c4d.InstanceObject.GetReferenceObject"></a>

Return the instantiated object.

> **Note:** Same as accessing the *INSTANCEOBJECT_LINK* parameter in the object’s data container.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document the instance object belongs to.

**Return type:** Optional[[c4d.BaseObject](../index.md#c4d.BaseObject)]

**Returns:** The reference object. **None** if the instance object is unassigned.

#### `InstanceObject.IsMultiInstance(self)` <a id="c4d.InstanceObject.IsMultiInstance"></a>

Checks if the instance object is in multi-instance mode.

**Return type:** bool

**Returns:** **True** if in multi-instance mode, otherwise **False**.

#### `InstanceObject.SetReferenceObject(self, refObj)` <a id="c4d.InstanceObject.SetReferenceObject"></a>

Sets the instantiated object used for the multiple instances.

> **Note:** Same as assigning the *INSTANCEOBJECT_LINK* parameter in the object’s data container.

**Parameters:** **refObj** ([*c4d.BaseObject*](../index.md#c4d.BaseObject)) – The reference object to set.

### Magic Methods <a id="c4d.InstanceObject-method-Magic-Methods"></a>

#### `InstanceObject.__init__(self)` <a id="c4d.InstanceObject.__init__"></a>

Creates an [`InstanceObject`](#c4d.InstanceObject).

### Transform Data <a id="c4d.InstanceObject-method-Transform-Data"></a>

#### `InstanceObject.GetInstanceCount(self)` <a id="c4d.InstanceObject.GetInstanceCount"></a>

Returns the instance count (number of instances and matrices).

**Return type:** int

**Returns:** The instance count.

#### `InstanceObject.GetInstanceMatrices(self)` <a id="c4d.InstanceObject.GetInstanceMatrices"></a>

Returns the instance matrices.

**Return type:** List[[c4d.Matrix](../../../../../Matrix/index.md#c4d.Matrix)]

**Returns:** The list of instance matrices.

#### `InstanceObject.GetInstanceMatrix(self, index)` <a id="c4d.InstanceObject.GetInstanceMatrix"></a>

Returns the global matrix of the instance at the specified *index*.

**Parameters:** **index** (*int*) – The instance index.

**Return type:** [c4d.Matrix](../../../../../Matrix/index.md#c4d.Matrix)

**Returns:** The instance matrix.

#### `InstanceObject.SetInstanceMatrices(self, matrices)` <a id="c4d.InstanceObject.SetInstanceMatrices"></a>

Sets the instance matrices.

> **Note:** The size of *matrices* iterable determines the instance count.

**Parameters:** **matrices** (*Union*[*List*[[*c4d.Matrix*](../../../../../Matrix/index.md#c4d.Matrix)], *Tuple*[[*c4d.Matrix*](../../../../../Matrix/index.md#c4d.Matrix)]]) – The iterable (list or tuple) for the instance matrices to set.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.
