<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/io/maxon.IoHandlerInterface.html -->

# maxon.IoHandlerInterface <a id="maxon-iohandlerinterface"></a>

## Description <a id="module-maxon.IoHandlerInterface"></a><a id="description"></a>

The IoHandler class offers some I/O functionality for filenames.  
This handler needs to be implemented for each scheme.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.IoHandler`](../../references/io/maxon.IoHandler.md#module-maxon.IoHandler)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetHandlerForScheme`](#maxon.IoHandlerInterface.GetHandlerForScheme)(scheme) | Returns the [`maxon.IoHandler`](../../references/io/maxon.IoHandler.md#module-maxon.IoHandler) which is responsible for the given scheme. |
| [`GetSystemPath`](#maxon.IoHandlerInterface.GetSystemPath)(url) | Translates a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) to a OS or handler-specific system path. |
| [`GetUrlScheme`](#maxon.IoHandlerInterface.GetUrlScheme)() | Returns the url scheme to use in Urls for this handler (such as “file” if this is the IoHandler for the file system). |
| [`IoNormalize`](#maxon.IoHandlerInterface.IoNormalize)(self, url, flags) | Returns a normalized [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |
| [`Normalize`](#maxon.IoHandlerInterface.Normalize)(self, url, flags) | Returns a normalized [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). Does not involve any Io operation and is just syntax based. |
| [`OpenConnection`](#maxon.IoHandlerInterface.OpenConnection)(url) | Opens a connection and returns the specified [`maxon.IoConnectionRef`](../../references/io/maxon.IoConnectionRef.md#module-maxon.IoConnectionRef) handler for this type of protocol. |
| [`RemoveUrl`](#maxon.IoHandlerInterface.RemoveUrl)(url) | Removes the last part of the given url and returns the parent url. |
| [`SetSystemPath`](#maxon.IoHandlerInterface.SetSystemPath)(url, systemPath) | Converts an OS or handler-specific system path to a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). |

## Methods Definition <a id="methods-definition"></a>

### *static* `IoHandlerInterface.GetHandlerForScheme(scheme)` <a id="maxon.IoHandlerInterface.GetHandlerForScheme"></a>

Returns the [`maxon.IoHandler`](../../references/io/maxon.IoHandler.md#module-maxon.IoHandler) which is responsible for the given scheme. The [`maxon.IoHandler`](../../references/io/maxon.IoHandler.md#module-maxon.IoHandler) is searched for at the IoHandlers registry.

**Parameters:** **scheme** ([`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)) – The [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) scheme for which the matching IoHandler shall be found.

**Returns:** The matching IoHandler, or a null reference.

**Return type:** [`maxon.IoHandler`](../../references/io/maxon.IoHandler.md#module-maxon.IoHandler)

**Raises:** **LookupError** – If the searched scheme can’t be found in the “net.maxon.registry.iohandlers” registry.

### `IoHandlerInterface.GetSystemPath(url)` <a id="maxon.IoHandlerInterface.GetSystemPath"></a>

Translates a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) to a OS or handler-specific system path.

**Parameters:** **url** ([`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)) – The [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) to translate.

**Returns:** The generated path.

**Return type:** str

### `IoHandlerInterface.GetUrlScheme()` <a id="maxon.IoHandlerInterface.GetUrlScheme"></a>

Returns the url scheme to use in Urls for this handler (such as “file” if this is the IoHandler for the file system).

**Returns:** Url scheme of this handler.

**Return type:** [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

### `IoHandlerInterface.IoNormalize(self, url, flags)` <a id="maxon.IoHandlerInterface.IoNormalize"></a>

Returns a normalized [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). If the normalized [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) is a link, the [`maxon.IoHandler`](../../references/io/maxon.IoHandler.md#module-maxon.IoHandler) can resolve it (if supported).

> **Note:** The [file:///](file:///) handler resolves symbolic links, where the [http://](http://) handler does not resolve links.

**Parameters:** **flags** (`maxon.NORMALIZEFLAGS`) – Flags to define type of normalization.

**Returns:** The normalized [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

**Return type:** [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

### `IoHandlerInterface.Normalize(self, url, flags)` <a id="maxon.IoHandlerInterface.Normalize"></a>

**Returns a normalized [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url). Does not involve any Io operation and is just syntax based.** If nothing needs to be normalized the same path is returned.

**Parameters:** **flags** (`maxon.NORMALIZEFLAGS`) – Flags to define type of normalization.

**Returns:** The normalized [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

**Return type:** [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

### `IoHandlerInterface.OpenConnection(url)` <a id="maxon.IoHandlerInterface.OpenConnection"></a>

Opens a connection and returns the specified [`maxon.IoConnectionRef`](../../references/io/maxon.IoConnectionRef.md#module-maxon.IoConnectionRef) handler for this type of protocol.

**Parameters:** **url** ([`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)) – [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url) of the connection to open.

**Returns:** A reference to the specialized [`maxon.IoConnectionRef`](../../references/io/maxon.IoConnectionRef.md#module-maxon.IoConnectionRef).

**Return type:** [`maxon.IoConnectionRef`](../../references/io/maxon.IoConnectionRef.md#module-maxon.IoConnectionRef)

### `IoHandlerInterface.RemoveUrl(url)` <a id="maxon.IoHandlerInterface.RemoveUrl"></a>

Removes the last part of the given url and returns the parent url.

**Parameters:** **url** ([`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)) – The [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

**Returns:** The modified [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

**Return type:** [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)

### `IoHandlerInterface.SetSystemPath(url, systemPath)` <a id="maxon.IoHandlerInterface.SetSystemPath"></a>

Converts an OS or handler-specific system path to a [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url).

**Parameters:**

- **url** ([`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)) – The url that will be filled.
- **systemPath** (*str*) – The path.
