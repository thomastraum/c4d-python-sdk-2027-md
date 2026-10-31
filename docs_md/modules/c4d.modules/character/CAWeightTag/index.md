<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/character/CAWeightTag/index.html -->

# c4d.modules.character.CAWeightTag <a id="c4d-modules-character-caweighttag"></a>

## *class* `c4d.modules.character.CAWeightTag` <a id="c4d.modules.character.CAWeightTag"></a>

A variety of properties can be added to objects using tags.  
For example, adding smoothing (Phong tag) or preventing an object from being edited accidentally (Protection tag).

Parent Class:

- [`c4d.BaseTag`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)

## Overview <a id="overview"></a>

**Dirty Tracking**

- [`CAWeightTag.GetWeightDirty()`](#c4d.modules.character.CAWeightTag.GetWeightDirty): Get the dirty state of the weights.
- [`CAWeightTag.WeightDirty()`](#c4d.modules.character.CAWeightTag.WeightDirty): Marks the weights dirty.

**Geometry Binding**

- [`CAWeightTag.GetGeomMg()`](#c4d.modules.character.CAWeightTag.GetGeomMg): Get the global matrix for the bind geometry.
- [`CAWeightTag.SetGeomMg()`](#c4d.modules.character.CAWeightTag.SetGeomMg): Set the global matrix for the bind geometry.

**Joint Management**

- [`CAWeightTag.AddJoint()`](#c4d.modules.character.CAWeightTag.AddJoint): Add a Joint object to the Weight tag’s “Joints” list.
- [`CAWeightTag.CalculateBoneStates()`](#c4d.modules.character.CAWeightTag.CalculateBoneStates): Helper function to initialize the Joint at *index*.
- [`CAWeightTag.FindJoint()`](#c4d.modules.character.CAWeightTag.FindJoint): Return the index of this object or *NOTOK* if not found.
- [`CAWeightTag.GetJoint()`](#c4d.modules.character.CAWeightTag.GetJoint): Get joint object at *index*.
- [`CAWeightTag.GetJointCount()`](#c4d.modules.character.CAWeightTag.GetJointCount): Get total joint count.
- [`CAWeightTag.RemoveJoint()`](#c4d.modules.character.CAWeightTag.RemoveJoint): Remove Joint object from the Weight tag’s “Joints” list.

**Magic Methods**

- [`CAWeightTag.__init__()`](#c4d.modules.character.CAWeightTag.__init__)

**Rest State**

- [`CAWeightTag.GetJointRestState()`](#c4d.modules.character.CAWeightTag.GetJointRestState): Get the rest state for the joint at *index*.
- [`CAWeightTag.SetJointRestState()`](#c4d.modules.character.CAWeightTag.SetJointRestState): Set the rest state for the joint at *index*.

**Weight Data**

- [`CAWeightTag.GetIndexWeight()`](#c4d.modules.character.CAWeightTag.GetIndexWeight): Get the *windex* weight and which point index *pntindex* it is as well as the *weight*
- [`CAWeightTag.GetWeight()`](#c4d.modules.character.CAWeightTag.GetWeight): Return the weight for the point *pntindex*.
- [`CAWeightTag.GetWeightCount()`](#c4d.modules.character.CAWeightTag.GetWeightCount): Gets the total number of stored weights for the given joint *index*.
- [`CAWeightTag.GetWeightMap()`](#c4d.modules.character.CAWeightTag.GetWeightMap): Returns all the weights.
- [`CAWeightTag.SetWeight()`](#c4d.modules.character.CAWeightTag.SetWeight): Set the weight for *pntindex*.
- [`CAWeightTag.SetWeightMap()`](#c4d.modules.character.CAWeightTag.SetWeightMap): Sets the weights with *map*.
- [`CAWeightTag.TransferWeightMap()`](#c4d.modules.character.CAWeightTag.TransferWeightMap): Transfer the weights from one Weight tag to another.

## Members <a id="members"></a>

### Dirty Tracking <a id="c4d.modules.character.CAWeightTag-method-Dirty-Tracking"></a>

#### `CAWeightTag.GetWeightDirty(self)` <a id="c4d.modules.character.CAWeightTag.GetWeightDirty"></a>

Get the dirty state of the weights.

**Return type:** int

**Returns:** The weight’s dirty state.

#### `CAWeightTag.WeightDirty(self)` <a id="c4d.modules.character.CAWeightTag.WeightDirty"></a>

Marks the weights dirty.

### Geometry Binding <a id="c4d.modules.character.CAWeightTag-method-Geometry-Binding"></a>

#### `CAWeightTag.GetGeomMg(self)` <a id="c4d.modules.character.CAWeightTag.GetGeomMg"></a>

Get the global matrix for the bind geometry.  
Use this with the global matrices of the joints to get the local transforms.

**Return type:** [c4d.Matrix](../../../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The global matrix for the bind geometry.

#### `CAWeightTag.SetGeomMg(self, mg)` <a id="c4d.modules.character.CAWeightTag.SetGeomMg"></a>

Set the global matrix for the bind geometry.

**Parameters:** **mg** ([*c4d.Matrix*](../../../c4d/Matrix/index.md#c4d.Matrix)) – The global matrix for the bind geometry.

### Joint Management <a id="c4d.modules.character.CAWeightTag-method-Joint-Management"></a>

#### `CAWeightTag.AddJoint(self, op)` <a id="c4d.modules.character.CAWeightTag.AddJoint"></a>

Add a Joint object to the Weight tag’s “Joints” list.

**Parameters:** **op** ([*c4d.BaseObject*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The Joint object to add to the Weight tag’s “Joints” list.

**Return type:** int

**Returns:** Joint object’s index in the “Joints” list.

#### `CAWeightTag.CalculateBoneStates(self, index)` <a id="c4d.modules.character.CAWeightTag.CalculateBoneStates"></a>

Helper function to initialize the Joint at *index*.

> **Note:** The Joints must be in the document.

**Parameters:**

**index** (*int*) –

The Joint index. .. note:

```python
Set to *NOTOK* to process all joints.
```

#### `CAWeightTag.FindJoint(self, op, doc=None)` <a id="c4d.modules.character.CAWeightTag.FindJoint"></a>

Return the index of this object or *NOTOK* if not found.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – Host object.
- **doc** (*Optional*[[*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]) – Document or **None**.

#### `CAWeightTag.GetJoint(self, index, doc=None)` <a id="c4d.modules.character.CAWeightTag.GetJoint"></a>

Get joint object at *index*.

**Parameters:**

- **index** (*int*) – The joint index.
- **doc** (*Optional*[[*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]) – Document or **None**.

**Returns:** The joint object.

**Return type:** Optional[[c4d.modules.character.CAJointObject](../CAJointObject/index.md#c4d.modules.character.CAJointObject)]

#### `CAWeightTag.GetJointCount(self)` <a id="c4d.modules.character.CAWeightTag.GetJointCount"></a>

Get total joint count.

**Return type:** int

**Returns:** Total joint count.

#### `CAWeightTag.RemoveJoint(self, op)` <a id="c4d.modules.character.CAWeightTag.RemoveJoint"></a>

Remove Joint object from the Weight tag’s “Joints” list.

**Parameters:** **op** ([*c4d.BaseObject*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The Joint object to remove from the Weight tag’s “Joint” list.

### Magic Methods <a id="c4d.modules.character.CAWeightTag-method-Magic-Methods"></a>

#### `CAWeightTag.__init__(self)` <a id="c4d.modules.character.CAWeightTag.__init__"></a>

### Rest State <a id="c4d.modules.character.CAWeightTag-method-Rest-State"></a>

#### `CAWeightTag.GetJointRestState(self, index)` <a id="c4d.modules.character.CAWeightTag.GetJointRestState"></a>

Get the rest state for the joint at *index*.

**Parameters:** **index** (*int*) – The index of the joint.

**Raises:** **IndexError** – If the joint index is out of range : *0<=index<*[`GetJointCount()`](#c4d.modules.character.CAWeightTag.GetJointCount).

**Return type:** dict{**m_bMg**: c4d.Matrix, **m_bMi**: c4d.Matrix, **m_oMg**: c4d.Matrix, **m_oMi**: c4d.Matrix}

**Returns:** The state.

#### `CAWeightTag.SetJointRestState(self, index, m_bMg, m_bMi, m_oMg, m_oMi, m_Len)` <a id="c4d.modules.character.CAWeightTag.SetJointRestState"></a>

Set the rest state for the joint at *index*.

**Parameters:**

- **index** (*int*) – The index of the joint.
- **m_bMg** ([*c4d.Matrix*](../../../c4d/Matrix/index.md#c4d.Matrix)) – Global matrix of the bone between two joints with the Z axis (V3) along the bone.
- **m_bMi** ([*c4d.Matrix*](../../../c4d/Matrix/index.md#c4d.Matrix)) – Inverse matrix of the bone between two joints with the Z axis (V3) along the bone.
- **m_oMg** ([*c4d.Matrix*](../../../c4d/Matrix/index.md#c4d.Matrix)) – Global matrix of the actual Joint object.
- **m_oMi** ([*c4d.Matrix*](../../../c4d/Matrix/index.md#c4d.Matrix)) – Inverse matrix of the actual Joint object.
- **m_Len** (*float*) – Bone rest length.

### Weight Data <a id="c4d.modules.character.CAWeightTag-method-Weight-Data"></a>

#### `CAWeightTag.GetIndexWeight(self, index, windex)` <a id="c4d.modules.character.CAWeightTag.GetIndexWeight"></a>

Get the *windex* weight and which point index *pntindex* it is as well as the *weight*

```python
pntindex, weight = caweighttag.GetIndexWeight(0, 0)
```

**Parameters:**

- **index** (*int*) – Joint index.
- **windex** (*int*) – Weight index.

**Return type:** Tuple[int, int]

**Returns:** Returns the point index, and the corresponding weight.

#### `CAWeightTag.GetWeight(self, index, pntindex)` <a id="c4d.modules.character.CAWeightTag.GetWeight"></a>

Return the weight for the point *pntindex*.

**Parameters:**

- **index** (*int*) – Joint index.
- **pntindex** (*int*) – Point index.

**Return type:** float

**Returns:** Weight.

#### `CAWeightTag.GetWeightCount(self, index)` <a id="c4d.modules.character.CAWeightTag.GetWeightCount"></a>

Gets the total number of stored weights for the given joint *index*.

**Parameters:** **index** (*int*) – Joint index.

**Return type:** int

**Returns:** The number of weights. 0 means weights are not stored.

#### `CAWeightTag.GetWeightMap(self, index, cnt, includeEffectors=False)` <a id="c4d.modules.character.CAWeightTag.GetWeightMap"></a>

Returns all the weights.

*New in version R21.*

**Parameters:**

- **index** (*int*) – The joint index: <= index < `CAWeightTag.GetJointCount()`.
- **cnt** (*int*) – The point count. Size of map. (Normally same as the point count).
- **includeEffectors** (*bool*) – If **True** the effectors weights are added to the map.

**Return type:** List[float]

**Returns:** A list of float filled with the weight data.

#### `CAWeightTag.SetWeight(self, index, pntindex, weight)` <a id="c4d.modules.character.CAWeightTag.SetWeight"></a>

Set the weight for *pntindex*.

*Deprecated since version 2025.3.0:* Use `CAWeightTag.SetWeightMap()` instead.

**Parameters:**

- **index** (*int*) – Joint index.
- **pntindex** (*int*) – Point index.
- **weight** (*float*) – New weight.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `CAWeightTag.SetWeightMap(self, index, map)` <a id="c4d.modules.character.CAWeightTag.SetWeightMap"></a>

Sets the weights with *map*.

*New in version R21.*

**Parameters:**

- **index** (*int*) – The joint index: <= index < `CAWeightTag.GetJointCount()`.
- **map** (*List*[*float*]) – A list of float to set the new weight map.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `CAWeightTag.TransferWeightMap(self, doc, dst, sindex, dindex, offset, cnt)` <a id="c4d.modules.character.CAWeightTag.TransferWeightMap"></a>

Transfer the weights from one Weight tag to another.

> **Note:** Pass *NOTOK* for *sindex*, *dindex* and *cnt* if they shouldn’t be evaluated.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document containing the Weight tags.
- **dst** ([*c4d.modules.character.CAWeightTag*](#c4d.modules.character.CAWeightTag)) – The destination Weight tag.
- **sindex** (*int*) – Index of the source Joint.
- **dindex** (*int*) – Index of the destination Joint.
- **offset** (*int*) – Offset to move the weight indices when they are copied to the destination.
- **cnt** (*int*) – Number of weights to be transferred.
