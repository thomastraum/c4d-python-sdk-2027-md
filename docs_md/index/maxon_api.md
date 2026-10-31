# Maxon API Reference

> Frameworks, interfaces, data types, and enums of the `maxon` package.


## modules/maxon/frameworks

- [maxon.frameworks.animation](../modules/maxon/frameworks/animation.md): Module for Weight Manager algorithms.
- [maxon.frameworks.asset](../modules/maxon/frameworks/asset.md): Module for interacting with assets.
- [maxon.frameworks.cinema_hybrid](../modules/maxon/frameworks/cinema_hybrid.md)
- [maxon](../modules/maxon/frameworks/core.md): Module for fundamental Maxon API types and operations.
- [maxon.frameworks.graph](../modules/maxon/frameworks/graph.md): Module for graph structures.
- [maxon.frameworks.mesh_misc](../modules/maxon/frameworks/mesh_misc.md): Module for mesh attributes.
- [maxon.frameworks.misc](../modules/maxon/frameworks/misc.md): Module for miscellaneous utilities.
- [maxon.frameworks.nodes](../modules/maxon/frameworks/nodes.md)
- [maxon.frameworks.nodespace](../modules/maxon/frameworks/nodespace.md)
- [maxon.frameworks.render_filter](../modules/maxon/frameworks/render_filter.md): Module for render filters.
- [maxon.frameworks.volume](../modules/maxon/frameworks/volume.md)

## modules/maxon

- [Maxon API](../modules/maxon/maxon_api.md)

## modules/maxon_generated/datatypes/base_core

- [maxon.Builtin](../modules/maxon_generated/datatypes/base_core/maxon.Builtin.md): Represents a built-in maxon.DataType (aka the one that can e converted automatically to python like maxon.Int32 to int)
- [maxon.Component](../modules/maxon_generated/datatypes/base_core/maxon.Component.md)
- [maxon.ComponentRoot](../modules/maxon_generated/datatypes/base_core/maxon.ComponentRoot.md)
- [maxon.Data](../modules/maxon_generated/datatypes/base_core/maxon.Data.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.DataType](../modules/maxon_generated/datatypes/base_core/maxon.DataType.md): Each type needs its own maxon.DataType with specific implementations of the access functions.
- [maxon.Declaration](../modules/maxon_generated/datatypes/base_core/maxon.Declaration.md)
- [maxon.Generic](../modules/maxon_generated/datatypes/base_core/maxon.Generic.md): The data type represents the maxon.Generic type.
- [maxon.ObjectDefinition](../modules/maxon_generated/datatypes/base_core/maxon.ObjectDefinition.md)
- [maxon.Ref](../modules/maxon_generated/datatypes/base_core/maxon.Ref.md): Base reference for all objects which hold a data capsule
- [maxon.Struct](../modules/maxon_generated/datatypes/base_core/maxon.Struct.md): Represents a C++ structure.
- [maxon.UnknownDataType](../modules/maxon_generated/datatypes/base_core/maxon.UnknownDataType.md): Class for all data objects, that have no proper wrapper class in Python.

## modules/maxon_generated/datatypes/collection

- [maxon.Array](../modules/maxon_generated/datatypes/collection/maxon.Array.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.BaseArray](../modules/maxon_generated/datatypes/collection/maxon.BaseArray.md): A generic array class template used to stored any kind of data.
- [maxon.Block](../modules/maxon_generated/datatypes/collection/maxon.Block.md)
- [maxon.Pair](../modules/maxon_generated/datatypes/collection/maxon.Pair.md)
- [maxon.StridedBlock](../modules/maxon_generated/datatypes/collection/maxon.StridedBlock.md): Similar to a maxon.Block.
- [maxon.Tuple](../modules/maxon_generated/datatypes/collection/maxon.Tuple.md)

## modules/maxon_generated/datatypes/core

- [maxon.ConfigInit.CONFIGURATION_DATATYPE_BOOL](../modules/maxon_generated/datatypes/core/maxon.ConfigInit.CONFIGURATION_DATATYPE_BOOL.md)
- [maxon.ConfigInit.CONFIGURATION_DATATYPE_FLOAT](../modules/maxon_generated/datatypes/core/maxon.ConfigInit.CONFIGURATION_DATATYPE_FLOAT.md)
- [maxon.ConfigInit.CONFIGURATION_DATATYPE_INT](../modules/maxon_generated/datatypes/core/maxon.ConfigInit.CONFIGURATION_DATATYPE_INT.md)
- [maxon.ConfigInit.CONFIGURATION_DATATYPE_STRING](../modules/maxon_generated/datatypes/core/maxon.ConfigInit.CONFIGURATION_DATATYPE_STRING.md)
- [maxon.ConfigInit.CONFIGURATION_DATATYPE_STRING_C](../modules/maxon_generated/datatypes/core/maxon.ConfigInit.CONFIGURATION_DATATYPE_STRING_C.md)
- [maxon.ConfigInit.default](../modules/maxon_generated/datatypes/core/maxon.ConfigInit.default.md)
- [maxon.ConfigInit.helpText](../modules/maxon_generated/datatypes/core/maxon.ConfigInit.helpText.md)
- [maxon.ConfigInit.key](../modules/maxon_generated/datatypes/core/maxon.ConfigInit.key.md)
- [maxon.ConfigInit.maxValue](../modules/maxon_generated/datatypes/core/maxon.ConfigInit.maxValue.md)
- [maxon.ConfigInit](../modules/maxon_generated/datatypes/core/maxon.ConfigInit.md): Represents an config entry value.
- [maxon.ConfigInit.minValue](../modules/maxon_generated/datatypes/core/maxon.ConfigInit.minValue.md)
- [maxon.ConfigInit.type](../modules/maxon_generated/datatypes/core/maxon.ConfigInit.type.md)
- [maxon.ConfigInit.value](../modules/maxon_generated/datatypes/core/maxon.ConfigInit.value.md)
- [maxon.DelegateBase](../modules/maxon_generated/datatypes/core/maxon.DelegateBase.md): Delegate base class which can be used for maxon.DataType.
- [maxon.SourceLocation.file](../modules/maxon_generated/datatypes/core/maxon.SourceLocation.file.md)
- [maxon.SourceLocation.lineAndFlags](../modules/maxon_generated/datatypes/core/maxon.SourceLocation.lineAndFlags.md)
- [maxon.SourceLocation](../modules/maxon_generated/datatypes/core/maxon.SourceLocation.md): An object to represents the current file location.

## modules/maxon_generated/datatypes/core_iterator

- [maxon.DataDictionaryIterator](../modules/maxon_generated/datatypes/core_iterator/maxon.DataDictionaryIterator.md): Iterator to iterate through all elements of a maxon.DataDictionaryIterator.
- [maxon.DataDictionaryIteratorInterface](../modules/maxon_generated/datatypes/core_iterator/maxon.DataDictionaryIteratorInterface.md): maxon.DataDictionaryIteratorInterface is used internally by DataDictionary.Iterator().
- [maxon.IoBrowseIterator](../modules/maxon_generated/datatypes/core_iterator/maxon.IoBrowseIterator.md): Represents a python iterator for an maxon.IoBrowseInterface
- [maxon.PlainIterator](../modules/maxon_generated/datatypes/core_iterator/maxon.PlainIterator.md)
- [maxon.RegistryEntryIteratorInterface](../modules/maxon_generated/datatypes/core_iterator/maxon.RegistryEntryIteratorInterface.md): RegistryEntryIteratorInterface is used internally by Registry.Iterator().

## modules/maxon_generated/datatypes/id

- [maxon.Id](../modules/maxon_generated/datatypes/id/maxon.Id.md): maxon.Id represents an identifier consisting of a c-string.
- [maxon.InternedId](../modules/maxon_generated/datatypes/id/maxon.InternedId.md): I.e., there are no two different Id objects with an equal id string, so for equality comparison you can compare pointers instead of whole strings.

## modules/maxon_generated/datatypes/simple

- [maxon.Bool](../modules/maxon_generated/datatypes/simple/maxon.Bool.md): Boolean type, possible values are only False/True, 8 bits.
- [maxon.Char.MAX](../modules/maxon_generated/datatypes/simple/maxon.Char.MAX.md)
- [maxon.Char.MIN](../modules/maxon_generated/datatypes/simple/maxon.Char.MIN.md)
- [maxon.Char](../modules/maxon_generated/datatypes/simple/maxon.Char.md)
- [maxon.Float.MAX](../modules/maxon_generated/datatypes/simple/maxon.Float.MAX.md)
- [maxon.Float.MIN](../modules/maxon_generated/datatypes/simple/maxon.Float.MIN.md)
- [maxon.Float.SIZEOF](../modules/maxon_generated/datatypes/simple/maxon.Float.SIZEOF.md)
- [maxon.Float](../modules/maxon_generated/datatypes/simple/maxon.Float.md): Floating point value 64 bits (double).
- [maxon.Float32.MAX](../modules/maxon_generated/datatypes/simple/maxon.Float32.MAX.md)
- [maxon.Float32.MIN](../modules/maxon_generated/datatypes/simple/maxon.Float32.MIN.md)
- [maxon.Float32](../modules/maxon_generated/datatypes/simple/maxon.Float32.md): Floating point value 32 bits (float).
- [maxon.Float64.MAX](../modules/maxon_generated/datatypes/simple/maxon.Float64.MAX.md)
- [maxon.Float64.MIN](../modules/maxon_generated/datatypes/simple/maxon.Float64.MIN.md)
- [maxon.Float64.SIZEOF](../modules/maxon_generated/datatypes/simple/maxon.Float64.SIZEOF.md)
- [maxon.Float64](../modules/maxon_generated/datatypes/simple/maxon.Float64.md): Floating point value 64 bits (double).
- [maxon.Int.MAX](../modules/maxon_generated/datatypes/simple/maxon.Int.MAX.md)
- [maxon.Int.MIN](../modules/maxon_generated/datatypes/simple/maxon.Int.MIN.md)
- [maxon.Int.SIZEOF](../modules/maxon_generated/datatypes/simple/maxon.Int.SIZEOF.md)
- [maxon.Int](../modules/maxon_generated/datatypes/simple/maxon.Int.md): Signed integer 64 bits (either positive or negative number).
- [maxon.Int16.MAX](../modules/maxon_generated/datatypes/simple/maxon.Int16.MAX.md)
- [maxon.Int16.MIN](../modules/maxon_generated/datatypes/simple/maxon.Int16.MIN.md)
- [maxon.Int16](../modules/maxon_generated/datatypes/simple/maxon.Int16.md): Signed integer 16 bits (either positive or negative number).
- [maxon.Int32.MAX](../modules/maxon_generated/datatypes/simple/maxon.Int32.MAX.md)
- [maxon.Int32.MIN](../modules/maxon_generated/datatypes/simple/maxon.Int32.MIN.md)
- [maxon.Int32](../modules/maxon_generated/datatypes/simple/maxon.Int32.md): Signed integer 32 bits (either positive or negative number).
- [maxon.Int64.MAX](../modules/maxon_generated/datatypes/simple/maxon.Int64.MAX.md)
- [maxon.Int64.MIN](../modules/maxon_generated/datatypes/simple/maxon.Int64.MIN.md)
- [maxon.Int64.SIZEOF](../modules/maxon_generated/datatypes/simple/maxon.Int64.SIZEOF.md)
- [maxon.Int64](../modules/maxon_generated/datatypes/simple/maxon.Int64.md): Signed integer 64 bits (either positive or negative number).
- [maxon.UChar.MAX](../modules/maxon_generated/datatypes/simple/maxon.UChar.MAX.md)
- [maxon.UChar.MIN](../modules/maxon_generated/datatypes/simple/maxon.UChar.MIN.md)
- [maxon.UChar](../modules/maxon_generated/datatypes/simple/maxon.UChar.md): Unsigned 8 bits character.
- [maxon.UInt.MAX](../modules/maxon_generated/datatypes/simple/maxon.UInt.MAX.md)
- [maxon.UInt.MIN](../modules/maxon_generated/datatypes/simple/maxon.UInt.MIN.md)
- [maxon.UInt.SIZEOF](../modules/maxon_generated/datatypes/simple/maxon.UInt.SIZEOF.md)
- [maxon.UInt](../modules/maxon_generated/datatypes/simple/maxon.UInt.md): Unsigned integer 64 bits (always positive number).
- [maxon.UInt16.MAX](../modules/maxon_generated/datatypes/simple/maxon.UInt16.MAX.md)
- [maxon.UInt16.MIN](../modules/maxon_generated/datatypes/simple/maxon.UInt16.MIN.md)
- [maxon.UInt16](../modules/maxon_generated/datatypes/simple/maxon.UInt16.md): Unsigned integer 16 bits (always positive number).
- [maxon.UInt32.MAX](../modules/maxon_generated/datatypes/simple/maxon.UInt32.MAX.md)
- [maxon.UInt32.MIN](../modules/maxon_generated/datatypes/simple/maxon.UInt32.MIN.md)
- [maxon.UInt32](../modules/maxon_generated/datatypes/simple/maxon.UInt32.md): Unsigned integer 32 bits (always positive number).
- [maxon.UInt64.MAX](../modules/maxon_generated/datatypes/simple/maxon.UInt64.MAX.md)
- [maxon.UInt64.MIN](../modules/maxon_generated/datatypes/simple/maxon.UInt64.MIN.md)
- [maxon.UInt64.SIZEOF](../modules/maxon_generated/datatypes/simple/maxon.UInt64.SIZEOF.md)
- [maxon.UInt64](../modules/maxon_generated/datatypes/simple/maxon.UInt64.md): Unsigned integer 64 bits (always positive number).

## modules/maxon_generated/datatypes/time

- [maxon.LocalDateTime](../modules/maxon_generated/datatypes/time/maxon.LocalDateTime.md)
- [maxon.Seconds](../modules/maxon_generated/datatypes/time/maxon.Seconds.md)
- [maxon.TimeValue](../modules/maxon_generated/datatypes/time/maxon.TimeValue.md): The maxon.TimeValue class encapsulates a timer value.
- [maxon.UniversalDateTime](../modules/maxon_generated/datatypes/time/maxon.UniversalDateTime.md)

## modules/maxon_generated/datatypes/vec_col_mat

- [maxon.Col3.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Col3.STRIDE.md)
- [maxon.Col3.b](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Col3.b.md)
- [maxon.Col3.g](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Col3.g.md)
- [maxon.Col3](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Col3.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.Col3.r](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Col3.r.md)
- [maxon.Color.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color.STRIDE.md)
- [maxon.Color.b](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color.b.md)
- [maxon.Color.g](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color.g.md)
- [maxon.Color](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.Color.r](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color.r.md)
- [maxon.Color32.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color32.STRIDE.md)
- [maxon.Color32.b](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color32.b.md)
- [maxon.Color32.g](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color32.g.md)
- [maxon.Color32](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color32.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.Color32.r](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color32.r.md)
- [maxon.Color64.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color64.STRIDE.md)
- [maxon.Color64.b](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color64.b.md)
- [maxon.Color64.g](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color64.g.md)
- [maxon.Color64](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color64.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.Color64.r](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Color64.r.md)
- [maxon.ColorA.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA.STRIDE.md)
- [maxon.ColorA.a](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA.a.md)
- [maxon.ColorA.b](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA.b.md)
- [maxon.ColorA.g](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA.g.md)
- [maxon.ColorA](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.ColorA.r](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA.r.md)
- [maxon.ColorA32.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA32.STRIDE.md)
- [maxon.ColorA32.a](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA32.a.md)
- [maxon.ColorA32.b](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA32.b.md)
- [maxon.ColorA32.g](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA32.g.md)
- [maxon.ColorA32](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA32.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.ColorA32.r](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA32.r.md)
- [maxon.ColorA64.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA64.STRIDE.md)
- [maxon.ColorA64.a](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA64.a.md)
- [maxon.ColorA64.b](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA64.b.md)
- [maxon.ColorA64.g](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA64.g.md)
- [maxon.ColorA64](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA64.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.ColorA64.r](../modules/maxon_generated/datatypes/vec_col_mat/maxon.ColorA64.r.md)
- [maxon.IntVector.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector.STRIDE.md)
- [maxon.IntVector.ValueType](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector.ValueType.md)
- [maxon.IntVector](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector.md): A vector consisting of three components X, Y and Z.
- [maxon.IntVector.x](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector.x.md)
- [maxon.IntVector.y](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector.y.md)
- [maxon.IntVector.z](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector.z.md)
- [maxon.IntVector32.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector32.STRIDE.md)
- [maxon.IntVector32.ValueType](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector32.ValueType.md)
- [maxon.IntVector32](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector32.md): A vector consisting of three components X, Y and Z.
- [maxon.IntVector32.x](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector32.x.md)
- [maxon.IntVector32.y](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector32.y.md)
- [maxon.IntVector32.z](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector32.z.md)
- [maxon.IntVector64.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector64.STRIDE.md)
- [maxon.IntVector64.ValueType](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector64.ValueType.md)
- [maxon.IntVector64](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector64.md): A vector consisting of three components X, Y and Z.
- [maxon.IntVector64.x](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector64.x.md)
- [maxon.IntVector64.y](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector64.y.md)
- [maxon.IntVector64.z](../modules/maxon_generated/datatypes/vec_col_mat/maxon.IntVector64.z.md)
- [maxon.Matrix](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Matrix.md)
- [maxon.Matrix32](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Matrix32.md)
- [maxon.Matrix64](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Matrix64.md)
- [maxon.SqMat3.V](../modules/maxon_generated/datatypes/vec_col_mat/maxon.SqMat3.V.md)
- [maxon.SqMat3](../modules/maxon_generated/datatypes/vec_col_mat/maxon.SqMat3.md)
- [maxon.SqMat3_32](../modules/maxon_generated/datatypes/vec_col_mat/maxon.SqMat3_32.md)
- [maxon.SqMat3_64](../modules/maxon_generated/datatypes/vec_col_mat/maxon.SqMat3_64.md)
- [maxon.Vec3.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vec3.STRIDE.md)
- [maxon.Vec3](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vec3.md): A vector consisting of three components X, Y and Z.
- [maxon.Vec3.x](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vec3.x.md)
- [maxon.Vec3.y](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vec3.y.md)
- [maxon.Vec3.z](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vec3.z.md)
- [maxon.Vec4.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vec4.STRIDE.md)
- [maxon.Vec4](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vec4.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.Vec4.w](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vec4.w.md)
- [maxon.Vec4.x](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vec4.x.md)
- [maxon.Vec4.y](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vec4.y.md)
- [maxon.Vec4.z](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vec4.z.md)
- [maxon.Vector.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector.STRIDE.md)
- [maxon.Vector.ValueType](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector.ValueType.md)
- [maxon.Vector](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector.md): A vector consisting of three components X, Y and Z.
- [maxon.Vector.x](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector.x.md)
- [maxon.Vector.y](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector.y.md)
- [maxon.Vector.z](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector.z.md)
- [maxon.Vector32.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector32.STRIDE.md)
- [maxon.Vector32.ValueType](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector32.ValueType.md)
- [maxon.Vector32](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector32.md): A vector consisting of three components X, Y and Z.
- [maxon.Vector32.x](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector32.x.md)
- [maxon.Vector32.y](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector32.y.md)
- [maxon.Vector32.z](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector32.z.md)
- [maxon.Vector4d.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d.STRIDE.md)
- [maxon.Vector4d.ValueType](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d.ValueType.md)
- [maxon.Vector4d](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.Vector4d.w](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d.w.md)
- [maxon.Vector4d.x](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d.x.md)
- [maxon.Vector4d.y](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d.y.md)
- [maxon.Vector4d.z](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d.z.md)
- [maxon.Vector4d32.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.STRIDE.md)
- [maxon.Vector4d32.ValueType](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.ValueType.md)
- [maxon.Vector4d32](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.Vector4d32.w](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.w.md)
- [maxon.Vector4d32.x](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.x.md)
- [maxon.Vector4d32.y](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.y.md)
- [maxon.Vector4d32.z](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d32.z.md)
- [maxon.Vector4d64.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d64.STRIDE.md)
- [maxon.Vector4d64.ValueType](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d64.ValueType.md)
- [maxon.Vector4d64](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d64.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.Vector4d64.w](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d64.w.md)
- [maxon.Vector4d64.x](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d64.x.md)
- [maxon.Vector4d64.y](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d64.y.md)
- [maxon.Vector4d64.z](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector4d64.z.md)
- [maxon.Vector64.STRIDE](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector64.STRIDE.md)
- [maxon.Vector64.ValueType](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector64.ValueType.md)
- [maxon.Vector64](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector64.md): A vector consisting of three components X, Y and Z.
- [maxon.Vector64.x](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector64.x.md)
- [maxon.Vector64.y](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector64.y.md)
- [maxon.Vector64.z](../modules/maxon_generated/datatypes/vec_col_mat/maxon.Vector64.z.md)

