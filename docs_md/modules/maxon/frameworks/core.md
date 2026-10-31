<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon/frameworks/core.html -->

# maxon <a id="maxon"></a><a id="framework-core"></a>

> **Note:** Core members documented here are defined directly in `maxon`; there is no `maxon.frameworks.core` module. See the [Maxon API](../../../manuals/manual_api_overview.md#maxon-api-introduction) section of the API Overview for more information about the special conventions of this API.

Module for fundamental Maxon API types and operations.

## Interfaces <a id="interfaces"></a>

### Hardware and Software Information <a id="hardware-and-software-information"></a>

|   |   |
|---|---|
| [`MachineInterface`](../../maxon_generated/interfaces/information/maxon.MachineInterface.md#module-maxon.MachineInterface)(*args) | This class is the entry point to access machine interfaces. |
| [`MachinesInterface`](../../maxon_generated/interfaces/information/maxon.MachinesInterface.md#module-maxon.MachinesInterface)() | This class declares functions to access and manage machines. |
| [`Application`](../../maxon_generated/interfaces/information/maxon.Application.md#module-maxon.Application)() | Application wide functions. |
| [`System`](../../maxon_generated/interfaces/information/maxon.System.md#module-maxon.System)() | Application wide system functions. |

### I/O <a id="i-o"></a>

|   |   |
|---|---|
| [`FileFormatHandlerInterface`](../../maxon_generated/interfaces/io/maxon.FileFormatHandlerInterface.md#module-maxon.FileFormatHandlerInterface)(*args) | FileFormatHandlerInterface implements a handler for a specific FileFormat. |
| [`FileFormatInterface`](../../maxon_generated/interfaces/io/maxon.FileFormatInterface.md#module-maxon.FileFormatInterface)(*args) | [`maxon.FileFormatInterface`](../../maxon_generated/interfaces/io/maxon.FileFormatInterface.md#module-maxon.FileFormatInterface) allows to implement and register file formats with its detection algorithm. |
| [`IoHandlerInterface`](../../maxon_generated/interfaces/io/maxon.IoHandlerInterface.md#module-maxon.IoHandlerInterface)(*args) | The IoHandler class offers some I/O functionality for filenames. |
| [`IoConnectionInterface`](../../maxon_generated/interfaces/io/maxon.IoConnectionInterface.md#module-maxon.IoConnectionInterface)(*args) | The connection interface a given [`maxon.Url`](../../maxon_generated/references/io/maxon.Url.md#module-maxon.Url). |
| [`IoBrowseInterface`](../../maxon_generated/interfaces/io/maxon.IoBrowseInterface.md#module-maxon.IoBrowseInterface)(*args) | The [`IoBrowseIterator`](../../maxon_generated/datatypes/core_iterator/maxon.IoBrowseIterator.md#module-maxon.IoBrowseIterator) interface for a given [`maxon.Url`](../../maxon_generated/references/io/maxon.Url.md#module-maxon.Url). |
| [`BaseStreamInterface`](../../maxon_generated/interfaces/io/maxon.BaseStreamInterface.md#module-maxon.BaseStreamInterface)(*args) | Interface is the base interface for all stream interfaces. |
| [`InOutputStreamInterface`](../../maxon_generated/interfaces/io/maxon.InOutputStreamInterface.md#module-maxon.InOutputStreamInterface)(*args) | Creates an [`maxon.InOutputStreamInterface`](../../maxon_generated/interfaces/io/maxon.InOutputStreamInterface.md#module-maxon.InOutputStreamInterface) class to read/write bytes from/into streams. |
| [`InputStreamInterface`](../../maxon_generated/interfaces/io/maxon.InputStreamInterface.md#module-maxon.InputStreamInterface)(*args) | Interface for input streams. It allows to read data from streams. |
| [`OutputStreamInterface`](../../maxon_generated/interfaces/io/maxon.OutputStreamInterface.md#module-maxon.OutputStreamInterface)(*args) | Creates an [`maxon.OutputStreamInterface`](../../maxon_generated/interfaces/io/maxon.OutputStreamInterface.md#module-maxon.OutputStreamInterface) class to write bytes into streams. |
| [`UrlInterface`](../../maxon_generated/interfaces/io/maxon.UrlInterface.md#module-maxon.UrlInterface)(*args) | Interface class for [`maxon.Url`](../../maxon_generated/references/io/maxon.Url.md#module-maxon.Url). |

### Network <a id="network"></a>

|   |   |
|---|---|
| [`NetworkIpInterface`](../../maxon_generated/interfaces/network/maxon.NetworkIpInterface.md#module-maxon.NetworkIpInterface)() | Static interface to access network functionality. |
| [`NetworkIpAddrInterface`](../../maxon_generated/interfaces/network/maxon.NetworkIpAddrInterface.md#module-maxon.NetworkIpAddrInterface)(*args) | Represents an Internet Protocol (IP) address. |
| [`NetworkIpAddrPortInterface`](../../maxon_generated/interfaces/network/maxon.NetworkIpAddrPortInterface.md#module-maxon.NetworkIpAddrPortInterface)(*args) | Provides an Internet Protocol (IP) address + port. |

### Logger <a id="logger"></a>

|   |   |
|---|---|
| [`LoggerTypeInterface`](../../maxon_generated/interfaces/logger/maxon.LoggerTypeInterface.md#module-maxon.LoggerTypeInterface)(*args) | Each object of `maxon.LoggerLine` represents an entry in the logger with several meta information. |
| [`LoggerInterface`](../../maxon_generated/interfaces/logger/maxon.LoggerInterface.md#module-maxon.LoggerInterface)(*args) | The logger interface allows to create new custom loggers for specific tasks and to access existing loggers. |

### Misc <a id="misc"></a>

|   |   |
|---|---|
| [`Timer`](../../maxon_generated/interfaces/misc/maxon.Timer.md#module-maxon.Timer)() | A timer class to retrieve the current time. |
| [`GradientKnot`](../../maxon_generated/interfaces/misc/maxon.GradientKnot.md#module-maxon.GradientKnot)([otherOrColor, brightness, …]) | Initializes the appropriate C++ Data object and store it within the _data member. |
| [`GradientInterface`](../../maxon_generated/interfaces/misc/maxon.GradientInterface.md#module-maxon.GradientInterface)() | This is the interface for the Gradient data type. |
| [`Gradient`](../../maxon_generated/interfaces/misc/maxon.Gradient.md#module-maxon.Gradient)(*args) | Reference class for [`maxon.GradientInterface`](../../maxon_generated/interfaces/misc/maxon.GradientInterface.md#module-maxon.GradientInterface). |
| [`GradientRenderDataInterface`](../../maxon_generated/interfaces/misc/maxon.GradientRenderDataInterface.md#module-maxon.GradientRenderDataInterface)() |  |
| [`GradientRenderData`](../../maxon_generated/interfaces/misc/maxon.GradientRenderData.md#module-maxon.GradientRenderData)(*args) | Reference class for [`maxon.GradientRenderDataInterface`](../../maxon_generated/interfaces/misc/maxon.GradientRenderDataInterface.md#module-maxon.GradientRenderDataInterface). |

### Core <a id="core"></a>

|   |   |
|---|---|
| [`DataDictionaryObjectInterface`](../../maxon_generated/interfaces/core/maxon.DataDictionaryObjectInterface.md#module-maxon.DataDictionaryObjectInterface)(*args) | Class to store and find any [`maxon.Data`](../../maxon_generated/datatypes/base_core/maxon.Data.md#module-maxon.Data) type under any type of key. |
| [`DataDictionaryInterface`](../../maxon_generated/interfaces/core/maxon.DataDictionaryInterface.md#module-maxon.DataDictionaryInterface)(*args) | Class to store and find any data type under any type of key. |
| [`RegistryInterface`](../../maxon_generated/interfaces/core/maxon.RegistryInterface.md#module-maxon.RegistryInterface)([C]) | [`maxon.RegistryInterface`](../../maxon_generated/interfaces/core/maxon.RegistryInterface.md#module-maxon.RegistryInterface) is used internally by [`maxon.Registry`](../../maxon_generated/references/core/maxon.Registry.md#module-maxon.Registry). |
| [`StringInterface`](../../maxon_generated/interfaces/core/maxon.StringInterface.md#module-maxon.StringInterface)([C]) | Class to store unicode strings. String stores 16bit unicode characters. |
| [`CStringInterface`](../../maxon_generated/interfaces/core/maxon.CStringInterface.md#module-maxon.CStringInterface)([C]) | Class to store ASCII strings. CString stores 8 bit characters. |
| [`UuidInterface`](../../maxon_generated/interfaces/core/maxon.UuidInterface.md#module-maxon.UuidInterface)() |  |
| [`Resource`](../../maxon_generated/interfaces/core/maxon.Resource.md#module-maxon.Resource)() | Class that handles resources. |
| [`LanguageInterface`](../../maxon_generated/interfaces/core/maxon.LanguageInterface.md#module-maxon.LanguageInterface)() |  |
| [`DataDescriptionInterface`](../../maxon_generated/interfaces/core/maxon.DataDescriptionInterface.md#module-maxon.DataDescriptionInterface)() |  |

### Core Helper <a id="core-helper"></a>

|   |   |
|---|---|
| [`ClassInterface`](../../maxon_generated/interfaces/core_helper/maxon.ClassInterface.md#module-maxon.ClassInterface)(*args) | A [`maxon.ClassInterface`](../../maxon_generated/interfaces/core_helper/maxon.ClassInterface.md#module-maxon.ClassInterface) object represents an object class at runtime. |
| [`ObjectInterface`](../../maxon_generated/interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)(*args) | Object is the root of the interface hierarchy of the MAXON API. |
| [`AutoIterator`](../../maxon_generated/interfaces/core_helper/maxon.AutoIterator.md#module-maxon.AutoIterator)(array[, beginIndex]) | AutoIterator implements a foreach iterator for a BaseArray |
| [`ObserverObjectInterface`](../../maxon_generated/interfaces/core_helper/maxon.ObserverObjectInterface.md#module-maxon.ObserverObjectInterface)(*args) | [`maxon.Component`](../../maxon_generated/datatypes/base_core/maxon.Component.md#maxon.Component) to allow [`maxon.ObjectInterface`](../../maxon_generated/interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface) interfaces to use the observable concept. |

## References <a id="references"></a>

### Hardware and Software Information <a id="id1"></a>

|   |   |
|---|---|
| [`MachineRef`](../../maxon_generated/references/information/maxon.MachineRef.md#module-maxon.MachineRef)(*args) | Reference class of [`maxon.MachineInterface`](../../maxon_generated/interfaces/information/maxon.MachineInterface.md#module-maxon.MachineInterface). |

### I/O <a id="id2"></a>

|   |   |
|---|---|
| [`FileFormatHandler`](../../maxon_generated/references/io/maxon.FileFormatHandler.md#module-maxon.FileFormatHandler)(*args) | Reference class of [`maxon.FileFormatHandlerInterface`](../../maxon_generated/interfaces/io/maxon.FileFormatHandlerInterface.md#module-maxon.FileFormatHandlerInterface). |
| [`FileFormat`](../../maxon_generated/references/io/maxon.FileFormat.md#module-maxon.FileFormat)(*args) | Reference class of [`maxon.FileFormatInterface`](../../maxon_generated/interfaces/io/maxon.FileFormatInterface.md#module-maxon.FileFormatInterface). |
| [`IoHandler`](../../maxon_generated/references/io/maxon.IoHandler.md#module-maxon.IoHandler)(*args) | Reference class of [`maxon.IoHandlerInterface`](../../maxon_generated/interfaces/io/maxon.IoHandlerInterface.md#module-maxon.IoHandlerInterface). |
| [`IoConnectionRef`](../../maxon_generated/references/io/maxon.IoConnectionRef.md#module-maxon.IoConnectionRef)(*args) | Reference class of [`maxon.IoConnectionInterface`](../../maxon_generated/interfaces/io/maxon.IoConnectionInterface.md#module-maxon.IoConnectionInterface). |
| [`IoBrowseRef`](../../maxon_generated/references/io/maxon.IoBrowseRef.md#module-maxon.IoBrowseRef)(*args) | Reference class of [`maxon.IoBrowseInterface`](../../maxon_generated/interfaces/io/maxon.IoBrowseInterface.md#module-maxon.IoBrowseInterface). |
| [`InOutputStreamRef`](../../maxon_generated/references/io/maxon.InOutputStreamRef.md#module-maxon.InOutputStreamRef)(*args) | Reference class of [`maxon.InOutputStreamInterface`](../../maxon_generated/interfaces/io/maxon.InOutputStreamInterface.md#module-maxon.InOutputStreamInterface). |
| [`InputStreamRef`](../../maxon_generated/references/io/maxon.InputStreamRef.md#module-maxon.InputStreamRef)(*args) | Reference class of [`maxon.InputStreamInterface`](../../maxon_generated/interfaces/io/maxon.InputStreamInterface.md#module-maxon.InputStreamInterface). |
| [`OutputStreamRef`](../../maxon_generated/references/io/maxon.OutputStreamRef.md#module-maxon.OutputStreamRef)(*args) | Reference class of [`maxon.OutputStreamInterface`](../../maxon_generated/interfaces/io/maxon.OutputStreamInterface.md#module-maxon.OutputStreamInterface). |
| [`Url`](../../maxon_generated/references/io/maxon.Url.md#module-maxon.Url)(*args, **kwargs) | Reference class of [`maxon.UrlInterface`](../../maxon_generated/interfaces/io/maxon.UrlInterface.md#module-maxon.UrlInterface). |

### Network <a id="id3"></a>

|   |   |
|---|---|
| [`NetworkIpAddr`](../../maxon_generated/references/network/maxon.NetworkIpAddr.md#module-maxon.NetworkIpAddr)(*args) | Reference class of [`maxon.NetworkIpAddrInterface`](../../maxon_generated/interfaces/network/maxon.NetworkIpAddrInterface.md#module-maxon.NetworkIpAddrInterface). |
| [`NetworkIpAddrPort`](../../maxon_generated/references/network/maxon.NetworkIpAddrPort.md#module-maxon.NetworkIpAddrPort)(*args) | Reference class of [`maxon.OutputStreamInterface`](../../maxon_generated/interfaces/io/maxon.OutputStreamInterface.md#module-maxon.OutputStreamInterface). |

### Logger <a id="id4"></a>

|   |   |
|---|---|
| [`LoggerTypeRef`](../../maxon_generated/references/logger/maxon.LoggerTypeRef.md#module-maxon.LoggerTypeRef)(*args) | Reference class of [`maxon.LoggerTypeInterface`](../../maxon_generated/interfaces/logger/maxon.LoggerTypeInterface.md#module-maxon.LoggerTypeInterface). |
| [`LoggerRef`](../../maxon_generated/references/logger/maxon.LoggerRef.md#module-maxon.LoggerRef)(*args) | Reference class of [`maxon.LoggerInterface`](../../maxon_generated/interfaces/logger/maxon.LoggerInterface.md#module-maxon.LoggerInterface). |

### Core <a id="id5"></a>

|   |   |
|---|---|
| [`DataDictionary`](../../maxon_generated/references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)(*args) | Reference class of [`maxon.DataDictionaryInterface`](../../maxon_generated/interfaces/core/maxon.DataDictionaryInterface.md#module-maxon.DataDictionaryInterface). |
| [`Registry`](../../maxon_generated/references/core/maxon.Registry.md#module-maxon.Registry)() | Registries are used to register specific implementations of a given interface. |
| [`String`](../../maxon_generated/references/core/maxon.String.md#module-maxon.String)([C]) | Reference class of [`maxon.StringInterface`](../../maxon_generated/interfaces/core/maxon.StringInterface.md#module-maxon.StringInterface). |
| [`CString`](../../maxon_generated/references/core/maxon.CString.md#module-maxon.CString)([C]) | Reference class of [`maxon.CStringInterface`](../../maxon_generated/interfaces/core/maxon.CStringInterface.md#module-maxon.CStringInterface). |
| [`ThreadRef`](../../maxon_generated/references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)([C]) | Reference to a `maxon.ThreadInterface`. |
| [`LanguageRef`](../../maxon_generated/references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)(*args) | Reference class of [`maxon.LanguageInterface`](../../maxon_generated/interfaces/core/maxon.LanguageInterface.md#module-maxon.LanguageInterface). |
| [`DataDescription`](../../maxon_generated/references/core/maxon.DataDescription.md#module-maxon.DataDescription)(*args) | Reference class of [`maxon.DataDescriptionInterface`](../../maxon_generated/interfaces/core/maxon.DataDescriptionInterface.md#module-maxon.DataDescriptionInterface). |
| [`Uuid`](../../maxon_generated/references/core/maxon.Uuid.md#module-maxon.Uuid)(*args) | Reference class of [`maxon.UuidInterface`](../../maxon_generated/interfaces/core/maxon.UuidInterface.md#module-maxon.UuidInterface). |

### Core Helper <a id="id6"></a>

|   |   |
|---|---|
| [`Class`](../../maxon_generated/references/core_helper/maxon.Class.md#module-maxon.Class)(*args) | Reference class of [`maxon.ClassInterface`](../../maxon_generated/interfaces/core_helper/maxon.ClassInterface.md#module-maxon.ClassInterface). |
| [`ObjectRef`](../../maxon_generated/references/core_helper/maxon.ObjectRef.md#module-maxon.ObjectRef)(*args) | Creates and stores internally the reference of the C++ Data. |

## Data Types <a id="data-types"></a>

### Simple Data Type <a id="simple-data-type"></a>

|   |   |
|---|---|
| [`Bool`](../../maxon_generated/datatypes/simple/maxon.Bool.md#module-maxon.Bool)([C]) | Boolean type, possible values are only False/True, 8 bits. |
| [`Char`](../../maxon_generated/datatypes/simple/maxon.Char.md#module-maxon.Char)([C]) | Signed 8 bits character. |
| [`UChar`](../../maxon_generated/datatypes/simple/maxon.UChar.md#module-maxon.UChar)([C]) | Unsigned 8 bits character. |
| [`Float`](../../maxon_generated/datatypes/simple/maxon.Float.md#module-maxon.Float) | alias of `maxon.interface.Float64` |
| [`Float32`](../../maxon_generated/datatypes/simple/maxon.Float32.md#module-maxon.Float32)([C]) | Floating point value 32 bits (float). |
| [`Float64`](../../maxon_generated/datatypes/simple/maxon.Float64.md#module-maxon.Float64)([C]) | Floating point value 64 bits (double). |
| [`Int`](../../maxon_generated/datatypes/simple/maxon.Int.md#module-maxon.Int) | alias of `maxon.interface.Int64` |
| [`Int16`](../../maxon_generated/datatypes/simple/maxon.Int16.md#module-maxon.Int16)([C]) | Signed integer 16 bits (either positive or negative number). |
| [`Int32`](../../maxon_generated/datatypes/simple/maxon.Int32.md#module-maxon.Int32)([C]) | Signed integer 32 bits (either positive or negative number). |
| [`Int64`](../../maxon_generated/datatypes/simple/maxon.Int64.md#module-maxon.Int64)([C]) | Signed integer 64 bits (either positive or negative number). |
| [`UInt`](../../maxon_generated/datatypes/simple/maxon.UInt.md#module-maxon.UInt) | alias of `maxon.interface.UInt64` |
| [`UInt16`](../../maxon_generated/datatypes/simple/maxon.UInt16.md#module-maxon.UInt16)([C]) | Unsigned integer 16 bits (always positive number). |
| [`UInt32`](../../maxon_generated/datatypes/simple/maxon.UInt32.md#module-maxon.UInt32)([C]) | Unsigned integer 32 bits (always positive number). |
| [`UInt64`](../../maxon_generated/datatypes/simple/maxon.UInt64.md#module-maxon.UInt64)([C]) | Unsigned integer 64 bits (always positive number). |

### Vector / Matrix Data Type <a id="vector-matrix-data-type"></a>

|   |   |
|---|---|
| [`Vec3`](../../maxon_generated/datatypes/vec_col_mat/maxon.Vec3.md#module-maxon.Vec3)([x, y, z]) | A vector consisting of three components X, Y and Z. |
| [`Vector32`](../../maxon_generated/datatypes/vec_col_mat/maxon.Vector32.md#module-maxon.Vector32)([x, y, z]) | Initializes a new three component vector. |
| [`Vector64`](../../maxon_generated/datatypes/vec_col_mat/maxon.Vector64.md#module-maxon.Vector64)([x, y, z]) | Initializes a new three component vector. |
| [`Vector`](../../maxon_generated/datatypes/vec_col_mat/maxon.Vector.md#module-maxon.Vector) | alias of `maxon.vector.Vector64` |
| [`IntVector32`](../../maxon_generated/datatypes/vec_col_mat/maxon.IntVector32.md#module-maxon.IntVector32)([x, y, z]) | Initializes a new three component vector. |
| [`IntVector64`](../../maxon_generated/datatypes/vec_col_mat/maxon.IntVector64.md#module-maxon.IntVector64)([x, y, z]) | Initializes a new three component vector. |
| [`IntVector`](../../maxon_generated/datatypes/vec_col_mat/maxon.IntVector.md#module-maxon.IntVector) | alias of `maxon.vector.IntVector64` |
| [`Col3`](../../maxon_generated/datatypes/vec_col_mat/maxon.Col3.md#module-maxon.Col3)([r, g, b]) | Initializes a new three component color. |
| [`Color32`](../../maxon_generated/datatypes/vec_col_mat/maxon.Color32.md#module-maxon.Color32)([r, g, b]) | Initializes a new three component color. |
| [`Color64`](../../maxon_generated/datatypes/vec_col_mat/maxon.Color64.md#module-maxon.Color64)([r, g, b]) | Initializes a new three component color. |
| [`Color`](../../maxon_generated/datatypes/vec_col_mat/maxon.Color.md#module-maxon.Color) | alias of `maxon.vector.Color64` |
| [`Vec4`](../../maxon_generated/datatypes/vec_col_mat/maxon.Vec4.md#module-maxon.Vec4)([x, y, z, w]) | Initializes a new four component vector. |
| [`Vector4d32`](../../maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.md#module-maxon.Vector4d32)([x, y, z, w]) | Initializes a new four component vector. |
| [`Vector4d64`](../../maxon_generated/datatypes/vec_col_mat/maxon.Vector4d64.md#module-maxon.Vector4d64)([x, y, z, w]) | Initializes a new four component vector. |
| [`Vector4d`](../../maxon_generated/datatypes/vec_col_mat/maxon.Vector4d.md#module-maxon.Vector4d) | alias of `maxon.vector4d.Vector4d64` |
| [`ColorA32`](../../maxon_generated/datatypes/vec_col_mat/maxon.ColorA32.md#module-maxon.ColorA32)([r, g, b, a]) | Initializes a new four component color. |
| [`ColorA64`](../../maxon_generated/datatypes/vec_col_mat/maxon.ColorA64.md#module-maxon.ColorA64)([r, g, b, a]) | Initializes a new four component color. |
| [`ColorA`](../../maxon_generated/datatypes/vec_col_mat/maxon.ColorA.md#module-maxon.ColorA) | alias of `maxon.vector4d.ColorA64` |
| [`SqMat3_32`](../../maxon_generated/datatypes/vec_col_mat/maxon.SqMat3_32.md#module-maxon.SqMat3_32)([v1_in, v2_in, v3_in]) | Initializes a new three components square matrix. |
| [`SqMat3_64`](../../maxon_generated/datatypes/vec_col_mat/maxon.SqMat3_64.md#module-maxon.SqMat3_64)([v1_in, v2_in, v3_in]) | Initializes a new three components square matrix. |
| [`SqMat3`](../../maxon_generated/datatypes/vec_col_mat/maxon.SqMat3.md#module-maxon.SqMat3)([v1_in, v2_in, v3_in]) | A 3x3 matrix |
| [`Matrix32`](../../maxon_generated/datatypes/vec_col_mat/maxon.Matrix32.md#module-maxon.Matrix32)([off_in, v1_or_sqmat_in, v2_in, v3_in]) | A 32 bits 3x3 matrix. |
| [`Matrix64`](../../maxon_generated/datatypes/vec_col_mat/maxon.Matrix64.md#module-maxon.Matrix64)([off_in, v1_or_sqmat_in, v2_in, v3_in]) | A 64 bits 3x3 matrix. |
| [`Matrix`](../../maxon_generated/datatypes/vec_col_mat/maxon.Matrix.md#module-maxon.Matrix) | Alias for [`maxon.Matrix64`](../../maxon_generated/datatypes/vec_col_mat/maxon.Matrix64.md#module-maxon.Matrix64) |

### Collection Data Type <a id="collection-data-type"></a>

|   |   |
|---|---|
| [`Array`](../../maxon_generated/datatypes/collection/maxon.Array.md#module-maxon.Array)([ob, input, count]) | Initialize the Array in order to store a given type. At the moment only maxon Data Type are supported. |
| [`BaseArray`](../../maxon_generated/datatypes/collection/maxon.BaseArray.md#module-maxon.BaseArray)([ob, input, count]) | A generic array class template used to stored any kind of data. |
| [`Pair`](../../maxon_generated/datatypes/collection/maxon.Pair.md#module-maxon.Pair)(typename) | [`maxon.Pair`](../../maxon_generated/datatypes/collection/maxon.Pair.md#module-maxon.Pair) provides in-place static storage for elements of arbitrary types. |
| [`Tuple`](../../maxon_generated/datatypes/collection/maxon.Tuple.md#module-maxon.Tuple)(typename) | [`maxon.Tuple`](../../maxon_generated/datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) provides in-place static storage for elements of arbitrary types. |
| [`Block`](../../maxon_generated/datatypes/collection/maxon.Block.md#module-maxon.Block)([C]) | A [`maxon.Block`](../../maxon_generated/datatypes/collection/maxon.Block.md#module-maxon.Block) stands for a number of elements with a regular memory layout. |
| [`StridedBlock`](../../maxon_generated/datatypes/collection/maxon.StridedBlock.md#module-maxon.StridedBlock)([C]) | Similar to a [`maxon.Block`](../../maxon_generated/datatypes/collection/maxon.Block.md#module-maxon.Block). |

### Id Data Type <a id="id-data-type"></a>

|   |   |
|---|---|
| [`InternedId`](../../maxon_generated/datatypes/id/maxon.InternedId.md#module-maxon.InternedId)([C]) | [`maxon.InternedId`](../../maxon_generated/datatypes/id/maxon.InternedId.md#module-maxon.InternedId) represents an [`maxon.Id`](../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id) which has been interned into a pool of unique |
| [`Id`](../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id)([C]) | [`maxon.Id`](../../maxon_generated/datatypes/id/maxon.Id.md#module-maxon.Id) represents an identifier consisting of a c-string. |

### Time Data Type <a id="time-data-type"></a>

|   |   |
|---|---|
| [`LocalDateTime`](../../maxon_generated/datatypes/time/maxon.LocalDateTime.md#module-maxon.LocalDateTime)([C]) | At some point developers have to deal with times, dates and timezones. |
| [`UniversalDateTime`](../../maxon_generated/datatypes/time/maxon.UniversalDateTime.md#module-maxon.UniversalDateTime)([C]) | Class that represents the Universal date-time (UTC+0000). |
| [`TimeValue`](../../maxon_generated/datatypes/time/maxon.TimeValue.md#module-maxon.TimeValue)(seconds) | The [`maxon.TimeValue`](../../maxon_generated/datatypes/time/maxon.TimeValue.md#module-maxon.TimeValue) class encapsulates a timer value. |
| [`Seconds`](../../maxon_generated/datatypes/time/maxon.Seconds.md#module-maxon.Seconds)(seconds) | Timer value in seconds. |

### Core Data Type <a id="core-data-type"></a>

|   |   |
|---|---|
| [`ConfigInit`](../../maxon_generated/datatypes/core/maxon.ConfigInit.md#module-maxon.ConfigInit)([C]) | Represents an config entry value. |
| [`SourceLocation`](../../maxon_generated/datatypes/core/maxon.SourceLocation.md#module-maxon.SourceLocation)([f, line]) | An object to represents the current file location. |
| [`DelegateBase`](../../maxon_generated/datatypes/core/maxon.DelegateBase.md#module-maxon.DelegateBase)([C]) | Delegate base class which can be used for [`maxon.DataType`](../../maxon_generated/datatypes/base_core/maxon.DataType.md#module-maxon.DataType). |

### Core Iterator Data Type <a id="core-iterator-data-type"></a>

|   |   |
|---|---|
| [`PlainIterator`](../../maxon_generated/datatypes/core_iterator/maxon.PlainIterator.md#module-maxon.PlainIterator)([C]) | Base class for iterator |
| [`RegistryEntryIteratorInterface`](../../maxon_generated/datatypes/core_iterator/maxon.RegistryEntryIteratorInterface.md#module-maxon.RegistryEntryIteratorInterface)([C]) | RegistryEntryIteratorInterface is used internally by `Registry.Iterator()`. |
| [`DataDictionaryIteratorInterface`](../../maxon_generated/datatypes/core_iterator/maxon.DataDictionaryIteratorInterface.md#module-maxon.DataDictionaryIteratorInterface)(memory) | [`maxon.DataDictionaryIteratorInterface`](../../maxon_generated/datatypes/core_iterator/maxon.DataDictionaryIteratorInterface.md#module-maxon.DataDictionaryIteratorInterface) is used internally by `DataDictionary.Iterator()`. |
| [`DataDictionaryIterator`](../../maxon_generated/datatypes/core_iterator/maxon.DataDictionaryIterator.md#module-maxon.DataDictionaryIterator)(dict, end) | Iterator to iterate through all elements of a [`maxon.DataDictionaryIterator`](../../maxon_generated/datatypes/core_iterator/maxon.DataDictionaryIterator.md#module-maxon.DataDictionaryIterator). |
| [`IoBrowseIterator`](../../maxon_generated/datatypes/core_iterator/maxon.IoBrowseIterator.md#module-maxon.IoBrowseIterator)(iteratorObject) | Represents a python iterator for an [`maxon.IoBrowseInterface`](../../maxon_generated/interfaces/io/maxon.IoBrowseInterface.md#module-maxon.IoBrowseInterface) |

### Base Core Data Type <a id="base-core-data-type"></a>

|   |   |
|---|---|
| [`Data`](../../maxon_generated/datatypes/base_core/maxon.Data.md#module-maxon.Data)([C]) | An object of this class can store every type of data as long as that type has been registered (see [`maxon.DataType`](../../maxon_generated/datatypes/base_core/maxon.DataType.md#module-maxon.DataType)). |
| [`DataType`](../../maxon_generated/datatypes/base_core/maxon.DataType.md#module-maxon.DataType)(dt) | [`maxon.DataType`](../../maxon_generated/datatypes/base_core/maxon.DataType.md#module-maxon.DataType) provides a set of functions which allow to operate on values of arbitrary |
| [`Ref`](../../maxon_generated/datatypes/base_core/maxon.Ref.md#module-maxon.Ref)() | Base reference for all objects which hold a data capsule |
| [`Struct`](../../maxon_generated/datatypes/base_core/maxon.Struct.md#module-maxon.Struct)() | Represents a C++ structure. |
| [`Builtin`](../../maxon_generated/datatypes/base_core/maxon.Builtin.md#module-maxon.Builtin)([C]) | Represents a built-in [`maxon.DataType`](../../maxon_generated/datatypes/base_core/maxon.DataType.md#module-maxon.DataType) (aka the one that can e converted automatically to python like [`maxon.Int32`](../../maxon_generated/datatypes/simple/maxon.Int32.md#module-maxon.Int32) to int) |
| [`UnknownDataType`](../../maxon_generated/datatypes/base_core/maxon.UnknownDataType.md#module-maxon.UnknownDataType)([C]) | Class for all data objects, that have no proper wrapper class in Python. |
| [`Declaration`](../../maxon_generated/datatypes/base_core/maxon.Declaration.md#module-maxon.Declaration)(ids[, entityBaseType, returnType]) | Maxon API rely on object that are declared. Such object are stored under a [`maxon.Declaration`](../../maxon_generated/datatypes/base_core/maxon.Declaration.md#module-maxon.Declaration) object. |
| [`Generic`](../../maxon_generated/datatypes/base_core/maxon.Generic.md#module-maxon.Generic)([C]) | The data type represents the [`maxon.Generic`](../../maxon_generated/datatypes/base_core/maxon.Generic.md#module-maxon.Generic) type. |
| [`Component`](../../maxon_generated/datatypes/base_core/maxon.Component.md#maxon.Component)(*INTERFACES) | A component implements the functions of a given interface. |
| [`ComponentRoot`](../../maxon_generated/datatypes/base_core/maxon.ComponentRoot.md#module-maxon.ComponentRoot)([data]) | [`maxon.ComponentRoot`](../../maxon_generated/datatypes/base_core/maxon.ComponentRoot.md#module-maxon.ComponentRoot) is the base class of all components (see [`maxon.MAXON_COMPONENT`](../../maxon_generated/decorators/registry/maxon.MAXON_COMPONENT.md#maxon.MAXON_COMPONENT)). |
| [`ObjectDefinition`](../../maxon_generated/datatypes/base_core/maxon.ObjectDefinition.md#module-maxon.ObjectDefinition)(iid, object) | Represent an Object |

## Registries and Enums <a id="registries-and-enums"></a>

### Registries <a id="registries"></a>

|   |   |
|---|---|
| [`Classes`](../../maxon_generated/registries/maxon.Classes.md#module-maxon.Classes)() |  |
| [`Loggers`](../../maxon_generated/registries/maxon.Loggers.md#module-maxon.Loggers)() |  |
| [`LoggerTypes`](../../maxon_generated/registries/maxon.LoggerTypes.md#module-maxon.LoggerTypes)() |  |
| [`IoHandlers`](../../maxon_generated/registries/maxon.IoHandlers.md#module-maxon.IoHandlers)() |  |
| [`FileFormats`](../../maxon_generated/registries/maxon.FileFormats.md#module-maxon.FileFormats)() |  |
| [`FileFormatHandlers`](../../maxon_generated/registries/maxon.FileFormatHandlers.md#module-maxon.FileFormatHandlers)() |  |
| [`ParametricTypes`](../../maxon_generated/registries/maxon.ParametricTypes.md#module-maxon.ParametricTypes)() | Registry of all Parametric Types. |
| [`DataTypes`](../../maxon_generated/registries/maxon.DataTypes.md#module-maxon.DataTypes)() |  |

## Decorators <a id="decorators"></a>

As a 3rd party developer you normally don’t have to deal with decorators.  
This is used only to exposes C++ MAXON API Component to Python.

### Interface Decorator <a id="interface-decorator"></a>

|   |   |
|---|---|
| [`MAXON_INTERFACE`](../../maxon_generated/decorators/interface/maxon.MAXON_INTERFACE.md#maxon.MAXON_INTERFACE)(REFKIND, ID[, doObjectCheck]) |  |
| [`MAXON_INTERFACE_REFERENCE`](../../maxon_generated/decorators/interface/maxon.MAXON_INTERFACE_REFERENCE.md#maxon.MAXON_INTERFACE_REFERENCE)() | Decorator to defines an Interface that can be treated as Reference at the same time. |
| [`MAXON_INTERFACE_NONVIRTUAL`](../../maxon_generated/decorators/interface/maxon.MAXON_INTERFACE_NONVIRTUAL.md#maxon.MAXON_INTERFACE_NONVIRTUAL)(REFKIND, ID) |  |
| [`MAXON_STATICMETHOD`](../../maxon_generated/decorators/interface/maxon.MAXON_STATICMETHOD.md#maxon.MAXON_STATICMETHOD)(identifier[, returnType, …]) |  |
| [`MAXON_METHOD`](../../maxon_generated/decorators/interface/maxon.MAXON_METHOD.md#maxon.MAXON_METHOD)([identifier, returnType, …]) |  |
| [`MAXON_FUNCTION`](../../maxon_generated/decorators/interface/maxon.MAXON_FUNCTION.md#maxon.MAXON_FUNCTION)(identifier) | At the moment MAXON_FUNCTION is just a dummy function to mark the function that it is trampolin code to another function. |
| [`MAXON_STATICFUNCTION`](../../maxon_generated/decorators/interface/maxon.MAXON_STATICFUNCTION.md#maxon.MAXON_STATICFUNCTION)(identifier) | At the moment MAXON_STATICFUNCTION is just a dummy function to mark the function that it is trampolin code to another function. |
| [`MAXON_OVERLOAD`](../../maxon_generated/decorators/interface/maxon.MAXON_OVERLOAD.md#maxon.MAXON_OVERLOAD)() | At the moment MAXON_OVERLOAD is just a dummy function to mark a function being overloaded |
| [`MAXON_FUNCTION_EXTEND`](../../maxon_generated/decorators/interface/maxon.MAXON_FUNCTION_EXTEND.md#maxon.MAXON_FUNCTION_EXTEND)(identifier) | At the moment MAXON_FUNCTION_EXTEND is just a dummy function to mark the function that it is trampolin code to another function. |
| [`MAXON_REFERENCE`](../../maxon_generated/decorators/interface/maxon.MAXON_REFERENCE.md#maxon.MAXON_REFERENCE)(SUPERCLASS) |  |

### Enum Decorator <a id="enum-decorator"></a>

|   |   |
|---|---|
| [`MAXON_ENUM_FLAGS`](../../maxon_generated/decorators/enum/maxon.MAXON_ENUM_FLAGS.md#maxon.MAXON_ENUM_FLAGS)(classId[, className]) |  |
| [`MAXON_ENUM_LIST`](../../maxon_generated/decorators/enum/maxon.MAXON_ENUM_LIST.md#maxon.MAXON_ENUM_LIST)(classId[, className]) |  |

### Registration Decorator <a id="registration-decorator"></a>

|   |   |
|---|---|
| [`MAXON_COMPONENT`](../../maxon_generated/decorators/registry/maxon.MAXON_COMPONENT.md#maxon.MAXON_COMPONENT)([kind]) | Decorator to mark an element as a Maxon API component (available from a registry) |
| [`MAXON_COMPONENT_OBJECT_REGISTER`](../../maxon_generated/decorators/registry/maxon.MAXON_COMPONENT_OBJECT_REGISTER.md#maxon.MAXON_COMPONENT_OBJECT_REGISTER)(impl, …[, …]) | MAXON_COMPONENT_OBJECT_REGISTER registers a component, creates an object class which uses the component and |
| [`MAXON_COMPONENT_CLASS_REGISTER`](../../maxon_generated/decorators/registry/maxon.MAXON_COMPONENT_CLASS_REGISTER.md#maxon.MAXON_COMPONENT_CLASS_REGISTER)(impl, …[, …]) | MAXON_COMPONENT_OBJECT_REGISTER registers a component, creates an object class which uses the component and |
| [`MAXON_REGISTRY`](../../maxon_generated/decorators/registry/maxon.MAXON_REGISTRY.md#maxon.MAXON_REGISTRY)(ids[, returnType]) |  |

## Functions <a id="functions"></a>

### Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`maxon.finally_once`](../../maxon_generated/functions/maxon.finally_once.md#maxon.finally_once)(func, *args, **kwargs) | Executes a function when the current scope is left. |
| [`maxon.MAXON_SOURCE_LOCATION`](../../maxon_generated/functions/maxon.MAXON_SOURCE_LOCATION.md#maxon.MAXON_SOURCE_LOCATION)([offset]) | Creates a SourceLocation object for the current Python Frame. |
| [`maxon.MAXON_ATTRIBUTE`](../../maxon_generated/functions/maxon.MAXON_ATTRIBUTE.md#maxon.MAXON_ATTRIBUTE)(id) | Alias for [`maxon.InternedId`](../../maxon_generated/datatypes/id/maxon.InternedId.md#module-maxon.InternedId). |
| [`maxon.GetDataType`](../../maxon_generated/functions/maxon.GetDataType.md#maxon.GetDataType)(obj) | Retrieves the [`maxon.DataType`](../../maxon_generated/datatypes/base_core/maxon.DataType.md#module-maxon.DataType) of the passed object. |
| [`maxon.MaxonConvert`](../../maxon_generated/functions/maxon.MaxonConvert.md#maxon.MaxonConvert)(*args) | Convert all passed objects to a maxon or Python object, depending on the passed type. |
| [`maxon.ToBlock`](../../maxon_generated/functions/maxon.ToBlock.md#maxon.ToBlock)(data, size[, stride, dt]) | Makes a [`maxon.Block`](../../maxon_generated/datatypes/collection/maxon.Block.md#module-maxon.Block) or a [`maxon.StridedBlock`](../../maxon_generated/datatypes/collection/maxon.StridedBlock.md#module-maxon.StridedBlock) from a pointer, a size and a stride. |
| [`maxon.Cast`](../../maxon_generated/functions/maxon.Cast.md#maxon.Cast)(T, o) | Cast the object *o* to the type *T*. |
| [`maxon.reinterpret_cast`](../../maxon_generated/functions/maxon.reinterpret_cast.md#maxon.reinterpret_cast)(T, o) | Cast(T, o) Cast the object *o* to the type *T*. |

### Methods Definition <a id="methods-definition"></a>

#### `maxon.finally_once(func, *args, **kwargs)`

Executes a function when the current scope is left.

> **Note:** An optional parameter *canRaise* can be passed to notify that *func* may eventually raise.

**Parameters:**

- **func** (`function(*args, **kwargs)`) – Function to be called.
- **args** (*Any*) – Optional arguments to be passed to func.
- **kwargs** (*Any*) – Optional settings like *canRaise* to control if *func* can raise an exception.

```python
cleanup = finally_once(lambda x: MyFunction(x), canRaise=False)
```

#### `maxon.MAXON_SOURCE_LOCATION(offset=0)`

Creates a SourceLocation object for the current Python Frame.

**Parameters:** **offset** (*Optional*[*int*])) – Optional trace back offset to retrieve the current source location from.

**Returns:** The source location corresponding to the Python frame calling this function.

**Return type:** [`maxon.SourceLocation`](../../maxon_generated/datatypes/core/maxon.SourceLocation.md#module-maxon.SourceLocation)

#### `maxon.MAXON_ATTRIBUTE(id)`

Alias for [`maxon.InternedId`](../../maxon_generated/datatypes/id/maxon.InternedId.md#module-maxon.InternedId).

#### `maxon.GetDataType(obj)`

Retrieves the [`maxon.DataType`](../../maxon_generated/datatypes/base_core/maxon.DataType.md#module-maxon.DataType) of the passed object.

**Parameters:** **type** – The object to retrieves the [`maxon.DataType`](../../maxon_generated/datatypes/base_core/maxon.DataType.md#module-maxon.DataType) from.

**Type:** [`maxon.Data`](../../maxon_generated/datatypes/base_core/maxon.Data.md#module-maxon.Data)

**Returns:** The datatype.

**Return type:** [`maxon.DataType`](../../maxon_generated/datatypes/base_core/maxon.DataType.md#module-maxon.DataType)

#### `maxon.MaxonConvert(*args)`

Convert all passed objects to a maxon or Python object, depending on the passed type.

> **Note:** Latest arguments determine how the conversion is done by passing a `maxon.CONVERSIONMODE`.

```python
import maxon

# Returns a maxon.Int32 of value 10
print maxon.MaxonConvert(10)

# Returns a int of value 10
print maxon.MaxonConvert(maxon.Int(10))

# Forces a return value to Maxon API type, in this case a maxon.Int32 of value 10
print maxon.MaxonConvert(maxon.Int(10), maxon.CONVERSIONMODE.TOMAXON)

# Forces a return value to Python Builtin, in this case a int of value 10
print maxon.MaxonConvert(10, maxon.CONVERSIONMODE.TOBUILTIN)
```

**Parameters:** **args** (*Any*) – The object to converts.

**Returns:** The object converted

**Return type:** Any

#### `maxon.ToBlock(data, size, stride=None, dt=None)`

Makes a [`maxon.Block`](../../maxon_generated/datatypes/collection/maxon.Block.md#module-maxon.Block) or a [`maxon.StridedBlock`](../../maxon_generated/datatypes/collection/maxon.StridedBlock.md#module-maxon.StridedBlock) from a pointer, a size and a stride.

**Parameters:**

- **data** ([`maxon.Data`](../../maxon_generated/datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The data to transform to a Block.
- **size** (*int*) – Number of elements.
- **stride** (*int*) – Element stride.
- **dt** ([`maxon.DataType`](../../maxon_generated/datatypes/base_core/maxon.DataType.md#module-maxon.DataType)) – The Datatype of the data to be converted as block

**Returns:** A block of elements for this data and datatype.

**Return type:** Union[[`maxon.StridedBlock`](../../maxon_generated/datatypes/collection/maxon.StridedBlock.md#module-maxon.StridedBlock), [`maxon.Block`](../../maxon_generated/datatypes/collection/maxon.Block.md#module-maxon.Block)]

#### `maxon.Cast(T, o)`

Cast the object *o* to the type *T*.

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.  
> Use [`maxon.MaxonConvert()`](../../maxon_generated/functions/maxon.MaxonConvert.md#maxon.MaxonConvert) instead.

**Parameters:**

- **T** (*type*) – The type to cast the object to.
- **o** ([`maxon.Data`](../../maxon_generated/datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The Initial object

**Returns:** The casted object

**Return type:** T

#### `maxon.reinterpret_cast(T, o)`

Cast(T, o) Cast the object *o* to the type *T*.

> **Warning:**
>
> This function is only there to expose a C++ Object to Python.  
> As a Python developer you normally don’t have to deal with this function.  
> Use [`maxon.MaxonConvert()`](../../maxon_generated/functions/maxon.MaxonConvert.md#maxon.MaxonConvert) instead.

**Parameters:**

- **T** (*type*) – The type to cast the object to.
- **o** ([`maxon.Data`](../../maxon_generated/datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The Initial object

**Returns:** The casted object

**Return type:** T
