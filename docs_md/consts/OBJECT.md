<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/OBJECT.html -->

# OBJECT <a id="object"></a>

| Symbol ID | Description |
|---|---|
| OBJECT_MODIFIER | Modifier object. Deforms the surrounding object. (E.g. bend.) |
| OBJECT_HIERARCHYMODIFIER | Hierarchical modifier. Deforms the surrounding objects together with other instances in a hierarchy chain. Only the top-most instance of the plugin in a chain is called. (E.g. bones.) |
| OBJECT_GENERATOR | Generator object. Produces a polygonal or spline representation on its own. (E.g. primitive cube.) |
| OBJECT_INPUT | Used in combination with OBJECT_GENERATOR. Specifies that the generator builds a polygon or spline, using its sub-objects as input. (E.g. Sweep Subdivision Surface, Boolean.) |
| OBJECT_PARTICLEMODIFIER | Particle modifier. |
| OBJECT_ISSPLINE | The object is a spline. |
| OBJECT_UNIQUEENUMERATION | Unique enumeration. See :`BaseObject.GetUniqueIP()`. |
| OBJECT_CAMERADEPENDENT | Camera dependent. |
| OBJECT_USECACHECOLOR | If this flag is specified, the generator object itself controls the objects’ colors (the ones that determine the wireframe/shaded color). Normally these are automatically overwritten by the generator objects settings. E.g. if the instance object is set to green, automatically all of its cache objects get the green color. By setting this flag an instance object could individually color objects. |
| OBJECT_POINTOBJECT | Point Object. |
| OBJECT_POLYGONOBJECT | Polygon object. |
| OBJECT_NO_PLA | Objects derived from [`PointObject`](../modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/PointObject/index.md#c4d.PointObject) will not use auto-keyframing (e.g. Joints can contain points and PLA auto-keyframing is not useful for them) |
| OBJECT_DONTFREECACHE | Objects’ (generators) caches will not be be deleted - users must maintain caches themselves. |
| OBJECT_CALL_ADDEXECUTION | Must be set to call `ObjectData.Execute()` in the priority pipeline specified by `ObjectData.AddToExecution()`. |
| OBJECT_NOCHILDEXPRESSIONS | *New in version R20:* Don’t execute expression tags on the children of the object. |
| OBJECT_FIELDOBJECT | *New in version R20:* Field object. Can’t be created in Python. |
| OBJECT_HASDEFORMMODE | *New in version R26:* Object has a deform mode even if it is not one of the standard types with a deform mode. |
| OBJECT_ICONCHOOSER_PARENT_IGNORE | Previously was expressed in the tag as c4d.TAG_ICONCHOOSER_PARENT_IGNORE. |
| OBJECT_CUSTOM_NAME_ADDITION | *New in version 2024.4:* Specify that an object implement MSG_GETCUSTOM_NAME_ADDITION and this message should be called from the Object Manager to retrieve its custom additional name. |
