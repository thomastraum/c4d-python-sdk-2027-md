<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/examples/nodes/xpresso_delete.py.html -->

Local source: [examples/nodes/xpresso_delete.py](../../../examples/nodes/xpresso_delete.py)

# xpresso_delete <a id="xpresso-delete"></a>

Deletes the first node created from the Xpresso Tag of the selected object.

## xpresso_delete.py <a id="xpresso-delete-py"></a>

```python
"""Deletes the first node created from the Xpresso Tag of the selected object.

Topics:
    * c4d.modules.graphview.GvNodeMaster
    * c4d.modules.graphview.GvNode
    * GvNodeMaster.GetRoot()
    * GeListNode.GetDown()
    * GeListNode.Remove()
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

    # Retrieves the Root node (the Main XGroup) that holds all others nodes
    gvRoot = gvNodeMaster.GetRoot()
    if gvRoot is None:
        raise RuntimeError("Failed to retrieve the Root Node.")

    # Gets the first child
    firstNode = gvRoot.GetDown()
    if firstNode is None:
        raise RuntimeError("Failed to retrieve the First Node.")

    # GvNode is a GeListNode so you can simply use Remove
    firstNode.Remove()

    # Pushes an update event to Cinema 4D
    c4d.EventAdd()

if __name__ == '__main__':
    main()
```
