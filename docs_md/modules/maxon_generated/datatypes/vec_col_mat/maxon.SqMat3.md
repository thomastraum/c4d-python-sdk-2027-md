<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/vec_col_mat/maxon.SqMat3.html -->

# maxon.SqMat3 <a id="maxon-sqmat3"></a>

## Description <a id="module-maxon.SqMat3"></a><a id="description"></a>

A 3x3 matrix

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)
- [`maxon.Struct`](../base_core/maxon.Struct.md#module-maxon.Struct)

Children Classes:

- [`maxon.SqMat3_32`](maxon.SqMat3_32.md#module-maxon.SqMat3_32)
- [`maxon.SqMat3_64`](maxon.SqMat3_64.md#module-maxon.SqMat3_64)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.SqMat3.V`](maxon.SqMat3.V.md#maxon.SqMat3.V) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetLength`](#maxon.SqMat3.GetLength)() | Returns a vector composed by length of each component. |
| [`GetNormalized`](#maxon.SqMat3.GetNormalized)() | Returns a normalized matrix. |
| [`GetTransposed`](#maxon.SqMat3.GetTransposed)() | Returns the transposed matrix. |
| [`Normalize`](#maxon.SqMat3.Normalize)() | Normalize all vectors of the matrix. |
| [`SetIdentity`](#maxon.SqMat3.SetIdentity)() | Defines the default identity matrix |
| [`__init__`](#maxon.SqMat3.__init__)([v1_in, v2_in, v3_in]) | Initializes a new three components square matrix. |

## Methods Definition <a id="methods-definition"></a>

### `SqMat3.GetLength()` <a id="maxon.SqMat3.GetLength"></a>

Returns a vector composed by length of each component.

**Returns:** The matrix length.

**Return type:** [`maxon.Vector`](maxon.Vector.md#module-maxon.Vector)

### `SqMat3.GetNormalized()` <a id="maxon.SqMat3.GetNormalized"></a>

Returns a normalized matrix.

**Returns:** The normalized matrix.

**Return type:** [`maxon.SqMat3`](#module-maxon.SqMat3)

### `SqMat3.GetTransposed()` <a id="maxon.SqMat3.GetTransposed"></a>

Returns the transposed matrix.

**Returns:** The transposed matrix.

**Return type:** [`maxon.SqMat3`](#module-maxon.SqMat3)

### `SqMat3.Normalize()` <a id="maxon.SqMat3.Normalize"></a>

Normalize all vectors of the matrix.

### `SqMat3.SetIdentity()` <a id="maxon.SqMat3.SetIdentity"></a>

Defines the default identity matrix

### `SqMat3.__init__(v1_in=None, v2_in=None, v3_in=None)` <a id="maxon.SqMat3.__init__"></a>

Initializes a new three components square matrix.  
When passing no arguments, the identity matrix will be constructed. The type can otherwise  
be only instantiated three at the moment, setting all three components individually.

**..note** This type should not be instantiated directly as this can lead to crashes, use instead the type [`maxon.Matrix`](maxon.Matrix.md#module-maxon.Matrix).

**Parameters:**

- **v1_in** (Optional[[`maxon.Vec3`](maxon.Vec3.md#module-maxon.Vec3)]) – If *v1_in* is the only passed argument, set this to v1_in/v2_in/v3_in components. Otherwise, set the v1 component.
- **v2_in** (Optional[[`maxon.Vec3`](maxon.Vec3.md#module-maxon.Vec3)]) – The v2 component. Can only be passed if *v3_in* is also defined.
- **v3_in** (Optional[[`maxon.Vec3`](maxon.Vec3.md#module-maxon.Vec3)]) – The v3 component.
