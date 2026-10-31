<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/hair/HairLibrary/index.html -->

# c4d.modules.hair.HairLibrary <a id="c4d-modules-hair-hairlibrary"></a>

## *class* `c4d.modules.hair.HairLibrary` <a id="c4d.modules.hair.HairLibrary"></a>

Hair library class.

## Overview <a id="overview"></a>

**Color And Coordinate Utilities**

- [`HairLibrary.BlendColors()`](#c4d.modules.hair.HairLibrary.BlendColors): Blend colors.
- [`HairLibrary.GetPolyPointST()`](#c4d.modules.hair.HairLibrary.GetPolyPointST): Calculate the *s* and *t* coordinates of the point *p* in the polygon described by *pa*, *pb*, *pc* and *pd*.
- [`HairLibrary.MixST()`](#c4d.modules.hair.HairLibrary.MixST): Mix by the *s* and *t* coordinates among *pa*, *pb*, *pc* and *pd*.

**State And Version**

- [`HairLibrary.GetHairVersion()`](#c4d.modules.hair.HairLibrary.GetHairVersion): Get the hair version.
- [`HairLibrary.GetMode()`](#c4d.modules.hair.HairLibrary.GetMode): Get hair mode.
- [`HairLibrary.SetMode()`](#c4d.modules.hair.HairLibrary.SetMode): Set hair mode.

## Members <a id="members"></a>

### Color And Coordinate Utilities <a id="c4d.modules.hair.HairLibrary-method-Color-And-Coordinate-Utilities"></a>

#### `HairLibrary.BlendColors(self, mode, colA, colB)` <a id="c4d.modules.hair.HairLibrary.BlendColors"></a>

Blend colors.

**Parameters:**

- **mode** (*int*) – Blend mode. (See *mhairmaterial.h* for modes, e.g. *HAIRMATERIAL_BLENDMODE_AVERAGE*.)
- **colA** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – First color.
- **colB** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – Second color.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** Resulting color.

#### `HairLibrary.GetPolyPointST(self, p, pa, pb, pc, pd, bQuad)` <a id="c4d.modules.hair.HairLibrary.GetPolyPointST"></a>

Calculate the *s* and *t* coordinates of the point *p* in the polygon described by *pa*, *pb*, *pc* and *pd*.

**Parameters:**

- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – Point to get the coordinates for.
- **pa** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – First point value.
- **pb** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – Second point value.
- **pc** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – Third point value.
- **pd** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – Fourth point value.
- **bQuad** (*bool*) – **True** means quadrangle, **False** means triangle.

**Return type:** Tuple[float, float]

**Returns:** The *s* and *t* coordinates.

#### `HairLibrary.MixST(self, s, t, pa, pb, pc, pd, bQuad)` <a id="c4d.modules.hair.HairLibrary.MixST"></a>

Mix by the *s* and *t* coordinates among *pa*, *pb*, *pc* and *pd*.

**Parameters:**

- **s** (*float*) – S coordinate.
- **t** (*float*) – T coordinate.
- **pa** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – First point value.
- **pb** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – Second point value.
- **pc** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – Third point value.
- **pd** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – Fourth point value.
- **bQuad** (*bool*) – **True** means quadrangle, **False** means triangle.

**Return type:** Tuple[float, float]

**Returns:** The *s* and *t* coordinates.

### State And Version <a id="c4d.modules.hair.HairLibrary-method-State-And-Version"></a>

#### `HairLibrary.GetHairVersion(self)` <a id="c4d.modules.hair.HairLibrary.GetHairVersion"></a>

Get the hair version.

**Return type:** int

**Returns:** Hair version number.

#### `HairLibrary.GetMode(self, doc)` <a id="c4d.modules.hair.HairLibrary.GetMode"></a>

Get hair mode.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – Document.

**Return type:** int

**Returns:**

Hair mode:

|   |   |
|---|---|
| *HAIR_MODE_LOCKED* | Locked mode |
| *HAIR_MODE_HIDDEN* | Hidden mode. |
| *HAIR_MODE_TIPS* | Tips mode. |
| *HAIR_MODE_POINTS* | Points mode. |
| *HAIR_MODE_GUIDES* | Guides mode. |
| *HAIR_MODE_ROOTS* | Roots mode. |
| *HAIR_MODE_VERTEX* | Vertex mode. |

#### `HairLibrary.SetMode(self, doc, mode)` <a id="c4d.modules.hair.HairLibrary.SetMode"></a>

Set hair mode.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – Document.

- **mode** (*int*) –

  New hair mode:

  |   |   |
  |---|---|
  | *HAIR_MODE_LOCKED* | Locked mode |
  | *HAIR_MODE_HIDDEN* | Hidden mode. |
  | *HAIR_MODE_TIPS* | Tips mode. |
  | *HAIR_MODE_POINTS* | Points mode. |
  | *HAIR_MODE_GUIDES* | Guides mode. |
  | *HAIR_MODE_ROOTS* | Roots mode. |
  | *HAIR_MODE_VERTEX* | Vertex mode. |
