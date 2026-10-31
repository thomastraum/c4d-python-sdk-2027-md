<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/datatypes/base_core/maxon.Data.html -->

# maxon.Data <a id="maxon-data"></a>

## Description <a id="module-maxon.Data"></a><a id="description"></a>

An object of this class can store every type of data as long as that type has been registered (see [`maxon.DataType`](maxon.DataType.md#module-maxon.DataType)).

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Ref`](maxon.Ref.md#module-maxon.Ref)

Children Classes:

- [`maxon.Builtin`](maxon.Builtin.md#module-maxon.Builtin)
- `maxon.IdStruct`
- [`maxon.SourceLocation`](../core/maxon.SourceLocation.md#module-maxon.SourceLocation)
- [`maxon.UnknownDataType`](maxon.UnknownDataType.md#module-maxon.UnknownDataType)
- [`maxon.ConfigInit`](../core/maxon.ConfigInit.md#module-maxon.ConfigInit)
- [`maxon.UniversalDateTime`](../time/maxon.UniversalDateTime.md#module-maxon.UniversalDateTime)
- [`maxon.LocalDateTime`](../time/maxon.LocalDateTime.md#module-maxon.LocalDateTime)
- [`maxon.DelegateBase`](../core/maxon.DelegateBase.md#module-maxon.DelegateBase)
- [`maxon.ThreadRef`](../../references/core/maxon.ThreadRef.md#module-maxon.ThreadRef)
- [`maxon.Block`](../collection/maxon.Block.md#module-maxon.Block)
- [`maxon.StridedBlock`](../collection/maxon.StridedBlock.md#module-maxon.StridedBlock)
- [`maxon.BaseArray`](../collection/maxon.BaseArray.md#module-maxon.BaseArray)
- [`maxon.Pair`](../collection/maxon.Pair.md#module-maxon.Pair)
- [`maxon.Array`](../collection/maxon.Array.md#module-maxon.Array)
- [`maxon.RegistryEntryIteratorInterface`](../core_iterator/maxon.RegistryEntryIteratorInterface.md#module-maxon.RegistryEntryIteratorInterface)
- [`maxon.RegistryInterface`](../../interfaces/core/maxon.RegistryInterface.md#module-maxon.RegistryInterface)
- [`maxon.PlainIterator`](../core_iterator/maxon.PlainIterator.md#module-maxon.PlainIterator)
- [`maxon.DataDictionaryIterator`](../core_iterator/maxon.DataDictionaryIterator.md#module-maxon.DataDictionaryIterator)
- [`maxon.String`](../../references/core/maxon.String.md#module-maxon.String)
- [`maxon.CString`](../../references/core/maxon.CString.md#module-maxon.CString)
- [`maxon.IoBrowseRef`](../../references/io/maxon.IoBrowseRef.md#module-maxon.IoBrowseRef)
- [`maxon.DataDictionary`](../../references/core/maxon.DataDictionary.md#module-maxon.DataDictionary)
- [`maxon.ObjectRef`](../../references/core_helper/maxon.ObjectRef.md#module-maxon.ObjectRef)
- [`maxon.LoggerTypeRef`](../../references/logger/maxon.LoggerTypeRef.md#module-maxon.LoggerTypeRef)
- [`maxon.LoggerRef`](../../references/logger/maxon.LoggerRef.md#module-maxon.LoggerRef)
- [`maxon.OutputStreamRef`](../../references/io/maxon.OutputStreamRef.md#module-maxon.OutputStreamRef)
- [`maxon.InputStreamRef`](../../references/io/maxon.InputStreamRef.md#module-maxon.InputStreamRef)
- [`maxon.IoConnectionRef`](../../references/io/maxon.IoConnectionRef.md#module-maxon.IoConnectionRef)
- `maxon.CryptoKey`
- [`maxon.FileFormatHandler`](../../references/io/maxon.FileFormatHandler.md#module-maxon.FileFormatHandler)
- [`maxon.FileFormat`](../../references/io/maxon.FileFormat.md#module-maxon.FileFormat)
- [`maxon.MachineRef`](../../references/information/maxon.MachineRef.md#module-maxon.MachineRef)
- [`maxon.Class`](../../references/core_helper/maxon.Class.md#module-maxon.Class)
- [`maxon.NetworkIpAddr`](../../references/network/maxon.NetworkIpAddr.md#module-maxon.NetworkIpAddr)
- [`maxon.NetworkIpAddrPort`](../../references/network/maxon.NetworkIpAddrPort.md#module-maxon.NetworkIpAddrPort)
- [`maxon.Url`](../../references/io/maxon.Url.md#module-maxon.Url)
- [`maxon.InOutputStreamRef`](../../references/io/maxon.InOutputStreamRef.md#module-maxon.InOutputStreamRef)
- [`maxon.IoHandler`](../../references/io/maxon.IoHandler.md#module-maxon.IoHandler)
- [`maxon.Uuid`](../../references/core/maxon.Uuid.md#module-maxon.Uuid)
- [`maxon.LanguageRef`](../../references/core/maxon.LanguageRef.md#module-maxon.LanguageRef)
- [`maxon.DataDescription`](../../references/core/maxon.DataDescription.md#module-maxon.DataDescription)
- [`maxon.Col3`](../vec_col_mat/maxon.Col3.md#module-maxon.Col3)
- [`maxon.Vec3`](../vec_col_mat/maxon.Vec3.md#module-maxon.Vec3)
- [`maxon.GradientKnot`](../../interfaces/misc/maxon.GradientKnot.md#module-maxon.GradientKnot)
- [`maxon.Gradient`](../../interfaces/misc/maxon.Gradient.md#module-maxon.Gradient)
- [`maxon.GradientRenderData`](../../interfaces/misc/maxon.GradientRenderData.md#module-maxon.GradientRenderData)
- `maxon.ParametricType`
- [`maxon.AssetDatabaseStruct`](../../frameworks/asset/datatype/maxon.AssetDatabaseStruct.md#module-maxon.AssetDatabaseStruct)
- [`maxon.DragAndDropDataAssetArray`](../../frameworks/asset/datatype/maxon.DragAndDropDataAssetArray.md#module-maxon.DragAndDropDataAssetArray)
- [`maxon.AssetDependencyStruct`](../../frameworks/asset/datatype/maxon.AssetDependencyStruct.md#module-maxon.AssetDependencyStruct)
- [`maxon.AssetMetaData`](../../frameworks/asset/reference/maxon.AssetMetaData.md#module-maxon.AssetMetaData)
- [`maxon.AssetType`](../../frameworks/asset/reference/maxon.AssetType.md#module-maxon.AssetType)
- [`maxon.AssetIdentifier`](../../frameworks/asset/reference/maxon.AssetIdentifier.md#module-maxon.AssetIdentifier)
- [`maxon.AssetLink`](../../frameworks/asset/reference/maxon.AssetLink.md#module-maxon.AssetLink)
- [`maxon.AssetRepositoryRef`](../../frameworks/asset/reference/maxon.AssetRepositoryRef.md#module-maxon.AssetRepositoryRef)
- [`maxon.DerivedAssetRepositoryDataRef`](../../frameworks/asset/reference/maxon.DerivedAssetRepositoryDataRef.md#module-maxon.DerivedAssetRepositoryDataRef)
- [`maxon.AssetBase`](../../frameworks/asset/reference/maxon.AssetBase.md#module-maxon.AssetBase)
- [`maxon.AssetDescription`](../../frameworks/asset/reference/maxon.AssetDescription.md#module-maxon.AssetDescription)
- [`maxon.AssetBaseWithUpdate`](../../frameworks/asset/reference/maxon.AssetBaseWithUpdate.md#module-maxon.AssetBaseWithUpdate)
- [`maxon.AssetReference`](../../frameworks/asset/reference/maxon.AssetReference.md#module-maxon.AssetReference)
- [`maxon.Asset`](../../frameworks/asset/reference/maxon.Asset.md#module-maxon.Asset)
- [`maxon.UpdatableAsset`](../../frameworks/asset/reference/maxon.UpdatableAsset.md#module-maxon.UpdatableAsset)
- [`maxon.UpdatableAssetRepositoryRef`](../../frameworks/asset/reference/maxon.UpdatableAssetRepositoryRef.md#module-maxon.UpdatableAssetRepositoryRef)
- [`maxon.CompactableAssetRepositoryRef`](../../frameworks/asset/reference/maxon.CompactableAssetRepositoryRef.md#module-maxon.CompactableAssetRepositoryRef)
- [`maxon.FileAsset`](../../frameworks/asset/reference/maxon.FileAsset.md#module-maxon.FileAsset)
- [`maxon.StoreAssetStruct`](../../frameworks/asset/datatype/maxon.StoreAssetStruct.md#module-maxon.StoreAssetStruct)
- [`maxon.BasePresetAssetType`](../../frameworks/asset/reference/maxon.BasePresetAssetType.md#module-maxon.BasePresetAssetType)
- [`maxon.BasePresetAsset`](../../frameworks/asset/reference/maxon.BasePresetAsset.md#module-maxon.BasePresetAsset)
- [`maxon.ResolveAssetDependenciesStruct`](../../frameworks/asset/datatype/maxon.ResolveAssetDependenciesStruct.md#module-maxon.ResolveAssetDependenciesStruct)
- [`maxon.CategoryAsset`](../../frameworks/asset/reference/maxon.CategoryAsset.md#module-maxon.CategoryAsset)
- [`maxon.KeywordAsset`](../../frameworks/asset/reference/maxon.KeywordAsset.md#module-maxon.KeywordAsset)
- [`maxon.ColorCategoryAsset`](../../frameworks/asset/reference/maxon.ColorCategoryAsset.md#module-maxon.ColorCategoryAsset)
- [`maxon.DatabaseAsset`](../../frameworks/asset/reference/maxon.DatabaseAsset.md#module-maxon.DatabaseAsset)
- [`maxon.LazyLanguageStringDataDescriptionDefinition`](../../frameworks/asset/reference/maxon.LazyLanguageStringDataDescriptionDefinition.md#module-maxon.LazyLanguageStringDataDescriptionDefinition)
- [`maxon.LazyLanguageDictionary`](../../frameworks/asset/reference/maxon.LazyLanguageDictionary.md#module-maxon.LazyLanguageDictionary)
- [`maxon.NodeSpaceAsset`](../../frameworks/asset/reference/maxon.NodeSpaceAsset.md#module-maxon.NodeSpaceAsset)
- [`maxon.PluginAsset`](../../frameworks/asset/reference/maxon.PluginAsset.md#module-maxon.PluginAsset)
- [`maxon.SmartSearchAsset`](../../frameworks/asset/reference/maxon.SmartSearchAsset.md#module-maxon.SmartSearchAsset)
- [`maxon.SubTypeAsset`](../../frameworks/asset/reference/maxon.SubTypeAsset.md#module-maxon.SubTypeAsset)
- [`maxon.UrlAssetRepositoryRef`](../../frameworks/asset/reference/maxon.UrlAssetRepositoryRef.md#module-maxon.UrlAssetRepositoryRef)
- `maxon.Col4`
- [`maxon.Vec4`](../vec_col_mat/maxon.Vec4.md#module-maxon.Vec4)
- `maxon.RamDiskRef`
- [`maxon.GraphTransaction`](../../frameworks/graph/datatype/maxon.GraphTransaction.md#module-maxon.GraphTransaction)
- [`maxon.GraphModelRef`](../../frameworks/graph/reference/maxon.GraphModelRef.md#module-maxon.GraphModelRef)
- [`maxon.NodePath`](../../frameworks/graph/datatype/maxon.NodePath.md#module-maxon.NodePath)
- [`maxon.Wires`](../../frameworks/graph/datatype/maxon.Wires.md#module-maxon.Wires)
- [`maxon.GraphNode`](../../frameworks/graph/datatype/maxon.GraphNode.md#module-maxon.GraphNode)
- [`maxon.GraphAttribute`](../../frameworks/graph/reference/maxon.GraphAttribute.md#module-maxon.GraphAttribute)
- [`maxon.GraphMessage`](../../frameworks/graph/reference/maxon.GraphMessage.md#module-maxon.GraphMessage)
- [`maxon.NimbusBaseRef`](../../frameworks/nodespace/reference/maxon.NimbusBaseRef.md#module-maxon.NimbusBaseRef)
- [`maxon.NodesGraphModelRef`](../../frameworks/nodes/reference/maxon.NodesGraphModelRef.md#module-maxon.NodesGraphModelRef)
- [`maxon.CustomDataTagDisplayRef`](../../frameworks/mesh_misc/reference/maxon.CustomDataTagDisplayRef.md#module-maxon.CustomDataTagDisplayRef)
- [`maxon.CustomDataTagClass`](../../frameworks/mesh_misc/reference/maxon.CustomDataTagClass.md#module-maxon.CustomDataTagClass)
- [`maxon.MeshAttribute`](../../frameworks/mesh_misc/datatype/maxon.MeshAttribute.md#module-maxon.MeshAttribute)
- [`maxon.FilterRef`](../../frameworks/render_filter/reference/maxon.FilterRef.md#module-maxon.FilterRef)
- [`maxon.FilterCommandQueueRef`](../../frameworks/render_filter/reference/maxon.FilterCommandQueueRef.md#module-maxon.FilterCommandQueueRef)
- [`maxon.FilterContextRef`](../../frameworks/render_filter/reference/maxon.FilterContextRef.md#module-maxon.FilterContextRef)
- [`maxon.FilterImageRef`](../../frameworks/render_filter/reference/maxon.FilterImageRef.md#module-maxon.FilterImageRef)
- [`maxon.SqMat3`](../vec_col_mat/maxon.SqMat3.md#module-maxon.SqMat3)
- `maxon.Mat3`
- `maxon.ProgressRef`
- [`maxon.GridAccessorRef`](../../frameworks/volume/reference/maxon.GridAccessorRef.md#module-maxon.GridAccessorRef)
- [`maxon.SDFFilterSettings`](../../frameworks/volume/datatype/maxon.SDFFilterSettings.md#module-maxon.SDFFilterSettings)
- [`maxon.FilterSettings`](../../frameworks/volume/datatype/maxon.FilterSettings.md#module-maxon.FilterSettings)
- [`maxon.FieldSampleData`](../../frameworks/volume/datatype/maxon.FieldSampleData.md#module-maxon.FieldSampleData)
- [`maxon.VolumeConversionPolygon`](../../frameworks/volume/datatype/maxon.VolumeConversionPolygon.md#module-maxon.VolumeConversionPolygon)
- [`maxon.PointsToVolumeListRef`](../../frameworks/volume/reference/maxon.PointsToVolumeListRef.md#module-maxon.PointsToVolumeListRef)
- [`maxon.VolumeRef`](../../frameworks/volume/reference/maxon.VolumeRef.md#module-maxon.VolumeRef)

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Create`](#maxon.Data.Create)(cls, *args) | Creates a Data and initializes it with the given type. |
| [`GetHashCode`](#maxon.Data.GetHashCode)() | Returns the HashCode of the current *maxon.DataType*. |
| [`GetType`](#maxon.Data.GetType)() | Returns the [`maxon.DataType`](maxon.DataType.md#module-maxon.DataType) which is passed to register the class via the @dec.MAXON_XXX functionss |
| [`IsEmpty`](#maxon.Data.IsEmpty)() | Checks if a Data is empty. |
| [`IsNullValue`](#maxon.Data.IsNullValue)() | Checks if the data is a NullValue. |
| [`MaxonConvert`](#maxon.Data.MaxonConvert)([expected]) | Converts the data to the expected type (built-in). |
| [`ToString`](#maxon.Data.ToString)() | Returns a string representation of the content. |
| [`__copy__`](#maxon.Data.__copy__)() | Used by copy.copy. |
| [`__deepcopy__`](#maxon.Data.__deepcopy__)(memo) | Used by copy.deepcopy. |
| [`__eq__`](#maxon.Data.__eq__)(b) | Performs an equality comparison. |
| [`__ge__`](#maxon.Data.__ge__)(b) | Performs a greater or equal than comparison. |
| [`__gt__`](#maxon.Data.__gt__)(b) | Performs a greater than comparison. |
| [`__hash__`](#maxon.Data.__hash__)() | Returns the hash code of a data. |
| [`__init__`](#maxon.Data.__init__)([C]) | Initializes the appropriate C++ Data object and store it within the _data member. |
| [`__le__`](#maxon.Data.__le__)(b) | Performs a lesser or equal than comparison. |
| [`__lt__`](#maxon.Data.__lt__)(a) | Performs a lesser than comparison. |
| [`__maxon_convert__`](#maxon.Data.__maxon_convert__)([expected]) |  |
| [`__ne__`](#maxon.Data.__ne__)(b) | Performs an inequality comparison. |
| [`__repr__`](#maxon.Data.__repr__)() | Returns the string representation of a data. |
| [`__str__`](#maxon.Data.__str__)() | Returns the string representation of a data. |

## Methods Definition <a id="methods-definition"></a>

### *classmethod* `Data.Create(cls, *args)` <a id="maxon.Data.Create"></a>

Creates a Data and initializes it with the given type.

**Parameters:**

- **cls** ([`maxon.DataType`](maxon.DataType.md#module-maxon.DataType)) – The datatype to create.
- **args** (*Any*) – Optional argument to be passed to the creation.

**Returns:** [`maxon.Data`](#module-maxon.Data) initialized to the given type on success.

**Return type:** Any.

### `Data.GetHashCode()` <a id="maxon.Data.GetHashCode"></a>

Returns the HashCode of the current *maxon.DataType*.

**Returns:** The *maxon.DataType* hash code.

**Return type:** int

### `Data.GetType()` <a id="maxon.Data.GetType"></a>

Returns the [`maxon.DataType`](maxon.DataType.md#module-maxon.DataType) which is passed to register the class via the @dec.MAXON_XXX functionss E.g: net.maxon.datatype.int32  
If you want to know the real datatype, use maxon.Data.GetRealType.  
This can indeed differ e.g. for types when a tuple or basearray is used.  
In this case the array GetRealType() returns the underlying type including the template parameter

**Returns:** Return the DataType of the current [`maxon.Data`](#module-maxon.Data).

**Return type:** *maxon.DataType*

### `Data.IsEmpty()` <a id="maxon.Data.IsEmpty"></a>

Checks if a Data is empty.

**Returns:** **True** if it doesn’t contain any data otherwise **False**.

**Return type:** bool

### `Data.IsNullValue()` <a id="maxon.Data.IsNullValue"></a>

Checks if the data is a NullValue.

**Returns:** **True** if the represented Data is a NullValue otherwise **False**.

**Return type:** bool

### `Data.MaxonConvert(expected=None)` <a id="maxon.Data.MaxonConvert"></a>

Converts the data to the expected type (built-in).

**Parameters:** **expected** (*Any*) – The expected type after the conversion.

**Returns:** The data converted.

**Return type:** Same as expected

### `Data.ToString()` <a id="maxon.Data.ToString"></a>

Returns a string representation of the content.

**Returns:** The string representation of the content of the [`maxon.Data`](#module-maxon.Data).

**Return type:** *maxon.String*

### `Data.__copy__()` <a id="maxon.Data.__copy__"></a>

Used by copy.copy. May fail if the C++ Data does not implement a logic for copying itself.

### `Data.__deepcopy__(memo)` <a id="maxon.Data.__deepcopy__"></a>

Used by copy.deepcopy. May fail if the C++ Data does not implement a logic for copying itself.

### `Data.__eq__(b)` <a id="maxon.Data.__eq__"></a>

Performs an equality comparison. It may not work since not all data implement the Compare method.

**Parameters:** **b** ([`maxon.Data`](#module-maxon.Data)) – The other data to compare against

**Returns:** **True** if other is equal to the current value, otherwise **False**.

**Return type:** bool

### `Data.__ge__(b)` <a id="maxon.Data.__ge__"></a>

Performs a greater or equal than comparison. It may not work since not all data implement the Compare method.

**Parameters:** **b** ([`maxon.Data`](#module-maxon.Data)) – The other data to compare against.

**Returns:** **True** if other is greater or equal than current value, otherwise **False**.

**Return type:** bool

### `Data.__gt__(b)` <a id="maxon.Data.__gt__"></a>

Performs a greater than comparison. It may not work since not all data implement the Compare method.

**Parameters:** **b** ([`maxon.Data`](#module-maxon.Data)) – The other data to compare against.

**Returns:** **True** if other is greater than current value, otherwise **False**.

**Return type:** bool

### `Data.__hash__()` <a id="maxon.Data.__hash__"></a>

Returns the hash code of a data.

### `Data.__init__(C=None)` <a id="maxon.Data.__init__"></a>

Initializes the appropriate C++ Data object and store it within the _data member.

If C is a Data then _data store a copy the C++ Data is done and stored.  
If C is a C++ Data then _data store a reference of the C++ Data.  
If C is not defined the C++ data is created and stored in the _data member.

**Parameters:** **C** (Optional[[`maxon.Data`](#module-maxon.Data)]) – Input data from which the Data should be created.

### `Data.__le__(b)` <a id="maxon.Data.__le__"></a>

Performs a lesser or equal than comparison. It may not work since not all data implement the Compare method.

**Parameters:** **b** ([`maxon.Data`](#module-maxon.Data)) – The other data to compare against.

**Returns:** **True** if other is lesser or equal than current value, otherwise **False**.

**Return type:** bool

### `Data.__lt__(a)` <a id="maxon.Data.__lt__"></a>

Performs a lesser than comparison. It may not work since not all data implement the Compare method.

**Parameters:** **a** ([`maxon.Data`](#module-maxon.Data)) – The other data to compare against.

**Returns:** **True** if other is lesser than current value, otherwise **False**.

**Return type:** bool

### `Data.__maxon_convert__(expected=None)` <a id="maxon.Data.__maxon_convert__"></a>

### `Data.__ne__(b)` <a id="maxon.Data.__ne__"></a>

Performs an inequality comparison. It may not work since not all data implement the Compare method.

**Parameters:** **b** ([`maxon.Data`](#module-maxon.Data)) – The other data to compare against

**Returns:** **True** if other is unequal to the current value, otherwise **False**.

**Return type:** bool

### `Data.__repr__()` <a id="maxon.Data.__repr__"></a>

Returns the string representation of a data.

**Return type:** str

### `Data.__str__()` <a id="maxon.Data.__str__"></a>

Returns the string representation of a data.

**Return type:** str
