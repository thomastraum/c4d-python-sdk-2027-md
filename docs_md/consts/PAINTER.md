<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/PAINTER.html -->

# PAINTER <a id="painter"></a>

|   |   |   |   |
|---|---|---|---|
| *PAINTER_SAVETEXTURE* | Save textures. If *doc* != **None** all textures associated with *doc* are saved. If *tex* != **None** only *tex* is saved, otherwise all textures are saved. |  |  |
|  | *PAINTER_SAVETEXTURE_FLAGS* | int | Save texture flags: |
|  | *PAINTER_SAVEBIT_SAVEAS* | Save As. |  |
|  | *PAINTER_SAVEBIT_SAVECOPY* | Save As Copy. |  |
|  | *PAINTER_SAVEBIT_SAVEALLOWWARNING* | Allow warnings. |  |
|  | *PAINTER_SAVEBIT_RENAMEINSCENE* | Rename. |  |
| *PAINTER_BRINGTOFRONT* | Bring the BodyPaint 3D application window to front (for exchange plugins). Private. |  |  |
| *PAINTER_LOADTEXTURE* | Load a texture. Returns the loaded [`PaintTexture`](../modules/c4d.modules/bodypaint/PaintBitmap/PaintTexture/index.md#c4d.modules.bodypaint.PaintTexture) if successful, otherwise **None**. |  |  |
|  | *LOADTEXTURE_FILENAME* | str | The filename of the texture to load. |
| *PAINTER_FORCECLOSETEXTURE* | Remove a texture from memory. Pass the texture to *tex*. |  |  |
| *PAINTER_CLOSETEXTURE* | Remove a texture from memory but ask for if the texture is unsaved. Pass the texture to *tex*. |  |  |
| *PAINTER_SAVETEXTURE_DIRECT* | Unused. |  |  |
| *PAINTER_RELOADTEXTURE* | Reload a texture in BodyPaint 3D and Cinema 4D’s renderer locklist. |  |  |
|  | *RELOADTEXTURE_FILENAME* | str | The filename of the texture to reload. |
