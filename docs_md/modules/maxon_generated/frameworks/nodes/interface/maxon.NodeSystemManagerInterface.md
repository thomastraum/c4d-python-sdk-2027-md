<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/nodes/interface/maxon.NodeSystemManagerInterface.html -->

# maxon.NodeSystemManagerInterface <a id="maxon-nodesystemmanagerinterface"></a>

## Description <a id="module-maxon.NodeSystemManagerInterface"></a><a id="description"></a>

A node system manager manages a `maxon.NodeSystem` and several views on that `maxon.NodeSystem`, where each view is a [`maxon.NodesGraphModelRef`](../reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)  
A node system manager is created by methods of [`maxon.NodesGraphModelInterface`](maxon.NodesGraphModelInterface.md#module-maxon.NodesGraphModelInterface).  
The task of the manager is to coordinate accesses to a shared node system from different views:

- It stores a single NodeSystem reference which is used by all views.
- A `maxon.ChangeList` to track changes made by any of the views.
- [`maxon.GraphTransaction`](../../graph/datatype/maxon.GraphTransaction.md#module-maxon.GraphTransaction) observers which get informed about transactions made by any of the views.

`maxon.NodeSystemManagerClass` is the base implementation of this interface.  
It has to be used as base class for custom implementations.

> **Note:**
>
> This class as well as the views are not thread-safe.  
> This class coordinates different views, but everything has to happen within the same thread (or be properly synchronized by the callers).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObserverObjectInterface`](../../../interfaces/core_helper/maxon.ObserverObjectInterface.md#module-maxon.ObserverObjectInterface)
