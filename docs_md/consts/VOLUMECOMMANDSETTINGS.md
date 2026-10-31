<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/VOLUMECOMMANDSETTINGS.html -->

# VOLUMECOMMANDSETTINGS <a id="volumecommandsettings"></a>

|   |   |   |   |   |
|---|---|---|---|---|
| *VOLUMECOMMANDTYPE_VOLUMETOMESH* |  |  |  |  |
|  | *VOLUMETOMESHSETTINGS_NONE* |  | None. |  |
|  | *VOLUMETOMESHSETTINGS_ISO* | float | Iso value to extract the mesh at. |  |
|  | *VOLUMETOMESHSETTINGS_ADAPTIVE* | float | Adaptive value for curvature based mesh reduction. |  |
| *VOLUMECOMMANDTYPE_MESHTOVOLUME* |  |  |  |  |
|  | *MESHTOVOLUMESETTINGS_NONE* |  | None. |  |
|  | *MESHTOVOLUMESETTINGS_GRIDSIZE* | float | Grid voxel cube size. |  |
|  | *MESHTOVOLUMESETTINGS_BANDWIDTH_INTERIOR* | int | Voxel bandwidth amount around the mesh interior. |  |
|  | *MESHTOVOLUMESETTINGS_BANDWIDTH_EXTERIOR* | int | Voxel bandwidth amount around the mesh exterior. |  |
|  | *MESHTOVOLUMESETTINGS_USE_POINTS* | bool | Use the vertices of the Mesh as particles for SDF construction. |  |
|  | *MESHTOVOLUMESETTINGS_RADIUS* | float | Radius for particle SDF construction if *MESHTOVOLUMESETTINGS_USE_POINTS* is **True**. |  |
| *VOLUMECOMMANDTYPE_VOLUMEBOOLE* |  |  |  |  |
|  | *BOOLESETTINGS_NONE* |  | None. |  |
|  | *BOOLESETTINGS_BOOLETYPE* | int | Boole type: |  |
|  |  |  | *BOOLTYPE_NONE* | None. |
|  |  |  | *BOOLTYPE_UNION* | Union. |
|  |  |  | *BOOLTYPE_DIFF* | Difference. |
|  |  |  | *BOOLTYPE_INTERSECT* | Intersection. |
| *VOLUMECOMMANDTYPE_PARTICLESTOVOLUME* |  |  |  |  |
|  | *PARTICLESTOVOLUMESETTINGS_NONE* |  | None. |  |
|  | *PARTICLESTOVOLUMESETTINGS_GRIDSIZE* | float | Grid voxel cube size. |  |
|  | *PARTICLESTOVOLUMESETTINGS_BANDWIDTH* | int | Voxel Bandwidth amount around a particle. |  |
|  | *PARTICLESTOVOLUMESETTINGS_RADIUS* | float | Radius of the SDF around a particle. |  |
|  | *PARTICLESTOVOLUMESETTINGS_VELOCITY_SCALE* | float | Velocity expansion scale. |  |
|  | *PARTICLESTOVOLUMESETTINGS_USE_PARTICLE_SIZE* | bool | If **True** it overrides the radius with the particle size. |  |
| *VOLUMECOMMANDTYPE_SPLINETOVOLUME* |  |  |  |  |
|  | *SPLINETOVOLUMESETTINGS_NONE* |  | None. |  |
|  | *SPLINETOVOLUMESETTINGS_GRIDSIZE* | float | Grid voxel cube size. |  |
|  | *SPLINETOVOLUMESETTINGS_BANDWIDTH* | int | Voxel bandwidth amount around the spline. |  |
|  | *SPLINETOVOLUMESETTINGS_RADIUS* | float | Radius of the SDF around the spline. |  |
|  | *SPLINETOVOLUMESETTINGS_DENSITY* | float | Sampling density on the spline. |  |
| *VOLUMECOMMANDTYPE_FILTER* |  |  |  |  |
|  | *FILTERSETTINGS_NONE* |  | None. |  |
|  | *FILTERSETTINGS_FILTERTYPE* | int | Filter type. |  |
|  | *FILTERSETTINGS_ITERATIONS* | int | Amount of iterations the filter is applied. |  |
|  | *FILTERSETTINGS_RADIUS* | int | Radius of the filter mask. |  |
|  | *FILTERSETTINGS_OFFSET* | float | Offset value for the offset filter. |  |
|  | *FILTERSETTINGS_FALLOFF* | PyCObject | Pointer to a falloff object maxon.BaseArray. Not supported. |  |
|  | *FILTERSETTINGS_REMAP_OLD_MIN* | float | Old minimum value for linear value remapping. |  |
|  | *FILTERSETTINGS_REMAP_OLD_MAX* | float | Old maximum value for linear value remapping. |  |
|  | *FILTERSETTINGS_REMAP_NEW_MIN* | float | New minimum value for linear value remapping. |  |
|  | *FILTERSETTINGS_REMAP_NEW_MAX* | float | New maximum value for linear value remapping. |  |
|  | *FILTERSETTINGS_STRENGTH* | float | Strength of the filter. |  |
|  | *FILTERSETTINGS_SPLINE* | PyCObject | Pointer to the spline for spline remapping. Not supported. |  |
| *VOLUMECOMMANDTYPE_SDFFILTER* |  |  |  |  |
|  | *SDFFILTERSETTINGS_NONE* |  | None. |  |
|  | *SDFFILTERSETTINGS_FILTERTYPE* | int | Filter type. |  |
|  | *SDFFILTERSETTINGS_ITERATIONS* | int | Amount of iterations that the filter is applied. |  |
|  | *SDFFILTERSETTINGS_STENCILWIDTH* | int | Voxel distance of the filter stencil. |  |
|  | *SDFFILTERSETTINGS_FILTERACCURACY* | int | Filter accuracy type. |  |
|  | *SDFFILTERSETTINGS_OFFSET* | float | Offset value for the dilate, erode and offset filter. |  |
|  | *SDFFILTERSETTINGS_HALFWIDTH* | int | Target half width of the resize filter. |  |
|  | *SDFFILTERSETTINGS_FALLOFF* | PyCObject | Pointer to a falloff object maxon.BaseArray. |  |
|  | *SDFFILTERSETTINGS_STRENGTH* | float | Strength of the filter. |  |
| *VOLUMECOMMANDTYPE_SDFTOFOG* |  |  |  |  |
|  | *SDFTOFOGSETTINGS_NONE* |  | None. |  |
|  | *SDFTOFOGSETTINGS_FALLOFFCUTOFF* | float | Distance for the falloff from the surface. |  |
| *VOLUMECOMMANDTYPE_FOGTOSDF* |  |  |  |  |
|  | *FOGTOSDFSETTINGS_NONE* |  | None. |  |
|  | *FOGTOSDFSETTINGS_ISO* | float | Iso value to extract the SDF at. |  |
| *VOLUMECOMMANDTYPE_RESAMPLE* |  |  |  |  |
|  | *RESAMPLESETTINGS_NONE* |  | None. |  |
|  | *RESAMPLESETTINGS_GRIDSIZE* | float | New grid voxel cube size. |  |
|  | *RESAMPLESETTINGS_INTERPOLATIONTYPE* | int | Interpolation type: |  |
|  |  |  | *RESAMPLEINTERPOLATIONTYPE_NONE* | None. |
|  |  |  | *RESAMPLEINTERPOLATIONTYPE_NEAREST* | Nearest. |
|  |  |  | *RESAMPLEINTERPOLATIONTYPE_LINEAR* | Linear. |
|  |  |  | *RESAMPLEINTERPOLATIONTYPE_QUADRATIC* | Quadratic. |
| *VOLUMECOMMANDTYPE_MIX* |  |  |  |  |
|  | *MIXSETTINGS_NONE* |  | None. |  |
|  | *MIXSETTINGS_MIXTYPE* | int | Mix type: |  |
|  |  |  | *MIXTYPE_NONE* | None. |
|  |  |  | *MIXTYPE_NORMAL* | Normal. |
|  |  |  | *MIXTYPE_MAX* | Maximum. |
|  |  |  | *MIXTYPE_MIN* | Minimum. |
|  |  |  | *MIXTYPE_ADD* | Addition. |
|  |  |  | *MIXTYPE_SUBTRACT* | Substract. |
|  |  |  | *MIXTYPE_MULTIPLY* | Multiply. |
|  |  |  | *MIXTYPE_DIVIDE* | Division. |
| *VOLUMECOMMANDTYPE_FIELDTOVOLUME* |  |  |  |  |
|  | *FIELDTOVOLUMESETTINGS_NONE* |  | None. |  |
|  | *FIELDTOVOLUMESETTINGS_BOUNDINGBOXMIN* | vector | Lower left point of the bounding box. |  |
|  | *FIELDTOVOLUMESETTINGS_BOUNDINGBOXMAX* | vector | Upper right point of the bounding box. |  |
|  | *FIELDTOVOLUMESETTINGS_GRIDSIZE* | float | Grid voxel cube size. |  |
| *VOLUMECOMMANDTYPE_CREATESPHEREVOLUME* |  |  |  |  |
|  | *CREATESPHEREVOLUMESETTINGS_NONE* |  | None. |  |
|  | *CREATESPHEREVOLUMESETTINGS_RADIUS* | float | Radius of the sphere. |  |
|  | *CREATESPHEREVOLUMESETTINGS_POSITION* | vector | World position of the sphere. |  |
|  | *CREATESPHEREVOLUMESETTINGS_BANDWIDTH* | int | Voxel bandwidth amount around the sphere. |  |
|  | *CREATESPHEREVOLUMESETTINGS_GRIDSIZE* | float | Grid voxel cube size. |  |
| *VOLUMECOMMANDTYPE_CREATEPLATONICVOLUME* |  |  |  |  |
|  | *CREATEPLATONICVOLUMESETTINGS_NONE* |  | None. |  |
|  | *CREATEPLATONICVOLUMESETTINGS_FACES* | int | Amount of faces of the platonic i.e. Tetrahedron = *4*, Cube = *6*, Octahedron = *8*. |  |
|  | *CREATEPLATONICVOLUMESETTINGS_SIZE* | float | Size of the platonic. |  |
|  | *CREATEPLATONICVOLUMESETTINGS_POSITION* | vector | World position of the platonic. |  |
|  | *CREATEPLATONICVOLUMESETTINGS_BANDWIDTH* | int | Voxel Bandwidth amount around the platonic. |  |
|  | *CREATEPLATONICVOLUMESETTINGS_GRIDSIZE* | float | Grid voxel cube size. |  |
