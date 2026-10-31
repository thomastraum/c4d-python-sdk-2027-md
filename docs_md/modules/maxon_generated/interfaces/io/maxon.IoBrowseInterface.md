<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/io/maxon.IoBrowseInterface.html -->

# maxon.IoBrowseInterface <a id="maxon-iobrowseinterface"></a>

## Description <a id="module-maxon.IoBrowseInterface"></a><a id="description"></a>

The `IoBrowseIterator` interface for a given [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).  
This `IoBrowseIterator` needs to be implemented for each protocol that support kind of directories (e.g. “file”, “zip”).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.IoBrowseRef`](../../references/io/maxon.IoBrowseRef.md#module-maxon.IoBrowseRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetBasePath`](#maxon.IoBrowseInterface.GetBasePath)() | Returns corresponding [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`GetCurrentPath`](#maxon.IoBrowseInterface.GetCurrentPath)() | Returns the current [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`GetExtraData`](#maxon.IoBrowseInterface.GetExtraData)() | Returns some extra data. |
| [`GetNext`](#maxon.IoBrowseInterface.GetNext)() | Browses to the next object in the list. |
| [`GetSize`](#maxon.IoBrowseInterface.GetSize)() | Returns the size of the current file. |
| [`HasEntry`](#maxon.IoBrowseInterface.HasEntry)() | Checks if there is any entry left |
| [`Init`](#maxon.IoBrowseInterface.Init)(connection, flags) | Private |
| [`IoGetAttributes`](#maxon.IoBrowseInterface.IoGetAttributes)() | Returns the flags (`maxon.IOATTRIBUTES`) of the children. |
| [`IoGetFlags`](#maxon.IoBrowseInterface.IoGetFlags)() | Returns the flags (`maxon.IOBROWSEFLAGS`) of the children. |
| [`Reset`](#maxon.IoBrowseInterface.Reset)() | Restart browsing of the directory. |

## Methods Definition <a id="methods-definition"></a>

### `IoBrowseInterface.GetBasePath()` <a id="maxon.IoBrowseInterface.GetBasePath"></a>

Returns corresponding [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

**Returns:** Name of the connection.

**Return type:** [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

### `IoBrowseInterface.GetCurrentPath()` <a id="maxon.IoBrowseInterface.GetCurrentPath"></a>

Returns the current [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

**Returns:** The current [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

**Return type:** [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

### `IoBrowseInterface.GetExtraData()` <a id="maxon.IoBrowseInterface.GetExtraData"></a>

Returns some extra data.

> **Note:**
>
> `maxon.URLSCHEME_VOLUME` returns the human readable drive name.

**Returns:** The return value depends on the handler what it returns.

**Return type:** str

### `IoBrowseInterface.GetNext()` <a id="maxon.IoBrowseInterface.GetNext"></a>

Browses to the next object in the list. You need to call GetNext() before you get the first object.

### `IoBrowseInterface.GetSize()` <a id="maxon.IoBrowseInterface.GetSize"></a>

Returns the size of the current file.

**Returns:** Size in bytes. -1 means unknown size.

**Return type:** int

### `IoBrowseInterface.HasEntry()` <a id="maxon.IoBrowseInterface.HasEntry"></a>

Checks if there is any entry left

**Returns:** True if the iterator still get content to iterate.

**Return type:** bool

### `IoBrowseInterface.Init(connection, flags)` <a id="maxon.IoBrowseInterface.Init"></a>

Private

**Parameters:**

- **connection** ([`maxon.IoConnectionRef`](../../references/io/maxon.IoConnectionRef.md#module-maxon.IoConnectionRef)) – [`maxon.IoConnectionRef`](../../references/io/maxon.IoConnectionRef.md#module-maxon.IoConnectionRef) Connected to this [`maxon.IoBrowseRef`](../../references/io/maxon.IoBrowseRef.md#module-maxon.IoBrowseRef).
- **flags** (`maxon.GETBROWSEITERATORFLAGS`) – Defines how the iterator should behave.

### `IoBrowseInterface.IoGetAttributes()` <a id="maxon.IoBrowseInterface.IoGetAttributes"></a>

Returns the flags (`maxon.IOATTRIBUTES`) of the children.

**Returns:** The children flags.

**Return type:**

`maxon.IOATTRIBUTES`

### `IoBrowseInterface.IoGetFlags()` <a id="maxon.IoBrowseInterface.IoGetFlags"></a>

Returns the flags (`maxon.IOBROWSEFLAGS`) of the children.

**Returns:** The children flags.

**Return type:**

`maxon.IOBROWSEFLAGS`

### `IoBrowseInterface.Reset()` <a id="maxon.IoBrowseInterface.Reset"></a>

Restart browsing of the directory.
