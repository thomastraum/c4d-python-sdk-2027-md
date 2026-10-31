<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/hair/HairObject/index.html -->

# c4d.modules.hair.HairObject <a id="c4d-modules-hair-hairobject"></a>

## *class* `c4d.modules.hair.HairObject` <a id="c4d.modules.hair.HairObject"></a>

The hair object.

Parent Class:

- [`c4d.BaseObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

## Overview <a id="overview"></a>

**Guide And Strand Generation**

- [`HairObject.GenerateHair()`](#c4d.modules.hair.HairObject.GenerateHair): Generates hair for the hair object.
- [`HairObject.GetDynamicGuides()`](#c4d.modules.hair.HairObject.GetDynamicGuides): Gets the dynamic guides of this hair object.
- [`HairObject.GetGuides()`](#c4d.modules.hair.HairObject.GetGuides): Gets the guides of this hair object.
- [`HairObject.RemoveGuides()`](#c4d.modules.hair.HairObject.RemoveGuides): Removes the guides of this hair object.
- [`HairObject.SetGuides()`](#c4d.modules.hair.HairObject.SetGuides): Sets guides for this hair object.

**Object Lifecycle**

- [`HairObject.GetRootObject()`](#c4d.modules.hair.HairObject.GetRootObject): Gets the root object and tag!
- [`HairObject.IsLocked()`](#c4d.modules.hair.HairObject.IsLocked): Checks if the hair object is locked.
- [`HairObject.Lock()`](#c4d.modules.hair.HairObject.Lock): Locks the hair object.
- [`HairObject.Unlock()`](#c4d.modules.hair.HairObject.Unlock): Unlocks the hair object.
- [`HairObject.Update()`](#c4d.modules.hair.HairObject.Update): Updates this hair object.

## Members <a id="members"></a>

### Guide And Strand Generation <a id="c4d.modules.hair.HairObject-method-Guide-And-Strand-Generation"></a>

#### `HairObject.GenerateHair(self, flags, count, segments)` <a id="c4d.modules.hair.HairObject.GenerateHair"></a>

Generates hair for the hair object.

**Parameters:**

- **flags** (*int*) –

  The generate flags:

  | Symbol ID | Description |
  |---|---|
  | HAIR_GENERATE_FLAGS_NONE | None |
  | HAIR_GENERATE_FLAGS_NO_MATERIAL | No material. |
  | HAIR_GENERATE_FLAGS_NO_DYNAMICS | No dynamics. |
  | HAIR_GENERATE_FLAGS_NO_TRANSFORM | No transformation. |
  | HAIR_GENERATE_FLAGS_NO_DEFORMERS | No deformers. |

- **count** (*int*) – The hair count.

- **segments** (*int*) – The segments.

#### `HairObject.GetDynamicGuides(self)` <a id="c4d.modules.hair.HairObject.GetDynamicGuides"></a>

Gets the dynamic guides of this hair object.

**Return type:** [c4d.modules.hair.HairGuides](../HairGuides/index.md#c4d.modules.hair.HairGuides)

**Returns:** The dynamic guides.

#### `HairObject.GetGuides(self)` <a id="c4d.modules.hair.HairObject.GetGuides"></a>

Gets the guides of this hair object.

**Return type:** [c4d.modules.hair.HairGuides](../HairGuides/index.md#c4d.modules.hair.HairGuides)

**Returns:** The guides.

#### `HairObject.RemoveGuides(self)` <a id="c4d.modules.hair.HairObject.RemoveGuides"></a>

Removes the guides of this hair object.

#### `HairObject.SetGuides(self, guides, clone)` <a id="c4d.modules.hair.HairObject.SetGuides"></a>

Sets guides for this hair object.

**Parameters:**

- **guides** ([*c4d.modules.hair.HairGuides*](../HairGuides/index.md#c4d.modules.hair.HairGuides)) – Guides to set.
- **clone** (*bool*) – Clone the supplied guides.

### Object Lifecycle <a id="c4d.modules.hair.HairObject-method-Object-Lifecycle"></a>

#### `HairObject.GetRootObject(self)` <a id="c4d.modules.hair.HairObject.GetRootObject"></a>

Gets the root object and tag!

```python
root = ho.GetRootObject()
if not root: return

print(root["pObject"], root["pTag"])
```

**Return type:** Optional[Dict[“pObject”: c4d.BaseObject, “pTag”: c4d.BaseTag]]

**Returns:** The root object and tag or **None**.

#### `HairObject.IsLocked(self)` <a id="c4d.modules.hair.HairObject.IsLocked"></a>

Checks if the hair object is locked.

**Return type:** bool

**Returns:** **True** if the hair object is locked, otherwise **False**.

#### `HairObject.Lock(self, pDoc, pThread, bValidate=True, flags=0)` <a id="c4d.modules.hair.HairObject.Lock"></a>

Locks the hair object.

**Parameters:**

- **pDoc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

- **pThread** ([*c4d.threading.BaseThread*](../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)) – The thread.

- **bValidate** (*bool*) – Validate the lock.

- **flags** (*int*) –

  Lock flags

  | Symbol ID | Description |
  |---|---|
  | HAIR_LOCK_FLAGS_ANIMATING | Animating. |
  | HAIR_LOCK_FLAGS_FULL_UPDATE | Full update. |
  | HAIR_LOCK_FLAGS_NO_TRANSFORM | No transformation. |

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `HairObject.Unlock(self)` <a id="c4d.modules.hair.HairObject.Unlock"></a>

Unlocks the hair object.

#### `HairObject.Update(self)` <a id="c4d.modules.hair.HairObject.Update"></a>

Updates this hair object.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.