## modules/maxon_generated/decorators/enum

- [maxon.MAXON_ENUM_FLAGS](../modules/maxon_generated/decorators/enum/maxon.MAXON_ENUM_FLAGS.md)
- [maxon.MAXON_ENUM_LIST](../modules/maxon_generated/decorators/enum/maxon.MAXON_ENUM_LIST.md)

## modules/maxon_generated/decorators/interface

- [maxon.MAXON_FUNCTION](../modules/maxon_generated/decorators/interface/maxon.MAXON_FUNCTION.md)
- [maxon.MAXON_FUNCTION_EXTEND](../modules/maxon_generated/decorators/interface/maxon.MAXON_FUNCTION_EXTEND.md)
- [maxon.MAXON_INTERFACE](../modules/maxon_generated/decorators/interface/maxon.MAXON_INTERFACE.md)
- [maxon.MAXON_INTERFACE_NONVIRTUAL](../modules/maxon_generated/decorators/interface/maxon.MAXON_INTERFACE_NONVIRTUAL.md)
- [maxon.MAXON_INTERFACE_REFERENCE](../modules/maxon_generated/decorators/interface/maxon.MAXON_INTERFACE_REFERENCE.md)
- [maxon.MAXON_METHOD](../modules/maxon_generated/decorators/interface/maxon.MAXON_METHOD.md)
- [maxon.MAXON_OVERLOAD](../modules/maxon_generated/decorators/interface/maxon.MAXON_OVERLOAD.md)
- [maxon.MAXON_REFERENCE](../modules/maxon_generated/decorators/interface/maxon.MAXON_REFERENCE.md)
- [maxon.MAXON_STATICFUNCTION](../modules/maxon_generated/decorators/interface/maxon.MAXON_STATICFUNCTION.md)
- [maxon.MAXON_STATICMETHOD](../modules/maxon_generated/decorators/interface/maxon.MAXON_STATICMETHOD.md)

## modules/maxon_generated/decorators/registry

- [maxon.MAXON_COMPONENT](../modules/maxon_generated/decorators/registry/maxon.MAXON_COMPONENT.md)
- [maxon.MAXON_COMPONENT_CLASS_REGISTER](../modules/maxon_generated/decorators/registry/maxon.MAXON_COMPONENT_CLASS_REGISTER.md)
- [maxon.MAXON_COMPONENT_OBJECT_REGISTER](../modules/maxon_generated/decorators/registry/maxon.MAXON_COMPONENT_OBJECT_REGISTER.md)
- [maxon.MAXON_REGISTRY](../modules/maxon_generated/decorators/registry/maxon.MAXON_REGISTRY.md)

## modules/maxon_generated/enums

