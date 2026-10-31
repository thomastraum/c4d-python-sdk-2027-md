<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/network/maxon.NetworkIpAddrPortInterface.html -->

# maxon.NetworkIpAddrPortInterface <a id="maxon-networkipaddrportinterface"></a>

## Description <a id="module-maxon.NetworkIpAddrPortInterface"></a><a id="description"></a>

Provides an Internet Protocol (IP) address + port.  
This class extends the [`maxon.NetworkIpAddrInterface`](maxon.NetworkIpAddrInterface.md#module-maxon.NetworkIpAddrInterface) with a port.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.NetworkIpAddrInterface`](maxon.NetworkIpAddrInterface.md#module-maxon.NetworkIpAddrInterface)

Child Class:

- [`maxon.NetworkIpAddrPort`](../../references/network/maxon.NetworkIpAddrPort.md#module-maxon.NetworkIpAddrPort)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetAddress`](#maxon.NetworkIpAddrPortInterface.GetAddress)() | Returns the address without the port. |
| [`GetPort`](#maxon.NetworkIpAddrPortInterface.GetPort)() | Returns the port. |
| [`SetPort`](#maxon.NetworkIpAddrPortInterface.SetPort)(port) | Sets the port. |

## Methods Definition <a id="methods-definition"></a>

### `NetworkIpAddrPortInterface.GetAddress()` <a id="maxon.NetworkIpAddrPortInterface.GetAddress"></a>

Returns the address without the port.

**Returns:** Returns the address without the port.

**Return type:** [`maxon.NetworkIpAddr`](../../references/network/maxon.NetworkIpAddr.md#module-maxon.NetworkIpAddr)

### `NetworkIpAddrPortInterface.GetPort()` <a id="maxon.NetworkIpAddrPortInterface.GetPort"></a>

Returns the port.

**Returns:** The port or 0 if no port was set.

**Return type:** int

### `NetworkIpAddrPortInterface.SetPort(port)` <a id="maxon.NetworkIpAddrPortInterface.SetPort"></a>

Sets the port.

**Parameters:** **port** (*int*) – The port or 0 to reset port information.
