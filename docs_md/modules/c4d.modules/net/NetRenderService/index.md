<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.modules/net/NetRenderService/index.html -->

# c4d.modules.net.NetRenderService <a id="c4d-modules-net-netrenderservice"></a>

## *class* `c4d.modules.net.NetRenderService` <a id="c4d.modules.net.NetRenderService"></a>

*New in version R15.037.*

> **Warning:** This type cannot be instantiated.

## Overview <a id="overview"></a>

**Communication And Logging**

- [`NetRenderService.AddLogToJob()`](#c4d.modules.net.NetRenderService.AddLogToJob): Add a string to the job log.
- [`NetRenderService.Message()`](#c4d.modules.net.NetRenderService.Message): Sends a message to the render service.
- [`NetRenderService.NetConsoleOutput()`](#c4d.modules.net.NetRenderService.NetConsoleOutput): Prints a string to the service.

**Job Management**

- [`NetRenderService.CreateRenderJob()`](#c4d.modules.net.NetRenderService.CreateRenderJob): Creates a render job.
- [`NetRenderService.DeleteRenderJob()`](#c4d.modules.net.NetRenderService.DeleteRenderJob): Deletes a render job.
- [`NetRenderService.GetJobsList()`](#c4d.modules.net.NetRenderService.GetJobsList): Retrieves the render jobs.
- [`NetRenderService.InsertJobAfter()`](#c4d.modules.net.NetRenderService.InsertJobAfter): Inserts *jobUuid1* after *jobUuid2*.
- [`NetRenderService.InsertJobBefore()`](#c4d.modules.net.NetRenderService.InsertJobBefore): Inserts *jobUuid1* before *jobUuid2*.
- [`NetRenderService.SetDefaultSceneName()`](#c4d.modules.net.NetRenderService.SetDefaultSceneName): Sets the Default Scene Name.

**Machine Management**

- [`NetRenderService.AddLogToMachine()`](#c4d.modules.net.NetRenderService.AddLogToMachine): Adds a string to the machine log.
- [`NetRenderService.AddMachine()`](#c4d.modules.net.NetRenderService.AddMachine): Adds a machine.
- [`NetRenderService.GetAllMachineUuids()`](#c4d.modules.net.NetRenderService.GetAllMachineUuids): Retrieves the UUIDs of all machines (with default parameters).
- [`NetRenderService.GetMachinesList()`](#c4d.modules.net.NetRenderService.GetMachinesList): Retrieves the information of all machines.

**Preferences And Users**

- [`NetRenderService.GetNetPreferences()`](#c4d.modules.net.NetRenderService.GetNetPreferences): Retrieves the NET preferences.
- [`NetRenderService.GetUserPool()`](#c4d.modules.net.NetRenderService.GetUserPool): Gets the user pool.

**Rendering Control**

- [`NetRenderService.InitAndStartRenderingFullAsync()`](#c4d.modules.net.NetRenderService.InitAndStartRenderingFullAsync): Starts a render job fully asynchronous.
- [`NetRenderService.InitRendering()`](#c4d.modules.net.NetRenderService.InitRendering): Initializes a render job.
- [`NetRenderService.StartRendering()`](#c4d.modules.net.NetRenderService.StartRendering): Starts a render job.
- [`NetRenderService.StopRendering()`](#c4d.modules.net.NetRenderService.StopRendering): Stops a render job.

**Result And Task Data**

- [`NetRenderService.ClearResults()`](#c4d.modules.net.NetRenderService.ClearResults): Clears the results.
- [`NetRenderService.CopyRenderTaskFrom()`](#c4d.modules.net.NetRenderService.CopyRenderTaskFrom): Copy the Render Task matching the jobUuid.
- [`NetRenderService.RemoveResult()`](#c4d.modules.net.NetRenderService.RemoveResult): Remove the result for the given job.

**Service Information**

- [`NetRenderService.GetName()`](#c4d.modules.net.NetRenderService.GetName): Gets the name of the service.
- [`NetRenderService.GetRepository()`](#c4d.modules.net.NetRenderService.GetRepository): Retrieves the repository for the service.
- [`NetRenderService.GetUuid()`](#c4d.modules.net.NetRenderService.GetUuid): Gets the UUID of the service.

## Members <a id="members"></a>

### Communication And Logging <a id="c4d.modules.net.NetRenderService-method-Communication-And-Logging"></a>

#### `NetRenderService.AddLogToJob(self, jobUuid, log, doLock, append=True)` <a id="c4d.modules.net.NetRenderService.AddLogToJob"></a>

Add a string to the job log.

*New in version R16.021.*

**Parameters:**

- **jobUuid** ([UUID](https://docs.python.org/3.9/library/uuid.html#uuid.UUID)) – The job UUID.
- **log** (*str*) – The string to add.
- **doLock** (*bool*) –
- **append** (*bool*) –

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `NetRenderService.Message(self, userUuid, op, isPrivate, msg, result=None)` <a id="c4d.modules.net.NetRenderService.Message"></a>

Sends a message to the render service.

*New in version R16.021.*

> **See also:** [MSG_NETRENDER](../../../../consts/MSG_NETRENDER.md) for the information on the messages type, data and input/output.

**Parameters:**

- **userUuid** – The user UUID.
- **op** (*object*) –
- **isPrivate** (*bool*) –
- **msg** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The message container.
- **result** (*Optional*[[*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)]) – The optional result container.

**Return type:** bool

**Returns:**

#### `NetRenderService.NetConsoleOutput(self, flags, value)` <a id="c4d.modules.net.NetRenderService.NetConsoleOutput"></a>

Prints a string to the service.

*New in version R16.021.*

**Parameters:**

- **flags** (*int*) –

  The console ouput flags:

  |   |   |
  |---|---|
  | *OUTPUT_DIAGNOSTIC* | Diagnostic output, shows up if a group of output is activated. This is the default. |
  | *OUTPUT_WARNING* | Warning output, shows up if a group of output is activated. |
  | *OUTPUT_CRITICAL* | Critical output, shows up if a group of output is activated. |
  | *OUTPUT_NOLINEBREAK* | If set, no line break is added. |
  | *OUTPUT_HEADER* | If set, header with line number and file name is added. C++ only. |

- **value** (*str*) – The string to output.

### Job Management <a id="c4d.modules.net.NetRenderService-method-Job-Management"></a>

#### `NetRenderService.CreateRenderJob(self, docName, jobUuid, creator, username, bt=None, watchFolderName='')` <a id="c4d.modules.net.NetRenderService.CreateRenderJob"></a>

Creates a render job.

*New in version R16.021.*

**Parameters:**

- **docName** (*str*) – The document name.

- **jobUuid** – The job UUID.

- **creator** (*int*) –

  The render job creator:

  |   |   |
  |---|---|
  | *RENDERJOBCREATOR_BATCHRENDER* | Batch render. |
  | *RENDERJOBCREATOR_PICTUREVIEWER* | Picture Viewer. |
  | *RENDERJOBCREATOR_USER* | User. |
  | *RENDERJOBCREATOR_WATCHDIRECTORY* | Watch directory. |
  | *RENDERJOBCREATOR_WATCHDIRECTORYSTARTUP* | Watch directory startup. |
  | *RENDERJOBCREATOR_OTHER* | Other. |

- **username** (*str*) – The user name.

- **bt** (*Optional*[[*c4d.threading.BaseThread*](../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)]) – The thread.

- **watchFolderName** (*str*) – The name of the folder to watch.

**Return type:** int

**Returns:**

The result:

|   |   |
|---|---|
| *CREATEJOBRESULT_OK* | Ok. |
| *CREATEJOBRESULT_OUTOFMEMORY* | Out of memory. |
| *CREATEJOBRESULT_ASSETMISSING* | Asset missing. |
| *CREATEJOBRESULT_SAVINGFAILED* | Saving failed. |
| *CREATEJOBRESULT_REPOSITORYERROR* | Repository error. |

#### `NetRenderService.DeleteRenderJob(self, jobUuid, informClients)` <a id="c4d.modules.net.NetRenderService.DeleteRenderJob"></a>

Deletes a render job.

*New in version R16.021.*

**Parameters:**

- **jobUuid** – The job UUID.
- **informClients** (*bool*) –

**Return type:** bool

**Returns:** **True** if the render job was deleted, otherwise **False**.

#### `NetRenderService.GetJobsList(self, triggerWatchDog, rdata, assets, results, log, selectedJob=None, selectedJobOnly=False, user=None, settings=None)` <a id="c4d.modules.net.NetRenderService.GetJobsList"></a>

Retrieves the render jobs.

*New in version R16.021.*

**Parameters:**

- **triggerWatchDog** (*bool*) –

- **rdata** (*int*) –

  The render data select flags:

  |   |   |
  |---|---|
  | *DETAILSELECTOR_NONE* | None |
  | *DETAILSELECTOR_SELECTED* | Selected. |
  | *DETAILSELECTOR_NONSELECTED* | Not selected. |

- **assets** (*int*) –

  The assets data select flags:

  |   |   |
  |---|---|
  | *DETAILSELECTOR_NONE* | None |
  | *DETAILSELECTOR_SELECTED* | Selected. |
  | *DETAILSELECTOR_NONSELECTED* | Not selected. |

- **results** (*int*) –

  The results data select flags:

  |   |   |
  |---|---|
  | *DETAILSELECTOR_NONE* | None |
  | *DETAILSELECTOR_SELECTED* | Selected. |
  | *DETAILSELECTOR_NONSELECTED* | Not selected. |

- **log** (*int*) –

  The log data select flags:

  |   |   |
  |---|---|
  | *DETAILSELECTOR_NONE* | None |
  | *DETAILSELECTOR_SELECTED* | Selected. |
  | *DETAILSELECTOR_NONSELECTED* | Not selected. |

- **selectedJob** –

- **selectedJobOnly** (*bool*) –

- **user** – The user UUID.

- **settings** (*Optional*[[*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)]) –

  *New in version R16.038:* The settings container.

**Return type:** List[[c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)]

**Returns:** The render jobs.

#### `NetRenderService.InsertJobAfter(self, jobUuid1, jobUuid2)` <a id="c4d.modules.net.NetRenderService.InsertJobAfter"></a>

Inserts *jobUuid1* after *jobUuid2*.

*New in version R16.021.*

**Parameters:**

- **jobUuid1** – The job to insert after *jobUuid2*.
- **jobUuid2** – The job to insert *jobUuid1* after.

**Return type:** bool

**Returns:** **True** if *jobUuid1* was inserted after *jobUuid2* otherwise **False**.

#### `NetRenderService.InsertJobBefore(self, jobUuid1, jobUuid2)` <a id="c4d.modules.net.NetRenderService.InsertJobBefore"></a>

Inserts *jobUuid1* before *jobUuid2*.

*New in version R16.021.*

**Parameters:**

- **jobUuid1** – The job to insert before *jobUuid2*.
- **jobUuid2** – The job to insert *jobUuid1* before.

**Return type:** bool

**Returns:** **True** if *jobUuid1* was inserted before *jobUuid2* otherwise **False**.

#### `NetRenderService.SetDefaultSceneName(self, jobUuid, defaultSceneName)` <a id="c4d.modules.net.NetRenderService.SetDefaultSceneName"></a>

Sets the Default Scene Name.

*New in version R16.021.*

**Parameters:**

- **jobUuid** – The job UUID.
- **defaultSceneName** (*str*) – The default scene name.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Machine Management <a id="c4d.modules.net.NetRenderService-method-Machine-Management"></a>

#### `NetRenderService.AddLogToMachine(self, jobUuid, log, doLock)` <a id="c4d.modules.net.NetRenderService.AddLogToMachine"></a>

Adds a string to the machine log.

*New in version R16.021.*

**Parameters:**

- **machineUuid** – The machine UUID.
- **log** (*str*) – The string to add.
- **doLock** (*bool*) –

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `NetRenderService.AddMachine(self, address, securityToken, allowGui, uuidOfMachineToOverwrite)` <a id="c4d.modules.net.NetRenderService.AddMachine"></a>

Adds a machine.

*New in version R16.038.*

**Parameters:**

- **address** (*str*) – The machine address.
- **securityToken** (*str*) – The security token.
- **allowGui** (*bool*) – **True** to allow GUI, otherwise **False**.
- **uuidOfMachineToOverwrite** – The UUID of the machine to overwrite.

**Return type:** bool

**Returns:** **True** if the machine was added successfully, otherwise **False**.

#### `NetRenderService.GetAllMachineUuids(self, list=7, bits=0, includeLocalMachine=True, includeBonjourMachines=True)` <a id="c4d.modules.net.NetRenderService.GetAllMachineUuids"></a>

Retrieves the UUIDs of all machines (with default parameters).  
Parameters can be changed to filter the machines.

**Parameters:**

- **list** (*int*) –

  Machine list flags:

  |   |   |
  |---|---|
  | *MACHINELIST_ONLINE* | Online. |
  | *MACHINELIST_OFFLINE* | Offline. |
  | *MACHINELIST_ALL* | All: *MACHINELIST_ONLINE* \| *MACHINELIST_OFFLINE*. |

- **bits** (*int*) –

  Verification bits:

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

- **includeLocalMachine** (*bool*) – Pass **False** to not include local machine. Default to **True**.

- **includeBonjourMachines** (*bool*) – Pass **False** to not include Bonjour machines. Default to **True**.

**Return type:** List[UUID]

**Returns:** The list of all machine UUIDs.

#### `NetRenderService.GetMachinesList(self, logCount=-1, getOnlyThisMachine=None)` <a id="c4d.modules.net.NetRenderService.GetMachinesList"></a>

Retrieves the information of all machines.

*New in version R16.021.*

**Parameters:**

- **logCount** (*int*) –

  *New in version R16.050:* The log count.

- **getOnlyThisMachine** – Pass a machine UUID to get only the information for this machine.

**Return type:** List[[c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)]

**Returns:** The list of machines.

### Preferences And Users <a id="c4d.modules.net.NetRenderService-method-Preferences-And-Users"></a>

#### `NetRenderService.GetNetPreferences(self)` <a id="c4d.modules.net.NetRenderService.GetNetPreferences"></a>

Retrieves the NET preferences.

*New in version R16.021.*

**Return type:** [c4d.BaseContainer](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)

**Returns:** The NET preferences container. For the container IDs, see preferences dialog and *WPREF_NET* in the C++ API header *ge_prepass.h*.

#### `NetRenderService.GetUserPool(self)` <a id="c4d.modules.net.NetRenderService.GetUserPool"></a>

Gets the user pool.

**Return type:** [c4d.modules.net.UserPool](../UserPool/index.md#c4d.modules.net.UserPool)

**Returns:** The user pool.

### Rendering Control <a id="c4d.modules.net.NetRenderService-method-Rendering-Control"></a>

#### `NetRenderService.InitAndStartRenderingFullAsync(self, jobUuid)` <a id="c4d.modules.net.NetRenderService.InitAndStartRenderingFullAsync"></a>

Starts a render job fully asynchronous.

*New in version R16.021.*

**Parameters:** **jobUuid** (*uuid.Uuid*) – The job UUID.

**Return type:** bool

**Returns:** **True** if rendering was started, otherwise **False**.

#### `NetRenderService.InitRendering(self, doc, rdata, jobUuid, flags, machines)` <a id="c4d.modules.net.NetRenderService.InitRendering"></a>

Initializes a render job.

*New in version R16.021.*

**Parameters:**

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

- **rdata** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The render data.

- **jobUuid** (*uuid.Uuid*) – The job UUID.

- **flags** (*int*) –

  The NET render flags:

  |   |   |
  |---|---|
  | *NETRENDERFLAGS_NONE* | None. |
  | *NETRENDERFLAGS_OPEN_PICTUREVIEWER* | Open Picture Viewer. |
  | *NETRENDERFLAGS_SHOWERRORS* | Show errors. |
  | *NETRENDERFLAGS_DELETEAFTERRENDERING* | Delete after rendering. |
  | *NETRENDERFLAGS_NOPEERTOPEERASSETDISTRIBUTION* | No peer-to-peer asset distribution. Automatically set by local preferences. |
  | *NETRENDERFLAGS_NOREQUESTONDEMAND* | No request on demand. Automatically set by local preferences. |
  | *NETRENDERFLAGS_EXCLUDECLIENTONRENDERINGERROR* | Exclude client on rendering error. Automatically set by local preferences. |
  | *NETRENDERFLAGS_SAVERESULTSINREPOSITORY* | Save results in repository. |
  | *NETRENDERFLAGS_ASSEMBLEB3DFILESIMMEDIATLEY* | Assemble BodyPaint 3D files immediately. |
  | *NETRENDERFLAGS_NOWRITETEST* | No write test for BodyPaint 3D files. |
  | *NETRENDERFLAGS_HANDLEWARNINGASERROR* | Handle warning as error. |
  | *NETRENDERFLAGS_KEEPB3DFILESAFTERASSEMBLING* | Keep the BodyPaint 3D files on assembling. |

- **machines** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The machines container.

**Return type:** int

**Returns:**

The result:

|   |   |
|---|---|
| *RENDERRESULT_OK* | Function was successful. |
| *RENDERRESULT_OUTOFMEMORY* | Not enough memory. |
| *RENDERRESULT_ASSETMISSING* | Assets (textures etc.) are missing. |
| *RENDERRESULT_SAVINGFAILED* | Failed to save. |
| *RENDERRESULT_USERBREAK* | User stopped the processing. |
| *RENDERRESULT_GICACHEMISSING* | GI cache is missing. |
| *RENDERRESULT_NOMACHINE* | Machine was not found. Can only happen during Team Rendering. |
| *RENDERRESULT_PROJECTNOTFOUND* | Project was not found. Can only be returned by Cinema 4D during command line rendering. |
| *RENDERRESULT_ERRORLOADINGPROJECT* | There was an error while loading the project. Can only be returned by Cinema 4D during command line rendering. |
| *RENDERRESULT_NOOUTPUTSPECIFIED* | Output was not specified. Can only be returned by Cinema 4D during command line rendering. |

#### `NetRenderService.StartRendering(self, mode, doc, jobUuid, bt)` <a id="c4d.modules.net.NetRenderService.StartRendering"></a>

Starts a render job.

*New in version R16.021.*

**Parameters:**

- **mode** (*int*) –

  The thread mode:

  |   |   |
  |---|---|
  | *THREADMODE_DEPRECATED_SYNCHRONOUS* | Synchronous thread. Deprecated. |
  | *THREADMODE_ASYNC* | Asynchronous thread. |
  | *THREADMODE_PRIVATE_OPENGL* | *New in version R18:* Private |

- **doc** ([*c4d.documents.BaseDocument*](../../../c4d.documents/BaseDocument/index.md#c4d.documents.BaseDocument)) – The document.

- **jobUuid** – The job UUID.

- **bt** ([*c4d.threading.BaseThread*](../../../c4d.threading/BaseThread/index.md#c4d.threading.BaseThread)) – The thread for the operation.

**Return type:** int

**Returns:**

The result:

|   |   |
|---|---|
| *RENDERRESULT_OK* | Function was successful. |
| *RENDERRESULT_OUTOFMEMORY* | Not enough memory. |
| *RENDERRESULT_ASSETMISSING* | Assets (textures etc.) are missing. |
| *RENDERRESULT_SAVINGFAILED* | Failed to save. |
| *RENDERRESULT_USERBREAK* | User stopped the processing. |
| *RENDERRESULT_GICACHEMISSING* | GI cache is missing. |
| *RENDERRESULT_NOMACHINE* | Machine was not found. Can only happen during Team Rendering. |
| *RENDERRESULT_PROJECTNOTFOUND* | Project was not found. Can only be returned by Cinema 4D during command line rendering. |
| *RENDERRESULT_ERRORLOADINGPROJECT* | There was an error while loading the project. Can only be returned by Cinema 4D during command line rendering. |
| *RENDERRESULT_NOOUTPUTSPECIFIED* | Output was not specified. Can only be returned by Cinema 4D during command line rendering. |

#### `NetRenderService.StopRendering(self, mode, jobUuid, result)` <a id="c4d.modules.net.NetRenderService.StopRendering"></a>

Stops a render job.

*New in version R16.021.*

**Parameters:**

- **mode** (*int*) –

  The thread mode:

  |   |   |
  |---|---|
  | *THREADMODE_DEPRECATED_SYNCHRONOUS* | Synchronous thread. Deprecated. |
  | *THREADMODE_ASYNC* | Asynchronous thread. |
  | *THREADMODE_PRIVATE_OPENGL* | *New in version R18:* Private |

- **jobUuid** – The job UUID.

- **result** (*int*) –

  The result:

  |   |   |
  |---|---|
  | *RENDERRESULT_OK* | Function was successful. |
  | *RENDERRESULT_OUTOFMEMORY* | Not enough memory. |
  | *RENDERRESULT_ASSETMISSING* | Assets (textures etc.) are missing. |
  | *RENDERRESULT_SAVINGFAILED* | Failed to save. |
  | *RENDERRESULT_USERBREAK* | User stopped the processing. |
  | *RENDERRESULT_GICACHEMISSING* | GI cache is missing. |
  | *RENDERRESULT_NOMACHINE* | Machine was not found. Can only happen during Team Rendering. |
  | *RENDERRESULT_PROJECTNOTFOUND* | Project was not found. Can only be returned by Cinema 4D during command line rendering. |
  | *RENDERRESULT_ERRORLOADINGPROJECT* | There was an error while loading the project. Can only be returned by Cinema 4D during command line rendering. |
  | *RENDERRESULT_NOOUTPUTSPECIFIED* | Output was not specified. Can only be returned by Cinema 4D during command line rendering. |

### Result And Task Data <a id="c4d.modules.net.NetRenderService-method-Result-And-Task-Data"></a>

#### `NetRenderService.ClearResults(self, jobUuid)` <a id="c4d.modules.net.NetRenderService.ClearResults"></a>

Clears the results.

*New in version R16.021.*

**Parameters:** **jobUuid** – The job UUID.

**Return type:** bool

**Returns:** **True** if results were cleared, otherwise **False**.

#### `NetRenderService.CopyRenderTaskFrom(self, jobUuid, resolveMachineUuids=False)` <a id="c4d.modules.net.NetRenderService.CopyRenderTaskFrom"></a>

Copy the Render Task matching the jobUuid.

**Parameters:**

- **jobUuid** – The job UUID.
- **resolveMachineUuids** (*bool*) – Currently ignored.

**Return type:** List[dict{“_frame”: int, “_state”: int, “_renderTime”: int, “_machines”: List[uuid]}]

**Returns:** a list filled with dictionary representing each render task - _frame: The frame number. - _state: The render state. - _renderTime: The render time. - _machines: A list with all the machines assigned to the job.

#### `NetRenderService.RemoveResult(self, jobUuid, relResultPath)` <a id="c4d.modules.net.NetRenderService.RemoveResult"></a>

Remove the result for the given job.

**Parameters:**

- **jobUuid** – The job UUID.
- **relResultPath** (*str*) – File Path of the result path?

**Return type:** bool

**Returns:** **True** if results were removed, otherwise **False**.

### Service Information <a id="c4d.modules.net.NetRenderService-method-Service-Information"></a>

#### `NetRenderService.GetName(self)` <a id="c4d.modules.net.NetRenderService.GetName"></a>

Gets the name of the service.

*New in version R16.021.*

**Return type:** str

**Returns:** The name of the service.

#### `NetRenderService.GetRepository(self)` <a id="c4d.modules.net.NetRenderService.GetRepository"></a>

> Retrieves the repository for the service.

*New in version R16.021.*

**Return type:** [c4d.modules.net.Repository](../Repository/index.md#c4d.modules.net.Repository)

**Returns:** The repository.

#### `NetRenderService.GetUuid(self)` <a id="c4d.modules.net.NetRenderService.GetUuid"></a>

Gets the UUID of the service.

**Return type:** [UUID](https://docs.python.org/3.9/library/uuid.html#uuid.UUID)

**Returns:** The UUID of the service.
