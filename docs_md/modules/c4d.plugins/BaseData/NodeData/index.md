<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseData/NodeData/index.html -->

# c4d.plugins.NodeData <a id="c4d-plugins-nodedata"></a>

## *class* `c4d.plugins.NodeData` <a id="c4d.plugins.NodeData"></a>

The base type for instantiable plugins.  
Use [`RegisterNodePlugin()`](../../index.md#c4d.plugins.RegisterNodePlugin) to register the plugin.

Parent Class:

- [`c4d.plugins.BaseData`](../index.md#c4d.plugins.BaseData)

Children Classes:

- [`c4d.plugins.ObjectData`](ObjectData/index.md#c4d.plugins.ObjectData)
- [`c4d.plugins.TagData`](TagData/index.md#c4d.plugins.TagData)
- [`c4d.plugins.ShaderData`](ShaderData/index.md#c4d.plugins.ShaderData)
- [`c4d.plugins.SceneSaverData`](SceneSaverData/index.md#c4d.plugins.SceneSaverData)
- [`c4d.plugins.SceneLoaderData`](SceneLoaderData/index.md#c4d.plugins.SceneLoaderData)
- [`c4d.plugins.PreferenceData`](PreferenceData/index.md#c4d.plugins.PreferenceData)

## Overview <a id="overview"></a>

**Description Parameters**

- [`NodeData.GetDDescription()`](#c4d.plugins.NodeData.GetDDescription): Called to add parameters to the description for the node.
- [`NodeData.GetDEnabling()`](#c4d.plugins.NodeData.GetDEnabling): Called to let decide which parameters should be enabled or disabled (ghosted).
- [`NodeData.GetDParameter()`](#c4d.plugins.NodeData.GetDParameter): Called to override the reading of description parameters.
- [`NodeData.SetDParameter()`](#c4d.plugins.NodeData.SetDParameter): Called to override the writing of parameters.
- [`NodeData.TranslateDescID()`](#c4d.plugins.NodeData.TranslateDescID): Called by the Attribute Manager for every object and every description ID.

**Lifecycle Management**

- [`NodeData.CopyTo()`](#c4d.plugins.NodeData.CopyTo): Override - Called when a node is duplicated.
- [`NodeData.Free()`](#c4d.plugins.NodeData.Free): Override - If your class has a destructor it is called as usual after this function.
- [`NodeData.Init()`](#c4d.plugins.NodeData.Init): Override - Called by Cinema 4D to let the node initialize its parameters and internal data.
- [`NodeData.InitAttr()`](#c4d.plugins.NodeData.InitAttr): Initializes a description parameter of the instance.

**Messaging And Help**

- [`NodeData.GetBubbleHelp()`](#c4d.plugins.NodeData.GetBubbleHelp): Called to create a contextual bubble help and status bar information for the node.
- [`NodeData.Message()`](#c4d.plugins.NodeData.Message): Override - Called when a node receives messages.

**Node Structure And Context**

- [`NodeData.Get()`](#c4d.plugins.NodeData.Get): Gets the GeListNode connected with the NodeData instance.
- [`NodeData.GetBranchInfo()`](#c4d.plugins.NodeData.GetBranchInfo): Override - Returns information about custom branches owned by *node*.
- [`NodeData.GetDocument()`](#c4d.plugins.NodeData.GetDocument): If you create your own BaseList elements this allows you to tell Cinema 4D how to retrieve the document.
- [`NodeData.IsDocumentRelated()`](#c4d.plugins.NodeData.IsDocumentRelated): Called by the Attribute Manager for correct undo handling.
- [`NodeData.IsInstanceOf()`](#c4d.plugins.NodeData.IsInstanceOf): Called to know if the *node* is an instance of the given base *type*.

**Persistence**

- [`NodeData.Read()`](#c4d.plugins.NodeData.Read): Override - Called when a node is loaded from a file.
- [`NodeData.Write()`](#c4d.plugins.NodeData.Write): Override - Called when a node is saved to a file.

## Members <a id="members"></a>

### Description Parameters <a id="c4d.plugins.NodeData-method-Description-Parameters"></a>

#### `NodeData.GetDDescription(self, node, description, flags)` <a id="c4d.plugins.NodeData.GetDDescription"></a>

Called to add parameters to the description for the node. Modify the passed description as needed and return the appropriate flags.

*New in version R18.011.*

> **Note:** If only a description resource is used it is not needed to overload `GetDDescription()`.

For instance, here is how [`GetDDescription()`](#c4d.plugins.NodeData.GetDDescription) can be implemented.

```python
def GetDDescription(self, node, description, flags):

    # Before adding dynamic parameters, load the parameters from the description resource
    if not description.LoadDescription(node.GetType()):
        return False

    # Get description single ID
    singleID = description.GetSingleDescID()

    # Check if dynamic parameter with ID paramID has to be added
    paramID = ...
    if singleID is None or paramID.IsPartOf(singleID)[0]:
        # Add dynamic parameter
        if not description.SetParameter(paramID, ...):
            return False

        ...

    # After parameters have been loaded and added successfully, return True and DESCFLAGS_DESC_LOADED with the input flags
    return (True, flags | c4d.DESCFLAGS_DESC_LOADED)
```

> **See also:** [`c4d.Description`](../../../c4d/Description/index.md#c4d.Description) and `DescID.IsPartOf()`

**Parameters:**

- **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.

- **description** ([*c4d.Description*](../../../c4d/Description/index.md#c4d.Description)) – The node’s description to add the parameters to.

- **flags** (*int*) –

  The flags for the description operation:

  |   |   |
  |---|---|
  | *DESCFLAGS_DESC_NONE* | None. |
  | *DESCFLAGS_DESC_RESOLVEMULTIPLEDATA* | Private and unused. |
  | *DESCFLAGS_DESC_LOADED* | Set if elements have been added to the description, either by loading or manual addition. |
  | *DESCFLAGS_DESC_RECURSIONLOCK* | Private. |
  | *DESCFLAGS_DESC_DONTLOADDEFAULT* | If set, the object description will also contain the tag’s descriptions (as sub-containers). |
  | *DESCFLAGS_DESC_MAPTAGS* | If specified, the object description will also contain the tag’s descriptions (as sub-containers). |
  | *DESCFLAGS_DESC_NEEDDEFAULTVALUE* | Set if *“Reset to Default”* was called by the user. |

**Return type:** Union[bool, Tuple[bool, int]]

**Returns:**

One of these options:

bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.  
Tuple[bool, int): The status (**True** if successful, otherwise **False**) and description flags (*DESCFLAGS_DESC*].

#### `NodeData.GetDEnabling(self, node, id, t_data, flags, itemdesc)` <a id="c4d.plugins.NodeData.GetDEnabling"></a>

Called to let decide which parameters should be enabled or disabled (ghosted).  
This can be used both for parameters that are stored in the node’s container and for custom parameters.  
Just read the passed *t_data* if the right *id* was provided, and return **True** to enable the parameter or **False** to disable it depending on the value.  
And if the passed *id* element is not processed, include a call to the base class method as last return.

```python
return NodeData.GetDEnabling(self, node, id, t_data, flags, itemdesc)
```

**Parameters:**

- **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.
- **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The ID of the parameter.
- **t_data** (*any*) – The current data for the parameter.
- **flags** (*int*) – Not used.
- **itemdesc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The description, encoded to a container as described in [`Description`](../../../c4d/Description/index.md#c4d.Description).

**Return type:** bool

**Returns:**

**True** if the parameter should be enabled, otherwise **False**.

> **Note:** It is recommended to include a call to the base class method as last return.

#### `NodeData.GetDParameter(self, node, id, flags)` <a id="c4d.plugins.NodeData.GetDParameter"></a>

Called to override the reading of description parameters. Necessary for parameters that are not simply stored in the node’s container e.g. class members.  
Return the parameter data and the appropriate flags if the right *id* is provided.

*New in version R18.011.*

> **Note:** If only a description resource is used it is not needed to overload `GetDParameter()`.

**Parameters:**

- **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.

- **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The ID of the parameter.

- **flags** (*int*) –

  The flags for the description operation:

  |   |   |
  |---|---|
  | *DESCFLAGS_GET_NONE* | None. |
  | *DESCFLAGS_GET_PARAM_GET* | Parameter retrieved. |
  | *DESCFLAGS_GET_NO_GEDATADEFAULTVALUE* | If set, the C++ *GeData* default type will not be initialized for `C4DAtom.GetParameter()`. |
  | *DESCFLAGS_GET_NO_GLOBALDATA* | Private. |

**Return type:** Union[bool, Tuple[bool, int]]

**Returns:**

One of these options:

bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.  
Tuple[bool, any, int): The status (**True** if successful, otherwise **False**), parameter data and description flags (*DESCFLAGS_DESC*].

#### `NodeData.SetDParameter(self, node, id, t_data, flags)` <a id="c4d.plugins.NodeData.SetDParameter"></a>

Called to override the writing of parameters.  
Read the passed *t_data* if the right *id* is provided, store the data and return the appropriate flags.

*New in version R18.011.*

> **Note:** If only a description resource is used it is not needed to overload `SetDParameter()`.

**Parameters:**

- **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.

- **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The ID of the parameter.

- **t_data** (*any*) – The parameter data to set.

- **flags** (*int*) –

  The flags for the description operation:

  |   |   |
  |---|---|
  | *DESCFLAGS_SET_NONE* | None. |
  | *DESCFLAGS_SET_PARAM_SET* | Parameter set. |
  | *DESCFLAGS_SET_USERINTERACTION* | Set when the GUI is calling `SetParameter()`. This is the only time when `SetParameter()` is allowed to use user interaction elements (e.g. open dialogs, display messages etc.). |
  | *DESCFLAGS_SET_DONTCHECKMINMAX* | No check is internally done if the parameter passed is within the [min/max] range of the description, to save some time. |
  | *DESCFLAGS_SET_DONTAFFECTINHERITANCE* | No parameter inheritance, for render settings and post effects only. |
  | *DESCFLAGS_SET_FORCESET* | Forces the set value without `GetParameter()`/Compare. Use only for calls where for sure the value was changed! |
  | *DESCFLAGS_SET_DONTFREESPLINECACHE* | **Private.** *New in version R16.038.* |
  | *DESCFLAGS_SET_INDRAG* | **Gadget (e.g. Slider) in dragging mode (not finished). Only used when *DESCFLAGS_SET_USERINTERACTION* is set.** *New in version R17.053.* |

**Return type:** Union[bool, Tuple[bool, int]]

**Returns:**

One of these options:

bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.  
Tuple[bool, int]: The status (**True** if successful, otherwise **False**) and description flags (*DESCFLAGS_DESC*].

#### `NodeData.TranslateDescID(self, node, id)` <a id="c4d.plugins.NodeData.TranslateDescID"></a>

Called by the Attribute Manager for every object and every description ID.  
Gives a *NodeData* plugin the opportunity to route a description ID in the description of a node to another one.  
For example used for tags that are embedded in an object description so that the keyframer for a tag property creates the track on the tag and not on the object.

*New in version R18.011.*

**Parameters:**

- **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.
- **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The source description ID.

**Return type:** Union[bool, Tuple[bool, [c4d.DescID](../../../c4d/DescID/index.md#c4d.DescID), [c4d.C4DAtom](../../../c4d/C4DAtom/index.md#c4d.C4DAtom)]]

**Returns:**

One of these options:

bool: **True** if successful, otherwise **False**. Useful in error state to only return **False**.  
Tuple[bool, c4d.DescID, c4d.C4DAtom]: The status (**True** if successful, otherwise **False**), target description ID and object.

### Lifecycle Management <a id="c4d.plugins.NodeData-method-Lifecycle-Management"></a>

#### `NodeData.CopyTo(self, dest, snode, dnode, flags, trn)` <a id="c4d.plugins.NodeData.CopyTo"></a>

Override - Called when a node is duplicated. [`Init()`](#c4d.plugins.NodeData.Init) is called for the destination node before this function.  
Use this function to copy any settings for the plugin that are not stored in the [`BaseContainer`](../../../c4d/BaseContainer/index.md#c4d.BaseContainer).  
Simply transfer them from the current node data to *dest* and/or *snode* to *dnode*:

```python
dest.offset = offset
dest.object_access = object_access
```

> **Note:**
>
> It is recommended to store as much as possible in the [`BaseContainer`](../../../c4d/BaseContainer/index.md#c4d.BaseContainer) as Cinema 4D will handle the copying of those values automatically.  
> Only use member variables when necessary.

> **Important:** If at least one of [`Read()`](#c4d.plugins.NodeData.Read), [`Write()`](#c4d.plugins.NodeData.Write) and [`CopyTo()`](#c4d.plugins.NodeData.CopyTo) is implemented, it is recommended to implement all three, otherwise data might be lost.

**Parameters:**

- **dest** ([*c4d.plugins.NodeData*](#c4d.plugins.NodeData)) – The destination node data.

- **snode** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The source node data, i.e. the current node.

- **dnode** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The destination node data.

- **flags** (*int*) –

  The copy flags:

  | Key | Description |
  |---|---|
  | COPYFLAGS_NONE | None. |
  | COPYFLAGS_NO_HIERARCHY | Copy without children. |
  | COPYFLAGS_NO_ANIMATION | Copy without tracks, sequences or keys. |
  | COPYFLAGS_NO_BITS | Do not copy [`BaseList2D`](../../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D) bits. |
  | COPYFLAGS_NO_MATERIALPREVIEW | Do not create a new material preview. |
  | COPYFLAGS_NO_BRANCHES | Do not copy branches, for example tags on an object. Automatically implies *COPYFLAGS_NO_ANIMATION*, as animation is a branch. |
  | COPYFLAGS_DOCUMENT | Read-only flag set when a complete document is copied. |
  | COPYFLAGS_NO_NGONS | Do not copy N-gons. |
  | COPYFLAGS_CACHE_BUILD | Read-only flag set when cache is built. |
  | COPYFLAGS_RECURSIONCHECK | Checks and avoids instances to cause recursions. |
  | COPYFLAGS_PRIVATE_IDENTMARKER | Private. |
  | COPYFLAGS_PRIVATE_NO_INTERNALS | Private. |
  | COPYFLAGS_PRIVATE_NO_PLUGINLAYER | Private. |
  | COPYFLAGS_PRIVATE_UNDO | Private. |
  | COPYFLAGS_PRIVATE_NO_TAGS | Private. |
  | COPYFLAGS_PRIVATE_DELETE | Private. |
  | COPYFLAGS_PRIVATE_NO_ASSETS | Private. |
  | COPYFLAGS_PRIVATE_NO_RESULTASSETS | Private. |
  | COPYFLAGS_PRIVATE_NO_LOGS | Private. |
  | COPYFLAGS_PRIVATE_BODYPAINT_NODATA | Private. |
  | COPYFLAGS_PRIVATE_BODYPAINT_CONVERTLAYER | Private. |
  | COPYFLAGS_PRIVATE_BODYPAINT_CONVERTLAYER | Private. |
  | COPYFLAGS_PRIVATE_NO_DESCRIPTION | *New in version 2024.5:* Private |

- **trn** ([*c4d.AliasTrans*](../../../c4d/AliasTrans/index.md#c4d.AliasTrans)) –

  *Changed in version R17.032.*

  An alias translator for the operation.

**Return type:** bool

**Returns:** **True** if the data was copied successfully, otherwise **False**.

#### `NodeData.Free(self, node)` <a id="c4d.plugins.NodeData.Free"></a>

Override - If your class has a destructor it is called as usual after this function.

**Parameters:** **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.

#### `NodeData.Init(self, node, isCloneInit)` <a id="c4d.plugins.NodeData.Init"></a>

Override - Called by Cinema 4D to let the node initialize its parameters and internal data.  
This function is called more often than one might expect, as Cinema 4D reinitializes nodes. For heavy pre-calculations, the message *c4d.MSG_MENUPREPARE* is the better choice, as it will only run once. You then also have to override *NodeData.CopyTo()* to copy over internal data in a copy event. When your class has a constructor, it is called before this function, but at that time there’s no node link established.

> **Warning:** If *False* is being returned, the object will not be created.

```python
def Init(self, node: c4d.BaseObject, isCloneInit: bool = False) -> bool:
    '''Called by Cinema 4D to let the node initialize its parameters and internal data.
    '''
    # Abort the node creation by returning False when #node or the data instance is None and
    # just exit the node initialization when this is a cloning event, in this case Cinema 4D
    # will copy the data from the original node.
    if not node or node.GetDataInstance() is None:
        return False
    
    if isCloneInit:
        return True

    # Initialize the parameters of the node.
    self.InitAttr(node, float, c4d.ID_MY_FLOAT_PARAMETER)
    self.InitAttr(node, int, c4d.ID_MY_INT_PARAMETER)
    self.InitAttr(node, c4d.BaseList2D, c4d.ID_MY_BASELISTLINK_PARAMETER)
    self.InitAttr(node, c4d.BaseTime, c4d.ID_MY_TIME_PARAMETER)
    self.InitAttr(node, c4d.Vector, c4d.ID_MY_VECTOR_PARAMETER)

    node[c4d.ID_MY_FLOAT_PARAMETER] = 200.0
    node[c4d.ID_MY_INT_PARAMETER] = 5
    node[c4d.ID_MY_BASELISTLINK_PARAMETER] = None
    node[c4d.ID_MY_TIME_PARAMETER] = c4d.BaseTime(2.)
    node[c4d.ID_MY_VECTOR_PARAMETER] = c4d.Vector(1, 0, 0)

    return True
```

**Parameters:**

- **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.

- **isCloneInit** (*bool*) –

  *New in version 2024.0.0.*

  True if the object data is a copy of another one.

**Return type:** bool

**Returns:** **True** on success, otherwise **False**.

#### `NodeData.InitAttr(self, host, type, id)` <a id="c4d.plugins.NodeData.InitAttr"></a>

Initializes a description parameter of the instance.  
This method has to be called for each parameter of a [`c4d.plugins.NodeData`](#c4d.plugins.NodeData) implementation in order to make the parameter usable. The data type with which a parameter has to be initialized depends on the `DTYPE` of the parameter definition in the resource definition of the plugin. The parameter initialization is usually done in [`c4d.plugins.NodeData.Init()`](#c4d.plugins.NodeData.Init).

```python
def Init(self, node: c4d.BaseObject, isCloneInit: bool = False) -> bool:
    '''Called by Cinema 4D to let the node initialize its parameters and internal data.
    '''
    # Abort the node creation by returning False when #node or the data instance is None and
    # just exit the node initialization when this is a cloning event, in this case Cinema 4D
    # will copy the data from the original node.
    if not node or node.GetDataInstance() is None:
        return False
    
    if isCloneInit:
        return True

    # Initialize the parameters of the node.
    self.InitAttr(node, float, c4d.ID_MY_FLOAT_PARAMETER)
    self.InitAttr(node, int, c4d.ID_MY_INT_PARAMETER)
    self.InitAttr(node, c4d.BaseList2D, c4d.ID_MY_BASELISTLINK_PARAMETER)
    self.InitAttr(node, c4d.BaseTime, c4d.ID_MY_TIME_PARAMETER)
    self.InitAttr(node, c4d.Vector, c4d.ID_MY_VECTOR_PARAMETER)

    node[c4d.ID_MY_FLOAT_PARAMETER] = 200.0
    node[c4d.ID_MY_INT_PARAMETER] = 5
    node[c4d.ID_MY_BASELISTLINK_PARAMETER] = None
    node[c4d.ID_MY_TIME_PARAMETER] = c4d.BaseTime(2.)
    node[c4d.ID_MY_VECTOR_PARAMETER] = c4d.Vector(1, 0, 0)

    return True
```

**Parameters:**

- **host** ([*c4d.BaseObject*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The host object.
- **type** (*any*) – Just pass the type like *float*, *int*, [`PriorityData`](../../../c4d/CustomDataType/PriorityData/index.md#c4d.PriorityData), etc.
- **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The parameter description ID to initialize.

**Return type:** bool

**Returns:** **True** if the parameter could be successfully initialized, otherwise **False**.

### Messaging And Help <a id="c4d.plugins.NodeData-method-Messaging-And-Help"></a>

#### `NodeData.GetBubbleHelp(self, node)` <a id="c4d.plugins.NodeData.GetBubbleHelp"></a>

Called to create a contextual bubble help and status bar information for the node.

*New in version R18.011.*

> **Note:**
>
> When dealing with strings it is advised to use the string resources files and the [`GeLoadString()`](../../index.md#c4d.plugins.GeLoadString) function.  
> This keeps the plugin easy to localize for any language to support and makes full use of the language features of Cinema 4D.

**Parameters:** **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.

**Return type:** str

**Returns:** The bubble help string.

#### `NodeData.Message(self, node, type, data)` <a id="c4d.plugins.NodeData.Message"></a>

Override - Called when a node receives messages.

> **See also:** [C4DAtom and Plugin Messages](../../../../consts/MSG_C4DATOM_PLUGINS.md) for information on the messages type, data and input/output.

<a id="msg-description-command-example"></a>

> **Note:** The following code shows how to handle *MSG_DESCRIPTION_COMMAND* sent by a button in a description:
>
> ```python
> def Message(self, node, type, data):
>     if type==c4d.MSG_DESCRIPTION_COMMAND:
>         if data['id'][0].id==THE_BUTTON_ID:
>             print(f"Pushed button with the ID {THE_BUTTON_ID}")
>             return True
>
>     return True
> ```

**Parameters:**

- **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.
- **type** (*int*) – The message type.
- **data** (*any*) – The message data.

**Return type:** bool

**Returns:** Depends on the message *type*.

### Node Structure And Context <a id="c4d.plugins.NodeData-method-Node-Structure-And-Context"></a>

#### `NodeData.Get(self)` <a id="c4d.plugins.NodeData.Get"></a>

Gets the GeListNode connected with the NodeData instance.

*New in version 2023.2.0.*

**Returns:** The list node connected with this instance

**Return type:** [`c4d.GeListNode`](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)

#### `NodeData.GetBranchInfo(self, node, flags=0)` <a id="c4d.plugins.NodeData.GetBranchInfo"></a>

Override - Returns information about custom branches owned by *node*.  
The returned value must be a list of dictionaries. Each dictionary must contain `head`  
(a [`c4d.GeListHead`](../../../c4d/C4DAtom/GeListNode/GeListHead/index.md#c4d.GeListHead) or [`c4d.GeListNode`](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)), `name` (`str`), `id`  
(`int`), and `flags` (`int`).  
Use `c4d.GETBRANCHINFO_ONLYWITHCHILDREN` to omit branches whose heads are empty.  
The branch head remains owned by the `NodeData` instance and must stay alive while  
the node can be queried.  
This callback uses the same dictionary representation as  
[`c4d.GeListNode.GetBranchInfo()`](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode.GetBranchInfo).

*New in version 2027.0.0.*

**Parameters:**

- **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.
- **flags** (*int*) – The `c4d.GETBRANCHINFO` query flags.

**Return type:** List[Dict[str, Union[[c4d.GeListHead](../../../c4d/C4DAtom/GeListNode/GeListHead/index.md#c4d.GeListHead), [c4d.GeListNode](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode), str, int]]]

**Returns:** The custom branch descriptions, or an empty list when there are none.

#### `NodeData.GetDocument(self, node)` <a id="c4d.plugins.NodeData.GetDocument"></a>

If you create your own BaseList elements this allows you to tell Cinema 4D how to retrieve the document.  
Any call to `GeListNode.GetDocument()` ends up here.

> **Note:**
>
> Standard nodes like objects, tags etc. do not need to override this function.  
> Only if you create elements that are allocated with AllocListNode(), AllocSmallListNode() and AllocMultiNode() do need this function.

**Parameters:** **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.

**Return type:** [c4d.documents.BaseDocument](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)

**Returns:** The document.

#### `NodeData.IsDocumentRelated(self, node)` <a id="c4d.plugins.NodeData.IsDocumentRelated"></a>

Called by the Attribute Manager for correct undo handling.

*New in version R18.011.*

> **Warning:**
>
> Should not be overloaded by regular plugins and should be used with extra care.  
> If **False** is returned no undo is possible.

**Parameters:** **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.

**Return type:** bool

**Returns:** **True** if the node is part of the document, otherwise **False**.

#### `NodeData.IsInstanceOf(self, node, type)` <a id="c4d.plugins.NodeData.IsInstanceOf"></a>

Called to know if the *node* is an instance of the given base *type*.

**Parameters:**

- **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.
- **type** (*int*) – The type to check.

**Return type:** bool

**Returns:** **True** if the *node* is an instance of the given *type*, otherwise **False**.

### Persistence <a id="c4d.plugins.NodeData-method-Persistence"></a>

#### `NodeData.Read(self, node, hf, level)` <a id="c4d.plugins.NodeData.Read"></a>

Override - Called when a node is loaded from a file.  
Use this function to read any settings for your plugin that are not stored in the [`BaseContainer`](../../../c4d/BaseContainer/index.md#c4d.BaseContainer).  
You must read these settings from the [`HyperFile`](../../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile) such as.

```python
hf.ReadInt32(offset)
hf.ReadBool(object_access)
```

For future extensions of your plugin you should check the *level* and only read the appropriate values.

```python
if level >= 0:
    hf.ReadInt32(offset)
    hf.ReadBool(object_access)
if level >= 1:
    hf->ReadFloat(a_new_feature)
```

[`Init()`](#c4d.plugins.NodeData.Init) will have already been called before this function is called.

> **Note:**
>
> It is recommended to store as much as possible in the [`BaseContainer`](../../../c4d/BaseContainer/index.md#c4d.BaseContainer) as Cinema 4D will handle the reading of those values automatically.  
> Only use member variables when necessary.

> **Important:**
>
> If you implement at least one of [`Read()`](#c4d.plugins.NodeData.Read), [`Write()`](#c4d.plugins.NodeData.Write) and [`CopyTo()`](#c4d.plugins.NodeData.CopyTo), you must usually implement all three.  
> Otherwise data might be lost.

**Parameters:**

- **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.

- **hf** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The hyper file to read the data from.

- **level** (*int*) –

  The plugin level is similar to a version number for your settings.  
  The default level is 0, you can then increase this for new revisions of your plugin, this allows for forward and backward compatibility.

  As an example you may have updated your plugin, if you now need to write additional information for new settings or changed types for old settings you can increase the level. During loading either a 0 is passed (if the file was written using your old plugin) or 1 (if the file was written by the new plugin). This allows you to easily save/read new values.

  > **Important:** For forward and backward compatibility to work you must not change any existing read order from a given level, Cinema 4D will skip any new settings automatically if they have not been read for your plugin.

  > **Note:** If you only use containers for all your values, you do not have to deal with *level*.

**Return type:** bool

**Returns:** **True** if the data was read successfully, otherwise **False**.

#### `NodeData.Write(self, node, hf)` <a id="c4d.plugins.NodeData.Write"></a>

Override - Called when a node is saved to a file.  
Use this function to write any settings for your plugin that are not stored in the [`BaseContainer`](../../../c4d/BaseContainer/index.md#c4d.BaseContainer).  
You must read these settings from the [`HyperFile`](../../../c4d.storage/HyperFile/index.md#c4d.storage.HyperFile) such as.

```python
hf.WriteInt32(offset)
hf.WriteBool(object_access)
```

For future extensions of your plugin you should make sure to introduce a new level (See [`Read()`](#c4d.plugins.NodeData.Read)) when writing new values.

```python
// Level 0
hf.WriteInt32(offset)
hf.WriteBool(object_access)

// Level 1
hf.WriteFloat(a_new_feature)
```

[`Free()`](#c4d.plugins.NodeData.Free) will be called after this function is called.

> **Note:**
>
> It is recommended to store as much as possible in the [`BaseContainer`](../../../c4d/BaseContainer/index.md#c4d.BaseContainer) as Cinema 4D will handle the writing of those values automatically.  
> Only use member variables when necessary.

> **Important:**
>
> If you implement at least one of [`Read()`](#c4d.plugins.NodeData.Read), [`Write()`](#c4d.plugins.NodeData.Write) and [`CopyTo()`](#c4d.plugins.NodeData.CopyTo), you must usually implement all three.  
> Otherwise data might be lost.

**Parameters:**

- **node** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The list node connected with this instance.
- **hf** ([*c4d.GeListNode*](../../../c4d/C4DAtom/GeListNode/index.md#c4d.GeListNode)) – The hyper file to write the data to.

**Return type:** bool

**Returns:** **True** if the data was written successfully, otherwise **False**.
