<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/VIEWPORT_PICK_FLAGS.html -->

# VIEWPORT_PICK_FLAGS <a id="viewport-pick-flags"></a>

| Symbol ID | Description |
|---|---|
| VIEWPORT_PICK_FLAGS_NONE | None. |
| VIEWPORT_PICK_FLAGS_ALLOW_OGL | Allow OpenGL. |
| VIEWPORT_PICK_FLAGS_DONT_STOP_THREADS | Do not stop threads. |
| VIEWPORT_PICK_FLAGS_USE_SEL_FILTER | Use selection filter. |
| VIEWPORT_PICK_FLAGS_OGL_ONLY_TOPMOST | Picks only topmost object. Use this only when the object pointer is not needed. Only works with OpenGL. |
| VIEWPORT_PICK_FLAGS_OGL_ONLY_VISIBLE | Picks only visible. Only works with OpenGL.<br>> > **Note:** Not supported by Python API. |
| VIEWPORT_PICK_FLAGS_OGL_IGNORE_Z | Picks ignore Z position. Set this to only check if an object (and which) was hit, not its Z position. Only works with OpenGL. |
| VIEWPORT_PICK_FLAGS_OGL_ONLY_TOPMOST_WITH_OBJ | Picks only topmost object but returns the topmost object with its Z position. Only works with OpenGL. |
| VIEWPORT_PICK_FLAGS_NO_DEPTH_CORRECTION | To support old tools, the matrix is usually corrected so that the depth can be in the [-1, 1] range. With this option set, this does not happen any more.<br>> *New in version R23.105.* |
