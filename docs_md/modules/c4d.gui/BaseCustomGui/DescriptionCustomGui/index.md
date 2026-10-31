<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.gui/BaseCustomGui/DescriptionCustomGui/index.html -->

# c4d.gui.DescriptionCustomGui <a id="c4d-gui-descriptioncustomgui"></a>

## *class* `c4d.gui.DescriptionCustomGui` <a id="c4d.gui.DescriptionCustomGui"></a>

Description GUI (**CUSTOMGUI_DESCRIPTION**). This is the GUI used in the Attribute Manager. These are the settings:

> |   |   |   |
> |---|---|---|
> | *DESCRIPTION_ALLOWFOLDING* | bool | Allow folding. |
> | *DESCRIPTION_SHOWTITLE* | bool | Show title. |
> | *DESCRIPTION_NOUNDO* | bool | No undo. |
> | *DESCRIPTION_OBJECTSNOTINDOC* | bool | Objects are not located in document. |
> | *DESCRIPTION_FORCEGETOBJECT* | bool | *New in version R20:* Force retrieve the objects regardless of document state. |
> | *DESCRIPTION_MODALMODE* | int | Mode for modal dialogs: *1* for normal, *2* for no scroll areas. |
> | *DESCRIPTION_LEFTMATEDITREGION* | bool | Mode for left Material Manager region. |
> | *DESCRIPTION_STORAGE* | container | Layout storage. |
> | *DESCRIPTION_FOLDERSTORE* | container | Folder store. |
> | *DESCRIPTION_SCALE_ALL_ELEMENTS* | bool | Scale all elements. |
> | *DESCRIPTION_NO_SHOW_SUBCHANNELS* | bool | Remove the “Show Sub-channels” context menu. |
> | *DESCRIPTION_OPEN_ALL_GROUPS* | bool | Unfold all parameter groups. |
> | *DESCRIPTION_NO_TAKE_OVERRIDES* | bool | *New in version R17.032:* If **True** ignore the overrides enabling/disabling. |
> | *DESCRIPTION_SINGLEDESC_MODE* | private | *New in version R17.032:* Private. |
> | *DESCRIPTION_MANAGER_TYPE* | private | *New in version R20:* Private. |
> | *DESCRIPTION_HIDE_EMPTY_GROUPS* | bool | *New in version R20.041:* If **True** hide empty User Data groups |

*New in version R16.050.*

Parent Class:

- [`c4d.gui.BaseCustomGui`](../index.md#c4d.gui.BaseCustomGui)

## Overview <a id="overview"></a>

- [`DescriptionCustomGui.SetObject()`](#c4d.gui.DescriptionCustomGui.SetObject): Sets a single object to show.

## Members <a id="members"></a>

### Object Assignment <a id="c4d.gui.DescriptionCustomGui-method-Object-Assignment"></a>

#### `DescriptionCustomGui.SetObject(self, op)` <a id="c4d.gui.DescriptionCustomGui.SetObject"></a>

Sets a single object to show.

**Parameters:** **op** ([*c4d.BaseObject*](../../../c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject)) – The object to show. Must not be **None**.
