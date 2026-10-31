<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/core_helper/maxon.ClassInterface.html -->

# maxon.ClassInterface <a id="maxon-classinterface"></a>

## Description <a id="module-maxon.ClassInterface"></a><a id="description"></a>

A [`maxon.ClassInterface`](#module-maxon.ClassInterface) object represents an object class at runtime.  
Such an object class can be published by `MAXON_DECLARATION()`, and it is then typically defined by `MAXON_COMPONENT_CLASS_REGISTER()`.  
A class consists of several components (see ComponentDescriptor), each of which may implement several virtual interfaces (declared by `ComponentDescriptor()`).  
The class itself then implements all interfaces of all of its components.  
Information about components and interfaces can be obtained from the ClassInfo object returned by `ObjectInterface.GetClassInfo()`.  
After allocation of a class, you have to add the components of which it shall consist via `ClassInterface.AddComponent()` or `ClassInterface.AddComponents()`.  
Afterwards, you can invoke `ClassInterface.Finalize()` to make the class ready for use.  
From then on, only const methods may be invoked on a class.  
If you use `maxon.GenericClass` or [`maxon.Class`](../../references/core_helper/maxon.Class.md#module-maxon.Class) to access a class, this is automatically guaranteed as those are const references.  
If you don’t invoke `ClassInterface.Finalize()`, this will be done implicitly when the first instance of the class is allocated.  
The `MAXON_COMPONENT_CLASS_REGISTER()` and `MAXON_COMPONENT_OBJECT_REGISTER()` macros greatly simplify the setup of a class.  
[`maxon.ClassInterface`](#module-maxon.ClassInterface) objects are automatically registered in the [`maxon.Classes`](../../registries/maxon.Classes.md#module-maxon.Classes) registry.

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.Class`](../../references/core_helper/maxon.Class.md#module-maxon.Class)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.ClassInterface.R`](maxon.ClassInterface.R.md#maxon.ClassInterface.R) | Stores the passed reference type if created e.g. |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Create`](#maxon.ClassInterface.Create)([type]) | Constructs a new instance of this class. |
| [`Finalize`](#maxon.ClassInterface.Finalize)() | Finalizes this class so that it can be used afterwards. |
| [`GetDataType`](#maxon.ClassInterface.GetDataType)() | Returns the data type corresponding to the set of implemented interfaces of this class. |
| [`GetId`](#maxon.ClassInterface.GetId)() | **return:** |
| [`GetKind`](#maxon.ClassInterface.GetKind)() | Returns the identifier of this object class. |
| [`IsFinalized`](#maxon.ClassInterface.IsFinalized)() | Returns True if the class has been finalized successfully before. |

## Methods Definition <a id="methods-definition"></a>

### `ClassInterface.Create(type=None)` <a id="maxon.ClassInterface.Create"></a>

Constructs a new instance of this class.  
This will invoke the constructors of each component in the order of addition, and then the [`ComponentRoot.InitComponent()`](../../datatypes/base_core/maxon.ComponentRoot.md#maxon.ComponentRoot.InitComponent) functions of each component.  
When one of the [`ComponentRoot.InitComponent()`](../../datatypes/base_core/maxon.ComponentRoot.md#maxon.ComponentRoot.InitComponent) functions fails with an error, [`ComponentRoot.FreeComponent()`](../../datatypes/base_core/maxon.ComponentRoot.md#maxon.ComponentRoot.FreeComponent) will be invoked on the previous (already initialized) components, the component destructors will be invoked, the memory will by freed, and [`ClassInterface.Create()`](#maxon.ClassInterface.Create) returns the error.  
For a singleton class, this doesn’t create a new instance, but returns the singleton instance of this class.  
This instance is automatically created on finalization of the class.  
For an abstract class, this will always raise an error.

**Parameters:**

- **type** – The expected type of object to create.
- **type** – Maxon API type.

**Returns:** Reference to new instance, or an error if the allocation or initialization failed.

**Return type:** [`maxon.Data`](../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

### `ClassInterface.Finalize()` <a id="maxon.ClassInterface.Finalize"></a>

Finalizes this class so that it can be used afterwards.  
The class has to be built before by `ClassInterface.AddComponent()`.  
Some internal data will be set-up for the class so that it is ready for use.  
If you don’t invoke [`ClassInterface.Finalize()`](#maxon.ClassInterface.Finalize), it will be done implicitly when an object of the class is instantiated for the first time.

### `ClassInterface.GetDataType()` <a id="maxon.ClassInterface.GetDataType"></a>

Returns the data type corresponding to the set of implemented interfaces of this class.

> **Note:** For an abstract class this will return None.

**Returns:** Data type of this class.

**Return type:** [`maxon.DataType`](../../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)

### `ClassInterface.GetId()` <a id="maxon.ClassInterface.GetId"></a>

**Returns:**

### `ClassInterface.GetKind()` <a id="maxon.ClassInterface.GetKind"></a>

Returns the identifier of this object class. Class identifiers are unique.

**Returns:** [`maxon.Class`](../../references/core_helper/maxon.Class.md#module-maxon.Class) identifier.

**Return type:** [`maxon.Id`](../../datatypes/id/maxon.Id.md#module-maxon.Id)

### `ClassInterface.IsFinalized()` <a id="maxon.ClassInterface.IsFinalized"></a>

Returns True if the class has been finalized successfully before.

**Returns:** True if the class is finalized.

**Return type:** bool
