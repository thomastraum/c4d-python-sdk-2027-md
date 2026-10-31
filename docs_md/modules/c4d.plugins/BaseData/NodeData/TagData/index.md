<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseData/NodeData/TagData/index.html -->

# c4d.plugins.TagData <a id="c4d-plugins-tagdata"></a>

## *class* `c4d.plugins.TagData` <a id="c4d.plugins.TagData"></a>

A data class for tag plugins.  
Use [`RegisterTagPlugin()`](../../../index.md#c4d.plugins.RegisterTagPlugin) to register the plugin.  
Registered tag plugins appear in the New Tag menu and can be attached to objects.

Parent Class:

- [`c4d.plugins.NodeData`](../index.md#c4d.plugins.NodeData)

## Overview <a id="overview"></a>

- [`TagData.AddToExecution()`](#c4d.plugins.TagData.AddToExecution): Override - By default this function returns **False**.
- [`TagData.Draw()`](#c4d.plugins.TagData.Draw): Override - Called when the display is updated for you to display some visual element of your tag in the 3D view.
- [`TagData.Execute()`](#c4d.plugins.TagData.Execute): Override - Called at the point when the tag is executed.

## Members <a id="members"></a>

### Display And Execution <a id="c4d.plugins.TagData-method-Display-And-Execution"></a>

#### `TagData.AddToExecution(self, tag, list)` <a id="c4d.plugins.TagData.AddToExecution"></a>

Override - By default this function returns **False**.  
Then Cinema 4D will call [`Execute()`](#c4d.plugins.TagData.Execute) at the priority specified by the user in the *EXPRESSION_PRIORITY* parameter of the container.

If you override this function and return **True**, then you can insert your own points of execution in the list by calling for example.

```python
list.Add(tag, EXECUTIONPRIORITY_ANIMATION, 0)
list.Add(tag, EXECUTIONPRIORITY_GENERATOR, 0)
```

Cinema 4D will then call [`Execute()`](#c4d.plugins.TagData.Execute) two times.

**Parameters:**

- **tag** ([*c4d.BaseTag*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)) – The established [`BaseTag`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag).
- **list** ([*c4d.plugins.PriorityList*](../../../PriorityList/index.md#c4d.plugins.PriorityList)) – The priority list to add your tag’s execution points to.

**Return type:** bool

**Returns:** **True** if you override this function and have added stuff to list.

#### `TagData.Draw(self, tag, op, bd, bh)` <a id="c4d.plugins.TagData.Draw"></a>

Override - Called when the display is updated for you to display some visual element of your tag in the 3D view.

> **Note:**
>
> This function is called in a thread context.  
> Please see the [important information](../../../../../manuals/manual_scene_execution.md#threading-information) about threading.

**Parameters:**

- **tag** ([*c4d.BaseTag*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)) – The object which is established with this instance.
- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The host object of the tag.
- **bd** ([*c4d.BaseDraw*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The editor’s view.
- **bh** ([*c4d.plugins.BaseDrawHelp*](../../../BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp)) – An helper class.

**Return type:** bool

**Returns:** Success of drawing into the editor view.

#### `TagData.Execute(self, tag, doc, op, bt, priority, flags)` <a id="c4d.plugins.TagData.Execute"></a>

Override - Called at the point when the tag is executed.

> **Note:**
>
> This function is called in a thread context.  
> Please see the [important information](../../../../../manuals/manual_scene_execution.md#threading-information) about threading.

**Parameters:**

- **tag** ([*c4d.BaseTag*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)) – The established [`BaseTag`](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag).

- **doc** ([*c4d.documents.BaseDocument*](../../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The host document of the tag’s object.

- **op** ([*c4d.BaseObject*](../../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The host object of the tag.

- **bt** ([*c4d.threading.BaseThread*](../../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)) – The calling thread.

- **priority** (*int*) –

  One of the following flags:

  |   |   |
  |---|---|
  | *EXECUTIONPRIORITY_INITIAL* | Initial. |
  | *EXECUTIONPRIORITY_ANIMATION* | Animation. |
  | *EXECUTIONPRIORITY_ANIMATION_NLA* | NLA. |
  | *EXECUTIONPRIORITY_EXPRESSION* | Expression. |
  | *EXECUTIONPRIORITY_DYNAMICS* | Dynamics. |
  | *EXECUTIONPRIORITY_GENERATOR* | Generators. |
  | *EXECUTIONPRIORITY_SCENENODE* | Scene nodes. |
  | *EXECUTIONPRIORITY_FORCE* | Highest priority that will ensure execution even if the execution pipeline is cancelled before. Only use this to e.g. release locks or do super-fast non-blocking operations. |

- **flags** (*int*) –

  A combination of the following flags:

  |   |   |
  |---|---|
  | *EXECUTIONFLAGS_NONE* | None. |
  | *EXECUTIONFLAGS_ANIMATION* | Animation is calculated. |
  | *EXECUTIONFLAGS_EXPRESSION* | Expressions are calculated. |
  | *EXECUTIONFLAGS_CACHEBUILDING* | Cache building is done. |
  | *EXECUTIONFLAGS_CAMERAONLY* | Only camera dependent expressions shall be executed. |
  | *EXECUTIONFLAGS_INDRAG* | Pipeline is done within scrubbing. |
  | *EXECUTIONFLAGS_INMOVE* | Pipeline is done within moving. |
  | *EXECUTIONFLAGS_RENDER* | The external renderer (Picture Viewer) is running. |
  | *EXECUTIONFLAGS_ALLOW_PRIORITYSHIFT* | *New in version R18:* Allow to shift the priority with the priority shift tag. Private. |

**Return type:** int

**Returns:**

One of the following results:

|   |   |
|---|---|
| *EXECUTIONRESULT_OK* | OK. |
| *EXECUTIONRESULT_USERBREAK* | User break. |
| *EXECUTIONRESULT_MEMORYERROR* | Not enough memory. |
