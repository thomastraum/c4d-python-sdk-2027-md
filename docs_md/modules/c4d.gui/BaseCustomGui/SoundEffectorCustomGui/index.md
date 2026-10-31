<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.gui/BaseCustomGui/SoundEffectorCustomGui/index.html -->

# c4d.gui.SoundEffectorCustomGui <a id="c4d-gui-soundeffectorcustomgui"></a>

## *class* `c4d.gui.SoundEffectorCustomGui` <a id="c4d.gui.SoundEffectorCustomGui"></a>

Custom GUI for [`c4d.SoundEffectorData`](../../../c4d/CustomDataType/SoundEffectorData/index.md#c4d.SoundEffectorData) (*CUSTOMGUI_SOUNDEFFECTOR*).

*New in version R19.*

Parent Class:

- [`c4d.gui.BaseCustomGui`](../index.md#c4d.gui.BaseCustomGui)

## Overview <a id="overview"></a>

- [`SoundEffectorCustomGui.GetGUIOwnerOverride()`](#c4d.gui.SoundEffectorCustomGui.GetGUIOwnerOverride): Retrieves the GUI owner.
- [`SoundEffectorCustomGui.SetGUIOwnerOverride()`](#c4d.gui.SoundEffectorCustomGui.SetGUIOwnerOverride): Sets the GUI owner that receives the sound track.

## Members <a id="members"></a>

### GUI Owner Overrides <a id="c4d.gui.SoundEffectorCustomGui-method-GUI-Owner-Overrides"></a>

#### `SoundEffectorCustomGui.GetGUIOwnerOverride(self, doc)` <a id="c4d.gui.SoundEffectorCustomGui.GetGUIOwnerOverride"></a>

Retrieves the GUI owner.

**Parameters:** **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

**Return type:** Optional[[c4d.BaseList2D](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

**Returns:** The GUI owner, or **None** if the function fails.

#### `SoundEffectorCustomGui.SetGUIOwnerOverride(self, bl)` <a id="c4d.gui.SoundEffectorCustomGui.SetGUIOwnerOverride"></a>

Sets the GUI owner that receives the sound track.

**Parameters:** **bl** ([*c4d.BaseList2D*](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The GUI owner.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.
