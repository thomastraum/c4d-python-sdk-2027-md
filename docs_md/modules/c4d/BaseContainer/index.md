<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/BaseContainer/index.html -->

# c4d.BaseContainer <a id="c4d-basecontainer"></a>

## *class* `c4d.BaseContainer` <a id="c4d.BaseContainer"></a>

Provides a container type used to store bundles of data.  
Containers are the form in which most scene elements exposed it parameters. See the *data/c4d_basecontainer.py* example in the SDK for more  
information on how to use containers.

## Overview <a id="overview"></a>

**Deprecated**

- [`BaseContainer.GetLLong()`](#c4d.BaseContainer.GetLLong): Use `GetInt64()` instead.
- [`BaseContainer.GetLong()`](#c4d.BaseContainer.GetLong): Use `GetInt32()` instead.
- [`BaseContainer.GetReal()`](#c4d.BaseContainer.GetReal): Use `GetFloat()` instead.
- [`BaseContainer.SetLLong()`](#c4d.BaseContainer.SetLLong): Use `SetInt64()` instead.
- [`BaseContainer.SetLong()`](#c4d.BaseContainer.SetLong): Use `SetInt32()` instead.
- [`BaseContainer.SetReal()`](#c4d.BaseContainer.SetReal): Use `SetFloat()` instead.

**Generic Data Access**

- [`BaseContainer.GetData()`](#c4d.BaseContainer.GetData): Returns the data for an element by ID.
- [`BaseContainer.GetDataPointer()`](#c4d.BaseContainer.GetDataPointer): Retrieves a pointer to directly access the data.
- [`BaseContainer.GetVoid()`](#c4d.BaseContainer.GetVoid): Gets the void* value at the specified id.
- [`BaseContainer.SetData()`](#c4d.BaseContainer.SetData): Sets an arbitrary data value at the specified ID.
- [`BaseContainer.SetDataNoDirty()`](#c4d.BaseContainer.SetDataNoDirty): Sets arbitrary data at the specified id without setting the container dirty.
- [`BaseContainer.SetVoid()`](#c4d.BaseContainer.SetVoid): Stores a PyCObject to an void* object with the specified ID.

**Identity And State**

- [`BaseContainer.GetDirty()`](#c4d.BaseContainer.GetDirty): Returns the dirty count.
- [`BaseContainer.GetId()`](#c4d.BaseContainer.GetId): Returns the ID of the container.
- [`BaseContainer.IsInstance()`](#c4d.BaseContainer.IsInstance): Checks if the container is an instance.
- [`BaseContainer.SetId()`](#c4d.BaseContainer.SetId): Sets the ID of the container.

**Index And Entry Management**

- [`BaseContainer.FindIndex()`](#c4d.BaseContainer.FindIndex): Returns the index for the value with the specified ID and its assigned data, or -1 if no such value exists.
- [`BaseContainer.GetIndexData()`](#c4d.BaseContainer.GetIndexData): Retrieves the data for the element at *index*.
- [`BaseContainer.GetIndexId()`](#c4d.BaseContainer.GetIndexId): Returns the ID of the element at the specified index, or *NOTOK* if it doesn’t exist.
- [`BaseContainer.GetType()`](#c4d.BaseContainer.GetType): Returns the type of a container element by ID.
- [`BaseContainer.InsData()`](#c4d.BaseContainer.InsData): Inserts an arbitrary data at the specified *id*.
- [`BaseContainer.InsDataAfter()`](#c4d.BaseContainer.InsDataAfter): Inserts an arbitrary data at the specified *id* after *last*.
- [`BaseContainer.RemoveData()`](#c4d.BaseContainer.RemoveData): Removes the first data item with the specified ID.
- [`BaseContainer.RemoveIndex()`](#c4d.BaseContainer.RemoveIndex): Removes the data item at the specified index *i*.
- [`BaseContainer.SetIndexData()`](#c4d.BaseContainer.SetIndexData): Sets the data for the element at *index*.
- [`BaseContainer.Sort()`](#c4d.BaseContainer.Sort): Sorts a container strings by their ID.

**Lifecycle And Composition**

- [`BaseContainer.CopyTo()`](#c4d.BaseContainer.CopyTo): Copies all values to *dst*.
- [`BaseContainer.FlushAll()`](#c4d.BaseContainer.FlushAll): Clears all values in the container.
- [`BaseContainer.GetClone()`](#c4d.BaseContainer.GetClone): Returns a copy of the container including all values.
- [`BaseContainer.MergeContainer()`](#c4d.BaseContainer.MergeContainer): Stores the values in src in this container, overwriting any elements with colliding IDs and keeping the rest.

**Magic Methods**

- [`BaseContainer.__eq__()`](#c4d.BaseContainer.__eq__): Check if the compared containers have the same ID, have the same values, and all values are equal.
- [`BaseContainer.__getitem__()`](#c4d.BaseContainer.__getitem__): Returns a value with the specified ID.
- [`BaseContainer.__init__()`](#c4d.BaseContainer.__init__): Initializes a new container.
- [`BaseContainer.__iter__()`](#c4d.BaseContainer.__iter__): The BaseContainer is iterable so just use it like in the following example:
- [`BaseContainer.__len__()`](#c4d.BaseContainer.__len__): Calculates the number of data elements inside the container.
- [`BaseContainer.__ne__()`](#c4d.BaseContainer.__ne__): Check if the compared containers don’t have the same ID, don’t have the same values, and all values are not equal.
- [`BaseContainer.__setitem__()`](#c4d.BaseContainer.__setitem__): Automatically redirect the value to the corresponding Set* method.

**Nested And Linked Data**

- [`BaseContainer.GetContainer()`](#c4d.BaseContainer.GetContainer): Returns a copy of the sub-container with the specified ID, or an empty container if it doesn’t exist.
- [`BaseContainer.GetContainerInstance()`](#c4d.BaseContainer.GetContainerInstance): Returns the sub-container with the specified ID, or **None** if it doesn’t exist.
- [`BaseContainer.GetCustomDataType()`](#c4d.BaseContainer.GetCustomDataType): Returns a copy of the custom data type or **None** if it doesn’t exist.
- [`BaseContainer.GetLink()`](#c4d.BaseContainer.GetLink): Returns a linked object, evaluated in the attached document.
- [`BaseContainer.GetMaterialLink()`](#c4d.BaseContainer.GetMaterialLink): Returns a linked material object, evaluated in the attached document.
- [`BaseContainer.GetObjectLink()`](#c4d.BaseContainer.GetObjectLink): Returns a linked base object, evaluated in the attached document.

**Typed Value Assignment**

- [`BaseContainer.SetBool()`](#c4d.BaseContainer.SetBool): Sets a bool value and changes the data type accordingly.
- [`BaseContainer.SetContainer()`](#c4d.BaseContainer.SetContainer): Sets a [`BaseContainer`](#c4d.BaseContainer) value and changes the data type accordingly.
- [`BaseContainer.SetFilename()`](#c4d.BaseContainer.SetFilename): Sets a new string value with the specified ID to *s* as a filepath, or inserts it if it didn’t exist.
- [`BaseContainer.SetFloat()`](#c4d.BaseContainer.SetFloat): Sets a float value and changes the data type accordingly.
- [`BaseContainer.SetInt32()`](#c4d.BaseContainer.SetInt32): Sets an int value and changes the data type accordingly.
- [`BaseContainer.SetInt64()`](#c4d.BaseContainer.SetInt64): Sets a long value and changes the data type accordingly.
- [`BaseContainer.SetLink()`](#c4d.BaseContainer.SetLink): Stores a link to an atom object with the specified ID.
- [`BaseContainer.SetMatrix()`](#c4d.BaseContainer.SetMatrix): Sets a [`Matrix`](../Matrix/index.md#c4d.Matrix) value and changes the data type accordingly.
- [`BaseContainer.SetString()`](#c4d.BaseContainer.SetString): Sets a string value and changes the data type accordingly.
- [`BaseContainer.SetTime()`](#c4d.BaseContainer.SetTime): Sets a [`BaseTime`](../BaseTime/index.md#c4d.BaseTime) value and changes the data type accordingly.
- [`BaseContainer.SetUuid()`](#c4d.BaseContainer.SetUuid): Sets a uuid value and changes the data type accordingly.
- [`BaseContainer.SetVector()`](#c4d.BaseContainer.SetVector): Sets a [`Vector`](../Vector/index.md#c4d.Vector) value and changes the data type accordingly.

**Typed Value Retrieval**

- [`BaseContainer.GetBool()`](#c4d.BaseContainer.GetBool): Returns a bool value with the specified ID, or *preset* if it doesn’t exist.
- [`BaseContainer.GetFilename()`](#c4d.BaseContainer.GetFilename): Returns a string value with the specified ID, or *preset* if it doesn’t exist.
- [`BaseContainer.GetFloat()`](#c4d.BaseContainer.GetFloat): Returns a float value with the specified ID, or *preset* if it doesn’t exist.
- [`BaseContainer.GetInt32()`](#c4d.BaseContainer.GetInt32): Returns a int value with the specified ID, or *preset* if it doesn’t exist.
- [`BaseContainer.GetInt64()`](#c4d.BaseContainer.GetInt64): Returns a long value with the specified ID, or *preset* if it doesn’t exist.
- [`BaseContainer.GetMatrix()`](#c4d.BaseContainer.GetMatrix): Returns a [`Matrix`](../Matrix/index.md#c4d.Matrix) value with the specified ID, or *preset* if it doesn’t exist.
- [`BaseContainer.GetString()`](#c4d.BaseContainer.GetString): Returns a string value with the specified ID, or *preset* if it doesn’t exist.
- [`BaseContainer.GetTime()`](#c4d.BaseContainer.GetTime): Returns a [`BaseTime`](../BaseTime/index.md#c4d.BaseTime) value with the specified ID, or *preset* if it doesn’t exist.
- [`BaseContainer.GetUuid()`](#c4d.BaseContainer.GetUuid): Returns a uuid value with the specified ID, or *preset* if it doesn’t exist.
- [`BaseContainer.GetVector()`](#c4d.BaseContainer.GetVector): Returns a [`Vector`](../Vector/index.md#c4d.Vector) value with the specified ID, or *preset* if it doesn’t exist.

## Members <a id="members"></a>

### Deprecated <a id="c4d.BaseContainer-method-Deprecated"></a>

#### `BaseContainer.GetLLong(self, id, preset=0)` <a id="c4d.BaseContainer.GetLLong"></a>

*Deprecated since version R15:* Use [`GetInt64()`](#c4d.BaseContainer.GetInt64) instead.

Returns a long value with the specified ID, or *preset* if it doesn’t exist.

**Parameters:**

- **id** (*int*) – The ID of the requested value.
- **preset** (*int*) – Returned if the value is not available.

**Return type:** int

**Returns:** The value.

#### `BaseContainer.GetLong(self, id, preset=0)` <a id="c4d.BaseContainer.GetLong"></a>

*Deprecated since version R15:* Use [`GetInt32()`](#c4d.BaseContainer.GetInt32) instead.

Returns a int value with the specified ID, or *preset* if it doesn’t exist.

**Parameters:**

- **id** (*int*) – The ID of the requested value.
- **preset** (*int*) – Returned if the value is not available.

**Return type:** int

**Returns:** The value.

#### `BaseContainer.GetReal(self, id, preset=0.0)` <a id="c4d.BaseContainer.GetReal"></a>

*Deprecated since version R15:* Use [`GetFloat()`](#c4d.BaseContainer.GetFloat) instead.

Returns a float value with the specified ID, or *preset* if it doesn’t exist.

**Parameters:**

- **id** (*int*) – The ID of the requested value.
- **preset** (*float*) – Returned if the value is not available.

**Return type:** float

**Returns:** The value.

#### `BaseContainer.SetLLong(self, id, l)` <a id="c4d.BaseContainer.SetLLong"></a>

*Deprecated since version R15:* Use [`SetInt64()`](#c4d.BaseContainer.SetInt64) instead.

Sets a long value and changes the data type accordingly.

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **l** (*int*) – The new value.

#### `BaseContainer.SetLong(self, id, l)` <a id="c4d.BaseContainer.SetLong"></a>

*Deprecated since version R15:* Use [`SetInt32()`](#c4d.BaseContainer.SetInt32) instead.

Sets an int value and changes the data type accordingly.

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **l** (*int*) – The new value.

#### `BaseContainer.SetReal(self, id, v)` <a id="c4d.BaseContainer.SetReal"></a>

*Deprecated since version R15:* Use [`SetFloat()`](#c4d.BaseContainer.SetFloat) instead.

Sets a float value and changes the data type accordingly.

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **l** (*int*) – The new value.

### Generic Data Access <a id="c4d.BaseContainer-method-Generic-Data-Access"></a>

#### `BaseContainer.GetData(self, id)` <a id="c4d.BaseContainer.GetData"></a>

Returns the data for an element by ID.

**Parameters:** **id** (*int*) – The ID of the element.

**Return type:** Optional[Any]

**Returns:** The data or **None** if it wasn’t found.

#### `BaseContainer.GetDataPointer(self, id)` <a id="c4d.BaseContainer.GetDataPointer"></a>

Retrieves a pointer to directly access the data.

*New in version R17.053.*

```python
bc = c4d.BaseContainer()
bc[1000] = "hello"
bc[2000] = "world"

# Print content
print("Original:")
for dataid, data in bc:
    print(data)

dataptr = bc.GetDataPointer(1000)
bc.InsDataAfter(3000, "beautiful", dataptr)

# Print content
print("Changed:")
for dataid, data in bc:
    print(data)
print(" ")
```

**Parameters:** **id** (*int*) – The ID of the element.

**Return type:** PyCObject

**Returns:** A pointer to the data.

#### `BaseContainer.GetVoid(self, id)` <a id="c4d.BaseContainer.GetVoid"></a>

Gets the void* value at the specified id.

**Parameters:** **id** (*int*) – The ID of the requested void object.

**Return type:** PyCObject

**Returns:** The PyCObject representing the void object.

#### `BaseContainer.SetData(self, id, n)` <a id="c4d.BaseContainer.SetData"></a>

Sets an arbitrary data value at the specified ID.  
If a value exists under the same ID, its content will be changed.

**Parameters:**

- **id** (*int*) – The ID of the element to set.
- **n** (*any*) – The data value to set.

#### `BaseContainer.SetDataNoDirty(self, id, n)` <a id="c4d.BaseContainer.SetDataNoDirty"></a>

Sets arbitrary data at the specified id without setting the container dirty.  
If a value exists under the same ID, its content will be changed. This function will not set the container dirty and can be used to store data without affecting the object system evaluation.

*New in version 2025.0.0.*

**Parameters:**

- **id** (*int*) – The ID of the element to set.
- **n** (*any*) – The data value to set.

#### `BaseContainer.SetVoid(self, id, v)` <a id="c4d.BaseContainer.SetVoid"></a>

Stores a PyCObject to an void* object with the specified ID.

**Parameters:**

- **id** (*int*) – The ID of the requested void object.
- **v** (*PyCObject*) – The void* as a PyCObject to store.

### Identity And State <a id="c4d.BaseContainer-method-Identity-And-State"></a>

#### `BaseContainer.GetDirty(self)` <a id="c4d.BaseContainer.GetDirty"></a>

Returns the dirty count.  
Can be used to check if the container has changed.

**Return type:** int

**Returns:** Dirty counter. It is incremented when the container changes.

#### `BaseContainer.GetId(self)` <a id="c4d.BaseContainer.GetId"></a>

Returns the ID of the container.

**Return type:** int

**Returns:** The container ID.

#### `BaseContainer.IsInstance(self)` <a id="c4d.BaseContainer.IsInstance"></a>

Checks if the container is an instance.

**Return type:** bool

**Returns:** **True** if the container is an instance, otherwise **False**.

#### `BaseContainer.SetId(self, id)` <a id="c4d.BaseContainer.SetId"></a>

Sets the ID of the container.

**Parameters:** **id** (*int*) – The container ID.

### Index And Entry Management <a id="c4d.BaseContainer-method-Index-And-Entry-Management"></a>

#### `BaseContainer.FindIndex(self, i)` <a id="c4d.BaseContainer.FindIndex"></a>

Returns the index for the value with the specified ID and its assigned data, or -1 if no such value exists.

**Parameters:** **i** (*int*) – The ID of the value.

**Return type:** Dict[**index**: int, **ppData**: Any]

**Returns:** The index of the value, or -1 if not found and its assigned data if found.

#### `BaseContainer.GetIndexData(self, index)` <a id="c4d.BaseContainer.GetIndexData"></a>

Retrieves the data for the element at *index*.

*New in version R16.038.*

**Parameters:** **index** (*int*) – The index of the element.

**Return type:** Optional[Any]

**Returns:** The data, or **None** if no data was found.

#### `BaseContainer.GetIndexId(self, index)` <a id="c4d.BaseContainer.GetIndexId"></a>

Returns the ID of the element at the specified index, or *NOTOK* if it doesn’t exist.  
Used to browse through the container.

**Parameters:** **index** (*int*) – The index of the value.

**Return type:** bool

**Returns:** The ID of the value, or *NOTOK*.

#### `BaseContainer.GetType(self, id)` <a id="c4d.BaseContainer.GetType"></a>

Returns the type of a container element by ID.

**Parameters:** **id** (*int*) – The ID of the element.

**Return type:** int

**Returns:**

The type:

|   |   |
|---|---|
| *DA_NIL* | No value. |
| *DA_VOID* | PyCObject |
| *DA_LONG* | Integer. |
| *DA_REAL* | Float. |
| *DA_TIME* | [`BaseTime`](../BaseTime/index.md#c4d.BaseTime). |
| *DA_VECTOR* | [`Vector`](../Vector/index.md#c4d.Vector). |
| *DA_MATRIX* | [`Matrix`](../Matrix/index.md#c4d.Matrix). |
| *DA_LLONG* | Integer. |
| *DA_STRING* | String. |
| *DA_FILENAME* | String. |
| *DA_CONTAINER* | [`BaseContainer`](#c4d.BaseContainer). |
| *DA_ALIASLINK* | [`BaseList2D`](../C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D). |
| *DA_MARKER* | Not used. |
| *DA_MISSINGPLUG* | Denotes a missing datatype plugin. |
| *DA_UUID* | *New in version R17.048:* [UUID](https://docs.python.org/3.9/library/uuid.html#uuid.UUID). |
| *DA_TRISTATE* | *New in version R20:* No single value. |
| *DA_CUSTOMDATATYPE* | Datatypes higher than this value are custom. |

#### `BaseContainer.InsData(self, id, n)` <a id="c4d.BaseContainer.InsData"></a>

Inserts an arbitrary data at the specified *id*.

> **Warning:** This function does not check if the ID already exists in the container!

**Parameters:**

- **id** (*int*) – The ID to insert at.
- **n** (*any*) – The data to insert.

**Return type:** Any

**Returns:** The inserted data.

#### `BaseContainer.InsDataAfter(self, id, n, last)` <a id="c4d.BaseContainer.InsDataAfter"></a>

Inserts an arbitrary data at the specified *id* after *last*.

> **Warning:** This function does not check if the ID already exists in the container!

**Parameters:**

- **id** (*int*) – The ID to insert at.
- **n** (*any*) – The data to insert.
- **last** (*any*) – The data to insert after.

**Return type:** Any

**Returns:** The inserted data.

#### `BaseContainer.RemoveData(self, id)` <a id="c4d.BaseContainer.RemoveData"></a>

Removes the first data item with the specified ID.

**Parameters:** **id** (*int*) – The container ID.

**Return type:** bool

**Returns:** **True** if any value was removed, otherwise **False**.

#### `BaseContainer.RemoveIndex(self, i)` <a id="c4d.BaseContainer.RemoveIndex"></a>

Removes the data item at the specified index *i*.

**Parameters:** **i** (*int*) – The index of the value to be removed.

**Return type:** bool

**Returns:** **True** if any value was removed, otherwise **False**.

#### `BaseContainer.SetIndexData(self, index, data)` <a id="c4d.BaseContainer.SetIndexData"></a>

Sets the data for the element at *index*.

*New in version R16.038.*

**Parameters:**

- **index** (*int*) – The index of the element.
- **data** (*any*) – The data for the element.

**Return type:** bool

**Returns:** **True** if the data was set, otherwise **False**.

#### `BaseContainer.Sort(self)` <a id="c4d.BaseContainer.Sort"></a>

Sorts a container strings by their ID.  
Intended for sorting menus and other string containers. Is useless for containers that hold any other type of data.

warning:

```python
Will replace all entries with string entries that are not strings or sub-containers.
```

### Lifecycle And Composition <a id="c4d.BaseContainer-method-Lifecycle-And-Composition"></a>

#### `BaseContainer.CopyTo(self, dst, flags, trans=None)` <a id="c4d.BaseContainer.CopyTo"></a>

Copies all values to *dst*.

**Parameters:**

- **dst** ([*c4d.BaseContainer*](#c4d.BaseContainer)) – The destination container.

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *COPYFLAGS_NONE* | None. |
  | *COPYFLAGS_PRIVATE_CONTAINER_COPY_DIRTY* | Private. |
  | *COPYFLAGS_PRIVATE_CONTAINER_COPY_IDENTICAL* | Private. |

- **trans** (*Optional*[[*c4d.AliasTrans*](../AliasTrans/index.md#c4d.AliasTrans)]) –

  *New in version R17.032.*

  An optional alias translator for the operation.

#### `BaseContainer.FlushAll(self)` <a id="c4d.BaseContainer.FlushAll"></a>

Clears all values in the container.  
The container ID is not changed.

#### `BaseContainer.GetClone(self, flags, trans=None)` <a id="c4d.BaseContainer.GetClone"></a>

Returns a copy of the container including all values.

**Parameters:**

- **flags** (*int*) –

  Flags:

  |   |   |
  |---|---|
  | *COPYFLAGS_NONE* | None. |
  | *COPYFLAGS_PRIVATE_CONTAINER_COPY_DIRTY* | Private. |
  | *COPYFLAGS_PRIVATE_CONTAINER_COPY_IDENTICAL* | Private. |

- **trans** (*Optional*[[*c4d.AliasTrans*](../AliasTrans/index.md#c4d.AliasTrans)]) –

  *New in version R17.032.*

  An optional alias translator for the operation.

**Return type:** [c4d.BaseContainer](#c4d.BaseContainer)

**Returns:** The cloned container.

#### `BaseContainer.MergeContainer(self, src)` <a id="c4d.BaseContainer.MergeContainer"></a>

Stores the values in src in this container, overwriting any elements with colliding IDs and keeping the rest.

**Parameters:** **src** ([*c4d.BaseContainer*](#c4d.BaseContainer)) – The source container.

### Magic Methods <a id="c4d.BaseContainer-method-Magic-Methods"></a>

#### `BaseContainer.__eq__(self, other)` <a id="c4d.BaseContainer.__eq__"></a>

Check if the compared containers have the same ID, have the same values, and all values are equal.

**Parameters:** **other** ([*c4d.BaseContainer*](#c4d.BaseContainer)) – Returns **True** if the compared containers are equal.

#### `BaseContainer.__getitem__(self, key)` <a id="c4d.BaseContainer.__getitem__"></a>

Returns a value with the specified ID.

**Parameters:** **key** (*int*) – Index of the value.

**Return type:** Any

**Returns:** Any value.

#### `BaseContainer.__init__(self, n=-1)` <a id="c4d.BaseContainer.__init__"></a>

Initializes a new container.

**Parameters:** **n** (*Optional*[*Union*[[*c4d.BaseContainer*](#c4d.BaseContainer), *int*]]) – Use int if you just want to set the ID of the container. Pass a container if you want to clone it, or **None** to use a standard empty container.

#### `BaseContainer.__iter__(self)` <a id="c4d.BaseContainer.__iter__"></a>

The BaseContainer is iterable so just use it like in the following example:

```python
>>> bc = c4d.BaseContainer()
>>> bc[0] = "foo"
>>> bc[37] = "bar"
>>> bc[42] = False

>>> for index, value in bc:
...     print(f"id: {index}, val: {value}")
id: 0, val: foo
id: 37, val: bar
id: 42, val: 0
```

#### `BaseContainer.__len__(self)` <a id="c4d.BaseContainer.__len__"></a>

Calculates the number of data elements inside the container.

**Return type:** int

**Returns:** The number of data elements.

#### `BaseContainer.__ne__(self, other)` <a id="c4d.BaseContainer.__ne__"></a>

Check if the compared containers don’t have the same ID, don’t have the same values, and all values are not equal.

**Parameters:** **other** ([*c4d.BaseContainer*](#c4d.BaseContainer)) – Returns **True** if the compared containers are equal.

#### `BaseContainer.__setitem__(self, key, value)` <a id="c4d.BaseContainer.__setitem__"></a>

Automatically redirect the value to the corresponding Set* method.  
Its recommended to use the original Set* method to avoid type problems.

> **Warning:**
>
> This method can replace types.  
> Please check the types before when a special key is associated with a special type.

To delete a key, call *del(bc[i])* or [`RemoveData()`](#c4d.BaseContainer.RemoveData).

**Parameters:**

- **key** (*int*) – Index of the value.
- **value** (*any*) – It depends on the type which Set* method is internally called.

### Nested And Linked Data <a id="c4d.BaseContainer-method-Nested-And-Linked-Data"></a>

#### `BaseContainer.GetContainer(self, id)` <a id="c4d.BaseContainer.GetContainer"></a>

Returns a copy of the sub-container with the specified ID, or an empty container if it doesn’t exist.

**Parameters:** **id** (*int*) – The ID of the requested sub-container.

**Return type:** [c4d.BaseContainer](#c4d.BaseContainer)

**Returns:** The Sub-container.

#### `BaseContainer.GetContainerInstance(self, id)` <a id="c4d.BaseContainer.GetContainerInstance"></a>

Returns the sub-container with the specified ID, or **None** if it doesn’t exist.  
Changes to the container are reflected in the stored sub-container.

**Parameters:** **id** (*int*) – The ID of the requested sub-container.

**Return type:** Optional[[c4d.BaseContainer](#c4d.BaseContainer)]

**Returns:** The sub-container, or **None**.

#### `BaseContainer.GetCustomDataType(self, id)` <a id="c4d.BaseContainer.GetCustomDataType"></a>

Returns a copy of the custom data type or **None** if it doesn’t exist.

**Parameters:** **id** (*int*) – The ID of the requested sub-container.

**Returns:** The custom data type.

**Return type:** Optional[object]

#### `BaseContainer.GetLink(self, id, doc=None, isinstanceof=0)` <a id="c4d.BaseContainer.GetLink"></a>

Returns a linked object, evaluated in the attached document.

> **Note:** If *instanceof* is specified, **None** is returned if the object is not of this type.

**Parameters:**

- **id** (*int*) – The ID of the requested sub-container.
- **doc** (*Optional*[[*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]) – The document to evalulate the link in or **None**.
- **isinstanceof** (*int*) – Set this to a node type to only return the link if it is of this type.

**Return type:** Optional[[c4d.BaseList2D](../C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The linked object, or **None** if the link is broken.

#### `BaseContainer.GetMaterialLink(self, id, doc=None)` <a id="c4d.BaseContainer.GetMaterialLink"></a>

Returns a linked material object, evaluated in the attached document.

> **Note:** Returns **None** if the link doesn’t point to a base object.

**Parameters:**

- **id** (*int*) – The ID of the requested sub-container.
- **doc** (*Optional*[[*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]) – The document to evalulate the link in.

**Return type:** Optional[[c4d.BaseMaterial](../C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial)]

**Returns:** The linked material object, or **None** if the link is broken.

#### `BaseContainer.GetObjectLink(self, id, doc=None)` <a id="c4d.BaseContainer.GetObjectLink"></a>

Returns a linked base object, evaluated in the attached document.

> **Note:** Returns **None** if the link doesn’t point to a base object.

**Parameters:**

- **id** (*int*) – The ID of the requested sub-container.
- **doc** (*Optional*[[*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)]) – The document to evalulate the link in.

**Return type:** Optional[[c4d.BaseObject](../C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

**Returns:** The linked base object, or **None** if the link is broken.

### Typed Value Assignment <a id="c4d.BaseContainer-method-Typed-Value-Assignment"></a>

#### `BaseContainer.SetBool(self, id, b)` <a id="c4d.BaseContainer.SetBool"></a>

Sets a bool value and changes the data type accordingly.

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **b** (*bool*) – The new value.

#### `BaseContainer.SetContainer(self, id, s)` <a id="c4d.BaseContainer.SetContainer"></a>

Sets a [`BaseContainer`](#c4d.BaseContainer) value and changes the data type accordingly.

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **s** ([*c4d.BaseContainer*](#c4d.BaseContainer)) – The sub-container

#### `BaseContainer.SetFilename(self, id, f)` <a id="c4d.BaseContainer.SetFilename"></a>

Sets a new string value with the specified ID to *s* as a filepath, or inserts it if it didn’t exist.

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **f** (*str*) – The new value.

#### `BaseContainer.SetFloat(self, id, v)` <a id="c4d.BaseContainer.SetFloat"></a>

Sets a float value and changes the data type accordingly.

*New in version R15.037.*

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **l** (*int*) – The new value.

#### `BaseContainer.SetInt32(self, id, l)` <a id="c4d.BaseContainer.SetInt32"></a>

Sets an int value and changes the data type accordingly.

*New in version R15.037.*

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **l** (*int*) – The new value.

#### `BaseContainer.SetInt64(self, id, l)` <a id="c4d.BaseContainer.SetInt64"></a>

Sets a long value and changes the data type accordingly.

*New in version R15.037.*

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **l** (*int*) – The new value.

#### `BaseContainer.SetLink(self, id, link)` <a id="c4d.BaseContainer.SetLink"></a>

Stores a link to an atom object with the specified ID.

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **link** ([*c4d.C4DAtom*](../C4DAtom/index.md#c4d.C4DAtom)) – The link to store.

#### `BaseContainer.SetMatrix(self, id, m)` <a id="c4d.BaseContainer.SetMatrix"></a>

Sets a [`Matrix`](../Matrix/index.md#c4d.Matrix) value and changes the data type accordingly.

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **m** ([*c4d.Matrix*](../Matrix/index.md#c4d.Matrix)) – The new value.

#### `BaseContainer.SetString(self, id, s)` <a id="c4d.BaseContainer.SetString"></a>

Sets a string value and changes the data type accordingly.

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **s** (*str*) – The new value.

#### `BaseContainer.SetTime(self, id, b)` <a id="c4d.BaseContainer.SetTime"></a>

Sets a [`BaseTime`](../BaseTime/index.md#c4d.BaseTime) value and changes the data type accordingly.

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **b** ([*c4d.BaseTime*](../BaseTime/index.md#c4d.BaseTime)) – The new value.

#### `BaseContainer.SetUuid(self, id, u)` <a id="c4d.BaseContainer.SetUuid"></a>

Sets a uuid value and changes the data type accordingly.

*New in version R16.021.*

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **u** – The new value.

#### `BaseContainer.SetVector(self, id, v)` <a id="c4d.BaseContainer.SetVector"></a>

Sets a [`Vector`](../Vector/index.md#c4d.Vector) value and changes the data type accordingly.

**Parameters:**

- **id** (*int*) – The ID of the value to set.
- **v** ([*c4d.Vector*](../Vector/index.md#c4d.Vector)) – The new value.

### Typed Value Retrieval <a id="c4d.BaseContainer-method-Typed-Value-Retrieval"></a>

#### `BaseContainer.GetBool(self, id, preset=False)` <a id="c4d.BaseContainer.GetBool"></a>

Returns a bool value with the specified ID, or *preset* if it doesn’t exist.

**Parameters:**

- **id** (*int*) – The ID of the requested value.
- **preset** (*bool*) – Returned if the value is not available.

**Return type:** bool

**Returns:** The value.

#### `BaseContainer.GetFilename(self, id, preset='')` <a id="c4d.BaseContainer.GetFilename"></a>

Returns a string value with the specified ID, or *preset* if it doesn’t exist.

**Parameters:**

- **id** (*int*) – The ID of the requested value.
- **preset** (*str*) – Returned if the value is not available.

**Return type:** str

**Returns:** The value.

#### `BaseContainer.GetFloat(self, id, preset=0.0)` <a id="c4d.BaseContainer.GetFloat"></a>

Returns a float value with the specified ID, or *preset* if it doesn’t exist.

*New in version R15.037.*

**Parameters:**

- **id** (*int*) – The ID of the requested value.
- **preset** (*float*) – Returned if the value is not available.

**Return type:** float

**Returns:** The value.

#### `BaseContainer.GetInt32(self, id, preset=0)` <a id="c4d.BaseContainer.GetInt32"></a>

Returns a int value with the specified ID, or *preset* if it doesn’t exist.

*New in version R15.037.*

**Parameters:**

- **id** (*int*) – The ID of the requested value.
- **preset** (*int*) – Returned if the value is not available.

**Return type:** int

**Returns:** The value.

#### `BaseContainer.GetInt64(self, id, preset=0)` <a id="c4d.BaseContainer.GetInt64"></a>

Returns a long value with the specified ID, or *preset* if it doesn’t exist.

*New in version R15.037.*

**Parameters:**

- **id** (*int*) – The ID of the requested value.
- **preset** (*int*) – Returned if the value is not available.

**Return type:** int

**Returns:** The value.

#### `BaseContainer.GetMatrix(self, id, preset=<_custom_c4d.Matrix object at 0x0000012EC3F09AE0>)` <a id="c4d.BaseContainer.GetMatrix"></a>

Returns a [`Matrix`](../Matrix/index.md#c4d.Matrix) value with the specified ID, or *preset* if it doesn’t exist.

**Parameters:**

- **id** (*int*) – The ID of the requested value.
- **preset** ([*c4d.Matrix*](../Matrix/index.md#c4d.Matrix)) – Returned if the value is not available.

**Return type:** [c4d.Matrix](../Matrix/index.md#c4d.Matrix)

**Returns:** The value.

#### `BaseContainer.GetString(self, id, preset='')` <a id="c4d.BaseContainer.GetString"></a>

Returns a string value with the specified ID, or *preset* if it doesn’t exist.

**Parameters:**

- **id** (*int*) – The ID of the requested value.
- **preset** (*str*) – Returned if the value is not available.

**Return type:** str

**Returns:** The value.

#### `BaseContainer.GetTime(self, id, preset=<_custom_c4d.BaseTime object at 0x0000012EC3F131A0>)` <a id="c4d.BaseContainer.GetTime"></a>

Returns a [`BaseTime`](../BaseTime/index.md#c4d.BaseTime) value with the specified ID, or *preset* if it doesn’t exist.

**Parameters:**

- **id** (*int*) – The ID of the requested value.
- **preset** ([*c4d.BaseTime*](../BaseTime/index.md#c4d.BaseTime)) – Returned if the value is not available.

**Return type:** [c4d.BaseTime](../BaseTime/index.md#c4d.BaseTime)

**Returns:** The value.

#### `BaseContainer.GetUuid(self, id, preset)` <a id="c4d.BaseContainer.GetUuid"></a>

Returns a uuid value with the specified ID, or *preset* if it doesn’t exist.

*New in version R16.021.*

**Parameters:**

- **id** (*int*) – The ID of the requested value.
- **preset** – Returned if the value is not available.

**Return type:** [UUID](https://docs.python.org/3.9/library/uuid.html#uuid.UUID)

**Returns:** The value.

#### `BaseContainer.GetVector(self, id, preset=<_custom_c4d.Vector object at 0x0000012EC3F08820>)` <a id="c4d.BaseContainer.GetVector"></a>

Returns a [`Vector`](../Vector/index.md#c4d.Vector) value with the specified ID, or *preset* if it doesn’t exist.

**Parameters:**

- **id** (*int*) – The ID of the requested value.
- **preset** ([*c4d.Vector*](../Vector/index.md#c4d.Vector)) – Returned if the value is not available.

**Return type:** [c4d.Vector](../Vector/index.md#c4d.Vector)

**Returns:** The value.
