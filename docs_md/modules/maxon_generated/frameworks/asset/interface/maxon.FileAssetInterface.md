<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.FileAssetInterface.html -->

# maxon.FileAssetInterface <a id="maxon-fileassetinterface"></a>

## Description <a id="module-maxon.FileAssetInterface"></a><a id="description"></a>

An Asset represents digital content which can be managed by an [`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef) “asset repository”. The management includes versioning, meta data and automatic updates.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetInterface`](maxon.AssetInterface.md#module-maxon.AssetInterface)

Child Class:

- [`maxon.FileAsset`](../reference/maxon.FileAsset.md#module-maxon.FileAsset)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.FileAssetInterface.VIRTUAL`](maxon.FileAssetInterface.VIRTUAL.md#maxon.FileAssetInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Create`](#maxon.FileAssetInterface.Create)(url) | Creates a new [`maxon.FileAsset`](../reference/maxon.FileAsset.md#module-maxon.FileAsset) for the given [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url). |
| [`GetUrl`](#maxon.FileAssetInterface.GetUrl)() | The [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) to access the file which is wrapped by this asset. |

## Methods Definition <a id="methods-definition"></a>

### *static* `FileAssetInterface.Create(url)` <a id="maxon.FileAssetInterface.Create"></a>

Creates a new [`maxon.FileAsset`](../reference/maxon.FileAsset.md#module-maxon.FileAsset) for the given [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url). The returned file asset doesn’t belong to a repository, you have to store it afterwards at a repository. This will change the [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) to a [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) within the repository.

**Parameters:** **url** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – The [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) of the file (or directory) which shall be made an asset.

**Returns:** The [`maxon.FileAsset`](../reference/maxon.FileAsset.md#module-maxon.FileAsset) wrapping [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url).

**Return type:** [`maxon.FileAsset`](../reference/maxon.FileAsset.md#module-maxon.FileAsset)

### `FileAssetInterface.GetUrl()` <a id="maxon.FileAssetInterface.GetUrl"></a>

The [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) to access the file which is wrapped by this asset. :return: The [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) of the file (or directory). :rtype: [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)
