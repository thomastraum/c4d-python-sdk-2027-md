<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.utils/PolygonReduction/index.html -->

# c4d.utils.PolygonReduction <a id="c4d-utils-polygonreduction"></a>

## *class* `c4d.utils.PolygonReduction` <a id="c4d.utils.PolygonReduction"></a>

Performs polygon reduction for a polygon object.

*New in version R19.*

<a id="polygonreductiondata-dictionary"></a>**PolygonReductionData Dictionary**

The dictionary stores information required for polygon reduction:

- *_doc*: [`BaseDocument`](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument): The document.
- *_op*: [`c4d.PolygonObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject): The polygon object to be reduced.
- *_thread*: [`c4d.threading.BaseThread`](../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread): The caller thread. Set to **None** if synchronous pre-processing calculation is needed (e.g. during rendering).
- *_settings*: [`c4d.BaseContainer`](../../c4d/BaseContainer/index.md#c4d.BaseContainer): The reduction constraints settings. See *opolyreduxgen.h*.

## Overview <a id="overview"></a>

**Magic Methods**

- [`PolygonReduction.__init__()`](#c4d.utils.PolygonReduction.__init__): Creates a polygon reduction object.

**Mesh Reduction Levels**

- [`PolygonReduction.GetRemainingEdgesLevel()`](#c4d.utils.PolygonReduction.GetRemainingEdgesLevel): Queries the current remaining number of edges available to collapse.
- [`PolygonReduction.GetTriangleLevel()`](#c4d.utils.PolygonReduction.GetTriangleLevel): Queries the current triangle count.
- [`PolygonReduction.GetVertexLevel()`](#c4d.utils.PolygonReduction.GetVertexLevel): Queries the current vertex count.
- [`PolygonReduction.SetRemainingEdgesLevel()`](#c4d.utils.PolygonReduction.SetRemainingEdgesLevel): Reduces or restores the mesh to the desired number of edges remaining to collapse.
- [`PolygonReduction.SetTriangleLevel()`](#c4d.utils.PolygonReduction.SetTriangleLevel): Reduces or restores the mesh to the desired number of triangles.
- [`PolygonReduction.SetVertexLevel()`](#c4d.utils.PolygonReduction.SetVertexLevel): Reduces or restores the mesh to the desired number of vertices.

**Preprocessing Control**

- [`PolygonReduction.IsPreprocessing()`](#c4d.utils.PolygonReduction.IsPreprocessing): Checks whether the background preprocessing thread is still running.
- [`PolygonReduction.PreProcess()`](#c4d.utils.PolygonReduction.PreProcess): Starts the background or synchronous preprocessing that sets up the polygon reduction cache.
- [`PolygonReduction.Reset()`](#c4d.utils.PolygonReduction.Reset): Aborts preprocessing if it is running in the background and frees all temporary data.
- [`PolygonReduction.StopPreprocessing()`](#c4d.utils.PolygonReduction.StopPreprocessing): Aborts preprocessing if it is running in the background.

**Reduction Bounds**

- [`PolygonReduction.GetMaxRemainingEdgesLevel()`](#c4d.utils.PolygonReduction.GetMaxRemainingEdgesLevel): Queries the total number of possible edge collapses.
- [`PolygonReduction.GetMaxTriangleLevel()`](#c4d.utils.PolygonReduction.GetMaxTriangleLevel): Queries the triangle count when no reduction has been performed.
- [`PolygonReduction.GetMaxVertexLevel()`](#c4d.utils.PolygonReduction.GetMaxVertexLevel): Queries the vertex count when no reduction has been performed.
- [`PolygonReduction.GetMinTriangleLevel()`](#c4d.utils.PolygonReduction.GetMinTriangleLevel): Queries the triangle count when complete reduction has been performed.
- [`PolygonReduction.GetMinVertexLevel()`](#c4d.utils.PolygonReduction.GetMinVertexLevel): Queries the vertex count when complete reduction has been performed.

**Reduction Strength**

- [`PolygonReduction.GetMaxReductionStrengthLevel()`](#c4d.utils.PolygonReduction.GetMaxReductionStrengthLevel): Queries the maximum reduction strength percentage.
- [`PolygonReduction.GetReductionStrengthLevel()`](#c4d.utils.PolygonReduction.GetReductionStrengthLevel): Queries the current reduction strength level.
- [`PolygonReduction.SetReductionStrengthLevel()`](#c4d.utils.PolygonReduction.SetReductionStrengthLevel): Sets the reduction strength level if the desired level is different than the current one.

**State And Data**

- [`PolygonReduction.GetData()`](#c4d.utils.PolygonReduction.GetData): Retrieves the associated data for the polygon reduction.
- [`PolygonReduction.IsValid()`](#c4d.utils.PolygonReduction.IsValid): Checks if a valid object and a valid document are associated with the [`PolygonReduction`](#c4d.utils.PolygonReduction) instance.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.utils.PolygonReduction-method-Magic-Methods"></a>

#### `PolygonReduction.__init__(self)` <a id="c4d.utils.PolygonReduction.__init__"></a>

Creates a polygon reduction object.

### Mesh Reduction Levels <a id="c4d.utils.PolygonReduction-method-Mesh-Reduction-Levels"></a>

#### `PolygonReduction.GetRemainingEdgesLevel(self)` <a id="c4d.utils.PolygonReduction.GetRemainingEdgesLevel"></a>

Queries the current remaining number of edges available to collapse.

**Return type:** int

**Returns:** The remaining edges level.

#### `PolygonReduction.GetTriangleLevel(self)` <a id="c4d.utils.PolygonReduction.GetTriangleLevel"></a>

Queries the current triangle count.

**Return type:** int

**Returns:** The triangle count.

#### `PolygonReduction.GetVertexLevel(self)` <a id="c4d.utils.PolygonReduction.GetVertexLevel"></a>

Queries the current vertex count.

**Return type:** int

**Returns:** The vertex count.

#### `PolygonReduction.SetRemainingEdgesLevel(self, desiredLevel)` <a id="c4d.utils.PolygonReduction.SetRemainingEdgesLevel"></a>

Reduces or restores the mesh to the desired number of edges remaining to collapse.

> **Note:**
>
> If the desired level is different than the current level, at least one edge collapse or restore will be performed.  
> The actual resulting number of edges may be slightly different.

**Parameters:** **desiredLevel** (*int*) – The desired number of collapse stack.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `PolygonReduction.SetTriangleLevel(self, desiredLevel)` <a id="c4d.utils.PolygonReduction.SetTriangleLevel"></a>

Reduces or restores the mesh to the desired number of triangles.

> **Note:**
>
> If the desired level is different than the current level, at least one edge collapse or restore will be performed.  
> The actual resulting number of triangles may be slightly different.

**Parameters:** **desiredLevel** (*int*) – The desired number of triangles on call.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `PolygonReduction.SetVertexLevel(self, desiredLevel)` <a id="c4d.utils.PolygonReduction.SetVertexLevel"></a>

Reduces or restores the mesh to the desired number of vertices.

> **Note:**
>
> If the desired level is different than the current level, at least one edge collapse or restore will be performed.  
> The actual resulting number of vertices may be slightly different.

**Parameters:** **desiredLevel** (*int*) – The desired number of vertices on call.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Preprocessing Control <a id="c4d.utils.PolygonReduction-method-Preprocessing-Control"></a>

#### `PolygonReduction.IsPreprocessing(self)` <a id="c4d.utils.PolygonReduction.IsPreprocessing"></a>

Checks whether the background preprocessing thread is still running.

**Return type:** bool

**Returns:** **True** if preprocessing is ongoing, otherwise **False**.

#### `PolygonReduction.PreProcess(self, data)` <a id="c4d.utils.PolygonReduction.PreProcess"></a>

Starts the background or synchronous preprocessing that sets up the polygon reduction cache.

**Parameters:** **data** (*dict*) – The data for the reduction. See [PolygonReductionData Dictionary](#polygonreductiondata-dictionary).

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `PolygonReduction.Reset(self)` <a id="c4d.utils.PolygonReduction.Reset"></a>

Aborts preprocessing if it is running in the background and frees all temporary data.

#### `PolygonReduction.StopPreprocessing(self)` <a id="c4d.utils.PolygonReduction.StopPreprocessing"></a>

Aborts preprocessing if it is running in the background. Resets the interactive settings values.

### Reduction Bounds <a id="c4d.utils.PolygonReduction-method-Reduction-Bounds"></a>

#### `PolygonReduction.GetMaxRemainingEdgesLevel(self)` <a id="c4d.utils.PolygonReduction.GetMaxRemainingEdgesLevel"></a>

Queries the total number of possible edge collapses.

**Return type:** int

**Returns:** The maximum collapse count.

#### `PolygonReduction.GetMaxTriangleLevel(self)` <a id="c4d.utils.PolygonReduction.GetMaxTriangleLevel"></a>

Queries the triangle count when no reduction has been performed.

**Return type:** int

**Returns:** The maximum triangle count.

#### `PolygonReduction.GetMaxVertexLevel(self)` <a id="c4d.utils.PolygonReduction.GetMaxVertexLevel"></a>

Queries the vertex count when no reduction has been performed.

**Return type:** int

**Returns:** The maximum vertex count.

#### `PolygonReduction.GetMinTriangleLevel(self)` <a id="c4d.utils.PolygonReduction.GetMinTriangleLevel"></a>

Queries the triangle count when complete reduction has been performed.

**Return type:** int

**Returns:** The minimum triangle count. May be non-zero if border constraints are enabled.

#### `PolygonReduction.GetMinVertexLevel(self)` <a id="c4d.utils.PolygonReduction.GetMinVertexLevel"></a>

Queries the vertex count when complete reduction has been performed.

**Return type:** int

**Returns:** The minimum vertex count. May be non-zero if border constraints are enabled.

### Reduction Strength <a id="c4d.utils.PolygonReduction-method-Reduction-Strength"></a>

#### `PolygonReduction.GetMaxReductionStrengthLevel(self)` <a id="c4d.utils.PolygonReduction.GetMaxReductionStrengthLevel"></a>

Queries the maximum reduction strength percentage.

**Return type:** float

**Returns:** The maximum reduction strength percentage. Always *1.0*.

#### `PolygonReduction.GetReductionStrengthLevel(self)` <a id="c4d.utils.PolygonReduction.GetReductionStrengthLevel"></a>

Queries the current reduction strength level.

**Return type:** int

**Returns:** The reduction strength percentage: *0* means no reduction performed, *1* means maximum reduction performed.

#### `PolygonReduction.SetReductionStrengthLevel(self, strengthLevel)` <a id="c4d.utils.PolygonReduction.SetReductionStrengthLevel"></a>

Sets the reduction strength level if the desired level is different than the current one.

**Parameters:** **strengthLevel** (*float*) – The desired reduction strength level.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### State And Data <a id="c4d.utils.PolygonReduction-method-State-And-Data"></a>

#### `PolygonReduction.GetData(self)` <a id="c4d.utils.PolygonReduction.GetData"></a>

Retrieves the associated data for the polygon reduction.

**Return type:** dict

**Returns:** The associated data. See [PolygonReductionData Dictionary](#polygonreductiondata-dictionary).

#### `PolygonReduction.IsValid(self)` <a id="c4d.utils.PolygonReduction.IsValid"></a>

Checks if a valid object and a valid document are associated with the [`PolygonReduction`](#c4d.utils.PolygonReduction) instance.

**Return type:** bool

**Returns:** **True** if the [`PolygonReduction`](#c4d.utils.PolygonReduction) instance is valid, otherwise **False**.
