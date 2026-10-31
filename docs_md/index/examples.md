# Examples

> Annotated example scripts and plugins of the SDK.


## examples/animation

- [key_quaternion_interpolation](../examples/animation/key_quaternion_interpolation.py.md) ([source](../../examples/animation/key_quaternion_interpolation.py)): Checks the interpolation of the first key for an object’s rotation track.
- [motion_tracker_object_track](../examples/animation/motion_tracker_object_track.py.md) ([source](../../examples/animation/motion_tracker_object_track.py)): Loops through all the tracks of the active Motion Tracker object.
- [object_find_best_euler_angle](../examples/animation/object_find_best_euler_angle.py.md) ([source](../../examples/animation/object_find_best_euler_angle.py)): Checks the rotation tracks of the active object.
- [object_quaternion_rotation](../examples/animation/object_quaternion_rotation.py.md) ([source](../../examples/animation/object_quaternion_rotation.py)): Checks if the active object uses quaternion interpolation.
- [object_sync_vector_keys](../examples/animation/object_sync_vector_keys.py.md) ([source](../../examples/animation/object_sync_vector_keys.py)): Synchronizes the keys for the tracks of the active cube’s “Size” parameter.
- [object_vector_curves](../examples/animation/object_vector_curves.py.md) ([source](../../examples/animation/object_vector_curves.py)): Reads the vector components curves of the active object’s rotation track curve.
- [object_vector_tracks](../examples/animation/object_vector_tracks.py.md) ([source](../../examples/animation/object_vector_tracks.py)): Reads the vector components tracks of the active object’s position track curve.

## examples/animation/simulation

- [field_list_add_mask](../examples/animation/simulation/field_list_add_mask.py.md) ([source](../../examples/animation/simulation/field_list_add_mask.py)): Creates a FieldList with a formula layer, a mask and another formula layer used as a mask of the first formula layer.
- [field_list_sampling](../examples/animation/simulation/field_list_sampling.py.md) ([source](../../examples/animation/simulation/field_list_sampling.py)): Samples arbitrary points from multiple fields with c4d.FieldList and stores the result into a vertex color tag.
- [field_object_sampling](../examples/animation/simulation/field_object_sampling.py.md) ([source](../../examples/animation/simulation/field_object_sampling.py)): Samples arbitrary points within a random field.
- [modata_get_selection](../examples/animation/simulation/modata_get_selection.py.md) ([source](../../examples/animation/simulation/modata_get_selection.py)): Retrieves all selected clones of the active Cloner object.
- [modata_get_weights](../examples/animation/simulation/modata_get_weights.py.md) ([source](../../examples/animation/simulation/modata_get_weights.py)): Retrieves the weights from all clones of the active Cloner object.
- [modata_read_color](../examples/animation/simulation/modata_read_color.py.md) ([source](../../examples/animation/simulation/modata_read_color.py)): Retrieves the color or each clone using two ways.
- [modata_set_selection](../examples/animation/simulation/modata_set_selection.py.md) ([source](../../examples/animation/simulation/modata_set_selection.py)): Generates and sets a MoGraph selection tag on a MoGraph cloner object.
- [modata_set_weights](../examples/animation/simulation/modata_set_weights.py.md) ([source](../../examples/animation/simulation/modata_set_weights.py)): Sets a weight of 1.0 for all clones of the active Cloner object.
- [particle_group_object](../examples/animation/simulation/particle_group_object.py.md) ([source](../../examples/animation/simulation/particle_group_object.py)): Demonstrates how to read particle data from a ParticleGroupObject.
- [thinking_particles_creates](../examples/animation/simulation/thinking_particles_creates.py.md) ([source](../../examples/animation/simulation/thinking_particles_creates.py)): Creates 90 Thinking Particles.
- [voronoi_fracture](../examples/animation/simulation/voronoi_fracture.py.md) ([source](../../examples/animation/simulation/voronoi_fracture.py)): Creates and define a noise shader as an input of a Voronoi Fracture object.

## examples/animation

- [track_copy](../examples/animation/track_copy.py.md) ([source](../../examples/animation/track_copy.py)): Copies the position, rotation and animation Tracks (so all Keyframes) from obj1 to obj2.
- [track_create_keys](../examples/animation/track_create_keys.py.md) ([source](../../examples/animation/track_create_keys.py)): Creates position Y tracks.
- [track_synchronized](../examples/animation/track_synchronized.py.md) ([source](../../examples/animation/track_synchronized.py)): Checks if the rotation track of an object is synchronized.

## examples/data

- [_c4d_basebitmap](../examples/data/_c4d_basebitmap.py.md) ([source](../../examples/data/_c4d_basebitmap.py)): Demonstrates the usage of the central bitmap type.
- [_c4d_basecontainer](../examples/data/_c4d_basecontainer.py.md) ([source](../../examples/data/_c4d_basecontainer.py)): Demonstrates the usage of the fundamental container type in the Cinema API.
- [_c4d_descid](../examples/data/_c4d_descid.py.md) ([source](../../examples/data/_c4d_descid.py)): Demonstrates important functions for the types c4d.DescID and c4d.DescLevel.
- [_c4d_description](../examples/data/_c4d_description.py.md) ([source](../../examples/data/_c4d_description.py)): Demonstrates important functions for the type c4d.Description.
- [_maxon_basearray](../examples/data/_maxon_basearray.py.md) ([source](../../examples/data/_maxon_basearray.py)): Demonstrates instantiation and usage of various Maxon data types.
- [_maxon_datadictionary](../examples/data/_maxon_datadictionary.py.md) ([source](../../examples/data/_maxon_datadictionary.py)): Demonstrates the key functionalities of maxon.DataDictionary.
- [_maxon_tuple](../examples/data/_maxon_tuple.py.md) ([source](../../examples/data/_maxon_tuple.py)): Creates a Maxon Tuple of 3 fields (any maxon type is working).

