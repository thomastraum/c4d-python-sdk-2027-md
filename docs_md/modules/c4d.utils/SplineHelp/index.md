<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.utils/SplineHelp/index.html -->

# c4d.utils.SplineHelp <a id="c4d-utils-splinehelp"></a>

## *class* `c4d.utils.SplineHelp` <a id="c4d.utils.SplineHelp"></a>

## Overview <a id="overview"></a>

**Cache And Output**

- [`SplineHelp.GetCacheObject()`](#c4d.utils.SplineHelp.GetCacheObject): Gets the cache SplineObject.
- [`SplineHelp.GetDirty()`](#c4d.utils.SplineHelp.GetDirty): Gets the dirty value for the [`SplineHelp`](#c4d.utils.SplineHelp) which indicates how often the help has been updated with new values.
- [`SplineHelp.GetLineObject()`](#c4d.utils.SplineHelp.GetLineObject): Gets a [`LineObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/LineObject/index.md#c4d.LineObject) from SplineHelp functions.

**Deprecated**

- [`SplineHelp.GetPos()`](#c4d.utils.SplineHelp.GetPos): Use `SplineHelp.GetPosition()`.
- [`SplineHelp.InitSpline()`](#c4d.utils.SplineHelp.InitSpline): Initializes the [`SplineHelp`](#c4d.utils.SplineHelp). Must be called before any other function.

**Frames And Orientation**

- [`SplineHelp.GetCrossNormal()`](#c4d.utils.SplineHelp.GetCrossNormal): Gets a cross normal vector (i.e.
- [`SplineHelp.GetMatrix()`](#c4d.utils.SplineHelp.GetMatrix): Retrieve a full matrix for any point along the spline, constructed as a local coordinate system at that point.
- [`SplineHelp.GetNormal()`](#c4d.utils.SplineHelp.GetNormal): Gets a normal vector for any point along the spline.
- [`SplineHelp.GetPointMatrix()`](#c4d.utils.SplineHelp.GetPointMatrix): Gets the matrix for a spline vertex.
- [`SplineHelp.GetTangent()`](#c4d.utils.SplineHelp.GetTangent): Gets a tangent vector for any point along the spline.
- [`SplineHelp.GetVertexMatrix()`](#c4d.utils.SplineHelp.GetVertexMatrix): Retrieves a full matrix for a specific point of the line.

**Length Measurement**

- [`SplineHelp.GetSegmentLength()`](#c4d.utils.SplineHelp.GetSegmentLength): Returns a specific segment’s realworld unit length.
- [`SplineHelp.GetSplineLength()`](#c4d.utils.SplineHelp.GetSplineLength): Returns the spline’s realworld unit length including all segments.

**Lifecycle And State**

- [`SplineHelp.Exists()`](#c4d.utils.SplineHelp.Exists): Useful check to see if the spline helper contains data and has been inited.
- [`SplineHelp.FreeSpline()`](#c4d.utils.SplineHelp.FreeSpline): Called to free the spline data.

**Magic Methods**

- [`SplineHelp.__init__()`](#c4d.utils.SplineHelp.__init__)

**Offset And Point Sampling**

- [`SplineHelp.GetOffsetFromReal()`](#c4d.utils.SplineHelp.GetOffsetFromReal): Convert a percentage offset into a natural offset.
- [`SplineHelp.GetOffsetFromUnit()`](#c4d.utils.SplineHelp.GetOffsetFromUnit): Retrieve an offset from a realworld unit.
- [`SplineHelp.GetPointIndex()`](#c4d.utils.SplineHelp.GetPointIndex): Retrieves the nearest line point index to the given real *offset*.
- [`SplineHelp.GetPointValue()`](#c4d.utils.SplineHelp.GetPointValue): Converts a natural offset value to a real percentage offset value.
- [`SplineHelp.GetPosition()`](#c4d.utils.SplineHelp.GetPosition): Retrieves the nearest line point index to the given real *offset*.

**Rail Distances**

- [`SplineHelp.GetSize()`](#c4d.utils.SplineHelp.GetSize): Get the distance to an existing rail spline for any point along the spline.
- [`SplineHelp.GetVertexSize()`](#c4d.utils.SplineHelp.GetVertexSize): Get the distance to an existing rail spline for a spline vertex specified by *index*.

**Spline Initialization**

- [`SplineHelp.InitSplineWith()`](#c4d.utils.SplineHelp.InitSplineWith): Initializes the [`SplineHelp`](#c4d.utils.SplineHelp) with the passed spline *op*.
- [`SplineHelp.InitSplineWithRail()`](#c4d.utils.SplineHelp.InitSplineWithRail): Initializes the [`SplineHelp`](#c4d.utils.SplineHelp) with the passed spline *op* and *rail*.
- [`SplineHelp.InitSplineWithUpVector()`](#c4d.utils.SplineHelp.InitSplineWithUpVector): Initializes the [`SplineHelp`](#c4d.utils.SplineHelp) with the passed spline *op* and *upvector*.

**Spline Structure**

- [`SplineHelp.GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount): Gets the number of segments in the spline.
- [`SplineHelp.GetVertexCount()`](#c4d.utils.SplineHelp.GetVertexCount): Get the number of vertices for a spline segment.
- [`SplineHelp.SplineToLineIndex()`](#c4d.utils.SplineHelp.SplineToLineIndex): Converts a spline vertex index to its corresponding line object vertex index.

## Members <a id="members"></a>

### Cache And Output <a id="c4d.utils.SplineHelp-method-Cache-And-Output"></a>

#### `SplineHelp.GetCacheObject(self)` <a id="c4d.utils.SplineHelp.GetCacheObject"></a>

Gets the cache SplineObject.  
Useful if you need to access the point array from outside the helper while avoiding duplicating the cache and deform fetch code duplication.

*New in version S22.*

> **Note:** Initializes the [`SplineHelp`](#c4d.utils.SplineHelp) with `SplineHelp.InitSpline()`.

**Returns:** The cache object or **None** if it fails or if the SplineHelp was not initialized.

**Return type:** Optional[[c4d.BaseList2D](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

#### `SplineHelp.GetDirty(self)` <a id="c4d.utils.SplineHelp.GetDirty"></a>

Gets the dirty value for the [`SplineHelp`](#c4d.utils.SplineHelp) which indicates how often the help has been updated with new values. i.e. how often the source spline has changed, and or the spline has been cleared.

*New in version R17.048.*

**Return type:** int

**Returns:** The dirty checksum.

#### `SplineHelp.GetLineObject(self)` <a id="c4d.utils.SplineHelp.GetLineObject"></a>

Gets a [`LineObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/LineObject/index.md#c4d.LineObject) from SplineHelp functions.

*New in version R17.048.*

> **Note:** Initializes the [`SplineHelp`](#c4d.utils.SplineHelp) with **SPLINEHELPFLAGS_RETAINLINEOBJECT** for this method to return a line object.

**Return type:** Optional[[c4d.LineObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/LineObject/index.md#c4d.LineObject)]

**Returns:** The line object. **None** if it fails or if the [`SplineHelp`](#c4d.utils.SplineHelp) was not initialized with **SPLINEHELPFLAGS_RETAINLINEOBJECT**

### Deprecated <a id="c4d.utils.SplineHelp-method-Deprecated"></a>

#### `SplineHelp.GetPos(self, offset, segment=0, smooth=True, realoffset=False)` <a id="c4d.utils.SplineHelp.GetPos"></a>

*Deprecated since version R15:* Use `SplineHelp.GetPosition()`.

**Parameters:**

- **offset** (*float*) – The offset given in spline space.
- **segment** (*int*) – The segment index.
- **smooth** (*bool*) – Smoothed position.
- **realoffset** (*bool*) – **True** to use uniform spline distribution.

**Raises:** **IndexError** – If *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount).

**Return type:** [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The position given by *offset* in global space.

#### `SplineHelp.InitSpline(self, op, upvector=<_custom_c4d.Vector object at 0x0000012EC7FAA8A0>, rail=None, target_rail=True, use_deformed_points=False, force_update=False, use_global_space=True)` <a id="c4d.utils.SplineHelp.InitSpline"></a>

Initializes the [`SplineHelp`](#c4d.utils.SplineHelp). Must be called before any other function.

*Deprecated since version R17.048:* Instead use the specialized **Init()** methods: [`InitSplineWith()`](#c4d.utils.SplineHelp.InitSplineWith), [`InitSplineWithUpVector()`](#c4d.utils.SplineHelp.InitSplineWithUpVector), [`InitSplineWithRail()`](#c4d.utils.SplineHelp.InitSplineWithRail)

**Parameters:**

- **op** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The spline object to use.
- **upvector** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – Optional upvector for the spline normals generation. This is only used at the start of splines/segments; this way it avoids gimbal lock if at all possible.
- **rail** (*Optional*[[*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – Optional rail spline object for the spline normals generation.
- **target_rail** (*bool*) – The optional rail spline is not only used as up-vector but also as target. This is used for instance in MoGraph’s Rail options (Cloner, Spline effector, Spline Wrap etc.).
- **use_deformed_points** (*bool*) – Use deformed point positions of the spline.
- **force_update** (*bool*) – The spline help class internally caches its own content. Thus it will be much faster if the same splines are used for initialization. However, a full initialization can be forced by setting this parameter to **True**.
- **use_global_space** (*bool*) – If **True** the resulting matrices are in global space rather than in the spline objects’ local space.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Frames And Orientation <a id="c4d.utils.SplineHelp-method-Frames-And-Orientation"></a>

#### `SplineHelp.GetCrossNormal(self, offset, segment=0, smooth=True, realoffset=False)` <a id="c4d.utils.SplineHelp.GetCrossNormal"></a>

Gets a cross normal vector (i.e. perpendicular to the normal and the tangent) for any point along the spline.

**Parameters:**

- **offset** (*float*) – The offset given in spline space.
- **segment** (*int*) – The segment index.
- **smooth** (*bool*) – Smoothed cross normal.
- **realoffset** (*bool*) – **True** to use uniform spline distribution.

**Raises:** **IndexError** – If *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount).

**Return type:** [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The cross normal given by *offset* in global space.

#### `SplineHelp.GetMatrix(self, offset, segment=0, smooth=True, realoffset=False)` <a id="c4d.utils.SplineHelp.GetMatrix"></a>

Retrieve a full matrix for any point along the spline, constructed as a local coordinate system at that point.  
Optionally use realworld percentage rather than spline natural space for the offset.

**Parameters:**

- **offset** (*float*) – The spline offset.
- **segment** (*int*) – Segment index.
- **smooth** (*bool*) – Smoothed position
- **realoffset** (*bool*) – **True** to use uniform spline distribution

**Raises:** **IndexError** – If *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount).

**Return type:** [c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** Coordinate system matrix at **offset**.

#### `SplineHelp.GetNormal(self, offset, segment=0, smooth=True, realoffset=False)` <a id="c4d.utils.SplineHelp.GetNormal"></a>

Gets a normal vector for any point along the spline.

**Parameters:**

- **offset** (*float*) – The offset given in spline space.
- **segment** (*int*) – The segment index.
- **smooth** (*bool*) – Smoothed normal.
- **realoffset** (*bool*) – **True** to use uniform spline distribution.

**Raises:** **IndexError** – If *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount).

**Return type:** [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The normal given by *offset* in global space.

#### `SplineHelp.GetPointMatrix(self, splineVertexIndex)` <a id="c4d.utils.SplineHelp.GetPointMatrix"></a>

Gets the matrix for a spline vertex.

*New in version R17.048.*

**Parameters:** **splineVertexIndex** (*int*) – The zero-based index of the spline vertex.

**Return type:** [c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The resulting matrix for the point along the spline.

#### `SplineHelp.GetTangent(self, offset, segment=0, smooth=True, realoffset=False)` <a id="c4d.utils.SplineHelp.GetTangent"></a>

Gets a tangent vector for any point along the spline.

**Parameters:**

- **offset** (*float*) – The offset given in spline space.
- **segment** (*int*) – The segment index.
- **smooth** (*bool*) – Smoothed tangent.
- **realoffset** (*bool*) – **True** to use uniform spline distribution.

**Raises:** **IndexError** – If *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount).

**Return type:** [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The tangent given by *offset* in global space.

#### `SplineHelp.GetVertexMatrix(self, index)` <a id="c4d.utils.SplineHelp.GetVertexMatrix"></a>

Retrieves a full matrix for a specific point of the line.

> **Note:** This is not the spline vertex, but instead the line object’s vertex. (Calculated with LOD=1.0.)

**Parameters:** **index** (*int*) – Line object’s vertex.

**Raises:** **IndexError** – If the point *index* is out of range : *0<=segment<*`PointObject.GetPointCount()`.

**Return type:** [c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** Coordinate system matrix at *index*.

### Length Measurement <a id="c4d.utils.SplineHelp-method-Length-Measurement"></a>

#### `SplineHelp.GetSegmentLength(self, segment)` <a id="c4d.utils.SplineHelp.GetSegmentLength"></a>

Returns a specific segment’s realworld unit length.

**Parameters:** **segment** (*int*) – The segment index.

**Raises:** **IndexError** – If *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount).

**Return type:** float

**Returns:** The length of the specified segment.

#### `SplineHelp.GetSplineLength(self)` <a id="c4d.utils.SplineHelp.GetSplineLength"></a>

Returns the spline’s realworld unit length including all segments.

**Return type:** float

**Returns:** Spline length.

### Lifecycle And State <a id="c4d.utils.SplineHelp-method-Lifecycle-And-State"></a>

#### `SplineHelp.Exists(self)` <a id="c4d.utils.SplineHelp.Exists"></a>

Useful check to see if the spline helper contains data and has been inited.

**Return type:** bool

**Returns:** **True** if the spline helper is ready to use.

#### `SplineHelp.FreeSpline(self)` <a id="c4d.utils.SplineHelp.FreeSpline"></a>

Called to free the spline data. Recalling [`InitSpline()`](#c4d.utils.SplineHelp.InitSpline) or calling **SplineHelp.__free__** will automatically call this.

### Magic Methods <a id="c4d.utils.SplineHelp-method-Magic-Methods"></a>

#### `SplineHelp.__init__(self)` <a id="c4d.utils.SplineHelp.__init__"></a>

### Offset And Point Sampling <a id="c4d.utils.SplineHelp-method-Offset-And-Point-Sampling"></a>

#### `SplineHelp.GetOffsetFromReal(self, offset, segment=0)` <a id="c4d.utils.SplineHelp.GetOffsetFromReal"></a>

Convert a percentage offset into a natural offset.  
Percentage offsets ignore spline interpolation etc. and are always x% along the spline.

**Parameters:**

- **offset** (*float*) – A percentage offset, *0<=offset<=1.0*.
- **segment** (*int*) – The segment index.

**Raises:** **IndexError** – If *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount).

**Return type:** float

**Returns:** The natural offset.

#### `SplineHelp.GetOffsetFromUnit(self, unitoffset, segment=0)` <a id="c4d.utils.SplineHelp.GetOffsetFromUnit"></a>

Retrieve an offset from a realworld unit.  
For example, if a spline is 50 units long, 25 would be 50% of the length, i.e. 0.5.

**Parameters:**

- **unitoffset** (*float*) – The real unit offset to convert.
- **segment** (*int*) – The segment index.

**Raises:** **IndexError** – If *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount).

**Return type:** float

**Returns:** The offset in spline space.

#### `SplineHelp.GetPointIndex(self, offset, segment)` <a id="c4d.utils.SplineHelp.GetPointIndex"></a>

Retrieves the nearest line point index to the given real *offset*.

**Parameters:**

- **offset** (*float*) – The offset given in spline space.
- **segment** (*int*) – The segment index.

**Raises:** **IndexError** – If *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount).

**Return type:** int

**Returns:** The nearest line object point index, rounded down.

#### `SplineHelp.GetPointValue(self, offset, segment)` <a id="c4d.utils.SplineHelp.GetPointValue"></a>

Converts a natural offset value to a real percentage offset value.

> **Note:**
>
> This percentage uses the real world units for its offset.  
> So regardless of how the spline’s points and interpolation is set, a gap of 2% on a 100m long spline will always be 2m whereas normally in spline natural space, a gap of 2% can vary a great deal depending on the spline’s interpolation etc.

**Parameters:**

- **offset** (*float*) – The offset given in spline space.
- **segment** (*int*) – The segment index.

**Raises:** **IndexError** – If *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount).

**Return type:** float

**Returns:** The realworld percentage offset.

#### `SplineHelp.GetPosition(self, offset, segment=0, smooth=True, realoffset=False)` <a id="c4d.utils.SplineHelp.GetPosition"></a>

Retrieves the nearest line point index to the given real *offset*.

**Parameters:**

- **offset** (*float*) – The offset given in spline space.
- **segment** (*int*) – The segment index.
- **smooth** (*bool*) – Smoothed position.
- **realoffset** (*bool*) – **True** to use uniform spline distribution.

**Raises:** **IndexError** – If *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount).

**Return type:** [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The position given by *offset* in global space.

### Rail Distances <a id="c4d.utils.SplineHelp-method-Rail-Distances"></a>

#### `SplineHelp.GetSize(self, offset, segment=0, smooth=True, realoffset=False)` <a id="c4d.utils.SplineHelp.GetSize"></a>

Get the distance to an existing rail spline for any point along the spline.

**Parameters:**

- **offset** (*float*) – The spline offset.
- **segment** (*int*) – The segment index.
- **smooth** (*bool*) – Smoothed position
- **realoffset** (*bool*) – **True** to use uniform spline distribution

**Raises:** **IndexError** – If *segment* index is out of range : *0<=segment<*[`GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount).

**Return type:** float

**Returns:** The distance given by **offset**.

#### `SplineHelp.GetVertexSize(self, index)` <a id="c4d.utils.SplineHelp.GetVertexSize"></a>

Get the distance to an existing rail spline for a spline vertex specified by *index*.

**Parameters:** **index** (*int*) – The vertex index.

**Raises:** **IndexError** – If the vertex *index* is out of range : must be *0<=segment<*[`GetVertexCount()`](#c4d.utils.SplineHelp.GetVertexCount).

**Return type:** int

**Returns:** The distance given by *index*.

### Spline Initialization <a id="c4d.utils.SplineHelp-method-Spline-Initialization"></a>

#### `SplineHelp.InitSplineWith(self, op, flags=10)` <a id="c4d.utils.SplineHelp.InitSplineWith"></a>

Initializes the [`SplineHelp`](#c4d.utils.SplineHelp) with the passed spline *op*.

*New in version R17.048.*

> **Warning:** Must be called before any other function.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The spline object to use.

- **flags** (*int*) –

  The optional flags used to control how the [`SplineHelp`](#c4d.utils.SplineHelp) is setup:

  |   |   |
  |---|---|
  | *SPLINEHELPFLAGS_NONE* | None. |
  | *SPLINEHELPFLAGS_USERDEFORMERS* | Use deformed splines. |
  | *SPLINEHELPFLAGS_GLOBALSPACE* | Generate results in global rather than spline local space. |
  | *SPLINEHELPFLAGS_TARGETRAIL* | Target the rail spline (if passed). |
  | *SPLINEHELPFLAGS_CONTINUECURVE* | Continue the curvature of an existing spline at the end points. |
  | *SPLINEHELPFLAGS_FORCEUPDATE* | Force [`SplineHelp`](#c4d.utils.SplineHelp) to recalculate regardless of spline dirtiness. |
  | *SPLINEHELPFLAGS_RETAINLINEOBJECT* | Retain a copy of the line object for user usage via `SplineHelp.GetLineObject()`. |

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SplineHelp.InitSplineWithRail(self, op, rail, flags=10)` <a id="c4d.utils.SplineHelp.InitSplineWithRail"></a>

Initializes the [`SplineHelp`](#c4d.utils.SplineHelp) with the passed spline *op* and *rail*.

*New in version R17.048.*

> **Warning:** Must be called before any other function.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The spline object to use.

- **rail** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The rail spline.

- **flags** (*int*) –

  The optional flags used to control how the [`SplineHelp`](#c4d.utils.SplineHelp) is setup:

  |   |   |
  |---|---|
  | *SPLINEHELPFLAGS_NONE* | None. |
  | *SPLINEHELPFLAGS_USERDEFORMERS* | Use deformed splines. |
  | *SPLINEHELPFLAGS_GLOBALSPACE* | Generate results in global rather than spline local space. |
  | *SPLINEHELPFLAGS_TARGETRAIL* | Target the rail spline (if passed). |
  | *SPLINEHELPFLAGS_CONTINUECURVE* | Continue the curvature of an existing spline at the end points. |
  | *SPLINEHELPFLAGS_FORCEUPDATE* | Force [`SplineHelp`](#c4d.utils.SplineHelp) to recalculate regardless of spline dirtiness. |
  | *SPLINEHELPFLAGS_RETAINLINEOBJECT* | Retain a copy of the line object for user usage via `SplineHelp.GetLineObject()`. |

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `SplineHelp.InitSplineWithUpVector(self, op, upvector, flags=10)` <a id="c4d.utils.SplineHelp.InitSplineWithUpVector"></a>

Initializes the [`SplineHelp`](#c4d.utils.SplineHelp) with the passed spline *op* and *upvector*.

*New in version R17.048.*

> **Warning:** Must be called before any other function.

**Parameters:**

- **op** ([*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The spline object to use.

- **upvector** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The initial up-vector for the spline.

- **flags** (*int*) –

  The optional flags used to control how the [`SplineHelp`](#c4d.utils.SplineHelp) is setup:

  |   |   |
  |---|---|
  | *SPLINEHELPFLAGS_NONE* | None. |
  | *SPLINEHELPFLAGS_USERDEFORMERS* | Use deformed splines. |
  | *SPLINEHELPFLAGS_GLOBALSPACE* | Generate results in global rather than spline local space. |
  | *SPLINEHELPFLAGS_TARGETRAIL* | Target the rail spline (if passed). |
  | *SPLINEHELPFLAGS_CONTINUECURVE* | Continue the curvature of an existing spline at the end points. |
  | *SPLINEHELPFLAGS_FORCEUPDATE* | Force [`SplineHelp`](#c4d.utils.SplineHelp) to recalculate regardless of spline dirtiness. |
  | *SPLINEHELPFLAGS_RETAINLINEOBJECT* | Retain a copy of the line object for user usage via `SplineHelp.GetLineObject()`. |

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Spline Structure <a id="c4d.utils.SplineHelp-method-Spline-Structure"></a>

#### `SplineHelp.GetSegmentCount(self)` <a id="c4d.utils.SplineHelp.GetSegmentCount"></a>

Gets the number of segments in the spline.

> **Note:** Unlike the way Cinema 4D handles segments where a segmenet count of 0 means there’s either no segments or 1 segment, this returns 1 segment if there is 1 and 0 if there are 0.

**Return type:** int

**Returns:** Segment count.

#### `SplineHelp.GetVertexCount(self, segment)` <a id="c4d.utils.SplineHelp.GetVertexCount"></a>

Get the number of vertices for a spline segment.

**Parameters:** **segment** (*int*) – The segment index.

**Raises:** **IndexError** – If the *segment* index is out of range : must be *0<=segment<*[`GetSegmentCount()`](#c4d.utils.SplineHelp.GetSegmentCount).

**Return type:** int

**Returns:** The number of vertices.

#### `SplineHelp.SplineToLineIndex(self, index)` <a id="c4d.utils.SplineHelp.SplineToLineIndex"></a>

Converts a spline vertex index to its corresponding line object vertex index.

**Parameters:** **index** (*int*) – The spline vertex index.

**Return type:** int

**Returns:** The line object vertex index.
