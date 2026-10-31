<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/MCOMMAND.html -->

# MCOMMAND <a id="mcommand"></a>

- There are several groups of IDs to use. First there are the internal modeling commands: (Indented IDs **MDATA_*** are for the passed container *bc*.)

|   |   |   |   |   |
|---|---|---|---|---|
| *MCOMMAND_SPLINE_HARDINTERPOLATION* | Hard interpolation. |  |  |  |
| *MCOMMAND_SPLINE_SOFTINTERPOLATION* | Soft interpolation. |  |  |  |
| *MCOMMAND_SPLINE_REORDER* | Set first point. |  |  |  |
| *MCOMMAND_SPLINE_REVERSE* | Reverse sequence. |  |  |  |
| *MCOMMAND_SPLINE_MOVEDOWN* | Move down sequence. |  |  |  |
| *MCOMMAND_SPLINE_MOVEUP* | Move up sequence. |  |  |  |
| *MCOMMAND_SPLINE_JOINSEGMENT* | Join segment. |  |  |  |
| *MCOMMAND_SPLINE_BREAKSEGMENT* | Break segment. |  |  |  |
| *MCOMMAND_SPLINE_EQUALLENGTH* | Equal tangent length. |  |  |  |
| *MCOMMAND_SPLINE_EQUALDIRECTION* | Equal tangent direction. |  |  |  |
| *MCOMMAND_SPLINE_LINEUP* | Line up. |  |  |  |
| *MCOMMAND_SPLINE_CREATEOUTLINE* | Create outline: |  |  |  |
|  | *MDATA_SPLINE_OUTLINE* | float | Distance. |  |
|  | *MDATA_SPLINE_PROJECTMODE* | int | Projection. (See dialog.) |  |
|  | *MDATA_SPLINE_ADDPOINTSEGMENT* | int | Segment. |  |
|  | *MDATA_SPLINE_ADDPOINTPOSITION* | float | Position. |  |
|  | *MDATA_SPLINE_ADDPOINTSELECT* | bool | Select added point. |  |
|  | *MDATA_SPLINE_OUTLINESEPARATE* | bool | Create new object. |  |
| *MCOMMAND_SPLINE_PROJECT* | Project: |  |  |  |
|  | *MDATA_SPLINE_PROJECTMODE* | int | Projection. (See dialog.) |  |
| *MCOMMAND_SPLINE_ADDPOINT* | Add point: |  |  |  |
|  | *MDATA_SPLINE_ADDPOINTSEGMENT* | int | Segment. |  |
|  | *MDATA_SPLINE_ADDPOINTPOSITION* | float | Position. |  |
| *MCOMMAND_SELECTALL* | Select all. |  |  |  |
| *MCOMMAND_DESELECTALL* | Deselect all. |  |  |  |
| *MCOMMAND_SELECTINVERSE* | Invert selection. |  |  |  |
| *MCOMMAND_SELECTCONNECTED* | Select connected. |  |  |  |
| *MCOMMAND_SELECTGROW* | Grow selection. |  |  |  |
| *MCOMMAND_SELECTSHRINK* | Shrink selection. |  |  |  |
| *MCOMMAND_SELECTPOINTTOPOLY* | Polygon selection from points. |  |  |  |
| *MCOMMAND_SELECTPOLYTOPOINT* | Point selection from polygons. |  |  |  |
| *MCOMMAND_SELECTADJACENT* | Select adjacent. |  |  |  |
| *MCOMMAND_GENERATESELECTION* | Set selection. |  |  |  |
| *MCOMMAND_HIDESELECTED* | Hide selected. |  |  |  |
| *MCOMMAND_HIDEUNSELECTED* | Hide unselected. |  |  |  |
| *MCOMMAND_HIDEINVERT* | Invert visibility. |  |  |  |
| *MCOMMAND_UNHIDE* | Unhide all. |  |  |  |
| *MCOMMAND_REVERSENORMALS* | Reverse normals. |  |  |  |
| *MCOMMAND_ALIGNNORMALS* | Align normals. |  |  |  |
| *MCOMMAND_SPLIT* | Split. |  |  |  |
|  | *MDATA_SPLIT_KEEPPOLYGONS* | bool | Keep polygon in source object |  |
| *MCOMMAND_TRIANGULATE* | Triangulate. |  |  |  |
| *MCOMMAND_UNTRIANGULATE* | Untriangulate: |  |  |  |
|  | *MDATA_UNTRIANGULATE_NGONS* | bool | Create N-gons. |  |
|  | *MDATA_UNTRIANGULATE_ANGLE_RAD* | float | Untriangulate angle radius. |  |
| *MCOMMAND_DELETE* | Delete. |  |  |  |
|  | *MDATA_DELETECOMPONENTS_ALTERNATE_BEHAVIOR* |  | Invert disconnected point preserve/delete preference behavior. |  |
| *MCOMMAND_OPTIMIZE* | Optimize: |  |  |  |
|  | *MDATA_OPTIMIZE_TOLERANCE* | float | Tolerance. |  |
|  | *MDATA_OPTIMIZE_POINTS* | bool | Points. |  |
|  | *MDATA_OPTIMIZE_POLYGONS* | bool | Polygons. |  |
|  | *MDATA_OPTIMIZE_UNUSEDPOINTS* | bool | Unused points. |  |
| *MCOMMAND_DISCONNECT* | Disconnect: |  |  |  |
|  | *MDATA_DISCONNECT_PRESERVEGROUPS* | bool | Preserve groups. |  |
| *MCOMMAND_MAKEEDITABLE* | Make editable. (Returns object.) |  |  |  |
| *MCOMMAND_MIRROR* | Mirror: |  |  |  |
|  | *MDATA_MIRROR_SNAPPOINTS* | bool | Snap to points. |  |
|  | *MDATA_MIRROR_DUPLICATE* | bool | Duplicate points. |  |
|  | *MDATA_MIRROR_WELD* | bool | Weld points. |  |
|  | *MDATA_MIRROR_TOLERANCE* | float | Weld tolerance. |  |
|  | *MDATA_MIRROR_SYSTEM* | int | Coordinate system. (See dialog.) |  |
|  | *MDATA_MIRROR_PLANE* | int | Mirror plane. (See dialog.) |  |
|  | *MDATA_MIRROR_VALUE* | float | Value. |  |
|  | *MDATA_MIRROR_POINT* | [`Vector`](../modules/c4d/Vector/index.md#c4d.Vector) | Mirror point. |  |
|  | *MDATA_MIRROR_VECTOR* | [`Vector`](../modules/c4d/Vector/index.md#c4d.Vector) | Mirror vector. |  |
|  | *MDATA_MIRROR_SELECTIONS* | bool | Duplicate tag selections. |  |
|  | *MDATA_MIRROR_ONPLANE* | bool | Symmetric. |  |
| *MCOMMAND_SUBDIVIDE* | Subdivide: |  |  |  |
|  | *MDATA_SUBDIVIDE_HYPER* | bool | Subdivision surface subdivide. |  |
|  | *MDATA_SUBDIVIDE_ANGLE* | float | Maximum angle. |  |
|  | *MDATA_SUBDIVIDE_SPLINESUB* | int | Subdivisions. (Spline.) |  |
|  | *MDATA_SUBDIVIDE_SUB* | int | Subdivisions. (Polygon.) |  |
| *MCOMMAND_EXPLODESEGMENTS* | Explode segments. |  |  |  |
| *MCOMMAND_KNIFE* | Knife. See *toolknife.h*. |  |  |  |
| *MCOMMAND_CURRENTSTATETOOBJECT* | Current State to Object |  |  |  |
|  | *MDATA_CURRENTSTATETOOBJECT_INHERITANCE* | bool | Use inheritance. |  |
|  | *MDATA_CURRENTSTATETOOBJECT_KEEPANIMATION* | bool | Keep animation. |  |
|  | *MDATA_CURRENTSTATETOOBJECT_NOGENERATE* | bool | No generate. |  |
|  | *MDATA_CURRENTSTATETOOBJECT_LOD* | Float | The LOD level to generate with. |  |
|  | *MDATA_CURRENTSTATETOOBJECT_BUILDFLAGS* | int | Override for the buildflags: |  |
|  |  |  | *BUILDFLAGS_NONE* | None. |
|  |  |  | *BUILDFLAGS_INTERNALRENDERER* | Rendering in the editor. |
|  |  |  | *BUILDFLAGS_EXTERNALRENDERER* | Rendering externally. |
|  |  |  | *BUILDFLAGS_ISOPARM* | Generate isoparm objects. |
|  |  |  | *BUILDFLAGS_EXPORTONLY* | Exporting (e.g. Alembic). |
| *MCOMMAND_JOIN* | Joins the objects that are parented to the passed null object. Passing multiple objects into SMC will *not* join them. |  |  |  |
|  | *MDATA_JOIN_MERGE_SELTAGS* | bool | Merge selection tags. |  |
| *MCOMMAND_CONVERTSELECTION* | Convert Selection: |  |  |  |
|  | *MDATA_CONVERTSELECTION_LEFT* | int | Left selection. (See dialog.) |  |
|  | *MDATA_CONVERTSELECTION_RIGHT* | int | Right selection. (See dialog.) |  |
|  | *MDATA_CONVERTSELECTION_TOLERANT* | bool | Tolerant conversion. |  |
| *MCOMMAND_EDGE_TO_SPLINE* | Edge to spline |  |  |  |
| *MCOMMAND_BREAKPHONG* | Break phong. |  |  |  |
| *MCOMMAND_UNBREAKPHONG* | Unbreak phong. |  |  |  |
| *MCOMMAND_PHONGTOSELECTION* | Phong to selection. |  |  |  |
| *MCOMMAND_MELT* | Melt. |  |  |  |
| *MCOMMAND_RESETSYSTEM* | Reset System: |  |  |  |
|  | *MDATA_RESETSYSTEM_COMPENSATE* | bool | Offsets. |  |
|  | *MDATA_RESETSYSTEM_RECURSIVE* | bool | Reset sub-objects. |  |
| *MCOMMAND_MIRRORSELECTION* | Mirror Selection. |  |  |  |
|  | *MDATA_MIRRORSELECTION_TOLERANCE* | float | Tolerance. |  |
|  | *MDATA_MIRRORSELECTION_MODE* | int | Selection mode (New, Add, Sub). |  |
|  | *MDATA_MIRRORSELECTION_SPACE* | int | Space (see dialog). |  |
|  | *MDATA_MIRRORSELECTION_PLANE* | int | Mirror plane (see dialog). |  |
| *MCOMMAND_UVUNWRAP* | Uv Unwrap. |  |  |  |
|  | *MDATA_UVUNWRAP_POLYGON* | bool | Restrict to polygon selection. |  |
|  | *MDATA_UVUNWRAP_PIN* | bool | Pin from point selection. |  |
|  | *MDATA_UVUNWRAP_REALIGN* | bool | Auto realign. |  |
| *MCOMMAND_UVWELDRELAX* | Uv Weld Relax. |  |  |  |
|  | *MDATA_UVWELDRELAX_PIN* | bool | Pin from point selection. |  |
|  | *MDATA_UVWELDRELAX_POLYGON* | bool | Restrict to polygon selection. |  |
|  | *MDATA_UVWELDRELAX_REALIGN* | bool | Auto realign. |  |

- Then there are the modeling library tool IDs, where you have to look up the parameters in the resource files:

|   |   |
|---|---|
| *ID_MODELING_EDGECUT_TOOL* | Edge cut tool. See *tooledgecut.h*. |
| *ID_MODELING_FILL_SELECTION_TOOL* | Fill selection tool. See *toolloopselection.h*. |
| *ID_MODELING_OUTLINE_SELECTION_TOOL* | Private. |
| *ID_MODELING_LOOP_TOOL* | Loop selection tool. See *toolloopselection.h*. |
| *ID_MODELING_RING_TOOL* | Ring selection tool. See *toolloopselection.h*. |
| *ID_MODELING_EXTRUDE_TOOL* | Extrude tool. See *toolextrude.h*. |
| *ID_MODELING_MATRIX_EXTRUDE_TOOL* | Matrix extrude tool. See *toolmatrixextrude.h*. |
| *ID_MODELING_NORMALMOVE_TOOL* | Normal move tool. See *toolnormalmove.h*. |
| *ID_MODELING_NORMALSCALE_TOOL* | Normal scale tool. See *toolnormalscale.h*. |
| *ID_MODELING_NORMALROTATE_TOOL* | Normal rotate tool. See *toolnormalrotate.h*. |
| *ID_MODELING_SMOOTH_SHIFT_TOOL* | Smooth shift tool. See *toolsmoothshift.h*. |
| *ID_MODELING_EXTRUDE_INNER_TOOL* | Extrude inner tool. See *toolextrudeinner.h*. |
| *ID_XBEVELTOOL* | *New in version R19:* <br> Bevel Tool (After R15). See *xbeveltool.h*. |
| *ID_MODELING_BEVEL_TOOL* | **Old Bevel tool(Before R15). See *toolbevel.h*.**<br>> **Note:** This tool cannot be used with [`SendModelingCommand()`](../modules/c4d.utils/index.md#c4d.utils.SendModelingCommand). Instead use [`CallCommand()`](../modules/c4d/index.md#c4d.CallCommand). |
| *ID_MODELING_POLYGON_CREATE_TOOL* | **Create polygon tool. See *toolcreatepolygon.h*.**<br>> **Note:** This tool cannot be used with [`SendModelingCommand()`](../modules/c4d.utils/index.md#c4d.utils.SendModelingCommand). Instead use [`CallCommand()`](../modules/c4d/index.md#c4d.CallCommand). |
| *ID_MODELING_POINT_ADD_TOOL* | Add point tool. See *tooladdpoint.h*. |
| *ID_MODELING_BRIDGE_TOOL* | Bridge tool. See *toolbridge.h*. |
| *ID_MODELING_WELD_TOOL* | Weld tool. See *toolpointweld.h*. |
| *ID_MODELING_CLOSEHOLE_TOOL* | Close polygon hole tool. See *toolclosehold.h*. |
| *ID_MODELING_STITCHANDSEW_TOOL* | Stich and sew tool. See *toolstitchandsew.h*. |
| *ID_MODELING_SLIDE_TOOL* | Slide tool. See *toolslide.h*. |
| *ID_MODELING_IRON_TOOL* | Iron tool. See *tooliron.h*. |
| *ID_MODELING_SETVALUE_TOOL* | Set value tool. See *toolsetvalue.h*. |
| *ID_MODELING_DUPLICATE_TOOL* | Duplicate tool. See *toolduplicate.h*. |
| *ID_MODELING_ARRANGE_TOOL* | Arrange tool. See *toolarrange.h*. |
| *ID_MODELING_TRANSFER_TOOL* | Transfer tool. See *tooltransfer.h*. |
| *ID_MODELING_RANDOMIZE_TOOL* | Randomize tool. See *toolrandomize.h*. |
| *ID_MODELING_CENTER_TOOL* | Center tool. See *toolcenter.h*. |
| *ID_MODELING_KNIFE_LINE* | *New in version R18:* <br> Knife line tool. See *toolknifeline.h*.<br>> > **Note:** This tool cannot be used with [`SendModelingCommand()`](../modules/c4d.utils/index.md#c4d.utils.SendModelingCommand). Instead use [`CallCommand()`](../modules/c4d/index.md#c4d.CallCommand). |
| *ID_MODELING_KNIFE_PLANE* | *New in version R18:* <br> Knife plane tool. See *toolknifeplane.h*. |
| *ID_MODELING_KNIFE_PATH* | *New in version R18:* <br> Knife path/loop tool. See toolknifepath.h. |
| *ID_MODELING_LIVESELECTION* | **Live selection tool. See *toolliveselection.h*.**<br>> **Note:** This tool cannot be used with [`SendModelingCommand()`](../modules/c4d.utils/index.md#c4d.utils.SendModelingCommand). Instead use [`CallCommand()`](../modules/c4d/index.md#c4d.CallCommand). |
| *ID_MODELING_RECTSELECTION* | **Rectangle selection tool. See *toolrectselection.h*.**<br>> **Note:** This tool cannot be used with [`SendModelingCommand()`](../modules/c4d.utils/index.md#c4d.utils.SendModelingCommand). Instead use [`CallCommand()`](../modules/c4d/index.md#c4d.CallCommand). |
| *ID_MODELING_FREESELECTION* | **Free selection tool. See *toolfreeselection.h*.**<br>> **Note:** This tool cannot be used with [`SendModelingCommand()`](../modules/c4d.utils/index.md#c4d.utils.SendModelingCommand). Instead use [`CallCommand()`](../modules/c4d/index.md#c4d.CallCommand). |
| *ID_MODELING_POLYSELECTION* | **Polygon selection tool. See *toolpolyselection.h*.**<br>> **Note:** This tool cannot be used with [`SendModelingCommand()`](../modules/c4d.utils/index.md#c4d.utils.SendModelingCommand). Instead use [`CallCommand()`](../modules/c4d/index.md#c4d.CallCommand). |
| *ID_MODELING_MAGNET_TOOL* | Magnet tool. See *toolmagnet.h*. |
| *ID_MODELING_BRUSH_TOOL* | **Brush tool. See *toolbrush.h*.**<br>> **Note:** This tool cannot be used with [`SendModelingCommand()`](../modules/c4d.utils/index.md#c4d.utils.SendModelingCommand). Instead use [`CallCommand()`](../modules/c4d/index.md#c4d.CallCommand). |
| *ID_MODELING_MODIFY_TOOL* | **Modify tool. See *toolmodify.h*.**<br>> **Note:** This tool cannot be used with [`SendModelingCommand()`](../modules/c4d.utils/index.md#c4d.utils.SendModelingCommand). Instead use [`CallCommand()`](../modules/c4d/index.md#c4d.CallCommand). |
| *ID_MEASURE_TOOL* | **Measure tool. See *toolmeasure.h*.**<br>> **Note:** This tool cannot be used with [`SendModelingCommand()`](../modules/c4d.utils/index.md#c4d.utils.SendModelingCommand). Instead use [`CallCommand()`](../modules/c4d/index.md#c4d.CallCommand). |
| *ID_MODELING_SPLINE_ROUND_TOOL* | Spline round tool. See *toolsplineround.h*. |
| *ID_MODELING_CLONE_TOOL* | Clone tool. See *toolclone.h*. |
| *ID_MODELING_SPLINE_CHAMFER_TOOL* | Spline chamfer tool. See *toolsplinechamfer.h*. |
| *ID_MODELING_ARRAY_TOOL* | Array tool. See *toolarray.h*. |
| *ID_MODELING_SPLINE_PROJECT_TOOL* | Spline project tool. See *toolsplineproject.h*. |
| *ID_MODELING_PATH* | The modeling tool Path. |

- Finally there are the modeling library menu commands. These have no parameters:

|   |   |
|---|---|
| *ID_MODELING_MELT_COMMAND* | Melt. |
| *ID_MODELING_EDGE_SPLINE_COMMAND* | Edge to spline. |
| *ID_MODELING_COLLAPSE_COMMAND* | Collapse. |
| *ID_NGON_RETRI_MENU* | Retriangulate N-gons. |
| *ID_NGON_REMOVE_MENU* | Remove N-gons. |
| *ID_NGON_FORCERETRI_MENU* | Force N-gon triangulation. |
| *ID_OBJECTHANDLES_ONOFF_MENU* | Object handles toggle. |
| *ID_SDS_INC_MENU* | Increment SDS. |
| *ID_SDS_DEC_MENU* | Decrement SDS. |
| *ID_SDS_ONFFF_MENU* | Toggle SDS. |
| *ID_MODELING_OM_SELECT_INVERT* | Invert object manager selection. |
| *ID_MODELING_OM_SELECT_HIDE* | Hide selected objects. |
| *ID_MODELING_OM_SELECT_SHOW* | Show selected objects. |
| *ID_MODELING_SHORTCUT_SELECTVISIBLE* | Toggle select visible. |
| *ID_CAMERA_SET_PIVOT* | Set the camera pivot. |
| *ID_CAMERA_LOCK_PIVOT* | Locks/unlocks the camera’s Point of Interest (POI) to the last used POI location. |
| *ID_LASTTOOL_START* | The first of the last used tools. The next last used tools can be accessed with *ID_LASTTOOL_START* + (1…7) |
| *ID_LASTTOOL_END* | The last of the last used tools. |
