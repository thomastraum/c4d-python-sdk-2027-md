<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/mxutils/mxutils.LocalImportPath.html -->

# mxutils.LocalImportPath <a id="mxutils-localimportpath"></a>

## Description <a id="module-mxutils.LocalImportPath"></a><a id="description"></a>

Provides the ability to import packages and modules from directories that are not exposed to the global module search paths.

Also allows for automatically reloading all modules which have been imported from such local package. This can be useful in the context of debugging, in order to be able to reload package dependencies when executing ‘Reload Python Plugins’ in Cinema 4D.

> **Note:** The auto reloading will discover relevant module dependencies on its own, but in cases where these modules must be reloaded in a specific order, the reloading must be carried out manually.

**Example:**

The manager will allow to import `my_package` (or parts of it) from the following directory structure,

```python
root
    +- res
        +- ...
    +- my_package
    |   +- __init__.py
    |   +- my_stuff.py
    |   +- my_things.py
    +- myPlugin.pyp
```

when executing it from within `myPlugin.pyp` with the module attribute `__file__` as follows:

```python
# This will expose `root` as a search path.
with LocalImportPath(__file__):
    import my_package
    from my_package import my_stuff as stuff
    ...
```

This will make the `root` as a search path available. Alternatively, a specific path can be provided and modules can be forcibly reloaded when Cinema 4D is executing the ‘Reload Python Plugins’ command.

```python
# This will (re)load the package `other_package` located in `c:\stuff` every time this
# scope is being executed. Auto reloading should not be turned on in release versions.
IS_DEBUG: bool = True
with LocalImportPath(r"c:\stuff", autoReload=IS_DEBUG):
    import other_package
```

Here is a more complete example where the type is used in a *CommandData* plugin.

```python
import c4d
from mxutils import LocalImportPath

# The plugin package would look as follows.
#
#     + root              <- the whole plugin
#       + myplibs         <- the libraries
#          + urllib3      <- a module/package to ship
#             ...
#          myplg_tools.py <- another module to ship
#          __init__.py    <- the package init file for "libs"
#       myplugin.pyp      <- this file

# Import the module urllib3 from 'libs'. We should not do what I am doing here, import a common 
# package under its common name. Importing urllib3 as 'url_lib3' does not change the key under which
# it is placed in `sys.modules`. Modules should always be named in such way that name collisions 
# become unlikely. LocalImportPath will avoid name collisions as best as it can, and not overwrite 
# existing modules, but this will then result in one of the plugins halting. To avoid this, urllib3
# should be renamed to something like myplg_urllib3, making it unique to ones plugin.
with LocalImportPath(__file__):
    import myplibs.urllib3 as url_lib3

class LocalImportContextTestCommand(c4d.plugins.CommandData):
    '''Realizes a command that uses the local module `url_lib3`.
    '''
    ID_PLUGIN: int = 1059908

    def Execute(self, doc: c4d.documents.BaseDocument) -> bool:
        '''Evaluates the response of "http://httpbin.org/robots.txt" on execution with `url_lib3`.
        '''
        # We can also import into a local scope. Here we import a module with a safe name, as there
        # could also be other plugins which have a `tools` module. In the local or global scope we
        # can then expose the module however we want, e.g., as `tools`.
        with LocalImportPath(__file__):
            import myplibs.myplg_tools as tools

        http = url_lib3.PoolManager()
        response = http.request("GET", "http://httpbin.org/robots.txt")

        print(f"{response.geturl() = }")
        print(f"{response.status = }")
        print(f"{response.data = }")
        return True

if __name__ == '__main__':
    c4d.plugins.RegisterCommandPlugin(
        id=LocalImportContextTestCommand.ID_PLUGIN,
        str="Local Import Context Test",
        info=c4d.PLUGINFLAG_SMALLNODE,
        icon=None,
        help="",
        dat=LocalImportContextTestCommand())
```

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`__enter__`](#mxutils.LocalImportPath.__enter__)() | Exposes the module search path of the manager to the global module search paths. |
| [`__exit__`](#mxutils.LocalImportPath.__exit__)(type, value, traceback) | Cleans up the module search paths and optionally reloads modules. |
| [`__init__`](#mxutils.LocalImportPath.__init__)(path[, autoReload]) | Initializes the context manger. |

## Methods Definition <a id="methods-definition"></a>

### `LocalImportPath.__enter__() → None` <a id="mxutils.LocalImportPath.__enter__"></a>

Exposes the module search path of the manager to the global module search paths.

### `LocalImportPath.__exit__(type: Any, value: Any, traceback: Any) → bool` <a id="mxutils.LocalImportPath.__exit__"></a>

Cleans up the module search paths and optionally reloads modules.

**Return type:** bool

### `LocalImportPath.__init__(path: str, autoReload: bool = False) → None` <a id="mxutils.LocalImportPath.__init__"></a>

Initializes the context manger.

**Parameters:** **path** (*str*) – The path relative to which packages should be exposed. If `path` is a file, its directory will be added. If `path` is a directory, `path` itself will be added to the search paths.

**Raises:**

- **TypeError** – On invalid argument types.
- **OSError** – When `path` does not point to an existing path.