## examples/gui

- [dialog_ask_number](../examples/gui/dialog_ask_number.py.md) ([source](../../examples/gui/dialog_ask_number.py)): Creates a Modal Dialog asking for an integer or a float.
- [dialog_menu_hide_content](../examples/gui/dialog_menu_hide_content.py.md) ([source](../../examples/gui/dialog_menu_hide_content.py)): Creates an async Dialog with a top menu.
- [dialog_modal](../examples/gui/dialog_modal.py.md) ([source](../../examples/gui/dialog_modal.py)): Creates a basic Modal Dialog.
- [dialog_quick_tab](../examples/gui/dialog_quick_tab.py.md) ([source](../../examples/gui/dialog_quick_tab.py)): Creates a Modal Dialog displaying a different SubDialog according to the selected entry of the QuickTab.
- [dialog_subdialog](../examples/gui/dialog_subdialog.py.md) ([source](../../examples/gui/dialog_subdialog.py)): Creates and attaches a SubDialog to a Dialog.
- [script_icon](../examples/gui/script_icon.py.md) ([source](../../examples/gui/script_icon.py)): Example to customize the icon used for a script.
- [script_name_description](../examples/gui/script_name_description.py.md) ([source](../../examples/gui/script_name_description.py)): Example to customize the name and the description in the script manager.
- [user_area_basic](../examples/gui/user_area_basic.py.md) ([source](../../examples/gui/user_area_basic.py)): Creates and attaches a GeUserArea to a Dialog.
- [user_area_drag](../examples/gui/user_area_drag.py.md) ([source](../../examples/gui/user_area_drag.py)): Creates and attaches a GeUserArea to a Dialog.

## examples/io

- [asset_databases](../examples/io/asset_databases.py.md) ([source](../../examples/io/asset_databases.py)): Provides examples for handling asset databases and repositories.
- [asset_metadata](../examples/io/asset_metadata.py.md) ([source](../../examples/io/asset_metadata.py)): Provides examples for reading and writing asset metadata.
- [asset_types](../examples/io/asset_types.py.md) ([source](../../examples/io/asset_types.py)): Provides examples for creating and loading different asset types.
- [bitmap_fill_color](../examples/io/bitmap_fill_color.py.md) ([source](../../examples/io/bitmap_fill_color.py)): Adds an overlay color to a Picture.
- [bitmap_init_vector_file](../examples/io/bitmap_init_vector_file.py.md) ([source](../../examples/io/bitmap_init_vector_file.py)): Initializes a bitmap from a vector image file.
- [export_alembic](../examples/io/export_alembic.py.md) ([source](../../examples/io/export_alembic.py)): Exports Alembic with custom settings.
- [export_obj](../examples/io/export_obj.py.md) ([source](../../examples/io/export_obj.py)): Exports Obj with custom settings.
- [image_copy_32bit](../examples/io/image_copy_32bit.py.md) ([source](../../examples/io/image_copy_32bit.py)): Copies the internal data of a 32 bit per-channel image to a new one.
- [import_obj](../examples/io/import_obj.py.md) ([source](../../examples/io/import_obj.py)): Imports Obj with custom settings.
- [import_sketchup](../examples/io/import_sketchup.py.md) ([source](../../examples/io/import_sketchup.py)): Imports Sketchup File with custom settings.
- [import_step](../examples/io/import_step.py.md) ([source](../../examples/io/import_step.py)): Imports STP/STEP with custom settings.
- [memory_file_bitmap](../examples/io/memory_file_bitmap.py.md) ([source](../../examples/io/memory_file_bitmap.py)): Writes/Reads a bitmap to/from memory.
- [memory_file_data](../examples/io/memory_file_data.py.md) ([source](../../examples/io/memory_file_data.py)): Writes/Reads simple data to/from memory.
- [texture_paths](../examples/io/texture_paths.py.md) ([source](../../examples/io/texture_paths.py)): Sets and gets global texture paths (Preferences->Files->Paths).

## examples/math

- [_c4d_geraycollider](../examples/math/_c4d_geraycollider.py.md) ([source](../../examples/math/_c4d_geraycollider.py)): Demonstrates ray casting.
- [_c4d_kdtree](../examples/math/_c4d_kdtree.py.md) ([source](../../examples/math/_c4d_kdtree.py)): Demonstrates how to use KDTree to find neighboring points in a mesh.
- [_c4d_matrix](../examples/math/_c4d_matrix.py.md) ([source](../../examples/math/_c4d_matrix.py)): Demonstrates working with matrices.
- [_c4d_noise](../examples/math/_c4d_noise.py.md) ([source](../../examples/math/_c4d_noise.py)): Demonstrates working with noise functions.
- [_c4d_quaternion](../examples/math/_c4d_quaternion.py.md) ([source](../../examples/math/_c4d_quaternion.py)): Demonstrates working with quaternions.
- [_c4d_vector](../examples/math/_c4d_vector.py.md) ([source](../../examples/math/_c4d_vector.py)): Demonstrates working with vectors.
- [_mxutils_random](../examples/math/_mxutils_random.py.md) ([source](../../examples/math/_mxutils_random.py)): Demonstrates deterministic random values with mxutils.Random.

## examples/misc

