<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.AssetLinkInterface.html -->

# maxon.AssetLinkInterface <a id="maxon-assetlinkinterface"></a>

## Description <a id="module-maxon.AssetLinkInterface"></a><a id="description"></a>

An AssetLink is a symbolic link to an asset identified by its id and version. Also an ASSET_UPDATE_POLICY is stored to control the behavior of the link when newer versions of the linked asset exists.

Alternatively an [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink) can also just wrap a [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) from which an asset can be loaded directly.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.AssetIdentifierInterface`](maxon.AssetIdentifierInterface.md#module-maxon.AssetIdentifierInterface)

Child Class:

- [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.AssetLinkInterface.VIRTUAL`](maxon.AssetLinkInterface.VIRTUAL.md#maxon.AssetLinkInterface.VIRTUAL) |  |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Create`](#maxon.AssetLinkInterface.Create)(type, aid[, up]) | Creates a new [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink). |
| [`GetUpdatePolicy`](#maxon.AssetLinkInterface.GetUpdatePolicy)() | Returns the update policy which this link uses. |
| [`GetUrl`](#maxon.AssetLinkInterface.GetUrl)() | Returns the [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) for a Url-based [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink). |
| [`Resolve`](#maxon.AssetLinkInterface.Resolve)(context) | Resolves this [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink) to an [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription) in the given context. |
| [`SetUpdatePolicy`](#maxon.AssetLinkInterface.SetUpdatePolicy)(up) | Returns the update policy which this link uses. |

## Methods Definition <a id="methods-definition"></a>

### *static* `AssetLinkInterface.Create(type, aid, up=None)` <a id="maxon.AssetLinkInterface.Create"></a>

Creates a new [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink).

Use an [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) for assets which aren’t stored in a repository, but shall be read directly from a Url such as a local image file.  
Only one of the next calls is possible:

> - Create(type: [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), aid: [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url))
> - Create(type: [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), aid: [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)], up: `maxon.ASSET_UPDATE_POLICY`)

**Parameters:**

- **type** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The expected type of the asset.
- **aid** (Union[[`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url), [`maxon.Tuple`](../../../datatypes/collection/maxon.Tuple.md#module-maxon.Tuple) [[`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id), [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)]]) – The [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) where the asset can be read from or the identifier and version of the asset.
- **up** (Optional[`maxon.ASSET_UPDATE_POLICY`]) – The update policy which the created link shall use. Only used when an tuple is passed for *aid*.

**Returns:** A new AssetLink.

**Return type:** [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink)

### `AssetLinkInterface.GetUpdatePolicy()` <a id="maxon.AssetLinkInterface.GetUpdatePolicy"></a>

Returns the update policy which this link uses.

**Returns:** The update policy of this link.

**Return type:**

`maxon.ASSET_UPDATE_POLICY`

### `AssetLinkInterface.GetUrl()` <a id="maxon.AssetLinkInterface.GetUrl"></a>

Returns the [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) for a Url-based [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink).

**Returns:** The [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url) to which this [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink) points. Or a null value when this [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink) uses an asset identifier instead of a [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url).

**Return type:** [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)

### `AssetLinkInterface.Resolve(context)` <a id="maxon.AssetLinkInterface.Resolve"></a>

Resolves this [`maxon.AssetLink`](../reference/maxon.AssetLink.md#module-maxon.AssetLink) to an [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription) in the given context.

The asset identifier of this link is used to find the asset in context, and if this link uses the policy *maxon.ASSET_UPDATE_POLICY.IMPLICIT* the latest version of the asset is used, otherwise the version recorded in this link.

**Parameters:** **context** ([`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)) – The repository to use for the asset lookup.

**Returns:** The found AssetDescription or a null value when no asset could be found.

**Return type:** [`maxon.AssetDescription`](../reference/maxon.AssetDescription.md#module-maxon.AssetDescription)

### `AssetLinkInterface.SetUpdatePolicy(up)` <a id="maxon.AssetLinkInterface.SetUpdatePolicy"></a>

Returns the update policy which this link uses.

**Parameters:** **up** (`maxon.ASSET_UPDATE_POLICY`) – The new update policy for this link.
