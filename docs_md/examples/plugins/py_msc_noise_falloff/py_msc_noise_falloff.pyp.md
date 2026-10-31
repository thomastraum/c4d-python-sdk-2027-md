<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/examples/plugins/py_msc_noise_falloff/py_msc_noise_falloff.pyp.html -->

Local source: [examples/plugins/py_msc_noise_falloff/py_msc_noise_falloff.pyp](../../../../examples/plugins/py_msc_noise_falloff/py_msc_noise_falloff.pyp)

# py_msc_noise_falloff <a id="py-msc-noise-falloff"></a>

Demonstrates legacy falloffs, a technology that has been replaced by fields in R20.

## DETAILS

The falloff changes effector sampling with noise and exposes handles for interactive parameter editing. Falloffs are retained here for compatibility with older scenes.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:

- Sampling a noise-based falloff
- Managing interactive falloff handles
- Maintaining a legacy falloff for compatibility

## Files <a id="files"></a>

### `py_msc_noise_falloff.pyp` <a id="py-msc-noise-falloff-pyp"></a>

```python
"""Demonstrates legacy falloffs, a technology that has been replaced by fields in R20.

The falloff changes effector sampling with noise and exposes handles for interactive parameter editing. Falloffs are retained here for compatibility with older scenes.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
    - Sampling a noise-based falloff
    - Managing interactive falloff handles
    - Maintaining a legacy falloff for compatibility
"""
__copyright__ = "Copyright 2026, MAXON Computer"
__author__ = "Maxime Adam"
__date__ = "25/08/2026"
__license__ = "Apache-2.0 license"
__version__ = "14.0.0"

import c4d

# Be sure to use a unique ID obtained from developers.maxon.net
PLUGIN_ID = 1028347

class NoiseFalloffHelper(object):
    """Utility class for the noise falloff"""

    @staticmethod
    def PointInBox(p, data):
        """Returns if a point is in box.

        Args:
            p (c4d.Vector): The point position.
            data (c4d.BaseContainer): Falloff data information.

        Returns:
            True if the point is in box, otherwise False
        """
        res = True

        point = [p.x, p.y, p.z]

        size = data.size * data.nodemat * data.scale
        size -= data.nodemat.off
        size = [size.x, size.y, size.z]

        offset = [data.offset.x, data.offset.y, data.offset.z]

        pos = c4d.Vector() * data.nodemat
        pos = [pos.x, pos.y, pos.z]

        for i in range(3):
            res = pos[i] + offset[i] + size[i] > point[i] > pos[i] + offset[i] - size[i]
            if not res:
                break

        return res

    @staticmethod
    def DrawHandleLines(bd, size, i):
        """Helper method to draw a handle.

        Args:
            bd (c4d.BaseDraw): The editor's view.
            size (c4d.Vector): vector size of the object
            i (int): The Handle Id
        """

        # Defines the Draw Color
        bd.SetPen(c4d.GetViewColor(c4d.VIEWCOLOR_ACTIVEPOINT), 0)

        # According the handle id, defines start/end of the line handle
        p1, p2, p3, p4 = c4d.Vector(), c4d.Vector(), c4d.Vector(), c4d.Vector()

        if i == 0:
            p1 = c4d.Vector(0, -size.y, -size.z)
            p2 = c4d.Vector(0, -size.y, size.z)
            p3 = c4d.Vector(0, size.y, size.z)
            p4 = c4d.Vector(0, size.y, -size.z)

        elif i == 1:
            p1 = c4d.Vector(-size.x, 0, -size.z)
            p2 = c4d.Vector(-size.x, 0, size.z)
            p3 = c4d.Vector(size.x, 0, size.z)
            p4 = c4d.Vector(size.x, 0, -size.z)

        elif i == 2:
            p1 = c4d.Vector(-size.x, -size.y, 0)
            p2 = c4d.Vector(-size.x, size.y, 0)
            p3 = c4d.Vector(size.x, size.y, 0)
            p4 = c4d.Vector(size.x, -size.y, 0)

        # Draws each line as a grid
        bd.DrawLine(p1, p2, 0)
        bd.DrawLine(p2, p3, 0)
        bd.DrawLine(p3, p4, 0)
        bd.DrawLine(p4, p1, 0)

class NoiseFalloff(c4d.plugins.FalloffData, NoiseFalloffHelper):
    """Noise Falloff"""

    HANDLECOUNT = 6
    FBM_TYPES = (c4d.NOISE_ZADA, c4d.NOISE_DISPL_VORONOI,
                 c4d.NOISE_OBER, c4d.NOISE_FBM, c4d.NOISE_BUYA)

    seed = 1234567
    noise = c4d.utils.noise.C4DNoise()
    type = c4d.NOISE_BOX_NOISE
    octaves = 4.0
    absolute = False
    sampling = True
    sampleRad = 0.25
    detailAtt = 0.25
    repeat = 0
    maxoctave = 21
    lacunarity = 2.1
    h = 0.5

    dirty = 0

    def Init(self, falldata, bc):
        """Called when Cinema 4D Initialize the Falloff Object (used to define, default values).

        Args:
            falldata (c4d.modules.mograph.FalloffDataData): Falloff data information.
            bc (c4d.BaseContainer): Falloff's container.

        Returns:
            True on success, otherwise False.
        """
        if bc is None:
            return False

        # Defines defaults values in the BaseContainer if tey are not already sets
        if bc.GetData(c4d.PYNOISEFALLOFF_SEED) is None:
            bc.SetInt32(c4d.PYNOISEFALLOFF_SEED, 1234567)

        if bc.GetData(c4d.PYNOISEFALLOFF_TYPE) is None:
            bc.SetInt32(c4d.PYNOISEFALLOFF_TYPE, c4d.NOISE_BOX_NOISE)

        if bc.GetData(c4d.PYNOISEFALLOFF_SAMPRAD) is None:
            bc.SetFloat(c4d.PYNOISEFALLOFF_SAMPRAD, 0.25)

        if bc.GetData(c4d.PYNOISEFALLOFF_DETATT) is None:
            bc.SetFloat(c4d.PYNOISEFALLOFF_DETATT, 0.25)

        if bc.GetData(c4d.PYNOISEFALLOFF_OCTAVES) is None:
            bc.SetFloat(c4d.PYNOISEFALLOFF_OCTAVES, 4.0)

        if bc.GetData(c4d.PYNOISEFALLOFF_ABSOLUTE) is None:
            bc.SetBool(c4d.PYNOISEFALLOFF_ABSOLUTE, False)

        if bc.GetData(c4d.PYNOISEFALLOFF_MAXOCTAVE) is None:
            bc.SetInt32(c4d.PYNOISEFALLOFF_MAXOCTAVE, 21)

        if bc.GetData(c4d.PYNOISEFALLOFF_LACUNARITY) is None:
            bc.SetFloat(c4d.PYNOISEFALLOFF_LACUNARITY, 2.1)

        if bc.GetData(c4d.PYNOISEFALLOFF_H) is None:
            bc.SetFloat(c4d.PYNOISEFALLOFF_H, 0.5)

        return True

    def InitFalloff(self, bc, falldata):
        """Called when Cinema 4D initialize the Falloff (Before a sampling process).

        Args:
            bc (c4d.BaseContainer): Falloff's container.
            falldata (c4d.modules.mograph.FalloffDataData): Falloff data information.

        Returns:
            True on success, otherwise False.
        """
        if bc is None:
            return False

        # If the dirtiness of the BaseContainer didn't change, simply returns
        dirty = bc.GetDirty()
        if self.dirty == dirty:
            return True

        # Retrieves parameters from the falloff object to the python object
        self.seed = bc.GetInt32(c4d.PYNOISEFALLOFF_SEED)
        self.type = bc.GetInt32(c4d.PYNOISEFALLOFF_TYPE)
        self.octaves = bc.GetFloat(c4d.PYNOISEFALLOFF_OCTAVES)
        self.absolute = bc.GetBool(c4d.PYNOISEFALLOFF_ABSOLUTE)
        self.sampling = bc.GetInt32(c4d.PYNOISEFALLOFF_SAMPLING) == 0
        self.sampleRad = bc.GetFloat(c4d.PYNOISEFALLOFF_SAMPRAD)
        self.detailAtt = bc.GetFloat(c4d.PYNOISEFALLOFF_DETATT)
        self.repeat = bc.GetInt32(c4d.PYNOISEFALLOFF_REPEAT)

        self.maxoctave = bc.GetInt32(c4d.PYNOISEFALLOFF_MAXOCTAVE)
        self.lacunarity = bc.GetFloat(c4d.PYNOISEFALLOFF_LACUNARITY)
        self.h = bc.GetInt32(c4d.PYNOISEFALLOFF_H)

        # Initializes the noise if needed
        self.noise = c4d.utils.noise.C4DNoise(seed=self.seed)
        if self.type in self.FBM_TYPES:
            self.noise.InitFbm(self.maxoctave, self.lacunarity, self.h)

        self.dirty = dirty

        return True

    def GetDVisible(self, id, bc, desc_bc):
        """Called  by Cinema 4D to decide which parameters is currently visible.

        Args:
            id (c4d.DescID): The Description ID of the parameter
            bc (c4d.BaseContainer): Falloff's container
            desc_bc (c4d.BaseContainer): The description, encoded to a container

        Returns:
            True if the parameter should be visible, otherwise False.
        """

        # Displays Octave only if current noise have Octave
        if id[0].id == c4d.PYNOISEFALLOFF_OCTAVES:
            return self.noise.HasOctaves(bc.GetInt32(c4d.PYNOISEFALLOFF_TYPE))

        # Displays Absolute only if current noise have Absolute
        elif id[0].id == c4d.PYNOISEFALLOFF_ABSOLUTE:
            return self.noise.HasAbsolute(bc.GetInt32(c4d.PYNOISEFALLOFF_TYPE))

        # Displays fbm types only if current noise have fbm
        elif id[0].id == c4d.PYNOISEFALLOFF_FBMSETTINGS:
            return bc.GetInt32(c4d.PYNOISEFALLOFF_TYPE) in self.FBM_TYPES

        # For any other parameters, display it
        return True

    def Sample(self, p, data):
        """Called by Cinema 4D, when a position is sampled.

        Args:
            p (c4d.Vector): The position of the point to sample in falloff space.
            data (c4d.modules.mograph.FalloffDataData): Falloff data information.

        Returns:
            float: How the effector modify the original object from 0.0 to 1.0
        """
        # If the point is in the bounding box of the falloff
        if NoiseFalloff.PointInBox(data.mat * p, data):
            return self.noise.Noise(self.type, self.sampling, data.mat * p, 0.0,
                                    self.octaves, self.absolute, self.sampleRad, self.detailAtt, self.repeat)
        else:
            return 1.0
    """========== Start of Handle Management =========="""

    def GetHandleCount(self, bc, data):
        """Called by Cinema 4D to retrieve the count of Handle the object will have.

        Args:
            bc (c4d.BaseContainer): Falloff's container
            data (c4d.modules.mograph.FalloffDataData): Falloff data information.

        Returns:
            int: The number of handle
        """
        return self.HANDLECOUNT

    def GetHandle(self, bc, i, info, data):
        """Called by Cinema 4D to retrieve the information of a given handle ID to represent a/some parameter(s).

        Args:
            bc (c4d.BaseContainer): Falloff's container
            i (int): The handle index.
            data (c4d.modules.mograph.FalloffDataData): Falloff data information.
            info (c4d.HandleInfo): The information for the requested handle to be filled.
        """
        if bc is None:
            return

        # Retrieves the current size, offset from noise parameter
        size = bc.GetVector(c4d.FALLOFF_SIZE) * bc.GetFloat(c4d.FALLOFF_SCALE)
        offset = bc.GetVector(c4d.FALLOFF_SHAPE_OFFSET)

        # Regarding the orientation, defines position / direction of the handle
        if i == c4d.FALLOFF_SHAPE_AXIS_XP:
            info.position = c4d.Vector(size.x + offset.x, offset.y, offset.z)
            info.direction = c4d.Vector(1.0, 0.0, 0.0)
        elif i == c4d.FALLOFF_SHAPE_AXIS_XN:
            info.position = c4d.Vector(-size.x + offset.x, offset.y, offset.z)
            info.direction = c4d.Vector(-1.0, 0.0, 0.0)
        elif i == c4d.FALLOFF_SHAPE_AXIS_YP:
            info.position = c4d.Vector(offset.x, size.y + offset.y, offset.z)
            info.direction = c4d.Vector(0.0, 1.0, 0.0)
        elif i == c4d.FALLOFF_SHAPE_AXIS_YN:
            info.position = c4d.Vector(offset.x, -size.y + offset.y, offset.z)
            info.direction = c4d.Vector(0.0, -1.0, 0.0)
        elif i == c4d.FALLOFF_SHAPE_AXIS_ZP:
            info.position = c4d.Vector(offset.x, offset.y, size.z + offset.z)
            info.direction = c4d.Vector(0.0, 0.0, 1.0)
        elif i == c4d.FALLOFF_SHAPE_AXIS_ZN:
            info.position = c4d.Vector(offset.x, offset.y, -size.z + offset.z)
            info.direction = c4d.Vector(0.0, 0.0, -1.0)

        info.type = c4d.HANDLECONSTRAINTTYPE_LINEAR

    def SetHandle(self, bc, i, p, data):
        """Called by Cinema 4D when the user set the handle.

        This is the place to retrieve the information of a given handle ID and drive your parameter(s).

        Args:
            bc (c4d.BaseContainer): Falloff's container
            i (int): The handle index.
            p (c4d.Vector): The new Handle Position.
            data (c4d.modules.mograph.FalloffDataData): Falloff data information.
        """
        if bc is None:
            return False

        # Retrieves the Falloff size
        size = bc.GetVector(c4d.FALLOFF_SIZE)

        # According the moved handles retrieves the position
        if i == 0 or i == 1:
            size = c4d.Vector(abs(p.x), size.y, size.z)
        elif i == 2 or i == 3:
            size = c4d.Vector(size.x, abs(p.y), size.z)
        elif i == 4 or i == 5:
            size = c4d.Vector(size.x, size.y, abs(p.z))

        # Defines the size vector
        bc.SetVector(c4d.FALLOFF_SIZE, size)

    def Draw(self, data, drawpass, bd, bh):
        """Called by Cinema 4D when the display is updated to display.

        Here you can draw visual representations and handles for your object in the 3D view.

        Args:
            data (c4d.BaseContainer.): The node settings container.
            op (c4d.modules.mograph.FalloffDataData): Falloff data information.
            drawpass (DRAWPASS): The current draw pass.
            bd (c4d.BaseDraw): The editor's view.
            bh (c4d.plugins.BaseDrawHelp): The BaseDrawHelp editor's view.

        Returns:
            The result of the drawing (most likely c4d.DRAWRESULT_OK)
        """
        # If the current draw pass is not the handle, skip this Draw Call.
        if drawpass == c4d.DRAWPASS_HIGHLIGHTS:
            return True

        # Defines the size and the position of the object
        size = data.size * data.scale
        mat = c4d.Matrix(data.nodemat.off + data.offset, data.nodemat.v1,
                         data.nodemat.v2, data.nodemat.v3)

        # Defines the drawing matrix to the object matrix
        bd.SetMatrix_Matrix(None, mat)

        # Draws the overall bounding box
        box = c4d.Matrix()
        box.v1 = box.v1 * size.x
        box.v2 = box.v2 * size.y
        box.v3 = box.v3 * size.z
        bd.DrawBox(box, 1.0, c4d.GetViewColor(c4d.VIEWCOLOR_ACTIVEPOINT), True)

        # Draws each handles
        NoiseFalloff.DrawHandleLines(bd, size, 0)
        NoiseFalloff.DrawHandleLines(bd, size, 1)
        NoiseFalloff.DrawHandleLines(bd, size, 2)

        return True
    """========== End of Handle Management =========="""

if __name__ == "__main__":
    # Registers the Falloff Plugin
    c4d.plugins.RegisterFalloffPlugin(id=PLUGIN_ID,
                                      str="Py SDK - Noise Falloff",
                                      info=0,
                                      g=NoiseFalloff,
                                      description="Ofalloff_pynoise")
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_msc_noise_falloff/py_msc_noise_falloff.pyp)

### `res/c4d_symbols.h` <a id="res-c4d-symbols-h"></a>

```cpp
enum
{
    // End of symbol definition
    _DUMMY_ELEMENT_
};
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_msc_noise_falloff/res/c4d_symbols.h)

