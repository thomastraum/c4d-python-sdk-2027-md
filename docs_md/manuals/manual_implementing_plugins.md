<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_implementing_plugins.html -->

# Implementing Plugins <a id="implementing-plugins"></a>

Explains the basic concepts of implementing plugins.

A Python plugin is a `.pyp` module that Cinema 4D loads at startup. It usually registers a *hook*: a class derived from a [`c4d.plugins`](../modules/c4d.plugins/index.md#c4d.plugins) data class that Cinema 4D calls to implement a command, object, tag, tool, or file format. This guide covers registration, scene-node hooks, plugin files and resources, and application lifecycle messages.

Unlike a [Script Manager script](manual_script_manager.md), a plugin is loaded once at startup, can keep state for the whole session, and can bring its own interface and localization resources.

## Hooks <a id="hooks"></a><a id="plugin-hooks"></a>

The list below shows every Python plugin hook. Click a hook to reveal its registration function and the SDK examples that demonstrate it. The lists are generated from the `.pyp` files of the SDK, so one example can show up for multiple hooks, and a hook without an example is still fully documented in the [`c4d.plugins`](../modules/c4d.plugins/index.md#c4d.plugins) API.

Hook

Description

Commands and Messages

`CommandData`

Runs on demand from menus, palettes, and shortcuts.

Hook

[`CommandData`](../modules/c4d.plugins/BaseData/CommandData/index.md#c4d.plugins.CommandData)

Registration

[`RegisterCommandPlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterCommandPlugin)

| Example | Description |
|---|---|
| [py_cmd_gui_dynamic.pyp](../examples/plugins/py_cmd_gui_dynamic/py_cmd_gui_dynamic.pyp.md) | Demonstrates a dialog with dynamic content, where the content changes based on user input. |
| [py_cmd_gui_hello_world.pyp](../examples/plugins/py_cmd_gui_hello_world/py_cmd_gui_hello_world.pyp.md) | Demonstrates the most basic command/dialog plugin possible. |
| [py_cmd_gui_html.pyp](../examples/plugins/py_cmd_gui_html/py_cmd_gui_html.pyp.md) | Demonstrates how to implement a dialog that hosts an HTML viewer and can send and receive data to/from the displayed web page. |
| [py_cmd_gui_persistent.pyp](../examples/plugins/py_cmd_gui_persistent/py_cmd_gui_persistent.pyp.md) | Demonstrates how to store dialog layout data and values persistently over dialog open/close and Cinema 4D restart boundaries. |
| [py_cmd_gui_persistent_no_restart.pyp](../examples/plugins/py_cmd_gui_persistent_no_restart/py_cmd_gui_persistent_no_restart.pyp.md) | Demonstrates a simple way to store dialog layout data and values persistently over dialog open/close boundaries (but not over Cinema 4D restart boundaries). |
| [py_cmd_gui_resources.pyp](../examples/plugins/py_cmd_gui_resources/py_cmd_gui_resources.pyp.md) | Demonstrates a plugin that uses resources to define its dialog layout and string translations. |
| [py_cmd_gui_simple.pyp](../examples/plugins/py_cmd_gui_simple/py_cmd_gui_simple.pyp.md) | Demonstrates a simple dialog with two number input fields, a combo box and a button to carry out numeric operations on the two numbers. |
| [py_cmd_memory_viewer.pyp](../examples/plugins/py_cmd_memory_viewer/py_cmd_memory_viewer.pyp.md) | Demonstrates implementing a simple legacy memory viewer dialog. |
| [py_cmd_sculpt_save_mask.pyp](../examples/plugins/py_cmd_sculpt_save_mask/py_cmd_sculpt_save_mask.pyp.md) | Demonstrates the legacy Sculpting API; it is highly specialized and not that useful outside of sculpting. |
| [py_cmd_texture_baker.pyp](../examples/plugins/py_cmd_texture_baker/py_cmd_texture_baker.pyp.md) | Demonstrates implementing a simple legacy texture baking dialog. |
| [py_cmd_tool_finalization.pyp](../examples/plugins/py_cmd_tool_finalization/py_cmd_tool_finalization.pyp.md) | Demonstrates a tool finalization workflow at the example of editing SDS weights. |
| [py_msc_licensing.pyp](../examples/plugins/py_msc_licensing/py_msc_licensing.pyp.md) | Demonstrates how to implement licensing checks in plugins. |
| [py_msc_licensing_simple.pyp](../examples/plugins/py_msc_licensing/py_msc_licensing_simple.pyp.md) | Demonstrates simple licensing workflow for Python plugins in Cinema 4D. |

`MessageData`

Listens to application-wide core messages.

Hook

[`MessageData`](../modules/c4d.plugins/BaseData/MessageData/index.md#c4d.plugins.MessageData)

Registration

[`RegisterMessagePlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterMessagePlugin)

See also

[Message System](manual_message_system.md)

No SDK examples are available for this hook yet.

Scene Elements

`ObjectData`

Implements objects, generators, and deformers.

Hook

[`ObjectData`](../modules/c4d.plugins/BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData)

Registration

[`RegisterObjectPlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterObjectPlugin)

| Example | Description |
|---|---|
| [py_msc_licensing.pyp](../examples/plugins/py_msc_licensing/py_msc_licensing.pyp.md) | Demonstrates how to implement licensing checks in plugins. |
| [py_obj_assetcontainer.pyp](../examples/plugins/py_obj_assetcontainer/py_obj_assetcontainer.pyp.md) | Demonstrates NodeData serialization and custom branching. |
| [py_obj_custom_icon.pyp](../examples/plugins/py_obj_custom_icon/py_obj_custom_icon.pyp.md) | Demonstrates how to implement a scene element that dynamically updates its icon. |
| [py_obj_double_circle.pyp](../examples/plugins/py_obj_double_circle/py_obj_double_circle.pyp.md) | Demonstrates how to implement a spline object generator with handles to drive parameters. |
| [py_obj_dynamic_parameters.pyp](../examples/plugins/py_obj_dynamic_parameters/py_obj_dynamic_parameters.pyp.md) | Demonstrates how to implement a node (at the example of an object) that dynamically updates its parameters. |
| [py_obj_gravitation.pyp](../examples/plugins/py_obj_gravitation/py_obj_gravitation.pyp.md) | Demonstrates how to implement a classic particle modifier object that applies a simple gravitation effect for each particle. |
| [py_obj_ocio_node.pyp](../examples/plugins/py_obj_ocio_node/py_obj_ocio_node.pyp.md) | Demonstrates how to implement a scene element respecting OpenColorIO color management. |
| [py_obj_offset_y_spline.pyp](../examples/plugins/py_obj_offset_y_spline/py_obj_offset_y_spline.pyp.md) | Demonstrates a spline offset generator (very questionable design, should not be followed). |
| [py_obj_rounded_tube.pyp](../examples/plugins/py_obj_rounded_tube/py_obj_rounded_tube.pyp.md) | Demonstrates how to implement a polygonal object generator with handles to drive parameters. |
| [py_obj_sculpt_modifier_deformer.pyp](../examples/plugins/py_obj_sculpt_modifier_deformer/py_obj_sculpt_modifier_deformer.pyp.md) | Demonstrates how to implement a modifier object that modifies a point object using the pull sculpting brush tool. |
| [py_obj_sphere_deformer.pyp](../examples/plugins/py_obj_sphere_deformer/py_obj_sphere_deformer.pyp.md) | Demonstrates how to implement a deformer object that pushes the points of a point object to a spherical shape, driven by radius and strength parameters. |

`TagData`

Implements tags attached to objects.

Hook

[`TagData`](../modules/c4d.plugins/BaseData/NodeData/TagData/index.md#c4d.plugins.TagData)

Registration

[`RegisterTagPlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterTagPlugin)

| Example | Description |
|---|---|
| [py_tag_look_at_camera.pyp](../examples/plugins/py_tag_look_at_camera/py_tag_look_at_camera.pyp.md) | Demonstrates how to implement a tag that forces the host object to look at the camera (like the Look At Camera Tag). |

`ShaderData`

Implements classic material shaders.

Hook

[`ShaderData`](../modules/c4d.plugins/BaseData/NodeData/ShaderData/index.md#c4d.plugins.ShaderData)

Registration

[`RegisterShaderPlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterShaderPlugin)

See also

[Graph Descriptions](manual_graph_descriptions.md) for node materials

| Example | Description |
|---|---|
| [py_sha_fresnel.pyp](../examples/plugins/py_sha_fresnel/py_sha_fresnel.pyp.md) | Demonstrates how to implement a shader that computes a fresnel effect. |

`NodeData`

Generic base for custom node elements.

Hook

[`NodeData`](../modules/c4d.plugins/BaseData/NodeData/index.md#c4d.plugins.NodeData)

Registration

[`RegisterNodePlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterNodePlugin)

No SDK examples are available for this hook yet.

Interactive Tools

`ToolData`

Handles interactive viewport input.

Hook

[`ToolData`](../modules/c4d.plugins/BaseData/ToolData/index.md#c4d.plugins.ToolData)

Registration

[`RegisterToolPlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterToolPlugin)

| Example | Description |
|---|---|
| [py_tool_liquid_painter.pyp](../examples/plugins/py_tool_liquid_painter/py_tool_liquid_painter.pyp.md) | Demonstrates how to implement a simple tool. |
| [py_tool_ui.pyp](../examples/plugins/py_tool_ui/py_tool_ui.pyp.md) | Demonstrates how to implement a ToolData with a linkBox where it’s possible to drag and drop an object, which is then cloned and added to the document in a random position. |

`SculptBrushToolData`

Implements sculpting brushes.

Hook

[`SculptBrushToolData`](../modules/c4d.plugins/BaseData/SculptBrushToolData/index.md#c4d.plugins.SculptBrushToolData)

Registration

[`RegisterSculptBrushPlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterSculptBrushPlugin)

| Example | Description |
|---|---|
| [py_tool_sculpt_grab_brush.pyp](../examples/plugins/py_tool_sculpt_grab_brush/py_tool_sculpt_grab_brush.pyp.md) | Demonstrates how to implement a brush tool that modifies a BaseObject by grabbing all points under the brush. |
| [py_tool_sculpt_paint_brush.pyp](../examples/plugins/py_tool_sculpt_paint_brush/py_tool_sculpt_paint_brush.pyp.md) | Demonstrates how to implement a brush tool that rasterizes the stencil onto the polygons touched by the brush, accessing the stencil and BodyPaint layer. |
| [py_tool_sculpt_pull_brush.pyp](../examples/plugins/py_tool_sculpt_pull_brush/py_tool_sculpt_pull_brush.pyp.md) | Demonstrates how to implement a brush tool that modifies a BaseObject by pulling all points under the brush. |
| [py_tool_sculpt_twist_brush.pyp](../examples/plugins/py_tool_sculpt_twist_brush/py_tool_sculpt_twist_brush.pyp.md) | Demonstrates how to implement a brush tool that modifies a BaseObject by twisting all points under the brush. |

File Formats

`SceneLoaderData`

Imports a scene file format.

Hook

[`SceneLoaderData`](../modules/c4d.plugins/BaseData/NodeData/SceneLoaderData/index.md#c4d.plugins.SceneLoaderData)

Registration

[`RegisterSceneLoaderPlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterSceneLoaderPlugin)

| Example | Description |
|---|---|
| [py_io_ies_meta_loader.pyp](../examples/plugins/py_io_ies_meta/py_io_ies_meta_loader.pyp.md) | Demonstrates a scene loader plugin for IES Meta data. |

`SceneSaverData`

Exports a scene file format.

Hook

[`SceneSaverData`](../modules/c4d.plugins/BaseData/NodeData/SceneSaverData/index.md#c4d.plugins.SceneSaverData)

Registration

[`RegisterSceneSaverPlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterSceneSaverPlugin)

| Example | Description |
|---|---|
| [py_io_ies_meta.pyp](../examples/plugins/py_io_ies_meta/py_io_ies_meta.pyp.md) | Demonstrates how to implement a scene saver plugin that exports all IES Meta information from the current document to a txt file, iterating through all objects in the scene. |

`BitmapLoaderData`

Reads an image file format.

Hook

[`BitmapLoaderData`](../modules/c4d.plugins/BaseData/BitmapLoaderData/index.md#c4d.plugins.BitmapLoaderData)

Registration

[`RegisterBitmapLoaderPlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterBitmapLoaderPlugin)

| Example | Description |
|---|---|
| [py_io_xample_loader.pyp](../examples/plugins/py_io_xample_loader/py_io_xample_loader.pyp.md) | Demonstrates how to implement a custom bitmap loader to import a custom picture format into Cinema 4D. |

`BitmapSaverData`

Writes an image file format.

Hook

[`BitmapSaverData`](../modules/c4d.plugins/BaseData/BitmapSaverData/index.md#c4d.plugins.BitmapSaverData)

Registration

[`RegisterBitmapSaverPlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterBitmapSaverPlugin)

| Example | Description |
|---|---|
| [py_io_xample_saver.pyp](../examples/plugins/py_io_xample_saver/py_io_xample_saver.pyp.md) | Demonstrates how to implement a custom bitmap saver to export a custom picture format into Cinema 4D. |

Preferences

`PreferenceData`

Adds a page to the Preferences.

Hook

[`PreferenceData`](../modules/c4d.plugins/BaseData/NodeData/PreferenceData/index.md#c4d.plugins.PreferenceData)

Registration

[`RegisterPreferencePlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterPreferencePlugin)

| Example | Description |
|---|---|
| [py_msc_preference.pyp](../examples/plugins/py_msc_preference/py_msc_preference.pyp.md) | Demonstrates how to implement a preference category in the Cinema 4D preference dialog, exposing parameters as global preferences. |

Module-Level Hooks

Render tokens

Replaces tokens in render paths.

Hook

Render tokens

Registration

[`RegisterToken()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterToken), [`RegisterHiddenToken()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterHiddenToken)

| Example | Description |
|---|---|
| [py_msc_render_token.pyp](../examples/plugins/py_msc_render_token/py_msc_render_token.pyp.md) | Demonstrates how to register two Tokens, one visible in the render settings and the other not. |

`PluginMessage()`

Receives startup, menu, and shutdown messages.

Hook

[`PluginMessage()`](#PluginMessage)

Registration

Define the function in the plugin module

See also

[Plugin Messages](#plugin-messages)

| Example | Description |
|---|---|
| [py_msc_licensing.pyp](../examples/plugins/py_msc_licensing/py_msc_licensing.pyp.md) | Demonstrates how to implement licensing checks in plugins. |
| [py_msc_menu.pyp](../examples/plugins/py_msc_menu/py_msc_menu.pyp.md) | Demonstrates how to build custom menus for your plugins. |

## Writing and Registering Hooks <a id="writing-and-registering-hooks"></a>

Hook classes derive from [`BaseData`](../modules/c4d.plugins/BaseData/index.md#c4d.plugins.BaseData) and override the callbacks they need. For example, a [`CommandData`](../modules/c4d.plugins/BaseData/CommandData/index.md#c4d.plugins.CommandData) runs when the user invokes its command:

```python
import c4d

class HelloCommand(c4d.plugins.CommandData):
    """Prints a message when the command is executed."""

    def Execute(self, doc: c4d.documents.BaseDocument) -> bool:
        print("Hello from a command!")
        return True
```

### Registration <a id="registration"></a>

Every hook is made known to Cinema 4D with a dedicated `Register*()` function in [`c4d.plugins`](../modules/c4d.plugins/index.md#c4d.plugins). Which argument that function expects depends on the hook:

- Hooks that exist once per session, such as `CommandData`, `MessageData`, or `ToolData`, take an *instance* of your class via the `dat` argument.
- Hooks that exist once per scene element, such as `ObjectData`, `TagData`, or `ShaderData`, take the *class* itself via the `g` argument, so that Cinema 4D can create one instance for each node. These hooks also take the name of the *description* resource that defines their parameters.

```python
PLUGIN_ID: int = ...  # Replace with your unique ID from developers.maxon.net.

c4d.plugins.RegisterCommandPlugin(
    id=PLUGIN_ID, str="Hello Command", info=0, icon=None, help="Says hello.", dat=HelloCommand())
```

For an object plugin, pass `g=MyObjectData` (the class, not an instance) to [`RegisterObjectPlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.RegisterObjectPlugin) and provide its `description` resource name and object flags. See [py_obj_double_circle](../examples/plugins/py_obj_double_circle/py_obj_double_circle.pyp.md) for a complete example.

Registration functions return `True` on success. Do this work inside an `if __name__ == "__main__":` block, as the SDK examples do, so that importing the module from elsewhere does not register the plugin twice.

> **Warning:** The ID passed to a registration function must be globally unique. If two plugins claim the same ID, only one of them is loaded at startup. *Always* obtain IDs from the plugin ID generator on [developers.maxon.net](https://developers.maxon.net/) to avoid collisions.

The `info` argument takes `PLUGINFLAG_*` flags. Use `PLUGINFLAG_HIDEPLUGINMENU` to place a command in a custom menu without duplicating its default entry ([Enhancing the Main Menu](#enhancing-main-menu)). For localized plugin names and help text, load `str` and `help` from string resources ([Resource Files](#plugin-resources)).

### Scene Nodes and Their Hooks <a id="scene-nodes-and-their-hooks"></a>

Hooks for scene elements, such as `ObjectData` or `TagData`, split a plugin into two layers.

- The **scene layer** consists of the nodes in the document, e.g., [`BaseObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) and [`BaseTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag), which share the base class [`BaseList2D`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D). Cinema 4D creates, stores, and manages these nodes. You only work with them through the node API.
- The **implementation layer** consists of the instances of your hook class. It is yours: you decide what a node generates, draws, or does, and which data it keeps.

You register a hook class only once. Cinema 4D then creates one instance of it for each node of that type, and links the node and its instance with each other. Built-in nodes, such as the *Cube* in the diagram, have no Python implementation.

![The two layers of a node plugin The scene layer, driven by Cinema 4D, contains the document tree with nodes: two BaseObject nodes and a BaseTag with a Python hook, and a plain Cube without one. The implementation layer, provided by the plugin, contains one class MyObjectData registered once with one instance per object node, and one class MyTagData with one instance for the tag. Each node reaches its instance with GetNodeData. Cinema 4D passes the node into the callbacks of the instance, for example Init and GetVirtualObjects.](../_images/inline/manuals_manual_implementing_plugins_0.svg)

*Fig. 1: The two layers of node plugins. The scene tree is driven by Cinema 4D, the instances of the registered hook classes are provided by the plugin.*

The two sides see each other in different ways:

- A node is mostly opaque about its implementation. It only hands it out when explicitly asked, with [`BaseList2D.GetNodeData()`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D.GetNodeData). This works for Python-defined nodes only.
- An implementation is always given the node it is working for, as an argument of its callbacks, e.g., `node` in [`NodeData.Init`](../modules/c4d.plugins/BaseData/NodeData/index.md#c4d.plugins.NodeData.Init) or `op` in `ObjectData.GetVirtualObjects`. Outside of callbacks, [`NodeData.Get()`](../modules/c4d.plugins/BaseData/NodeData/index.md#c4d.plugins.NodeData.Get) returns the node of an instance.

This also defines the lifetime of an instance:

- **When you pass an *instance* to the registration function, that instance is kept for the whole Cinema 4D session.** This applies to command and message hooks, which have no scene node.
- **When you pass a *class* to the registration function, there is a *1:1* relationship between an instance and a node** in the scene. Cinema 4D creates and frees the implementation with the node, calling [`NodeData.Init`](../modules/c4d.plugins/BaseData/NodeData/index.md#c4d.plugins.NodeData.Init) after construction and [`NodeData.Free`](../modules/c4d.plugins/BaseData/NodeData/index.md#c4d.plugins.NodeData.Free) before destruction. The node link is not available in the constructor; initialize node parameters in `Init()`.

### Threading and Startup <a id="threading-and-startup"></a>

Many hook methods, such as `GetVirtualObjects` or the `Execute` method of a tag, are called from a threading context, where you must not modify the document or touch the GUI. The module level code of a plugin runs in the restricted boot phase of Cinema 4D. Avoid GUI operations, long running file operations, or web requests there. See [Scene Execution](manual_scene_execution.md) for the execution model and [Licensing](manual_licensing.md) for the consequences of the boot phase.

## Plugin Files <a id="plugin-files"></a><a id="directory-structure"></a>

Cinema 4D searches the *plugins* folder in the user preferences folder at startup, and executes every file with the suffix `.pyp`, or `.pypv` for encrypted plugin files. A `.pyp` file can be placed directly into that folder, but it is usually better to group a plugin in a subfolder.

A plugin with resources typically has this layout:

```text
myPlugin/
├── myPlugin.pyp                    # The plugin module, registers the hooks.
├── myIcon.tif                      # Any other files the plugin needs, e.g., icons.
└── res/                            # The plugin resources.
    ├── c4d_symbols.h               # Global symbols of the plugin, e.g., string and dialog IDs.
    ├── description/                # Description resources for objects, tags, shaders, etc.
    │   ├── omyobject.h             # The parameter symbols of the description.
    │   └── omyobject.res           # The parameter layout of the description.
    ├── dialogs/                    # Dialog resources for GeDialog.
    │   └── idd_main.res
    ├── strings_en-US/              # The English strings, required.
    │   ├── c4d_strings.str         # Generic strings, e.g., the plugin name and help text.
    │   ├── description/
    │   │   └── omyobject.str       # The strings of the description.
    │   └── dialogs/
    │       └── idd_main.str        # The strings of the dialog.
    └── strings_de-DE/              # Any other language, same structure as en-US.
        └── ...
```

The `.pyp` file registers hooks; `res` holds descriptions, dialogs, and translations. Locate assets relative to `__file__` rather than the process working directory:

```python
import os

pluginFolder: str = os.path.dirname(__file__)
iconPath: str = os.path.join(pluginFolder, "myIcon.tif")
```

> **Warning:** If the console reports *Could not find required ‘__res__’.* at startup, check the plugin’s `res` directory and its required symbol and string files.

## Resource Files <a id="resource-files"></a><a id="plugin-resources"></a>

Resources separate the *definition* of an interface and its text from the code that drives it. A plugin that implements an object, tag, or shader *needs* a description resource to expose its parameters. A plugin with a dialog *can* define it in a dialog resource instead of building it in code. Any plugin *should* put user-facing strings into string tables, so that it can be translated.

This section covers the files and their folders. [Dialog and Description Resources](manual_resource_files.md) explains how to write dialog and description resources.

| File | Purpose |
|---|---|
| `c4d_symbols.h` | Declares the global symbols of the plugin as an `enum`: string IDs (`IDS_`), dialog IDs (`IDD_`), gadget IDs (`IDC_`), and optionally the plugin ID. The prefixes are a Cinema 4D convention, not a requirement. |
| `description/*.res`, `*.h` | The parameter layout of an object, tag, shader, or other scene element, and the symbols for its parameters. The file name must match the `description` argument of the registration function, e.g., `Omyobject`. |
| `dialogs/*.res` | The markup of a dialog, loaded with [`GeDialog.LoadDialogResource()`](../modules/c4d.gui/GeDialog/index.md#c4d.gui.GeDialog.LoadDialogResource). |
| `strings_<language>/**/*.str` | The strings for a language. Each `.res` file needs a `.str` file with the same name in the same relative folder, and `c4d_strings.str` holds all other strings. |

### Using Symbols and Strings <a id="using-symbols-and-strings"></a>

The symbols of description headers are available as attributes of `c4d`, e.g., `c4d.PYCIRCLEOBJECT_RAD`. The symbols in `c4d_symbols.h` are not. Import them into the module namespace with [`mxutils.ImportSymbols()`](../modules/mxutils_api.md#mxutils.ImportSymbols), see [Symbol Parsing](manual_symbol_parsing.md), and load a localized string with [`c4d.plugins.GeLoadString()`](../modules/c4d.plugins/index.md#c4d.plugins.GeLoadString):

```python
import os
import typing

import c4d
import mxutils

# Makes ID_PLUGIN, IDS_PLUGIN_NAME, etc. available as module attributes.
mxutils.ImportSymbols(os.path.join(os.path.dirname(__file__), "res"))
if typing.TYPE_CHECKING:  # Silences linters, which cannot see resource symbols.
    ID_PLUGIN: int
    IDS_PLUGIN_NAME: int
    IDS_PLUGIN_HELP: int

name: str = c4d.plugins.GeLoadString(IDS_PLUGIN_NAME)
help: str = c4d.plugins.GeLoadString(IDS_PLUGIN_HELP)
```

A string table in `strings_en-US/c4d_strings.str` looks like this:

```c4dstr
STRINGTABLE
{
    IDS_PLUGIN_NAME "Py SDK - Resource Gui";
    IDS_PLUGIN_HELP "Opens a dialog window that is populated using resource files.";
}
```

[`GeLoadString()`](../modules/c4d.plugins/index.md#c4d.plugins.GeLoadString) returns the string in the current language of Cinema 4D, and falls back to *en-US* when the plugin has no translation for it.

Functions such as `GeLoadString` and `LoadDialogResource` use the [`GeResource`](../modules/c4d.plugins/GeResource/index.md#c4d.plugins.GeResource) stored in the plugin module’s global `__res__`. Cinema 4D normally creates it for `.pyp` files. When loading resources from another module or location, initialize a resource once and share it among the modules that need it:

```python
if __name__ == "__main__":
    res: c4d.plugins.GeResource | None = globals().get("__res__", None)
    if not isinstance(res, c4d.plugins.GeResource):
        res = c4d.plugins.GeResource()
        if not res.Init(os.path.join(os.path.dirname(__file__), "res")):
            raise RuntimeError("Failed to initialize the plugin resources.")
        __res__ = res

    MyCommand.Register()
```

> **Note:** [py_cmd_gui_resources](../examples/plugins/py_cmd_gui_resources/py_cmd_gui_resources.pyp.md) builds a dialog from two resources, loads translated strings, and shows manual `__res__` initialization. For a node description and its `description` registration argument, see [py_obj_double_circle](../examples/plugins/py_obj_double_circle/py_obj_double_circle.pyp.md).

## Localization <a id="localization"></a>

For each language a plugin supports, there must be a `strings_<language>` folder named after the language code. The languages that ship with Cinema 4D, as defined in its `resource/language` folder, are:

| Folder | Language |
|---|---|
| `strings_en-US` | English (required, fallback language) |
| `strings_de-DE` | German |
| `strings_es-ES` | Spanish |
| `strings_fr-FR` | French |
| `strings_it-IT` | Italian |
| `strings_ja-JP` | Japanese |
| `strings_ko-KR` | Korean |
| `strings_pt-BR` | Brazilian Portuguese |
| `strings_zh-CN` | Simplified Chinese |

A plugin is not required to support all of them. Develop it in *en-US* first, then copy the strings folder for each translation. Other languages can be introduced by adding a folder named after the scheme above to the `resource/language` folder of Cinema 4D and placing a `language.txt` file in it which contains the display name of the language.

> **Note:** Before R20, languages were named by a short code, e.g., `strings_us` for English or `strings_jp` for Japanese. `strings_us` is still picked up for compatibility, but new plugins should use `strings_en-US`.

> **Warning:** Non-ASCII characters in `.str` files, e.g., in Chinese, Japanese, French, or German strings, must be written as ASCII escape sequences. Cinema 4D has no built-in tool for this conversion; the example script `unicode_encode_strings.py` is a starting point for a conversion pipeline.

## Plugin Messages <a id="plugin-messages"></a><a id="id1"></a>

Besides hooks, a plugin module can define the function `PluginMessage`. Cinema 4D calls it for lifecycle events, such as startup, menu building, and shutdown. Other plugins can send messages to it via [`c4d.GePluginMessage()`](../modules/c4d/index.md#c4d.GePluginMessage). The function is called for every plugin module that defines it. This is distinct from the `MessageData` hook, which receives core messages of the application.

### `PluginMessage(id, data)` <a id="PluginMessage"></a>

Called to receive plugin messages. These can either be from Cinema 4D or from other plugins via [`GePluginMessage()`](../modules/c4d/index.md#c4d.GePluginMessage).

**Parameters:**

- **id** (*int*) –

  The message ID. Built-in ones are:

  |   |   |
  |---|---|
  | *C4DPL_INIT_SYS* | Initialize system. |
  | *C4DPL_INIT* | Initialize the plugin, calling *PluginStart*. |
  | *C4DPL_END* | End the plugin, calling *PluginEnd*. |
  | *C4DPL_MESSAGE* | Receive plugin message, calling *PluginMessage*. |
  | *C4DPL_BUILDMENU* | Called when the menus are built during startup. Use [`GetMenuResource()`](../modules/c4d.gui/index.md#c4d.gui.GetMenuResource) etc. to add own menus here if necessary. See the [example](#enhancing-main-menu). |
  | *C4DPL_STARTACTIVITY* | Sent to all plugins after all *PluginStart* have been called. |
  | *C4DPL_ENDACTIVITY* | Sent to all plugins before any *PluginEnd* has been called. This allows to close dialogs, end threads, delete temporary/undo buffers etc. |
  | *C4DPL_CHANGEDSECURITYTOKEN* | Sent to all plugins if the Security Token of Team Render was changed. |
  | *C4DPL_SHUTDOWNTHREADS* | Sent to all plugins before the threading system of Cinema 4D is shutdown. After that no threads should be started. |
  | *C4DPL_LAYOUTCHANGED* | Sent to all plugins after the layout has been switched. |
  | *C4DPL_RELOADPYTHONPLUGINS* | Sent when Python plugins are to be reloaded. See [Plugin Messages](#plugin-messages). |
  | *C4DPL_COMMANDLINEARGS* | Sent to let plugins parse the command line arguments used when starting Cinema 4D. Retrieve the arguments by calling [sys.argv](https://docs.python.org/3.9/library/sys.html#sys.argv). See [Command Line Arguments](#commandline-args). |
  | *C4DPL_EDITIMAGE* | Sent to allow plugins to start any other actions when Cinema 4D tries to show an image (e.g. in the shader popup). *data* is dict{‘imagefn’: str, filename of the image that triggered the message} |
  | *C4DPL_ENDPROGRAM* | Sent when Cinema 4D is about to close. *data* is dict{‘cancel’: bool, set to **True** to cancel close of Cinema 4D} |
  | *C4DPL_DEVICECHANGE* | Sent when a device has changed. *data* is dict{‘name’: str, name of the device, ‘eject’: bool Eject, state of the device} |
  | *C4DPL_NETWORK_CHANGE* | Sent to all plugins if the network configuration on the system changed. |
  | *C4DPL_SYSTEM_SLEEP* | Sent to all plugins if the system goes to sleep. |
  | *C4DPL_SYSTEM_WAKE* | Sent to all plugins if the system wakes up. |
  | *C4DPL_PROGRAM_STARTED* | Sent when the application has been started. |

- **data** (*any*) – The message data.

**Return type:** bool

**Returns:** **True** if the message was consumed, otherwise **False**.

### Command Line Arguments <a id="command-line-arguments"></a><a id="commandline-args"></a>

To read the command line arguments of Cinema 4D, filter the *C4DPL_COMMANDLINEARGS* message in [`PluginMessage()`](#PluginMessage):

```python
import c4d
import sys

def PluginMessage(id: int, data: object) -> bool:
    if id == c4d.C4DPL_COMMANDLINEARGS:
        print(sys.argv)
        return True

    return False
```

Save this code as a `.pyp` file in the plugins folder, start Cinema 4D with arguments such as `Cinema 4D.exe --hello`, and open the console to see them.

> **Warning:** Arguments which are handled by Cinema 4D modules are removed from the list. When you start Cinema 4D with `--hello -parallel`, `-parallel` will not show up in the printed arguments.

> **Note:** *Reload Python Plugins* recompiles and executes `.pyp` files, but does not reload modules they imported. Handle *C4DPL_RELOADPYTHONPLUGINS* in [`PluginMessage()`](#PluginMessage) to release open resources such as sockets or files, and use `importlib.reload()` if an imported module must also be reloaded.

## Enhancing the Main Menu <a id="enhancing-the-main-menu"></a><a id="enhancing-main-menu"></a>

Cinema 4D builds its menus at startup and when plugins are reloaded, and announces this with *C4DPL_BUILDMENU*. This is the moment to add custom menus. Find the Extensions menu with [`c4d.gui.SearchPluginMenuResource()`](../modules/c4d.gui/index.md#c4d.gui.SearchPluginMenuResource), cast the result to a [`BaseContainer`](../modules/c4d/BaseContainer/index.md#c4d.BaseContainer), and insert `MENURESOURCE_*` entries. Reference a registered command by `PLUGIN_CMD_<ID>`; Cinema 4D supplies its localized name and icon. For example, with `PLUGIN_ID` set to the ID of your registered command:

```python
import c4d

def PluginMessage(mid: int, data: object) -> bool:
    if mid != c4d.C4DPL_BUILDMENU:
        return False

    resource: object = c4d.gui.SearchPluginMenuResource("IDS_EDITOR_PIPELINE")
    extensions: c4d.BaseContainer | None = c4d.Cast(None, resource)
    if extensions is None:
        return False

    menu: c4d.BaseContainer = c4d.BaseContainer()
    menu.InsData(c4d.MENURESOURCE_SUBTITLE, "My Menu")
    menu.InsData(c4d.MENURESOURCE_COMMAND, f"PLUGIN_CMD_{PLUGIN_ID}")
    extensions.InsData(c4d.MENURESOURCE_SUBMENU, menu)
    return True
```

Check whether the submenu already exists before inserting it when menus are rebuilt. If you modify menus outside *C4DPL_BUILDMENU*, call [`c4d.gui.UpdateMenus()`](../modules/c4d.gui/index.md#c4d.gui.UpdateMenus).

To avoid duplicate menu entries, register the command with `PLUGINFLAG_HIDEPLUGINMENU`. Load submenu titles from string resources with [`GeLoadString()`](../modules/c4d.plugins/index.md#c4d.plugins.GeLoadString) when they need translation.

> **Note:** [py_msc_menu](../examples/plugins/py_msc_menu/py_msc_menu.pyp.md) builds a localized *Python SDK* submenu in *Extensions*. It hides the default entries of the SDK plugins and skips unavailable commands. This menu code can live alongside other hooks in a plugin; its resources use the legacy `strings_us` name.

## See Also <a id="see-also"></a>

- [Dialog and Description Resources](manual_resource_files.md): Explains how to define dialogs and node parameters with resource files, and how to use them from Python.
- [Message System](manual_message_system.md): Explains messages between Cinema 4D scene elements and interfaces.
- [Scene Execution](manual_scene_execution.md): Explains how Cinema 4D updates a scene, and where Python code runs in that process.
- [Licensing](manual_licensing.md): Explains licensing for Python plugins in Cinema 4D.
- [Example py_cmd_gui_resources.pyp](../examples/plugins/py_cmd_gui_resources/py_cmd_gui_resources.pyp.md): Demonstrates a plugin that uses resources to define its dialog layout and string translations.
- [Example py_msc_menu.pyp](../examples/plugins/py_msc_menu/py_msc_menu.pyp.md): Demonstrates how to build custom menus for your plugins.
- [Example py_obj_double_circle.pyp](../examples/plugins/py_obj_double_circle/py_obj_double_circle.pyp.md): Demonstrates how to implement a spline object generator with handles to drive parameters.
