<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/index.html -->

# c4d.GeListNode <a id="c4d-gelistnode"></a>

## *class* `c4d.GeListNode` <a id="c4d.GeListNode"></a>

The base class of many other classes.  
This class is also a linked list which enables you to link several objects with each other.

Parent Class:

- [`c4d.C4DAtom`](../index.md#c4d.C4DAtom)

Children Classes:

- [`c4d.CKey`](../CKey/index.md#c4d.CKey)
- [`c4d.GeListHead`](GeListHead/index.md#c4d.GeListHead)
- [`c4d.BaseList2D`](BaseList2D/index.md#c4d.BaseList2D)

## Overview <a id="overview"></a>

**Document Context**

- [`GeListNode.GetDocument()`](#c4d.GeListNode.GetDocument): Get the document for this node.
- [`GeListNode.IsDocumentRelated()`](#c4d.GeListNode.IsDocumentRelated): Checks if the node is of a type that can be inserted into a [`BaseDocument`](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)

**Hierarchy Navigation Methods**

- [`GeListNode.GetChildren()`](#c4d.GeListNode.GetChildren): Returns children in a list (not grandchild).
- [`GeListNode.GetDown()`](#c4d.GeListNode.GetDown): Returns the first child of this object in the list.
- [`GeListNode.GetDownLast()`](#c4d.GeListNode.GetDownLast): Returns the last child of this object in the list.
- [`GeListNode.GetNext()`](#c4d.GeListNode.GetNext): Returns the next object in the list.
- [`GeListNode.GetPred()`](#c4d.GeListNode.GetPred): Returns the previous object in the list.
- [`GeListNode.GetUp()`](#c4d.GeListNode.GetUp): Returns the parent object.

**Insertion Methods**

- [`GeListNode.InsertAfter()`](#c4d.GeListNode.InsertAfter): Insert self after *obj*.
- [`GeListNode.InsertBefore()`](#c4d.GeListNode.InsertBefore): Insert self before *obj*.
- [`GeListNode.InsertUnder()`](#c4d.GeListNode.InsertUnder): Insert self under *obj*.
- [`GeListNode.InsertUnderLast()`](#c4d.GeListNode.InsertUnderLast): Insert self as the last child of *obj*.

**List Structure**

- [`GeListNode.GetBranchInfo()`](#c4d.GeListNode.GetBranchInfo): Returns information about which other nodes the node contains.
- [`GeListNode.GetListHead()`](#c4d.GeListNode.GetListHead): Returns the list head.
- [`GeListNode.Remove()`](#c4d.GeListNode.Remove): Removes this node from a list.

**Magic Methods**

- [`GeListNode.__getitem__()`](#c4d.GeListNode.__getitem__): Uses a description ID as a key into the container, and retrieves the stored data.
- [`GeListNode.__setitem__()`](#c4d.GeListNode.__setitem__): Uses a description ID as a key into the container, and stores the specified data.

**N-Bit Methods**

- [`GeListNode.ChangeNBit()`](#c4d.GeListNode.ChangeNBit): Sets bits in the 64-bit bitfield of the node.
- [`GeListNode.GetNBit()`](#c4d.GeListNode.GetNBit): Raw access to a 64-bit bitfield, containing information about the node state.

## Members <a id="members"></a>

### Document Context <a id="c4d.GeListNode-method-Document-Context"></a>

#### `GeListNode.GetDocument(self)` <a id="c4d.GeListNode.GetDocument"></a>

Get the document for this node.

**Return type:** [c4d.documents.BaseDocument](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)

**Returns:** The document.

#### `GeListNode.IsDocumentRelated(self)` <a id="c4d.GeListNode.IsDocumentRelated"></a>

Checks if the node is of a type that can be inserted into a [`BaseDocument`](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)

**Return type:** bool

**Returns:** **True** if the node is document related, otherwise **False**.

### Hierarchy Navigation Methods <a id="c4d.GeListNode-method-Hierarchy-Navigation-Methods"></a>

#### `GeListNode.GetChildren(self)` <a id="c4d.GeListNode.GetChildren"></a>

Returns children in a list (not grandchild).

**Return type:** List[[c4d.GeListNode](#c4d.GeListNode)]

**Returns:** All children in a list.

#### `GeListNode.GetDown(self)` <a id="c4d.GeListNode.GetDown"></a>

Returns the first child of this object in the list.

**Return type:** Optional[[c4d.GeListNode](#c4d.GeListNode)]

**Returns:** The first child object.

#### `GeListNode.GetDownLast(self)` <a id="c4d.GeListNode.GetDownLast"></a>

Returns the last child of this object in the list.

**Return type:** Optional[[c4d.GeListNode](#c4d.GeListNode)]

**Returns:** The first child object.

#### `GeListNode.GetNext(self)` <a id="c4d.GeListNode.GetNext"></a>

Returns the next object in the list.

**Return type:** Optional[[c4d.GeListNode](#c4d.GeListNode)]

**Returns:** The next object.

#### `GeListNode.GetPred(self)` <a id="c4d.GeListNode.GetPred"></a>

Returns the previous object in the list.

**Return type:** Optional[[c4d.GeListNode](#c4d.GeListNode)]

**Returns:** The previous object.

#### `GeListNode.GetUp(self)` <a id="c4d.GeListNode.GetUp"></a>

Returns the parent object.

**Return type:** Optional[[c4d.GeListNode](#c4d.GeListNode)]

**Returns:** The parent object.

### Insertion Methods <a id="c4d.GeListNode-method-Insertion-Methods"></a>

#### `GeListNode.InsertAfter(self, obj)` <a id="c4d.GeListNode.InsertAfter"></a>

Insert self after *obj*.

> **Note:**
>
> Take care *obj* is a correct type.  
> For example it is not possible to insert a document after a [`BaseObject`](BaseList2D/BaseObject/index.md#c4d.BaseObject).  
> Check this using `C4DAtom.GetClassification()` and `C4DAtom.GetType()`.

> **Warning:**
>
> Forbidden to call in expressions (tags/nodes). Changing the document structure while an expression is evaluated will crash the application!  
> See [Threading Restrictions](../../../../manuals/manual_scene_execution.md#threading-information).

**Parameters:** **obj** ([*c4d.GeListNode*](#c4d.GeListNode)) – The object to insert after.

#### `GeListNode.InsertBefore(self, obj)` <a id="c4d.GeListNode.InsertBefore"></a>

Insert self before *obj*.

> **Note:**
>
> Take care *obj* is a correct type.  
> For example it is not possible to insert a document before a [`BaseObject`](BaseList2D/BaseObject/index.md#c4d.BaseObject).  
> Check this using `C4DAtom.GetClassification()` and `C4DAtom.GetType()`.

> **Warning:**
>
> Forbidden to call in expressions (tags/nodes). Changing the document structure while an expression is evaluated will crash the application!  
> See [Threading Restrictions](../../../../manuals/manual_scene_execution.md#threading-information).

**Parameters:** **obj** ([*c4d.GeListNode*](#c4d.GeListNode)) – The object to insert before.

#### `GeListNode.InsertUnder(self, obj)` <a id="c4d.GeListNode.InsertUnder"></a>

Insert self under *obj*.

> **Note:**
>
> Take care *obj* is a correct type.  
> For example it is not possible to insert a document under a [`BaseObject`](BaseList2D/BaseObject/index.md#c4d.BaseObject).  
> Check this using `C4DAtom.GetClassification()` and `C4DAtom.GetType()`.

**Parameters:** **obj** ([*c4d.GeListNode*](#c4d.GeListNode)) – The object to insert under.

#### `GeListNode.InsertUnderLast(self, obj)` <a id="c4d.GeListNode.InsertUnderLast"></a>

Insert self as the last child of *obj*.

> **Note:**
>
> Take care *obj* is a correct type.  
> For example it is not possible to insert a document under a [`BaseObject`](BaseList2D/BaseObject/index.md#c4d.BaseObject).  
> Check this using `C4DAtom.GetClassification()` and `C4DAtom.GetType()`.

> **Warning:**
>
> Forbidden to call in expressions (tags/nodes). Changing the document structure while an expression is evaluated will crash the application!  
> See [Threading Restrictions](../../../../manuals/manual_scene_execution.md#threading-information).

**Parameters:** **obj** ([*c4d.GeListNode*](#c4d.GeListNode)) – The object to insert under.

### List Structure <a id="c4d.GeListNode-method-List-Structure"></a>

#### `GeListNode.GetBranchInfo(self, flags=0)` <a id="c4d.GeListNode.GetBranchInfo"></a>

Returns information about which other nodes the node contains. For example objects contain tags.

*New in version R19.*

**Parameters:**

**flags** (*int*) –

The flags:

|   |   |
|---|---|
| *GETBRANCHINFO_NONE* | None. |
| *GETBRANCHINFO_ONLYWITHCHILDREN* | Only return branch if it is in use, i.e. has content. |
| *GETBRANCHINFO_GELISTNODES* | Private. |
| *GETBRANCHINFO_ONLYMODIFIABLE* | Private. |

**Return type:** List[Dict[str: Union[Optional[[c4d.GeListHead](GeListHead/index.md#c4d.GeListHead)], str, int]]]

**Returns:**

A list of dictionaries (**None** if the function failed) with the following information:

’head’: [`c4d.GeListHead`](GeListHead/index.md#c4d.GeListHead): Either a [`c4d.GeListNode`](#c4d.GeListNode) or a [`c4d.GeListHead`](GeListHead/index.md#c4d.GeListHead) for the branch, depending on *flags*.  
’name’: *str*: The human readable name of the branch.  
’id’: *int*: The base ID of the branch. For example *VPbase*, *Mbase* or *Obase*.  
’flags’: *int*: The flags for the branch:

|   |   |
|---|---|
| *BRANCHINFOFLAGS_NONE* | None. |
| *BRANCHINFOFLAGS_ANIMATE* | Animate the nodes in the branch. |
| *BRANCHINFOFLAGS_HIDEINTIMELINE* | If set, the branch does not show up in the timeline. |

#### `GeListNode.GetListHead(self)` <a id="c4d.GeListNode.GetListHead"></a>

Returns the list head.

**Return type:** Optional[[c4d.GeListHead](GeListHead/index.md#c4d.GeListHead)]

**Returns:**

The list head, or **None** if the node is not attached to one.

*Changed in version R19:* The function now returns a [`c4d.GeListHead`](GeListHead/index.md#c4d.GeListHead) object.

#### `GeListNode.Remove(self)` <a id="c4d.GeListNode.Remove"></a>

Removes this node from a list.

> **Warning:**
>
> Forbidden to call in expressions (tags/nodes). Changing the document structure while an expression is evaluated will crash the application!  
> See [Threading Restrictions](../../../../manuals/manual_scene_execution.md#threading-information).

### Magic Methods <a id="c4d.GeListNode-method-Magic-Methods"></a>

#### `GeListNode.__getitem__(self, key)` <a id="c4d.GeListNode.__getitem__"></a>

Uses a description ID as a key into the container, and retrieves the stored data.

> **Note:** Has to be used to get an object’s parameters data. Its corresponding function of the C++ API is *C4DAtom::GetParameter()*.

**Parameters:** **key** (*Union*[*int*, *list*, [*c4d.DescID*](../../DescID/index.md#c4d.DescID), *str*]) – The description ID or a string representing a node attribute id.

**Return type:** Any

**Returns:** See [`__setitem__()`](#c4d.GeListNode.__setitem__)

#### `GeListNode.__setitem__(self, key, value)` <a id="c4d.GeListNode.__setitem__"></a>

Uses a description ID as a key into the container, and stores the specified data.

> **Note:**
>
> Has to be used to set an object’s parameters data.  
> Its corresponding function of the C++ API is *C4DAtom::SetParameter()*.

**Parameters:**

- **key** (*Union*[*int*, *list*, [*c4d.DescID*](../../DescID/index.md#c4d.DescID), *str*]) – The description ID or a string representing a node attribute id.

- **value** (*any*) –

  The data to store:

  | Types to get and set |
  |---|
  | *bool* |
  | *int* |
  | *float* |
  | *str* |
  | [`BaseContainer`](../../BaseContainer/index.md#c4d.BaseContainer) |
  | [`Matrix`](../../Matrix/index.md#c4d.Matrix) |
  | [`Vector`](../../Vector/index.md#c4d.Vector) |
  | [`BaseList2D`](BaseList2D/index.md#c4d.BaseList2D) |
  | [`BaseTime`](../../BaseTime/index.md#c4d.BaseTime) |
  | [`MatAssignData`](../../CustomDataType/MatAssignData/index.md#c4d.MatAssignData) |
  | [`InExcludeData`](../../CustomDataType/InExcludeData/index.md#c4d.InExcludeData) |
  | [`SplineData`](../../CustomDataType/SplineData/index.md#c4d.SplineData) |
  | [`Gradient`](../../CustomDataType/Gradient/index.md#c4d.Gradient) |
  | [`DateTimeData`](../../CustomDataType/DateTimeData/index.md#c4d.DateTimeData) |
  | [`PriorityData`](../../CustomDataType/PriorityData/index.md#c4d.PriorityData) |
  | [`LayerSet`](../../CustomDataType/LayerSet/index.md#c4d.LayerSet) |
  | [`FontData`](../../CustomDataType/FontData/index.md#c4d.FontData) |
  | [`UnitScaleData`](../../CustomDataType/UnitScaleData/index.md#c4d.UnitScaleData) |
  | [`PLAData`](../../CustomDataType/PLAData/index.md#c4d.PLAData) |
  | [`maxon.Data`](../../../maxon_generated/datatypes/base_core/maxon.Data.md#module-maxon.Data) |

### N-Bit Methods <a id="c4d.GeListNode-method-N-Bit-Methods"></a>

#### `GeListNode.ChangeNBit(self, bit, bitmode)` <a id="c4d.GeListNode.ChangeNBit"></a>

Sets bits in the 64-bit bitfield of the node.

**Parameters:**

- **bit** (*int*) –

  Bit index:

  |   |   |
  |---|---|
  | *NBIT_NONE* | None. |
  | *NBIT_TL1_FOLD* | Folding bit for Timeline 1. |
  | *NBIT_TL2_FOLD* | Folding bit for Timeline 2. |
  | *NBIT_TL3_FOLD* | Folding bit for Timeline 3. |
  | *NBIT_TL4_FOLD* | Folding bit for Timeline 4. |
  | *NBIT_TL1_SELECT* | Selection bit for Timeline 1. |
  | *NBIT_TL2_SELECT* | Selection bit for Timeline 2. |
  | *NBIT_TL3_SELECT* | Selection bit for Timeline 3. |
  | *NBIT_TL4_SELECT* | Selection bit for Timeline 4. |
  | *NBIT_TL1_TDRAW* | Private. |
  | *NBIT_TL2_TDRAW* | Private. |
  | *NBIT_TL3_TDRAW* | Private. |
  | *NBIT_TL4_TDRAW* | Private. |
  | *NBIT_CKEY_ACTIVE* | Active point of animation path in editor. |
  | *NBIT_OM1_FOLD* | Folding bit for Object Manager 1. |
  | *NBIT_OM2_FOLD* | Folding bit for Object Manager 2. |
  | *NBIT_OM3_FOLD* | Folding bit for Object Manager 3. |
  | *NBIT_OM4_FOLD* | Folding bit for Object Manager 4. |
  | *NBIT_TL1_FOLDTR* | Track folding for Timeline 1. |
  | *NBIT_TL2_FOLDTR* | Track folding for Timeline 2. |
  | *NBIT_TL3_FOLDTR* | Track folding for Timeline 3. |
  | *NBIT_TL4_FOLDTR* | Track folding for Timeline 4. |
  | *NBIT_TL1_FOLDFC* | F-Curve folding for Timeline 1. |
  | *NBIT_TL2_FOLDFC* | F-Curve folding for Timeline 2. |
  | *NBIT_TL3_FOLDFC* | F-Curve folding for Timeline 3. |
  | *NBIT_TL4_FOLDFC* | F-Curve folding for Timeline 4. |
  | *NBIT_SOURCEOPEN* | Source open in motion clip hierarchy tree. |
  | *NBIT_TL1_HIDE* | Hide in Timeline 1. |
  | *NBIT_TL2_HIDE* | Hide in Timeline 2. |
  | *NBIT_TL3_HIDE* | Hide in Timeline 3. |
  | *NBIT_TL4_HIDE* | Hide in Timeline 4. |
  | *NBIT_SOLO_ANIM* | Solo animation. |
  | *NBIT_SOLO_LAYER* | Solo layer. |
  | *NBIT_TL1_SELECT2* | Private. |
  | *NBIT_TL2_SELECT2* | Private. |
  | *NBIT_TL3_SELECT2* | Private. |
  | *NBIT_TL4_SELECT2* | Private. |
  | *NBIT_SOLO_MOTION* | Solo motion. |
  | *NBIT_CKEY_LOCK_T* | Lock key time. |
  | *NBIT_CKEY_LOCK_V* | Lock key value. |
  | *NBIT_CKEY_MUTE* | Mute key. |
  | *NBIT_CKEY_CLAMP* | Clamp key tangents. |
  | *NBIT_CKEY_BREAK* | Break key tangents. |
  | *NBIT_CKEY_KEEPVISUALANGLE* | Keep visual angle. |
  | *NBIT_CKEY_LOCK_O* | Lock key tangents angles. |
  | *NBIT_CKEY_LOCK_L* | Lock key tangents length. |
  | *NBIT_CKEY_AUTO* | Key auto tangents. |
  | *NBIT_CKEY_ZERO_O_OLD* | Deprecated. |
  | *NBIT_CKEY_ZERO_L_OLD* | Deprecated. |
  | *NBIT_TL1_FCSELECT* | F-Curve selection bit for Timeline 1. |
  | *NBIT_TL2_FCSELECT* | F-Curve selection bit for Timeline 2. |
  | *NBIT_TL3_FCSELECT* | F-Curve selection bit for Timeline 3. |
  | *NBIT_TL4_FCSELECT* | F-Curve selection bit for Timeline 4. |
  | *NBIT_CKEY_BREAKDOWN* | Private. |
  | *NBIT_TL1_FOLDMOTION* | Motion clip folding for Timeline 1. |
  | *NBIT_TL2_FOLDMOTION* | Motion clip folding for Timeline 2. |
  | *NBIT_TL3_FOLDMOTION* | Motion clip folding for Timeline 3. |
  | *NBIT_TL4_FOLDMOTION* | Motion clip folding for Timeline 4. |
  | *NBIT_TL1_SELECTMOTION* | Motion clip selection for Timeline 1. |
  | *NBIT_TL2_SELECTMOTION* | Motion clip selection for Timeline 2. |
  | *NBIT_TL3_SELECTMOTION* | Motion clip selection for Timeline 3. |
  | *NBIT_TL4_SELECTMOTION* | Motion clip selection for Timeline 4. |
  | *NBIT_OHIDE* | Hide object/tag in Object Manager or material in Material Manager. |
  | *NBIT_TL_TBAKE* | Private. |
  | *NBIT_TL1_FOLDSM* | Private. |
  | *NBIT_TL2_FOLDSM* | Private. |
  | *NBIT_TL3_FOLDSM* | Private. |
  | *NBIT_TL4_FOLDSM* | Private. |
  | *NBIT_SUBOBJECT* | Private. |
  | *NBIT_LINK_ACTIVE* | Private. |
  | *NBIT_THIDE* | Hide object in Timeline. |
  | *NBIT_SUBOBJECT_AM* | Private. |
  | *NBIT_PROTECTION* | PSR protection. |
  | *NBIT_NOANIM* | No animation. |
  | *NBIT_NODE_TEMP* | *New in version R23:* Private. |
  | *NBIT_NOSELECT* | No selection. |
  | *NBIT_EHIDE* | Hide in viewport. |
  | *NBIT_REF* | XRef. |
  | *NBIT_REF_NO_DD* | XRef object no drag and drop. Private. |
  | *NBIT_REF_OHIDE* | XRef object hide. Private. |
  | *NBIT_NO_DD* | No drag and drop duplication. |
  | *NBIT_HIDEEXCEPTVIEWSELECT* | Hide in viewport except to viewport select. |
  | *NBIT_CKEY_WEIGHTEDTANGENT* | *New in version R17.032:* Weighted tangent. |
  | *NBIT_CKEY_REMOVEOVERSHOOT* | *New in version R17.032:* Gradual clamp of tangent to avoid over shooting. |
  | *NBIT_CKEY_AUTOWEIGHT* | *New in version R17.032:* Weight still adjusted even if angle is user defined. |
  | *NBIT_TAKE_LOCK* | *New in version R17.032:* A node in an override group cannot be changed. |
  | *NBIT_TAKE_OBJINGROUP* | *New in version R17.032:* The object is overridden by an override group. |
  | *NBIT_TAKE_EGROUPOVERIDDEN* | *New in version R17.032:* The object editor visibility is overridden by an override group. |
  | *NBIT_TAKE_RGROUPOVERIDDEN* | *New in version R17.032:* The object render visibility is overridden by an override group. |
  | *NBIT_CKEY_BREAKDOWNCOLOR* | *New in version R18:* The key is a golden pose. |
  | *NBIT_NO_DELETE* | *New in version R18:* No delete in Object Manager. |
  | *NBIT_LOD_HIDE* | *New in version R19:* Used by LOD object to hide itself outside the view. |
  | *NBIT_LOD_PRIVATECACHE* | *New in version R19:* Private. |
  | *NBIT_AHIDE_FOR_HOST* | *New in version R20:* Hide Tag data in Attribute Manager when host object selected (tabs otherwise automatically added) |
  | *NBIT_MAX* | Maximum *NBIT*. |

- **bitmode** (*int*) –

  Bit mode:

  |   |   |
  |---|---|
  | *NBITCONTROL_SET* | Set bit. |
  | *NBITCONTROL_CLEAR* | Clear bit. |
  | *NBITCONTROL_TOGGLE* | Toggle bit. |
  | *NBITCONTROL_PRIVATE_NODIRTY* | Private. |

**Return type:** bool

**Returns:** Bit state.

#### `GeListNode.GetNBit(self, bit)` <a id="c4d.GeListNode.GetNBit"></a>

Raw access to a 64-bit bitfield, containing information about the node state.

**Parameters:**

**bit** (*int*) –

Bit index:

|   |   |
|---|---|
| *NBIT_NONE* | None. |
| *NBIT_TL1_FOLD* | Folding bit for Timeline 1. |
| *NBIT_TL2_FOLD* | Folding bit for Timeline 2. |
| *NBIT_TL3_FOLD* | Folding bit for Timeline 3. |
| *NBIT_TL4_FOLD* | Folding bit for Timeline 4. |
| *NBIT_TL1_SELECT* | Selection bit for Timeline 1. |
| *NBIT_TL2_SELECT* | Selection bit for Timeline 2. |
| *NBIT_TL3_SELECT* | Selection bit for Timeline 3. |
| *NBIT_TL4_SELECT* | Selection bit for Timeline 4. |
| *NBIT_TL1_TDRAW* | Private. |
| *NBIT_TL2_TDRAW* | Private. |
| *NBIT_TL3_TDRAW* | Private. |
| *NBIT_TL4_TDRAW* | Private. |
| *NBIT_CKEY_ACTIVE* | Active point of animation path in editor. |
| *NBIT_OM1_FOLD* | Folding bit for Object Manager 1. |
| *NBIT_OM2_FOLD* | Folding bit for Object Manager 2. |
| *NBIT_OM3_FOLD* | Folding bit for Object Manager 3. |
| *NBIT_OM4_FOLD* | Folding bit for Object Manager 4. |
| *NBIT_TL1_FOLDTR* | Track folding for Timeline 1. |
| *NBIT_TL2_FOLDTR* | Track folding for Timeline 2. |
| *NBIT_TL3_FOLDTR* | Track folding for Timeline 3. |
| *NBIT_TL4_FOLDTR* | Track folding for Timeline 4. |
| *NBIT_TL1_FOLDFC* | F-Curve folding for Timeline 1. |
| *NBIT_TL2_FOLDFC* | F-Curve folding for Timeline 2. |
| *NBIT_TL3_FOLDFC* | F-Curve folding for Timeline 3. |
| *NBIT_TL4_FOLDFC* | F-Curve folding for Timeline 4. |
| *NBIT_SOURCEOPEN* | Source open in motion clip hierarchy tree. |
| *NBIT_TL1_HIDE* | Hide in Timeline 1. |
| *NBIT_TL2_HIDE* | Hide in Timeline 2. |
| *NBIT_TL3_HIDE* | Hide in Timeline 3. |
| *NBIT_TL4_HIDE* | Hide in Timeline 4. |
| *NBIT_SOLO_ANIM* | Solo animation. |
| *NBIT_SOLO_LAYER* | Solo layer. |
| *NBIT_TL1_SELECT2* | Private. |
| *NBIT_TL2_SELECT2* | Private. |
| *NBIT_TL3_SELECT2* | Private. |
| *NBIT_TL4_SELECT2* | Private. |
| *NBIT_SOLO_MOTION* | Solo motion. |
| *NBIT_CKEY_LOCK_T* | Lock key time. |
| *NBIT_CKEY_LOCK_V* | Lock key value. |
| *NBIT_CKEY_MUTE* | Mute key. |
| *NBIT_CKEY_CLAMP* | Clamp key tangents. |
| *NBIT_CKEY_BREAK* | Break key tangents. |
| *NBIT_CKEY_KEEPVISUALANGLE* | Keep visual angle. |
| *NBIT_CKEY_LOCK_O* | Lock key tangents angles. |
| *NBIT_CKEY_LOCK_L* | Lock key tangents length. |
| *NBIT_CKEY_AUTO* | Key auto tangents. |
| *NBIT_CKEY_ZERO_O_OLD* | Deprecated. |
| *NBIT_CKEY_ZERO_L_OLD* | Deprecated. |
| *NBIT_TL1_FCSELECT* | F-Curve selection bit for Timeline 1. |
| *NBIT_TL2_FCSELECT* | F-Curve selection bit for Timeline 2. |
| *NBIT_TL3_FCSELECT* | F-Curve selection bit for Timeline 3. |
| *NBIT_TL4_FCSELECT* | F-Curve selection bit for Timeline 4. |
| *NBIT_CKEY_BREAKDOWN* | Private. |
| *NBIT_TL1_FOLDMOTION* | Motion clip folding for Timeline 1. |
| *NBIT_TL2_FOLDMOTION* | Motion clip folding for Timeline 2. |
| *NBIT_TL3_FOLDMOTION* | Motion clip folding for Timeline 3. |
| *NBIT_TL4_FOLDMOTION* | Motion clip folding for Timeline 4. |
| *NBIT_TL1_SELECTMOTION* | Motion clip selection for Timeline 1. |
| *NBIT_TL2_SELECTMOTION* | Motion clip selection for Timeline 2. |
| *NBIT_TL3_SELECTMOTION* | Motion clip selection for Timeline 3. |
| *NBIT_TL4_SELECTMOTION* | Motion clip selection for Timeline 4. |
| *NBIT_OHIDE* | Hide object/tag in Object Manager or material in Material Manager. |
| *NBIT_TL_TBAKE* | Private. |
| *NBIT_TL1_FOLDSM* | Private. |
| *NBIT_TL2_FOLDSM* | Private. |
| *NBIT_TL3_FOLDSM* | Private. |
| *NBIT_TL4_FOLDSM* | Private. |
| *NBIT_SUBOBJECT* | Private. |
| *NBIT_LINK_ACTIVE* | Private. |
| *NBIT_THIDE* | Hide object in Timeline. |
| *NBIT_SUBOBJECT_AM* | Private. |
| *NBIT_PROTECTION* | PSR protection. |
| *NBIT_NOANIM* | No animation. |
| *NBIT_NODE_TEMP* | *New in version R23:* Private. |
| *NBIT_NOSELECT* | No selection. |
| *NBIT_EHIDE* | Hide in viewport. |
| *NBIT_REF* | XRef. |
| *NBIT_REF_NO_DD* | XRef object no drag and drop. Private. |
| *NBIT_REF_OHIDE* | XRef object hide. Private. |
| *NBIT_NO_DD* | No drag and drop duplication. |
| *NBIT_HIDEEXCEPTVIEWSELECT* | Hide in viewport except to viewport select. |
| *NBIT_CKEY_WEIGHTEDTANGENT* | *New in version R17.032:* Weighted tangent. |
| *NBIT_CKEY_REMOVEOVERSHOOT* | *New in version R17.032:* Gradual clamp of tangent to avoid over shooting. |
| *NBIT_CKEY_AUTOWEIGHT* | *New in version R17.032:* Weight still adjusted even if angle is user defined. |
| *NBIT_TAKE_LOCK* | *New in version R17.032:* A node in an override group cannot be changed. |
| *NBIT_TAKE_OBJINGROUP* | *New in version R17.032:* The object is overridden by an override group. |
| *NBIT_TAKE_EGROUPOVERIDDEN* | *New in version R17.032:* The object editor visibility is overridden by an override group. |
| *NBIT_TAKE_RGROUPOVERIDDEN* | *New in version R17.032:* The object render visibility is overridden by an override group. |
| *NBIT_CKEY_BREAKDOWNCOLOR* | *New in version R18:* The key is a golden pose. |
| *NBIT_NO_DELETE* | *New in version R18:* No delete in Object Manager. |
| *NBIT_LOD_HIDE* | *New in version R19:* Used by LOD object to hide itself outside the view. |
| *NBIT_LOD_PRIVATECACHE* | *New in version R19:* Private. |
| *NBIT_AHIDE_FOR_HOST* | *New in version R20:* Hide Tag data in Attribute Manager when host object selected (tabs otherwise automatically added) |
| *NBIT_MAX* | Maximum *NBIT*. |

**Return type:** bool

**Returns:** Bit state.
