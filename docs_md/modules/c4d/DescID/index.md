<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/DescID/index.html -->

# c4d.DescID <a id="c4d-descid"></a>

## *class* `c4d.DescID` <a id="c4d.DescID"></a>

An ID class for description elements. Contains a stack of [`DescLevel`](../DescLevel/index.md#c4d.DescLevel) objects.

The description ID is used to exactly identify a parameter value.

**Constants**

## `c4d.DESCID_ROOT` <a id="c4d.DESCID_ROOT"></a>

Root description ID.

## `c4d.ID_USERDATA` <a id="c4d.ID_USERDATA"></a>

User data ID.

## `c4d.DESCID_DYNAMICSUB` <a id="c4d.DESCID_DYNAMICSUB"></a>

User data/dynamic parameters description level.

## Overview <a id="overview"></a>

**Identity And Matching**

- [`DescID.GetHashCode()`](#c4d.DescID.GetHashCode): Gets a hash code for the description ID.
- [`DescID.IsPartOf()`](#c4d.DescID.IsPartOf): Checks if the description ID is part of *cmp* and returns the length of the match.

**Magic Methods**

- [`DescID.__eq__()`](#c4d.DescID.__eq__): Checks if all levels are equal.
- [`DescID.__getitem__()`](#c4d.DescID.__getitem__): Returns the level at position *key* in the stack
- [`DescID.__init__()`](#c4d.DescID.__init__): Initializes a *c4d.DescID* from up to three *c4d.DescLevel* instances or an integer.
- [`DescID.__lshift__()`](#c4d.DescID.__lshift__): Returns the result of popping *shift* levels from the **bottom** of the stack
- [`DescID.__ne__()`](#c4d.DescID.__ne__): The reverse of `__eq__`.
- [`DescID.__str__()`](#c4d.DescID.__str__): Returns a string representation of the DescID object.

**Persistence**

- [`DescID.Read()`](#c4d.DescID.Read): Reads the description from a file.
- [`DescID.Write()`](#c4d.DescID.Write): Writes the description to a file.

**Stack Navigation**

- [`DescID.GetDepth()`](#c4d.DescID.GetDepth): Return the depth.
- [`DescID.PopId()`](#c4d.DescID.PopId): Pops the highest level from the stack.
- [`DescID.PushId()`](#c4d.DescID.PushId): Push a new level onto the stack.
- [`DescID.SetId()`](#c4d.DescID.SetId): Set the highest level to *subid*.

## Members <a id="members"></a>

### Identity And Matching <a id="c4d.DescID-method-Identity-And-Matching"></a>

#### `DescID.GetHashCode(self)` <a id="c4d.DescID.GetHashCode"></a>

Gets a hash code for the description ID.

*New in version R17.048.*

**Return type:** int

**Returns:** The hash code.

#### `DescID.IsPartOf(self, cmp)` <a id="c4d.DescID.IsPartOf"></a>

Checks if the description ID is part of *cmp* and returns the length of the match.

*New in version R18.020.*

**Parameters:**

**cmp** (*Union*[*int*, *list*, [*c4d.DescID*](#c4d.DescID)]) –

The super description ID.

*Changed in version R18.057.*

Can be a int, list or [`DescID`](#c4d.DescID)

**Return type:** Tuple[bool, int]

**Returns:**

A tuple with the following information:

bool: **True** if the description ID matches a lowest part of *cmp*, otherwise **False**.  
int: The length of the match.

### Magic Methods <a id="c4d.DescID-method-Magic-Methods"></a>

#### `DescID.__eq__(self, other)` <a id="c4d.DescID.__eq__"></a>

Checks if all levels are equal.

#### `DescID.__getitem__(self, key)` <a id="c4d.DescID.__getitem__"></a>

Returns the level at position *key* in the stack

```python
>>> dId = c4d.DescID(c4d.DescLevel(30), c4d.DescLevel(40), c4d.DescLevel(50))
>>> dId[2]
<c4d.DescLevel object at 0x00000265FBB1F600>
```

**Parameters:** **key** (*int*) – The position.

**Raises:** **IndexError** – If *other* is out of range : *0<=key<*[`GetDepth()`](#c4d.DescID.GetDepth).

**Return type:** [c4d.DescLevel](../DescLevel/index.md#c4d.DescLevel)

**Returns:** The level at the specified position.

#### `DescID.__init__(self, id1=0, id2=0, id3=0)` <a id="c4d.DescID.__init__"></a>

Initializes a *c4d.DescID* from up to three *c4d.DescLevel* instances or an integer.

```python
# op: c4d.BaseObject # An object to access parameters for.

# Construct an ID from an integer directly, this only works when `id1` is the only
# argument. One can path either one of the ID symbols or a numeric literal. Here we 
# construct the ID for the relative position of an object.
idPos: c4d.DescID = c4d.DescID(903)
idPos: c4d.DescID = c4d.DescID(c4d.ID_BASEOBJECT_REL_POSITION) # Same as 903

# But `c4d.DescID` instances can have up to three levels. Here we construct the ID for 
# the x-component of the relative position vector of an object.
idPosX: c4d.DescID = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION), 
                                c4d.DescLevel(c4d.VECTOR_X))

# Or a three level ID for the x-component of a vector inside the user data container. 
# The addressed element is the first user data element as expressed by the second level.
idUserVecX: c4d.DescID = c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA),
                                    c4d.DescLevel(1), 
                                    c4d.DescLevel(c4d.VECTOR_X))

# And finally the ID for the x component of the relative potion of an object expressed
# with the highest possible precision. Here we also express data types and ownership.
# Being that precise this is usually only necessary when interacting with descriptions.
# For parameter access the former definition `idPosX` will suffice.
idPosX: c4d.DescID = c4d.DescID(
    c4d.DescLevel(
        c4d.ID_BASEOBJECT_REL_POSITION, # The ID of the first level, the whole vector.
        c4d.DTYPE_VECTOR,               # The data type of the first level.
        op.GetType()                    # The owner of the parameter, usually the type 
                                        # of the node, e.g., `c4d.Ocube`.
    ),
    c4d.DescLevel(
        c4d.VECTOR_X,                   # The ID of the second level, here the x-component
                                        # of the vector.
        c4d.DTYPE_REAL,                 # The data type of this channel/level. A vector
                                        # is composed out of three real numbers.
        0                               # Ownership is usually only defined for the
                                        # first level.
    )
)
```

**Parameters:**

- **id1** (*Optional*[*Union*[*int*, [*c4d.DescLevel*](../DescLevel/index.md#c4d.DescLevel)]]) – First level.
- **id2** (*Optional*[[*c4d.DescLevel*](../DescLevel/index.md#c4d.DescLevel)]) – Second level.
- **id3** (*Optional*[[*c4d.DescLevel*](../DescLevel/index.md#c4d.DescLevel)]) – Third level.

#### `DescID.__lshift__(self, other)` <a id="c4d.DescID.__lshift__"></a>

Returns the result of popping *shift* levels from the **bottom** of the stack

```python
>>> dId = c4d.DescID(c4d.DescLevel(30), c4d.DescLevel(40), c4d.DescLevel(50))
>>> dId<<2
(50, 0, 0)
```

**Parameters:** **other** (*int*) – Number of levels to pop.

**Raises:** **IndexError** – If *other* is out of range : *0<=other<*[`GetDepth()`](#c4d.DescID.GetDepth).

**Return type:** [c4d.DescID](#c4d.DescID)

**Returns:** Result.

#### `DescID.__ne__(self, other)` <a id="c4d.DescID.__ne__"></a>

The reverse of `__eq__`.

#### `DescID.__str__(self)` <a id="c4d.DescID.__str__"></a>

Returns a string representation of the DescID object.  
Called if [str()](https://docs.python.org/3.9/library/functions.html#func-str) is invoked on a [`DescID`](#c4d.DescID) object. See [object.__str__()](https://docs.python.org/3.9/reference/datamodel.html#object.__str__) for more information on Python’s data model.

```python
>>> dId = c4d.DescID(c4d.DescLevel(30))
>>> print(dId)
(30, 0, 0)
```

**Return type:** str

**Returns:** The DescID as string.

### Persistence <a id="c4d.DescID-method-Persistence"></a>

#### `DescID.Read(self, hf)` <a id="c4d.DescID.Read"></a>

Reads the description from a file.

**Parameters:** **hf** ([*c4d.storage.HyperFile*](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile)) – The hyperfile to read from.

**Return type:** bool

**Returns:** True if successful, otherwise False.

#### `DescID.Write(self, hf)` <a id="c4d.DescID.Write"></a>

Writes the description to a file.

**Parameters:** **hf** ([*c4d.storage.HyperFile*](../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile)) – The hyperfile to write to.

### Stack Navigation <a id="c4d.DescID-method-Stack-Navigation"></a>

#### `DescID.GetDepth(self)` <a id="c4d.DescID.GetDepth"></a>

Return the depth.

**Return type:** int

**Returns:** The depth.

#### `DescID.PopId(self)` <a id="c4d.DescID.PopId"></a>

Pops the highest level from the stack.

#### `DescID.PushId(self, subid)` <a id="c4d.DescID.PushId"></a>

Push a new level onto the stack.

**Parameters:** **subid** ([*c4d.DescLevel*](../DescLevel/index.md#c4d.DescLevel)) – Level to push.

#### `DescID.SetId(self, subid)` <a id="c4d.DescID.SetId"></a>

Set the highest level to *subid*.

**Parameters:** **subid** ([*c4d.DescLevel*](../DescLevel/index.md#c4d.DescLevel)) – New toplevel.
