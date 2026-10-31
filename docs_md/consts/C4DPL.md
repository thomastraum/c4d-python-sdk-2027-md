<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/C4DPL.html -->

# C4DPL <a id="c4dpl"></a>

|   |   |
|---|---|
| *C4DPL_INIT_SYS* | Initialize system. |
| *C4DPL_INIT* | Initialize the plugin, calling *PluginStart*. |
| *C4DPL_END* | End the plugin, calling *PluginEnd*. |
| *C4DPL_MESSAGE* | Receive plugin message, calling *PluginMessage*. |
| *C4DPL_BUILDMENU* | Called when the menus are built during startup. Use [`GetMenuResource()`](../modules/c4d.gui/index.md#c4d.gui.GetMenuResource) etc. to add own menus here if necessary. See the [example](../manuals/manual_implementing_plugins.md#enhancing-main-menu). |
| *C4DPL_STARTACTIVITY* | Sent to all plugins after all *PluginStart* have been called. |
| *C4DPL_ENDACTIVITY* | Sent to all plugins before any *PluginEnd* has been called. This allows to close dialogs, end threads, delete temporary/undo buffers etc. |
| *C4DPL_CHANGEDSECURITYTOKEN* | Sent to all plugins if the Security Token of Team Render was changed. |
| *C4DPL_SHUTDOWNTHREADS* | Sent to all plugins before the threading system of Cinema 4D is shutdown. After that no threads should be started. |
| *C4DPL_LAYOUTCHANGED* | Sent to all plugins after the layout has been switched. |
| *C4DPL_RELOADPYTHONPLUGINS* | Sent when Python plugins are to be reloaded. See [Plugin Messages](../manuals/manual_implementing_plugins.md#plugin-messages). |
| *C4DPL_COMMANDLINEARGS* | Sent to let plugins parse the command line arguments used when starting Cinema 4D. Retrieve the arguments by calling [sys.argv](https://docs.python.org/3.9/library/sys.html#sys.argv). See [Command Line Arguments](../manuals/manual_implementing_plugins.md#commandline-args). |
| *C4DPL_EDITIMAGE* | Sent to allow plugins to start any other actions when Cinema 4D tries to show an image (e.g. in the shader popup). *data* is dict{‘imagefn’: str, filename of the image that triggered the message} |
| *C4DPL_ENDPROGRAM* | Sent when Cinema 4D is about to close. *data* is dict{‘cancel’: bool, set to **True** to cancel close of Cinema 4D} |
| *C4DPL_DEVICECHANGE* | Sent when a device has changed. *data* is dict{‘name’: str, name of the device, ‘eject’: bool Eject, state of the device} |
| *C4DPL_NETWORK_CHANGE* | Sent to all plugins if the network configuration on the system changed. |
| *C4DPL_SYSTEM_SLEEP* | Sent to all plugins if the system goes to sleep. |
| *C4DPL_SYSTEM_WAKE* | Sent to all plugins if the system wakes up. |
| *C4DPL_PROGRAM_STARTED* | Sent when the application has been started. |
