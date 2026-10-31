<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/PLAData/index.html -->

# c4d.PLAData <a id="c4d-pladata"></a>

## *class* `c4d.PLAData` <a id="c4d.PLAData"></a>

PLA data type (*CUSTOMDATATYPE_PLA*) for PLA tracks.

*New in version R14.014.*

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Animation Data**

- [`PLAData.GetVariableTags()`](#c4d.PLAData.GetVariableTags): Retrieve the data of a PLA key.

**Magic Methods**

- [`PLAData.__init__()`](#c4d.PLAData.__init__)

## Members <a id="members"></a>

### Animation Data <a id="c4d.PLAData-method-Animation-Data"></a>

#### `PLAData.GetVariableTags(self)` <a id="c4d.PLAData.GetVariableTags"></a>

Retrieve the data of a PLA key.

**Return type:** Optional[Tuple[[c4d.PointTag](../../C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/PointTag/index.md#c4d.PointTag), [c4d.TangentTag](../../C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/TangentTag/index.md#c4d.TangentTag)]]

**Returns:**

A [`PointTag`](../../C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/PointTag/index.md#c4d.PointTag) containing the points of the PLA key and a [`TangentTag`](../../C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/TangentTag/index.md#c4d.TangentTag) with the hermite tangents of each point. Returns **None** in case of an error.

> **Note:** The point tag contains the same number of points as the object, though you should always test for this.

> **Note:** The tangent tag contains the same number of tangents as the object, though you should always test for this.

### Magic Methods <a id="c4d.PLAData-method-Magic-Methods"></a>

#### `PLAData.__init__(self, v)` <a id="c4d.PLAData.__init__"></a>

**Parameters:** **v** ([*c4d.PLAData*](#c4d.PLAData)) – Copy constructor.
