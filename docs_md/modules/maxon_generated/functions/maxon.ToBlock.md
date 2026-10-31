<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/functions/maxon.ToBlock.html -->

# maxon.ToBlock <a id="maxon-toblock"></a>

## `maxon.ToBlock(data, size, stride=None, dt=None)` <a id="maxon.ToBlock"></a>

Makes a [`maxon.Block`](../datatypes/collection/maxon.Block.md#module-maxon.Block) or a [`maxon.StridedBlock`](../datatypes/collection/maxon.StridedBlock.md#module-maxon.StridedBlock) from a pointer, a size and a stride.

**Parameters:**

- **data** ([`maxon.Data`](../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The data to transform to a Block.
- **size** (*int*) – Number of elements.
- **stride** (*int*) – Element stride.
- **dt** ([`maxon.DataType`](../datatypes/base_core/maxon.DataType.md#module-maxon.DataType)) – The Datatype of the data to be converted as block

**Returns:** A block of elements for this data and datatype.

**Return type:** Union[[`maxon.StridedBlock`](../datatypes/collection/maxon.StridedBlock.md#module-maxon.StridedBlock), [`maxon.Block`](../datatypes/collection/maxon.Block.md#module-maxon.Block)]
