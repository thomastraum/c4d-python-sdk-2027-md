<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/examples/nodes/xpresso_from_tag.py.html -->

Local source: [examples/nodes/xpresso_from_tag.py](../../../examples/nodes/xpresso_from_tag.py)

# xpresso_from_tag <a id="xpresso-from-tag"></a>

Retrieves the Node Master (The BaseList2D object that holds all nodes) from an Xpresso Tag.

## xpresso_from_tag.py <a id="xpresso-from-tag-py"></a>

```python
"""Retrieves the Node Master (The BaseList2D object that holds all nodes) from an Xpresso Tag.

Topics:
    * c4d.modules.graphview.GvNodeMaster
"""
__author__ = "Maxime Adam"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "R13"

import c4d

def main():
    # Checks if selected object is valid
    if op is None:
        raise ValueError("op is none, please select one object.")

    # Retrieves the xpresso Tag
    xpressoTag = op.GetTag(c4d.Texpresso)
    if xpressoTag is None:
        raise ValueError("Make sure the selected object get an Xpresso Tag.")

    # Retrieves the node master
    gvNodeMaster = xpressoTag.GetNodeMaster()
    if gvNodeMaster is None:
        raise RuntimeError("Failed to retrieve the Node Master.")

    print(gvNodeMaster)

if __name__ == '__main__':
    main()
```
