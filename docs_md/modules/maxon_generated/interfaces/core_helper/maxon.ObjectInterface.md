<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/interfaces/core_helper/maxon.ObjectInterface.html -->

# maxon.ObjectInterface <a id="maxon-objectinterface"></a>

## Description <a id="module-maxon.ObjectInterface"></a><a id="description"></a>

Object is the root of the interface hierarchy of the MAXON API.  
As a C++ class, each virtual interface is directly derived from Object, but as an interface a virtual interface may have an arbitrary number of base interfaces, all of which have Object as direct or indirect base interface.  
The interface hierarchy is reflected by the Ptr, ConstPtr and reference classes of the interfaces: They have conversion operators to all base interfaces, and they contain functions for all methods of the interface and its base interfaces.  
Object provides some general inheritance-related functions such as GetClass() and IsInstanceOf(), data-related functions such as Clone() and CopyFrom(), and virtual methods such as ToString() which are required for each Object.  
All Object instances are reference-counted.  
Within the declaration of an interface you may choose the reference behaviour on invocation of a non-const method (normal, const, copy-on-write).

## Inheritance diagram <a id="inheritance-diagram"></a>

Children Classes:

- [`maxon.IoHandlerInterface`](../io/maxon.IoHandlerInterface.md#module-maxon.IoHandlerInterface)
- [`maxon.ClassInterface`](maxon.ClassInterface.md#module-maxon.ClassInterface)
- [`maxon.UrlInterface`](../io/maxon.UrlInterface.md#module-maxon.UrlInterface)
- [`maxon.NetworkIpAddrInterface`](../network/maxon.NetworkIpAddrInterface.md#module-maxon.NetworkIpAddrInterface)
- [`maxon.IoBrowseInterface`](../io/maxon.IoBrowseInterface.md#module-maxon.IoBrowseInterface)
- [`maxon.DataDictionaryObjectInterface`](../core/maxon.DataDictionaryObjectInterface.md#module-maxon.DataDictionaryObjectInterface)
- [`maxon.DataDictionaryInterface`](../core/maxon.DataDictionaryInterface.md#module-maxon.DataDictionaryInterface)
- `maxon.UnitTestInterface`
- [`maxon.LoggerTypeInterface`](../logger/maxon.LoggerTypeInterface.md#module-maxon.LoggerTypeInterface)
- [`maxon.LoggerInterface`](../logger/maxon.LoggerInterface.md#module-maxon.LoggerInterface)
- [`maxon.ObserverObjectInterface`](maxon.ObserverObjectInterface.md#module-maxon.ObserverObjectInterface)
- [`maxon.FileFormatHandlerInterface`](../io/maxon.FileFormatHandlerInterface.md#module-maxon.FileFormatHandlerInterface)
- [`maxon.ObjectRef`](../../references/core_helper/maxon.ObjectRef.md#module-maxon.ObjectRef)
- `maxon.ParametricTypeInterface`
- [`maxon.AssetDataBasesInterface`](../../frameworks/asset/interface/maxon.AssetDataBasesInterface.md#module-maxon.AssetDataBasesInterface)
- [`maxon.AssetMetaDataInterface`](../../frameworks/asset/interface/maxon.AssetMetaDataInterface.md#module-maxon.AssetMetaDataInterface)
- [`maxon.AssetIdentifierInterface`](../../frameworks/asset/interface/maxon.AssetIdentifierInterface.md#module-maxon.AssetIdentifierInterface)
- [`maxon.DerivedAssetRepositoryDataInterface`](../../frameworks/asset/interface/maxon.DerivedAssetRepositoryDataInterface.md#module-maxon.DerivedAssetRepositoryDataInterface)
- [`maxon.LazyLanguageStringDataDescriptionDefinitionInterface`](../../frameworks/asset/interface/maxon.LazyLanguageStringDataDescriptionDefinitionInterface.md#module-maxon.LazyLanguageStringDataDescriptionDefinitionInterface)
- [`maxon.LazyLanguageDictionaryInterface`](../../frameworks/asset/interface/maxon.LazyLanguageDictionaryInterface.md#module-maxon.LazyLanguageDictionaryInterface)
- [`maxon.GraphAttributeInterface`](../../frameworks/graph/interface/maxon.GraphAttributeInterface.md#module-maxon.GraphAttributeInterface)
- [`maxon.GraphMessageInterface`](../../frameworks/graph/interface/maxon.GraphMessageInterface.md#module-maxon.GraphMessageInterface)
- [`maxon.NimbusBaseInterface`](../../frameworks/nodespace/interface/maxon.NimbusBaseInterface.md#module-maxon.NimbusBaseInterface)
- [`maxon.AssetCreationInterface`](../../frameworks/cinema_hybrid/interface/maxon.AssetCreationInterface.md#module-maxon.AssetCreationInterface)
- [`maxon.MeshAttributeClassInterface`](../../frameworks/mesh_misc/interface/maxon.MeshAttributeClassInterface.md#module-maxon.MeshAttributeClassInterface)
- [`maxon.CustomDataTagDisplayInterface`](../../frameworks/mesh_misc/interface/maxon.CustomDataTagDisplayInterface.md#module-maxon.CustomDataTagDisplayInterface)
- [`maxon.FilterInterface`](../../frameworks/render_filter/interface/maxon.FilterInterface.md#module-maxon.FilterInterface)
- [`maxon.FilterCommandQueueInterface`](../../frameworks/render_filter/interface/maxon.FilterCommandQueueInterface.md#module-maxon.FilterCommandQueueInterface)
- [`maxon.FilterContextInterface`](../../frameworks/render_filter/interface/maxon.FilterContextInterface.md#module-maxon.FilterContextInterface)
- [`maxon.FilterImageInterface`](../../frameworks/render_filter/interface/maxon.FilterImageInterface.md#module-maxon.FilterImageInterface)
- [`maxon.VolumeInterface`](../../frameworks/volume/interface/maxon.VolumeInterface.md#module-maxon.VolumeInterface)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`GetClass`](#maxon.ObjectInterface.GetClass)() |  |
| [`GetHashCodeImpl`](#maxon.ObjectInterface.GetHashCodeImpl)() | Retrieves the HashCode of the implementation of an Interface. |
| [`__init__`](#maxon.ObjectInterface.__init__)([data]) | Creates and stores internally the reference of the C++ Data. |

## Methods Definition <a id="methods-definition"></a>

### `ObjectInterface.GetClass()` <a id="maxon.ObjectInterface.GetClass"></a>

### `ObjectInterface.GetHashCodeImpl()` <a id="maxon.ObjectInterface.GetHashCodeImpl"></a>

Retrieves the HashCode of the implementation of an Interface.

**Returns:** The implementation hashcode.

**Return type:** int

### `ObjectInterface.__init__(data=None)` <a id="maxon.ObjectInterface.__init__"></a>

Creates and stores internally the reference of the C++ Data.  
When the passed data is None, an empty data is still allocated.

**Parameters:** **data** (*Optional*[*Data*]) – An optional c++ data used to hold the C++ reference alive during the whole lifetime of this python object.
