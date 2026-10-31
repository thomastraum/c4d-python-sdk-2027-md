<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/consts/HDIRTYFLAGS.html -->

# HDIRTYFLAGS <a id="hdirtyflags"></a>

Expresses hierarchical or branching dirty state categories for a scene element. These states propagate from the changed scene element to its parent elements and branch owners.

|   |   |
|---|---|
| *HDIRTYFLAGS_NONE* | Signals no state. |
| *HDIRTYFLAGS_ANIMATION* | Signals that animation data in a hierarchy has changed. |
| *HDIRTYFLAGS_OBJECT* | Signals that object data in a hierarchy has changed. |
| *HDIRTYFLAGS_OBJECT_MATRIX* | Signals that an object matrix in a hierarchy has changed. |
| *HDIRTYFLAGS_OBJECT_HIERARCHY* | Signals that an object hierarchy in a hierarchy has changed. |
| *HDIRTYFLAGS_TAG* | Signals that tag data in a hierachy has changed. |
| *HDIRTYFLAGS_MATERIAL* | Signals that material data in a hierachy has changed. |
| *HDIRTYFLAGS_SHADER* | Signals that shader data in a hierachy has changed. |
| *HDIRTYFLAGS_RENDERSETTINGS* | Signals that render settings in a hierachy have changed. |
| *HDIRTYFLAGS_VP* | Signals that a video post effect in a hierachy has changed. |
| *HDIRTYFLAGS_FILTER* | Signals that a filter in a hierachy has changed. |
| *HDIRTYFLAGS_NBITS* | Signals that bit flags in a hierachy have changed. |
| *HDIRTYFLAGS_ALL* | Signals all states. |
