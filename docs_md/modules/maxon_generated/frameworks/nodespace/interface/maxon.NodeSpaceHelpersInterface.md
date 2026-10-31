<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/nodespace/interface/maxon.NodeSpaceHelpersInterface.html -->

# maxon.NodeSpaceHelpersInterface <a id="maxon-nodespacehelpersinterface"></a>

## Description <a id="module-maxon.NodeSpaceHelpersInterface"></a><a id="description"></a>

Provides a collection of static helpers.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetNodeSpaceData`](#maxon.NodeSpaceHelpersInterface.GetNodeSpaceData)(spaceId) | Looks up the NodeSpaceRef within the MaterialNodeSpaces registry and returns the result of NodeSpaceInterface::GetData(). |
| [`LoadDescription`](#maxon.NodeSpaceHelpersInterface.LoadDescription)(spaceDescriptionId) | Loads resource name under the current language for the provided Id and assigns it to the attribute maxon.nodes.NODESPACE.SPACENAME of the returned data container. |

## Methods Definition <a id="methods-definition"></a>

### *static* `NodeSpaceHelpersInterface.GetNodeSpaceData(spaceId)` <a id="maxon.NodeSpaceHelpersInterface.GetNodeSpaceData"></a>

Looks up the NodeSpaceRef within the MaterialNodeSpaces registry and returns the result of NodeSpaceInterface::GetData(). :param spaceId: The id of the space. :type spaceId: [`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id) :return: The data container of the space. :rtype: [`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)

### *static* `NodeSpaceHelpersInterface.LoadDescription(spaceDescriptionId)` <a id="maxon.NodeSpaceHelpersInterface.LoadDescription"></a>

Loads resource name under the current language for the provided Id and assigns it to the attribute maxon.nodes.NODESPACE.SPACENAME of the returned data container.

**Parameters:** **spaceDescriptionId** ([`maxon.Id`](../../../datatypes/id/maxon.Id.md#module-maxon.Id)) – The id of the named description.

**Returns:** The data container with the assigned maxon.nodes.NODESPACE.SPACENAME attribute.

**Return type:** [`maxon.DataDictionary`](../../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)
