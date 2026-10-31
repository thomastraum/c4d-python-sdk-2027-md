<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/hair/HairGuides/index.html -->

# c4d.modules.hair.HairGuides <a id="c4d-modules-hair-hairguides"></a>

## *class* `c4d.modules.hair.HairGuides` <a id="c4d.modules.hair.HairGuides"></a>

Helper class for guides/hair.

## Overview <a id="overview"></a>

**Coordinate Conversion**

- [`HairGuides.GetMg()`](#c4d.modules.hair.HairGuides.GetMg): Gets the global matrix.
- [`HairGuides.SetMg()`](#c4d.modules.hair.HairGuides.SetMg): Sets the global matrix.
- [`HairGuides.ToLocal()`](#c4d.modules.hair.HairGuides.ToLocal): Changes all the points for the guides into a local coordinate system.
- [`HairGuides.ToWorld()`](#c4d.modules.hair.HairGuides.ToWorld): Changes all the points for the guides into the world coordinate system.

**Flags**

- [`HairGuides.GetFlags()`](#c4d.modules.hair.HairGuides.GetFlags): Gets the flags.
- [`HairGuides.SetFlags()`](#c4d.modules.hair.HairGuides.SetFlags): Sets the flags.

**Geometry Conversion**

- [`HairGuides.CreateSpline()`](#c4d.modules.hair.HairGuides.CreateSpline): Create splines from the guides.
- [`HairGuides.GetTangent()`](#c4d.modules.hair.HairGuides.GetTangent): Gets the tangent of *guide* at *segment* and *t*.

**Object And Copy Operations**

- [`HairGuides.CopyFrom()`](#c4d.modules.hair.HairGuides.CopyFrom): Copies the guide data from *src* to this instance.
- [`HairGuides.GetObject()`](#c4d.modules.hair.HairGuides.GetObject): Gets the corresponding hair object.

**Point Editing**

- [`HairGuides.GetPoints()`](#c4d.modules.hair.HairGuides.GetPoints): Gets a list of points for the guides.
- [`HairGuides.SetPoint()`](#c4d.modules.hair.HairGuides.SetPoint): Set the point *p* at index *id*.

**Root Placement**

- [`HairGuides.DisplaceRoots()`](#c4d.modules.hair.HairGuides.DisplaceRoots): Used when HNs have affected the guide roots.
- [`HairGuides.GetRootAxis()`](#c4d.modules.hair.HairGuides.GetRootAxis): Gets the root axis of guide index.
- [`HairGuides.GetRootUV()`](#c4d.modules.hair.HairGuides.GetRootUV): Gets the root UV at index.
- [`HairGuides.GetTransformMatrix()`](#c4d.modules.hair.HairGuides.GetTransformMatrix): Gets the transformation matrix list.
- [`HairGuides.UndisplaceRoots()`](#c4d.modules.hair.HairGuides.UndisplaceRoots): Inverse of `HairGuides.DisplaceRoots()`.

**Selection**

- [`HairGuides.ConvertSelection()`](#c4d.modules.hair.HairGuides.ConvertSelection): Converts the selection state.
- [`HairGuides.GetSelected()`](#c4d.modules.hair.HairGuides.GetSelected): Gets the selection state.
- [`HairGuides.SetSelected()`](#c4d.modules.hair.HairGuides.SetSelected): Sets the selection state.

**Structure**

- [`HairGuides.GetCount()`](#c4d.modules.hair.HairGuides.GetCount): Gets the number of guides.
- [`HairGuides.GetGuidePointCount()`](#c4d.modules.hair.HairGuides.GetGuidePointCount): Gets the number of points per segment.
- [`HairGuides.GetPointCount()`](#c4d.modules.hair.HairGuides.GetPointCount): Gets the number of points per guide.
- [`HairGuides.GetSegmentCount()`](#c4d.modules.hair.HairGuides.GetSegmentCount): Gets the number of segments per guide (number of points is one more than this).

## Members <a id="members"></a>

### Coordinate Conversion <a id="c4d.modules.hair.HairGuides-method-Coordinate-Conversion"></a>

#### `HairGuides.GetMg(self)` <a id="c4d.modules.hair.HairGuides.GetMg"></a>

Gets the global matrix.

**Return type:** [c4d.Matrix](../../../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** Global matrix.

#### `HairGuides.SetMg(self, mg)` <a id="c4d.modules.hair.HairGuides.SetMg"></a>

Sets the global matrix.

**Parameters:** **mg** ([*c4d.Matrix*](../../../c4d/Matrix/index.md#c4d.Matrix)) – New global matrix.

#### `HairGuides.ToLocal(self)` <a id="c4d.modules.hair.HairGuides.ToLocal"></a>

Changes all the points for the guides into a local coordinate system.

#### `HairGuides.ToWorld(self)` <a id="c4d.modules.hair.HairGuides.ToWorld"></a>

Changes all the points for the guides into the world coordinate system.

### Flags <a id="c4d.modules.hair.HairGuides-method-Flags"></a>

#### `HairGuides.GetFlags(self)` <a id="c4d.modules.hair.HairGuides.GetFlags"></a>

Gets the flags.

**Return type:** int

**Returns:**

Flags:

|   |   |
|---|---|
| *HAIR_GUIDE_FLAGS_LOCAL* | Chains are in local object space. |
| *HAIR_GUIDE_FLAGS_AS_GUIDES* | Special case guides. |
| *HAIR_GUIDE_FLAGS_INITIAL* | Chains are in their original initial space (like a stick texture tag). |
| *HAIR_GUIDE_FLAGS_HAIRS* | Created for hairs. |
| *HAIR_GUIDE_FLAGS_INITIALAXIS* | Initial space and root axis aligned. |

#### `HairGuides.SetFlags(self, flags)` <a id="c4d.modules.hair.HairGuides.SetFlags"></a>

Sets the flags.

**Parameters:**

**flags** (*int*) –

New flags:

|   |   |
|---|---|
| *HAIR_GUIDE_FLAGS_LOCAL* | Chains are in local object space. |
| *HAIR_GUIDE_FLAGS_AS_GUIDES* | Special case guides. |
| *HAIR_GUIDE_FLAGS_INITIAL* | Chains are in their original initial space (like a stick texture tag). |
| *HAIR_GUIDE_FLAGS_HAIRS* | Created for hairs. |
| *HAIR_GUIDE_FLAGS_INITIALAXIS* | Initial space and root axis aligned. |

**Return type:** int

**Returns:** Old flags.

### Geometry Conversion <a id="c4d.modules.hair.HairGuides-method-Geometry-Conversion"></a>

#### `HairGuides.CreateSpline(self)` <a id="c4d.modules.hair.HairGuides.CreateSpline"></a>

Create splines from the guides.

**Return type:** [c4d.SplineObject](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/SplineObject/index.md#c4d.SplineObject)

**Returns:** Created splines.

#### `HairGuides.GetTangent(self, guide, segment, t)` <a id="c4d.modules.hair.HairGuides.GetTangent"></a>

Gets the tangent of *guide* at *segment* and *t*.

**Parameters:**

- **guide** (*int:*) – Guide index.
- **segment** (*int*) – Segment index.
- **t** (*float*) – T coordinate.

### Object And Copy Operations <a id="c4d.modules.hair.HairGuides-method-Object-And-Copy-Operations"></a>

#### `HairGuides.CopyFrom(self, src)` <a id="c4d.modules.hair.HairGuides.CopyFrom"></a>

Copies the guide data from *src* to this instance.

**Parameters:** **src** ([*c4d.BaseSelect*](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)) – Source.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `HairGuides.GetObject(self)` <a id="c4d.modules.hair.HairGuides.GetObject"></a>

Gets the corresponding hair object.

**Return type:** [c4d.modules.hair.HairObject](../HairObject/index.md#c4d.modules.hair.HairObject)

**Returns:** Hair object.

### Point Editing <a id="c4d.modules.hair.HairGuides-method-Point-Editing"></a>

#### `HairGuides.GetPoints(self)` <a id="c4d.modules.hair.HairGuides.GetPoints"></a>

Gets a list of points for the guides.

**Return type:** List[[c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)]

**Returns:** Point list.

#### `HairGuides.SetPoint(self, id, p)` <a id="c4d.modules.hair.HairGuides.SetPoint"></a>

Set the point *p* at index *id*.

**Parameters:**

- **id** (*int*) – The point index.
- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The point.

**Raises:** **IndexError** – If the point index *id* is out of range : *0<=id<*[`GetPointCount()`](#c4d.modules.hair.HairGuides.GetPointCount).

### Root Placement <a id="c4d.modules.hair.HairGuides-method-Root-Placement"></a>

#### `HairGuides.DisplaceRoots(self)` <a id="c4d.modules.hair.HairGuides.DisplaceRoots"></a>

Used when HNs have affected the guide roots.  
Call `HairGuides.DisplaceRoots()` and it will ensure they are in the correct displaced state for HNs, `HairGuides.UndisplaceRoots()` will make sure they are not.  
Generally not needed if using ToInitial(), as the initial state is undisplaced.

#### `HairGuides.GetRootAxis(self, index, bAlign=False, bLocal=True, bInitial=False, bZAxis=False)` <a id="c4d.modules.hair.HairGuides.GetRootAxis"></a>

Gets the root axis of guide index.

**Parameters:**

- **index** (*int*) – Guide index.
- **bAlign** (*bool*) – Aligned.
- **bLocal** (*bool*) – Local.
- **bInitial** (*bool*) – Initial
- **bLocal** – If **True** then the alignment is done along the Z axis, otherwise it is Y.

**Return type:** [c4d.Matrix](../../../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The root axis.

#### `HairGuides.GetRootUV(self, index)` <a id="c4d.modules.hair.HairGuides.GetRootUV"></a>

Gets the root UV at index.

**Parameters:** **index** (*int*) – Guide index.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

#### `HairGuides.GetTransformMatrix(self, index)` <a id="c4d.modules.hair.HairGuides.GetTransformMatrix"></a>

Gets the transformation matrix list.

**Parameters:** **index** (*int*) – Guide index.

**Return type:** List[[c4d.Matrix](../../../c4d/Matrix/index.md#c4d.Matrix)]

**Returns:** The transformation matrix list.

#### `HairGuides.UndisplaceRoots(self)` <a id="c4d.modules.hair.HairGuides.UndisplaceRoots"></a>

Inverse of `HairGuides.DisplaceRoots()`.

### Selection <a id="c4d.modules.hair.HairGuides-method-Selection"></a>

#### `HairGuides.ConvertSelection(self, from_mode, to_mode, from_select, to_select)` <a id="c4d.modules.hair.HairGuides.ConvertSelection"></a>

Converts the selection state.

**Parameters:**

- **from_mode** (*int*) –

  Selection mode:

  |   |   |
  |---|---|
  | *HAIR_MODE_LOCKED* | Locked mode |
  | *HAIR_MODE_HIDDEN* | Hidden mode. |
  | *HAIR_MODE_TIPS* | Tips mode. |
  | *HAIR_MODE_POINTS* | Points mode. |
  | *HAIR_MODE_GUIDES* | Guides mode. |
  | *HAIR_MODE_ROOTS* | Roots mode. |
  | *HAIR_MODE_VERTEX* | Vertex mode. |

- **to_mode** (*int*) –

  To mode.

  |   |   |
  |---|---|
  | *HAIR_MODE_LOCKED* | Locked mode |
  | *HAIR_MODE_HIDDEN* | Hidden mode. |
  | *HAIR_MODE_TIPS* | Tips mode. |
  | *HAIR_MODE_POINTS* | Points mode. |
  | *HAIR_MODE_GUIDES* | Guides mode. |
  | *HAIR_MODE_ROOTS* | Roots mode. |
  | *HAIR_MODE_VERTEX* | Vertex mode. |

- **from_select** ([*c4d.BaseSelect*](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)) – From selection.

- **to_select** ([*c4d.BaseSelect*](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)) – To selection.

#### `HairGuides.GetSelected(self, mode)` <a id="c4d.modules.hair.HairGuides.GetSelected"></a>

Gets the selection state.

**Parameters:**

**mode** (*int*) –

Selection mode:

|   |   |
|---|---|
| *HAIR_MODE_LOCKED* | Locked mode |
| *HAIR_MODE_HIDDEN* | Hidden mode. |
| *HAIR_MODE_TIPS* | Tips mode. |
| *HAIR_MODE_POINTS* | Points mode. |
| *HAIR_MODE_GUIDES* | Guides mode. |
| *HAIR_MODE_ROOTS* | Roots mode. |
| *HAIR_MODE_VERTEX* | Vertex mode. |

**Return type:** Optional[[c4d.BaseSelect](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)]

**Returns:** The selection or **None**.

#### `HairGuides.SetSelected(self, mode, select)` <a id="c4d.modules.hair.HairGuides.SetSelected"></a>

Sets the selection state.

**Parameters:**

- **mode** (*int*) –

  Selection mode:

  |   |   |
  |---|---|
  | *HAIR_MODE_LOCKED* | Locked mode |
  | *HAIR_MODE_HIDDEN* | Hidden mode. |
  | *HAIR_MODE_TIPS* | Tips mode. |
  | *HAIR_MODE_POINTS* | Points mode. |
  | *HAIR_MODE_GUIDES* | Guides mode. |
  | *HAIR_MODE_ROOTS* | Roots mode. |
  | *HAIR_MODE_VERTEX* | Vertex mode. |

- **select** ([*c4d.BaseSelect*](../../../c4d/BaseSelect/index.md#c4d.BaseSelect)) – The selection.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Structure <a id="c4d.modules.hair.HairGuides-method-Structure"></a>

#### `HairGuides.GetCount(self)` <a id="c4d.modules.hair.HairGuides.GetCount"></a>

Gets the number of guides.

**Return type:** int

**Returns:** Guide count.

#### `HairGuides.GetGuidePointCount(self)` <a id="c4d.modules.hair.HairGuides.GetGuidePointCount"></a>

Gets the number of points per segment.

**Return type:** int

**Returns:** Number of points per segment.

#### `HairGuides.GetPointCount(self)` <a id="c4d.modules.hair.HairGuides.GetPointCount"></a>

Gets the number of points per guide. (One more than segments.)

**Return type:** int

**Returns:** Number of points per guide.

#### `HairGuides.GetSegmentCount(self)` <a id="c4d.modules.hair.HairGuides.GetSegmentCount"></a>

Gets the number of segments per guide (number of points is one more than this).

**Return type:** int

**Returns:** Number of segments per guide.
