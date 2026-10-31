<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/misc/maxon.GradientKnot.html -->

# maxon.GradientKnot <a id="maxon-gradientknot"></a>

## Description <a id="module-maxon.GradientKnot"></a><a id="description"></a>

An object of this class can store every type of data as long as that type has been registered (see [`maxon.DataType`](../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)
- [`maxon.Struct`](../../datatypes/base_core/maxon.Struct.md#module-maxon.Struct)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.GradientKnot.bias`](maxon.GradientKnot.bias.md#maxon.GradientKnot.bias) | (float) Bias. |
| [`maxon.GradientKnot.brightness`](maxon.GradientKnot.brightness.md#maxon.GradientKnot.brightness) | (float) Brightness. |
| [`maxon.GradientKnot.col`](maxon.GradientKnot.col.md#maxon.GradientKnot.col) | ([`maxon.Color`](../../datatypes/vec_col_mat/maxon.Color.md#module-maxon.Color)) Color. |
| [`maxon.GradientKnot.index`](maxon.GradientKnot.index.md#maxon.GradientKnot.index) | (Int32) Knot ID in GradientInterface, knot index in GradientRenderDataInterface. |
| [`maxon.GradientKnot.interpolation`](maxon.GradientKnot.interpolation.md#maxon.GradientKnot.interpolation) | (`maxon.GRADIENT_INTERPOLATION_TYPE`) |
| [`maxon.GradientKnot.pos`](maxon.GradientKnot.pos.md#maxon.GradientKnot.pos) | (float) Position. |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`__init__`](#maxon.GradientKnot.__init__)([otherOrColor, brightness, pos, …]) | Initializes the appropriate C++ Data object and store it within the _data member. |
| [`__str__`](#maxon.GradientKnot.__str__)() | Returns the string representation of a data. |

## Methods Definition <a id="methods-definition"></a>

### `GradientKnot.__init__(otherOrColor=maxon.Color64 object at 0x12e9b02e8a0 with the data: R:1.0, G:1.0, B:1.0, brightness=1.0, pos=0.0, bias=0.5, index=0, interpolation=2)` <a id="maxon.GradientKnot.__init__"></a>

Initializes the appropriate C++ Data object and store it within the _data member.

If C is a Data then _data store a copy the C++ Data is done and stored.  
If C is a C++ Data then _data store a reference of the C++ Data.  
If C is not defined the C++ data is created and stored in the _data member.

**Parameters:** **C** (Optional[[`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)]) – Input data from which the Data should be created.

### `GradientKnot.__str__()` <a id="maxon.GradientKnot.__str__"></a>

Returns the string representation of a data.

**Return type:** str
