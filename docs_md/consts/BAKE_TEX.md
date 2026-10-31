<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/BAKE_TEX.html -->

# BAKE_TEX <a id="bake-tex"></a>

|   |   |   |
|---|---|---|
| *BAKE_TEX_USE_CAMERA_VECTOR* | bool | Use camera vector. |
| *BAKE_TEX_USE_POLYSELECTION* | bool | Use polygon selection. |
| *BAKE_TEX_AMBIENT_OCCLUSION* | bool | Bake ambient occlusion. |
| *BAKE_TEX_NORMAL* | bool | Bake normal channel. |
| *BAKE_TEX_SURFACECOLOR* | bool | Bake surface color. |
| *BAKE_TEX_COLOR* | bool | Bake color. |
| *BAKE_TEX_DIFFUSION* | bool | Bake diffusion channel. |
| *BAKE_TEX_LUMINANCE* | bool | Bake luminance. |
| *BAKE_TEX_ALPHA* | bool | Bake alpha channel. |
| *BAKE_TEX_ILLUMINATION* | bool | Bake illumination. |
| *BAKE_TEX_SHADOWS* | bool | Bake shadows. |
| *BAKE_TEX_BUMP* | bool | Bake bump. |
| *BAKE_TEX_TRANSPARENCY* | bool | Bake transparency. |
| *BAKE_TEX_UVMAP* | bool | Bake UV map. |
| *BAKE_TEX_REFLECTION* | bool | Bake reflection. |
| *BAKE_TEX_DISPLACEMENT* | bool | Bake displacement. |
| *BAKE_TEX_WIDTH* | int | Width. |
| *BAKE_TEX_HEIGHT* | int | Height. |
| *BAKE_TEX_PIXELBORDER* | int | Pixel border. |
| *BAKE_TEX_FILL_COLOR* | [`Vector`](../modules/c4d/Vector/index.md#c4d.Vector) | Fill color. |
| *BAKE_TEX_UV_LEFT* | float | Left UV coordinate. |
| *BAKE_TEX_UV_RIGHT* | float | Right UV coordinate. |
| *BAKE_TEX_UV_TOP* | float | Top UV coordinate. |
| *BAKE_TEX_UV_BOTTOM* | float | Bottom UV coordinate. |
| *BAKE_TEX_SUPERSAMPLING* | int | Supersampling. |
| *BAKE_TEX_USE_BUMP* | bool | Use bump. |
| *BAKE_TEX_NO_GI* | bool | No GI. |
| *BAKE_TEX_CONTINUE_UV* | bool | Continue UV. |
| *BAKE_TEX_USE_PHONG_TAG* | bool | The pixel will be clamped to the current polygon if set to **True** and if the angle between polygons is bigger than their phong angle. Only needed if *BAKE_TEX_CONTINUE_UV* is set to **True**. |
| *BAKE_TEX_COLORPROFILE* | [`ColorProfile`](../modules/c4d.bitmaps/ColorProfile/index.md#c4d.bitmaps.ColorProfile) | Color profile of the baked texture. |
| *BAKE_TEX_SHOW_STATUS* | bool | Show status. |
| *BAKE_TEX_PROGRESS_BITMAP* | bool | Show the bitmap in a preview during baking. |
| *BAKE_TEX_GENERATE_UNDO* | bool | Generate undo for UVW tags and Vertex tags created by the baker. |
| *BAKE_TEX_PREVIEW* | bool | Bake texture preview. |
| *BAKE_TEX_COLOR_ILLUM* | bool | Illumination in color. |
| *BAKE_TEX_COLOR_SHADOWS* | bool | Shadows in color. |
| *BAKE_TEX_COLOR_LUMINANCE* | bool | Luminance in color. |
| *BAKE_TEX_COLOR_DIFFUSION* | bool | Diffusion in color. |
| *BAKE_TEX_LUMINANCE_DIFFUSION* | bool | Diffusion in luminance. |
| *BAKE_TEX_ILLUMINATION_SHADOWS* | bool | Shadows in luminance. |
| *BAKE_TEX_NORMAL_METHOD* | int | Normal method: |
| *BAKE_TEX_NORMAL_METHOD_OBJECT* |  | Object. |
| *BAKE_TEX_NORMAL_METHOD_TANGENT* |  | Tangent. |
| *BAKE_TEX_NORMAL_METHOD_WORLD* |  | World. |
| *BAKE_TEX_NORMAL_FLIP_X* | bool | Flip X. |
| *BAKE_TEX_NORMAL_FLIP_Y* | bool | Flip Y. |
| *BAKE_TEX_NORMAL_FLIP_Z* | bool | Flip Z. |
| *BAKE_TEX_NORMAL_SWAP_YZ* | bool | Swap Y/Z. |
| *BAKE_TEX_NORMAL_SOURCE* | link | Normal source. |
| *BAKE_TEX_NORMAL_USE_RAYCAST* | bool | *New in version R18:* Whether the normal map will be generated using ray casting. True when baking the normal map only. |
| *BAKE_TEX_SURFACE_ILLUMINATION* | bool | Surface illumination. |
| *BAKE_TEX_AO_VERTEX_MAP* | bool | Ambient occlusion in vertex map. |
| *BAKE_TEX_AO_SELFINTERSECTION* | bool | Ambient occlusion self-intersection. |
| *BAKE_TEX_AO_VERTEXMAPS* | [`BaseContainer`](../modules/c4d/BaseContainer/index.md#c4d.BaseContainer) | A container that stores all new generated vertex maps. |
| *BAKE_TEX_DISPLACEMENT_SOURCE* | link | The high-res source object. |
| *BAKE_TEX_DISPLACEMENT_HEIGHT* | float | A float that will receive the displacement height. |
| *BAKE_TEX_DISPLACEMENT_METHOD* | int | Displacement method: |
| *BAKE_TEX_DISPLACEMENT_METHOD_OBJECT* |  | Object. |
| *BAKE_TEX_DISPLACEMENT_METHOD_WORLD* |  | World. |
| *BAKE_TEX_DISPLACEMENT_METHOD_TANGENT* |  | Tangent. |
| *BAKE_TEX_DISPLACEMENT_METHOD_INTENSITY* |  | Intensity. |
| *BAKE_TEX_DISPLACEMENT_METHOD_CENTEREDINTENSITY* |  | Centered intensity. |
| *BAKE_TEX_DISPLACEMENT_METHOD_REDGREEN* |  | Red <-> Green. |
| *BAKE_TEX_DISPLACEMENT_SUBPOLY* | bool | Displacement subpoly. |
| *BAKE_TEX_DISPLACEMENT_SUBPOLY_SUBDIVISION* | int | Displacement subpoly subdivision. |
| *BAKE_TEX_DISPLACEMENT_SUBPOLY_ROUND* | bool | Displacement subpoly round. |
| *BAKE_TEX_DISPLACEMENT_SUBPOLY_ROUNDCONTOUR* | bool | Displacement subpoly round contour. |
| *BAKE_TEX_DISPLACEMENT_SUBPOLY_HQREMAPPING* | bool | Displacement subpoly HQ remapping. |
| *BAKE_TEX_DISPLACEMENT_SUBPOLY_MAPRESULT* | bool | Displacement subpoly map result. |
| *BAKE_TEX_DISPLACEMENT_SUBPOLY_KEEPEDGES* | bool | Displacement subpoly keep edges. |
| *BAKE_TEX_DISPLACEMENT_SUBPOLY_DISTRIBUTION* | bool | Displacement subpoly distribution. |
| *BAKE_TEX_RAYCAST_USE_MAX_DISTANCE* | bool | *New in version R18:* Use maximum ray casting distance. |
| *BAKE_TEX_RAYCAST_CUSTOM_MAX_DISTANCE* | float | *New in version R18:* Custom maximum ray casting distance. |
| *BAKE_TEX_RAYCAST_USE_AUTO_SPIKE_FILTER_THRESHOLD* | bool | *New in version R18:* Use automatic spike filter threshold. |
| *BAKE_TEX_RAYCAST_CUSTOM_SPIKE_FILTER_THRESHOLD* | float | *New in version R18:* Custom spike filter threshold. |
| *BAKE_TEX_OPTIMAL_MAPPING* | int | Optimal mapping: |
| *BAKE_TEX_OPTIMAL_MAPPING_OFF* |  | Off. |
| *BAKE_TEX_OPTIMAL_MAPPING_CUBIC* |  | Cubic. |
| *BAKE_TEX_OPTIMAL_MAPPING_ANGLE* |  | Angle. |
| *BAKE_TEX_OPTIMAL_MAPPING_PACKED* |  | Packed. |
| *BAKE_TEX_OPTIMAL_MAPPING_RELAXCOUNT* | int | Optimal mapping relax count. |
| *BAKE_TEX_OPTIMAL_MAPPING_PREVIEW* | int | Optimal mapping preview. |
| *BAKE_TEX_NO_INIT_BITMAP* | bool | Set to **True** if the passed [`MultipassBitmap`](../modules/c4d.bitmaps/BaseBitmap/MultipassBitmap/index.md#c4d.bitmaps.MultipassBitmap) is already initialized. |
| *BAKE_TEX_AUTO_SIZE* | bool | Auto size. |
| *BAKE_TEX_AUTO_SIZE_MIN* | int | Minimum auto size. |
| *BAKE_TEX_AUTO_SIZE_MAX* | int | Maximum auto size. |
| *BAKE_TEX_AUTO_PIXEL_SIZE* | float | Automatic pixel size. |
| *BAKE_TEX_STATUSBAR* | str | Status bar text. |
