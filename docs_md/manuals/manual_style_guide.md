<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_style_guide.html -->

# Style Guide <a id="style-guide"></a>

Explains the code style and conventions used in this SDK.

The Cinema 4D Python SDK follows the [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/) in its code examples and documentation, and adopts the naming and execution conventions of the Cinema API. This guide documents the most important conventions and deviations from PEP 8 that might not be obvious to users, and the practices required to run safely alongside other scripts and plugins. SDK contributors should also follow `py_sdk/AGENTS.md` when adding examples.

> **Warning:** Not all older SDK examples have been converted to the style described in this guide yet. This guide is the current norm for all new and updated examples; when an older example differs from it, follow this guide.

## Conventions <a id="conventions"></a>

### Line Length and Indentation <a id="line-length-and-indentation"></a>

The Cinema 4D Python SDK follows the PEP 8 guidelines but relaxes their line length limit from 79 characters to 100 characters, as this is more practical for modern documentation needs. SDK examples use four spaces per indentation level and no tabs. For users, we recommend an even more relaxed limit of 120 characters, as this is more practical when writing code on modern wide screens where printing the code on paper is not a concern (one of the original reasons for the 79 characters limit). We do however recommend adhering to a finite line length, as code interoperability is still important. Just because your code looks good on your screen with lines of 200 characters and more, it does not mean it will look good on your colleague’s smaller mobile device screen or when published on GitHub. A fixed length ensures that your code looks good everywhere. Break expressions at a natural boundary rather than shrinking names or hiding complex logic on one line.

### Naming <a id="naming"></a>

Use the Cinema API’s published names as written: `c4d.BaseObject`, `c4d.EventAdd()`, and `GetName()`. In SDK examples, classes, functions, and methods start with a capital letter, while variables and attributes start with a lowercase letter and use camelCase. Constants use uppercase letters and underscores. The conventional `main()` entry point is an exception. When you change an older example only slightly, you may keep its existing naming style; use the conventions of this guide when you revise the whole example.

```python
import c4d

def RenameSelectedObject(activeObject: c4d.BaseObject, newName: str) -> None:
    """Renames #activeObject to #newName.
    """
    activeObject.SetName(newName)
```

### Type Hinting <a id="type-hinting"></a>

