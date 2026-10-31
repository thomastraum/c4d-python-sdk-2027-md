<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/core/maxon.SourceLocation.html -->

# maxon.SourceLocation <a id="maxon-sourcelocation"></a>

## Description <a id="module-maxon.SourceLocation"></a><a id="description"></a>

An object to represents the current file location. This can either to trace error or memory leak.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Data`](../base_core/maxon.Data.md#module-maxon.Data)
- [`maxon.Struct`](../base_core/maxon.Struct.md#module-maxon.Struct)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.SourceLocation.file`](maxon.SourceLocation.file.md#maxon.SourceLocation.file) | (str) The file represented by this Source Location. |
| [`maxon.SourceLocation.lineAndFlags`](maxon.SourceLocation.lineAndFlags.md#maxon.SourceLocation.lineAndFlags) | (int) The line number represented by this Source Location. |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetFile`](#maxon.SourceLocation.GetFile)() | Retrieves the file represented by the source location object. |
| [`GetLine`](#maxon.SourceLocation.GetLine)() | Retrieves the line represented by the source location object. |
| [`__init__`](#maxon.SourceLocation.__init__)([f, line]) | Initializes a Source location with a given file and line |

## Methods Definition <a id="methods-definition"></a>

### `SourceLocation.GetFile()` <a id="maxon.SourceLocation.GetFile"></a>

Retrieves the file represented by the source location object.

**Returns:** The file represented by the source location object.

**Return type:** str

### `SourceLocation.GetLine()` <a id="maxon.SourceLocation.GetLine"></a>

Retrieves the line represented by the source location object.

**Returns:** The line represented by the source location object.

**Return type:** int

### `SourceLocation.__init__(f=None, line=None)` <a id="maxon.SourceLocation.__init__"></a>

Initializes a Source location with a given file and line

**Parameters:**

- **f** (*Optional*[*str*]) – The file represented.
- **line** (*Optional*[*int*]) – The line represented.
