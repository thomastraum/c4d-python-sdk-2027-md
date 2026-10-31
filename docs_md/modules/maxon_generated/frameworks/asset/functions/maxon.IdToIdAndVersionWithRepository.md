<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/functions/maxon.IdToIdAndVersionWithRepository.html -->

# maxon.IdToIdAndVersionWithRepository <a id="maxon-idtoidandversionwithrepository"></a>

## `maxon.IdToIdAndVersionWithRepository(id, lookupRepository)` <a id="maxon.IdToIdAndVersionWithRepository"></a>

Calls IdToIdAndVersion and adds the repository on top.

**Parameters:**

- **id** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – Id to extract.
- **lookupRepository** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – Repository to look at.

**Returns:** Tuple\<AssetRepositoryRef, IdAndVersion, Bool> on success. Bool: limitRepository

**Return type:** [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef), [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)], bool]