- [maxon.ANIMATION.AUTOWEIGHT.BASE.ALLOWZEROLENGTH](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BASE.ALLOWZEROLENGTH.md)
- [maxon.ANIMATION.AUTOWEIGHT.BASE.FALLOFFDISTANCE](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BASE.FALLOFFDISTANCE.md)
- [maxon.ANIMATION.AUTOWEIGHT.BASE.GROUP](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BASE.GROUP.md)
- [maxon.ANIMATION.AUTOWEIGHT.BASE.JOINTCOUNT](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BASE.JOINTCOUNT.md)
- [maxon.ANIMATION.AUTOWEIGHT.BASE.SELECTEDPOINTS](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BASE.SELECTEDPOINTS.md)
- [maxon.ANIMATION.AUTOWEIGHT.BASE.SMOOTHGROUP](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BASE.SMOOTHGROUP.md)
- [maxon.ANIMATION.AUTOWEIGHT.BASE.SMOOTHITERATION](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BASE.SMOOTHITERATION.md)
- [maxon.ANIMATION.AUTOWEIGHT.BASE.SMOOTHSTRENGTH](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BASE.SMOOTHSTRENGTH.md)
- [maxon.ANIMATION.AUTOWEIGHT.BASE.STRENGTH](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BASE.STRENGTH.md)
- [maxon.ANIMATION.AUTOWEIGHT.BASE](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BASE.md)
- [maxon.ANIMATION.AUTOWEIGHT.BONEGLOW.GROUP](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BONEGLOW.GROUP.md)
- [maxon.ANIMATION.AUTOWEIGHT.BONEGLOW.IGNOREINNERPOLY](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BONEGLOW.IGNOREINNERPOLY.md)
- [maxon.ANIMATION.AUTOWEIGHT.BONEGLOW.USEVISIBILITY](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BONEGLOW.USEVISIBILITY.md)
- [maxon.ANIMATION.AUTOWEIGHT.BONEGLOW.VISIBILITYRATIO](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BONEGLOW.VISIBILITYRATIO.md)
- [maxon.ANIMATION.AUTOWEIGHT.BONEGLOW](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.BONEGLOW.md)
- [maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW.GROUP](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW.GROUP.md)
- [maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW.IGNOREINNERPOLY](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW.IGNOREINNERPOLY.md)
- [maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW.SIZE](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW.SIZE.md)
- [maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW.USEAUTOVOXELSIZE](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW.USEAUTOVOXELSIZE.md)
- [maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW.USEVISIBILITY](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW.USEVISIBILITY.md)
- [maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW.VISIBILITYRATIO](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW.VISIBILITYRATIO.md)
- [maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW](../modules/maxon_generated/enums/maxon.ANIMATION.AUTOWEIGHT.VOXELBONEGLOW.md)
- [maxon.APPSETTINGS.ASSETS.CACHEPATH](../modules/maxon_generated/enums/maxon.APPSETTINGS.ASSETS.CACHEPATH.md)
- [maxon.APPSETTINGS.ASSETS.DEFAULTS](../modules/maxon_generated/enums/maxon.APPSETTINGS.ASSETS.DEFAULTS.md)
- [maxon.APPSETTINGS.ASSETS.INSERTOBJECTAS](../modules/maxon_generated/enums/maxon.APPSETTINGS.ASSETS.INSERTOBJECTAS.md)
- [maxon.APPSETTINGS.ASSETS.LASTSAVEREPOSITORY](../modules/maxon_generated/enums/maxon.APPSETTINGS.ASSETS.LASTSAVEREPOSITORY.md)
- [maxon.APPSETTINGS.ASSETS.USERPATHS](../modules/maxon_generated/enums/maxon.APPSETTINGS.ASSETS.USERPATHS.md)
- [maxon.APPSETTINGS.ASSETS](../modules/maxon_generated/enums/maxon.APPSETTINGS.ASSETS.md)
- [maxon.ASSET.INFO.NAME](../modules/maxon_generated/enums/maxon.ASSET.INFO.NAME.md)
- [maxon.ASSET.INFO](../modules/maxon_generated/enums/maxon.ASSET.INFO.md)
- [maxon.ASSET.METAPROPERTIES](../modules/maxon_generated/enums/maxon.ASSET.METAPROPERTIES.md)
- [maxon.ASSETINSERTOBJECTMODE.ASINSTANCE](../modules/maxon_generated/enums/maxon.ASSETINSERTOBJECTMODE.ASINSTANCE.md)
- [maxon.ASSETINSERTOBJECTMODE.ASOBJECT](../modules/maxon_generated/enums/maxon.ASSETINSERTOBJECTMODE.ASOBJECT.md)
- [maxon.ASSETINSERTOBJECTMODE.ASRENDERINSTANCE](../modules/maxon_generated/enums/maxon.ASSETINSERTOBJECTMODE.ASRENDERINSTANCE.md)
- [maxon.ASSETINSERTOBJECTMODE.ASXREF](../modules/maxon_generated/enums/maxon.ASSETINSERTOBJECTMODE.ASXREF.md)
- [maxon.ASSETINSERTOBJECTMODE](../modules/maxon_generated/enums/maxon.ASSETINSERTOBJECTMODE.md)
- [maxon.ASSETLICENSETYPE.ALLBITS](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.ALLBITS.md)
- [maxon.ASSETLICENSETYPE.ENABLE_IN_ALL](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.ENABLE_IN_ALL.md)
- [maxon.ASSETLICENSETYPE.ENABLE_IN_ARCHVIZ](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.ENABLE_IN_ARCHVIZ.md)
- [maxon.ASSETLICENSETYPE.ENABLE_IN_CINEWARE](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.ENABLE_IN_CINEWARE.md)
- [maxon.ASSETLICENSETYPE.ENABLE_IN_EDUCATION](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.ENABLE_IN_EDUCATION.md)
- [maxon.ASSETLICENSETYPE.ENABLE_IN_LITE](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.ENABLE_IN_LITE.md)
- [maxon.ASSETLICENSETYPE.ENABLE_IN_PERPETUAL](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.ENABLE_IN_PERPETUAL.md)
- [maxon.ASSETLICENSETYPE.ENABLE_IN_STUDENT](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.ENABLE_IN_STUDENT.md)
- [maxon.ASSETLICENSETYPE.ENABLE_IN_SUBSCRIPTION](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.ENABLE_IN_SUBSCRIPTION.md)
- [maxon.ASSETLICENSETYPE.ENABLE_IN_TRIAL](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.ENABLE_IN_TRIAL.md)
- [maxon.ASSETLICENSETYPE.NONE](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.NONE.md)
- [maxon.ASSETLICENSETYPE.ONLY_IN_MAXONONE](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.ONLY_IN_MAXONONE.md)
- [maxon.ASSETLICENSETYPE.SHOW_IN_ALL](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.SHOW_IN_ALL.md)
- [maxon.ASSETLICENSETYPE.SHOW_IN_ARCHVIZ](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.SHOW_IN_ARCHVIZ.md)
- [maxon.ASSETLICENSETYPE.SHOW_IN_CINEWARE](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.SHOW_IN_CINEWARE.md)
- [maxon.ASSETLICENSETYPE.SHOW_IN_EDUCATION](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.SHOW_IN_EDUCATION.md)
- [maxon.ASSETLICENSETYPE.SHOW_IN_LITE](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.SHOW_IN_LITE.md)
- [maxon.ASSETLICENSETYPE.SHOW_IN_PERPETUAL](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.SHOW_IN_PERPETUAL.md)
- [maxon.ASSETLICENSETYPE.SHOW_IN_STUDENT](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.SHOW_IN_STUDENT.md)
- [maxon.ASSETLICENSETYPE.SHOW_IN_SUBSCRIPTION](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.SHOW_IN_SUBSCRIPTION.md)
- [maxon.ASSETLICENSETYPE.SHOW_IN_TRIAL](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.SHOW_IN_TRIAL.md)
- [maxon.ASSETLICENSETYPE](../modules/maxon_generated/enums/maxon.ASSETLICENSETYPE.md)
- [maxon.ASSETMETADATA.ANALYTICS](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ANALYTICS.md)
- [maxon.ASSETMETADATA.ASSET_CREATED](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ASSET_CREATED.md)
- [maxon.ASSETMETADATA.ASSET_PREVIEWANIMURL](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ASSET_PREVIEWANIMURL.md)
- [maxon.ASSETMETADATA.ASSET_PREVIEWIMAGEURL](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ASSET_PREVIEWIMAGEURL.md)
- [maxon.ASSETMETADATA.ASSET_SIZE](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ASSET_SIZE.md)
- [maxon.ASSETMETADATA.ASSET_SORT](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ASSET_SORT.md)
- [maxon.ASSETMETADATA.ASSET_TIMESTAMP](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ASSET_TIMESTAMP.md)
- [maxon.ASSETMETADATA.ASSET_VERSIONTAG](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ASSET_VERSIONTAG.md)
- [maxon.ASSETMETADATA.Category](../modules/maxon_generated/enums/maxon.ASSETMETADATA.Category.md)
- [maxon.ASSETMETADATA.ColorCategory](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ColorCategory.md)
- [maxon.ASSETMETADATA.CommandExecute](../modules/maxon_generated/enums/maxon.ASSETMETADATA.CommandExecute.md)
- [maxon.ASSETMETADATA.CommandHelp](../modules/maxon_generated/enums/maxon.ASSETMETADATA.CommandHelp.md)
- [maxon.ASSETMETADATA.CommandLegacyId](../modules/maxon_generated/enums/maxon.ASSETMETADATA.CommandLegacyId.md)
- [maxon.ASSETMETADATA.CommandLegacyScope](../modules/maxon_generated/enums/maxon.ASSETMETADATA.CommandLegacyScope.md)
- [maxon.ASSETMETADATA.CommandQueryState](../modules/maxon_generated/enums/maxon.ASSETMETADATA.CommandQueryState.md)
- [maxon.ASSETMETADATA.CommandScopes](../modules/maxon_generated/enums/maxon.ASSETMETADATA.CommandScopes.md)
- [maxon.ASSETMETADATA.CommandShortcuts](../modules/maxon_generated/enums/maxon.ASSETMETADATA.CommandShortcuts.md)
- [maxon.ASSETMETADATA.CreationProperties](../modules/maxon_generated/enums/maxon.ASSETMETADATA.CreationProperties.md)
- [maxon.ASSETMETADATA.Creator](../modules/maxon_generated/enums/maxon.ASSETMETADATA.Creator.md)
- [maxon.ASSETMETADATA.DecryptionKeys](../modules/maxon_generated/enums/maxon.ASSETMETADATA.DecryptionKeys.md)
- [maxon.ASSETMETADATA.Dependencies](../modules/maxon_generated/enums/maxon.ASSETMETADATA.Dependencies.md)
- [maxon.ASSETMETADATA.DerivedMetaDataStamp](../modules/maxon_generated/enums/maxon.ASSETMETADATA.DerivedMetaDataStamp.md)
- [maxon.ASSETMETADATA.HiddenCommand](../modules/maxon_generated/enums/maxon.ASSETMETADATA.HiddenCommand.md)
- [maxon.ASSETMETADATA.ID_FAVOURITEKEYWORD](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ID_FAVOURITEKEYWORD.md)
- [maxon.ASSETMETADATA.ID_FEATUREDKEYWORD](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ID_FEATUREDKEYWORD.md)
- [maxon.ASSETMETADATA.InternetResources](../modules/maxon_generated/enums/maxon.ASSETMETADATA.InternetResources.md)
- [maxon.ASSETMETADATA.Keywords](../modules/maxon_generated/enums/maxon.ASSETMETADATA.Keywords.md)
- [maxon.ASSETMETADATA.License](../modules/maxon_generated/enums/maxon.ASSETMETADATA.License.md)
- [maxon.ASSETMETADATA.LicenseUrl](../modules/maxon_generated/enums/maxon.ASSETMETADATA.LicenseUrl.md)
- [maxon.ASSETMETADATA.MXAI1](../modules/maxon_generated/enums/maxon.ASSETMETADATA.MXAI1.md)
- [maxon.ASSETMETADATA.MetaProperties](../modules/maxon_generated/enums/maxon.ASSETMETADATA.MetaProperties.md)
- [maxon.ASSETMETADATA.NodeSpace](../modules/maxon_generated/enums/maxon.ASSETMETADATA.NodeSpace.md)
- [maxon.ASSETMETADATA.PROXYGEOMETRY](../modules/maxon_generated/enums/maxon.ASSETMETADATA.PROXYGEOMETRY.md)
- [maxon.ASSETMETADATA.Plugin](../modules/maxon_generated/enums/maxon.ASSETMETADATA.Plugin.md)
- [maxon.ASSETMETADATA.SmartSearch](../modules/maxon_generated/enums/maxon.ASSETMETADATA.SmartSearch.md)
- [maxon.ASSETMETADATA.SubType](../modules/maxon_generated/enums/maxon.ASSETMETADATA.SubType.md)
- [maxon.ASSETMETADATA.SubType_ENUM_ExternalPlugin](../modules/maxon_generated/enums/maxon.ASSETMETADATA.SubType_ENUM_ExternalPlugin.md)
- [maxon.ASSETMETADATA.SubType_ENUM_InternalModule](../modules/maxon_generated/enums/maxon.ASSETMETADATA.SubType_ENUM_InternalModule.md)
- [maxon.ASSETMETADATA.SubType_ENUM_Laubwerk](../modules/maxon_generated/enums/maxon.ASSETMETADATA.SubType_ENUM_Laubwerk.md)
- [maxon.ASSETMETADATA.SubType_ENUM_Material](../modules/maxon_generated/enums/maxon.ASSETMETADATA.SubType_ENUM_Material.md)
- [maxon.ASSETMETADATA.SubType_ENUM_MediaImage](../modules/maxon_generated/enums/maxon.ASSETMETADATA.SubType_ENUM_MediaImage.md)
- [maxon.ASSETMETADATA.SubType_ENUM_MediaMovie](../modules/maxon_generated/enums/maxon.ASSETMETADATA.SubType_ENUM_MediaMovie.md)
- [maxon.ASSETMETADATA.SubType_ENUM_Object](../modules/maxon_generated/enums/maxon.ASSETMETADATA.SubType_ENUM_Object.md)
- [maxon.ASSETMETADATA.SubType_ENUM_Scene](../modules/maxon_generated/enums/maxon.ASSETMETADATA.SubType_ENUM_Scene.md)
- [maxon.ASSETMETADATA.Usage](../modules/maxon_generated/enums/maxon.ASSETMETADATA.Usage.md)
- [maxon.ASSETMETADATA.UserKeywords](../modules/maxon_generated/enums/maxon.ASSETMETADATA.UserKeywords.md)
- [maxon.ASSETMETADATA.ValidLicenseType](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ValidLicenseType.md)
- [maxon.ASSETMETADATA.ValidLicenses](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ValidLicenses.md)
- [maxon.ASSETMETADATA.ValidVersionRange](../modules/maxon_generated/enums/maxon.ASSETMETADATA.ValidVersionRange.md)
- [maxon.ASSETMETADATA.Vendor](../modules/maxon_generated/enums/maxon.ASSETMETADATA.Vendor.md)
- [maxon.ASSETMETADATA](../modules/maxon_generated/enums/maxon.ASSETMETADATA.md)
- [maxon.ASSETPOPUPOPTIONS.ALLOWDRAGANDDROP](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.ALLOWDRAGANDDROP.md)
- [maxon.ASSETPOPUPOPTIONS.ALLOWPINPOPUP](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.ALLOWPINPOPUP.md)
- [maxon.ASSETPOPUPOPTIONS.COMMANDER](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.COMMANDER.md)
- [maxon.ASSETPOPUPOPTIONS.DISPLAYASLIST](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.DISPLAYASLIST.md)
- [maxon.ASSETPOPUPOPTIONS.EXECUTELOAD](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.EXECUTELOAD.md)
- [maxon.ASSETPOPUPOPTIONS.HIDEAIBUTTON](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.HIDEAIBUTTON.md)
- [maxon.ASSETPOPUPOPTIONS.HIDENAVIGATIONBAR](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.HIDENAVIGATIONBAR.md)
- [maxon.ASSETPOPUPOPTIONS.HIDEWATCHFOLDERS](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.HIDEWATCHFOLDERS.md)
- [maxon.ASSETPOPUPOPTIONS.MODAL](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.MODAL.md)
- [maxon.ASSETPOPUPOPTIONS.NONE](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.NONE.md)
- [maxon.ASSETPOPUPOPTIONS.POPUPMODE](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.POPUPMODE.md)
- [maxon.ASSETPOPUPOPTIONS.SHOWCATEGORIESONLY](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.SHOWCATEGORIESONLY.md)
- [maxon.ASSETPOPUPOPTIONS.SHOWCATEGORYLIST](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.SHOWCATEGORYLIST.md)
- [maxon.ASSETPOPUPOPTIONS.SHOWKEYWORDSONLY](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.SHOWKEYWORDSONLY.md)
- [maxon.ASSETPOPUPOPTIONS.SHOWQUICKTABS](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.SHOWQUICKTABS.md)
- [maxon.ASSETPOPUPOPTIONS.SUBDIALOG](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.SUBDIALOG.md)
- [maxon.ASSETPOPUPOPTIONS](../modules/maxon_generated/enums/maxon.ASSETPOPUPOPTIONS.md)
- [maxon.ASSETREPOSITORYPROPERTIES.ASSETCOUNT](../modules/maxon_generated/enums/maxon.ASSETREPOSITORYPROPERTIES.ASSETCOUNT.md)
- [maxon.ASSETREPOSITORYPROPERTIES.ASSETSIZE](../modules/maxon_generated/enums/maxon.ASSETREPOSITORYPROPERTIES.ASSETSIZE.md)
- [maxon.ASSETREPOSITORYPROPERTIES.CATEGORYCOUNT](../modules/maxon_generated/enums/maxon.ASSETREPOSITORYPROPERTIES.CATEGORYCOUNT.md)
- [maxon.ASSETREPOSITORYPROPERTIES.DETAILCOUNT](../modules/maxon_generated/enums/maxon.ASSETREPOSITORYPROPERTIES.DETAILCOUNT.md)
- [maxon.ASSETREPOSITORYPROPERTIES.EXPORT_ON_SAVE_PROJECT](../modules/maxon_generated/enums/maxon.ASSETREPOSITORYPROPERTIES.EXPORT_ON_SAVE_PROJECT.md)
- [maxon.ASSETREPOSITORYPROPERTIES.SKIP_ON_SEARCH](../modules/maxon_generated/enums/maxon.ASSETREPOSITORYPROPERTIES.SKIP_ON_SEARCH.md)
- [maxon.ASSETREPOSITORYPROPERTIES.WRITABILITY_CHANGE_ALLOWED](../modules/maxon_generated/enums/maxon.ASSETREPOSITORYPROPERTIES.WRITABILITY_CHANGE_ALLOWED.md)
- [maxon.ASSETREPOSITORYPROPERTIES](../modules/maxon_generated/enums/maxon.ASSETREPOSITORYPROPERTIES.md)
- [maxon.ASSETTYPEPROPERTIES](../modules/maxon_generated/enums/maxon.ASSETTYPEPROPERTIES.md)
- [maxon.ASSET_FIND_MODE.ALL](../modules/maxon_generated/enums/maxon.ASSET_FIND_MODE.ALL.md)
- [maxon.ASSET_FIND_MODE.CHECK_CANCELLATION](../modules/maxon_generated/enums/maxon.ASSET_FIND_MODE.CHECK_CANCELLATION.md)
- [maxon.ASSET_FIND_MODE.LATEST](../modules/maxon_generated/enums/maxon.ASSET_FIND_MODE.LATEST.md)
- [maxon.ASSET_FIND_MODE.NONE](../modules/maxon_generated/enums/maxon.ASSET_FIND_MODE.NONE.md)
- [maxon.ASSET_FIND_MODE.PREFIX](../modules/maxon_generated/enums/maxon.ASSET_FIND_MODE.PREFIX.md)
- [maxon.ASSET_FIND_MODE.PRIVATE_QUERY_REPOSITORY_VISIBILITY](../modules/maxon_generated/enums/maxon.ASSET_FIND_MODE.PRIVATE_QUERY_REPOSITORY_VISIBILITY.md)
- [maxon.ASSET_FIND_MODE.RANDOMIZED_ORDER](../modules/maxon_generated/enums/maxon.ASSET_FIND_MODE.RANDOMIZED_ORDER.md)
- [maxon.ASSET_FIND_MODE.WITHOUT_BASES](../modules/maxon_generated/enums/maxon.ASSET_FIND_MODE.WITHOUT_BASES.md)
- [maxon.ASSET_FIND_MODE.WITH_DELETED](../modules/maxon_generated/enums/maxon.ASSET_FIND_MODE.WITH_DELETED.md)
- [maxon.ASSET_FIND_MODE](../modules/maxon_generated/enums/maxon.ASSET_FIND_MODE.md): The flags of ASSET_FIND_MODE control the behavior of AssetRepositoryInterface.FindAssets().
- [maxon.AssetMetaDataInterface.KIND.COPY_AS_PERSISTENT](../modules/maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.COPY_AS_PERSISTENT.md)
- [maxon.AssetMetaDataInterface.KIND.DERIVED](../modules/maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.DERIVED.md)
- [maxon.AssetMetaDataInterface.KIND.DERIVED_FALLBACK](../modules/maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.DERIVED_FALLBACK.md)
- [maxon.AssetMetaDataInterface.KIND.IGNORE_READ_ONLY](../modules/maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.IGNORE_READ_ONLY.md)
- [maxon.AssetMetaDataInterface.KIND.MASK](../modules/maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.MASK.md)
- [maxon.AssetMetaDataInterface.KIND.NONE](../modules/maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.NONE.md)
- [maxon.AssetMetaDataInterface.KIND.PERSISTENT](../modules/maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.PERSISTENT.md)
- [maxon.AssetMetaDataInterface.KIND.READ_ONLY](../modules/maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.READ_ONLY.md)
- [maxon.AssetMetaDataInterface.KIND.SAVEASBINARY](../modules/maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.SAVEASBINARY.md)
- [maxon.AssetMetaDataInterface.KIND.USER](../modules/maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.USER.md)
- [maxon.AssetMetaDataInterface.KIND.USER_FALLBACK](../modules/maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.USER_FALLBACK.md)
- [maxon.AssetMetaDataInterface.KIND.VERSION](../modules/maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.VERSION.md)
- [maxon.AssetMetaDataInterface.KIND](../modules/maxon_generated/enums/maxon.AssetMetaDataInterface.KIND.md)
- [maxon.CONNECTION_POSITION.CENTER](../modules/maxon_generated/enums/maxon.CONNECTION_POSITION.CENTER.md)
- [maxon.CONNECTION_POSITION.SOURCE](../modules/maxon_generated/enums/maxon.CONNECTION_POSITION.SOURCE.md)
- [maxon.CONNECTION_POSITION.TARGET](../modules/maxon_generated/enums/maxon.CONNECTION_POSITION.TARGET.md)
- [maxon.CONNECTION_POSITION](../modules/maxon_generated/enums/maxon.CONNECTION_POSITION.md)
- [maxon.FILTERACCURACY.FIRST](../modules/maxon_generated/enums/maxon.FILTERACCURACY.FIRST.md)
- [maxon.FILTERACCURACY.HJWENO5](../modules/maxon_generated/enums/maxon.FILTERACCURACY.HJWENO5.md)
- [maxon.FILTERACCURACY.NONE](../modules/maxon_generated/enums/maxon.FILTERACCURACY.NONE.md)
- [maxon.FILTERACCURACY.SECOND](../modules/maxon_generated/enums/maxon.FILTERACCURACY.SECOND.md)
- [maxon.FILTERACCURACY.THIRD](../modules/maxon_generated/enums/maxon.FILTERACCURACY.THIRD.md)
- [maxon.FILTERACCURACY.WENO5](../modules/maxon_generated/enums/maxon.FILTERACCURACY.WENO5.md)
- [maxon.FILTERACCURACY.denominator](../modules/maxon_generated/enums/maxon.FILTERACCURACY.denominator.md)
- [maxon.FILTERACCURACY.imag](../modules/maxon_generated/enums/maxon.FILTERACCURACY.imag.md)
- [maxon.FILTERACCURACY](../modules/maxon_generated/enums/maxon.FILTERACCURACY.md): int([x]) -> integer int(x, base=10) -> integer
- [maxon.FILTERACCURACY.numerator](../modules/maxon_generated/enums/maxon.FILTERACCURACY.numerator.md)
- [maxon.FILTERACCURACY.real](../modules/maxon_generated/enums/maxon.FILTERACCURACY.real.md)
- [maxon.GENERATESCENEPREVIEWIMAGEFLAGS.AUTODETECT_RENDERENGINE](../modules/maxon_generated/enums/maxon.GENERATESCENEPREVIEWIMAGEFLAGS.AUTODETECT_RENDERENGINE.md)
- [maxon.GENERATESCENEPREVIEWIMAGEFLAGS.BAKE_OCIO_VIEW_TRANSFORM](../modules/maxon_generated/enums/maxon.GENERATESCENEPREVIEWIMAGEFLAGS.BAKE_OCIO_VIEW_TRANSFORM.md)
- [maxon.GENERATESCENEPREVIEWIMAGEFLAGS.FRAMESCENE](../modules/maxon_generated/enums/maxon.GENERATESCENEPREVIEWIMAGEFLAGS.FRAMESCENE.md)
- [maxon.GENERATESCENEPREVIEWIMAGEFLAGS.GEOMETRYONLY](../modules/maxon_generated/enums/maxon.GENERATESCENEPREVIEWIMAGEFLAGS.GEOMETRYONLY.md)
- [maxon.GENERATESCENEPREVIEWIMAGEFLAGS.ISORIGINALDOCUMENT](../modules/maxon_generated/enums/maxon.GENERATESCENEPREVIEWIMAGEFLAGS.ISORIGINALDOCUMENT.md)
- [maxon.GENERATESCENEPREVIEWIMAGEFLAGS.NONE](../modules/maxon_generated/enums/maxon.GENERATESCENEPREVIEWIMAGEFLAGS.NONE.md)
- [maxon.GENERATESCENEPREVIEWIMAGEFLAGS.PREVIEWRENDER](../modules/maxon_generated/enums/maxon.GENERATESCENEPREVIEWIMAGEFLAGS.PREVIEWRENDER.md)
- [maxon.GENERATESCENEPREVIEWIMAGEFLAGS](../modules/maxon_generated/enums/maxon.GENERATESCENEPREVIEWIMAGEFLAGS.md)
- [maxon.GraphAttributeInterface.FLAGS.DERIVED](../modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.DERIVED.md)
- [maxon.GraphAttributeInterface.FLAGS.DIRECT](../modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.DIRECT.md)
- [maxon.GraphAttributeInterface.FLAGS.ERROR](../modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.ERROR.md)
- [maxon.GraphAttributeInterface.FLAGS.IMMUTABLE](../modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.IMMUTABLE.md)
- [maxon.GraphAttributeInterface.FLAGS.MESSAGE_MASK](../modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.MESSAGE_MASK.md)
- [maxon.GraphAttributeInterface.FLAGS.META](../modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.META.md)
- [maxon.GraphAttributeInterface.FLAGS.NONE](../modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.NONE.md)
- [maxon.GraphAttributeInterface.FLAGS.ROOT](../modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.ROOT.md)
- [maxon.GraphAttributeInterface.FLAGS.TRANSIENT](../modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.TRANSIENT.md)
- [maxon.GraphAttributeInterface.FLAGS.TYPE_MASK](../modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.TYPE_MASK.md)
- [maxon.GraphAttributeInterface.FLAGS.USER_STATE](../modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.USER_STATE.md)
- [maxon.GraphAttributeInterface.FLAGS.WARNING](../modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.WARNING.md)
- [maxon.GraphAttributeInterface.FLAGS](../modules/maxon_generated/enums/maxon.GraphAttributeInterface.FLAGS.md): FLAGS provide information about the nature of the attribute.
- [maxon.GraphDescription.PARSE_FLAGS.ALWAYS_VALIDATE_PATHS](../modules/maxon_generated/enums/maxon.GraphDescription.PARSE_FLAGS.ALWAYS_VALIDATE_PATHS.md)
- [maxon.GraphDescription.PARSE_FLAGS.NONE](../modules/maxon_generated/enums/maxon.GraphDescription.PARSE_FLAGS.NONE.md)
- [maxon.GraphDescription.PARSE_FLAGS.RAW_COLORS](../modules/maxon_generated/enums/maxon.GraphDescription.PARSE_FLAGS.RAW_COLORS.md)
- [maxon.GraphDescription.PARSE_FLAGS.VERBOSE_ATTRIBUTES](../modules/maxon_generated/enums/maxon.GraphDescription.PARSE_FLAGS.VERBOSE_ATTRIBUTES.md)
- [maxon.GraphDescription.PARSE_FLAGS.VERBOSE_REFERENCES](../modules/maxon_generated/enums/maxon.GraphDescription.PARSE_FLAGS.VERBOSE_REFERENCES.md)
- [maxon.GraphDescription.PARSE_FLAGS](../modules/maxon_generated/enums/maxon.GraphDescription.PARSE_FLAGS.md): Expresses options when parsing graph descriptions.
- [maxon.GraphDescription.QUERY_FLAGS.DEBUG](../modules/maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.DEBUG.md)
- [maxon.GraphDescription.QUERY_FLAGS.MATCH_ALL](../modules/maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.MATCH_ALL.md)
- [maxon.GraphDescription.QUERY_FLAGS.MATCH_FIRST](../modules/maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.MATCH_FIRST.md)
- [maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE](../modules/maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE.md)
- [maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL](../modules/maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_ALL.md)
- [maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_FIRST](../modules/maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.MATCH_MAYBE_FIRST.md)
- [maxon.GraphDescription.QUERY_FLAGS.NONE](../modules/maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.NONE.md)
- [maxon.GraphDescription.QUERY_FLAGS.RAW_COLORS](../modules/maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.RAW_COLORS.md)
- [maxon.GraphDescription.QUERY_FLAGS.RAW_URLS](../modules/maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.RAW_URLS.md)
- [maxon.GraphDescription.QUERY_FLAGS.SELECT_THIS](../modules/maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.SELECT_THIS.md)
- [maxon.GraphDescription.QUERY_FLAGS](../modules/maxon_generated/enums/maxon.GraphDescription.QUERY_FLAGS.md): Expresses options when querying a graph for nodes.
- [maxon.GraphModelInterface.GET_CONNECTIONS_MODE.CONNECTIONS](../modules/maxon_generated/enums/maxon.GraphModelInterface.GET_CONNECTIONS_MODE.CONNECTIONS.md)
- [maxon.GraphModelInterface.GET_CONNECTIONS_MODE.DERIVATION_FILTER](../modules/maxon_generated/enums/maxon.GraphModelInterface.GET_CONNECTIONS_MODE.DERIVATION_FILTER.md)
- [maxon.GraphModelInterface.GET_CONNECTIONS_MODE.EXTERNAL_CONNECTIONS](../modules/maxon_generated/enums/maxon.GraphModelInterface.GET_CONNECTIONS_MODE.EXTERNAL_CONNECTIONS.md)
- [maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INCLUDE_HIDDEN](../modules/maxon_generated/enums/maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INCLUDE_HIDDEN.md)
- [maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INDUCED_DEPENDENCIES](../modules/maxon_generated/enums/maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INDUCED_DEPENDENCIES.md)
- [maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INTERNAL_CONNECTIONS](../modules/maxon_generated/enums/maxon.GraphModelInterface.GET_CONNECTIONS_MODE.INTERNAL_CONNECTIONS.md)
- [maxon.GraphModelInterface.GET_CONNECTIONS_MODE.NONE](../modules/maxon_generated/enums/maxon.GraphModelInterface.GET_CONNECTIONS_MODE.NONE.md)
- [maxon.GraphModelInterface.GET_CONNECTIONS_MODE.SKIP_REROUTER](../modules/maxon_generated/enums/maxon.GraphModelInterface.GET_CONNECTIONS_MODE.SKIP_REROUTER.md)
- [maxon.GraphModelInterface.GET_CONNECTIONS_MODE.WITHOUT_INHIBITED](../modules/maxon_generated/enums/maxon.GraphModelInterface.GET_CONNECTIONS_MODE.WITHOUT_INHIBITED.md)
- [maxon.GraphModelInterface.GET_CONNECTIONS_MODE](../modules/maxon_generated/enums/maxon.GraphModelInterface.GET_CONNECTIONS_MODE.md)
- [maxon.GraphModelInterface.MODIFIED.ALL_MASK](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.ALL_MASK.md)
- [maxon.GraphModelInterface.MODIFIED.ATTRIBUTE_MASK](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.ATTRIBUTE_MASK.md)
- [maxon.GraphModelInterface.MODIFIED.CHILD_REMOVED](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.CHILD_REMOVED.md)
- [maxon.GraphModelInterface.MODIFIED.COMPLETE](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.COMPLETE.md)
- [maxon.GraphModelInterface.MODIFIED.CONNECTION_MASK](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.CONNECTION_MASK.md)
- [maxon.GraphModelInterface.MODIFIED.DATA_ATTRIBUTE_MASK](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.DATA_ATTRIBUTE_MASK.md)
- [maxon.GraphModelInterface.MODIFIED.DERIVED_ATTRIBUTE_MASK](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.DERIVED_ATTRIBUTE_MASK.md)
- [maxon.GraphModelInterface.MODIFIED.DIRECT_ATTRIBUTE](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.DIRECT_ATTRIBUTE.md)
- [maxon.GraphModelInterface.MODIFIED.DIRECT_ATTRIBUTE_MASK](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.DIRECT_ATTRIBUTE_MASK.md)
- [maxon.GraphModelInterface.MODIFIED.DIRECT_META_ATTRIBUTE](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.DIRECT_META_ATTRIBUTE.md)
- [maxon.GraphModelInterface.MODIFIED.INHERITED_ATTRIBUTE](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.INHERITED_ATTRIBUTE.md)
- [maxon.GraphModelInterface.MODIFIED.INPUT_CONNECTION](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.INPUT_CONNECTION.md)
- [maxon.GraphModelInterface.MODIFIED.NODE_ADDED](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.NODE_ADDED.md)
- [maxon.GraphModelInterface.MODIFIED.NODE_MASK](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.NODE_MASK.md)
- [maxon.GraphModelInterface.MODIFIED.NONE](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.NONE.md)
- [maxon.GraphModelInterface.MODIFIED.OUTPUT_CONNECTION](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.OUTPUT_CONNECTION.md)
- [maxon.GraphModelInterface.MODIFIED.SPECIAL0](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.SPECIAL0.md)
- [maxon.GraphModelInterface.MODIFIED.SPECIAL1](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.SPECIAL1.md)
- [maxon.GraphModelInterface.MODIFIED.SPECIAL_NAME](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.SPECIAL_NAME.md)
- [maxon.GraphModelInterface.MODIFIED.STRUCTURE_MASK](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.STRUCTURE_MASK.md)
- [maxon.GraphModelInterface.MODIFIED.SYNTHESIZED_ATTRIBUTE](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.SYNTHESIZED_ATTRIBUTE.md)
- [maxon.GraphModelInterface.MODIFIED.USER_STATE_ATTRIBUTE](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.USER_STATE_ATTRIBUTE.md)
- [maxon.GraphModelInterface.MODIFIED](../modules/maxon_generated/enums/maxon.GraphModelInterface.MODIFIED.md): These flags are reported by GraphModelInterface.GetModificationsSince() to tell which properties of the node have changed.
- [maxon.MASTERFILTER.ALL](../modules/maxon_generated/enums/maxon.MASTERFILTER.ALL.md)
- [maxon.MASTERFILTER.MATERIALS](../modules/maxon_generated/enums/maxon.MASTERFILTER.MATERIALS.md)
- [maxon.MASTERFILTER.MEDIA](../modules/maxon_generated/enums/maxon.MASTERFILTER.MEDIA.md)
- [maxon.MASTERFILTER.NODES](../modules/maxon_generated/enums/maxon.MASTERFILTER.NODES.md)
- [maxon.MASTERFILTER.OBJECTCOMMANDS](../modules/maxon_generated/enums/maxon.MASTERFILTER.OBJECTCOMMANDS.md)
- [maxon.MASTERFILTER.OBJECTS](../modules/maxon_generated/enums/maxon.MASTERFILTER.OBJECTS.md)
- [maxon.MASTERFILTER.OTHERCOMMANDS](../modules/maxon_generated/enums/maxon.MASTERFILTER.OTHERCOMMANDS.md)
- [maxon.MASTERFILTER.PRESETS](../modules/maxon_generated/enums/maxon.MASTERFILTER.PRESETS.md)
- [maxon.MASTERFILTER.SCENES](../modules/maxon_generated/enums/maxon.MASTERFILTER.SCENES.md)
- [maxon.MASTERFILTER.SCENE_NODES](../modules/maxon_generated/enums/maxon.MASTERFILTER.SCENE_NODES.md)
- [maxon.MASTERFILTER.SPECIAL](../modules/maxon_generated/enums/maxon.MASTERFILTER.SPECIAL.md)
- [maxon.MASTERFILTER.TOOLCOMMANDS](../modules/maxon_generated/enums/maxon.MASTERFILTER.TOOLCOMMANDS.md)
- [maxon.MASTERFILTER](../modules/maxon_generated/enums/maxon.MASTERFILTER.md)
- [maxon.NIMBUS_PATH.MATERIALENDNODE](../modules/maxon_generated/enums/maxon.NIMBUS_PATH.MATERIALENDNODE.md)
- [maxon.NIMBUS_PATH.SOLO](../modules/maxon_generated/enums/maxon.NIMBUS_PATH.SOLO.md)
- [maxon.NIMBUS_PATH.STARTNODE](../modules/maxon_generated/enums/maxon.NIMBUS_PATH.STARTNODE.md)
- [maxon.NIMBUS_PATH](../modules/maxon_generated/enums/maxon.NIMBUS_PATH.md): NIMBUS_PATH is used as argument for NimbusBaseInterface._GetPath() and NimbusBaseInterface.SetPath().
- [maxon.NODE_KIND.ALL_MASK](../modules/maxon_generated/enums/maxon.NODE_KIND.ALL_MASK.md)
- [maxon.NODE_KIND.INPORT](../modules/maxon_generated/enums/maxon.NODE_KIND.INPORT.md)
- [maxon.NODE_KIND.INPUTS](../modules/maxon_generated/enums/maxon.NODE_KIND.INPUTS.md)
- [maxon.NODE_KIND.IN_MASK](../modules/maxon_generated/enums/maxon.NODE_KIND.IN_MASK.md)
- [maxon.NODE_KIND.NODE](../modules/maxon_generated/enums/maxon.NODE_KIND.NODE.md)
- [maxon.NODE_KIND.NONE](../modules/maxon_generated/enums/maxon.NODE_KIND.NONE.md)
- [maxon.NODE_KIND.OUTPORT](../modules/maxon_generated/enums/maxon.NODE_KIND.OUTPORT.md)
- [maxon.NODE_KIND.OUTPUTS](../modules/maxon_generated/enums/maxon.NODE_KIND.OUTPUTS.md)
- [maxon.NODE_KIND.OUT_MASK](../modules/maxon_generated/enums/maxon.NODE_KIND.OUT_MASK.md)
- [maxon.NODE_KIND.PORTLIST_MASK](../modules/maxon_generated/enums/maxon.NODE_KIND.PORTLIST_MASK.md)
- [maxon.NODE_KIND.PORT_MASK](../modules/maxon_generated/enums/maxon.NODE_KIND.PORT_MASK.md)
- [maxon.NODE_KIND](../modules/maxon_generated/enums/maxon.NODE_KIND.md)
- [maxon.NodeSpaceIdentifiers.RedshiftMaterial](../modules/maxon_generated/enums/maxon.NodeSpaceIdentifiers.RedshiftMaterial.md)
- [maxon.NodeSpaceIdentifiers.SceneNodes](../modules/maxon_generated/enums/maxon.NodeSpaceIdentifiers.SceneNodes.md)
- [maxon.NodeSpaceIdentifiers.StandardMaterial](../modules/maxon_generated/enums/maxon.NodeSpaceIdentifiers.StandardMaterial.md)
- [maxon.NodeSpaceIdentifiers](../modules/maxon_generated/enums/maxon.NodeSpaceIdentifiers.md): Holds the identifiers for all node spaces shipped with Cinema 4D.
- [maxon.NodeSystemManagerInterface.FILTER.INCLUDE_ALL](../modules/maxon_generated/enums/maxon.NodeSystemManagerInterface.FILTER.INCLUDE_ALL.md)
- [maxon.NodeSystemManagerInterface.FILTER.INCLUDE_HIDDEN](../modules/maxon_generated/enums/maxon.NodeSystemManagerInterface.FILTER.INCLUDE_HIDDEN.md)
- [maxon.NodeSystemManagerInterface.FILTER.INCLUDE_INNER](../modules/maxon_generated/enums/maxon.NodeSystemManagerInterface.FILTER.INCLUDE_INNER.md)
- [maxon.NodeSystemManagerInterface.FILTER.NONE](../modules/maxon_generated/enums/maxon.NodeSystemManagerInterface.FILTER.NONE.md)
- [maxon.NodeSystemManagerInterface.FILTER.READ_ONLY](../modules/maxon_generated/enums/maxon.NodeSystemManagerInterface.FILTER.READ_ONLY.md)
- [maxon.NodeSystemManagerInterface.FILTER](../modules/maxon_generated/enums/maxon.NodeSystemManagerInterface.FILTER.md)
- [maxon.OPENSAVEASSETDIALOGFLAGS.ALLOW_EDIT_ID](../modules/maxon_generated/enums/maxon.OPENSAVEASSETDIALOGFLAGS.ALLOW_EDIT_ID.md)
- [maxon.OPENSAVEASSETDIALOGFLAGS.ALLOW_EDIT_NAME](../modules/maxon_generated/enums/maxon.OPENSAVEASSETDIALOGFLAGS.ALLOW_EDIT_NAME.md)
- [maxon.OPENSAVEASSETDIALOGFLAGS.ALLOW_EMPTY_CATEGORY](../modules/maxon_generated/enums/maxon.OPENSAVEASSETDIALOGFLAGS.ALLOW_EMPTY_CATEGORY.md)
- [maxon.OPENSAVEASSETDIALOGFLAGS.HIDE_AI_BUTTON](../modules/maxon_generated/enums/maxon.OPENSAVEASSETDIALOGFLAGS.HIDE_AI_BUTTON.md)
- [maxon.OPENSAVEASSETDIALOGFLAGS.NONE](../modules/maxon_generated/enums/maxon.OPENSAVEASSETDIALOGFLAGS.NONE.md)
- [maxon.OPENSAVEASSETDIALOGFLAGS.SHOW_MAKE_DEFAULT](../modules/maxon_generated/enums/maxon.OPENSAVEASSETDIALOGFLAGS.SHOW_MAKE_DEFAULT.md)
- [maxon.OPENSAVEASSETDIALOGFLAGS.SHOW_VERSION](../modules/maxon_generated/enums/maxon.OPENSAVEASSETDIALOGFLAGS.SHOW_VERSION.md)
- [maxon.OPENSAVEASSETDIALOGFLAGS](../modules/maxon_generated/enums/maxon.OPENSAVEASSETDIALOGFLAGS.md)
- [maxon.POLYGONCONVERSIONFLAGS.DISABLE_INTERSECTING_VOXEL_REMOVAL](../modules/maxon_generated/enums/maxon.POLYGONCONVERSIONFLAGS.DISABLE_INTERSECTING_VOXEL_REMOVAL.md)
- [maxon.POLYGONCONVERSIONFLAGS.DISABLE_NARROW_BAND_TRIMMING](../modules/maxon_generated/enums/maxon.POLYGONCONVERSIONFLAGS.DISABLE_NARROW_BAND_TRIMMING.md)
- [maxon.POLYGONCONVERSIONFLAGS.DISABLE_RENORMALIZATION](../modules/maxon_generated/enums/maxon.POLYGONCONVERSIONFLAGS.DISABLE_RENORMALIZATION.md)
- [maxon.POLYGONCONVERSIONFLAGS.NONE](../modules/maxon_generated/enums/maxon.POLYGONCONVERSIONFLAGS.NONE.md)
- [maxon.POLYGONCONVERSIONFLAGS.UNSIGNED_DISTANCE_FIELD](../modules/maxon_generated/enums/maxon.POLYGONCONVERSIONFLAGS.UNSIGNED_DISTANCE_FIELD.md)
- [maxon.POLYGONCONVERSIONFLAGS.denominator](../modules/maxon_generated/enums/maxon.POLYGONCONVERSIONFLAGS.denominator.md)
- [maxon.POLYGONCONVERSIONFLAGS.imag](../modules/maxon_generated/enums/maxon.POLYGONCONVERSIONFLAGS.imag.md)
- [maxon.POLYGONCONVERSIONFLAGS](../modules/maxon_generated/enums/maxon.POLYGONCONVERSIONFLAGS.md): int([x]) -> integer int(x, base=10) -> integer
- [maxon.POLYGONCONVERSIONFLAGS.numerator](../modules/maxon_generated/enums/maxon.POLYGONCONVERSIONFLAGS.numerator.md)
- [maxon.POLYGONCONVERSIONFLAGS.real](../modules/maxon_generated/enums/maxon.POLYGONCONVERSIONFLAGS.real.md)
- [maxon.PORT_DIR.BEGIN](../modules/maxon_generated/enums/maxon.PORT_DIR.BEGIN.md)
- [maxon.PORT_DIR.END](../modules/maxon_generated/enums/maxon.PORT_DIR.END.md)
- [maxon.PORT_DIR.INPUT](../modules/maxon_generated/enums/maxon.PORT_DIR.INPUT.md)
- [maxon.PORT_DIR.OUTPUT](../modules/maxon_generated/enums/maxon.PORT_DIR.OUTPUT.md)
- [maxon.PORT_DIR](../modules/maxon_generated/enums/maxon.PORT_DIR.md)
- [maxon.RESAMPLEINTERPOLATIONTYPE.LINEAR](../modules/maxon_generated/enums/maxon.RESAMPLEINTERPOLATIONTYPE.LINEAR.md)
- [maxon.RESAMPLEINTERPOLATIONTYPE.NEAREST](../modules/maxon_generated/enums/maxon.RESAMPLEINTERPOLATIONTYPE.NEAREST.md)
- [maxon.RESAMPLEINTERPOLATIONTYPE.NONE](../modules/maxon_generated/enums/maxon.RESAMPLEINTERPOLATIONTYPE.NONE.md)
- [maxon.RESAMPLEINTERPOLATIONTYPE.QUADRATIC](../modules/maxon_generated/enums/maxon.RESAMPLEINTERPOLATIONTYPE.QUADRATIC.md)
- [maxon.RESAMPLEINTERPOLATIONTYPE.denominator](../modules/maxon_generated/enums/maxon.RESAMPLEINTERPOLATIONTYPE.denominator.md)
- [maxon.RESAMPLEINTERPOLATIONTYPE.imag](../modules/maxon_generated/enums/maxon.RESAMPLEINTERPOLATIONTYPE.imag.md)
- [maxon.RESAMPLEINTERPOLATIONTYPE](../modules/maxon_generated/enums/maxon.RESAMPLEINTERPOLATIONTYPE.md): int([x]) -> integer int(x, base=10) -> integer
- [maxon.RESAMPLEINTERPOLATIONTYPE.numerator](../modules/maxon_generated/enums/maxon.RESAMPLEINTERPOLATIONTYPE.numerator.md)
- [maxon.RESAMPLEINTERPOLATIONTYPE.real](../modules/maxon_generated/enums/maxon.RESAMPLEINTERPOLATIONTYPE.real.md)
- [maxon.SDFFILTERTYPE.CLOSE](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.CLOSE.md)
- [maxon.SDFFILTERTYPE.DILATE](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.DILATE.md)
- [maxon.SDFFILTERTYPE.ERODE](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.ERODE.md)
- [maxon.SDFFILTERTYPE.GAUSSIAN](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.GAUSSIAN.md)
- [maxon.SDFFILTERTYPE.LAPLACIANFLOW](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.LAPLACIANFLOW.md)
- [maxon.SDFFILTERTYPE.MEANCURVATURE](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.MEANCURVATURE.md)
- [maxon.SDFFILTERTYPE.MEANVALUE](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.MEANVALUE.md)
- [maxon.SDFFILTERTYPE.MEDIANVALUE](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.MEDIANVALUE.md)
- [maxon.SDFFILTERTYPE.NONE](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.NONE.md)
- [maxon.SDFFILTERTYPE.OPEN](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.OPEN.md)
- [maxon.SDFFILTERTYPE.RENORMALIZE](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.RENORMALIZE.md)
- [maxon.SDFFILTERTYPE.RESIZE](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.RESIZE.md)
- [maxon.SDFFILTERTYPE.TRACK](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.TRACK.md)
- [maxon.SDFFILTERTYPE.denominator](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.denominator.md)
- [maxon.SDFFILTERTYPE.imag](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.imag.md)
- [maxon.SDFFILTERTYPE](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.md): int([x]) -> integer int(x, base=10) -> integer
- [maxon.SDFFILTERTYPE.numerator](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.numerator.md)
- [maxon.SDFFILTERTYPE.real](../modules/maxon_generated/enums/maxon.SDFFILTERTYPE.real.md)
- [maxon.VOLUMESAMPLER.LINEAR](../modules/maxon_generated/enums/maxon.VOLUMESAMPLER.LINEAR.md)
- [maxon.VOLUMESAMPLER.NEAREST](../modules/maxon_generated/enums/maxon.VOLUMESAMPLER.NEAREST.md)
- [maxon.VOLUMESAMPLER.QUADRATIC](../modules/maxon_generated/enums/maxon.VOLUMESAMPLER.QUADRATIC.md)
- [maxon.VOLUMESAMPLER.denominator](../modules/maxon_generated/enums/maxon.VOLUMESAMPLER.denominator.md)
- [maxon.VOLUMESAMPLER.imag](../modules/maxon_generated/enums/maxon.VOLUMESAMPLER.imag.md)
- [maxon.VOLUMESAMPLER](../modules/maxon_generated/enums/maxon.VOLUMESAMPLER.md): int([x]) -> integer int(x, base=10) -> integer
- [maxon.VOLUMESAMPLER.numerator](../modules/maxon_generated/enums/maxon.VOLUMESAMPLER.numerator.md)
- [maxon.VOLUMESAMPLER.real](../modules/maxon_generated/enums/maxon.VOLUMESAMPLER.real.md)
- [maxon.WIRE_MODE.ALL](../modules/maxon_generated/enums/maxon.WIRE_MODE.ALL.md)
- [maxon.WIRE_MODE.ALL_INCLUDING_IMPLICIT](../modules/maxon_generated/enums/maxon.WIRE_MODE.ALL_INCLUDING_IMPLICIT.md)
- [maxon.WIRE_MODE.AMBIGUOUS](../modules/maxon_generated/enums/maxon.WIRE_MODE.AMBIGUOUS.md)
- [maxon.WIRE_MODE.AUTO_PROPAGATION](../modules/maxon_generated/enums/maxon.WIRE_MODE.AUTO_PROPAGATION.md)
- [maxon.WIRE_MODE.CONNECT_DEFAULT](../modules/maxon_generated/enums/maxon.WIRE_MODE.CONNECT_DEFAULT.md)
- [maxon.WIRE_MODE.FLAG0](../modules/maxon_generated/enums/maxon.WIRE_MODE.FLAG0.md)
- [maxon.WIRE_MODE.FLAG1](../modules/maxon_generated/enums/maxon.WIRE_MODE.FLAG1.md)
- [maxon.WIRE_MODE.FLAGS_MASK](../modules/maxon_generated/enums/maxon.WIRE_MODE.FLAGS_MASK.md)
- [maxon.WIRE_MODE.FULL_MASK](../modules/maxon_generated/enums/maxon.WIRE_MODE.FULL_MASK.md)
- [maxon.WIRE_MODE.GETCONNECTIONS_DEFAULT](../modules/maxon_generated/enums/maxon.WIRE_MODE.GETCONNECTIONS_DEFAULT.md)
- [maxon.WIRE_MODE.IMPLICIT](../modules/maxon_generated/enums/maxon.WIRE_MODE.IMPLICIT.md)
- [maxon.WIRE_MODE.INHERIT](../modules/maxon_generated/enums/maxon.WIRE_MODE.INHERIT.md)
- [maxon.WIRE_MODE.MAX](../modules/maxon_generated/enums/maxon.WIRE_MODE.MAX.md)
- [maxon.WIRE_MODE.MIN](../modules/maxon_generated/enums/maxon.WIRE_MODE.MIN.md)
- [maxon.WIRE_MODE.NONE](../modules/maxon_generated/enums/maxon.WIRE_MODE.NONE.md)
- [maxon.WIRE_MODE.NORMAL](../modules/maxon_generated/enums/maxon.WIRE_MODE.NORMAL.md)
- [maxon.WIRE_MODE.PRIORITY_MASK](../modules/maxon_generated/enums/maxon.WIRE_MODE.PRIORITY_MASK.md)
- [maxon.WIRE_MODE.PROPAGATION](../modules/maxon_generated/enums/maxon.WIRE_MODE.PROPAGATION.md)
- [maxon.WIRE_MODE.REMOVE](../modules/maxon_generated/enums/maxon.WIRE_MODE.REMOVE.md)
- [maxon.WIRE_MODE](../modules/maxon_generated/enums/maxon.WIRE_MODE.md)

