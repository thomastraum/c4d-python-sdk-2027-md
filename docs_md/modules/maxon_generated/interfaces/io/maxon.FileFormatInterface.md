<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/io/maxon.FileFormatInterface.html -->

# maxon.FileFormatInterface <a id="maxon-fileformatinterface"></a>

## Description <a id="module-maxon.FileFormatInterface"></a><a id="description"></a>

[`maxon.FileFormatInterface`](#module-maxon.FileFormatInterface) allows to implement and register file formats with its detection algorithm.  
The [`maxon.FileFormats`](../../registries/maxon.FileFormats.md#module-maxon.FileFormats) registry allows to register any format (e.g. FileFormats.Browsable, FileFormats.ImageJpg…).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.DataDictionaryObjectInterface`](../core/maxon.DataDictionaryObjectInterface.md#module-maxon.DataDictionaryObjectInterface)

Child Class:

- [`maxon.FileFormat`](../../references/io/maxon.FileFormat.md#module-maxon.FileFormat)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Detect`](#maxon.FileFormatInterface.Detect)(url, probeStream, flags) | Checks if the given URL or stream supports this file format. |

## Methods Definition <a id="methods-definition"></a>

### `FileFormatInterface.Detect(url, probeStream, flags)` <a id="maxon.FileFormatInterface.Detect"></a>

Checks if the given URL or stream supports this file format.

**Parameters:**

- **url** ([`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)) – [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) to check.
- **probeStream** (Optional[[`maxon.InputStreamRef`](../../references/io/maxon.InputStreamRef.md#module-maxon.InputStreamRef)]) – Optional stream to read file content from.
- **flags** (`maxon.FILEFORMATDETECTIONFLAGS`) – Detection flags.

**Returns:** True if the URL or stream fits this file format implementation.

**Return type:** bool
