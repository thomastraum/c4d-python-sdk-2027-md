<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/VIEWPORTSELECTFLAGS.html -->

# VIEWPORTSELECTFLAGS <a id="viewportselectflags"></a>

|   |   |
|---|---|
| *VIEWPORTSELECTFLAGS_NONE* | None. |
| *VIEWPORTSELECTFLAGS_USE_HN* | Use HyperNURBS. |
| *VIEWPORTSELECTFLAGS_USE_DEFORMERS* | Use deformers. |
| *VIEWPORTSELECTFLAGS_REGION_SELECT* | A rectangle, polygon and lasso selection counts the number of vertices of a polygon within its area. Usually hidden vertices are not taken into account. This flag allows hidden vertices to be taken into account, otherwise it would not be possible to select polygons if for example all points are hidden. |
| *VIEWPORTSELECTFLAGS_IGNORE_HIDDEN_SEL* | Ignore hidden selection. |
| *VIEWPORTSELECTFLAGS_USE_DISPLAY_MODE* | If this flag is set and the display mode is Wireframe or Isoparms only edges and vertices are written into the [`ViewportSelect`](../modules/c4d.utils/ViewportSelect/index.md#c4d.utils.ViewportSelect) buffer. The [`ViewportSelect`](../modules/c4d.utils/ViewportSelect/index.md#c4d.utils.ViewportSelect) mode must be *Mpolyedgepoint*. |
| *VIEWPORTSELECTFLAGS_FORCE_USE_DEFORMERS* | Use deformers even when the viewport *DISPLAYEDITSTATE_DEFORM* is disabled. |