## modules/maxon_generated/frameworks/asset/datatype

- [maxon.AddAssetDepencendyStruct](../modules/maxon_generated/frameworks/asset/datatype/maxon.AddAssetDepencendyStruct.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.AssetDatabaseStruct](../modules/maxon_generated/frameworks/asset/datatype/maxon.AssetDatabaseStruct.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.AssetDependencyStruct.assetCreationDate](../modules/maxon_generated/frameworks/asset/datatype/maxon.AssetDependencyStruct.assetCreationDate.md)
- [maxon.AssetDependencyStruct.assetIdAndVersion](../modules/maxon_generated/frameworks/asset/datatype/maxon.AssetDependencyStruct.assetIdAndVersion.md)
- [maxon.AssetDependencyStruct.assetTypeId](../modules/maxon_generated/frameworks/asset/datatype/maxon.AssetDependencyStruct.assetTypeId.md)
- [maxon.AssetDependencyStruct](../modules/maxon_generated/frameworks/asset/datatype/maxon.AssetDependencyStruct.md): Helper class to pass several arguments into asset creation functions.
- [maxon.AssetDependencyStruct.originalName](../modules/maxon_generated/frameworks/asset/datatype/maxon.AssetDependencyStruct.originalName.md)
- [maxon.AssetDependencyStruct.updatePolicy](../modules/maxon_generated/frameworks/asset/datatype/maxon.AssetDependencyStruct.updatePolicy.md)
- [maxon.DragAndDropDataAssetArray](../modules/maxon_generated/frameworks/asset/datatype/maxon.DragAndDropDataAssetArray.md): Message data for DRAGTYPE_ASSET
- [maxon.ResolveAssetDependenciesStruct](../modules/maxon_generated/frameworks/asset/datatype/maxon.ResolveAssetDependenciesStruct.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.StoreAssetStruct](../modules/maxon_generated/frameworks/asset/datatype/maxon.StoreAssetStruct.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).

