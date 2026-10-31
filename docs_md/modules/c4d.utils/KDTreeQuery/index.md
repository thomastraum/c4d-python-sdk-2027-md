<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.utils/KDTreeQuery/index.html -->

# c4d.utils.KDTreeQuery <a id="c4d-utils-kdtreequery"></a>

## *class* `c4d.utils.KDTreeQuery` <a id="c4d.utils.KDTreeQuery"></a>

Query interface for performing spatial searches on a KDTree.  
Provides efficient nearest neighbor searches, range queries, and spatial clustering operations.

This class is created by calling `KDTree.CreateQueryObject()` and provides the main  
interface for spatial queries. It maintains internal state for optimized repeated queries.

*New in version 2026.2.0.*

> **Note:** KDTreeQuery objects are lightweight and can be created multiple times from the same KDTree. The parent KDTree will be remain valid for the lifetime of any query objects.

## Overview <a id="overview"></a>

- [`KDTreeQuery.FindNearest()`](#c4d.utils.KDTreeQuery.FindNearest): Finds the nearest point in the KDTree to the given query point.
- [`KDTreeQuery.FindNearestMultiple()`](#c4d.utils.KDTreeQuery.FindNearestMultiple): Finds multiple nearest points within specified distance and count constraints.
- [`KDTreeQuery.FindRange()`](#c4d.utils.KDTreeQuery.FindRange): Finds all points within a specified distance range from the query point.

## Members <a id="members"></a>

### Spatial Queries <a id="c4d.utils.KDTreeQuery-method-Spatial-Queries"></a>

#### `KDTreeQuery.FindNearest(self, point, idx_to_ignore=None, return_nearest_info=False)` <a id="c4d.utils.KDTreeQuery.FindNearest"></a>

Finds the nearest point in the KDTree to the given query point.

This method performs an efficient nearest neighbor search using the KDTree’s spatial partitioning. Optionally returns detailed information about the nearest point.

**Parameters:**

- **point** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The 3D position to search from.
- **idx_to_ignore** (*Optional*[*int*]) – Optional point index to ignore during the search. Useful when searching for the nearest neighbor excluding a known point.
- **return_nearest_info** (*bool*) – **False** (default) to return only the point index. **True** to return both index and detailed information about the nearest point.

**Return type:** Union[int, Tuple[int, Dict[str, Any]]]

**Returns:**

**If *return_nearest_info* is False** The index of the nearest point, or **-1** if no points are found.

**If *return_nearest_info* is True**

A tuple containing:

- **int**: The index of the nearest point (-1 if not found)

- **Dict[str, Any]**: Detailed information with the following keys:

  > - ’node’: Dict with ‘point’ (c4d.Vector) and ‘id’ (int)
  > - ’dist’: float - Distance to the nearest point

**Raises:** **RuntimeError** – If the KDTreeQuery object is not valid.

Examples:

```python
# Simple nearest neighbor search
nearest_index = query.FindNearest(c4d.Vector(1, 1, 1))
if nearest_index != -1:
    print("Nearest point found at index:", nearest_index)

# Detailed search with distance information
nearest_index, info = query.FindNearest(
    c4d.Vector(1, 1, 1), 
    return_nearest_info=True
)

if nearest_index != -1:
    node = info['node']
    print(f"Nearest: {node['point']} (ID: {node['id']}) at distance {info['dist']}")

# Ignore a specific point during search
second_nearest = query.FindNearest(c4d.Vector(1, 1, 1), idx_to_ignore=nearest_index)
```

#### `KDTreeQuery.FindNearestMultiple(self, point, max_distance=inf, max_elements=10, sort_results=True, squared_distances=False, idx_to_ignore=None)` <a id="c4d.utils.KDTreeQuery.FindNearestMultiple"></a>

Finds multiple nearest points within specified distance and count constraints.

This method returns up to *max_elements* points that are within *max_distance* of the query point. Results can optionally be sorted by distance and can use squared distances for performance.

**Parameters:**

- **point** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The 3D position to search from.
- **max_distance** (*float*) – Maximum distance to search within. Points farther than this distance are excluded from results. Defaults to infinity (no distance limit).
- **max_elements** (*int*) – Maximum number of points to return. Defaults to 10. The actual number returned may be less if fewer points exist within the distance limit.
- **sort_results** (*bool*) – **True** (default) to sort results by distance (nearest first). **False** for unsorted results, which may be faster for large result sets.
- **squared_distances** (*bool*) – **False** (default) to return actual distances. **True** to return squared distances for performance optimization when only relative distances matter.
- **idx_to_ignore** (*Optional*[*int*]) – Optional point index to ignore during the search.

**Return type:** List[Dict[str, Any]]

**Returns:**

A list of dictionaries, each containing:

- ’node’: Dict with ‘point’ (c4d.Vector) and ‘id’ (int)
- ’dist’: float - Distance to the point (squared if squared_distances=True)

Returns an empty list if no points are found within the constraints.

**Raises:** **RuntimeError** – If the KDTreeQuery object is not valid.

Examples:

```python
# Find up to 5 nearest points within distance 10
nearby = query.FindNearestMultiple(
    c4d.Vector(0, 0, 0),
    max_distance=10.0,
    max_elements=5
)

for result in nearby:
    node = result['node']
    print(f"Point {node['point']} (ID: {node['id']}) at distance {result['dist']}")

# Performance optimization: use squared distances when only relative order matters
nearby_squared = query.FindNearestMultiple(
    c4d.Vector(0, 0, 0),
    max_elements=10,
    squared_distances=True,
    sort_results=False  # Skip sorting for better performance
)

# Find all neighbors within radius, unlimited count
all_neighbors = query.FindNearestMultiple(
    c4d.Vector(5, 5, 5),
    max_distance=2.0,
    max_elements=99999  # Effectively unlimited
)
```

#### `KDTreeQuery.FindRange(self, point, max_distance, sort_results=True, squared_distances=False, idx_to_ignore=None)` <a id="c4d.utils.KDTreeQuery.FindRange"></a>

Finds all points within a specified distance range from the query point.

This method returns all points within *max_distance* of the query point without limiting the number of results. Use this for range queries where you need all points within a specific radius.

**Parameters:**

- **point** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The 3D position to search from.
- **max_distance** (*float*) – Maximum distance to search within. All points within this distance from the query point will be included in the results.
- **sort_results** (*bool*) – **True** (default) to sort results by distance (nearest first). **False** for unsorted results, which may be faster for large result sets.
- **squared_distances** (*bool*) – **False** (default) to return actual distances. **True** to return squared distances for performance optimization.
- **idx_to_ignore** (*Optional*[*int*]) – Optional point index to ignore during the search.

**Return type:** List[Dict[str, Any]]

**Returns:**

A list of dictionaries for all points within range, each containing:

- ’node’: Dict with ‘point’ (c4d.Vector) and ‘id’ (int)
- ’dist’: float - Distance to the point (squared if squared_distances=True)

Returns an empty list if no points are found within the range.

**Raises:** **RuntimeError** – If the KDTreeQuery object is not valid.

Examples:

```python
# Find all points within distance 5 from origin
points_in_range = query.FindRange(
    c4d.Vector(0, 0, 0),
    max_distance=5.0
)

print(f"Found {len(points_in_range)} points within radius 5")
for result in points_in_range:
    node = result['node']
    print(f"Point {node['point']} at distance {result['dist']}")

# Large radius search with performance optimization
large_range = query.FindRange(
    c4d.Vector(10, 10, 10),
    max_distance=50.0,
    sort_results=False,     # Skip sorting for performance
    squared_distances=True  # Use squared distances
)

# Clustering: find points near each other
cluster_centers = [c4d.Vector(0, 0, 0), c4d.Vector(10, 0, 0)]
for i, center in enumerate(cluster_centers):
    cluster_points = query.FindRange(center, max_distance=3.0)
    print(f"Cluster {i}: {len(cluster_points)} points")
```
