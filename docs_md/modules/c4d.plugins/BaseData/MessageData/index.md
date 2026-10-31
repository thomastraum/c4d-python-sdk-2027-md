<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d.plugins/BaseData/MessageData/index.html -->

# c4d.plugins.MessageData <a id="c4d-plugins-messagedata"></a>

## *class* `c4d.plugins.MessageData` <a id="c4d.plugins.MessageData"></a>

A data class for creating message plugins.  
Use [`RegisterMessagePlugin()`](../../index.md#c4d.plugins.RegisterMessagePlugin) to register a message plugin.

Here is an example of a message plugin, which `CoreMessage()` method is called each 100 ms.

```python
import c4d

class TimerMessage(c4d.plugins.MessageData):

    def GetTimer(self):
        return 100

    def CoreMessage(self, id, bc):
        if id == c4d.MSG_TIMER:
            # Do something
        return True

if __name__ == "__main__":
    c4d.plugins.RegisterMessagePlugin(id=1234567, str="", info=0, dat=TimerMessage())
```

Parent Class:

- [`c4d.plugins.BaseData`](../index.md#c4d.plugins.BaseData)

## Overview <a id="overview"></a>

- [`MessageData.CoreMessage()`](#c4d.plugins.MessageData.CoreMessage): Override - Called to receive core messages.
- [`MessageData.GetTimer()`](#c4d.plugins.MessageData.GetTimer): Override - Called to return a time in milliseconds to receive timer messages (*MSG_TIMER*) with that interval in `CoreMessage()`.

## Members <a id="members"></a>

### Message Handling <a id="c4d.plugins.MessageData-method-Message-Handling"></a>

#### `MessageData.CoreMessage(self, id, bc)` <a id="c4d.plugins.MessageData.CoreMessage"></a>

Override - Called to receive core messages.

**Parameters:**

- **id** (*int*) – The received *core message\<MSG_CORE_EVENT>*.
- **bc** ([*c4d.BaseContainer*](../../../c4d/BaseContainer/index.md#c4d.BaseContainer)) – The core message container.

**Return type:** bool

**Returns:** Currently not used but a bool has to be returned.

#### `MessageData.GetTimer(self)` <a id="c4d.plugins.MessageData.GetTimer"></a>

Override - Called to return a time in milliseconds to receive timer messages (*MSG_TIMER*) with that interval in [`CoreMessage()`](#c4d.plugins.MessageData.CoreMessage).  
This method is queried again after each message.

**Return type:** int

**Returns:** The timer interval in milliseconds, or *0* for no timer messages.
