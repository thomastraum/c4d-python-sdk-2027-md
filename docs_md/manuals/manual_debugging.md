<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_debugging.html -->

# Debugging <a id="debugging"></a><a id="manual-debugging"></a>

Explains how to find errors in Python code for Cinema 4D with the mxutils debug tools, and how to track down crashes caused by threading violations.

Python code in Cinema 4D mostly runs inside the application, and often in callbacks which Cinema 4D calls on its own schedule and on a thread of its choosing, see [Scene Execution](manual_scene_execution.md). This makes classic step debugging inconvenient, and at the moment impossible, see below. This manual describes what remains: inspecting scene data with the mxutils debug tools, failing early with type checks, tracing and timing calls, building reproducible test scenes, and tracking down crashes that are caused by violating the threading restrictions.

> **Warning:** The VS Code debugger is currently broken. Setting breakpoints in scripts or plugins with the Cinema 4D Connector or `debugpy`, as described in [Working with the SDK](manual_working_with_sdk.md), does not work at the moment, and debugging [c4dpy](manual_standalone_interpreter.md) with `F5` does not work out of the box either. Until this is fixed, use the techniques of this manual, none of which depend on an IDE.

## Overview <a id="overview"></a>

| Question | Tool |
|---|---|
| What is in this container, node, or scene? | [`mxutils.DebugPrint`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#module-mxutils.DebugPrint) `Get` and `Print` functions |
| What is different between these two nodes? | [`mxutils.DebugPrint`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#module-mxutils.DebugPrint) `Diff` functions |
| Is this value what I think it is? | [`mxutils.CheckType()`](../modules/mxutils_api.md#mxutils.CheckType) and [`mxutils.CheckIterable()`](../modules/mxutils_api.md#mxutils.CheckIterable) |
| Was my function called, how often, and how long did it take? | [`mxutils.REPORT()`](../modules/mxutils_api.md#mxutils.REPORT) and [`mxutils.TIMEIT()`](../modules/mxutils_api.md#mxutils.TIMEIT) |
| I need a scene to test my code with. | [`mxutils.SceneFaker`](../modules/maxon_generated/mxutils/mxutils.SceneFaker.md#module-mxutils.SceneFaker) |
| Cinema 4D crashes or hangs, but not always. | [Threading violations](#debugging-threading) and `faulthandler` |

The output of all tools ends up in the Python Console. Call [`c4d.ClearPythonConsole()`](../modules/c4d/index.md#c4d.ClearPythonConsole) at the start of a script to keep it readable, and print behind a flag such as `IS_DEBUG` in code that runs often, e.g., in callbacks which are called for every update. Very large trees, e.g., of a whole document, can exceed what the console prints in one go. Print them in slices, or write them to a file.

## Inspecting Scene Data <a id="inspecting-scene-data"></a>

The class [`mxutils.DebugPrint`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#module-mxutils.DebugPrint) converts data of the Cinema API into trees of [`mxutils.DebugNode`](../modules/maxon_generated/mxutils/mxutils.DebugNode.md#module-mxutils.DebugNode). Each kind of data has up to three functions: `Get` returns the tree, `Print` prints it, and `Diff` returns the differences of two inputs as a unified diff.

| Data | Get | Print | Diff |
|---|---|---|---|
| [`c4d.BaseContainer`](../modules/c4d/BaseContainer/index.md#c4d.BaseContainer) | [`GetContainer()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetContainer) | [`PrintContainer()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.PrintContainer) | [`DiffContainer()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.DiffContainer) |
| Parameters of a [`c4d.BaseList2D`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) | [`GetParameters()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetParameters) | [`PrintParameters()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.PrintParameters) | [`DiffParameters()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.DiffParameters) |
| Bit and NBit flags of a node | [`GetFlags()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetFlags) | [`PrintFlags()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.PrintFlags) | [`DiffFlags()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.DiffFlags) |
| Parameters and flags combined | [`GetBaseList()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetBaseList) |  | [`DiffBaseList()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.DiffBaseList) |
| Scene graph below a node | [`GetGraph()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetGraph) | [`PrintGraph()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.PrintGraph) | [`DiffGraph()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.DiffGraph) |

The functions do not modify the scene, but they walk descriptions, containers, and graphs, which is expensive. Do not call them unconditionally in code that runs often.

### Debug Trees <a id="debug-trees"></a>

A [`DebugNode`](../modules/maxon_generated/mxutils/mxutils.DebugNode.md#module-mxutils.DebugNode) has a label, a parent, and children. [`DebugNode.ToString()`](../modules/maxon_generated/mxutils/mxutils.DebugNode.md#mxutils.DebugNode.ToString) renders the tree below it as text. You can also build your own reports with [`DebugNode.Add()`](../modules/maxon_generated/mxutils/mxutils.DebugNode.md#mxutils.DebugNode.Add), or from an indented string with [`DebugNode.FromString()`](../modules/maxon_generated/mxutils/mxutils.DebugNode.md#mxutils.DebugNode.FromString):

```python
report: mxutils.DebugNode = mxutils.DebugNode("Report")
objects: mxutils.DebugNode = mxutils.DebugNode("Objects")
report.Add(objects)
objects.Add(mxutils.DebugNode("Cube"))
objects.Add(mxutils.DebugNode("Sphere"))
report.Add(mxutils.DebugNode("Tags"))
print(report.ToString())

# Report
# ├── Objects
# │   ├── Cube
# │   └── Sphere
# └── Tags
```

For arbitrary tree-like data, [`DebugPrint.GetTreeString()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetTreeString) prints any node type that either stores its children in an attribute, or that can be navigated with a `GetDown` and `GetNext` function, and accepts a callback to customize the label of each node.

### Containers <a id="containers"></a>

[`GetContainer()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetContainer) prints the entries of a container with their data type. Container IDs are integers, so the function can resolve them to symbols when you give it a regular expression as a hint, e.g., `'^BFM_'` to only consider symbols that start with `BFM_`. When there is no symbol or more than one for an ID, the number is printed instead:

```python
bc: c4d.BaseContainer = c4d.BaseContainer()
bc[1000] = "Hello"
bc[1001] = 42
sub: c4d.BaseContainer = c4d.BaseContainer()
sub[1000] = "Sub"
bc[1002] = sub

mxutils.DebugPrint.PrintContainer(bc)

# Root (None , id = -1):
# ├── 1000 (DTYPE_STRING): Hello
# ├── 1001 (DTYPE_LONG): 42
# └── 1002 (DTYPE_SUBCONTAINER , id = -1):
#     └── 1000 (DTYPE_STRING): Sub
```

> **Warning:** Resolving a container ID to a symbol is ambiguous, as the same number is used by many symbols in different contexts. A resolved symbol is correct numerically, but can imply a different meaning than the entry has. Only use hints when you know which family of symbols to expect.

### Parameters <a id="parameters"></a>

For the parameters of a node, [`GetParameters()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetParameters) is the better choice, as it reads the description of the node and with that always shows the correct symbols, names, and data types. The output is large, so the function can be narrowed down with `whiteList` and `blackList`, which take parameter or group IDs, and with the `show...` arguments:

```python
cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
cube[c4d.PRIM_CUBE_LEN] = c4d.Vector(300, 200, 100)
cube[c4d.PRIM_CUBE_SUBX] = 4

# Only show the parameters of the Object Properties group.
mxutils.DebugPrint.PrintParameters(cube, whiteList=(c4d.ID_OBJECTPROPERTIES,), showDescId=False)

# 'Cube' (Ocube)' object at 0x00000213AC962240 with the parameters:
# └── 'Object Properties (ID_OBJECTPROPERTIES)' - type: DTYPE_GROUP
#     ├── 'Size (PRIM_CUBE_LEN)' - type: DTYPE_VECTOR, value: Vector(300, 200, 100)
#     ├── 'Segments X (PRIM_CUBE_SUBX)' - type: DTYPE_LONG, value: 4
#     ├── 'Segments Y (PRIM_CUBE_SUBY)' - type: DTYPE_LONG, value: 1
#     ├── 'Segments Z (PRIM_CUBE_SUBZ)' - type: DTYPE_LONG, value: 1
#     ├── 'Separate Surfaces (PRIM_CUBE_SEP)' - type: DTYPE_BOOL, value: 0
#     ├── 'Fillet (PRIM_CUBE_DOFILLET)' - type: DTYPE_BOOL, value: 0
#     ├── 'Fillet Radius (PRIM_CUBE_FRAD)' - type: DTYPE_REAL, value: 3.0
#     └── 'Fillet Subdivision (PRIM_CUBE_SUBF)' - type: DTYPE_LONG, value: 3
```

By default, groups and separators without a name are hidden, as they do not matter for data access. Pass `hideLayoutElements=False` when you need the true parameter tree. Setting `showDefaultValues=False` only shows parameters which differ from their description default, parameters without such a default are always shown.

### Flags <a id="flags"></a>

[`GetFlags()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetFlags) prints the state of the `BIT_` and `NBIT_` flags of a node. `hint` is a regular expression which filters the flag symbols, and `showSetOnly` hides all flags which are not set. Use this to find out which flags a node has, e.g., after a user action in the Object Manager:

```python
mxutils.DebugPrint.PrintFlags(cube, showBit=False, showSetOnly=True)

# Cube (BaseObject)
# ├── NBIT_OHIDE: 1
# └── NBIT_OM1_FOLD: 1
```

[`GetBaseList()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetBaseList) returns the parameters and the flags of a node in one tree with the branches `Parameters` and `Flags`.

### Scene Graphs <a id="scene-graphs"></a>

[`GetGraph()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetGraph) prints the hierarchy, the caches, and the branches below a node, e.g., a document, an object, or a material. It is the quickest way to see what a generator has built, and which tags a cache holds. See [Scene Structure](manual_scene_structure.md) for an explanation of the output.

### Comparing Two Nodes <a id="comparing-two-nodes"></a>

A frequent question while debugging is why a node *A* does not behave like a node *B*. Instead of searching for the difference by eye, the `Diff` functions compare the output of the matching `Get` function and return only the differences as a unified diff. They accept the same arguments as their `Get` counterpart. The following examples compare two cubes `a` and `b`, where the Size and Segments X parameters of `a` have been changed, and the Object Manager fold and hide flags of `b` have been set:

```python
print(mxutils.DebugPrint.DiffParameters(
    a, b, whiteList=(c4d.ID_OBJECTPROPERTIES,), showDescId=False, showType=False))

# --- first
# +++ second
# @@ -1,7 +1,7 @@
# -'Cube' (Ocube)' object at 0x0000025AD4D9C3C0 with the parameters:
# +'Cube.1' (Ocube)' object at 0x0000025AD4D9B040 with the parameters:
#  └── 'Object Properties (ID_OBJECTPROPERTIES)'
# -    ├── 'Size (PRIM_CUBE_LEN)' - value: Vector(300, 200, 100)
# -    ├── 'Segments X (PRIM_CUBE_SUBX)' - value: 4
# +    ├── 'Size (PRIM_CUBE_LEN)' - value: Vector(200, 200, 200)
# +    ├── 'Segments X (PRIM_CUBE_SUBX)' - value: 1
#      ├── 'Segments Y (PRIM_CUBE_SUBY)' - value: 1
#      ├── 'Segments Z (PRIM_CUBE_SUBZ)' - value: 1
#      ├── 'Separate Surfaces (PRIM_CUBE_SEP)' - value: 0

print(mxutils.DebugPrint.DiffFlags(a, b, showBit=False, hint="OM|OHIDE"))

# --- first
# +++ second
# @@ -1,7 +1,7 @@
# -Cube (BaseObject)
# +Cube.1 (BaseObject)
#  ├── NBIT_IS_FROM_HOST: 0
# -├── NBIT_OHIDE: 0
# -├── NBIT_OM1_FOLD: 0
# +├── NBIT_OHIDE: 1
# +├── NBIT_OM1_FOLD: 1
#  ├── NBIT_OM2_FOLD: 0
#  ├── NBIT_OM3_FOLD: 0
#  ├── NBIT_OM4_FOLD: 0
```

The first line of a diff always differs, as it contains the name of the node. [`DiffGraph()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.DiffGraph) compares the scene graphs of two nodes, and [`DiffBaseList()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.DiffBaseList) parameters and flags in one go. [`DiffContainer()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.DiffContainer) does the same for containers, e.g., to find out what a user action has changed in the data container of a node. See [mxutils_debugprint](../examples/misc/mxutils_debugprint.py.md) for all functions in action.

## Checking Assumptions <a id="checking-assumptions"></a>

Many errors surface long after they have been caused. A failed allocation returns `None`, and the script then fails ten lines later with a message that points at the wrong place. [`mxutils.CheckType()`](../modules/mxutils_api.md#mxutils.CheckType) and [`mxutils.CheckIterable()`](../modules/mxutils_api.md#mxutils.CheckIterable) move the failure to the cause. They return the value when the check passes, so they can be used inline, and they name the checked expression in the error message:

```python
# Fails here and not in the next line, when the allocation fails.
cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))

data: list[str | int] = ["1", 2]
mxutils.CheckIterable(data, str)
# TypeError: Expected iterable 'data' to be composed of type <class 'str'>. Found item of type: <class 'int'>
```

The symbol of the checked expression can only be discovered in saved files, in the Script Manager and in the console you will see a generic message. Checking every element of a large iterable is expensive, check function arguments and results, not data in loops. See [mxutils_checktype](../examples/misc/mxutils_checktype.py.md) for more cases.

## Tracing and Timing <a id="tracing-and-timing"></a>

The decorator [`mxutils.REPORT()`](../modules/mxutils_api.md#mxutils.REPORT) prints the name of a function when it is called, with a rule underneath, and an empty line when it returns. For methods it also prints the memory address of the object. This helps to follow call chains without setting breakpoints:

```python
@mxutils.REPORT()
def Foo(msg: str) -> None:
    print(f"{msg = }")

Foo("Hello World!")

# Running 'Foo':
# ----------------------------------------------------------------------------------------------------
# msg = 'Hello World!'
```

[`mxutils.TIMEIT()`](../modules/mxutils_api.md#mxutils.TIMEIT) measures how long a call takes and prints it. It takes a flag as its first argument, and when the flag is `False` the function is returned unchanged, so decorators can stay in your code, controlled by an `IS_DEBUG` constant. The decorator can also print the arguments and the result, and profile the call with `cProfile` instead of timing it:

```python
IS_DEBUG: bool = True

@mxutils.TIMEIT(IS_DEBUG, showArgs=True, showResult=True)
def Factorial(n: int) -> int:
    return 1 if n == 0 else n * Factorial(n - 1)
```

> **Note:** Profiling has a high impact on the runtime of a function, timing a low one. Neither should ship in released code. For recursive functions, `inCallProtection=True` only reports the outermost call, but this protection is not thread-safe.

[`mxutils.GetMemoryAddress()`](../modules/mxutils_api.md#mxutils.GetMemoryAddress) returns the address of an object in the format Python uses in its default `repr`. It is useful for `__str__` methods of your own classes, and to find out if two callbacks operate on the same instance. See [mxutils_decorators](../examples/misc/mxutils_decorators.py.md) for more decorator examples.

## Test Scenes <a id="test-scenes"></a>

Bugs are easiest to fix when they can be reproduced in a small scene. [`mxutils.SceneFaker`](../modules/maxon_generated/mxutils/mxutils.SceneFaker.md#module-mxutils.SceneFaker), available as the global instance `mxutils.g_scene_faker`, creates objects, materials, tags, layers, render data, and animation tracks for development and testing purposes. [`SceneFaker.AddHierarchyFromString()`](../modules/maxon_generated/mxutils/mxutils.SceneFaker.md#mxutils.SceneFaker.AddHierarchyFromString) builds an object hierarchy from an indented string, where `::` followed by an object type ID selects the type, and objects without one are Null objects:

```python
objects: list[c4d.BaseObject] = mxutils.g_scene_faker.AddHierarchyFromString(doc, f"""
    A
        B::{c4d.Ocube}
        C::{c4d.Osphere}
        D
            E
    """)

mxutils.DebugPrint.PrintGraph(objects[0]) # Check that the scene is what the test needs.
```

The `AddRandom...` methods add content to an existing scene, and `RandomizeScene` fills a document with random content. Pass your own seeded [`mxutils.Random`](../modules/maxon_generated/mxutils/mxutils.Random.md#module-mxutils.Random) to a new [`SceneFaker`](../modules/maxon_generated/mxutils/mxutils.SceneFaker.md#module-mxutils.SceneFaker) instance to get the same content on every run. Because the faker builds caches, it must run on the main thread, e.g., in a Script Manager script. See [traversal](../examples/scene/traversal.py.md) for a scene that has been built this way.

## Threading Violations <a id="threading-violations"></a><a id="debugging-threading"></a>

Ignoring the [threading restrictions](manual_scene_execution.md#threading-information) is the most common reason for crashes of Python plugins and scripting elements. It is also the hardest to debug, because the result is undefined behavior: Cinema 4D does not raise an error at the faulty line, it is left with a dangling pointer which is dereferenced later, in another place, or on another thread.

Typical signs of a threading violation are:

- Cinema 4D terminates without a Python traceback, or stops responding.
- The crash only happens sometimes, or in specific situations, e.g., during playback, while rendering, while the Object Manager is open and showing the affected nodes, or after the scene has been edited for a while.
- The code works when it is executed from the Script Manager, but not as a plugin or scripting element, because a script always runs on the main thread, while a callback does not.
- The crash location, if there is one, does not match the code that caused it.

### Find Out Where the Code Runs <a id="find-out-where-the-code-runs"></a>

Start with the facts. Log the context of the suspicious callbacks and everything they call. [`c4d.threading.GeIsMainThreadAndNoDrawThread()`](../modules/c4d.threading/index.md#c4d.threading.GeIsMainThreadAndNoDrawThread) is `True` when the code runs on the main thread and that thread is not currently executing drawing code, while [`c4d.threading.GeIsMainThread()`](../modules/c4d.threading/index.md#c4d.threading.GeIsMainThread) is also `True` during drawing:

```python
import functools

import c4d

def GetContext() -> str:
    """Returns a description of the thread context the caller is running in."""
    if c4d.threading.GeIsMainThreadAndNoDrawThread():
        return "main thread"
    if c4d.threading.GeIsMainThread():
        return "main thread (drawing)"
    return "threaded context"

def LogContext(func):
    """Prints the context a function is called in."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__qualname__}: {GetContext()}")
        return func(*args, **kwargs)
    return wrapper
```

Decorate the callbacks and the helper functions which they call. The violation is often not in the callback itself, but in a helper function that was written for a script and later reused in a callback. Callbacks are called often, so remove the logging once you know the answer.

### Turn Violations into Errors <a id="turn-violations-into-errors"></a>

Once you know which operations are not allowed in the context of a callback, replace the silent undefined behavior with a Python exception while you debug. A guard like the following raises an error with a traceback at the offending line, instead of crashing Cinema 4D later. [`mxutils.SceneFaker`](../modules/maxon_generated/mxutils/mxutils.SceneFaker.md#module-mxutils.SceneFaker) uses the same technique to protect its cache building:

```python
IS_DEBUG: bool = True

def AssertMainThread() -> None:
    """Raises an error when called from a threaded context, instead of risking a crash."""
    if IS_DEBUG and not c4d.threading.GeIsMainThreadAndNoDrawThread():
        raise RuntimeError("Main thread only code has been called from a threaded context.")

class MyGenerator(c4d.plugins.ObjectData):

    def GetVirtualObjects(self, op: c4d.BaseObject, hh: object) -> c4d.BaseObject | None:
        doc: c4d.documents.BaseDocument = op.GetDocument()
        AssertMainThread() # Not allowed here, this will raise an error and not crash.
        doc.InsertObject(c4d.BaseObject(c4d.Onull))
        return None
```

Place the guard in front of each operation which the [restrictions table](manual_scene_execution.md#threading-information) marks as forbidden in a threaded context: inserting, moving, or removing nodes of a document, modifying the parameters or matrices of the own node, creating or modifying materials, creating undo steps, and anything that touches the user interface. Do not leave a guard as the fix. It only tells you where the code is wrong, [the fix](#debugging-threading-fix) is to move the work to the main thread.

### Capture the Crash <a id="capture-the-crash"></a>

When there is no traceback, Python’s `faulthandler` module can still write one. When enabled, it dumps the Python stack of the crashing thread, and optionally of all other threads, if the process receives a fatal error such as an access violation. The first entry of the stack is the Python line that made the call into the Cinema API which crashed. As the violation can have happened earlier, this is a starting point and not always the cause, but the log tells you which callback and which thread were involved.

Enable it at the start of your plugin module, and keep the file object alive for as long as the handler is enabled:

```python
import faulthandler
import os

# The file object must stay open as long as faulthandler is enabled.
g_crashLog = open(os.path.join(os.path.dirname(__file__), "crash.log"), "w")
faulthandler.enable(file=g_crashLog, all_threads=True)
```

After a crash, the file contains an entry like the following:

```text
Fatal Python error: Segmentation fault

Current thread 0x0001c38c (most recent call first):
  File "C:\plugins\py_obj_example\py_obj_example.pyp", line 52 in BuildCache
  File "C:\plugins\py_obj_example\py_obj_example.pyp", line 38 in GetVirtualObjects
```

The same module also helps with hangs, which are the other symptom of threading problems, e.g., when a lock is held while calling into the Cinema API. `faulthandler.dump_traceback_later()` writes the stacks of all threads to the log when your code has not finished after a given number of seconds:

```python
faulthandler.dump_traceback_later(10, repeat=False, file=g_crashLog)
# ... run the code that hangs ...
faulthandler.cancel_dump_traceback_later()
```

> **Note:** This has been verified for the standalone interpreter c4dpy, where a deliberate fault produced the entry shown above. In the Cinema 4D application, its own crash handling is involved. Test the setup once with a deliberate crash in a scratch session, e.g., with `faulthandler._sigsegv()`, which terminates Cinema 4D immediately, before you rely on it.

### Reduce and Reproduce <a id="reduce-and-reproduce"></a>

A crash that happens “sometimes” is only fixed when it can be provoked. Because threading violations need another thread that uses the same data at the same time, make Cinema 4D busy while the code under test is running: play the timeline, start a render in the Picture Viewer, open the Object Manager and the Attribute Manager with the affected nodes, and change parameters while a slider is being dragged. Combine this with a small test scene built with [`mxutils.SceneFaker`](../modules/maxon_generated/mxutils/mxutils.SceneFaker.md#module-mxutils.SceneFaker), and remove parts of the callback until the crash disappears. The last part that was removed contains the violation. When the fix is done, run the same procedure again, as a violation that does not crash proves nothing.

### Fix the Violation <a id="fix-the-violation"></a><a id="debugging-threading-fix"></a>

A callback cannot modify the document on its own. Move the work to the main thread, either with a core message and a [`c4d.plugins.MessageData`](../modules/c4d.plugins/BaseData/MessageData/index.md#c4d.plugins.MessageData) plugin, or in the `Message` method of a node, as described in the section *Deferring Workloads* of [Scene Execution](manual_scene_execution.md). Also do not use Python’s `threading` module to access Cinema 4D data, see the section *Python and Threads* in the same manual.

### See Also <a id="see-also"></a>

- [Scene Execution](manual_scene_execution.md): Explains how Cinema 4D updates a scene, and where Python code runs in that process.
- [Scene Structure](manual_scene_structure.md): Explains how a Cinema 4D scene is organized with hierarchies and branches, and how to traverse it.
- [Working with the SDK](manual_working_with_sdk.md): Set up Visual Studio Code to work with the Cinema 4D Python SDK.
- [Example mxutils_checktype.py](../examples/misc/mxutils_checktype.py.md): Demonstrates type and iterable validation with mxutils.
- [Example mxutils_debugprint.py](../examples/misc/mxutils_debugprint.py.md): Demonstrates mxutils helpers for diagnosing Cinema 4D scene data.
- [Example mxutils_decorators.py](../examples/misc/mxutils_decorators.py.md): Demonstrates mxutils helpers for diagnosing Cinema 4D scene data.
