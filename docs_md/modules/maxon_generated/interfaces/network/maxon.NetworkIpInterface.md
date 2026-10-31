<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/network/maxon.NetworkIpInterface.html -->

# maxon.NetworkIpInterface <a id="maxon-networkipinterface"></a>

## Description <a id="module-maxon.NetworkIpInterface"></a><a id="description"></a>

Static interface to access network functionality.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`SplitAddress`](#maxon.NetworkIpInterface.SplitAddress)(address) | Splits a passed address in its elements. |

## Methods Definition <a id="methods-definition"></a>

### *static* `NetworkIpInterface.SplitAddress(address)` <a id="maxon.NetworkIpInterface.SplitAddress"></a>

Splits a passed address in its elements.

**Parameters:** **address** (*str*) – The address.

**Returns:** A tuple with the Scheme, host and port in this order.

**Return type:** tuple(str, str, int)
