<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/MSG_DOCUMENTINFO_TYPE.html -->

# MSG_DOCUMENTINFO_TYPE <a id="msg-documentinfo-type"></a>

|   |   |
|---|---|
| *MSG_DOCUMENTINFO_TYPE_SETACTIVE* | Document was set as active. |
| *MSG_DOCUMENTINFO_TYPE_LOAD* | Document was loaded. |
| *MSG_DOCUMENTINFO_TYPE_MERGE* | Document was merged. |
| *MSG_DOCUMENTINFO_TYPE_BEFOREMERGE* | Document before merge. *data* is a [MSG_DOCUMENTINFO_TYPE_BEFOREMERGE_RESULT](MSG_DOCUMENTINFO_TYPE_BEFOREMERGE_RESULT.md). |
| *MSG_DOCUMENTINFO_TYPE_SAVE_BEFORE* | Document is about to be written. |
| *MSG_DOCUMENTINFO_TYPE_SAVE_AFTER* | Document was saved. |
| *MSG_DOCUMENTINFO_TYPE_SAVEPROJECT_BEFORE* | Save Project with Assets is about to be executed. |
| *MSG_DOCUMENTINFO_TYPE_SAVEPROJECT_AFTER* | Save Project with Assets was executed. |
| *MSG_DOCUMENTINFO_TYPE_REMOVE* | The document is removed from the document list. All structures are still accessible. |
| *MSG_DOCUMENTINFO_TYPE_TOOL_CHANGED* | Tool changed. |
| *MSG_DOCUMENTINFO_TYPE_OBJECT_INSERT* | Objects got inserted into the document. |
| *MSG_DOCUMENTINFO_TYPE_TAG_INSERT* | Tags got inserted into the document. |
| *MSG_DOCUMENTINFO_TYPE_MATERIAL_INSERT* | Materials got inserted into the document. |
| *MSG_DOCUMENTINFO_TYPE_UNDO* | Undo was called. |
| *MSG_DOCUMENTINFO_TYPE_REDO* | Redo was called. |
| *MSG_DOCUMENTINFO_TYPE_PASTE* | Paste was called. |
| *MSG_DOCUMENTINFO_TYPE_COPY* | Copy was called. Private. |
| *MSG_DOCUMENTINFO_TYPE_LOAD_XREFS* | Private. |
| *MSG_DOCUMENTINFO_TYPE_MERGE_XREFS* | Private. |
| *MSG_DOCUMENTINFO_TYPE_XREFS_IMPORTED* | Private. |
| *MSG_DOCUMENTINFO_TYPE_MAKEPROJECT* | Sent around during “Save as Project” for each texture / asset it copies. The data contains the source and destination files. This message is only sent to scene hooks. |
| *MSG_DOCUMENTINFO_TYPE_SWAP_XREF* | Private. |
| *MSG_DOCUMENTINFO_TYPE_NODE_ASSETS_CHANGED* | *New in version R20.000:* Send around after node assets in a basedocument have been changed. |
| *MSG_DOCUMENTINFO_TYPE_MODE_CHANGED* | *New in version R20.000:* Mode changed. |
| *MSG_DOCUMENTINFO_TYPE_FLUSHCACHES* | *New in version R19.062:* Document caches are flushed. This message is only sent to scene hooks. |
