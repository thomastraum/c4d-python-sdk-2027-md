<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.AssetBaseInterface.html -->

# maxon.AssetBaseInterface <a id="maxon-assetbaseinterface"></a>

## Description <a id="module-maxon.AssetBaseInterface"></a><a id="description"></a>

The base interface of [`maxon.AssetBaseWithUpdateInterface`](maxon.AssetBaseWithUpdateInterface.md#module-maxon.AssetBaseWithUpdateInterface) and [`maxon.AssetDescriptionInterface`](maxon.AssetDescriptionInterface.md#module-maxon.AssetDescriptionInterface).

It inherits from [`maxon.AssetIdentifierInterface`](maxon.AssetIdentifierInterface.md#module-maxon.AssetIdentifierInterface) and adds methods to obtain the repository.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetIdentifierInterface`](maxon.AssetIdentifierInterface.md#module-maxon.AssetIdentifierInterface)

Children Classes:

- [`maxon.AssetBase`](../reference/maxon.AssetBase.md#module-maxon.AssetBase)
- [`maxon.AssetDescriptionInterface`](maxon.AssetDescriptionInterface.md#module-maxon.AssetDescriptionInterface)
- [`maxon.AssetBaseWithUpdateInterface`](maxon.AssetBaseWithUpdateInterface.md#module-maxon.AssetBaseWithUpdateInterface)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.AssetBaseInterface.VIRTUAL`](maxon.AssetBaseInterface.VIRTUAL.md#maxon.AssetBaseInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetRepository`](#maxon.AssetBaseInterface.GetRepository)() | Returns the repository where this asset is stored. |
| [`GetRepositoryId`](#maxon.AssetBaseInterface.GetRepositoryId)() | Returns the identifier of the repository where this asset is stored. |

## Methods Definition <a id="methods-definition"></a>

### `AssetBaseInterface.GetRepository()` <a id="maxon.AssetBaseInterface.GetRepository"></a>

Returns the repository where this asset is stored.

> **Note:** The implementation should use a weak reference to avoid circular references.

**Returns:** Asset repository (empty when the asset doesn’t belong to a repository).

**Return type:** [`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)

### `AssetBaseInterface.GetRepositoryId()` <a id="maxon.AssetBaseInterface.GetRepositoryId"></a>

Returns the identifier of the repository where this asset is stored.

**Returns:** Asset repository identifier (empty when the asset doesn’t belong to a repository).

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)