- [mxutils_checktype](../examples/misc/mxutils_checktype.py.md) ([source](../../examples/misc/mxutils_checktype.py)): Demonstrates type and iterable validation with mxutils.
- [mxutils_debugprint](../examples/misc/mxutils_debugprint.py.md) ([source](../../examples/misc/mxutils_debugprint.py)): Demonstrates mxutils helpers for diagnosing Cinema 4D scene data.
- [mxutils_decorators](../examples/misc/mxutils_decorators.py.md) ([source](../../examples/misc/mxutils_decorators.py)): Demonstrates mxutils helpers for diagnosing Cinema 4D scene data.
- [mxutils_localimportpath](../examples/misc/mxutils_localimportpath.py.md) ([source](../../examples/misc/mxutils_localimportpath.py)): Demonstrates importing a package relative to a saved Python script.
- [mxutils_symboltranslationcache](../examples/misc/mxutils_symboltranslationcache.py.md) ([source](../../examples/misc/mxutils_symboltranslationcache.py)): Demonstrates translating Cinema 4D symbols with SymbolTranslationCache.
- [script_load](../examples/misc/script_load.py.md) ([source](../../examples/misc/script_load.py)): Create a new temporary script.

## examples/modeling

- [geometry_cache](../examples/modeling/geometry_cache.py.md) ([source](../../examples/modeling/geometry_cache.py)): Explains the geometry model of the Cinema API in Cinema 4D.
- [geometry_edges](../examples/modeling/geometry_edges.py.md) ([source](../../examples/modeling/geometry_edges.py)): Demonstrates handling edges in polygon objects at the example of splitting edges.
- [geometry_extrude](../examples/modeling/geometry_extrude.py.md) ([source](../../examples/modeling/geometry_extrude.py)): Demonstrates how to modify polygonal geometry at the example of extruding polygons.
- [geometry_flatten](../examples/modeling/geometry_flatten.py.md) ([source](../../examples/modeling/geometry_flatten.py)): Demonstrates how to deform points of a point object at the example of ‘flattening’ the selected polygons in a polygon object.
- [geometry_polygon_object](../examples/modeling/geometry_polygon_object.py.md) ([source](../../examples/modeling/geometry_polygon_object.py)): Explains the user-editable polygon object model of the Cinema API.
- [geometry_sds_weights](../examples/modeling/geometry_sds_weights.py.md) ([source](../../examples/modeling/geometry_sds_weights.py)): Demonstrates how to read and write data of an SDS weight tag.
- [geometry_spline_object](../examples/modeling/geometry_spline_object.py.md) ([source](../../examples/modeling/geometry_spline_object.py)): Explains the user-editable spline object model of the Cinema API.
- [geometry_transfer_axis](../examples/modeling/geometry_transfer_axis.py.md) ([source](../../examples/modeling/geometry_transfer_axis.py)): Demonstrates how to ‘transfer’ the axis of a point object to another object while keeping its vertices in place.
- [lod](../examples/modeling/lod.py.md) ([source](../../examples/modeling/lod.py)): Demonstrates creating and configuring LOD objects.
- [modeling_command_bridge](../examples/modeling/modeling_command_bridge.py.md) ([source](../../examples/modeling/modeling_command_bridge.py)): Demonstrates how to execute the ‘Bridge’ tool.
- [modeling_command_current_state](../examples/modeling/modeling_command_current_state.py.md) ([source](../../examples/modeling/modeling_command_current_state.py)): Demonstrates how to execute the ‘Current State to Object’ tool.
- [modeling_command_edge_smooth](../examples/modeling/modeling_command_edge_smooth.py.md) ([source](../../examples/modeling/modeling_command_edge_smooth.py)): Demonstrates how to execute the ‘Edge Smooth’ tool.
- [modeling_command_extrude](../examples/modeling/modeling_command_extrude.py.md) ([source](../../examples/modeling/modeling_command_extrude.py)): Demonstrates how to use the SendModelingCommand (SMC) function in general at the example of the ‘Extrude’ tool.
- [modeling_command_flatten](../examples/modeling/modeling_command_flatten.py.md) ([source](../../examples/modeling/modeling_command_flatten.py)): Demonstrates how to execute the ‘Flatten’ tool.
- [modeling_command_join](../examples/modeling/modeling_command_join.py.md) ([source](../../examples/modeling/modeling_command_join.py)): Demonstrates how to execute the ‘Join’ tool.
- [normal_tag](../examples/modeling/normal_tag.py.md) ([source](../../examples/modeling/normal_tag.py)): Script creates a NormalTag for a selected polygon object with a phong tag where the normals have been rotated by 45° around the world z-axis.
- [reduction_create](../examples/modeling/reduction_create.py.md) ([source](../../examples/modeling/reduction_create.py)): Creates a new PolygonReduction object.
- [reduction_edge_level](../examples/modeling/reduction_edge_level.py.md) ([source](../../examples/modeling/reduction_edge_level.py)): Reduces the active PolygonObject to the given edge count.
- [reduction_preprocess](../examples/modeling/reduction_preprocess.py.md) ([source](../../examples/modeling/reduction_preprocess.py)): Configures the given PolygonReduction object.
- [reduction_triangle_level](../examples/modeling/reduction_triangle_level.py.md) ([source](../../examples/modeling/reduction_triangle_level.py)): Copyright: MAXON Computer GmbH Author: Yannick Puech
- [reduction_vertex_level](../examples/modeling/reduction_vertex_level.py.md) ([source](../../examples/modeling/reduction_vertex_level.py)): Reduces the active PolygonObject to the given vertex count.
- [snap_3d_point](../examples/modeling/snap_3d_point.py.md) ([source](../../examples/modeling/snap_3d_point.py)): Enables the snap if it’s not already the case.
- [snap_quantize](../examples/modeling/snap_quantize.py.md) ([source](../../examples/modeling/snap_quantize.py)): Enables the quantize if it’s not already the case.
- [snap_workplane](../examples/modeling/snap_workplane.py.md) ([source](../../examples/modeling/snap_workplane.py)): Retrieves the current workplane position and object.
- [uv_command](../examples/modeling/uv_command.py.md) ([source](../../examples/modeling/uv_command.py)): Calls BodyPaint 3D UV commands.
- [uv_geometry](../examples/modeling/uv_geometry.py.md) ([source](../../examples/modeling/uv_geometry.py)): Explains how to generate UVW data for polygon objects.
- [uv_pin_deselect](../examples/modeling/uv_pin_deselect.py.md) ([source](../../examples/modeling/uv_pin_deselect.py)): Removes the polygon point selection to the uv points pinned.
- [uv_pin_points](../examples/modeling/uv_pin_points.py.md) ([source](../../examples/modeling/uv_pin_points.py)): Sets the polygon point selection to the uv points pinned.
- [uv_pin_select](../examples/modeling/uv_pin_select.py.md) ([source](../../examples/modeling/uv_pin_select.py)): Adds the polygon point selection to the uv points pinned.
- [uv_seams](../examples/modeling/uv_seams.py.md) ([source](../../examples/modeling/uv_seams.py)): Copies the UV seams to the edge polygon selection.
- [vertex_color_points](../examples/modeling/vertex_color_points.py.md) ([source](../../examples/modeling/vertex_color_points.py)): Gets and Sets Vertex Colors in Point mode: Changes all black Vertex Colors to red.
- [vertex_color_polygons](../examples/modeling/vertex_color_polygons.py.md) ([source](../../examples/modeling/vertex_color_polygons.py)): Gets and Sets Vertex Colors in Polygon mode: Changes all vertex colors to red.
- [volume_boolean_mesh](../examples/modeling/volume_boolean_mesh.py.md) ([source](../../examples/modeling/volume_boolean_mesh.py)): Converts a Polygon Object to a Volume.
- [volume_builder_access](../examples/modeling/volume_builder_access.py.md) ([source](../../examples/modeling/volume_builder_access.py)): Retrieves a volume object from a volume builder.
- [volume_builder_add_object](../examples/modeling/volume_builder_add_object.py.md) ([source](../../examples/modeling/volume_builder_add_object.py)): Creates a volume builder and adds a cube object to it.
- [volume_builder_create](../examples/modeling/volume_builder_create.py.md) ([source](../../examples/modeling/volume_builder_create.py)): Creates a volume builder and inserts it into the active document.
- [volume_builder_inputs](../examples/modeling/volume_builder_inputs.py.md) ([source](../../examples/modeling/volume_builder_inputs.py)): Iterates over all input of a Volume Builder.
- [volume_command_sphere](../examples/modeling/volume_command_sphere.py.md) ([source](../../examples/modeling/volume_command_sphere.py)): Creates a sphere volume with the corresponding command.
- [volume_command_spline](../examples/modeling/volume_command_spline.py.md) ([source](../../examples/modeling/volume_command_spline.py)): Creates a volume from the selected spline object.
- [volume_curl](../examples/modeling/volume_curl.py.md) ([source](../../examples/modeling/volume_curl.py)): Creates a new vector volume object with a curl filter applied from an existing Volume Builder set as vector mode.
- [volume_export_mesh](../examples/modeling/volume_export_mesh.py.md) ([source](../../examples/modeling/volume_export_mesh.py)): Convert a Polygon Object to a Volume and save this volume to a VDB File Save a VDB file.
- [volume_gradient_sphere](../examples/modeling/volume_gradient_sphere.py.md) ([source](../../examples/modeling/volume_gradient_sphere.py)): Create a Spherical Volume filled with gradient data.
- [volume_grid_read](../examples/modeling/volume_grid_read.py.md) ([source](../../examples/modeling/volume_grid_read.py)): Reads the Float value of the first channel available from a Volume stored in a Volume Builder.
- [volume_grid_write](../examples/modeling/volume_grid_write.py.md) ([source](../../examples/modeling/volume_grid_write.py)): Create a volume from scratch and assign values to voxels.
- [volume_import_vdb](../examples/modeling/volume_import_vdb.py.md) ([source](../../examples/modeling/volume_import_vdb.py)): Loads a VDB file to a c4d.VolumeObject.
- [volume_mesh_conversion](../examples/modeling/volume_mesh_conversion.py.md) ([source](../../examples/modeling/volume_mesh_conversion.py)): Convert a Polygon Object to a Volume and convert it back to a Polygon Object
- [volume_mix_meshes](../examples/modeling/volume_mix_meshes.py.md) ([source](../../examples/modeling/volume_mix_meshes.py)): Converts a Polygon Object to a FOG Volume.
- [volume_mix_vectors](../examples/modeling/volume_mix_vectors.py.md) ([source](../../examples/modeling/volume_mix_vectors.py)): Creates 2 vector volume from scratch.
- [volume_vdb_import](../examples/modeling/volume_vdb_import.py.md) ([source](../../examples/modeling/volume_vdb_import.py)): Asks for a VDB file to load into a VolumeRef (a VolumeInterface Reference).
- [volume_vector_to_fog](../examples/modeling/volume_vector_to_fog.py.md) ([source](../../examples/modeling/volume_vector_to_fog.py)): Creates a vector volume from scratch.

