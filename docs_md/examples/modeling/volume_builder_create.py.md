<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/examples/modeling/volume_builder_create.py.html -->

Local source: [examples/modeling/volume_builder_create.py](../../../examples/modeling/volume_builder_create.py)

# volume_builder_create <a id="volume-builder-create"></a>

Creates a volume builder and inserts it into the active document.

## volume_builder_create.py <a id="volume-builder-create-py"></a>

```python
"""Creates a volume builder and inserts it into the active document.

Topics:
    * c4d.modules.volume.VolumeBuilder
    * BaseDocument.InsertObject()
"""
__author__ = "Maxime Adam"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "R20"

import c4d

def main():
    # Creates a volume builder object
    volumeBuilder = c4d.modules.volume.VolumeBuilder()
    if volumeBuilder is None:
        raise MemoryError("Failed to create a volume builder.")

    # Inserts it in the scene
    doc.InsertObject(volumeBuilder, None, None)

    # Pushes an update event to Cinema 4D
    c4d.EventAdd()

if __name__ == '__main__':
    main()
```
