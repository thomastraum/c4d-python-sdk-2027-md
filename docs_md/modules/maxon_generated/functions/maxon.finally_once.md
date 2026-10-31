<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/functions/maxon.finally_once.html -->

# maxon.finally_once <a id="maxon-finally-once"></a>

## `maxon.finally_once(func, *args, **kwargs)` <a id="maxon.finally_once"></a>

Executes a function when the current scope is left.

> **Note:** An optional parameter *canRaise* can be passed to notify that *func* may eventually raise.

**Parameters:**

- **func** (`function(*args, **kwargs)`) – Function to be called.
- **args** (*Any*) – Optional arguments to be passed to func.
- **kwargs** (*Any*) – Optional settings like *canRaise* to control if *func* can raise an exception.

```python
cleanup = finally_once(lambda x: MyFunction(x), canRaise=False)
```
