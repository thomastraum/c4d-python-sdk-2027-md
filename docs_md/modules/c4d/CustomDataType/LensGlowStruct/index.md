<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/LensGlowStruct/index.html -->

# c4d.LensGlowStruct <a id="c4d-lensglowstruct"></a>

## *class* `c4d.LensGlowStruct` <a id="c4d.LensGlowStruct"></a>

Lens glow data type (*CUSTOMDATATYPE_LENSGLOW*).

*New in version R17.032.*

**Attributes**

## `c4d.LensGlowStruct.glow` <a id="c4d.LensGlowStruct.glow"></a>

[Read/Write]

A list of dictionaries with the following keys:

- size: float
- sv: float
- col: [`Vector`](../../Vector/index.md#c4d.Vector)
- type: int

## `c4d.LensGlowStruct.streak` <a id="c4d.LensGlowStruct.streak"></a>

[Read/Write]

A list of dictionaries with the following keys:

- random: bool
- randomlen: bool
- star: bool
- cnt: int
- holecnt: int
- size: float
- sv: float
- holewidth: float
- thickness: float
- rot: float
- col: [`Vector`](../../Vector/index.md#c4d.Vector)
- type: int

## `c4d.LensGlowStruct.halo` <a id="c4d.LensGlowStruct.halo"></a>

[Read/Write]

A dictionary with the following keys:

- size: float
- sv: float
- col: [`Vector`](../../Vector/index.md#c4d.Vector)
- type: int

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

- [`LensGlowStruct.__init__()`](#c4d.LensGlowStruct.__init__)

## Members <a id="members"></a>

### Magic Methods <a id="c4d.LensGlowStruct-method-Magic-Methods"></a>

#### `LensGlowStruct.__init__(self, v)` <a id="c4d.LensGlowStruct.__init__"></a>

**Parameters:** **v** ([*c4d.LensGlowStruct*](#c4d.LensGlowStruct)) – Copy constructor.
