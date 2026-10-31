<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/GeListHead/index.html -->

# c4d.GeListHead <a id="c4d-gelisthead"></a>

## *class* `c4d.GeListHead` <a id="c4d.GeListHead"></a>

Stores a list of [`GeListNode`](../index.md#c4d.GeListNode) objects.

*New in version R19.*

Parent Class:

- [`c4d.GeListNode`](../index.md#c4d.GeListNode)

## Overview <a id="overview"></a>

**Insertion Operations**

- [`GeListHead.Insert()`](#c4d.GeListHead.Insert): Inserts *node* as a child of *parent* or after *prev*.
- [`GeListHead.InsertFirst()`](#c4d.GeListHead.InsertFirst): Inserts *node* as the first element in the list.
- [`GeListHead.InsertLast()`](#c4d.GeListHead.InsertLast): Inserts *node* as the last element in the list.

**Magic Methods**

- [`GeListHead.__init__()`](#c4d.GeListHead.__init__): Creates a list head.

**Structure And Lifecycle**

- [`GeListHead.FlushAll()`](#c4d.GeListHead.FlushAll): Clears the list, removing all nodes.
- [`GeListHead.GetFirst()`](#c4d.GeListHead.GetFirst): Returns the first node in the list.
- [`GeListHead.GetLast()`](#c4d.GeListHead.GetLast): Returns the last node in the list.
- [`GeListHead.GetParent()`](#c4d.GeListHead.GetParent): Returns the parent of the list head.
- [`GeListHead.SetParent()`](#c4d.GeListHead.SetParent): Sets the parent of the list head.

## Members <a id="members"></a>

### Insertion Operations <a id="c4d.GeListHead-method-Insertion-Operations"></a>

#### `GeListHead.Insert(self, node, parent, prev)` <a id="c4d.GeListHead.Insert"></a>

Inserts *node* as a child of *parent* or after *prev*.

**Parameters:**

- **node** ([*c4d.GeListNode*](../index.md#c4d.GeListNode)) – The node to insert.
- **parent** ([*c4d.GeListNode*](../index.md#c4d.GeListNode)) – The node to insert *node* as child.
- **prev** ([*c4d.GeListNode*](../index.md#c4d.GeListNode)) – The node to insert *node* after.

#### `GeListHead.InsertFirst(self, node)` <a id="c4d.GeListHead.InsertFirst"></a>

Inserts *node* as the first element in the list.

**Parameters:** **node** ([*c4d.GeListNode*](../index.md#c4d.GeListNode)) – The node to insert first.

#### `GeListHead.InsertLast(self, node)` <a id="c4d.GeListHead.InsertLast"></a>

Inserts *node* as the last element in the list.

**Parameters:** **node** ([*c4d.GeListNode*](../index.md#c4d.GeListNode)) – The node to insert last.

### Magic Methods <a id="c4d.GeListHead-method-Magic-Methods"></a>

#### `GeListHead.__init__(self, type)` <a id="c4d.GeListHead.__init__"></a>

Creates a list head.

**Parameters:** **type** (*int*) – The id of the object, e.g: (*Ocube*).

### Structure And Lifecycle <a id="c4d.GeListHead-method-Structure-And-Lifecycle"></a>

#### `GeListHead.FlushAll(self)` <a id="c4d.GeListHead.FlushAll"></a>

Clears the list, removing all nodes.

#### `GeListHead.GetFirst(self)` <a id="c4d.GeListHead.GetFirst"></a>

Returns the first node in the list.

**Return type:** [c4d.GeListNode](../index.md#c4d.GeListNode)

**Returns:** The first child node in the list.

#### `GeListHead.GetLast(self)` <a id="c4d.GeListHead.GetLast"></a>

Returns the last node in the list.

**Return type:** [c4d.GeListNode](../index.md#c4d.GeListNode)

**Returns:** The last child node in the list.

#### `GeListHead.GetParent(self)` <a id="c4d.GeListHead.GetParent"></a>

Returns the parent of the list head.  
For the tag list head this would be the object, for the object list head this would be the document etc.

**Return type:** Optional[[c4d.GeListNode](../index.md#c4d.GeListNode)]

**Returns:** The parent, or **None** if the list head has no parent.

#### `GeListHead.SetParent(self, parent)` <a id="c4d.GeListHead.SetParent"></a>

Sets the parent of the list head.  
Usually called directly after the list head is created.

**Parameters:** **parent** ([*c4d.GeListNode*](../index.md#c4d.GeListNode)) – The parent to set.
