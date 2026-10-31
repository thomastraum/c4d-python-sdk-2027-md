<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/examples/plugins/py_tool_sculpt_pull_brush/py_tool_sculpt_pull_brush.pyp.html -->

Local source: [examples/plugins/py_tool_sculpt_pull_brush/py_tool_sculpt_pull_brush.pyp](../../../../examples/plugins/py_tool_sculpt_pull_brush/py_tool_sculpt_pull_brush.pyp)

# py_tool_sculpt_pull_brush <a id="py-tool-sculpt-pull-brush"></a>

Demonstrates how to implement a brush tool that modifies a BaseObject by pulling all points under the brush.

## DETAILS

The brush finds points under the cursor and displaces them according to the pull interaction, illustrating the SculptBrushToolData callbacks.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:

- Finding points under a sculpt brush
- Displacing points with a pull interaction

## Files <a id="files"></a>

### `py_tool_sculpt_pull_brush.pyp` <a id="py-tool-sculpt-pull-brush-pyp"></a>

```python
"""Demonstrates how to implement a brush tool that modifies a BaseObject by pulling all points under the brush.

The brush finds points under the cursor and displaces them according to the pull interaction, illustrating the SculptBrushToolData callbacks.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
    - Finding points under a sculpt brush
    - Displacing points with a pull interaction
"""
__copyright__ = "Copyright 2026, MAXON Computer"
__author__ = "Kent Barber"
__date__ = "25/08/2026"
__license__ = "Apache-2.0 license"
__version__ = "16.0.0"

import c4d

# Be sure to use a unique ID obtained from developers.maxon.net
PLUGIN_ID = 1031349

# Values must match with the header file
IDS_PYTHON_BRUSH_PULL = 10000

class SculptBrushPullTool(c4d.plugins.SculptBrushToolData):
    """Inherit from SculptBrushToolData to create your own sculpting tool"""

    def GetToolPluginId(self):
        """Called by Cinema 4D, to know the plugin ID of this tool.

        Returns:
            int: The unique id for the tool plugin as obtained from developers.maxon.net
        """
        return PLUGIN_ID

    def GetResourceSymbol(self):
        """Called by Cinema 4D, to know the resource to be used for this tool.

        Returns:
            str: The resource name of the tool
        """
        return "pythonpullbrush"

    def ApplyDab(self, dab):
        """Called by Cinema 4D, to modify the sculpt object.

        Implement the brush functionality in this method.

        Args:
            dab (c4d.modules.sculpting.BrushDabData): The brush dab data.
        """
        # Retrieves the strength applied
        strength = dab.GetBrushStrength()
        if strength == 0:
            return True

        # Retrieves tool parameters
        bc = dab.GetData()

        # Retrieves polygons count affected
        pointCount = dab.GetPointCount()

        # Retrieves if it's a preview action (aka do nothing on the mesh)
        usePreview = dab.IsPreviewDab()

        # Retrieves polygons objects affected
        polyObj = dab.GetPolygonObject()

        # Retrieves the radius (size) of the object bounding box
        rad = polyObj.GetRad()

        # Pre-calculates the offset vector
        dim = rad.GetLength() * 0.005
        buildup = bc.GetFloat(c4d.MDATA_SCULPTBRUSH_SETTINGS_BUILDUP) * 0.002
        pressurePreMult = strength * 10.0 * buildup * dim
        multPreMult = dab.GetNormal() * pressurePreMult

        # Checks if the user hold the CLTR key (it will sets OVERRIDE_INVERT)
        invert = dab.GetBrushOverride() & c4d.OVERRIDE_INVERT
        if invert is True or bc.GetBool(c4d.MDATA_SCULPTBRUSH_SETTINGS_INVERT) is True:
            # Inverses the direction according result
            multPreMult = -multPreMult

        # Checks if the invert checkbox is enabled in the UI.
        if bc.GetBool(c4d.MDATA_SCULPTBRUSH_SETTINGS_INVERT) is True:
            # Inverses the direction according result
            multPreMult = -multPreMult

        # Loops over every points for this dab and move it if we need to.
        for a in range(0, pointCount):
            # Retrieves the index of the point on the PolygonObject.
            pointData = dab.GetPointData(a)
            pointIndex = pointData["pointIndex"]

            # Retrieves the falloff for this point. This will always be a value from 0 to 1.
            # The value returned is a combination of the following values all multiplied together to give a final value.
            # - The falloff curve.
            # - The color of the stamp with its color value averaged to gray and adjusted by the Gray Value.
            # - The color of the stencil with its color value averaged to gray and adjusted by the Gray Value.
            fallOff = dab.GetBrushFalloff(a)

            # If the falloff value is 0 then we don't have to do anything at all.
            if fallOff == 0:
                continue

            # Multiplies the falloff value with the multiply vector we calculated
            # early. This will result in an offset vector that we want to move the
            # vertex on the model by.
            res = fallOff * multPreMult

            # If the brush is not in preview mode (preview mode happens with in
            # DragDab or DragRect mode) then we can offset the final point on the
            # selected layer.
            if usePreview is False:
                dab.OffsetPoint(pointIndex, res)
            # Otherwise applies the offset to the preview layer.
            else:
                dab.OffsetPreviewPoint(pointIndex, res)
        return True

if __name__ == "__main__":
    # Defines global parameter for the brush (how the brush should act)
    params = c4d.modules.sculpting.SculptBrushParams()
    params.EnableInvertCheckbox(True)
    params.EnableBuildup(True)
    params.EnableModifier(True)
    params.SetFloodType(c4d.SCULPTBRUSHDATATYPE_POINT)
    params.SetBrushMode(c4d.SCULPTBRUSHMODE_NORMAL)
    params.SetFirstHitPointType(c4d.FIRSTHITPPOINTTYPE_SELECTED)
    params.SetUndoType(c4d.SCULPTBRUSHDATATYPE_POINT)

    # Registers the sculpt brush plugin. PLUGINFLAG_HIDEPLUGINMENU hides the natural menu entry of
    # this plugin. Omit this flag or replace it by 0 when you do not have custom menu handling as
    # the SDK has (see py_menu).
    c4d.plugins.RegisterSculptBrushPlugin(id=PLUGIN_ID,
                                          str="Py SDK - Pull Brush",
                                          info=c4d.PLUGINFLAG_HIDEPLUGINMENU, 
                                          icon=None,
                                          help="Python Pull Brush",
                                          sculptparams=params,
                                          dat=SculptBrushPullTool())
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_tool_sculpt_pull_brush/py_tool_sculpt_pull_brush.pyp)

### `res/c4d_symbols.h` <a id="res-c4d-symbols-h"></a>

```cpp
#ifndef C4D_SYMBOLS_H__
#define C4D_SYMBOLS_H__

