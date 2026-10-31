<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.gui/BaseCustomGui/HtmlViewerCustomGui/index.html -->

# c4d.gui.HtmlViewerCustomGui <a id="c4d-gui-htmlviewercustomgui"></a>

## *class* `c4d.gui.HtmlViewerCustomGui` <a id="c4d.gui.HtmlViewerCustomGui"></a>

Realizes a HTML viewer GUI.  
The gui ID is *CUSTOMGUI_HTMLVIEWER*. See *plugins/py_cmd_gui_html* in the SDK for an example of how to use this GUI.

Parent Class:

- [`c4d.gui.BaseCustomGui`](../index.md#c4d.gui.BaseCustomGui)

## Overview <a id="overview"></a>

**Content And Navigation**

- [`HtmlViewerCustomGui.SetText()`](#c4d.gui.HtmlViewerCustomGui.SetText): Set the HTML viewer text.
- [`HtmlViewerCustomGui.SetUrl()`](#c4d.gui.HtmlViewerCustomGui.SetUrl): Set the HTML viewer URL.

**JavaScript And Interaction**

- [`HtmlViewerCustomGui.DoAction()`](#c4d.gui.HtmlViewerCustomGui.DoAction): Do an action in the HTML viewer.
- [`HtmlViewerCustomGui.ExecuteJavaScript()`](#c4d.gui.HtmlViewerCustomGui.ExecuteJavaScript): Executes JavaScript code in the HTML viewer’s JavaScript context.
- [`HtmlViewerCustomGui.PostWebMessage()`](#c4d.gui.HtmlViewerCustomGui.PostWebMessage): Posts a web message to the HTML viewer’s JavaScript context.
- [`HtmlViewerCustomGui.SetWebMessageCallback()`](#c4d.gui.HtmlViewerCustomGui.SetWebMessageCallback): Sets a callback for web messages sent from the HTML viewer’s JavaScript context.

**Web Integration**

- [`HtmlViewerCustomGui.SetRequestHeader()`](#c4d.gui.HtmlViewerCustomGui.SetRequestHeader): Sets an HTTP request header that is injected on requests to *hostname*.
- [`HtmlViewerCustomGui.SetURLCallback()`](#c4d.gui.HtmlViewerCustomGui.SetURLCallback): Set the URL callback.

## Members <a id="members"></a>

### Content And Navigation <a id="c4d.gui.HtmlViewerCustomGui-method-Content-And-Navigation"></a>

#### `HtmlViewerCustomGui.SetText(self, url)` <a id="c4d.gui.HtmlViewerCustomGui.SetText"></a>

Set the HTML viewer text.

**Parameters:** **url** (*str*) – New text.

#### `HtmlViewerCustomGui.SetUrl(self, url, encoding)` <a id="c4d.gui.HtmlViewerCustomGui.SetUrl"></a>

Set the HTML viewer URL.

**Parameters:**

- **url** (*str*) – New URL.

- **encoding** (*int*) –

  Encoding:

  |   |   |
  |---|---|
  | *URL_ENCODING_UTF16* | A string containing umlauts and spaces. The last # following the last slash is regarded as start of the anchor (the anchor following the hash mark must be escaped!) |
  | *URL_ENCODING_ESCAPED* | String contains an escaped url (all umlauts, spaces and other stuff that does not belong there is % according to RFC 2396.) |

### JavaScript And Interaction <a id="c4d.gui.HtmlViewerCustomGui-method-JavaScript-And-Interaction"></a>

#### `HtmlViewerCustomGui.DoAction(self, action)` <a id="c4d.gui.HtmlViewerCustomGui.DoAction"></a>

Do an action in the HTML viewer.

**Parameters:**

**action** (*int*) –

Action:

|   |   |
|---|---|
| *WEBPAGE_GOBACK* | Go back. |
| *WEBPAGE_GOFORWARD* | Go forward. |
| *WEBPAGE_GOHOME* | Go home. |
| *WEBPAGE_SEARCH* | Search. |
| *WEBPAGE_REFRESH* | Refresh. |
| *WEBPAGE_STOP* | Stop |

#### `HtmlViewerCustomGui.ExecuteJavaScript(self, script)` <a id="c4d.gui.HtmlViewerCustomGui.ExecuteJavaScript"></a>

Executes JavaScript code in the HTML viewer’s JavaScript context.

**Parameters:** **script** (*str*) – The JavaScript code to execute.

#### `HtmlViewerCustomGui.PostWebMessage(self, message)` <a id="c4d.gui.HtmlViewerCustomGui.PostWebMessage"></a>

Posts a web message to the HTML viewer’s JavaScript context.  
The message is delivered to *window.maxon.messageListener*, the cross-platform receive hook that behaves identically on Windows and MacOS. The page assigns a function to it; the host invokes that function with the message.

> **Warning:** We strongly recommend to only send JSON-encoded strings as messages to ensure proper parsing and handling. On MacOS, plain text messages containing double quotes, control characters, or other special characters may not be parsed correctly, leading to unexpected behavior. Sending pure alphanumeric strings will work on all platforms, for complex data structures, you must use JSON.

> **Note:** Sending the empty string as a message is not supported and will be ignored.

**Parameters:** **message** (*str*) – The message to send to JavaScript. Cannot be the empty string. We strongly recommend to send JSON-encoded strings to ensure proper parsing and handling.

**Example:**

```javascript
// Receiving the message in the web page (same code on Windows and MacOS).
window.maxon.messageListener = (message) => {
    if (!message || typeof message !== 'string')
        return;

    try {
        var data = JSON.parse(message);
    }
    catch (error) {
        return;
    }
    // Do something with the data ...
};
```

#### `HtmlViewerCustomGui.SetWebMessageCallback(self, callback, urlPartial, user_data)` <a id="c4d.gui.HtmlViewerCustomGui.SetWebMessageCallback"></a>

Sets a callback for web messages sent from the HTML viewer’s JavaScript context.  
The callback is triggered when JavaScript calls *window.maxon.postMessage(msg)*.

**Parameters:**

- **callback** (*Optional*[*Callable*[[*None*, *str*], *None*]]) – The callback function to handle web messages.
- **urlPartial** (*str*) – A partial URL to filter which messages trigger the callback.
- **user_data** (*Optional*[*any*]) – User data pointer passed to the callback.

**Example:**

```javascript
// Somewhere in the web page, send a message to the host:
function postMessage(payload) {
    window.maxon.postMessage(payload);
};
```

### Web Integration <a id="c4d.gui.HtmlViewerCustomGui-method-Web-Integration"></a>

#### `HtmlViewerCustomGui.SetRequestHeader(self, name, value, hostname, httpsOnly=True)` <a id="c4d.gui.HtmlViewerCustomGui.SetRequestHeader"></a>

Sets an HTTP request header that is injected on requests to *hostname*.

**Parameters:**

- **name** (*str*) – The header name, e.g. “Accept-Language”.
- **value** (*str*) – The header value, e.g. “de-DE”.
- **hostname** (*str*) – The host the header applies to, e.g. “example.com”. Required; bare host only, no scheme, port or path. Matched exactly and case-insensitively, so a subdomain like “api.example.com” needs its own registration.
- **httpsOnly** (*bool*) – Send the header only over HTTPS. Default is **True**; pass **False** for a host served over plain HTTP, e.g. a local development server.

> **Note:** The header is applied to main-frame navigations only, i.e. to top-level document loads, and not to the sub-resource or API requests the loaded page issues (images, scripts, fetch/XHR, …). A page that needs a header on its own API requests has to set it in JavaScript.

> **Note:** On macOS the header is applied to plain page loads only, and not to form submissions, reloads, or back/forward navigation. Windows has no such restriction.

> **Note:** Registered headers are discarded when the viewer’s window is destroyed (e.g. a layout switch), so set them again from the dialog’s InitValues().

> **Warning:** The header is sent on every navigation to hostname, including those the page triggers itself.

> **Note:** This function is not implemented on Linux (no-op).

#### `HtmlViewerCustomGui.SetURLCallback(self, callback, user_data)` <a id="c4d.gui.HtmlViewerCustomGui.SetURLCallback"></a>

Set the URL callback.

**Parameters:**

- **callback** (*Optional*[*Callable*[[*None*, *str*, *int*], *None*]]) – New callback, or **None** to disable callback.
- **user_data** (*Optional*[*any*]) – User data. - Not used currently, limitation of the implementation.
