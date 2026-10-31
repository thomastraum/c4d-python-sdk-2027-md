<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/core/maxon.CStringInterface.html -->

# maxon.CStringInterface <a id="maxon-cstringinterface"></a>

## Description <a id="module-maxon.CStringInterface"></a><a id="description"></a>

Class to store ASCII strings. CString stores 8 bit characters.  
Any characters are legal, including 0C (strings are not null-terminated).  
Strings are reference-counted objects.  
This means that as long as you copy and do not modify strings they are just referenced.  
The first modification breaks the link and it becomes a unique new object.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Builtin`](../../datatypes/base_core/maxon.Builtin.md#module-maxon.Builtin)

Child Class:

- [`maxon.CString`](../../references/core/maxon.CString.md#module-maxon.CString)
