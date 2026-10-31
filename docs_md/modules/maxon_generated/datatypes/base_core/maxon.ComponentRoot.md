<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/base_core/maxon.ComponentRoot.html -->

# maxon.ComponentRoot <a id="maxon-componentroot"></a>

## Description <a id="module-maxon.ComponentRoot"></a><a id="description"></a>

[`maxon.ComponentRoot`](#module-maxon.ComponentRoot) is the base class of all components (see [`maxon.MAXON_COMPONENT`](../../decorators/registry/maxon.MAXON_COMPONENT.md#maxon.MAXON_COMPONENT)).  
Usually you don’t have to take care of this because the [`maxon.Component`](maxon.Component.md#maxon.Component) template automatically sets [`maxon.ComponentRoot`](#module-maxon.ComponentRoot) as base class.  
But if you use `maxon.ComponentWithBase` instead, you have to make sure that the base class you use for that template derives from [`maxon.ComponentRoot`](#module-maxon.ComponentRoot).

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`CreateInit`](#maxon.ComponentRoot.CreateInit)(*args) | **param args:** |
| [`FreeComponent`](#maxon.ComponentRoot.FreeComponent)() | Gets called before an object gets destructed. |
| [`Get`](#maxon.ComponentRoot.Get)(ref) | **param ref:** |
| [`GetClass`](#maxon.ComponentRoot.GetClass)() | Retrieve the stored class |
| [`InitComponent`](#maxon.ComponentRoot.InitComponent)() | Gets called right after a new object has been constructed. |
| [`__init__`](#maxon.ComponentRoot.__init__)([data]) | Initialize self. |

## Methods Definition <a id="methods-definition"></a>

### *classmethod* `ComponentRoot.CreateInit(*args)` <a id="maxon.ComponentRoot.CreateInit"></a>

**Parameters:** **args** –

**Returns:**

### `ComponentRoot.FreeComponent()` <a id="maxon.ComponentRoot.FreeComponent"></a>

Gets called before an object gets destructed.  
You can override this function in a component class to free the component at a point of time where the whole object is still valid, so you can call methods or access other components which is not allowed in the destructor.  
But keep in mind that later components might already have done clean-up in their [`ComponentRoot.FreeComponent()`](#maxon.ComponentRoot.FreeComponent) functions.

### *classmethod* `ComponentRoot.Get(ref)` <a id="maxon.ComponentRoot.Get"></a>

**Parameters:** **ref** –

**Returns:**

### *classmethod* `ComponentRoot.GetClass()` <a id="maxon.ComponentRoot.GetClass"></a>

Retrieve the stored class

### `ComponentRoot.InitComponent()` <a id="maxon.ComponentRoot.InitComponent"></a>

Gets called right after a new object has been constructed.  
You can override this function in a component class to initialize the component.  
Unlike the constructor this function can return an error.  
Also all components have been constructed when this function gets called, so you can call methods or access other components.  
But keep in mind that only super components have been initialized.

### `ComponentRoot.__init__(data=None)` <a id="maxon.ComponentRoot.__init__"></a>

Initialize self. See help(type(self)) for accurate signature.
