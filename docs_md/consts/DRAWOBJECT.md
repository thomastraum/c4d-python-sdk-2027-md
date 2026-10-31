<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/DRAWOBJECT.html -->

# DRAWOBJECT <a id="drawobject"></a>

|   |   |
|---|---|
| *DRAWOBJECT_NONE* | None. |
| *DRAWOBJECT_FORCELINES* | Force wireframe display, independent of view settings. |
| *DRAWOBJECT_NOBACKCULL* | Force no backface culling, independent of view settings. |
| *DRAWOBJECT_LOCALMATRIX* | Object will be drawn relative to the currently processed object (used when called from the *Draw()* function in an object. |
| *DRAWOBJECT_EDITMODE* | Object is drawn in edit-mode style. |
| *DRAWOBJECT_FORCEBASE* | The draw call is only executed for the base class, and thus not for the instanciated object, if passed to `BaseDraw.DrawObject()` and the object type is an instance of either *Opoint* or *Opolygon*. This way, a draw call can be invoked from points/polygons derived object without running into a recursion. |
| *DRAWOBJECT_FORCEPOINTS* | Force points display. |
| *DRAWOBJECT_NO_EOGL* | No Extended OpenGL. |
| *DRAWOBJECT_USE_OBJECT_COLOR* | Use the object’s color. |
| *DRAWOBJECT_USE_CUSTOM_COLOR* | Use a custom color. |
| *DRAWOBJECT_XRAY_ON* | Enables X-Ray mode. |
| *DRAWOBJECT_XRAY_OFF* | Disables X-Ray mode. |
| *DRAWOBJECT_IMMEDIATELY* | Draws an object immediately. Usually all objects are collected in a Z-depth sorted list before drawing. This flag is used for objects which are immediately deleted after drawing. |
| *DRAWOBJECT_Z_OFFSET* | Do not change the Z offset. |
| *DRAWOBJECT_PRIVATE_ANY* | Private. |
