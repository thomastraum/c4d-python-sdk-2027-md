<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/GeResource/index.html -->

# c4d.plugins.GeResource <a id="c4d-plugins-geresource"></a>

## *class* `c4d.plugins.GeResource` <a id="c4d.plugins.GeResource"></a>

This class is used for accessing resource files on the hard drive, for example to load dialog resources or to access string tables.

## Overview <a id="overview"></a>

**Magic Methods**

- [`GeResource.__init__()`](#c4d.plugins.GeResource.__init__): Creates a new resource object.

**Resource Management**

- [`GeResource.Init()`](#c4d.plugins.GeResource.Init): Initializes the resources from their files in the ‘res’ folder.
- [`GeResource.InitAsGlobal()`](#c4d.plugins.GeResource.InitAsGlobal): Lets access the *Cinema 4D* main application string resource.
- [`GeResource.LoadString()`](#c4d.plugins.GeResource.LoadString): Loads a string from the string resource file.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.plugins.GeResource-method-Magic-Methods"></a>

#### `GeResource.__init__(self)` <a id="c4d.plugins.GeResource.__init__"></a>

Creates a new resource object.

### Resource Management <a id="c4d.plugins.GeResource-method-Resource-Management"></a>

#### `GeResource.Init(self, path)` <a id="c4d.plugins.GeResource.Init"></a>

Initializes the resources from their files in the ‘res’ folder.

**Parameters:** **path** (*str*) – The root directory of the plugin’s folder to find the ‘res’ folder.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `GeResource.InitAsGlobal(self)` <a id="c4d.plugins.GeResource.InitAsGlobal"></a>

Lets access the *Cinema 4D* main application string resource.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `GeResource.LoadString(self, id)` <a id="c4d.plugins.GeResource.LoadString"></a>

Loads a string from the string resource file.

> > **See also:** [`GeLoadString()`](../index.md#c4d.plugins.GeLoadString)

**Parameters:** **id** (*int*) – The ID for the string in the resource file.

**Return type:** str

**Returns:** The string from the resource file for the passed *id*.
