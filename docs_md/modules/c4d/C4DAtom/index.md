<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/index.html -->

# c4d.C4DAtom <a id="c4d-c4datom"></a>

## *class* `c4d.C4DAtom` <a id="c4d.C4DAtom"></a>

The base class of many other classes.

Child Class:

- [`c4d.GeListNode`](GeListNode/index.md#c4d.GeListNode)

## Overview <a id="overview"></a>

**Copying And Cloning**

- [`C4DAtom.CopyTo()`](#c4d.C4DAtom.CopyTo): Copies all values from *self* to *dst*. The atoms must be of the same type!
- [`C4DAtom.GetClone()`](#c4d.C4DAtom.GetClone): Clones the object and returns the reference.

**Description And Parameters**

- [`C4DAtom.GetDescription()`](#c4d.C4DAtom.GetDescription): Gets the description for this atom.
- [`C4DAtom.GetParameter()`](#c4d.C4DAtom.GetParameter): Gets a description parameter of this atom.
- [`C4DAtom.SetParameter()`](#c4d.C4DAtom.SetParameter): Sets a description parameter of this atom.

**Dirty State**

- [`C4DAtom.GetDirty()`](#c4d.C4DAtom.GetDirty): Returns the dirty counter for the passed dirty flags on this scene element.
- [`C4DAtom.GetHDirty()`](#c4d.C4DAtom.GetHDirty): Returns the accumulated dirty counter for the passed dirty flags in this local hierarchy
- [`C4DAtom.SetDirty()`](#c4d.C4DAtom.SetDirty): Marks the passed dirty flags on this scene element as changed.
- [`C4DAtom.SetHDirty()`](#c4d.C4DAtom.SetHDirty): Reports the passed dirty flags to parent nodes and branch owners.

**Lifecycle And Type**

- [`C4DAtom.CheckType()`](#c4d.C4DAtom.CheckType): Checks if this atom is an instance of a base type.
- [`C4DAtom.GetClassification()`](#c4d.C4DAtom.GetClassification): Returns the base type of the object, e.g.
- [`C4DAtom.GetEnabling()`](#c4d.C4DAtom.GetEnabling): Checks if a description parameter should be disabled or enabled.
- [`C4DAtom.GetRealType()`](#c4d.C4DAtom.GetRealType): Get the real type of the atom.
- [`C4DAtom.GetType()`](#c4d.C4DAtom.GetType): Get the type of the atom.
- [`C4DAtom.IsAlive()`](#c4d.C4DAtom.IsAlive): Even though a reference to an object still exists, the object might be freed by an user interaction.
- [`C4DAtom.IsInstanceOf()`](#c4d.C4DAtom.IsInstanceOf): Checks if this atom is an instance of a base type.

**Magic Methods**

- [`C4DAtom.__call__()`](#c4d.C4DAtom.__call__): Returns the atom if it is alive or **None** if the atom is dead.
- [`C4DAtom.__eq__()`](#c4d.C4DAtom.__eq__)
- [`C4DAtom.__hash__()`](#c4d.C4DAtom.__hash__): Returns a hash of the Unique ID derived of the given C4DAtom.
- [`C4DAtom.__ne__()`](#c4d.C4DAtom.__ne__): Check if two different objects point to the same object.

**Messaging**

- [`C4DAtom.Message()`](#c4d.C4DAtom.Message): Sends a message to the atom.
- [`C4DAtom.MultiMessage()`](#c4d.C4DAtom.MultiMessage): Sends a message to the atom and to its children, parents or branches, depending on *flags*.

**Serialization**

- [`C4DAtom.Read()`](#c4d.C4DAtom.Read): Reads to this atom from a [`HyperFile`](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile), manually specifying ID and level.
- [`C4DAtom.ReadObject()`](#c4d.C4DAtom.ReadObject): Reads to this atom from a [`HyperFile`](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile) within another read operation.
- [`C4DAtom.Write()`](#c4d.C4DAtom.Write): Writes the atom to a [`HyperFile`](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile).
- [`C4DAtom.WriteObject()`](#c4d.C4DAtom.WriteObject): Writes this atom to a [`HyperFile`](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile), within another write operation.

**Unique Identifiers**

- [`C4DAtom.AddUniqueID()`](#c4d.C4DAtom.AddUniqueID): Adds unique application ID to the object.
- [`C4DAtom.FindUniqueID()`](#c4d.C4DAtom.FindUniqueID): Checks for a specific unique application ID.
- [`C4DAtom.GetUniqueIDCount()`](#c4d.C4DAtom.GetUniqueIDCount): Retrieves the number of unique application IDs.
- [`C4DAtom.GetUniqueIDIndex()`](#c4d.C4DAtom.GetUniqueIDIndex): Gets the *idx*-th unique application ID data.

## Members <a id="members"></a>

### Copying And Cloning <a id="c4d.C4DAtom-method-Copying-And-Cloning"></a>

#### `C4DAtom.CopyTo(self, dst, flags, trn=None)` <a id="c4d.C4DAtom.CopyTo"></a>

Copies all values from *self* to *dst*. The atoms must be of the same type!

**Parameters:**

- **dst** ([*c4d.C4DAtom*](#c4d.C4DAtom)) – The destination.

- **flags** (*int*) –

  Optional flags for the copy:

  | Key | Description |
  |---|---|
  | COPYFLAGS_NONE | None. |
  | COPYFLAGS_NO_HIERARCHY | Copy without children. |
  | COPYFLAGS_NO_ANIMATION | Copy without tracks, sequences or keys. |
  | COPYFLAGS_NO_BITS | Do not copy [`BaseList2D`](GeListNode/BaseList2D/index.md#c4d.BaseList2D) bits. |
  | COPYFLAGS_NO_MATERIALPREVIEW | Do not create a new material preview. |
  | COPYFLAGS_NO_BRANCHES | Do not copy branches, for example tags on an object. Automatically implies *COPYFLAGS_NO_ANIMATION*, as animation is a branch. |
  | COPYFLAGS_DOCUMENT | Read-only flag set when a complete document is copied. |
  | COPYFLAGS_NO_NGONS | Do not copy N-gons. |
  | COPYFLAGS_CACHE_BUILD | Read-only flag set when cache is built. |
  | COPYFLAGS_RECURSIONCHECK | Checks and avoids instances to cause recursions. |
  | COPYFLAGS_PRIVATE_IDENTMARKER | Private. |
  | COPYFLAGS_PRIVATE_NO_INTERNALS | Private. |
  | COPYFLAGS_PRIVATE_NO_PLUGINLAYER | Private. |
  | COPYFLAGS_PRIVATE_UNDO | Private. |
  | COPYFLAGS_PRIVATE_NO_TAGS | Private. |
  | COPYFLAGS_PRIVATE_DELETE | Private. |
  | COPYFLAGS_PRIVATE_NO_ASSETS | Private. |
  | COPYFLAGS_PRIVATE_NO_RESULTASSETS | Private. |
  | COPYFLAGS_PRIVATE_NO_LOGS | Private. |
  | COPYFLAGS_PRIVATE_BODYPAINT_NODATA | Private. |
  | COPYFLAGS_PRIVATE_BODYPAINT_CONVERTLAYER | Private. |
  | COPYFLAGS_PRIVATE_BODYPAINT_CONVERTLAYER | Private. |
  | COPYFLAGS_PRIVATE_NO_DESCRIPTION | *New in version 2024.5:* Private |

- **trn** (*Optional*[[*c4d.AliasTrans*](../AliasTrans/index.md#c4d.AliasTrans)]) –

  *New in version R17.032.*

  An optional alias translator for the operation.

**Return type:** bool

**Returns:** **True** if the atom was copied.

#### `C4DAtom.GetClone(self, flags=0, trn=None)` <a id="c4d.C4DAtom.GetClone"></a>

Clones the object and returns the reference.

**Parameters:**

- **flags** (*int*) –

  Optional flags for the clone:

  | Key | Description |
  |---|---|
  | COPYFLAGS_NONE | None. |
  | COPYFLAGS_NO_HIERARCHY | Copy without children. |
  | COPYFLAGS_NO_ANIMATION | Copy without tracks, sequences or keys. |
  | COPYFLAGS_NO_BITS | Do not copy [`BaseList2D`](GeListNode/BaseList2D/index.md#c4d.BaseList2D) bits. |
  | COPYFLAGS_NO_MATERIALPREVIEW | Do not create a new material preview. |
  | COPYFLAGS_NO_BRANCHES | Do not copy branches, for example tags on an object. Automatically implies *COPYFLAGS_NO_ANIMATION*, as animation is a branch. |
  | COPYFLAGS_DOCUMENT | Read-only flag set when a complete document is copied. |
  | COPYFLAGS_NO_NGONS | Do not copy N-gons. |
  | COPYFLAGS_CACHE_BUILD | Read-only flag set when cache is built. |
  | COPYFLAGS_RECURSIONCHECK | Checks and avoids instances to cause recursions. |
  | COPYFLAGS_PRIVATE_IDENTMARKER | Private. |
  | COPYFLAGS_PRIVATE_NO_INTERNALS | Private. |
  | COPYFLAGS_PRIVATE_NO_PLUGINLAYER | Private. |
  | COPYFLAGS_PRIVATE_UNDO | Private. |
  | COPYFLAGS_PRIVATE_NO_TAGS | Private. |
  | COPYFLAGS_PRIVATE_DELETE | Private. |
  | COPYFLAGS_PRIVATE_NO_ASSETS | Private. |
  | COPYFLAGS_PRIVATE_NO_RESULTASSETS | Private. |
  | COPYFLAGS_PRIVATE_NO_LOGS | Private. |
  | COPYFLAGS_PRIVATE_BODYPAINT_NODATA | Private. |
  | COPYFLAGS_PRIVATE_BODYPAINT_CONVERTLAYER | Private. |
  | COPYFLAGS_PRIVATE_BODYPAINT_CONVERTLAYER | Private. |
  | COPYFLAGS_PRIVATE_NO_DESCRIPTION | *New in version 2024.5:* Private |

- **trn** (*Optional*[[*c4d.AliasTrans*](../AliasTrans/index.md#c4d.AliasTrans)]) –

  *New in version R17.032.*

  An optional alias translator for the operation.

**Return type:** [c4d.C4DAtom](#c4d.C4DAtom)

**Returns:** Minimum of type atom.

### Description And Parameters <a id="c4d.C4DAtom-method-Description-And-Parameters"></a>

#### `C4DAtom.GetDescription(self, flags)` <a id="c4d.C4DAtom.GetDescription"></a>

Gets the description for this atom.

*New in version R15.037.*

> **Warning:**
>
> Every caller of [`GetDescription()`](#c4d.C4DAtom.GetDescription) gets a copy of the object’s description, including the Attribute Manager.  
> The only way to customize the description is to override `NodeData.GetDDescription()`.

**Parameters:**

**flags** (*int*) –

Flags:

|   |   |
|---|---|
| *DESCFLAGS_DESC_NONE* | None. |
| *DESCFLAGS_DESC_RESOLVEMULTIPLEDATA* | Private and unused. |
| *DESCFLAGS_DESC_LOADED* | Set if elements have been added to the description, either by loading or manual addition. |
| *DESCFLAGS_DESC_RECURSIONLOCK* | Private. |
| *DESCFLAGS_DESC_DONTLOADDEFAULT* | If set, the object description will also contain the tag’s descriptions (as sub-containers). |
| *DESCFLAGS_DESC_MAPTAGS* | If specified, the object description will also contain the tag’s descriptions (as sub-containers). |
| *DESCFLAGS_DESC_NEEDDEFAULTVALUE* | Set if *“Reset to Default”* was called by the user. |

**Return type:** [c4d.Description](../Description/index.md#c4d.Description)

**Returns:** The atom’s description.

#### `C4DAtom.GetParameter(self, id, flags)` <a id="c4d.C4DAtom.GetParameter"></a>

Gets a description parameter of this atom.

*New in version R16.021.*

**Parameters:**

- **id** ([*c4d.DescID*](../DescID/index.md#c4d.DescID)) – The ID of the parameter.

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *DESCFLAGS_GET_NONE* | None. |
  | *DESCFLAGS_GET_PARAM_GET* | Parameter retrieved. |
  | *DESCFLAGS_GET_NO_GEDATADEFAULTVALUE* | If set, the C++ *GeData* default type will not be initialized for `C4DAtom.GetParameter()`. |
  | *DESCFLAGS_GET_NO_GLOBALDATA* | Private. |

**Return type:** Optional[Any]

**Returns:** The parameter data, or **None** if an error occured.

#### `C4DAtom.SetParameter(self, id, data, flags)` <a id="c4d.C4DAtom.SetParameter"></a>

Sets a description parameter of this atom.

*New in version R16.021.*

**Parameters:**

- **id** ([*c4d.DescID*](../DescID/index.md#c4d.DescID)) – The ID of the parameter.

- **data** (*any*) – The parameter data to set.

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *DESCFLAGS_SET_NONE* | None. |
  | *DESCFLAGS_SET_PARAM_SET* | Parameter set. |
  | *DESCFLAGS_SET_USERINTERACTION* | Set when the GUI is calling `SetParameter()`. This is the only time when `SetParameter()` is allowed to use user interaction elements (e.g. open dialogs, display messages etc.). |
  | *DESCFLAGS_SET_DONTCHECKMINMAX* | No check is internally done if the parameter passed is within the [min/max] range of the description, to save some time. |
  | *DESCFLAGS_SET_DONTAFFECTINHERITANCE* | No parameter inheritance, for render settings and post effects only. |
  | *DESCFLAGS_SET_FORCESET* | Forces the set value without `GetParameter()`/Compare. Use only for calls where for sure the value was changed! |
  | *DESCFLAGS_SET_DONTFREESPLINECACHE* | **Private.** *New in version R16.038.* |
  | *DESCFLAGS_SET_INDRAG* | **Gadget (e.g. Slider) in dragging mode (not finished). Only used when *DESCFLAGS_SET_USERINTERACTION* is set.** *New in version R17.053.* |

**Return type:** bool

**Returns:** **True** if the parameter was set, otherwise **False**.

### Dirty State <a id="c4d.C4DAtom-method-Dirty-State"></a>

#### `C4DAtom.GetDirty(self, flags)` <a id="c4d.C4DAtom.GetDirty"></a>

Returns the dirty counter for the passed dirty flags on this scene element.

Call this on the element being monitored. The counters for all passed flags are summed; compare the result with an earlier value to detect changes.

> **See also:** [`GetHDirty()`](#c4d.C4DAtom.GetHDirty) for the accumulated dirty counter in the local hierarchy.

**Parameters:**

**flags** (*int*) –

The passed dirty flags:

Expresses dirty state categories for a single scene element. Unlike `HDIRTYFLAGS`, these flags only track changes on the element itself.

|   |   |
|---|---|
| *DIRTYFLAGS_NONE* | Signals no state. |
| *DIRTYFLAGS_MATRIX* | Signals that the matrix of a [`BaseObject`](GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) has changed. |
| *DIRTYFLAGS_DATA* | Signals that container or parameter data of a scene element has changed. |
| *DIRTYFLAGS_SELECT* | Signals that a point, edge, or polygon selection of a [`BaseObject`](GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) has changed. |
| *DIRTYFLAGS_CACHE* | Signals that the cache of a [`BaseObject`](GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) has changed or been rebuilt. |
| *DIRTYFLAGS_CHILDREN* | Signals that owned child data of a scene element, such as animation keys, has changed. |
| *DIRTYFLAGS_DESCRIPTION* | Signals that the description of a scene element has changed. |
| *DIRTYFLAGS_VISIBILITY* | Signals that the visibility state of a scene element has changed. |
| *DIRTYFLAGS_SELECTION_OBJECTS* | Signals that the object selection of a [`BaseDocument`](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) has changed. |
| *DIRTYFLAGS_SELECTION_TAGS* | Signals that the tag selection of a [`BaseDocument`](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) has changed. |
| *DIRTYFLAGS_SELECTION_MATERIALS* | Signals that the material selection of a [`BaseDocument`](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) has changed. |
| *DIRTYFLAGS_ALL* | Signals all states. |

**Return type:** int

**Returns:** The dirty counter.

#### `C4DAtom.GetHDirty(self, mask)` <a id="c4d.C4DAtom.GetHDirty"></a>

Returns the accumulated dirty counter for the passed dirty flags in this local hierarchy and its branches.

Call this on any element to collect its own dirty counters and those of its descendants. Counters for all passed flags are summed; compare the result with an earlier value to detect matching changes.

> **See also:** [`GetDirty()`](#c4d.C4DAtom.GetDirty) for the dirty counter of this element only.

*New in version R19.*

**Parameters:**

**mask** (*int*) –

The passed dirty flags:

Expresses hierarchical or branching dirty state categories for a scene element. These states propagate from the changed scene element to its parent elements and branch owners.

|   |   |
|---|---|
| *HDIRTYFLAGS_NONE* | Signals no state. |
| *HDIRTYFLAGS_ANIMATION* | Signals that animation data in a hierarchy has changed. |
| *HDIRTYFLAGS_OBJECT* | Signals that object data in a hierarchy has changed. |
| *HDIRTYFLAGS_OBJECT_MATRIX* | Signals that an object matrix in a hierarchy has changed. |
| *HDIRTYFLAGS_OBJECT_HIERARCHY* | Signals that an object hierarchy in a hierarchy has changed. |
| *HDIRTYFLAGS_TAG* | Signals that tag data in a hierachy has changed. |
| *HDIRTYFLAGS_MATERIAL* | Signals that material data in a hierachy has changed. |
| *HDIRTYFLAGS_SHADER* | Signals that shader data in a hierachy has changed. |
| *HDIRTYFLAGS_RENDERSETTINGS* | Signals that render settings in a hierachy have changed. |
| *HDIRTYFLAGS_VP* | Signals that a video post effect in a hierachy has changed. |
| *HDIRTYFLAGS_FILTER* | Signals that a filter in a hierachy has changed. |
| *HDIRTYFLAGS_NBITS* | Signals that bit flags in a hierachy have changed. |
| *HDIRTYFLAGS_ALL* | Signals all states. |

**Return type:** int

**Returns:** The accumulated dirty counter.

#### `C4DAtom.SetDirty(self, flags)` <a id="c4d.C4DAtom.SetDirty"></a>

Marks the passed dirty flags on this scene element as changed.

Call this on the element that changed. This updates the corresponding dirty counters returned by [`GetDirty()`](#c4d.C4DAtom.GetDirty); derived element types can also report the change to their parent nodes.

> **See also:** [`SetHDirty()`](#c4d.C4DAtom.SetHDirty) for reporting dirty flags to parent nodes.

**Parameters:**

**flags** (*int*) –

The passed dirty flags:

Expresses dirty state categories for a single scene element. Unlike `HDIRTYFLAGS`, these flags only track changes on the element itself.

|   |   |
|---|---|
| *DIRTYFLAGS_NONE* | Signals no state. |
| *DIRTYFLAGS_MATRIX* | Signals that the matrix of a [`BaseObject`](GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) has changed. |
| *DIRTYFLAGS_DATA* | Signals that container or parameter data of a scene element has changed. |
| *DIRTYFLAGS_SELECT* | Signals that a point, edge, or polygon selection of a [`BaseObject`](GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) has changed. |
| *DIRTYFLAGS_CACHE* | Signals that the cache of a [`BaseObject`](GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) has changed or been rebuilt. |
| *DIRTYFLAGS_CHILDREN* | Signals that owned child data of a scene element, such as animation keys, has changed. |
| *DIRTYFLAGS_DESCRIPTION* | Signals that the description of a scene element has changed. |
| *DIRTYFLAGS_VISIBILITY* | Signals that the visibility state of a scene element has changed. |
| *DIRTYFLAGS_SELECTION_OBJECTS* | Signals that the object selection of a [`BaseDocument`](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) has changed. |
| *DIRTYFLAGS_SELECTION_TAGS* | Signals that the tag selection of a [`BaseDocument`](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) has changed. |
| *DIRTYFLAGS_SELECTION_MATERIALS* | Signals that the material selection of a [`BaseDocument`](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) has changed. |
| *DIRTYFLAGS_ALL* | Signals all states. |

#### `C4DAtom.SetHDirty(self, mask)` <a id="c4d.C4DAtom.SetHDirty"></a>

Reports the passed dirty flags to parent nodes and branch owners.

Call this on the element that changed. This marks each passed flag and propagates newly marked flags to parent nodes and branch owners.

> **See also:** [`SetDirty()`](#c4d.C4DAtom.SetDirty) for marking this element as dirty.

*New in version R19.*

**Parameters:**

**mask** (*int*) –

The passed dirty flags:

Expresses hierarchical or branching dirty state categories for a scene element. These states propagate from the changed scene element to its parent elements and branch owners.

|   |   |
|---|---|
| *HDIRTYFLAGS_NONE* | Signals no state. |
| *HDIRTYFLAGS_ANIMATION* | Signals that animation data in a hierarchy has changed. |
| *HDIRTYFLAGS_OBJECT* | Signals that object data in a hierarchy has changed. |
| *HDIRTYFLAGS_OBJECT_MATRIX* | Signals that an object matrix in a hierarchy has changed. |
| *HDIRTYFLAGS_OBJECT_HIERARCHY* | Signals that an object hierarchy in a hierarchy has changed. |
| *HDIRTYFLAGS_TAG* | Signals that tag data in a hierachy has changed. |
| *HDIRTYFLAGS_MATERIAL* | Signals that material data in a hierachy has changed. |
| *HDIRTYFLAGS_SHADER* | Signals that shader data in a hierachy has changed. |
| *HDIRTYFLAGS_RENDERSETTINGS* | Signals that render settings in a hierachy have changed. |
| *HDIRTYFLAGS_VP* | Signals that a video post effect in a hierachy has changed. |
| *HDIRTYFLAGS_FILTER* | Signals that a filter in a hierachy has changed. |
| *HDIRTYFLAGS_NBITS* | Signals that bit flags in a hierachy have changed. |
| *HDIRTYFLAGS_ALL* | Signals all states. |

### Lifecycle And Type <a id="c4d.C4DAtom-method-Lifecycle-And-Type"></a>

#### `C4DAtom.CheckType(self, id)` <a id="c4d.C4DAtom.CheckType"></a>

Checks if this atom is an instance of a base type.

> **Note:** This is only an alias to `C4DAtom.IsInstanceOf()`

**Parameters:** **id** (*int*) – The base type ID, for example *Ocube*.

**Return type:** int

**Returns:** **True** if the atom is an instance of the type *id*, otherwise **False**.

#### `C4DAtom.GetClassification(self)` <a id="c4d.C4DAtom.GetClassification"></a>

Returns the base type of the object, e.g. for all objects *Obase*, for all materials *Mmat*, for all tags *Tbase* etc.

**Return type:** int

**Returns:** The base type.

#### `C4DAtom.GetEnabling(self, DescID)` <a id="c4d.C4DAtom.GetEnabling"></a>

Checks if a description parameter should be disabled or enabled.

*New in version 24.*

**Parameters:** **DescID** ([*c4d.DescID*](../DescID/index.md#c4d.DescID)) – The ID of the parameter.

**Return type:** bool

**Returns:** **True** if the parameter is enabled, otherwise **False**

#### `C4DAtom.GetRealType(self)` <a id="c4d.C4DAtom.GetRealType"></a>

Get the real type of the atom.  
This is similar to [`GetType()`](#c4d.C4DAtom.GetType), but for multinodes the ID of the last linked part is returned.  
E.g. XPresso nodes have the type *ID_GV_GROUPDATA* or *ID_GV_NODEDATA*. With [`GetRealType()`](#c4d.C4DAtom.GetRealType) you will get the ID of the operator as a return value.

*New in version R15.037.*

**Return type:** int

**Returns:** The real type, for example *Ocube*.

#### `C4DAtom.GetType(self)` <a id="c4d.C4DAtom.GetType"></a>

Get the type of the atom.  
This must be used to make sure that the derived object really is of the right type before trying to access its members.

**Return type:** int

**Returns:** The type, for example *Ocube*.

#### `C4DAtom.IsAlive(self)` <a id="c4d.C4DAtom.IsAlive"></a>

Even though a reference to an object still exists, the object might be freed by an user interaction. Normally not needed.  
E.g. the C++ Python Object representing a BaseList2D actually store a pointer to this BaseList2D.  
This pointed BaseList2D could be dead for some reason, but we still have a Python object. So in this case IsAlive will return False.

**Return type:** bool

**Returns:** **True** if the object is still alive, otherwise **False**

#### `C4DAtom.IsInstanceOf(self, id)` <a id="c4d.C4DAtom.IsInstanceOf"></a>

Checks if this atom is an instance of a base type.

*New in version R16.021.*

**Parameters:** **id** (*int*) – The base type ID, for example *Ocube*.

**Return type:** int

**Returns:** **True** if the atom is an instance of the type *id*, otherwise **False**.

### Magic Methods <a id="c4d.C4DAtom-method-Magic-Methods"></a>

#### `C4DAtom.__call__(self)` <a id="c4d.C4DAtom.__call__"></a>

Returns the atom if it is alive or **None** if the atom is dead.  
This is a convenient way to know if you can still use the object.

**Return type:** Optional[[c4d.C4DAtom](#c4d.C4DAtom)]

**Returns:** The atom if it is still alive, otherwise **None**.

#### `C4DAtom.__eq__(self, other)` <a id="c4d.C4DAtom.__eq__"></a>

#### `C4DAtom.__hash__(self)` <a id="c4d.C4DAtom.__hash__"></a>

Returns a hash of the Unique ID derived of the given C4DAtom.

```python
print(hash(obj) #hash calls obj.__hash__())
```

**Return type:** int

**Returns:** Hash value

#### `C4DAtom.__ne__(self, other)` <a id="c4d.C4DAtom.__ne__"></a>

Check if two different objects point to the same object.

> **Note:** Does not compare if two different objects are equal.

**Return type:** bool

**Returns:** **True** if the objects point to the same object, otherwise **False**.

### Messaging <a id="c4d.C4DAtom-method-Messaging"></a>

#### `C4DAtom.Message(self, type, data=None)` <a id="c4d.C4DAtom.Message"></a>

Sends a message to the atom.

> **See also:** [C4DAtom and Plugin Messages](../../../consts/MSG_C4DATOM_PLUGINS.md) for information on the messages type, data and input/output.

> **Note:** Some notification messages are automatically passed along to branches: *MSG_POINTS_CHANGED*, *MSG_POLYGONS_CHANGED* and *MSG_SEGMENTS_CHANGED*. This is for convenience and historical reasons.

**Parameters:**

- **type** (*int*) – The message type.
- **data** (*Optional*[*any*]) – The message data.

**Return type:** bool

**Returns:** Depends on the message *type*.

#### `C4DAtom.MultiMessage(self, flags, type, data)` <a id="c4d.C4DAtom.MultiMessage"></a>

Sends a message to the atom and to its children, parents or branches, depending on *flags*.

> **See also:** [MSG](../../../consts/MSG_C4DATOM_PLUGINS.md) for information on the messages type, data and input/output.

**Parameters:**

- **flags** (*int*) –

  A combination of the following flags:

  |   |   |
  |---|---|
  | *MULTIMSG_ROUTE_NONE* | None. |
  | *MULTIMSG_ROUTE_UP* | Send to parents. |
  | *MULTIMSG_ROUTE_ROOT* | Send to root object. |
  | *MULTIMSG_ROUTE_DOWN* | Send to children. |
  | *MULTIMSG_ROUTE_BROADCAST* | Broadcast the message, i.e. distribute it to all branches given by `GeListNode.GetBranchInfo()`. |

- **type** (*int*) – The message type.

- **data** (*any*) – The message data.

**Return type:** bool

**Returns:** Depends on the message *type*.

### Serialization <a id="c4d.C4DAtom-method-Serialization"></a>

#### `C4DAtom.Read(self, hf, id, level)` <a id="c4d.C4DAtom.Read"></a>

Reads to this atom from a [`HyperFile`](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile), manually specifying ID and level.

> **Note:**
>
> This is the function to use if you have opened the hyper file yourself and are reading the object separately.  
> If reading within a plugin function where Cinema 4D has passed the hyper file you should use [`ReadObject()`](#c4d.C4DAtom.ReadObject).

> **Note:** The methods [`Read()`](#c4d.C4DAtom.Read), [`Write()`](#c4d.C4DAtom.Write), [`ReadObject()`](#c4d.C4DAtom.ReadObject) and [`WriteObject()`](#c4d.C4DAtom.WriteObject) are generally not recommended for plugins.

**Parameters:**

- **hf** ([*c4d.storage.HyperFile*](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile)) – The hyperfile to read from.
- **id** (*int*) – The ID of the atom to read.
- **level** (*int*) – The disklevel of the atom to read.

**Return type:** bool

**Returns:** **True** if the atom was read, otherwise **False**.

#### `C4DAtom.ReadObject(self, hf, readheader)` <a id="c4d.C4DAtom.ReadObject"></a>

Reads to this atom from a [`HyperFile`](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile) within another read operation.

> **Note:**
>
> This is the function to use where Cinema 4D has passed the hyper file you should use, for example in a plugin hook.  
> Otherwise you should use [`Read()`](#c4d.C4DAtom.Read).

> **Note:** The methods [`Read()`](#c4d.C4DAtom.Read), [`Write()`](#c4d.C4DAtom.Write), [`ReadObject()`](#c4d.C4DAtom.ReadObject) and [`WriteObject()`](#c4d.C4DAtom.WriteObject) are generally not recommended for plugins.

**Parameters:**

- **hf** ([*c4d.storage.HyperFile*](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile)) – The hyperfile to read from.
- **readheader** (*bool*) – Normally **True**. Should only be **False** if you have manually read the file header yourself.

**Return type:** bool

**Returns:** **True** if the atom was read, otherwise **False**.

#### `C4DAtom.Write(self, hf)` <a id="c4d.C4DAtom.Write"></a>

Writes the atom to a [`HyperFile`](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile).

> **Note:**
>
> This is the function to use if you have opened the hyper file yourself and are writing the object manually.  
> If writing within a plugin function where Cinema 4D has passed the hyper file you should use [`WriteObject()`](#c4d.C4DAtom.WriteObject).

> **Note:** The methods [`Read()`](#c4d.C4DAtom.Read), [`Write()`](#c4d.C4DAtom.Write), [`ReadObject()`](#c4d.C4DAtom.ReadObject) and [`WriteObject()`](#c4d.C4DAtom.WriteObject) are generally not recommended for plugins.

**Parameters:** **hf** ([*c4d.storage.HyperFile*](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile)) – The hyperfile to write to.

**Return type:** bool

**Returns:** **True** if the atom was written, otherwise **False**.

#### `C4DAtom.WriteObject(self, hf)` <a id="c4d.C4DAtom.WriteObject"></a>

Writes this atom to a [`HyperFile`](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile), within another write operation.

> **Note:**
>
> This is the function to use where Cinema 4D has passed the hyper file you should use, for example in a plugin hook.  
> Otherwise you should use [`Write()`](#c4d.C4DAtom.Write).

> **Note:** The methods [`Read()`](#c4d.C4DAtom.Read), [`Write()`](#c4d.C4DAtom.Write), [`ReadObject()`](#c4d.C4DAtom.ReadObject) and [`WriteObject()`](#c4d.C4DAtom.WriteObject) are generally not recommended for plugins.

**Parameters:** **hf** ([*c4d.storage.HyperFile*](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile)) – The hyperfile to write to.

**Return type:** bool

**Returns:** **True** if the atom was written, otherwise **False**.

### Unique Identifiers <a id="c4d.C4DAtom-method-Unique-Identifiers"></a>

#### `C4DAtom.AddUniqueID(self, appid, mem)` <a id="c4d.C4DAtom.AddUniqueID"></a>

Adds unique application ID to the object.

*New in version R16.021.*

**Parameters:**

- **appid** (*int*) – A unique application ID, has to be registered at MAXON, at least it should be obtained from [http://www.plugincafe.com](http://www.plugincafe.com)
- **mem** (*bytes*) – The unique application ID data. Used for instance to store the name of a software vendor.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `C4DAtom.FindUniqueID(self, appid)` <a id="c4d.C4DAtom.FindUniqueID"></a>

Checks for a specific unique application ID.

*New in version R16.021.*

**Parameters:** **appid** (*int*) – A unique application ID, has to be registered at MAXON, at least it should be obtained from [http://www.plugincafe.com](http://www.plugincafe.com)

**Return type:** Optional[memoryview]

**Returns:** The unique application ID data, or **None** if it could not be found.

#### `C4DAtom.GetUniqueIDCount(self)` <a id="c4d.C4DAtom.GetUniqueIDCount"></a>

Retrieves the number of unique application IDs.

*New in version R16.021.*

**Return type:** int

**Returns:** The number of unique application IDs.

#### `C4DAtom.GetUniqueIDIndex(self, idx)` <a id="c4d.C4DAtom.GetUniqueIDIndex"></a>

Gets the *idx*-th unique application ID data.

*New in version R16.050.*

**Parameters:** **idx** (*int*) – The unique ID index: *0<=idx<*[`GetUniqueIDCount()`](#c4d.C4DAtom.GetUniqueIDCount)

**Return type:** Optional[Tuple[int, bytes]]

**Returns:** The unique application ID and its data. Used for instance to read the name of a software vendor.

**None** if it could not be found.
