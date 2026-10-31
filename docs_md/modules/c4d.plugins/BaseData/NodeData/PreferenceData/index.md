<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseData/NodeData/PreferenceData/index.html -->

# c4d.plugins.PreferenceData <a id="c4d-plugins-preferencedata"></a>

## *class* `c4d.plugins.PreferenceData` <a id="c4d.plugins.PreferenceData"></a>

Defines a new preference category in the Cinema 4D preference dialog.  
Register this type of plugin with [`RegisterPreferencePlugin()`](../../../index.md#c4d.plugins.RegisterPreferencePlugin).

*New in version R19.*

Parent Class:

- [`c4d.plugins.NodeData`](../index.md#c4d.plugins.NodeData)

## Overview <a id="overview"></a>

- [`PreferenceData.InitPreferenceValue()`](#c4d.plugins.PreferenceData.InitPreferenceValue): Initializes preference values in *bc*.

## Members <a id="members"></a>

### Preference Initialization <a id="c4d.plugins.PreferenceData-method-Preference-Initialization"></a>

#### `PreferenceData.InitPreferenceValue(self, id, data, desc, descid, bc)` <a id="c4d.plugins.PreferenceData.InitPreferenceValue"></a>

Initializes preference values in *bc*.

**Parameters:**

- **id** (*int*) – The world container ID of the preference parameter.
- **data** (*any*) – The value used for the initialization.
- **desc** (*Optional*[[*c4d.Description*](../../../../c4d/Description/index.md#c4d.Description)]) – The description of the preference hook. If **None**, *id* is used instead of *descid*.
- **descid** ([*c4d.DescID*](../../../../c4d/DescID/index.md#c4d.DescID)) – The description ID of the preference parameter.
- **bc** ([*c4d.BaseContainer*](../../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The preference world container. A plugin should always store its parameters in a sub-container in the world container.
