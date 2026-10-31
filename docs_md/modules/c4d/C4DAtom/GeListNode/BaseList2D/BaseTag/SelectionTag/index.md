<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/SelectionTag/index.html -->

# c4d.SelectionTag <a id="c4d-selectiontag"></a>

## *class* `c4d.SelectionTag` <a id="c4d.SelectionTag"></a>

Represents the Selection tag.  
Holds user defined point, polygon and edge selections.

Parent Class:

- [`c4d.BaseTag`](../index.md#c4d.BaseTag)

## Overview <a id="overview"></a>

**Magic Methods**

- [`SelectionTag.__init__()`](#c4d.SelectionTag.__init__)

**Selection Access**

- [`SelectionTag.GetBaseSelect()`](#c4d.SelectionTag.GetBaseSelect): Gets the selection.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.SelectionTag-method-Magic-Methods"></a>

#### `SelectionTag.__init__(self, type)` <a id="c4d.SelectionTag.__init__"></a>

**Parameters:**

**type** (*int*) –

The type of selection tag:

|   |   |
|---|---|
| *Tpolygonselection* | Polygon selection. |
| *Tpointselection* | Point selection. |
| *Tedgeselection* | Edge selection. The edges are encodes like this: *(4*poly)+edge*, where *edge* goes from *0-3*. |

### Selection Access <a id="c4d.SelectionTag-method-Selection-Access"></a>

#### `SelectionTag.GetBaseSelect(self)` <a id="c4d.SelectionTag.GetBaseSelect"></a>

Gets the selection.

**Return type:** [c4d.BaseSelect](../../../../../BaseSelect/index.md#c4d.BaseSelect)

**Returns:** The selection instance.
