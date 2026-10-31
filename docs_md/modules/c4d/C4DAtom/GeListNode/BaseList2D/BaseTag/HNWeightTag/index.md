<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/HNWeightTag/index.html -->

# c4d.HNWeightTag <a id="c4d-hnweighttag"></a>

## *class* `c4d.HNWeightTag` <a id="c4d.HNWeightTag"></a>

Represents an SDS Weight Tag, which stores subdivision surface weighting data for points and polygon edges.

> **Note:** The tag must be attached to a PolygonObject for operations to work properly and [`InitFromObject()`](#c4d.HNWeightTag.InitFromObject) must be called methods to work properly.

**Example:**

```python
import c4d

# Create a polygon object (cube)
polyObj = c4d.BaseObject(c4d.Ocube)

# Create an SDS object and put the cube under it
sds = c4d.BaseObject(c4d.Osds)
polyObj.InsertUnder(sds)

# Add weight tag to the cube
weight_tag = polyObj.MakeTag(c4d.Tsds)

# No need to explicitly call InitFromObject() - setter methods will initialize automatically
weight_tag.SetPointWeight(index=0, weight=0.5)

# Set polygon edge weight with validation and neighbor synchronization
weight_tag.SetPolyEdgeWeight(poly_index=0, edge_index=1, weight=0.8, validate=True)

# Update the cache
weight_tag.SetDirty(c4d.DIRTYFLAGS_DATA)
polyObj.SetDirty(c4d.DIRTYFLAGS_DATA)

# Insert into document
doc.InsertObject(sds)
c4d.EventAdd()
```

Parent Class:

- [`c4d.BaseTag`](../index.md#c4d.BaseTag)

## Overview <a id="overview"></a>

**Data Initialization And Storage**

- [`HNWeightTag.GetTagData()`](#c4d.HNWeightTag.GetTagData): Retrieves the weight data as a dictionary containing point and polygon weight information.
- [`HNWeightTag.InitFromObject()`](#c4d.HNWeightTag.InitFromObject): Initializes the weight tag with default weights based on the attached geometry.
- [`HNWeightTag.SetTagData()`](#c4d.HNWeightTag.SetTagData): Sets the weight data from a dictionary containing point and polygon weight information.

**Edge Weight Management**

- [`HNWeightTag.GetPolyEdgeWeight()`](#c4d.HNWeightTag.GetPolyEdgeWeight): Gets the weight value for a specific polygon edge.
- [`HNWeightTag.SetPolyEdgeWeight()`](#c4d.HNWeightTag.SetPolyEdgeWeight): Sets the weight value for a specific polygon edge with optional validation and neighbor synchronization.

**Point Weight Management**

- [`HNWeightTag.GetAllPointWeights()`](#c4d.HNWeightTag.GetAllPointWeights): Gets all point weights as a list.
- [`HNWeightTag.GetPointCount()`](#c4d.HNWeightTag.GetPointCount): Gets the number of points in the weight tag.
- [`HNWeightTag.GetPointWeight()`](#c4d.HNWeightTag.GetPointWeight): Gets the weight value for a specific point by index.
- [`HNWeightTag.SetAllPointWeights()`](#c4d.HNWeightTag.SetAllPointWeights): Sets all point weights from a list.
- [`HNWeightTag.SetPointWeight()`](#c4d.HNWeightTag.SetPointWeight): Sets the weight value for a specific point by index.

**Polygon Weight Management**

- [`HNWeightTag.GetAllPolyWeights()`](#c4d.HNWeightTag.GetAllPolyWeights): Gets all polygon weights as a list of dictionaries.
- [`HNWeightTag.GetPolyCount()`](#c4d.HNWeightTag.GetPolyCount): Gets the number of polygons in the weight tag.
- [`HNWeightTag.GetPolyWeight()`](#c4d.HNWeightTag.GetPolyWeight): Gets the weight values for a specific polygon by index as a dictionary.
- [`HNWeightTag.SetAllPolyWeights()`](#c4d.HNWeightTag.SetAllPolyWeights): Sets all polygon weights from a list of dictionaries.
- [`HNWeightTag.SetPolyWeight()`](#c4d.HNWeightTag.SetPolyWeight): Sets the weight values for a specific polygon by index from a dictionary.

## Members <a id="members"></a>

### Data Initialization And Storage <a id="c4d.HNWeightTag-method-Data-Initialization-And-Storage"></a>

#### `HNWeightTag.GetTagData(self)` <a id="c4d.HNWeightTag.GetTagData"></a>

Retrieves the weight data as a dictionary containing point and polygon weight information.

**Return type:** Optional[Dict[str, Any]]

**Returns:**

A dictionary containing all wieghting data or **None** if data cannot be retrieved. On success, the dictionary will contain:

> - ’points’: *int* or *None* - Number of points (None if not available)
> - ’polys’: *int* or *None* - Number of polygons (None if not available)
> - ’pointweight’: *List[float]* - Point weights (empty list if not available)
> - ’polyweight’: *List[Dict[str, float]]* - Polygon edge weights (empty list if not available)

**Example:**

```python
tag_data = weight_tag.GetTagData()
if tag_data is not None:
    point_count = tag_data.get('points')
    point_weights = tag_data.get('pointweight', [])
    poly_weights = tag_data.get('polyweight', [])
```

#### `HNWeightTag.InitFromObject(self)` <a id="c4d.HNWeightTag.InitFromObject"></a>

Initializes the weight tag with default weights based on the attached geometry.

Also sends MSG_POLYGONS_CHANGED and MSG_POINTS_CHANGED messages to update the tag data. Calling this method is usually only necessary when attempting to retrive data from an uninitialized tag, as setter methods will automatically initialize the tag if needed.

**Raises:** **RuntimeError** – If the tag is not attached to a PolygonObject, if the attached object cannot be converted to a PolygonObject, or if tag data initialization fails.

**Example:**

```python
weight_tag = polygon_object.MakeTag(c4d.Tsds)
weight_tag.InitFromObject()  # Optional - explicitly initialize
```

#### `HNWeightTag.SetTagData(self, data)` <a id="c4d.HNWeightTag.SetTagData"></a>

Sets the weight data from a dictionary containing point and polygon weight information.

Only the data fields present in the dictionary will be updated, missing fields will be left unchanged.

> **Warning:** Other than :class:polygons \<c4d.CPolygon>, SDS weights look at the *d* entry for the third edge of a triangle, not at *c* as polygons do. So, to fill the SDS weight for a triangle, one must fill *a*, *b*, and *d*. But just as for polygons, it is convention to fill the empty slot with the third value, so a triangle is often defined with the weights *(a, b, c, c)*.

**Parameters:**

**data** (*Dict*[*str*, *Any*]) –

Dictionary containing tag data. Expected structure:

- ’pointweight’: *List[float]*, optional - Point weight values
- ’polyweight’: *List[Dict[str, float]]*, optional - Polygon weight dictionaries Each polygon weight dict should contain ‘a’, ‘b’, ‘c’, ‘d’ keys for edge weights.

**Raises:**

- **TypeError** – If data is not a dictionary, if pointweight is not a list, if polyweight is not a list, or if polygon weight elements are not dictionaries.
- **ValueError** – If pointweight list size exceeds available points, if polyweight list size exceeds available polygons, or if data is not available.
- **RuntimeError** – If tag data cannot be retrieved or accessed.

**Example:**

```python
tag_data = weight_tag.GetTagData()
if tag_data and 'pointweight' in tag_data:
    tag_data['pointweight'][0] = 1.0  # Modify first point weight
if tag_data and 'polyweight' in tag_data:
    tag_data['polyweight'][0]['a'] = 0.8  # Modify first polygon's edge 'a'
weight_tag.SetTagData(tag_data)

weight_tag.SetDirty(c4d.DIRTYFLAGS_DATA)
weight_tag.GetObject().SetDirty(c4d.DIRTYFLAGS_DATA)
```

### Edge Weight Management <a id="c4d.HNWeightTag-method-Edge-Weight-Management"></a>

#### `HNWeightTag.GetPolyEdgeWeight(self, poly_index, edge_index)` <a id="c4d.HNWeightTag.GetPolyEdgeWeight"></a>

Gets the weight value for a specific polygon edge.

**Parameters:**

- **poly_index** (*int*) – Zero-based index of the polygon.
- **edge_index** (*int*) – Edge index (0=a, 1=b, 2=c, 3=d). Must be between 0 and 3 inclusive.

**Return type:** Optional[float]

**Returns:** The weight value for the specified polygon edge, or **None** if tag data cannot be retrieved or if the tag is not properly initialized.

**Raises:** **IndexError** – If poly_index is negative or >= polygon count, or if edge_index is not 0-3.

**Example:**

```python
edge_a_weight = weight_tag.GetPolyEdgeWeight(poly_index=0, edge_index=0)
edge_c_weight = weight_tag.GetPolyEdgeWeight(poly_index=0, edge_index=2)
if edge_a_weight is not None and edge_c_weight is not None:
    print("Edge weights: a={}, c={}".format(edge_a_weight, edge_c_weight))
else:
    print("Could not retrieve edge weights - tag not initialized?")
```

#### `HNWeightTag.SetPolyEdgeWeight(self, poly_index, edge_index, weight, validate=True)` <a id="c4d.HNWeightTag.SetPolyEdgeWeight"></a>

Sets the weight value for a specific polygon edge with optional validation and neighbor synchronization.

When *validate* is **True**, the method will validate is between 0.0 and 1.0 inclusive and will update neighboring polygon edges that share the same geometric edge to ensure consistent weighting across shared edges. When validate=False, validation and neighbor updating are skipped.

> **Warning:** Other than :class:polygons \<c4d.CPolygon>, SDS weights look at the *d* entry for the third edge of a triangle, not at *c* as polygons do. So, to fill the SDS weight for a triangle, one must fill *a*, *b*, and *d*. But just as for polygons, it is convention to fill the empty slot with the third value, so a triangle is often defined with the weights *(a, b, c, c)*.

**Parameters:**

- **poly_index** (*int*) – Zero-based index of the polygon.
- **edge_index** (*int*) – Edge index (0=a, 1=b, 2=c, 3=d). Must be between 0 and 3 inclusive.
- **weight** (*float*) – Weight value to set for the polygon edge.
- **validate** (*bool*) – If **True** (default), validates weight range (0.0-1.0) and synchronizes neighbor edges. If **False**, skips validation for performance-critical operations.

**Raises:**

- **IndexError** – If poly_index is negative or >= polygon count, or if edge_index is not 0-3.
- **ValueError** – If validate=True and weight is not between 0.0 and 1.0 inclusive.
- **RuntimeError** – If tag data cannot be retrieved or if the tag is not properly initialized.

**Example:**

```python
# No need to call InitFromObject() - this will initialize automatically
# Set edge weight with validation and neighbor synchronization
weight_tag.SetPolyEdgeWeight(poly_index=0, edge_index=1, weight=0.8)

# Skip validation for special cases or performance
weight_tag.SetPolyEdgeWeight(poly_index=5, edge_index=2, weight=1.5, validate=False)

# Set multiple edges
for i in range(4):
    weight_tag.SetPolyEdgeWeight(poly_index=0, edge_index=i, weight=0.5 + i * 0.1)

weight_tag.SetDirty(c4d.DIRTYFLAGS_DATA)
weight_tag.GetObject().SetDirty(c4d.DIRTYFLAGS_DATA)
```

### Point Weight Management <a id="c4d.HNWeightTag-method-Point-Weight-Management"></a>

#### `HNWeightTag.GetAllPointWeights(self)` <a id="c4d.HNWeightTag.GetAllPointWeights"></a>

Gets all point weights as a list.

**Return type:** Optional[List[float]]

**Returns:** List of weight values for all points, or **None** if tag data cannot be retrieved or if the tag is not properly initialized.

**Example:**

```python
weights = weight_tag.GetAllPointWeights()
if weights is not None:
    print("First 3 weights: {}".format(weights[:3]))
    avg_weight = sum(weights) / len(weights) if weights else 0
else:
    print("Could not retrieve point weights - tag not initialized?")
```

#### `HNWeightTag.GetPointCount(self)` <a id="c4d.HNWeightTag.GetPointCount"></a>

Gets the number of points in the weight tag.

**Return type:** Optional[int]

**Returns:** Number of points, or **None** if tag data cannot be retrieved or if the tag is not properly initialized.

**Example:**

```python
count = weight_tag.GetPointCount()
if count is not None:
    print("Tag manages weights for {} points".format(count))
else:
    print("Could not retrieve point count - tag not initialized?")
```

#### `HNWeightTag.GetPointWeight(self, index)` <a id="c4d.HNWeightTag.GetPointWeight"></a>

Gets the weight value for a specific point by index.

**Parameters:** **index** (*int*) – Zero-based index of the point.

**Return type:** Optional[float]

**Returns:** The weight value for the specified point, or **None** if tag data cannot be retrieved or if the tag is not properly initialized.

**Raises:** **IndexError** – If index is negative or >= point count.

**Example:**

```python
weight = weight_tag.GetPointWeight(index=0)
if weight is not None:
    print("Point 0 weight: {}".format(weight))
else:
    print("Could not retrieve point weight - tag not initialized?")
```

#### `HNWeightTag.SetAllPointWeights(self, weights)` <a id="c4d.HNWeightTag.SetAllPointWeights"></a>

Sets all point weights from a list.

**Parameters:** **weights** (*List*[*float*]) – List of weight values. Length must exactly match the point count.

**Raises:**

- **ValueError** – If list size doesn’t match point count or if weight values are invalid.
- **TypeError** – If weights is not a list or if weight values are not numeric.
- **RuntimeError** – If tag data cannot be retrieved or if the tag is not properly initialized.

**Example:**

```python
# No need to call InitFromObject() - this will initialize automatically
point_count = weight_tag.GetPointCount()
if point_count is not None:
    weights = [0.5] * point_count  # Set all weights to 0.5
    weight_tag.SetAllPointWeights(weights)
    
    # Create gradient weights
    gradient_weights = [i / float(point_count - 1) for i in range(point_count)]
    weight_tag.SetAllPointWeights(gradient_weights)

    weight_tag.SetDirty(c4d.DIRTYFLAGS_DATA)
    weight_tag.GetObject().SetDirty(c4d.DIRTYFLAGS_DATA)
```

#### `HNWeightTag.SetPointWeight(self, index, weight)` <a id="c4d.HNWeightTag.SetPointWeight"></a>

Sets the weight value for a specific point by index.

**Parameters:**

- **index** (*int*) – Zero-based index of the point.
- **weight** (*float*) – Weight value to set for the point.

**Raises:**

- **IndexError** – If index is negative or >= point count.
- **RuntimeError** – If tag data cannot be retrieved or if the tag is not properly initialized.

**Example:**

```python
# No need to call InitFromObject() - this will initialize automatically
weight_tag.SetPointWeight(index=0, weight=0.75)
weight_tag.SetPointWeight(index=5, weight=1.0)
weight_tag.SetDirty(c4d.DIRTYFLAGS_DATA)
weight_tag.GetObject().SetDirty(c4d.DIRTYFLAGS_DATA)
```

### Polygon Weight Management <a id="c4d.HNWeightTag-method-Polygon-Weight-Management"></a>

#### `HNWeightTag.GetAllPolyWeights(self)` <a id="c4d.HNWeightTag.GetAllPolyWeights"></a>

Gets all polygon weights as a list of dictionaries.

**Return type:** Optional[List[Dict[str, float]]]

**Returns:**

List of polygon weight dictionaries. Each dictionary contains:

- ’a’: float - Weight for edge A-B
- ’b’: float - Weight for edge B-C
- ’c’: float - Weight for edge C-D
- ’d’: float - Weight for edge D-A

Returns **None** if tag data cannot be retrieved or if the tag is not properly initialized.

**Example:**

```python
all_weights = weight_tag.GetAllPolyWeights()
if all_weights is not None:
    for i, poly_weight in enumerate(all_weights):
        print("Polygon {}: max_weight={}".format(i, max(poly_weight.values())))
    
    # Find polygons with high edge weights
    high_weight_polys = [
        i for i, w in enumerate(all_weights) 
        if any(val > 0.8 for val in w.values())
    ]
else:
    print("Could not retrieve polygon weights - tag not initialized?")
```

#### `HNWeightTag.GetPolyCount(self)` <a id="c4d.HNWeightTag.GetPolyCount"></a>

Gets the number of polygons in the weight tag.

**Return type:** Optional[int]

**Returns:** Number of polygons, or **None** if tag data cannot be retrieved or if the tag is not properly initialized.

**Example:**

```python
count = weight_tag.GetPolyCount()
if count is not None:
    print("Tag manages weights for {} polygons".format(count))
    print("Total edges: {}".format(count * 4))
else:
    print("Could not retrieve polygon count - tag not initialized?")
```

#### `HNWeightTag.GetPolyWeight(self, index)` <a id="c4d.HNWeightTag.GetPolyWeight"></a>

Gets the weight values for a specific polygon by index as a dictionary.

Triangles will store the same value in their ‘c’ and ‘d’ keys.

**Parameters:** **index** (*int*) – Zero-based index of the polygon.

**Return type:** Optional[Dict[str, float]]

**Returns:**

The weights for the polygon or **None** if no data can be retrieved. On success, the dictionary will contain:

> - ’a’: *float* - Weight for edge A-B
> - ’b’: *float* - Weight for edge B-C
> - ’c’: *float* - Weight for edge C-D
> - ’d’: *float* - Weight for edge D-A

**Raises:** **IndexError** – If index is negative or >= polygon count.

**Example:**

```python
poly_weight = weight_tag.GetPolyWeight(index=0)
if poly_weight is not None:
    print("Edge weights: a={}, b={}".format(poly_weight['a'], poly_weight['b']))
    max_weight = max(poly_weight.values())
else:
    print("Could not retrieve polygon weight - tag not initialized?")
```

#### `HNWeightTag.SetAllPolyWeights(self, weights)` <a id="c4d.HNWeightTag.SetAllPolyWeights"></a>

Sets all polygon weights from a list of dictionaries.

Only specified edges in each dictionary will be updated. Unspecified edges retain their current values. The list length must exactly match the polygon count.

**Parameters:** **weights** (*List*[*Dict*[*str*, *float*]]) – List of polygon weight dictionaries. Length must exactly match polygon count. Each dictionary may contain ‘a’, ‘b’, ‘c’, ‘d’ keys for edge weights.

**Raises:**

- **ValueError** – If list size doesn’t match polygon count.
- **TypeError** – If weights is not a list, or if polygon weights are not dictionaries.
- **RuntimeError** – If tag data cannot be retrieved or if the tag is not properly initialized.

**Example:**

```python
# No need to call InitFromObject() - this will initialize automatically
poly_count = weight_tag.GetPolyCount()
if poly_count is not None:
    # Set uniform weights for all polygons
    uniform_weights = [{'a': 0.5, 'b': 0.5, 'c': 0.5, 'd': 0.5}] * poly_count
    weight_tag.SetAllPolyWeights(uniform_weights)
    
    # Set gradient weights
    gradient_weights = []
    for i in range(poly_count):
        base_weight = i / float(poly_count - 1) * 0.5
        gradient_weights.append({
            'a': base_weight,
            'b': base_weight + 0.1,
            'c': base_weight + 0.2, 
            'd': base_weight + 0.3
        })
    weight_tag.SetAllPolyWeights(gradient_weights)

    weight_tag.SetDirty(c4d.DIRTYFLAGS_DATA)
    weight_tag.GetObject().SetDirty(c4d.DIRTYFLAGS_DATA)
```

#### `HNWeightTag.SetPolyWeight(self, index, weight)` <a id="c4d.HNWeightTag.SetPolyWeight"></a>

Sets the weight values for a specific polygon by index from a dictionary.

Only the edges specified in the weight dictionary will be modified. Unspecified edges retain their current values.

> **Warning:** Other than :class:polygons \<c4d.CPolygon>, SDS weights look at the *d* entry for the third edge of a triangle, not at *c* as polygons do. So, to fill the SDS weight for a triangle, one must fill *a*, *b*, and *d*. But just as for polygons, it is convention to fill the empty slot with the third value, so a triangle is often defined with the weights *(a, b, c, c)*.

**Parameters:**

- **index** (*int*) – Zero-based index of the polygon.
- **weight** (*Dict*[*str*, *float*]) – Dictionary containing edge weights. Valid keys are ‘a’, ‘b’, ‘c’, ‘d’. Only specified edges will be updated.

**Raises:**

- **IndexError** – If index is negative or >= polygon count.
- **TypeError** – If weight is not a dictionary.
- **RuntimeError** – If tag data cannot be retrieved or if the tag is not properly initialized.

**Example:**

```python
# No need to call InitFromObject() - this will initialize automatically
# Set all edges of polygon 0
weight_tag.SetPolyWeight(index=0, weight={'a': 0.2, 'b': 0.4, 'c': 0.6, 'd': 0.8})

# Update only specific edges
weight_tag.SetPolyWeight(index=1, weight={'a': 1.0, 'c': 0.5})

weight_tag.SetDirty(c4d.DIRTYFLAGS_DATA)
weight_tag.GetObject().SetDirty(c4d.DIRTYFLAGS_DATA)
```