## examples/nodes

- [graph_descriptions_basics](../examples/nodes/graph_descriptions_basics.py.md) ([source](../../examples/nodes/graph_descriptions_basics.py)): Demonstrates how graph descriptions create and modify node graphs.
- [graph_descriptions_commands](../examples/nodes/graph_descriptions_commands.py.md) ([source](../../examples/nodes/graph_descriptions_commands.py)): Demonstrates graph description commands.
- [graph_descriptions_queries](../examples/nodes/graph_descriptions_queries.py.md) ([source](../../examples/nodes/graph_descriptions_queries.py)): Demonstrates graph description queries, including lazy color and vector literals.
- [graph_descriptions_references](../examples/nodes/graph_descriptions_references.py.md) ([source](../../examples/nodes/graph_descriptions_references.py)): Demonstrates graph description references together with lazy color and URL literals.
- [nodes_associate_nodes](../examples/nodes/nodes_associate_nodes.py.md) ([source](../../examples/nodes/nodes_associate_nodes.py)): Demonstrates how to associate nodes in a Maxon API graph with their corresponding Cinema 4D API surrogate elements.
- [nodes_create_or_get_graphs](../examples/nodes/nodes_create_or_get_graphs.py.md) ([source](../../examples/nodes/nodes_create_or_get_graphs.py)): Demonstrates creating or getting node graphs in a scene.
- [nodes_graph_entities](../examples/nodes/nodes_graph_entities.py.md) ([source](../../examples/nodes/nodes_graph_entities.py)): Demonstrates the inner structure of node graphs and how to find entities in them.
- [nodes_group](../examples/nodes/nodes_group.py.md) ([source](../../examples/nodes/nodes_group.py)): Retrieve the selected node material and group the node that are selected.
- [nodes_info](../examples/nodes/nodes_info.py.md) ([source](../../examples/nodes/nodes_info.py)): Retrieve information about the selected port of a selected material.
- [nodes_material_access](../examples/nodes/nodes_material_access.py.md) ([source](../../examples/nodes/nodes_material_access.py)): Demonstrates accessing node materials and their graph contents in a scene.
- [nodes_material_create_redshift](../examples/nodes/nodes_material_create_redshift.py.md) ([source](../../examples/nodes/nodes_material_create_redshift.py)): Demonstrates setting up a Redshift node material composed out of multiple nodes.
- [nodes_material_standard](../examples/nodes/nodes_material_standard.py.md) ([source](../../examples/nodes/nodes_material_standard.py)): Demonstrates setting up a Standard renderer node material composed out of multiple nodes.
- [nodes_modify_port](../examples/nodes/nodes_modify_port.py.md) ([source](../../examples/nodes/nodes_modify_port.py)): Create a material for the standard node space and modify the value of the BDSF color port.
- [nodes_selection](../examples/nodes/nodes_selection.py.md) ([source](../../examples/nodes/nodes_selection.py)): This example shows how to select different elements on a node graph.
- [nodes_solo](../examples/nodes/nodes_solo.py.md) ([source](../../examples/nodes/nodes_solo.py)): This example shows how to solo a node.
- [nodes_wire_mute](../examples/nodes/nodes_wire_mute.py.md) ([source](../../examples/nodes/nodes_wire_mute.py)): Retrieve the selected node material and toggle-mute the selected connection, i.e., if the connection is muted, it will be unmuted or vice-versa.
- [xpresso_create_connect](../examples/nodes/xpresso_create_connect.py.md) ([source](../../examples/nodes/xpresso_create_connect.py)): Creates a Constants and Results node in the Xpresso Tag of the selected object.
- [xpresso_delete](../examples/nodes/xpresso_delete.py.md) ([source](../../examples/nodes/xpresso_delete.py)): Deletes the first node created from the Xpresso Tag of the selected object.
- [xpresso_from_tag](../examples/nodes/xpresso_from_tag.py.md) ([source](../../examples/nodes/xpresso_from_tag.py)): Retrieves the Node Master (The BaseList2D object that holds all nodes) from an Xpresso Tag.
- [xpresso_iterate](../examples/nodes/xpresso_iterate.py.md) ([source](../../examples/nodes/xpresso_iterate.py)): Loops through all nodes from the Xpresso Tag of the selected object.
- [xpresso_move](../examples/nodes/xpresso_move.py.md) ([source](../../examples/nodes/xpresso_move.py)): Moves the first node in the Graph View created from the Xpresso Tag of the selected object.

