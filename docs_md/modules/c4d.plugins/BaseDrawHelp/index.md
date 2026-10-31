<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseDrawHelp/index.html -->

# c4d.plugins.BaseDrawHelp <a id="c4d-plugins-basedrawhelp"></a>

## *class* `c4d.plugins.BaseDrawHelp` <a id="c4d.plugins.BaseDrawHelp"></a>

Contains useful data for drawing objects into a BaseDraw view.

## Overview <a id="overview"></a>

**Display Settings**

- [`BaseDrawHelp.GetDisplay()`](#c4d.plugins.BaseDrawHelp.GetDisplay): Retrieves a container with the display mode for the object to be drawn.
- [`BaseDrawHelp.SetDisplay()`](#c4d.plugins.BaseDrawHelp.SetDisplay): Sets the display mode for the object to be drawn.

**Magic Methods**

- [`BaseDrawHelp.__init__()`](#c4d.plugins.BaseDrawHelp.__init__): Create a new help object for base draw *bd*.

**Scene Context**

- [`BaseDrawHelp.GetActiveTag()`](#c4d.plugins.BaseDrawHelp.GetActiveTag): Returns the currently active tag, or **None** if no tag is active (similar to `BaseDocument.GetActiveTag()` but more efficient since the active tag is cached).
- [`BaseDrawHelp.GetDocument()`](#c4d.plugins.BaseDrawHelp.GetDocument): Returns the relevant document for the current draw operation, i.e.

**Transform**

- [`BaseDrawHelp.GetMg()`](#c4d.plugins.BaseDrawHelp.GetMg): Returns the global matrix of the object to be drawn (similar to `BaseObject.GetMg()` but more efficient since the matrix is cached).
- [`BaseDrawHelp.SetMg()`](#c4d.plugins.BaseDrawHelp.SetMg): Sets the matrix returned by `GetMg()`.

**View Interaction State**

- [`BaseDrawHelp.GetViewSchedulerFlags()`](#c4d.plugins.BaseDrawHelp.GetViewSchedulerFlags): Returns the flags which have been passed to [`DrawViews()`](../../c4d/index.md#c4d.DrawViews).
- [`BaseDrawHelp.IsActive()`](#c4d.plugins.BaseDrawHelp.IsActive): Checks if the current object is active.
- [`BaseDrawHelp.IsHighlight()`](#c4d.plugins.BaseDrawHelp.IsHighlight): Checks if the current object is highlighted (i.e.

## Members <a id="members"></a>

### Display Settings <a id="c4d.plugins.BaseDrawHelp-method-Display-Settings"></a>

#### `BaseDrawHelp.GetDisplay(self)` <a id="c4d.plugins.BaseDrawHelp.GetDisplay"></a>

Retrieves a container with the display mode for the object to be drawn. See *Tdisplay.h* for values.

**Return type:** [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The display mode container.

#### `BaseDrawHelp.SetDisplay(self, bc)` <a id="c4d.plugins.BaseDrawHelp.SetDisplay"></a>

Sets the display mode for the object to be drawn. See *Tdisplay.h* for values.

*New in version R19.*

**Parameters:** **bc** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The new display mode container.

### Magic Methods <a id="c4d.plugins.BaseDrawHelp-method-Magic-Methods"></a>

#### `BaseDrawHelp.__init__(self, bd, doc)` <a id="c4d.plugins.BaseDrawHelp.__init__"></a>

Create a new help object for base draw *bd*.

**Parameters:**

- **bd** ([*c4d.BaseDraw*](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseView/BaseDraw/index.md#c4d.BaseDraw)) – The base draw the [`BaseDrawHelp`](#c4d.plugins.BaseDrawHelp) is assigned to.
- **doc** ([*c4d.documents.BaseDocument*](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document of the base draw *bd*.

### Scene Context <a id="c4d.plugins.BaseDrawHelp-method-Scene-Context"></a>

#### `BaseDrawHelp.GetActiveTag(self)` <a id="c4d.plugins.BaseDrawHelp.GetActiveTag"></a>

Returns the currently active tag, or **None** if no tag is active (similar to `BaseDocument.GetActiveTag()` but more efficient since the active tag is cached).

**Return type:** Optional[[c4d.BaseTag](../../c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag)]

**Returns:** The active tag.

#### `BaseDrawHelp.GetDocument(self)` <a id="c4d.plugins.BaseDrawHelp.GetDocument"></a>

Returns the relevant document for the current draw operation, i.e. the currently active document. Never returns **None**.

**Return type:** [c4d.documents.BaseDocument](../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)

**Returns:** The relevant document.

### Transform <a id="c4d.plugins.BaseDrawHelp-method-Transform"></a>

#### `BaseDrawHelp.GetMg(self)` <a id="c4d.plugins.BaseDrawHelp.GetMg"></a>

Returns the global matrix of the object to be drawn (similar to `BaseObject.GetMg()` but more efficient since the matrix is cached).

**Return type:** [c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix)

**Returns:** The global matrix.

#### `BaseDrawHelp.SetMg(self, mg)` <a id="c4d.plugins.BaseDrawHelp.SetMg"></a>

Sets the matrix returned by [`GetMg()`](#c4d.plugins.BaseDrawHelp.GetMg).

**Parameters:** **mg** ([*c4d.Matrix*](../../c4d/Matrix/index.md#c4d.Matrix)) – New matrix.

### View Interaction State <a id="c4d.plugins.BaseDrawHelp-method-View-Interaction-State"></a>

#### `BaseDrawHelp.GetViewSchedulerFlags(self)` <a id="c4d.plugins.BaseDrawHelp.GetViewSchedulerFlags"></a>

Returns the flags which have been passed to [`DrawViews()`](../../c4d/index.md#c4d.DrawViews).

**Return type:** int

**Returns:**

Flags:

|   |   |
|---|---|
| *DRAWFLAGS_NONE* | None. |
| *DRAWFLAGS_NO_THREAD* | Synchronous call. |
| *DRAWFLAGS_NO_ANIMATION* | Ignore all animation. |
| *DRAWFLAGS_ONLY_ACTIVE_VIEW* | Only redraw the active view. |
| *DRAWFLAGS_NO_EXPRESSIONS* | Ignore expressions. |
| *DRAWFLAGS_INDRAG* | In drag. |
| *DRAWFLAGS_NO_HIGHLIGHT_PLANE* | The entire view is drawn, not just the highlight plane. |
| *DRAWFLAGS_FORCEFULLREDRAW* | Force full redraw. |
| *DRAWFLAGS_ONLY_CAMERAEXPRESSION* | Camera expression. |
| *DRAWFLAGS_INMOVE* | In move. |
| *DRAWFLAGS_ONLY_BASEDRAW* | Draw specific base draw only. |
| *DRAWFLAGS_ONLY_HIGHLIGHT* | Only highlights. |
| *DRAWFLAGS_STATICBREAK* | If the display is done in the main thread (Cinema 4D only does this during animation playback) this allows that a special thread is used that polls the escape key. **Note**: Use only in combination with *DRAWFLAGS_NO_THREAD*. |
| *DRAWFLAGS_PRIVATE_NO_WAIT_GL_FINISHED* | Private. |
| *DRAWFLAGS_PRIVATE_ONLYBACKGROUND* | Private. |
| *DRAWFLAGS_PRIVATE_NOBLIT* | Private. |
| *DRAWFLAGS_PRIVATE_OPENGLHACK* | Private. |
| *DRAWFLAGS_PRIVATE_ONLY_PREPARE* | Private. |
| *DRAWFLAGS_PRIVATE_NO_DCLIPPING* | Private. |
| *DRAWFLAGS_NO_PRESENT* | *New in version R24:* \| Prevents the drawport from swapping buffers.. \| Use only in combination with *DRAWFLAGS_NO_THREAD*. |

#### `BaseDrawHelp.IsActive(self)` <a id="c4d.plugins.BaseDrawHelp.IsActive"></a>

Checks if the current object is active.

*New in version R14.014.*

**Return type:** bool

**Returns:** **True** if the current object is active.

#### `BaseDrawHelp.IsHighlight(self)` <a id="c4d.plugins.BaseDrawHelp.IsHighlight"></a>

Checks if the current object is highlighted (i.e. when the user has moved the mouse over it).

*New in version R14.014.*

**Return type:** bool

**Returns:** **True** if the current object is highlighted.
