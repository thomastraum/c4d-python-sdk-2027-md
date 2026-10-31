<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/types/tags.html -->

# Tag Types <a id="tag-types"></a>

|   |   |
|---|---|
| *Talembicmorphtag* | *New in version R19:* Alembic morph. |
| *Taligntopath* | Align to path. |
| *Taligntospline* | Align to spline. |
| *Tannotation* | Annotation. |
| *Tarchigrass* | Architectural grass. |
| *Tbakeparticle* | Bake particle. |
| *Tbaketexture* | Bake texture. |
| *Tbase* | Base tag - [`BaseTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/index.md#c4d.BaseTag). |
| *Tcompositing* | Compositing/render. |
| *Tcorner* | Corner. (Phong break.) |
| *Tcrane* | Camera crane. |
| *Tdisplay* | Display. |
| *Tedgeselection* | Edge selection - [`SelectionTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/SelectionTag/index.md#c4d.SelectionTag). The edges are encodes like this: *(4*poly)+edge*, where *edge* goes from *0-3*. |
| *Texpresso* | XPresso. |
| *Tgrouppriority* | *New in version R18:* Group priority. |
| *Tinteraction* | Interaction. |
| *Tline* | Line. |
| *Tlookatcamera* | Look at camera. |
| *Tmetaball* | Metaball. |
| *Tmgselection* | MoGraph selection. |
| *Tmgweight* | *New in version R18.011:* MoGraph weights. |
| *Tmorphcam* | Morph camera. |
| *Tmotionblur* | Motion blur. |
| *Tmotioncam* | Motion camera. |
| *Tnormal* | Normal - [`NormalTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/NormalTag/index.md#c4d.NormalTag). Contains 12 integer values per polygon, enumerated like the following: *ax,ay,az,bx,by,bz,cx,cy,cz,dx,dy,dz*. The value is the float value of the normal vector component multiplied by *32000.0*. |
| *Tparticle* | Particle. |
| *Tphong* | Phong. |
| *Tplugin* | Plugin tag. Pass the plugin ID. |
| *Tpoint* | Point - [`PointTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/PointTag/index.md#c4d.PointTag). |
| *Tpointselection* | Point selection - [`SelectionTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/SelectionTag/index.md#c4d.SelectionTag). |
| *Tpolygon* | Polygon - [`PolygonTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/PolygonTag/index.md#c4d.PolygonTag). |
| *Tpolygonselection* | Polygon selection - [`SelectionTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/SelectionTag/index.md#c4d.SelectionTag). |
| *Tposemorph* | Pose morph. |
| *Tprotection* | Protection. |
| *Tpython* | Python expression. |
| *Trestriction* | Restriction. |
| *Tsavetemp* | Internal. |
| *Tsculpt* | Sculpt. |
| *Tsds* | SDS. |
| *Tsdsdata* | SDS data. |
| *Tsegment* | Segment - [`SegmentTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/SegmentTag/index.md#c4d.SegmentTag). |
| *Tsoftselection* | Soft selection. |
| *Tsplinenormal* | Spline normals. |
| *Tsticktexture* | Stick texture. |
| *Tstop* | Stop. |
| *Tsunexpression* | Sun expression. |
| *Ttangent* | Tangent - [`TangentTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/TangentTag/index.md#c4d.TangentTag). |
| *Ttargetexpression* | Target expression. |
| *Ttexture* | Texture tag - [`TextureTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/TextureTag/index.md#c4d.TextureTag). |
| *Tuvw* | UVW - [`UVWTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/UVWTag/index.md#c4d.UVWTag). |
| *Tvariable* | Variable tag - [`VariableTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/index.md#c4d.VariableTag). |
| *Tvertexcolor* | *New in version R18:* Vertex color - [`VariableTag`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/VariableTag/VertexColorTag/index.md#c4d.VertexColorTag). |
| *Tvertexmap* | Vertex map. |
| *Tvibrate* | Vibration. |
| *Tweights* | Weights tag. |
| *Tmeshattribute* | *New in version R20:* CustomDataTag. |
| *Tuserdata* | *New in version R21:* User Data Tag. |
| *Tcacheproxytag* | *New in version R21:* Cache proxy tag. Private for generators. |
| *Tcacheproxytagpolyselection* | *New in version R21:* Cache proxy tag for polygon selection. Private for generators. |
| *Tcacheproxytagpointselection* | *New in version R21:* Cache proxy tag for point selection. Private for generators. |
| *Tcacheproxytagedgeselection* | *New in version R21:* Cache proxy tag for edge selection. Private for generators. |
| *Tcharmotiontransfer* | *New in version R24:* Character Motion Transfer Tag. |
| *Tchardefinition* | *New in version R24:* Character Definition Tag. |
| *Tcameracalibrator* | *New in version 2023.0.0:* Tag plugin ‘Camera Calibrator’. |
| *Tcameraorrientation* | *New in version 2023.0.0:* Tag plugin ‘Camera Orientation Constraint’. |
| *Tcacomponent* | *New in version 2023.0.0:* Tag plugin ‘Character Component’. |
| *Tcloth* | *New in version 2023.0.0:* Tag plugin ‘Cloth’. |
| *Tclothbelt* | *New in version 2023.0.0:* Tag plugin ‘Cloth Belt’. |
| *Tcollider* | *New in version 2023.0.0:* Tag plugin ‘Collider’. |
| *Tconnector* | *New in version 2023.0.0:* Tag plugin ‘Connector’. |
| *Tcaconstraint* | *New in version 2023.0.0:* Tag plugin ‘Constraint’. |
| *Tdoodleimage* | *New in version 2023.0.0:* Tag plugin ‘Doodle Image’. |
| *Tdriver* | *New in version 2023.0.0:* Tag plugin ‘Driver’. |
| *Tdynamicsbody* | *New in version 2023.0.0:* Tag plugin ‘Dynamics Body’. |
| *Tcaik* | *New in version 2023.0.0:* Tag plugin ‘IK’. |
| *Tcaikspline* | *New in version 2023.0.0:* Tag plugin ‘IK-Spline’. |
| *Tmaskconstraint* | *New in version 2023.0.0:* Tag plugin ‘Mask Constraint’. |
| *Tmgcolor* | *New in version 2023.0.0:* Tag plugin ‘Motion Graphics Color Tag’. |
| *Tmgdependence* | *New in version 2023.0.0:* Tag plugin ‘Motion Graphics Dependance Tag’. |
| *Tmgtracer* | *New in version 2023.0.0:* Tag plugin ‘Motion Graphics Tracer Tag’. |
| *Tmoveseye* | *New in version 2023.0.0:* Tag plugin ‘Moves Eye Tag’. |
| *Tmovesposemorph* | *New in version 2023.0.0:* Tag plugin ‘Moves Pose Morph Helper’. |
| *Tplanarconstraint* | *New in version 2023.0.0:* Tag plugin ‘Planar Constraint’. |
| *Tcapointcache* | *New in version 2023.0.0:* Tag plugin ‘Point Cache’. |
| *Tpositionconstraint* | *New in version 2023.0.0:* Tag plugin ‘Position Constraint’. |
| *Trscamera* | *New in version 2023.0.0:* Tag plugin ‘Redshift Camera’. |
| *Trsobject* | *New in version 2023.0.0:* Tag plugin ‘Redshift Object’. |
| *Trender* | *New in version 2023.0.0:* Tag plugin ‘Render’. |
| *Tretarget* | *New in version 2023.0.0:* Tag plugin ‘Retarget’. |
| *Trope* | *New in version 2023.0.0:* Tag plugin ‘Rope’. |
| *Tropebelt* | *New in version 2023.0.0:* Tag plugin ‘Rope Belt’. |
| *Tscenenodes* | *New in version 2023.0.0:* Tag plugin ‘Scene Nodes Tag’. |
| *Tsketchrender* | *New in version 2023.0.0:* Tag plugin ‘Sketch Render’. |
| *Tsketchstyle* | *New in version 2023.0.0:* Tag plugin ‘Sketch Style’. |
| *Tcatension* | *New in version 2023.0.0:* Tag plugin ‘Tension’. |
| *Ttodo* | *New in version 2023.0.0:* Tag plugin ‘To Do’. |
| *Tvectorconstraint* | *New in version 2023.0.0:* Tag plugin ‘Vector Constraint’. |
| *Tcavisualselector* | *New in version 2023.0.0:* Tag plugin ‘Visual Selector’. |
| *Tmotionsystem* | *New in version 2023.0.0:* Tag plugin ‘Motion System’. |
| *Ttrackmodifier* | *New in version 2024.4.0:* Tag plugin ‘Track Modifier’. |
