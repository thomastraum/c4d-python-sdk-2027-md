<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/net/index.html -->

# c4d.modules.net <a id="c4d-modules-net"></a>

## *class* `c4d.modules.net` <a id="c4d.modules.net"></a>

*New in version R15.037.*

- [`c4d.modules.net.NetRenderService`](NetRenderService/index.md#c4d.modules.net.NetRenderService)
- [`c4d.modules.net.RenderJob`](RenderJob/index.md#c4d.modules.net.RenderJob)
- [`c4d.modules.net.Repository`](Repository/index.md#c4d.modules.net.Repository)
- [`c4d.modules.net.UserPool`](UserPool/index.md#c4d.modules.net.UserPool)

## Overview <a id="overview"></a>

**Error Reporting Configuration**

- [`c4d.modules.net.SetErrorLevel()`](#c4d.modules.net.SetErrorLevel): Sets the level for stack and location in errors.

**Event Messaging**

- [`c4d.modules.net.NetGeSyncMessage()`](#c4d.modules.net.NetGeSyncMessage): Sends a synchronous event message over NET.
- [`c4d.modules.net.NetSpecialEventAdd()`](#c4d.modules.net.NetSpecialEventAdd): Adds a custom event over NET.

**Job Formatting**

- [`c4d.modules.net.JobCommandToString()`](#c4d.modules.net.JobCommandToString): Format a job *command* as a string.

**Service Access**

- [`c4d.modules.net.GetGlobalNetRenderService()`](#c4d.modules.net.GetGlobalNetRenderService): Get the global NET render service.

**State Formatting**

- [`c4d.modules.net.JobStateToString()`](#c4d.modules.net.JobStateToString): Format a job *state* as a string.
- [`c4d.modules.net.VerificationStateToString()`](#c4d.modules.net.VerificationStateToString): Format a verification *state* as a string.

## Members <a id="members"></a>

### Error Reporting Configuration <a id="c4d.modules.net-function-Error-Reporting-Configuration"></a>

#### `c4d.modules.net.SetErrorLevel(printDebugErrors, stackInErrors, locationInErrors)` <a id="c4d.modules.net.SetErrorLevel"></a>

Sets the level for stack and location in errors.

*New in version R16.038.*

**Parameters:**

- **printDebugErrors** (*bool*) –

  *New in version R16.050:* **True** to print debug errors, otherwise **False**.

- **stackInErrors** (*bool*) – **True** to enable stack in errors, otherwise **False**.

- **locationInErrors** (*bool*) – **True** to enable location in errors, otherwise **False**.

### Event Messaging <a id="c4d.modules.net-function-Event-Messaging"></a>

#### `c4d.modules.net.NetGeSyncMessage(service, remoteUuid, msg, forceConnect=True)` <a id="c4d.modules.net.NetGeSyncMessage"></a>

Sends a synchronous event message over NET.

*New in version R16.021.*

**Parameters:**

- **service** ([*c4d.modules.net.NetRenderService*](NetRenderService/index.md#c4d.modules.net.NetRenderService)) – The NET render service.
- **remoteUuid** ([UUID](https://docs.python.org/3.9/library/uuid.html#uuid.UUID)) – The machine to send the message to.
- **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The message container.
- **forceConnect** (*bool*) – Private.

**Return type:** Tuple[bool, [c4d.BaseContainer](../../c4d/BaseContainer/index.md#c4d.BaseContainer)]

**Returns:** The successful status and result container.

#### `c4d.modules.net.NetSpecialEventAdd(service, remoteUuid, msg, forceConnect=True)` <a id="c4d.modules.net.NetSpecialEventAdd"></a>

Adds a custom event over NET.

*New in version R16.021.*

**Parameters:**

- **service** ([*c4d.modules.net.NetRenderService*](NetRenderService/index.md#c4d.modules.net.NetRenderService)) – The NET render service.
- **remoteUuid** – The machine to send the message to.
- **msg** ([*c4d.BaseContainer*](../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The message container.
- **forceConnect** (*bool*) – Private.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Job Formatting <a id="c4d.modules.net-function-Job-Formatting"></a>

#### `c4d.modules.net.JobCommandToString(command)` <a id="c4d.modules.net.JobCommandToString"></a>

Format a job *command* as a string.

**Parameters:**

**command** (*int*) –

The job command:

| Symbol ID | Description |
|---|---|
| JOBCOMMAND_NONE | Do nothing. |
| JOBCOMMAND_FETCHJOB | Fetch job. |
| JOBCOMMAND_ALLOCATESPACE | Allocate space. |
| JOBCOMMAND_DOWNLOAD | Download. |
| JOBCOMMAND_RENDER | Render. |
| JOBCOMMAND_DELETE_ | Delete. |
| JOBCOMMAND_STOPANDDELETE | Stop and delete. |
| JOBCOMMAND_ASSEMBLE | Assemble. |
| JOBCOMMAND_END | End. |

**Return type:** str

**Returns:** The formatted job command.

### Service Access <a id="c4d.modules.net-function-Service-Access"></a>

#### `c4d.modules.net.GetGlobalNetRenderService()` <a id="c4d.modules.net.GetGlobalNetRenderService"></a>

Get the global NET render service.

**Return type:** [c4d.modules.net.NetRenderService](NetRenderService/index.md#c4d.modules.net.NetRenderService)

**Returns:** The global NET render service.

### State Formatting <a id="c4d.modules.net-function-State-Formatting"></a>

#### `c4d.modules.net.JobStateToString(state)` <a id="c4d.modules.net.JobStateToString"></a>

Format a job *state* as a string.

*New in version R16.021.*

**Parameters:**

**command** (*int*) –

The job state:

|   |   |
|---|---|
| *JOBSTATE_IDLE* | Idle. |
| *JOBSTATE_PREPARING_RUNNING* | Preparing running. Preparing only for server in async mode for [`NetRenderService.StartRendering()`](NetRenderService/index.md#c4d.modules.net.NetRenderService.StartRendering). |
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

**Return type:** str

**Returns:** The formatted job state.

#### `c4d.modules.net.VerificationStateToString(state)` <a id="c4d.modules.net.VerificationStateToString"></a>

Format a verification *state* as a string.

**Parameters:**

**state** (*int*) –

The verification state:

|   |   |
|---|---|
| *VERIFICATIONBIT_NONE* | None. |
| *VERIFICATIONBIT_ONLINE* | Online. |
| *VERIFICATIONBIT_VERIFIED* | Verified. |
| *VERIFICATIONBIT_VERIFIEDME* | Certified client (set on client for server). |
| *VERIFICATIONBIT_SHARED* | Shared. |
| *VERIFICATIONBIT_VERIFYING* | Verifying. |
| *VERIFICATIONBIT_FAILURE* | Unknown. |
| *VERIFICATIONBIT_SECURITYTOKENCHANGED* | Security token changed. |
| *VERIFICATIONBIT_WRONGBUILDID* | Wrong build ID. |
| *VERIFICATIONBIT_WRONGARCHITECTURE* | Wrong architecture. |
| *VERIFICATIONBIT_REMOTENOTREACHABLE* | Remote not reachable. |
| *VERIFICATIONBIT_THISNOTREACHABLE* | This not reachable. |
| *VERIFICATIONBIT_WRONGSECURITYTOKEN* | Wrong security token. |
| *VERIFICATIONBIT_DEMONOTACTIVATED* | Demo not activated. |
| *VERIFICATIONBIT_REMOVING* | Removing. |
| *VERIFICATIONBIT_NORENDERSUPPORT* | No render support. |
| *VERIFICATIONBIT_INITIALIZING* | GUI flag only to show a please wait indicator on startup. |
| *VERIFICATIONBIT_VERIFICATIONESTABLISHED* | Set soon after the persistent connection has been registered. Can be set without *VERIFICATIONBIT_VERIFIED* on first connect and host adds itself on the server. |

**Return type:** str

**Returns:** The formatted verification state.
