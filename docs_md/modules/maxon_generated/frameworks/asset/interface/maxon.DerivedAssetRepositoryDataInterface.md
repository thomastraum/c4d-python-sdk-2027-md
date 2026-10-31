<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.DerivedAssetRepositoryDataInterface.html -->

# maxon.DerivedAssetRepositoryDataInterface <a id="maxon-derivedassetrepositorydatainterface"></a>

## Description <a id="module-maxon.DerivedAssetRepositoryDataInterface"></a><a id="description"></a>

Object is the root of the interface hierarchy of the MAXON API.  
As a C++ class, each virtual interface is directly derived from Object, but as an interface a virtual interface may have an arbitrary number of base interfaces, all of which have Object as direct or indirect base interface.  
The interface hierarchy is reflected by the Ptr, ConstPtr and reference classes of the interfaces: They have conversion operators to all base interfaces, and they contain functions for all methods of the interface and its base interfaces.  
Object provides some general inheritance-related functions such as GetClass() and IsInstanceOf(), data-related functions such as Clone() and CopyFrom(), and virtual methods such as ToString() which are required for each Object.  
All Object instances are reference-counted.  
Within the declaration of an interface you may choose the reference behaviour on invocation of a non-const method (normal, const, copy-on-write).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

Child Class:

- [`maxon.DerivedAssetRepositoryDataRef`](../reference/maxon.DerivedAssetRepositoryDataRef.md#module-maxon.DerivedAssetRepositoryDataRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`HandleAssetErased`](#maxon.DerivedAssetRepositoryDataInterface.HandleAssetErased)(asset) | Gets called when an asset has been erased. |
| [`HandleAssetStored`](#maxon.DerivedAssetRepositoryDataInterface.HandleAssetStored)(asset) | Gets called when an asset has been stored. |
| [`HandleAssetUpdated`](#maxon.DerivedAssetRepositoryDataInterface.HandleAssetUpdated)(asset) | Gets called when an asset has been updated. |
| [`HandleBaseChanged`](#maxon.DerivedAssetRepositoryDataInterface.HandleBaseChanged)(repo, base, added) | Gets called when the base of the asset repository has been changed. |
| [`HandleDownloadStateChanged`](#maxon.DerivedAssetRepositoryDataInterface.HandleDownloadStateChanged)(repository, finished) |  |
| [`HandleMetaDataStored`](#maxon.DerivedAssetRepositoryDataInterface.HandleMetaDataStored)(asset, metaId, kind, …) | Gets called when meta data has been stored. |

## Methods Definition <a id="methods-definition"></a>

### `DerivedAssetRepositoryDataInterface.HandleAssetErased(asset)` <a id="maxon.DerivedAssetRepositoryDataInterface.HandleAssetErased"></a>

Gets called when an asset has been erased.

**Parameters:** **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – The description of the erased asset version.

### `DerivedAssetRepositoryDataInterface.HandleAssetStored(asset)` <a id="maxon.DerivedAssetRepositoryDataInterface.HandleAssetStored"></a>

Gets called when an asset has been stored.

**Parameters:** **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – The description of the new asset version.

### `DerivedAssetRepositoryDataInterface.HandleAssetUpdated(asset)` <a id="maxon.DerivedAssetRepositoryDataInterface.HandleAssetUpdated"></a>

Gets called when an asset has been updated.

**Parameters:** **asset** ([`maxon.Asset`](../reference/maxon.Asset.md#module-maxon.Asset)) – The updated asset.

### `DerivedAssetRepositoryDataInterface.HandleBaseChanged(repo, base, added)` <a id="maxon.DerivedAssetRepositoryDataInterface.HandleBaseChanged"></a>

Gets called when the base of the asset repository has been changed.

**Parameters:**

- **repo** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – The asset repository which owns the derived data.
- **base** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – The base repository.
- **added** (*bool*) – **True** if base has been added, **False** if it has been removed.

### `DerivedAssetRepositoryDataInterface.HandleDownloadStateChanged(repository, finished)` <a id="maxon.DerivedAssetRepositoryDataInterface.HandleDownloadStateChanged"></a>

### `DerivedAssetRepositoryDataInterface.HandleMetaDataStored(asset, metaId, kind, prevData, newData)` <a id="maxon.DerivedAssetRepositoryDataInterface.HandleMetaDataStored"></a>

Gets called when meta data has been stored.

**Parameters:**

- **asset** ([`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)) – The asset.
- **metaId** ([`maxon.InternedId`](../../../datatypes/id/maxon.InternedId.md#module-maxon.InternedId)) – The identifier of the stored meta data attribute.
- **kind** ([`maxon.AssetMetaDataInterface.KIND`](../../../enums/maxon.AssetMetaDataInterface.KIND.md#module-maxon.AssetMetaDataInterface.KIND)) – The meta data kind.
- **prevData** ([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The previous value of the attribute (may be empty).
- **newData** ([`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)) – The new value of the attribute.
