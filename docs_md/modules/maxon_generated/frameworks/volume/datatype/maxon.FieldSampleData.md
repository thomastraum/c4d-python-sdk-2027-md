<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/volume/datatype/maxon.FieldSampleData.html -->

# maxon.FieldSampleData <a id="maxon-fieldsampledata"></a>

## Description <a id="module-maxon.FieldSampleData"></a><a id="description"></a>

An object of this class can store every type of data as long as that type has been registered (see [`maxon.DataType`](../../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)
- [`maxon.Struct`](../../../datatypes/base_core/maxon.Struct.md#module-maxon.Struct)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.FieldSampleData.doc`](maxon.FieldSampleData.doc.md#maxon.FieldSampleData.doc) | ([`c4d.documents.BaseDocument`](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) The document to evaluate the field list for (for field object links). |
| [`maxon.FieldSampleData.extraTransform`](maxon.FieldSampleData.extraTransform.md#maxon.FieldSampleData.extraTransform) | ([`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix)) An extra transformation for the sample positions of the field. |
| [`maxon.FieldSampleData.fieldList`](maxon.FieldSampleData.fieldList.md#maxon.FieldSampleData.fieldList) | ([`c4d.FieldList`](../../../../c4d/CustomDataType/FieldList/index.md#c4d.FieldList)) The field list object to use. |
| [`maxon.FieldSampleData.fieldOwner`](maxon.FieldSampleData.fieldOwner.md#maxon.FieldSampleData.fieldOwner) | ([`c4d.BaseList2D`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) Can be either a field object for direct sampling or needs to be the owner of this field list. |
| [`maxon.FieldSampleData.flags`](maxon.FieldSampleData.flags.md#maxon.FieldSampleData.flags) | (`c4d.FIELDLAYER_FLAG`) Output flags of the field sampling. |
| [`maxon.FieldSampleData.targetRelativeSpace`](maxon.FieldSampleData.targetRelativeSpace.md#maxon.FieldSampleData.targetRelativeSpace) | ([`maxon.Matrix`](../../../datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix)) The target coordinate system for the sampled data. |
