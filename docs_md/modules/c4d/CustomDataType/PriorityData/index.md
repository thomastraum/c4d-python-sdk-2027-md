<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/PriorityData/index.html -->

# c4d.PriorityData <a id="c4d-prioritydata"></a>

## *class* `c4d.PriorityData` <a id="c4d.PriorityData"></a>

Priority data type (*CUSTOMGUI_PRIORITY_DATA*).

This type is called by value.

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Magic Methods**

- [`PriorityData.__init__()`](#c4d.PriorityData.__init__)

**Value Management**

- [`PriorityData.GetPriorityValue()`](#c4d.PriorityData.GetPriorityValue): Retrieves the priority values.
- [`PriorityData.SetPriorityValue()`](#c4d.PriorityData.SetPriorityValue): Sets a priority values.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.PriorityData-method-Magic-Methods"></a>

#### `PriorityData.__init__(self, v=None)` <a id="c4d.PriorityData.__init__"></a>

**Parameters:** **v** (*Optional*[[*c4d.PriorityData*](#c4d.PriorityData)]) – Copy constructor.

### Value Management <a id="c4d.PriorityData-method-Value-Management"></a>

#### `PriorityData.GetPriorityValue(self, lValueID)` <a id="c4d.PriorityData.GetPriorityValue"></a>

Retrieves the priority values.

**Parameters:**

**lValueID** (*int*) –

The priority value ID to get:

|   |   |   |
|---|---|---|
| *PRIORITYVALUE_MODE* | int | Mode: |
|  | *CYCLE_INITIAL* | Initial. |
|  | *CYCLE_ANIMATION* | Animation. |
|  | *CYCLE_EXPRESSION* | Expression. |
|  | *CYCLE_DYNAMICS* | Dynamics. |
|  | *CYCLE_GENERATORS* | Generators. |
| *PRIORITYVALUE_PRIORITY* | int | Priority. |
| *PRIORITYVALUE_CAMERADEPENDENT* | bool | Camera dependent. |

**Return type:** Any

**Returns:** The priority value.

#### `PriorityData.SetPriorityValue(self, lValueID, data)` <a id="c4d.PriorityData.SetPriorityValue"></a>

Sets a priority values.

**Parameters:**

- **lValueID** (*int*) –

  The priority value ID to set:

  |   |   |   |
  |---|---|---|
  | *PRIORITYVALUE_MODE* | int | Mode: |
  |  | *CYCLE_INITIAL* | Initial. |
  |  | *CYCLE_ANIMATION* | Animation. |
  |  | *CYCLE_EXPRESSION* | Expression. |
  |  | *CYCLE_DYNAMICS* | Dynamics. |
  |  | *CYCLE_GENERATORS* | Generators. |
  | *PRIORITYVALUE_PRIORITY* | int | Priority. |
  | *PRIORITYVALUE_CAMERADEPENDENT* | bool | Camera dependent. |

- **data** (*any*) – The priority value to set.

**Return type:** bool

**Returns:** **True** if successful, otherwise *False*
