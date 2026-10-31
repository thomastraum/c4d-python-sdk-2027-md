<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/asset/interface/maxon.AssetDataBasesInterface.html -->

# maxon.AssetDataBasesInterface <a id="maxon-assetdatabasesinterface"></a>

## Description <a id="module-maxon.AssetDataBasesInterface"></a><a id="description"></a>

This interface provides helper functions to register asset repositories.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.ObjectInterface`](../../../interfaces/core_helper/maxon.ObjectInterface.md#module-maxon.ObjectInterface)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`ClearAssetDatabaseCache`](#maxon.AssetDataBasesInterface.ClearAssetDatabaseCache)() | Deletes the cache. |
| [`FindRepository`](#maxon.AssetDataBasesInterface.FindRepository)(repository) | Returns the `maxon.url` of a asset repository. |
| [`GetAssetDatabaseCachePath`](#maxon.AssetDataBasesInterface.GetAssetDatabaseCachePath)() | GetAssetDatabaseCachePath returns the path to the cache folder. |
| [`GetAssetDatabaseCacheSize`](#maxon.AssetDataBasesInterface.GetAssetDatabaseCacheSize)() | GetAssetDatabaseCacheSize returns the size of the cached files. |
| [`GetDatabases`](#maxon.AssetDataBasesInterface.GetDatabases)([entry]) | Returns all repositories added by the user. |
| [`ReloadAssetRepositories`](#maxon.AssetDataBasesInterface.ReloadAssetRepositories)() | ReloadDatabases reloads the asset repositories from disk. |
| [`SetAssetDatabaseCachePath`](#maxon.AssetDataBasesInterface.SetAssetDatabaseCachePath)(*args) | SetAssetDatabaseCachePath sets a new cache path to store temporary downloaded objects. |
| [`SetDatabases`](#maxon.AssetDataBasesInterface.SetDatabases)(newDataBases) | Set the new user repositories. |
| [`WaitForDatabaseLoading`](#maxon.AssetDataBasesInterface.WaitForDatabaseLoading)() | Waits for the execution of the database loading. |
| [`WriteGmlDependencies`](#maxon.AssetDataBasesInterface.WriteGmlDependencies)() | Writes the gml file with the dependencies of the given asset repository. |

## Methods Definition <a id="methods-definition"></a>

### *static* `AssetDataBasesInterface.ClearAssetDatabaseCache()` <a id="maxon.AssetDataBasesInterface.ClearAssetDatabaseCache"></a>

Deletes the cache.

### *static* `AssetDataBasesInterface.FindRepository(repository)` <a id="maxon.AssetDataBasesInterface.FindRepository"></a>

Returns the `maxon.url` of a asset repository.

When `repository` is of type [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url), the result must be cast to a repository reference to provide meaningful access to the found repository.

```python
url: maxon.Url = maxon.Url(r"/Volumes/database")
obj: maxon.ObjectRef = maxon.AssetDataBasesInterface.FindRepository(url)
if obj.IsNullValue():
    raise RuntimeError(f"Could not establish repository for: {url}.")

# Cast #obj to an AssetRepositoryRef. What #obj must be cast to depends on the repository #url
# is representing. But all repositories are of type AssetRepositoryInterface, so a ref for that
# will give access to all common asset repository methods.
repo: maxon.AssetRepositoryRef = maxon.Cast(maxon.AssetRepositoryRef, obj)
if repo.IsNullValue():
    raise RuntimeError(f"Could not establish repository for: {url}.")
```

**Parameters:** **repository** (Union[[`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url), [`maxon.AssetRepositoryRef`](../reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)]) – Repository to find.

**Return type:** Union[[`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url), [`maxon.ObjectRef`](../../../references/core_helper/maxon.ObjectRef.md#module-maxon.ObjectRef)]

**Returns:** On success the repository reference or url of *repository*, depending on the type of *repository*.

### *static* `AssetDataBasesInterface.GetAssetDatabaseCachePath()` <a id="maxon.AssetDataBasesInterface.GetAssetDatabaseCachePath"></a>

GetAssetDatabaseCachePath returns the path to the cache folder.

**Returns:** The path to the cache folder.

**Return type:** [`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)

### *static* `AssetDataBasesInterface.GetAssetDatabaseCacheSize()` <a id="maxon.AssetDataBasesInterface.GetAssetDatabaseCacheSize"></a>

GetAssetDatabaseCacheSize returns the size of the cached files.

**Returns:** The size of the cached files.

**Return type:** int

### *static* `AssetDataBasesInterface.GetDatabases(entry=None)` <a id="maxon.AssetDataBasesInterface.GetDatabases"></a>

Returns all repositories added by the user.

**Parameters:** **entry** (*Optional*[*Union*[*list*, *Callable*[[*maxon.AssetDatabaseStruct*], *bool*]]]) – ValueReceiver to receive the entries.

**Returns:** If *callback* is None or a list then a list of [`maxon.AssetDatabaseStruct`](../datatype/maxon.AssetDatabaseStruct.md#module-maxon.AssetDatabaseStruct) otherwise **False** if *callback* cancelled further evaluation, **True** otherwise.

**Return type:** Union[list[[`maxon.AssetDatabaseStruct`](../datatype/maxon.AssetDatabaseStruct.md#module-maxon.AssetDatabaseStruct)], bool]

### *static* `AssetDataBasesInterface.ReloadAssetRepositories()` <a id="maxon.AssetDataBasesInterface.ReloadAssetRepositories"></a>

ReloadDatabases reloads the asset repositories from disk.

### *static* `AssetDataBasesInterface.SetAssetDatabaseCachePath(*args)` <a id="maxon.AssetDataBasesInterface.SetAssetDatabaseCachePath"></a>

SetAssetDatabaseCachePath sets a new cache path to store temporary downloaded objects.

**Parameters:** **cachePath** ([`maxon.Url`](../../../references/io/maxon.Url.md#module-maxon.Url)) – Path to set.

### *static* `AssetDataBasesInterface.SetDatabases(newDataBases)` <a id="maxon.AssetDataBasesInterface.SetDatabases"></a>

Set the new user repositories.

**Parameters:** **newDataBases** (Union[[`maxon.AssetDatabaseStruct`](../datatype/maxon.AssetDatabaseStruct.md#module-maxon.AssetDatabaseStruct), list[[`maxon.AssetDatabaseStruct`](../datatype/maxon.AssetDatabaseStruct.md#module-maxon.AssetDatabaseStruct)], [`maxon.Block`](../../../datatypes/collection/maxon.Block.md#module-maxon.Block) [[`maxon.AssetDatabaseStruct`](../datatype/maxon.AssetDatabaseStruct.md#module-maxon.AssetDatabaseStruct)]]) – Block with tuples of the new urls and activation states.

### *static* `AssetDataBasesInterface.WaitForDatabaseLoading()` <a id="maxon.AssetDataBasesInterface.WaitForDatabaseLoading"></a>

Waits for the execution of the database loading.

Since this is async now during the startup and modification of database lists it gives the developer a chance to wait for that end.

**Returns:** **True** if loading is finished. **False** if canceled.

**Return type:** bool

### *static* `AssetDataBasesInterface.WriteGmlDependencies()` <a id="maxon.AssetDataBasesInterface.WriteGmlDependencies"></a>

Writes the gml file with the dependencies of the given asset repository.
