<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/SAVEPROJECT.html -->

# SAVEPROJECT <a id="saveproject"></a>

|   |   |
|---|---|
| *SAVEPROJECT_NONE* | None. |
| *SAVEPROJECT_ASSETS* | Pass if the assets will be taken into account. |
| *SAVEPROJECT_SCENEFILE* | Pass if the scene will be taken into account. |
| *SAVEPROJECT_DIALOGSALLOWED* | Show dialogs like error messages, a file selection for missing assets or alerts if necessary. |
| *SAVEPROJECT_SHOWMISSINGASSETDIALOG* | If an asset is missing show a warning dialog. Flag can be set without *SAVEPROJECT_DIALOGSALLOWED*. |
| *SAVEPROJECT_ADDTORECENTLIST* | Add document to the recent list. |
| *SAVEPROJECT_DONTCOPYFILES* | Does the same as without this flag but does not copy the files to the destination. Flag used to simulate the function. |
| *SAVEPROJECT_PROGRESSALLOWED* | Show the progress bar in the main window. |
| *SAVEPROJECT_DONTTOUCHDOCUMENT* | Document will be in the same state as before the call was made. |
| *SAVEPROJECT_DONTFAILONMISSINGASSETS* | If this flag is passed, the function does not fail anymore when assets are missing. |
| *SAVEPROJECT_ISNET* | Private. Set only if NET module is collecting assets. |
| *SAVEPROJECT_USEDOCUMENTNAMEASFILENAME* | Use the document name as the file name to save as project. |
| *SAVEPROJECT_DONTCLEARSUGGESTEDFOLDER* | Do not change asset paths of nodes. |
| *SAVEPROJECT_WITHCACHES* | *New in version R17.048:* Save the project assets with Global Illumination / Ambient Occlusion caches. See also *ASSETDATA_FLAG_WITHCACHES*. |
| *SAVEPROJECT_DONTGENERATEPAINTTEX* | *New in version R17.053:* Does the same as without this flag but does not generate the textures from painted materials. |
| *SAVEPROJECT_ASSETLINKS_COPY_FILEASSETS* | *New in version R24:* Copy file assets (assets://) to the tex folder. |
| *SAVEPROJECT_ASSETLINKS_COPY_NODEASSETS* | *New in version R24:* Copy node assets to the scene repository. |
