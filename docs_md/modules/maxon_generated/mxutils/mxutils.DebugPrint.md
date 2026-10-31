<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/mxutils/mxutils.DebugPrint.html -->

# mxutils.DebugPrint <a id="mxutils-debugprint"></a>

## Description <a id="module-mxutils.DebugPrint"></a><a id="description"></a>

Contains utility functions for printing debug information about selected Cinema API data.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`DiffBaseList`](#mxutils.DebugPrint.DiffBaseList)(first, second[, showName, …]) | Returns a unified diff of two combined debug trees. |
| [`DiffContainer`](#mxutils.DebugPrint.DiffContainer)(first, second[, keyHint]) | Returns a unified diff of two container debug trees. |
| [`DiffFlags`](#mxutils.DebugPrint.DiffFlags)(first, second[, showBit, …]) | Returns a unified diff of two flag debug trees. |
| [`DiffGraph`](#mxutils.DebugPrint.DiffGraph)(first, second) | Returns a unified diff of two scene graph debug trees. |
| [`DiffParameters`](#mxutils.DebugPrint.DiffParameters)(first, second[, showName, …]) | Returns a unified diff of two parameter debug trees. |
| [`GetBaseList`](#mxutils.DebugPrint.GetBaseList)(node[, showName, showSymbol, …]) | Returns the debug representation of the passed *node* and its state. |
| [`GetContainer`](#mxutils.DebugPrint.GetContainer)(container[, keyHint]) | Returns the debug representation of the passed *container* tree. |
| [`GetFlags`](#mxutils.DebugPrint.GetFlags)(node[, showBit, showNBit, hint, …]) | Returns a tree representation of the bit and NBit flags of `node`. |
| [`GetGraph`](#mxutils.DebugPrint.GetGraph)(node) | Returns a tree representation of the scene structure of the passed *node*. |
| [`GetParameters`](#mxutils.DebugPrint.GetParameters)(node[, showName, showSymbol, …]) | Returns the debug representation of the description parameter tree of a passed *node*. |
| [`GetTreeString`](#mxutils.DebugPrint.GetTreeString)(node[, childrenAttr, …]) | Returns a string representation of a tree structure. |
| [`PrintContainer`](#mxutils.DebugPrint.PrintContainer)(container[, keyHint]) | Prints the passed container as a debug tree. |
| [`PrintFlags`](#mxutils.DebugPrint.PrintFlags)(node[, showBit, showNBit, hint, …]) | Prints the passed node flags as a debug tree. |
| [`PrintGraph`](#mxutils.DebugPrint.PrintGraph)(node) | Prints the passed node graph as a debug tree. |
| [`PrintParameters`](#mxutils.DebugPrint.PrintParameters)(node[, showName, …]) | Prints the passed node parameters as a debug tree. |

## Methods Definition <a id="methods-definition"></a>

### *classmethod* `DebugPrint.DiffBaseList(first: c4d.BaseList2D, second: c4d.BaseList2D, showName: bool = True, showSymbol: bool = True, showDescId: bool = True, showType: bool = True, showHidden: bool = False, showValue: bool = True, hideLayoutElements: bool = True, blackList: tuple = (), whiteList: tuple = (), showDefaultValues: bool = True, showBit: bool = True, showNBit: bool = True, hint: str | None = None, showSetOnly: bool = False) → str` <a id="mxutils.DebugPrint.DiffBaseList"></a>

Returns a unified diff of two combined debug trees.

See [`GetBaseList()`](#mxutils.DebugPrint.GetBaseList) for an explanation of the shared arguments.

**Parameters:**

- **first** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The first node to compare.
- **second** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The second node to compare.

**Returns:** The unified diff of the two combined debug trees.

**Return type:** str

### *classmethod* `DebugPrint.DiffContainer(first: c4d.BaseContainer, second: c4d.BaseContainer, keyHint: str | None = None) → str` <a id="mxutils.DebugPrint.DiffContainer"></a>

Returns a unified diff of two container debug trees.

See [`GetContainer()`](#mxutils.DebugPrint.GetContainer) for an explanation of the shared arguments.

**Parameters:**

- **first** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The first container to compare.
- **second** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The second container to compare.
- **keyHint** (*str | None*, *optional*) – A regular expression used to resolve container keys to symbols, defaults to `None`.

**Returns:** The unified diff of the two container debug trees.

**Return type:** str

### *classmethod* `DebugPrint.DiffFlags(first: c4d.BaseList2D, second: c4d.BaseList2D, showBit: bool = True, showNBit: bool = True, hint: str | None = None, showSetOnly: bool = False) → str` <a id="mxutils.DebugPrint.DiffFlags"></a>

Returns a unified diff of two flag debug trees.

See [`GetFlags()`](#mxutils.DebugPrint.GetFlags) for an explanation of the shared arguments.

**Parameters:**

- **first** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The first node whose flags should be compared.
- **second** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The second node whose flags should be compared.

**Returns:** The unified diff of the two flag debug trees.

**Return type:** str

### *classmethod* `DebugPrint.DiffGraph(first: c4d.BaseList2D, second: c4d.BaseList2D) → str` <a id="mxutils.DebugPrint.DiffGraph"></a>

Returns a unified diff of two scene graph debug trees.

See [`GetGraph()`](#mxutils.DebugPrint.GetGraph) for an explanation of the shared arguments.

**Parameters:**

- **first** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The first scene element whose graph should be compared.
- **second** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The second scene element whose graph should be compared.

**Returns:** The unified diff of the two scene graph debug trees.

**Return type:** str

### *classmethod* `DebugPrint.DiffParameters(first: c4d.BaseList2D, second: c4d.BaseList2D, showName: bool = True, showSymbol: bool = True, showDescId: bool = True, showType: bool = True, showHidden: bool = False, showValue: bool = True, hideLayoutElements: bool = True, blackList: tuple = (), whiteList: tuple = (), showDefaultValues: bool = True) → str` <a id="mxutils.DebugPrint.DiffParameters"></a>

Returns a unified diff of two parameter debug trees.

See [`GetParameters()`](#mxutils.DebugPrint.GetParameters) for an explanation of the shared arguments.

**Parameters:**

- **first** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The first node whose parameters should be compared.
- **second** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The second node whose parameters should be compared.

**Returns:** The unified diff of the two parameter debug trees.

**Return type:** str

### *classmethod* `DebugPrint.GetBaseList(node: c4d.BaseList2D, showName: bool = True, showSymbol: bool = True, showDescId: bool = True, showType: bool = True, showHidden: bool = False, showValue: bool = True, hideLayoutElements: bool = True, blackList: tuple = (), whiteList: tuple = (), showDefaultValues: bool = True, showBit: bool = True, showNBit: bool = True, hint: str | None = None, showSetOnly: bool = False) → mxutils.mxu_scene.DebugNode` <a id="mxutils.DebugPrint.GetBaseList"></a>

Returns the debug representation of the passed *node* and its state.

The returned tree contains the parameter description and the BIT and NBit flags of the node under separate *Parameters* and *Flags* branches.

**Parameters:**

- **node** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The node to inspect.
- **showName** – Whether to show parameter names, defaults to *True*.
- **showSymbol** – Whether to show parameter symbols, defaults to *True*.
- **showDescId** – Whether to show parameter DescIDs, defaults to *True*.
- **showType** – Whether to show parameter types, defaults to *True*.
- **showHidden** – Whether to show hidden parameters, defaults to *False*.
- **showValue** – Whether to show parameter values, defaults to *True*.
- **hideLayoutElements** – Whether to hide unnamed groups and separators, defaults to *True*.
- **blackList** – Parameter IDs to exclude, defaults to an empty tuple.
- **whiteList** – Parameter IDs to include, defaults to an empty tuple.
- **showDefaultValues** – Whether to include parameters with default values, defaults to *True*.
- **showBit** – Whether to include regular bit flags, defaults to *True*.
- **showNBit** – Whether to include NBit flags, defaults to *True*.
- **hint** – A regular expression used to filter flag symbols, defaults to *None*.
- **showSetOnly** – Whether to include only set flags, defaults to *False*.

**Returns:** The combined parameter and flag tree.

**Return type:** DebugNode

**Example:**

```python
import mxutils

print(mxutils.DebugPrint.GetBaseList(op).ToString())
```

### *classmethod* `DebugPrint.GetContainer(container: c4d.BaseContainer, keyHint: str | None = None) → mxutils.mxu_scene.DebugNode` <a id="mxutils.DebugPrint.GetContainer"></a>

Returns the debug representation of the passed *container* tree.

> **Warning:** Resolving keys of a container to symbols is highly ambiguous. The ID *1000* could resolve to dozens of different symbols, depending on the context. When using the symbol resolving in this function, always keep in mind that output might be incorrect in the sense that the returned symbol is representing that entry numerically, but that the symbol name implies another semantic context than is actually the case.

> **Note:** The symbol resolving will fall back to the numeric value of an entry when either no symbol or more than one symbol is found for the entry.

**Parameters:**

- **container** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The container to get the tree string for.
- **keyHint** (*str | None*, *optional*) – A regular expression that is used to resolve container keys to symbols. E.g., passing *^BFM_|^DTYPE_* will pick symbols that start with *BFM_* or *DTYPE_*. Passing the empty string will yield any symbol, passing *None* will turn off symbol resolving. Defaults to *None*.

**Returns:** The node representation of the container tree.

**Return type:** DebugNode

**Raises:** **TypeError** – If the container is not of type *c4d.BaseContainer*.

**Example:**

```python
import c4d
import mxutils

# Print a part of the world container without using hints. Hinting would not make much sense
# here, as most entries are not unambiguously resolvable. This tree will also be very large,
# so large in fact that Python will refuse to print everything in one go (and then also hide
# our other print statements below). So, we will only print the first ten lines.
data: list[str] = mxutils.DebugPrint.GetContainer(c4d.GetWorldContainer()).ToString().splitlines()
block: str = "\n".join(data[:10] + ["..."])
print(f"World Container:\n\n{block}")

# Poll for the input state of the mouse and then print the state hinting at the fact that
# these message symbols usually start with `BFM_`.
state: c4d.BaseContainer = c4d.BaseContainer()
c4d.gui.GetInputState(c4d.BFM_INPUT_MOUSE, 0, state)
print(f"\nMouse Input State:\n\n{mxutils.DebugPrint.GetContainer(state, '^BFM_').ToString()}")

# And lastly, we print a simple nested container structure. Here hinting does not make any
# sense at all, as it us who defines the keys and their symbols. If we would define symbols
# in our code (and did not expose them in the `c4d` module), #DebugPrint.GetContainer would
# not be able to see them.
bc: c4d.BaseContainer = c4d.BaseContainer()
bc[1000] = "Hello World"
bc[1001] = 42
sub: c4d.BaseContainer = c4d.BaseContainer()
sub[1000] = "Sub Hello World"
sub[1001] = 84
bc[1002] = sub
print(f"\nNested:\n\n{mxutils.DebugPrint.GetContainer(bc).ToString()}")
```

The output will look like this, note how the second call falls back to the numeric value *1768977011*, as there is no symbol for that ID in the context of *BFM_* messages (and this is correct, there is not symbol at all exposed for this entry).

```text
World Container:

Root (None , id = -1):
├── 1005 (DTYPE_LONG): 0
├── 1030 (DTYPE_LONG): 1
├── 1071 (DTYPE_LONG): 2
├── 1072 (DTYPE_LONG): 8
├── 1073 (DTYPE_LONG): 2
├── 1089 (DTYPE_LONG): 1
├── 1091 (DTYPE_LONG): 1
├── 1094 (DTYPE_LONG): 1
├── 1095 (DTYPE_LONG): 0
...

Mouse Input State:

Root (None , id = -1):
├── BFM_INPUT_DEVICE (DTYPE_LONG): 1836021107
├── BFM_INPUT_CHANNEL (DTYPE_LONG): 101
├── BFM_INPUT_QUALIFIER (DTYPE_LONG): 0
├── BFM_INPUT_MODIFIERS (DTYPE_LONG): 0
├── BFM_INPUT_X (DTYPE_REAL): 1476.41796875
├── BFM_INPUT_Y (DTYPE_REAL): 974.4765625
├── BFM_INPUT_Z (DTYPE_REAL): 0.0
├── BFM_INPUT_ORIENTATION (DTYPE_REAL): 0.0
├── 1768977011 (DTYPE_REAL): 0.0
├── BFM_INPUT_TILT (DTYPE_REAL): 0.0
├── BFM_INPUT_FINGERWHEEL (DTYPE_REAL): 0.0
└── BFM_INPUT_P_ROTATION (DTYPE_REAL): 0.0

Nested:

Root (None , id = -1):
├── 1000 (DTYPE_STRING): Hello World
├── 1001 (DTYPE_LONG): 42
└── 1002 (DTYPE_SUBCONTAINER , id = -1):
    ├── 1000 (DTYPE_STRING): Sub Hello World
    └── 1001 (DTYPE_LONG): 84
```

### *classmethod* `DebugPrint.GetFlags(node: c4d.BaseList2D, showBit: bool = True, showNBit: bool = True, hint: str | None = None, showSetOnly: bool = False) → mxutils.mxu_scene.DebugNode` <a id="mxutils.DebugPrint.GetFlags"></a>

Returns a tree representation of the bit and NBit flags of `node`.

Flag symbols are discovered through the global symbol translation cache. The optional `hint` is interpreted as a regular expression and filters the discovered flag symbols. The optional `showSetOnly` argument limits the output to flags whose value is `True`.

**Parameters:**

- **node** – The node whose flags should be printed.
- **showBit** – Whether regular bit flags should be included, defaults to `True`.
- **showNBit** – Whether NBit flags should be included, defaults to `True`.
- **hint** – A regular expression used to filter flag symbols, defaults to `None`.
- **showSetOnly** – Whether to only show flags whose value is `True`, defaults to `False`.

**Returns:** A tree representation of the flags and their values.

**Return type:** DebugNode

**Raises:** **re.error** – If `hint` is not a valid regular expression.

**Example:**

```python
import mxutils

# Print all flags of the selected object.
print(mxutils.DebugPrint.GetFlags(op).ToString())

# Print only set NBits related to the Object Manager.
print(mxutils.DebugPrint.GetFlags(op, showBit=False, hint="OM", showSetOnly=True).ToString())
```

### *classmethod* `DebugPrint.GetGraph(node: c4d.BaseList2D) → mxutils.mxu_scene.DebugNode` <a id="mxutils.DebugPrint.GetGraph"></a>

Returns a tree representation of the scene structure of the passed *node*.

Will denote the start of caches with *[Cache]* and *[DeformCache]* and branches with *[Branch]*.

**Parameters:** **node** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The scene element to build the representation for. Can be a document, an object, a tag, a material, etc.

**Returns:** The scene graph tree.

**Return type:** DebugNode

**Example:**

```python
import c4d
import mxutils

# This will print the entire scene graph of the active document to the console.
print(mxutils.DebugPrint.GetGraph(c4d.documents.GetActiveDocument()).ToString())
```

For the following very simple object tree,

```text
'Cloner'          # a MoGraph CLoner object in radial mode, with 3 clones
└── 'Cube'        # a Cube generator object
    └── 'Bend'    # a Bend deformer object
```

*print(mxutils.DebugPrint.GetGraph(Cloner).ToString())* will print:

```text
'Cloner' (BaseObject: Omgcloner)
├── [Cache]
│   └── 'Null' (BaseObject: Onull)
│       ├── 'Cube 0' (BaseObject: Ocube)
│       │   ├── [Cache]
│       │   │   └── 'Cube 0' (PolygonObject: Opolygon)
│       │   │       ├── [Deform Cache]
│       │   │       │   └── 'Cube 0' (PolygonObject: Opolygon)
│       │   │       │       └── [Branch] 'Tags' (Tbase)
│       │   │       │           ├── 'UVW' (UVWTag: Tuvw)
│       │   │       │           ├── '' (PolygonTag: Tpolygon)
│       │   │       │           └── '' (PointTag: Tpoint)
│       │   │       └── [Branch] 'Tags' (Tbase)
│       │   │           ├── 'UVW' (UVWTag: Tuvw)
│       │   │           ├── '' (PolygonTag: Tpolygon)
│       │   │           └── '' (PointTag: Tpoint)
│       │   ├── [Branch] 'Tags' (Tbase)
│       │   │   └── 'Motion Graphics Color Tag' (BaseTag: Tmgcolor)
│       │   └── 'Bend' (BaseObject: Obend)
│       ├── 'Cube 1' (BaseObject: Ocube)
│       │   ├── [Cache]
│       │   │   └── 'Cube 1' (PolygonObject: Opolygon)
│       │   │       ├── [Deform Cache]
│       │   │       │   └── 'Cube 1' (PolygonObject: Opolygon)
│       │   │       │       └── [Branch] 'Tags' (Tbase)
│       │   │       │           ├── 'UVW' (UVWTag: Tuvw)
│       │   │       │           ├── '' (PolygonTag: Tpolygon)
│       │   │       │           └── '' (PointTag: Tpoint)
│       │   │       └── [Branch] 'Tags' (Tbase)
│       │   │           ├── 'UVW' (UVWTag: Tuvw)
│       │   │           ├── '' (PolygonTag: Tpolygon)
│       │   │           └── '' (PointTag: Tpoint)
│       │   ├── [Branch] 'Tags' (Tbase)
│       │   │   └── 'Motion Graphics Color Tag' (BaseTag: Tmgcolor)
│       │   └── 'Bend' (BaseObject: Obend)
│       └── 'Cube 2' (BaseObject: Ocube)
│           ├── [Cache]
│           │   └── 'Cube 2' (PolygonObject: Opolygon)
│           │       ├── [Deform Cache]
│           │       │   └── 'Cube 2' (PolygonObject: Opolygon)
│           │       │       └── [Branch] 'Tags' (Tbase)
│           │       │           ├── 'UVW' (UVWTag: Tuvw)
│           │       │           ├── '' (PolygonTag: Tpolygon)
│           │       │           └── '' (PointTag: Tpoint)
│           │       └── [Branch] 'Tags' (Tbase)
│           │           ├── 'UVW' (UVWTag: Tuvw)
│           │           ├── '' (PolygonTag: Tpolygon)
│           │           └── '' (PointTag: Tpoint)
│           ├── [Branch] 'Tags' (Tbase)
│           │   └── 'Motion Graphics Color Tag' (BaseTag: Tmgcolor)
│           └── 'Bend' (BaseObject: Obend)
├── [Branch] 'Tags' (Tbase)
│   └── 'Info' (BaseTag: ID_MOTAGDATA)
└── 'Cube' (BaseObject: Ocube)
    └── 'Bend' (BaseObject: Obend)
```

### *classmethod* `DebugPrint.GetParameters(node: c4d.BaseList2D, showName: bool = True, showSymbol: bool = True, showDescId: bool = True, showType: bool = True, showHidden: bool = False, showValue: bool = True, hideLayoutElements: bool = True, blackList: tuple = (), whiteList: tuple = (), showDefaultValues: bool = True) → mxutils.mxu_scene.DebugNode` <a id="mxutils.DebugPrint.GetParameters"></a>

Returns the debug representation of the description parameter tree of a passed *node*.

> **Warning:** The output hides by default all groups and separators that have the empty string as the name. This is because they are usually inconsequential for data access. When you need the true parameter tree of a scene element, you must set *hideLayoutElements* to *False*.

**Parameters:**

- **node** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The node to get the parameter tree for.
- **showName** (*bool*, *optional*) – Whether to show the name of the parameter, defaults to *True*.
- **showSymbol** (*bool*, *optional*) – Whether to show the symbol of the parameter, defaults to *True*.
- **showDescId** (*bool*, *optional*) – Whether to show the full DescID of the parameter, defaults to *True*.
- **showType** (*bool*, *optional*) – Whether to show the type of the parameter. This will always unpack the type of the last element of the id of the parameter. E.g., an integer within a sub-container will be printed as *DTYPE_LONG*. Can only discover type symbols that start with *DTYPE_* and have been exposed to Python. Defaults to *True*.
- **showHidden** (*bool*, *optional*) – Whether to show if the parameter is hidden, defaults to *False*.
- **showValue** (*bool*, *optional*) – Whether to show the value of the parameter, defaults to *True*.
- **hideLayoutElements** (*bool*, *optional*) – Whether to hide groups and separators with the empty string as the name, defaults to *True*.
- **blackList** (*tuple*[*int*], *optional*) – A list of parameter IDs to ignore. When passing here group IDs, everything within the group will be ignored. Defaults to an empty tuple.
- **whiteList** (*tuple*[*int*], *optional*) – A list of parameter IDs to include. When passing here group IDs, everything within the group will be included. An empty tuple includes all parameters. Defaults to an empty tuple.
- **showDefaultValues** (*bool*, *optional*) – Whether to include parameters whose current value equals their description default, defaults to `True`. Set this to `False` to show only values that differ from their description default. Parameters without a defined description default are always shown. Combine this setting with *whiteList* and specific groups such as *ID_OBJECTPROPERTIES* to only see the value you need.

**Returns:** The parameter tree.

**Return type:** DebugNode

**Raises:**

- **TypeError** – If the node is not of type *c4d.BaseList2D*.
- **TypeError** – If the blackList is not of type *tuple* or *list*.

**Example:**

```python
import c4d
import mxutils

# Print the parameter tree of the active object in the document and disable ID output.
print(mxutils.DebugPrint.GetParameters(op, showDescId=False).ToString())
```

The output for a *op* being of type *Ocube* would look like this:

```text
'Cube' (Ocube)' object at 0x00000003C0D268C0 with the parameters:
├── 'Basic Properties (Obaselist)' - type: DTYPE_GROUP
│   ├── 'Icon (ID_BASELIST_ICON_SETTINGS_GROUP)' - type: DTYPE_GROUP
│   │   ├── 'Icon File / ID (ID_BASELIST_ICON_FILE)' - type: DTYPE_TEXTURE, value:
│   │   ├── 'Icon Color (ID_BASELIST_ICON_COLORIZE_MODE)' - type: DTYPE_LONG, value: 0
│   │   ├── 'Color (ID_BASELIST_ICON_COLOR)' - type: DTYPE_COLOR, value: Vector(0.887, 0.794, 0.222)
│   │   └── 'ID_BASELIST_ICON_PRESET_BUTTONS' - type: ICONCHOOSER_DATA, value: 'Inaccessible in Python'
│   ├── 'Name (ID_BASELIST_NAME)' - type: DTYPE_STRING, value: Cube
│   ├── 'Layer (ID_LAYER_LINK)' - type: DTYPE_BASELISTLINK, value: None
│   ├── 'Node Space (ID_BASELIST_NODESPACE_ADD_REMOVE_GROUP)' - type: DTYPE_GROUP
│   │   └── 'ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS' - type: 1050442, value: 'Inaccessible in Python'
│   ├── 'Viewport Visibility (ID_BASEOBJECT_VISIBILITY_EDITOR)' - type: DTYPE_LONG, value: 2
│   ├── 'Renderer Visibility (ID_BASEOBJECT_VISIBILITY_RENDER)' - type: DTYPE_LONG, value: 2
│   ├── 'Enabled (ID_BASEOBJECT_GENERATOR_FLAG)' - type: DTYPE_BOOL, value: 1
│   ├── 'Display Color (ID_BASEOBJECT_USECOLOR)' - type: DTYPE_LONG, value: 0
│   ├── 'Color (ID_BASEOBJECT_COLOR)' - type: DTYPE_COLOR, value: Vector(1, 1, 1)
│   └── 'X-Ray (ID_BASEOBJECT_XRAY)' - type: DTYPE_BOOL, value: 0
├── 'Coordinates (ID_BASEOBJECT_GROUP1)' - type: DTYPE_GROUP
│   ├── 'Transform (ID_BASEOBJECT_QUATERNION_ROTATION)' - type: DTYPE_GROUP
│   │   ├── 'Position (ID_BASEOBJECT_REL_POSITION)' - type: DTYPE_VECTOR, value: Vector(0, 0, 0)
│   │   ├── 'Rotation (ID_BASEOBJECT_REL_ROTATION)' - type: DTYPE_VECTOR, value: Vector(0, 0, 0)
│   │   ├── 'Scale (ID_BASEOBJECT_REL_SCALE)' - type: DTYPE_VECTOR, value: Vector(1, 1, 1)
│   │   ├── 'Rotation Order (ID_BASEOBJECT_ROTATION_ORDER)' - type: DTYPE_LONG, value: 6
│   │   └── 'Quaternion Rotation (ID_BASEOBJECT_QUATERNION_ROTATION_INTERPOLATION)' - type: DTYPE_BOOL, value: 0
│   ├── 'Freeze Transform (ID_BASEOBJECT_FROZEN_COORDS)' - type: DTYPE_GROUP
│   │   ├── 'Freeze All (ID_BASEOBJECT_FREEZE)' - type: DTYPE_BUTTON
│   │   ├── 'Unfreeze All (ID_BASEOBJECT_FROZEN_RESET)' - type: DTYPE_BUTTON
│   │   ├── 'Frozen Position (ID_BASEOBJECT_FROZEN_POSITION)' - type: DTYPE_VECTOR, value: Vector(0, 0, 0)
│   │   ├── 'Freeze P (ID_BASEOBJECT_FREEZE_P)' - type: DTYPE_BUTTON
│   │   ├── 'Frozen Rotation (ID_BASEOBJECT_FROZEN_ROTATION)' - type: DTYPE_VECTOR, value: Vector(0, 0, 0)
│   │   ├── 'Freeze R (ID_BASEOBJECT_FREEZE_R)' - type: DTYPE_BUTTON
│   │   ├── 'Frozen Scale (ID_BASEOBJECT_FROZEN_SCALE)' - type: DTYPE_VECTOR, value: Vector(1, 1, 1)
│   │   └── 'Freeze S (ID_BASEOBJECT_FREEZE_S)' - type: DTYPE_BUTTON
│   ├── 'Deform Transform (ID_BASEOBJECT_DEFORMATION_MATRIX)' - type: DTYPE_GROUP
│   │   ├── 'Deform Position (ID_BASEOBJECT_DEFORM_POSITION)' - type: DTYPE_VECTOR, value: None
│   │   ├── 'Deform Rotation (ID_BASEOBJECT_DEFORM_ROTATION)' - type: DTYPE_VECTOR, value: None
│   │   └── 'Deform Scale (ID_BASEOBJECT_DEFORM_SCALE)' - type: DTYPE_VECTOR, value: None
│   ├── 'Global Position (ID_BASEOBJECT_GLOBAL_POSITION)' - type: DTYPE_VECTOR, value: Vector(0, 0, 0)
│   ├── 'Global Rotation (ID_BASEOBJECT_GLOBAL_ROTATION)' - type: DTYPE_VECTOR, value: Vector(0, 0, 0)
│   ├── 'Transformed Position (ID_BASEOBJECT_ABS_POSITION)' - type: DTYPE_VECTOR, value: Vector(0, 0, 0)
│   ├── 'Transformed Scale (ID_BASEOBJECT_ABS_SCALE)' - type: DTYPE_VECTOR, value: Vector(1, 1, 1)
│   └── 'Transformed Rotation (ID_BASEOBJECT_ABS_ROTATION)' - type: DTYPE_VECTOR, value: Vector(0, 0, 0)
└── 'Object Properties (ID_OBJECTPROPERTIES)' - type: DTYPE_GROUP
    ├── 'Size (PRIM_CUBE_LEN)' - type: DTYPE_VECTOR, value: Vector(200, 200, 200)
    ├── 'Segments X (PRIM_CUBE_SUBX)' - type: DTYPE_LONG, value: 1
    ├── 'Segments Y (PRIM_CUBE_SUBY)' - type: DTYPE_LONG, value: 1
    ├── 'Segments Z (PRIM_CUBE_SUBZ)' - type: DTYPE_LONG, value: 1
    ├── 'Separate Surfaces (PRIM_CUBE_SEP)' - type: DTYPE_BOOL, value: 0
    ├── 'Fillet (PRIM_CUBE_DOFILLET)' - type: DTYPE_BOOL, value: 0
    ├── 'Fillet Radius (PRIM_CUBE_FRAD)' - type: DTYPE_REAL, value: 3.0
    └── 'Fillet Subdivision (PRIM_CUBE_SUBF)' - type: DTYPE_LONG, value: 3
```

### *classmethod* `DebugPrint.GetTreeString(node: Any, childrenAttr: str | None = None, getDownFunc: str | None = 'GetDown', getNextFunc: str | None = 'GetNext', indentWidth: int = 3, callback: Optional[Callable, None] = None) → str` <a id="mxutils.DebugPrint.GetTreeString"></a>

Returns a string representation of a tree structure.

The tree of *node* is traversed using either a list of child nodes attached to each node under the attribute *childrenAttr*, or by calling the functions *getDownFunc* and *getNextFunc* on each node to get the first child and the next sibling, respectively.

**Parameters:**

- **node** (*typing.Any*) – The root node of the tree.
- **childrenAttr** (*str*, *optional*) – The attribute name to access the children of a node, defaults to None.
- **getDownFunc** (*str*, *optional*) – The function name to get the first child of a node, defaults to “GetDown”.
- **getNextFunc** (*str*, *optional*) – The function name to get the next sibling of a node, defaults to “GetNext”.
- **indentWidth** (*int*, *optional*) – The width of the tree indentation for one level, defaults to 3.
- **callback** (*typing.Callable*, *optional*) – A callback function to customize the string representation of each node, defaults to None.

**Returns:** The string representation of the tree structure.

**Return type:** str

**Raises:**

- **ValueError** – If the callback is provided but not callable.
- **AttributeError** – If the childrenAttr is not found on a node.
- **AttributeError** – If the getDownFunc is not found on a node.
- **AttributeError** – If the getNextFunc is not found on a node.
- **ValueError** – If neither childrenAttr nor getDownFunc and getNextFunc are provided.

**Example:**

```python
import c4d
import mxutils

# A node type to print trees for, this is a node type which stores its children as a list.
class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.children = []

    def __str__(self) -> str:
        return str(self.value)

    def AddChild(self, child: 'Node') -> None:
        self.children.append(child)

# Create a tree structure.
tree: Node = Node(1)
tree.AddChild(Node(2))
tree.AddChild(Node(3))
tree.children[1].AddChild(Node(4))

# Print the tree structure by telling the function to use the #children attribute.
print(mxutils.DebugPrint.GetTreeString(tree, "children"))
```

```text
1
├─ 2
└─ 3
    └─ 4
```

```python
# Example for printing a node tree for a node type which can be navigated using a function which
# yields the first child and a function which yields the next sibling, here at the example of a
# Cinema 4D BaseObject tree.

# Get the first object in the active document.
doc: c4d.documents.BaseDocument = c4d.documents.GetActiveDocument()
op: c4d.BaseObject = doc.GetFirstObject()
if not op:
    raise ValueError("No object found in the document.")

# Print the object tree of #op using its navigation functions 'GetDown' and 'GetNext'. We could
# just invoke #GetTreeString(op) here since 'GetDown' and 'GetNext' are the default values.
print(mxutils.DebugPrint.GetTreeString(op, getDownFunc="GetDown", getNextFunc="GetNext"))

print("")

def PrintObject(node: c4d.BaseObject) -> str:
    '''Returns the name of an object and the names of its tags as a string.
    '''
    return f"{node.GetName()} {' '.join(f'[{tag.GetName()}]' for tag in node.GetTags())}"

# We can also customize the string representation of each node by passing a callback function.
print(mxutils.DebugPrint.GetTreeString(op, callback=PrintObject))
```

```text
<c4d.BaseObject object called Cone/Cone with ID 5162 at 140511902113152>
├── <c4d.BaseObject object called Cube/Cube with ID 5159 at 140511902142592>
└── <c4d.BaseObject object called Sphere/Sphere with ID 5160 at 140511902160768>
    └── <c4d.BaseObject object called Torus/Torus with ID 5163 at 140511902065024>

Cone [Display] [Phong] [Material]
├── Cube [Phong]
└── Sphere [Phong] [Material]
    └── Torus [Phong]
```

### *classmethod* `DebugPrint.PrintContainer(container: c4d.BaseContainer, keyHint: str | None = None) → None` <a id="mxutils.DebugPrint.PrintContainer"></a>

Prints the passed container as a debug tree.

See [`GetContainer()`](#mxutils.DebugPrint.GetContainer) for an explanation of the shared arguments. :return: None. :rtype: None

### *classmethod* `DebugPrint.PrintFlags(node: c4d.BaseList2D, showBit: bool = True, showNBit: bool = True, hint: str | None = None, showSetOnly: bool = False) → None` <a id="mxutils.DebugPrint.PrintFlags"></a>

Prints the passed node flags as a debug tree.

See [`GetFlags()`](#mxutils.DebugPrint.GetFlags) for an explanation of the shared arguments. :return: None. :rtype: None

### *classmethod* `DebugPrint.PrintGraph(node: c4d.BaseList2D) → None` <a id="mxutils.DebugPrint.PrintGraph"></a>

Prints the passed node graph as a debug tree.

See [`GetGraph()`](#mxutils.DebugPrint.GetGraph) for an explanation of the shared arguments. :return: None. :rtype: None

### *classmethod* `DebugPrint.PrintParameters(node: c4d.BaseList2D, showName: bool = True, showSymbol: bool = True, showDescId: bool = True, showType: bool = True, showHidden: bool = False, showValue: bool = True, hideLayoutElements: bool = True, blackList: tuple = (), whiteList: tuple = (), showDefaultValues: bool = True) → None` <a id="mxutils.DebugPrint.PrintParameters"></a>

Prints the passed node parameters as a debug tree.

See [`GetParameters()`](#mxutils.DebugPrint.GetParameters) for an explanation of the shared arguments. :return: None. :rtype: None
