<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/SCENEFILTER.html -->

# SCENEFILTER <a id="scenefilter"></a>

|   |   |
|---|---|
| *SCENEFILTER_NONE* | None. |
| *SCENEFILTER_OBJECTS* | Load/save objects. |
| *SCENEFILTER_MATERIALS* | Load/save materials. |
| *SCENEFILTER_DIALOGSALLOWED* | Flag to inform a plugin that a dialog can be displayed. If this flag is not set then no dialogs must be opened. |
| *SCENEFILTER_PROGRESSALLOWED* | Flag to inform a plugin that a progress bar can be displayed. The progress bar can be set by calling [`StatusSetBar()`](../modules/c4d/index.md#c4d.StatusSetBar). |
| *SCENEFILTER_MERGESCENE* | Flag to inform a plugin that this is a merge operation, i.e. the document that is inserted to is an existing scene. |
| *SCENEFILTER_NONEWMARKERS* | Objects loaded from disk will keep their markers. |
| *SCENEFILTER_SAVECACHES* | For *melange* export only. Caches of objects will also be written (only supported by Cinema 4D format). This is the same as the global option “Save Polygon Objects for Melange Exchange”. |
| *SCENEFILTER_NOUNDO* | Use together with *SCENEFILTER_MERGESCENE* to avoid that undos are created for the merge operation. |
| *SCENEFILTER_SAVE_BINARYCACHE* | Save the binary compiled shaders with the scene (only for Cinema 4D format). |
| *SCENEFILTER_IDENTIFY_ONLY* | Do not load the whole document, identify it only. |
| *SCENEFILTER_ONLY_RENDERDATA* | Only load render settings. If this flag is set, *SCENEFILTER_OBJECTS* and *SCENEFILTER_MATERIALS* are ignored. |
| *SCENEFILTER_IGNOREMISSINGPLUGINSINNONACTIVERENDERDATA* | Ignore all missing plugins which are part of a non-active render data. |
| *SCENEFILTER_IGNOREXREFS* | *New in version R16.038:* Avoid that included X-Refs will be loaded. |
| *SCENEFILTER_DONTCORRECTOUTPUTFORMAT* | Do not change unknown output formats in render settings. |
