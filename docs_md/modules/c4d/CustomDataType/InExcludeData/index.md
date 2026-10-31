<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/InExcludeData/index.html -->

# c4d.InExcludeData <a id="c4d-inexcludedata"></a>

## *class* `c4d.InExcludeData` <a id="c4d.InExcludeData"></a>

InExclude data type (*CUSTOMDATATYPE_INEXCLUDE_LIST*) for use with the [`InExcludeCustomGui`](../../../c4d.gui/BaseCustomGui/InExcludeCustomGui/index.md#c4d.gui.InExcludeCustomGui) GUI.

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Flag Configuration**

- [`InExcludeData.GetDefaultFlag()`](#c4d.InExcludeData.GetDefaultFlag): Gets the default flag for new items in the list.
- [`InExcludeData.GetFlagCount()`](#c4d.InExcludeData.GetFlagCount): Gets the number of flags for each object.
- [`InExcludeData.GetFlags()`](#c4d.InExcludeData.GetFlags): Gets the flags for the object at *index* in the list.
- [`InExcludeData.SetDefaultFlag()`](#c4d.InExcludeData.SetDefaultFlag): Sets the default flag for new items in the list.
- [`InExcludeData.SetFlagCount()`](#c4d.InExcludeData.SetFlagCount): Sets the number of flags for each object.
- [`InExcludeData.SetFlags()`](#c4d.InExcludeData.SetFlags): Sets the flags for the object at *index* in the list.

**List Management**

- [`InExcludeData.DeleteObject()`](#c4d.InExcludeData.DeleteObject): Removes the object at *index* from the list.
- [`InExcludeData.GetObjectCount()`](#c4d.InExcludeData.GetObjectCount): Gets the object count.
- [`InExcludeData.InsertObject()`](#c4d.InExcludeData.InsertObject): Inserts an object into the list.
- [`InExcludeData.Reset()`](#c4d.InExcludeData.Reset): Resets the list.

**Magic Methods**

- [`InExcludeData.__init__()`](#c4d.InExcludeData.__init__)

**Object Lookup And Data**

- [`InExcludeData.GetData()`](#c4d.InExcludeData.GetData): Retrieves the data container for the object at index *lIndex* in the list.
- [`InExcludeData.GetObjectIndex()`](#c4d.InExcludeData.GetObjectIndex): Gets the index of *pObject* in the list.
- [`InExcludeData.ObjectFromIndex()`](#c4d.InExcludeData.ObjectFromIndex): Gets the object at *index* in the list.

## Members <a id="members"></a>

### Flag Configuration <a id="c4d.InExcludeData-method-Flag-Configuration"></a>

#### `InExcludeData.GetDefaultFlag(self)` <a id="c4d.InExcludeData.GetDefaultFlag"></a>

Gets the default flag for new items in the list.

*New in version R18.020.*

**Return type:** int

**Returns:** The default flag for new items in the list.

#### `InExcludeData.GetFlagCount(self)` <a id="c4d.InExcludeData.GetFlagCount"></a>

Gets the number of flags for each object.

*New in version R18.020.*

**Return type:** int

**Returns:** The number of flags for each object.

#### `InExcludeData.GetFlags(self, index)` <a id="c4d.InExcludeData.GetFlags"></a>

Gets the flags for the object at *index* in the list.

**Parameters:** **index** (*int*) – Object index. (0 <= *index* < [`GetObjectCount()`](#c4d.InExcludeData.GetObjectCount))

**Return type:** int

**Returns:** A bit field for the selection state of the object.

#### `InExcludeData.SetDefaultFlag(self, defaultFlag)` <a id="c4d.InExcludeData.SetDefaultFlag"></a>

Sets the default flag for new items in the list.

*New in version R18.020.*

**Parameters:** **defaultFlag** (*int*) – The default flag for new items in the list.

#### `InExcludeData.SetFlagCount(self, flagCount)` <a id="c4d.InExcludeData.SetFlagCount"></a>

Sets the number of flags for each object.

*New in version R18.020.*

**Parameters:** **flagCount** (*int*) – The number of flags for each object.

#### `InExcludeData.SetFlags(self, index, flags)` <a id="c4d.InExcludeData.SetFlags"></a>

Sets the flags for the object at *index* in the list.

*New in version R18.020.*

**Parameters:**

- **index** (*int*) – Object index. (0 <= *index* < [`GetObjectCount()`](#c4d.InExcludeData.GetObjectCount))
- **flags** (*int*) – A bit field for the selection state of the object.

### List Management <a id="c4d.InExcludeData-method-List-Management"></a>

#### `InExcludeData.DeleteObject(self, index)` <a id="c4d.InExcludeData.DeleteObject"></a>

Removes the object at *index* from the list.

**Parameters:** **index** (*int*) – Object index. (0 <= *index* < [`GetObjectCount()`](#c4d.InExcludeData.GetObjectCount))

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `InExcludeData.GetObjectCount(self)` <a id="c4d.InExcludeData.GetObjectCount"></a>

Gets the object count.

**Return type:** int

**Returns:** Number of objects in the list.

#### `InExcludeData.InsertObject(self, pObject, lFlags)` <a id="c4d.InExcludeData.InsertObject"></a>

Inserts an object into the list.

**Parameters:**

- **pObject** ([*c4d.BaseList2D*](../../C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – Object to insert.
- **lFlags** (*int*) – A bit field for the initial selection state of *pObject*. Pass **1** to activate the inserted object.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `InExcludeData.Reset(self)` <a id="c4d.InExcludeData.Reset"></a>

Resets the list.

*New in version 24.*

### Magic Methods <a id="c4d.InExcludeData-method-Magic-Methods"></a>

#### `InExcludeData.__init__(self, v=None)` <a id="c4d.InExcludeData.__init__"></a>

**Parameters:** **v** (*Optional*[[*c4d.InExcludeData*](#c4d.InExcludeData)]) – Copy constructor.

### Object Lookup And Data <a id="c4d.InExcludeData-method-Object-Lookup-And-Data"></a>

#### `InExcludeData.GetData(self, lIndex)` <a id="c4d.InExcludeData.GetData"></a>

Retrieves the data container for the object at index *lIndex* in the list.

*New in version 2023.1.0.*

> **Note:** The retrieval of the currently only supported key *c4d.IN_EXCLUDE_DATA_SELECTION* will only work when the *InExcludeCustomGui* which owns the relevant *InExcludeData* has set the description flag *SEND_SELCHNGMSG*. Many native nodes of Cinema 4D which hold *InExcludeData* parameters, for example the Cloner object, do *not* set this flag, and as a user, you cannot change that (at least in Python).

**Parameters:** **lIndex** (*int*) – Object index. (0 <= *index* < [`GetObjectCount()`](#c4d.InExcludeData.GetObjectCount))

**Returns:** The data container. Mostly used with the *c4d.IN_EXCLUDE_DATA_SELECTION* key to detect or define if an element is selected.

**Return type:** [`c4d.BaseContainer`](../../BaseContainer/index.md#c4d.BaseContainer)

#### `InExcludeData.GetObjectIndex(self, doc, pObject)` <a id="c4d.InExcludeData.GetObjectIndex"></a>

Gets the index of *pObject* in the list.

*New in version R18.020.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to evaluate the links in.
- **pObject** ([*c4d.BaseList2D*](../../C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The object to search for.

**Return type:** int

**Returns:** The object index, or **c4d.NOTOK** if it was not found.

#### `InExcludeData.ObjectFromIndex(self, doc, index)` <a id="c4d.InExcludeData.ObjectFromIndex"></a>

Gets the object at *index* in the list.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to evaluate the links in.
- **index** (*int*) – Object index. (0 <= *index* < [`GetObjectCount()`](#c4d.InExcludeData.GetObjectCount))

**Return type:** Optional[[c4d.BaseList2D](../../C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The found object, or **None**.
