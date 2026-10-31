<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/mxutils_api.html -->

# mxutils API <a id="mxutils-api"></a>

Contains helper functions and types that are written in Python and exclusive to the Python API.

## Overview <a id="overview"></a>

### Classes <a id="classes"></a>

|   |   |
|---|---|
| [`mxutils.DebugNode`](maxon_generated/mxutils/mxutils.DebugNode.md#module-mxutils.DebugNode)(name, nid) | Realizes a simple tree structure used in printing debug information. |
| [`mxutils.DebugPrint`](maxon_generated/mxutils/mxutils.DebugPrint.md#module-mxutils.DebugPrint)() | Contains utility functions for printing debug information about selected Cinema API data. |
| [`mxutils.IdProvider`](maxon_generated/mxutils/mxutils.IdProvider.md#module-mxutils.IdProvider)(idType) | Generates `int` or `maxon.Id` identifiers. |
| [`mxutils.LocalImportPath`](maxon_generated/mxutils/mxutils.LocalImportPath.md#module-mxutils.LocalImportPath)(path, autoReload) | Provides the ability to import packages and modules from directories that are not exposed to the global module search paths. |
| [`mxutils.Random`](maxon_generated/mxutils/mxutils.Random.md#module-mxutils.Random)(seed, magic, noPyReseed) | Generates pseudo-random floating point, integer, vector, color, and matrix values in a deterministic manner. |
| [`mxutils.SceneFaker`](maxon_generated/mxutils/mxutils.SceneFaker.md#module-mxutils.SceneFaker)(random) | Generates random scene data such as objects, materials, tags, layers, render data and tracks. |
| [`mxutils.SymbolTranslationCache`](maxon_generated/mxutils/mxutils.SymbolTranslationCache.md#module-mxutils.SymbolTranslationCache)(module, …) | Caches and provides access to string symbols over their integer values. |

### Functions <a id="functions"></a>

|   |   |
|---|---|
| [`mxutils.CheckIterable`](#mxutils.CheckIterable)(item[, tElement, …]) | Checks `item` for being an iterable of a specific type, being composed of specific elements, or being of specific length. |
| [`mxutils.CheckType`](#mxutils.CheckType)(item[, t, label]) | Checks `item` for being of type `t`. |
| [`mxutils.GetFirstSiblingNode`](#mxutils.GetFirstSiblingNode)(node) | Rewinds the passed *node* to its first sibling. |
| [`mxutils.GetMemoryAddress`](#mxutils.GetMemoryAddress)(obj) | Returns the native Python formatting memory address string for *#obj*. |
| [`mxutils.GetNodeFromPath`](#mxutils.GetNodeFromPath)(node, path[, …]) | Returns the node reached by following a hierarchy path from `node`. |
| [`mxutils.GetRootNode`](#mxutils.GetRootNode)(node) | Rewinds the passed *node* to its root. |
| [`mxutils.ImportSymbols`](#mxutils.ImportSymbols)(path[, output]) | Parses elements of all resource files contained in the given `path` into the global scope of the caller or into a dictionary. |
| [`mxutils.IterateGraph`](#mxutils.IterateGraph)(node[, yieldCaches, …]) | Yields nodes that are in some relationship with the passed `c4d.GeListNode` *node*. |
| [`mxutils.IterateTree`](#mxutils.IterateTree)(node[, yieldSiblings, …]) | Yields nodes that are hierarchically related to *node*. |
| [`mxutils.RecurseTree`](#mxutils.RecurseTree)(node) | Yields nodes that are hierarchically related to *node*. |

### Decorators <a id="decorators"></a>

|   |   |
|---|---|
| [`mxutils.TIMEIT`](#mxutils.TIMEIT)(enabled[, showDigits, …]) | Decorates a function call with a timing or profiling report printed to the console. |
| [`mxutils.SET_STATUS`](#mxutils.SET_STATUS)(message[, doSpin, …]) | Decorates a function call with output to the Cinema 4D status bar. |
| [`mxutils.REPORT`](#mxutils.REPORT)([character, characterCount]) | Decorates a function call by printing the function name, a horizontal bar below it, and an empty line after the function finished. |

## Attributes <a id="attributes"></a>

### `mxutils.g_c4d_symbol_translation_cache` <a id="mxutils.mxutils.g_c4d_symbol_translation_cache"></a>

Global [`mxutils.SymbolTranslationCache`](maxon_generated/mxutils/mxutils.SymbolTranslationCache.md#module-mxutils.SymbolTranslationCache) instance for the c4d module.

### `mxutils.g_id_provider` <a id="mxutils.mxutils.g_id_provider"></a>

Global [`mxutils.IdProvider`](maxon_generated/mxutils/mxutils.IdProvider.md#module-mxutils.IdProvider) instance.

### `mxutils.g_random` <a id="mxutils.mxutils.g_random"></a>

Global [`mxutils.Random`](maxon_generated/mxutils/mxutils.Random.md#module-mxutils.Random) instance.

### `mxutils.g_scene_faker` <a id="mxutils.mxutils.g_scene_faker"></a>

Global [`mxutils.SceneFaker`](maxon_generated/mxutils/mxutils.SceneFaker.md#module-mxutils.SceneFaker) instance.

### `mxutils.TRAVERSAL_BREADTH_FIRST` <a id="mxutils.mxutils.TRAVERSAL_BREADTH_FIRST"></a>

Enables breadth-first level-order traversal (BFS: breadth-first search).

### `mxutils.TRAVERSAL_DEPTH_FIRST` <a id="mxutils.mxutils.TRAVERSAL_DEPTH_FIRST"></a>

Enables depth-first pre-order traversal (NLR: node, left, right).

### `mxutils.TRAVERSAL_INVERSE_DEPTH_FIRST` <a id="mxutils.mxutils.TRAVERSAL_INVERSE_DEPTH_FIRST"></a>

Enables inverse depth-first post-order traversal (LRN: left, right, node).

## Function Listing <a id="function-listing"></a>

### `mxutils.CheckIterable(item: Any, tElement: Optional[Union[Type, tuple]] = None, tIterable: Optional[Union[Type, tuple]] = None, label: str | None = None, minCount: int | None = None, maxCount: int | None = None) → Any` <a id="mxutils.CheckIterable"></a>

Checks `item` for being an iterable of a specific type, being composed of specific elements, or being of specific length.

When any of the checks fail, an error is being raised. If not, `item` is being passed through. The function can automatically discover the symbol of `item` when it is defined in the local or global scope of the function call. While all types of iterables are supported, it is only `dict` and `c4d.BaseContainer` which are supported in their specific item, i.e., pairs, decomposition. All other iterables are treated as iterables of singular elements as for example lists or tuples.

When possible, it is advantageous to replace iterable type checks with type conversions due to the computationally expensive nature of checking every item in an iterable. The expensive part of this call is passing not `None` for `tElement`, i.e., checking the type of every element in `item` (when `item` is very large), all other checks are negligible in cost.

**Parameters:**

- **item** (*typing.Any*) – The item to be type checked.
- **tElement** (*typing.Type | tuple*[*typing.Type*] *| None* (, *optional*)) – The type or types of elements the iterable `item` is allowed to have. Passing `None` will will accept any kind of element type. Defaults to `None`.
- **tIterable** (*typing.Type | tuple*[*typing.Type*] *| None* (, *optional*)) – The type or types the iterable `item` is allowed to be. Passing `None` will accept any kind of iterable. Defaults to `None`.
- **label** (*str | None* (, *optional*)) – The label with which to refer to `item` in exceptions. Passing `None` will result in an attempt to infer the symbol. Defaults to `None`.
- **minCount** (*int | None* (, *optional*)) – The minimum length for the iterable `item`. Passing `None` will accept any iterable that is smaller than or equal to `maxCount`. Value must be smaller than or equal to `maxCount` Defaults to `None`.
- **maxCount** (*int | None* (, *optional*)) – The maximum length for the iterable `item`. Passing `None` will accept any iterable that is greater than or equal to `minCount`. Value must be larger or equal to `minCount` Defaults to `None`.

**Raises:**

- **TypeError** – When `item` is failing the type tests.
- **ValueError** – When `minCount` is larger than `maxCount`.
- **RuntimeError** – When any of the length checks fail.
- **RuntimeError** – When accessing a stack trace or reading an executed file failed on a symbol discovery attempt.

**Returns:** The value of `item` when the checks succeeded.

**Return type:** typing.Any

**Example:**

```python
import c4d

from mxutils import CheckIterable

# Checks if `data` is composed of strings only; this will fail as there is an `int` in it.
data: list[str|int] = ["1", "2", "3", 4, "5"]
data = CheckIterable(data, str)

# But the prior case is also an example for where element type assertions are unnecessary. 
# As we can enforce the type of items in `data` with `str()`.
item: str = str(data[3])

# The common use case is checking type composition assumptions of function arguments passed 
# by unsafe sources, in order to avoid carrying out expensive computations which fail in a 
# very late stage due to encountering a malformed item in the input data.
class Foo:
    def __init__(self, nodes: list[c4d.BaseObject | c4d.BaseTag]) -> None:
        # Assure that _nodes will be a list of tags and objects.
        self._nodes = CheckIterable(nodes, (c4d.BaseObject, c4d.BaseTag), list)

# Tested can also be the length of the iterable.

# Assures that `data` has at least the length of one. No specific type checks are performed 
# in this case, but `data` is still being tested for being an iterable. This is a very low
# cost call, no matter how large data is, as the first argument `tElement` has is `None` and
# `data` is therefore never traversed as elements of any type are accepted.
data = CheckIterable(data, minCount=1)

# Assures that `data` is not longer than five elements.
data = CheckIterable(data, maxCount=5)

# Assures that the length of `data` lies in the interval [1, 5].
data = CheckIterable(data, minCount=1, maxCount=5)

# The function will always test if ``item`` is an iterable, even when both type tests are
# set to None. So, this will raise an error as `int` does not implement `__iter__`
CheckIterable(1)

# but this will not, as `c4d.BaseContainer` does implement `__iter__`:
data: c4d.BaseContainer = c4d.BaseContainer()
CheckIterable(data)

# All forms of iterable are supported, but only `c4d.BaseContainer` and `dict` are handled
# manually to type test values in key, value pairs instead of testing the type of the pair.

data[0] = "Hello world"
data[1] = True
# Will test data for being of type BaseContainer, holding only values of type str or bool.
CheckIterable(data, (str, bool), c4d.BaseContainer)

# The same thing for dict, key type testing is not supported.
data = {1: "Hello World", "my_key": True}
CheckIterable(data, (str, bool), dict)
```

### `mxutils.CheckType(item: Any, t: Optional[Union[Type, tuple]] = None, label: str | None = None) → Any` <a id="mxutils.CheckType"></a>

Checks `item` for being of type `t`.

When the check fails, an error is being raised. If not, `item` is being passed through.

> **Note:** Automatic symbol discovery is only possible in saved files. Which makes it impossible in the console and Script Manager scripts which have not been yet saved.

**Parameters:**

- **item** (*typing.Any*) – The item to be type checked.
- **t** (*typing.Type | tuple*[*typing.Type*] *| None* (, *optional*)) – The type or types `item` is allowed to be. Passing `None` will only assert that `item` is not `None`. Defaults to `None`.
- **label** (*str | None* (, *optional*)) – The label with which to refer to `item` in exceptions. Passing `None` will result in an attempt to infer the symbol. Defaults to `None`.

**Raises:**

- **TypeError** – When `item` is failing the type test.
- **RuntimeError** – When accessing a stack trace or reading an executed file failed on a symbol discovery attempt.

**Returns:** The value of `item` when the check succeeded.

**Return type:** typing.Any

**Example:**

```python
import c4d
import math

from mxutils import CheckType

MY_INT: int = 42

class Foo:
    SOME_INT: int = 42

    def __init__(self, x: int) -> None:
        # Asserts that `x` is not `None`.
        CheckType(x)

        # Asserts that `x` is not `None` and assigns its values to `self._x`.
        self._x: object = CheckType(x)

        # Asserts that `MY_INT` is of type `int` or `float` and assigns its int value to `self._y`.
        self._y: int = int(CheckType(MY_INT, (int, float)))

        # CheckType and CheckIterable can now also discover expressions and variables that are not 
        # bound to the local or global scope.

        CheckType(math.pi, int) # math.pi is neither part of global or local scope.
        # TypeError: Expected value of type <class 'int'> for 'math.pi'. Received: <class 'float'>

        CheckType(c4d.BaseObject(c4d.Ocube), c4d.BaseObject) # A failed allocation results in None.
        # TypeError: Expected value of type <class 'c4d.BaseObject'> for 'c4d.BaseObject(c4d.Ocube)'.
        # Received: <class 'None'>
```

### `mxutils.GetContainerTreeString(*args, **kwargs) → str` <a id="mxutils.GetContainerTreeString"></a>

Deprecated, use *mxutils.DebugPrint.GetContainer(…).ToString()* instead.

### `mxutils.GetFirstSiblingNode(node: c4d.GeListNode) → c4d.GeListNode` <a id="mxutils.GetFirstSiblingNode"></a>

Rewinds the passed *node* to its first sibling.

**Parameters:** **node** ([*c4d.GeListNode*](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The node to rewind.

**Returns:** The first sibling node.

**Example:**

```python
import c4d
from mxutils import CheckType, GetFirstSiblingNode

# For the object tree:
#   A
#   |___B
#       |___C
#       |___D

# Find the object named "D" in the scene.
d: c4d.BaseObject = CheckType(doc.FindObject("D"))

# Rewind to the first sibling node.
firstSibling: c4d.GeListNode = GetFirstSiblingNode(d)
print (firstSibling.GetName())  # Output: C

# Find the first sibling of the object named "B" (it is B itself).
b: c4d.BaseObject = CheckType(doc.FindObject("B")) # Output: B
```

### `mxutils.GetMemoryAddress(obj: any) → str` <a id="mxutils.GetMemoryAddress"></a>

Returns the native Python formatting memory address string for *#obj*.

Can be useful when implementing the *__str__* or *__repr__* method of an object while wanting to maintain how Python naturally prints objects.

**Parameters:** **obj** (*any*) – The object for which to get the memory address string.

**Returns:** The memory address string.

**Return type:** str

**Example:**

```python
import mxutils

class Foo:
    def __init__(self, x: int) -> None:
        self.x = x

    def __str__(self) -> str:
        return (f"{self.__class__.__qualname__} (x={self.x}) "
                f"object at {mxutils.GetMemoryAddress(self)}")

f: Foo = Foo(42)
print(f)

# Output:

# Foo (x=42) object at 0x00000139A3198540
```

### `mxutils.GetNodeFromPath(node: c4d.GeListNode, path: str, raisePathErrors: bool = False) → c4d.GeListNode | None` <a id="mxutils.GetNodeFromPath"></a>

Returns the node reached by following a hierarchy path from `node`.

The path is evaluated from left to right and consists of the following navigation characters:

- `d` | `D`: Calls [`c4d.GeListNode.GetDown()`](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode.GetDown) to move to the first child node.
- `u` | `U`: Calls [`c4d.GeListNode.GetUp()`](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode.GetUp) to move to the parent node.
- `n` | `N`: Calls [`c4d.GeListNode.GetNext()`](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode.GetNext) to move to the next sibling node.
- `p` | `P`: Calls [`c4d.GeListNode.GetPred()`](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode.GetPred) to move to the previous sibling node.
- `r` | `R`: Calls [`GetRootNode()`](#mxutils.GetRootNode) to move to the root node.
- `f` | `F`: Calls [`GetFirstSiblingNode()`](#mxutils.GetFirstSiblingNode) to move to the first previous sibling node.

**Parameters:**

- **node** – The node from which to start navigating.
- **path** – The navigation path to follow. The search is case-insensitive.
- **raisePathErrors** – Whether to raise a `ValueError` when the path cannot be followed. When set to `False`, the function will return `None` for invalid paths. Defaults to `False`.

**Returns:** The node reached by the path.

**Raises:**

- **TypeError** – If `node`, `path`, or `raisePathErrors` has an invalid type.
- **ValueError** – If `raisePathErrors` is `True` and the path contains an unknown character or cannot be followed.

**Example:**

```python
import c4d
from mxutils import CheckType, GetNodeFromPath

# For the object tree:
#   A
#   ├── B
#   │   ├── C
#   │   └── D
#   └── E

d: c4d.BaseObject = CheckType(doc.FindObject("D"))
a: c4d.GeListNode = GetNodeFromPath(d, "r")
c: c4d.GeListNode = GetNodeFromPath(d, "p")
e: c4d.GeListNode = GetNodeFromPath(d, "nf")
```

### `mxutils.GetParameterTreeString(*args, **kwargs) → str` <a id="mxutils.GetParameterTreeString"></a>

Deprecated, use *mxutils.DebugPrint.GetParameters(…).ToString()* instead.

### `mxutils.GetRootNode(node: c4d.GeListNode) → c4d.GeListNode` <a id="mxutils.GetRootNode"></a>

Rewinds the passed *node* to its root.

**Parameters:** **node** ([*c4d.GeListNode*](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The node to rewind.

**Returns:** The root node.

**Example:**

```python
import c4d
from mxutils import CheckType, GetRootNode

# For the object tree:
#   A
#   |___B   
#   |   |___C   
#   |   |___D 
#   E
#   |___F

# Find the object named "D" in the scene.
d: c4d.BaseObject = CheckType(doc.FindObject("D"))

# Rewind to the root node.
root: c4d.GeListNode = GetRootNode(d)
print (root.GetName())  # Output: A

# Find the root of the object named "F".
f: c4d.BaseObject = CheckType(doc.FindObject("F"))
e: c4d.BaseObject = GetRootNode(f) # Output: E
```

### `mxutils.GetSceneGraphString(*args, **kwargs) → str` <a id="mxutils.GetSceneGraphString"></a>

Deprecated, use *mxutils.DebugPrint.GetGraph(…).ToString()* instead.

### `mxutils.GetTreeString(*args, **kwargs) → str` <a id="mxutils.GetTreeString"></a>

Deprecated, use *mxutils.DebugPrint.GetTreeString* instead.

### `mxutils.ImportSymbols(path: str, output: Type = None) → dict[str, float | int | str] | None` <a id="mxutils.ImportSymbols"></a>

Parses elements of all resource files contained in the given `path` into the global scope of the caller or into a dictionary.

> **See also:** [Symbol Parsing](../manuals/manual_symbol_parsing.md#manual-py-symbols)

**Parameters:**

- **path** (*str*) – The path within which header files should be discovered and parsed.
- **output** (*typing.Type*) – If the parsed symbols should be placed in the global scope or be returned as a dictionary. Pass `None` to let them be placed in the global scope and `dict` to have the function return them as a dictionary. Defaults to `None`.

**Returns:** The parsed symbol value pairs as or nothing when the `output` was `None`

**Return type:** dict[str, float | int | str] | None

**Example:**

The following header file `c:\data\c4d_symbols.h`,

```cpp
enum
{
    ID_FOO = 1000,
    ID_BAR = 1001,
    _DUMMY_ELEMENT_
};
```

can be imported as follows:

```python
import os
import mxutils

# Recursively parse header files in "c:\data" into this scope.
mxutils.ImportSymbols("c:\data")

# This would also work when only a singular file should be parsed.
mxutils.ImportSymbols("c:\data\c4d_symbols.h")

# The parsed symbols are now exposed in the global scope.
print(ID_FOO) # Will print 1000
print(ID_BAR) # Will print 1001

# Alternatively, symbols can also be parsed into a dictionary.
data: dict[str, int] = mxutils.ImportSymbols("c:\data\c4d_symbols.h", output=dict)

print(data["ID_FOO"]) # Will print 1000
print(data["ID_BAR"]) # Will print 1001
```

### `mxutils.IterateGraph(node: c4d.GeListNode, yieldCaches: bool = False, yieldBranches: bool = False, yieldHierarchy: bool = False, nodeFilter: list[int] | None = None, branchFilter: list[int] | None = None, maxBranchingDepth: int | None = None, stopBranchingEarly: bool = False, complexYield: bool = False, **kwargs: Any) → Iterator[c4d.GeListNode | tuple[c4d.GeListNode, c4d.GeListNode, int, bool, bool]]` <a id="mxutils.IterateGraph"></a>

Yields nodes that are in some relationship with the passed `c4d.GeListNode` *node*.

The Cinema API of Cinema 4D has a special view on the concept of a scene graph where node relations are split into three categories: hierarchies, caches, and branches; each with their own set of functions to traverse such relationships. This function combines these three categories into one interface that can be used to traverse the scene graph in a more user-friendly way.

> **Note:** This function is about the Cinema API concept of a node as represented by *c4d.GeListNode*. It is not about nodes in the sense of the Nodes API, i.e. *maxon.GraphNode*. You cannot traverse node graphs of the Nodes API with this function.

> **Warning:** This function is relatively computationally expensive in large scenes. It should not be used in performance critical scenarios, e.g., a *MessageData* plugin that scans the whole scene every 50ms. In these cases, write a custom traversal function that is tailored to your specific needs. For very large scenes (as in 1000s of nodes), expect execution times in the order of multiple milliseconds per traversal. The argument *stopBranchingEarly* is crucial in reducing traversal times, as it can mean the difference between traversing a few hundred nodes and traversing thousands of nodes in large scenes.

> **Note:** This function can still be called via its legacy symbol *mxutils.RecurseGraph* for backwards compatibility.

**Parameters:**

- **node** ([*c4d.GeListNode*](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The node to start the iteration from.

- **yieldCaches** (*bool*, *optional*) – Whether to yield the caches of the node, defaults to *False*.

- **yieldBranches** (*bool*, *optional*) – Whether to yield the branches of the node, defaults to *False*.

- **yieldHierarchy** (*bool*, *optional*) – Whether to yield the hierarchy of the node, defaults to *False*.

- **nodeFilter** (*list*[*int**] or* *None*, *optional*) –

  A list of node types that should be yielded or *None* for all types, defaults to *None*. Examples for node type symbols are:

  - *c4d.Tbaselist2d* matches all nodes (except for branch heads which are not yielded by this function anyway).
  - *c4d.Obase* matches all objects.
  - *c4d.Ocube* matches a cube object.
  - *c4d.Mbase* matches all materials.
  - *c4d.Mmaterial* matches a standard material.
  - *c4d.Tbase* matches all tags.
  - *c4d.Ttexture* matches a texture tag.
  - *c4d.Xbase* matches all shaders.
  - *c4d.Xnoise* matches a noise shader.
  - *c4d.GVbase* matches all xpresso nodes.
  - …

  > **See also:** [Types and Symbols List](../indexes/type_index.md) for a list of node type symbols.

- **branchFilter** (*list*[*int**] or* *None*, *optional*) –

  A list of branch types to filter the branches by or *None* for all types, defaults to *None*. Common branch types are:

  - *c4d.Obase* for objects.
  - *c4d.Mbase* for materials.
  - *c4d.Olayer* for layers.
  - *c4d.Xbase* for shaders.
  - *c4d.Tbase* for tags.
  - *c4d.Rbase* for render data.
  - *c4d.GVbase* for xpresso graphs.
  - *c4d.CTbase* for tracks.
  - *c4d.CSbase* for curves.
  - *c4d.SHplugin* for scene hooks.

- **maxBranchingDepth** (*int* or *None*, *optional*) – The maximum depth to which to traverse branches to or *None* to apply no limit, defaults to *None*.

- **stopBranchingEarly** (*bool*, *optional*) – Whether to stop branching early when a branch does not meet the branch filter criteria, defaults to *False*.

- **complexYield** (*bool*, *optional*) – Whether to yield complex values or just the current node, defaults to *False*.

- **kwargs** – Additional private keyword arguments. Do not pass any arguments to this function that are not documented here as you might accidentally override internal arguments.

**Returns:**

An iterator that yields the nodes that are in some relationship with the passed *node* based on the search criteria. When *complexYield* is set to True, the function yields the tuple *[node, owner, depth, isBranch, isCache]* where:

- *node* is the node that is yielded.
- *owner* is the node that holds the cache or branch.
- ***depth* is the traversal depth of the current node. The depth is 0 for the passed node,** each level increases the depth by 1.
- *isBranch* is a flag that indicates if the node is part of a branch relationship.
- *isCache* is a flag that indicates if the node is part of a cache relationship.

**Return type:** typing.Iterator[[c4d.GeListNode](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)] or typing.Iterator[tuple[[c4d.GeListNode](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode), [c4d.GeListNode](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode), int, bool, bool]]

**Example:**

```python
import c4d
import mxutils

doc: c4d.documents.BaseDocument  # The currently active document.
op: c4d.BaseObject | None  # The primary selected object in `doc`. Can be `None`.

# This is the scene we will be working with.
#   doc
#   ├── Objects
#   │   └── Cube (selected) [Motion Tag][Phong Tag][Material Tag]
#   │       └── Sphere [Phong Tag][Material Tag]
#   │           └── Position.Y Track
#   ├── Materials
#   │   └── Mat.1
#   │       └── Layer Shader
#   │           ├── Gradient
#   │           └── Noise
#   ├── Layers
#   │   ├── Layer.1
#   │   └── Layer.2
#   └── Render Settings
#       ├── Motion Source Render Data
#       └── My Render Settings.1

# With this function we can iterate over all nodes (GeListNode) in a scene, such as objects, tags, 
# materials, shaders, and many things more. All these things are in a branching relation to each 
# other expressed by GeListNode.GetBranchInfo() and the hierarchical relations expressed by the
# other GeListNode methods.

# When we pass only the active object #op to IterateGraph() nothing will happen as all traversal
# options are disabled by default. To use the function, we always have to configure the output.
print("IterateGraph(op):")
for node in mxutils.IterateGraph(op):
    print(node)

# > IterateGraph(op):

# Here we we enable hierarchical traversal by setting yieldHierarchy=True. This will yield the
# nodes that are in a hierarchical descendant relation to the active object.
print("IterateGraph(op, yieldHierarchy=True):")
for node in mxutils.IterateGraph(op, yieldHierarchy=True):
    print(node)

# > IterateGraph(op, yieldHierarchy=True):
# > <c4d.BaseObject object called Cube/Cube with ID 5159 at 2544283200960>          # The active object #op.
# > <c4d.BaseObject object called Sphere/Sphere with ID 5160 at 2544283291584>      # The child of #op.

# --------------------------------------------------------------------------------------------------------------

# But there are more traversal options. We can also yield caches for example. We must leave the 
# hierarchical traversal enabled when we not only want to see the direct cache of #op but also
# hierarchal relations within that cache and the cache of objects parented to #op.
print("IterateGraph(op, yieldHierarchy=True, yieldCaches=True):")
for node in mxutils.IterateGraph(op, yieldHierarchy=True, yieldCaches=True):
    print(node)

# > IterateGraph(op, yieldHierarchy=True, yieldCaches=True):
# > <c4d.BaseObject object called Cube/Cube with ID 5159 at 2544283200960>          # #op
# > <c4d.PolygonObject object called Cube/Polygon with ID 5100 at 2547767808256>    # Its cache.
# > <c4d.BaseObject object called Sphere/Sphere with ID 5160 at 2544283291584>      # The child of #op.
# > <c4d.PolygonObject object called Sphere/Polygon with ID 5100 at 2547767808256>  # Its cache.

# --------------------------------------------------------------------------------------------------------------

# The most important traversal dimension is branching, it is what ties a Cinema API scene graph
# together. We enable it by setting #yieldBranches to #True. We also enable complex yielding here
# which will change the yield type of the function to also provide traversal metadata. We turn off
# cache traversal as this example would get otherwise too long as caches also hold branches.

print("IterateGraph(op, yieldBranches=True, yieldHierarchy=True, complexYield=True):")
for node, owner, depth, isBranch, isCache in mxutils.IterateGraph(
    op, yieldBranches=True, yieldHierarchy=True, complexYield=True):

    prefix: str = "[]" if not isBranch else "[BRANCH]"
    space: str = "  " * depth
    nodeStr: str = f"{node.GetName()}({node.__class__.__name__})"
    ownerStr: str = f"[{owner.GetName()}]" if owner else ""
    print (f"{space}{prefix} {nodeStr}{ownerStr}")

# > IterateGraph(op, yieldBranches=True, yieldHierarchy=True, complexYield=True):
# > [] Cube.1(BaseObject)                              # Active object, #op.
# >    [BRANCH] Position.X(CTrack)[Cube.1]             # Pos.X track of, in the track branch owned by #op.
# >        [BRANCH] (CCurve)[Position.X]               # Curve of it, in the curve branch owned by the track.
# >    [BRANCH] Motion System(BaseTag)[Cube.1]         # Motion System tag of #op, tag branch of #op.
# >        [BRANCH] Layer(BaseList2D)[Motion System]   # A layer in the layer branch of the motion system.
# >            [BRANCH] Cube(BaseObject)[Layer]        # An object in the object branch of the layer.
# >    [BRANCH] Phong(BaseTag)[Cube.1]                 # Phong tag in the tag branch of #op.
# >    [BRANCH] Material(TextureTag)[Cube.1]           # Material tag in the tag branch of #op.
# >    [] Sphere(BaseObject)                           # The sphere object child of #op.
# >        [BRANCH] Position . Y(CTrack)[Sphere]       # Pos.Y track of the sphere.
# >            [BRANCH] (CCurve)[Position . Y]         # Its curve.
# >        [BRANCH] Phong(BaseTag)[Sphere]             # Phong tag of the sphere.

# We can see that there are many hidden things in the branches of a scene element. The motion system
# holds attached to #op an internal copy of #op, and there is also a track on #op which is not
# visible in the timeline. It is the position track the motion system layer has been created 
# from (and is therefor now hidden from the user).

# --------------------------------------------------------------------------------------------------------------

# Even a seemingly simple scene can be quite complex under the hood. Since a document (BaseDocument)
# is a node itself, we can also start the traversal from the document. When we now enable everything
# which can be enabled regarding traversal complexity, we will traverse every node in the scene.

print("IterateGraph(doc, yieldBranches=True, yieldHierarchy=True, complexYield=True):")
allNodes: list[c4d.GeListNode] = list(mxutils.IterateGraph(doc, True, True, True))
print(f"Total number of nodes: {len(allNodes)}")flush#

# > IterateGraph(doc, yieldBranches=True, yieldHierarchy=True, complexYield=True):
# > Total number of nodes: 118

# Our scene contains 118 nodes in total but there are only 18 tangible nodes when we count every
# object, tag, track, curve, material, shader, layer, and render setting. The remaining nodes are
# in hidden branches like the motion system or in caches.

# --------------------------------------------------------------------------------------------------------------

# To deal with this overwhelming amount of information, IterateGraph() offers tools to filter the
# output of traversal. An important filter is the #branchFilter. It limits the yielded nodes to
# the provided branch types. This does not mean by default that the function will not traverse
# other branches, but it will not yield from them,

# Traverse #doc in full complexity, but only yield nodes that are part of an Object or Curve branch.
print("IterateGraph(doc, ... branchFilter=[c4d.Obase, c4d.CSbase]):")
for node in mxutils.IterateGraph(doc, True, True, True, branchFilter=[c4d.Obase, c4d.CSbase]):
    print (f"`{node.GetName()}`({node.__class__.__name__})")

# > IterateGraph(doc, ... branchFilter=[c4d.Obase, c4d.CSbase]):
# > ``(BaseDocument)`
# > `Cube`(BaseObject)
# > `Cube`(PolygonObject)
# > ``(CCurve)`
# > `Sphere`(BaseObject)
# > `Sphere`(PolygonObject)
# > ``(CCurve)`
# > `Default Simulation Scene`(BaseObject)
# > `PKHOP`(BaseObject)

# We get CCurve and BaseObjects yielded, but also a singular BaseDocument. This is because the input
# node does not have a branch in the logic of this method (it might very well have), it simply does
# not look at it. Here this is of course true, there is nothing above a document. 

# The last two yielded nodes might also be a bit surprising, they are objects being held by scene hooks, 
# a special kind of hidden scene element type that acts like a spider in the net to control things in 
# the scene; yet another example for hidden scene elements in a scene.

# --------------------------------------------------------------------------------------------------------------

# With #stopBranchingEarly we can make sure that the traversal only goes into the branches we
# specify. This is different from the default, as which will only yield from the specified
# branch types but still traverse the whole scene.

print("IterateGraph(doc, ..., branchFilter=[c4d.Obase, c4d.CTbase], stopBranchingEarly=True):")
for node in mxutils.IterateGraph(doc, True, True, True, 
    branchFilter=[c4d.Obase, c4d.CTbase], stopBranchingEarly=True):
    print (f"`{node.GetName()}`({node.__class__.__name__})")

# > IterateGraph(doc, ..., branchFilter=[c4d.Obase, c4d.CTbase], stopBranchingEarly=True):
# > ``(BaseDocument)`
# > `Cube`(BaseObject)
# > `Cube`(PolygonObject)
# > `Position.X`(CTrack)
# > `Sphere`(BaseObject)
# > `Sphere`(PolygonObject)
# > `Position.Y`(CTrack)

# The last two objects have now disappeared from the output. Because they are parts of the
# Obase branches of two scene hooks which themselves are part of the SHplugin branch of #doc.
# And since we do not include SHplugin in the branchFilter, the traversal stops at the scene
# hooks branch SHplugin. Analogously, if our scene would have animations anywhere else than on
# objects, we could not see them either, as we never step into tag, material, shader, etc. 
# branches.

# --------------------------------------------------------------------------------------------------------------

# Another filter option is the branching #maxDepth. When we pass here for example 1, and start at
# document level, we will never see tags or shaders, as we will only go only one level deep, i.e.,
# direct branches of the document. But tags are branches of objects and shaders are branches of
# materials, shaders, objects, tags, etc., but never documents. So, would need at least a depth of
# 2 to see tags and shaders. 
for node in mxutils.IterateGraph(doc, True, True, True,  maxDepth=1):
    print (node)

# --------------------------------------------------------------------------------------------------------------

# The last and for non-power-users probably the most important filter is the #nodeFilter. It 
# simply allows us to do type checks before yielding a node. The same could also easily be done
# with a line like `if node.Chekcktype(c4d.Obase): doStuff()` inside a IterateGraph() loop.

# Grab all Xpresso nodes from the document, e.g., an Xpresso "Contant" node in an Xpresso tag. 
for xpressoNode in mxutils.IterateGraph(doc, True, True, True, nodeFilter=[c4d.GVbase]):
    print (xpressoNode)

# Get all Cube objects and Phong tags in the scene, regardless of where they hide.
for node in mxutils.IterateGraph(doc, True, True, True, nodeFilter=[c4d.Ocube, c4d.Tphong]):
    print (node)

# The danger of these two examples is that we get yielded nodes we assume to be something
# different then what they are, there is for example still an Ocube held by the motion system. A
# way out of this is using complex yielding and checking the type of the owner of each node, we 
# then can for example discard every cube that is not owned directly by a document.
for node, owner, *_ in mxutils.IterateGraph(doc, True, True, True, nodeFilter=[c4d.Ocube], complexYield=True):
    if node.CheckType(c4d.Ocube) and not isinstance(owner, c4d.documents.BaseDocument):
        continue
```

### `mxutils.IterateTree(node: c4d.GeListNode | None, yieldSiblings: bool = False, rewindToFirstSibling: bool = False, rewindToRoot: bool = False, traversalMode: int = 0) → Iterator[c4d.GeListNode]` <a id="mxutils.IterateTree"></a>

Yields nodes that are hierarchically related to *node*.

**Parameters:**

- **node** ([*c4d.GeListNode*](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode) or *None*) – The root node to start iterating from.
- **yieldSiblings** (*bool*, *optional*) – Whether to yield the next siblings of the current node, defaults to *False*.
- **rewindToFirstSibling** (*bool*, *optional*) – Whether to rewind the node to its first sibling before the iteration is carried out, defaults to *False*.
- **rewindToRoot** (*bool*, *optional*) – Whether to rewind the node to its root before the iteration is carried out, defaults to *False*.
- **traversalMode** (*int*, *optional*) – The traversal mode, defaults to [`mxutils.TRAVERSAL_DEPTH_FIRST`](#mxutils.mxutils.TRAVERSAL_DEPTH_FIRST). Must be one of [`mxutils.TRAVERSAL_DEPTH_FIRST`](#mxutils.mxutils.TRAVERSAL_DEPTH_FIRST), [`mxutils.TRAVERSAL_INVERSE_DEPTH_FIRST`](#mxutils.mxutils.TRAVERSAL_INVERSE_DEPTH_FIRST), or [`mxutils.TRAVERSAL_BREADTH_FIRST`](#mxutils.mxutils.TRAVERSAL_BREADTH_FIRST).

**Returns:** An iterator that yields the descendants of the passed *node*.

**Return type:** typing.Iterator[[c4d.GeListNode](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)]

**Raises:** **ValueError** – If *traversalMode* is not a supported traversal mode.

**Example:**

```python
import c4d
from mxutils import CheckType, IterateTree

# For the object tree:
#
#   A
#   ├── B
#   │   ├── C
#   │   ├── D
#   │   │   └── E
#   │   └── F
#   G

# Find the object named "D" in the scene.
d: c4d.BaseObject = CheckType(doc.FindObject("D"))

# Will yield D and E.
for node in IterateTree(d):
    print (node)

# Will yield D, E, and F. But not C as we start out at D and #yieldSiblings only looks
# downwards, at next siblings and not previous ones.
for node in IterateTree(d, yieldSiblings=True):
    print (node)

# Will yield C, D, E, and F. Because we rewind to the first sibling of D - which is C.
for node in IterateTree(d, yieldSiblings=True, rewindToFirstSibling=True):
    print (node)

# Will yield A, B, C, D, E, and F. But not G, as we do not yield siblings.
for node in IterateTree(d, rewindToRoot=True):
    print (node)

# Will always yield the whole tree, no matter where we start.
for node in IterateTree(d, True, True, True):
    print (node)

# Get the root and try out the traversal modes.
a: c4d.BaseObject = CheckType(doc.FindObject("A"))

# Depth-first traversal is the default mode. It yields elements in a top-down manner,
# just as a human would naturally read the tree from top to bottom, left to right. Will 
# yield: A, B, C, D, E, F, G.
for node in IterateTree(a, True, traversalMode=mxutils.TRAVERSAL_DEPTH_FIRST):
    print (node)

# Inverse depth-first traversal enables processing elements in a bottom-up manner, processing 
# children before their parents, this is often useful for cleanup or dependency resolution 
# tasks. Will yield: C, E, D, F, B, A, G.
for node in IterateTree(a, True, traversalMode=mxutils.TRAVERSAL_INVERSE_DEPTH_FIRST):
    print (node)

# Breadth-first traversal (BFS) processes nodes level by level, from left to right. This is 
# useful for scenarios where you want to process all nodes at a given depth before moving to 
# the next level. Will yield: A, G, B, C, D, F, E.
for node in IterateTree(a, True, traversalMode=mxutils.TRAVERSAL_BREADTH_FIRST):
    print (node)
```

### `mxutils.RecurseGraph(node: c4d.GeListNode, yieldCaches: bool = False, yieldBranches: bool = False, yieldHierarchy: bool = False, nodeFilter: list[int] | None = None, branchFilter: list[int] | None = None, maxBranchingDepth: int | None = None, stopBranchingEarly: bool = False, complexYield: bool = False, **kwargs: Any) → Iterator[c4d.GeListNode | tuple[c4d.GeListNode, c4d.GeListNode, int, bool, bool]]` <a id="mxutils.RecurseGraph"></a>

Deprecated, use [`mxutils.IterateGraph()`](#mxutils.IterateGraph) instead.

### `mxutils.RecurseTree(node: c4d.GeListNode) → Iterator[c4d.GeListNode]` <a id="mxutils.RecurseTree"></a>

Yields nodes that are hierarchically related to *node*.

> **Note:** This function is slower than *IterateTree* for medium to large trees. For small trees (<= 100 nodes) this function is negligibly faster than the iterative version.

> **Warning:** This function uses recursion to traverse the parent-child relations of the node tree. This bears the risk of hitting the recursion limit of Python; or worse, a stack overflow in the C++ backend when you increase the limit too much. If you want to be safe, use *IterateTree* instead.

**Parameters:** **node** ([*c4d.GeListNode*](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The root node to start iterating from.

**Returns:** An iterator that yields the descendants of the passed *node*.

**Return type:** typing.Iterator[[c4d.GeListNode](c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)]

**Example:**

```python
import c4d
import mxutils
from mxutils import RecurseTree

# Iterate over all objects that are descendants of the active object. This will not yield
# the siblings before and after op, use `IterateTree` for that.
for obj in mxutils.RecurseTree(op):
    print(obj)
```

## Decorator Listing <a id="decorator-listing"></a>

### `mxutils.TIMEIT(enabled: bool, showDigits: int = 5, showArgs: bool = False, showResult: bool = False, useProfiler: bool = False, inCallProtection: bool = False) → Callable[[T], T]` <a id="mxutils.TIMEIT"></a>

Decorates a function call with a timing or profiling report printed to the console.

Meant for debugging and profiling purposes only. The decorator can be enabled or disabled by passing a boolean flag to the decorator. When enabled, the decorator will print a report to the console after the function call has finished.

> **Warning:** This decorator will have an impact on the performance of the decorated function (timing = low impact, profiling = high impact). It is not recommended to use this decorator in production code.

**Parameters:**

- **enabled** (*bool*) – Whether the decorator should be enabled. Setting this to *False* will result in the decorated function being passed through without any modifications, disabling all measurements and almost all overhead of the decorator. You should pass here some debug flag you defined, e.g., *IS_DEBUG*.
- **showDigits** (*int*, *optional*) – The number of digits to round timing measurements to. Only applies when *useProfiler* is *False*. Defaults to *5*.
- **showArgs** (*bool*, *optional*) – Whether the arguments of the function call should be printed. Defaults to *False*.
- **showResult** (*bool*, *optional*) – Whether the result of the function call should be printed. Defaults to *False*.
- **useProfiler** (*bool*, *optional*) – Whether the function should be profiled instead of timed. Defaults to *False*.
- **inCallProtection** (*bool*, *optional*) – If to mute inner calls of a recursive call chain of the decorated function. This feature is not thread-safe as it decorates the function or class instance object with a dictionary to keep track of the call state. Defaults to *False*.

**Example:**

```python
import math
import mxutils

IS_DEBUG: bool = True

# We define a recursive function and decorate it with the default timeit decorator.
@mxutils.TIMEIT(IS_DEBUG)
def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n - 1)

# We call the function and see the time measurements. Because the function is recursive, we 
# see the a report for each call in the recursion chain.
factorial(3)
# --------------------------------------------------------------------------------
# TIMEIT: Ran 'factorial()' in 0.0 sec
# --------------------------------------------------------------------------------
# TIMEIT: Ran 'factorial()' in 6e-05 sec
# --------------------------------------------------------------------------------
# TIMEIT: Ran 'factorial()' in 0.00011 sec
# --------------------------------------------------------------------------------
# TIMEIT: Ran 'factorial()' in 0.00013 sec

# We redefine the function but this time enable in-call protection. We also enable seeing 
# the arguments and result of a function call.
@mxutils.TIMEIT(IS_DEBUG, showArgs=True, showResult=True, inCallProtection=True)
def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n - 1)

# Now we call the function again. This time we only see the the timing for the outmost
# call of the recursion chain.
factorial(10)
# --------------------------------------------------------------------------------
# TIMEIT: Ran 'factorial((10,), {}) -> 3628800' in 1e-05 sec

# And finally a more complex example where we decorate class methods and use full profiling.
class Processor: 
    # The arguments we pass to the timeit decorator in this class.
    TIMEIT_KWARGS: dict[str, typing.Any] = {
        "enabled": IS_DEBUG, "showArgs": True, 
        "showResult": True, "inCallProtection": True, 
        "useProfiler": True
    }

    def __init__(self, n: int) -> None:
        self.recursive(n)
        self.iterative(n)

    @mxutils.TIMEIT(**TIMEIT_KWARGS)
    def recursive(self, n: int) -> int:
        return 1 if n == 0 else n * self.recursive(n - 1)

    @mxutils.TIMEIT(**TIMEIT_KWARGS)
    def iterative(self, n: int) -> int:
        x: int = n
        for i in range(int(n * 1000)):
            x += math.sqrt(x)
            x *= math.sin(i)
        return x

p: Processor = Processor(50)

# The output will look something like this. For the recursive call we mostly see the overhead
# of the decorator. Profiling recursive functions in this manner that are not very expensive 
# (execute in the microsecond range) is not very useful.

# --------------------------------------------------------------------------------
# TIMEIT: Ran 'recursive((<__main__.Processor object at 0x7fd18c0696a0>, 50), {}) -> 
#     30414093201713378043612608166064768844377641568960512000000000000' with 302 function 
#     calls (203 primitive calls) in 0.000 seconds
#
#     Ordered by: cumulative time
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       51/1    0.000    0.000    0.000    0.000 scriptmanager:476(recursive)
#       50/1    0.000    0.000    0.000    0.000 scriptmanager:401(wrapper)
#         50    0.000    0.000    0.000    0.000 /Applications/Maxon Cinema 4D 2024.4.0/...
#         50    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#         50    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
#         50    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
#         1     0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# --------------------------------------------------------------------------------
# TIMEIT: Ran 'iterative((<__main__.Processor object at 0x7fd18c0696a0>, 50), {}) -> -0.0' with 
#     100002 function calls in 0.037 seconds
#
#    Ordered by: cumulative time
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#          1    0.025    0.025    0.037    0.037 scriptmanager:480(iterative)
#      50000    0.007    0.000    0.007    0.000 {built-in method math.sin}
#      50000    0.005    0.000    0.005    0.000 {built-in method math.sqrt}
#          1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

### `mxutils.SET_STATUS(message: str | None, doSpin: bool = False, clearOnReturn: bool = True) → Callable[[T], T]` <a id="mxutils.SET_STATUS"></a>

Decorates a function call with output to the Cinema 4D status bar.

This decorator is meant to be used in functions or methods which take a long time to execute and should be indicated in the Cinema 4D status bar. The decorator will display a message in the status bar while the function or method is being executed.

> **Note:** Use this decorator sparingly. Its overhead is low but status bar spam can confuse or annoy users.

**Parameters:**

- **message** (*str | None*, *optional*) – The message to be displayed in the status bar. Will not be displayed when *None*. Defaults to *None*.
- **doSpin** (*bool*, *optional*) – Whether the status bar should display the spin bar to signal an ongoing computation. Defaults to *False*.
- **clearOnReturn** (*bool*, *optional*) – Whether the status bar should be cleared when the function or method returns. Defaults to *True*.

**Example:**

```python
import c4d
import mxutils

# We define a function and decorate it with the SET_STATUS decorator.
@mxutils.SET_STATUS("Processing data ...", doSpin=True)
def process_data(data: list[int]) -> list[int]:
    return [x ** .5 for x in data]

# We call the function and see the status bar message in Cinema 4D.
process_data(list(range(10000)))
```

### `mxutils.REPORT(character: str = '-', characterCount: int = 100) → Callable[[T], T]` <a id="mxutils.REPORT"></a>

Decorates a function call by printing the function name, a horizontal bar below it, and an empty line after the function finished.

Can be useful when debugging functions which print to the console.

**Parameters:**

- **character** (*int*, *optional*) – The character(s) out of which the bar is composed. Defaults to *-*.
- **characterCount** (*int*, *optional*) – How often *character* is repeated. Defaults to *100*.

**Example:**

```python
import c4d
import mxutils

# We decorate a function with the default arguments.
@mxutils.REPORT()
def foo(msg: str) -> None:
    print(f"{msg = }")

class Bar:
    # We decorate a method with a custom horizontal bar.
    @mxutils.REPORT("=", 50)
    def baz (self, msg: str) -> None:
        print(f"{msg = }")

# Now we invoke the function and method.
bar: Bar = Bar()

foo("Hello World!")
bar.baz("Bob's your uncle!")

# Output:

# Running 'foo':
# ---------------------------------------------------------------------------------------...
# msg = 'Hello World!'
#
# Running 'Bar.baz (object at 0x0000020BEE9B57A0)':
# ==================================================
# msg = "Bob's your uncle!"
```