## modules/maxon_generated/frameworks/asset/functions

- [maxon.GetAssetUrl](../modules/maxon_generated/frameworks/asset/functions/maxon.GetAssetUrl.md)
- [maxon.IdAndVersionToId](../modules/maxon_generated/frameworks/asset/functions/maxon.IdAndVersionToId.md)
- [maxon.IdAndVersionToIdWithRepository](../modules/maxon_generated/frameworks/asset/functions/maxon.IdAndVersionToIdWithRepository.md)
- [maxon.IdToIdAndVersion](../modules/maxon_generated/frameworks/asset/functions/maxon.IdToIdAndVersion.md)
- [maxon.IdToIdAndVersionWithRepository](../modules/maxon_generated/frameworks/asset/functions/maxon.IdToIdAndVersionWithRepository.md)
- [maxon.UpdateAssetUsage](../modules/maxon_generated/frameworks/asset/functions/maxon.UpdateAssetUsage.md)

## modules/maxon_generated/frameworks/asset/interface

- [maxon.AssetBaseInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetBaseInterface.VIRTUAL.md)
- [maxon.AssetBaseInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetBaseInterface.md): The base interface of maxon.AssetBaseWithUpdateInterface and maxon.AssetDescriptionInterface.
- [maxon.AssetBaseWithUpdateInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetBaseWithUpdateInterface.VIRTUAL.md)
- [maxon.AssetBaseWithUpdateInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetBaseWithUpdateInterface.md): The base interface of maxon.AssetInterface and maxon.AssetReferenceInterface.
- [maxon.AssetDataBasesInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetDataBasesInterface.md): This interface provides helper functions to register asset repositories.
- [maxon.AssetDescriptionInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetDescriptionInterface.VIRTUAL.md)
- [maxon.AssetDescriptionInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetDescriptionInterface.md): Represents all meta information about an asset, namely its identifier and version, the maxon.AssetMetaData and some further information.
- [maxon.AssetIdentifierInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetIdentifierInterface.VIRTUAL.md)
- [maxon.AssetIdentifierInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetIdentifierInterface.md): The base interface of maxon.AssetBaseInterface and maxon.AssetLinkInterface.
- [maxon.AssetInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetInterface.VIRTUAL.md)
- [maxon.AssetInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetInterface.md): An Asset represents digital content which can be managed by an maxon.AssetRepositoryRef “asset repository”.
- [maxon.AssetLinkInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetLinkInterface.VIRTUAL.md)
- [maxon.AssetLinkInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetLinkInterface.md): An AssetLink is a symbolic link to an asset identified by its id and version.
- [maxon.AssetMetaDataInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetMetaDataInterface.md): maxon.AssetMetaData allows to query the meta data of an asset.
- [maxon.AssetReferenceInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetReferenceInterface.VIRTUAL.md)
- [maxon.AssetReferenceInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetReferenceInterface.md): maxon.AssetReference is needed for the asset update mechanism and represents a specific updatable maxon.AssetLink within an asset, see AssetInterface.GetRefere…
- [maxon.AssetRepositoryInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetRepositoryInterface.md): An AssetRepositoryInterface manages a set of assets: - Assets can be looked up using their identifier and version.
- [maxon.AssetTypeInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetTypeInterface.md): Class to store and find any maxon.Data type under any type of key.
- [maxon.AssetUtilitiesInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.AssetUtilitiesInterface.md): Helper Interface for Asset functions.
- [maxon.BasePresetAssetInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.BasePresetAssetInterface.VIRTUAL.md)
- [maxon.BasePresetAssetInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.BasePresetAssetInterface.md): maxon.BasePresetAssetInterface allows to implement details for preset assets.
- [maxon.BasePresetAssetTypeInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.BasePresetAssetTypeInterface.md): Defines a new preset type and is the connector to BasePresetAssetInterface
- [maxon.CategoryAssetInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.CategoryAssetInterface.VIRTUAL.md)
- [maxon.CategoryAssetInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.CategoryAssetInterface.md): Implementation of category assets
- [maxon.ColorCategoryAssetInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.ColorCategoryAssetInterface.VIRTUAL.md)
- [maxon.ColorCategoryAssetInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.ColorCategoryAssetInterface.md): Implementation of a color category asset.
- [maxon.CompactableAssetRepositoryInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.CompactableAssetRepositoryInterface.md): Repository which allows to write an index.
- [maxon.DataDescriptionPresetStorageInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.DataDescriptionPresetStorageInterface.md): Helper class to handle loading and saving of presets.
- [maxon.DatabaseAssetInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.DatabaseAssetInterface.VIRTUAL.md)
- [maxon.DatabaseAssetInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.DatabaseAssetInterface.md): Implementation of DatabaseAsset.
- [maxon.DerivedAssetRepositoryDataInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.DerivedAssetRepositoryDataInterface.md)
- [maxon.FileAssetInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.FileAssetInterface.VIRTUAL.md)
- [maxon.FileAssetInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.FileAssetInterface.md): An Asset represents digital content which can be managed by an maxon.AssetRepositoryRef “asset repository”.
- [maxon.KeywordAssetInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.KeywordAssetInterface.VIRTUAL.md)
- [maxon.KeywordAssetInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.KeywordAssetInterface.md): An Asset represents digital content which can be managed by an maxon.AssetRepositoryRef “asset repository”.
- [maxon.LazyLanguageDictionaryInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.LazyLanguageDictionaryInterface.md): Interface to manage lazy loading of maxon.LanguageDictionary for description strings.
- [maxon.LazyLanguageStringDataDescriptionDefinitionInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.LazyLanguageStringDataDescriptionDefinitionInterface.md): Interface to manage lazy loading of maxon.LanguageStringDataDescriptionDefinition for description strings.
- [maxon.NodeSpaceAssetInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.NodeSpaceAssetInterface.VIRTUAL.md)
- [maxon.NodeSpaceAssetInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.NodeSpaceAssetInterface.md): Implementation of NodeSpaceAssets
- [maxon.PluginAssetInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.PluginAssetInterface.VIRTUAL.md)
- [maxon.PluginAssetInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.PluginAssetInterface.md): Implements the PluginAsset type
- [maxon.SmartSearchAssetInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.SmartSearchAssetInterface.VIRTUAL.md)
- [maxon.SmartSearchAssetInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.SmartSearchAssetInterface.md): Implements the smartsearch asset type.
- [maxon.SubTypeAssetInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.SubTypeAssetInterface.VIRTUAL.md)
- [maxon.SubTypeAssetInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.SubTypeAssetInterface.md): Implements the SubTypeAsset.
- [maxon.UpdatableAssetInterface.VIRTUAL](../modules/maxon_generated/frameworks/asset/interface/maxon.UpdatableAssetInterface.VIRTUAL.md)
- [maxon.UpdatableAssetInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.UpdatableAssetInterface.md): An maxon.UpdatableAsset is an maxon.Asset which supports the update of its updatable references to other assets to newer versions.
- [maxon.UpdatableAssetRepositoryInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.UpdatableAssetRepositoryInterface.md): Asset repository which allows to update assets.
- [maxon.UrlAssetRepositoryInterface](../modules/maxon_generated/frameworks/asset/interface/maxon.UrlAssetRepositoryInterface.md): Asset repository which allows to update assets.

## modules/maxon_generated/frameworks/asset/reference

- [maxon.Asset.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.Asset.VIRTUAL.md)
- [maxon.Asset](../modules/maxon_generated/frameworks/asset/reference/maxon.Asset.md): Represents a reference of a maxon.AssetInterface
- [maxon.AssetBase.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetBase.VIRTUAL.md)
- [maxon.AssetBase](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetBase.md): Represents a reference of a maxon.AssetBaseInterface
- [maxon.AssetBaseWithUpdate.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetBaseWithUpdate.VIRTUAL.md)
- [maxon.AssetBaseWithUpdate](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetBaseWithUpdate.md): Represents a reference of a maxon.AssetBaseWithUpdateInterface
- [maxon.AssetDescription.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetDescription.VIRTUAL.md)
- [maxon.AssetDescription](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetDescription.md): Represents a reference of a maxon.AssetDescriptionInterface
- [maxon.AssetIdentifier.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetIdentifier.VIRTUAL.md)
- [maxon.AssetIdentifier](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetIdentifier.md): Represents a reference of a maxon.AssetIdentifierInterface
- [maxon.AssetLink.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetLink.VIRTUAL.md)
- [maxon.AssetLink](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetLink.md): Represents a reference of a maxon.AssetLinkInterface
- [maxon.AssetMetaData](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetMetaData.md): Represents a reference of a maxon.AssetMetaDataInterface
- [maxon.AssetReference.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetReference.VIRTUAL.md)
- [maxon.AssetReference](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetReference.md): Represents a reference of a maxon.AssetReferenceInterface
- [maxon.AssetRepositoryRef](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetRepositoryRef.md): Represents a reference of a maxon.AssetRepositoryInterface
- [maxon.AssetType](../modules/maxon_generated/frameworks/asset/reference/maxon.AssetType.md): Represents a reference of a maxon.AssetTypeInterface
- [maxon.BasePresetAsset.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.BasePresetAsset.VIRTUAL.md)
- [maxon.BasePresetAsset](../modules/maxon_generated/frameworks/asset/reference/maxon.BasePresetAsset.md): Represents a reference of a maxon.BasePresetAssetInterface
- [maxon.BasePresetAssetType](../modules/maxon_generated/frameworks/asset/reference/maxon.BasePresetAssetType.md): Represents a reference of a maxon.BasePresetAssetTypeInterface
- [maxon.CategoryAsset.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.CategoryAsset.VIRTUAL.md)
- [maxon.CategoryAsset](../modules/maxon_generated/frameworks/asset/reference/maxon.CategoryAsset.md): Represents a reference of a maxon.CategoryAssetInterface
- [maxon.ColorCategoryAsset.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.ColorCategoryAsset.VIRTUAL.md)
- [maxon.ColorCategoryAsset](../modules/maxon_generated/frameworks/asset/reference/maxon.ColorCategoryAsset.md): Represents a reference of a maxon.ColorCategoryAssetInterface
- [maxon.CompactableAssetRepositoryRef](../modules/maxon_generated/frameworks/asset/reference/maxon.CompactableAssetRepositoryRef.md): Represents a reference of a maxon.CompactableAssetRepositoryInterface
- [maxon.DatabaseAsset.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.DatabaseAsset.VIRTUAL.md)
- [maxon.DatabaseAsset](../modules/maxon_generated/frameworks/asset/reference/maxon.DatabaseAsset.md): Represents a reference of a maxon.DatabaseAssetInterface
- [maxon.DerivedAssetRepositoryDataRef](../modules/maxon_generated/frameworks/asset/reference/maxon.DerivedAssetRepositoryDataRef.md): Represents a reference of a maxon.DerivedAssetRepositoryDataInterface
- [maxon.FileAsset.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.FileAsset.VIRTUAL.md)
- [maxon.FileAsset](../modules/maxon_generated/frameworks/asset/reference/maxon.FileAsset.md): Represents a reference of a maxon.FileAssetInterface
- [maxon.KeywordAsset.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.KeywordAsset.VIRTUAL.md)
- [maxon.KeywordAsset](../modules/maxon_generated/frameworks/asset/reference/maxon.KeywordAsset.md): Represents a reference of a maxon.KeywordAssetInterface
- [maxon.LazyLanguageDictionary](../modules/maxon_generated/frameworks/asset/reference/maxon.LazyLanguageDictionary.md): Represents a reference of a maxon.LazyLanguageDictionaryInterface
- [maxon.LazyLanguageStringDataDescriptionDefinition](../modules/maxon_generated/frameworks/asset/reference/maxon.LazyLanguageStringDataDescriptionDefinition.md): Represents a reference of a maxon.LazyLanguageStringDataDescriptionDefinitionInterface
- [maxon.NodeSpaceAsset.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.NodeSpaceAsset.VIRTUAL.md)
- [maxon.NodeSpaceAsset](../modules/maxon_generated/frameworks/asset/reference/maxon.NodeSpaceAsset.md): Represents a reference of a maxon.NodeSpaceAssetInterface
- [maxon.PluginAsset.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.PluginAsset.VIRTUAL.md)
- [maxon.PluginAsset](../modules/maxon_generated/frameworks/asset/reference/maxon.PluginAsset.md): Represents a reference of a maxon.PluginAssetInterface
- [maxon.SmartSearchAsset.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.SmartSearchAsset.VIRTUAL.md)
- [maxon.SmartSearchAsset](../modules/maxon_generated/frameworks/asset/reference/maxon.SmartSearchAsset.md): Represents a reference of a maxon.SmartSearchAssetInterface
- [maxon.SubTypeAsset.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.SubTypeAsset.VIRTUAL.md)
- [maxon.SubTypeAsset](../modules/maxon_generated/frameworks/asset/reference/maxon.SubTypeAsset.md): Represents a reference of a maxon.SubTypeAssetInterface
- [maxon.UpdatableAsset.VIRTUAL](../modules/maxon_generated/frameworks/asset/reference/maxon.UpdatableAsset.VIRTUAL.md)
- [maxon.UpdatableAsset](../modules/maxon_generated/frameworks/asset/reference/maxon.UpdatableAsset.md): Represents a reference of a maxon.UpdatableAssetInterface
- [maxon.UpdatableAssetRepositoryRef](../modules/maxon_generated/frameworks/asset/reference/maxon.UpdatableAssetRepositoryRef.md): Represents a reference of a maxon.UpdatableAssetRepositoryInterface
- [maxon.UrlAssetRepositoryRef](../modules/maxon_generated/frameworks/asset/reference/maxon.UrlAssetRepositoryRef.md): Represents a reference of a maxon.UrlAssetRepositoryInterface

## modules/maxon_generated/frameworks/asset/registry

