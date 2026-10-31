<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.threading/index.html -->

# c4d.threading <a id="c4d-threading"></a>

## *class* `c4d.threading` <a id="c4d.threading"></a>

Provides functions and classes to handle the execution of code in multiple threads.  
The class [`c4d.threading.BaseThread`](BaseThread/index.md#c4d.threading.BaseThread) and its implementable child class [`c4d.threading.C4DThread`](C4DThread/index.md#c4d.threading.C4DThread) are a replacement for the builtin threading module `threading` of Python. They ensure the compatibility of Python code executed in parallel with the threading system of Cinema 4D implemented in C++ and should always be used in favor of the builtin *threading* module of Python.  
Please note that [`C4DThread`](C4DThread/index.md#c4d.threading.C4DThread), just as its native Python counterpart `threading.Thread`, is a mechanism to decouple the execution of code, but not to speed it up. Its intended use is to make computationally complex tasks non-blocking for the main-thread of Cinema 4D and by that ensure the responsiveness of the user interface. Parallelism in the sense of executing multiple parts of a larger task in parallel is currently not offered by the Python SDK. This also applies by extension to the *multiprocessing* module of Python which offers such functionality but it is not supported by Cinema 4D. Trying to use [`C4DThread`](C4DThread/index.md#c4d.threading.C4DThread) to speed up the parallel execution of such multiple parts task will not only yield no execution speed improvements but will most likely even be slower than a single threaded execution of the same task.

> **See also:** The important [Threading Restrictions](../../manuals/manual_scene_execution.md#threading-information).

- [`c4d.threading.BaseThread`](BaseThread/index.md#c4d.threading.BaseThread)
- [`c4d.threading.C4DThread`](C4DThread/index.md#c4d.threading.C4DThread)

## Overview <a id="overview"></a>

**Background Thread Management**

- [`c4d.threading.GeCheckBackgroundThreadsRunning()`](#c4d.threading.GeCheckBackgroundThreadsRunning): Checks if any of the threads matching *typeclass* is running.
- [`c4d.threading.GeStopBackgroundThreads()`](#c4d.threading.GeStopBackgroundThreads): Stops all running background threads of the given *typeclass*.

**Deprecated**

- [`c4d.threading.GeGetCPUCount()`](#c4d.threading.GeGetCPUCount): Gets the number of threads available.

**Test Threads**

- [`c4d.threading.GeGetDummyThread()`](#c4d.threading.GeGetDummyThread): Returns a dummy thread.
- [`c4d.threading.GeGetEscTestThread()`](#c4d.threading.GeGetEscTestThread): Returns a dummy thread for escape key testing.

**Thread Context Checks**

- [`c4d.threading.GeIsMainThread()`](#c4d.threading.GeIsMainThread): Checks if the code is run from within the main thread of Cinema 4D.
- [`c4d.threading.GeIsMainThreadAndNoDrawThread()`](#c4d.threading.GeIsMainThreadAndNoDrawThread): Checks if code is run from within the main thread of Cinema 4D and if the main thread does not execute any drawing code currently.

**Thread Identification**

- [`c4d.threading.GeGetCurrentThread()`](#c4d.threading.GeGetCurrentThread): Returns the current thread.
- [`c4d.threading.IdentifyThread()`](#c4d.threading.IdentifyThread): Identifies a thread’s type.

**Thread Information**

- [`c4d.threading.GeGetCurrentThreadCount()`](#c4d.threading.GeGetCurrentThreadCount): Gets the number of threads available.
- [`c4d.threading.GeGetCurrentThreadId()`](#c4d.threading.GeGetCurrentThreadId): Returns a unique ID for the current thread.

**Thread Locking**

- [`c4d.threading.GeThreadLock()`](#c4d.threading.GeThreadLock): Locks using a global semaphore.
- [`c4d.threading.GeThreadUnlock()`](#c4d.threading.GeThreadUnlock): Continues blocked threads after a call to `GeThreadLock()`.

## Members <a id="members"></a>

### Background Thread Management <a id="c4d.threading-function-Background-Thread-Management"></a>

#### `c4d.threading.GeCheckBackgroundThreadsRunning(typeclass, all)` <a id="c4d.threading.GeCheckBackgroundThreadsRunning"></a>

Checks if any of the threads matching *typeclass* is running.

**Parameters:**

- **typeclass** (*int*) –

  The type class of the background threads to check. If *0*, all threads are checked. Pass **BACKGROUNDHANDLER_TYPECLASS_C4D** to check Cinema 4D background handlers.  
  For example *GeCheckBackgroundThreadsRunning(BACKGROUNDHANDLER_TYPECLASS_C4D, True)* checks if Cinema 4D is doing anything right now.  
  If **False** were passed it would not check for the external renderer (which are always running in a BodyPaint 3D selection).

- **all** (*bool*) – If **True** then background handler with negative priority are also checked.

**Return type:** bool

**Returns:** **True** if the specified threads are running, otherwise **False**.

#### `c4d.threading.GeStopBackgroundThreads(typeclass, flags)` <a id="c4d.threading.GeStopBackgroundThreads"></a>

Stops all running background threads of the given *typeclass*.

**Parameters:**

- **typeclass** (*int*) – The type class of the background threads to stop. If *0*, all threads are stopped. Pass **BACKGROUNDHANDLER_TYPECLASS_C4D** to stop Cinema 4D background handlers.

- **flags** (*int*) –

  If *typeclass* is **BACKGROUNDHANDLER_TYPECLASS_C4D** then the following flags can be used:

  |   |   |
  |---|---|
  | *BACKGROUNDHANDLERFLAGS_NONE* | None. |
  | *BACKGROUNDHANDLERFLAGS_VIEWREDRAW* | View redraw. |
  | *BACKGROUNDHANDLERFLAGS_EDITORRENDDER* | Editor render. |
  | *BACKGROUNDHANDLERFLAGS_MATERIALPREVIEW* | Material preview. |
  | *BACKGROUNDHANDLERFLAGS_RENDEREXTERNAL* | Render external. |
  | *BACKGROUNDHANDLERFLAGS_PRIVATE_VIEWREDRAW* | Private. |
  | *BACKGROUNDHANDLERFLAGS_SHUTDOWN* | Shutdown. |

  *GeStopBackgroundThreads(BACKGROUNDHANDLER_TYPECLASS_C4D, BACKGROUNDHANDLER_FLAGS_EDITORRENDDER)* only stops the editor renderer (if it was running).  
  *GeStopBackgroundThreads(0, BACKGROUNDHANDLERFLAGS_SHUTDOWN)* kills anything running.  
  Pass flags as needed for custom type classes, they will be routed to the background handler function.

### Deprecated <a id="c4d.threading-function-Deprecated"></a>

#### `c4d.threading.GeGetCPUCount()` <a id="c4d.threading.GeGetCPUCount"></a>

Gets the number of threads available.

*Deprecated since version R16.*

Use `threading.GeGetCurrentThreadCount()`

**Return type:** int

**Returns:** The number of current threads.

### Test Threads <a id="c4d.threading-function-Test-Threads"></a>

#### `c4d.threading.GeGetDummyThread()` <a id="c4d.threading.GeGetDummyThread"></a>

Returns a dummy thread. The thread’s [`BaseThread.TestBreak()`](BaseThread/index.md#c4d.threading.BaseThread.TestBreak) function always returns **False**.

*New in version R17.048.*

**Return type:** [`BaseThread`](BaseThread/index.md#c4d.threading.BaseThread)

**Returns:** A dummy thread .

#### `c4d.threading.GeGetEscTestThread()` <a id="c4d.threading.GeGetEscTestThread"></a>

Returns a dummy thread for escape key testing.  
The thread’s [`BaseThread.TestBreak()`](BaseThread/index.md#c4d.threading.BaseThread.TestBreak) function returns **True** when the user presses the escape key.

*New in version R17.048.*

**Return type:** [`BaseThread`](BaseThread/index.md#c4d.threading.BaseThread)

**Returns:** An escape key test thread.

### Thread Context Checks <a id="c4d.threading-function-Thread-Context-Checks"></a>

#### `c4d.threading.GeIsMainThread()` <a id="c4d.threading.GeIsMainThread"></a>

Checks if the code is run from within the main thread of Cinema 4D.

**Return type:** bool

**Returns:** **True** if called from the main thread, otherwise **False**.

#### `c4d.threading.GeIsMainThreadAndNoDrawThread()` <a id="c4d.threading.GeIsMainThreadAndNoDrawThread"></a>

Checks if code is run from within the main thread of Cinema 4D and if the main thread does not execute any drawing code currently.

*New in version R16.038.*

> **Note:**
>
> This routine can be used to make sure that no illegal code is called during a drawing operation.  
> In Cinema 4D the drawing will be started threaded or non-threaded, depending on the situation.  
> It is not allowed to add e.g. undo or delete objects or materials while the drawing is in progress (this would lead to immediate crashes).  
> If code calls other routines that are not aware of their context (e.g. some code within a Message() that does not know whether it was called from a drawing thread or during a command call).  
> [`GeIsMainThreadAndNoDrawThread()`](#c4d.threading.GeIsMainThreadAndNoDrawThread) can be used to detect the correct situation.

**Return type:** bool

**Returns:** **True** if called from the main thread and main thread does not execute a drawing operation, otherwise **False**.

### Thread Identification <a id="c4d.threading-function-Thread-Identification"></a>

#### `c4d.threading.GeGetCurrentThread()` <a id="c4d.threading.GeGetCurrentThread"></a>

Returns the current thread.

**Return type:** [`BaseThread`](BaseThread/index.md#c4d.threading.BaseThread)

**Returns:** The current thread.

#### `c4d.threading.IdentifyThread(bt)` <a id="c4d.threading.IdentifyThread"></a>

Identifies a thread’s type.

**Parameters:** **bt** ([*BaseThread*](BaseThread/index.md#c4d.threading.BaseThread)) – The thread to identify.

**Return type:** int

**Returns:**

The thread type:

|   |   |
|---|---|
| *THREADTYPE_NONE* | None. |
| *THREADTYPE_EDITORREDRAW* | Editor redraw. |
| *THREADTYPE_RENDEREDITOR* | Editor render. |
| *THREADTYPE_RENDEREXTERNAL* | External render. |

### Thread Information <a id="c4d.threading-function-Thread-Information"></a>

#### `c4d.threading.GeGetCurrentThreadCount()` <a id="c4d.threading.GeGetCurrentThreadCount"></a>

Gets the number of threads available.

*New in version R16.021.*

**Return type:** int

**Returns:** The number of current threads.

#### `c4d.threading.GeGetCurrentThreadId()` <a id="c4d.threading.GeGetCurrentThreadId"></a>

Returns a unique ID for the current thread.

> **Note:** Usually do not care about this.

**Return type:** int

**Returns:** The unique ID for the current thread.

### Thread Locking <a id="c4d.threading-function-Thread-Locking"></a>

#### `c4d.threading.GeThreadLock()` <a id="c4d.threading.GeThreadLock"></a>

Locks using a global semaphore.  
When locked, any other thread trying to acquire the lock will have to wait.  
Other threads will continue.

> **Note:**
>
> As this blocks all threads it should only be used if and when necessary.  
> A local semaphore is a more elegant and efficient solution to multiple thread data access.

#### `c4d.threading.GeThreadUnlock()` <a id="c4d.threading.GeThreadUnlock"></a>

Continues blocked threads after a call to [`GeThreadLock()`](#c4d.threading.GeThreadLock).
