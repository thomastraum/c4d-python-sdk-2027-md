<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/sculpting/SculptLayerBase/index.html -->

# c4d.modules.sculpting.SculptLayerBase <a id="c4d-modules-sculpting-sculptlayerbase"></a>

## *class* `c4d.modules.sculpting.SculptLayerBase` <a id="c4d.modules.sculpting.SculptLayerBase"></a>

*New in version R15.037.*

Parent Class:

- [`c4d.BaseObject`](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

Children Classes:

- [`c4d.modules.sculpting.SculptLayer`](../SculptLayer/index.md#c4d.modules.sculpting.SculptLayer)
- [`c4d.modules.sculpting.SculptFolder`](../SculptFolder/index.md#c4d.modules.sculpting.SculptFolder)

## Overview <a id="overview"></a>

**Layer Management**

- [`SculptLayerBase.IsLocked()`](#c4d.modules.sculpting.SculptLayerBase.IsLocked): Check if the layer is currently locked on the sculpt object.
- [`SculptLayerBase.IsVisible()`](#c4d.modules.sculpting.SculptLayerBase.IsVisible): Check if the layer is currently visible on the sculpt object.
- [`SculptLayerBase.Select()`](#c4d.modules.sculpting.SculptLayerBase.Select): Select the layer.
- [`SculptLayerBase.SetLocked()`](#c4d.modules.sculpting.SculptLayerBase.SetLocked): Set the locked status of the layer on the sculpt object.
- [`SculptLayerBase.SetVisible()`](#c4d.modules.sculpting.SculptLayerBase.SetVisible): Set the visibility of this layer on the sculpt object.

**Strength Control**

- [`SculptLayerBase.GetStrength()`](#c4d.modules.sculpting.SculptLayerBase.GetStrength): Get the currents strength of the layer.
- [`SculptLayerBase.SetStrength()`](#c4d.modules.sculpting.SculptLayerBase.SetStrength): Set the strength of the layer on the sculpt object.

## Members <a id="members"></a>

### Layer Management <a id="c4d.modules.sculpting.SculptLayerBase-method-Layer-Management"></a>

#### `SculptLayerBase.IsLocked(self)` <a id="c4d.modules.sculpting.SculptLayerBase.IsLocked"></a>

Check if the layer is currently locked on the sculpt object.

**Return type:** bool

**Returns:** **True** if locked, **False** if unlocked.

#### `SculptLayerBase.IsVisible(self)` <a id="c4d.modules.sculpting.SculptLayerBase.IsVisible"></a>

Check if the layer is currently visible on the sculpt object.

**Return type:** bool

**Returns:** **True** if visible, **False** if invisible.

#### `SculptLayerBase.Select(self)` <a id="c4d.modules.sculpting.SculptLayerBase.Select"></a>

Select the layer.

> **Note:** This will only work if the subdivision level is at the same level as this layer.

**Return type:** bool

**Returns:** **True** if the layer was selected, otherwise **False**.

#### `SculptLayerBase.SetLocked(self, state)` <a id="c4d.modules.sculpting.SculptLayerBase.SetLocked"></a>

Set the locked status of the layer on the sculpt object.

**Parameters:** **state** (*bool*) – The locked state.

#### `SculptLayerBase.SetVisible(self, state)` <a id="c4d.modules.sculpting.SculptLayerBase.SetVisible"></a>

Set the visibility of this layer on the sculpt object.

**Parameters:** **state** (*bool*) – The visibility state.

### Strength Control <a id="c4d.modules.sculpting.SculptLayerBase-method-Strength-Control"></a>

#### `SculptLayerBase.GetStrength(self)` <a id="c4d.modules.sculpting.SculptLayerBase.GetStrength"></a>

Get the currents strength of the layer.

**Return type:** float

**Returns:** The strength value.

#### `SculptLayerBase.SetStrength(self, strength)` <a id="c4d.modules.sculpting.SculptLayerBase.SetStrength"></a>

Set the strength of the layer on the sculpt object.

**Parameters:** **strength** (*float*) – The strength value to set.