- [maxon.AssetTypes.BPBrushPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.BPBrushPreset.md)
- [maxon.AssetTypes.BPColorPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.BPColorPreset.md)
- [maxon.AssetTypes.BPGradientPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.BPGradientPreset.md)
- [maxon.AssetTypes.CameraFXPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.CameraFXPreset.md)
- [maxon.AssetTypes.CameraSensorPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.CameraSensorPreset.md)
- [maxon.AssetTypes.CapsAndBevelPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.CapsAndBevelPreset.md)
- [maxon.AssetTypes.Category](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.Category.md)
- [maxon.AssetTypes.CharacterDefinitionPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.CharacterDefinitionPreset.md)
- [maxon.AssetTypes.ColorCategory](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.ColorCategory.md)
- [maxon.AssetTypes.ColorSwatchPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.ColorSwatchPreset.md)
- [maxon.AssetTypes.Command](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.Command.md)
- [maxon.AssetTypes.Database](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.Database.md)
- [maxon.AssetTypes.DefaultsPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.DefaultsPreset.md)
- [maxon.AssetTypes.DisplayFilterPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.DisplayFilterPreset.md)
- [maxon.AssetTypes.DocumentPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.DocumentPreset.md)
- [maxon.AssetTypes.Entity](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.Entity.md)
- [maxon.AssetTypes.ExchangeSettingsPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.ExchangeSettingsPreset.md)
- [maxon.AssetTypes.File](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.File.md)
- [maxon.AssetTypes.GradientPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.GradientPreset.md)
- [maxon.AssetTypes.IconChooserPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.IconChooserPreset.md)
- [maxon.AssetTypes.Keyword](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.Keyword.md)
- [maxon.AssetTypes.MotionSequencePreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.MotionSequencePreset.md)
- [maxon.AssetTypes.NodeContext](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.NodeContext.md)
- [maxon.AssetTypes.NodeDefaultsPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.NodeDefaultsPreset.md)
- [maxon.AssetTypes.NodeDescription](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.NodeDescription.md)
- [maxon.AssetTypes.NodeSpace](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.NodeSpace.md)
- [maxon.AssetTypes.NodeTemplate](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.NodeTemplate.md)
- [maxon.AssetTypes.PictureViewerPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.PictureViewerPreset.md)
- [maxon.AssetTypes.Plugin](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.Plugin.md)
- [maxon.AssetTypes.Poselib](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.Poselib.md)
- [maxon.AssetTypes.Preset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.Preset.md)
- [maxon.AssetTypes.RenderQueuePreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.RenderQueuePreset.md)
- [maxon.AssetTypes.RenderSettingsPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.RenderSettingsPreset.md)
- [maxon.AssetTypes.ResourceEditorDefaultsPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.ResourceEditorDefaultsPreset.md)
- [maxon.AssetTypes.SculptBrushPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.SculptBrushPreset.md)
- [maxon.AssetTypes.SculptSplinePreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.SculptSplinePreset.md)
- [maxon.AssetTypes.SculptStampPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.SculptStampPreset.md)
- [maxon.AssetTypes.SculptStencilPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.SculptStencilPreset.md)
- [maxon.AssetTypes.SketchPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.SketchPreset.md)
- [maxon.AssetTypes.SkyLayerPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.SkyLayerPreset.md)
- [maxon.AssetTypes.SkyPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.SkyPreset.md)
- [maxon.AssetTypes.SkyWeatherPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.SkyWeatherPreset.md)
- [maxon.AssetTypes.SmartSearch](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.SmartSearch.md)
- [maxon.AssetTypes.SplinePreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.SplinePreset.md)
- [maxon.AssetTypes.SubType](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.SubType.md)
- [maxon.AssetTypes.TakePreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.TakePreset.md)
- [maxon.AssetTypes.TimelineDefinitionPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.TimelineDefinitionPreset.md)
- [maxon.AssetTypes.UserDataPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.UserDataPreset.md)
- [maxon.AssetTypes.VideoPostPreset](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.VideoPostPreset.md)
- [maxon.AssetTypes](../modules/maxon_generated/frameworks/asset/registry/maxon.AssetTypes.md)
- [maxon.PresetAssetImplementations.BPBrushPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.BPBrushPresetClass.md)
- [maxon.PresetAssetImplementations.BPColorPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.BPColorPresetClass.md)
- [maxon.PresetAssetImplementations.BPGradientPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.BPGradientPresetClass.md)
- [maxon.PresetAssetImplementations.CameraFXPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.CameraFXPresetClass.md)
- [maxon.PresetAssetImplementations.CameraSensorPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.CameraSensorPresetClass.md)
- [maxon.PresetAssetImplementations.CapsAndBevelPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.CapsAndBevelPresetClass.md)
- [maxon.PresetAssetImplementations.CharacterDefinitionPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.CharacterDefinitionPresetClass.md)
- [maxon.PresetAssetImplementations.ColorSwatchPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.ColorSwatchPresetClass.md)
- [maxon.PresetAssetImplementations.DefaultsPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.DefaultsPresetClass.md)
- [maxon.PresetAssetImplementations.DisplayFilterPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.DisplayFilterPresetClass.md)
- [maxon.PresetAssetImplementations.DocumentPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.DocumentPresetClass.md)
- [maxon.PresetAssetImplementations.ExchangeSettingsPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.ExchangeSettingsPresetClass.md)
- [maxon.PresetAssetImplementations.GradientPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.GradientPresetClass.md)
- [maxon.PresetAssetImplementations.IconChooserPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.IconChooserPresetClass.md)
- [maxon.PresetAssetImplementations.MotionSequencePresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.MotionSequencePresetClass.md)
- [maxon.PresetAssetImplementations.NodeDefaultsPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.NodeDefaultsPresetClass.md)
- [maxon.PresetAssetImplementations.PictureViewerPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.PictureViewerPresetClass.md)
- [maxon.PresetAssetImplementations.RenderQueuePresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.RenderQueuePresetClass.md)
- [maxon.PresetAssetImplementations.RenderSettingsPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.RenderSettingsPresetClass.md)
- [maxon.PresetAssetImplementations.ResourceEditorDefaultsPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.ResourceEditorDefaultsPresetClass.md)
- [maxon.PresetAssetImplementations.SculptBrushPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.SculptBrushPresetClass.md)
- [maxon.PresetAssetImplementations.SculptSplinePresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.SculptSplinePresetClass.md)
- [maxon.PresetAssetImplementations.SculptStampPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.SculptStampPresetClass.md)
- [maxon.PresetAssetImplementations.SculptStencilPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.SculptStencilPresetClass.md)
- [maxon.PresetAssetImplementations.SketchPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.SketchPresetClass.md)
- [maxon.PresetAssetImplementations.SkyLayerPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.SkyLayerPresetClass.md)
- [maxon.PresetAssetImplementations.SkyPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.SkyPresetClass.md)
- [maxon.PresetAssetImplementations.SkyWeatherPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.SkyWeatherPresetClass.md)
- [maxon.PresetAssetImplementations.SplinePresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.SplinePresetClass.md)
- [maxon.PresetAssetImplementations.TakePresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.TakePresetClass.md)
- [maxon.PresetAssetImplementations.TimelineDefinitionPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.TimelineDefinitionPresetClass.md)
- [maxon.PresetAssetImplementations.UserDataPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.UserDataPresetClass.md)
- [maxon.PresetAssetImplementations.VideoPostPresetClass](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.VideoPostPresetClass.md)
- [maxon.PresetAssetImplementations](../modules/maxon_generated/frameworks/asset/registry/maxon.PresetAssetImplementations.md)

## modules/maxon_generated/frameworks/cinema_hybrid/interface

- [maxon.AssetCreationInterface](../modules/maxon_generated/frameworks/cinema_hybrid/interface/maxon.AssetCreationInterface.md): Helper interface for asset creation and drag&drop
- [maxon.AssetManagerInterface](../modules/maxon_generated/frameworks/cinema_hybrid/interface/maxon.AssetManagerInterface.md): Helper class to control the Asset Manager.

## modules/maxon_generated/frameworks/graph/datatype

- [maxon.GraphNode](../modules/maxon_generated/frameworks/graph/datatype/maxon.GraphNode.md): A maxon.GraphNode represents a general node (g-node for short) in the hierarchy of a maxon.GraphModelInterface.
- [maxon.GraphTransaction](../modules/maxon_generated/frameworks/graph/datatype/maxon.GraphTransaction.md): Modifications to a GraphModelInterface may only be done when there is an active GraphTransaction.
- [maxon.NodePath.INPUTS](../modules/maxon_generated/frameworks/graph/datatype/maxon.NodePath.INPUTS.md)
- [maxon.NodePath.OUTPUTS](../modules/maxon_generated/frameworks/graph/datatype/maxon.NodePath.OUTPUTS.md)
- [maxon.NodePath.TEMPLATE](../modules/maxon_generated/frameworks/graph/datatype/maxon.NodePath.TEMPLATE.md)
- [maxon.NodePath](../modules/maxon_generated/frameworks/graph/datatype/maxon.NodePath.md): Reference class for maxon.NodePathInterface.
- [maxon.Wires.context](../modules/maxon_generated/frameworks/graph/datatype/maxon.Wires.CONTEXT.md)
- [maxon.Wires.COUNT](../modules/maxon_generated/frameworks/graph/datatype/maxon.Wires.COUNT.md)
- [maxon.Wires.dependency](../modules/maxon_generated/frameworks/graph/datatype/maxon.Wires.DEPENDENCY.md)
- [maxon.Wires.event](../modules/maxon_generated/frameworks/graph/datatype/maxon.Wires.EVENT.md)
- [maxon.Wires.hidden](../modules/maxon_generated/frameworks/graph/datatype/maxon.Wires.HIDDEN.md)
- [maxon.Wires.inhibit](../modules/maxon_generated/frameworks/graph/datatype/maxon.Wires.INHIBIT.md)
- [maxon.Wires.NONE](../modules/maxon_generated/frameworks/graph/datatype/maxon.Wires.NONE.md)
- [maxon.Wires.slink](../modules/maxon_generated/frameworks/graph/datatype/maxon.Wires.SLINK.md)
- [maxon.Wires.tlink](../modules/maxon_generated/frameworks/graph/datatype/maxon.Wires.TLINK.md)
- [maxon.Wires.value](../modules/maxon_generated/frameworks/graph/datatype/maxon.Wires.VALUE.md)
- [maxon.Wires](../modules/maxon_generated/frameworks/graph/datatype/maxon.Wires.md): In most cases you only need a combination of a value, event and dependency wire.

## modules/maxon_generated/frameworks/graph/interface

- [maxon.GraphAttributeInterface](../modules/maxon_generated/frameworks/graph/interface/maxon.GraphAttributeInterface.md)
- [maxon.GraphLib](../modules/maxon_generated/frameworks/graph/interface/maxon.GraphLib.md): GraphLib contains some static functions for graphs.
- [maxon.GraphMessageInterface](../modules/maxon_generated/frameworks/graph/interface/maxon.GraphMessageInterface.md)
- [maxon.GraphModelHelper](../modules/maxon_generated/frameworks/graph/interface/maxon.GraphModelHelper.md): Regroups functions to simplify the usage of the node API.
- [maxon.GraphModelInterface](../modules/maxon_generated/frameworks/graph/interface/maxon.GraphModelInterface.md)
- [maxon.NodePathInterface.INPUTS](../modules/maxon_generated/frameworks/graph/interface/maxon.NodePathInterface.INPUTS.md)
- [maxon.NodePathInterface.OUTPUTS](../modules/maxon_generated/frameworks/graph/interface/maxon.NodePathInterface.OUTPUTS.md)
- [maxon.NodePathInterface.TEMPLATE](../modules/maxon_generated/frameworks/graph/interface/maxon.NodePathInterface.TEMPLATE.md)
- [maxon.NodePathInterface](../modules/maxon_generated/frameworks/graph/interface/maxon.NodePathInterface.md)

## modules/maxon_generated/frameworks/graph/reference

- [maxon.GraphAttribute](../modules/maxon_generated/frameworks/graph/reference/maxon.GraphAttribute.md): Reference class for maxon.GraphAttributeInterface.
- [maxon.GraphMessage](../modules/maxon_generated/frameworks/graph/reference/maxon.GraphMessage.md): Reference class for maxon.GraphMessageInterface.
- [maxon.GraphModelRef](../modules/maxon_generated/frameworks/graph/reference/maxon.GraphModelRef.md): Reference class for maxon.GraphModelInterface.

## modules/maxon_generated/frameworks/mesh_misc/datatype

- [maxon.MeshAttribute](../modules/maxon_generated/frameworks/mesh_misc/datatype/maxon.MeshAttribute.md)

## modules/maxon_generated/frameworks/mesh_misc/decorator

- [maxon.MAXON_MESHATTRIBUTE](../modules/maxon_generated/frameworks/mesh_misc/decorator/maxon.MAXON_MESHATTRIBUTE.md)

## modules/maxon_generated/frameworks/mesh_misc/interface

- [maxon.CustomDataTagClassInterface](../modules/maxon_generated/frameworks/mesh_misc/interface/maxon.CustomDataTagClassInterface.md)
- [maxon.CustomDataTagDisplayInterface](../modules/maxon_generated/frameworks/mesh_misc/interface/maxon.CustomDataTagDisplayInterface.md): maxon.CustomDataTagDisplayInterface can be optionally implemented for each maxon.CustomDataTagClassInterface implementation and defines if and how a c4d.Custom…
- [maxon.MeshAttributeClassInterface](../modules/maxon_generated/frameworks/mesh_misc/interface/maxon.MeshAttributeClassInterface.md)

## modules/maxon_generated/frameworks/mesh_misc/reference

- [maxon.CustomDataTagClass](../modules/maxon_generated/frameworks/mesh_misc/reference/maxon.CustomDataTagClass.md): Represents a reference of a maxon.CustomDataTagClassInterface
- [maxon.CustomDataTagDisplayRef](../modules/maxon_generated/frameworks/mesh_misc/reference/maxon.CustomDataTagDisplayRef.md): Represents a reference of a maxon.CustomDataTagDisplayInterface

## modules/maxon_generated/frameworks/mesh_misc/registry

- [maxon.CustomDataTagDisplayClasses.POLYGROUPDISPLAY](../modules/maxon_generated/frameworks/mesh_misc/registry/maxon.CustomDataTagDisplayClasses.POLYGROUPDISPLAY.md)
- [maxon.CustomDataTagDisplayClasses](../modules/maxon_generated/frameworks/mesh_misc/registry/maxon.CustomDataTagDisplayClasses.md): Registry storing all maxon.CustomDataTagDisplayInterface.

## modules/maxon_generated/frameworks/misc/function

- [maxon.Reverse](../modules/maxon_generated/frameworks/misc/function/maxon.Reverse.md)

## modules/maxon_generated/frameworks/nodes/interface

- [maxon.GraphDescription.ClearSoloNodeCommand](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.ClearSoloNodeCommand.md)
- [maxon.GraphDescription.ClearStartNodeCommand](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.ClearStartNodeCommand.md)
- [maxon.GraphDescription.Commands](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Commands.md)
- [maxon.GraphDescription.Default](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Default.md)
- [maxon.GraphDescription.DefaultCommand](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.DefaultCommand.md)
- [maxon.GraphDescription.Description](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Description.md)
- [maxon.GraphDescription.DisconnectCommand](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.DisconnectCommand.md)
- [maxon.GraphDescription.Enum](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Enum.md)
- [maxon.GraphDescription.Flags](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Flags.md)
- [maxon.GraphDescription.GroupChildren](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.GroupChildren.md)
- [maxon.GraphDescription.HidePortsCommand](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.HidePortsCommand.md)
- [maxon.GraphDescription.Id](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Id.md)
- [maxon.GraphDescription.InputGroup](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.InputGroup.md)
- [maxon.GraphDescription.Language](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Language.md)
- [maxon.GraphDescription.Max](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Max.md)
- [maxon.GraphDescription.Min](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Min.md)
- [maxon.GraphDescription.Ports](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Ports.md)
- [maxon.GraphDescription.Query](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Query.md)
- [maxon.GraphDescription.QueryComposition](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryComposition.md)
- [maxon.GraphDescription.QueryFlags](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryFlags.md)
- [maxon.GraphDescription.QueryMaxError](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryMaxError.md)
- [maxon.GraphDescription.QueryMode](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryMode.md)
- [maxon.GraphDescription.QueryOpAnd](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryOpAnd.md)
- [maxon.GraphDescription.QueryOpEqual](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryOpEqual.md)
- [maxon.GraphDescription.QueryOpGreater](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryOpGreater.md)
- [maxon.GraphDescription.QueryOpGreaterEqual](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryOpGreaterEqual.md)
- [maxon.GraphDescription.QueryOpLess](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryOpLess.md)
- [maxon.GraphDescription.QueryOpLessEqual](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryOpLessEqual.md)
- [maxon.GraphDescription.QueryOpNotEqual](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryOpNotEqual.md)
- [maxon.GraphDescription.QueryOpOr](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryOpOr.md)
- [maxon.GraphDescription.QueryOpRegexMatch](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryOpRegexMatch.md)
- [maxon.GraphDescription.QueryOpRegexSearch](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryOpRegexSearch.md)
- [maxon.GraphDescription.QueryOperator](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryOperator.md)
- [maxon.GraphDescription.QuerySelectPorts](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QuerySelectPorts.md)
- [maxon.GraphDescription.QueryValue](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.QueryValue.md)
- [maxon.GraphDescription.RecursiveUngroupCommand](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.RecursiveUngroupCommand.md)
- [maxon.GraphDescription.RemoveCommand](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.RemoveCommand.md)
- [maxon.GraphDescription.SetPortCountCommand](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.SetPortCountCommand.md)
- [maxon.GraphDescription.ShowPortsCommand](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.ShowPortsCommand.md)
- [maxon.GraphDescription.SoloNodeCommand](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.SoloNodeCommand.md)
- [maxon.GraphDescription.Space](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Space.md)
- [maxon.GraphDescription.StartNodeCommand](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.StartNodeCommand.md)
- [maxon.GraphDescription.Step](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Step.md)
- [maxon.GraphDescription.Type](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.Type.md)
- [maxon.GraphDescription.TypeBool](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.TypeBool.md)
- [maxon.GraphDescription.TypeColor](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.TypeColor.md)
- [maxon.GraphDescription.TypeColorA](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.TypeColorA.md)
- [maxon.GraphDescription.TypeFloat](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.TypeFloat.md)
- [maxon.GraphDescription.TypeId](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.TypeId.md)
- [maxon.GraphDescription.TypeInt](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.TypeInt.md)
- [maxon.GraphDescription.TypeInternedId](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.TypeInternedId.md)
- [maxon.GraphDescription.TypeString](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.TypeString.md)
- [maxon.GraphDescription.TypeUrl](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.TypeUrl.md)
- [maxon.GraphDescription.TypeVector](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.TypeVector.md)
- [maxon.GraphDescription.UngroupCommand](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.UngroupCommand.md)
- [maxon.GraphDescription](../modules/maxon_generated/frameworks/nodes/interface/maxon.GraphDescription.md): Provides functions and constants to read and write node graphs from and into the graph description format.
- [maxon.NodeSystemManagerInterface](../modules/maxon_generated/frameworks/nodes/interface/maxon.NodeSystemManagerInterface.md)
- [maxon.NodesGraphModelInterface](../modules/maxon_generated/frameworks/nodes/interface/maxon.NodesGraphModelInterface.md)

## modules/maxon_generated/frameworks/nodes/reference

- [maxon.NodesGraphModelRef](../modules/maxon_generated/frameworks/nodes/reference/maxon.NodesGraphModelRef.md): Reference class for maxon.GraphModelInterface.

## modules/maxon_generated/frameworks/nodespace/interface

- [maxon.NimbusBaseInterface](../modules/maxon_generated/frameworks/nodespace/interface/maxon.NimbusBaseInterface.md)
- [maxon.NodeSpaceHelpersInterface](../modules/maxon_generated/frameworks/nodespace/interface/maxon.NodeSpaceHelpersInterface.md): Provides a collection of static helpers.

## modules/maxon_generated/frameworks/nodespace/reference

- [maxon.NimbusBaseRef](../modules/maxon_generated/frameworks/nodespace/reference/maxon.NimbusBaseRef.md): Reference class for maxon.NimbusBaseInterface.

## modules/maxon_generated/frameworks/render_filter/interface

- [maxon.FilterCommandQueueInterface](../modules/maxon_generated/frameworks/render_filter/interface/maxon.FilterCommandQueueInterface.md)
- [maxon.FilterContextInterface](../modules/maxon_generated/frameworks/render_filter/interface/maxon.FilterContextInterface.md)
- [maxon.FilterImageInterface](../modules/maxon_generated/frameworks/render_filter/interface/maxon.FilterImageInterface.md)
- [maxon.FilterInterface](../modules/maxon_generated/frameworks/render_filter/interface/maxon.FilterInterface.md)

