<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/collection/maxon.Block.html -->

# maxon.Block <a id="maxon-block"></a>

## Description <a id="module-maxon.Block"></a><a id="description"></a>

A [`maxon.Block`](#module-maxon.Block) stands for a number of elements with a regular memory layout.  
It consists of a pointer for the first element, the element count and optionally a stride.  
All elements are placed consecutively in memory, but with a possible padding in between.  
The stride is the pointer difference between consecutive elements in bytes.  
y default, the stride is just SIZEOF(T).  
You can use an alternative stride length to access only specific elements of your array.  
For example if you have an array with XYZ vectors and want to access only the X-values as a block, you could use the pointer to the first X-value and a stride length of SIZEOF(Vector).  
Or for a [`maxon.Block`](#module-maxon.Block) whose elements are all the same, you can use a stride of 0 and a pointer to a single value.  
There is an important difference between a Block and arrays such as BaseArray with respect  
to the meaning of a const Block: A const block can’t be modified itself, so its pointer and length cannot be  
changed, but the memory to which the block points is still non-const (if #T is a non-const type).  
So you can modify the memory through a const block. In other words, a[13] = 42;  
A [`maxon.Block`](#module-maxon.Block) supports the usual array functions which do not modify the length.  
Also it can be converted to the Array interface.  
If unsupported functions are invoked then, they will cause a DebugStop and indicate a failure on return.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)