## examples/plugins/py_cmd_gui_dynamic

- [py_cmd_gui_dynamic](../examples/plugins/py_cmd_gui_dynamic/py_cmd_gui_dynamic.pyp.md) ([source](../../examples/plugins/py_cmd_gui_dynamic/py_cmd_gui_dynamic.pyp)): Demonstrates a dialog with dynamic content, where the content changes based on user input.

## examples/plugins/py_cmd_gui_hello_world

- [py_cmd_gui_hello_world](../examples/plugins/py_cmd_gui_hello_world/py_cmd_gui_hello_world.pyp.md) ([source](../../examples/plugins/py_cmd_gui_hello_world/py_cmd_gui_hello_world.pyp)): Demonstrates the most basic command/dialog plugin possible.

## examples/plugins/py_cmd_gui_html

- [py_cmd_gui_html](../examples/plugins/py_cmd_gui_html/py_cmd_gui_html.pyp.md) ([source](../../examples/plugins/py_cmd_gui_html/py_cmd_gui_html.pyp)): Demonstrates how to implement a dialog that hosts an HTML viewer and can send and receive data to/from the displayed web page.

## examples/plugins/py_cmd_gui_persistent

- [py_cmd_gui_persistent](../examples/plugins/py_cmd_gui_persistent/py_cmd_gui_persistent.pyp.md) ([source](../../examples/plugins/py_cmd_gui_persistent/py_cmd_gui_persistent.pyp)): Demonstrates how to store dialog layout data and values persistently over dialog open/close and Cinema 4D restart boundaries.

## examples/plugins/py_cmd_gui_persistent_no_restart

