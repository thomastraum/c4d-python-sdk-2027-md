<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/HandleInfo/index.html -->

# c4d.HandleInfo <a id="c4d-handleinfo"></a>

## *class* `c4d.HandleInfo` <a id="c4d.HandleInfo"></a>

**Attributes**

## `c4d.HandleInfo.position` <a id="c4d.HandleInfo.position"></a>

The current handle position.

**Type:** [`Vector`](../Vector/index.md#c4d.Vector)

## `c4d.HandleInfo.direction` <a id="c4d.HandleInfo.direction"></a>

The normal used for the handle travel. For linear handle constraints it is the line on which a handle can travel. For planar and radial constraints it is the normal of the plane/disc. Otherwise it is not needed.

**Type:** [`Vector`](../Vector/index.md#c4d.Vector)

## `c4d.HandleInfo.center` <a id="c4d.HandleInfo.center"></a>

Handle constraint center, for radial and spherical handle constraints.

**Type:** [`Vector`](../Vector/index.md#c4d.Vector)

## `c4d.HandleInfo.radius` <a id="c4d.HandleInfo.radius"></a>

Handle constraint radius, for radial and spherical handle constraints.

**Type:** float

## `c4d.HandleInfo.type` <a id="c4d.HandleInfo.type"></a>

Handle constraint type. One of these types:

|   |   |
|---|---|
| *HANDLECONSTRAINTTYPE_INVALID* | Invalid handle constraint type, used to temporarily ignore handles (e.g. in the Camera Object with the Front/Back DOF handles). |
| *HANDLECONSTRAINTTYPE_LINEAR* | Linear handle constraint. |
| *HANDLECONSTRAINTTYPE_PLANAR* | Planar handle constraint. |
| *HANDLECONSTRAINTTYPE_FREE* | No constraint. |
| *HANDLECONSTRAINTTYPE_RADIAL* | Radial handle constraint. |
| *HANDLECONSTRAINTTYPE_SPHERICAL* | Spherical handle constraint. |

## Overview <a id="overview"></a>

**Magic Methods**

- [`HandleInfo.__init__()`](#c4d.HandleInfo.__init__): Constructor.

**Position Calculation**

- [`HandleInfo.CalculateNewPosition()`](#c4d.HandleInfo.CalculateNewPosition): Calculates a handle position for a given mouse position.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.HandleInfo-method-Magic-Methods"></a>

#### `HandleInfo.__init__(self)` <a id="c4d.HandleInfo.__init__"></a>

Constructor.

### Position Calculation <a id="c4d.HandleInfo-method-Position-Calculation"></a>

#### `HandleInfo.CalculateNewPosition(self, bd, mg, mouse_pos)` <a id="c4d.HandleInfo.CalculateNewPosition"></a>

Calculates a handle position for a given mouse position.

**Parameters:**

- **bd** ([*c4d.BaseDraw*](../C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The active viewport.
- **mg** ([*c4d.Matrix*](../Matrix/index.md#c4d.Matrix)) – The global matrix of the handle’s parent object.
- **mouse_pos** ([*c4d.Vector*](../Vector/index.md#c4d.Vector)) – The mouse coordinates for which to calculate the handle position.
