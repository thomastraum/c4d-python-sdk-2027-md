<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/MatAssignData/index.html -->

# c4d.MatAssignData <a id="c4d-matassigndata"></a>

## *class* `c4d.MatAssignData` <a id="c4d.MatAssignData"></a>

Material assignment data type (*CUSTOMDATATYPE_MATASSIGN*).

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Collection Management**

- [`MatAssignData.DeleteObject()`](#c4d.MatAssignData.DeleteObject): Deletes an object from the list.
- [`MatAssignData.GetObjectCount()`](#c4d.MatAssignData.GetObjectCount): Gets the object count.
- [`MatAssignData.InsertObject()`](#c4d.MatAssignData.InsertObject): Inserts an object into the list.
- [`MatAssignData.ObjectFromIndex()`](#c4d.MatAssignData.ObjectFromIndex): Gets an object by index.

**Magic Methods**

- [`MatAssignData.__init__()`](#c4d.MatAssignData.__init__)

## Members <a id="members"></a>

### Collection Management <a id="c4d.MatAssignData-method-Collection-Management"></a>

#### `MatAssignData.DeleteObject(self, lIndex)` <a id="c4d.MatAssignData.DeleteObject"></a>

Deletes an object from the list.

**Parameters:** **lIndex** (*int*) – Object index. (0 <= *lIndex* < [`GetObjectCount()`](#c4d.MatAssignData.GetObjectCount))

**Return type:** int

**Returns:** **True** if the object was deleted, otherwise **False**

#### `MatAssignData.GetObjectCount(self)` <a id="c4d.MatAssignData.GetObjectCount"></a>

Gets the object count.

**Return type:** int

**Returns:** Number of objects in the list.

#### `MatAssignData.InsertObject(self, pObject, lFlags)` <a id="c4d.MatAssignData.InsertObject"></a>

Inserts an object into the list.

**Parameters:**

- **pObject** ([*c4d.BaseList2D*](../../C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – Object to insert.
- **lFlags** (*int*) – A bit field for the initial selection state of *pObject*.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**

#### `MatAssignData.ObjectFromIndex(self, doc, lIndex)` <a id="c4d.MatAssignData.ObjectFromIndex"></a>

Gets an object by index.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – Object document.
- **lIndex** (*int*) – Object index. (0 <= *lIndex* < [`GetObjectCount()`](#c4d.MatAssignData.GetObjectCount))

**Return type:** Optional[[c4d.BaseList2D](../../C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The object or **None**.

### Magic Methods <a id="c4d.MatAssignData-method-Magic-Methods"></a>

#### `MatAssignData.__init__(self, v)` <a id="c4d.MatAssignData.__init__"></a>

**Parameters:** **v** ([*c4d.MatAssignData*](#c4d.MatAssignData)) – Copy constructor.
