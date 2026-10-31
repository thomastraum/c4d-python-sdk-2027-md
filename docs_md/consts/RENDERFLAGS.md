<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/RENDERFLAGS.html -->

# RENDERFLAGS <a id="renderflags"></a>

|   |   |
|---|---|
| *RENDERFLAGS_NONE* | Default flag which can lead to unexpected results. See *RENDERFLAGS_EXTERNAL*. |
| *RENDERFLAGS_EXTERNAL* | Enables using render engines other than the standard renderer. When this flag is not set, Cinema 4D will fall back to what it considers the “standard” engine in its context (either Standard or Redshift when it is installed). So, when you render data set for example the Hardware Preview renderer or a third party render engine, Cinema 4D will ignore that engine choice and use the standard engine instead; unless you set this flag. Setting this flag will also entail a ‘full fidelity’ render, in the sense that caches are being busted and rebuilt with full render quality. |
| *RENDERFLAGS_NODOCUMENTCLONE* | Suppresses the document being cloned for rendering, even when *RENDERFLAGS_EXTERNAL* is set. This is a performance optimization but not recommended for final renderings. |
| *RENDERFLAGS_SHOWERRORS* | If to show error messages of the renderer. |
| *RENDERFLAGS_PREVIEWRENDER* | Many subsystems check for this flag to produce lower quality results, as used in material previews or the asset browser. Is not related to the hardware preview renderer. |
| *RENDERFLAGS_IRR* | An interactive render region render. |
| *RENDERFLAGS_CREATE_PICTUREVIEWER* | Returns the rendering in a new Picture Viewer instance. |
| *RENDERFLAGS_OPEN_PICTUREVIEWER* | Opens the rendering in the Picture Viewer. |
| *RENDERFLAGS_KEEP_CONTEXT* | Private. |
| *RENDERFLAGS_BATCHRENDER* | Private. |
| *RENDERFLAGS_NET* | Use NET for rendering. |
| *RENDERFLAGS_DONTANIMATE* | Do not animate document before rendering. This should only be used in combination with *RENDERFLAGS_PREVIEWRENDER*. |
| *RENDERFLAGS_PREVIEWSETTINGS* | Use preview settings. |
| *RENDERFLAGS_RENDERQUEUEERRORS* | Cancel Render Queue rendering if scene has missing assets. |
| *RENDERFLAGS_FORCE_LINEAR_COLOR_PROFILE* | Forces a linear color profile on the render bitmap in some settings. |
| *RENDERFLAGS_OCIO_RAW_RENDERING* | Shorthand for setting *RDATA_BAKE_OCIO_VIEW_TRANSFORM_RENDER* according to the color management settings of the document. This will cause OCIO documents to return render results in raw render space, instead of having data baked down. Will have no effect on documents which are not using OCIO color management. |
| *RENDERFLAGS_OCIO_BAKE_RENDERING* | Shorthand for calling [`BakeOcioViewToBitmap`](../modules/c4d.documents/index.md#c4d.documents.BakeOcioViewToBitmap) on the render result bitmap, baking down all OCIO transforms as if Cinema 4D would when saving the rendering to disk, depending on the passed render settings. This only affects the returned render bitmap. .. warning:: Setting this flag will cause the bake result to be copied into the render result bitmap. Using [`BakeOcioViewToBitmap`](../modules/c4d.documents/index.md#c4d.documents.BakeOcioViewToBitmap) manually is faster as it does not copy data and should be preferred in performance critical code paths. |
| *RENDERFLAGS_AUTO_SETUP* | Alias for *EXTERNAL \| OCIO_RAW_RENDERING*. This is the recommended flags combination to use as a base for most rendering tasks. |
| *RENDERFLAGS_INTERNAL_USE_CURRENT_QUEUE* | Internal. |
| *RENDERFLAGS_INTERNAL_SPECIAL_PREVIEW* | Internal. |
