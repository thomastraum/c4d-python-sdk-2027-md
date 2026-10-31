<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BasePlugin/index.html -->

# c4d.plugins.BasePlugin <a id="c4d-plugins-baseplugin"></a>

## *class* `c4d.plugins.BasePlugin` <a id="c4d.plugins.BasePlugin"></a>

Represents a registered Cinema 4D plugin.

> **Warning:** This type cannot be instantiated.

Parent Class:

- [`c4d.BaseList2D`](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)

## Overview <a id="overview"></a>

- [`BasePlugin.GetFilename()`](#c4d.plugins.BasePlugin.GetFilename): Returns the filename of the plugin.
- [`BasePlugin.GetID()`](#c4d.plugins.BasePlugin.GetID): Gets the plugin ID.
- [`BasePlugin.GetInfo()`](#c4d.plugins.BasePlugin.GetInfo): Flags for the plugin.

## Members <a id="members"></a>

### Plugin Metadata <a id="c4d.plugins.BasePlugin-method-Plugin-Metadata"></a>

#### `BasePlugin.GetFilename(self)` <a id="c4d.plugins.BasePlugin.GetFilename"></a>

Returns the filename of the plugin.

**Return type:** str

**Returns:** The filename of the plugin.

#### `BasePlugin.GetID(self)` <a id="c4d.plugins.BasePlugin.GetID"></a>

Gets the plugin ID.

**Return type:** int

**Returns:** The plugin ID.

#### `BasePlugin.GetInfo(self)` <a id="c4d.plugins.BasePlugin.GetInfo"></a>

Flags for the plugin.

**Return type:** int

**Returns:**

The flags:

|   |   |
|---|---|
| *PLUGINFLAG_HIDE* | Hide the plugin. |
| *PLUGINFLAG_SMALLNODE* | Create a small node. |
| *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
| *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |
