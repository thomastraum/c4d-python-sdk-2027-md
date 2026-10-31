<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/information/maxon.MachineInterface.html -->

# maxon.MachineInterface <a id="maxon-machineinterface"></a>

## Description <a id="module-maxon.MachineInterface"></a><a id="description"></a>

This class is the entry point to access machine interfaces.  
So there is no difference if the machine is running local or remote via rpc.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObserverObjectInterface`](../core_helper/maxon.ObserverObjectInterface.md#module-maxon.ObserverObjectInterface)

Child Class:

- [`maxon.MachineRef`](../../references/information/maxon.MachineRef.md#module-maxon.MachineRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetMachineInfo`](#maxon.MachineInterface.GetMachineInfo)() | Returns information about the system and processor. |
| [`GetUniqueId`](#maxon.MachineInterface.GetUniqueId)() | Returns the service name of the local machine. |

## Methods Definition <a id="methods-definition"></a>

### `MachineInterface.GetMachineInfo()` <a id="maxon.MachineInterface.GetMachineInfo"></a>

Returns information about the system and processor.  
See `maxon.MACHINEINFO` for [`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary) properties.

**Returns:** System and processor information.

**Return type:**

`maxon.MACHINEINFO`

### `MachineInterface.GetUniqueId()` <a id="maxon.MachineInterface.GetUniqueId"></a>

Returns the service name of the local machine. This name is a unique name which allows to identify the machine.

**Returns:** The service name.

**Return type:** str
