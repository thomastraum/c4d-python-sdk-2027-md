<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/manuals/manual_message_system.html -->

# Message System <a id="message-system"></a><a id="manual-message-system"></a>

Explains messages between Cinema 4D scene elements and interfaces.

## Overview <a id="overview"></a>

Messages are a core principal of the Cinema API of Cinema 4D and fulfill an event-like purpose. Various interfaces in the Cinema API have methods attached to them which are linked to the message system. A message is always denoted by an identifier, e.g., [MSG_DESCRIPTION_EDIT_ENTRY](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-edit-entry), which does signify the message event to the object it is being send to. Messages can also be accompanied by ingoing or outgoing message data which does qualify that event. This message data can consist out of multiple elements and is usually wrapped as a dictionary in the Python API.

The message data that is related to a message can be treated in an in- or outgoing fashion or both. The message [MSG_DESCRIPTION_EDIT_ENTRY](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-edit-entry) will be broadcasted with a dictionary containing the [`DescID`](../modules/c4d/DescID/index.md#c4d.DescID) for the element which did raise that message. Attempting to modify this [`DescID`](../modules/c4d/DescID/index.md#c4d.DescID) or returning modified message data will have no effect on the [`DescID`](../modules/c4d/DescID/index.md#c4d.DescID) of the raising element, the data is only ingoing. Other message events will however explicitly being sent with the intent that the recipient does modify or complement the data. [MSG_GETCUSTOMICON](../consts/MSG_C4DATOM_PLUGINS.md#msg-getcustomicon) for example is being sent so that a `NodeData.Message()` instance can return a specific icon for the associated node with the returned message data.

## Technical Overview <a id="technical-overview"></a>

There are three major categories of messages in Cinema 4D: Core messages, messages to scene elements, and messages to dialogs and custom interface elements. Message to [`C4DAtom`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom) instances, e.g., objects, tags, or other scene elements, are being sent with `C4DAtom.Message()`. When the message identifier sent to an atom is being supported by the atom type and the message data is well formed, then the message will invoke a certain action in the atom as documented by the message symbols below. Sending [MSG_UPDATE](../consts/MSG_C4DATOM_PLUGINS.md#msg-update) to a [`PointObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/index.md#c4d.PointObject) will for example force a point object to update all its internal data that does rely on the vertices of the point object. The handling of messages sent to [`C4DAtom`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom) instances plays a fundamental role when implementing plugin interfaces, e.g., `c4d.ObjectData`, `c4d.TagData` or `c4d.ShaderData`. Listening for [MSG_DESCRIPTION_COMMAND](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-command) in the `Message` method of an `ObjectData` interface will allow for example to react on button clicks in the description interface of the corresponding [`BaseObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.md#c4d.BaseObject) instances of that type.

Core messages are a message category that is related to global system wide events; as opposed to the messages sent to [`C4DAtom`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom) instances which only affect a single atom. Core messages can be invoked among other functions with [`c4d.SendCoreMessage()`](../modules/c4d/index.md#c4d.SendCoreMessage) and [`c4d.GeSyncMessage()`](../modules/c4d/index.md#c4d.GeSyncMessage) and received with [`MessageData`](../modules/c4d.plugins/BaseData/MessageData/index.md#c4d.plugins.MessageData), [`GeDialog`](../modules/c4d.gui/GeDialog/index.md#c4d.gui.GeDialog) and [`GeUserArea`](../modules/c4d.gui/GeUserArea/index.md#c4d.gui.GeUserArea) instances by overwriting their `CoreMessage` methods. Core messages convey broad events as for example enforcing redraw event or reacting on the modification of the active document.

A third category of messages is received by [`GeDialog`](../modules/c4d.gui/GeDialog/index.md#c4d.gui.GeDialog) and [`GeUserArea`](../modules/c4d.gui/GeUserArea/index.md#c4d.gui.GeUserArea) instances in their `Message` methods. The messages received here differ from those broadcasted to the `Message` methods of [`C4DAtom`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom) instances. These messages only rarely have to be sent by users and instead are primarily intended to react to events in the respective user interface, e.g., a mouse or key press event. These messages also do play an important role in the execution of the event loop of such GUI elements, e.g., sending [BFM_DRAW](../consts/MSG_GUI.md#bfm-draw) to a [`GeUserArea`](../modules/c4d.gui/GeUserArea/index.md#c4d.gui.GeUserArea) instance will cause its `GeUserArea.DrawMsg()` being called.

## Message Contexts <a id="message-contexts"></a>

### C4DAtom Messages <a id="c4datom-messages"></a><a id="msg-c4datom"></a>

The following messages can be broadcasted to [`C4DAtom`](../modules/c4d/C4DAtom/index.md#c4d.C4DAtom) instances with the method `C4DAtom.Message()`.

| Symbol | Numeric Value | Description |
|---|---|---|
| [c4d.MSG_ANIMATE](../consts/MSG_C4DATOM_PLUGINS.md#msg-animate) | 300001037 | Sent to objects after they have been animated. |
| [c4d.MSG_BASECONTAINER](../consts/MSG_C4DATOM_PLUGINS.md#msg-basecontainer) | 9 | Sent to pass arbitrary data in a container to a node. |
| [c4d.MSG_CHANGE](../consts/MSG_C4DATOM_PLUGINS.md#msg-change) | 7 | Sent if any data except for the matrix has been changed. |
| [c4d.MSG_COLLECTC4DFALLOFF](../consts/MSG_C4DATOM_PLUGINS.md#msg-collectc4dfalloff) | 440000221 | Sent to atoms that might contain a falloff. |
| [c4d.MSG_COMMANDINFORMATION](../consts/MSG_C4DATOM_PLUGINS.md#msg-commandinformation) | 300001001 | Sent to retrieve command information. |
| [c4d.MSG_DESCRIPTION_ALLOWOVERRIDE](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-allowoverride) | 431000094 | Sent to check if take override operation is allowed. |
| [c4d.MSG_DESCRIPTION_CHECKDRAGANDDROP](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-checkdraganddrop) | 26 | Sent to ask an atom if a drag and drop operation is accepted. |
| [c4d.MSG_DESCRIPTION_CHECKUPDATE](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-checkupdate) | 17 | Sent to allow elements to determine the type of refresh after a parameter has been changed. |
| [c4d.MSG_DESCRIPTION_COMMAND](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-command) | 18 | Sent for button description elements. |
| [c4d.MSG_DESCRIPTION_CUSTOMGUI_NOTIFICATION](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-customgui-notification) | 431000175 | Sent by a custom GUI to its parent node. |
| [c4d.MSG_DESCRIPTION_EDIT_ENTRY](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-edit-entry) | 25 | Sent to tell an atom to edit a description entry. |
| [c4d.MSG_DESCRIPTION_GETBITMAP](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-getbitmap) | 27 | Sent to query a description for a [`c4d.gui.BitmapButtonCustomGui`](../modules/c4d.gui/BaseCustomGui/BitmapButtonCustomGui/index.md#c4d.gui.BitmapButtonCustomGui) bitmap. |
| [c4d.MSG_DESCRIPTION_POPUP](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-popup) | 300001046 | Sent to handle description popup menus in the Attribute Manager. |
| [c4d.MSG_DESCRIPTION_POSTSETPARAMETER](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-postsetparameter) | 19 | Sent after a `C4DAtom.SetParameter()` call. |
| [c4d.MSG_DESCRIPTION_REMOVE_ENTRY](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-remove-entry) | 24 | Sent to tell an atom to remove a description entry. |
| [c4d.MSG_DESCRIPTION_VALIDATE](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-validate) | 20 | Sent to update dependencies or to check for invalid values after a parameter change. |
| [c4d.MSG_DOCUMENT_MODE_CHANGED](../consts/MSG_C4DATOM_PLUGINS.md#msg-document-mode-changed) | 200000091 | Sent to the active tool plugin when document mode is changed. |
| [c4d.MSG_DOCUMENTINFO](../consts/MSG_C4DATOM_PLUGINS.md#msg-documentinfo) | 1001078 | Sent when a document has been loaded, saved, merged or other document related actions occurred. |
| [c4d.MSG_DRAGANDDROP](../consts/MSG_C4DATOM_PLUGINS.md#msg-draganddrop) | 1018756 | Sent to elements in the Object Manager when something is dropped on it. |
| [c4d.MSG_EDIT](../consts/MSG_C4DATOM_PLUGINS.md#msg-edit) | 21 | Sent to perform an action when element is being edited. |
| [c4d.MSG_FILTER](../consts/MSG_C4DATOM_PLUGINS.md#msg-filter) | 14 | Sent to allow or block `C4DAtom.MultiMessage()` calls. |
| [c4d.MSG_GET_MODATASELECTION](../consts/MSG_C4DATOM_PLUGINS.md#msg-get-modataselection) | 1021339 | Sent to retrieve the data of MoGraph selection tags. |
| [c4d.MSG_GET_MODATAWEIGHTS](../consts/MSG_C4DATOM_PLUGINS.md#msg-get-modataweights) | 440000230 | Sent to retrieve the data for MoGraph weights tags. |
| [c4d.MSG_GETALLASSETS](../consts/MSG_C4DATOM_PLUGINS.md#msg-getallassets) | 112004 | Sent to retrieve all assets from an object. |
| [c4d.MSG_GETCUSTOMICON](../consts/MSG_C4DATOM_PLUGINS.md#msg-getcustomicon) | 1001090 | Sent to retrieve a custom icon. |
| [c4d.MSG_GETCUSTOMICON_SETTINGS](../consts/MSG_C4DATOM_PLUGINS.md#msg-getcustomicon-settings) | 1041699 | Sent to retrieve the custom icon settings of an object. |
| [c4d.MSG_GETREALCAMERADATA](../consts/MSG_C4DATOM_PLUGINS.md#msg-getrealcameradata) | 1028476 | Sent to get a real camera object from a generator. |
| [c4d.MSG_GETREALTAGDATA](../consts/MSG_C4DATOM_PLUGINS.md#msg-getrealtagdata) | 1036447 | Sent to get the real tag object from a virtual ‘generator’ tag. |
| [c4d.MSG_MENUPREPARE](../consts/MSG_C4DATOM_PLUGINS.md#msg-menuprepare) | 22 | Sent to allow tags, objects, shaders etc. to do some setup work when called from the menu. |
| [c4d.MSG_MULTI_CLEARSUGGESTEDFOLDER](../consts/MSG_C4DATOM_PLUGINS.md#msg-multi-clearsuggestedfolder) | 200000040 | Sent to nodes to convert absolute paths to filename. |
| [c4d.MSG_MULTI_DOCUMENTCLONED](../consts/MSG_C4DATOM_PLUGINS.md#msg-multi-documentcloned) | 11 | Sent when a document is being cloned. |
| [c4d.MSG_MULTI_RENDERNOTIFICATION](../consts/MSG_C4DATOM_PLUGINS.md#msg-multi-rendernotification) | 1001071 | Sent to a document and all of its elements before a render starts. |
| [c4d.MSG_POINTS_CHANGED](../consts/MSG_C4DATOM_PLUGINS.md#msg-points-changed) | 1 | Sent to notify an object its points have changed. |
| [c4d.MSG_POLYGONS_CHANGED](../consts/MSG_C4DATOM_PLUGINS.md#msg-polygons-changed) | 2 | Sent to notify an object its polygons have changed. |
| [c4d.MSG_RETRIEVEPRIVATEDATA](../consts/MSG_C4DATOM_PLUGINS.md#msg-retrieveprivatedata) | 23 | Sent to retrieve private data from an atom. |
| [c4d.MSG_SCALEDOCUMENT](../consts/MSG_C4DATOM_PLUGINS.md#msg-scaledocument) | 300001069 | Sent to signal that another document with different scale has been merged with the current document. |
| [c4d.MSG_SEGMENTS_CHANGED](../consts/MSG_C4DATOM_PLUGINS.md#msg-segments-changed) | 10 | Sent to notify an object that its segments have changed. |
| [c4d.MSG_SMALLUPDATE](../consts/MSG_C4DATOM_PLUGINS.md#msg-smallupdate) | 6 | Sent if part of an object has changed and does not need cache rebuilding. |
| [c4d.MSG_UPDATE](../consts/MSG_C4DATOM_PLUGINS.md#msg-update) | 5 | Sent to inform an object that its bounding box must be recalculated. Otherwise use [MSG_CHANGE](../consts/MSG_C4DATOM_PLUGINS.md#msg-change). |

### Core Messages <a id="core-messages"></a><a id="msg-core"></a>

The following messages can be broadcasted with [`c4d.SendCoreMessage()`](../modules/c4d/index.md#c4d.SendCoreMessage).

| Symbol | Numeric Value | Description |
|---|---|---|
| [c4d.COREMSG_CINEMA_EXECUTEEDITORCOMMAND](../consts/MSG_CORE_EVMSG.md#coremsg-cinema-executeeditorcommand) | 200000023 | Executes the command with ID specified by `COREMSG_CINEMA_EXECUTEEDITORCOMMAND` in `msg`. |
| [c4d.COREMSG_CINEMA_EXECUTEOPTIONMODE](../consts/MSG_CORE_EVMSG.md#coremsg-cinema-executeoptionmode) | 300001037 | Pass whether to open the option dialog or not for `COREMSG_CINEMA_EXECUTEEDITORCOMMAND`. |
| [c4d.COREMSG_CINEMA_EXECUTESUBID](../consts/MSG_CORE_EVMSG.md#coremsg-cinema-executesubid) | 300001036 | Pass the sub-ID for `COREMSG_CINEMA_EXECUTEEDITORCOMMAND`. |
| [c4d.COREMSG_CINEMA_FORCE_AM_UPDATE](../consts/MSG_CORE_EVMSG.md#coremsg-cinema-force-am-update) | 1001077 | Forces an Attribute Manager update. |
| [c4d.COREMSG_CINEMA_GETCOMMANDCHECKED](../consts/MSG_CORE_EVMSG.md#coremsg-cinema-getcommandchecked) | 300000115 | Checks if the command with ID specified by `COREMSG_CINEMA_GETCOMMANDCHECKED` in `msg` is checked or not. |
| [c4d.COREMSG_CINEMA_GETCOMMANDENABLED](../consts/MSG_CORE_EVMSG.md#coremsg-cinema-getcommandenabled) | 200000035 | Checks if the command with ID specified by `COREMSG_CINEMA_GETCOMMANDENABLED` in `msg` is enabled or disabled. |
| [c4d.COREMSG_CINEMA_GETCOMMANDHELP](../consts/MSG_CORE_EVMSG.md#coremsg-cinema-getcommandhelp) | 200000234 | Gets the help string of a command. Pass the command’s ID. |
| [c4d.COREMSG_CINEMA_GETCOMMANDNAME](../consts/MSG_CORE_EVMSG.md#coremsg-cinema-getcommandname) | 200000033 | Returns the name of the command with ID specified by `COREMSG_CINEMA_GETCOMMANDNAME` in `msg`. |
| [c4d.COREMSG_CINEMA_GETMACHINEFEATURES](../consts/MSG_CORE_EVMSG.md#coremsg-cinema-getmachinefeatures) | 1733248844 | Retrieves machine features. Returned container IDs see [MACHINEINFO](../consts/MACHINEINFO.md) and [Viewport](../consts/VP_PREVIEWHARDWARE.md). |
| [c4d.COREMSG_UPDATECOMMANDSMESSAGE](../consts/MSG_CORE_EVMSG.md#coremsg-updatecommandsmessage) | 200000100 | *Private* |

### Event Messages <a id="event-messages"></a>

The following messages can be broadcasted with [`c4d.GeSyncMessage()`](../modules/c4d/index.md#c4d.GeSyncMessage) and received in the `CoreMessage` methods in [`MessageData`](../modules/c4d.plugins/BaseData/MessageData/index.md#c4d.plugins.MessageData), [`GeDialog`](../modules/c4d.gui/GeDialog/index.md#c4d.gui.GeDialog) and [`GeUserArea`](../modules/c4d.gui/GeUserArea/index.md#c4d.gui.GeUserArea) interfaces.

| Symbol | Numeric Value | Description |
|---|---|---|
| [c4d.EVMSG_ACTIVEVIEWCHANGED](../consts/MSG_CORE_EVMSG.md#evmsg-activeviewchanged) | 1633908343 | *Private* |
| [c4d.EVMSG_ASYNCEDITORMOVE](../consts/MSG_CORE_EVMSG.md#evmsg-asynceditormove) | 1701080438 | The user moved something in the editor window. |
| [c4d.EVMSG_AUTKEYMODECHANGED](../consts/MSG_CORE_EVMSG.md#evmsg-autkeymodechanged) | 200000009 | The autokey mode was changed. |
| [c4d.EVMSG_BROWSERCHANGE](../consts/MSG_CORE_EVMSG.md#evmsg-browserchange) | -1002 | Something in the browser has been changed (local event). |
| [c4d.EVMSG_CHANGE](../consts/MSG_CORE_EVMSG.md#evmsg-change) | 604 | Sent by [`EventAdd()`](../modules/c4d/index.md#c4d.EventAdd). |
| [c4d.EVMSG_DOCUMENTRECALCULATED](../consts/MSG_CORE_EVMSG.md#evmsg-documentrecalculated) | 1685218156 | Sent while drawing after the animation, expressions and cache building have been done. |
| [c4d.EVMSG_FCURVECHANGE](../consts/MSG_CORE_EVMSG.md#evmsg-fcurvechange) | -1010 | Something in the F-Curve manager has been changed (local event). |
| [c4d.EVMSG_GRAPHVIEWCHANGED](../consts/MSG_CORE_EVMSG.md#evmsg-graphviewchanged) | 400008000 | Something in XPresso has been changed (local event). |
| [c4d.EVMSG_MATERIALPREVIEW](../consts/MSG_CORE_EVMSG.md#evmsg-materialpreview) | -1008 | *Private* |
| [c4d.EVMSG_MATERIALSELECTION](../consts/MSG_CORE_EVMSG.md#evmsg-materialselection) | -1009 | A material selection has been changed (local event). |
| [c4d.EVMSG_RAYTRACER_FINISHED](../consts/MSG_CORE_EVMSG.md#evmsg-raytracer-finished) | -1003 | *Private* |
| [c4d.EVMSG_SETMODE](../consts/MSG_CORE_EVMSG.md#evmsg-setmode) | 1055256 | *Private* |
| [c4d.EVMSG_SHOWIN_FC](../consts/MSG_CORE_EVMSG.md#evmsg-showin-fc) | -200000076 | Show in Function Curve editor. |
| [c4d.EVMSG_SHOWIN_LM](../consts/MSG_CORE_EVMSG.md#evmsg-showin-lm) | -200000077 | Show in Layer Manager. |
| [c4d.EVMSG_SHOWIN_MT](../consts/MSG_CORE_EVMSG.md#evmsg-showin-mt) | -200000078 | Show in Motion editor. |
| [c4d.EVMSG_SHOWIN_SB](../consts/MSG_CORE_EVMSG.md#evmsg-showin-sb) | -200000074 | Show in Scene Browser. |
| [c4d.EVMSG_SHOWIN_TL](../consts/MSG_CORE_EVMSG.md#evmsg-showin-tl) | -200000075 | Show in Timeline. |
| [c4d.EVMSG_TAKECHANGED](../consts/MSG_CORE_EVMSG.md#evmsg-takechanged) | 431000159 | Sent by the Take System when the current Take ID changed to let all managers react to the new status. |
| [c4d.EVMSG_TIMECHANGED](../consts/MSG_CORE_EVMSG.md#evmsg-timechanged) | 1952671847 | *Private* |
| [c4d.EVMSG_TIMELINESELECTION](../consts/MSG_CORE_EVMSG.md#evmsg-timelineselection) | -1001 | A timeline selection has been changed (local event). |
| [c4d.EVMSG_TL_FCURVE_POS](../consts/MSG_CORE_EVMSG.md#evmsg-tl-fcurve-pos) | -200000079 | Show and frame fcurve position tracks. |
| [c4d.EVMSG_TL_FCURVE_ROT](../consts/MSG_CORE_EVMSG.md#evmsg-tl-fcurve-rot) | -200000080 | Show and frame fcurve rotation tracks. |
| [c4d.EVMSG_TL_FCURVE_SCALE](../consts/MSG_CORE_EVMSG.md#evmsg-tl-fcurve-scale) | -200000081 | Show and frame fcurve scale tracks. |
| [c4d.EVMSG_TLOM_MERGE](../consts/MSG_CORE_EVMSG.md#evmsg-tlom-merge) | -465001000 | *Private* |
| [c4d.EVMSG_TOOLCHANGED](../consts/MSG_CORE_EVMSG.md#evmsg-toolchanged) | -826267 | A tool setting has changed (local event). |
| [c4d.EVMSG_UPDATEBASEDRAW](../consts/MSG_CORE_EVMSG.md#evmsg-updatebasedraw) | 200000099 | Sent in the case that the view should be redrawn. |
| [c4d.EVMSG_UPDATEHIGHLIGHT](../consts/MSG_CORE_EVMSG.md#evmsg-updatehighlight) | 200000073 | A special message sent by Cinema 4D in the case that only the highlighting changes. |
| [c4d.EVMSG_UPDATESCHEME](../consts/MSG_CORE_EVMSG.md#evmsg-updatescheme) | 200000010 | Scheme has been updated. |
| [c4d.EVMSG_VIEWWINDOW_3DPAINTUPD](../consts/MSG_CORE_EVMSG.md#evmsg-viewwindow-3dpaintupd) | -1012 | *Private* |
| [c4d.EVMSG_VIEWWINDOW_OUTPUT](../consts/MSG_CORE_EVMSG.md#evmsg-viewwindow-output) | -1011 | *Private* |

### GUI Messages <a id="gui-messages"></a><a id="msg-gui"></a>

The following messages can be send to and received by the `Message` methods of [`GeDialog`](../modules/c4d.gui/GeDialog/index.md#c4d.gui.GeDialog) and [`GeUserArea`](../modules/c4d.gui/GeUserArea/index.md#c4d.gui.GeUserArea) instances.

| Symbol | Numeric Value | Description |
|---|---|---|
| [c4d.MSG_ANIMATE](../consts/MSG_C4DATOM_PLUGINS.md#msg-animate) | 300001037 | Sent to objects after they have been animated. |
| [c4d.BFM_ACTION](../consts/MSG_GUI.md#bfm-action) | 1648444244 | One of the child elements made action. |
| [c4d.BFM_ACTION_ESC](../consts/MSG_GUI.md#bfm-action-esc) | 1634038627 | *Internal* |
| [c4d.BFM_ACTION_ID](../consts/MSG_GUI.md#bfm-action-id) | 1835362660 | ID of the dialog element that triggered the action. |
| [c4d.BFM_ACTION_INDRAG](../consts/MSG_GUI.md#bfm-action-indrag) | 1835361394 | Slider in dragging mode (not finished). |
| [c4d.BFM_ACTION_KEYDOWN](../consts/MSG_GUI.md#bfm-action-keydown) | 1801812324 | Key Down pressed while editfield is active. |
| [c4d.BFM_ACTION_KEYUP](../consts/MSG_GUI.md#bfm-action-keyup) | 1801812341 | Key Up pressed while editfield is active. |
| [c4d.BFM_ACTION_RESET](../consts/MSG_GUI.md#bfm-action-reset) | 1634887027 | Reset to default value on right-click of input field arrows. |
| [c4d.BFM_ACTION_STRCHG](../consts/MSG_GUI.md#bfm-action-strchg) | 1835365236 | String in text field changed. |
| [c4d.BFM_ACTION_UPDATE](../consts/MSG_GUI.md#bfm-action-update) | 1970300020 | *Internal* |
| [c4d.BFM_ACTION_VALCHG](../consts/MSG_GUI.md#bfm-action-valchg) | 1986226279 | Edit/slider changed. |
| [c4d.BFM_ACTION_VALUE](../consts/MSG_GUI.md#bfm-action-value) | 1835365985 | GeData Action value. |
| [c4d.BFM_ACTIVATE_WINDOW](../consts/MSG_GUI.md#bfm-activate-window) | 2002871156 | *Private* |
| [c4d.BFM_ACTIVE](../consts/MSG_GUI.md#bfm-active) | 1633907830 | *Private* |
| [c4d.BFM_ACTIVE_CHG](../consts/MSG_GUI.md#bfm-active-chg) | 1648444231 | *Private* |
| [c4d.BFM_ADJUSTSIZE](../consts/MSG_GUI.md#bfm-adjustsize) | 1715553354 | *Private* |
| [c4d.BFM_ADJUSTSIZE_HEIGHT](../consts/MSG_GUI.md#bfm-adjustsize-height) | 4 | *Private* |
| [c4d.BFM_ADJUSTSIZE_LEFT](../consts/MSG_GUI.md#bfm-adjustsize-left) | 1 | *Private* |
| [c4d.BFM_ADJUSTSIZE_TOP](../consts/MSG_GUI.md#bfm-adjustsize-top) | 2 | *Private* |
| [c4d.BFM_ADJUSTSIZE_WIDTH](../consts/MSG_GUI.md#bfm-adjustsize-width) | 3 | *Private* |
| [c4d.BFM_ASK_TABSWITCH](../consts/MSG_GUI.md#bfm-ask-tabswitch) | 1937006946 | *Internal* |
| [c4d.BFM_ASKCLOSE](../consts/MSG_GUI.md#bfm-askclose) | 1634954083 | Ask if a dialog is able to close. Return false it is OK to close, otherwise true. |
| [c4d.BFM_CALCSIZE](../consts/MSG_GUI.md#bfm-calcsize) | 1648574803 | Called if the element has to calculate its own minimum X and Y dimensions. |
| [c4d.BFM_CHECKCLOSE](../consts/MSG_GUI.md#bfm-checkclose) | 1667787619 | Check if a dialog is able to close. Return false it is OK to close, otherwise true. |
| [c4d.BFM_CHECKCLOSE_LAYOUTSWITCH](../consts/MSG_GUI.md#bfm-checkclose-layoutswitch) | 1667460204 | Check if a dialog is able to close when layouts are switched. Return false it is OK to close, otherwise true. |
| [c4d.BFM_CHILD_ID](../consts/MSG_GUI.md#bfm-child-id) | 1 | *Private* |
| [c4d.BFM_CHILD_REMOVED](../consts/MSG_GUI.md#bfm-child-removed) | 1649567085 | *Private* |
| [c4d.BFM_CLEARFOCUS](../consts/MSG_GUI.md#bfm-clearfocus) | 1648576067 | *Private* |
| [c4d.BFM_CLOSEWINDOW](../consts/MSG_GUI.md#bfm-closewindow) | 1668050803 | *Internal* |
| [c4d.BFM_COLORCHOOSER](../consts/MSG_GUI.md#bfm-colorchooser) | 1668246595 | Color chooser settings: |
| [c4d.BFM_COLORCHOOSER_PARENTMESSAGE](../consts/MSG_GUI.md#bfm-colorchooser-parentmessage) | 1668246608 | Color chooser parent message. |
| [c4d.BFM_COLORCHOOSER_RGB_RANGE](../consts/MSG_GUI.md#bfm-colorchooser-rgb-range) | 2 | RGB range: COLORSYSTEM_RANGE |
| [c4d.BFM_COLORCHOOSER_SYSTEMMESSAGE](../consts/MSG_GUI.md#bfm-colorchooser-systemmessage) | 5 | Sends a parent message BFM_COLORCHOOSER_PARENTMESSAGE if the settings change. |
| [c4d.BFM_COMMANDSCHANGED](../consts/MSG_GUI.md#bfm-commandschanged) | 1668113256 | *Private* |
| [c4d.BFM_CORE_ID](../consts/MSG_GUI.md#bfm-core-id) | 1298360649 | Core message ID. |
| [c4d.BFM_CORE_MESSAGE](../consts/MSG_GUI.md#bfm-core-message) | 1298360653 | Core message. |
| [c4d.BFM_CORE_PAR1](../consts/MSG_GUI.md#bfm-core-par1) | 1298360625 | Parameter 1. |
| [c4d.BFM_CORE_PAR2](../consts/MSG_GUI.md#bfm-core-par2) | 1298360626 | Parameter 2. |
| [c4d.BFM_CORE_SPECIALCOREID](../consts/MSG_GUI.md#bfm-core-specialcoreid) | 1935894884 | Special manager ID for sync message. |
| [c4d.BFM_CORE_UNIQUEID](../consts/MSG_GUI.md#bfm-core-uniqueid) | 1299540324 | Time stamp. |
| [c4d.BFM_CORE_UPDATEACTIVECOMMANDS](../consts/MSG_GUI.md#bfm-core-updateactivecommands) | 1970300001 | *Private* |
| [c4d.BFM_CORE_UPDATECOMMANDS](../consts/MSG_GUI.md#bfm-core-updatecommands) | 1970300003 | *Internal* |
| [c4d.BFM_CURSORINFO_REMOVE](../consts/MSG_GUI.md#bfm-cursorinfo-remove) | 1667854957 | Sent when mouse cursor has left a user area. |
| [c4d.BFM_DESTINATION_GROUP](../consts/MSG_GUI.md#bfm-destination-group) | 1734636404 | *Internal* |
| [c4d.BFM_DESTROY](../consts/MSG_GUI.md#bfm-destroy) | 1685288057 | Sent just before the window is destroyed. |
| [c4d.BFM_DISABLE](../consts/MSG_GUI.md#bfm-disable) | 1648650611 | *Internal* |
| [c4d.BFM_DRAG_DATA_](../consts/MSG_GUI.md#bfm-drag-data) | 2 | *Internal* |
| [c4d.BFM_DRAG_DATA_NEW](../consts/MSG_GUI.md#bfm-drag-data-new) | 9 | *Internal* |
| [c4d.BFM_DRAG_ESC](../consts/MSG_GUI.md#bfm-drag-esc) | 10 | Drag escaped. |
| [c4d.BFM_DRAG_FINISHED](../consts/MSG_GUI.md#bfm-drag-finished) | 5 | Drag finished. |
| [c4d.BFM_DRAG_LOST](../consts/MSG_GUI.md#bfm-drag-lost) | 7 | Drag lost. |
| [c4d.BFM_DRAG_SCREENX](../consts/MSG_GUI.md#bfm-drag-screenx) | 3 | Screen X. |
| [c4d.BFM_DRAG_SCREENY](../consts/MSG_GUI.md#bfm-drag-screeny) | 4 | Screen Y. |
| [c4d.BFM_DRAG_TYPE_NEW](../consts/MSG_GUI.md#bfm-drag-type-new) | 8 | Drag type: DRAGTYPE |
| [c4d.BFM_DRAGAUTOSCROLL](../consts/MSG_GUI.md#bfm-dragautoscroll) | 10005 | *Internal* |
| [c4d.BFM_DRAGEND](../consts/MSG_GUI.md#bfm-dragend) | 10004 | *Internal* |
| [c4d.BFM_DRAGRECEIVE](../consts/MSG_GUI.md#bfm-dragreceive) | 10003 | Drag receive. |
| [c4d.BFM_DRAGSTART](../consts/MSG_GUI.md#bfm-dragstart) | 10001 | *Internal* |
| [c4d.BFM_DRAW](../consts/MSG_GUI.md#bfm-draw) | 1648644673 | Redraw message for user areas. |
| [c4d.BFM_DRAW_BOTTOM](../consts/MSG_GUI.md#bfm-draw-bottom) | 4 | Bottom clipping. |
| [c4d.BFM_DRAW_HASRECT](../consts/MSG_GUI.md#bfm-draw-hasrect) | 5 | *Internal* |
| [c4d.BFM_DRAW_LEFT](../consts/MSG_GUI.md#bfm-draw-left) | 1 | Left clipping. |
| [c4d.BFM_DRAW_OGL](../consts/MSG_GUI.md#bfm-draw-ogl) | 6 | *Internal* |
| [c4d.BFM_DRAW_REASON](../consts/MSG_GUI.md#bfm-draw-reason) | 7 | BaseContainer Message which started the redraw. |
| [c4d.BFM_DRAW_RIGHT](../consts/MSG_GUI.md#bfm-draw-right) | 3 | Right clipping. |
| [c4d.BFM_DRAW_TOP](../consts/MSG_GUI.md#bfm-draw-top) | 2 | Top clipping. |
| [c4d.BFM_DRAWUSERITEM](../consts/MSG_GUI.md#bfm-drawuseritem) | 1970500196 | *Private* |
| [c4d.BFM_DRAWUSERITEM_ID](../consts/MSG_GUI.md#bfm-drawuseritem-id) | 1 | *Internal* |
| [c4d.BFM_EDITFIELD_FLUSHUNDO](../consts/MSG_GUI.md#bfm-editfield-flushundo) | 1718383982 | Flushes the undo stack for a multi-line edit text. |
| [c4d.BFM_EDITFIELD_GETBLOCKSTART](../consts/MSG_GUI.md#bfm-editfield-getblockstart) | 1734702178 | Returns the block start position in an edit field. |
| [c4d.BFM_EDITFIELD_GETCURSORPOS](../consts/MSG_GUI.md#bfm-editfield-getcursorpos) | 1734702179 | Return the cursor position in an edit field. |
| [c4d.BFM_EDITFIELD_GETUNDOSTATS](../consts/MSG_GUI.md#bfm-editfield-getundostats) | 1970172788 | *Internal* |
| [c4d.BFM_EDITFIELD_RESTOREUNDO](../consts/MSG_GUI.md#bfm-editfield-restoreundo) | 1920169077 | Restore the undo container for a multi-line edit text. |
| [c4d.BFM_EDITFIELD_SETCURSORPOS](../consts/MSG_GUI.md#bfm-editfield-setcursorpos) | 1936028771 | Set the cursor position in an edit field. |
| [c4d.BFM_EDITFIELD_STOREUNDO](../consts/MSG_GUI.md#bfm-editfield-storeundo) | 1937011317 | Stores the undo container for a multi-line edit text. |
| [c4d.BFM_EDITFIELD_UNDOSTAT_COUNT](../consts/MSG_GUI.md#bfm-editfield-undostat-count) | 1 | The undo stack size. |
| [c4d.BFM_EDITFIELD_UNDOSTAT_UNDOLEVEL](../consts/MSG_GUI.md#bfm-editfield-undostat-undolevel) | 2 | The current undo level. |
| [c4d.BFM_ENABLE](../consts/MSG_GUI.md#bfm-enable) | 1648717409 | *Internal* |
| [c4d.BFM_FADE](../consts/MSG_GUI.md#bfm-fade) | 1717658725 | Sent to blend GUI color with ease in a GeUserArea. |
| [c4d.BFM_FADE_REMOVEALL](../consts/MSG_GUI.md#bfm-fade-removeall) | 1178682437 | *Private* |
| [c4d.BFM_FULLSCREENMODE_OFF](../consts/MSG_GUI.md#bfm-fullscreenmode-off) | 1718971440 | *Internal* |
| [c4d.BFM_FULLSCREENMODE_ON](../consts/MSG_GUI.md#bfm-fullscreenmode-on) | 1718971441 | *Internal* |
| [c4d.BFM_GET_FOCUS_RECTANGLE](../consts/MSG_GUI.md#bfm-get-focus-rectangle) | 1734759011 | Returns the coordinates of the input field with the current focus. |
| [c4d.BFM_GET_FOCUS_RECTANGLE_H](../consts/MSG_GUI.md#bfm-get-focus-rectangle-h) | 3 | Input field height. |
| [c4d.BFM_GET_FOCUS_RECTANGLE_W](../consts/MSG_GUI.md#bfm-get-focus-rectangle-w) | 2 | Input field width. |
| [c4d.BFM_GET_FOCUS_RECTANGLE_X](../consts/MSG_GUI.md#bfm-get-focus-rectangle-x) | 0 | Input field X coordinate. |
| [c4d.BFM_GET_FOCUS_RECTANGLE_Y](../consts/MSG_GUI.md#bfm-get-focus-rectangle-y) | 1 | Input field Y coordinate. |
| [c4d.BFM_GETACTIVETABTITLE](../consts/MSG_GUI.md#bfm-getactivetabtitle) | 1952539508 | *Private* |
| [c4d.BFM_GETCURSORINFO](../consts/MSG_GUI.md#bfm-getcursorinfo) | 1667853926 | Respond this message to display help information in the bubble help or global statusbar. |
| [c4d.BFM_GETCUSTOMGUILAYOUTDATA](../consts/MSG_GUI.md#bfm-getcustomguilayoutdata) | 1818327367 | *Private* |
| [c4d.BFM_GETFOCUSBEFOREUPDATE](../consts/MSG_GUI.md#bfm-getfocusbeforeupdate) | 1648838229 | A custom GUI receives this message before the layout is updated. This is used to avoid losing the focus over a specific gadget after the layout is updated. |
| [c4d.BFM_GETINFO](../consts/MSG_GUI.md#bfm-getinfo) | 1648979558 | *Private* |
| [c4d.BFM_GETPARENT_MANAGER_ID](../consts/MSG_GUI.md#bfm-getparent-manager-id) | 1735420260 | *Private* |
| [c4d.BFM_GETVALUE](../consts/MSG_GUI.md#bfm-getvalue) | 1733706060 | *Private* |
| [c4d.BFM_GETVIEWPANELDATA](../consts/MSG_GUI.md#bfm-getviewpaneldata) | 1987077236 | *Private* |
| [c4d.BFM_GETVISIBLE_HEIGHT](../consts/MSG_GUI.md#bfm-getvisible-height) | 10014 | *Private* |
| [c4d.BFM_GETVISIBLE_WIDTH](../consts/MSG_GUI.md#bfm-getvisible-width) | 10013 | *Private* |
| [c4d.BFM_GETVISIBLE_XOFF](../consts/MSG_GUI.md#bfm-getvisible-xoff) | 10011 | *Private* |
| [c4d.BFM_GETVISIBLE_YOFF](../consts/MSG_GUI.md#bfm-getvisible-yoff) | 10012 | *Private* |
| [c4d.BFM_GOTFOCUS](../consts/MSG_GUI.md#bfm-gotfocus) | 1648838211 | Item got the focus. |
| [c4d.BFM_GUIPREFSCHANGED](../consts/MSG_GUI.md#bfm-guiprefschanged) | 1735418728 | *Private* |
| [c4d.BFM_IDCHNG](../consts/MSG_GUI.md#bfm-idchng) | 1648968771 | *Private* |
| [c4d.BFM_INIT](../consts/MSG_GUI.md#bfm-init) | 1648971337 | Sent after an element has been created. |
| [c4d.BFM_INITVALUES](../consts/MSG_GUI.md#bfm-initvalues) | 1649822030 | Sent after the layout is done. |
| [c4d.BFM_INPUT](../consts/MSG_GUI.md#bfm-input) | 1648971854 | A dialog/user area receives this message if mouse or keyboard input is received. See Input Events for more information. |
| [c4d.BFM_INPUT_AFTER_SCROLL](../consts/MSG_GUI.md#bfm-input-after-scroll) | 1648968019 | Input message ID sent after scroll area processed input messages. |
| [c4d.BFM_INPUT_ASC](../consts/MSG_GUI.md#bfm-input-asc) | 1801548643 | String Contains the Unicode input from keyboard. |
| [c4d.BFM_INPUT_CHANNEL](../consts/MSG_GUI.md#bfm-input-channel) | 1768973153 | Contains the key or mouse button. See also KEY. |
| [c4d.BFM_INPUT_DEVICE](../consts/MSG_GUI.md#bfm-input-device) | 1768973430 | Device: |
| [c4d.BFM_INPUT_DOUBLECLICK](../consts/MSG_GUI.md#bfm-input-doubleclick) | 1768973410 | Double click. |
| [c4d.BFM_INPUT_FINGERWHEEL](../consts/MSG_GUI.md#bfm-input-fingerwheel) | 1768320615 | Finger wheel (tangential pen pressure). |
| [c4d.BFM_INPUT_HSCROLL](../consts/MSG_GUI.md#bfm-input-hscroll) | 1768452963 | Amount of horizontal scrolling (touch pad, mouse ball) |
| [c4d.BFM_INPUT_KEYBOARD](../consts/MSG_GUI.md#bfm-input-keyboard) | 1801812322 | Keyboard. |
| [c4d.BFM_INPUT_MAGNIFY](../consts/MSG_GUI.md#bfm-input-magnify) | 102 | Zoom guesture on touch pad or touch screen (or mouse scroll with ctrl to indicate zoom). Value in BFM_INPUT_VALUE_REAL. |
| [c4d.BFM_INPUT_MODIFIERS](../consts/MSG_GUI.md#bfm-input-modifiers) | 1768975727 | *Private* |
| [c4d.BFM_INPUT_MOUSE](../consts/MSG_GUI.md#bfm-input-mouse) | 1836021107 | Mouse. |
| [c4d.BFM_INPUT_MOUSELEFT](../consts/MSG_GUI.md#bfm-input-mouseleft) | 1 | Left mouse button. |
| [c4d.BFM_INPUT_MOUSEMIDDLE](../consts/MSG_GUI.md#bfm-input-mousemiddle) | 3 | Middle mouse button. |
| [c4d.BFM_INPUT_MOUSEMOVE](../consts/MSG_GUI.md#bfm-input-mousemove) | 101 | Mouse move. |
| [c4d.BFM_INPUT_MOUSERIGHT](../consts/MSG_GUI.md#bfm-input-mouseright) | 2 | Right mouse button. |
| [c4d.BFM_INPUT_MOUSEWHEEL](../consts/MSG_GUI.md#bfm-input-mousewheel) | 100 | Mouse wheel or panning on touch pad or touch screen. Values in BFM_INPUT_HSCROLL, BFM_INPUT_VSCROLL. |
| [c4d.BFM_INPUT_MOUSEX1](../consts/MSG_GUI.md#bfm-input-mousex1) | 5 | Fourth mouse button. |
| [c4d.BFM_INPUT_MOUSEX2](../consts/MSG_GUI.md#bfm-input-mousex2) | 6 | Five mouse button. |
| [c4d.BFM_INPUT_MULTITOUCHSCROLL](../consts/MSG_GUI.md#bfm-input-multitouchscroll) | 1768780643 | True for scroll events on a multitouch device (which also supports magnify), false for scroll-only mice. |
| [c4d.BFM_INPUT_ORIENTATION](../consts/MSG_GUI.md#bfm-input-orientation) | 1769107316 | Pen rotation. |
| [c4d.BFM_INPUT_P_ROTATION](../consts/MSG_GUI.md#bfm-input-p-rotation) | 1886547828 | Pen rotation around its own axis. |
| [c4d.BFM_INPUT_QUALIFIER](../consts/MSG_GUI.md#bfm-input-qualifier) | 1768976737 | A bit mask with the qualifiers at the time when the event occurred: QUALIFIER |
| [c4d.BFM_INPUT_TILT](../consts/MSG_GUI.md#bfm-input-tilt) | 1769237620 | Pen tilt. |
| [c4d.BFM_INPUT_TIMESTAMP](../consts/MSG_GUI.md#bfm-input-timestamp) | 1769237875 | Time stamp of the event or 0.0 (unavailable). |
| [c4d.BFM_INPUT_VALUE](../consts/MSG_GUI.md#bfm-input-value) | 1768978017 | Value of the input channel (true/false or a value, e.g. for scroll wheel data). |
| [c4d.BFM_INPUT_VALUE_REAL](../consts/MSG_GUI.md#bfm-input-value-real) | 1768977985 | Channel value (e.g. pen pressure). |
| [c4d.BFM_INPUT_VSCROLL](../consts/MSG_GUI.md#bfm-input-vscroll) | 1769370467 | Amount of vertical scrolling (touch pad, mouse wheel/ball) |
| [c4d.BFM_INPUT_WHEELSCROLL](../consts/MSG_GUI.md#bfm-input-wheelscroll) | 1769436003 | True for scroll events on a classic wheel mouse. False for everything else (touchpad, magic mouse). |
| [c4d.BFM_INPUT_X](../consts/MSG_GUI.md#bfm-input-x) | 1768978040 | X value. |
| [c4d.BFM_INPUT_Y](../consts/MSG_GUI.md#bfm-input-y) | 1768978041 | Y value. |
| [c4d.BFM_INPUT_Z](../consts/MSG_GUI.md#bfm-input-z) | 1768978042 | Z value. |
| [c4d.BFM_INTERACTEND](../consts/MSG_GUI.md#bfm-interactend) | 1768846437 | Sent when user interaction ends. |
| [c4d.BFM_INTERACTSTART](../consts/MSG_GUI.md#bfm-interactstart) | 1768846433 | Sent when user interaction starts. |
| [c4d.BFM_ISACTIVE](../consts/MSG_GUI.md#bfm-isactive) | 1767990132 | *Private* |
| [c4d.BFM_LAYOUT_CHANGED](../consts/MSG_GUI.md#bfm-layout-changed) | 1716273497 | *Internal* |
| [c4d.BFM_LAYOUT_GETDATA](../consts/MSG_GUI.md#bfm-layout-getdata) | 1818327399 | Sent when saving the layout. Return a container to store with the layout for this dialog. |
| [c4d.BFM_LAYOUT_SETDATA](../consts/MSG_GUI.md#bfm-layout-setdata) | 1818327411 | Receive the container saved with BFM_LAYOUT_GETDATA when loading a layout. |
| [c4d.BFM_LOSTFOCUS](../consts/MSG_GUI.md#bfm-lostfocus) | 1649165891 | Item lost the focus. |
| [c4d.BFM_MANAGER_ID](../consts/MSG_GUI.md#bfm-manager-id) | 2 | *Internal* |
| [c4d.BFM_MARKFOCUS](../consts/MSG_GUI.md#bfm-markfocus) | 1649231427 | *Private* |
| [c4d.BFM_MARKFORCELAYOUT](../consts/MSG_GUI.md#bfm-markforcelayout) | 1835755116 | *Private* |
| [c4d.BFM_MAXCHNG](../consts/MSG_GUI.md#bfm-maxchng) | 1649230147 | *Private* |
| [c4d.BFM_MENU_CHECK](../consts/MSG_GUI.md#bfm-menu-check) | 4 | *Internal* |
| [c4d.BFM_MENU_OFF](../consts/MSG_GUI.md#bfm-menu-off) | 2 | *Internal* |
| [c4d.BFM_MENU_ON](../consts/MSG_GUI.md#bfm-menu-on) | 1 | *Internal* |
| [c4d.BFM_MENU_SET](../consts/MSG_GUI.md#bfm-menu-set) | 10000 | *Private* |
| [c4d.BFM_MENU_UNCHECK](../consts/MSG_GUI.md#bfm-menu-uncheck) | 8 | *Internal* |
| [c4d.BFM_MENUFINDER](../consts/MSG_GUI.md#bfm-menufinder) | 1718185572 | *Private* |
| [c4d.BFM_MINCHNG](../consts/MSG_GUI.md#bfm-minchng) | 1649232195 | *Private* |
| [c4d.BFM_OPTIMIZE](../consts/MSG_GUI.md#bfm-optimize) | 1869640809 | *Private* |
| [c4d.BFM_PARENT_TITLECHNG](../consts/MSG_GUI.md#bfm-parent-titlechng) | 1886545262 | *Internal* |
| [c4d.BFM_POPUPNOTIFY](../consts/MSG_GUI.md#bfm-popupnotify) | 1886351470 | Notification of popup before the menu opens. |
| [c4d.BFM_REDRAW_EDITMODE](../consts/MSG_GUI.md#bfm-redraw-editmode) | 1685546340 | *Private* |
| [c4d.BFM_RELOAD_MENUS](../consts/MSG_GUI.md#bfm-reload-menus) | 1818520942 | *Private* |
| [c4d.BFM_REMOVE_DIALOG](../consts/MSG_GUI.md#bfm-remove-dialog) | 1649558861 | *Internal* |
| [c4d.BFM_RENAMEWINDOW](../consts/MSG_GUI.md#bfm-renamewindow) | 2003985774 | *Internal* |
| [c4d.BFM_REQUIRESRESULT](../consts/MSG_GUI.md#bfm-requiresresult) | 1919250802 | Set to true in the passed container for `GeDialog.SendMessage()` to return a value from the message. |
| [c4d.BFM_SCROLLAREA](../consts/MSG_GUI.md#bfm-scrollarea) | 10010 | *Internal* |
| [c4d.BFM_SCROLLGROUP_OFFSETCHANGED](../consts/MSG_GUI.md#bfm-scrollgroup-offsetchanged) | 1666139718 | *Internal* |
| [c4d.BFM_SCROLLGROUP_SCALE](../consts/MSG_GUI.md#bfm-scrollgroup-scale) | 1935897443 | *Private* |
| [c4d.BFM_SCROLLGROUP_SCROLLED](../consts/MSG_GUI.md#bfm-scrollgroup-scrolled) | 1935897203 | Scroll group scrolled. |
| [c4d.BFM_SCROLLX](../consts/MSG_GUI.md#bfm-scrollx) | 1 | *Internal* |
| [c4d.BFM_SCROLLY](../consts/MSG_GUI.md#bfm-scrolly) | 2 | *Internal* |
| [c4d.BFM_SET_MSG_BITMASK](../consts/MSG_GUI.md#bfm-set-msg-bitmask) | 1651078253 | *Private* |
| [c4d.BFM_SETACTIVE](../consts/MSG_GUI.md#bfm-setactive) | 1649623363 | *Private* |
| [c4d.BFM_SETACTIVE_DATA](../consts/MSG_GUI.md#bfm-setactive-data) | 1649623363 | *Private* |
| [c4d.BFM_SETCURSORINFO](../consts/MSG_GUI.md#bfm-setcursorinfo) | 1936028771 | Same as BFM_EDITFIELD_SETCURSORPOS. |
| [c4d.BFM_SETFIRSTFOCUS](../consts/MSG_GUI.md#bfm-setfirstfocus) | 1649624646 | *Internal* |
| [c4d.BFM_SETFOCUS](../consts/MSG_GUI.md#bfm-setfocus) | 1649624643 | *Internal* |
| [c4d.BFM_SETFOCUSAFTERUPDATE](../consts/MSG_GUI.md#bfm-setfocusafterupdate) | 1649624661 | A custom GUI description receives this message after the layout is updated to reactivate previously focused gadget. |
| [c4d.BFM_SETLASTFOCUS](../consts/MSG_GUI.md#bfm-setlastfocus) | 1649626182 | *Private* |
| [c4d.BFM_SETMAINTITLE](../consts/MSG_GUI.md#bfm-setmaintitle) | 1836345716 | *Private* |
| [c4d.BFM_SETSPECIALMULTI](../consts/MSG_GUI.md#bfm-setspecialmulti) | 1397969747 | *Private* |
| [c4d.BFM_SETSPECIALMULTID](../consts/MSG_GUI.md#bfm-setspecialmultid) | 1397969732 | *Private* |
| [c4d.BFM_SETSTATUSBAR](../consts/MSG_GUI.md#bfm-setstatusbar) | 1937006964 | Sets a statusbar. |
| [c4d.BFM_SETVIEWPANELLAYOUT](../consts/MSG_GUI.md#bfm-setviewpanellayout) | 1987081068 | *Private* |
| [c4d.BFM_SETVIEWPORTORIGIN](../consts/MSG_GUI.md#bfm-setviewportorigin) | 1666142791 | *Internal* |
| [c4d.BFM_SETVIEWPORTORIGIN_X](../consts/MSG_GUI.md#bfm-setviewportorigin-x) | 1 | *Internal* |
| [c4d.BFM_SETVIEWPORTORIGIN_Y](../consts/MSG_GUI.md#bfm-setviewportorigin-y) | 2 | *Internal* |
| [c4d.BFM_SETVIEWPORTSIZE](../consts/MSG_GUI.md#bfm-setviewportsize) | 1666402650 | *Private* |
| [c4d.BFM_SHOW_AREA](../consts/MSG_GUI.md#bfm-show-area) | 1935766117 | *Internal* |
| [c4d.BFM_SHOW_FRAME](../consts/MSG_GUI.md#bfm-show-frame) | 1933996653 | *Internal* |
| [c4d.BFM_SHOW_ID](../consts/MSG_GUI.md#bfm-show-id) | 1 | *Internal* |
| [c4d.BFM_SIZED](../consts/MSG_GUI.md#bfm-sized) | 1648972617 | Element has been sized. |
| [c4d.BFM_SPECIALGETSTRING](../consts/MSG_GUI.md#bfm-specialgetstring) | 1735684980 | *Private* |
| [c4d.BFM_SPECIALMODE](../consts/MSG_GUI.md#bfm-specialmode) | 1936879213 | Set the multi-line edit field to the right language mode. |
| [c4d.BFM_SPECIALSETRANGE](../consts/MSG_GUI.md#bfm-specialsetrange) | 1936879207 | *Private* |
| [c4d.BFM_STATUSBAR_HELP](../consts/MSG_GUI.md#bfm-statusbar-help) | 5 | Help second text. |
| [c4d.BFM_STATUSBAR_NETPROGRESS](../consts/MSG_GUI.md#bfm-statusbar-netprogress) | 11 | *Internal* |
| [c4d.BFM_STATUSBAR_NETPROGRESSON](../consts/MSG_GUI.md#bfm-statusbar-netprogresson) | 9 | *Internal* |
| [c4d.BFM_STATUSBAR_NETPROGRESSSPIN](../consts/MSG_GUI.md#bfm-statusbar-netprogressspin) | 12 | *Internal* |
| [c4d.BFM_STATUSBAR_NETTINT_COLOR](../consts/MSG_GUI.md#bfm-statusbar-nettint-color) | 8 | *Internal* |
| [c4d.BFM_STATUSBAR_NETTXT](../consts/MSG_GUI.md#bfm-statusbar-nettxt) | 10 | *Internal* |
| [c4d.BFM_STATUSBAR_PROGRESS](../consts/MSG_GUI.md#bfm-statusbar-progress) | 3 | Between 0.0 and 1.0. |
| [c4d.BFM_STATUSBAR_PROGRESSFULLSIZE](../consts/MSG_GUI.md#bfm-statusbar-progressfullsize) | 6 | *Internal* |
| [c4d.BFM_STATUSBAR_PROGRESSON](../consts/MSG_GUI.md#bfm-statusbar-progresson) | 1 | Statusbar active. |
| [c4d.BFM_STATUSBAR_PROGRESSSPIN](../consts/MSG_GUI.md#bfm-statusbar-progressspin) | 4 | Spinning bar. |
| [c4d.BFM_STATUSBAR_TINT_COLOR](../consts/MSG_GUI.md#bfm-statusbar-tint-color) | 7 | Color ID for the status bar, or as RGB value (Vector). |
| [c4d.BFM_STATUSBAR_TXT](../consts/MSG_GUI.md#bfm-statusbar-txt) | 2 | Help first text. |
| [c4d.BFM_STORE_WEIGHTS](../consts/MSG_GUI.md#bfm-store-weights) | 1937012583 | *Private* |
| [c4d.BFM_SYNC_MESSAGE](../consts/MSG_GUI.md#bfm-sync-message) | 1937337955 | Sync message. |
| [c4d.BFM_TESTONLY](../consts/MSG_GUI.md#bfm-testonly) | 1952805748 | *Private* |
| [c4d.BFM_TIMER_MESSAGE](../consts/MSG_GUI.md#bfm-timer-message) | 10020 | Timer message. Use `GeDialog.SetTimer()` / `GeUserArea.SetTimer()` to set the periodical time. |
| [c4d.BFM_TITLECHNG](../consts/MSG_GUI.md#bfm-titlechng) | 1649690947 | *Private* |
| [c4d.BFM_UPDATE_REGION](../consts/MSG_GUI.md#bfm-update-region) | 1970303591 | *Private* |
| [c4d.BFM_VALUEADD](../consts/MSG_GUI.md#bfm-valueadd) | 1649819972 | *Private* |
| [c4d.BFM_VALUECHNG](../consts/MSG_GUI.md#bfm-valuechng) | 1649819971 | *Private* |
| [c4d.BFM_VALUESUB](../consts/MSG_GUI.md#bfm-valuesub) | 1649824578 | *Private* |
| [c4d.BFM_VISIBLE_OFF](../consts/MSG_GUI.md#bfm-visible-off) | 1986622278 | *Internal* |
| [c4d.BFM_VISIBLE_ON](../consts/MSG_GUI.md#bfm-visible-on) | 1986622292 | *Internal* |
| [c4d.BFM_VPD_LAYOUTTYPE](../consts/MSG_GUI.md#bfm-vpd-layouttype) | 1987079284 | *Private* |
| [c4d.BFM_VPD_MAXIMIZED](../consts/MSG_GUI.md#bfm-vpd-maximized) | 1987079544 | *Private* |
| [c4d.BFM_VPD_PANELID](../consts/MSG_GUI.md#bfm-vpd-panelid) | 1987078500 | *Private* |
| [c4d.BFM_WEIGHTS_CHANGED](../consts/MSG_GUI.md#bfm-weights-changed) | 2000906343 | Group weights changed. |

### Plugin Messages <a id="plugin-messages"></a><a id="msg-plugins"></a>

The following messages can be received in the `Message` methods of [`CommandData`](../modules/c4d.plugins/BaseData/CommandData/index.md#c4d.plugins.CommandData), [`FalloffData`](../modules/c4d.plugins/BaseData/FalloffData/index.md#c4d.plugins.FalloffData), [`NodeData`](../modules/c4d.plugins/BaseData/NodeData/index.md#c4d.plugins.NodeData), [`SculptBrushToolData`](../modules/c4d.plugins/BaseData/SculptBrushToolData/index.md#c4d.plugins.SculptBrushToolData), and [`ToolData`](../modules/c4d.plugins/BaseData/ToolData/index.md#c4d.plugins.ToolData) interfaces and their derived interfaces.

| Symbol | Numeric Value | Description |
|---|---|---|
| [c4d.MSG_ANIMATE](../consts/MSG_C4DATOM_PLUGINS.md#msg-animate) | 300001037 | Sent to objects after they have been animated. |
| [c4d.MSG_BASECONTAINER](../consts/MSG_C4DATOM_PLUGINS.md#msg-basecontainer) | 9 | Sent to pass arbitrary data in a container to a node. |
| [c4d.MSG_CHANGE](../consts/MSG_C4DATOM_PLUGINS.md#msg-change) | 7 | Sent if any data except for the matrix has been changed. |
| [c4d.MSG_COLLECTC4DFALLOFF](../consts/MSG_C4DATOM_PLUGINS.md#msg-collectc4dfalloff) | 440000221 | Sent to atoms that might contain a falloff. |
| [c4d.MSG_COMMANDINFORMATION](../consts/MSG_C4DATOM_PLUGINS.md#msg-commandinformation) | 300001001 | Sent to retrieve command information. |
| [c4d.MSG_DESCRIPTION_ALLOWOVERRIDE](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-allowoverride) | 431000094 | Sent to check if take override operation is allowed. |
| [c4d.MSG_DESCRIPTION_CHECKDRAGANDDROP](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-checkdraganddrop) | 26 | Sent to ask an atom if a drag and drop operation is accepted. |
| [c4d.MSG_DESCRIPTION_CHECKUPDATE](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-checkupdate) | 17 | Sent to allow elements to determine the type of refresh after a parameter has been changed. |
| [c4d.MSG_DESCRIPTION_COMMAND](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-command) | 18 | Sent for button description elements. |
| [c4d.MSG_DESCRIPTION_CUSTOMGUI_NOTIFICATION](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-customgui-notification) | 431000175 | Sent by a custom GUI to its parent node. |
| [c4d.MSG_DESCRIPTION_EDIT_ENTRY](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-edit-entry) | 25 | Sent to tell an atom to edit a description entry. |
| [c4d.MSG_DESCRIPTION_GETBITMAP](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-getbitmap) | 27 | Sent to query a description for a [`c4d.gui.BitmapButtonCustomGui`](../modules/c4d.gui/BaseCustomGui/BitmapButtonCustomGui/index.md#c4d.gui.BitmapButtonCustomGui) bitmap. |
| [c4d.MSG_DESCRIPTION_INITUNDO](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-initundo) | 16 | Sent to allows elements to create undo actions for the following parameter changes. |
| [c4d.MSG_DESCRIPTION_POPUP](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-popup) | 300001046 | Sent to handle description popup menus in the Attribute Manager. |
| [c4d.MSG_DESCRIPTION_POSTSETPARAMETER](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-postsetparameter) | 19 | Sent after a `C4DAtom.SetParameter()` call. |
| [c4d.MSG_DESCRIPTION_REMOVE_ENTRY](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-remove-entry) | 24 | Sent to tell an atom to remove a description entry. |
| [c4d.MSG_DESCRIPTION_VALIDATE](../consts/MSG_C4DATOM_PLUGINS.md#msg-description-validate) | 20 | Sent to update dependencies or to check for invalid values after a parameter change. |
| [c4d.MSG_DOCUMENT_MODE_CHANGED](../consts/MSG_C4DATOM_PLUGINS.md#msg-document-mode-changed) | 200000091 | Sent to the active tool plugin when document mode is changed. |
| [c4d.MSG_DOCUMENTINFO](../consts/MSG_C4DATOM_PLUGINS.md#msg-documentinfo) | 1001078 | Sent when a document has been loaded, saved, merged or other document related actions occurred. |
| [c4d.MSG_DRAGANDDROP](../consts/MSG_C4DATOM_PLUGINS.md#msg-draganddrop) | 1018756 | Sent to elements in the Object Manager when something is dropped on it. |
| [c4d.MSG_EDIT](../consts/MSG_C4DATOM_PLUGINS.md#msg-edit) | 21 | Sent to perform an action when element is being edited. |
| [c4d.MSG_FILTER](../consts/MSG_C4DATOM_PLUGINS.md#msg-filter) | 14 | Sent to allow or block `C4DAtom.MultiMessage()` calls. |
| [c4d.MSG_GETALLASSETS](../consts/MSG_C4DATOM_PLUGINS.md#msg-getallassets) | 112004 | Sent to retrieve all assets from an object. |
| [c4d.MSG_GETCUSTOMICON](../consts/MSG_C4DATOM_PLUGINS.md#msg-getcustomicon) | 1001090 | Sent to retrieve a custom icon. |
| [c4d.MSG_GETCUSTOMICON_SETTINGS](../consts/MSG_C4DATOM_PLUGINS.md#msg-getcustomicon-settings) | 1041699 | Sent to retrieve the custom icon settings of an object. |
| [c4d.MSG_GETREALCAMERADATA](../consts/MSG_C4DATOM_PLUGINS.md#msg-getrealcameradata) | 1028476 | Sent to get a real camera object from a generator. |
| [c4d.MSG_MENUPREPARE](../consts/MSG_C4DATOM_PLUGINS.md#msg-menuprepare) | 22 | Sent to allow tags, objects, shaders etc. to do some setup work when called from the menu. |
| [c4d.MSG_MULTI_CLEARSUGGESTEDFOLDER](../consts/MSG_C4DATOM_PLUGINS.md#msg-multi-clearsuggestedfolder) | 200000040 | Sent to nodes to convert absolute paths to filename. |
| [c4d.MSG_MULTI_DOCUMENTCLONED](../consts/MSG_C4DATOM_PLUGINS.md#msg-multi-documentcloned) | 11 | Sent when a document is being cloned. |
| [c4d.MSG_MULTI_RENDERNOTIFICATION](../consts/MSG_C4DATOM_PLUGINS.md#msg-multi-rendernotification) | 1001071 | Sent to a document and all of its elements before a render starts. |
| [c4d.MSG_POINTS_CHANGED](../consts/MSG_C4DATOM_PLUGINS.md#msg-points-changed) | 1 | Sent to notify an object its points have changed. |
| [c4d.MSG_POLYGONS_CHANGED](../consts/MSG_C4DATOM_PLUGINS.md#msg-polygons-changed) | 2 | Sent to notify an object its polygons have changed. |
| [c4d.MSG_SCALEDOCUMENT](../consts/MSG_C4DATOM_PLUGINS.md#msg-scaledocument) | 300001069 | Sent to signal that another document with different scale has been merged with the current document. |
| [c4d.MSG_SEGMENTS_CHANGED](../consts/MSG_C4DATOM_PLUGINS.md#msg-segments-changed) | 10 | Sent to notify an object that its segments have changed. |
| [c4d.MSG_SMALLUPDATE](../consts/MSG_C4DATOM_PLUGINS.md#msg-smallupdate) | 6 | Sent if part of an object has changed and does not need cache rebuilding. |
| [c4d.MSG_UPDATE](../consts/MSG_C4DATOM_PLUGINS.md#msg-update) | 5 | Sent to inform an object that its bounding box must be recalculated. Otherwise use [MSG_CHANGE](../consts/MSG_C4DATOM_PLUGINS.md#msg-change). |

## See Also <a id="see-also"></a>

- [Input Events](manual_input_events.md): Input events are messages about input from the keyboard or from the mouse.
- [Implementing Plugins](manual_implementing_plugins.md): Explains the basic concepts of implementing plugins.
- [Scene Execution](manual_scene_execution.md): Explains how Cinema 4D updates a scene, and where Python code runs in that process.
