<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/render_filter/interface/maxon.FilterImageInterface.html -->

# maxon.FilterImageInterface <a id="maxon-filterimageinterface"></a>

## Description <a id="module-maxon.FilterImageInterface"></a><a id="description"></a>

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

- [`maxon.FilterImageRef`](../reference/maxon.FilterImageRef.md#module-maxon.FilterImageRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`ReadFromCPUMemory`](#maxon.FilterImageInterface.ReadFromCPUMemory)(data) | Copies contents from the CPU memory block. |
| [`WriteToBuffer`](#maxon.FilterImageInterface.WriteToBuffer)(buffer) | Writes the contents out into a buffer. |
| [`WriteToFile`](#maxon.FilterImageInterface.WriteToFile)(url) | Writes the contents out into a file. |

## Methods Definition <a id="methods-definition"></a>

### `FilterImageInterface.ReadFromCPUMemory(data)` <a id="maxon.FilterImageInterface.ReadFromCPUMemory"></a>

Copies contents from the CPU memory block.

**Parameters:** **data** (*maxon.BaseArray*(*maxon.Vector4D32*)) – Data to read.

**Returns:**

### `FilterImageInterface.WriteToBuffer(buffer)` <a id="maxon.FilterImageInterface.WriteToBuffer"></a>

Writes the contents out into a buffer.

**Parameters:** **buffer** (*maxon.BaseArray*(*maxon.Vector4D32*)) – The output buffer.

**Returns:**

### `FilterImageInterface.WriteToFile(url)` <a id="maxon.FilterImageInterface.WriteToFile"></a>

Writes the contents out into a file.

**Parameters:** **url** (*maxon.Url*) – The url to write to.
