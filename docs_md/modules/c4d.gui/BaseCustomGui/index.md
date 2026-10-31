<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.gui/BaseCustomGui/index.html -->

# c4d.gui.BaseCustomGui <a id="c4d-gui-basecustomgui"></a>

## *class* `c4d.gui.BaseCustomGui` <a id="c4d.gui.BaseCustomGui"></a>

The base class for custom GUI libraries.

Children Classes:

- [`c4d.gui.LinkBoxGui`](LinkBoxGui/index.md#c4d.gui.LinkBoxGui)
- [`c4d.gui.InExcludeCustomGui`](InExcludeCustomGui/index.md#c4d.gui.InExcludeCustomGui)
- [`c4d.gui.HtmlViewerCustomGui`](HtmlViewerCustomGui/index.md#c4d.gui.HtmlViewerCustomGui)
- [`c4d.gui.SplineCustomGui`](SplineCustomGui/index.md#c4d.gui.SplineCustomGui)
- [`c4d.gui.SoundEffectorCustomGui`](SoundEffectorCustomGui/index.md#c4d.gui.SoundEffectorCustomGui)
- [`c4d.gui.TreeViewCustomGui`](TreeViewCustomGui/index.md#c4d.gui.TreeViewCustomGui)
- [`c4d.gui.GradientCustomGui`](GradientCustomGui/index.md#c4d.gui.GradientCustomGui)
- [`c4d.gui.DescriptionCustomGui`](DescriptionCustomGui/index.md#c4d.gui.DescriptionCustomGui)
- [`c4d.gui.BitmapButtonCustomGui`](BitmapButtonCustomGui/index.md#c4d.gui.BitmapButtonCustomGui)
- [`c4d.gui.QuickTabCustomGui`](QuickTabCustomGui/index.md#c4d.gui.QuickTabCustomGui)
- [`c4d.gui.DateTimeControl`](DateTimeControlData/index.md#c4d.gui.DateTimeControl)
- [`c4d.gui.HyperLinkCustomGui`](HyperLinkCustomGui/index.md#c4d.gui.HyperLinkCustomGui)
- [`c4d.gui.FontChooserCustomGui`](FontChooserCustomGui/index.md#c4d.gui.FontChooserCustomGui)
- [`c4d.gui.RangeCustomGui`](RangeCustomGui/index.md#c4d.gui.RangeCustomGui)

## Overview <a id="overview"></a>

**Activation And Defaults**

- [`BaseCustomGui.Activate()`](#c4d.gui.BaseCustomGui.Activate): Activates the custom GUI.
- [`BaseCustomGui.SetDefaultForResEdit()`](#c4d.gui.BaseCustomGui.SetDefaultForResEdit): Sets the custom GUI to the resource editor defaults.

**Dimensions**

- [`BaseCustomGui.GetHeight()`](#c4d.gui.BaseCustomGui.GetHeight): Retrieves the height of the custom GUI in pixels.
- [`BaseCustomGui.GetWidth()`](#c4d.gui.BaseCustomGui.GetWidth): Retrieves the width of the custom GUI in pixels.

**Rendering And Layout**

- [`BaseCustomGui.GetLayoutMode()`](#c4d.gui.BaseCustomGui.GetLayoutMode): Retrieves the layout mode.
- [`BaseCustomGui.LayoutChanged()`](#c4d.gui.BaseCustomGui.LayoutChanged): Tells the custom GUI that the layout has changed.
- [`BaseCustomGui.Redraw()`](#c4d.gui.BaseCustomGui.Redraw): Redraws the custom GUI.
- [`BaseCustomGui.SetLayoutMode()`](#c4d.gui.BaseCustomGui.SetLayoutMode): Sets the layout mode.
- [`BaseCustomGui.SupportLayoutSwitch()`](#c4d.gui.BaseCustomGui.SupportLayoutSwitch): Checks if the custom GUI supports layout switching.

**State And Data**

- [`BaseCustomGui.GetData()`](#c4d.gui.BaseCustomGui.GetData): Retrieves the custom GUI data.
- [`BaseCustomGui.SetData()`](#c4d.gui.BaseCustomGui.SetData): Sets the custom GUI data.

## Members <a id="members"></a>

### Activation And Defaults <a id="c4d.gui.BaseCustomGui-method-Activation-And-Defaults"></a>

#### `BaseCustomGui.Activate(self)` <a id="c4d.gui.BaseCustomGui.Activate"></a>

Activates the custom GUI.

*New in version R18.011.*

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `BaseCustomGui.SetDefaultForResEdit(self)` <a id="c4d.gui.BaseCustomGui.SetDefaultForResEdit"></a>

Sets the custom GUI to the resource editor defaults.

*New in version R18.011.*

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Dimensions <a id="c4d.gui.BaseCustomGui-method-Dimensions"></a>

#### `BaseCustomGui.GetHeight(self)` <a id="c4d.gui.BaseCustomGui.GetHeight"></a>

Retrieves the height of the custom GUI in pixels.

*New in version R18.011.*

**Return type:** int

**Returns:** The height of the custom GUI.

#### `BaseCustomGui.GetWidth(self)` <a id="c4d.gui.BaseCustomGui.GetWidth"></a>

Retrieves the width of the custom GUI in pixels.

*New in version R18.011.*

**Return type:** int

**Returns:** The width of the custom GUI.

### Rendering And Layout <a id="c4d.gui.BaseCustomGui-method-Rendering-And-Layout"></a>

#### `BaseCustomGui.GetLayoutMode(self)` <a id="c4d.gui.BaseCustomGui.GetLayoutMode"></a>

Retrieves the layout mode.

*New in version R18.011.*

**Return type:** int

**Returns:**

The current layout mode:

|   |   |
|---|---|
| *LAYOUTMODE_NONE* | Does not support layout modes. |
| *LAYOUTMODE_MINIMIZED* | Minimized. |
| *LAYOUTMODE_MAXIMIZED* | Maximized. |

#### `BaseCustomGui.LayoutChanged(self)` <a id="c4d.gui.BaseCustomGui.LayoutChanged"></a>

Tells the custom GUI that the layout has changed.

*New in version R18.011.*

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `BaseCustomGui.Redraw(self)` <a id="c4d.gui.BaseCustomGui.Redraw"></a>

Redraws the custom GUI.

*New in version R18.011.*

#### `BaseCustomGui.SetLayoutMode(self, mode)` <a id="c4d.gui.BaseCustomGui.SetLayoutMode"></a>

Sets the layout mode.

*New in version R18.011.*

**Parameters:**

**mode** (*int*) –

The new layout mode:

|   |   |
|---|---|
| *LAYOUTMODE_NONE* | Does not support layout modes. |
| *LAYOUTMODE_MINIMIZED* | Minimized. |
| *LAYOUTMODE_MAXIMIZED* | Maximized. |

#### `BaseCustomGui.SupportLayoutSwitch(self)` <a id="c4d.gui.BaseCustomGui.SupportLayoutSwitch"></a>

Checks if the custom GUI supports layout switching.

*New in version R18.011.*

**Return type:** bool

**Returns:** **True** if the layout switch is supported, otherwise **False**.

### State And Data <a id="c4d.gui.BaseCustomGui-method-State-And-Data"></a>

#### `BaseCustomGui.GetData(self)` <a id="c4d.gui.BaseCustomGui.GetData"></a>

Retrieves the custom GUI data.

*New in version R18.011.*

**Return type:** Any

**Returns:** The current data.

#### `BaseCustomGui.SetData(self, data)` <a id="c4d.gui.BaseCustomGui.SetData"></a>

Sets the custom GUI data.

*New in version R18.011.*

**Parameters:** **data** (*any*) – The new data.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.
