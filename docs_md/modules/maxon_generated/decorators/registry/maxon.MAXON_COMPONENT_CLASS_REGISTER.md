<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/decorators/registry/maxon.MAXON_COMPONENT_CLASS_REGISTER.html -->

# maxon.MAXON_COMPONENT_CLASS_REGISTER <a id="maxon-maxon-component-class-register"></a>

## `maxon.MAXON_COMPONENT_CLASS_REGISTER(impl, registryOrCid, cid='', printErrors=True)` <a id="maxon.MAXON_COMPONENT_CLASS_REGISTER"></a>

MAXON_COMPONENT_OBJECT_REGISTER registers a component, creates an object class which uses the component and finally creates an instance of the object class.  
The instance is registered under the given identifier.  
As for MAXON_COMPONENT_CLASS_REGISTER, the object class consists of the base components and base classes (if any) which you have specified in the MAXON_COMPONENT macro, and then the component itself.  
You can obtain the object class by the GetClass() function of the component implementation class.  
In addition to MAXON_COMPONENT_CLASS_REGISTER this macro also creates an instance of the object class (using Create() on the class).  
This instance will be registered using the identifier given as argument to the macro.  
So you use this macro e.g. for registries like IoHandlers with entries of type IoHandler, while you use MAXON_COMPONENT_CLASS_REGISTER for registries like  
UnitTestClasses with entries of type Class\<UnitTestRef>.

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.