### `res/description/Ofalloff_pynoise.h` <a id="res-description-ofalloff-pynoise-h"></a>

```cpp
#ifndef _Ofalloff_pyrandom_H_
#define _Ofalloff_pyrandom_H_

enum
{
    PYNOISEFALLOFF_SETTINGS    = 7000,
    
    PYNOISEFALLOFF_SEED = 5000,
    PYNOISEFALLOFF_TYPE = 5001,

        NOISE_BOX_NOISE             =  1,
        NOISE_BLIST_TURB            =  2,
        NOISE_BUYA                  =  3,
        NOISE_CELL_NOISE            =  4,
        NOISE_CRANAL                =  5,
        NOISE_DENTS                 =  6,
        NOISE_DISPL_TURB            =  7,
        NOISE_FBM                   =  8,
        NOISE_HAMA                  =  9,
        NOISE_LUKA                  = 10,
        NOISE_MOD_NOISE             = 11,
        NOISE_NAKI                  = 12,
        NOISE_NOISE                 = 13,
        NOISE_NUTOUS                = 14,
        NOISE_OBER                  = 15,
        NOISE_PEZO                  = 16,
        NOISE_POXO                  = 17,
        NOISE_RANDOM                = 18,
        NOISE_SEMA                  = 19,
        NOISE_STUPL                 = 20,
        NOISE_TURBULENCE            = 21,
        NOISE_VL_NOISE              = 22,
        NOISE_WAVY_TURB             = 23,
        NOISE_CELL_VORONOI          = 24,
        NOISE_DISPL_VORONOI         = 25,
        NOISE_SPARSE_CONV           = 26,
        NOISE_VORONOI_1             = 27,
        NOISE_VORONOI_2             = 28,
        NOISE_VORONOI_3             = 29,
        NOISE_ZADA                  = 30,
        NOISE_FIRE                  = 31,
        NOISE_ELECTRIC              = 32,
        NOISE_GASEOUS               = 33,

        NOISE_NONE                  = 99,
    
    PYNOISEFALLOFF_SAMPLING   = 5002,
    
        SAMPLING_2D = 0,
        SAMPLING_3D = 1,
    
    PYNOISEFALLOFF_SAMPRAD = 5003,
    PYNOISEFALLOFF_DETATT  = 5004,
    PYNOISEFALLOFF_REPEAT  = 5005,
        
        REPEAT_0    = 0,
        REPEAT_1    = 1,
        REPEAT_3    = 3,
        REPEAT_7    = 7,
        REPEAT_15   = 15,
        REPEAT_31   = 31,
        REPEAT_63   = 63,
        REPEAT_127  = 127,
        REPEAT_255  = 255,
        REPEAT_511  = 511,
        REPEAT_1023 = 1023,
    
    PYNOISEFALLOFF_OCTAVES  = 5006,
    PYNOISEFALLOFF_ABSOLUTE = 5007,
    
    PYNOISEFALLOFF_FBMSETTINGS = 7001,
    
    PYNOISEFALLOFF_MAXOCTAVE  = 5008,
    PYNOISEFALLOFF_LACUNARITY = 5009,
    PYNOISEFALLOFF_H          = 5010
};

#endif
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_msc_noise_falloff/res/description/Ofalloff_pynoise.h)

### `res/description/Ofalloff_pynoise.res` <a id="res-description-ofalloff-pynoise-res"></a>

```c4dres
CONTAINER Ofalloff_pynoise
{
	NAME Ofalloff_pyrandom;
    INCLUDE Ofalloff_standard;
    
    HIDE FALLOFF_SHAPE_AXIS;
    
    HIDE FALLOFF_SHAPE_SLICE;
    
    HIDE FALLOFF_FUNCTION_RADIUS;
        
    GROUP FALLOFF_GROUPFALLOFF
	{
        GROUP FALLOFF_SETTINGS
		{
            GROUP PYNOISEFALLOFF_SETTINGS
            {
                OPEN;
                
                LONG PYNOISEFALLOFF_SEED { MIN 0; }
                
                LONG PYNOISEFALLOFF_TYPE
                {
                    CYCLE
                    {
                        NOISE_BOX_NOISE;
                        NOISE_BLIST_TURB;
                        NOISE_BUYA;
                        NOISE_CELL_NOISE;
                        NOISE_CRANAL;
                        NOISE_DENTS;
                        NOISE_DISPL_TURB;
                        NOISE_FBM;
                        NOISE_HAMA;
                        NOISE_LUKA;
                        NOISE_MOD_NOISE;
                        NOISE_NAKI;
                        NOISE_NOISE;
                        NOISE_NUTOUS;
                        NOISE_OBER;
                        NOISE_PEZO;
                        NOISE_POXO;
                        NOISE_RANDOM;
                        NOISE_SEMA;
                        NOISE_STUPL;
                        NOISE_TURBULENCE;
                        NOISE_VL_NOISE;
                        NOISE_WAVY_TURB;
                        NOISE_FIRE;
                        NOISE_ELECTRIC;
                        NOISE_GASEOUS;
                        NOISE_CELL_VORONOI;
                        NOISE_DISPL_VORONOI;
                        NOISE_SPARSE_CONV;
                        NOISE_VORONOI_1;
                        NOISE_VORONOI_2;
                        NOISE_VORONOI_3;
                        NOISE_ZADA;
                    }
                }
                
                LONG PYNOISEFALLOFF_SAMPLING
                {
                    CYCLE
                    {
                        SAMPLING_2D;
                        SAMPLING_3D;
                    }
                }
                
                REAL PYNOISEFALLOFF_SAMPRAD { MIN 0; STEP 0.01; }
                REAL PYNOISEFALLOFF_DETATT { MIN 0; STEP 0.01; }
                LONG PYNOISEFALLOFF_REPEAT
                {
                    CYCLE
                    {
                        REPEAT_0;
                        REPEAT_1;
                        REPEAT_3;
                        REPEAT_7;
                        REPEAT_15;
                        REPEAT_31;
                        REPEAT_63;
                        REPEAT_127;
                        REPEAT_255;
                        REPEAT_511;
                        REPEAT_1023;
                    }
                }
                
                REAL PYNOISEFALLOFF_OCTAVES { MIN 0; }
                BOOL PYNOISEFALLOFF_ABSOLUTE {}
                
                GROUP PYNOISEFALLOFF_FBMSETTINGS
                {
                    OPEN;
                    
                    LONG PYNOISEFALLOFF_MAXOCTAVE { MIN 0; }
                    LONG PYNOISEFALLOFF_LACUNARITY { MIN 0; }
                    REAL PYNOISEFALLOFF_H { MIN 0; STEP 0.01; }
                }
            }
        }
    }
}
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_msc_noise_falloff/res/description/Ofalloff_pynoise.res)

