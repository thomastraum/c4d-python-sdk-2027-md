<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/JOBSTATE.html -->

# JOBSTATE <a id="jobstate"></a>

|   |   |
|---|---|
| *JOBSTATE_IDLE* | Idle. |
| *JOBSTATE_PREPARING_RUNNING* | Preparing running. Preparing only for server in async mode for `NetRenderService.StartRendering()`. |
| *JOBSTATE_PREPARING_FAILED* | Preparing failed. |
| *JOBSTATE_PREPARING_OK* | Preparing ok. |
| *JOBSTATE_RENDER_RUNNING* | Render running. |
| *JOBSTATE_RENDER_OK* | Render ok. |
| *JOBSTATE_RENDER_FAILED* | Render failed. |
| *JOBSTATE_ALLOCATESPACE_RUNNING* | Allocate space running. |
| *JOBSTATE_ALLOCATESPACE_OK* | Allocate space ok. |
| *JOBSTATE_ALLOCATESPACE_FAILED* | Allocated space failed. |
| *JOBSTATE_DOWNLOAD_RUNNING* | Download running. |
| *JOBSTATE_DOWNLOAD_OK* | Download ok. |
| *JOBSTATE_DOWNLOAD_FAILED* | Download failed. |
| *JOBSTATE_ASSEMBLE_RUNNING* | Assemble running. |
| *JOBSTATE_ASSEMBLE_OK* | Assemble ok. |
| *JOBSTATE_ASSEMBLE_FAILED* | Assemble failed. |
| *JOBSTATE_STOPPED* | Stopped. |
| *JOBSTATE_QUEUED* | Queued. |
| *JOBSTATE_PENDING* | Non-native state which is only available in the server when no machine is involved in a running job. |
| *JOBSTATE_QUEUED_WAITING* | *New in version R18:* Queued waiting. |
| *JOBSTATE_ASSEMBLE_PENDING* | *New in version R17.053:* Allocate space running. |
