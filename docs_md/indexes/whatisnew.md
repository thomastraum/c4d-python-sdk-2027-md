<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/indexes/whatisnew.html -->

# SDK Change Notes for Cinema 4D 2027.0.0 <a id="sdk-change-notes-for-cinema-4d-release-version"></a>

Summarizes the API and API documentation changes made between Cinema 4D version 2026.0.0 and 2027.0.0.

## Documentation Changes <a id="documentation-changes"></a>

**Documentation**

**Added** and updated many manuals and removed outdated content.

- Added [API Overview](../manuals/manual_api_overview.md), providing an overview of the major API components.
- Added [Debugging](../manuals/manual_debugging.md), explaining how to find errors with the mxutils debug tools, and how to track down crashes caused by threading violations.
- Added [Geometry Model](../manuals/manual_geometry.md), explaining the geometry model of Cinema 4D: polygons, edges, normals, caches, and splines.
- Added [Implementing Plugins](../manuals/manual_implementing_plugins.md), explaining the basic concepts of implementing plugins.
- Added [Matrices](../manuals/manual_matrices.md), explaining matrices in the Cinema API: coordinate systems, transforms, and the operations of [`c4d.Matrix`](../modules/c4d/Matrix/index.md#c4d.Matrix).
- Added [Quickstart](../manuals/manual_quickstart.md), explaining the basics of using the Cinema 4D Python API.
- Added [Dialog and Description Resources](../manuals/manual_resource_files.md), explaining how to define dialogs and node parameters with resource files, and how to use them from Python.
- Added [Scene Execution](../manuals/manual_scene_execution.md), explaining how Cinema 4D updates a scene, and where Python code runs in that process.
- Added [Scene Structure](../manuals/manual_scene_structure.md), explaining how a scene is organized with hierarchies and branches, and how to traverse it.
- Added [Scripting Elements](../manuals/manual_scripting_elements.md), explaining the Python scripting elements embedded in Cinema 4D scenes.
- Added [Style Guide](../manuals/manual_style_guide.md), explaining the code style and conventions used in this SDK.
- Added [Vectors](../manuals/manual_vectors.md), explaining how to do vector operations.
- Added [Working with the SDK](../manuals/manual_working_with_sdk.md), providing an overview of how to work with the SDK in Cinema 4D.

**Added** the [Example Index](examples_index.md), listing all example scripts and plugins of the SDK.

**Added** the [Resource Index](resource_index.md), listing description resources, icons, description data types, and node templates.

**Added** many improvements to the documentation UI.

- Added dark mode support.
- Added custom search functionality.
- Added new change notes style.
- Added card-based layout for manuals and links.
- Added AI driven classification for entities in the Cinema API.
- Added SDK license information.
- Reworked the landing page by giving the Cinema and Maxon API a more logical structure.
- Updated sidebar handling.

**Added** stubs for the plugin reload and update functions.

- Added the documentation for [`c4d.plugins.ReloadPythonPlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.ReloadPythonPlugin), which reloads a single Python plugin file.
- Added the documentation for [`c4d.plugins.ReloadAllPythonPlugins()`](../modules/c4d.plugins/index.md#c4d.plugins.ReloadAllPythonPlugins), which reloads all Python plugin files.
- Added the documentation for [`c4d.plugins.ReloadDocumentAfterReload()`](../modules/c4d.plugins/index.md#c4d.plugins.ReloadDocumentAfterReload), which reloads documents so that their nodes use the classes of reloaded plugins.
- Added the documentation for [`c4d.plugins.Update()`](../modules/c4d.plugins/index.md#c4d.plugins.Update), which adds the symbols of the *c4d* module to the namespace of a plugin after its registration.

**Updated** the SDK structure and organization.

- Added auto-generated overview tables to the SDK examples.
- Added agentic metadata with *.agents* folder.
- Added place for user projects with the *projects* folder.
- Removed the old unnecessarily complicated example structure.

**Updated** the [Graph Descriptions](../manuals/manual_graph_descriptions.md) manual, see [Graph Queries](../manuals/manual_graph_descriptions.md#graph-description-queries) and [Lazy Literals](../manuals/manual_graph_descriptions.md#graph-description-lazy-literals) in particular.

- Added the ability to query connections between nodes.
- Added query operators and query compositions; you can now do more than simple equality checks, and carry out multiple checks on the same value.
- Added a query function which can be used outside of descriptions. With this function, you can also select ports as a query result, and not just nodes.
- Added [`maxon.GraphDescription.EvaluateQuery()`](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.md#maxon.GraphDescription.EvaluateQuery), which evaluates a query against a node graph.
- Added multiple new attributes on [`maxon.GraphDescription`](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.md#module-maxon.GraphDescription).
- Added syntax to describe groups in a graph description, and a command to dissolve groups.
- Added the concept of input groups.
- Added commands for setting nodes as start or solo nodes.
- Updated the already existing but mostly undocumented lazy literal functionality.
- Updated relevant description commands to now support specifying the ports to which the command selectively should apply to (some commands already supported this, but now all of them do where it makes sense).
- Updated [`maxon.GraphDescription.PARSE_FLAGS()`](../modules/maxon_generated/enums/maxon.GraphDescription.PARSE_FLAGS.md#module-maxon.GraphDescription.PARSE_FLAGS) to support new parsing modes.
- Updated [`maxon.GraphDescription.QUERY_FLAGS()`](../modules/maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.md#module-maxon.GraphDescription.QUERY_FLAGS) to support new query modes.

**Updated** the documentation of element-local dirty states and hierarchical change propagation.

- Updated the documentation for [`c4d.C4DAtom.GetDirty()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.GetDirty), [`c4d.C4DAtom.SetDirty()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.SetDirty), [`c4d.C4DAtom.GetHDirty()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.GetHDirty), [`c4d.C4DAtom.SetHDirty()`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom.SetHDirty), `DIRTYFLAGS`, and `HDIRTYFLAGS` to clarify element-local dirty states and hierarchical change propagation.

**Examples**

**Added** 33 example scripts.

| Example | Description |
|---|---|
| [data/_c4d_basebitmap.py](../examples/data/_c4d_basebitmap.py.md) | Demonstrates the usage of the central bitmap type. |
| [data/_c4d_basecontainer.py](../examples/data/_c4d_basecontainer.py.md) | Demonstrates the usage of the fundamental container type in the Cinema API. |
| [data/_c4d_descid.py](../examples/data/_c4d_descid.py.md) | Demonstrates important functions for the types c4d.DescID and c4d.DescLevel. |
| [data/_c4d_description.py](../examples/data/_c4d_description.py.md) | Demonstrates important functions for the type c4d.Description. |
| [data/_maxon_basearray.py](../examples/data/_maxon_basearray.py.md) | Demonstrates instantiation and usage of various Maxon data types. |
| [io/bitmap_init_vector_file.py](../examples/io/bitmap_init_vector_file.py.md) | Initializes a bitmap from a vector image file. |
| [math/_c4d_geraycollider.py](../examples/math/_c4d_geraycollider.py.md) | Demonstrates ray casting. |
| [math/_c4d_matrix.py](../examples/math/_c4d_matrix.py.md) | Demonstrates working with matrices. |
| [math/_c4d_noise.py](../examples/math/_c4d_noise.py.md) | Demonstrates working with noise functions. |
| [math/_c4d_quaternion.py](../examples/math/_c4d_quaternion.py.md) | Demonstrates working with quaternions. |
| [math/_c4d_vector.py](../examples/math/_c4d_vector.py.md) | Demonstrates working with vectors. |
| [math/_mxutils_random.py](../examples/math/_mxutils_random.py.md) | Demonstrates deterministic random values with mxutils.Random. |
| [misc/mxutils_checktype.py](../examples/misc/mxutils_checktype.py.md) | Demonstrates type and iterable validation with mxutils. |
| [misc/mxutils_debugprint.py](../examples/misc/mxutils_debugprint.py.md) | Demonstrates mxutils helpers for diagnosing Cinema 4D scene data. |
| [misc/mxutils_decorators.py](../examples/misc/mxutils_decorators.py.md) | Demonstrates mxutils helpers for diagnosing Cinema 4D scene data. |
| [misc/mxutils_localimportpath.py](../examples/misc/mxutils_localimportpath.py.md) | Demonstrates importing a package relative to a saved Python script. |
| [misc/mxutils_symboltranslationcache.py](../examples/misc/mxutils_symboltranslationcache.py.md) | Demonstrates translating Cinema 4D symbols with SymbolTranslationCache. |
| [nodes/graph_descriptions_basics.py](../examples/nodes/graph_descriptions_basics.py.md) | Demonstrates how graph descriptions create and modify node graphs. |
| [nodes/graph_descriptions_commands.py](../examples/nodes/graph_descriptions_commands.py.md) | Demonstrates graph description commands. |
| [nodes/graph_descriptions_queries.py](../examples/nodes/graph_descriptions_queries.py.md) | Demonstrates graph description queries, including lazy color and vector literals. |
| [nodes/graph_descriptions_references.py](../examples/nodes/graph_descriptions_references.py.md) | Demonstrates graph description references together with lazy color and URL literals. |
| [nodes/nodes_create_or_get_graphs.py](../examples/nodes/nodes_create_or_get_graphs.py.md) | Demonstrates creating or getting node graphs in a scene. |
| [scene/_c4d_atom.py](../examples/scene/_c4d_atom.py.md) | Demonstrates important functions for the type c4d.C4DAtom. |
| [scene/_c4d_baselist2d.py](../examples/scene/_c4d_baselist2d.py.md) | Demonstrates important functions for the type c4d.BaseList2D. |
| [scene/_c4d_gelistnode.py](../examples/scene/_c4d_gelistnode.py.md) | Demonstrates important functions for the type c4d.GeListNode. |
| [scene/documents.py](../examples/scene/documents.py.md) | Demonstrates basic document operations. |
| [scene/layers.py](../examples/scene/layers.py.md) | Demonstrates how to assign a scene element to a layer. |
| [scene/objects.py](../examples/scene/objects.py.md) | Demonstrates basic operations on objects. |
| [scene/parameters.py](../examples/scene/parameters.py.md) | Demonstrates different ways to access and modify parameters of Cinema 4D scene elements. |
| [scene/takes.py](../examples/scene/takes.py.md) | Demonstrates the fundamental operations of the Take System. |
| [scene/traversal.py](../examples/scene/traversal.py.md) | Demonstrates scene traversal. |
| [scene/undos.py](../examples/scene/undos.py.md) | Demonstrates adding undo steps for document modifications. |
| [scene/userdata.py](../examples/scene/userdata.py.md) | Demonstrates how to work with user data parameters. |

**Added** 2 example plugins.

| Example | Description |
|---|---|
| [py_cmd_gui_html](../examples/plugins/py_cmd_gui_html/py_cmd_gui_html.pyp.md) | Demonstrates how to implement a dialog that hosts an HTML viewer and can send and receive data to/from the displayed web page. |
| [py_obj_assetcontainer](../examples/plugins/py_obj_assetcontainer/py_obj_assetcontainer.pyp.md) | Demonstrates NodeData serialization and custom branching. |

## API Changes <a id="api-changes"></a>

**Cinema API**

**Added** [`c4d.bitmaps.BaseBitmap.InitFromImageRef()`](../modules/c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap.InitFromImageRef) and [`c4d.bitmaps.BaseBitmap.InitWithVectorFile()`](../modules/c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap.InitWithVectorFile).

- Added [`c4d.bitmaps.BaseBitmap.InitFromImageRef()`](../modules/c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap.InitFromImageRef), which initializes a *BaseBitmap* from an image reference.
- Added [`c4d.bitmaps.BaseBitmap.InitWithVectorFile()`](../modules/c4d.bitmaps/BaseBitmap/index.md#c4d.bitmaps.BaseBitmap.InitWithVectorFile), which initializes a *BaseBitmap* from a vector file.

**Added** JavaScript execution and web messaging to [`c4d.gui.HtmlViewerCustomGui`](../modules/c4d.gui/BaseCustomGui/HtmlViewerCustomGui/index.md#c4d.gui.HtmlViewerCustomGui).

- Added [`c4d.gui.HtmlViewerCustomGui.ExecuteJavaScript()`](../modules/c4d.gui/BaseCustomGui/HtmlViewerCustomGui/index.md#c4d.gui.HtmlViewerCustomGui.ExecuteJavaScript), which allows for executing JavaScript code within the HTML viewer.
- Added [`c4d.gui.HtmlViewerCustomGui.PostWebMessage()`](../modules/c4d.gui/BaseCustomGui/HtmlViewerCustomGui/index.md#c4d.gui.HtmlViewerCustomGui.PostWebMessage), which allows for posting web messages to the HTML viewer, see the *py_cmd_gui_html* example for details.
- Added [`c4d.gui.HtmlViewerCustomGui.SetRequestHeader()`](../modules/c4d.gui/BaseCustomGui/HtmlViewerCustomGui/index.md#c4d.gui.HtmlViewerCustomGui.SetRequestHeader), which allows for setting custom request headers in the HTML viewer.
- Added [`c4d.gui.HtmlViewerCustomGui.SetWebMessageCallback()`](../modules/c4d.gui/BaseCustomGui/HtmlViewerCustomGui/index.md#c4d.gui.HtmlViewerCustomGui.SetWebMessageCallback), which is the counter part to *PostWebMessage*.

**Added** [`c4d.plugins.NodeData.GetBranchInfo()`](../modules/c4d.plugins/BaseData/NodeData/index.md#c4d.plugins.NodeData.GetBranchInfo), which allows for adding custom branches to your node based plugins, see the *py_obj_assetcontainer* example.

**Fixed** [`c4d.plugins.ReloadPythonPlugin()`](../modules/c4d.plugins/index.md#c4d.plugins.ReloadPythonPlugin) scripts generated from the Plugin Manager to always use raw plugin paths, to avoid issues on Windows.

**Maxon API**

**Added** [`maxon.GraphDescription`](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.md#module-maxon.GraphDescription) connection queries, query operators, and port selection to graph descriptions.

- Added the ability to query connections between nodes.
- Added query operators and query compositions; you can now do more than simple equality checks, and carry out multiple checks on the same value.
- Added a query function which can be used outside of descriptions. With this function, you can also select ports as a query result, and not just nodes.
- Added [`maxon.GraphDescription.EvaluateQuery()`](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.md#maxon.GraphDescription.EvaluateQuery), which evaluates a query against a node graph.
- Added multiple new attributes on [`maxon.GraphDescription`](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.md#module-maxon.GraphDescription).
- Added syntax to describe groups in a graph description, and a command to dissolve groups.
- Added the concept of input groups.
- Added commands for setting nodes as start or solo nodes.
- Updated the already existing but mostly undocumented lazy literal functionality.
- Updated relevant description commands to now support specifying the ports to which the command selectively should apply to (some commands already supported this, but now all of them do where it makes sense).
- Updated [`maxon.GraphDescription.PARSE_FLAGS()`](../modules/maxon_generated/enums/maxon.GraphDescription.PARSE_FLAGS.md#module-maxon.GraphDescription.PARSE_FLAGS) to support new parsing modes.
- Updated [`maxon.GraphDescription.QUERY_FLAGS()`](../modules/maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.md#module-maxon.GraphDescription.QUERY_FLAGS) to support new query modes.

**Added** [`maxon.NodePath.GetPortPath()`](../modules/maxon_generated/frameworks/graph/datatype/maxon.NodePath.md#maxon.NodePath.GetPortPath) and [`maxon.NodePath.ToBlock()`](../modules/maxon_generated/frameworks/graph/datatype/maxon.NodePath.md#maxon.NodePath.ToBlock).

- Added [`maxon.NodePath.GetPortPath()`](../modules/maxon_generated/frameworks/graph/datatype/maxon.NodePath.md#maxon.NodePath.GetPortPath), which retrieves the port path component for a given node path.
- Added [`maxon.NodePath.ToBlock()`](../modules/maxon_generated/frameworks/graph/datatype/maxon.NodePath.md#maxon.NodePath.ToBlock), which converts the node path to a block representation.

**Updated** [`maxon.GraphNode.FindInnerNode()`](../modules/maxon_generated/frameworks/graph/datatype/maxon.GraphNode.md#maxon.GraphNode.FindInnerNode) to also accept [`maxon.NodePath`](../modules/maxon_generated/frameworks/graph/datatype/maxon.NodePath.md#module-maxon.NodePath) and strings.

**Mxutils API**

**Added** [`mxutils.DebugNode`](../modules/maxon_generated/mxutils/mxutils.DebugNode.md#module-mxutils.DebugNode) and [`mxutils.DebugPrint`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#module-mxutils.DebugPrint) for debug printing.

- Added [`mxutils.DebugNode`](../modules/maxon_generated/mxutils/mxutils.DebugNode.md#module-mxutils.DebugNode), a class for representing debug printing results.
- Added [`mxutils.DebugPrint`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#module-mxutils.DebugPrint), a class for performing debug printing operations.
- Added [`mxutils.DebugPrint.GetContainer()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetContainer), to get a *DebugNode* representation of a *c4d.BaseContainer*.
- Added [`mxutils.DebugPrint.GetFlags()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetFlags), to get a *DebugNode* representation of the flags of a *c4d.BaseList2D*.
- Added [`mxutils.DebugPrint.GetGraph()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetGraph), to get a *DebugNode* representation of a (partial) scene graph for a *c4d.BaseList2D*.
- Added [`mxutils.DebugPrint.GetParameters()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetParameters), to get a *DebugNode* representation of the parameters of a *c4d.BaseList2D*.
- Added [`mxutils.DebugPrint.GetTreeString()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetTreeString), to get a string representation of a *DebugNode*.
- Added [`mxutils.DebugPrint.PrintContainer()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.PrintContainer), to directly print the debug output of a *c4d.BaseContainer*.
- Added [`mxutils.DebugPrint.PrintFlags()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.PrintFlags), to directly print the debug output of the flags of a *c4d.BaseList2D*.
- Added [`mxutils.DebugPrint.PrintGraph()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.PrintGraph), to directly print the debug output of a (partial) scene graph for a *c4d.BaseList2D*.
- Added [`mxutils.DebugPrint.PrintParameters()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.PrintParameters), to directly print the debug output of the parameters of a *c4d.BaseList2D*.
- Added [`mxutils.DebugPrint.DiffParameters()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.DiffParameters), to get a string representation of the differences between the parameters of two *c4d.BaseList2D* objects.
- Added [`mxutils.DebugPrint.DiffFlags()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.DiffFlags), to get a string representation of the differences between the flags of two *c4d.BaseList2D* objects.
- Added [`mxutils.DebugPrint.DiffBaseList()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.DiffBaseList), to get a string representation of the differences between two *c4d.BaseList2D* objects.
- Added [`mxutils.DebugPrint.DiffGraph()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.DiffGraph), to get a string representation of the differences between the (partial) scene graphs of two *c4d.BaseList2D* objects.

**Added** [`mxutils.GetNodeFromPath()`](../modules/mxutils_api.md#mxutils.GetNodeFromPath), [`mxutils.IterateGraph()`](../modules/mxutils_api.md#mxutils.IterateGraph), and [`mxutils.SceneFaker.AddHierarchyFromString()`](../modules/maxon_generated/mxutils/mxutils.SceneFaker.md#mxutils.SceneFaker.AddHierarchyFromString).

- Added [`mxutils.GetNodeFromPath()`](../modules/mxutils_api.md#mxutils.GetNodeFromPath), which retrieves a *GeListNode* by a hierarchical path such as *‘ddn’* (down, down, next).
- Added [`mxutils.IterateGraph()`](../modules/mxutils_api.md#mxutils.IterateGraph), a 20% faster and safer replacement for *mxutils.RecurseGraph*.
- Added [`mxutils.SceneFaker.AddHierarchyFromString()`](../modules/maxon_generated/mxutils/mxutils.SceneFaker.md#mxutils.SceneFaker.AddHierarchyFromString).

**Updated** [`mxutils.IterateTree()`](../modules/mxutils_api.md#mxutils.IterateTree) to support depth-first, inverse depth-first, and breadth-first traversal.

- Updated [`mxutils.IterateTree()`](../modules/mxutils_api.md#mxutils.IterateTree) to now support the traversal modes `mxutils.TRAVERSAL_DEPTH_FIRST`, `mxutils.TRAVERSAL_INVERSE_DEPTH_FIRST`, and `mxutils.TRAVERSAL_BREADTH_FIRST`.

**Deprecated** five functions, which now point to their replacements and keep working.

All deprecated functions and methods now point to their respective replacements. The old callables will never be removed but no longer show up in the documentation. All replacements are API stable, i.e., old code of yours will continue to run as is (but automatically be redirected to the new implementations).

- Deprecated *mxutils.GetContainerTreeString*, please use [`mxutils.DebugPrint.GetContainer()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetContainer) instead.
- Deprecated *mxutils.GetParameterTreeString*, please use [`mxutils.DebugPrint.GetParameters()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetParameters) instead.
- Deprecated *mxutils.GetSceneGraphString*, please use [`mxutils.DebugPrint.GetGraph()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetGraph) instead.
- Deprecated *mxutils.GetTreeString*, please use [`mxutils.DebugPrint.GetTreeString()`](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md#mxutils.DebugPrint.GetTreeString) instead.
- Deprecated *mxutils.RecurseGraph*, please use [`mxutils.IterateGraph()`](../modules/mxutils_api.md#mxutils.IterateGraph) instead.
