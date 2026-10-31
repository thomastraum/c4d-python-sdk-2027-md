<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/net/Repository/index.html -->

# c4d.modules.net.Repository <a id="c4d-modules-net-repository"></a>

## *class* `c4d.modules.net.Repository` <a id="c4d.modules.net.Repository"></a>

*New in version R16.021.*

> **Warning:** This type cannot be instantiated.

## Overview <a id="overview"></a>

- [`Repository.ConvertAbsolute2RelativePath()`](#c4d.modules.net.Repository.ConvertAbsolute2RelativePath)
- [`Repository.ConvertRelative2Absolute()`](#c4d.modules.net.Repository.ConvertRelative2Absolute)
- [`Repository.GetJobsPath()`](#c4d.modules.net.Repository.GetJobsPath): Gets the jobs path.
- [`Repository.GetRepositoryPath()`](#c4d.modules.net.Repository.GetRepositoryPath): Gets the repository path.
- [`Repository.SetRepositoryPath()`](#c4d.modules.net.Repository.SetRepositoryPath): Sets the repository path.

## Members <a id="members"></a>

### Path Management <a id="c4d.modules.net.Repository-method-Path-Management"></a>

#### `Repository.ConvertAbsolute2RelativePath(self)` <a id="c4d.modules.net.Repository.ConvertAbsolute2RelativePath"></a>

*New in version R16.021.*

#### `Repository.ConvertRelative2Absolute(self)` <a id="c4d.modules.net.Repository.ConvertRelative2Absolute"></a>

*New in version R16.021.*

#### `Repository.GetJobsPath(self, server)` <a id="c4d.modules.net.Repository.GetJobsPath"></a>

Gets the jobs path.

*New in version R16.021.*

**Parameters:** **server** (*bool*) – Pass **True** to ask for the jobs path on the server.

**Return type:** str

**Returns:** The jobs path.

#### `Repository.GetRepositoryPath(self)` <a id="c4d.modules.net.Repository.GetRepositoryPath"></a>

Gets the repository path.

*New in version R16.021.*

**Return type:** str

**Returns:** The default repository path.

#### `Repository.SetRepositoryPath(self, repositoryPath)` <a id="c4d.modules.net.Repository.SetRepositoryPath"></a>

Sets the repository path.

*New in version R16.021.*

**Parameters:** **repositoryPath** (*str*) – The repository path to set.
