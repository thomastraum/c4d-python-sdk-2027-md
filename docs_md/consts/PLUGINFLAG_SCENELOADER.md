<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/PLUGINFLAG_SCENELOADER.html -->

# PLUGINFLAG_SCENELOADER <a id="pluginflag-sceneloader"></a>

| Symbol ID | Description |
|---|---|
| PLUGINFLAG_SCENELOADER_MERGEORIGINAL | If this flag is set, the original (existing) document will be passed to the scene loader instead of a new (empty) one.  <br>This allows the importer to change existing data, merge data or to make other modifications based on the existing scene. |
| PLUGINFLAG_SCENELOADER_URL_AWARE | *New in version R24:* Scene loader plugin flag to signal that the scene loader is capable to deal with urls not in the file system e.g. asset:/// |
| PLUGINFLAG_SCENELOADER_SUPPORT_ASYNC | *New in version R26:* Signals that a scene loader should run asynchronously. |