### `res/strings_us/description/Ofalloff_pynoise.str` <a id="res-strings-us-description-ofalloff-pynoise-str"></a>

```c4dstr
STRINGTABLE Ofalloff_pynoise
{
	Ofalloff_pyrandom "Falloff Noise";
    
    PYNOISEFALLOFF_SETTINGS    "Py - NoiseFalloff Settings";
    
    PYNOISEFALLOFF_SEED "Seed";
    
    PYNOISEFALLOFF_TYPE "Noise";
    
        NOISE_BOX_NOISE             "Box Noise";
        NOISE_BLIST_TURB            "Blistered Turbulence";
        NOISE_BUYA                  "Buya";
        NOISE_CELL_NOISE            "Cell Noise";
        NOISE_CRANAL                "Cranal";
        NOISE_DENTS                 "Dents";
        NOISE_DISPL_TURB            "Displaced Turbulence";
        NOISE_FBM                   "FBM";
        NOISE_HAMA                  "Hama";
        NOISE_LUKA                  "Luka";
        NOISE_MOD_NOISE             "Mod Noise";
        NOISE_NAKI                  "Naki";
        NOISE_NOISE                 "Noise";
        NOISE_NUTOUS                "Nutous";
        NOISE_OBER                  "Ober";
        NOISE_PEZO                  "Pezo";
        NOISE_POXO                  "Poxo";
        NOISE_RANDOM                "Random";
        NOISE_SEMA                  "Sema";
        NOISE_STUPL                 "Stupl";
        NOISE_TURBULENCE            "Turbulence";
        NOISE_VL_NOISE              "VL Noise";
        NOISE_WAVY_TURB             "Wavy Turbulence";
        NOISE_FIRE                  "Fire";
        NOISE_ELECTRIC              "Electric";
        NOISE_GASEOUS               "Gaseous";
        NOISE_CELL_VORONOI          "Cell Voronoi";
        NOISE_DISPL_VORONOI         "Displaced Voronoi";
        NOISE_SPARSE_CONV           "Sparse Convolution";
        NOISE_VORONOI_1             "Voronoi 1";
        NOISE_VORONOI_2             "Voronoi 2";
        NOISE_VORONOI_3             "Voronoi 3";
        NOISE_ZADA                  "Zada";
        NOISE_NONE                  "None";
    
    PYNOISEFALLOFF_SAMPLING "Sampling";
    
        SAMPLING_2D "2D";
        SAMPLING_3D "3D";
    
    PYNOISEFALLOFF_SAMPRAD "Sample Radius";
    PYNOISEFALLOFF_DETATT  "Detail Attenuation";
    PYNOISEFALLOFF_REPEAT  "Repeat";
        
        REPEAT_0    "0";
        REPEAT_1    "1";
        REPEAT_3    "3";
        REPEAT_7    "7";
        REPEAT_15   "15";
        REPEAT_31   "31";
        REPEAT_63   "63";
        REPEAT_127  "127";
        REPEAT_255  "255";
        REPEAT_511  "511";
        REPEAT_1023 "1023";
        
    PYNOISEFALLOFF_OCTAVES  "Octaves";
    PYNOISEFALLOFF_ABSOLUTE "Absolute";
    
    PYNOISEFALLOFF_FBMSETTINGS "FBM Settings";
    
    PYNOISEFALLOFF_MAXOCTAVE  "Max Octave";
    PYNOISEFALLOFF_LACUNARITY "Lacunarity";
    PYNOISEFALLOFF_H          "H";
}
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_msc_noise_falloff/res/strings_us/description/Ofalloff_pynoise.str)