Type hinting is a feature of Python that allows authors to specify the expected types of variables, function parameters, and return values. The Cinema 4D Python SDK uses the most recent type hinting features available in the Python version shipped with the respective Cinema 4D release (i.e., [PEP 484](https://peps.python.org/pep-0484/), [PEP 585](https://peps.python.org/pep-0585/), and [PEP 604](https://peps.python.org/pep-0604/)). We use the built-in generic and union syntax rather than the older `typing.List` and `typing.Optional` spellings.

Type hinting is entirely optional, and code without type hints is functionally equivalent to the same code with type hints. The major purpose of type hinting is to convey the intent of the code author to users and tools (e.g., linters, IDEs, type checkers). It can help catch certain types of errors early, improve code readability, and enhance the development experience with better autocompletion and type checking in editors. E.g., the following two code blocks are functionally equivalent, but the second code block uses type hints to specify the expected types of variables and function parameters:

```python
# Example without type hints
import myLib

def Uppercase(item):
    ...

data = myLib.GetData()
print(Uppercase(data))
```

```python
# Example with type hints
import myLib

def Uppercase(item: str | list[str]) -> str | list[str]:
    ...

data: list[str] = myLib.GetData()
print(Uppercase(data))
```

With its type hints, the second code block hints at the fact that the function `Uppercase` can take either a single string or a list of strings as input, and will return either a single uppercase string or a list of uppercase strings. The variable `data` is also explicitly declared to be a list of strings. Note that type hints are by default not checked at runtime, which for once means that they do not impact performance or behavior of the code but also that they can be incorrect or misleading. `Uppercase` could for example also hint at the fact that it takes an integer as input, and the code would still run without errors, even though actually passing an integer would result in a runtime error. Annotating a result as `c4d.BaseObject` can therefore not make an API call succeed. Check optional results explicitly or use [`mxutils.CheckType()`](../modules/mxutils_api.md#mxutils.CheckType) where a failed call should stop the script.

But typing information can help users understand how to use the function correctly, and can also help tools catch potential type-related errors. The following table summarizes the most important syntax elements used in type hinting in the Cinema 4D Python SDK. See the [Python Type Annotations](https://typing.python.org/en/latest/spec/annotations.html) documentation for more information about type hinting syntax and conventions.

| Syntax | Description |
|---|---|
| `type` | Class names are used to denote types. E.g., `str`, `int`, `float`, `bool`, `bytes`, `list`, `dict`, `tuple` are all primitive classes in Python and commonly used in type hinting. However, user-defined classes such as `MyClass` and Cinema API classes such as `c4d.BaseObject` are also valid types for type hinting.<br>`import c4d`<br>`class Person:`<br>`def __init__(self, name: str, age: int) -> None:`<br>`self.name = name`<br>`self.age = age`<br>`# Here we declare that #name is a string, #age is an integer, #item is of type Person, and`<br>`# #cube is a Cinema 4D object.`<br>`name: str = "Bob"`<br>`age: int = 30`<br>`item: Person = Person(name, age)`<br>`cube: c4d.BaseObject = c4d.BaseObject(c4d.Ocube)` |
| `:` | The colon is used to denote the start of a type hint for variables and function arguments. In rare cases, type hints can also be used without a variable definition, e.g., `item: str` declares that the variable `item` is of type `str` but does not define its value. This is for example often used in loops, as loop variables cannot be type hinted in the loop definition itself.<br>`# Here we declare that #data is a list of strings and define its value at the same time.`<br>`data: list[str] = ["Alice", "Bob", "Charlie"]`<br>`# Here we just declare that #name will be a string, but do not yet define its value.`<br>`name: str`<br>`# This loop will then actually define the variable. In this case it is a bit pointless as`<br>`# both a human and linter would know by the declaration of #data of what type #name is.`<br>`for name in data:`<br>`print(f"Hello, {name}!")`<br>`# But in cases where we loop over function return values of some opaquely typed function,`<br>`# this can be useful.`<br>`obj: c4d.BaseObject`<br>`for obj in doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_NONE):`<br>`print(f"Hello, {obj.GetName()}!")` |
| `->` | The arrow is used to denote the return type of a function. For functions that do not return a value, i.e., where the return type is `None`, the return type annotation can be omitted. E.g., `def Foo():` and `def Foo() -> None:` are equivalent.<br>`# Here we declare that the function #Greet takes a string as argument and returns a string.`<br>`def Greet(name: str) -> str:`<br>`return f"Hello, {name}!"`<br>`message: str = Greet("Alice")` |
| `\|` | The pipe symbol is used to denote a union of types, that a variable or argument can be of multiple types. We do not use the older `Union` and `Optional` syntax from [PEP 484](https://peps.python.org/pep-0484/) as it is less readable. A union with `None` denotes that a value may be absent, e.g., `c4d.BaseObject \| None`; check for `None` before using it.<br>`# Data can be either a single string or a list of strings.`<br>`data: str \| list[str] = "Hello"`<br>`# This function can take either a single string or a list of strings as its argument and`<br>`# will return either a single uppercase string or a list of uppercase strings.`<br>`def Uppercase(item: str \| list[str]) -> str \| list[str]:`<br>`if isinstance(item, str):`<br>`return item.upper()`<br>`elif isinstance(item, list):`<br>`return [s.upper() for s in item]`<br>`else:`<br>`raise ValueError("Invalid input type")`<br>`# An object that may be absent, as the result of a lookup.`<br>`found: c4d.BaseObject \| None = doc.SearchObject("Cube")` |
| `[]` | Square brackets are used to denote collection types, i.e., a type that contains multiple elements of another type.<br>`# #names is a list of strings.`<br>`names: list[str] = ["Alice", "Bob", "Charlie"]`<br>`# #employees is a list of strings or Person objects.`<br>`employees: list[str \| Person] = ["Alice", Person("Bob", 30)]`<br>`# #ages is a dictionary that maps strings to integers.`<br>`ages: dict[str, int] = {"Alice": 30, "Bob": 25, "Charlie": 35}`<br>`# #person is a tuple of exactly two elements, a string and an integer.`<br>`person: tuple[str, int] = ("Alice", 30)`<br>`# Tuples can also be of variable length: #data is a tuple of the pattern`<br>`# (float, int, float, int, ...), of arbitrary length.`<br>`data: tuple[float \| int, ...] = (1.0, 2, 3.5, 4, 5.0)`<br>`# #objects is a list of Cinema 4D objects.`<br>`objects: list[c4d.BaseObject] = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_NONE)` |
| `Any` | `Any` denotes that a variable or argument can be of any type. It is basically the type hinting way of not type hinting something. It is often used in cases where the type of a variable is not known or can vary widely.<br>`import typing`<br>`# Here we declare that #value can be of any type. typing.Any should be used sparingly, as it`<br>`# defeats the purpose of type hinting. Usually there is a more specific annotation that can be used.`<br>`def PrintValue(value: typing.Any) -> None:`<br>`print(value)` |
| `Iterator` | `Iterator` denotes values and return types that yield values. We do not use the more complex `Generator` type hinting syntax.<br>`import typing`<br>`# Here we declare that #CountUpTo is an iterator that yields integers. #Iterator effectively hints`<br>`# at the fact that a function not only returns but also yields values.`<br>`def CountUpTo(n: int) -> typing.Iterator[int]:`<br>`count: int = 1`<br>`while count <= n:`<br>`yield count`<br>`count += 1`<br>`for number in CountUpTo(5):`<br>`print(number)` |
| `Callable` | `Callable` denotes a variable or argument that is a function and what its signature is. The general logic is that the outer brackets are the full signature, where the first element - the inner brackets - is the argument type list, and the second element is the return type.<br>`import typing`<br>`# Here we declare that #Compute is a function which takes a function #f as its first argument,`<br>`# and two integers as its second and third argument. #f must have the signature [int, int], int,`<br>`# i.e., must take two integers as arguments and return an integer.`<br>`def Compute(f: typing.Callable[[int, int], int], a: int, b: int) -> int:`<br>`return f(a, b)`<br>`# Here we define a function #Add which matches the signature of #f required by #Compute.`<br>`def Add(x: int, y: int) -> int:`<br>`return x + y`<br>`# And here we call #Compute.`<br>`result: int = Compute(Add, 5, 10)` |

Script Manager supplies `doc` as a `c4d.documents.BaseDocument` and `op` as `c4d.BaseObject | None`. Declare these hints only when you use the variables; neither name is supplied automatically in plugin modules. The following Script Manager example handles an absent selection before accessing the object:

```python
import c4d

doc: c4d.documents.BaseDocument # The active document.
op: c4d.BaseObject | None # The active object, can be None.

def main() -> None:
    """Renames the selected object.
    """
    if op is None:
        return

    doc.AddUndo(c4d.UNDOTYPE_CHANGE, op)
    op.SetName("Selected Object")
    c4d.EventAdd()

if __name__ == "__main__":
    main()
```

See [API Overview](manual_api_overview.md) for the three API components and [Quickstart](manual_quickstart.md) for a first runnable example.

### Comprehensions <a id="comprehensions"></a>

List comprehensions are a short-hand syntax for assembling collections without a traditionally written loop. They can make code more readable and shorter but can also be confusing to beginners, especially when nested or combined with other complex expressions. The Cinema 4D Python SDK uses list and other comprehensions quite frequently, but strives for limiting their usage to simple cases. The following code block with a loop:

```python
# Build a list of powers of two from 0 to 9.
result: list[int] = []
for n in range(10):
    result.append(2 ** n)
```

Can be rewritten with a list comprehension and with that reduces the code from 4 lines to a single line:

```python
# Build a list of powers of two from 0 to 9.
result: list[int] = [2 ** n for n in range(10)]

# Comprehensions also work with other collection types, e.g., dictionaries. Here we build a dictionary
# that maps the numbers from 0 to 9 to their squares.
squares: dict[int, int] = {n: n ** 2 for n in range(10)}
```

Comprehensions can be used for lists, sets, tuples, dictionaries. See the [Python Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) documentation for more information about the subject.

A comprehension is useful for a short transformation, such as collecting the names of the selected objects. A loop is clearer when each item needs several API calls or an error check, or when the data is not a plain collection, such as when walking an object hierarchy. Cinema 4D hierarchies are traversed through the first child and the next sibling:

```python
# Gather the names of the selected objects with a comprehension.
selected: list[c4d.BaseObject] = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_NONE)
selectedNames: list[str] = [obj.GetName() for obj in selected]

# Gather the names of the children of #op with a loop. Use a loop like this one if you later need to
# inspect or modify each child.
childNames: list[str] = []
child: c4d.BaseObject | None = op.GetDown()
while child is not None:
    childNames.append(child.GetName())
    child = child.GetNext()
```

### Example Structure <a id="example-structure"></a>

Start a runnable SDK example with a short module docstring describing its purpose and how to run it. Put its work in `main()` and invoke it in an `if __name__ == "__main__":` block. Use concise Google-style docstrings for functions, ending the summary with a line break, and refer to arguments with a leading `#`, e.g., `#newName`. Include the author, license, copyright, and version fields specified in `py_sdk/AGENTS.md` for new SDK examples. Comments should explain decisions rather than repeat the next API call, and are clustered rather than placed above every line.

## Best Practices <a id="best-practices"></a>

Cinema 4D is a shared Python environment, meaning that all scripts and plugins running in Cinema 4D share the same Python interpreter and the same global state. This has some implications for writing code that collides with what one might be used to from volatile Python environments, such as scripts running in a standard CPython VM.

### Shared Modules State <a id="shared-modules-state"></a>

Avoid altering the state of shared builtin module objects, such as `sys`, `math`, or `random`. In a vanilla Python environment, you might overwrite module attributes or call functions that change a module’s behavior. And there this is fine, because such a Python VM only runs your code. But in a shared environment, this will not only affect your code, but also all other scripts and plugins running in Cinema 4D.

```python
import sys
import math
import random

# We clear all modules. This will not directly break all plugins, as they still hold a local reference to their
# module objects. But this is still a terrible idea, as any code running after this will create new module objects
# when importing modules, causing these modules to exist twice in memory.
sys.modules.clear()

# We overwrite a module attribute and call a function that changes the module's behavior. This will affect
# all code running after this, not only our own code.
math.pi = 3
random.seed(42)

# A side effect of this is also, that when you accidentally made this common mistake, random.seed is a function
# and not an attribute, you have now permanently bricked random.seed until Cinema 4D is restarted, as just running
# the corrected code again, will not change the fact that you have before overwritten random.seed function.
random.seed = 42
```

### Importing Libraries <a id="importing-libraries"></a>

Another cause for issues can be colliding dependencies in a shared environment. In a standard CPython VM, the path of the executed script is automatically added to the module search paths (i.e., `sys.path`) when the script is executed. This is not the case for a shared Python VM such as Cinema 4D, as adding all found scripts and plugin folders to the module search paths would lead to unpredictable importing behavior. This means that you must expose the script directory yourself if you want to import modules from the same directory as your script. Use [`mxutils.LocalImportPath`](../modules/maxon_generated/mxutils/mxutils.LocalImportPath.md#module-mxutils.LocalImportPath) for this, which exposes a directory only for the duration of a `with` block. See [Python Environment](manual_python_environment.md) and [External Libraries](manual_external_libraries.md) for more things to consider due to the shared nature of the Cinema 4D Python VM.

```python
import os
import sys

# This is a really bad idea, as it will not only expose your search paths to all other scripts and plugins
# running in Cinema 4D, but can also cause module name collisions.
libs: str = os.path.join(os.path.dirname(__file__), "libs")
if libs not in sys.path:
    sys.path.insert(0, libs)

# The local math library collides with the builtin module of the same name.
from libs import math
```

```python
import mxutils

# Do this instead: the directory of this file is only part of the search paths within the block.
with mxutils.LocalImportPath(__file__):
    import myLocalModule
```

### StdIn/StdOut/StdErr <a id="stdin-stdout-stderr"></a>

Avoid overwriting `sys.stdin`, `sys.stdout`, or `sys.stderr`. The Cinema 4D Python VM uses a custom stream handler to redirect standard output and error streams to the Cinema 4D Python console. This means that you cannot easily overwrite the stream handlers, as this will break the output redirection to the console.

```python
import sys

# This will break the output redirection to the Cinema 4D console. There is no way to reestablish the
# redirection with a custom stream handler.
sys.stdout = open("output.txt", "w")
print("This will not appear in the Cinema 4D console.")
```

### Python Processes <a id="python-processes"></a>

Do not attempt to spawn new Python processes (e.g., via `multiprocessing` or `subprocess`), and do not use Python’s `threading` to operate on Cinema 4D data. The Cinema 4D Python VM is the Cinema 4D executable itself, and neither does it understand Python-specific command line arguments, nor will it be able to communicate with other running Cinema 4D instances. Use `c4d.threading` for threading and the standalone interpreter, see [Standalone Interpreter](manual_standalone_interpreter.md), when you need a separate Python process.

```python
import multiprocessing
import runpy
import subprocess
import sys

# This will not work as expected, as sys.executable points to the Cinema 4D executable.
subprocess.run([sys.executable, "myScript.py"], check=True)

# This is a valid alternative to subprocess, but it will run in the same Python process and therefore
# will not have the performance and isolation benefits of a separate process.
runpy.run_path("myScript.py", run_name="__main__")

# multiprocessing is not supported at all for the same reason, as multiprocessing just spawns new
# Python processes and then handles their inter-process communication. There is no alternative or
# workaround for this, and trying it can crash Cinema 4D.

def Worker():
    print("Worker process")

pool: list[multiprocessing.Process] = [
    multiprocessing.Process(target=Worker) for _ in range(4)
]
```

### Working Directory <a id="working-directory"></a>

The working directory of the Cinema 4D Python VM is not the directory of your script. This differs from a common CPython instance, where scripts are often run from their own directory. This becomes especially relevant when using relative paths in your scripts. It is also not recommended to change the current working directory of the Cinema 4D Python VM, as this violates the rule of not modifying the state of shared builtin module objects. Other plugins and scripts might rely on the working directory not changing. When working with files, always use absolute paths or paths relative to the script directory. The following code block shows a bad and a good example:

```python
import os

# This will try to open the file "myFile.txt" relative to the working directory of Cinema 4D, not in
# the directory of this script.
with open("myFile.txt", "r") as file:
    data = file.read()

# Do this instead.
scriptDirectory: str = os.path.dirname(__file__)
with open(os.path.join(scriptDirectory, "myFile.txt"), "r") as file:
    data = file.read()
```

### Document Changes <a id="document-changes"></a>

Script Manager provides `doc` and `op`; plugins and scene scripting elements do not receive those same variables automatically. A Script Manager command that edits the document should register supported undo steps and call `c4d.EventAdd()` once after its edits. An execution callback, such as a Python Generator’s `main()`, must not modify the active document or show interface dialogs. See [Scripting Elements](manual_scripting_elements.md) and [Scene Execution](manual_scene_execution.md) for the restrictions on execution and threads.

### Plugins <a id="plugins"></a>

Obtain a unique plugin ID from the developer portal; never ship an SDK example ID in a plugin. Keep `.pyp` code, resources, descriptions, and icons together as described in [Implementing Plugins](manual_implementing_plugins.md).

## See Also <a id="see-also"></a>

- [Quickstart](manual_quickstart.md): Learn the basics of using the Cinema 4D Python API.
- [API Overview](manual_api_overview.md): Provides an overview of the major API components.
- [Implementing Plugins](manual_implementing_plugins.md): Explains the basic concepts of implementing plugins.
- [Python Environment](manual_python_environment.md): Explains the features and limitations of Cinema 4D’s Python runtime.
