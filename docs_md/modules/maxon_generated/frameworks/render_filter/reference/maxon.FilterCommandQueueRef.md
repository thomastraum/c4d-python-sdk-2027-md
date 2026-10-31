<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/render_filter/reference/maxon.FilterCommandQueueRef.html -->

# maxon.FilterCommandQueueRef <a id="maxon-filtercommandqueueref"></a>

## Description <a id="module-maxon.FilterCommandQueueRef"></a><a id="description"></a>

Object is the root of the interface hierarchy of the MAXON API.  
As a C++ class, each virtual interface is directly derived from Object, but as an interface a virtual interface may have an arbitrary number of base interfaces, all of which have Object as direct or indirect base interface.  
The interface hierarchy is reflected by the Ptr, ConstPtr and reference classes of the interfaces: They have conversion operators to all base interfaces, and they contain functions for all methods of the interface and its base interfaces.  
Object provides some general inheritance-related functions such as GetClass() and IsInstanceOf(), data-related functions such as Clone() and CopyFrom(), and virtual methods such as ToString() which are required for each Object.  
All Object instances are reference-counted.  
Within the declaration of an interface you may choose the reference behaviour on invocation of a non-const method (normal, const, copy-on-write).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.FilterCommandQueueInterface`](../interface/maxon.FilterCommandQueueInterface.md#module-maxon.FilterCommandQueueInterface)
- [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)
