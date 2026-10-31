<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_api_overview.html -->

# API Overview <a id="api-overview"></a>

Provides an overview of the major API components.

The Cinema 4D Python API includes three complementary components: the Cinema API (`c4d`, see the [reference](../modules/cinema_api.md)), the Maxon API (`maxon`, see the [reference](../modules/maxon/maxon_api.md)), and Python-specific helpers in `mxutils` (see the [reference](../modules/mxutils_api.md)). They can be used together in the same script or plugin. See [Quickstart](manual_quickstart.md) to run an introductory script.

## Cinema API <a id="cinema-api"></a>

The `c4d` module provides core Cinema 4D functionality. A [`BaseDocument`](../modules/c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument) contains a scene hierarchy, materials, animation, and render settings. Objects are [`BaseObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) instances; tags are [`BaseTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag) instances attached to objects. These scene entities derive from [`BaseList2D`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D), which provides names, descriptions, and parameter access. Traverse the object hierarchy through its first child and next sibling, rather than assuming that all objects are in one flat list, see [Scene Structure](manual_scene_structure.md).

Parameters have identifiers defined in Cinema 4D’s description resources. Access a value with `object[c4d.PRIM_CUBE_LEN]` or a [`DescID`](../modules/c4d/DescID/index.md#c4d.DescID) when addressing a nested parameter. These identifiers are not necessarily the interface labels shown in the Attribute Manager. Use the [Resource Index](../indexes/resource_index.md) and the type reference to look up the identifier rather than guessing it.

## Maxon API <a id="maxon-api"></a><a id="maxon-api-introduction"></a>

The `maxon` module exposes nodes, assets, volumes, and other modern parts of Cinema 4D. It is the API which Cinema 4D itself is built with, and it follows different conventions than the Cinema API: functionality is split into frameworks, types come as interfaces and references, and a failed operation raises an exception. Do not assume that a Maxon reference and a similarly named `c4d` object are interchangeable.

Node materials and scene nodes are a common reason to use `maxon`. A graph contains nodes and their input/output ports; editing it requires the proper graph context and transaction. The [Graph Descriptions](manual_graph_descriptions.md) shows how to create and update node materials. The classes for graphs are in the [nodes](../modules/maxon/frameworks/nodes.md) and [graph](../modules/maxon/frameworks/graph.md) frameworks. For node IDs and port definitions shipped with a given release, consult the [Resource Index](../indexes/resource_index.md).

### Frameworks <a id="frameworks"></a>

The API is organized in frameworks, each covering one area, such as [volume](../modules/maxon/frameworks/volume.md) for OpenVDB volumes or [nodes](../modules/maxon/frameworks/nodes.md) for node graphs. The members of all frameworks are available directly in the `maxon` module. The [Maxon API reference](../modules/maxon/maxon_api.md) lists them by framework.

### Interfaces and References <a id="interfaces-and-references"></a><a id="maxon-api-interfaces-references"></a>

Most types of the Maxon API consist of two parts:

| Part | Naming | Role |
|---|---|---|
| Interface | [`maxon.VolumeInterface`](../modules/maxon_generated/frameworks/volume/interface/maxon.VolumeInterface.md#module-maxon.VolumeInterface) | Declares the functions of a type. The implementation lives in Cinema 4D and is hidden. Python cannot define new implementations, only use the existing ones. Interfaces are not used directly. |
| Reference | [`maxon.VolumeRef`](../modules/maxon_generated/frameworks/volume/reference/maxon.VolumeRef.md#module-maxon.VolumeRef) | The object a script works with. It is a handle to an instance of an implementation, and calling one of its methods runs the function of the interface on that instance. |

You get a reference by calling the reference type, for example `maxon.VolumeRef()`, or as the result of an API call. Assigning a reference in Python only adds another name for the same handle.

Some references have no `Ref` suffix, e.g., [`maxon.Url`](../modules/maxon_generated/references/io/maxon.Url.md#module-maxon.Url) for [`maxon.UrlInterface`](../modules/maxon_generated/interfaces/io/maxon.UrlInterface.md#module-maxon.UrlInterface). These are copy-on-write references: copies share their data until one of them is modified. Scripts do not have to handle this; it only explains why the suffix can be missing.

### Data Types and Registries <a id="data-types-and-registries"></a>

The Maxon API has its own data types which match its C++ counterparts: for example [`maxon.Int32`](../modules/maxon_generated/datatypes/simple/maxon.Int32.md#module-maxon.Int32), [`maxon.Float64`](../modules/maxon_generated/datatypes/simple/maxon.Float64.md#module-maxon.Float64), [`maxon.BaseArray`](../modules/maxon_generated/datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray), [`maxon.Tuple`](../modules/maxon_generated/datatypes/collection/maxon.Tuple.md#module-maxon.Tuple), [`maxon.Url`](../modules/maxon_generated/references/io/maxon.Url.md#module-maxon.Url), and [`maxon.Id`](../modules/maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id). Use [`maxon.MaxonConvert()`](../modules/maxon_generated/functions/maxon.MaxonConvert.md#maxon.MaxonConvert) to convert a Maxon value to a Python built-in type.

Registries store the components of the API, such as classes and implementations, by [`maxon.Id`](../modules/maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id). They are how you discover what is available, for example [`maxon.Loggers`](../modules/maxon_generated/registries/maxon.Loggers.md#module-maxon.Loggers), the registry of all loggers. Python can read registries, but only the C++ API can add new entries to them.

## mxutils API <a id="mxutils-api"></a>

The `mxutils` module offers Python-specific convenience tools, mainly for working with the Cinema API. For example, [`mxutils.LocalImportPath`](../modules/maxon_generated/mxutils/mxutils.LocalImportPath.md#module-mxutils.LocalImportPath) temporarily adds a plugin-local module directory to the import path, and [`mxutils.CheckType()`](../modules/mxutils_api.md#mxutils.CheckType) checks the result of an API call before you use it. These helpers complement rather than replace `c4d` and `maxon`. The [mxutils reference](../modules/mxutils_api.md) lists all of them.

## See Also <a id="see-also"></a>

- [Quickstart](manual_quickstart.md): Learn the basics of using the Cinema 4D Python API.
- [Python Environment](manual_python_environment.md): Explains the features and limitations of Cinema 4D’s Python runtime.
- [Scene Structure](manual_scene_structure.md): Explains how a Cinema 4D scene is organized with hierarchies and branches, and how to traverse it.
- [Implementing Plugins](manual_implementing_plugins.md): Explains the basic concepts of implementing plugins.
