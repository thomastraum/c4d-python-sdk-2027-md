<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/render_filter/interface/maxon.FilterCommandQueueInterface.html -->

# maxon.FilterCommandQueueInterface <a id="maxon-filtercommandqueueinterface"></a>

## Description <a id="module-maxon.FilterCommandQueueInterface"></a><a id="description"></a>

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

- [`maxon.FilterCommandQueueRef`](../reference/maxon.FilterCommandQueueRef.md#module-maxon.FilterCommandQueueRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`AttachFilter`](#maxon.FilterCommandQueueInterface.AttachFilter)(filter, input, output) | Enqueues a filter to the filter queue. |
| [`AttachFilterRect`](#maxon.FilterCommandQueueInterface.AttachFilterRect)(filter, input, output, x, …) | Enqueues a filter to the filter queue which will operate on a specific region of the image. |
| [`DetachFilter`](#maxon.FilterCommandQueueInterface.DetachFilter)(filter) | Dequeues a filter from the filter queue. |

## Methods Definition <a id="methods-definition"></a>

### `FilterCommandQueueInterface.AttachFilter(filter, input, output)` <a id="maxon.FilterCommandQueueInterface.AttachFilter"></a>

Enqueues a filter to the filter queue.

**Parameters:**

- **filter** (*maxon.FilterRef*) – Filter to enqueue.
- **input** (*maxon.FilterImageRef*) – Input Image to the filter.
- **output** (*maxon.FilterImageRef*) – Output Image of the filter.

### `FilterCommandQueueInterface.AttachFilterRect(filter, input, output, x, y, w, h)` <a id="maxon.FilterCommandQueueInterface.AttachFilterRect"></a>

Enqueues a filter to the filter queue which will operate on a specific region of the image.

**Parameters:**

- **filter** (*maxon.FilterRef*) – Filter to enqueue.
- **input** (*maxon.FilterImageRef*) – Input Image to the filter.
- **output** (*maxon.FilterImageRef*) – Output Image of the filter.
- **x** (*maxon.UInt32*) – Starting point x.
- **y** (*maxon.UInt32*) – Starting point y.
- **w** (*maxon.UInt32*) – Width of region.
- **h** (*maxon.UInt32*) – Height of region.

### `FilterCommandQueueInterface.DetachFilter(filter)` <a id="maxon.FilterCommandQueueInterface.DetachFilter"></a>

Dequeues a filter from the filter queue.

**Parameters:** **filter** (*maxon.FilterRef*) – Filter to dequeue
