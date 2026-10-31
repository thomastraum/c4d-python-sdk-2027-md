<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/Description/index.html -->

# c4d.Description <a id="c4d-description"></a>

## *class* `c4d.Description` <a id="c4d.Description"></a>

The description class contains information for all description IDs of an object.  
For example it stores a [`BaseContainer`](../BaseContainer/index.md#c4d.BaseContainer) for *ID_BASEOBJECT_REL_POSITION* that describes that this value is a [`Vector`](../Vector/index.md#c4d.Vector), has minimum and maximum values XYZ etc.

*New in version R15.037.*

The information about each description parameter is stored in a [`BaseContainer`](../BaseContainer/index.md#c4d.BaseContainer) with the following values:

| Name | Type | Description |
|---|---|---|
| *DESC_NAME* | str | Name for standalone use. |
| *DESC_SHORT_NAME* | str | Short name, for attributes dialog. |
| *DESC_VERSION* | int | Show in versions: |
|  | *DESC_VERSION_DEMO* | Demo versions. |
|  | *DESC_VERSION_XL* | XL Versions. |
|  | *DESC_VERSION_ALL* | All versions. |
| *DESC_CHILDREN* | [`c4d.BaseContainer`](../BaseContainer/index.md#c4d.BaseContainer) | Internal. |
| *DESC_MIN* | int/float/[`c4d.Vector`](../Vector/index.md#c4d.Vector) | Minimum value. |
| *DESC_MAX* | int/float/[`c4d.Vector`](../Vector/index.md#c4d.Vector) | Maximum value. |
| *DESC_MINEX* | bool | **True** if *DESC_MIN* is exclusive, otherwise it is inclusive. |
| *DESC_MAXEX* | bool | **True** if *DESC_MAX* is exclusive, otherwise it is inclusive. |
| *DESC_STEP* | int/float/[`c4d.Vector`](../Vector/index.md#c4d.Vector) | The step for the edit field arrows. |
| *DESC_ANIMATE* | int | Animation mode: |
|  | *DESC_ANIMATE_OFF* | Parameter is not animatable. |
|  | *DESC_ANIMATE_ON* | Parameter is animatable. |
|  | *DESC_ANIMATE_MIX* | Parameter is animatable, but needs to know the left and right data element. |
| *DESC_ASKOBJECT* | bool | **True** means ask object for the parameter, **False** means look in container. |
| *DESC_UNIT* | int | Unit for *DTYPE_REAL*/*DTYPE_VECTOR*: |
|  | *DESC_UNIT_FLOAT* | *FORMAT_FLOAT* |
|  | *DESC_UNIT_INT* | *FORMAT_INT* |
|  | *DESC_UNIT_PERCENT* | *FORMAT_PERCENT* |
|  | *DESC_UNIT_DEGREE* | *FORMAT_DEGREE* |
|  | *DESC_UNIT_METER* | *FORMAT_METER* |
|  | *DESC_UNIT_TIME* | *FORMAT_FRAMES* |
| *DESC_PARENTGROUP* | int/[`c4d.DescID`](../DescID/index.md#c4d.DescID) | Parent ID. |
| *DESC_CYCLE* | [`c4d.BaseContainer`](../BaseContainer/index.md#c4d.BaseContainer) | Contains members of cycle as string, e.g. *GetString(10041)* == ‘-X’. |
| *DESC_HIDE* | bool | Indicates whether the property is hidden or not. |
| *DESC_DEFAULT* | int/float/[`c4d.Vector`](../Vector/index.md#c4d.Vector) | Default numeric value. |
| *DESC_ACCEPT* | [`c4d.BaseContainer`](../BaseContainer/index.md#c4d.BaseContainer) | Contains the accepted IDs as strings. For `C4DAtom.IsInstanceOf()` checks, e.g. *GetString(5155)* == ‘Obase’. |
| *DESC_SEPARATORLINE* | bool | **True** if separators should have a visible line. |
| *DESC_REFUSE* | [`c4d.BaseContainer`](../BaseContainer/index.md#c4d.BaseContainer) | Contains the refused IDs as strings. For `C4DAtom.IsInstanceOf()` checks, e.g. *GetString(5155)* == ‘Obase’. |
| *DESC_PARENTID* | int | The ID of the parent parameter used for indentation and animation track. |
| *DESC_CUSTOMGUI* | int | The ID of the custom GUI for the parameter. Either a 3rd party plugin ID or a *CUSTOMGUI*. |
| *DESC_COLUMNS* | int | Number of columns for layout groups (*DTYPE_GROUP*). |
| *DESC_LAYOUTGROUP* | bool | **True** for layout groups (*LAYOUTGROUP*). |
| *DESC_REMOVEABLE* | bool | **True** if entry is removable. |
| *DESC_GUIOPEN* | bool | **True** if the maximized GUI is shown by default. |
| *DESC_EDITABLE* | bool | **True** if entry is editable. |
| *DESC_MINSLIDER* | int/float/[`c4d.Vector`](../Vector/index.md#c4d.Vector) | Minimum value for slider. |
| *DESC_MAXSLIDER* | int/float/[`c4d.Vector`](../Vector/index.md#c4d.Vector) | Maximum value for slider. |
| *DESC_GROUPSCALEV* | bool | Allow the group height to be scaled. |
| *DESC_SCALEH* | bool | Scale element horizontally. |
| *DESC_LAYOUTVERSION* | int | Layout version. |
| *DESC_ALIGNLEFT* | bool | Align element left. |
| *DESC_FITH* | bool | Fit element. |
| *DESC_NEWLINE* | bool | Line break. |
| *DESC_TITLEBAR* | bool | Main group title bar. |
| *DESC_CYCLEICONS* | [`c4d.BaseContainer`](../BaseContainer/index.md#c4d.BaseContainer) | Icon IDs for cycle. |
| *DESC_CYCLESYMBOLS* | [`c4d.BaseContainer`](../BaseContainer/index.md#c4d.BaseContainer) | String identifiers for help symbol export. |
| *DESC_PARENT_COLLAPSE* | int | Parent collapse ID. |
| *DESC_FORBID_INLINE_FOLDING* | bool | Instructs the Attribute Manager to not allow expanding inline objects for entry. |
| *DESC_FORBID_SCALING* | bool | Prevents auto-scaling of the parameter with the scale tool (for *DESC_UNIT_METER*). |
| *DESC_ANGULAR_XYZ* | bool | **True** for XYZ as angular representation, or **False** for HPB. |
| *DESC_FORBID_COLOR_CONVERSION* | bool | *New in version 2025.0:* Prevents the automated converter from transforming values for this Color field. |
| *DESC_HELPTEXT* | str | *New in version 2025.1:* Allows to display a help text for string fields. |
| *DESC_INPORT* | bool | GV in port. |
| *DESC_OUTPORT* | bool | GV out port. |
| *DESC_STATICPORT* | bool | GV static port. |
| *DESC_NEEDCONNECTION* | bool | GV needs connection. |
| *DESC_MULTIPLE* | bool | GV multiple ports allowed. |
| *DESC_PORTONLY* | bool | GV port only. |
| *DESC_CREATEPORT* | bool | GV create port. |
| *DESC_PORTSMIN* | int | GV minimum number of ports. |
| *DESC_PORTSMAX* | int | GV maximum number of ports. |
| *DESC_NOTMOVABLE* | bool | GV not movable. |
| *DESC_EDITPORT* | bool | GV editable. |
| *DESC_ITERATOR* | bool | GV iterator port. |
| *DESC_PARENTMSG* | int | Used in the Material Editor on the boolean tabs to specify which section to open. |
| *DESC_MATEDNOTEXT* | bool | No text in Material Editor window. |
| *DESC_COLUMNSMATED* | int | Number of columns in left Material Editor window. |
| *DESC_SHADERLINKFLAG* | bool | Specifies that the parameter is a shader link. Only if data type is *DTYPE_BASELISTLINK*. |
| *DESC_NOGUISWITCH* | bool | Disables GUI switching for this description element. |
| *DESC_COLORALWAYSLINEAR* | bool | Treats color field always as linear input. |
| *DESC_HIDE_WHEN_INLINE* | bool | **True** to hide this attribute in inline descriptions. |
| *DESC_MATERIALEDITOR_LEFTSIDE* | bool | **True** if the property should appear on the left side of the material editor. |
| *DESC_CHANGED* | bool | **True** if entry is changed. |
| *DESC_HIDEINFIELDS* | bool | **True** if group is visible in fields UI. |
| *DESC_SHOWINFIELDS* | bool | **True** if group is shown in fields UI even though group may be hidden. |
| *DESC_FIELDCOLORCHANNEL* | bool | **True** if the group belongs only to the color channel in the fields list (so will be hidden when the channel is disabled in the UI). |
| *DESC_FIELDDIRECTIONCHANNEL* | bool | **True** if the group belongs only to the direction channel in the fields list (so will be hidden when the channel is disabled in the UI). |
| *DESC_FIELDVALUECHANNEL* | bool | **True** if the group belongs only to the value channel in the fields list (so will be hidden when the channel is disabled in the UI). |
| *DESC_FIELDROTATIONCHANNEL* | bool | **True** if the group belongs only to the rotation channel in the fields list (so will be hidden when the channel is disabled in the UI). |
| *DESC_NODEPORT* | bool | **True** to indicate a nodeport. |
| *DESC_REPLACECOMPLEXUI* | bool | [`c4d.BaseContainer`](../BaseContainer/index.md#c4d.BaseContainer) filled with descids of props to replace. |
| *DESC_REPLACE_HIDE* | bool | **True** if the property is hidden because it’s remplaced by a complex ui. |
| *DESC_RESOURCEPATH* | bool | *New in version R20:* Private. |
| *DESC_RESOURCELINE* | bool | *New in version R20:* Private. |
| *DESC_TEMPDESCID* | [`c4d.DescID`](../DescID/index.md#c4d.DescID) | Internal. Used internally to store the preferred description ID. |
| *DESC_IDENT* | str | Resource identifier, e.g. ‘ID_BASEOBJECT_REL_POSITION’. |
| *DESC_IDENT_ORIGIN* | str | Origin Resource identifier, e.g. ‘ID_BASEOBJECT_REL_POSITION’. |
| *DESC_DISABLELAYOUTSWITCH* | bool | Hides the Layout Switch arrow displayed on CUSTOMGUI elements. |
| *DESC_UNIMPORTANTFORDEFAULTS* | bool | Ignore this parameter when comparing defaults. |

## Overview <a id="overview"></a>

**Lookup Operations**

- [`Description.CheckDescID()`](#c4d.Description.CheckDescID): Checks if a description ID *searchid* exists for the given objects *ops*.
- [`Description.GetParameter()`](#c4d.Description.GetParameter): Retrieves the information container for a parameter.
- [`Description.GetParameterI()`](#c4d.Description.GetParameterI): Retrieves the information container instance for a parameter.
- [`Description.GetSingleDescID()`](#c4d.Description.GetSingleDescID): Retrieves the single description ID.
- [`Description.GetSubDescriptionWithData()`](#c4d.Description.GetSubDescriptionWithData): Retrieves dynamic sub-description data (e.g.
- [`Description.LoadDescription()`](#c4d.Description.LoadDescription): Loads a description by name or ID.

**Magic Methods**

- [`Description.__init__()`](#c4d.Description.__init__): Initializes any empty description.
- [`Description.__iter__()`](#c4d.Description.__iter__): Iterate over the parameters of an object’s description.

**Parameter Controls**

- [`Description.CreatePopupMenu()`](#c4d.Description.CreatePopupMenu): Builds a popup menu for choosing a parameter in the description.
- [`Description.SetParameter()`](#c4d.Description.SetParameter): Inserts a description parameter into the collection.

## Members <a id="members"></a>

### Lookup Operations <a id="c4d.Description-method-Lookup-Operations"></a>

#### `Description.CheckDescID(self, searchid, ops)` <a id="c4d.Description.CheckDescID"></a>

Checks if a description ID *searchid* exists for the given objects *ops*.

> **Note:** usually only one single object is passed as otherwise the smallest common nominator is returned.

*New in version R18.011.*

**Parameters:**

- **searchid** ([*c4d.DescID*](../DescID/index.md#c4d.DescID)) – The partial ID.
- **ops** (*Optional*[*List*[[*c4d.C4DAtom*](../C4DAtom/index.md#c4d.C4DAtom)]]) – A list of atom objects for dynamic descriptions. Usually **None**.

**Return type:** [c4d.DescID](../DescID/index.md#c4d.DescID)

**Returns:** The complete ID.

#### `Description.GetParameter(self, id, ar=None)` <a id="c4d.Description.GetParameter"></a>

Retrieves the information container for a parameter.

*New in version R18.011.*

**Parameters:**

- **id** ([*c4d.DescID*](../DescID/index.md#c4d.DescID)) – The description ID.

- **ar** (*Optional*[*List*[[*c4d.C4DAtom*](../C4DAtom/index.md#c4d.C4DAtom)]]) –

  *New in version R18.039.*

  Optional array for dynamic descriptions, e.g. sub-descriptions of a gradient or dynamic XPresso node, that need an array of elements the parameter is assigned to.

**Return type:** [c4d.BaseContainer](../BaseContainer/index.md#c4d.BaseContainer)

**Returns:**

The information container.

*Changed in version R18.057.*

Returns only one information container.

#### `Description.GetParameterI(self, id, ar=None)` <a id="c4d.Description.GetParameterI"></a>

Retrieves the information container instance for a parameter.

*New in version R18.011.*

**Parameters:**

- **id** ([*c4d.DescID*](../DescID/index.md#c4d.DescID)) – The description ID.
- **ar** (*Optional*[*List*[[*c4d.C4DAtom*](../C4DAtom/index.md#c4d.C4DAtom)]]) – Optional array for dynamic descriptions, e.g. sub-descriptions of a gradient or dynamic XPresso node, that need an array of elements the parameter is assigned to.

**Return type:** Optional[[c4d.BaseContainer](../BaseContainer/index.md#c4d.BaseContainer)]

**Returns:** The information container instance or **None**.

#### `Description.GetSingleDescID(self)` <a id="c4d.Description.GetSingleDescID"></a>

Retrieves the single description ID.

*New in version R18.011.*

**Return type:** [c4d.DescID](../DescID/index.md#c4d.DescID)

**Returns:** The single description ID.

#### `Description.GetSubDescriptionWithData(self, did, op, bc, singledescid)` <a id="c4d.Description.GetSubDescriptionWithData"></a>

Retrieves dynamic sub-description data (e.g. the gradient data type).

*New in version R18.011.*

**Parameters:**

- **did** ([*c4d.DescID*](../DescID/index.md#c4d.DescID)) – The description ID.
- **op** (*List*[[*c4d.C4DAtom*](../C4DAtom/index.md#c4d.C4DAtom)]) – A list of atom objects.
- **bc** ([*c4d.BaseContainer*](../BaseContainer/index.md#c4d.BaseContainer)) – The existing container for the data type. Can be just [`c4d.BaseContainer()`](../BaseContainer/index.md#c4d.BaseContainer).
- **singledescid** (*Optional*[[*c4d.DescID*](../DescID/index.md#c4d.DescID)]) – Should be **None**.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `Description.LoadDescription(self, id)` <a id="c4d.Description.LoadDescription"></a>

Loads a description by name or ID.

*New in version R18.011.*

> **Warning:** Existing description parameters are lost.

**Parameters:** **id** (*Union*[*int*, *str*]) – The description name (e.g. “Obase”) or ID (e.g. *c4d.Obase*).

**Return type:** bool

**Returns:** **True** if the description was loaded, otherwise **False**.

### Magic Methods <a id="c4d.Description-method-Magic-Methods"></a>

#### `Description.__init__(self)` <a id="c4d.Description.__init__"></a>

Initializes any empty description.

**Example:**

```python
import c4d

description: c4d.Description = c4d.Description()
if not description.LoadDescription(c4d.Ocube):
    raise RuntimeError("Failed to load description for cube object.")

for bc, paramid, groupid in description:
    print(bc[c4d.DESC_NAME])
```

#### `Description.__iter__(self, bc, id, groupid)` <a id="c4d.Description.__iter__"></a>

Iterate over the parameters of an object’s description.

**Parameters:**

- **bc** ([*c4d.BaseContainer*](../BaseContainer/index.md#c4d.BaseContainer)) – The container that holds the information for the current description parameter.
- **id** ([*c4d.DescID*](../DescID/index.md#c4d.DescID)) – The ID of the current description parameter.
- **groupid** ([*c4d.DescID*](../DescID/index.md#c4d.DescID)) – The group ID of the current description parameter.

Here is how to print the name of all the parameters of an object

```python
import c4d

def main():
        if op is None:
            return

        description = op.GetDescription(c4d.DESCFLAGS_DESC_NONE)    # Get the description of the active object
        for bc, paramid, groupid in description:                    # Iterate over the parameters of the description
            print(bc[c4d.DESC_NAME])                                # Print the current parameter name

if __name__=='__main__':
        main()
```

### Parameter Controls <a id="c4d.Description-method-Parameter-Controls"></a>

#### `Description.CreatePopupMenu(self)` <a id="c4d.Description.CreatePopupMenu"></a>

Builds a popup menu for choosing a parameter in the description.

*New in version R18.011.*

**Return type:** [c4d.BaseContainer](../BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The menu container.

#### `Description.SetParameter(self, id, param, groupid)` <a id="c4d.Description.SetParameter"></a>

Inserts a description parameter into the collection.

*New in version R18.011.*

**Parameters:**

- **id** ([*c4d.DescID*](../DescID/index.md#c4d.DescID)) – The description ID.
- **param** ([*c4d.BaseContainer*](../BaseContainer/index.md#c4d.BaseContainer)) – The settings for the new parameter.
- **groupid** ([*c4d.DescID*](../DescID/index.md#c4d.DescID)) – The ID of the parameter’s group, or [`c4d.DESCID_ROOT`](../DescID/index.md#c4d.DESCID_ROOT).

**Return type:** bool

**Returns:** **True** if the parameter was inserted, otherwise **False**.
