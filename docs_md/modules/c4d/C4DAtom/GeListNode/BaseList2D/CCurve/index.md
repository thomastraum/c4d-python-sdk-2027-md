<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/CCurve/index.html -->

# c4d.CCurve <a id="c4d-ccurve"></a>

## *class* `c4d.CCurve` <a id="c4d.CCurve"></a>

This is the animation curve base class.  
Belongs to a [`CTrack`](../CTrack/index.md#c4d.CTrack) that contain [`CKeys`](../../../CKey/index.md#c4d.CKey).

Parent Class:

- [`c4d.BaseList2D`](../index.md#c4d.BaseList2D)

## Overview <a id="overview"></a>

**Curve Evaluation**

- [`CCurve.GetEndTime()`](#c4d.CCurve.GetEndTime): Returns the end time of the curve.
- [`CCurve.GetStartTime()`](#c4d.CCurve.GetStartTime): Returns the start time of the curve.
- [`CCurve.GetValue()`](#c4d.CCurve.GetValue): Get the value calculated at *time*, taking into account things like timecurves.

**Key Access**

- [`CCurve.FindKey()`](#c4d.CCurve.FindKey): Find a writable key by time.
- [`CCurve.GetKey()`](#c4d.CCurve.GetKey): Get a writeable key by index.
- [`CCurve.GetKeyCount()`](#c4d.CCurve.GetKeyCount): Returns the count of [`CKey`](../../../CKey/index.md#c4d.CKey)

**Key Editing**

- [`CCurve.AddKey()`](#c4d.CCurve.AddKey): Adds a *CKey \<c4d.CKey>* to the curve.
- [`CCurve.AddKeyAdaptTangent()`](#c4d.CCurve.AddKeyAdaptTangent): Add a key to the curve but retain the curve’s current curvature.
- [`CCurve.DelKey()`](#c4d.CCurve.DelKey): Delete a key from this curve.
- [`CCurve.FlushKeys()`](#c4d.CCurve.FlushKeys): Remove all keys from this curve.
- [`CCurve.InsertKey()`](#c4d.CCurve.InsertKey): Insert a key into this curve.
- [`CCurve.MoveKey()`](#c4d.CCurve.MoveKey): Move a key in the curve.
- [`CCurve.SortKeysByTime()`](#c4d.CCurve.SortKeysByTime): Private.

**Key Navigation**

- [`CCurve.FindNextUnmuted()`](#c4d.CCurve.FindNextUnmuted): Returns the next unmuted key.
- [`CCurve.FindPrevUnmuted()`](#c4d.CCurve.FindPrevUnmuted): Returns the previous unmuted key.

**Maintenance And Configuration**

- [`CCurve.GetTrack()`](#c4d.CCurve.GetTrack): Get the track of this curve.
- [`CCurve.SetKeyDefault()`](#c4d.CCurve.SetKeyDefault): Set the defaults for key *kidx* for the curve.
- [`CCurve.SetKeyDirty()`](#c4d.CCurve.SetKeyDirty): Set keys to dirty.

**Tangent Processing**

- [`CCurve.AdjustTangentAutoWeight()`](#c4d.CCurve.AdjustTangentAutoWeight): Adjusts Tangent Time and Value to reflect an auto-tangent (slope is preserved).
- [`CCurve.AdjustTangentLength()`](#c4d.CCurve.AdjustTangentLength): Adjusts Tangent Length to avoid curve intersection
- [`CCurve.GetTangents()`](#c4d.CCurve.GetTangents): Computes the tangents of a key, taking into account all options like zero slope, link slope etc.

## Members <a id="members"></a>

### Curve Evaluation <a id="c4d.CCurve-method-Curve-Evaluation"></a>

#### `CCurve.GetEndTime(self)` <a id="c4d.CCurve.GetEndTime"></a>

Returns the end time of the curve.

*New in version R19.*

**Return type:** [c4d.BaseTime](../../../../BaseTime/index.md#c4d.BaseTime)

**Returns:** The end time of the curve.

#### `CCurve.GetStartTime(self)` <a id="c4d.CCurve.GetStartTime"></a>

Returns the start time of the curve.

*New in version R19.*

**Return type:** [c4d.BaseTime](../../../../BaseTime/index.md#c4d.BaseTime)

**Returns:** The start time of the curve.

#### `CCurve.GetValue(self, time, fps)` <a id="c4d.CCurve.GetValue"></a>

Get the value calculated at *time*, taking into account things like timecurves.

**Parameters:**

- **time** ([*c4d.BaseTime*](../../../../BaseTime/index.md#c4d.BaseTime)) – The time to calculate the value at.

- **fps** (*int*) –

  *Deprecated since version R17.048:* The number of frames per second.

**Return type:** float

**Returns:** The calculated value.

### Key Access <a id="c4d.CCurve-method-Key-Access"></a>

#### `CCurve.FindKey(self, time, match=0)` <a id="c4d.CCurve.FindKey"></a>

Find a writable key by time.

```python
found = curve.FindKey(time)
if found is None:
    raise RuntimeError("Could not find key at given BaseTime.")

# The index of the retrieved key
index = found["idx"]
# The retrieved key
key = found["key"]
```

**Parameters:**

- **time** ([*c4d.BaseTime*](../../../../BaseTime/index.md#c4d.BaseTime)) – A time.

- **match** (*int*) –

  Search method:

  |   |   |
  |---|---|
  | *FINDANIM_EXACT* | Exact. |
  | *FINDANIM_LEFT* | Search left. |
  | *FINDANIM_RIGHT* | Search right. |

**Return type:** Optional[Dict[**key**: [`CKey`](../../../CKey/index.md#c4d.CKey), **int**: int]]

**Returns:** Dict with the found key and index, or **None**.

#### `CCurve.GetKey(self, index)` <a id="c4d.CCurve.GetKey"></a>

Get a writeable key by index.

**Parameters:** **index** (*int*) – Key index.

**Raises:** **IndexError** – If key *index* is out of range : *0<=index<*[`GetKeyCount()`](#c4d.CCurve.GetKeyCount).

**Return type:** Optional[[c4d.CKey](../../../CKey/index.md#c4d.CKey)]

**Returns:** The key found, or **None**.

#### `CCurve.GetKeyCount(self)` <a id="c4d.CCurve.GetKeyCount"></a>

Returns the count of [`CKey`](../../../CKey/index.md#c4d.CKey)

**Return type:** int

**Returns:** The count.

### Key Editing <a id="c4d.CCurve-method-Key-Editing"></a>

#### `CCurve.AddKey(self, time, bUndo=False, SynchronizeKeys=False)` <a id="c4d.CCurve.AddKey"></a>

Adds a *CKey \<c4d.CKey>* to the curve.

```python
# Create a cube object.
cube = c4d.BaseObject(c4d.Ocube)

# The DescId for the BaseObject position parameter x component.
descIdPosition = c4d.DescID(
    c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION, c4d.DTYPE_VECTOR, 0),
    c4d.DescLevel(c4d.VECTOR_X, c4d.DTYPE_REAL, 0))
# Create a track and insert it into our cube.
track = c4d.CTrack(cube, descIdPosition)
cube.InsertTrackSorted(track)

# Get the curve of the track.
curve = track.GetCurve()
# Add a key frame at t == 1.0 seconds.
result = curve.AddKey(c4d.BaseTime(1))

# Something went horribly wrong.
if result is None:
    raise RuntimeError("Failed to create key.")

# If we were successful, we get a result dictionary containing the key.
print(result)
# {'nidx': 0, 'key': <c4d.CKey object at 0x0000018AA3494800>}

# Get the key and set the value (of the x-component at t=1 sec)
# to 200 units.
key = result["key"]
key.SetValue(curve, 200.)

# Insert the cube object into the document.
doc.InsertObject(cube)

# Push an update event to Cinema 4D
c4d.EventAdd()
```

**Parameters:**

- **time** ([*c4d.BaseTime*](../../../../BaseTime/index.md#c4d.BaseTime)) – The time to add the key at.

- **bUndo** (*bool*) –

  *New in version R18.020.*

  If **True** this action will be undoable.

  > **Note:** The caller has to to manage start/end of undo actions with `BaseDocument.StartUndo()`/`EndUndo()`.

- **SynchronizeKeys** (*bool*) –

  *New in version R18.020.*

  If **True** the routine is called on other components of the vector (if valid). Curve must be part of a Track.

**Return type:** Optional[Dict[‘nidx’: int, ‘key’: [`c4d.CKey`](../../../CKey/index.md#c4d.CKey)]]

**Returns:** The added key index and object (**None** if it failed).

#### `CCurve.AddKeyAdaptTangent(self, time, bUndo, SynchronizeKeys=False)` <a id="c4d.CCurve.AddKeyAdaptTangent"></a>

Add a key to the curve but retain the curve’s current curvature.

*New in version R18.020.*

**Parameters:**

- **time** ([*c4d.BaseTime*](../../../../BaseTime/index.md#c4d.BaseTime)) – The time to add the key at.
- **bUndo** (*bool*) – If **True** this action will be undoable. The caller has to to manage start/end of undo actions with `BaseDocument.StartUndo()`/`EndUndo()`.
- **SynchronizeKeys** (*bool*) – If **True** the routine is called on other components of the vector (if valid). Curve must be part of a Track.

**Return type:** Optional[Dict[‘nidx’: int, ‘key’: [`c4d.CKey`](../../../CKey/index.md#c4d.CKey)]]

**Returns:** The added key index and object (**None** if it failed).

#### `CCurve.DelKey(self, index, bUndo=False, SynchronizeKeys=False)` <a id="c4d.CCurve.DelKey"></a>

Delete a key from this curve.

**Parameters:**

- **index** (*int*) – The index of the key to delete.

- **bUndo** (*bool*) –

  *New in version R18.020.*

  If **True** this action will be undoable.

  > **Note:** The caller has to to manage start/end of undo actions with `BaseDocument.StartUndo()`/`EndUndo()`.

- **SynchronizeKeys** (*bool*) –

  *New in version R18.020.*

  If **True** the routine is called on other components of the vector (if valid). Curve must be part of a Track.

**Raises:** **IndexError** – If key *index* is out of range : *0<=index<*[`GetKeyCount()`](#c4d.CCurve.GetKeyCount).

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `CCurve.FlushKeys(self, bUndo=False, SynchronizeKeys=False)` <a id="c4d.CCurve.FlushKeys"></a>

Remove all keys from this curve.

**Parameters:**

- **bUndo** (*bool*) –

  *New in version R18.020.*

  If **True** this action will be undoable.

  > **Note:** The caller has to to manage start/end of undo actions with `BaseDocument.StartUndo()`/`EndUndo()`.

- **SynchronizeKeys** (*bool*) –

  *New in version R18.020.*

  If **True** the routine is called on other components of the vector (if valid). Curve must be part of a Track.

#### `CCurve.InsertKey(self, ckey, bUndo=False, SynchronizeKeys=False)` <a id="c4d.CCurve.InsertKey"></a>

Insert a key into this curve.

**Parameters:**

- **ckey** ([*c4d.CKey*](../../../CKey/index.md#c4d.CKey)) – The key to insert.

- **bUndo** (*bool*) –

  *New in version R18.020.*

  If **True** this action will be undoable.

  > **Note:** The caller has to to manage start/end of undo actions with `BaseDocument.StartUndo()`/`EndUndo()`.

- **SynchronizeKeys** (*bool*) –

  *New in version R18.020.*

  If **True** the routine is called on other components of the vector (if valid). Curve must be part of a Track.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `CCurve.MoveKey(self, time, idx, seq=None, bUndo=False, SynchronizeKeys=False)` <a id="c4d.CCurve.MoveKey"></a>

Move a key in the curve.

**Parameters:**

- **time** ([*c4d.BaseTime*](../../../../BaseTime/index.md#c4d.BaseTime)) – The new time.

- **idx** (*int*) – The index of the key to move.

- **seq** (*Optional*[[*c4d.CCurve*](#c4d.CCurve)]) – Optional destination curve.

- **bUndo** (*bool*) –

  *New in version R18.020.*

  If **True** this action will be undoable.

  > **Note:** The caller has to to manage start/end of undo actions with `BaseDocument.StartUndo()`/`EndUndo()`.

- **SynchronizeKeys** (*bool*) –

  *New in version R18.020.*

  If **True** the routine is called on other components of the vector (if valid). Curve must be part of a Track.

**Raises:** **IndexError** – If key *idx* is out of range : *0<=idx<*[`GetKeyCount()`](#c4d.CCurve.GetKeyCount).

**Return type:** int

**Returns:** The new index.

#### `CCurve.SortKeysByTime(self)` <a id="c4d.CCurve.SortKeysByTime"></a>

Private. Should not be used.

### Key Navigation <a id="c4d.CCurve-method-Key-Navigation"></a>

#### `CCurve.FindNextUnmuted(self, index)` <a id="c4d.CCurve.FindNextUnmuted"></a>

Returns the next unmuted key. The key index passed as argument is included in the test.

*New in version R19.*

**Parameters:** **index** (*int*) – The key index to start (included) the search from: *0* <= *idx* < [`GetKeyCount()`](#c4d.CCurve.GetKeyCount)

**Return type:** Optional[Tuple[[c4d.CKey](../../../CKey/index.md#c4d.CKey), int]]

**Returns:** The first unmuted key and its index founded in the next direction, or **None** if there is no next unmuted key.

#### `CCurve.FindPrevUnmuted(self, index)` <a id="c4d.CCurve.FindPrevUnmuted"></a>

Returns the previous unmuted key. The key index passed as argument is included in the test.

*New in version R19.*

**Parameters:** **index** (*int*) – The key index to start (included) the search from: *0* <= *idx* < [`GetKeyCount()`](#c4d.CCurve.GetKeyCount)

**Return type:** Optional[Tuple[[c4d.CKey](../../../CKey/index.md#c4d.CKey), int]]

**Returns:** The first unmuted key and its index founded in the previous direction, or **None** if there is no previous unmuted key.

### Maintenance And Configuration <a id="c4d.CCurve-method-Maintenance-And-Configuration"></a>

#### `CCurve.GetTrack(self)` <a id="c4d.CCurve.GetTrack"></a>

Get the track of this curve.

**Return type:** [c4d.CTrack](../CTrack/index.md#c4d.CTrack)

**Returns:** The track of this curve.

#### `CCurve.SetKeyDefault(self, doc, kidx)` <a id="c4d.CCurve.SetKeyDefault"></a>

Set the defaults for key *kidx* for the curve.

> **Note:**
>
> This includes lock, mute, clamp, break, auto properties, interpolation and tangents.  
> This way you can set up a value and complete the missing properties with the defaults.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The curve’s document.
- **kidx** (*int*) – The key index.

#### `CCurve.SetKeyDirty(self)` <a id="c4d.CCurve.SetKeyDirty"></a>

Set keys to dirty. Equivalent to *SetDirty(c4d.DIRTYFLAGS_CHILDREN)*.

### Tangent Processing <a id="c4d.CCurve-method-Tangent-Processing"></a>

#### `CCurve.AdjustTangentAutoWeight(self, keyIndex)` <a id="c4d.CCurve.AdjustTangentAutoWeight"></a>

Adjusts Tangent Time and Value to reflect an auto-tangent (slope is preserved).  
Consider if broken tangent is active for weighted auto-tangent

*New in version 24.*

**Parameters:** **keyIndex** (*int*) – The key index: 0 <= *keyIndex* < `CCurve.GetKeyCount()`

#### `CCurve.AdjustTangentLength(self, keyTime1, keyTime2, tan1_val, tan2_val, tan1Time, tan2Time, applyHermiteFactor)` <a id="c4d.CCurve.AdjustTangentLength"></a>

Adjusts Tangent Length to avoid curve intersection

*New in version 24.*

> **Note:** The value of *tan1_val*, *tan2_val*, *tan1Time* and *tan2Time* are modified to the newly adjusted length.

**Parameters:**

- **keyTime1** (*float*) – First key Time value.
- **keyTime2** (*float*) – Second key Time value.
- **tan1_val** (*float*) – First key right tangent value.
- **tan2_val** (*float*) – Second key left tangent value.
- **tan1Time** (*float*) – First key right tangent time.
- **tan2Time** (*float*) – Second key left tangent time.
- **applyHermiteFactor** (*bool*) – Apply the Hermite factor to tangent.

#### `CCurve.GetTangents(self, kidx)` <a id="c4d.CCurve.GetTangents"></a>

Computes the tangents of a key, taking into account all options like zero slope, link slope etc.

**Parameters:** **kidx** (*int*) – The key index. 0 <= kidx < `CCurve.GetKeyCount()`.

**Return type:** Tuple[float, float, float, float]

**Returns:**

A tuple in the following order:

- The left value.
- The right value.
- The left time.
- The right time.

**Raises:** **OutOfRange** – if kidx < 0 or kidx > `CCurve.GetKeyCount()`.