- [py_cmd_gui_persistent_no_restart](../examples/plugins/py_cmd_gui_persistent_no_restart/py_cmd_gui_persistent_no_restart.pyp.md) ([source](../../examples/plugins/py_cmd_gui_persistent_no_restart/py_cmd_gui_persistent_no_restart.pyp)): Demonstrates a simple way to store dialog layout data and values persistently over dialog open/close boundaries (but not over Cinema 4D restart boundaries).

## examples/plugins/py_cmd_gui_resources

- [py_cmd_gui_resources](../examples/plugins/py_cmd_gui_resources/py_cmd_gui_resources.pyp.md) ([source](../../examples/plugins/py_cmd_gui_resources/py_cmd_gui_resources.pyp)): Demonstrates a plugin that uses resources to define its dialog layout and string translations.
- [unicode_encode_strings](../examples/plugins/py_cmd_gui_resources/unicode_encode_strings.py.md) ([source](../../examples/plugins/py_cmd_gui_resources/unicode_encode_strings.py)): Provides an example for how one could realize a string encoding pipeline for plugin resources.

## examples/plugins/py_cmd_gui_simple

- [py_cmd_gui_simple](../examples/plugins/py_cmd_gui_simple/py_cmd_gui_simple.pyp.md) ([source](../../examples/plugins/py_cmd_gui_simple/py_cmd_gui_simple.pyp)): Demonstrates a simple dialog with two number input fields, a combo box and a button to carry out numeric operations on the two numbers.

## examples/plugins/py_cmd_memory_viewer

- [py_cmd_memory_viewer](../examples/plugins/py_cmd_memory_viewer/py_cmd_memory_viewer.pyp.md) ([source](../../examples/plugins/py_cmd_memory_viewer/py_cmd_memory_viewer.pyp)): Demonstrates implementing a simple legacy memory viewer dialog.

## examples/plugins/py_cmd_sculpt_save_mask

- [py_cmd_sculpt_save_mask](../examples/plugins/py_cmd_sculpt_save_mask/py_cmd_sculpt_save_mask.pyp.md) ([source](../../examples/plugins/py_cmd_sculpt_save_mask/py_cmd_sculpt_save_mask.pyp)): Demonstrates the legacy Sculpting API; it is highly specialized and not that useful outside of sculpting.

## examples/plugins/py_cmd_texture_baker

- [py_cmd_texture_baker](../examples/plugins/py_cmd_texture_baker/py_cmd_texture_baker.pyp.md) ([source](../../examples/plugins/py_cmd_texture_baker/py_cmd_texture_baker.pyp)): Demonstrates implementing a simple legacy texture baking dialog.

## examples/plugins/py_cmd_tool_finalization

- [py_cmd_tool_finalization](../examples/plugins/py_cmd_tool_finalization/py_cmd_tool_finalization.pyp.md) ([source](../../examples/plugins/py_cmd_tool_finalization/py_cmd_tool_finalization.pyp)): Demonstrates a tool finalization workflow at the example of editing SDS weights.

## examples/plugins/py_io_ies_meta

- [py_io_ies_meta](../examples/plugins/py_io_ies_meta/py_io_ies_meta.pyp.md) ([source](../../examples/plugins/py_io_ies_meta/py_io_ies_meta.pyp)): Demonstrates how to implement a scene saver plugin that exports all IES Meta information from the current document to a txt file, iterating through all objects…
- [py_io_ies_meta_loader](../examples/plugins/py_io_ies_meta/py_io_ies_meta_loader.pyp.md) ([source](../../examples/plugins/py_io_ies_meta/py_io_ies_meta_loader.pyp)): Demonstrates a scene loader plugin for IES Meta data.

## examples/plugins/py_io_xample_loader

- [py_io_xample_loader](../examples/plugins/py_io_xample_loader/py_io_xample_loader.pyp.md) ([source](../../examples/plugins/py_io_xample_loader/py_io_xample_loader.pyp)): Demonstrates how to implement a custom bitmap loader to import a custom picture format into Cinema 4D.

## examples/plugins/py_io_xample_saver

- [py_io_xample_saver](../examples/plugins/py_io_xample_saver/py_io_xample_saver.pyp.md) ([source](../../examples/plugins/py_io_xample_saver/py_io_xample_saver.pyp)): Demonstrates how to implement a custom bitmap saver to export a custom picture format into Cinema 4D.

## examples/plugins/py_msc_licensing

- [py_msc_licensing](../examples/plugins/py_msc_licensing/py_msc_licensing.pyp.md) ([source](../../examples/plugins/py_msc_licensing/py_msc_licensing.pyp)): Demonstrates how to implement licensing checks in plugins.
- [py_msc_licensing_simple](../examples/plugins/py_msc_licensing/py_msc_licensing_simple.pyp.md) ([source](../../examples/plugins/py_msc_licensing/py_msc_licensing_simple.pyp)): Demonstrates simple licensing workflow for Python plugins in Cinema 4D.

## examples/plugins/py_msc_menu

- [py_msc_menu](../examples/plugins/py_msc_menu/py_msc_menu.pyp.md) ([source](../../examples/plugins/py_msc_menu/py_msc_menu.pyp)): Demonstrates how to build custom menus for your plugins.

## examples/plugins/py_msc_noise_falloff

- [py_msc_noise_falloff](../examples/plugins/py_msc_noise_falloff/py_msc_noise_falloff.pyp.md) ([source](../../examples/plugins/py_msc_noise_falloff/py_msc_noise_falloff.pyp)): Demonstrates legacy falloffs, a technology that has been replaced by fields in R20.

## examples/plugins/py_msc_preference

- [py_msc_preference](../examples/plugins/py_msc_preference/py_msc_preference.pyp.md) ([source](../../examples/plugins/py_msc_preference/py_msc_preference.pyp)): Demonstrates how to implement a preference category in the Cinema 4D preference dialog, exposing parameters as global preferences.

