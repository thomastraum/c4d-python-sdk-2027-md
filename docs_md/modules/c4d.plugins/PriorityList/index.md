<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/PriorityList/index.html -->

# c4d.plugins.PriorityList <a id="c4d-plugins-prioritylist"></a>

## *class* `c4d.plugins.PriorityList` <a id="c4d.plugins.PriorityList"></a>

Stores execution priorities.

## Overview <a id="overview"></a>

- [`PriorityList.Add()`](#c4d.plugins.PriorityList.Add): Adds an execution point for *node* and the time specified by *priority*.

## Members <a id="members"></a>

### Execution Scheduling <a id="c4d.plugins.PriorityList-method-Execution-Scheduling"></a>

#### `PriorityList.Add(self, node, priority, flags)` <a id="c4d.plugins.PriorityList.Add"></a>

Adds an execution point for *node* and the time specified by *priority*.

**Parameters:**

- **node** ([*c4d.BaseList2D*](../../c4d/C4DAtom/GeListNode/BaseList2D/index.md#c4d.BaseList2D)) – The node to execute.

- **priority** (*int*) –

  The priority in the pipeline. Standard values are:

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

  Flags:

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
