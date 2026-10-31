<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.utils/ConvexHullDecomposition/index.html -->

# c4d.utils.ConvexHullDecomposition <a id="c4d-utils-convexhulldecomposition"></a>

## *class* `c4d.utils.ConvexHullDecomposition` <a id="c4d.utils.ConvexHullDecomposition"></a>

Efficient way to generate a low polygon representation of a given object.

*New in version 2026.0.0.*

## Overview <a id="overview"></a>

**Decomposition Workflow**

- [`ConvexHullDecomposition.Clear()`](#c4d.utils.ConvexHullDecomposition.Clear): Clear the stored result of the previous computation if there is any.
- [`ConvexHullDecomposition.Compute()`](#c4d.utils.ConvexHullDecomposition.Compute): Compute convex decomposition.
- [`ConvexHullDecomposition.FetchResults()`](#c4d.utils.ConvexHullDecomposition.FetchResults): Fetch results of the decomposition.

**Magic Methods**

- [`ConvexHullDecomposition.__init__()`](#c4d.utils.ConvexHullDecomposition.__init__): Initialize the convex decomposition library.

## Members <a id="members"></a>

### Decomposition Workflow <a id="c4d.utils.ConvexHullDecomposition-method-Decomposition-Workflow"></a>

#### `ConvexHullDecomposition.Clear(self)` <a id="c4d.utils.ConvexHullDecomposition.Clear"></a>

Clear the stored result of the previous computation if there is any.

#### `ConvexHullDecomposition.Compute(self, geometry)` <a id="c4d.utils.ConvexHullDecomposition.Compute"></a>

Compute convex decomposition.

**Parameters:** **geometry** ([*c4d.PolygonObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject)) – Geometry object to decompose.

#### `ConvexHullDecomposition.FetchResults(self)` <a id="c4d.utils.ConvexHullDecomposition.FetchResults"></a>

Fetch results of the decomposition. To be called after Compute().

**Return type:** list[[c4d.PolygonObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject)]

**Returns:** A list of objects where each entry represents one of the convex hulls the original object was decomposed into.

### Magic Methods <a id="c4d.utils.ConvexHullDecomposition-method-Magic-Methods"></a>

#### `ConvexHullDecomposition.__init__(self, lod, maxVoxelCount=16000000, maxVerticesPerConvexHull=64, maxConvexHull=1024, threadCount=0)` <a id="c4d.utils.ConvexHullDecomposition.__init__"></a>

Initialize the convex decomposition library.

**Parameters:**

- **lod** (*float*) – Desired level of detail to retail in the decomposition. Allowed values are between 0 and 1. Recommended 0.5.
- **maxVoxelCount** (*int*) – Maximum number of voxels used to decompose the bounding box, if the implementation uses voxelization.
- **maxVerticesPerConvexHull** (*int*) – Maximum number of vertices for each output convex hull. For use with physx on the gpu: set lower or equal to 64
- **maxConvexHull** (*int*) – Maximum number of output convex hulls.
- **threadCount** (*int*) – Maximum number of thread to use for the computation, 0 means all threads.
