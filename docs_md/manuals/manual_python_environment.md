<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_python_environment.html -->

# Python Environment <a id="python-environment"></a>

Explains the features and limitations of Cinema 4D’s Python runtime.

Cinema 4D 2027.0.0 embeds a CPython 3.11 interpreter. It behaves much like standard Python, but code runs in Cinema 4D alongside other scripts and plugins. The application supplies the `c4d`, `maxon`, and `mxutils` modules. The differences below matter when importing libraries and managing interpreter state.

## Virtual Machine <a id="virtual-machine"></a>

The embedded interpreter persists while Cinema 4D runs. Scripts and plugins share its imported modules and other interpreter-wide state. Reloading a script does not necessarily reset a module that it previously imported; restarting Cinema 4D provides a fresh interpreter.

| Difference | Implication |
|---|---|
| Shared state | Changes to common modules and global settings can affect other scripts and plugins in the same application process. |
| Execution context | Script Manager provides `doc` and `op`; plugin modules do not. Scene scripting elements run in execution callbacks, which restrict what they can change. See [Scripting Elements](manual_scripting_elements.md). |
| Search paths | A plugin folder is not automatically on `sys.path`. Use explicit installation paths or [`mxutils.LocalImportPath`](../modules/maxon_generated/mxutils/mxutils.LocalImportPath.md#module-mxutils.LocalImportPath) when importing code packaged alongside a plugin. |
| Standalone Python | Cinema 4D ships `c4dpy` for running Python outside the graphical application. A separate system Python cannot simply import `c4d`. See [Standalone Interpreter](manual_standalone_interpreter.md). |

## Libraries and Search Paths <a id="libraries-and-search-paths"></a>

Third-party packages must be compatible with Cinema 4D’s Python version, platform, and architecture. An editor’s virtual environment is separate from the application: installing a package there does not install it into Cinema 4D. Native extensions need matching binaries; check the Python Console with `import sys; print(sys.version)` when selecting them.

Install libraries in an application-specific or interpreter-bound search path, or configure the appropriate `C4DPYTHONPATH` variable for the Python version shipped with your Cinema 4D release. Avoid putting unrelated versions of the same library on global search paths. Plugin directories are not default module search paths; use [`mxutils.LocalImportPath`](../modules/maxon_generated/mxutils/mxutils.LocalImportPath.md#module-mxutils.LocalImportPath) for local imports rather than permanently changing `sys.path`. See [External Libraries](manual_external_libraries.md) for the current paths, variable names, and examples.

## Interpreter Limits <a id="interpreter-limits"></a>

Do not launch another Cinema 4D Python VM with `multiprocessing` or by passing `sys.executable` to `subprocess`. Use [Standalone Interpreter](manual_standalone_interpreter.md) for supported standalone execution. Do not use Python’s `threading` module to operate on Cinema 4D data; see [Scene Execution](manual_scene_execution.md) and `c4d.threading` for the application’s threading rules. Scene execution callbacks can be invoked repeatedly or concurrently and must not make arbitrary edits to the active document.

## See Also <a id="see-also"></a>

- [Quickstart](manual_quickstart.md): Learn the basics of using the Cinema 4D Python API.
- [Standalone Interpreter](manual_standalone_interpreter.md): Explains how to use Cinema 4D’s standalone interpreter, c4dpy.
- [External Libraries](manual_external_libraries.md): Explains how to expose third-party libraries to Cinema 4D Python.
- [Working with the SDK](manual_working_with_sdk.md): Set up Visual Studio Code to work with the Cinema 4D Python SDK.
