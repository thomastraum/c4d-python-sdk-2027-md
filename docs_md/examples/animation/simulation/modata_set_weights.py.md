<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/examples/animation/simulation/modata_set_weights.py.html -->

Local source: [examples/animation/simulation/modata_set_weights.py](../../../../examples/animation/simulation/modata_set_weights.py)

# modata_set_weights <a id="modata-set-weights"></a>

Sets a weight of 1.0 for all clones of the active Cloner object.

## modata_set_weights.py <a id="modata-set-weights-py"></a>

```python
"""Sets a weight of 1.0 for all clones of the active Cloner object.

Topics:
    * c4d.modules.mograph.GeSetMoDataWeights()
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "R18"

import c4d

def main():
    # Checks if there is an active object
    if op is None:
        raise ValueError("op is None, please select one object.")

    # Checks if the active object is a MoGraph Cloner Object
    if not op.IsInstanceOf(1018544):
        raise TypeError("Selected object is not a Mograph Cloner Object.")

    # Builds list for clones weights values
    weights = [1.0] * op[c4d.MG_LINEAR_COUNT]

    # Sets clones weights values
    c4d.modules.mograph.GeSetMoDataWeights(op, weights)

    # Pushes an update event to Cinema 4D
    c4d.EventAdd()

if __name__ == '__main__':
    main()
```
