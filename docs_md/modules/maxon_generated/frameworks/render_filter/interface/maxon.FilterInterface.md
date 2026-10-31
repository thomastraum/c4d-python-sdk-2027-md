<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/render_filter/interface/maxon.FilterInterface.html -->

# maxon.FilterInterface <a id="maxon-filterinterface"></a>

## Description <a id="module-maxon.FilterInterface"></a><a id="description"></a>

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

- [`maxon.FilterRef`](../reference/maxon.FilterRef.md#module-maxon.FilterRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Execute`](#maxon.FilterInterface.Execute)(input, output) | Executes the filter standalone. |
| [`Set`](#maxon.FilterInterface.Set)(parameter, data) | Sets a filter parameter. |
| [`SetProgressMonitor`](#maxon.FilterInterface.SetProgressMonitor)(progressMonitor, userPtr) | Sets a callback function which is getting invoked during filter execution with its progress. |

## Methods Definition <a id="methods-definition"></a>

### `FilterInterface.Execute(input, output)` <a id="maxon.FilterInterface.Execute"></a>

Executes the filter standalone.

**Parameters:**

- **input** (*maxon.FilterImageRef*) – The input Filter Image.
- **output** (*maxon.FilterImageRef*) – The target Filter Image.

### `FilterInterface.Set(parameter, data)` <a id="maxon.FilterInterface.Set"></a>

Sets a filter parameter.

**Parameters:**

- **parameter** (*maxon.Id*) – The id of the parameter to set.
- **data** (*maxon.Data*) – The data for the parameter.

### `FilterInterface.SetProgressMonitor(progressMonitor, userPtr)` <a id="maxon.FilterInterface.SetProgressMonitor"></a>

Sets a callback function which is getting invoked during filter execution with its progress.  
There can only be one callback attached at a time. Multiple calls to SetProgressMonitor() will replace the previously attached callback. The callback function is being called with the provided userPtr and a progress in the range [0, 1]. Returning false within the monitor will cancel further execution of the filter.

**Parameters:**

- **progressMonitor** (*Callable*[[*any*, *float*], *bool*]) – The progress monitor function with the signature `def MyCallBack (userPtr: any, progress: float) -> bool`.
- **userPtr** (*any*) – A custom user ptr that gets passed to the function pointer.
