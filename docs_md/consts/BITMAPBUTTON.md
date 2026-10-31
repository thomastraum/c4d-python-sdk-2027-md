<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/BITMAPBUTTON.html -->

# BITMAPBUTTON <a id="bitmapbutton"></a>

| Key | Value Type | Description |
|---|---|---|
| BITMAPBUTTON_BORDER | int | **Border type used for the pressed button state if *BITMAPBUTTON_OUTBORDER* is set**<br>*BORDER_NONE*: No border.<br>*BORDER_THIN_IN*: Thin border inward.<br>*BORDER_THIN_OUT*: Thin border outward.<br>*BORDER_IN*: Normal border inward.<br>*BORDER_OUT*: Normal border outward.<br>*BORDER_GROUP_IN*: Group border inside.<br>*BORDER_GROUP_OUT*: Group border outside.<br>*BORDER_OUT2*: Outward border 2.<br>*BORDER_OUT3*: Outward border 3<br>*BORDER_BLACK*: Thin black line.<br>*BORDER_ACTIVE_1*: Active border 1.<br>*BORDER_ACTIVE_2*: Active border 2.<br>*BORDER_ACTIVE_3*: Active border 3.<br>*BORDER_ACTIVE_4*: Active border 4.<br>*BORDER_GROUP_TOP*: Border along the top.<br>*BORDER_ROUND*: Border with round corners.<br>*BORDER_SCHEME_EDIT*: Edit field border like the shortcut gadget for example.<br>*BORDER_SCHEME_EDIT_NUMERIC*: Edit field border that is open to the right like the link field for example.<br>*BORDER_OUT3l*: Outward border 3, open to the left.<br>*BORDER_OUT3r*: Outward border 3, open to the right.<br>*BORDER_THIN_INb*: Thin border inward, open to the botton.<br>*BORDER_MASK*: Masks out border type.<br>*BORDER_TEXT_DOTTED*: Only used with `GeDialog.AddStaticText()`.  <br>Draws a dotted line at right of text, useful to visually connect the text with its parameter.<br>*BORDER_WITH_TITLE_MONO*: Display group title with monospaced font.<br>*BORDER_WITH_TITLE_BOLD*: Display group title with bold font.<br>*BORDER_WITH_TITLE*: Display group title in the border. |
| BITMAPBUTTON_BUTTON | bool | Clickable button. To detect when the button is pressed in a description check if the *DESCFLAGS_SET_USERINTERACTION* flag is set in the `NodeData.SetDParameter()` call. |
| BITMAPBUTTON_TOGGLE | bool | Toggle button, like a checkbox. |
| BITMAPBUTTON_IGNORE_BITMAP_WIDTH | bool | Ignore bitmap width. |
| BITMAPBUTTON_IGNORE_BITMAP_HEIGHT | bool | Ignore bitmap height. |
| BITMAPBUTTON_DRAWPOPUPBUTTON | bool | Draw popup button. |
| BITMAPBUTTON_TOOLTIP | str | Tooltip string. Only works if *BITMAPBUTTON_BUTTON* is **True**. |
| BITMAPBUTTON_ICONID1 | int | Registered icon bitmap ID. *On* state for toggle buttons. |
| BITMAPBUTTON_ICONID2 | int | Registered icon bitmap ID. *Off* state for toggle buttons. |
| BITMAPBUTTON_FORCE_SIZE | int | Forces the width and height of the icon in pixels if value is greater than 0. |
| BITMAPBUTTON_FORCE_SIZE_Y | int | Additionally forces the y size of the bitmap button. FORCE_SIZE is used for y size when not specified. |
| BITMAPBUTTON_SPECIAL | bool | Private. |
| BITMAPBUTTON_NOBORDERDRAW | bool | Disable border drawing. |
| BITMAPBUTTON_OUTBORDER | int | **Out border type used if *BITMAPBUTTON_BUTTON* is True**<br>*BORDER_NONE*: No border.<br>*BORDER_THIN_IN*: Thin border inward.<br>*BORDER_THIN_OUT*: Thin border outward.<br>*BORDER_IN*: Normal border inward.<br>*BORDER_OUT*: Normal border outward.<br>*BORDER_GROUP_IN*: Group border inside.<br>*BORDER_GROUP_OUT*: Group border outside.<br>*BORDER_OUT2*: Outward border 2.<br>*BORDER_OUT3*: Outward border 3<br>*BORDER_BLACK*: Thin black line.<br>*BORDER_ACTIVE_1*: Active border 1.<br>*BORDER_ACTIVE_2*: Active border 2.<br>*BORDER_ACTIVE_3*: Active border 3.<br>*BORDER_ACTIVE_4*: Active border 4.<br>*BORDER_GROUP_TOP*: Border along the top.<br>*BORDER_ROUND*: Border with round corners.<br>*BORDER_SCHEME_EDIT*: Edit field border like the shortcut gadget for example.<br>*BORDER_SCHEME_EDIT_NUMERIC*: Edit field border that is open to the right like the link field for example.<br>*BORDER_OUT3l*: Outward border 3, open to the left.<br>*BORDER_OUT3r*: Outward border 3, open to the right.<br>*BORDER_THIN_INb*: Thin border inward, open to the botton.<br>*BORDER_MASK*: Masks out border type.<br>*BORDER_TEXT_DOTTED*: Only used with `GeDialog.AddStaticText()`.  <br>Draws a dotted line at right of text, useful to visually connect the text with its parameter.<br>*BORDER_WITH_TITLE_MONO*: Display group title with monospaced font.<br>*BORDER_WITH_TITLE_BOLD*: Display group title with bold font.<br>*BORDER_WITH_TITLE*: Display group title in the border. |
| BITMAPBUTTON_BACKCOLOR | int | Background color. See [COLOR constants](COLOR.md). |
| BITMAPBUTTON_MIRROR | bool | Mirror the button in an Arabic interface. |
| BITMAPBUTTON_STRING | str | *New in version R20:* Adds a string in bold font at left of the icon. |
| BITMAPBUTTON_DISABLE_FADING | bool | *New in version S22:* Disables the mouse over fading effect. |
| BITMAPBUTTON_FORCE_TOOLTIP | bool | *New in version R26:* Forces to show the defined tooltip when **BITMAPBUTTON_BUTTON** is false. |
| BITMAPBUTTON_NO_COLOR_INFO | bool | *New in version R26:* Hides the per-pixel color info that pops-up when holding CTRL key on mouse hover when **BITMAPBUTTON_BUTTON** is false. |
