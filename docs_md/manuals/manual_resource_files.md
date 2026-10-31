<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_resource_files.html -->

# Dialog and Description Resources <a id="dialog-and-description-resources"></a>

Explains how to define dialogs and node parameters with resource files, and how to use them from Python.

Cinema 4D defines user interfaces in *resource files*: small text files in the `res` folder of a plugin. Two kinds are relevant for plugin development:

- A **dialog resource** defines the layout of a [`GeDialog`](../modules/c4d.gui/GeDialog/index.md#c4d.gui.GeDialog): groups, labels, buttons, and input fields.
- A **description resource** defines the *parameters* of a scene element such as an object, tag, or shader. Cinema 4D builds the Attribute Manager page of the element from it, and stores, animates, and serializes the values.

Both kinds share the same markup, symbol, and string files. This manual explains these basics first, and then each kind with a practical example. It is a guide, not a reference: the [Resource Index](../indexes/resource_index.md) lists the descriptions and description data types that ship with Cinema 4D. The [Implementing Plugins](manual_implementing_plugins.md) manual explains where the `res` folder lives, how languages are organized, and how a plugin loads its resources.

|  | Dialog Resource | Description Resource |
|---|---|---|
| Defines | The layout of a `GeDialog` | The parameters of a node, tool, or preference page |
| Markup file | `res/dialogs/<name>.res` with a `DIALOG` block | `res/description/<name>.res` with a `CONTAINER` block |
| Symbols | `res/c4d_symbols.h` | `res/description/<name>.h` |
| Strings | `strings_<language>/dialogs/<name>.str` with `DIALOGSTRINGS` | `strings_<language>/description/<name>.str` with `STRINGTABLE` |
| Loaded by | [`GeDialog.LoadDialogResource()`](../modules/c4d.gui/GeDialog/index.md#c4d.gui.GeDialog.LoadDialogResource) | The `description` argument of the `Register*Plugin()` function |
| Values | You read and write them with the gadget ID, e.g., `GetFloat()` | Cinema 4D stores them in the node, you access them with `node[ID]` |
| Optional | Yes, a dialog can also be built in code | Not for parameters of a node, unless they are added dynamically |

## The res Folder at a Glance <a id="the-res-folder-at-a-glance"></a>

All resources of a plugin live in its `res` folder, next to the `.pyp` file. This is a plugin that has one dialog and one object description, translated into two languages:

```text
myPlugin/
├── myPlugin.pyp
└── res/
    ├── c4d_symbols.h                 # Global symbols: dialog IDs, gadget IDs, string IDs.
    ├── dialogs/
    │   └── idd_values.res            # DIALOG IDD_VALUES
    ├── description/
    │   ├── opyexample.res            # CONTAINER Opyexample
    │   └── opyexample.h              # The parameter symbols of Opyexample.
    ├── strings_en-US/                # The strings of a language, required.
    │   ├── c4d_strings.str           # Generic strings, e.g., the plugin name.
    │   ├── dialogs/
    │   │   └── idd_values.str        # DIALOGSTRINGS IDD_VALUES
    │   └── description/
    │       └── opyexample.str        # STRINGTABLE Opyexample
    └── strings_de-DE/                # Another language, with the same structure.
        └── ...
```

The files of one resource are tied together by their names, which must be spelled the same everywhere:

- A **dialog** `idd_values` consists of `dialogs/idd_values.res` with `DIALOG IDD_VALUES`, a symbol `IDD_VALUES` in `c4d_symbols.h`, and `dialogs/idd_values.str` in each language with `DIALOGSTRINGS IDD_VALUES`.
- A **description** `opyexample` consists of `description/opyexample.res` with `CONTAINER Opyexample`, `description/opyexample.h`, and `description/opyexample.str` in each language with `STRINGTABLE Opyexample`. The same name is passed as `description` to the registration function.

Keep the names in sync. A mismatch between the file, container, and string table is a common cause of a description that does not load, or that shows no labels. Cinema 4D writes its own files with a lowercase file name and a capitalized symbol, e.g., `ocube.res` with `CONTAINER Ocube`, and the SDK examples do the same.

## Shared Basics <a id="shared-basics"></a>

### Markup <a id="markup"></a>

Resource files are a tree of blocks. A block consists of a type, an optional ID, and braces with flags and child blocks. Flags end with a semicolon, and `//` starts a comment:

```c4dres
ELEMENTTYPE ELEMENT_ID
{
    FLAG;
    FLAG value;
    CHILDTYPE { FLAG; }
}
```

The ID of an element is a symbol from a header file. It is optional for elements that you never address, such as a label. Text is never written into the markup: flags like `NAME` take the symbol of a string, so that every text can be translated.

### Symbols <a id="symbols"></a>

Symbols are defined in a C style header with an `enum`. The files are parsed by Cinema 4D, and are not compiled:

```cpp
#ifndef C4D_SYMBOLS_H__
#define C4D_SYMBOLS_H__

enum
{
    IDD_VALUES = 1100,    // A dialog.
    IDC_VALUE_A,          // 1101, a gadget in the dialog.
    IDS_VALUE_A,          // 1102, a string.

    __DUMMY__             // Marks the end of the enumeration.
};

#endif
```

The symbols of a description header are available in Python as attributes of `c4d`, e.g., `c4d.PYCIRCLEOBJECT_RAD`. Import the symbols of other headers, such as `c4d_symbols.h`, into your module with [`mxutils.ImportSymbols()`](../modules/mxutils_api.md#mxutils.ImportSymbols). See [Symbol Parsing](manual_symbol_parsing.md) for how the parser works.

### Strings <a id="strings"></a>

A string file maps symbols to text, once for each language in a `strings_<language>` folder. Dialogs and descriptions use different table types, and the table name must match the name of the resource:

```c4dstr
// strings_en-US/dialogs/idd_values.str
DIALOGSTRINGS IDD_VALUES
{
    IDS_VALUE_A "Value A";
}

// strings_en-US/description/opydoublecircle.str
STRINGTABLE Opydoublecircle
{
    Opydoublecircle     "Double Circle";
    PYCIRCLEOBJECT_RAD  "Radius";
}
```

Generic strings, e.g., for a plugin name, live in `c4d_strings.str` and are loaded with [`c4d.plugins.GeLoadString()`](../modules/c4d.plugins/index.md#c4d.plugins.GeLoadString). Non-ASCII characters must be written as `\uHHHH` escapes, see [Resource Files](manual_implementing_plugins.md#plugin-resources) for the details and the available languages.

> **Note:** Cinema 4D parses resource files and symbols when it starts. Restart it after you changed one of them.

## Dialog Resources <a id="dialog-resources"></a>

A dialog resource places the elements of a [`GeDialog`](../modules/c4d.gui/GeDialog/index.md#c4d.gui.GeDialog). Cinema 4D arranges them dynamically: you do not specify positions, but relations between elements, so that a dialog adapts to the language, the display scale, and the size of its window.

### A First Dialog <a id="a-first-dialog"></a>

This resource defines a group with two columns, one label and input field per row:

```c4dres
// res/dialogs/idd_values.res
DIALOG IDD_VALUES
{
    SCALE_H; SCALE_V;               // Use all the space the parent offers.

    GROUP
    {
        COLUMNS 2;                  // Two elements per row: label, field.
        SPACE 5, 5;                 // Padding between the elements.

        STATICTEXT { NAME IDS_VALUE_A; }
        EDITNUMBERARROWS IDC_VALUE_A { SIZE 100, 0; SCALE_H; }

        STATICTEXT { NAME IDS_VALUE_B; }
        EDITNUMBERARROWS IDC_VALUE_B { SIZE 100, 0; SCALE_H; }
    }
}
```

The dialog class only loads it and then talks to the elements by their IDs:

```python
import os
import c4d
import mxutils

mxutils.ImportSymbols(os.path.join(os.path.dirname(__file__), "res"))

class ValuesDialog(c4d.gui.GeDialog):

    def CreateLayout(self) -> bool:
        return self.LoadDialogResource(IDD_VALUES)

    def InitValues(self) -> bool:
        self.SetFloat(IDC_VALUE_A, 42.0)
        self.SetFloat(IDC_VALUE_B, 3.14159)
        return True
```

[`LoadDialogResource()`](../modules/c4d.gui/GeDialog/index.md#c4d.gui.GeDialog.LoadDialogResource) does not finalize the dialog. You can call it multiple times to assemble a dialog from reusable parts, and mix it with the `Add*` methods of `GeDialog`. Dialog resources are optional: they are mostly useful when a dialog is large, is composed from recurring parts, or must be localized. The complete, runnable version of this example is [py_cmd_gui_resources](../examples/plugins/py_cmd_gui_resources/py_cmd_gui_resources.pyp.md).

### Groups and Layout <a id="groups-and-layout"></a>

Everything in a dialog is placed in a `GROUP`. A group arranges its children in `COLUMNS` from left to right, and top to bottom. Nest groups to build complex layouts. These flags control the group:

| Flag | Effect |
|---|---|
| `COLUMNS n` | The number of columns. Elements fill a row before they start a new one. |
| `SPACE x, y` | The padding between the elements, in pixels. |
| `BORDERSIZE l, t, r, b` | The padding between the group and its content, in pixels. |
| `NAME id` | The title of the group or tab, a string symbol. |

Most elements additionally accept layout flags. Cinema 4D always gives an element at least the space it asks for. The flags say what happens when more space is available:

| Flag | Effect |
|---|---|
| `SCALE_H`, `SCALE_V` | The element may grow horizontally or vertically. Without it, the element keeps its size. |
| `FIT_H`, `FIT_V` | The element fills the space that is available for it. |
| `ALIGN_LEFT`, `ALIGN_RIGHT`, `ALIGN_TOP`, `ALIGN_BOTTOM` | Aligns the element within its space. |
| `CENTER_H`, `CENTER_V` | Centers the element within its space, e.g., a label next to a taller field. |
| `SIZE w, h` | The requested size. Negative values are pixels, `SIZE -100, -20` is 100 by 20 pixels. Positive values are in tenths of a character width and line height, so `SIZE 100, 10` is 10 characters wide and one line high. 0 means the default size of the element. |

### Common Elements <a id="common-elements"></a>

| Element | Purpose |
|---|---|
| `STATICTEXT` | A label, with the text defined by `NAME`. |
| `BUTTON` | A button with a `NAME` that sends a command to the dialog. |
| `CHECKBOX` | A boolean checkbox. |
| `EDITTEXT`, `MULTILINEEDIT` | A single line and a multi line text field. |
| `EDITNUMBER`, `EDITNUMBERARROWS` | A numeric field, optionally with arrows. |
| `EDITSLIDER`, `SLIDER` | A numeric field with a slider, and a slider only. |
| `COMBOBOX`, `POPUPBUTTON` | A drop down list, filled with a `CHILDS` block. |
| `TAB`, `SCROLLGROUP` | A group with tabs, and a scrollable group. |
| `SEPARATOR` | A dividing line. |
| `DLGGROUP` | A standard button row, e.g., `DLGGROUP { OK; CANCEL; }`. |

The [Dialog Resource](https://developers.maxon.net/docs/cpp/2026_3_0/page_dialog_resource.html) page of the C++ documentation lists all element types with their flags. Custom GUI elements, such as a bitmap button, are available too.

### A Typical Form <a id="a-typical-form"></a>

A form with a text field, a drop down, and the standard buttons. The entries of a `COMBOBOX` are pairs of an ID and a string symbol, and the ID is the value that the dialog reports for the selected entry:

```c4dres
DIALOG IDD_EXPORT
{
    NAME IDS_EXPORT;
    SCALE_H;

    GROUP
    {
        COLUMNS 2; SPACE 6, 4; BORDERSIZE 8, 8, 8, 8; SCALE_H;

        STATICTEXT { NAME IDS_NAME; CENTER_V; ALIGN_LEFT; }
        EDITTEXT IDC_NAME { SCALE_H; }

        STATICTEXT { NAME IDS_FORMAT; CENTER_V; ALIGN_LEFT; }
        COMBOBOX IDC_FORMAT
        {
            SCALE_H;
            CHILDS
            {
                IDC_FORMAT_OBJ, IDS_FORMAT_OBJ;
                IDC_FORMAT_FBX, IDS_FORMAT_FBX;
            }
        }
    }

    DLGGROUP { OK; CANCEL; }
}
```

```python
class ExportDialog(c4d.gui.GeDialog):

    def CreateLayout(self) -> bool:
        return self.LoadDialogResource(IDD_EXPORT)

    def InitValues(self) -> bool:
        self.SetString(IDC_NAME, "scene")
        self.SetInt32(IDC_FORMAT, IDC_FORMAT_FBX)  # Select an entry by its ID.
        return True

    def Command(self, cid: int, msg: c4d.BaseContainer) -> bool:
        if cid == c4d.DLG_OK:
            print(self.GetString(IDC_NAME), self.GetInt32(IDC_FORMAT) == IDC_FORMAT_FBX)
            self.Close()
        elif cid == c4d.DLG_CANCEL:
            self.Close()
        return True
```

[py_msc_licensing](../examples/plugins/py_msc_licensing/py_msc_licensing.pyp.md) contains a larger dialog resource with tabs, combo boxes, and multi line fields.

## Description Resources <a id="description-resources"></a>

A description resource defines the parameters of a node. A parameter is more than a widget: Cinema 4D creates the interface, stores the value in the node, makes it animatable, and saves it with the scene. Your plugin only has to read and write the value.

### Naming and Files <a id="naming-and-files"></a>

Descriptions are named with a capital prefix for the type of node and a lowercase name. The name is the symbol of the description container, the base name of the three description files, and, by convention, the name of the symbol for the plugin ID. For built-in nodes, all of them are identical: `c4d.Ocube` is the ID of the cube object, and the name of its description.

| Prefix | Node Type | Example Symbol | Example Files |
|---|---|---|---|
| `O` | Objects | `Ocube` | `ocube.res` |
| `T` | Tags | `Tpylookatcamera` | `tpylookatcamera.res` |
| `X` | Shaders | `Xsss` | `xsss.res` |
| `M` | Materials | `Marchigrass` | `marchigrass.res` |
| `VP` | Video posts | `VPcolormapping` | `vpcolormapping.res` |
| `F` | Scene loaders and savers | `Fbase` | `fbase.res` |
| `D` | Data types, e.g., gradient | `Dgradient` | `dgradient.res` |
| `GV` | Graph View nodes | `GVbase` | `gvbase.res` |

Tracks, keys, and sequences have their own prefixes. Look at their base descriptions in the [Resource Index](../indexes/resource_index.md) to see them. Using the cube as an example, a complete description consists of these items, which all use the same name:

| Item | Name |
|---|---|
| Plugin ID symbol | `Ocube` |
| Container in the markup file | `CONTAINER Ocube` |
| Markup file | `description/ocube.res` |
| Symbol file | `description/ocube.h` |
| String file and table | `strings_<language>/description/ocube.str` with `STRINGTABLE Ocube` |

The names of the files, the container, and the string table must be identical, and the same is true for the `description` argument of the registration function. Python plugins are not forced to follow the convention for the plugin ID: the SDK examples store it in a constant such as `PLUGIN_ID`, since the description is found by its name. A symbol named like the description, e.g., `Opyexample = 1065655` in `c4d_symbols.h`, is still the better choice as it makes `node.GetType() == Opyexample` readable. Import it with [`mxutils.ImportSymbols()`](../modules/mxutils_api.md#mxutils.ImportSymbols).

The *Double Circle* object of the SDK is a complete example. It has the symbol `Opydoublecircle`, and consists of `opydoublecircle.res`, `opydoublecircle.h`, and `opydoublecircle.str`:

```c4dres
// res/description/opydoublecircle.res
CONTAINER Opydoublecircle
{
    NAME Opydoublecircle;                   // The name of the object, a string symbol.
    INCLUDE Obase;                          // Inherit the parameters of all objects.

    GROUP ID_OBJECTPROPERTIES               // Place the parameters in the 'Object' tab.
    {
        REAL PYCIRCLEOBJECT_RAD { UNIT METER; MIN 0.0; }
    }
    INCLUDE Osplineprimitive;               // Add the parameters of spline primitives.
}
```

```cpp
// res/description/opydoublecircle.h
#ifndef _Opydoublecircle_H_
#define _Opydoublecircle_H_

enum
{
    PYCIRCLEOBJECT_RAD = 10000  // Start above the IDs of the included descriptions.
};

#endif
```

```c4dstr
// res/strings_en-US/description/opydoublecircle.str
STRINGTABLE Opydoublecircle
{
    Opydoublecircle     "Double Circle";
    PYCIRCLEOBJECT_RAD  "Radius";
}
```

The name in `CONTAINER` is the name that you pass as `description` when you register the hook:

```python
c4d.plugins.RegisterObjectPlugin(
    id=PLUGIN_ID, str="Double Circle", g=DoubleCircleData, description="Opydoublecircle",
    icon=bitmap, info=c4d.OBJECT_GENERATOR | c4d.OBJECT_ISSPLINE)
```

### Structure <a id="structure"></a>

A description is built from these parts:

| Statement | Purpose |
|---|---|
| `NAME id` | The name of the description, a string symbol that is by convention equal to the name of the description. |
| `INCLUDE parent` | Inserts all parameters of another description first. Always include the base of your node type, e.g., `Obase` for objects or `Tbase` for tags, so that your node has the common parameters. |
| `GROUP id { ... }` | A group of parameters, e.g., a tab or a foldable section. Reuse a group of an included description to add your parameters to it, such as `ID_OBJECTPROPERTIES` for objects and `ID_TAGPROPERTIES` for tags. |
| `HIDE id` / `SHOW id` | Hides or shows a parameter of an included description, e.g., `HIDE FALLOFF_SHAPE_AXIS;`. The value remains accessible from code. |
| `TYPE id { flags }` | A parameter, see below. |

### Parameters <a id="parameters"></a>

A parameter is written as a data type, the symbol, and a block of flags. The data type determines the type of the value in Python, and the type that you pass to [`NodeData.InitAttr()`](../modules/c4d.plugins/BaseData/NodeData/index.md#c4d.plugins.NodeData.InitAttr):

| Data Type | Python Type | Interface |
|---|---|---|
| `BOOL` | `bool` | A checkbox. |
| `LONG` | `int` | An integer field. With `CYCLE` a drop down, with `CUSTOMGUI LONGSLIDER` a slider. |
| `REAL` | `float` | A float field, optionally with a unit or a slider. |
| `VECTOR`, `COLOR` | `c4d.Vector` | Three values, or a color picker. |
| `STRING` | `str` | A text field. |
| `BASETIME` | `c4d.BaseTime` | A time field. |
| `LINK` | `c4d.BaseList2D` | A link field that accepts a node. |
| `BUTTON` | None | A button that sends a command to the node, it has no value. |
| `SEPARATOR`, `STATICTEXT` | None | Layout elements without a value. |

The data types and flags that exist in the resources of Cinema 4D change with each release. Use the [Description Data Types](../indexes/resource_index.md) view of the [Resource Index](../indexes/resource_index.md) to see every type and flag that is used in practice, including examples. Its [Descriptions](../indexes/resource_index.md) view shows the parameters and source files of built-in descriptions: use it to find the description to `INCLUDE`, to look up a parameter ID, and to learn how Cinema 4D itself writes a certain interface.

Common flags are:

| Flag | Effect |
|---|---|
| `MIN v`, `MAX v` | Limits the value. |
| `MINSLIDER v`, `MAXSLIDER v`, `CUSTOMGUI REALSLIDER` | The range of a slider, and the slider itself. `LONGSLIDER` is the integer variant. |
| `STEP v` | The step of the field arrows. |
| `UNIT METER` / `DEGREE` / `PERCENT` | Displays the value with a unit. `METER` values scale with the object when the user scales it. |
| `CYCLE { SYMBOL; ... }` | The entries of a `LONG` drop down. The value of an entry is the value of its symbol. |
| `ACCEPT { Obase; }` | The node types a `LINK` accepts, e.g., only objects. |
| `ANIM OFF` | The parameter cannot be animated. |
| `SCALE_H`, `FIT_H` | Layout flags like in dialogs. |
| `SEPARATOR { LINE; }` | A separator with a visible line. |
| `COLUMNS n`, `DEFAULT 1`, `OPEN` | For groups: the number of columns, and whether the group is unfolded by default. |

### A Complete Example <a id="a-complete-example"></a>

This description of an object combines the common elements. A parameter ID must be unique within the description, and also within the descriptions that it includes. Since `Obase` and spline descriptions reserve many low IDs, start your own at 10000:

```c4dres
CONTAINER Opyexample
{
    NAME Opyexample;
    INCLUDE Obase;

    GROUP ID_OBJECTPROPERTIES
    {
        REAL PYEXAMPLE_RADIUS { UNIT METER; MIN 0.0; }
        REAL PYEXAMPLE_STRENGTH
        {
            UNIT PERCENT; MIN 0.0; MAX 100.0; CUSTOMGUI REALSLIDER; SCALE_H;
        }

        GROUP PYEXAMPLE_GROUP_MODE
        {
            DEFAULT 1;
            COLUMNS 1;

            LONG PYEXAMPLE_MODE { CYCLE { PYEXAMPLE_MODE_FAST; PYEXAMPLE_MODE_ACCURATE; } }
            BOOL PYEXAMPLE_SMOOTH { }
        }

        SEPARATOR { LINE; }
        LINK PYEXAMPLE_SOURCE { ACCEPT { Obase; } }
        BUTTON PYEXAMPLE_RESET { }
    }
}
```

```cpp
enum
{
    PYEXAMPLE_RADIUS = 10000,
    PYEXAMPLE_STRENGTH,
    PYEXAMPLE_GROUP_MODE,
    PYEXAMPLE_MODE,
    PYEXAMPLE_MODE_FAST = 0,        // The entries of a cycle are the values of the parameter.
    PYEXAMPLE_MODE_ACCURATE = 1,
    PYEXAMPLE_SMOOTH = 10010,
    PYEXAMPLE_SOURCE,
    PYEXAMPLE_RESET
};
```

```c4dstr
STRINGTABLE Opyexample
{
    Opyexample              "Example Object";

    PYEXAMPLE_RADIUS        "Radius";
    PYEXAMPLE_STRENGTH      "Strength";
    PYEXAMPLE_GROUP_MODE    "Mode";
    PYEXAMPLE_MODE          "Mode";
    PYEXAMPLE_MODE_FAST     "Fast";
    PYEXAMPLE_MODE_ACCURATE "Accurate";
    PYEXAMPLE_SMOOTH        "Smooth";
    PYEXAMPLE_SOURCE        "Source";
    PYEXAMPLE_RESET         "Reset";
}
```

A parameter name can also have a short variant for narrow Attribute Manager layouts, written as a second string: `PYEXAMPLE_STRENGTH "Strength" "Str";`.

### Using Parameters in Python <a id="using-parameters-in-python"></a>

A description only defines the parameters. Your hook initializes their values, reads them, and can react to the user:

```python
class ExampleData(c4d.plugins.ObjectData):

    def Init(self, node: c4d.BaseObject, isCloneInit: bool = False) -> bool:
        # Parameters must be initialized with their type before they can be used. Clones copy values.
        if isCloneInit:
            return True

        self.InitAttr(node, float, c4d.PYEXAMPLE_RADIUS)
        self.InitAttr(node, float, c4d.PYEXAMPLE_STRENGTH)
        self.InitAttr(node, int, c4d.PYEXAMPLE_MODE)
        self.InitAttr(node, bool, c4d.PYEXAMPLE_SMOOTH)
        self.InitAttr(node, c4d.BaseList2D, c4d.PYEXAMPLE_SOURCE)

        node[c4d.PYEXAMPLE_RADIUS] = 100.0
        node[c4d.PYEXAMPLE_STRENGTH] = 50.0
        node[c4d.PYEXAMPLE_MODE] = c4d.PYEXAMPLE_MODE_FAST
        return True

    def GetVirtualObjects(self, op: c4d.BaseObject, hh: object) -> c4d.BaseObject | None:
        radius: float = op[c4d.PYEXAMPLE_RADIUS]  # Read a value of the node that is passed in.
        ...

    def GetDEnabling(self, node: c4d.BaseObject, id: c4d.DescID, t_data: object, flags: int,
                     itemdesc: c4d.BaseContainer) -> bool:
        # Grey out 'Smooth' unless the accurate mode is active.
        if id[0].id == c4d.PYEXAMPLE_SMOOTH:
            return node[c4d.PYEXAMPLE_MODE] == c4d.PYEXAMPLE_MODE_ACCURATE
        return c4d.plugins.ObjectData.GetDEnabling(self, node, id, t_data, flags, itemdesc)

    def Message(self, node: c4d.BaseObject, msgId: int, data: object) -> bool:
        # The user clicked the 'Reset' button.
        if msgId == c4d.MSG_DESCRIPTION_COMMAND and data["id"][0].id == c4d.PYEXAMPLE_RESET:
            node[c4d.PYEXAMPLE_RADIUS] = 100.0
        return True
```

Values are read and written with `node[id]` anywhere you have the node, also outside of the hook, as long as the [threading rules](manual_scene_execution.md) are respected. Buttons send [MSG_DESCRIPTION_COMMAND](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-command) to the `Message` method, see [Message System](manual_message_system.md). The same system is used by tools and preference pages, see [py_msc_preference](../examples/plugins/py_msc_preference/py_msc_preference.pyp.md).

### Inspecting a Description <a id="inspecting-a-description"></a>

The [`Description`](../modules/c4d/Description/index.md#c4d.Description) of a node lists all of its parameters, also the ones inherited from the included descriptions. This is a quick way to find the symbol and type of a parameter in a script:

```python
import c4d

description: c4d.Description = op.GetDescription(c4d.DESCFLAGS_DESC_NONE)
for bc, paramId, groupId in description:
    print(bc[c4d.DESC_NAME], paramId)
```

### Settings of a Parameter <a id="settings-of-a-parameter"></a>

Cinema 4D stores the flags of every parameter in a [`BaseContainer`](../modules/c4d/BaseContainer/index.md#c4d.BaseContainer), which you can read and modify in code. The containers are described in [DESC](../consts/DESC.md). Most flags of a resource have a counterpart:

| Resource | Container ID and Value |
|---|---|
| `MIN`, `MAX`, `STEP` | `DESC_MIN`, `DESC_MAX`, `DESC_STEP` |
| `MINSLIDER`, `MAXSLIDER` | `DESC_MINSLIDER`, `DESC_MAXSLIDER` |
| `CUSTOMGUI REALSLIDER` | `DESC_CUSTOMGUI` set to `CUSTOMGUI_REALSLIDER` |
| `UNIT METER` | `DESC_UNIT` set to `DESC_UNIT_METER` |
| `ANIM OFF` | `DESC_ANIMATE` set to `DESC_ANIMATE_OFF` |
| `CYCLE { ... }` | `DESC_CYCLE`, a container of IDs and strings |
| `ACCEPT { ... }` | `DESC_ACCEPT`, a container of node type names |
| `SEPARATOR { LINE; }` | `DESC_SEPARATORLINE` |
| `COLUMNS n` of a group | `DESC_COLUMNS` |
| The strings of the string table | `DESC_NAME` and `DESC_SHORT_NAME` |

### Dynamic Descriptions <a id="dynamic-descriptions"></a>

Some content of a description is only known at runtime: the entries of a drop down, a number of parameters that depends on another parameter. Implement [`NodeData.GetDDescription()`](../modules/c4d.plugins/BaseData/NodeData/index.md#c4d.plugins.NodeData.GetDDescription) to change the description of a node after it has been loaded from its resource. This example fills a cycle with the names of the children of the node:

```python
def GetDDescription(self, node: c4d.BaseObject, description: c4d.Description,
                    flags: int) -> bool | tuple[bool, int]:
    # Load the resource first, then modify what has been loaded.
    if not description.LoadDescription(node.GetType()):
        return False

    # Only do the work when the parameter is requested, as this method is called often.
    paramId: c4d.DescID = c4d.DescID(c4d.DescLevel(c4d.PYEXAMPLE_MODE))
    singleId: c4d.DescID | None = description.GetSingleDescID()
    if singleId is not None and not paramId.IsPartOf(singleId)[0]:
        return True, flags

    settings: c4d.BaseContainer | None = description.GetParameterI(paramId)
    if settings is not None:
        items: c4d.BaseContainer = c4d.BaseContainer()
        for i, child in enumerate(node.GetChildren()):
            items.SetString(i, child.GetName())
        settings.SetContainer(c4d.DESC_CYCLE, items)
        flags |= c4d.DESCFLAGS_DESC_LOADED

    return True, flags
```

Entirely new parameters are added with [`Description.SetParameter()`](../modules/c4d/Description/index.md#c4d.Description.SetParameter), starting from [`c4d.GetCustomDataTypeDefault()`](../modules/c4d/index.md#c4d.GetCustomDataTypeDefault) and the container IDs above. Parameters that are not stored in the node container must also be provided by `GetDParameter` and `SetDParameter`. Two SDK examples cover these cases:

- [py_obj_assetcontainer](../examples/plugins/py_obj_assetcontainer/py_obj_assetcontainer.pyp.md) fills a cycle with stored assets, handles its buttons, and enables them based on the state of the node.
- [py_obj_dynamic_parameters](../examples/plugins/py_obj_dynamic_parameters/py_obj_dynamic_parameters.pyp.md) adds a variable number of parameters in a dynamic group.

## See Also <a id="see-also"></a>

- [Implementing Plugins](manual_implementing_plugins.md): Explains the basic concepts of implementing plugins.
- [Symbol Parsing](manual_symbol_parsing.md): Explains resource symbols and mxutils.ImportSymbols.
- [Example py_cmd_gui_resources.pyp](../examples/plugins/py_cmd_gui_resources/py_cmd_gui_resources.pyp.md): Demonstrates a plugin that uses resources to define its dialog layout and string translations.
- [Example py_msc_preference.pyp](../examples/plugins/py_msc_preference/py_msc_preference.pyp.md): Demonstrates how to implement a preference category in the Cinema 4D preference dialog, exposing parameters as global preferences.
- [Example py_obj_dynamic_parameters.pyp](../examples/plugins/py_obj_dynamic_parameters/py_obj_dynamic_parameters.pyp.md): Demonstrates how to implement a node (at the example of an object) that dynamically updates its parameters.
