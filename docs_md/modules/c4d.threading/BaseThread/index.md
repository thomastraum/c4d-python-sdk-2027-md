<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.threading/BaseThread/index.html -->

# c4d.threading.BaseThread <a id="c4d-threading-basethread"></a>

## *class* `c4d.threading.BaseThread` <a id="c4d.threading.BaseThread"></a>

This is the main thread base class used internally by Cinema 4D.

> **Warning:** This type cannot be instantiated.

## Overview <a id="overview"></a>

- [`BaseThread.End()`](#c4d.threading.BaseThread.End): End the thread.
- [`BaseThread.IsRunning()`](#c4d.threading.BaseThread.IsRunning): Check if the thread is running.
- [`BaseThread.TestBreak()`](#c4d.threading.BaseThread.TestBreak): Check if the thread received a break command to stop processing.

## Members <a id="members"></a>

### Thread Lifecycle <a id="c4d.threading.BaseThread-method-Thread-Lifecycle"></a>

#### `BaseThread.End(self, wait=True)` <a id="c4d.threading.BaseThread.End"></a>

End the thread. This function will not return before the thread has completely stopped.

> **Note:** If the thread does not check for [`TestBreak()`](#c4d.threading.BaseThread.TestBreak) then this function will not return and you will get a deadlock.

**Parameters:** **wait** (*bool*) – This parameter determines if thread termination is synchronous or asynchronous. If **True** the function will not return until the thread is finished. If **False** the function returns immediately although the thread will still run until it is finished.

#### `BaseThread.IsRunning(self)` <a id="c4d.threading.BaseThread.IsRunning"></a>

Check if the thread is running.

**Return type:** bool

**Returns:** **True** if the thread is running, otherwise **False**.

#### `BaseThread.TestBreak(self)` <a id="c4d.threading.BaseThread.TestBreak"></a>

Check if the thread received a break command to stop processing.

**Return type:** bool

**Returns:** **True** when Cinema 4D closes, or when a stopping condition has occurred, such as [`End()`](#c4d.threading.BaseThread.End).