## examples/plugins/py_msc_render_token

- [py_msc_render_token](../examples/plugins/py_msc_render_token/py_msc_render_token.pyp.md) ([source](../../examples/plugins/py_msc_render_token/py_msc_render_token.pyp)): Demonstrates how to register two Tokens, one visible in the render settings and the other not.

## examples/plugins/py_obj_assetcontainer

- [py_obj_assetcontainer](../examples/plugins/py_obj_assetcontainer/py_obj_assetcontainer.pyp.md) ([source](../../examples/plugins/py_obj_assetcontainer/py_obj_assetcontainer.pyp)): Demonstrates NodeData serialization and custom branching.

## examples/plugins/py_obj_custom_icon

- [py_obj_custom_icon](../examples/plugins/py_obj_custom_icon/py_obj_custom_icon.pyp.md) ([source](../../examples/plugins/py_obj_custom_icon/py_obj_custom_icon.pyp)): Demonstrates how to implement a scene element that dynamically updates its icon.

## examples/plugins/py_obj_double_circle

- [py_obj_double_circle](../examples/plugins/py_obj_double_circle/py_obj_double_circle.pyp.md) ([source](../../examples/plugins/py_obj_double_circle/py_obj_double_circle.pyp)): Demonstrates how to implement a spline object generator with handles to drive parameters.

## examples/plugins/py_obj_dynamic_parameters

- [py_obj_dynamic_parameters](../examples/plugins/py_obj_dynamic_parameters/py_obj_dynamic_parameters.pyp.md) ([source](../../examples/plugins/py_obj_dynamic_parameters/py_obj_dynamic_parameters.pyp)): Demonstrates how to implement a node (at the example of an object) that dynamically updates its parameters.

## examples/plugins/py_obj_gravitation

- [py_obj_gravitation](../examples/plugins/py_obj_gravitation/py_obj_gravitation.pyp.md) ([source](../../examples/plugins/py_obj_gravitation/py_obj_gravitation.pyp)): Demonstrates how to implement a classic particle modifier object that applies a simple gravitation effect for each particle.

## examples/plugins/py_obj_ocio_node

- [py_obj_ocio_node](../examples/plugins/py_obj_ocio_node/py_obj_ocio_node.pyp.md) ([source](../../examples/plugins/py_obj_ocio_node/py_obj_ocio_node.pyp)): Demonstrates how to implement a scene element respecting OpenColorIO color management.

## examples/plugins/py_obj_offset_y_spline

- [py_obj_offset_y_spline](../examples/plugins/py_obj_offset_y_spline/py_obj_offset_y_spline.pyp.md) ([source](../../examples/plugins/py_obj_offset_y_spline/py_obj_offset_y_spline.pyp)): Demonstrates a spline offset generator (very questionable design, should not be followed).

## examples/plugins/py_obj_rounded_tube

- [py_obj_rounded_tube](../examples/plugins/py_obj_rounded_tube/py_obj_rounded_tube.pyp.md) ([source](../../examples/plugins/py_obj_rounded_tube/py_obj_rounded_tube.pyp)): Demonstrates how to implement a polygonal object generator with handles to drive parameters.

## examples/plugins/py_obj_sculpt_modifier_deformer

- [py_obj_sculpt_modifier_deformer](../examples/plugins/py_obj_sculpt_modifier_deformer/py_obj_sculpt_modifier_deformer.pyp.md) ([source](../../examples/plugins/py_obj_sculpt_modifier_deformer/py_obj_sculpt_modifier_deformer.pyp)): Demonstrates how to implement a modifier object that modifies a point object using the pull sculpting brush tool.

## examples/plugins/py_obj_sphere_deformer

- [py_obj_sphere_deformer](../examples/plugins/py_obj_sphere_deformer/py_obj_sphere_deformer.pyp.md) ([source](../../examples/plugins/py_obj_sphere_deformer/py_obj_sphere_deformer.pyp)): Demonstrates how to implement a deformer object that pushes the points of a point object to a spherical shape, driven by radius and strength parameters.

## examples/plugins/py_sha_fresnel

- [py_sha_fresnel](../examples/plugins/py_sha_fresnel/py_sha_fresnel.pyp.md) ([source](../../examples/plugins/py_sha_fresnel/py_sha_fresnel.pyp)): Demonstrates how to implement a shader that computes a fresnel effect.

## examples/plugins/py_tag_look_at_camera

- [py_tag_look_at_camera](../examples/plugins/py_tag_look_at_camera/py_tag_look_at_camera.pyp.md) ([source](../../examples/plugins/py_tag_look_at_camera/py_tag_look_at_camera.pyp)): Demonstrates how to implement a tag that forces the host object to look at the camera (like the Look At Camera Tag).

## examples/plugins/py_tool_liquid_painter

- [py_tool_liquid_painter](../examples/plugins/py_tool_liquid_painter/py_tool_liquid_painter.pyp.md) ([source](../../examples/plugins/py_tool_liquid_painter/py_tool_liquid_painter.pyp)): Demonstrates how to implement a simple tool.

## examples/plugins/py_tool_sculpt_grab_brush

- [py_tool_sculpt_grab_brush](../examples/plugins/py_tool_sculpt_grab_brush/py_tool_sculpt_grab_brush.pyp.md) ([source](../../examples/plugins/py_tool_sculpt_grab_brush/py_tool_sculpt_grab_brush.pyp)): Demonstrates how to implement a brush tool that modifies a BaseObject by grabbing all points under the brush.

## examples/plugins/py_tool_sculpt_paint_brush