## modules/maxon_generated/frameworks/render_filter/reference

- [maxon.FilterCommandQueueRef](../modules/maxon_generated/frameworks/render_filter/reference/maxon.FilterCommandQueueRef.md)
- [maxon.FilterContextRef](../modules/maxon_generated/frameworks/render_filter/reference/maxon.FilterContextRef.md)
- [maxon.FilterImageRef](../modules/maxon_generated/frameworks/render_filter/reference/maxon.FilterImageRef.md)
- [maxon.FilterRef](../modules/maxon_generated/frameworks/render_filter/reference/maxon.FilterRef.md)

## modules/maxon_generated/frameworks/render_filter/registry

- [maxon.FilterClasses.OIDNFILTERRT](../modules/maxon_generated/frameworks/render_filter/registry/maxon.FilterClasses.OIDNFILTERRT.md)
- [maxon.FilterClasses](../modules/maxon_generated/frameworks/render_filter/registry/maxon.FilterClasses.md)
- [maxon.FilterCommandQueueClasses.OIDNFILTERCOMMANDQUEUE](../modules/maxon_generated/frameworks/render_filter/registry/maxon.FilterCommandQueueClasses.OIDNFILTERCOMMANDQUEUE.md)
- [maxon.FilterCommandQueueClasses](../modules/maxon_generated/frameworks/render_filter/registry/maxon.FilterCommandQueueClasses.md)
- [maxon.FilterContextClasses.OIDNCONTEXT](../modules/maxon_generated/frameworks/render_filter/registry/maxon.FilterContextClasses.OIDNCONTEXT.md)
- [maxon.FilterContextClasses](../modules/maxon_generated/frameworks/render_filter/registry/maxon.FilterContextClasses.md)
- [maxon.FilterImageClasses.OIDNFILTERIMAGE](../modules/maxon_generated/frameworks/render_filter/registry/maxon.FilterImageClasses.OIDNFILTERIMAGE.md)
- [maxon.FilterImageClasses](../modules/maxon_generated/frameworks/render_filter/registry/maxon.FilterImageClasses.md)

## modules/maxon_generated/frameworks/volume/datatype

- [maxon.FieldSampleData.doc](../modules/maxon_generated/frameworks/volume/datatype/maxon.FieldSampleData.doc.md)
- [maxon.FieldSampleData.extraTransform](../modules/maxon_generated/frameworks/volume/datatype/maxon.FieldSampleData.extraTransform.md)
- [maxon.FieldSampleData.fieldList](../modules/maxon_generated/frameworks/volume/datatype/maxon.FieldSampleData.fieldList.md)
- [maxon.FieldSampleData.fieldOwner](../modules/maxon_generated/frameworks/volume/datatype/maxon.FieldSampleData.fieldOwner.md)
- [maxon.FieldSampleData.flags](../modules/maxon_generated/frameworks/volume/datatype/maxon.FieldSampleData.flags.md)
- [maxon.FieldSampleData](../modules/maxon_generated/frameworks/volume/datatype/maxon.FieldSampleData.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.FieldSampleData.targetRelativeSpace](../modules/maxon_generated/frameworks/volume/datatype/maxon.FieldSampleData.targetRelativeSpace.md)
- [maxon.FilterSettings.filterType](../modules/maxon_generated/frameworks/volume/datatype/maxon.FilterSettings.filterType.md)
- [maxon.FilterSettings.iterations](../modules/maxon_generated/frameworks/volume/datatype/maxon.FilterSettings.iterations.md)
- [maxon.FilterSettings](../modules/maxon_generated/frameworks/volume/datatype/maxon.FilterSettings.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.FilterSettings.offset](../modules/maxon_generated/frameworks/volume/datatype/maxon.FilterSettings.offset.md)
- [maxon.FilterSettings.radius](../modules/maxon_generated/frameworks/volume/datatype/maxon.FilterSettings.radius.md)
- [maxon.FilterSettings.remap_newMax](../modules/maxon_generated/frameworks/volume/datatype/maxon.FilterSettings.remap_newMax.md)
- [maxon.FilterSettings.remap_newMin](../modules/maxon_generated/frameworks/volume/datatype/maxon.FilterSettings.remap_newMin.md)
- [maxon.FilterSettings.remap_oldMax](../modules/maxon_generated/frameworks/volume/datatype/maxon.FilterSettings.remap_oldMax.md)
- [maxon.FilterSettings.remap_oldMin](../modules/maxon_generated/frameworks/volume/datatype/maxon.FilterSettings.remap_oldMin.md)
- [maxon.FilterSettings.splineData](../modules/maxon_generated/frameworks/volume/datatype/maxon.FilterSettings.splineData.md)
- [maxon.FilterSettings.strength](../modules/maxon_generated/frameworks/volume/datatype/maxon.FilterSettings.strength.md)
- [maxon.SDFFilterSettings.accuracy](../modules/maxon_generated/frameworks/volume/datatype/maxon.SDFFilterSettings.accuracy.md)
- [maxon.SDFFilterSettings.filterType](../modules/maxon_generated/frameworks/volume/datatype/maxon.SDFFilterSettings.filterType.md)
- [maxon.SDFFilterSettings.halfWidth](../modules/maxon_generated/frameworks/volume/datatype/maxon.SDFFilterSettings.halfWidth.md)
- [maxon.SDFFilterSettings.iterations](../modules/maxon_generated/frameworks/volume/datatype/maxon.SDFFilterSettings.iterations.md)
- [maxon.SDFFilterSettings](../modules/maxon_generated/frameworks/volume/datatype/maxon.SDFFilterSettings.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.SDFFilterSettings.offset](../modules/maxon_generated/frameworks/volume/datatype/maxon.SDFFilterSettings.offset.md)
- [maxon.SDFFilterSettings.stencilWidth](../modules/maxon_generated/frameworks/volume/datatype/maxon.SDFFilterSettings.stencilWidth.md)
- [maxon.SDFFilterSettings.strength](../modules/maxon_generated/frameworks/volume/datatype/maxon.SDFFilterSettings.strength.md)
- [maxon.VolumeConversionPolygon.a](../modules/maxon_generated/frameworks/volume/datatype/maxon.VolumeConversionPolygon.a.md)
- [maxon.VolumeConversionPolygon.b](../modules/maxon_generated/frameworks/volume/datatype/maxon.VolumeConversionPolygon.b.md)
- [maxon.VolumeConversionPolygon.c](../modules/maxon_generated/frameworks/volume/datatype/maxon.VolumeConversionPolygon.c.md)
- [maxon.VolumeConversionPolygon.d](../modules/maxon_generated/frameworks/volume/datatype/maxon.VolumeConversionPolygon.d.md)
- [maxon.VolumeConversionPolygon](../modules/maxon_generated/frameworks/volume/datatype/maxon.VolumeConversionPolygon.md): Data used, to converts c4d.PolygonObject to a Volume Polygon.
- [maxon.VolumeConversionPolygon.size](../modules/maxon_generated/frameworks/volume/datatype/maxon.VolumeConversionPolygon.size.md)

## modules/maxon_generated/frameworks/volume/interface

- [maxon.GridAccessorCreationInterface](../modules/maxon_generated/frameworks/volume/interface/maxon.GridAccessorCreationInterface.md): Helper class to create the templated interface maxon.GridAccessorInterface.
- [maxon.GridAccessorInterface](../modules/maxon_generated/frameworks/volume/interface/maxon.GridAccessorInterface.md): maxon.GridAccessorInterface allows to access volume data.
- [maxon.PointsToVolumeListInterface](../modules/maxon_generated/frameworks/volume/interface/maxon.PointsToVolumeListInterface.md): Interface to convert point position to a volume.
- [maxon.VolumeInterface](../modules/maxon_generated/frameworks/volume/interface/maxon.VolumeInterface.md): maxon.VolumeInterface represents a core volume object in cinema.
- [maxon.VolumeToolsInterface](../modules/maxon_generated/frameworks/volume/interface/maxon.VolumeToolsInterface.md): maxon.VolumeToolsInterface provides methods to process volumes.

## modules/maxon_generated/frameworks/volume/reference

- [maxon.GridAccessorRef](../modules/maxon_generated/frameworks/volume/reference/maxon.GridAccessorRef.md): Reference class for maxon.GridAccessorInterface.
- [maxon.PointsToVolumeListRef](../modules/maxon_generated/frameworks/volume/reference/maxon.PointsToVolumeListRef.md): Reference class for maxon.PointsToVolumeListInterface.
- [maxon.VolumeRef](../modules/maxon_generated/frameworks/volume/reference/maxon.VolumeRef.md): Represents a reference of a maxon.VolumeInterface

## modules/maxon_generated/functions

- [maxon.Cast](../modules/maxon_generated/functions/maxon.Cast.md)
- [maxon.GetDataType](../modules/maxon_generated/functions/maxon.GetDataType.md)
- [maxon.MAXON_ATTRIBUTE](../modules/maxon_generated/functions/maxon.MAXON_ATTRIBUTE.md)
- [maxon.MAXON_SOURCE_LOCATION](../modules/maxon_generated/functions/maxon.MAXON_SOURCE_LOCATION.md)
- [maxon.MaxonConvert](../modules/maxon_generated/functions/maxon.MaxonConvert.md)
- [maxon.ToBlock](../modules/maxon_generated/functions/maxon.ToBlock.md)
- [maxon.finally_once](../modules/maxon_generated/functions/maxon.finally_once.md)
- [maxon.reinterpret_cast](../modules/maxon_generated/functions/maxon.reinterpret_cast.md)

## modules/maxon_generated/interfaces/core

- [maxon.CStringInterface](../modules/maxon_generated/interfaces/core/maxon.CStringInterface.md)
- [maxon.DataDescriptionInterface](../modules/maxon_generated/interfaces/core/maxon.DataDescriptionInterface.md)
- [maxon.DataDictionaryInterface](../modules/maxon_generated/interfaces/core/maxon.DataDictionaryInterface.md): Class to store and find any data type under any type of key.
- [maxon.DataDictionaryObjectInterface](../modules/maxon_generated/interfaces/core/maxon.DataDictionaryObjectInterface.md): Class to store and find any maxon.Data type under any type of key.
- [maxon.LanguageInterface](../modules/maxon_generated/interfaces/core/maxon.LanguageInterface.md)
- [maxon.RegistryInterface](../modules/maxon_generated/interfaces/core/maxon.RegistryInterface.md): maxon.RegistryInterface is used internally by maxon.Registry.
- [maxon.Resource](../modules/maxon_generated/interfaces/core/maxon.Resource.md): Class that handles resources.
- [maxon.StringInterface](../modules/maxon_generated/interfaces/core/maxon.StringInterface.md)
- [maxon.UuidInterface](../modules/maxon_generated/interfaces/core/maxon.UuidInterface.md)

## modules/maxon_generated/interfaces/core_helper

- [maxon.AutoIterator](../modules/maxon_generated/interfaces/core_helper/maxon.AutoIterator.md): AutoIterator implements a foreach iterator for a BaseArray
- [maxon.ClassInterface.R](../modules/maxon_generated/interfaces/core_helper/maxon.ClassInterface.R.md)
- [maxon.ClassInterface](../modules/maxon_generated/interfaces/core_helper/maxon.ClassInterface.md)
- [maxon.ObjectInterface](../modules/maxon_generated/interfaces/core_helper/maxon.ObjectInterface.md)
- [maxon.ObserverObjectInterface](../modules/maxon_generated/interfaces/core_helper/maxon.ObserverObjectInterface.md): maxon.Component to allow maxon.ObjectInterface interfaces to use the observable concept.

## modules/maxon_generated/interfaces/information

- [maxon.Application](../modules/maxon_generated/interfaces/information/maxon.Application.md)
- [maxon.MachineInterface](../modules/maxon_generated/interfaces/information/maxon.MachineInterface.md)
- [maxon.MachinesInterface](../modules/maxon_generated/interfaces/information/maxon.MachinesInterface.md)
- [maxon.System](../modules/maxon_generated/interfaces/information/maxon.System.md)

## modules/maxon_generated/interfaces/io

- [maxon.BaseStreamInterface](../modules/maxon_generated/interfaces/io/maxon.BaseStreamInterface.md)
- [maxon.BaseStreamInterface.softspace](../modules/maxon_generated/interfaces/io/maxon.BaseStreamInterface.softspace.md)
- [maxon.FileFormatHandlerInterface](../modules/maxon_generated/interfaces/io/maxon.FileFormatHandlerInterface.md)
- [maxon.FileFormatInterface](../modules/maxon_generated/interfaces/io/maxon.FileFormatInterface.md)
- [maxon.InOutputStreamInterface.FromBlock](../modules/maxon_generated/interfaces/io/maxon.InOutputStreamInterface.FromBlock.md)
- [maxon.InOutputStreamInterface](../modules/maxon_generated/interfaces/io/maxon.InOutputStreamInterface.md)
- [maxon.InOutputStreamInterface.softspace](../modules/maxon_generated/interfaces/io/maxon.InOutputStreamInterface.softspace.md)
- [maxon.InputStreamInterface.FromBlock](../modules/maxon_generated/interfaces/io/maxon.InputStreamInterface.FromBlock.md)
- [maxon.InputStreamInterface](../modules/maxon_generated/interfaces/io/maxon.InputStreamInterface.md)
- [maxon.InputStreamInterface.softspace](../modules/maxon_generated/interfaces/io/maxon.InputStreamInterface.softspace.md)
- [maxon.IoBrowseInterface](../modules/maxon_generated/interfaces/io/maxon.IoBrowseInterface.md)
- [maxon.IoConnectionInterface](../modules/maxon_generated/interfaces/io/maxon.IoConnectionInterface.md)
- [maxon.IoHandlerInterface](../modules/maxon_generated/interfaces/io/maxon.IoHandlerInterface.md)
- [maxon.OutputStreamInterface](../modules/maxon_generated/interfaces/io/maxon.OutputStreamInterface.md): Creates an maxon.OutputStreamInterface class to write bytes into streams.
- [maxon.OutputStreamInterface.softspace](../modules/maxon_generated/interfaces/io/maxon.OutputStreamInterface.softspace.md)
- [maxon.UrlInterface](../modules/maxon_generated/interfaces/io/maxon.UrlInterface.md)

## modules/maxon_generated/interfaces/logger

- [maxon.LoggerInterface](../modules/maxon_generated/interfaces/logger/maxon.LoggerInterface.md)
- [maxon.LoggerTypeInterface](../modules/maxon_generated/interfaces/logger/maxon.LoggerTypeInterface.md)

## modules/maxon_generated/interfaces/misc

- [maxon.Gradient](../modules/maxon_generated/interfaces/misc/maxon.Gradient.md): Reference class for maxon.GradientInterface.
- [maxon.GradientInterface](../modules/maxon_generated/interfaces/misc/maxon.GradientInterface.md)
- [maxon.GradientKnot.bias](../modules/maxon_generated/interfaces/misc/maxon.GradientKnot.bias.md)
- [maxon.GradientKnot.brightness](../modules/maxon_generated/interfaces/misc/maxon.GradientKnot.brightness.md)
- [maxon.GradientKnot.col](../modules/maxon_generated/interfaces/misc/maxon.GradientKnot.col.md)
- [maxon.GradientKnot.index](../modules/maxon_generated/interfaces/misc/maxon.GradientKnot.index.md)
- [maxon.GradientKnot.interpolation](../modules/maxon_generated/interfaces/misc/maxon.GradientKnot.interpolation.md)
- [maxon.GradientKnot](../modules/maxon_generated/interfaces/misc/maxon.GradientKnot.md): An object of this class can store every type of data as long as that type has been registered (see maxon.DataType).
- [maxon.GradientKnot.pos](../modules/maxon_generated/interfaces/misc/maxon.GradientKnot.pos.md)
- [maxon.GradientRenderData](../modules/maxon_generated/interfaces/misc/maxon.GradientRenderData.md): Reference class for maxon.GradientRenderDataInterface.
- [maxon.GradientRenderDataInterface](../modules/maxon_generated/interfaces/misc/maxon.GradientRenderDataInterface.md)
- [maxon.Timer](../modules/maxon_generated/interfaces/misc/maxon.Timer.md): A timer class to retrieve the current time.

## modules/maxon_generated/interfaces/network

- [maxon.NetworkIpAddrInterface](../modules/maxon_generated/interfaces/network/maxon.NetworkIpAddrInterface.md): Represents an Internet Protocol (IP) address.
- [maxon.NetworkIpAddrPortInterface](../modules/maxon_generated/interfaces/network/maxon.NetworkIpAddrPortInterface.md)
- [maxon.NetworkIpInterface](../modules/maxon_generated/interfaces/network/maxon.NetworkIpInterface.md): Static interface to access network functionality.

## modules/maxon_generated/mxutils

- [mxutils.DebugNode.Children](../modules/maxon_generated/mxutils/mxutils.DebugNode.Children.md)
- [mxutils.DebugNode.Depth](../modules/maxon_generated/mxutils/mxutils.DebugNode.Depth.md)
- [mxutils.DebugNode.Label](../modules/maxon_generated/mxutils/mxutils.DebugNode.Label.md)
- [mxutils.DebugNode.Nid](../modules/maxon_generated/mxutils/mxutils.DebugNode.Nid.md)
- [mxutils.DebugNode.Parent](../modules/maxon_generated/mxutils/mxutils.DebugNode.Parent.md)
- [mxutils.DebugNode](../modules/maxon_generated/mxutils/mxutils.DebugNode.md): Realizes a simple tree structure used in printing debug information.
- [mxutils.DebugPrint](../modules/maxon_generated/mxutils/mxutils.DebugPrint.md): Contains utility functions for printing debug information about selected Cinema API data.
- [mxutils.IdProvider.DEFAULT_SCOPE](../modules/maxon_generated/mxutils/mxutils.IdProvider.DEFAULT_SCOPE.md)
- [mxutils.IdProvider.ID_TYPES](../modules/maxon_generated/mxutils/mxutils.IdProvider.ID_TYPES.md)
- [mxutils.IdProvider.IdType](../modules/maxon_generated/mxutils/mxutils.IdProvider.IdType.md)
- [mxutils.IdProvider.Scopes](../modules/maxon_generated/mxutils/mxutils.IdProvider.Scopes.md)
- [mxutils.IdProvider](../modules/maxon_generated/mxutils/mxutils.IdProvider.md): Generates int or maxon.Id identifiers.
- [mxutils.LocalImportPath](../modules/maxon_generated/mxutils/mxutils.LocalImportPath.md): Provides the ability to import packages and modules from directories that are not exposed to the global module search paths.
- [mxutils.Random.Magic](../modules/maxon_generated/mxutils/mxutils.Random.Magic.md)
- [mxutils.Random.Random](../modules/maxon_generated/mxutils/mxutils.Random.Random.md)
- [mxutils.Random.Seed](../modules/maxon_generated/mxutils/mxutils.Random.Seed.md)
- [mxutils.Random](../modules/maxon_generated/mxutils/mxutils.Random.md): Generates pseudo-random floating point, integer, vector, color, and matrix values in a deterministic manner.
- [mxutils.SceneFaker](../modules/maxon_generated/mxutils/mxutils.SceneFaker.md): Generates random scene data such as objects, materials, tags, layers, render data and tracks.
- [mxutils.SymbolTranslationCache](../modules/maxon_generated/mxutils/mxutils.SymbolTranslationCache.md): Caches and provides access to string symbols over their integer values.

