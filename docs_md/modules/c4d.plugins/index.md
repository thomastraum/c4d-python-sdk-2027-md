<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/index.html -->

# c4d.plugins <a id="c4d-plugins"></a>

## *class* `c4d.plugins` <a id="c4d.plugins"></a>

Provides classes to implement and functions to register plugins.

> **Note:**
>
> - See [Implementing Plugins](../../manuals/manual_implementing_plugins.md) for information how to implement a plugin and set up a plugin project in a folder.
> - The ID passed to plugin registration functions has to be globally unique. Attempting to reuse an identifier will cause only one of the plugins that tries to claim that identifier to be successfully loaded on the startup of Cinema 4D. Please make sure to *always* obtain identifiers for plugins from the Plugin ID generator on [Plugin Café](https://plugincafe.maxon.net/c4dpluginid_cp) to avoid identifier collisions. You must create an account with Plugin Café in order to use the generator.

- [`c4d.plugins.BaseData`](BaseData/index.md#c4d.plugins.BaseData)

  - [`c4d.plugins.BitmapLoaderData`](BaseData/BitmapLoaderData/index.md#c4d.plugins.BitmapLoaderData)

  - [`c4d.plugins.BitmapSaverData`](BaseData/BitmapSaverData/index.md#c4d.plugins.BitmapSaverData)

  - [`c4d.plugins.CommandData`](BaseData/CommandData/index.md#c4d.plugins.CommandData)

  - [`c4d.plugins.MessageData`](BaseData/MessageData/index.md#c4d.plugins.MessageData)

  - [`c4d.plugins.ToolData`](BaseData/ToolData/index.md#c4d.plugins.ToolData)

  - [`c4d.plugins.SculptBrushToolData`](BaseData/SculptBrushToolData/index.md#c4d.plugins.SculptBrushToolData)

  - [`c4d.plugins.NodeData`](BaseData/NodeData/index.md#c4d.plugins.NodeData)

    - [`c4d.plugins.TagData`](BaseData/NodeData/TagData/index.md#c4d.plugins.TagData)
    - [`c4d.plugins.ObjectData`](BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData)
    - [`c4d.plugins.ShaderData`](BaseData/NodeData/ShaderData/index.md#c4d.plugins.ShaderData)
    - [`c4d.plugins.SceneLoaderData`](BaseData/NodeData/SceneLoaderData/index.md#c4d.plugins.SceneLoaderData)
    - [`c4d.plugins.SceneSaverData`](BaseData/NodeData/SceneSaverData/index.md#c4d.plugins.SceneSaverData)
    - [`c4d.plugins.PreferenceData`](BaseData/NodeData/PreferenceData/index.md#c4d.plugins.PreferenceData)

- [`c4d.plugins.BaseDrawHelp`](BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp)

- [`c4d.plugins.BasePlugin`](BasePlugin/index.md#c4d.plugins.BasePlugin)

- [`c4d.plugins.GeResource`](GeResource/index.md#c4d.plugins.GeResource)

- [`c4d.plugins.HierarchyHelp`](HierarchyHelp/index.md#c4d.plugins.HierarchyHelp)

- [`c4d.plugins.PriorityList`](PriorityList/index.md#c4d.plugins.PriorityList)

## Overview <a id="overview"></a>

**Plugin Data Functions**

- [`c4d.plugins.GetWorldPluginData()`](#c4d.plugins.GetWorldPluginData): Retrieves a container stored with `SetWorldPluginData()` from the Cinema 4D preferences.
- [`c4d.plugins.ReadPluginInfo()`](#c4d.plugins.ReadPluginInfo): Read private serial information for a plugin.
- [`c4d.plugins.ReadRegInfo()`](#c4d.plugins.ReadRegInfo): Reads user-specific data (e.g.
- [`c4d.plugins.SetWorldPluginData()`](#c4d.plugins.SetWorldPluginData): Stores a container in the Cinema 4D preferences.
- [`c4d.plugins.WritePluginInfo()`](#c4d.plugins.WritePluginInfo): Write private serial information for a plugin.
- [`c4d.plugins.WriteRegInfo()`](#c4d.plugins.WriteRegInfo): Writes user-specific data (e.g.

**Plugin Reload Functions**

- [`c4d.plugins.ReloadAllPythonPlugins()`](#c4d.plugins.ReloadAllPythonPlugins): Reloads all Python plugin files, i.e., recompiles and executes all of them again.
- [`c4d.plugins.ReloadDocumentAfterReload()`](#c4d.plugins.ReloadDocumentAfterReload): Reloads documents after Python plugins have been reloaded, so that the nodes in them use the classes of the reloaded plugins.
- [`c4d.plugins.ReloadPythonPlugin()`](#c4d.plugins.ReloadPythonPlugin): Reloads a single Python plugin file, i.e., recompiles and executes the file again, so that its registrations and classes are replaced by the ones of the changed file.

**Plugin Utilities**

- [`c4d.plugins.GeLoadString()`](#c4d.plugins.GeLoadString): Load a string and replace the first ‘#’ with the placeholder string.
- [`c4d.plugins.GetToolData()`](#c4d.plugins.GetToolData): Gets the tool data container for the tool with ID *pluginid*.

**Register Functions**

- [`c4d.plugins.RegisterBitmapLoaderPlugin()`](#c4d.plugins.RegisterBitmapLoaderPlugin): Registers a [`BitmapLoaderData`](BaseData/BitmapLoaderData/index.md#c4d.plugins.BitmapLoaderData) plugin.
- [`c4d.plugins.RegisterBitmapSaverPlugin()`](#c4d.plugins.RegisterBitmapSaverPlugin): Registers a [`BitmapSaverData`](BaseData/BitmapSaverData/index.md#c4d.plugins.BitmapSaverData) plugin.
- [`c4d.plugins.RegisterCommandPlugin()`](#c4d.plugins.RegisterCommandPlugin): Registers a [`CommandData`](BaseData/CommandData/index.md#c4d.plugins.CommandData) plugin.
- [`c4d.plugins.RegisterDescription()`](#c4d.plugins.RegisterDescription): Registers a description for a plugin ID.
- [`c4d.plugins.RegisterHiddenToken()`](#c4d.plugins.RegisterHiddenToken): This function registers a hidden token that is not displayed in Render Settings.
- [`c4d.plugins.RegisterManagerInformation()`](#c4d.plugins.RegisterManagerInformation): Registers manager information for use when registering shortcuts with [`AddShortcut()`](../c4d.gui/index.md#c4d.gui.AddShortcut).
- [`c4d.plugins.RegisterMessagePlugin()`](#c4d.plugins.RegisterMessagePlugin): Registers a [`MessageData`](BaseData/MessageData/index.md#c4d.plugins.MessageData) plugin.
- [`c4d.plugins.RegisterNodePlugin()`](#c4d.plugins.RegisterNodePlugin): Registers a [`NodeData`](BaseData/NodeData/index.md#c4d.plugins.NodeData) plugin.
- [`c4d.plugins.RegisterObjectPlugin()`](#c4d.plugins.RegisterObjectPlugin): Registers an [`ObjectData`](BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData) plugin.
- [`c4d.plugins.RegisterPluginHelpCallback()`](#c4d.plugins.RegisterPluginHelpCallback): Registers a callback for plugin help support.
- [`c4d.plugins.RegisterPreferencePlugin()`](#c4d.plugins.RegisterPreferencePlugin): Registers a new preference in the Cinema 4D preferences dialog.
- [`c4d.plugins.RegisterSceneLoaderPlugin()`](#c4d.plugins.RegisterSceneLoaderPlugin): Registers a [`SceneLoaderData`](BaseData/NodeData/SceneLoaderData/index.md#c4d.plugins.SceneLoaderData) plugin.
- [`c4d.plugins.RegisterSceneSaverPlugin()`](#c4d.plugins.RegisterSceneSaverPlugin): Registers a [`SceneSaverData`](BaseData/NodeData/SceneSaverData/index.md#c4d.plugins.SceneSaverData) plugin.
- [`c4d.plugins.RegisterSculptBrushPlugin()`](#c4d.plugins.RegisterSculptBrushPlugin): Registers a [`SculptBrushToolData`](BaseData/SculptBrushToolData/index.md#c4d.plugins.SculptBrushToolData).
- [`c4d.plugins.RegisterShaderPlugin()`](#c4d.plugins.RegisterShaderPlugin): Registers a [`ShaderData`](BaseData/NodeData/ShaderData/index.md#c4d.plugins.ShaderData) plugin.
- [`c4d.plugins.RegisterTagPlugin()`](#c4d.plugins.RegisterTagPlugin): Registers a TagData plugin:
- [`c4d.plugins.RegisterToken()`](#c4d.plugins.RegisterToken): Registers a new Token that can be used in a render filename, the token is displayed in the render setting and can be selected by the user.
- [`c4d.plugins.RegisterToolPlugin()`](#c4d.plugins.RegisterToolPlugin): Registers a [`ToolData`](BaseData/ToolData/index.md#c4d.plugins.ToolData) plugin.
- [`c4d.plugins.Update()`](#c4d.plugins.Update): Subscribes the plugin that is currently being registered to be updated after the registration process.

**Registered Plugins Functions**

- [`c4d.plugins.FilterPluginList()`](#c4d.plugins.FilterPluginList): Browses recursively through the plugin list looking for plugin of the specified *type*. For example, to find all bitmap savers you can write:
- [`c4d.plugins.FindPlugin()`](#c4d.plugins.FindPlugin): Returns the [`BasePlugin`](BasePlugin/index.md#c4d.plugins.BasePlugin) found by id.
- [`c4d.plugins.GetFirstPlugin()`](#c4d.plugins.GetFirstPlugin): Returns the first plugin of Cinema 4D.

## Members <a id="members"></a>

### Plugin Data Functions <a id="c4d.plugins-function-Plugin-Data-Functions"></a>

#### `c4d.plugins.GetWorldPluginData(id)` <a id="c4d.plugins.GetWorldPluginData"></a>

Retrieves a container stored with [`SetWorldPluginData()`](#c4d.plugins.SetWorldPluginData) from the Cinema 4D preferences. This can be used by any plugin to store preferences.

**Parameters:** **id** (*int*) – The plugin ID that the container should be associated with.

**Return type:** [c4d.BaseContainer](../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The retrieved container

#### `c4d.plugins.ReadPluginInfo(pluginid, size)` <a id="c4d.plugins.ReadPluginInfo"></a>

Read private serial information for a plugin. Cinema 4D will store this data encrypted.

**Parameters:**

- **pluginid** (*int*) – The plugin ID the data is associated with.
- **size** (*int*) – The buffer size

**Return type:** bytes

**Returns:** The data buffer.

#### `c4d.plugins.ReadRegInfo(pluginid, size)` <a id="c4d.plugins.ReadRegInfo"></a>

Reads user-specific data (e.g. login data for a user account).

> **Note:** Use this method instead of [`WritePluginInfo()`](#c4d.plugins.WritePluginInfo) in a license server environment.

**Parameters:**

- **pluginid** (*int*) – The plugin ID the data is associated with.
- **size** (*int*) – The buffer size

**Return type:** bytes

**Returns:** The data buffer.

#### `c4d.plugins.SetWorldPluginData(id, bc, add=True)` <a id="c4d.plugins.SetWorldPluginData"></a>

Stores a container in the Cinema 4D preferences. Can be used by any plugin to store preferences.

**Parameters:**

- **id** (*int*) – The plugin ID that the container should be associated with. Please use a unique ID from [PluginCafe](http://www.plugincafe.com).
- **bc** ([*c4d.BaseContainer*](../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The container to store.
- **add** (*bool*) – If this is **True** the container values are merged with the ones currently stored for this ID. Otherwise the previous values are lost.

**Return type:** bool

**Returns:** **True** if the container was stored, otherwise **False**.

#### `c4d.plugins.WritePluginInfo(pluginid, buffer)` <a id="c4d.plugins.WritePluginInfo"></a>

Write private serial information for a plugin. Cinema 4D will store this data encrypted.

**Parameters:**

- **pluginid** (*int*) – The plugin ID the data is associated with.
- **buffer** (*bytes*) – The data buffer.

#### `c4d.plugins.WriteRegInfo(pluginid, buffer)` <a id="c4d.plugins.WriteRegInfo"></a>

Writes user-specific data (e.g. login data for a user account).

> **Note:** Use this method instead of [`WritePluginInfo()`](#c4d.plugins.WritePluginInfo) in a license server environment.

**Parameters:**

- **pluginid** (*int*) – The plugin ID the data is associated with.
- **buffer** (*bytes*) – The data buffer.

### Plugin Reload Functions <a id="c4d.plugins-function-Plugin-Reload-Functions"></a>

#### `c4d.plugins.ReloadAllPythonPlugins()` <a id="c4d.plugins.ReloadAllPythonPlugins"></a>

Reloads all Python plugin files, i.e., recompiles and executes all of them again. This is what the *Reload Python Plugins* command of Cinema 4D does.

The function sends the message *C4DPL_RELOADPYTHONPLUGINS* to all plugins (see [Plugin Messages](../../manuals/manual_implementing_plugins.md#plugin-messages)), stops the animation of the active document and all running threads, reloads the plugin files one after another, and then reloads the active document, see [`ReloadDocumentAfterReload()`](#c4d.plugins.ReloadDocumentAfterReload). Modules that are imported by the plugins are not reloaded.

> **Note:** The function takes no arguments. Other than [`ReloadPythonPlugin()`](#c4d.plugins.ReloadPythonPlugin), it cannot be told to skip or to extend the document reload.

**Return type:** bool

**Returns:** Always **True**, errors during the reload of a plugin file are not reported.

#### `c4d.plugins.ReloadDocumentAfterReload(onlyActiveDocument=True)` <a id="c4d.plugins.ReloadDocumentAfterReload"></a>

Reloads documents after Python plugins have been reloaded, so that the nodes in them use the classes of the reloaded plugins.

Reloading a plugin replaces all of its plugin types. Nodes that already exist in a scene still reference the old types. This function clones the documents, so that each node is re-instantiated with the new type, and then requests an update of Cinema 4D with [`c4d.EventAdd()`](../c4d/index.md#c4d.EventAdd). Documents that are in the render queue are intentionally not updated.

This function is called by [`ReloadPythonPlugin()`](#c4d.plugins.ReloadPythonPlugin) when its argument *reloadDocumentAfterReload* is **True**. Call it manually after reloading with *reloadDocumentAfterReload* set to **False**, e.g., after reloading several plugins.

*New in version R14.*

> **Warning:** The animation of the active document is stopped when only the active document is reloaded.

**Parameters:** **onlyActiveDocument** (*bool*) – If **True**, only the active document is reloaded and its animation is stopped, otherwise all open documents are reloaded.

#### `c4d.plugins.ReloadPythonPlugin(path, reloadDocumentAfterReload=True, reloadOnlyActiveDocument=True)` <a id="c4d.plugins.ReloadPythonPlugin"></a>

Reloads a single Python plugin file, i.e., recompiles and executes the file again, so that its registrations and classes are replaced by the ones of the changed file.

The function sends the message *C4DPL_RELOADPYTHONPLUGINS* to all plugins (see [Plugin Messages](../../manuals/manual_implementing_plugins.md#plugin-messages)), stops all running threads, and then reloads the file. The *Reload* command of the Plugin Manager does this for each selected plugin. Use [`ReloadAllPythonPlugins()`](#c4d.plugins.ReloadAllPythonPlugins) to reload all plugins. Modules that are imported by the plugin are not reloaded.

For example, the script that the *Create Reload Script* command of the Plugin Manager copies to the clipboard for the selected plugins looks like this:

```python
import c4d
from c4d import plugins

plugins.ReloadPythonPlugin(path=r"C:\plugins\myplugin\myplugin.pyp", reloadDocumentAfterReload=False, reloadOnlyActiveDocument=False)
plugins.ReloadDocumentAfterReload(True) # Internal update
```

> **Note:** The plugin file must have been loaded by Cinema 4D at startup. A file that is not known to Cinema 4D, e.g., a new plugin that has been added after the startup, cannot be reloaded.

> **Warning:** The result of the reload itself is not reported. The function only returns **True** when the plugin file has been found.

**Parameters:**

- **path** (*str*) – The path of the plugin file to reload. It must end with *.pyp* or *.pypv*, and must be equal to the path under which Cinema 4D has loaded the plugin. Use a raw string for paths on Windows.
- **reloadDocumentAfterReload** (*bool*) – If **True**, the documents are reloaded after the plugin has been reloaded, see [`ReloadDocumentAfterReload()`](#c4d.plugins.ReloadDocumentAfterReload). This is necessary for nodes of the reloaded plugin that are already in a scene to use the new classes. If **False**, the caller must do the update, e.g., with a following call to [`ReloadDocumentAfterReload()`](#c4d.plugins.ReloadDocumentAfterReload), which allows to reload multiple plugins with a single update.
- **reloadOnlyActiveDocument** (*bool*) – Only has an effect when *reloadDocumentAfterReload* is **True**. If **True**, only the active document is reloaded, otherwise all open documents.

**Return type:** bool

**Returns:** **True** if the plugin file has been found and reloaded.

**Raises:** **LookupError** – If *path* does not end with *.pyp* or *.pypv*, or if no loaded plugin file matches *path*.

### Plugin Utilities <a id="c4d.plugins-function-Plugin-Utilities"></a>

#### `c4d.plugins.GeLoadString(id, p1='', p2='', p3='', p4='')` <a id="c4d.plugins.GeLoadString"></a>

Load a string and replace the first ‘#’ with the placeholder string.

In Cinema 4D there is a convention that in strings ‘#’ is a placeholder for dynamic parts (this allows you to translate a whole sentence as sentence structure and word placement may be reverted in other language).

> **Warning:** To use this function, *__res__* must be defined in your global scope.

For example:

> If the string is named: “loading of file ‘#’ failed” then you can pass the actual filename (as string) as *p1* and you’ll get the desired result.

**Parameters:**

- **id** (*int*) – The ID of the string to get.
- **p1** (*Optional*[*str*]) – The string to insert into the first placeholder.
- **p2** (*Optional*[*str*]) – The string to insert into the second placeholder.
- **p3** (*Optional*[*str*]) – The string to insert into the third placeholder.
- **p4** (*Optional*[*str*]) – The string to insert into the fourth placeholder.

**Return type:** str

**Returns:** The completed string.

#### `c4d.plugins.GetToolData(doc, pluginid)` <a id="c4d.plugins.GetToolData"></a>

Gets the tool data container for the tool with ID *pluginid*.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to get the settings for.
- **pluginid** (*int*) – The plugin ID of the tool.

**Return type:** [c4d.BaseContainer](../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** Tool data container.

### Register Functions <a id="c4d.plugins-function-Register-Functions"></a>

#### `c4d.plugins.RegisterBitmapLoaderPlugin(id, str, info, dat)` <a id="c4d.plugins.RegisterBitmapLoaderPlugin"></a>

Registers a [`BitmapLoaderData`](BaseData/BitmapLoaderData/index.md#c4d.plugins.BitmapLoaderData) plugin.

**Parameters:**

- **id** (*int*) – A unique plugin ID. You **must** obtain this from [PluginCafe.com](http://plugincafe.com/)

- **str** (*str*) –

  The name of the plugin.

  > **Note:**
  >
  > If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.  
  > Lower numbers are displayed before higher numbers. If you make the name “–” it will show up as a menu separator.

- **info** (*int*) –

  The settings for the plugin. Possible flags are:

  - Plugin General Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_HIDE* | Hide the plugin. |
  | *PLUGINFLAG_SMALLNODE* | Create a small node. |
  | *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
  | *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |

  - Bitmap Loader Plugin Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_BITMAPLOADER_MOVIE* | Support movies. |

- **dat** ([*c4d.plugins.BitmapLoaderData*](BaseData/BitmapLoaderData/index.md#c4d.plugins.BitmapLoaderData)) – A data instance for the plugin.

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.RegisterBitmapSaverPlugin(id, str, info, dat, suffix)` <a id="c4d.plugins.RegisterBitmapSaverPlugin"></a>

Registers a [`BitmapSaverData`](BaseData/BitmapSaverData/index.md#c4d.plugins.BitmapSaverData) plugin.

**Parameters:**

- **id** (*int*) –

  A unique plugin ID. You **must** obtain this from [PluginCafe.com](http://plugincafe.com/)

- **str** (*str*) –

  The name of the plugin.

  > **Note:**
  >
  > If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.  
  > Lower numbers are displayed before higher numbers. If you make the name “–” it will show up as a menu separator.

- **info** (*int*) –

  The settings for the plugin.

  - Plugin General Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_HIDE* | Hide the plugin. |
  | *PLUGINFLAG_SMALLNODE* | Create a small node. |
  | *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
  | *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |

  - Bitmap Saver Plugin Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_BITMAPSAVER_SUPPORT_8BIT* | Support 8-bit bitmaps. |
  | *PLUGINFLAG_BITMAPSAVER_SUPPORT_16BIT* | Support 16-bit bitmaps. |
  | *PLUGINFLAG_BITMAPSAVER_SUPPORT_32BIT* | Support 32-bit bitmaps. |
  | *PLUGINFLAG_BITMAPSAVER_SUPPORT_8BIT_LAYERS* | Support 8-bit layered bitmaps |
  | *PLUGINFLAG_BITMAPSAVER_SUPPORT_16BIT_LAYERS* | Support 16-bit layered bitmaps. |
  | *PLUGINFLAG_BITMAPSAVER_SUPPORT_32BIT_LAYERS* | Support 32-bit layered bitmaps. |
  | *PLUGINFLAG_BITMAPSAVER_MOVIE* | Support movies. |
  | *PLUGINFLAG_BITMAPSAVER_ALLOWOPTIONS* | Flag for Cinema 4D to identify the savers that have “Edit…” enabled. |
  | *PLUGINFLAG_BITMAPSAVER_FORCESUFFIX* | Ensure that saved files always get the specified suffix. |
  | *PLUGINFLAG_BITMAPSAVER_SUPPORT_SOUND* | *New in version R19:* Ensure that saved files always get the specified suffix. |

- **dat** ([*c4d.plugins.BitmapSaverData*](BaseData/BitmapSaverData/index.md#c4d.plugins.BitmapSaverData)) – A data instance for the plugin.

- **suffix** (*str*) – The format’s file suffix.

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.RegisterCommandPlugin(id, str, info, icon, help, dat)` <a id="c4d.plugins.RegisterCommandPlugin"></a>

Registers a [`CommandData`](BaseData/CommandData/index.md#c4d.plugins.CommandData) plugin.

**Parameters:**

- **id** (*int*) –

  A unique plugin ID. You **must** obtain this from [PluginCafe.com](http://plugincafe.com/)

- **str** (*str*) –

  The name of the plugin.

  > **Note:**
  >
  > If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.  
  > Lower numbers are displayed before higher numbers. If you make the name “–” it will show up as a menu separator.

- **info** (*int*) –

  The settings for the plugin. Possible flags are:

  - Plugin General Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_HIDE* | Hide the plugin. |
  | *PLUGINFLAG_SMALLNODE* | Create a small node. |
  | *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
  | *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |

  - Command Plugin Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_COMMAND_HOTKEY* | Command is a hotkey command. Hotkey commands can only work globally. |
  | *PLUGINFLAG_COMMAND_OPTION_DIALOG* | Command has additional options. The user can access them through a small gadget. |
  | *PLUGINFLAG_COMMAND_STICKY* | Command is a “sticky” command. This means [`CommandData.Execute()`](BaseData/CommandData/index.md#c4d.plugins.CommandData.Execute) is called when the user presses an assigned hotkey and when the hotkey is released. Otherwise the command would be called continously. |
  | *PLUGINFLAG_COMMAND_ICONGADGET* | Command can be dragged into an icon bar and delivers its own dialogs instead of icons. |

- **icon** (*Optional*[[*c4d.bitmaps.BaseBitmap*](../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]) –

  The icon for the command. The bitmap is copied.

  > **Note:**
  >
  > The icon should be of size 32x32, but will be scaled if needed.  
  > It must also be 24 bits and should if possible include an alpha to support pattern backgrounds.

- **help** (*str*) –

  The tool tips and status bar help text for the command.

  > **Note:**
  >
  > When using strings it is advised to use the string resources files and the [`GeLoadString()`](#c4d.plugins.GeLoadString) function.  
  > This keeps the plugin easy to localise for any language you wish to support and makes full use of the language features of Cinema 4D.

- **dat** ([*c4d.plugins.CommandData*](BaseData/CommandData/index.md#c4d.plugins.CommandData)) – A data instance for the plugin.

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.RegisterDescription(id, str, res=None)` <a id="c4d.plugins.RegisterDescription"></a>

Registers a description for a plugin ID.

*New in version R16.021.*

> **Note:** Not needed for plugin types whose Register() functions have a *description* parameter.

**Parameters:**

- **id** (*int*) – The plugin ID. If this is a standalone description, use a unique ID.

- **str** (*str*) –

  The name of the description resource file to use for your plugin without .res extension, for example “registered”.  
  The name has to be unique, i.e. *Tdisplay* cannot be used for two different descriptions.

- **res** (*Optional*[[*c4d.plugins.GeResource*](GeResource/index.md#c4d.plugins.GeResource)]) – Pass to search in a specific resource class. Otherwise the default path is used.

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.RegisterHiddenToken(key, help, example, hook)` <a id="c4d.plugins.RegisterHiddenToken"></a>

This function registers a hidden token that is not displayed in Render Settings.

*New in version R21.*

> **Note:**
>
> The key is the identifier for the Token and has to be unique.  
> For this reason identify your plugin in the Token key as a prefix.  
> Example: “myplug.pass” instead of just “pass” as it will collide wit the generic “pass” Token definition.

**Parameters:**

- **key** (*str*) – The key string for the Token itself without the “$”.

- **help** (*str*) – An help string used to show the Token in the menu.

- **example** (*str*) – An example string for the use of the Token.

- **hook** (*function*(*data*)) –

  A function used to define the string to replace the Token.

  The expected function signature is *functionName(data)* and parameters correspond to:

  > - data: ([`c4d.BaseContainer`](../c4d/BaseContainer/index.md#c4d.BaseContainer)) A baseContainer with the next data:
  >
  >   > - data[0] ([`c4d.documents.BaseDocument`](../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) The BaseDocument used for rendering, can be a clone of original document.
  >   > - data[1] ([`c4d.documents.RenderData`](../c4d.documents/RenderData/index.md#c4d.documents.RenderData)) The RenderData used for rendering.
  >   > - data[2] ([`c4d.BaseContainer`](../c4d/BaseContainer/index.md#c4d.BaseContainer)) The BaseContainer with the render settings (can be different from _rData->GetDataInstance() eg. RQ change paths).
  >   > - data[3] ([`c4d.modules.takesystem.BaseTake`](../c4d.modules/takesystem/BaseTake/index.md#c4d.modules.takesystem.BaseTake)) The BaseTake used for rendering.
  >   > - data[4] (int) The frame number used for rendering or NOTOK if the frame is not yet recognized.
  >   > - data[5] (str) The pass user name if multipass is activated.
  >   > - data[6] (str) The pass type name if multipass is activated.
  >   > - data[7] (int) The pass ID used for rendering or NOTOK if multipass is not active or not yet recognized.
  >   > - data[8] (bool) **True** if the pass is a separated light pass.
  >   > - data[9] (int) The light number id.
  >   > - data[10] (bool) **True** if the pass is a separated reflectance material pass.
  >   > - data[11] (str) if data[9] is **True** or data[10] is **True** store here the object scene name.
  >   > - data[12] (bool) if **True** warning strings will be used for the Tokens that cannot be resolved.
  >   > - data[13] ([`c4d.BaseList2D`](../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) An owner node for certain tokens such as MoGraph cache tokens. Can be **None**.

**Return type:** str

**Returns:** The string that will replace the Token.

#### `c4d.plugins.RegisterManagerInformation(id, str, info)` <a id="c4d.plugins.RegisterManagerInformation"></a>

Registers manager information for use when registering shortcuts with [`AddShortcut()`](../c4d.gui/index.md#c4d.gui.AddShortcut).

**Parameters:**

- **id** (*int*) –

  A unique plugin ID. You **must** obtain this from [PluginCafe.com](http://plugincafe.com/)

- **str** (*str*) – Manager name.

- **info** (*int*) –

  The settings for the plugin. Possible flags are:

  |   |   |
  |---|---|
  | *PLUGINFLAG_HIDE* | Hide the plugin. |
  | *PLUGINFLAG_SMALLNODE* | Create a small node. |
  | *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
  | *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.RegisterMessagePlugin(id, str, info, dat)` <a id="c4d.plugins.RegisterMessagePlugin"></a>

Registers a [`MessageData`](BaseData/MessageData/index.md#c4d.plugins.MessageData) plugin.

**Parameters:**

- **id** (*int*) –

  A unique plugin ID. You **must** obtain this from [PluginCafe.com](http://plugincafe.com/)

- **str** (*str*) –

  The name of the plugin.

  > **Note:**
  >
  > If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.  
  > Lower numbers are displayed before higher numbers. If you make the name “–” it will show up as a menu separator.

- **info** (*int*) –

  The settings for the plugin.

  - Plugin General Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_HIDE* | Hide the plugin. |
  | *PLUGINFLAG_SMALLNODE* | Create a small node. |
  | *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
  | *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |

  - Message Plugin Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_MESSAGE_SYNCEVENT* | *New in version R17.032:* Sync messages will also be received by the message plugin. |

- **dat** ([*c4d.plugins.MessageData*](BaseData/MessageData/index.md#c4d.plugins.MessageData)) – A data instance for the plugin.

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.RegisterNodePlugin(id, str, info, g, icon, disklevel=0)` <a id="c4d.plugins.RegisterNodePlugin"></a>

Registers a [`NodeData`](BaseData/NodeData/index.md#c4d.plugins.NodeData) plugin.

> **Note:** Normally you won’t use this function directly, but rather the specific registration functions for each [`NodeData`](BaseData/NodeData/index.md#c4d.plugins.NodeData) child class.

**Parameters:**

- **id** (*int*) –

  A unique plugin ID. You **must** obtain this from [PluginCafe.com](http://plugincafe.com/)

- **str** (*str*) –

  The name of the plugin.

  > **Note:**
  >
  > If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.  
  > Lower numbers are displayed before higher numbers. If you make the name “–” it will show up as a menu separator.

- **info** (*int*) –

  One of the following flags:

  |   |   |
  |---|---|
  | *PLUGINFLAG_HIDE* | Hide the plugin. |
  | *PLUGINFLAG_SMALLNODE* | Create a small node. |
  | *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
  | *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |

- **g** (*any*) – The class which inherits from [`NodeData`](BaseData/NodeData/index.md#c4d.plugins.NodeData)

- **icon** (*Optional*[[*c4d.bitmaps.BaseBitmap*](../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]) –

  The icon for the command. Can be **None**. The bitmap is copied.

  > **Note:**
  >
  > The icon should be of size 32x32, but will be scaled if needed.  
  > It must also be 24 bits and should if possible include an alpha to support pattern backgrounds.

- **disklevel** (*Optional*[*int*]) –

  The plugin level is similar to a version number for your settings.  
  The default level is 0, you can then increase this for new revisions of your plugin, this allows for forward and backward compatibility.

  As an example you may have updated your plugin, if you now need to write additional information for new settings or changed types for old settings you can increase the level. During loading either a 0 is passed (if the file was written using your old plugin) or 1 (if the file was written by the new plugin). This allows you to easily save/read new values.

  > **Important:** For forward and backward compatibility to work you must not change any existing read order from a given level, Cinema 4D will skip any new settings automatically if they have not been read for your plugin.

  > **Note:** If you only use containers for all your values, you do not have to deal with the disklevel.

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.RegisterObjectPlugin(id, str, g, description, info, icon, disklevel=0, res=None)` <a id="c4d.plugins.RegisterObjectPlugin"></a>

Registers an [`ObjectData`](BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData) plugin.

> **Note:** To use this function, *__res__* must be defined in your global scope.

**Parameters:**

- **id** (*int*) –

  A unique plugin ID. You **must** obtain this from [PluginCafe.com](http://plugincafe.com/)

- **str** (*str*) –

  The name of the plugin.

  > **Note:**
  >
  > If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.  
  > Lower numbers are displayed before higher numbers. If you make the name “–” it will show up as a menu separator.

- **g** (*any*) – The class which inherits from [`ObjectData`](BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData)

- **description** (*str*) – The name of the description resource file to use for your plugin without **.res**, for example **Oobjectname**. The name has to be unique, i.e. **Tdisplay** cannot be used for two different descriptions.

- **info** (*int*) –

  One of the following flags:

  - Plugin General Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_HIDE* | Hide the plugin. |
  | *PLUGINFLAG_SMALLNODE* | Create a small node. |
  | *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
  | *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |

  - Object Plugin Flags

  | Symbol ID | Description |
  |---|---|
  | OBJECT_MODIFIER | Modifier object. Deforms the surrounding object. (E.g. bend.) |
  | OBJECT_HIERARCHYMODIFIER | Hierarchical modifier. Deforms the surrounding objects together with other instances in a hierarchy chain. Only the top-most instance of the plugin in a chain is called. (E.g. bones.) |
  | OBJECT_GENERATOR | Generator object. Produces a polygonal or spline representation on its own. (E.g. primitive cube.) |
  | OBJECT_INPUT | Used in combination with OBJECT_GENERATOR. Specifies that the generator builds a polygon or spline, using its sub-objects as input. (E.g. Sweep Subdivision Surface, Boolean.) |
  | OBJECT_PARTICLEMODIFIER | Particle modifier. |
  | OBJECT_ISSPLINE | The object is a spline. |
  | OBJECT_UNIQUEENUMERATION | Unique enumeration. See :`BaseObject.GetUniqueIP()`. |
  | OBJECT_CAMERADEPENDENT | Camera dependent. |
  | OBJECT_USECACHECOLOR | If this flag is specified, the generator object itself controls the objects’ colors (the ones that determine the wireframe/shaded color). Normally these are automatically overwritten by the generator objects settings. E.g. if the instance object is set to green, automatically all of its cache objects get the green color. By setting this flag an instance object could individually color objects. |
  | OBJECT_POINTOBJECT | Point Object. |
  | OBJECT_POLYGONOBJECT | Polygon object. |
  | OBJECT_NO_PLA | Objects derived from [`PointObject`](../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/index.md#c4d.PointObject) will not use auto-keyframing (e.g. Joints can contain points and PLA auto-keyframing is not useful for them) |
  | OBJECT_DONTFREECACHE | Objects’ (generators) caches will not be be deleted - users must maintain caches themselves. |
  | OBJECT_CALL_ADDEXECUTION | Must be set to call [`ObjectData.Execute()`](BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData.Execute) in the priority pipeline specified by [`ObjectData.AddToExecution()`](BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData.AddToExecution). |
  | OBJECT_NOCHILDEXPRESSIONS | *New in version R20:* Don’t execute expression tags on the children of the object. |
  | OBJECT_FIELDOBJECT | *New in version R20:* Field object. Can’t be created in Python. |
  | OBJECT_HASDEFORMMODE | *New in version R26:* Object has a deform mode even if it is not one of the standard types with a deform mode. |
  | OBJECT_ICONCHOOSER_PARENT_IGNORE | Previously was expressed in the tag as c4d.TAG_ICONCHOOSER_PARENT_IGNORE. |
  | OBJECT_CUSTOM_NAME_ADDITION | *New in version 2024.4:* Specify that an object implement MSG_GETCUSTOM_NAME_ADDITION and this message should be called from the Object Manager to retrieve its custom additional name. |

- **icon** (*Optional*[[*c4d.bitmaps.BaseBitmap*](../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]) –

  The icon for the command. Can be **None**. The bitmap is copied.

  > **Note:**
  >
  > The icon should be of size 32x32, but will be scaled if needed.  
  > It must also be 24 bits and should if possible include an alpha to support pattern backgrounds.

- **disklevel** (*int*) –

  The plugin level is similar to a version number for your settings.  
  The default level is 0, you can then increase this for new revisions of your plugin, this allows for forward and backward compatibility.

  As an example you may have updated your plugin, if you now need to write additional information for new settings or changed types for old settings you can increase the level. During loading either a 0 is passed (if the file was written using your old plugin) or 1 (if the file was written by the new plugin). This allows you to easily save/read new values.

  > **Important:** For forward and backward compatibility to work you must not change any existing read order from a given level, Cinema 4D will skip any new settings automatically if they have not been read for your plugin.

  > **Note:** If you only use containers for all your values, you do not have to deal with the disklevel.

- **res** (*Optional*[[*c4d.plugins.GeResource*](GeResource/index.md#c4d.plugins.GeResource)]) – The optional resource.

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.RegisterPluginHelpCallback(pluginid, callback)` <a id="c4d.plugins.RegisterPluginHelpCallback"></a>

Registers a callback for plugin help support.

*New in version R19.*

**Parameters:**

- **pluginid** (*int*) –

  The plugin id. Please obtain a serial from [PluginCafe.com](http://plugincafe.com/)

- **callback** (function(*opType*, *baseType*, *group*, *property*)) –

  The help callback for the plugin. Useful to display context sensitive help when the user selects “Show Help” for a node or attribute.  
  The passed arguments are:

  > *opType*: *str*: The node type name, for example “OATOM”.  
  > *baseType*: *str*: The name of the base object type that *opType* is derived from, usually the same as *opType*.  
  > *group*: *str*: The name of the group in the attribute manager, for example “ID_OBJECTPROPERTIES”.  
  > *property*: *str*: The name of the property, for example “ATOMOBJECT_SINGLE”.

  The callback function returns **True** if help has been provided, otherwise **False**.

  > **Warning:** Only return **True** for the registered plugin types.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `c4d.plugins.RegisterPreferencePlugin(id, g, name, description, parentid, sortid)` <a id="c4d.plugins.RegisterPreferencePlugin"></a>

Registers a new preference in the Cinema 4D preferences dialog.

*New in version R19.*

**Parameters:**

- **id** (*int*) –

  A unique plugin ID. You **must** obtain this from [PluginCafe.com](http://plugincafe.com/)

- **g** (*any*) – The class which inherits from [`PreferenceData`](BaseData/NodeData/PreferenceData/index.md#c4d.plugins.PreferenceData)

- **name** (*str*) – The name of the preference.

- **description** (*str*) – The name of the description resource file to use for your plugin without **.res**, for example **Oobjectname**. The name has to be unique, i.e. **Tdisplay** cannot be used for two different descriptions.

- **parentid** (*int*) – The ID of the preference parent hook. Should be usually set to *0*.

- **sortid** (*int*) –

  The ID of the parent category in the preferences tree or *0* to create a top-level category. The internal categories are:

  |   |   |
  |---|---|
  | *PREFS_THEME* | Interface Colors. |
  | *PREFS_COLORNEW* | Editor Colors. |
  | *PREFS_MOUSE* | Input Devices. |
  | *PREFS_OPENGL* | OpenGL. |
  | *PREFS_VIEW* | Viewport. |
  | *PREFS_FILES* | Files. |
  | *PREFS_UNITS* | Units. |
  | *PREFS_MEMORY* | Memory. |
  | *PREFS_COMMUNICATION* | Communication. |
  | *PREFS_RENDERERNEW* | Renderer. |
  | *PREFS_NEWPREFS* | Interface. |
  | *PREFS_BP* | Bodypaint 3D. |
  | *PREFS_MATMANAGER* | Material. |
  | *PREFS_IMPORTEXPORT* | Import/Export. |
  | *PREFS_LINUX* | Linux Command Line. |
  | *PREFS_SCHEMECOLORS* | Color Scheme. |
  | *PREFS_HAIR_COLOR* | Hair Color. |
  | *PREFS_NAVIGATION* | Navigation. |
  | *PREFS_PLUGINS* | Plugins. |
  | *PREFS_GPURENDERER* | ProRender. |
  | *PREFS_LIVELINK* |  |
  | *PREFS_EXTENSIONS* |  |

#### `c4d.plugins.RegisterSceneLoaderPlugin(id, str, g, info, description, res=None)` <a id="c4d.plugins.RegisterSceneLoaderPlugin"></a>

Registers a [`SceneLoaderData`](BaseData/NodeData/SceneLoaderData/index.md#c4d.plugins.SceneLoaderData) plugin.

> **Note:** To use this function, *__res__* must be defined in your global scope.

**Parameters:**

- **id** (*int*) –

  The plugin id. Please obtain a serial from [PluginCafe.com](http://plugincafe.com/)

- **str** (*str*) –

  The name of the plugin.

  > **Note:**
  >
  > If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.  
  > Lower numbers are displayed before higher numbers. If you make the name “–” it will show up as a menu separator.

- **g** (*any*) – The class which inherits from [`SceneLoaderData`](BaseData/NodeData/SceneLoaderData/index.md#c4d.plugins.SceneLoaderData)

- **info** (*int*) –

  The settings for the plugin. Possible flags are:

  - Plugin General Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_HIDE* | Hide the plugin. |
  | *PLUGINFLAG_SMALLNODE* | Create a small node. |
  | *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
  | *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |

  - Scene Loader Plugin Flags

  | Symbol ID | Description |
  |---|---|
  | PLUGINFLAG_SCENELOADER_MERGEORIGINAL | If this flag is set, the original (existing) document will be passed to the scene loader instead of a new (empty) one.  <br>This allows the importer to change existing data, merge data or to make other modifications based on the existing scene. |
  | PLUGINFLAG_SCENELOADER_URL_AWARE | *New in version R24:* Scene loader plugin flag to signal that the scene loader is capable to deal with urls not in the file system e.g. asset:/// |
  | PLUGINFLAG_SCENELOADER_SUPPORT_ASYNC | *New in version R26:* Signals that a scene loader should run asynchronously. |

  - Scene Filter Plugin Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_SCENEFILTER_DIALOGCONTROL* | By default the scene loader/saver displays its own description dialog during importing/exporting of scene files. By setting this flag it will surpress this behaviour allowing to display another extended dialog for example. |

- **description** (*str*) – The name of the description resource file to use for your plugin without .res, for example *Ffiltername*. The name has to be unique, i.e. *Tdisplay* cannot be used for two different descriptions.

- **res** (*Optional*[[*c4d.plugins.GeResource*](GeResource/index.md#c4d.plugins.GeResource)]) – The optional resource.

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.RegisterSceneSaverPlugin(id, str, g, info, description, suffix, res=None)` <a id="c4d.plugins.RegisterSceneSaverPlugin"></a>

Registers a [`SceneSaverData`](BaseData/NodeData/SceneSaverData/index.md#c4d.plugins.SceneSaverData) plugin.

> **Note:** To use this function, *__res__* must be defined in your global scope.

**Parameters:**

- **id** (*int*) –

  The plugin id. Please obtain a serial from [PluginCafe.com](http://plugincafe.com/)

- **str** (*str*) –

  The name of the plugin.

  > **Note:**
  >
  > If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.  
  > Lower numbers are displayed before higher numbers. If you make the name “–” it will show up as a menu separator.

- **g** (*any*) – The class which inherits from [`SceneSaverData`](BaseData/NodeData/SceneSaverData/index.md#c4d.plugins.SceneSaverData)

- **info** (*int*) –

  The flags are

  - Plugin General Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_HIDE* | Hide the plugin. |
  | *PLUGINFLAG_SMALLNODE* | Create a small node. |
  | *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
  | *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |

  - Scene Filter Plugin Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_SCENEFILTER_DIALOGCONTROL* | By default the scene loader/saver displays its own description dialog during importing/exporting of scene files. By setting this flag it will surpress this behaviour allowing to display another extended dialog for example. |

- **description** (*str*) – The name of the description resource file to use for your plugin without .res, for example *Ffiltername*. The name has to be unique, i.e. *Tdisplay* cannot be used for two different descriptions.

- **suffix** (*str*) – The format’s file suffix.

- **res** (*Optional*[[*c4d.plugins.GeResource*](GeResource/index.md#c4d.plugins.GeResource)]) – The optional resource.

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.RegisterSculptBrushPlugin(id, str, info, icon, help, sculptparams, dat, res)` <a id="c4d.plugins.RegisterSculptBrushPlugin"></a>

Registers a [`SculptBrushToolData`](BaseData/SculptBrushToolData/index.md#c4d.plugins.SculptBrushToolData).

*New in version R16.021.*

**Parameters:**

- **id** (*int*) –

  The plugin id. Please obtain a serial from [PluginCafe.com](http://plugincafe.com/)

- **str** (*str*) –

  The name.

  > **Note:**
  >
  > If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.  
  > Lower numbers are displayed before higher numbers. If you make the name “–” it will show up as a menu separator.

- **info** (*int*) –

  The settings for the plugin. Possible flags are:

  - Plugin General Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_HIDE* | Hide the plugin. |
  | *PLUGINFLAG_SMALLNODE* | Create a small node. |
  | *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
  | *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |

  - Tool Plugin Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_TOOL_EVALUATEHANDLES* | Evaluate object handles when tool is active. |
  | *PLUGINFLAG_TOOL_DRAW_MULTIPLANE* | Draw multiple planes. |
  | *PLUGINFLAG_TOOL_TWEAK* | Tweak mode supported. |
  | *PLUGINFLAG_TOOL_HIGHLIGHT* | Hightlighting supported. |
  | *PLUGINFLAG_TOOL_EDITSTATES* | Edit states supported. |
  | *PLUGINFLAG_TOOL_SNAPSETTINGS* | Snap settings supported. |
  | *PLUGINFLAG_TOOL_SINGLECLICK* | Single click tool. |
  | *PLUGINFLAG_TOOL_TWEAK_NO_HIGHLIGHT* | Tweak mode with no hightlighting. |
  | *PLUGINFLAG_TOOL_SWITCHACTION* | *New in version R17.032:* Allow the tool to switch to a different tool on modifier. |
  | *PLUGINFLAG_TOOL_IS_SELECTION* | *New in version S22:* The tool is a selection tool, will be used to toggle the tool accordingly. |
  | *PLUGINFLAG_TOOL_NO_TOPOLOGY_EDIT* | *New in version S22:* \| The tool do not affect the polygon object topology (for example is a transform tool). \| It is used internally to allow advance UV display in the 3d viewport. |

- **icon** (*Optional*[[*c4d.bitmaps.BaseBitmap*](../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]) –

  The icon for the command. The bitmap is copied.

  > **Note:**
  >
  > The icon should be of size 32x32, but will be scaled if needed.  
  > It must also be 24 bits and should if possible include an alpha to support pattern backgrounds.

- **help** (*str*) –

  The tool tips and status bar help text for the command.

  > **Note:**
  >
  > When using strings it is advised to use the string resources files and the [`GeLoadString()`](#c4d.plugins.GeLoadString) function.  
  > This keeps the plugin easy to localise for any language you wish to support and makes full use of the language features of Cinema 4D.

- **sculptparams** ([*c4d.modules.sculpting.SculptBrushParams*](../c4d.modules/sculpting/SculptBrushParams/index.md#c4d.modules.sculpting.SculptBrushParams)) – The brush parameters.

- **dat** ([*c4d.plugins.SculptBrushToolData*](BaseData/SculptBrushToolData/index.md#c4d.plugins.SculptBrushToolData)) – A data instance for the plugin.

- **res** ([*c4d.plugins.GeResource*](GeResource/index.md#c4d.plugins.GeResource)) – The optional resource.

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.RegisterShaderPlugin(id, str, info, g, description, disklevel=0, res=None)` <a id="c4d.plugins.RegisterShaderPlugin"></a>

Registers a [`ShaderData`](BaseData/NodeData/ShaderData/index.md#c4d.plugins.ShaderData) plugin.

**Parameters:**

- **id** (*int*) –

  A unique plugin ID. You **must** obtain this from [PluginCafe.com](http://plugincafe.com/)

- **str** (*str*) –

  The name of the plugin.

  > **Note:**
  >
  > If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.  
  > Lower numbers are displayed before higher numbers. If you make the name “–” it will show up as a menu separator.

- **info** (*int*) –

  One of the following flags:

  |   |   |
  |---|---|
  | *PLUGINFLAG_HIDE* | Hide the plugin. |
  | *PLUGINFLAG_SMALLNODE* | Create a small node. |
  | *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
  | *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |

- **g** (*any*) – The class which inherits from [`ShaderData`](BaseData/NodeData/ShaderData/index.md#c4d.plugins.ShaderData)

- **description** (*str*) – The name of the description resource file to use for your plugin without **.res**, for example **“Xshadername”**. The name has to be unique, i.e. **“Tdisplay”** cannot be used for two different descriptions.

- **disklevel** (*int*) –

  The plugin level is similar to a version number for your settings.  
  The default level is 0, you can then increase this for new revisions of your plugin, this allows for forward and backward compatibility.

  As an example you may have updated your plugin, if you now need to write additional information for new settings or changed types for old settings you can increase the level. During loading either a 0 is passed (if the file was written using your old plugin) or 1 (if the file was written by the new plugin). This allows you to easily save/read new values.

  > **Important:** For forward and backward compatibility to work you must not change any existing read order from a given level, Cinema 4D will skip any new settings automatically if they have not been read for your plugin.

  > **Note:** If you only use containers for all your values, you do not have to deal with the disklevel.

- **res** (*Optional*[[*c4d.plugins.GeResource*](GeResource/index.md#c4d.plugins.GeResource)]) – The optional resource.

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.RegisterTagPlugin(id, str, info, g, description, icon, disklevel=0, res=None)` <a id="c4d.plugins.RegisterTagPlugin"></a>

Registers a TagData plugin:

> **Note:** To use this function, *__res__* must be defined in your global scope.

**Parameters:**

- **id** (*int*) –

  A unique plugin ID. You **must** obtain this from [PluginCafe.com](http://plugincafe.com/)

- **str** (*str*) –

  The name of the plugin.

  > **Note:**
  >
  > If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number.  
  > Lower numbers are displayed before higher numbers. If you make the name “–” it will show up as a menu separator.

- **info** (*int*) –

  The settings for the plugin. Possible flags are:

  - Plugin General Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_HIDE* | Hide the plugin. |
  | *PLUGINFLAG_SMALLNODE* | Create a small node. |
  | *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
  | *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |

  - Tag Plugin Flags

  |   |   |
  |---|---|
  | *TAG_VISIBLE* | The tag can be seen in the object manager. |
  | *TAG_MULTIPLE* | Multiple copies of the tag allowed on a single object. |
  | *TAG_HIERARCHICAL* | The tag works hierarchical, so that sub-objects inherit its properties (e.g. the material tag). |
  | *TAG_EXPRESSION* | The tag is an expression. |
  | *TAG_TEMPORARY* | Private. |
  | *TAG_ADDTOTAKEGROUP* | *New in version R17.032:* The tag is added to the Take override groups system. |
  | *TAG_IMPLEMENTS_DRAW_FUNCTION* | *New in version S22:* The tag implements the [`TagData.Draw()`](BaseData/NodeData/TagData/index.md#c4d.plugins.TagData.Draw) function. |

- **g** (*any*) – The class which inherits from [`TagData`](BaseData/NodeData/TagData/index.md#c4d.plugins.TagData)

- **description** (*str*) –

  The name of the description resource file to use for your plugin without **.res**, for example **Ttagname**.  
  The name has to be unique, i.e. **Tdisplay** cannot be used for two different descriptions.

- **icon** (*Optional*[[*c4d.bitmaps.BaseBitmap*](../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]) –

  The icon for the command. Can be **None**. The bitmap is copied.

  > **Note:**
  >
  > The icon should be of size 32x32, but will be scaled if needed.  
  > It must also be 24 bits and should if possible include an alpha to support pattern backgrounds.

- **disklevel** (*int*) –

  The plugin level is similar to a version number for your settings. The default level is 0, you can then increase this for new revisions of your plugin, this allows for forward and backward compatibility.

  As an example you may have updated your plugin, if you now need to write additional information for new settings or changed types for old settings you can increase the level. During loading either a 0 is passed (if the file was written using your old plugin) or 1 (if the file was written by the new plugin). This allows you to easily save/read new values.

  > **Important:** For forward and backward compatibility to work you must not change any existing read order from a given level, Cinema 4D will skip any new settings automatically if they have not been read for your plugin.

  > **Note:** If you only use containers for all your values, you do not have to deal with the disklevel.

- **res** (*Optional*[[*c4d.plugins.GeResource*](GeResource/index.md#c4d.plugins.GeResource)]) – The optional resource.

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.RegisterToken(key, help, example, hook)` <a id="c4d.plugins.RegisterToken"></a>

Registers a new Token that can be used in a render filename, the token is displayed in the render setting and can be selected by the user.

*New in version R21.*

> **Note:**
>
> The key is the identifier for the Token and has to be unique.  
> For this reason identify your plugin in the Token key as a prefix.  
> Example: “myplug.pass” instead of just “pass” as it will collide wit the generic “pass” Token definition.

**Parameters:**

- **key** (*str*) – The key string for the Token itself without the “$”.

- **help** (*str*) – An help string used to show the Token in the menu.

- **example** (*str*) – An example string for the use of the Token.

- **hook** (*function*(*data*)) –

  A function used to define the string to replace the Token.

  The expected function signature is *functionName(data)* and parameters correspond to:

  > - data: ([`c4d.BaseContainer`](../c4d/BaseContainer/index.md#c4d.BaseContainer)) A baseContainer with the next data:
  >
  >   > - data[0] ([`c4d.documents.BaseDocument`](../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) The BaseDocument used for rendering, can be a clone of original document.
  >   > - data[1] ([`c4d.documents.RenderData`](../c4d.documents/RenderData/index.md#c4d.documents.RenderData)) The RenderData used for rendering.
  >   > - data[2] ([`c4d.BaseContainer`](../c4d/BaseContainer/index.md#c4d.BaseContainer)) The BaseContainer with the render settings (can be different from _rData->GetDataInstance() eg. RQ change paths).
  >   > - data[3] ([`c4d.modules.takesystem.BaseTake`](../c4d.modules/takesystem/BaseTake/index.md#c4d.modules.takesystem.BaseTake)) The BaseTake used for rendering.
  >   > - data[4] (int) The frame number used for rendering or NOTOK if the frame is not yet recognized.
  >   > - data[5] (str) The pass user name if multipass is activated.
  >   > - data[6] (str) The pass type name if multipass is activated.
  >   > - data[7] (int) The pass ID used for rendering or NOTOK if multipass is not active or not yet recognized.
  >   > - data[8] (bool) **True** if the pass is a separated light pass.
  >   > - data[9] (int) The light number id.
  >   > - data[10] (bool) **True** if the pass is a separated reflectance material pass.
  >   > - data[11] (str) if data[9] is **True** or data[10] is **True** store here the object scene name.
  >   > - data[12] (bool) if **True** warning strings will be used for the Tokens that cannot be resolved.
  >   > - data[13] ([`c4d.BaseList2D`](../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) An owner node for certain tokens such as MoGraph cache tokens. Can be **None**.

**Return type:** str

**Returns:** The string that will replace the Token.

#### `c4d.plugins.RegisterToolPlugin(id, str, info, icon, help, dat)` <a id="c4d.plugins.RegisterToolPlugin"></a>

Registers a [`ToolData`](BaseData/ToolData/index.md#c4d.plugins.ToolData) plugin.

**Parameters:**

- **id** (*int*) –

  The plugin id. Please obtain a serial from [PluginCafe.com](http://plugincafe.com/)

- **str** (*str*) –

  The name.

  > **Note:** If you want to affect the order that your plugins are displayed in menus you can add *#$n* as a prefix to this name, where *n* is a number. Lower numbers are displayed before higher numbers. If you make the name “–” it will show up as a menu separator.

- **info** (*int*) –

  The settings for the plugin. Possible flags are:

  - Plugin General Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_HIDE* | Hide the plugin. |
  | *PLUGINFLAG_SMALLNODE* | Create a small node. |
  | *PLUGINFLAG_HIDEPLUGINMENU* | Hide the plugin’s menu entry. |
  | *PLUGINFLAG_REFRESHALWAYS* | Deprecated. Legacy plugin flag. |

  - Tool Plugin Flags

  |   |   |
  |---|---|
  | *PLUGINFLAG_TOOL_EVALUATEHANDLES* | Evaluate object handles when tool is active. |
  | *PLUGINFLAG_TOOL_DRAW_MULTIPLANE* | Draw multiple planes. |
  | *PLUGINFLAG_TOOL_TWEAK* | Tweak mode supported. |
  | *PLUGINFLAG_TOOL_HIGHLIGHT* | Hightlighting supported. |
  | *PLUGINFLAG_TOOL_EDITSTATES* | Edit states supported. |
  | *PLUGINFLAG_TOOL_SNAPSETTINGS* | Snap settings supported. |
  | *PLUGINFLAG_TOOL_SINGLECLICK* | Single click tool. |
  | *PLUGINFLAG_TOOL_TWEAK_NO_HIGHLIGHT* | Tweak mode with no hightlighting. |
  | *PLUGINFLAG_TOOL_SWITCHACTION* | *New in version R17.032:* Allow the tool to switch to a different tool on modifier. |
  | *PLUGINFLAG_TOOL_IS_SELECTION* | *New in version S22:* The tool is a selection tool, will be used to toggle the tool accordingly. |
  | *PLUGINFLAG_TOOL_NO_TOPOLOGY_EDIT* | *New in version S22:* \| The tool do not affect the polygon object topology (for example is a transform tool). \| It is used internally to allow advance UV display in the 3d viewport. |

- **icon** (*Optional*[[*c4d.bitmaps.BaseBitmap*](../c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap)]) –

  The icon for the command. The bitmap is copied.

  > **Note:**
  >
  > The icon should be of size 32x32, but will be scaled if needed.  
  > It must also be 24 bits and should if possible include an alpha to support pattern backgrounds.

- **help** (*str*) –

  The tool tips and status bar help text for the command.

  > **Note:**
  >
  > When using strings it is advised to use the string resources files and the [`GeLoadString()`](#c4d.plugins.GeLoadString) function.  
  > This keeps the plugin easy to localise for any language you wish to support and makes full use of the language features of Cinema 4D.

- **dat** ([*c4d.plugins.ToolData*](BaseData/ToolData/index.md#c4d.plugins.ToolData)) – A data instance for the plugin.

**Return type:** bool

**Returns:** **True** if the registration was successful.

#### `c4d.plugins.Update()` <a id="c4d.plugins.Update"></a>

Subscribes the plugin that is currently being registered to be updated after the registration process.

When a plugin module imports the *c4d* module with `from c4d import *`, only the objects that exist at that time are imported into its namespace. During the startup of Cinema 4D, the constants and symbols of the *c4d* module are not parsed yet, so they would be missing. After the registration process is done, all symbols that were added to the *c4d* module are also added to the global namespace of a plugin that has called this function.

> **Note:** The function must be called from the registration routine of a plugin, i.e., while the plugin module is executed by Cinema 4D at startup or when it is reloaded.

**Raises:** **LookupError** – If the function is not called while a plugin is being registered.

### Registered Plugins Functions <a id="c4d.plugins-function-Registered-Plugins-Functions"></a>

#### `c4d.plugins.FilterPluginList(type, sortbyname)` <a id="c4d.plugins.FilterPluginList"></a>

Browses recursively through the plugin list looking for plugin of the specified *type*. For example, to find all bitmap savers you can write:

```python
import c4d

pluginList = c4d.plugins.FilterPluginList(c4d.PLUGINTYPE_BITMAPSAVER, True)
for plugin in pluginList:
    print plugin
```

**Parameters:**

- **type** (*int*) –

  Plugin type filter:

  |   |   |
  |---|---|
  | *PLUGINTYPE_ANY* | Any. |
  | *PLUGINTYPE_SHADER* | 2D Shader. ([`ShaderData`](BaseData/NodeData/ShaderData/index.md#c4d.plugins.ShaderData)) |
  | *PLUGINTYPE_MATERIAL* | 3D Shader. |
  | *PLUGINTYPE_COMMAND* | Command. ([`CommandData`](BaseData/CommandData/index.md#c4d.plugins.CommandData)) |
  | *PLUGINTYPE_OBJECT* | Object. ([`ObjectData`](BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData)) |
  | *PLUGINTYPE_TAG* | Tag. ([`TagData`](BaseData/NodeData/TagData/index.md#c4d.plugins.TagData)) |
  | *PLUGINTYPE_BITMAPFILTER* | Bitmap filter. ([`BitmapLoaderData`](BaseData/BitmapLoaderData/index.md#c4d.plugins.BitmapLoaderData), [`BitmapSaverData`](BaseData/BitmapSaverData/index.md#c4d.plugins.BitmapSaverData)) |
  | *PLUGINTYPE_VIDEOPOST* | Videopost effect. |
  | *PLUGINTYPE_TOOL* | Tool. ([`ToolData`](BaseData/ToolData/index.md#c4d.plugins.ToolData)) |
  | *PLUGINTYPE_SCENEHOOK* | Scene hook. |
  | *PLUGINTYPE_NODE* | Node. ([`NodeData`](BaseData/NodeData/index.md#c4d.plugins.NodeData)) |
  | *PLUGINTYPE_LIBRARY* | Library. |
  | *PLUGINTYPE_BITMAPLOADER* | Bitmap loader. ([`BitmapLoaderData`](BaseData/BitmapLoaderData/index.md#c4d.plugins.BitmapLoaderData)) |
  | *PLUGINTYPE_BITMAPSAVER* | Bitmap saver. ([`BitmapSaverData`](BaseData/BitmapSaverData/index.md#c4d.plugins.BitmapSaverData)) |
  | *PLUGINTYPE_SCENELOADER* | Scene loader. ([`SceneLoaderData`](BaseData/NodeData/SceneLoaderData/index.md#c4d.plugins.SceneLoaderData)) |
  | *PLUGINTYPE_SCENESAVER* | Scene saver. ([`SceneSaverData`](BaseData/NodeData/SceneSaverData/index.md#c4d.plugins.SceneSaverData)) |
  | *PLUGINTYPE_COREMESSAGE* | Core message. ([`MessageData`](BaseData/MessageData/index.md#c4d.plugins.MessageData)) |
  | *PLUGINTYPE_CUSTOMGUI* | Custom GUI. |
  | *PLUGINTYPE_CUSTOMDATATYPE* | Custom datatype. |
  | *PLUGINTYPE_RESOURCEDATATYPE* | Resource datatype. |
  | *PLUGINTYPE_MANAGERINFORMATION* | Manager information plugin. |
  | *PLUGINTYPE_CTRACK* | Track. |
  | *PLUGINTYPE_FALLOFF* | Falloff. ([`FalloffData`](BaseData/FalloffData/index.md#c4d.plugins.FalloffData)) |
  | *PLUGINTYPE_PREFS* | Preference hook. ([`PreferenceData`](BaseData/NodeData/PreferenceData/index.md#c4d.plugins.PreferenceData)) |
  | *PLUGINTYPE_SNAP* | Snap. |

- **sortbyname** (*bool*) – If this is **True** then the found plugins are sorted alphabetically by name.

**Return type:** List[[c4d.plugins.BasePlugin](BasePlugin/index.md#c4d.plugins.BasePlugin)]

**Returns:** The list.

#### `c4d.plugins.FindPlugin(id, type=0)` <a id="c4d.plugins.FindPlugin"></a>

Returns the [`BasePlugin`](BasePlugin/index.md#c4d.plugins.BasePlugin) found by id.

**Parameters:**

- **id** (*int*) – The plugin id. Please obtain a serial from plugincafe.com

- **type** (*int*) –

  Optionally a plugin type filter:

  |   |   |
  |---|---|
  | *PLUGINTYPE_ANY* | Any. |
  | *PLUGINTYPE_SHADER* | 2D Shader. ([`ShaderData`](BaseData/NodeData/ShaderData/index.md#c4d.plugins.ShaderData)) |
  | *PLUGINTYPE_MATERIAL* | 3D Shader. |
  | *PLUGINTYPE_COMMAND* | Command. ([`CommandData`](BaseData/CommandData/index.md#c4d.plugins.CommandData)) |
  | *PLUGINTYPE_OBJECT* | Object. ([`ObjectData`](BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData)) |
  | *PLUGINTYPE_TAG* | Tag. ([`TagData`](BaseData/NodeData/TagData/index.md#c4d.plugins.TagData)) |
  | *PLUGINTYPE_BITMAPFILTER* | Bitmap filter. ([`BitmapLoaderData`](BaseData/BitmapLoaderData/index.md#c4d.plugins.BitmapLoaderData), [`BitmapSaverData`](BaseData/BitmapSaverData/index.md#c4d.plugins.BitmapSaverData)) |
  | *PLUGINTYPE_VIDEOPOST* | Videopost effect. |
  | *PLUGINTYPE_TOOL* | Tool. ([`ToolData`](BaseData/ToolData/index.md#c4d.plugins.ToolData)) |
  | *PLUGINTYPE_SCENEHOOK* | Scene hook. |
  | *PLUGINTYPE_NODE* | Node. ([`NodeData`](BaseData/NodeData/index.md#c4d.plugins.NodeData)) |
  | *PLUGINTYPE_LIBRARY* | Library. |
  | *PLUGINTYPE_BITMAPLOADER* | Bitmap loader. ([`BitmapLoaderData`](BaseData/BitmapLoaderData/index.md#c4d.plugins.BitmapLoaderData)) |
  | *PLUGINTYPE_BITMAPSAVER* | Bitmap saver. ([`BitmapSaverData`](BaseData/BitmapSaverData/index.md#c4d.plugins.BitmapSaverData)) |
  | *PLUGINTYPE_SCENELOADER* | Scene loader. ([`SceneLoaderData`](BaseData/NodeData/SceneLoaderData/index.md#c4d.plugins.SceneLoaderData)) |
  | *PLUGINTYPE_SCENESAVER* | Scene saver. ([`SceneSaverData`](BaseData/NodeData/SceneSaverData/index.md#c4d.plugins.SceneSaverData)) |
  | *PLUGINTYPE_COREMESSAGE* | Core message. ([`MessageData`](BaseData/MessageData/index.md#c4d.plugins.MessageData)) |
  | *PLUGINTYPE_CUSTOMGUI* | Custom GUI. |
  | *PLUGINTYPE_CUSTOMDATATYPE* | Custom datatype. |
  | *PLUGINTYPE_RESOURCEDATATYPE* | Resource datatype. |
  | *PLUGINTYPE_MANAGERINFORMATION* | Manager information plugin. |
  | *PLUGINTYPE_CTRACK* | Track. |
  | *PLUGINTYPE_FALLOFF* | Falloff. ([`FalloffData`](BaseData/FalloffData/index.md#c4d.plugins.FalloffData)) |
  | *PLUGINTYPE_PREFS* | Preference hook. ([`PreferenceData`](BaseData/NodeData/PreferenceData/index.md#c4d.plugins.PreferenceData)) |
  | *PLUGINTYPE_SNAP* | Snap. |

**Return type:** [c4d.plugins.BasePlugin](BasePlugin/index.md#c4d.plugins.BasePlugin)

**Returns:** The plugin.

#### `c4d.plugins.GetFirstPlugin()` <a id="c4d.plugins.GetFirstPlugin"></a>

Returns the first plugin of Cinema 4D.

**Return type:** [c4d.plugins.BasePlugin](BasePlugin/index.md#c4d.plugins.BasePlugin)

**Returns:** The first plugin.
