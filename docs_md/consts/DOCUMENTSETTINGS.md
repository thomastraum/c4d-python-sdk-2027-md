<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/DOCUMENTSETTINGS.html -->

# DOCUMENTSETTINGS <a id="documentsettings"></a>

**DOCUMENTSETTINGS_GENERAL** General Settings.

|   |   |   |
|---|---|---|
| *DOCUMENT_TIME* | [`BaseTime`](../modules/c4d/BaseTime/index.md#c4d.BaseTime) | Current document time. |
| *DOCUMENT_FPS* | int | Frame rate (frames per second). |
| *DOCUMENT_MINTIME* | [`BaseTime`](../modules/c4d/BaseTime/index.md#c4d.BaseTime) | Start time. |
| *DOCUMENT_MAXTIME* | [`BaseTime`](../modules/c4d/BaseTime/index.md#c4d.BaseTime) | End time. |
| *DOCUMENT_LOOPMINTIME* | [`BaseTime`](../modules/c4d/BaseTime/index.md#c4d.BaseTime) | Start preview loop time. |
| *DOCUMENT_LOOPMAXTIME* | [`BaseTime`](../modules/c4d/BaseTime/index.md#c4d.BaseTime) | End preview loop time. |
| *DOCUMENT_LOD* | float | Level of detail (0-100%). |
| *DOCUMENT_RENDERLOD* | bool | Render LOD in editor. |
| *DOCUMENT_USEANIMATION* | bool | Use animation. |
| *DOCUMENT_USEEXPRESSIONS* | bool | Use expressions. |
| *DOCUMENT_USEGENERATORS* | bool | Use generators. |
| *DOCUMENT_USEDEFORMERS* | bool | Use deformers. |
| *DOCUMENT_MODE* | bool | Editor mode. |
|  | *Mcamera* | Camera mode. |
|  | *Mobject* | Object mode. |
|  | *Mtexture* | Texture mode. |
|  | *Mtextureaxis* | Texture axis mode. |
|  | *Mpoints* | Point edit mode. |
|  | *Medges* | Edge edit mode. |
|  | *Mpolygons* | Polygon edit mode. |
|  | *Manimation* | Animation mode. |
|  | *Mkinematic* | IK mode. |
|  | *Mmodel* | Model mode. |
|  | *Mpaint* | Paint mode. |
|  | *Muvpoints* | UV points mode. |
|  | *Muvpolygons* | UV polygons mode. |
|  | *Mpolyedgepoint* | Combined poly/edge/point mode. Must only be used in [`ViewportSelect`](../modules/c4d.utils/ViewportSelect/index.md#c4d.utils.ViewportSelect). |
|  | *Medgepoint* | Combined edge/point mode. Must only be used in [`ViewportSelect`](../modules/c4d.utils/ViewportSelect/index.md#c4d.utils.ViewportSelect). |
|  | *Mworkplane* | Workplane mode. |
|  | *Mdrag* | Drag mode. |
| *DOCUMENT_ACTION* | int | ID of the current tool. |
| *DOCUMENT_USERCHANGE* | bool | Private. |
| *DOCUMENT_PATH* | str | Document file path. |
| *DOCUMENT_NAME* | str | Document filename. |
| *DOCUMENT_STATEX* | bool | Lock/unlock X-axis. |
| *DOCUMENT_STATEY* | bool | Lock/unlock Y-axis. |
| *DOCUMENT_STATEZ* | bool | Lock/unlock Z-axis. |
| *DOCUMENT_STATEW* | bool | Use world/object coordinate system. |

**DOCUMENTSETTINGS_MODELING** Modeler settings.

|   |   |   |
|---|---|---|
| *MDATA_DISCONNECT_PRESERVEGROUPS* | bool | Preserve groups. |
| *MDATA_UNTRIANGULATE_ANGLE* | bool | Evaluate angle. |
| *MDATA_SUBDIVIDE_HYPER* | bool | Subdivide Hyper NURBS. |
| *MDATA_UNTRIANGULATE_ANGLE_RAD* | float | Angle radius. |
| *MDATA_SUBDIVIDE_ANGLE* | float | Subdivide maximum angle. |
| *MDATA_SUBDIVIDE_SUB* | int | Subdivisions (polygon). |
| *MDATA_SUBDIVIDE_SPLINESUB* | int | Subdivisions (spline). |
| *MDATA_OPTIMIZE_POINTS* | bool | Optimize points. |
| *MDATA_OPTIMIZE_UNUSEDPOINTS* | bool | Optimize unused points. |
| *MDATA_OPTIMIZE_POLYGONS* | bool | Optimize polygons. |
| *MDATA_OPTIMIZE_TOLERANCE* | float | Optimize tolerance. |
| *MDATA_REVERSENORMALS_USERNORMALS* | bool | Reverse user normals. |
| *MDATA_ALIGNNORMALS_USERNORMALS* | bool | Align user normals. |
| *MDATA_SPLINE_PROJECTMODE* | int | Project mode (see dialog). |
| *MDATA_SPLINE_FREEHANDTOLERANCE* | float | Freehand tolerance. |
| *MDATA_SPLINE_OUTLINE* | float | Spline outline distance. |
| *MDATA_SPLINE_OUTLINESEPARATE* | bool | Outline separate. Creates new object. |
| *MDATA_CROSSSECTION_ANGLE* | float | Maximum angle. |
| *MDATA_MIRROR_SYSTEM* | int | Coordinate system (see dialog). |
| *MDATA_MIRROR_PLANE* | int | Mirror plane (see dialog). |
| *MDATA_MIRROR_SNAPPOINTS* | bool | Snap to points. |
| *MDATA_MIRROR_ONPLANE* | bool | Mirror on plane. |
| *MDATA_MIRROR_DUPLICATE* | bool | Duplicate points. |
| *MDATA_MIRROR_SELECTIONS* | bool | Mirror selections |
| *MDATA_MIRROR_WELD* | bool | Mirror points. |
| *MDATA_MIRROR_TOLERANCE* | float | Mirror tolerance. |
| *MDATA_MIRROR_VALUE* | float | Mirror value. |
| *MDATA_CONVERTSELECTION_LEFT* | int | Left selection (see dialog). |
| *MDATA_CONVERTSELECTION_RIGHT* | int | Right selection (see dialog). |
| *MDATA_CONVERTSELECTION_TOLERANT* | bool | Tolerant conversion. |

> **See also:** [SNAP_SETTINGS](SNAP_SETTINGS.md)

**DOCUMENTSETTINGS_DOCUMENT** Document Settings.

|   |   |   |
|---|---|---|
| *DOCUMENT_INFO_DATECREATED* | long | Creation date. |
| *DOCUMENT_INFO_PRGCREATOR_NAME* | str | Name of the creation software. |
| *DOCUMENT_INFO_PRGCREATOR_ID* | int | ID of the creation software. |
|  | *MAXON_CREATOR_ID* | MAXON. |
| *DOCUMENT_INFO_PRGCREATOR_STRING* | str | Creation software string. |
| *DOCUMENT_INFO_PRGWRITER_NAME* | str | Software the document was saved last. |
| *DOCUMENT_INFO_PRGWRITER_ID* | int | ID of the software the document was saved last. |
|  | *MAXON_CREATOR_ID* | MAXON. |
| *DOCUMENT_INFO_PRGWRITER_STRING* | str | String of the software the document was saved last. |
| *DOCUMENT_INFO_AUTHOR* | str | Document author. |
| *DOCUMENT_INFO_COPYRIGHT* | str | Copyright info. |
| *DOCUMENT_INFO_README* | str | Info string. |
| *DOCUMENT_INFO_FILEFORMAT* | str | File format. |
| *DOCUMENT_INFO_FILEVERSION* | str | File version number. |
| *DOCUMENT_INFO_DATECREATED* | long | Date created. |
| *DOCUMENT_INFO_DATECREATED_STRING* | str | Date created formatted as string. |
| *DOCUMENT_INFO_DATESAVED* | long | Last save date. |
| *DOCUMENT_INFO_DATESAVED_STRING* | str | Last save date formatted as string. |
| *DOCUMENT_COLORPROFILE* | int | Input color profile: |
|  | *DOCUMENT_COLORPROFILE_SRGB* | sRGB. |
|  | *DOCUMENT_COLORPROFILE_LINEAR* | Linear. |
|  | *DOCUMENT_COLORPROFILE_DISABLED* | Disabled. |
| *DOCUMENT_LINEARWORKFLOW* | bool | Use linear workflow. |
| *DOCUMENT_COLORINFO* | str | Color profile information string. |
| *DOCUMENT_DEFAULTMATERIAL_COLOR* | [`Vector`](../modules/c4d/Vector/index.md#c4d.Vector) | Default object color. |
| *DOCUMENT_DEFAULTMATERIAL_TYPE* | int | Default object color preset: |
|  | *DOCUMENT_DEFAULTMATERIAL_TYPE_WHITE* | 80% Gray. |
|  | *DOCUMENT_DEFAULTMATERIAL_TYPE_BLUE* | Gray-Blue. |
|  | *DOCUMENT_DEFAULTMATERIAL_TYPE_USER* | Custom. |
| *DOCUMENT_CLIPPING_PRESET* | int | View clipping preset: |
|  | *DOCUMENT_CLIPPING_PRESET_TINY* | Tiny. |
|  | *DOCUMENT_CLIPPING_PRESET_SMALL* | Small. |
|  | *DOCUMENT_CLIPPING_PRESET_MEDIUM* | Medium. |
|  | *DOCUMENT_CLIPPING_PRESET_LARGE* | Large. |
|  | *DOCUMENT_CLIPPING_PRESET_HUGE* | Huge. |
|  | *DOCUMENT_CLIPPING_PRESET_CUSTOM* | Custom. |
| *DOCUMENT_CLIPPING_PRESET_NEAR* | float | Near view clipping. |
| *DOCUMENT_CLIPPING_PRESET_FAR* | float | Far view clipping. |
| *DOCUMENT_DOCUNIT* | [`UnitScaleData`](../modules/c4d/CustomDataType/UnitScaleData/index.md#c4d.UnitScaleData) | Project scale. |
| *DOCUMENT_SCALEDOCUMENT* | button | Scale Project button. |
| *DOCUMENT_PREVIEW_IMAGE* | [`BitmapButtonStruct`](../modules/c4d/CustomDataType/BitmapButtonStruct/index.md#c4d.BitmapButtonStruct) | Document preview bitmap. |
| *DOCUMENT_PREVIEW_COMMAND* | int | Preview command. |
|  | *DOCUMENT_PREVIEW_COMMAND_AUTO* | Auto Save Editor. |
|  | *DOCUMENT_PREVIEW_COMMAND_PASTE* | Paste from Clipboard. |
|  | *DOCUMENT_PREVIEW_COMMAND_FROMEDITOR* | Copy from Editor. |
|  | *DOCUMENT_PREVIEW_COMMAND_LOAD* | Load from File. |
| *DOCUMENT_PRESET_COMMAND_LOAD* | button | Load preset. |
| *DOCUMENT_PRESET_COMMAND_SAVE* | button | Save preset. |

**DOCUMENTSETTINGS_ANIMATIONSYSTEM** Timeline settings. Private.

**DOCUMENTSETTINGS_TOOLS** Tools settings.