- [py_tool_sculpt_paint_brush](../examples/plugins/py_tool_sculpt_paint_brush/py_tool_sculpt_paint_brush.pyp.md) ([source](../../examples/plugins/py_tool_sculpt_paint_brush/py_tool_sculpt_paint_brush.pyp)): Demonstrates how to implement a brush tool that rasterizes the stencil onto the polygons touched by the brush, accessing the stencil and BodyPaint layer.

## examples/plugins/py_tool_sculpt_pull_brush

- [py_tool_sculpt_pull_brush](../examples/plugins/py_tool_sculpt_pull_brush/py_tool_sculpt_pull_brush.pyp.md) ([source](../../examples/plugins/py_tool_sculpt_pull_brush/py_tool_sculpt_pull_brush.pyp)): Demonstrates how to implement a brush tool that modifies a BaseObject by pulling all points under the brush.

## examples/plugins/py_tool_sculpt_twist_brush

- [py_tool_sculpt_twist_brush](../examples/plugins/py_tool_sculpt_twist_brush/py_tool_sculpt_twist_brush.pyp.md) ([source](../../examples/plugins/py_tool_sculpt_twist_brush/py_tool_sculpt_twist_brush.pyp)): Demonstrates how to implement a brush tool that modifies a BaseObject by twisting all points under the brush.

## examples/plugins/py_tool_ui

- [py_tool_ui](../examples/plugins/py_tool_ui/py_tool_ui.pyp.md) ([source](../../examples/plugins/py_tool_ui/py_tool_ui.pyp)): Demonstrates how to implement a ToolData with a linkBox where it’s possible to drag and drop an object, which is then cloned and added to the document in a ran…

## examples/rendering

- [_c4d_renderdata](../examples/rendering/_c4d_renderdata.py.md) ([source](../../examples/rendering/_c4d_renderdata.py))
- [batch_render_postprocess](../examples/rendering/batch_render_postprocess.py.md) ([source](../../examples/rendering/batch_render_postprocess.py)): Demonstrates to manipulate the file outputs of a batch render post process once the rendering has finished.
- [batch_render_preprocess](../examples/rendering/batch_render_preprocess.py.md) ([source](../../examples/rendering/batch_render_preprocess.py)): Demonstrates how to pre-process multiple documents before adding them to the batch renderer for rendering.
- [ocio](../examples/rendering/ocio.py.md) ([source](../../examples/rendering/ocio.py)): Demonstrates how to read, write, and convert colors in an OpenColorIO (OCIO) color-managed document in Cinema 4D.
- [render_complex](../examples/rendering/render_complex.py.md) ([source](../../examples/rendering/render_complex.py)): Demonstrates the details and manual handling of a programmatic rendering process.
- [render_hardware](../examples/rendering/render_hardware.py.md) ([source](../../examples/rendering/render_hardware.py)): Demonstrates how carry out a ‘hardware preview’ rendering, i.e., a rendering of what is shown in the viewport using the hardware renderer.
- [render_openexr](../examples/rendering/render_openexr.py.md) ([source](../../examples/rendering/render_openexr.py)): Configures OpenEXR output render format with SetImageSettingsDictionary() then reads these with GetImageSettingsDictionary().
- [render_preroll](../examples/rendering/render_preroll.py.md) ([source](../../examples/rendering/render_preroll.py)): Demonstrates how to render document from or at a given frame after prerolling it.
- [render_set_engine](../examples/rendering/render_set_engine.py.md) ([source](../../examples/rendering/render_set_engine.py)): Demonstrates how to manipulate the render settings of a rendering, specifically also the used render engine.
- [render_simple](../examples/rendering/render_simple.py.md) ([source](../../examples/rendering/render_simple.py)): Demonstrates a simple way to programmatically render a document to either memory or disk.
- [render_tiles](../examples/rendering/render_tiles.py.md) ([source](../../examples/rendering/render_tiles.py)): Demonstrates how to render a document split into tiles which can be composited back together to a full image.
- [render_token](../examples/rendering/render_token.py.md) ([source](../../examples/rendering/render_token.py)): Renders a BaseDocument and saves the resulting image using a filename handling tokens.

## examples/scene

- [_c4d_atom](../examples/scene/_c4d_atom.py.md) ([source](../../examples/scene/_c4d_atom.py)): Demonstrates important functions for the type c4d.C4DAtom.
- [_c4d_baselist2d](../examples/scene/_c4d_baselist2d.py.md) ([source](../../examples/scene/_c4d_baselist2d.py)): Demonstrates important functions for the type c4d.BaseList2D.
- [_c4d_gelistnode](../examples/scene/_c4d_gelistnode.py.md) ([source](../../examples/scene/_c4d_gelistnode.py)): Demonstrates important functions for the type c4d.GeListNode.
- [documents](../examples/scene/documents.py.md) ([source](../../examples/scene/documents.py)): Demonstrates basic document operations.
- [layers](../examples/scene/layers.py.md) ([source](../../examples/scene/layers.py)): Demonstrates how to assign a scene element to a layer.
- [objects](../examples/scene/objects.py.md) ([source](../../examples/scene/objects.py)): Demonstrates basic operations on objects.
- [parameters](../examples/scene/parameters.py.md) ([source](../../examples/scene/parameters.py)): Demonstrates different ways to access and modify parameters of Cinema 4D scene elements.
- [takes](../examples/scene/takes.py.md) ([source](../../examples/scene/takes.py)): Demonstrates the fundamental operations of the Take System.
- [traversal](../examples/scene/traversal.py.md) ([source](../../examples/scene/traversal.py)): Demonstrates scene traversal.
- [undos](../examples/scene/undos.py.md) ([source](../../examples/scene/undos.py)): Demonstrates adding undo steps for document modifications.
- [userdata](../examples/scene/userdata.py.md) ([source](../../examples/scene/userdata.py)): Demonstrates how to work with user data parameters.
