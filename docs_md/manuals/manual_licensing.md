<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_licensing.html -->

# Licensing <a id="licensing"></a>

Explains licensing for Python plugins in Cinema 4D.

[YouTube video player](https://www.youtube.com/embed/gk4t8hP01S0?si=6U2PY8ZAV8X1Yp1t&controls=0)

> **See also:** The [py_msc_licensing](../examples/plugins/py_msc_licensing/py_msc_licensing.pyp.md) example demonstrates how to implement a licensable Python plugin for Cinema 4D.

Licensing plugins is an important aspect of commercial plugin development, but it is also a complex subject. In Python, licensing is complicated by the fact that Python code is inherently insecure, as source code must be sent as plain text to the interpreter for execution. All Python *‘obfuscation’* measures—be it the built-in encryption of Cinema 4D or third-party tools such as *pyarmor* or *nuitka*—cannot prevent this. A motivated and even mildly competent attacker will always be able to easily decrypt your code and remove any licensing checks you have implemented. Therefore, licensing should always be implemented in Python with the goal of *keeping honest users honest*. You will not be able to prevent determined attackers from cracking your licensing scheme.

Nonetheless, it can be useful to implement non-trivial licensing mechanisms in Python plugins to enable features such as trial periods, feature-limited demo modes, educational licenses, and dynamic license changes, without having to restart Cinema 4D.

## Core Concepts <a id="core-concepts"></a>

The general idea of licensing is to restrict access to certain or all functionalities of your plugin to users who possess a valid license. A license is typically represented by a license key or serial number, which the user must enter to unlock the full functionality of the plugin. The license key is usually generated based on user-specific data such as name, email, or machine ID, to bind the license to a specific user or machine (a ‘node-locked’ license).

### Cinema 4D Licensing API <a id="cinema-4d-licensing-api"></a>

Cinema 4D exposes its own licensing infrastructure, primarily through [`c4d.ExportLicenses()`](../modules/c4d/index.md#c4d.ExportLicenses). Where the returned data could look like this:

```json
{
    "userid":"e3a1c2d4-7f8b-4a6e-9d2c-3f5b8e1a2c4d",
    "systemid":"QwErTyUiOpAsDfGhJkLzXcVbNm1234567890abCDt",
    "name":"Alice",
    "surname":"Smith",
    "version":"2026.1.0",
    "currentproduct":"net.maxon.license.app.cinema4d-release~commercial",
    "accountlicenses":{
        "net.maxon.license.app.cinema4d-release~commandline-floating":10,
        "net.maxon.license.app.teamrender-release~commercial-floating":10,
        "net.maxon.license.app.cinema4d-release~commercial-floating":10,
        "net.maxon.license.app.cinema4d-release~education-floating":10,
        "net.maxon.license.app.teamrender-release~education-floating":10,
        "net.maxon.license.app.teamrender-release~commercial":5,
        "net.maxon.license.app.cinema4d-release~commercial":5
    }
}
```

The returned dictionary contains the following relevant fields:

- *userid*: A unique identifier for the user, i.e., the currently logged in Maxon Account.
- *systemid*: A unique identifier for the machine, the currently running Maxon app (e.g., Cinema 4D) is running attached to.
- *name* and *surname*: The name of the user, mostly redundant with the *userid*.
- *version*: The version of the Maxon app (e.g., Cinema 4D) that is currently running.
- *currentproduct*: A unique identifier for the product license currently in use.
- *accountlicenses*: A dictionary of all licenses available to the user, with the license identifier as key and the number of available seats as value.

The structure of a product identifier as found in the *currentproduct* and *accountlicenses* fields is as follows:

```text
net.maxon.license.app.{product}[~{modifier}][-floating]
```

Below are some example product identifiers:

- *net.maxon.license.app.zpad~commercial*: A commercial license for ZBrush on iPad.
- *net.maxon.license.app.bundle_maxonone-release~student*: A student license for the Maxon One bundle.
- *net.maxon.license.service.cineversity*: A Cineversity service license.
- *net.maxon.license.app.teamrenderclient~commercial-floating*: A commercial floating license for the Team Render Client.
- *net.maxon.license.app.cinema4d-release~commercial*: A commercial customer release license for Cinema 4D.
- *net.maxon.license.app.cinema4d-release~commandline*: A commercial customer release commandline license for Cinema 4D.

The available products found in a user account change with the products Maxon offers, and not all products can be publicly documented. Therefore, there can be no exhaustive list of all possible product identifiers. The following list however contains the most common product identifiers relevant for Cinema 4D:

- *net.maxon.license.app.bundle_maxonone-release*: A Maxon One bundle product, containing access to all Maxon apps.
- *net.maxon.license.app.cinema4d-release*: A Cinema 4D product.
- *net.maxon.license.app.teamrender-release*: A Team Render product.
- *net.maxon.license.app.redshift*: A Redshift standalone product.
- *net.maxon.license.app.zpad*: A ZBrush on iPad product.
- *net.maxon.license.app.zbrush*: A ZBrush desktop product.

> **Note:** Licenses can be buried in license bundles, e.g., the Maxon One bundle. A user might not have a dedicated Cinema 4D license, but still have access to Cinema 4D through the Maxon One bundle license.

The product modifiers are fully documented and can be:

- *~commercial*: A commercial license.
- *~education*: An educational license (i.e, a classroom license).
- *~student*: A student license.
- *~trial*: A trial license.
- *~commandline*: A commandline license.

Note that *~beta* is not an existing modifier. Maxon beta products instead have their own product identifiers. Finally, the optional *-floating* suffix indicates that the license is a floating license. To get the current product ID and check if the user is using either a student or classroom license (so you can, for example, disable certain features in your plugin), one could do the following:

```python
import c4d
import re

data: dict = c4d.ExportLicenses()
currentProduct: str = data.get("currentproduct", "")
isEducational: bool = re.search(r"~(education|student)", currentProduct) is not None
```

### Generating and Validating <a id="generating-and-validating"></a>

To generate license serials of your own, you can use any hashing algorithm you like. A common choice is to use SHA-256 hashing to generate a unique license serial based on user-specific data such as name, email, or machine ID. To obtain such user-specific data, you can either use the Cinema Licensing API with [`c4d.ExportLicenses()`](../modules/c4d/index.md#c4d.ExportLicenses) as shown above, a web service where the user must authenticate, or more primitive methods such as binding to the machine MAC address or similar.

To validate a license serial, simply re-gather all relevant user-specific data, generate a new license serial using the same algorithm, and compare it to the license serial provided by the user. If both serials match, the license is valid. An abstracted serial generation and validation could look like this:

```python
import hashlib

def generate_license_serial(userid: str, systemid: str, salt: str) -> str:
    """Generates a license serial based on user and system ID and a secret key.
    """
    # We just concatenate all our data we want to bind the license to in a string and then
    # mix in our secret salt value so that only we can generate valid license serials. We then
    # just hash the resulting string with SHA-256 and return the hex representation.
    data: str = f"{userid}:{systemid}:{salt}"
    sha256: hashlib._hashlib.HASH = hashlib.sha256()
    sha256.update(data.encode("utf-8"))
    return sha256.hexdigest()

def validate_license_serial(serial: str, userid: str, systemid: str, salt: str) -> bool:
    """Validates a license serial by regenerating it and comparing it to the provided one.
    """
    expectedSerial: str = generate_license_serial(userid, systemid, salt)
    return serial == expectedSerial
```

## Licensing Workflows <a id="licensing-workflows"></a>

Aside from the basic concept of generating and validating license serials, there are multiple possible workflows to implement licensing in your plugin. First, there are several options for where a license can be stored:

### Storing Licenses <a id="storing-licenses"></a>

- *File*: The license is stored in a **.lic* or **.txt* file. For Cinema 4D, the best storage location is the user preferences folder, which you can get with [`c4d.storage.GeGetC4DPath()`](../modules/c4d.storage/index.md#c4d.storage.GeGetC4DPath) or [`maxon.Application.GetUrl()`](../modules/maxon_generated/interfaces/information/maxon.Application.md#maxon.Application.GetUrl) (the latter is the more modern and recommended variant). The advantage of this approach is that the user can easily copy a license file to a machine. This is especially useful in the context of render farms, which might not want to run more complex GUI-based operations for each render node. The success of your plugin can depend on how easy it is to install licenses on render nodes. The disadvantage is that license files are more easily manipulated or copied to unauthorized users. However, if you design your licensing scheme sufficiently well, this should not be a major issue.
- *Cinema 4D*: The license is stored in the internal encrypted storage of Cinema 4D via [`c4d.plugins.WritePluginInfo()`](../modules/c4d.plugins/index.md#c4d.plugins.WritePluginInfo). There are few advantages to this approach, because despite being stored encrypted, access is not regulated. Once an attacker knows under which ID your plugin stores its data, this is not any safer than storing it in a file. A slight advantage of this approach is that, unlike the file-based approach, different flavors of Cinema 4D (i.e., Cinema 4D, Teams Client, Commandline, etc.) will automatically share the same plugin storage, but all have different user preference folders. See the *py-licensing_2026* example for details on how the file-based approach can handle this nonetheless.
- *Web Service*: The license is stored and validated via a web service. This is the most complex approach, but also the most flexible. The advantage is that you never store a perpetual license on the user machine, but only a temporary token that can be revoked at any time. This allows for more complex licensing schemes such as subscription-based licenses. For Python plugins, this is only rarely the right choice, and it is also not demonstrated in the provided examples. The disadvantage is that you must run and maintain a web service, which is a non-trivial task.

### Activating Licenses <a id="activating-licenses"></a>

The other big decision to make is how users can activate their licenses. There are two options:

- *Restart*: The user must restart Cinema 4D after entering a license serial to activate the license. This is the simplest approach to implement, as you can just check for a valid license in the boot phase of Cinema 4D when your plugin is loaded. The disadvantage is that this is not a very user-friendly approach, and in more complex plugins you might need the ability to register a plugin without actually running it, for example, to install extra content or dependencies before you unlock the full functionality of your plugin. With a simple restart-based approach where you only check for a valid license in the boot phase, this is not possible.
- *Dynamic*: The user can enter and activate a license serial at any time, without having to restart Cinema 4D. This is the more complex approach to implement, as you must be able to register and unregister your plugin at runtime based on the presence of a valid license. The advantage is that this is a more user-friendly approach and allows for more complex workflows such as trial periods or feature-limited demo modes. The disadvantage is that this is more complex to implement, as you must handle the registration and un-registration of your plugin at runtime.

### Registering Plugins <a id="registering-plugins"></a>

> **Warning:** The boot phase of Cinema 4D is a very restricted environment. You must avoid doing GUI operations, complex web requests, or complex file operations (i.e., ‘installing’ content) in this phase. Such operations can lead to Cinema 4D hanging or crashing during startup.

Plugins are registered in the boot phase of Cinema 4D, i.e., formally when [`C4DPL_INIT`](manual_implementing_plugins.md#PluginMessage) is emitted. For Python plugins, this is the same moment when they are loaded. Therefore, the earliest point where one can check for a valid license and register the plugin is in this phase. If no valid license is present, you can simply skip the registration of your plugin, effectively disabling it. However, this approach has some limitations. First, you cannot perform complex operations in this phase, such as GUI operations, complex web requests, or complex file operations (i.e., ‘installing’ content). Such operations can lead to Cinema 4D hanging or crashing during startup, the earliest point where you can do such things is when the *C4DPL_STARTACTIVITY* plugin message is emitted, i.e., when Cinema 4D and all its plugins have been fully loaded and Cinema 4D has finished its startup sequence.

Second, if you want to implement dynamic license activation, you must always register your plugin the boot phase, and then add license checks in the actual plugin code to enable or disable functionality based on the presence of a valid license. This is demonstrated in the *py-licensing_2026* example, where the plugin is always registered, but its functionality is gated behind license checks.

## See Also <a id="see-also"></a>

- [Implementing Plugins](manual_implementing_plugins.md): Explains the basic concepts of implementing plugins.
- [Example py_msc_licensing.pyp](../examples/plugins/py_msc_licensing/py_msc_licensing.pyp.md): Demonstrates how to implement licensing checks in plugins.
- [Example py_msc_licensing_simple.pyp](../examples/plugins/py_msc_licensing/py_msc_licensing_simple.pyp.md): Demonstrates simple licensing workflow for Python plugins in Cinema 4D.
