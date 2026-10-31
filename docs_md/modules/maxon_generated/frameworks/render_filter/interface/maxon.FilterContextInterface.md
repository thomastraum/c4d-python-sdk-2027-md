<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/render_filter/interface/maxon.FilterContextInterface.html -->

# maxon.FilterContextInterface <a id="maxon-filtercontextinterface"></a>

## Description <a id="module-maxon.FilterContextInterface"></a><a id="description"></a>

Object is the root of the interface hierarchy of the MAXON API.  
As a C++ class, each virtual interface is directly derived from Object, but as an interface a virtual interface may have an arbitrary number of base interfaces, all of which have Object as direct or indirect base interface.  
The interface hierarchy is reflected by the Ptr, ConstPtr and reference classes of the interfaces: They have conversion operators to all base interfaces, and they contain functions for all methods of the interface and its base interfaces.  
Object provides some general inheritance-related functions such as GetClass() and IsInstanceOf(), data-related functions such as Clone() and CopyFrom(), and virtual methods such as ToString() which are required for each Object.  
All Object instances are reference-counted.  
Within the declaration of an interface you may choose the reference behaviour on invocation of a non-const method (normal, const, copy-on-write).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.FilterContextRef`](../reference/maxon.FilterContextRef.md#module-maxon.FilterContextRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`CreateCommandQueue`](#maxon.FilterContextInterface.CreateCommandQueue)() | Creates a command queue. |
| [`CreateFilter`](#maxon.FilterContextInterface.CreateFilter)(filterType) | Creates a filter from a filter type identifier. |
| [`CreateImage`](#maxon.FilterContextInterface.CreateImage)(imageDesc) | Creates an image matching the passed image description. |
| [`ExecuteCommandQueue`](#maxon.FilterContextInterface.ExecuteCommandQueue)(commandQueue) | Executes all the filters inside the command queue. |
| [`Init`](#maxon.FilterContextInterface.Init)([dict]) | Initializes the context. |

## Methods Definition <a id="methods-definition"></a>

### `FilterContextInterface.CreateCommandQueue()` <a id="maxon.FilterContextInterface.CreateCommandQueue"></a>

Creates a command queue.

**Returns:** The created Command Queue.

**Return type:** maxon.FilterCommandQueueRef

### `FilterContextInterface.CreateFilter(filterType)` <a id="maxon.FilterContextInterface.CreateFilter"></a>

Creates a filter from a filter type identifier.

**Parameters:** **filterType** (*maxon.LiteralId*) – The type of the filter.

**Returns:** The created Filter.

**Return type:** maxon.FilterRef

### `FilterContextInterface.CreateImage(imageDesc)` <a id="maxon.FilterContextInterface.CreateImage"></a>

Creates an image matching the passed image description.

**Parameters:** **imageDesc** (*maxon.DataDictionnary*) – The image description.

**Returns:** The created Image.

**Return type:** maxon.FilterImageRef

### `FilterContextInterface.ExecuteCommandQueue(commandQueue)` <a id="maxon.FilterContextInterface.ExecuteCommandQueue"></a>

Executes all the filters inside the command queue.

**Parameters:** **commandQueue** (*maxon.FilterCommandQueueRef*) – The command queue to execute.

### `FilterContextInterface.Init(dict=maxon.DataDictionary object at 0x12e9b7b2860 with the data: DataDictionary{})` <a id="maxon.FilterContextInterface.Init"></a>

Initializes the context.

**Parameters:** **dict** (*maxon.DataDictionnary*) – (Optional) input parameters.
