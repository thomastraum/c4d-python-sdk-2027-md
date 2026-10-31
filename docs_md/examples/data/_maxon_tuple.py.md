<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/examples/data/_maxon_tuple.py.html -->

Local source: [examples/data/_maxon_tuple.py](../../../examples/data/_maxon_tuple.py)

# _maxon_tuple <a id="maxon-tuple"></a>

Creates a Maxon Tuple of 3 fields (any maxon type is working).

## _maxon_tuple.py <a id="maxon-tuple-py"></a>

```python
"""Creates a Maxon Tuple of 3 fields (any maxon type is working).

Topics:
    * maxon.Tuple
    * Tuple.Set()
"""
__author__ = "Maxime Adam"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "R20"

import maxon

def main():
    # Creates a python tuple object
    pyTuple = ('test', 2, 4)

    # Creates a maxon tuple object that will accept 3 fields as string, int, int
    mTuple = maxon.Tuple((maxon.String, maxon.Int32, maxon.Int32))

    # Sets the value of the tuple
    for idx, value in enumerate(pyTuple):
        mTuple.Set(idx, value)

    print(mTuple)

if __name__ == "__main__":
    main()
```