enum
{
    // string table definitions
    IDS_PYTHON_BRUSH_PULL =  10000,
    IDS_PYTHON_BRUSH_PULL_HELP,

// End of symbol definition
    _DUMMY_ELEMENT_
};

#endif	// C4D_SYMBOLS_H__
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_tool_sculpt_pull_brush/res/c4d_symbols.h)

### `res/description/pythonpullbrush.h` <a id="res-description-pythonpullbrush-h"></a>

```cpp
#ifndef PYTHONPULLBRUSH_H__
#define PYTHONPULLBRUSH_H__

enum
{
    PythonPullBrush_Start = 20000,
};

#endif	// PYTHONPULLBRUSH_H__
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_tool_sculpt_pull_brush/res/description/pythonpullbrush.h)

### `res/description/pythonpullbrush.res` <a id="res-description-pythonpullbrush-res"></a>

```c4dres
CONTAINER pythonpullbrush
{
  NAME pythonpullbrush;
  INCLUDE toolsculptbrushbase;
 
    GROUP MDATA_SCULPTBRUSH_SETTINGS_GROUP
    {
        COLUMNS 3;

        REAL MDATA_SCULPTBRUSH_SETTINGS_BUILDUP { MIN 1; MAX 100; MINSLIDER 1; MAXSLIDER 100; CUSTOMGUI REALSLIDER; FIT_H; SCALE_H; }
        STATICTEXT { JOINENDSCALE; }
        STATICTEXT { JOINEND; }

        BOOL MDATA_SCULPTBRUSH_SETTINGS_INVERT { }
        STATICTEXT { DUMMY; }
        STATICTEXT { DUMMY; }

        GROUP
        {
            COLUMNS 3;
            LONG MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE
            {
                CYCLE
                {
                    MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_FREEHAND;
                    MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_DRAGRECT;
                    MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_DRAGDAB;
                    MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_LINE;
                    MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_LASSO_FILL;
                    MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_POLY_FILL;
                    MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_RECTANGLE_FILL;
                }
            }
            BOOL MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_FILL_SYMMETRY { }
            BOOL MDATA_SCULPTBRUSH_SETTINGS_FILL_BACKFACES { }
        }
        STATICTEXT { JOINENDSCALE; }
        STATICTEXT { JOINEND; }

        SEPARATOR { LINE; }
        STATICTEXT { JOINENDSCALE; }
        STATICTEXT { JOINEND; }
    }

}
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_tool_sculpt_pull_brush/res/description/pythonpullbrush.res)

### `res/strings_us/c4d_strings.str` <a id="res-strings-us-c4d-strings-str"></a>

```c4dstr
// C4D-StringResource
// Identifier	Text

STRINGTABLE
{
    IDS_PYTHON_BRUSH_PULL		"Python Pull";
    IDS_PYTHON_BRUSH_PULL_HELP	"Pull or push the surface";
}
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_tool_sculpt_pull_brush/res/strings_us/c4d_strings.str)

### `res/strings_us/description/pythonpullbrush.str` <a id="res-strings-us-description-pythonpullbrush-str"></a>

```c4dstr
STRINGTABLE PythonPullBrush
{
    PythonPullBrush		"Python Pull Brush";
}
```

[Example on GitHub](https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples/tree/master/examples/plugins/py_tool_sculpt_pull_brush/res/strings_us/description/pythonpullbrush.str)
