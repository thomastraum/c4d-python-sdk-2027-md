<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_scripting_elements.html -->

# Scripting Elements <a id="scripting-elements"></a><a id="manual-python-scripting-elements"></a>

Explains Python scripting elements embedded in Cinema 4D scenes.

Scripting elements are scene elements such as object, tags, or materials in Cinema 4D that have Python script parameters which control the whole element or aspects of it. Many scripting elements are either miniature versions of full plugins, the Python Generator object is for example a miniature version of a [`c4d.plugins.ObjectData`](../modules/c4d.plugins/BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData) plugin, or stand for plugin types that have never been ported to the Python API, such as the Python Effector and Python Field.

> **Warning:** Because many scripting elements are derived from [`c4d.plugins.NodeData`](../modules/c4d.plugins/BaseData/NodeData/index.md#c4d.plugins.NodeData), they inherit its threading restrictions. See [Threading Restrictions](manual_scene_execution.md#threading-information) for more details.

## Python Generator Object <a id="python-generator-object"></a>

A Python Generator Object is an object that dynamically creates a generator output based on a Python script. It is a miniature version of a [`c4d.plugins.ObjectData`](../modules/c4d.plugins/BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData) plugin. The generator has a *Optimize Cache* parameter that acts just like the method [`c4d.plugins.ObjectData.SetOptimizeCache()`](../modules/c4d.plugins/BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData.SetOptimizeCache) and causes the *main* function only to be called when any of the parameters of the generator changed. Disabling it will rebuild the generator on each scene update which can be quite expensive and when not paired with a manual dirtiness check.

> **Warning:** The *main* function of a Python Generator is subject to threading restrictions, i.e., you cannot modify a loaded document from there or perform GUI operations. See [Threading Restrictions](manual_scene_execution.md#threading-information) for more details.

### Attributes <a id="attributes"></a>

These are module level attributes which are injected by Cinema 4D into the Python Generator’s module. `hh` is only available while `main()` is being evaluated.

| Name | Datatype | Description |
|---|---|---|
| `doc` | `c4d.documents.BaseDocument` | The active document. |
| `hh` | `c4d.plugins.HierarchyHelp` | The hierarchy helper used to process child objects of the generator. Available only while `main()` is evaluated. |
| `op` | `c4d.BaseObject` | The Python Generator object itself. |

### Methods <a id="methods"></a>

#### `main() → c4d.BaseObject`

Override to generate and return the object output for the generator.

Equivalent to the [`c4d.plugins.ObjectData.GetVirtualObjects()`](../modules/c4d.plugins/BaseData/NodeData/ObjectData/index.md#c4d.plugins.ObjectData.GetVirtualObjects) method. You can return a single [`c4d.PolygonObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/PolygonObject/index.md#c4d.PolygonObject) or a whole hierarchy of objects under a null objects. You can also return splines, and in many cases this will work, but this formally not a spline generator, and some other components of Cinema 4D therefore might fail to recognize your generator as a spline.

**Returns:** The new cache of the generator (i.e., what the user sees as its geometry).

**Return type:** [c4d.BaseObject](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)

#### `message(mid: int, data: dict | object) → bool | None`

Override to handle messages sent to the Python Generator.

Equivalent to the [`c4d.plugins.NodeData.Message()`](../modules/c4d.plugins/BaseData/NodeData/index.md#c4d.plugins.NodeData.Message) method. This can be used to react to modify to button clicks, modify the UI of the generator, and many other things that are possible with messages. Messages are also the *only* context in a generator where you are not always bound by threading restrictions. Messages often run on the main thread, but you must check with [`c4d.threading.GeIsMainThread()`](../modules/c4d.threading/index.md#c4d.threading.GeIsMainThread) to be sure.

> **Warning:** Do not consume messages unless you have to, i.e., the default should be to return *None*. Consuming messages that you do not handle yourself can break the functionality of the node, as data is then now longer reaching its consumer higher up the call chain.

**Parameters:**

- **mid** (*int*) – The message ID.
- **data** (*dict | object*) – The message data, usually a *dict*.

**Returns:** *True* or *False* if you either successfully or unsuccessfully consumed the message, or *None* if not consumed.

**Return type:** bool | None

## Python Programming Tag <a id="python-programming-tag"></a>

A Python Programming Tag executes the Python code stored in its script parameter when the tag is being executed. The tag acts as a miniature version of a [`c4d.plugins.TagData`](../modules/c4d.plugins/BaseData/NodeData/TagData/index.md#c4d.plugins.TagData) plugin.

> **Warning:** The *main* and *draw* functions of a Python Programming Tag are subject to threading restrictions. See [Threading Restrictions](manual_scene_execution.md#threading-information) for more details.

### Attributes <a id="id1"></a>

These module-level attributes are injected into the Python Programming Tag’s script scope.

| Name | Datatype | Description |
|---|---|---|
| `doc` | `c4d.documents.BaseDocument` | The document containing the tag. |
| `op` | `c4d.BaseTag` | The Python Programming Tag. |
| `flags` | `int` | The execution flags passed to `main()`. See [EXECUTIONFLAGS](../consts/EXECUTIONFLAGS.md). |
| `priority` | `int` | The execution priority of the tag. See [EXECUTIONPRIORITY](../consts/EXECUTIONPRIORITY.md). |
| `tp` | `c4d.modules.thinkingparticles.TP_MasterSystem \| None` | The document’s Thinking Particles master system, or `None`. |

### Methods <a id="id2"></a>

#### `main() → None`

Override to execute the tag. It corresponds to [`c4d.plugins.TagData.Execute()`](../modules/c4d.plugins/BaseData/NodeData/TagData/index.md#c4d.plugins.TagData.Execute) and may be called multiple times per frame.

#### `message(mid: int, data: object) → bool | None`

Override to handle messages sent to the tag. Return `None` unless the script explicitly consumes the message.

**Parameters:**

- **mid** (*int*) – The message ID.
- **data** (*object*) – The message data.

**Return type:** bool | None

#### `draw(bd: c4d.BaseDraw) → None`

Override to draw visual elements in the viewport. It corresponds to [`c4d.plugins.TagData.Draw()`](../modules/c4d.plugins/BaseData/NodeData/TagData/index.md#c4d.plugins.TagData.Draw).

**Parameters:** **bd** ([*c4d.BaseDraw*](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The editor view.

## Python Effector <a id="python-effector"></a>

A Python Effector controls MoGraph data. Its `main()` callback is called in full-control mode. The scope provides `doc`, `op` (the effector), and `gen` (the MoGraph generator).

> **Warning:** The *main* function of a Python Effector is subject to threading restrictions and should not create or modify objects in the scene. See [Threading Restrictions](manual_scene_execution.md#threading-information) for more details.

### Attributes <a id="id3"></a>

These module-level attributes are injected into the Python Effector’s script scope.

| Name | Datatype | Description |
|---|---|---|
| `doc` | `c4d.documents.BaseDocument` | The document containing the effector. |
| `op` | `c4d.BaseObject` | The Python Effector object. |
| `gen` | `c4d.BaseObject` | The MoGraph generator executing the effector. |

### Methods <a id="id4"></a>

#### `main() → bool | float`

Override to read and modify the MoGraph data returned by [`c4d.modules.mograph.GeGetMoData()`](../modules/c4d.modules/mograph/index.md#c4d.modules.mograph.GeGetMoData). In full-control mode it is called once to handle all clones. In parameter-control mode it is called for each clone.

**Returns:**

`True` or a numeric result as required by the effector mode.

**Return type:** bool | float

The implementation invokes `main()` without positional arguments. In parameter mode it is evaluated for the current clone; in full-control mode it is evaluated once and can modify the [`c4d.modules.mograph.MoData`](../modules/c4d.modules/mograph/MoData/index.md#c4d.modules.mograph.MoData) obtained from [`c4d.modules.mograph.GeGetMoData()`](../modules/c4d.modules/mograph/index.md#c4d.modules.mograph.GeGetMoData).

## Python Field Object and Layer <a id="python-field-object-and-layer"></a>

A Python Field can be a Field Object in the scene or a Field Layer in a [`c4d.FieldList`](../modules/c4d/CustomDataType/FieldList/index.md#c4d.FieldList). The same callback names are used for both, but `Aggregate()` is called only for a Field Layer. The callbacks are called for each sampling pass and must not modify the scene.

> **Warning:** The field callbacks are subject to threading restrictions and should not create or modify objects in the scene. See [Threading Restrictions](manual_scene_execution.md#threading-information) for more details.

### Attributes <a id="id5"></a>

These module-level attributes are injected into the Python Field script scope. The sampling objects and information are passed as callback arguments, not stored as module-level attributes.

| Name | Datatype | Description |
|---|---|---|
| `doc` | `c4d.documents.BaseDocument` | The document containing the field. The field or layer is passed explicitly as `op` to callbacks. |

### Methods <a id="id6"></a>

#### `InitSampling(op: c4d.modules.mograph.FieldObject, info: c4d.modules.mograph.FieldInfo) → bool`

Called before a sampling pass starts. Use it to allocate resources needed by `Sample()`, such as a neighbor lookup or a KD-tree. Free those resources in `FreeSampling()`.

**Parameters:**

- **op** – The Python Field Object or Layer.
- **info** – Information about the current sampling pass.

**Returns:**

`True` to continue sampling.

**Return type:** bool

#### `Sample(op: c4d.modules.mograph.FieldObject, inputs: c4d.modules.mograph.FieldInput, outputs: c4d.modules.mograph.FieldOutputBlock, info: c4d.modules.mograph.FieldInfo) → bool`

Called for each field output block. Populate `outputs._value` and update its deactivation state. For a Field Layer, the output can already contain values from preceding fields.

**Parameters:**

- **op** – The Python Field Object or Layer.
- **inputs** – The input positions and transform for the current block.
- **outputs** – The output block to populate.
- **info** – Information about the current sampling pass.

**Returns:**

`True` to continue sampling.

**Return type:** bool

#### `Aggregate(op: c4d.modules.mograph.FieldObject, inputs: c4d.modules.mograph.FieldInput, outputs: c4d.modules.mograph.FieldOutputBlock, info: c4d.modules.mograph.FieldInfo) → bool`

Called after sample blocks have been processed for a Python Field Layer. It is not called for a Python Field Object. Use it to post-process or normalize the output, for example by applying a smoothing filter.

**Returns:**

`True` to continue.

**Return type:** bool

#### `FreeSampling(op: c4d.modules.mograph.FieldObject, info: c4d.modules.mograph.FieldInfo) → bool`

Called after a sampling pass. Free resources allocated in `InitSampling()` here.

**Returns:**

`True` when cleanup succeeded.

**Return type:** bool

The callback must return `True`. The result is converted to a boolean by the host.

Python Field scripts do not receive `op` or `info` as globals. The field or layer and the sampling information are passed explicitly to every sampling callback. `doc` is the only injected document reference.

## Python Interaction Tag <a id="python-interaction-tag"></a>

Python code in an Interaction Tag responds to mouse and selection events on the host object. The tag is intended for interactive viewport behavior and implements the interaction callbacks of a tag plugin.

> **Warning:** The interaction callbacks are subject to threading restrictions. See [Threading Restrictions](manual_scene_execution.md#threading-information) for more details.

### Attributes <a id="id7"></a>

These module-level attributes are injected into the Interaction Tag’s script scope. They are updated by Cinema 4D for the current interaction.

| Name | Datatype | Description |
|---|---|---|
| `tag` | `c4d.BaseTag` | The Interaction Tag. |
| `op` | `c4d.BaseObject` | The object hosting the tag. |
| `proxy` | `c4d.BaseObject` | The proxy object, or undefined when no proxy is involved. |
| `thread` | `c4d.threading.BaseThread` | The thread in which the tag is executed. |
| `qualifier` | `int` | The qualifier keys that were pressed. See [QUALIFIER](../consts/QUALIFIER.md). |

### Methods <a id="id8"></a>

#### `mouseDown() → None`

Called when the user presses the mouse button on the host object.

#### `mouseDrag() → None`

Called for each tick while the user drags with the mouse.

#### `mouseUp() → None`

Called when the user releases the mouse button.

#### `doubleClick() → None`

Called when the user double-clicks the host object.

#### `onSelect() → None`

Called when the host object is selected.

#### `onDeselect() → None`

Called when the host object is deselected.

#### `onHighlight() → None`

Called when the host object is highlighted.

#### `onUnhighlight() → None`

Called when the host object is no longer highlighted.

#### `draw(bd: c4d.BaseDraw) → None`

Called to draw visual elements in the editor view.

**Parameters:** **bd** ([*c4d.BaseDraw*](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The editor view.

The return value is ignored.

#### `message(mid: int, data: object) → bool | None`

Called when the tag receives a message.

**Parameters:**

- **mid** – The message ID.
- **data** – The message data.

**Return type:** bool | None

## Python Character Component Tag <a id="python-character-component-tag"></a>

Python code can customize the components of a Character Object through a Character Component Tag. The callbacks are available in the Python tab of the Character Component Tag and in Python insertion and adjustment rules.

> **Warning:** The Character Component Tag callbacks are subject to threading restrictions. See [Threading Restrictions](manual_scene_execution.md#threading-information) for more details.

### Attributes <a id="id9"></a>

The available callback-local attributes depend on the Character workflow and callback being executed. The following types are the Python types registered by the Character Builder module.

| Name | Datatype | Description |
|---|---|---|
| `doc` | `c4d.documents.BaseDocument` | The current document. |
| `charop` | `c4d.modules.character.builder.CharacterObject` | The Character Object. |
| `template` | `c4d.modules.character.builder.Template` | Character template data for template-related callbacks. |
| `op` | `c4d.BaseObject` | The object currently processed by the callback. |
| `pcompop` | `c4d.modules.character.builder.ComponentObject` | The parent component object. |
| `pcomp` | `c4d.modules.character.builder.Component` | The parent component. |
| `comp` | `c4d.modules.character.builder.Component` | The component being processed. |
| `compop` | `c4d.modules.character.builder.ComponentObject` | The component object being processed. |
| `parent` / `insertat` / `chainstart` / `chainend` / `linkop` | `c4d.BaseObject` | Callback-specific objects used by component insertion and dependency callbacks. |
| `incdata` | `c4d.BaseContainer` | Container used by `IncludeObjects()` to describe additional objects. |
| `mg` | `c4d.Matrix` | Matrix supplied to or returned by transform-related callbacks. |
| `itype` / `count` / `omode` / `nmode` | `int` | Insertion type, item count, and old/new mode values used by the corresponding callbacks. |

### Methods <a id="id10"></a>

#### `BuildTemplate() → None`

Override to build or modify a character template when it is saved.

**Parameters:**

- **doc** – The template document.
- **op** – The object with the Component Tag.

#### `GetComponents() → c4d.BaseContainer | None`

Override to control which components are available. Return a [`c4d.BaseContainer`](../modules/c4d/BaseContainer/index.md#c4d.BaseContainer) of component links, or `None` to use the standard inclusion rules.

#### `ModeChanged() → None`

Called when the Character Object changes between Build, Adjust, Bind, and Animate modes. The old and new modes are available as `omode` and `nmode`.

#### `InsertComponent() → c4d.BaseObject`

Override component insertion. Return the main component object from the Python tab, or the object under which the component should be inserted from an insertion rule. Set the global `itype` variable when using an insertion rule.

#### `PostInsertComponent() → None`

Called after a component has been inserted when `InsertComponent()` is not used.

#### `MirrorComponent() → bool`

Called when a mirrored component is added. Return `True` when mirroring was handled by Python.

#### `IncludeObjects() → bool`

Define additional objects to include with the `incdata` variable. Return `True` when it was changed.

#### `AdjustObject() → c4d.Matrix`

Return the matrix to set for an object controlled by an adjustment rule. The matrices are local to the Character Object.

#### `GetDependency() → c4d.BaseContainer`

Return a [`c4d.BaseContainer`](../modules/c4d/BaseContainer/index.md#c4d.BaseContainer) containing the objects on which an adjustment depends. This callback runs before `AdjustObject()`.

#### `TransformComponent() → c4d.Matrix`

Return the global matrix for an inserted component. The matrices are local to the Character Object.

#### `AllowComponent() → bool`

Return `True` when the component is allowed.

## Python Sketch and Toon Material <a id="python-sketch-and-toon-material"></a>

Python code can control the Color, Thickness, and Opacity channels of a Sketch and Toon Material. Enable the Python option in the channel to execute the script. Return a [`c4d.Vector`](../modules/c4d/Vector/index.md#c4d.Vector) for Color, and a float for Thickness or Opacity.

> **Warning:** The Sketch and Toon callback is evaluated during rendering and is subject to threading restrictions. See [Threading Restrictions](manual_scene_execution.md#threading-information) for more details.

### Attributes <a id="id11"></a>

The following module-level attributes are available while a Sketch and Toon channel script is evaluated. Additional variables depend on the channel and sampled line.

The host supplies the following values for the line being evaluated. Values in the ray/surface group describe the current render sample and are most useful for scripts in the Color channel.

| Name | Datatype | Description |
|---|---|---|
| `op` | `c4d.BaseObject` | The object currently being sampled. |
| `sPosition` | `float` | Position along the current stroke. |
| `sNormalisedP` | `float` | Normalized position along the current stroke. |
| `ToLine` | `float` | Distance from the sampled point to the line. |
| `Thickness` | `float` | Current stroke thickness. |
| `StrokeLength` | `float` | Length of the current stroke. |
| `ScnPnt` | `c4d.Vector` | Current point in scene coordinates. |
| `LineOff` | `float` | Offset of the current line. |
| `wPnt` | `c4d.Vector` | Current point in world coordinates. |
| `Time` | `float` | Current scene time in seconds. |
| `Frame` | `int` | Current frame number, computed from time and frame rate. |
| `FPS` | `int` | Current scene frame rate. |
| `LineStart` / `LineEnd` | `c4d.Vector` | Screen-space start and end points of the current line segment. |
| `LineNormal` | `c4d.Vector` | Normal of the current line segment. |
| `EdgeNormal` | `c4d.Vector` | Normal of the source edge. |
| `LinePosA` / `LinePosB` | `float` | Positions of the line endpoints within their source edges. |
| `JoinAngleA` / `JoinAngleB` | `float` | Join angle at the start and end of the line. The value is `0.0` when no join exists. |
| `PntA` / `PntB` | `int` | Point indices of the line’s start and end vertices. |
| `PolyA` / `PolyB` | `int` | Polygon indices associated with the line’s start and end. |
| `Color` | `c4d.Vector` | Current line color. For the Color channel, return the modified value from `main()`. |
| `RayBits` | `int` | Ray-intersection flags for the current render sample. |
| `CosC` | `float` | Cosine value for the current render sample. |
| `Normal` | `c4d.Vector` | Surface normal at the current render sample. |
| `BumpNormal` | `c4d.Vector` | Bump-mapped surface normal at the current render sample. |
| `Dist` | `float` | Distance for the current render sample. |
| `PolyHit` | `int` | Polygon index hit by the current render ray. |
| `RayPos` / `RayDirn` | `c4d.Vector` | Origin and direction of the current render ray. These are set only when ray data exists. |
| `SurfPnt` | `c4d.Vector` | Surface point for the current render sample. |
| `RendLeft` / `RendTop` / `RendRight` / `RendBottom` | `int` | Pixel bounds of the current render region. |
| `ObjLeft` / `ObjTop` / `ObjRight` / `ObjBottom` | `int` | Pixel bounds of the current object’s outline. If no outline is available, these fall back to the render-region bounds. |

### Methods <a id="id12"></a>

#### `main()`

Return a [`c4d.Vector`](../modules/c4d/Vector/index.md#c4d.Vector) for Color, or a float for Thickness and Opacity. The callback is evaluated for each sampled line.

## Python Visual Selector Tag <a id="python-visual-selector-tag"></a>

Python code can respond when a hotspot is clicked. The script is evaluated in the context of the Visual Selector Tag.

> **Warning:** The *main* function of a Python Visual Selector Tag is subject to threading restrictions. See [Threading Restrictions](manual_scene_execution.md#threading-information) for more details.

### Attributes <a id="id13"></a>

These module-level attributes are injected into the Visual Selector script scope for the selected hotspot.

| Name | Datatype | Description |
|---|---|---|
| `doc` | `c4d.documents.BaseDocument` | The document containing the tag. |
| `op` | `c4d.BaseObject \| None` | The object in the tag’s link field, or `None`. |

### Methods <a id="id14"></a>

#### `main()`

Called when the user presses a hotspot.

## Python Xpresso Node <a id="python-xpresso-node"></a>

Python code can be executed in a Python Xpresso Node. The node creates a global variable for each input and output port using the port name. `main()` takes no positional arguments. Read input variables and assign output variables before returning. A Python Xpresso Node should not modify the scene.

> **Warning:** The *main* function of a Python Xpresso Node is subject to threading restrictions. See [Threading Restrictions](manual_scene_execution.md#threading-information) for more details.

### Attributes <a id="id15"></a>

These module-level attributes are injected into the Python Xpresso Node’s script scope. The Thinking Particles reference is set to `None` when the document has no Thinking Particles system.

| Name | Datatype | Description |
|---|---|---|
| `doc` | `c4d.documents.BaseDocument` | The document containing the Xpresso tag. |
| `op` | `c4d.modules.graphview.GvNode` | The current Python Xpresso Node. |
| `tp` | `c4d.modules.thinkingparticles.TP_MasterSystem \| None` | The document’s Thinking Particles master system, or `None`. |

### Methods <a id="id16"></a>

#### `main()`

Called when the node is evaluated by the GvNodeMaster. The return value is ignored.

Input and output variables are dynamic: their names and types are determined by the ports on the node. The activation input named `On` controls whether the callback is evaluated, but is not exposed as a regular input variable.

### See Also <a id="see-also"></a>

- [Script Manager and Console](manual_script_manager.md): Write and run scripts in the Script Manager and inspect results in the Python Console.
- [Scene Execution](manual_scene_execution.md): Explains how Cinema 4D updates a scene, and where Python code runs in that process.
