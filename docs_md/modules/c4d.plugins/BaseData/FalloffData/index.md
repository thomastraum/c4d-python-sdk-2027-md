<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseData/FalloffData/index.html -->

# c4d.plugins.FalloffData <a id="c4d-plugins-falloffdata"></a>

## *class* `c4d.plugins.FalloffData` <a id="c4d.plugins.FalloffData"></a>

This class is the base falloff class. Falloffs will appear in any falloff descriptions (unless the flag *PLUGIN_HIDE* is used during registration), and extend the functionality of tools such as effectors (or anything that uses the falloffs). Use `RegisterFalloffPlugin()` to register the plugin.

Parent Class:

- [`c4d.plugins.BaseData`](../index.md#c4d.plugins.BaseData)

## Overview <a id="overview"></a>

**Evaluation State**

- [`FalloffData.CheckDirty()`](#c4d.plugins.FalloffData.CheckDirty)
- [`FalloffData.Sample()`](#c4d.plugins.FalloffData.Sample): Called to sample any point.

**Handle Management**

- [`FalloffData.GetHandle()`](#c4d.plugins.FalloffData.GetHandle): Called to get the information for handle at index *i*. Part of the automated handle interface.
- [`FalloffData.GetHandleCount()`](#c4d.plugins.FalloffData.GetHandleCount): Called to get the number of handles the falloff has.
- [`FalloffData.SetHandle()`](#c4d.plugins.FalloffData.SetHandle): Called to set the information for handle at index *i*. Part of the automated handle interface.

**Initialization And Messaging**

- [`FalloffData.Init()`](#c4d.plugins.FalloffData.Init): Called when the falloff is first created.
- [`FalloffData.InitFalloff()`](#c4d.plugins.FalloffData.InitFalloff): Called just before sampling.
- [`FalloffData.Message()`](#c4d.plugins.FalloffData.Message): Called when the falloff receives messages.

**Viewport Display**

- [`FalloffData.Draw()`](#c4d.plugins.FalloffData.Draw): For allowing you to draw the falloff in the viewport.
- [`FalloffData.GetDVisible()`](#c4d.plugins.FalloffData.GetDVisible): Called to change the visibility of any element in the description; just return **True** or **False** for the *id*.

## Members <a id="members"></a>

### Evaluation State <a id="c4d.plugins.FalloffData-method-Evaluation-State"></a>

#### `FalloffData.CheckDirty(self, doc, bc)` <a id="c4d.plugins.FalloffData.CheckDirty"></a>

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document to operates in.
- **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Falloff’s basecontainer; normally this is the owning object’s basecontainer.

**Return type:** bool

**Returns:** Dirty state.

#### `FalloffData.Sample(self, p, data)` <a id="c4d.plugins.FalloffData.Sample"></a>

Called to sample any point.

> **Note:** To get *p* in world coordinates multiply it by `data.mat`.

**Parameters:**

- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The position of the point to sample in falloff space.
- **data** (*c4d.modules.mograph.FalloffDataData*) – Falloff data information.

**Return type:** float

**Returns:** The falloff value.

### Handle Management <a id="c4d.plugins.FalloffData-method-Handle-Management"></a>

#### `FalloffData.GetHandle(self, bc, i, info, data)` <a id="c4d.plugins.FalloffData.GetHandle"></a>

Called to get the information for handle at index *i*. Part of the automated handle interface.

**Parameters:**

- **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Falloff’s container; normally this is the owning falloff’s basecontainer.
- **i** (*int*) – The handle index.
- **info** ([*c4d.HandleInfo*](../../../c4d/HandleInfo/index.md#c4d.HandleInfo)) – The handle info.
- **data** (*c4d.modules.mograph.FalloffDataData*) – Falloff data information.

**Return type:** [c4d.Vector](../../../c4d/Vector/index.md#c4d.Vector)

**Returns:** The current local position of the handle with index *i*.

#### `FalloffData.GetHandleCount(self, bc)` <a id="c4d.plugins.FalloffData.GetHandleCount"></a>

Called to get the number of handles the falloff has. Part of the automated handle interface.

**Parameters:** **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Falloff’s container; normally this is the owning falloff’s basecontainer.

**Return type:** int

**Returns:** The number of handles.

#### `FalloffData.SetHandle(self, bc, i, p, data)` <a id="c4d.plugins.FalloffData.SetHandle"></a>

Called to set the information for handle at index *i*. Part of the automated handle interface.  
Called when the user has moved handle *i* to position *p*. Update the falloff’s internal data accordingly (e.g. parameter values etc).

**Parameters:**

- **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Falloff’s container; normally this is the owning falloff’s basecontainer.
- **i** (*int*) – The handle index.
- **p** ([*c4d.Vector*](../../../c4d/Vector/index.md#c4d.Vector)) – The new position for handle *i*.
- **data** (*c4d.modules.mograph.FalloffDataData*) – Falloff data information.

### Initialization And Messaging <a id="c4d.plugins.FalloffData-method-Initialization-And-Messaging"></a>

#### `FalloffData.Init(self, bc)` <a id="c4d.plugins.FalloffData.Init"></a>

Called when the falloff is first created.

**Parameters:** **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Falloff’s basecontainer; normally this is the owning object’s basecontainer.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `FalloffData.InitFalloff(self, bc, falldata)` <a id="c4d.plugins.FalloffData.InitFalloff"></a>

Called just before sampling. Allows you to set up any necessary data in *falldata* or *bc*.

**Parameters:**

- **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Falloff’s basecontainer; normally this is the owning object’s basecontainer.
- **falldata** (*c4d.modules.mograph.FalloffDataData*) – Falloff data information.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `FalloffData.Message(self, type, bc, m_data)` <a id="c4d.plugins.FalloffData.Message"></a>

Called when the falloff receives messages.

> **See also:** [C4DAtom and Plugin Messages](../../../../consts/MSG_C4DATOM_PLUGINS.md) for information on the messages type, data and input/output.

**Parameters:**

- **type** (*int*) – The message type:
- **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Falloff’s basecontainer; normally this is the owning object’s basecontainer.
- **m_data** (*any*) – The message data.

**Return type:** bool

**Returns:** Depends on the message type.

### Viewport Display <a id="c4d.plugins.FalloffData-method-Viewport-Display"></a>

#### `FalloffData.Draw(self, data, drawpass, bd, bh)` <a id="c4d.plugins.FalloffData.Draw"></a>

For allowing you to draw the falloff in the viewport. You should use these predefined color constants:

|   |   |
|---|---|
| *FALLOFFCAGE* | Default cage color. |
| *FALLOFFFALLOFF* | Default falloff color. |

> **Note:** This function is called in a thread context. Please see the [important information](../../../../manuals/manual_scene_execution.md#threading-information) about threading.

**Parameters:**

- **data** (*c4d.modules.mograph.FalloffDataData*) – Falloff data information.

- **drawpass** (*int*) –

  One of the following:

  |   |   |
  |---|---|
  | *DRAWPASS_OBJECT* | Object pass. |
  | *DRAWPASS_BOX* | Box pass. |
  | *DRAWPASS_HANDLES* | Handle pass. |
  | *DRAWPASS_HIGHLIGHTS* | Highlights pass. |
  | *DRAWPASS_XRAY* | X-Ray pass. |

  > **Warning:** Only draw in *DRAWPASS_HIGHLIGHTS* if you **really** know what you are doing. Otherwise **always** check the *drawpass* and then **do not** draw if it is *DRAWPASS_HIGHLIGHTS*.

  Here is an example.

  ```python
  def Draw(self, data, drawpass, bd, bh):

      if drawpass==c4d.DRAWPASS_HIGHLIGHTS:
          return False

      # Put here your drawing operations

      return True
  ```

- **bd** ([*c4d.BaseDraw*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The editor’s view.

- **bh** ([*c4d.plugins.BaseDrawHelp*](../../BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp)) – The [`BaseDrawHelp`](../../BaseDrawHelp/index.md#c4d.plugins.BaseDrawHelp) editor’s view.

**Return type:** int

**Returns:**

Success of drawing into the editor view:

| Symbol ID | Description |
|---|---|
| DRAWRESULT_FAILURE | There was an error while drawing. |
| DRAWRESULT_OK | Something was drawn. |
| DRAWRESULT_SKIP | There was nothing to draw in the pass. |

*Changed in version R18.011:* Changed to *DRAWRESULT*. Returning a bool is still supported for backward compatibility.

#### `FalloffData.GetDVisible(self, id, bc, desc_bc)` <a id="c4d.plugins.FalloffData.GetDVisible"></a>

Called to change the visibility of any element in the description; just return **True** or **False** for the *id*.

**Parameters:**

- **id** ([*c4d.DescID*](../../../c4d/DescID/index.md#c4d.DescID)) – The ID being evaluated.
- **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – Falloff’s basecontainer; normally this is the owning object’s basecontainer.
- **desc_bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The description element’s container.

**Return type:** bool

**Returns:** Visibility of *id*.
