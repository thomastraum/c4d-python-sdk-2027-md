<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/CTrack/index.html -->

# c4d.CTrack <a id="c4d-ctrack"></a>

## *class* `c4d.CTrack` <a id="c4d.CTrack"></a>

This is the animation track base class. Contains [`CCurve`](../CCurve/index.md#c4d.CCurve) that contain [`CKeys`](../../../CKey/index.md#c4d.CKey).  
A [`BaseList2D`](../index.md#c4d.BaseList2D) can host a [`CTrack`](#c4d.CTrack) object.  
This can be the position, rotation or custom value track.  
These tracks contain a [`CCurve`](../CCurve/index.md#c4d.CCurve) which contains [`CKeys`](../../../CKey/index.md#c4d.CKey).

Parent Class:

- [`c4d.BaseList2D`](../index.md#c4d.BaseList2D)

## Overview <a id="overview"></a>

**Component Synchronization**

- [`CTrack.IsSynchronized()`](#c4d.CTrack.IsSynchronized): Checks if keys are synchronized with other Component tracks (Vector Track only).
- [`CTrack.SetSynchronized()`](#c4d.CTrack.SetSynchronized): Sets synchronization between component Track (Vector Track only).

**Curve Handling**

- [`CTrack.GetCurve()`](#c4d.CTrack.GetCurve): Get a curve of this track.
- [`CTrack.GetTrackCategory()`](#c4d.CTrack.GetTrackCategory): Get a curve of this track.

**Data Lifecycle**

- [`CTrack.FillKey()`](#c4d.CTrack.FillKey): Fills *key* with default values.
- [`CTrack.FlushData()`](#c4d.CTrack.FlushData): Clears the data of the track itself, for example removes time curves, pre/post loop type, etc.

**Description Metadata**

- [`CTrack.GetDescriptionID()`](#c4d.CTrack.GetDescriptionID): Retrieve the description ID of this track.
- [`CTrack.SetDescriptionID()`](#c4d.CTrack.SetDescriptionID): Set the description ID of this track.

**Display Dimensions**

- [`CTrack.GetHeight()`](#c4d.CTrack.GetHeight): Get the height of the track.
- [`CTrack.GetTLHeight()`](#c4d.CTrack.GetTLHeight): Get the height of the mini f-curves in the timeline.
- [`CTrack.GetUnit()`](#c4d.CTrack.GetUnit): Get the unit and step of the track.
- [`CTrack.SetTLHeight()`](#c4d.CTrack.SetTLHeight): Get the height of the track.

**Display Rendering**

- [`CTrack.Draw()`](#c4d.CTrack.Draw): Draws the track into a clip map bitmap, if drawing is supported.

**Evaluation Settings**

- [`CTrack.GetEvaluationMode()`](#c4d.CTrack.GetEvaluationMode): Gets evaluation mode.
- [`CTrack.SetEvaluationMode()`](#c4d.CTrack.SetEvaluationMode): Sets evaluation mode.

**Loop Behavior**

- [`CTrack.GetAfter()`](#c4d.CTrack.GetAfter): Get the pre track loop type of this track.
- [`CTrack.GetBefore()`](#c4d.CTrack.GetBefore): Get the pre track loop type of this track.
- [`CTrack.SetAfter()`](#c4d.CTrack.SetAfter): Set the post track loop type of this track.
- [`CTrack.SetBefore()`](#c4d.CTrack.SetBefore): Set the pre track loop type of this track.

**Magic Methods**

- [`CTrack.__init__()`](#c4d.CTrack.__init__): Allocates a track object.

**Track Information**

- [`CTrack.GetTrackInformation()`](#c4d.CTrack.GetTrackInformation): Returns the track information at the current time in *doc*, or at *key* if specified.
- [`CTrack.SetTrackInformation()`](#c4d.CTrack.SetTrackInformation): Sets the track information at the current time in *doc*, or at *key* if specified.

**Track Relationships**

- [`CTrack.GetObject()`](#c4d.CTrack.GetObject): Get the host object of this track.
- [`CTrack.GetTimeTrack()`](#c4d.CTrack.GetTimeTrack): Returns the time track.
- [`CTrack.SetTimeTrack()`](#c4d.CTrack.SetTimeTrack): Sets the time track.

**Value Evaluation**

- [`CTrack.GetValue()`](#c4d.CTrack.GetValue): Retrieve the value of this track at *time*.
- [`CTrack.Remap()`](#c4d.CTrack.Remap): Remaps *time*.

## Members <a id="members"></a>

### Component Synchronization <a id="c4d.CTrack-method-Component-Synchronization"></a>

#### `CTrack.IsSynchronized(self)` <a id="c4d.CTrack.IsSynchronized"></a>

Checks if keys are synchronized with other Component tracks (Vector Track only).

*New in version R18.020.*

**Return type:** bool

**Returns:** **True** if track is synchronized, otherwise **False**.

#### `CTrack.SetSynchronized(self, synch)` <a id="c4d.CTrack.SetSynchronized"></a>

Sets synchronization between component Track (Vector Track only).

*New in version R18.020.*

**Parameters:** **synch** (*bool*) – **True** if Track needs to be synchronized, otherwise **False**.

### Curve Handling <a id="c4d.CTrack-method-Curve-Handling"></a>

#### `CTrack.GetCurve(self, type=1, bCreate=True)` <a id="c4d.CTrack.GetCurve"></a>

Get a curve of this track.

**Parameters:**

- **type** ([*c4d.BaseList2D*](../index.md#c4d.BaseList2D)) –

  The curve type:

  |   |   |
  |---|---|
  | *CCURVE_CURVE* | Standard curve. |
  | *CCURVE_HLE_BASE* | Internal reduced modification reference curve. |
  | *CCURVE_HLE_CURVE* | Reduced Modification Curve - Curve. |
  | *CCURVE_SS_CURVE* | Snapshot 1. |
  | *CCURVE_SS_CURVE2* | Snapshot 2. |
  | *CCURVE_SS_CURVE3* | Snapshot 3. |
  | *CCURVE_SS_CURVE4* | Snapshot 4. |
  | *CCURVE_SS_CURVE5* | Snapshot 5. |
  | *CCURVE_HLE_SCALE* | Reduced modification curve - scale. |
  | *CCURVE_HLE_MOVE* | Reduced modification curve - move. |

- **bCreate** (*bool*) – If True a curve is created if none exists.

**Return type:** [c4d.CCurve](../CCurve/index.md#c4d.CCurve)

**Returns:** The curve of this track.

#### `CTrack.GetTrackCategory(self)` <a id="c4d.CTrack.GetTrackCategory"></a>

Get a curve of this track.

**Return type:** int

**Returns:**

Track category:

|   |   |
|---|---|
| *CTRACK_CATEGORY_VALUE* | Value track. |
| *CTRACK_CATEGORY_DATA* | Data track. |
| *CTRACK_CATEGORY_PLUGIN* | Plugin track. |

### Data Lifecycle <a id="c4d.CTrack-method-Data-Lifecycle"></a>

#### `CTrack.FillKey(self, doc, bl, key)` <a id="c4d.CTrack.FillKey"></a>

Fills *key* with default values.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.
- **bl** ([*c4d.BaseList2D*](../index.md#c4d.BaseList2D)) – The object of the key to fill.
- **key** ([*c4d.CKey*](../../../CKey/index.md#c4d.CKey)) – The key to fill.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `CTrack.FlushData(self)` <a id="c4d.CTrack.FlushData"></a>

Clears the data of the track itself, for example removes time curves, pre/post loop type, etc.

### Description Metadata <a id="c4d.CTrack-method-Description-Metadata"></a>

#### `CTrack.GetDescriptionID(self)` <a id="c4d.CTrack.GetDescriptionID"></a>

Retrieve the description ID of this track.

**Return type:** [c4d.DescID](../../../../DescID/index.md#c4d.DescID)

**Returns:** The description ID.

#### `CTrack.SetDescriptionID(self, object, id)` <a id="c4d.CTrack.SetDescriptionID"></a>

Set the description ID of this track.

**Parameters:**

- **object** ([*c4d.BaseList2D*](../index.md#c4d.BaseList2D)) – Object for the new description ID.
- **id** ([*c4d.DescID*](../../../../DescID/index.md#c4d.DescID)) – New description ID.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Display Dimensions <a id="c4d.CTrack-method-Display-Dimensions"></a>

#### `CTrack.GetHeight(self)` <a id="c4d.CTrack.GetHeight"></a>

Get the height of the track.

**Return type:** int

**Returns:** The height in pixels.

#### `CTrack.GetTLHeight(self, id)` <a id="c4d.CTrack.GetTLHeight"></a>

Get the height of the mini f-curves in the timeline.

**Parameters:** **id** (*int*) – 0-3 for one of the four timelines.

**Return type:** int

**Returns:** The height of the mini f-curve in pixels.

#### `CTrack.GetUnit(self)` <a id="c4d.CTrack.GetUnit"></a>

Get the unit and step of the track.

**Return type:** Tuple[int, float]

**Returns:**

The unit and the step. The units:

|   |   |
|---|---|
| *UNIT_NONE* | No units. |
| *UNIT_KM* | Kilometer. |
| *UNIT_M* | Meter. |
| *UNIT_CM* | Centimeter. |
| *UNIT_MM* | Millimeter. |
| *UNIT_UM* | Micrometer. |
| *UNIT_NM* | Nanometer. |
| *UNIT_MILE* | Mile. |
| *UNIT_YARD* | Yard. |
| *UNIT_FEET* | Feet. |
| *UNIT_INCH* | Inch. |

#### `CTrack.SetTLHeight(self, id, size)` <a id="c4d.CTrack.SetTLHeight"></a>

Get the height of the track.

**Parameters:**

- **id** (*int*) – 0-3 for one of the four timelines.
- **size** (*int*) – The new size of the mini f-curve in pixels.

### Display Rendering <a id="c4d.CTrack-method-Display-Rendering"></a>

#### `CTrack.Draw(self, map, clip_left, clip_right)` <a id="c4d.CTrack.Draw"></a>

Draws the track into a clip map bitmap, if drawing is supported.

*New in version R19.*

**Parameters:**

- **map** ([*c4d.bitmaps.GeClipMap*](../../../../../c4d.bitmaps/GeClipMap/index.md#c4d.bitmaps.GeClipMap)) – The clip map to draw into.
- **clip_left** ([*c4d.BaseTime*](../../../../BaseTime/index.md#c4d.BaseTime)) – The left time clipping.
- **clip_right** ([*c4d.BaseTime*](../../../../BaseTime/index.md#c4d.BaseTime)) – The right time clipping.

**Return type:** bool

**Returns:** **True** if the track was drawn, otherwise **False**.

### Evaluation Settings <a id="c4d.CTrack-method-Evaluation-Settings"></a>

#### `CTrack.GetEvaluationMode(self)` <a id="c4d.CTrack.GetEvaluationMode"></a>

Gets evaluation mode.

*New in version 24.*

**Returns:**

Interpolation mode.

| Symbol ID | Description |
|---|---|
| R23 | Hermite evaluation with some tangent issues. |
| CURRENT | Spline evaluation. |

**Return type:** int

#### `CTrack.SetEvaluationMode(self, mode)` <a id="c4d.CTrack.SetEvaluationMode"></a>

Sets evaluation mode.

*New in version 24.*

**Parameters:**

**mode** (*int*) –

Interpolation mode.

| Symbol ID | Description |
|---|---|
| R23 | Hermite evaluation with some tangent issues. |
| CURRENT | Spline evaluation. |

### Loop Behavior <a id="c4d.CTrack-method-Loop-Behavior"></a>

#### `CTrack.GetAfter(self)` <a id="c4d.CTrack.GetAfter"></a>

Get the pre track loop type of this track.

**Return type:** int

**Returns:**

Loop type:

|   |   |
|---|---|
| *CLOOP_OFF* | No loop. |
| *CLOOP_CONSTANT* | Constant. |
| *CLOOP_CONTINUE* | Continue. |
| *CLOOP_REPEAT* | Repeat. |
| *CLOOP_OFFSETREPEAT* | Offset repeat. |
| *CLOOP_OSCILLATE* | Oscillate. |
| *CLOOP_LOOP* | *New in version R24:* Loop. |

#### `CTrack.GetBefore(self)` <a id="c4d.CTrack.GetBefore"></a>

Get the pre track loop type of this track.

**Return type:** int

**Returns:**

Loop type:

|   |   |
|---|---|
| *CLOOP_OFF* | No loop. |
| *CLOOP_CONSTANT* | Constant. |
| *CLOOP_CONTINUE* | Continue. |
| *CLOOP_REPEAT* | Repeat. |
| *CLOOP_OFFSETREPEAT* | Offset repeat. |
| *CLOOP_OSCILLATE* | Oscillate. |
| *CLOOP_LOOP* | *New in version R24:* Loop. |

#### `CTrack.SetAfter(self, type)` <a id="c4d.CTrack.SetAfter"></a>

Set the post track loop type of this track.

**Parameters:**

**type** (*int*) –

Loop type:

|   |   |
|---|---|
| *CLOOP_OFF* | No loop. |
| *CLOOP_CONSTANT* | Constant. |
| *CLOOP_CONTINUE* | Continue. |
| *CLOOP_REPEAT* | Repeat. |
| *CLOOP_OFFSETREPEAT* | Offset repeat. |
| *CLOOP_OSCILLATE* | Oscillate. |
| *CLOOP_LOOP* | *New in version R24:* Loop. |

#### `CTrack.SetBefore(self, type)` <a id="c4d.CTrack.SetBefore"></a>

Set the pre track loop type of this track.

**Parameters:**

**type** (*int*) –

Loop type:

|   |   |
|---|---|
| *CLOOP_OFF* | No loop. |
| *CLOOP_CONSTANT* | Constant. |
| *CLOOP_CONTINUE* | Continue. |
| *CLOOP_REPEAT* | Repeat. |
| *CLOOP_OFFSETREPEAT* | Offset repeat. |
| *CLOOP_OSCILLATE* | Oscillate. |
| *CLOOP_LOOP* | *New in version R24:* Loop. |

### Magic Methods <a id="c4d.CTrack-method-Magic-Methods"></a>

#### `CTrack.__init__(self, bl, id)` <a id="c4d.CTrack.__init__"></a>

Allocates a track object.

**Parameters:**

- **bl** ([*c4d.BaseList2D*](../index.md#c4d.BaseList2D)) – Object to allocate the track for.
- **id** ([*c4d.DescID*](../../../../DescID/index.md#c4d.DescID)) – Description ID to allocate the track for.

For instance a position track will be allocated like this.

```python
descId = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION, c4d.DTYPE_VECTOR, 0),
                    c4d.DescLevel(c4d.VECTOR_X, c4d.DTYPE_REAL, 0))
track = c4d.CTrack(op, descId)
```

A track of type **int** will be allocated like this.

```python
descId = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_VISIBILITY_EDITOR, c4d.DTYPE_LONG, 0))
track = c4d.CTrack(op, descId)
```

For a plugin and special tracks you pass the ID.

```python
tr = c4d.CTrack(op, c4d.DescID(ID, ID, 0))
```

IDs for Cinema 4D’s special tracks are:

> |   |   |
> |---|---|
> | *CTpla* | PLA. |
> | *CT2d* | 2D Tracks. |
> | *CTdoodle* | Doodle. |
> | *CTmask* | mask. |
> | *CTsound* | Sound. |
> | *CTmorph* | Morph. |
> | *CTtime* | Time. |

### Track Information <a id="c4d.CTrack-method-Track-Information"></a>

#### `CTrack.GetTrackInformation(self, doc, key)` <a id="c4d.CTrack.GetTrackInformation"></a>

Returns the track information at the current time in *doc*, or at *key* if specified.

*New in version R19.*

> **Note:** The track information string is displayed in tooltips inside the Timeline for instance.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the operation.
- **key** (*Optional*[[*c4d.CKey*](../../../CKey/index.md#c4d.CKey)]) – Pass a key to retrieve the track information at, otherwise **None** to retrieve it at the current time.

**Return type:** str

**Returns:** The information string.

#### `CTrack.SetTrackInformation(self, doc, key, info)` <a id="c4d.CTrack.SetTrackInformation"></a>

Sets the track information at the current time in *doc*, or at *key* if specified.

*New in version R19.*

> **Note:** The track information string is displayed in tooltips inside the Timeline for instance.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the operation.
- **key** (*Optional*[[*c4d.CKey*](../../../CKey/index.md#c4d.CKey)]) – Pass a key to set the track information at, otherwise **None** to set it at the current time.
- **info** (*str*) – The information string to set.

**Return type:** bool

**Returns:** **True** if the track information was set, otherwise **False**.

### Track Relationships <a id="c4d.CTrack-method-Track-Relationships"></a>

#### `CTrack.GetObject(self)` <a id="c4d.CTrack.GetObject"></a>

Get the host object of this track.

**Return type:** Optional[[c4d.BaseList2D](../index.md#c4d.BaseList2D)]

**Returns:** The host object or **None**.

#### `CTrack.GetTimeTrack(self, doc)` <a id="c4d.CTrack.GetTimeTrack"></a>

Returns the time track.

*New in version R19.*

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document for the operation.

**Return type:** [c4d.CTrack](#c4d.CTrack)

**Returns:** The time track.

#### `CTrack.SetTimeTrack(self, track)` <a id="c4d.CTrack.SetTimeTrack"></a>

Sets the time track.

*New in version R19.*

**Parameters:** **track** ([*c4d.CTrack*](#c4d.CTrack)) – The time track to set.

### Value Evaluation <a id="c4d.CTrack-method-Value-Evaluation"></a>

#### `CTrack.GetValue(self, doc, time, fps)` <a id="c4d.CTrack.GetValue"></a>

Retrieve the value of this track at *time*.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

- **time** ([*c4d.BaseTime*](../../../../BaseTime/index.md#c4d.BaseTime)) – The time.

- **fps** (*int*) –

  *Deprecated since version R17.048:* The number of frames per second.

**Return type:** float

**Returns:** The value.

#### `CTrack.Remap(self, time)` <a id="c4d.CTrack.Remap"></a>

Remaps *time*.

**Parameters:** **time** (*float*) – The input time.

**Return type:** Optional[Dict[‘ret_time’: float, ‘ret_cycle’ int]]

**Returns:** The output time and cycle, or **None** if *time* could not be remapped.
