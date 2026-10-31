<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/AliasTrans/index.html -->

# c4d.AliasTrans <a id="c4d-aliastrans"></a>

## *class* `c4d.AliasTrans` <a id="c4d.AliasTrans"></a>

The alias translator takes care about reconnecting BaseLink links when cloning, copying, reading or writing objects.

*New in version R17.032.*

Normally Cinema 4D provides an alias translator when needed, for example in `NodeData.CopyTo()`. However, to copy objects manually use:

```python
trans = c4d.AliasTrans()
if not trans or not trans.Init(doc):
    return False

clone = op.GetClone(c4d.COPYFLAGS_NONE, trans)
if not clone:
    return False

trans.Translate(True)
```

## Overview <a id="overview"></a>

**Initialization**

- [`AliasTrans.Init()`](#c4d.AliasTrans.Init): Initializes the alias translator in the specified document *doc*.

**Link Translation**

- [`AliasTrans.Translate()`](#c4d.AliasTrans.Translate): Translates the links in all objects that the translator has come across.

## Members <a id="members"></a>

### Initialization <a id="c4d.AliasTrans-method-Initialization"></a>

#### `AliasTrans.Init(self, doc)` <a id="c4d.AliasTrans.Init"></a>

Initializes the alias translator in the specified document *doc*.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

**Return type:** bool

**Returns:** **True** if the alias translator was initialized, otherwise **False**.

### Link Translation <a id="c4d.AliasTrans-method-Link-Translation"></a>

#### `AliasTrans.Translate(self, connect_oldgoals)` <a id="c4d.AliasTrans.Translate"></a>

Translates the links in all objects that the translator has come across.

**Parameters:**

**connect_oldgoals** (*bool*) –

**True** to connect old goals.  
For example: Take a cube with an instance linked to this cube, select both and duplicate them in one action.  
The new cube is linked to the new instance if *connect_oldgoals* is **True**.  
If it is **False** the new instance is linked to the old cube.
