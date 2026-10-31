<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/MSG_CORE_EVMSG.html -->

# Core and Event Messages <a id="core-and-event-messages"></a>

The following core and event message identifiers are can be broadcasted or received. See [Message System](../manuals/manual_message_system.md#manual-message-system) for details on the message system of Cinema 4D.

<a id="msg-core-core"></a>The following messages can be broadcasted with [`c4d.SendCoreMessage()`](../modules/c4d/index.md#c4d.SendCoreMessage).

| Symbol | Numeric Value | Description |
|---|---|---|
| [c4d.COREMSG_CINEMA_EXECUTEEDITORCOMMAND](#coremsg-cinema-executeeditorcommand) | 200000023 | Executes the command with ID specified by `COREMSG_CINEMA_EXECUTEEDITORCOMMAND` in `msg`. |
| [c4d.COREMSG_CINEMA_EXECUTEOPTIONMODE](#coremsg-cinema-executeoptionmode) | 300001037 | Pass whether to open the option dialog or not for `COREMSG_CINEMA_EXECUTEEDITORCOMMAND`. |
| [c4d.COREMSG_CINEMA_EXECUTESUBID](#coremsg-cinema-executesubid) | 300001036 | Pass the sub-ID for `COREMSG_CINEMA_EXECUTEEDITORCOMMAND`. |
| [c4d.COREMSG_CINEMA_FORCE_AM_UPDATE](#coremsg-cinema-force-am-update) | 1001077 | Forces an Attribute Manager update. |
| [c4d.COREMSG_CINEMA_GETCOMMANDCHECKED](#coremsg-cinema-getcommandchecked) | 300000115 | Checks if the command with ID specified by `COREMSG_CINEMA_GETCOMMANDCHECKED` in `msg` is checked or not. |
| [c4d.COREMSG_CINEMA_GETCOMMANDENABLED](#coremsg-cinema-getcommandenabled) | 200000035 | Checks if the command with ID specified by `COREMSG_CINEMA_GETCOMMANDENABLED` in `msg` is enabled or disabled. |
| [c4d.COREMSG_CINEMA_GETCOMMANDHELP](#coremsg-cinema-getcommandhelp) | 200000234 | Gets the help string of a command. Pass the command’s ID. |
| [c4d.COREMSG_CINEMA_GETCOMMANDNAME](#coremsg-cinema-getcommandname) | 200000033 | Returns the name of the command with ID specified by `COREMSG_CINEMA_GETCOMMANDNAME` in `msg`. |
| [c4d.COREMSG_CINEMA_GETMACHINEFEATURES](#coremsg-cinema-getmachinefeatures) | 1733248844 | Retrieves machine features. Returned container IDs see [MACHINEINFO](MACHINEINFO.md) and [Viewport](VP_PREVIEWHARDWARE.md). |
| [c4d.COREMSG_UPDATECOMMANDSMESSAGE](#coremsg-updatecommandsmessage) | 200000100 | *Private* |

<a id="msg-core-event"></a>Event messages can be broadcasted with [`c4d.GeSyncMessage()`](../modules/c4d/index.md#c4d.GeSyncMessage) and received in the `CoreMessage` methods of [`c4d.gui.GeDialog`](../modules/c4d.gui/GeDialog/index.md#c4d.gui.GeDialog), [`c4d.gui.GeUserArea`](../modules/c4d.gui/GeUserArea/index.md#c4d.gui.GeUserArea) and [`c4d.plugins.MessageData`](../modules/c4d.plugins/BaseData/MessageData/index.md#c4d.plugins.MessageData).

| Symbol | Numeric Value | Description |
|---|---|---|
| [c4d.EVMSG_ACTIVEVIEWCHANGED](#evmsg-activeviewchanged) | 1633908343 | *Private* |
| [c4d.EVMSG_ASYNCEDITORMOVE](#evmsg-asynceditormove) | 1701080438 | The user moved something in the editor window. |
| [c4d.EVMSG_AUTKEYMODECHANGED](#evmsg-autkeymodechanged) | 200000009 | The autokey mode was changed. |
| [c4d.EVMSG_BROWSERCHANGE](#evmsg-browserchange) | -1002 | Something in the browser has been changed (local event). |
| [c4d.EVMSG_CHANGE](#evmsg-change) | 604 | Sent by [`EventAdd()`](../modules/c4d/index.md#c4d.EventAdd). |
| [c4d.EVMSG_DOCUMENTRECALCULATED](#evmsg-documentrecalculated) | 1685218156 | Sent while drawing after the animation, expressions and cache building have been done. |
| [c4d.EVMSG_FCURVECHANGE](#evmsg-fcurvechange) | -1010 | Something in the F-Curve manager has been changed (local event). |
| [c4d.EVMSG_GRAPHVIEWCHANGED](#evmsg-graphviewchanged) | 400008000 | Something in XPresso has been changed (local event). |
| [c4d.EVMSG_MATERIALPREVIEW](#evmsg-materialpreview) | -1008 | *Private* |
| [c4d.EVMSG_MATERIALSELECTION](#evmsg-materialselection) | -1009 | A material selection has been changed (local event). |
| [c4d.EVMSG_RAYTRACER_FINISHED](#evmsg-raytracer-finished) | -1003 | *Private* |
| [c4d.EVMSG_SETMODE](#evmsg-setmode) | 1055256 | *Private* |
| [c4d.EVMSG_SHOWIN_FC](#evmsg-showin-fc) | -200000076 | Show in Function Curve editor. |
| [c4d.EVMSG_SHOWIN_LM](#evmsg-showin-lm) | -200000077 | Show in Layer Manager. |
| [c4d.EVMSG_SHOWIN_MT](#evmsg-showin-mt) | -200000078 | Show in Motion editor. |
| [c4d.EVMSG_SHOWIN_SB](#evmsg-showin-sb) | -200000074 | Show in Scene Browser. |
| [c4d.EVMSG_SHOWIN_TL](#evmsg-showin-tl) | -200000075 | Show in Timeline. |
| [c4d.EVMSG_TAKECHANGED](#evmsg-takechanged) | 431000159 | Sent by the Take System when the current Take ID changed to let all managers react to the new status. |
| [c4d.EVMSG_TIMECHANGED](#evmsg-timechanged) | 1952671847 | *Private* |
| [c4d.EVMSG_TIMELINESELECTION](#evmsg-timelineselection) | -1001 | A timeline selection has been changed (local event). |
| [c4d.EVMSG_TL_FCURVE_POS](#evmsg-tl-fcurve-pos) | -200000079 | Show and frame fcurve position tracks. |
| [c4d.EVMSG_TL_FCURVE_ROT](#evmsg-tl-fcurve-rot) | -200000080 | Show and frame fcurve rotation tracks. |
| [c4d.EVMSG_TL_FCURVE_SCALE](#evmsg-tl-fcurve-scale) | -200000081 | Show and frame fcurve scale tracks. |
| [c4d.EVMSG_TLOM_MERGE](#evmsg-tlom-merge) | -465001000 | *Private* |
| [c4d.EVMSG_TOOLCHANGED](#evmsg-toolchanged) | -826267 | A tool setting has changed (local event). |
| [c4d.EVMSG_UPDATEBASEDRAW](#evmsg-updatebasedraw) | 200000099 | Sent in the case that the view should be redrawn. |
| [c4d.EVMSG_UPDATEHIGHLIGHT](#evmsg-updatehighlight) | 200000073 | A special message sent by Cinema 4D in the case that only the highlighting changes. |
| [c4d.EVMSG_UPDATESCHEME](#evmsg-updatescheme) | 200000010 | Scheme has been updated. |
| [c4d.EVMSG_VIEWWINDOW_3DPAINTUPD](#evmsg-viewwindow-3dpaintupd) | -1012 | *Private* |
| [c4d.EVMSG_VIEWWINDOW_OUTPUT](#evmsg-viewwindow-output) | -1011 | *Private* |

## `c4d.COREMSG_CINEMA_EXECUTEEDITORCOMMAND` <a id="c4d.COREMSG_CINEMA_EXECUTEEDITORCOMMAND"></a> <a id="coremsg-cinema-executeeditorcommand"></a>

Executes the command with ID specified by `COREMSG_CINEMA_EXECUTEEDITORCOMMAND` in `msg`.

## `c4d.COREMSG_CINEMA_EXECUTEOPTIONMODE` <a id="c4d.COREMSG_CINEMA_EXECUTEOPTIONMODE"></a> <a id="coremsg-cinema-executeoptionmode"></a>

Pass whether to open the option dialog or not for `COREMSG_CINEMA_EXECUTEEDITORCOMMAND`.

## `c4d.COREMSG_CINEMA_EXECUTESUBID` <a id="c4d.COREMSG_CINEMA_EXECUTESUBID"></a> <a id="coremsg-cinema-executesubid"></a>

Pass the sub-ID for `COREMSG_CINEMA_EXECUTEEDITORCOMMAND`.

## `c4d.COREMSG_CINEMA_FORCE_AM_UPDATE` <a id="c4d.COREMSG_CINEMA_FORCE_AM_UPDATE"></a> <a id="coremsg-cinema-force-am-update"></a>

Forces an Attribute Manager update.

## `c4d.COREMSG_CINEMA_GETCOMMANDCHECKED` <a id="c4d.COREMSG_CINEMA_GETCOMMANDCHECKED"></a> <a id="coremsg-cinema-getcommandchecked"></a>

Checks if the command with ID specified by `COREMSG_CINEMA_GETCOMMANDCHECKED` in `msg` is checked or not.  
The state is given as `True` or `False`.

## `c4d.COREMSG_CINEMA_GETCOMMANDENABLED` <a id="c4d.COREMSG_CINEMA_GETCOMMANDENABLED"></a> <a id="coremsg-cinema-getcommandenabled"></a>

Checks if the command with ID specified by `COREMSG_CINEMA_GETCOMMANDENABLED` in `msg` is enabled or disabled.  
The state is returned as `True` or `False`.

## `c4d.COREMSG_CINEMA_GETCOMMANDHELP` <a id="c4d.COREMSG_CINEMA_GETCOMMANDHELP"></a> <a id="coremsg-cinema-getcommandhelp"></a>

Gets the help string of a command. Pass the command’s ID.  
The help is returned as string.

## `c4d.COREMSG_CINEMA_GETCOMMANDNAME` <a id="c4d.COREMSG_CINEMA_GETCOMMANDNAME"></a> <a id="coremsg-cinema-getcommandname"></a>

Returns the name of the command with ID specified by `COREMSG_CINEMA_GETCOMMANDNAME` in `msg`.  
The name is returned as a string.

## `c4d.COREMSG_CINEMA_GETMACHINEFEATURES` <a id="c4d.COREMSG_CINEMA_GETMACHINEFEATURES"></a> <a id="coremsg-cinema-getmachinefeatures"></a>

Retrieves machine features. Returned container IDs see [MACHINEINFO](MACHINEINFO.md) and [Viewport](VP_PREVIEWHARDWARE.md).

## `c4d.COREMSG_UPDATECOMMANDSMESSAGE` <a id="c4d.COREMSG_UPDATECOMMANDSMESSAGE"></a> <a id="coremsg-updatecommandsmessage"></a>

*Private*

## `c4d.EVMSG_ACTIVEVIEWCHANGED` <a id="c4d.EVMSG_ACTIVEVIEWCHANGED"></a> <a id="evmsg-activeviewchanged"></a>

*Private*

## `c4d.EVMSG_ASYNCEDITORMOVE` <a id="c4d.EVMSG_ASYNCEDITORMOVE"></a> <a id="evmsg-asynceditormove"></a>

The user moved something in the editor window.  
Managers should update things like position fields.

## `c4d.EVMSG_AUTKEYMODECHANGED` <a id="c4d.EVMSG_AUTKEYMODECHANGED"></a> <a id="evmsg-autkeymodechanged"></a>

The autokey mode was changed.

## `c4d.EVMSG_BROWSERCHANGE` <a id="c4d.EVMSG_BROWSERCHANGE"></a> <a id="evmsg-browserchange"></a>

Something in the browser has been changed (local event).

## `c4d.EVMSG_CHANGE` <a id="c4d.EVMSG_CHANGE"></a> <a id="evmsg-change"></a>

Sent by [`EventAdd()`](../modules/c4d/index.md#c4d.EventAdd).

## `c4d.EVMSG_DOCUMENTRECALCULATED` <a id="c4d.EVMSG_DOCUMENTRECALCULATED"></a> <a id="evmsg-documentrecalculated"></a>

Sent while drawing after the animation, expressions and cache building have been done.  
It allows that certain managers (e.g. attribute manager) update their values to the changes done by the expressions etc. Any reactions on this message should be pretty fast! No modifying stuff must be done here as the draw thread is running at the same time and accesses the same data!

## `c4d.EVMSG_FCURVECHANGE` <a id="c4d.EVMSG_FCURVECHANGE"></a> <a id="evmsg-fcurvechange"></a>

Something in the F-Curve manager has been changed (local event).

## `c4d.EVMSG_GRAPHVIEWCHANGED` <a id="c4d.EVMSG_GRAPHVIEWCHANGED"></a> <a id="evmsg-graphviewchanged"></a>

Something in XPresso has been changed (local event).

## `c4d.EVMSG_MATERIALPREVIEW` <a id="c4d.EVMSG_MATERIALPREVIEW"></a> <a id="evmsg-materialpreview"></a>

*Private*

## `c4d.EVMSG_MATERIALSELECTION` <a id="c4d.EVMSG_MATERIALSELECTION"></a> <a id="evmsg-materialselection"></a>

A material selection has been changed (local event).

## `c4d.EVMSG_RAYTRACER_FINISHED` <a id="c4d.EVMSG_RAYTRACER_FINISHED"></a> <a id="evmsg-raytracer-finished"></a>

*Private*

## `c4d.EVMSG_SETMODE` <a id="c4d.EVMSG_SETMODE"></a> <a id="evmsg-setmode"></a>

*Private*

## `c4d.EVMSG_SHOWIN_FC` <a id="c4d.EVMSG_SHOWIN_FC"></a> <a id="evmsg-showin-fc"></a>

Show in Function Curve editor.

## `c4d.EVMSG_SHOWIN_LM` <a id="c4d.EVMSG_SHOWIN_LM"></a> <a id="evmsg-showin-lm"></a>

Show in Layer Manager.

## `c4d.EVMSG_SHOWIN_MT` <a id="c4d.EVMSG_SHOWIN_MT"></a> <a id="evmsg-showin-mt"></a>

Show in Motion editor.

## `c4d.EVMSG_SHOWIN_SB` <a id="c4d.EVMSG_SHOWIN_SB"></a> <a id="evmsg-showin-sb"></a>

Show in Scene Browser.

## `c4d.EVMSG_SHOWIN_TL` <a id="c4d.EVMSG_SHOWIN_TL"></a> <a id="evmsg-showin-tl"></a>

Show in Timeline.

## `c4d.EVMSG_TAKECHANGED` <a id="c4d.EVMSG_TAKECHANGED"></a> <a id="evmsg-takechanged"></a>

**Sent by the Take System when the current Take ID changed to let all managers react to the new status.** *New in version R17.032.*

## `c4d.EVMSG_TIMECHANGED` <a id="c4d.EVMSG_TIMECHANGED"></a> <a id="evmsg-timechanged"></a>

*Private*

## `c4d.EVMSG_TIMELINESELECTION` <a id="c4d.EVMSG_TIMELINESELECTION"></a> <a id="evmsg-timelineselection"></a>

A timeline selection has been changed (local event).

## `c4d.EVMSG_TL_FCURVE_POS` <a id="c4d.EVMSG_TL_FCURVE_POS"></a> <a id="evmsg-tl-fcurve-pos"></a>

Show and frame fcurve position tracks.

## `c4d.EVMSG_TL_FCURVE_ROT` <a id="c4d.EVMSG_TL_FCURVE_ROT"></a> <a id="evmsg-tl-fcurve-rot"></a>

Show and frame fcurve rotation tracks.

## `c4d.EVMSG_TL_FCURVE_SCALE` <a id="c4d.EVMSG_TL_FCURVE_SCALE"></a> <a id="evmsg-tl-fcurve-scale"></a>

Show and frame fcurve scale tracks.

## `c4d.EVMSG_TLOM_MERGE` <a id="c4d.EVMSG_TLOM_MERGE"></a> <a id="evmsg-tlom-merge"></a>

*Private*

## `c4d.EVMSG_TOOLCHANGED` <a id="c4d.EVMSG_TOOLCHANGED"></a> <a id="evmsg-toolchanged"></a>

A tool setting has changed (local event).

## `c4d.EVMSG_UPDATEBASEDRAW` <a id="c4d.EVMSG_UPDATEBASEDRAW"></a> <a id="evmsg-updatebasedraw"></a>

Sent in the case that the view should be redrawn.

## `c4d.EVMSG_UPDATEHIGHLIGHT` <a id="c4d.EVMSG_UPDATEHIGHLIGHT"></a> <a id="evmsg-updatehighlight"></a>

A special message sent by Cinema 4D in the case that only the highlighting changes.  
This happens for example when the mouse is moved over the viewport. Plugins usually do not need to care about this.

## `c4d.EVMSG_UPDATESCHEME` <a id="c4d.EVMSG_UPDATESCHEME"></a> <a id="evmsg-updatescheme"></a>

Scheme has been updated.

## `c4d.EVMSG_VIEWWINDOW_3DPAINTUPD` <a id="c4d.EVMSG_VIEWWINDOW_3DPAINTUPD"></a> <a id="evmsg-viewwindow-3dpaintupd"></a>

*Private*

## `c4d.EVMSG_VIEWWINDOW_OUTPUT` <a id="c4d.EVMSG_VIEWWINDOW_OUTPUT"></a> <a id="evmsg-viewwindow-output"></a>

*Private*
