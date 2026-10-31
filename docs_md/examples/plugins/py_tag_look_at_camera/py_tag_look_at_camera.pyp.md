<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/examples/plugins/py_tag_look_at_camera/py_tag_look_at_camera.pyp.html -->

Local source: [examples/plugins/py_tag_look_at_camera/py_tag_look_at_camera.pyp](../../../../examples/plugins/py_tag_look_at_camera/py_tag_look_at_camera.pyp)

# py_tag_look_at_camera <a id="py-tag-look-at-camera"></a>

Demonstrates how to implement a tag that forces the host object to look at the camera (like the Look At Camera Tag).

## DETAILS

The tag evaluates the active camera and updates the host orientation, providing a small example of implementing TagData.Execute().

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:

- Implementing a TagData orientation update
- Aligning a host object with the active camera

## Files <a id="files"></a>

### `py_tag_look_at_camera.pyp` <a id="py-tag-look-at-camera-pyp"></a>

```python
"""Demonstrates how to implement a tag that forces the host object to look at the camera (like the Look At Camera Tag).

The tag evaluates the active camera and updates the host orientation, providing a small example of implementing TagData.Execute().

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
    - Implementing a TagData orientation update
    - Aligning a host object with the active camera
"""
__copyright__ = "Copyright 2026, MAXON Computer"
__author__ = "Maxime Adam"
__date__ = "25/08/2026"
__license__ = "Apache-2.0 license"
__version__ = "13.0.0"

import os
import c4d

# Be sure to use a unique ID obtained from developers.maxon.net
PLUGIN_ID = 1028284

class LookAtCamera(c4d.plugins.TagData):
    """Look at Camera"""

    def Init(self, node, isCloneInit=False):
        """Called when Cinema 4D Initialize the TagData (used to define, default values).

        Args:
            node (c4d.GeListNode): The instance of the TagData.
            isCloneInit (bool): True if the tag data is a copy of another one.

        Returns:
            True on success, otherwise False.
        """
        self.InitAttr(node, bool, c4d.PYLOOKATCAMERA_PITCH)
        node[c4d.PYLOOKATCAMERA_PITCH] = True

        pd = c4d.PriorityData()
        if pd is None:
            raise MemoryError("Failed to create a priority data.")

        pd.SetPriorityValue(c4d.PRIORITYVALUE_CAMERADEPENDENT, True)
        node[c4d.EXPRESSION_PRIORITY] = pd

        return True

    def Execute(self, tag, doc, op, bt, priority, flags):
        """Called by Cinema 4D at each Scene Execution, this is the place where calculation should take place.

        Args:
            tag (c4d.BaseTag): The instance of the TagData.
            doc (c4d.documents.BaseDocument): The host document of the tag's object.
            op (c4d.BaseObject): The host object of the tag.
            bt (c4d.threading.BaseThread): The Thread that execute the this TagData.
            priority (EXECUTIONPRIORITY): Information about the execution priority of this TagData.
            flags (EXECUTIONFLAGS): Information about when this TagData is executed.
        """
        # Retrieves the current active base draw
        bd = doc.GetRenderBaseDraw()
        if bd is None:
            return c4d.EXECUTIONRESULT_OK

        # Retrieves the active camera
        cp = bd.GetSceneCamera(doc) if bd.GetSceneCamera(doc) is not None else bd.GetEditorCamera()
        if cp is None:
            return c4d.EXECUTIONRESULT_OK

        # Calculates the position to target
        local = cp.GetMg().off * (~(op.GetUpMg() * op.GetFrozenMln())) - op.GetRelPos()

        # Calculates the rotation to target
        hpb = c4d.utils.VectorToHPB(local)

        if not tag[c4d.PYLOOKATCAMERA_PITCH]:
            hpb.y = op.GetRelRot().y
        hpb.z = op.GetRelRot().z

        # Defines the rotation
        op.SetRelRot(hpb)

        return c4d.EXECUTIONRESULT_OK

if __name__ == "__main__":
    # Retrieves the icon path
    directory, _ = os.path.split(__file__)
    fn = os.path.join(directory, "res", "tpylookatcamera.tif")

    # Creates a BaseBitmap
    bmp = c4d.bitmaps.BaseBitmap()
    if bmp is None:
        raise MemoryError("Failed to create a BaseBitmap.")

    # Init the BaseBitmap with the icon
    if bmp.InitWith(fn)[0] != c4d.IMAGERESULT_OK:
        raise MemoryError("Failed to initialize the BaseBitmap.")

    c4d.plugins.RegisterTagPlugin(id=PLUGIN_ID,
                                  str="Py SDK - Look At Camera",
                                  info=c4d.TAG_EXPRESSION | c4d.TAG_VISIBLE,
                                  g=LookAtCamera,
                                  description="Tpylookatcamera",
                                  icon=bmp)
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_tag_look_at_camera/py_tag_look_at_camera.pyp)

### `res/c4d_symbols.h` <a id="res-c4d-symbols-h"></a>

```cpp
enum
{
    // End of symbol definition
    _DUMMY_ELEMENT_
};
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_tag_look_at_camera/res/c4d_symbols.h)

### `res/description/tpylookatcamera.h` <a id="res-description-tpylookatcamera-h"></a>

```cpp
#ifndef _Tpylookatcamera_H_
#define _Tpylookatcamera_H_

enum
{
    PYLOOKATCAMERA_PITCH     = 1000
}

#endif
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_tag_look_at_camera/res/description/tpylookatcamera.h)

### `res/description/tpylookatcamera.res` <a id="res-description-tpylookatcamera-res"></a>

```c4dres
CONTAINER Tpylookatcamera
{
	NAME Tpylookatcamera;
    INCLUDE Texpression;
    
    GROUP ID_TAGPROPERTIES
	{
		BOOL PYLOOKATCAMERA_PITCH { }
	}
}
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_tag_look_at_camera/res/description/tpylookatcamera.res)

### `res/strings_us/description/tpylookatcamera.str` <a id="res-strings-us-description-tpylookatcamera-str"></a>

```c4dstr
STRINGTABLE Tpylookatcamera
{
	Tpylookatcamera         "Py - Look At Camera";
    PYLOOKATCAMERA_PITCH    "Change Pitch Rotation";
}
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_tag_look_at_camera/res/strings_us/description/tpylookatcamera.str)
