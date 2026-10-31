<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.AssetIdentifierInterface.html -->

# maxon.AssetIdentifierInterface <a id="maxon-assetidentifierinterface"></a>

## Description <a id="module-maxon.AssetIdentifierInterface"></a><a id="description"></a>

The base interface of [`maxon.AssetBaseInterface`](maxon.AssetBaseInterface.md#module-maxon.AssetBaseInterface) and [`maxon.AssetLinkInterface`](maxon.AssetLinkInterface.md#module-maxon.AssetLinkInterface). It contains their common methods to obtain type, identifier and version.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Children Classes:

- [`maxon.AssetIdentifier`](../reference/maxon.AssetIdentifier.md#module-maxon.AssetIdentifier)
- [`maxon.AssetLinkInterface`](maxon.AssetLinkInterface.md#module-maxon.AssetLinkInterface)
- [`maxon.AssetBaseInterface`](maxon.AssetBaseInterface.md#module-maxon.AssetBaseInterface)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.AssetIdentifierInterface.VIRTUAL`](maxon.AssetIdentifierInterface.VIRTUAL.md#maxon.AssetIdentifierInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetId`](#maxon.AssetIdentifierInterface.GetId)() | Returns the identifier of this asset. |
| [`GetIdAndVersion`](#maxon.AssetIdentifierInterface.GetIdAndVersion)() | Returns the identifier and version of this asset as a tuple. |
| [`GetTypeId`](#maxon.AssetIdentifierInterface.GetTypeId)() | Returns the identifier of the [`maxon.AssetType`](../reference/maxon.AssetType.md#module-maxon.AssetType) of this asset. |
| [`GetVersion`](#maxon.AssetIdentifierInterface.GetVersion)() | Returns the version of this asset. |

## Methods Definition <a id="methods-definition"></a>

### `AssetIdentifierInterface.GetId()` <a id="maxon.AssetIdentifierInterface.GetId"></a>

Returns the identifier of this asset. Asset identifiers have to be globally unique.

**Returns:** Asset identifier (empty for an Asset which doesn’t belong to a repository).

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)

### `AssetIdentifierInterface.GetIdAndVersion()` <a id="maxon.AssetIdentifierInterface.GetIdAndVersion"></a>

Returns the identifier and version of this asset as a tuple.

**Returns:** (identifier, version) of this asset.

**Return type:** [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]

### `AssetIdentifierInterface.GetTypeId()` <a id="maxon.AssetIdentifierInterface.GetTypeId"></a>

Returns the identifier of the [`maxon.AssetType`](../reference/maxon.AssetType.md#module-maxon.AssetType) of this asset.

**Returns:** Identifier of the [`maxon.AssetType`](../reference/maxon.AssetType.md#module-maxon.AssetType) of this asset.

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)

### `AssetIdentifierInterface.GetVersion()` <a id="maxon.AssetIdentifierInterface.GetVersion"></a>

Returns the version of this asset. | Version identifiers are assigned by repositories when assets are stored, typically this is a hash value derived from the asset content or a UUID. | In general two assets should have equal version identifiers only if they have equal content.

**Returns:** Asset identifier (empty for an Asset which doesn’t belong to a repository).

**Return type:** [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)
