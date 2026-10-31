<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/examples/animation/simulation/modata_get_weights.py.html -->

Local source: [examples/animation/simulation/modata_get_weights.py](../../../../examples/animation/simulation/modata_get_weights.py)

# modata_get_weights <a id="modata-get-weights"></a>

Retrieves the weights from all clones of the active Cloner object.

## modata_get_weights.py <a id="modata-get-weights-py"></a>

```python
"""Retrieves the weights from all clones of the active Cloner object.

Topics:
    * c4d.modules.mograph.GeGetMoDataWeights()
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

    # Retrieves MoGraph Weight Tag from the cloner
    tag = op.GetTag(c4d.Tmgweight)
    if tag is None:
        raise RuntimeError("Failed to retrieve a Mograph Weight Tag on the selected object.")

    # Retrieves the clones weight values
    weights = c4d.modules.mograph.GeGetMoDataWeights(tag)

    # Prints clones weights
    print("'{0}' Clones Weights:".format(op.GetName()))

    for index, value in enumerate(weights):
        print("{0} : {1}".format(index, value))

if __name__ == '__main__':
    main()
```
