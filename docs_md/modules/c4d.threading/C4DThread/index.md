<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.threading/C4DThread/index.html -->

# c4d.threading.C4DThread <a id="c4d-threading-c4dthread"></a>

## *class* `c4d.threading.C4DThread` <a id="c4d.threading.C4DThread"></a>

Here you see a very simple example how to create code which runs in another thread.

```python
import c4d

class UserThread(c4d.threading.C4DThread):

    def Main():
        # Put in your code here
        # which you want to run
        # in another thread
        pass

thread = UserThread()
thread.Start()
# Do some other operations here
thread.Wait(True) # Wait until the main method is done
```

> **Warning:**
>
> Ensure that every thread created by [`C4DThread`](#c4d.threading.C4DThread) is closed by the user on exit.  
> [PluginMessage()](../../../manuals/manual_implementing_plugins.md#plugin-messages) can be used for that purpose, intercepting *C4DPL_ENDACTIVITY* message.

> **See also:** [Threading Restrictions](../../../manuals/manual_scene_execution.md#threading-information) for important information about threads.

## Overview <a id="overview"></a>

**Methods to Call**

- [`C4DThread.End()`](#c4d.threading.C4DThread.End): End the thread.
- [`C4DThread.Get()`](#c4d.threading.C4DThread.Get): Get the [`BaseThread`](../BaseThread/index.md#c4d.threading.BaseThread) for this thread.
- [`C4DThread.IsRunning()`](#c4d.threading.C4DThread.IsRunning): Checks if the thread is running.
- [`C4DThread.Start()`](#c4d.threading.C4DThread.Start): Start the thread running.
- [`C4DThread.TestBreak()`](#c4d.threading.C4DThread.TestBreak): Checks if the thread received a break command to stop processing.
- [`C4DThread.Wait()`](#c4d.threading.C4DThread.Wait): Waits until the thread has finished.

**Methods to Override**

- [`C4DThread.Main()`](#c4d.threading.C4DThread.Main): Override with your thread main code.
- [`C4DThread.TestDBreak()`](#c4d.threading.C4DThread.TestDBreak): Override this to add user breaks such as pressing ESC.

## Members <a id="members"></a>

### Methods to Call <a id="c4d.threading.C4DThread-method-Methods-to-Call"></a>

#### `C4DThread.End(self, wait=True)` <a id="c4d.threading.C4DThread.End"></a>

End the thread.

> **Note:** If the thread does not check for [`TestBreak()`](#c4d.threading.C4DThread.TestBreak) then this function will not return and you will get a deadlock.

**Parameters:** **wait** (*bool*) – This parameter determines if thread termination is synchronous or asynchronous. If **True** the function will not return until the thread is finished. If **False** the function returns immediately although the thread will still run until it is finished.

#### `C4DThread.Get(self)` <a id="c4d.threading.C4DThread.Get"></a>

Get the [`BaseThread`](../BaseThread/index.md#c4d.threading.BaseThread) for this thread.

**Return type:** [c4d.threading.BaseThread](../BaseThread/index.md#c4d.threading.BaseThread)

**Returns:** The [`BaseThread`](../BaseThread/index.md#c4d.threading.BaseThread) of this thread.

#### `C4DThread.IsRunning(self)` <a id="c4d.threading.C4DThread.IsRunning"></a>

Checks if the thread is running.

**Return type:** bool

**Returns:** **True** if the thread is running, otherwise **False**.

#### `C4DThread.Start(self, mode=1, priority=0)` <a id="c4d.threading.C4DThread.Start"></a>

Start the thread running.

**Parameters:**

- **mode** (*int*) –

  Thread mode:

  |   |   |
  |---|---|
  | *THREADMODE_DEPRECATED_SYNCHRONOUS* | Synchronous thread. Deprecated. |
  | *THREADMODE_ASYNC* | Asynchronous thread. |
  | *THREADMODE_PRIVATE_OPENGL* | *New in version R18:* Private |

- **priority** (*int*) –

  Thread priority:

  | Symbol ID | Description |
  |---|---|
  | THREADPRIORITYEX_NORMAL | Normal. |
  | THREADPRIORITYEX_ABOVE | Above. |
  | THREADPRIORITYEX_BELOW | Below. |
  | THREADPRIORITYEX_LOWEST | Lowest. |

**Return type:** bool

**Returns:** **True** if the thread was started, otherwise **False**.

#### `C4DThread.TestBreak(self)` <a id="c4d.threading.C4DThread.TestBreak"></a>

Checks if the thread received a break command to stop processing.  
Normally this is only **True** when Cinema 4D is closing, or when [`End()`](#c4d.threading.C4DThread.End) has been called.

> **Note:** You can add more break conditions, such as if *ESC* has been pressed, in [`TestDBreak()`](#c4d.threading.C4DThread.TestDBreak).

**Return type:** bool

**Returns:** **True** if processing should be terminated, otherwise **False**.

#### `C4DThread.Wait(self, checkevents)` <a id="c4d.threading.C4DThread.Wait"></a>

Waits until the thread has finished.

**Parameters:** **checkevents** (*bool*) – If **False** then wait until the thread has finished. If **True** then additionally return if a Cinema 4D event occurred.

### Methods to Override <a id="c4d.threading.C4DThread-method-Methods-to-Override"></a>

#### `C4DThread.Main(self)` <a id="c4d.threading.C4DThread.Main"></a>

Override with your thread main code.

> **Note:**
>
> Remember that a scope might be done even the threaded code is still executed.  
> In this situation you have to use [`Wait()`](#c4d.threading.C4DThread.Wait) to wait until the code is finished or you should create an instance of your thread class into a scope which is longer alive than the code needs to run.

#### `C4DThread.TestDBreak(self)` <a id="c4d.threading.C4DThread.TestDBreak"></a>

Override this to add user breaks such as pressing ESC. This function is called by [`TestBreak()`](#c4d.threading.C4DThread.TestBreak).

**Return type:** bool

**Returns:** **True** if processing should be terminated, otherwise **False**.
