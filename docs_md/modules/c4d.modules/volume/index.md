<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/volume/index.html -->

# c4d.modules.volume <a id="c4d-modules-volume"></a>

## *class* `c4d.modules.volume` <a id="c4d.modules.volume"></a>

- [`c4d.modules.volume.VolumeBuilder`](VolumeBuilder/index.md#c4d.modules.volume.VolumeBuilder)
- [`c4d.modules.volume.VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject)

## Overview <a id="overview"></a>

- [`c4d.modules.volume.SendVolumeCommand()`](#c4d.modules.volume.SendVolumeCommand): Sends a volume command.

## Members <a id="members"></a>

### Volume Commands <a id="c4d.modules.volume-function-Volume-Commands"></a>

#### `c4d.modules.volume.SendVolumeCommand(command, list, bc, doc)` <a id="c4d.modules.volume.SendVolumeCommand"></a>

Sends a volume command.

**Parameters:**

- **command** (*int*) –

  The volume command ID:

  |   |   |
  |---|---|
  | *VOLUMECOMMANDTYPE_VOLUMETOMESH* | Converts a [`VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject) into a [`PolygonObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject). |
  | *VOLUMECOMMANDTYPE_MESHTOVOLUME* | Converts a PolygonObject into a SDF [`VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject). |
  | *VOLUMECOMMANDTYPE_VOLUMEBOOLE* | Boolean operation on SDF volume objects. |
  | *VOLUMECOMMANDTYPE_PARTICLESTOVOLUME* | Converts particle objects and TP groups to a SDF [`VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject). |
  | *VOLUMECOMMANDTYPE_SPLINETOVOLUME* | Converts a [`SplineObject`](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/SplineObject/index.md#c4d.SplineObject) to a SDF [`VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject). |
  | *VOLUMECOMMANDTYPE_FILTER* | Filters a float grid [`VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject). |
  | *VOLUMECOMMANDTYPE_SDFFILTER* | Filters a float grid SDF [`VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject). |
  | *VOLUMECOMMANDTYPE_SDFTOFOG* | Converts a SDF Volume to a fog [`VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject). |
  | *VOLUMECOMMANDTYPE_FOGTOSDF* | Converts a fog Volume to a SDF [`VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject). |
  | *VOLUMECOMMANDTYPE_RESAMPLE* | Resamples a [`VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject) to a new grid size. |
  | *VOLUMECOMMANDTYPE_MIX* | Mix operation on several fog [`VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject). |
  | *VOLUMECOMMANDTYPE_FIELDTOVOLUME* | Converts a field to a fog [`VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject). |
  | *VOLUMECOMMANDTYPE_CREATESPHEREVOLUME* | Creates a sphere [`VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject). |
  | *VOLUMECOMMANDTYPE_CREATEPLATONICVOLUME* | Creates a platonic [`VolumeObject`](VolumeObject/index.md#c4d.modules.volume.VolumeObject). |

- **list** (*List*[[*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – The objects to apply the volume command to.

- **bc** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The settings container. See [VOLUMECOMMANDSETTINGS](../../../consts/VOLUMECOMMANDSETTINGS.md).

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

**Return type:** Union[bool, List[[c4d.BaseObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]]

**Returns:**

**True** if the volume command succeeded, otherwise **False**.  
If the volume command succeeds the resulting objects are returned, if any, instead of **True**.
