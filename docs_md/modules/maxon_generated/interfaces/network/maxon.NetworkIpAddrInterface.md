<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/network/maxon.NetworkIpAddrInterface.html -->

# maxon.NetworkIpAddrInterface <a id="maxon-networkipaddrinterface"></a>

## Description <a id="module-maxon.NetworkIpAddrInterface"></a><a id="description"></a>

Represents an Internet Protocol (IP) address.

It is version agnostic and supports both IPv4 and IPv6.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Children Classes:

- [`maxon.NetworkIpAddrPortInterface`](maxon.NetworkIpAddrPortInterface.md#module-maxon.NetworkIpAddrPortInterface)
- [`maxon.NetworkIpAddr`](../../references/network/maxon.NetworkIpAddr.md#module-maxon.NetworkIpAddr)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Flush`](#maxon.NetworkIpAddrInterface.Flush)() | *Deprecated since version 20.* |
| [`GetNativeProtocol`](#maxon.NetworkIpAddrInterface.GetNativeProtocol)() | Returns the type of the IP address used in this object. |
| [`GetProtocol`](#maxon.NetworkIpAddrInterface.GetProtocol)() | Returns the type of the IP address used in this object. |
| [`GetString`](#maxon.NetworkIpAddrInterface.GetString)([port]) | Retrieves the string representation of the current IP address. |
| [`SetIPv4`](#maxon.NetworkIpAddrInterface.SetIPv4)() | Sets an IP v4 address from the native in_addr structure. |
| [`SetIPv6`](#maxon.NetworkIpAddrInterface.SetIPv6)() | Sets an IP v6 address from the native in_addr structure. |
| [`__str__`](#maxon.NetworkIpAddrInterface.__str__)() | Return str(self). |

## Methods Definition <a id="methods-definition"></a>

### `NetworkIpAddrInterface.Flush()` <a id="maxon.NetworkIpAddrInterface.Flush"></a>

*Deprecated since version 20:* Use `NetworkIpAddrInterface.Reset()` instead.

### `NetworkIpAddrInterface.GetNativeProtocol()` <a id="maxon.NetworkIpAddrInterface.GetNativeProtocol"></a>

Returns the type of the IP address used in this object.

**Returns:** The Protocol type.

**Return type:** int

### `NetworkIpAddrInterface.GetProtocol()` <a id="maxon.NetworkIpAddrInterface.GetProtocol"></a>

Returns the type of the IP address used in this object.

**Returns:** The IP address type.

**Return type:**

`maxon.PROTOCOL`

### `NetworkIpAddrInterface.GetString(port=0)` <a id="maxon.NetworkIpAddrInterface.GetString"></a>

Retrieves the string representation of the current IP address.

**Parameters:** **port** (*int*) – The port to be appended at the end of the IP address.

**Returns:** The string representation of the current IP address.

**Return type:** str

### `NetworkIpAddrInterface.SetIPv4()` <a id="maxon.NetworkIpAddrInterface.SetIPv4"></a>

Sets an IP v4 address from the native in_addr structure.

### `NetworkIpAddrInterface.SetIPv6()` <a id="maxon.NetworkIpAddrInterface.SetIPv6"></a>

Sets an IP v6 address from the native in_addr structure.

### `NetworkIpAddrInterface.__str__()` <a id="maxon.NetworkIpAddrInterface.__str__"></a>

Return str(self).