## modules/maxon_generated/references/core

- [maxon.CString](../modules/maxon_generated/references/core/maxon.CString.md): Reference class of maxon.CStringInterface.
- [maxon.DataDescription](../modules/maxon_generated/references/core/maxon.DataDescription.md): Reference class of maxon.DataDescriptionInterface.
- [maxon.DataDictionary](../modules/maxon_generated/references/core/maxon.DataDictionary.md): Reference class of maxon.DataDictionaryInterface.
- [maxon.LanguageRef](../modules/maxon_generated/references/core/maxon.LanguageRef.md): Reference class of maxon.LanguageInterface.
- [maxon.Registry](../modules/maxon_generated/references/core/maxon.Registry.md)
- [maxon.String](../modules/maxon_generated/references/core/maxon.String.md): Reference class of maxon.StringInterface.
- [maxon.ThreadRef](../modules/maxon_generated/references/core/maxon.ThreadRef.md): Reference to a maxon.ThreadInterface.
- [maxon.Uuid](../modules/maxon_generated/references/core/maxon.Uuid.md): Reference class of maxon.UuidInterface.

## modules/maxon_generated/references/core_helper

- [maxon.Class.R](../modules/maxon_generated/references/core_helper/maxon.Class.R.md)
- [maxon.Class](../modules/maxon_generated/references/core_helper/maxon.Class.md): Reference class of maxon.ClassInterface.
- [maxon.ObjectRef](../modules/maxon_generated/references/core_helper/maxon.ObjectRef.md)

## modules/maxon_generated/references/information

- [maxon.MachineRef](../modules/maxon_generated/references/information/maxon.MachineRef.md): Reference class of maxon.MachineInterface.

## modules/maxon_generated/references/io

- [maxon.FileFormat](../modules/maxon_generated/references/io/maxon.FileFormat.md): Reference class of maxon.FileFormatInterface.
- [maxon.FileFormatHandler](../modules/maxon_generated/references/io/maxon.FileFormatHandler.md): Reference class of maxon.FileFormatHandlerInterface.
- [maxon.InOutputStreamRef.FromBlock](../modules/maxon_generated/references/io/maxon.InOutputStreamRef.FromBlock.md)
- [maxon.InOutputStreamRef](../modules/maxon_generated/references/io/maxon.InOutputStreamRef.md): Reference class of maxon.InOutputStreamInterface.
- [maxon.InOutputStreamRef.softspace](../modules/maxon_generated/references/io/maxon.InOutputStreamRef.softspace.md)
- [maxon.InputStreamRef.FromBlock](../modules/maxon_generated/references/io/maxon.InputStreamRef.FromBlock.md)
- [maxon.InputStreamRef](../modules/maxon_generated/references/io/maxon.InputStreamRef.md): Reference class of maxon.InputStreamInterface.
- [maxon.InputStreamRef.softspace](../modules/maxon_generated/references/io/maxon.InputStreamRef.softspace.md)
- [maxon.IoBrowseRef](../modules/maxon_generated/references/io/maxon.IoBrowseRef.md): Reference class of maxon.IoBrowseInterface.
- [maxon.IoConnectionRef](../modules/maxon_generated/references/io/maxon.IoConnectionRef.md): Reference class of maxon.IoConnectionInterface.
- [maxon.IoHandler](../modules/maxon_generated/references/io/maxon.IoHandler.md): Reference class of maxon.IoHandlerInterface.
- [maxon.OutputStreamRef](../modules/maxon_generated/references/io/maxon.OutputStreamRef.md): Reference class of maxon.OutputStreamInterface.
- [maxon.OutputStreamRef.softspace](../modules/maxon_generated/references/io/maxon.OutputStreamRef.softspace.md)
- [maxon.Url](../modules/maxon_generated/references/io/maxon.Url.md): Reference class of maxon.UrlInterface.

## modules/maxon_generated/references/logger

- [maxon.LoggerRef](../modules/maxon_generated/references/logger/maxon.LoggerRef.md): Reference class of maxon.LoggerInterface.
- [maxon.LoggerTypeRef](../modules/maxon_generated/references/logger/maxon.LoggerTypeRef.md): Reference class of maxon.LoggerTypeInterface.

## modules/maxon_generated/references/network

- [maxon.NetworkIpAddr](../modules/maxon_generated/references/network/maxon.NetworkIpAddr.md): Reference class of maxon.NetworkIpAddrInterface.
- [maxon.NetworkIpAddrPort](../modules/maxon_generated/references/network/maxon.NetworkIpAddrPort.md): Reference class of maxon.OutputStreamInterface.

## modules/maxon_generated/registries

- [maxon.Classes](../modules/maxon_generated/registries/maxon.Classes.md)
- [maxon.DataTypes](../modules/maxon_generated/registries/maxon.DataTypes.md)
- [maxon.FileFormatHandlers.AudioAVFoundation](../modules/maxon_generated/registries/maxon.FileFormatHandlers.AudioAVFoundation.md)
- [maxon.FileFormatHandlers.AudioLoaderAiff](../modules/maxon_generated/registries/maxon.FileFormatHandlers.AudioLoaderAiff.md)
- [maxon.FileFormatHandlers.AudioLoaderWav](../modules/maxon_generated/registries/maxon.FileFormatHandlers.AudioLoaderWav.md)
- [maxon.FileFormatHandlers.AudioWinMF](../modules/maxon_generated/registries/maxon.FileFormatHandlers.AudioWinMF.md)
- [maxon.FileFormatHandlers.Browsable](../modules/maxon_generated/registries/maxon.FileFormatHandlers.Browsable.md)
- [maxon.FileFormatHandlers.GZipArchiveHandler](../modules/maxon_generated/registries/maxon.FileFormatHandlers.GZipArchiveHandler.md)
- [maxon.FileFormatHandlers.GZipDirectoryBrowser](../modules/maxon_generated/registries/maxon.FileFormatHandlers.GZipDirectoryBrowser.md)
- [maxon.FileFormatHandlers.GenericFile](../modules/maxon_generated/registries/maxon.FileFormatHandlers.GenericFile.md)
- [maxon.FileFormatHandlers.ImageLoaderBmp](../modules/maxon_generated/registries/maxon.FileFormatHandlers.ImageLoaderBmp.md)
- [maxon.FileFormatHandlers.ImageLoaderHdr](../modules/maxon_generated/registries/maxon.FileFormatHandlers.ImageLoaderHdr.md)
- [maxon.FileFormatHandlers.ImageLoaderIco](../modules/maxon_generated/registries/maxon.FileFormatHandlers.ImageLoaderIco.md)
- [maxon.FileFormatHandlers.ImageLoaderIff](../modules/maxon_generated/registries/maxon.FileFormatHandlers.ImageLoaderIff.md)
- [maxon.FileFormatHandlers.ImageLoaderJpg](../modules/maxon_generated/registries/maxon.FileFormatHandlers.ImageLoaderJpg.md)
- [maxon.FileFormatHandlers.ImageLoaderPict](../modules/maxon_generated/registries/maxon.FileFormatHandlers.ImageLoaderPict.md)
- [maxon.FileFormatHandlers.ImageLoaderPng](../modules/maxon_generated/registries/maxon.FileFormatHandlers.ImageLoaderPng.md)
- [maxon.FileFormatHandlers.ImageLoaderPsb](../modules/maxon_generated/registries/maxon.FileFormatHandlers.ImageLoaderPsb.md)
- [maxon.FileFormatHandlers.ImageLoaderPsd](../modules/maxon_generated/registries/maxon.FileFormatHandlers.ImageLoaderPsd.md)
- [maxon.FileFormatHandlers.ImageLoaderTiff](../modules/maxon_generated/registries/maxon.FileFormatHandlers.ImageLoaderTiff.md)
- [maxon.FileFormatHandlers.MaxonDocumentBinaryHandler](../modules/maxon_generated/registries/maxon.FileFormatHandlers.MaxonDocumentBinaryHandler.md)
- [maxon.FileFormatHandlers.MaxonDocumentJsonHandler](../modules/maxon_generated/registries/maxon.FileFormatHandlers.MaxonDocumentJsonHandler.md)
- [maxon.FileFormatHandlers.MaxonDocumentXmlHandler](../modules/maxon_generated/registries/maxon.FileFormatHandlers.MaxonDocumentXmlHandler.md)
- [maxon.FileFormatHandlers.MovieAVFoundation](../modules/maxon_generated/registries/maxon.FileFormatHandlers.MovieAVFoundation.md)
- [maxon.FileFormatHandlers.MovieImageSequence](../modules/maxon_generated/registries/maxon.FileFormatHandlers.MovieImageSequence.md)
- [maxon.FileFormatHandlers.MovieWinMF](../modules/maxon_generated/registries/maxon.FileFormatHandlers.MovieWinMF.md)
- [maxon.FileFormatHandlers.ZipArchiveHandler](../modules/maxon_generated/registries/maxon.FileFormatHandlers.ZipArchiveHandler.md)
- [maxon.FileFormatHandlers.ZipDirectoryBrowser](../modules/maxon_generated/registries/maxon.FileFormatHandlers.ZipDirectoryBrowser.md)
- [maxon.FileFormatHandlers](../modules/maxon_generated/registries/maxon.FileFormatHandlers.md)
- [maxon.FileFormats.AudioAVFoundation](../modules/maxon_generated/registries/maxon.FileFormats.AudioAVFoundation.md)
- [maxon.FileFormats.AudioAiff](../modules/maxon_generated/registries/maxon.FileFormats.AudioAiff.md)
- [maxon.FileFormats.AudioWav](../modules/maxon_generated/registries/maxon.FileFormats.AudioWav.md)
- [maxon.FileFormats.AudioWinMF](../modules/maxon_generated/registries/maxon.FileFormats.AudioWinMF.md)
- [maxon.FileFormats.Browsable](../modules/maxon_generated/registries/maxon.FileFormats.Browsable.md)
- [maxon.FileFormats.File](../modules/maxon_generated/registries/maxon.FileFormats.File.md)
- [maxon.FileFormats.GZipArchive](../modules/maxon_generated/registries/maxon.FileFormats.GZipArchive.md)
- [maxon.FileFormats.ImageBmp](../modules/maxon_generated/registries/maxon.FileFormats.ImageBmp.md)
- [maxon.FileFormats.ImageDds](../modules/maxon_generated/registries/maxon.FileFormats.ImageDds.md)
- [maxon.FileFormats.ImageDpx](../modules/maxon_generated/registries/maxon.FileFormats.ImageDpx.md)
- [maxon.FileFormats.ImageGif](../modules/maxon_generated/registries/maxon.FileFormats.ImageGif.md)
- [maxon.FileFormats.ImageHdr](../modules/maxon_generated/registries/maxon.FileFormats.ImageHdr.md)
- [maxon.FileFormats.ImageIco](../modules/maxon_generated/registries/maxon.FileFormats.ImageIco.md)
- [maxon.FileFormats.ImageIff](../modules/maxon_generated/registries/maxon.FileFormats.ImageIff.md)
- [maxon.FileFormats.ImageJpg](../modules/maxon_generated/registries/maxon.FileFormats.ImageJpg.md)
- [maxon.FileFormats.ImagePict](../modules/maxon_generated/registries/maxon.FileFormats.ImagePict.md)
- [maxon.FileFormats.ImagePng](../modules/maxon_generated/registries/maxon.FileFormats.ImagePng.md)
- [maxon.FileFormats.ImagePsb](../modules/maxon_generated/registries/maxon.FileFormats.ImagePsb.md)
- [maxon.FileFormats.ImagePsd](../modules/maxon_generated/registries/maxon.FileFormats.ImagePsd.md)
- [maxon.FileFormats.ImageRla](../modules/maxon_generated/registries/maxon.FileFormats.ImageRla.md)
- [maxon.FileFormats.ImageRpf](../modules/maxon_generated/registries/maxon.FileFormats.ImageRpf.md)
- [maxon.FileFormats.ImageTga](../modules/maxon_generated/registries/maxon.FileFormats.ImageTga.md)
- [maxon.FileFormats.ImageTiff](../modules/maxon_generated/registries/maxon.FileFormats.ImageTiff.md)
- [maxon.FileFormats.MaxonDocumentBinary](../modules/maxon_generated/registries/maxon.FileFormats.MaxonDocumentBinary.md)
- [maxon.FileFormats.MaxonDocumentJson](../modules/maxon_generated/registries/maxon.FileFormats.MaxonDocumentJson.md)
- [maxon.FileFormats.MaxonDocumentXml](../modules/maxon_generated/registries/maxon.FileFormats.MaxonDocumentXml.md)
- [maxon.FileFormats.Movie3GP](../modules/maxon_generated/registries/maxon.FileFormats.Movie3GP.md)
- [maxon.FileFormats.MovieASF](../modules/maxon_generated/registries/maxon.FileFormats.MovieASF.md)
- [maxon.FileFormats.MovieAVFoundation](../modules/maxon_generated/registries/maxon.FileFormats.MovieAVFoundation.md)
- [maxon.FileFormats.MovieAVI](../modules/maxon_generated/registries/maxon.FileFormats.MovieAVI.md)
- [maxon.FileFormats.MovieImageSequence](../modules/maxon_generated/registries/maxon.FileFormats.MovieImageSequence.md)
- [maxon.FileFormats.MovieMP4](../modules/maxon_generated/registries/maxon.FileFormats.MovieMP4.md)
- [maxon.FileFormats.MovieMov](../modules/maxon_generated/registries/maxon.FileFormats.MovieMov.md)
- [maxon.FileFormats.MovieWMV](../modules/maxon_generated/registries/maxon.FileFormats.MovieWMV.md)
- [maxon.FileFormats.MovieWinMF](../modules/maxon_generated/registries/maxon.FileFormats.MovieWinMF.md)
- [maxon.FileFormats.ZipArchive](../modules/maxon_generated/registries/maxon.FileFormats.ZipArchive.md)
- [maxon.FileFormats](../modules/maxon_generated/registries/maxon.FileFormats.md)
- [maxon.IoHandlers.IoHandlerObjectBaseClass](../modules/maxon_generated/registries/maxon.IoHandlers.IoHandlerObjectBaseClass.md)
- [maxon.IoHandlers.IoHandlerObjectFileClass](../modules/maxon_generated/registries/maxon.IoHandlers.IoHandlerObjectFileClass.md)
- [maxon.IoHandlers](../modules/maxon_generated/registries/maxon.IoHandlers.md)
- [maxon.LoggerTypes.Application](../modules/maxon_generated/registries/maxon.LoggerTypes.Application.md)
- [maxon.LoggerTypes.File](../modules/maxon_generated/registries/maxon.LoggerTypes.File.md)
- [maxon.LoggerTypes.MultiFile](../modules/maxon_generated/registries/maxon.LoggerTypes.MultiFile.md)
- [maxon.LoggerTypes.Process](../modules/maxon_generated/registries/maxon.LoggerTypes.Process.md)
- [maxon.LoggerTypes](../modules/maxon_generated/registries/maxon.LoggerTypes.md)
- [maxon.Loggers.Asset](../modules/maxon_generated/registries/maxon.Loggers.Asset.md)
- [maxon.Loggers.Default](../modules/maxon_generated/registries/maxon.Loggers.Default.md)
- [maxon.Loggers.Neutron](../modules/maxon_generated/registries/maxon.Loggers.Neutron.md)
- [maxon.Loggers.Process](../modules/maxon_generated/registries/maxon.Loggers.Process.md)
- [maxon.Loggers.Python](../modules/maxon_generated/registries/maxon.Loggers.Python.md)
- [maxon.Loggers](../modules/maxon_generated/registries/maxon.Loggers.md)
- [maxon.ParametricTypes.ACOWReference](../modules/maxon_generated/registries/maxon.ParametricTypes.ACOWReference.md)
- [maxon.ParametricTypes.ArrayInterface](../modules/maxon_generated/registries/maxon.ParametricTypes.ArrayInterface.md)
- [maxon.ParametricTypes.Atomic](../modules/maxon_generated/registries/maxon.ParametricTypes.Atomic.md)
- [maxon.ParametricTypes.Block](../modules/maxon_generated/registries/maxon.ParametricTypes.Block.md)
- [maxon.ParametricTypes.COWReference](../modules/maxon_generated/registries/maxon.ParametricTypes.COWReference.md)
- [maxon.ParametricTypes.Col](../modules/maxon_generated/registries/maxon.ParametricTypes.Col.md)
- [maxon.ParametricTypes.Const](../modules/maxon_generated/registries/maxon.ParametricTypes.Const.md)
- [maxon.ParametricTypes.Intersection](../modules/maxon_generated/registries/maxon.ParametricTypes.Intersection.md)
- [maxon.ParametricTypes.LVReference](../modules/maxon_generated/registries/maxon.ParametricTypes.LVReference.md)
- [maxon.ParametricTypes.Mat](../modules/maxon_generated/registries/maxon.ParametricTypes.Mat.md)
- [maxon.ParametricTypes.Optional](../modules/maxon_generated/registries/maxon.ParametricTypes.Optional.md)
- [maxon.ParametricTypes.Pointer](../modules/maxon_generated/registries/maxon.ParametricTypes.Pointer.md)
- [maxon.ParametricTypes.RVReference](../modules/maxon_generated/registries/maxon.ParametricTypes.RVReference.md)
- [maxon.ParametricTypes.Range](../modules/maxon_generated/registries/maxon.ParametricTypes.Range.md)
- [maxon.ParametricTypes.Result](../modules/maxon_generated/registries/maxon.ParametricTypes.Result.md)
- [maxon.ParametricTypes.Simd](../modules/maxon_generated/registries/maxon.ParametricTypes.Simd.md)
- [maxon.ParametricTypes.SqrMat](../modules/maxon_generated/registries/maxon.ParametricTypes.SqrMat.md)
- [maxon.ParametricTypes.StridedBlock](../modules/maxon_generated/registries/maxon.ParametricTypes.StridedBlock.md)
- [maxon.ParametricTypes.StrongReference](../modules/maxon_generated/registries/maxon.ParametricTypes.StrongReference.md)
- [maxon.ParametricTypes.Union](../modules/maxon_generated/registries/maxon.ParametricTypes.Union.md)
- [maxon.ParametricTypes.UniqueReference](../modules/maxon_generated/registries/maxon.ParametricTypes.UniqueReference.md)
- [maxon.ParametricTypes.Vec](../modules/maxon_generated/registries/maxon.ParametricTypes.Vec.md)
- [maxon.ParametricTypes](../modules/maxon_generated/registries/maxon.ParametricTypes.md): Registry of all Parametric Types.
