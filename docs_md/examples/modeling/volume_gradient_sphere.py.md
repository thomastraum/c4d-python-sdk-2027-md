<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/examples/modeling/volume_gradient_sphere.py.html -->

Local source: [examples/modeling/volume_gradient_sphere.py](../../../examples/modeling/volume_gradient_sphere.py)

# volume_gradient_sphere <a id="volume-gradient-sphere"></a>

Create a Spherical Volume filled with gradient data.

## volume_gradient_sphere.py <a id="volume-gradient-sphere-py"></a>

```python
"""Create a Spherical Volume filled with gradient data.

Topics:
    * Ovolume.SetVolume()
    * maxon.VolumeToolsInterface.CreateSphereVolume()
    * maxon.VolumeToolsInterface.CreateGradient()
"""
__author__ = "Maxime Adam"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "R20"

import c4d
import maxon

def main():

    # Creates a Volume Object
    volumeObj = c4d.BaseObject(c4d.Ovolume)
    if volumeObj is None:
        raise MemoryError("Failed to create a volume object.")

    # Creates a Sphere Volume
    sphereVolume = maxon.VolumeToolsInterface.CreateSphereVolume(maxon.Float(100.0),
                                                                 maxon.Vector(0, 100, 0),
                                                                 maxon.Float(1.0),
                                                                 maxon.Int32(2),
                                                                 maxon.ThreadRef(),
                                                                 None)

    # Fills the volume with a Gradient
    gradientVolume = maxon.VolumeToolsInterface.CreateGradientVolume(sphereVolume, maxon.ThreadRef())

    # Sets the VolumeRef in the Volume Object and insert it in the scene
    volumeObj.SetVolume(gradientVolume)
    doc.InsertObject(volumeObj)

    # Pushes an update event to Cinema 4D
    c4d.EventAdd()

if __name__ == '__main__':
    main()
```
