<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/MSG_DOCUMENTINFO_TYPE_BEFOREMERGE_RESULT.html -->

# MSG_DOCUMENTINFO_TYPE_BEFOREMERGE_RESULT <a id="msg-documentinfo-type-beforemerge-result"></a>

|   |   |
|---|---|
| *MSG_DOCUMENTINFO_TYPE_BEFOREMERGE_RESULT_CANCEL* | Allows to cancel the merge. |
| *MSG_DOCUMENTINFO_TYPE_BEFOREMERGE_RESULT_MERGE* | Default, as before, just merge. |
| *MSG_DOCUMENTINFO_TYPE_BEFOREMERGE_RESULT_NEWSCENE* | Overwrites the merge flag and loads the scene as opened with load. In that case the message *MSG_DOCUMENTINFO_TYPE_MERGE* will not be send to the original document but a *MSG_DOCUMENTINFO_TYPE_LOAD* message instead. |
