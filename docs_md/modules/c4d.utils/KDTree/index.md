<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.utils/KDTree/index.html -->

# c4d.utils.KDTree <a id="c4d-utils-kdtree"></a>

## *class* `c4d.utils.KDTree` <a id="c4d.utils.KDTree"></a>

Provides an interface for efficient indexing and searching points in 2D or 3D space.

*New in version 2026.2.0.*

**Example:**

```python
import c4d

# Create a KDTree
kd_tree = c4d.utils.KDTree()

# Insert some points with custom IDs
kd_tree.Insert(c4d.Vector(0, 0, 0), 100)
kd_tree.Insert(c4d.Vector(1, 1, 1), 101)
kd_tree.Insert(c4d.Vector(2, 2, 2), 102)

# Append multiple points at once (indices will be 3, 4, 5, ...)
points = [c4d.Vector(x, x, x) for x in range(5, 10)]
kd_tree.Insert(points)

# Balance the tree (required after inserting points)
kd_tree.Balance()

# Create a query object for searching
query = kd_tree.CreateQueryObject()

# Find the nearest point
nearest_index = query.FindNearest(c4d.Vector(0.1, 0.1, 0.1))
print("Nearest point index:", nearest_index)
```

Advanced usage with detailed results:

```python
# Get detailed information about the nearest point
nearest_index, nearest_info = query.FindNearest(
    c4d.Vector(1.2, 1.2, 1.2), 
    return_nearest_info=True
)

if nearest_info:
    node = nearest_info['node']
    print("Nearest point:", node['point'])
    print("Point ID:", node['id'])
    print("Distance:", nearest_info['dist'])

# Find multiple nearest points within a radius
nearby_points = query.FindNearestMultiple(
    c4d.Vector(1.5, 1.5, 1.5),
    max_distance=2.0,
    max_elements=3,
    sort_results=True
)

for result in nearby_points:
    node = result['node']
    print(f"Point {node['point']} (ID: {node['id']}) at distance {result['dist']}")

# Find all points within a specific range
points_in_range = query.FindRange(
    c4d.Vector(0, 0, 0),
    max_distance=3.0,
    sort_results=True
)

print(f"Found {len(points_in_range)} points within range")
```

Performance considerations:

```python
# For better performance with large datasets
kd_tree = c4d.utils.KDTree()
kd_tree.SetSplitMode(2)  # Use SPLIT_BY_MAX_EXTENT for optimal splitting

# Insert large point arrays efficiently
large_point_array = [c4d.Vector(x, y, z) for x in range(100) for y in range(100) for z in range(10)]
kd_tree.Insert(large_point_array)
kd_tree.Balance()
```

## Overview <a id="overview"></a>

**Magic Methods**

- [`KDTree.__init__()`](#c4d.utils.KDTree.__init__): Instantiates a new KDTree object.

**Tree Management**

- [`KDTree.Balance()`](#c4d.utils.KDTree.Balance): Balances the KDTree to optimize query performance.
- [`KDTree.CreateQueryObject()`](#c4d.utils.KDTree.CreateQueryObject): Creates a query interface for performing spatial searches on the KDTree.
- [`KDTree.Insert()`](#c4d.utils.KDTree.Insert): Inserts one or more points into the KDTree.
- [`KDTree.SetSplitMode()`](#c4d.utils.KDTree.SetSplitMode): Sets the axis split mode used during tree balancing operations.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.utils.KDTree-method-Magic-Methods"></a>

#### `KDTree.__init__(self)` <a id="c4d.utils.KDTree.__init__"></a>

Instantiates a new KDTree object.

**Raises:** **RuntimeError** – If the KDTree could not be created due to memory limitations or system constraints.

### Tree Management <a id="c4d.utils.KDTree-method-Tree-Management"></a>

#### `KDTree.Balance(self)` <a id="c4d.utils.KDTree.Balance"></a>

Balances the KDTree to optimize query performance.

This method must be called after inserting points and before performing any spatial queries. Balancing reorganizes the internal tree structure for optimal search performance based on the current point distribution and the selected split mode.

> **Note:** This is a potentially expensive operation for large datasets. Consider balancing only after inserting all required points rather than balancing after each insertion.

**Raises:** **RuntimeError** – If the KDTree object is not valid or if balancing fails.

#### `KDTree.CreateQueryObject(self)` <a id="c4d.utils.KDTree.CreateQueryObject"></a>

Creates a query interface for performing spatial searches on the KDTree.

The query object provides methods for nearest neighbor searches, range queries, and other spatial operations. Multiple query objects can be created from the same KDTree for concurrent access.

> **Note:** The KDTree must be balanced before creating query objects. Ensure [`Balance()`](#c4d.utils.KDTree.Balance) has been called after inserting points.

**Return type:** [c4d.utils.KDTreeQuery](../KDTreeQuery/index.md#c4d.utils.KDTreeQuery)

**Returns:** A query interface for performing spatial searches on this KDTree.

**Raises:** **RuntimeError** – If the KDTree object is not valid or if query object creation fails.

#### `KDTree.Insert(self, points, id_value=None)` <a id="c4d.utils.KDTree.Insert"></a>

Inserts one or more points into the KDTree.

When inserting a list, points are automatically assigned sequential indices starting from 0.

> **Note:** After inserting points, you must call [`Balance()`](#c4d.utils.KDTree.Balance) before performing any queries. The tree structure is not updated until balancing occurs.

**Parameters:**

- **points** (*Union*[[*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector), *List*[[*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)]]) – Either a single Vector point or a list of Vector points to insert.
- **id_value** (*Optional*[*int*]) – Custom ID for the point when inserting a single Vector. Required when inserting a single point. Ignored when inserting a list of points.

**Raises:**

- **ValueError** – If inserting a single point without providing id_value, or if the points parameter is invalid.
- **TypeError** – If points is not a Vector or list of Vectors, or if any list item is not a Vector.
- **RuntimeError** – If the KDTree object is not valid or if insertion fails.
- **MemoryError** – If there is insufficient memory to store the points.

Examples:

```python
# Insert single points with custom IDs
kd_tree.Insert(c4d.Vector(1, 2, 3), 100)
kd_tree.Insert(c4d.Vector(4, 5, 6), 101)

# Insert multiple points (automatic sequential IDs: 2, 3, 4, because the first two points took IDs 100 and 101)
points = [c4d.Vector(x, 0, 0) for x in range(10)]
kd_tree.Insert(points)

# Balance after inserting
kd_tree.Balance()
```

#### `KDTree.SetSplitMode(self, split_mode)` <a id="c4d.utils.KDTree.SetSplitMode"></a>

Sets the axis split mode used during tree balancing operations.

This method controls how the KDTree subdivides space when balancing the tree structure. Different split modes can provide better performance depending on your data distribution.

> **Note:** This method only affects the tree structure when [`Balance()`](#c4d.utils.KDTree.Balance) is called. Changing the split mode after balancing requires rebalancing to take effect.

**Parameters:**

**split_mode** (*int*) –

The splitting algorithm to use:

- 0: **SPLIT_BY_COORD** - Split by coordinate axis in rotation
- 1: **SPLIT_BY_VARIANCE** - Split by axis with highest variance
- 2: **SPLIT_BY_MAX_EXTENT** - Split by axis with maximum extent (recommended for most cases)

**Raises:** **RuntimeError** – If the KDTree object is not valid or if the split mode could not be set.
