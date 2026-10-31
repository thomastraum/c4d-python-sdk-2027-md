<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/information/maxon.MachinesInterface.html -->

# maxon.MachinesInterface <a id="maxon-machinesinterface"></a>

## Description <a id="module-maxon.MachinesInterface"></a><a id="description"></a>

This class declares functions to access and manage machines.  
There is no difference when accessing the machines using the available rpc interfaces where the machine runs (local, remote, webbrowser).

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetLocal`](#maxon.MachinesInterface.GetLocal)() | Returns the local machine. |

## Methods Definition <a id="methods-definition"></a>

### *static* `MachinesInterface.GetLocal()` <a id="maxon.MachinesInterface.GetLocal"></a>

Returns the local machine.  
It can be used like every other machine in the network.  
The difference is that the functions for this machine are called directly not using rpc.

**Returns:** Handle to the machine.

**Return type:** [`maxon.MachineRef`](../../references/information/maxon.MachineRef.md#module-maxon.MachineRef)
