<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/PLUGINFLAG_COMMAND.html -->

# PLUGINFLAG_COMMAND <a id="pluginflag-command"></a>

|   |   |
|---|---|
| *PLUGINFLAG_COMMAND_HOTKEY* | Command is a hotkey command. Hotkey commands can only work globally. |
| *PLUGINFLAG_COMMAND_OPTION_DIALOG* | Command has additional options. The user can access them through a small gadget. |
| *PLUGINFLAG_COMMAND_STICKY* | Command is a “sticky” command. This means `CommandData.Execute()` is called when the user presses an assigned hotkey and when the hotkey is released. Otherwise the command would be called continously. |
| *PLUGINFLAG_COMMAND_ICONGADGET* | Command can be dragged into an icon bar and delivers its own dialogs instead of icons. |
