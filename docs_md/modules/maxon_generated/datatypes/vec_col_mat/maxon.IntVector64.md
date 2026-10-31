<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector64.html -->

# maxon.IntVector64 <a id="maxon-intvector64"></a>

## Description <a id="module-maxon.IntVector64"></a><a id="description"></a>

A vector consisting of three components X, Y and Z.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Vec3`](maxon.Vec3.md#module-maxon.Vec3)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.IntVector64.STRIDE`](maxon.IntVector64.STRIDE.md#maxon.IntVector64.STRIDE) |  |
| [`maxon.IntVector64.ValueType`](maxon.IntVector64.ValueType.md#maxon.IntVector64.ValueType) |  |
| [`maxon.IntVector64.x`](maxon.IntVector64.x.md#maxon.IntVector64.x) |  |
| [`maxon.IntVector64.y`](maxon.IntVector64.y.md#maxon.IntVector64.y) |  |
| [`maxon.IntVector64.z`](maxon.IntVector64.z.md#maxon.IntVector64.z) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`__init__`](#maxon.IntVector64.__init__)([x, y, z]) | Initializes a new three component vector. |

## Methods Definition <a id="methods-definition"></a>

### `IntVector64.__init__(x=None, y=None, z=None)` <a id="maxon.IntVector64.__init__"></a>

Initializes a new three component vector.  
It is possible to instantiate a new vector without any arguments, causing the *x, y, z*  
components to default to the value *0*. The type can otherwise be instantiated with one or  
three arguments, either setting all components to the same value or copying another  
[`maxon.Vec3`](maxon.Vec3.md#module-maxon.Vec3) instance, or setting all three components individually.

**..note** This type should not be instantiated directly, use instead the type [`maxon.Vector`](maxon.Vector.md#module-maxon.Vector).

**Parameters:**

- **x** (Optional[[`maxon.Vec4`](maxon.Vec4.md#module-maxon.Vec4), float]) – If *x* is the only passed argument. If this is a float set this value to X/Y/Z components. If this is a vector, this vector is copied.
- **y** (*float*) – The z component. Can only be passed if *z* is also defined.
- **z** (*float*) – The z component
