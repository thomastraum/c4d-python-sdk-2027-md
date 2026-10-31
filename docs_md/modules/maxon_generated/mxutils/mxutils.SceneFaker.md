<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/mxutils/mxutils.SceneFaker.html -->

# mxutils.SceneFaker <a id="mxutils-scenefaker"></a>

## Description <a id="module-mxutils.SceneFaker"></a><a id="description"></a>

Generates random scene data such as objects, materials, tags, layers, render data and tracks.

Meant to be used in development, testing, and debugging scenarios. Is not meant to be used in production code.

> **Note:**
>
> `mxutils.g_scene_faker` is a global instance of this class that can be used directly.

**Example:**

```python
import c4d
import mxutils

# Get the active document and the global scene faker.
doc: c4d.documents.BaseDocument = c4d.documents.GetActiveDocument()
faker: mxutils.SceneFaker = mxutils.g_scene_faker

# Add 3 to 10 random generator objects to the document.
generators: list[c4d.BaseObject] = faker.AddRandomGeneratorObjects(doc, 3, 10)

# Add 3 to 5 random materials to the document and apply them to the generator objects.
materials: list[c4d.BaseMaterial] = faker.AddRandomMaterials(doc, 3, 5, generators)

# Add 1 to 2 random tags to the generator objects.
tags: list[c4d.BaseTag] = faker.AddRandomTags(generators, 1, 2)

# Flush the whole document and create a new random scene in it.
faker.RandomizeScene(doc, flushScene=True)
```

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`AddHierarchyFromString`](#mxutils.SceneFaker.AddHierarchyFromString)(doc, hierarchy[, …]) | Creates and returns an object hierarchy described by an indented string. |
| [`AddRandomGeneratorObjects`](#mxutils.SceneFaker.AddRandomGeneratorObjects)(doc[, minCount, …]) | Returns a list of randomly selected generator objects which have been added to the passed document. |
| [`AddRandomLayers`](#mxutils.SceneFaker.AddRandomLayers)(doc[, minCount, maxCount, …]) | Returns a list of randomly created layers which have been added to the passed document. |
| [`AddRandomMaterials`](#mxutils.SceneFaker.AddRandomMaterials)(doc[, minCount, …]) | Returns a list of randomly created standard renderer materials which have been added to the passed document. |
| [`AddRandomRenderData`](#mxutils.SceneFaker.AddRandomRenderData)(doc[, minCount, …]) | Returns a list of randomly created render data which have been added to the passed document. |
| [`AddRandomTags`](#mxutils.SceneFaker.AddRandomTags)(objects[, minCount, maxCount, …]) | Returns a list of randomly created tags which have been added to the passed objects. |
| [`AddRandomTracks`](#mxutils.SceneFaker.AddRandomTracks)(elements[, minCount, …]) | Returns a list of randomly created tracks which have been added to the passed elements. |
| [`RandomizeHierarchy`](#mxutils.SceneFaker.RandomizeHierarchy)(objects[, …]) | Randomizes the hierarchy of the passed objects. |
| [`RandomizeParameters`](#mxutils.SceneFaker.RandomizeParameters)(nodes[, whitelist, …]) | Randomizes parameter values of the passed nodes. |
| [`RandomizeScene`](#mxutils.SceneFaker.RandomizeScene)([doc, flushScene, …]) | Randomizes the scene data of the passed document. |
| [`RandomizeTransform`](#mxutils.SceneFaker.RandomizeTransform)(nodes[, minPosition, …]) | Randomizes the global transformation matrices of the passed objects. |
| [`__init__`](#mxutils.SceneFaker.__init__)([random]) | Initializes the faker with a random number generator. |

## Methods Definition <a id="methods-definition"></a>

### `SceneFaker.AddHierarchyFromString(doc: c4d.documents.BaseDocument, hierarchy: str, callback: Optional[Callable[[c4d.BaseObject], None], None] = None, buildCaches: bool = True) → list` <a id="mxutils.SceneFaker.AddHierarchyFromString"></a>

Creates and returns an object hierarchy described by an indented string.

Each non-empty line describes one object. Leading indentation defines the parent-child relationship, and the indentation size is discovered from the input. Spaces and tabs can be used for indentation. A line can end with `::` followed by an integer object type ID. Lines without a type ID create null objects. The special name `:@` leaves the object’s natural name unchanged, and can be combined with a type ID as in `:@::{c4d.Ocube}`.

> **Note:** The indentation is not of fixed size and can use either spaces or tabs but must be consistent throughout the hierarchy. I.e., when the first indentation is three spaces, all subsequent indentations must be a multiple of three spaces. The function can correctly handle extra indentation due to indented scopes.

**Parameters:**

- **doc** – The document in which to create the hierarchy.
- **hierarchy** – The indented hierarchy description.
- **callback** – An optional callback invoked for each created object.
- **buildCaches** – Whether to execute the document passes after creating the hierarchy. Defaults to `True`.

**Returns:** All created objects in input order.

**Example:**

```python
import c4d
import mxutils

def OnNodeCreated(node: c4d.BaseObject) -> None:
    '''Helper function called when a new node is created.
    '''
    # Unfold the node in the first Object Manager.
    node.ChangeNBit(c4d.NBIT_OM1_FOLD, c4d.NBITCONTROL_SET)

# Creates the hierarchy described by the indented string.
#
#  A
#  ├── B (Cube)
#  ├── C (Sphere)
#  └── D
#      └── E
#
doc: c4d.documents.BaseDocument = c4d.documents.GetActiveDocument()
hierarchy: str = (
f'''
A
    B::{c4d.Ocube}
    C::{c4d.Osphere}
    D
        E
''')

mxutils.g_scene_faker.AddHierarchyFromString(doc, hierarchy, OnNodeCreated)

# The function also handles extra indentation gracefully, ignoring all indentation that 
# is common to all lines. We could also write the example like this:
class Bar:
    def foo(self) -> list[c4d.BaseObject]:
        return mxutils.g_scene_faker.AddHierarchyFromString(doc,
        f'''
        A
            B::{c4d.Ocube}
            C::{c4d.Osphere}
            D
                E
        ''' )

# And it would work the same despite there being preceding indentation in the string. Make
# sure to add a line break after the opening triple quotes, so that the function can correctly 
# determine the base indentation.
```

### `SceneFaker.AddRandomGeneratorObjects(doc: c4d.documents.BaseDocument, minCount: int = 3, maxCount: int = 10, randomizeParameters: bool = True, buildCaches: bool = False, objTypes: tuple = 5160, 5159, 5163, 5161, 5171, 5164, 5167) → list` <a id="mxutils.SceneFaker.AddRandomGeneratorObjects"></a>

Returns a list of randomly selected generator objects which have been added to the passed document.

> **Note:** This method is primarily meant to generate generator objects.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to create the objects in.
- **minCount** (*int* (, *optional*)) – The minimum number of objects to generate. Defaults to `3`.
- **maxCount** (*int* (, *optional*)) – The maximum number of objects to generate. Defaults to `10`.
- **randomizeParameters** (*bool* (, *optional*)) – When `True` the parameters of the objects will be randomized. Defaults to `True`.
- **buildCaches** (*bool* (, *optional*)) – When `True` the generator caches of the objects will be built. Defaults to `False`.
- **objTypes** (*tuple*[*int*] (, *optional*)) – The list of object types to choose from. Defaults to `(c4d.Osphere, c4d.Ocube, c4d.Otorus, c4d.Oplatonic, c4d.Ocapsule, c4d.Odisc, c4d.Opyramid)`.

**Returns:** The list of generator objects which have been added to the document.

**Return type:** list[[c4d.BaseObject](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]

### `SceneFaker.AddRandomLayers(doc: c4d.documents.BaseDocument, minCount: int = 3, maxCount: int = 5, elements: list[c4d.BaseList2D] | None = None) → list` <a id="mxutils.SceneFaker.AddRandomLayers"></a>

Returns a list of randomly created layers which have been added to the passed document.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to create the layers in.
- **minCount** (*int* (, *optional*)) – The minimum number of layers to generate. Defaults to `3`.
- **maxCount** (*int* (, *optional*)) – The maximum number of layers to generate. Defaults to `5`.
- **elements** (*list*[[*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)] *| None* (, *optional*)) – The scene elements to add to the layers. When `None` the layers will be empty. Defaults to `None`.

**Returns:** The list of layers which have been added to the document.

**Return type:** list[[c4d.BaseList2D](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

### `SceneFaker.AddRandomMaterials(doc: c4d.documents.BaseDocument, minCount: int = 3, maxCount: int = 5, objects: list[c4d.BaseObject] | None = None) → list` <a id="mxutils.SceneFaker.AddRandomMaterials"></a>

Returns a list of randomly created standard renderer materials which have been added to the passed document.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to create the materials in.
- **minCount** (*int* (, *optional*)) – The minimum number of materials to generate. Defaults to `3`.
- **maxCount** (*int* (, *optional*)) – The maximum number of materials to generate. Defaults to `5`.
- **objects** (*list*[[*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)] *| None* (, *optional*)) – The objects to apply the materials to. When `None`, the materials will not be applied to any object. Defaults to `None`.

**Returns:** The list of materials which have been added to the document.

**Return type:** list[[c4d.BaseMaterial](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.md#c4d.BaseMaterial)]

### `SceneFaker.AddRandomRenderData(doc: c4d.documents.BaseDocument, minCount: int = 1, maxCount: int = 3, randomizeParameters: bool = False) → list` <a id="mxutils.SceneFaker.AddRandomRenderData"></a>

Returns a list of randomly created render data which have been added to the passed document.

When `randomizeParameters` is set to `True`, the parameters `c4d.RDATA_XRES`, `c4d.RDATA_YRES`, `c4d.RDATA_FRAMEFROM`, `c4d.RDATA_FRAMETO`, `c4d.RDATA_FORMAT` and `c4d.RDATA_PATH` will be randomized.

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to create the render data in.
- **minCount** (*int* (, *optional*)) – The minimum number of render data to generate. Defaults to `1`.
- **maxCount** (*int* (, *optional*)) – The maximum number of render data to generate. Defaults to `3`.
- **randomizeParameters** (*bool* (, *optional*)) – When `True` the parameters of the render data will be randomized. Defaults to `False`.

**Returns:** The list of render data which have been added to the document.

**Return type:** list[[c4d.BaseList2D](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]

### `SceneFaker.AddRandomTags(objects: list, minCount: int = 1, maxCount: int = 2, randomizeParameters: bool = False, tagTypes: tuple = 5612, 465001537, 5682, buildCaches: bool = False) → list` <a id="mxutils.SceneFaker.AddRandomTags"></a>

Returns a list of randomly created tags which have been added to the passed objects.

**Parameters:**

- **objects** (*list*[[*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – The objects to add the tags to.
- **minCount** (*int* (, *optional*)) – The minimum number of tags to generate per object. Defaults to `1`.
- **maxCount** (*int* (, *optional*)) – The maximum number of tags to generate per object. Defaults to `2`.
- **randomizeParameters** (*bool* (, *optional*)) – When `True` the parameters of the tags will be randomized. Defaults to `False`.
- **tagTypes** (*tuple*[*int*] (, *optional*)) – The list of tag types to choose from. Defaults to `(c4d.Tphong, c4d.Ttodo, c4d.Tvertexmap)`.
- **buildCaches** (*bool* (, *optional*)) – When `True` the caches of the objects will be built. Defaults to `False`.

**Returns:** The list of tags which have been added to the objects.

**Return type:** list[[c4d.BaseTag](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)]

### `SceneFaker.AddRandomTracks(elements: list, minCount: int = 1, maxCount: int = 3, minKeys: int = 1, maxKeys: int = 10) → list` <a id="mxutils.SceneFaker.AddRandomTracks"></a>

Returns a list of randomly created tracks which have been added to the passed elements.

> **Note:** This method is currently bugged. It will not work as intended.

**Parameters:**

- **elements** (*list*[[*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)]) – The elements to add the tracks to.
- **minCount** (*int* (, *optional*)) – The minimum number of tracks to generate per element. Defaults to `1`.
- **maxCount** (*int* (, *optional*)) – The maximum number of tracks to generate per element. Defaults to `3`.
- **minKeys** (*int* (, *optional*)) – The minimum number of keys to generate per track. Defaults to `1`.
- **maxKeys** (*int* (, *optional*)) – The maximum number of keys to generate per track. Defaults to `10`.
- **randomizeParameters** (*bool* (, *optional*)) – When `True` the parameters of the tracks will be randomized. Defaults to `False`.

**Returns:** The list of tracks which have been added to the elements.

**Return type:** list[[c4d.CTrack](../../c4d/C4DAtom/GeListNode/BaseList2D/CTrack/index.md#c4d.CTrack)]

### `SceneFaker.RandomizeHierarchy(objects: list, randomizeParameters: bool = False, buildCaches: bool = False) → None` <a id="mxutils.SceneFaker.RandomizeHierarchy"></a>

Randomizes the hierarchy of the passed objects.

The objects will be removed from their document and reinserted in a random order. The hierarchy will not necessarily terminate into a single root object. The objects will be renamed to reflect their new hierarchy. All objects must belong to the same document.

**Parameters:**

- **objects** (*list*[[*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – The objects to randomize the hierarchy for.
- **randomizeParameters** (*bool* (, *optional*)) – When `True` the parameters of the objects will be randomized. Defaults to `False`.
- **buildCaches** (*bool* (, *optional*)) – When `True` the caches of the objects will be built. Defaults to `False`.

**Raises:** **ValueError** – When the objects do not belong to the same document.

### `SceneFaker.RandomizeParameters(nodes: list, whitelist: list[c4d.DescID] | list[int] | None = None, buildCaches: bool = False) → None` <a id="mxutils.SceneFaker.RandomizeParameters"></a>

Randomizes parameter values of the passed nodes.

Only parameters of type `bool`, `int`, `float`, `str`, `c4d.BaseTime` and `c4d.Vector` will be randomized. Parameters below an ID of 1000 will be ignored.

**Parameters:**

- **node** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The node to randomize the parameters for.
- **whitelist** (*list*[[*c4d.DescID*](../../c4d/DescID/index.md#c4d.DescID)] *| list*[*int*] *| None* (, *optional*)) – A list of parameter IDs to randomize. When `None`, all parameters will be randomized, otherwise only the parameters in the list will be randomized. Defaults to `None`.
- **buildCaches** (*bool* (, *optional*)) – When `True` the caches of the nodes will be built. Defaults to `False`.

### `SceneFaker.RandomizeScene(doc: c4d.documents.BaseDocument | None = None, flushScene: bool = True, minObjects: int = 5, maxObjects: int = 10, minMaterials: int = 3, maxMaterials: int = 5, minLayers: int = 2, maxLayers: int = 3, minRenderData: int = 1, maxRenderData: int = 3, minTracks: int = 1, maxTracks: int = 2, minKeys: int = 2, maxKeys: int = 8, randomizeParameters: bool = True, buildCaches: bool = True) → None` <a id="mxutils.SceneFaker.RandomizeScene"></a>

Randomizes the scene data of the passed document.

Provides a high-level wrapper around the other methods of this class to generate complete scenes from scratch.

**Parameters:**

- **doc** (*c4d.documents.BaseDocument | None*) – The document to randomize the scene data for. Will create a new document when `None` is passed. Defaults to `None`.
- **flushScene** (*bool* (, *optional*)) – When `True` the scene will be flushed before adding new data. Defaults to `True`.
- **minObjects** (*int* (, *optional*)) – The minimum number of objects to generate. Defaults to `5`.
- **maxObjects** (*int* (, *optional*)) – The maximum number of objects to generate. Defaults to `10`.
- **minMaterials** (*int* (, *optional*)) – The minimum number of materials to generate. Defaults to `3`.
- **maxMaterials** (*int* (, *optional*)) – The maximum number of materials to generate. Defaults to `5`.
- **minLayers** (*int* (, *optional*)) – The minimum number of layers to generate. Defaults to `2`.
- **maxLayers** (*int* (, *optional*)) – The maximum number of layers to generate. Defaults to `3`.
- **minRenderData** (*int* (, *optional*)) – The minimum number of render data to generate. Defaults to `1`.
- **maxRenderData** (*int* (, *optional*)) – The maximum number of render data to generate. Defaults to `3`.
- **minTracks** (*int* (, *optional*)) – The minimum number of tracks to generate. Defaults to `1`.
- **maxTracks** (*int* (, *optional*)) – The maximum number of tracks to generate. Defaults to `2`.
- **minKeys** (*int* (, *optional*)) – The minimum number of keys to generate per track. Defaults to `2`.
- **maxKeys** (*int* (, *optional*)) – The maximum number of keys to generate per track. Defaults to `8`.
- **randomizeParameters** (*bool* (, *optional*)) – When `True` the parameters of scene elements will be randomized. Defaults to `True`.
- **buildCaches** (*bool* (, *optional*)) – When `True` the caches of the generated scene will be built. Defaults to `True`.

### `SceneFaker.RandomizeTransform(nodes: list, minPosition: c4d.Vector = Vector(- 2000, - 2000, - 2000), maxPosition: c4d.Vector = Vector(2000, 2000, 2000), minRotation: c4d.Vector = Vector(0, 0, 0), maxRotation: c4d.Vector = Vector(3.142, 3.142, 3.142), minScale: c4d.Vector = Vector(1, 1, 1), maxScale: c4d.Vector = Vector(1, 1, 1))` <a id="mxutils.SceneFaker.RandomizeTransform"></a>

Randomizes the global transformation matrices of the passed objects.

**Parameters:**

- **nodes** (*list*[[*c4d.BaseObject*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)]) – The nodes to randomize the transformation for.
- **minPosition** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector) (, *optional*)) – The minimum position values for the objects. Defaults to `c4d.Vector(-2000.0)`.
- **maxPosition** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector) (, *optional*)) – The maximum position values for the objects. Defaults to `c4d.Vector(2000.0)`.
- **minRotation** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector) (, *optional*)) – The minimum rotation values for the objects. Defaults to `c4d.Vector(0)`.
- **maxRotation** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector) (, *optional*)) – The maximum rotation values for the objects. Defaults to `c4d.Vector(3.1415)`.
- **minScale** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector) (, *optional*)) – The minimum scale values for the objects. Defaults to `c4d.Vector(1)`.
- **maxScale** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector) (, *optional*)) – The maximum scale values for the objects. Defaults to `c4d.Vector(1.0)`.

### `SceneFaker.__init__(random: mxutils.mxu_math.Random | None = None) → None` <a id="mxutils.SceneFaker.__init__"></a>

Initializes the faker with a random number generator.

**Parameters:** **random** (*mxutils.Random | None*) – The random number generator to use. Will use the global random number generator when not provided. Defaults to `None`.
