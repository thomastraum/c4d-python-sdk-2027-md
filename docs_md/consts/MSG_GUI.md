<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/MSG_GUI.html -->

# GUI Messages <a id="gui-messages"></a>

The following messages can be received in the message methods of [`c4d.gui.GeDialog`](../modules/c4d.gui/GeDialog/index.md#c4d.gui.GeDialog) and [`c4d.gui.GeUserArea`](../modules/c4d.gui/GeUserArea/index.md#c4d.gui.GeUserArea).

Refer to [Message System](../manuals/manual_message_system.md#manual-message-system) for details on the message system of Cinema 4D.

| Symbol | Numeric Value | Description |
|---|---|---|
| [c4d.BFM_ACTION](#bfm-action) | 1648444244 | One of the child elements made action. |
| [c4d.BFM_ACTION_ESC](#bfm-action-esc) | 1634038627 | *Internal* |
| [c4d.BFM_ACTION_ID](#bfm-action-id) | 1835362660 | ID of the dialog element that triggered the action. |
| [c4d.BFM_ACTION_INDRAG](#bfm-action-indrag) | 1835361394 | Slider in dragging mode (not finished). |
| [c4d.BFM_ACTION_KEYDOWN](#bfm-action-keydown) | 1801812324 | Key Down pressed while editfield is active. |
| [c4d.BFM_ACTION_KEYUP](#bfm-action-keyup) | 1801812341 | Key Up pressed while editfield is active. |
| [c4d.BFM_ACTION_RESET](#bfm-action-reset) | 1634887027 | Reset to default value on right-click of input field arrows. |
| [c4d.BFM_ACTION_STRCHG](#bfm-action-strchg) | 1835365236 | String in text field changed. |
| [c4d.BFM_ACTION_UPDATE](#bfm-action-update) | 1970300020 | *Internal* |
| [c4d.BFM_ACTION_VALCHG](#bfm-action-valchg) | 1986226279 | Edit/slider changed. |
| [c4d.BFM_ACTION_VALUE](#bfm-action-value) | 1835365985 | GeData Action value. |
| [c4d.BFM_ACTIVATE_WINDOW](#bfm-activate-window) | 2002871156 | *Private* |
| [c4d.BFM_ACTIVE](#bfm-active) | 1633907830 | *Private* |
| [c4d.BFM_ACTIVE_CHG](#bfm-active-chg) | 1648444231 | *Private* |
| [c4d.BFM_ADJUSTSIZE](#bfm-adjustsize) | 1715553354 | *Private* |
| [c4d.BFM_ADJUSTSIZE_HEIGHT](#bfm-adjustsize-height) | 4 | *Private* |
| [c4d.BFM_ADJUSTSIZE_LEFT](#bfm-adjustsize-left) | 1 | *Private* |
| [c4d.BFM_ADJUSTSIZE_TOP](#bfm-adjustsize-top) | 2 | *Private* |
| [c4d.BFM_ADJUSTSIZE_WIDTH](#bfm-adjustsize-width) | 3 | *Private* |
| [c4d.BFM_ASK_TABSWITCH](#bfm-ask-tabswitch) | 1937006946 | *Internal* |
| [c4d.BFM_ASKCLOSE](#bfm-askclose) | 1634954083 | Ask if a dialog is able to close. Return false it is OK to close, otherwise true. |
| [c4d.BFM_CALCSIZE](#bfm-calcsize) | 1648574803 | Called if the element has to calculate its own minimum X and Y dimensions. |
| [c4d.BFM_CHECKCLOSE](#bfm-checkclose) | 1667787619 | Check if a dialog is able to close. Return false it is OK to close, otherwise true. |
| [c4d.BFM_CHECKCLOSE_LAYOUTSWITCH](#bfm-checkclose-layoutswitch) | 1667460204 | Check if a dialog is able to close when layouts are switched. Return false it is OK to close, otherwise true. |
| [c4d.BFM_CHILD_ID](#bfm-child-id) | 1 | *Private* |
| [c4d.BFM_CHILD_REMOVED](#bfm-child-removed) | 1649567085 | *Private* |
| [c4d.BFM_CLEARFOCUS](#bfm-clearfocus) | 1648576067 | *Private* |
| [c4d.BFM_CLOSEWINDOW](#bfm-closewindow) | 1668050803 | *Internal* |
| [c4d.BFM_COLORCHOOSER](#bfm-colorchooser) | 1668246595 | Color chooser settings: |
| [c4d.BFM_COLORCHOOSER_PARENTMESSAGE](#bfm-colorchooser-parentmessage) | 1668246608 | Color chooser parent message. |
| [c4d.BFM_COLORCHOOSER_RGB_RANGE](#bfm-colorchooser-rgb-range) | 2 | RGB range: COLORSYSTEM_RANGE |
| [c4d.BFM_COLORCHOOSER_SYSTEMMESSAGE](#bfm-colorchooser-systemmessage) | 5 | Sends a parent message BFM_COLORCHOOSER_PARENTMESSAGE if the settings change. |
| [c4d.BFM_COMMANDSCHANGED](#bfm-commandschanged) | 1668113256 | *Private* |
| [c4d.BFM_CORE_ID](#bfm-core-id) | 1298360649 | Core message ID. |
| [c4d.BFM_CORE_MESSAGE](#bfm-core-message) | 1298360653 | Core message. |
| [c4d.BFM_CORE_PAR1](#bfm-core-par1) | 1298360625 | Parameter 1. |
| [c4d.BFM_CORE_PAR2](#bfm-core-par2) | 1298360626 | Parameter 2. |
| [c4d.BFM_CORE_SPECIALCOREID](#bfm-core-specialcoreid) | 1935894884 | Special manager ID for sync message. |
| [c4d.BFM_CORE_UNIQUEID](#bfm-core-uniqueid) | 1299540324 | Time stamp. |
| [c4d.BFM_CORE_UPDATEACTIVECOMMANDS](#bfm-core-updateactivecommands) | 1970300001 | *Private* |
| [c4d.BFM_CORE_UPDATECOMMANDS](#bfm-core-updatecommands) | 1970300003 | *Internal* |
| [c4d.BFM_CURSORINFO_REMOVE](#bfm-cursorinfo-remove) | 1667854957 | Sent when mouse cursor has left a user area. |
| [c4d.BFM_DESTINATION_GROUP](#bfm-destination-group) | 1734636404 | *Internal* |
| [c4d.BFM_DESTROY](#bfm-destroy) | 1685288057 | Sent just before the window is destroyed. |
| [c4d.BFM_DISABLE](#bfm-disable) | 1648650611 | *Internal* |
| [c4d.BFM_DRAG_DATA_](#bfm-drag-data) | 2 | *Internal* |
| [c4d.BFM_DRAG_DATA_NEW](#bfm-drag-data-new) | 9 | *Internal* |
| [c4d.BFM_DRAG_ESC](#bfm-drag-esc) | 10 | Drag escaped. |
| [c4d.BFM_DRAG_FINISHED](#bfm-drag-finished) | 5 | Drag finished. |
| [c4d.BFM_DRAG_LOST](#bfm-drag-lost) | 7 | Drag lost. |
| [c4d.BFM_DRAG_SCREENX](#bfm-drag-screenx) | 3 | Screen X. |
| [c4d.BFM_DRAG_SCREENY](#bfm-drag-screeny) | 4 | Screen Y. |
| [c4d.BFM_DRAG_TYPE_NEW](#bfm-drag-type-new) | 8 | Drag type: DRAGTYPE |
| [c4d.BFM_DRAGAUTOSCROLL](#bfm-dragautoscroll) | 10005 | *Internal* |
| [c4d.BFM_DRAGEND](#bfm-dragend) | 10004 | *Internal* |
| [c4d.BFM_DRAGRECEIVE](#bfm-dragreceive) | 10003 | Drag receive. |
| [c4d.BFM_DRAGSTART](#bfm-dragstart) | 10001 | *Internal* |
| [c4d.BFM_DRAW](#bfm-draw) | 1648644673 | Redraw message for user areas. |
| [c4d.BFM_DRAW_BOTTOM](#bfm-draw-bottom) | 4 | Bottom clipping. |
| [c4d.BFM_DRAW_HASRECT](#bfm-draw-hasrect) | 5 | *Internal* |
| [c4d.BFM_DRAW_LEFT](#bfm-draw-left) | 1 | Left clipping. |
| [c4d.BFM_DRAW_OGL](#bfm-draw-ogl) | 6 | *Internal* |
| [c4d.BFM_DRAW_REASON](#bfm-draw-reason) | 7 | BaseContainer Message which started the redraw. |
| [c4d.BFM_DRAW_RIGHT](#bfm-draw-right) | 3 | Right clipping. |
| [c4d.BFM_DRAW_TOP](#bfm-draw-top) | 2 | Top clipping. |
| [c4d.BFM_DRAWUSERITEM](#bfm-drawuseritem) | 1970500196 | *Private* |
| [c4d.BFM_DRAWUSERITEM_ID](#bfm-drawuseritem-id) | 1 | *Internal* |
| [c4d.BFM_EDITFIELD_FLUSHUNDO](#bfm-editfield-flushundo) | 1718383982 | Flushes the undo stack for a multi-line edit text. |
| [c4d.BFM_EDITFIELD_GETBLOCKSTART](#bfm-editfield-getblockstart) | 1734702178 | Returns the block start position in an edit field. |
| [c4d.BFM_EDITFIELD_GETCURSORPOS](#bfm-editfield-getcursorpos) | 1734702179 | Return the cursor position in an edit field. |
| [c4d.BFM_EDITFIELD_GETUNDOSTATS](#bfm-editfield-getundostats) | 1970172788 | *Internal* |
| [c4d.BFM_EDITFIELD_RESTOREUNDO](#bfm-editfield-restoreundo) | 1920169077 | Restore the undo container for a multi-line edit text. |
| [c4d.BFM_EDITFIELD_SETCURSORPOS](#bfm-editfield-setcursorpos) | 1936028771 | Set the cursor position in an edit field. |
| [c4d.BFM_EDITFIELD_STOREUNDO](#bfm-editfield-storeundo) | 1937011317 | Stores the undo container for a multi-line edit text. |
| [c4d.BFM_EDITFIELD_UNDOSTAT_COUNT](#bfm-editfield-undostat-count) | 1 | The undo stack size. |
| [c4d.BFM_EDITFIELD_UNDOSTAT_UNDOLEVEL](#bfm-editfield-undostat-undolevel) | 2 | The current undo level. |
| [c4d.BFM_ENABLE](#bfm-enable) | 1648717409 | *Internal* |
| [c4d.BFM_FADE](#bfm-fade) | 1717658725 | Sent to blend GUI color with ease in a GeUserArea. |
| [c4d.BFM_FADE_REMOVEALL](#bfm-fade-removeall) | 1178682437 | *Private* |
| [c4d.BFM_FULLSCREENMODE_OFF](#bfm-fullscreenmode-off) | 1718971440 | *Internal* |
| [c4d.BFM_FULLSCREENMODE_ON](#bfm-fullscreenmode-on) | 1718971441 | *Internal* |
| [c4d.BFM_GET_FOCUS_RECTANGLE](#bfm-get-focus-rectangle) | 1734759011 | Returns the coordinates of the input field with the current focus. |
| [c4d.BFM_GET_FOCUS_RECTANGLE_H](#bfm-get-focus-rectangle-h) | 3 | Input field height. |
| [c4d.BFM_GET_FOCUS_RECTANGLE_W](#bfm-get-focus-rectangle-w) | 2 | Input field width. |
| [c4d.BFM_GET_FOCUS_RECTANGLE_X](#bfm-get-focus-rectangle-x) | 0 | Input field X coordinate. |
| [c4d.BFM_GET_FOCUS_RECTANGLE_Y](#bfm-get-focus-rectangle-y) | 1 | Input field Y coordinate. |
| [c4d.BFM_GETACTIVETABTITLE](#bfm-getactivetabtitle) | 1952539508 | *Private* |
| [c4d.BFM_GETCURSORINFO](#bfm-getcursorinfo) | 1667853926 | Respond this message to display help information in the bubble help or global status-bar. |
| [c4d.BFM_GETCUSTOMGUILAYOUTDATA](#bfm-getcustomguilayoutdata) | 1818327367 | *Private* |
| [c4d.BFM_GETFOCUSBEFOREUPDATE](#bfm-getfocusbeforeupdate) | 1648838229 | A custom GUI receives this message before the layout is updated. This is used to avoid losing the focus over a specific gadget after the layout is updated. |
| [c4d.BFM_GETINFO](#bfm-getinfo) | 1648979558 | *Private* |
| [c4d.BFM_GETPARENT_MANAGER_ID](#bfm-getparent-manager-id) | 1735420260 | *Private* |
| [c4d.BFM_GETVALUE](#bfm-getvalue) | 1733706060 | *Private* |
| [c4d.BFM_GETVIEWPANELDATA](#bfm-getviewpaneldata) | 1987077236 | *Private* |
| [c4d.BFM_GETVISIBLE_HEIGHT](#bfm-getvisible-height) | 10014 | *Private* |
| [c4d.BFM_GETVISIBLE_WIDTH](#bfm-getvisible-width) | 10013 | *Private* |
| [c4d.BFM_GETVISIBLE_XOFF](#bfm-getvisible-xoff) | 10011 | *Private* |
| [c4d.BFM_GETVISIBLE_YOFF](#bfm-getvisible-yoff) | 10012 | *Private* |
| [c4d.BFM_GOTFOCUS](#bfm-gotfocus) | 1648838211 | Item got the focus. |
| [c4d.BFM_GUIPREFSCHANGED](#bfm-guiprefschanged) | 1735418728 | *Private* |
| [c4d.BFM_IDCHNG](#bfm-idchng) | 1648968771 | *Private* |
| [c4d.BFM_INIT](#bfm-init) | 1648971337 | Sent after an element has been created. |
| [c4d.BFM_INITVALUES](#bfm-initvalues) | 1649822030 | Sent after the layout is done. |
| [c4d.BFM_INPUT](#bfm-input) | 1648971854 | A dialog/user area receives this message if mouse or keyboard input is received. See Input Events for more information. |
| [c4d.BFM_INPUT_AFTER_SCROLL](#bfm-input-after-scroll) | 1648968019 | Input message ID sent after scroll area processed input messages. |
| [c4d.BFM_INPUT_ASC](#bfm-input-asc) | 1801548643 | String Contains the Unicode input from keyboard. |
| [c4d.BFM_INPUT_CHANNEL](#bfm-input-channel) | 1768973153 | Contains the key or mouse button. See also KEY. |
| [c4d.BFM_INPUT_DEVICE](#bfm-input-device) | 1768973430 | Device: |
| [c4d.BFM_INPUT_DOUBLECLICK](#bfm-input-doubleclick) | 1768973410 | Double click. |
| [c4d.BFM_INPUT_FINGERWHEEL](#bfm-input-fingerwheel) | 1768320615 | Finger wheel (tangential pen pressure). |
| [c4d.BFM_INPUT_HSCROLL](#bfm-input-hscroll) | 1768452963 | Amount of horizontal scrolling (touch pad, mouse ball) |
| [c4d.BFM_INPUT_KEYBOARD](#bfm-input-keyboard) | 1801812322 | Keyboard. |
| [c4d.BFM_INPUT_MAGNIFY](#bfm-input-magnify) | 102 | Zoom gesture on touch pad or touch screen (or mouse scroll with ctrl to indicate zoom). Value in BFM_INPUT_VALUE_REAL. |
| [c4d.BFM_INPUT_MODIFIERS](#bfm-input-modifiers) | 1768975727 | *Private* |
| [c4d.BFM_INPUT_MOUSE](#bfm-input-mouse) | 1836021107 | Mouse. |
| [c4d.BFM_INPUT_MOUSELEFT](#bfm-input-mouseleft) | 1 | Left mouse button. |
| [c4d.BFM_INPUT_MOUSEMIDDLE](#bfm-input-mousemiddle) | 3 | Middle mouse button. |
| [c4d.BFM_INPUT_MOUSEMOVE](#bfm-input-mousemove) | 101 | Mouse move. |
| [c4d.BFM_INPUT_MOUSERIGHT](#bfm-input-mouseright) | 2 | Right mouse button. |
| [c4d.BFM_INPUT_MOUSEWHEEL](#bfm-input-mousewheel) | 100 | Mouse wheel or panning on touch pad or touch screen. Values in BFM_INPUT_HSCROLL, BFM_INPUT_VSCROLL. |
| [c4d.BFM_INPUT_MOUSEX1](#bfm-input-mousex1) | 5 | Fourth mouse button. |
| [c4d.BFM_INPUT_MOUSEX2](#bfm-input-mousex2) | 6 | Five mouse button. |
| [c4d.BFM_INPUT_MULTITOUCHSCROLL](#bfm-input-multitouchscroll) | 1768780643 | True for scroll events on a multi-touch device (which also supports magnify), false for scroll-only mice. |
| [c4d.BFM_INPUT_ORIENTATION](#bfm-input-orientation) | 1769107316 | Pen rotation. |
| [c4d.BFM_INPUT_P_ROTATION](#bfm-input-p-rotation) | 1886547828 | Pen rotation around its own axis. |
| [c4d.BFM_INPUT_QUALIFIER](#bfm-input-qualifier) | 1768976737 | A bit mask with the qualifiers at the time when the event occurred: QUALIFIER |
| [c4d.BFM_INPUT_TILT](#bfm-input-tilt) | 1769237620 | Pen tilt. |
| [c4d.BFM_INPUT_TIMESTAMP](#bfm-input-timestamp) | 1769237875 | Time stamp of the event or 0.0 (unavailable). |
| [c4d.BFM_INPUT_VALUE](#bfm-input-value) | 1768978017 | Value of the input channel (true/false or a value, e.g. for scroll wheel data). |
| [c4d.BFM_INPUT_VALUE_REAL](#bfm-input-value-real) | 1768977985 | Channel value (e.g. pen pressure). |
| [c4d.BFM_INPUT_VSCROLL](#bfm-input-vscroll) | 1769370467 | Amount of vertical scrolling (touch pad, mouse wheel/ball) |
| [c4d.BFM_INPUT_WHEELSCROLL](#bfm-input-wheelscroll) | 1769436003 | True for scroll events on a classic wheel mouse. False for everything else (touch pad, magic mouse). |
| [c4d.BFM_INPUT_X](#bfm-input-x) | 1768978040 | X value. |
| [c4d.BFM_INPUT_Y](#bfm-input-y) | 1768978041 | Y value. |
| [c4d.BFM_INPUT_Z](#bfm-input-z) | 1768978042 | Z value. |
| [c4d.BFM_INTERACTEND](#bfm-interactend) | 1768846437 | Sent when user interaction ends. |
| [c4d.BFM_INTERACTSTART](#bfm-interactstart) | 1768846433 | Sent when user interaction starts. |
| [c4d.BFM_ISACTIVE](#bfm-isactive) | 1767990132 | *Private* |
| [c4d.BFM_LAYOUT_CHANGED](#bfm-layout-changed) | 1716273497 | *Internal* |
| [c4d.BFM_LAYOUT_GETDATA](#bfm-layout-getdata) | 1818327399 | Sent when saving the layout. Return a container to store with the layout for this dialog. |
| [c4d.BFM_LAYOUT_SETDATA](#bfm-layout-setdata) | 1818327411 | Receive the container saved with BFM_LAYOUT_GETDATA when loading a layout. |
| [c4d.BFM_LOSTFOCUS](#bfm-lostfocus) | 1649165891 | Item lost the focus. |
| [c4d.BFM_MANAGER_ID](#bfm-manager-id) | 2 | *Internal* |
| [c4d.BFM_MARKFOCUS](#bfm-markfocus) | 1649231427 | *Private* |
| [c4d.BFM_MARKFORCELAYOUT](#bfm-markforcelayout) | 1835755116 | *Private* |
| [c4d.BFM_MAXCHNG](#bfm-maxchng) | 1649230147 | *Private* |
| [c4d.BFM_MENU_CHECK](#bfm-menu-check) | 4 | *Internal* |
| [c4d.BFM_MENU_OFF](#bfm-menu-off) | 2 | *Internal* |
| [c4d.BFM_MENU_ON](#bfm-menu-on) | 1 | *Internal* |
| [c4d.BFM_MENU_SET](#bfm-menu-set) | 10000 | *Private* |
| [c4d.BFM_MENU_UNCHECK](#bfm-menu-uncheck) | 8 | *Internal* |
| [c4d.BFM_MENUFINDER](#bfm-menufinder) | 1718185572 | *Private* |
| [c4d.BFM_MINCHNG](#bfm-minchng) | 1649232195 | *Private* |
| [c4d.BFM_MOVEFOCUSNEXT](#bfm-movefocusnext) | 1648774744 | *Private* |
| [c4d.BFM_MOVEFOCUSPREV](#bfm-movefocusprev) | 1648775250 | *Private* |
| [c4d.BFM_OPTIMIZE](#bfm-optimize) | 1869640809 | *Private* |
| [c4d.BFM_PARENT_TITLECHNG](#bfm-parent-titlechng) | 1886545262 | *Internal* |
| [c4d.BFM_POPUPNOTIFY](#bfm-popupnotify) | 1886351470 | Notification of popup before the menu opens. |
| [c4d.BFM_REDRAW_EDITMODE](#bfm-redraw-editmode) | 1685546340 | *Private* |
| [c4d.BFM_RELOAD_MENUS](#bfm-reload-menus) | 1818520942 | *Private* |
| [c4d.BFM_REMOVE_DIALOG](#bfm-remove-dialog) | 1649558861 | *Internal* |
| [c4d.BFM_RENAMEWINDOW](#bfm-renamewindow) | 2003985774 | *Internal* |
| [c4d.BFM_REQUIRESRESULT](#bfm-requiresresult) | 1919250802 | Set to true in the passed container for `GeDialog.SendMessage()` to return a value from the message. |
| [c4d.BFM_SCROLLAREA](#bfm-scrollarea) | 10010 | *Internal* |
| [c4d.BFM_SCROLLGROUP_OFFSETCHANGED](#bfm-scrollgroup-offsetchanged) | 1666139718 | *Internal* |
| [c4d.BFM_SCROLLGROUP_SCALE](#bfm-scrollgroup-scale) | 1935897443 | *Private* |
| [c4d.BFM_SCROLLGROUP_SCROLLED](#bfm-scrollgroup-scrolled) | 1935897203 | Scroll group scrolled. |
| [c4d.BFM_SCROLLX](#bfm-scrollx) | 1 | *Internal* |
| [c4d.BFM_SCROLLY](#bfm-scrolly) | 2 | *Internal* |
| [c4d.BFM_SET_MSG_BITMASK](#bfm-set-msg-bitmask) | 1651078253 | *Private* |
| [c4d.BFM_SETACTIVE](#bfm-setactive) | 1649623363 | *Private* |
| [c4d.BFM_SETACTIVE_DATA](#bfm-setactive-data) | 1649623363 | *Private* |
| [c4d.BFM_SETCURSORINFO](#bfm-setcursorinfo) | 1936028771 | Same as BFM_EDITFIELD_SETCURSORPOS. |
| [c4d.BFM_SETFIRSTFOCUS](#bfm-setfirstfocus) | 1649624646 | *Internal* |
| [c4d.BFM_SETFOCUS](#bfm-setfocus) | 1649624643 | *Internal* |
| [c4d.BFM_SETFOCUSAFTERUPDATE](#bfm-setfocusafterupdate) | 1649624661 | A custom GUI description receives this message after the layout is updated to reactivate previously focused gadget. |
| [c4d.BFM_SETLASTFOCUS](#bfm-setlastfocus) | 1649626182 | *Private* |
| [c4d.BFM_SETMAINTITLE](#bfm-setmaintitle) | 1836345716 | *Private* |
| [c4d.BFM_SETSPECIALMULTI](#bfm-setspecialmulti) | 1397969747 | *Private* |
| [c4d.BFM_SETSPECIALMULTID](#bfm-setspecialmultid) | 1397969732 | *Private* |
| [c4d.BFM_SETSTATUSBAR](#bfm-setstatusbar) | 1937006964 | Sets a status-bar. |
| [c4d.BFM_SETVIEWPANELLAYOUT](#bfm-setviewpanellayout) | 1987081068 | *Private* |
| [c4d.BFM_SETVIEWPORTORIGIN](#bfm-setviewportorigin) | 1666142791 | *Internal* |
| [c4d.BFM_SETVIEWPORTORIGIN_X](#bfm-setviewportorigin-x) | 1 | *Internal* |
| [c4d.BFM_SETVIEWPORTORIGIN_Y](#bfm-setviewportorigin-y) | 2 | *Internal* |
| [c4d.BFM_SETVIEWPORTSIZE](#bfm-setviewportsize) | 1666402650 | *Private* |
| [c4d.BFM_SHOW_AREA](#bfm-show-area) | 1935766117 | *Internal* |
| [c4d.BFM_SHOW_FRAME](#bfm-show-frame) | 1933996653 | *Internal* |
| [c4d.BFM_SHOW_ID](#bfm-show-id) | 1 | *Internal* |
| [c4d.BFM_SIZED](#bfm-sized) | 1648972617 | Element has been sized. |
| [c4d.BFM_SPECIALGETSTRING](#bfm-specialgetstring) | 1735684980 | *Private* |
| [c4d.BFM_SPECIALMODE](#bfm-specialmode) | 1936879213 | Set the multi-line edit field to the right language mode. |
| [c4d.BFM_SPECIALSETRANGE](#bfm-specialsetrange) | 1936879207 | *Private* |
| [c4d.BFM_STATUSBAR_HELP](#bfm-statusbar-help) | 5 | Help second text. |
| [c4d.BFM_STATUSBAR_NETPROGRESS](#bfm-statusbar-netprogress) | 11 | *Internal* |
| [c4d.BFM_STATUSBAR_NETPROGRESSON](#bfm-statusbar-netprogresson) | 9 | *Internal* |
| [c4d.BFM_STATUSBAR_NETPROGRESSSPIN](#bfm-statusbar-netprogressspin) | 12 | *Internal* |
| [c4d.BFM_STATUSBAR_NETTINT_COLOR](#bfm-statusbar-nettint-color) | 8 | *Internal* |
| [c4d.BFM_STATUSBAR_NETTXT](#bfm-statusbar-nettxt) | 10 | *Internal* |
| [c4d.BFM_STATUSBAR_PROGRESS](#bfm-statusbar-progress) | 3 | Between 0.0 and 1.0. |
| [c4d.BFM_STATUSBAR_PROGRESSFULLSIZE](#bfm-statusbar-progressfullsize) | 6 | *Internal* |
| [c4d.BFM_STATUSBAR_PROGRESSON](#bfm-statusbar-progresson) | 1 | Status-bar active. |
| [c4d.BFM_STATUSBAR_PROGRESSSPIN](#bfm-statusbar-progressspin) | 4 | Spinning bar. |
| [c4d.BFM_STATUSBAR_TINT_COLOR](#bfm-statusbar-tint-color) | 7 | Color ID for the status-bar, or as RGB value (Vector). |
| [c4d.BFM_STATUSBAR_TXT](#bfm-statusbar-txt) | 2 | Help first text. |
| [c4d.BFM_STORE_WEIGHTS](#bfm-store-weights) | 1937012583 | *Private* |
| [c4d.BFM_SYNC_MESSAGE](#bfm-sync-message) | 1937337955 | Sync message. |
| [c4d.BFM_TESTONLY](#bfm-testonly) | 1952805748 | *Private* |
| [c4d.BFM_TIMER_MESSAGE](#bfm-timer-message) | 10020 | Timer message. Use `GeDialog.SetTimer()` / `GeUserArea.SetTimer()` to set the periodical time. |
| [c4d.BFM_TITLECHNG](#bfm-titlechng) | 1649690947 | *Private* |
| [c4d.BFM_UPDATE_REGION](#bfm-update-region) | 1970303591 | *Private* |
| [c4d.BFM_VALUEADD](#bfm-valueadd) | 1649819972 | *Private* |
| [c4d.BFM_VALUECHNG](#bfm-valuechng) | 1649819971 | *Private* |
| [c4d.BFM_VALUESUB](#bfm-valuesub) | 1649824578 | *Private* |
| [c4d.BFM_VISIBLE_OFF](#bfm-visible-off) | 1986622278 | *Internal* |
| [c4d.BFM_VISIBLE_ON](#bfm-visible-on) | 1986622292 | *Internal* |
| [c4d.BFM_VPD_LAYOUTTYPE](#bfm-vpd-layouttype) | 1987079284 | *Private* |
| [c4d.BFM_VPD_MAXIMIZED](#bfm-vpd-maximized) | 1987079544 | *Private* |
| [c4d.BFM_VPD_PANELID](#bfm-vpd-panelid) | 1987078500 | *Private* |
| [c4d.BFM_WEIGHTS_CHANGED](#bfm-weights-changed) | 2000906343 | Group weights changed. |

## `c4d.BFM_ACTION` <a id="c4d.BFM_ACTION"></a> <a id="bfm-action"></a>

One of the child elements made action.

## `c4d.BFM_ACTION_ESC` <a id="c4d.BFM_ACTION_ESC"></a> <a id="bfm-action-esc"></a>

*Internal*

## `c4d.BFM_ACTION_ID` <a id="c4d.BFM_ACTION_ID"></a> <a id="bfm-action-id"></a>

ID of the dialog element that triggered the action.

## `c4d.BFM_ACTION_INDRAG` <a id="c4d.BFM_ACTION_INDRAG"></a> <a id="bfm-action-indrag"></a>

Slider in dragging mode (not finished).

## `c4d.BFM_ACTION_KEYDOWN` <a id="c4d.BFM_ACTION_KEYDOWN"></a> <a id="bfm-action-keydown"></a>

Key Down pressed while editfield is active.

## `c4d.BFM_ACTION_KEYUP` <a id="c4d.BFM_ACTION_KEYUP"></a> <a id="bfm-action-keyup"></a>

Key Up pressed while editfield is active.

## `c4d.BFM_ACTION_RESET` <a id="c4d.BFM_ACTION_RESET"></a> <a id="bfm-action-reset"></a>

Reset to default value on right-click of input field arrows.

## `c4d.BFM_ACTION_STRCHG` <a id="c4d.BFM_ACTION_STRCHG"></a> <a id="bfm-action-strchg"></a>

String in text field changed.

## `c4d.BFM_ACTION_UPDATE` <a id="c4d.BFM_ACTION_UPDATE"></a> <a id="bfm-action-update"></a>

*Internal*

## `c4d.BFM_ACTION_VALCHG` <a id="c4d.BFM_ACTION_VALCHG"></a> <a id="bfm-action-valchg"></a>

Edit/slider changed.

## `c4d.BFM_ACTION_VALUE` <a id="c4d.BFM_ACTION_VALUE"></a> <a id="bfm-action-value"></a>

GeData Action value.

## `c4d.BFM_ACTIVATE_WINDOW` <a id="c4d.BFM_ACTIVATE_WINDOW"></a> <a id="bfm-activate-window"></a>

*Private*

## `c4d.BFM_ACTIVE` <a id="c4d.BFM_ACTIVE"></a> <a id="bfm-active"></a>

*Private*

## `c4d.BFM_ACTIVE_CHG` <a id="c4d.BFM_ACTIVE_CHG"></a> <a id="bfm-active-chg"></a>

*Private*

## `c4d.BFM_ADJUSTSIZE` <a id="c4d.BFM_ADJUSTSIZE"></a> <a id="bfm-adjustsize"></a>

*Private*

## `c4d.BFM_ADJUSTSIZE_HEIGHT` <a id="c4d.BFM_ADJUSTSIZE_HEIGHT"></a> <a id="bfm-adjustsize-height"></a>

*Private*

## `c4d.BFM_ADJUSTSIZE_LEFT` <a id="c4d.BFM_ADJUSTSIZE_LEFT"></a> <a id="bfm-adjustsize-left"></a>

*Private*

## `c4d.BFM_ADJUSTSIZE_TOP` <a id="c4d.BFM_ADJUSTSIZE_TOP"></a> <a id="bfm-adjustsize-top"></a>

*Private*

## `c4d.BFM_ADJUSTSIZE_WIDTH` <a id="c4d.BFM_ADJUSTSIZE_WIDTH"></a> <a id="bfm-adjustsize-width"></a>

*Private*

## `c4d.BFM_ASK_TABSWITCH` <a id="c4d.BFM_ASK_TABSWITCH"></a> <a id="bfm-ask-tabswitch"></a>

*Internal*

## `c4d.BFM_ASKCLOSE` <a id="c4d.BFM_ASKCLOSE"></a> <a id="bfm-askclose"></a>

Ask if a dialog is able to close. Return false it is OK to close, otherwise true.

## `c4d.BFM_CALCSIZE` <a id="c4d.BFM_CALCSIZE"></a> <a id="bfm-calcsize"></a>

Called if the element has to calculate its own minimum X and Y dimensions.

## `c4d.BFM_CHECKCLOSE` <a id="c4d.BFM_CHECKCLOSE"></a> <a id="bfm-checkclose"></a>

Check if a dialog is able to close. Return false it is OK to close, otherwise true.

## `c4d.BFM_CHECKCLOSE_LAYOUTSWITCH` <a id="c4d.BFM_CHECKCLOSE_LAYOUTSWITCH"></a> <a id="bfm-checkclose-layoutswitch"></a>

Check if a dialog is able to close when layouts are switched. Return false it is OK to close, otherwise true.

## `c4d.BFM_CHILD_ID` <a id="c4d.BFM_CHILD_ID"></a> <a id="bfm-child-id"></a>

*Private*

## `c4d.BFM_CHILD_REMOVED` <a id="c4d.BFM_CHILD_REMOVED"></a> <a id="bfm-child-removed"></a>

*Private*

## `c4d.BFM_CLEARFOCUS` <a id="c4d.BFM_CLEARFOCUS"></a> <a id="bfm-clearfocus"></a>

*Private*

## `c4d.BFM_CLOSEWINDOW` <a id="c4d.BFM_CLOSEWINDOW"></a> <a id="bfm-closewindow"></a>

*Internal*

## `c4d.BFM_COLORCHOOSER` <a id="c4d.BFM_COLORCHOOSER"></a> <a id="bfm-colorchooser"></a>

Color chooser settings:

## `c4d.BFM_COLORCHOOSER_PARENTMESSAGE` <a id="c4d.BFM_COLORCHOOSER_PARENTMESSAGE"></a> <a id="bfm-colorchooser-parentmessage"></a>

Color chooser parent message.

## `c4d.BFM_COLORCHOOSER_RGB_RANGE` <a id="c4d.BFM_COLORCHOOSER_RGB_RANGE"></a> <a id="bfm-colorchooser-rgb-range"></a>

RGB range: COLORSYSTEM_RANGE

## `c4d.BFM_COLORCHOOSER_SYSTEMMESSAGE` <a id="c4d.BFM_COLORCHOOSER_SYSTEMMESSAGE"></a> <a id="bfm-colorchooser-systemmessage"></a>

Sends a parent message BFM_COLORCHOOSER_PARENTMESSAGE if the settings change.

## `c4d.BFM_COMMANDSCHANGED` <a id="c4d.BFM_COMMANDSCHANGED"></a> <a id="bfm-commandschanged"></a>

*Private*

## `c4d.BFM_CORE_ID` <a id="c4d.BFM_CORE_ID"></a> <a id="bfm-core-id"></a>

Core message ID.

## `c4d.BFM_CORE_MESSAGE` <a id="c4d.BFM_CORE_MESSAGE"></a> <a id="bfm-core-message"></a>

Core message.

## `c4d.BFM_CORE_PAR1` <a id="c4d.BFM_CORE_PAR1"></a> <a id="bfm-core-par1"></a>

Parameter 1.

## `c4d.BFM_CORE_PAR2` <a id="c4d.BFM_CORE_PAR2"></a> <a id="bfm-core-par2"></a>

Parameter 2.

## `c4d.BFM_CORE_SPECIALCOREID` <a id="c4d.BFM_CORE_SPECIALCOREID"></a> <a id="bfm-core-specialcoreid"></a>

Special manager ID for sync message.

## `c4d.BFM_CORE_UNIQUEID` <a id="c4d.BFM_CORE_UNIQUEID"></a> <a id="bfm-core-uniqueid"></a>

Time stamp.

## `c4d.BFM_CORE_UPDATEACTIVECOMMANDS` <a id="c4d.BFM_CORE_UPDATEACTIVECOMMANDS"></a> <a id="bfm-core-updateactivecommands"></a>

*Private*

## `c4d.BFM_CORE_UPDATECOMMANDS` <a id="c4d.BFM_CORE_UPDATECOMMANDS"></a> <a id="bfm-core-updatecommands"></a>

*Internal*

## `c4d.BFM_CURSORINFO_REMOVE` <a id="c4d.BFM_CURSORINFO_REMOVE"></a> <a id="bfm-cursorinfo-remove"></a>

Sent when mouse cursor has left a user area.

## `c4d.BFM_DESTINATION_GROUP` <a id="c4d.BFM_DESTINATION_GROUP"></a> <a id="bfm-destination-group"></a>

*Internal*

## `c4d.BFM_DESTROY` <a id="c4d.BFM_DESTROY"></a> <a id="bfm-destroy"></a>

Sent just before the window is destroyed.

## `c4d.BFM_DISABLE` <a id="c4d.BFM_DISABLE"></a> <a id="bfm-disable"></a>

*Internal*

## `c4d.BFM_DRAG_DATA_` <a id="c4d.BFM_DRAG_DATA_"></a> <a id="bfm-drag-data"></a>

*Internal*

## `c4d.BFM_DRAG_DATA_NEW` <a id="c4d.BFM_DRAG_DATA_NEW"></a> <a id="bfm-drag-data-new"></a>

*Internal*

## `c4d.BFM_DRAG_ESC` <a id="c4d.BFM_DRAG_ESC"></a> <a id="bfm-drag-esc"></a>

Drag escaped.

## `c4d.BFM_DRAG_FINISHED` <a id="c4d.BFM_DRAG_FINISHED"></a> <a id="bfm-drag-finished"></a>

Drag finished.

## `c4d.BFM_DRAG_LOST` <a id="c4d.BFM_DRAG_LOST"></a> <a id="bfm-drag-lost"></a>

Drag lost.

## `c4d.BFM_DRAG_SCREENX` <a id="c4d.BFM_DRAG_SCREENX"></a> <a id="bfm-drag-screenx"></a>

Screen X.

## `c4d.BFM_DRAG_SCREENY` <a id="c4d.BFM_DRAG_SCREENY"></a> <a id="bfm-drag-screeny"></a>

Screen Y.

## `c4d.BFM_DRAG_TYPE_NEW` <a id="c4d.BFM_DRAG_TYPE_NEW"></a> <a id="bfm-drag-type-new"></a>

Drag type: DRAGTYPE

## `c4d.BFM_DRAGAUTOSCROLL` <a id="c4d.BFM_DRAGAUTOSCROLL"></a> <a id="bfm-dragautoscroll"></a>

*Internal*

## `c4d.BFM_DRAGEND` <a id="c4d.BFM_DRAGEND"></a> <a id="bfm-dragend"></a>

*Internal*

## `c4d.BFM_DRAGRECEIVE` <a id="c4d.BFM_DRAGRECEIVE"></a> <a id="bfm-dragreceive"></a>

Drag receive.

## `c4d.BFM_DRAGSTART` <a id="c4d.BFM_DRAGSTART"></a> <a id="bfm-dragstart"></a>

*Internal*

## `c4d.BFM_DRAW` <a id="c4d.BFM_DRAW"></a> <a id="bfm-draw"></a>

Redraw message for user areas:

## `c4d.BFM_DRAW_BOTTOM` <a id="c4d.BFM_DRAW_BOTTOM"></a> <a id="bfm-draw-bottom"></a>

Bottom clipping.

## `c4d.BFM_DRAW_HASRECT` <a id="c4d.BFM_DRAW_HASRECT"></a> <a id="bfm-draw-hasrect"></a>

*Internal*

## `c4d.BFM_DRAW_LEFT` <a id="c4d.BFM_DRAW_LEFT"></a> <a id="bfm-draw-left"></a>

Left clipping.

## `c4d.BFM_DRAW_OGL` <a id="c4d.BFM_DRAW_OGL"></a> <a id="bfm-draw-ogl"></a>

*Internal*

## `c4d.BFM_DRAW_REASON` <a id="c4d.BFM_DRAW_REASON"></a> <a id="bfm-draw-reason"></a>

BaseContainer Message which started the redraw.

## `c4d.BFM_DRAW_RIGHT` <a id="c4d.BFM_DRAW_RIGHT"></a> <a id="bfm-draw-right"></a>

Right clipping.

## `c4d.BFM_DRAW_TOP` <a id="c4d.BFM_DRAW_TOP"></a> <a id="bfm-draw-top"></a>

Top clipping.

## `c4d.BFM_DRAWUSERITEM` <a id="c4d.BFM_DRAWUSERITEM"></a> <a id="bfm-drawuseritem"></a>

*Private*

## `c4d.BFM_DRAWUSERITEM_ID` <a id="c4d.BFM_DRAWUSERITEM_ID"></a> <a id="bfm-drawuseritem-id"></a>

*Internal*

## `c4d.BFM_EDITFIELD_FLUSHUNDO` <a id="c4d.BFM_EDITFIELD_FLUSHUNDO"></a> <a id="bfm-editfield-flushundo"></a>

Flushes the undo stack for a multi-line edit text.

## `c4d.BFM_EDITFIELD_GETBLOCKSTART` <a id="c4d.BFM_EDITFIELD_GETBLOCKSTART"></a> <a id="bfm-editfield-getblockstart"></a>

Returns the block start position in an edit field.

## `c4d.BFM_EDITFIELD_GETCURSORPOS` <a id="c4d.BFM_EDITFIELD_GETCURSORPOS"></a> <a id="bfm-editfield-getcursorpos"></a>

Return the cursor position in an edit field.

## `c4d.BFM_EDITFIELD_GETUNDOSTATS` <a id="c4d.BFM_EDITFIELD_GETUNDOSTATS"></a> <a id="bfm-editfield-getundostats"></a>

*Internal*

## `c4d.BFM_EDITFIELD_RESTOREUNDO` <a id="c4d.BFM_EDITFIELD_RESTOREUNDO"></a> <a id="bfm-editfield-restoreundo"></a>

Restore the undo container for a multi-line edit text.

## `c4d.BFM_EDITFIELD_SETCURSORPOS` <a id="c4d.BFM_EDITFIELD_SETCURSORPOS"></a> <a id="bfm-editfield-setcursorpos"></a>

Set the cursor position in an edit field.

## `c4d.BFM_EDITFIELD_STOREUNDO` <a id="c4d.BFM_EDITFIELD_STOREUNDO"></a> <a id="bfm-editfield-storeundo"></a>

Stores the undo container for a multi-line edit text.

## `c4d.BFM_EDITFIELD_UNDOSTAT_COUNT` <a id="c4d.BFM_EDITFIELD_UNDOSTAT_COUNT"></a> <a id="bfm-editfield-undostat-count"></a>

The undo stack size.

## `c4d.BFM_EDITFIELD_UNDOSTAT_UNDOLEVEL` <a id="c4d.BFM_EDITFIELD_UNDOSTAT_UNDOLEVEL"></a> <a id="bfm-editfield-undostat-undolevel"></a>

The current undo level.

## `c4d.BFM_ENABLE` <a id="c4d.BFM_ENABLE"></a> <a id="bfm-enable"></a>

*Internal*

## `c4d.BFM_FADE` <a id="c4d.BFM_FADE"></a> <a id="bfm-fade"></a>

Sent to blend GUI color with ease in a GeUserArea.

## `c4d.BFM_FADE_REMOVEALL` <a id="c4d.BFM_FADE_REMOVEALL"></a> <a id="bfm-fade-removeall"></a>

*Private*

## `c4d.BFM_FULLSCREENMODE_OFF` <a id="c4d.BFM_FULLSCREENMODE_OFF"></a> <a id="bfm-fullscreenmode-off"></a>

*Internal*

## `c4d.BFM_FULLSCREENMODE_ON` <a id="c4d.BFM_FULLSCREENMODE_ON"></a> <a id="bfm-fullscreenmode-on"></a>

*Internal*

## `c4d.BFM_GET_FOCUS_RECTANGLE` <a id="c4d.BFM_GET_FOCUS_RECTANGLE"></a> <a id="bfm-get-focus-rectangle"></a>

Returns the coordinates of the input field with the current focus.

## `c4d.BFM_GET_FOCUS_RECTANGLE_H` <a id="c4d.BFM_GET_FOCUS_RECTANGLE_H"></a> <a id="bfm-get-focus-rectangle-h"></a>

Input field height.

## `c4d.BFM_GET_FOCUS_RECTANGLE_W` <a id="c4d.BFM_GET_FOCUS_RECTANGLE_W"></a> <a id="bfm-get-focus-rectangle-w"></a>

Input field width.

## `c4d.BFM_GET_FOCUS_RECTANGLE_X` <a id="c4d.BFM_GET_FOCUS_RECTANGLE_X"></a> <a id="bfm-get-focus-rectangle-x"></a>

Input field X coordinate.

## `c4d.BFM_GET_FOCUS_RECTANGLE_Y` <a id="c4d.BFM_GET_FOCUS_RECTANGLE_Y"></a> <a id="bfm-get-focus-rectangle-y"></a>

Input field Y coordinate.

## `c4d.BFM_GETACTIVETABTITLE` <a id="c4d.BFM_GETACTIVETABTITLE"></a> <a id="bfm-getactivetabtitle"></a>

*Private*

## `c4d.BFM_GETCURSORINFO` <a id="c4d.BFM_GETCURSORINFO"></a> <a id="bfm-getcursorinfo"></a>

Respond this message to display help information in the bubble help or global status-bar.

## `c4d.BFM_GETCUSTOMGUILAYOUTDATA` <a id="c4d.BFM_GETCUSTOMGUILAYOUTDATA"></a> <a id="bfm-getcustomguilayoutdata"></a>

*Private*

## `c4d.BFM_GETFOCUSBEFOREUPDATE` <a id="c4d.BFM_GETFOCUSBEFOREUPDATE"></a> <a id="bfm-getfocusbeforeupdate"></a>

A custom GUI receives this message before the layout is updated. This is used to avoid losing the focus over a specific gadget after the layout is updated.

## `c4d.BFM_GETINFO` <a id="c4d.BFM_GETINFO"></a> <a id="bfm-getinfo"></a>

*Private*

## `c4d.BFM_GETPARENT_MANAGER_ID` <a id="c4d.BFM_GETPARENT_MANAGER_ID"></a> <a id="bfm-getparent-manager-id"></a>

*Private*

## `c4d.BFM_GETVALUE` <a id="c4d.BFM_GETVALUE"></a> <a id="bfm-getvalue"></a>

*Private*

## `c4d.BFM_GETVIEWPANELDATA` <a id="c4d.BFM_GETVIEWPANELDATA"></a> <a id="bfm-getviewpaneldata"></a>

*Private*

## `c4d.BFM_GETVISIBLE_HEIGHT` <a id="c4d.BFM_GETVISIBLE_HEIGHT"></a> <a id="bfm-getvisible-height"></a>

*Private*

## `c4d.BFM_GETVISIBLE_WIDTH` <a id="c4d.BFM_GETVISIBLE_WIDTH"></a> <a id="bfm-getvisible-width"></a>

*Private*

## `c4d.BFM_GETVISIBLE_XOFF` <a id="c4d.BFM_GETVISIBLE_XOFF"></a> <a id="bfm-getvisible-xoff"></a>

*Private*

## `c4d.BFM_GETVISIBLE_YOFF` <a id="c4d.BFM_GETVISIBLE_YOFF"></a> <a id="bfm-getvisible-yoff"></a>

*Private*

## `c4d.BFM_GOTFOCUS` <a id="c4d.BFM_GOTFOCUS"></a> <a id="bfm-gotfocus"></a>

Item got the focus.

## `c4d.BFM_GUIPREFSCHANGED` <a id="c4d.BFM_GUIPREFSCHANGED"></a> <a id="bfm-guiprefschanged"></a>

*Private*

## `c4d.BFM_IDCHNG` <a id="c4d.BFM_IDCHNG"></a> <a id="bfm-idchng"></a>

*Private*

## `c4d.BFM_INIT` <a id="c4d.BFM_INIT"></a> <a id="bfm-init"></a>

Sent after an element has been created.

## `c4d.BFM_INITVALUES` <a id="c4d.BFM_INITVALUES"></a> <a id="bfm-initvalues"></a>

Sent after the layout is done.

## `c4d.BFM_INPUT` <a id="c4d.BFM_INPUT"></a> <a id="bfm-input"></a>

A dialog/user area receives this message if mouse or keyboard input is received. See Input Events for more information.

## `c4d.BFM_INPUT_AFTER_SCROLL` <a id="c4d.BFM_INPUT_AFTER_SCROLL"></a> <a id="bfm-input-after-scroll"></a>

Input message ID sent after scroll area processed input messages.

## `c4d.BFM_INPUT_ASC` <a id="c4d.BFM_INPUT_ASC"></a> <a id="bfm-input-asc"></a>

String Contains the Unicode input from keyboard.

## `c4d.BFM_INPUT_CHANNEL` <a id="c4d.BFM_INPUT_CHANNEL"></a> <a id="bfm-input-channel"></a>

Contains the key or mouse button. See also KEY.

## `c4d.BFM_INPUT_DEVICE` <a id="c4d.BFM_INPUT_DEVICE"></a> <a id="bfm-input-device"></a>

Device:

## `c4d.BFM_INPUT_DOUBLECLICK` <a id="c4d.BFM_INPUT_DOUBLECLICK"></a> <a id="bfm-input-doubleclick"></a>

Double click.

## `c4d.BFM_INPUT_FINGERWHEEL` <a id="c4d.BFM_INPUT_FINGERWHEEL"></a> <a id="bfm-input-fingerwheel"></a>

Finger wheel (tangential pen pressure).

## `c4d.BFM_INPUT_HSCROLL` <a id="c4d.BFM_INPUT_HSCROLL"></a> <a id="bfm-input-hscroll"></a>

Amount of horizontal scrolling (touch pad, mouse ball)

## `c4d.BFM_INPUT_KEYBOARD` <a id="c4d.BFM_INPUT_KEYBOARD"></a> <a id="bfm-input-keyboard"></a>

Keyboard.

## `c4d.BFM_INPUT_MAGNIFY` <a id="c4d.BFM_INPUT_MAGNIFY"></a> <a id="bfm-input-magnify"></a>

Zoom gesture on touch pad or touch screen (or mouse scroll with ctrl to indicate zoom). Value in BFM_INPUT_VALUE_REAL.

## `c4d.BFM_INPUT_MODIFIERS` <a id="c4d.BFM_INPUT_MODIFIERS"></a> <a id="bfm-input-modifiers"></a>

*Private*

## `c4d.BFM_INPUT_MOUSE` <a id="c4d.BFM_INPUT_MOUSE"></a> <a id="bfm-input-mouse"></a>

Mouse.

## `c4d.BFM_INPUT_MOUSELEFT` <a id="c4d.BFM_INPUT_MOUSELEFT"></a> <a id="bfm-input-mouseleft"></a>

Left mouse button.

## `c4d.BFM_INPUT_MOUSEMIDDLE` <a id="c4d.BFM_INPUT_MOUSEMIDDLE"></a> <a id="bfm-input-mousemiddle"></a>

Middle mouse button.

## `c4d.BFM_INPUT_MOUSEMOVE` <a id="c4d.BFM_INPUT_MOUSEMOVE"></a> <a id="bfm-input-mousemove"></a>

Mouse move.

## `c4d.BFM_INPUT_MOUSERIGHT` <a id="c4d.BFM_INPUT_MOUSERIGHT"></a> <a id="bfm-input-mouseright"></a>

Right mouse button.

## `c4d.BFM_INPUT_MOUSEWHEEL` <a id="c4d.BFM_INPUT_MOUSEWHEEL"></a> <a id="bfm-input-mousewheel"></a>

Mouse wheel or panning on touch pad or touch screen. Values in BFM_INPUT_HSCROLL, BFM_INPUT_VSCROLL.

## `c4d.BFM_INPUT_MOUSEX1` <a id="c4d.BFM_INPUT_MOUSEX1"></a> <a id="bfm-input-mousex1"></a>

Fourth mouse button.

## `c4d.BFM_INPUT_MOUSEX2` <a id="c4d.BFM_INPUT_MOUSEX2"></a> <a id="bfm-input-mousex2"></a>

Five mouse button.

## `c4d.BFM_INPUT_MULTITOUCHSCROLL` <a id="c4d.BFM_INPUT_MULTITOUCHSCROLL"></a> <a id="bfm-input-multitouchscroll"></a>

True for scroll events on a multi-touch device (which also supports magnify), false for scroll-only mice.

## `c4d.BFM_INPUT_ORIENTATION` <a id="c4d.BFM_INPUT_ORIENTATION"></a> <a id="bfm-input-orientation"></a>

Pen rotation.

## `c4d.BFM_INPUT_P_ROTATION` <a id="c4d.BFM_INPUT_P_ROTATION"></a> <a id="bfm-input-p-rotation"></a>

Pen rotation around its own axis.

## `c4d.BFM_INPUT_QUALIFIER` <a id="c4d.BFM_INPUT_QUALIFIER"></a> <a id="bfm-input-qualifier"></a>

A bit mask with the qualifiers at the time when the event occurred: QUALIFIER

## `c4d.BFM_INPUT_TILT` <a id="c4d.BFM_INPUT_TILT"></a> <a id="bfm-input-tilt"></a>

Pen tilt.

## `c4d.BFM_INPUT_TIMESTAMP` <a id="c4d.BFM_INPUT_TIMESTAMP"></a> <a id="bfm-input-timestamp"></a>

Time stamp of the event or 0.0 (unavailable).

## `c4d.BFM_INPUT_VALUE` <a id="c4d.BFM_INPUT_VALUE"></a> <a id="bfm-input-value"></a>

Value of the input channel (true/false or a value, e.g. for scroll wheel data).

## `c4d.BFM_INPUT_VALUE_REAL` <a id="c4d.BFM_INPUT_VALUE_REAL"></a> <a id="bfm-input-value-real"></a>

Channel value (e.g. pen pressure).

## `c4d.BFM_INPUT_VSCROLL` <a id="c4d.BFM_INPUT_VSCROLL"></a> <a id="bfm-input-vscroll"></a>

Amount of vertical scrolling (touch pad, mouse wheel/ball)

## `c4d.BFM_INPUT_WHEELSCROLL` <a id="c4d.BFM_INPUT_WHEELSCROLL"></a> <a id="bfm-input-wheelscroll"></a>

True for scroll events on a classic wheel mouse. False for everything else (touch pad, magic mouse).

## `c4d.BFM_INPUT_X` <a id="c4d.BFM_INPUT_X"></a> <a id="bfm-input-x"></a>

X value.

## `c4d.BFM_INPUT_Y` <a id="c4d.BFM_INPUT_Y"></a> <a id="bfm-input-y"></a>

Y value.

## `c4d.BFM_INPUT_Z` <a id="c4d.BFM_INPUT_Z"></a> <a id="bfm-input-z"></a>

Z value.

## `c4d.BFM_INTERACTEND` <a id="c4d.BFM_INTERACTEND"></a> <a id="bfm-interactend"></a>

Sent when user interaction ends.

## `c4d.BFM_INTERACTSTART` <a id="c4d.BFM_INTERACTSTART"></a> <a id="bfm-interactstart"></a>

Sent when user interaction starts.

## `c4d.BFM_ISACTIVE` <a id="c4d.BFM_ISACTIVE"></a> <a id="bfm-isactive"></a>

*Private*

## `c4d.BFM_LAYOUT_CHANGED` <a id="c4d.BFM_LAYOUT_CHANGED"></a> <a id="bfm-layout-changed"></a>

*Internal*

## `c4d.BFM_LAYOUT_GETDATA` <a id="c4d.BFM_LAYOUT_GETDATA"></a> <a id="bfm-layout-getdata"></a>

Sent when saving the layout. Return a container to store with the layout for this dialog.

## `c4d.BFM_LAYOUT_SETDATA` <a id="c4d.BFM_LAYOUT_SETDATA"></a> <a id="bfm-layout-setdata"></a>

Receive the container saved with BFM_LAYOUT_GETDATA when loading a layout.

## `c4d.BFM_LOSTFOCUS` <a id="c4d.BFM_LOSTFOCUS"></a> <a id="bfm-lostfocus"></a>

Item lost the focus.

## `c4d.BFM_MANAGER_ID` <a id="c4d.BFM_MANAGER_ID"></a> <a id="bfm-manager-id"></a>

*Internal*

## `c4d.BFM_MARKFOCUS` <a id="c4d.BFM_MARKFOCUS"></a> <a id="bfm-markfocus"></a>

*Private*

## `c4d.BFM_MARKFORCELAYOUT` <a id="c4d.BFM_MARKFORCELAYOUT"></a> <a id="bfm-markforcelayout"></a>

*Private*

## `c4d.BFM_MAXCHNG` <a id="c4d.BFM_MAXCHNG"></a> <a id="bfm-maxchng"></a>

*Private*

## `c4d.BFM_MENU_CHECK` <a id="c4d.BFM_MENU_CHECK"></a> <a id="bfm-menu-check"></a>

*Internal*

## `c4d.BFM_MENU_OFF` <a id="c4d.BFM_MENU_OFF"></a> <a id="bfm-menu-off"></a>

*Internal*

## `c4d.BFM_MENU_ON` <a id="c4d.BFM_MENU_ON"></a> <a id="bfm-menu-on"></a>

*Internal*

## `c4d.BFM_MENU_SET` <a id="c4d.BFM_MENU_SET"></a> <a id="bfm-menu-set"></a>

*Private*

## `c4d.BFM_MENU_UNCHECK` <a id="c4d.BFM_MENU_UNCHECK"></a> <a id="bfm-menu-uncheck"></a>

*Internal*

## `c4d.BFM_MENUFINDER` <a id="c4d.BFM_MENUFINDER"></a> <a id="bfm-menufinder"></a>

*Private*

## `c4d.BFM_MINCHNG` <a id="c4d.BFM_MINCHNG"></a> <a id="bfm-minchng"></a>

*Private*

## `c4d.BFM_MOVEFOCUSNEXT` <a id="c4d.BFM_MOVEFOCUSNEXT"></a> <a id="bfm-movefocusnext"></a>

*Private*

## `c4d.BFM_MOVEFOCUSPREV` <a id="c4d.BFM_MOVEFOCUSPREV"></a> <a id="bfm-movefocusprev"></a>

*Private*

## `c4d.BFM_OPTIMIZE` <a id="c4d.BFM_OPTIMIZE"></a> <a id="bfm-optimize"></a>

*Private*

## `c4d.BFM_PARENT_TITLECHNG` <a id="c4d.BFM_PARENT_TITLECHNG"></a> <a id="bfm-parent-titlechng"></a>

*Internal*

## `c4d.BFM_POPUPNOTIFY` <a id="c4d.BFM_POPUPNOTIFY"></a> <a id="bfm-popupnotify"></a>

Notification of popup before the menu opens.

## `c4d.BFM_REDRAW_EDITMODE` <a id="c4d.BFM_REDRAW_EDITMODE"></a> <a id="bfm-redraw-editmode"></a>

*Private*

## `c4d.BFM_RELOAD_MENUS` <a id="c4d.BFM_RELOAD_MENUS"></a> <a id="bfm-reload-menus"></a>

*Private*

## `c4d.BFM_REMOVE_DIALOG` <a id="c4d.BFM_REMOVE_DIALOG"></a> <a id="bfm-remove-dialog"></a>

*Internal*

## `c4d.BFM_RENAMEWINDOW` <a id="c4d.BFM_RENAMEWINDOW"></a> <a id="bfm-renamewindow"></a>

*Internal*

## `c4d.BFM_REQUIRESRESULT` <a id="c4d.BFM_REQUIRESRESULT"></a> <a id="bfm-requiresresult"></a>

Set to true in the passed container for `GeDialog.SendMessage()` to return a value from the message.

## `c4d.BFM_SCROLLAREA` <a id="c4d.BFM_SCROLLAREA"></a> <a id="bfm-scrollarea"></a>

*Internal*

## `c4d.BFM_SCROLLGROUP_OFFSETCHANGED` <a id="c4d.BFM_SCROLLGROUP_OFFSETCHANGED"></a> <a id="bfm-scrollgroup-offsetchanged"></a>

*Internal*

## `c4d.BFM_SCROLLGROUP_SCALE` <a id="c4d.BFM_SCROLLGROUP_SCALE"></a> <a id="bfm-scrollgroup-scale"></a>

*Private*

## `c4d.BFM_SCROLLGROUP_SCROLLED` <a id="c4d.BFM_SCROLLGROUP_SCROLLED"></a> <a id="bfm-scrollgroup-scrolled"></a>

Scroll group scrolled.

## `c4d.BFM_SCROLLX` <a id="c4d.BFM_SCROLLX"></a> <a id="bfm-scrollx"></a>

*Internal*

## `c4d.BFM_SCROLLY` <a id="c4d.BFM_SCROLLY"></a> <a id="bfm-scrolly"></a>

*Internal*

## `c4d.BFM_SET_MSG_BITMASK` <a id="c4d.BFM_SET_MSG_BITMASK"></a> <a id="bfm-set-msg-bitmask"></a>

*Private*

## `c4d.BFM_SETACTIVE` <a id="c4d.BFM_SETACTIVE"></a> <a id="bfm-setactive"></a>

*Private*

## `c4d.BFM_SETACTIVE_DATA` <a id="c4d.BFM_SETACTIVE_DATA"></a> <a id="bfm-setactive-data"></a>

*Private*

## `c4d.BFM_SETCURSORINFO` <a id="c4d.BFM_SETCURSORINFO"></a> <a id="bfm-setcursorinfo"></a>

Same as BFM_EDITFIELD_SETCURSORPOS.

## `c4d.BFM_SETFIRSTFOCUS` <a id="c4d.BFM_SETFIRSTFOCUS"></a> <a id="bfm-setfirstfocus"></a>

*Internal*

## `c4d.BFM_SETFOCUS` <a id="c4d.BFM_SETFOCUS"></a> <a id="bfm-setfocus"></a>

*Internal*

## `c4d.BFM_SETFOCUSAFTERUPDATE` <a id="c4d.BFM_SETFOCUSAFTERUPDATE"></a> <a id="bfm-setfocusafterupdate"></a>

A custom GUI description receives this message after the layout is updated to reactivate previously focused gadget.

## `c4d.BFM_SETLASTFOCUS` <a id="c4d.BFM_SETLASTFOCUS"></a> <a id="bfm-setlastfocus"></a>

*Private*

## `c4d.BFM_SETMAINTITLE` <a id="c4d.BFM_SETMAINTITLE"></a> <a id="bfm-setmaintitle"></a>

*Private*

## `c4d.BFM_SETSPECIALMULTI` <a id="c4d.BFM_SETSPECIALMULTI"></a> <a id="bfm-setspecialmulti"></a>

*Private*

## `c4d.BFM_SETSPECIALMULTID` <a id="c4d.BFM_SETSPECIALMULTID"></a> <a id="bfm-setspecialmultid"></a>

*Private*

## `c4d.BFM_SETSTATUSBAR` <a id="c4d.BFM_SETSTATUSBAR"></a> <a id="bfm-setstatusbar"></a>

Sets a status-bar.

## `c4d.BFM_SETVIEWPANELLAYOUT` <a id="c4d.BFM_SETVIEWPANELLAYOUT"></a> <a id="bfm-setviewpanellayout"></a>

*Private*

## `c4d.BFM_SETVIEWPORTORIGIN` <a id="c4d.BFM_SETVIEWPORTORIGIN"></a> <a id="bfm-setviewportorigin"></a>

*Internal*

## `c4d.BFM_SETVIEWPORTORIGIN_X` <a id="c4d.BFM_SETVIEWPORTORIGIN_X"></a> <a id="bfm-setviewportorigin-x"></a>

*Internal*

## `c4d.BFM_SETVIEWPORTORIGIN_Y` <a id="c4d.BFM_SETVIEWPORTORIGIN_Y"></a> <a id="bfm-setviewportorigin-y"></a>

*Internal*

## `c4d.BFM_SETVIEWPORTSIZE` <a id="c4d.BFM_SETVIEWPORTSIZE"></a> <a id="bfm-setviewportsize"></a>

*Private*

## `c4d.BFM_SHOW_AREA` <a id="c4d.BFM_SHOW_AREA"></a> <a id="bfm-show-area"></a>

*Internal*

## `c4d.BFM_SHOW_FRAME` <a id="c4d.BFM_SHOW_FRAME"></a> <a id="bfm-show-frame"></a>

*Internal*

## `c4d.BFM_SHOW_ID` <a id="c4d.BFM_SHOW_ID"></a> <a id="bfm-show-id"></a>

*Internal*

## `c4d.BFM_SIZED` <a id="c4d.BFM_SIZED"></a> <a id="bfm-sized"></a>

Element has been sized.

## `c4d.BFM_SPECIALGETSTRING` <a id="c4d.BFM_SPECIALGETSTRING"></a> <a id="bfm-specialgetstring"></a>

*Private*

## `c4d.BFM_SPECIALMODE` <a id="c4d.BFM_SPECIALMODE"></a> <a id="bfm-specialmode"></a>

Set the multi-line edit field to the right language mode.

## `c4d.BFM_SPECIALSETRANGE` <a id="c4d.BFM_SPECIALSETRANGE"></a> <a id="bfm-specialsetrange"></a>

*Private*

## `c4d.BFM_STATUSBAR_HELP` <a id="c4d.BFM_STATUSBAR_HELP"></a> <a id="bfm-statusbar-help"></a>

Help second text.

## `c4d.BFM_STATUSBAR_NETPROGRESS` <a id="c4d.BFM_STATUSBAR_NETPROGRESS"></a> <a id="bfm-statusbar-netprogress"></a>

*Internal*

## `c4d.BFM_STATUSBAR_NETPROGRESSON` <a id="c4d.BFM_STATUSBAR_NETPROGRESSON"></a> <a id="bfm-statusbar-netprogresson"></a>

*Internal*

## `c4d.BFM_STATUSBAR_NETPROGRESSSPIN` <a id="c4d.BFM_STATUSBAR_NETPROGRESSSPIN"></a> <a id="bfm-statusbar-netprogressspin"></a>

*Internal*

## `c4d.BFM_STATUSBAR_NETTINT_COLOR` <a id="c4d.BFM_STATUSBAR_NETTINT_COLOR"></a> <a id="bfm-statusbar-nettint-color"></a>

*Internal*

## `c4d.BFM_STATUSBAR_NETTXT` <a id="c4d.BFM_STATUSBAR_NETTXT"></a> <a id="bfm-statusbar-nettxt"></a>

*Internal*

## `c4d.BFM_STATUSBAR_PROGRESS` <a id="c4d.BFM_STATUSBAR_PROGRESS"></a> <a id="bfm-statusbar-progress"></a>

Between 0.0 and 1.0.

## `c4d.BFM_STATUSBAR_PROGRESSFULLSIZE` <a id="c4d.BFM_STATUSBAR_PROGRESSFULLSIZE"></a> <a id="bfm-statusbar-progressfullsize"></a>

*Internal*

## `c4d.BFM_STATUSBAR_PROGRESSON` <a id="c4d.BFM_STATUSBAR_PROGRESSON"></a> <a id="bfm-statusbar-progresson"></a>

Status-bar active.

## `c4d.BFM_STATUSBAR_PROGRESSSPIN` <a id="c4d.BFM_STATUSBAR_PROGRESSSPIN"></a> <a id="bfm-statusbar-progressspin"></a>

Spinning-bar.

## `c4d.BFM_STATUSBAR_TINT_COLOR` <a id="c4d.BFM_STATUSBAR_TINT_COLOR"></a> <a id="bfm-statusbar-tint-color"></a>

Color ID for the status-bar, or as RGB value (Vector).

## `c4d.BFM_STATUSBAR_TXT` <a id="c4d.BFM_STATUSBAR_TXT"></a> <a id="bfm-statusbar-txt"></a>

Help first text.

## `c4d.BFM_STORE_WEIGHTS` <a id="c4d.BFM_STORE_WEIGHTS"></a> <a id="bfm-store-weights"></a>

*Private*

## `c4d.BFM_SYNC_MESSAGE` <a id="c4d.BFM_SYNC_MESSAGE"></a> <a id="bfm-sync-message"></a>

Sync message.

## `c4d.BFM_TESTONLY` <a id="c4d.BFM_TESTONLY"></a> <a id="bfm-testonly"></a>

*Private*

## `c4d.BFM_TIMER_MESSAGE` <a id="c4d.BFM_TIMER_MESSAGE"></a> <a id="bfm-timer-message"></a>

Timer message. Use `GeDialog.SetTimer()` / `GeUserArea.SetTimer()` to set the periodical time.

## `c4d.BFM_TITLECHNG` <a id="c4d.BFM_TITLECHNG"></a> <a id="bfm-titlechng"></a>

*Private*

## `c4d.BFM_UPDATE_REGION` <a id="c4d.BFM_UPDATE_REGION"></a> <a id="bfm-update-region"></a>

*Private*

## `c4d.BFM_VALUEADD` <a id="c4d.BFM_VALUEADD"></a> <a id="bfm-valueadd"></a>

*Private*

## `c4d.BFM_VALUECHNG` <a id="c4d.BFM_VALUECHNG"></a> <a id="bfm-valuechng"></a>

*Private*

## `c4d.BFM_VALUESUB` <a id="c4d.BFM_VALUESUB"></a> <a id="bfm-valuesub"></a>

*Private*

## `c4d.BFM_VISIBLE_OFF` <a id="c4d.BFM_VISIBLE_OFF"></a> <a id="bfm-visible-off"></a>

*Internal*

## `c4d.BFM_VISIBLE_ON` <a id="c4d.BFM_VISIBLE_ON"></a> <a id="bfm-visible-on"></a>

*Internal*

## `c4d.BFM_VPD_LAYOUTTYPE` <a id="c4d.BFM_VPD_LAYOUTTYPE"></a> <a id="bfm-vpd-layouttype"></a>

*Private*

## `c4d.BFM_VPD_MAXIMIZED` <a id="c4d.BFM_VPD_MAXIMIZED"></a> <a id="bfm-vpd-maximized"></a>

*Private*

## `c4d.BFM_VPD_PANELID` <a id="c4d.BFM_VPD_PANELID"></a> <a id="bfm-vpd-panelid"></a>

*Private*

## `c4d.BFM_WEIGHTS_CHANGED` <a id="c4d.BFM_WEIGHTS_CHANGED"></a> <a id="bfm-weights-changed"></a>

Group weights changed. The group ID is returned.
