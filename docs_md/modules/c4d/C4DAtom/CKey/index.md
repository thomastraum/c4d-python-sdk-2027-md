<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/C4DAtom/CKey/index.html -->

# c4d.CKey <a id="c4d-ckey"></a>

## *class* `c4d.CKey` <a id="c4d.CKey"></a>

Represents a key in the curve of a track which represent the animation of a parameter.  
Tangents are only guaranteed to be available for tracks of category `CTRACK_CATEGORY_VALUE`. Tracks of the categories `CTRACK_CATEGORY_DATA` and `CTRACK_CATEGORY_PLUGIN` may contain tangent data or not. E.g., a `BaseTime` track will provide tangents for its keys, while a PLA track will not. Such tracks which do not provide tangent data will however not raise an error on attempting to retrieve a tangent for a key, but instead return the null-vector `(0, 0, 0)`.

Parent Class:

- [`c4d.GeListNode`](../GeListNode/index.md#c4d.GeListNode)

## Overview <a id="overview"></a>

**Curve And Track**

- [`CKey.GetCurve()`](#c4d.CKey.GetCurve): Gets the curve of the key.
- [`CKey.GetTrack()`](#c4d.CKey.GetTrack): Gets the track of the key.

**Data Management**

- [`CKey.FlushData()`](#c4d.CKey.FlushData): Flushes the data of the key.
- [`CKey.GetClone()`](#c4d.CKey.GetClone): Gets a clone of the key.
- [`CKey.GetGeData()`](#c4d.CKey.GetGeData): Gets the data of the key.
- [`CKey.SetGeData()`](#c4d.CKey.SetGeData): Sets the data of the key.

**Interpolation**

- [`CKey.GetInterpolation()`](#c4d.CKey.GetInterpolation): Returns the interpolation type of the key.
- [`CKey.GetQuatInterpolation()`](#c4d.CKey.GetQuatInterpolation): Gets the quaternion interpolation type of the key.
- [`CKey.SetInterpolation()`](#c4d.CKey.SetInterpolation): Sets the interpolation type of the key.
- [`CKey.SetQuatInterpolation()`](#c4d.CKey.SetQuatInterpolation): Sets the quaternion interpolation type of the key.

**Key Timing**

- [`CKey.GetTime()`](#c4d.CKey.GetTime): Gets the time of the key.
- [`CKey.GetTimeLeft()`](#c4d.CKey.GetTimeLeft): Gets the time component of the left tangent of the key.
- [`CKey.GetTimeRight()`](#c4d.CKey.GetTimeRight): Gets the time component of the right tangent of the key.
- [`CKey.SetTime()`](#c4d.CKey.SetTime): Sets the time of the key.
- [`CKey.SetTimeLeft()`](#c4d.CKey.SetTimeLeft): Sets the time component of the left tangent of the key.
- [`CKey.SetTimeLeftAdjustValue()`](#c4d.CKey.SetTimeLeftAdjustValue): Sets Time Left and adjusts Value so the angle stays the same.
- [`CKey.SetTimeRight()`](#c4d.CKey.SetTimeRight): Sets the time component of the right tangent of the key.
- [`CKey.SetTimeRightAdjustValue()`](#c4d.CKey.SetTimeRightAdjustValue): Sets Time Right and adjusts Value so the angle stays the same.

**Key Values**

- [`CKey.GetValue()`](#c4d.CKey.GetValue): Gets the value of the key.
- [`CKey.GetValueLeft()`](#c4d.CKey.GetValueLeft): Gets the value component of the left tangent of the key.
- [`CKey.GetValueRight()`](#c4d.CKey.GetValueRight): Gets the value component of the right tangent of the key.
- [`CKey.SetValue()`](#c4d.CKey.SetValue): Sets the value of the key.
- [`CKey.SetValueLeft()`](#c4d.CKey.SetValueLeft): Sets the value component of the left tangent of the key.
- [`CKey.SetValueRight()`](#c4d.CKey.SetValueRight): Sets the value component of the right tangent of the key.

**Tangent Modes**

- [`CKey.GetAutomaticTangentMode()`](#c4d.CKey.GetAutomaticTangentMode): Gets the AutoTangent mode of the key.
- [`CKey.SetAutomaticTangentMode()`](#c4d.CKey.SetAutomaticTangentMode): Sets the AutoTangent mode of the key.

## Members <a id="members"></a>

### Curve And Track <a id="c4d.CKey-method-Curve-And-Track"></a>

#### `CKey.GetCurve(self)` <a id="c4d.CKey.GetCurve"></a>

Gets the curve of the key.

**Return type:** [c4d.CCurve](../GeListNode/BaseList2D/CCurve/index.md#c4d.CCurve)

**Returns:** The curve.

#### `CKey.GetTrack(self)` <a id="c4d.CKey.GetTrack"></a>

Gets the track of the key.

**Return type:** [c4d.CTrack](../GeListNode/BaseList2D/CTrack/index.md#c4d.CTrack)

**Returns:** The track.

### Data Management <a id="c4d.CKey-method-Data-Management"></a>

#### `CKey.FlushData(self)` <a id="c4d.CKey.FlushData"></a>

Flushes the data of the key.

#### `CKey.GetClone(self, trans=None)` <a id="c4d.CKey.GetClone"></a>

Gets a clone of the key.

**Parameters:** **trans** (*Optional*[[*c4d.AliasTrans*](../../AliasTrans/index.md#c4d.AliasTrans)]) –

*New in version R17.032:* An optional alias translator for the operation.

**Return type:** [c4d.CKey](#c4d.CKey)

**Returns:** The cloned key.

#### `CKey.GetGeData(self)` <a id="c4d.CKey.GetGeData"></a>

Gets the data of the key.  
Used to read keys of tracks that are of category `CTRACK_CATEGORY_DATA`. This usually does apply to tracks that neither store `DTYPE_REAL` and `DTYPE_LONG` data, those data types must be read with `CKey.GetValue()`. An exception to that rule are tracks for data types that are composed out of `float` values, like for example [`c4d.Vector`](../../Vector/index.md#c4d.Vector) or [`c4d.Matrix`](../../Matrix/index.md#c4d.Matrix). Here the type is being decomposed into multiple tracks of floating point values. E.g., for a vector into its three or four components and for a matrix first into its vectors and then each vector into its components. Call `CTrack.GetTrackCategory()` to determine the category of a track and therefore the method which has to be used to read data from its keys. See the example below for how to read complex data out of a key. The compilation of the returned [`c4d.BaseContainer`](../../BaseContainer/index.md#c4d.BaseContainer) depends on the described data type. See [`c4d.CustomDataType`](../../CustomDataType/index.md#c4d.CustomDataType) for an overview of the custom data types exposed to Python.

```python
# This is a PLA track, we get its curve and iterate over all keys.
if ctrack.IsInstanceOf(c4d.CTpla):
    curve =  ctrack.GetCurve(c4d.CCURVE_CURVE)

    for i in range(curve.GetKeyCount()):
        ckey = curve.GetKey(i)
        # We retrieve the key data with GetGeData which usually returns
        # a BaseContainer().
        data = ckey.GetGeData()
        if not isinstance(data, c4d.BaseContainer):
            RuntimeError("Failed to retrieve PLA data.")

        print (data[c4d.CK_PLA_DATA])
```

> **See also:** To read keys of tracks of the category `CTRACK_CATEGORY_VALUE`, use `CKey.GetValue()`.

**Return type:** Any

**Returns:** The data, depends on the key.

#### `CKey.SetGeData(self, seq, d)` <a id="c4d.CKey.SetGeData"></a>

Sets the data of the key.  
Used to write keys of tracks that are of category `CTRACK_CATEGORY_DATA`. This usually does apply to tracks that neither store `DTYPE_REAL` and `DTYPE_LONG` data, and those data types must be written with `CKey.SetValue()`. An exception to that rule are tracks for data types that are composed out of `float` values, like for example [`c4d.Vector`](../../Vector/index.md#c4d.Vector) or [`c4d.Matrix`](../../Matrix/index.md#c4d.Matrix). Here the type is being decomposed into multiple tracks of floating point values. E.g., for a vector into its three or four components and for a matrix first into its vectors and then each vector into its components. Call `CTrack.GetTrackCategory()` to determine the category of a track and therefore the method which has to be used to write data into its keys. See the example below for how to write a boolean key value with this method.

```python
# Get the first material of the document and its first track.
mat = doc.GetFirstMaterial()
if mat is None:
    raise RuntimeError("No material found.")
track = mat.GetFirstCTrack()
if track is None:
    raise RuntimeError("Material has no tracks.")

# Bail when this first track is not for the boolean "use color" parameter 
# of the material.
if track.GetDescriptionID()[0].id != c4d.MATERIAL_USE_COLOR:
    raise RuntimeError("'Use-Color' track not found")

# Get the curve of the track and its first key. 
curve = track.GetCurve(c4d.CCURVE_CURVE)
if curve.GetKeyCount() < 1:
    raise RuntimeError("Curve has no keys.")
key = curve.GetKey(0)

# Print the current value of the boolean key and then set it to `True`.
print (key.GetGeData())
key.SetGeData(curve, True)

# Push an update event to Cinema 4D.
c4d.EventAdd()
```

> **See also:** To write keys of tracks of the category `CTRACK_CATEGORY_VALUE`, use `CKey.SetValue()`.

**Parameters:**

- **seq** ([*c4d.CCurve*](../GeListNode/BaseList2D/CCurve/index.md#c4d.CCurve)) – The curve.
- **d** (*any*) – The data.

### Interpolation <a id="c4d.CKey-method-Interpolation"></a>

#### `CKey.GetInterpolation(self)` <a id="c4d.CKey.GetInterpolation"></a>

Returns the interpolation type of the key.

**Return type:** int

**Returns:**

The interpolation type:

|   |   |
|---|---|
| *CINTERPOLATION_SPLINE* | Spline. |
| *CINTERPOLATION_LINEAR* | Linear |
| *CINTERPOLATION_STEP* | Step. |

#### `CKey.GetQuatInterpolation(self)` <a id="c4d.CKey.GetQuatInterpolation"></a>

Gets the quaternion interpolation type of the key.

*New in version R18.020.*

**Return type:** int

**Returns:**

The quaternion interpolation type:

|   |   |
|---|---|
| *ROTATIONINTERPOLATION_QUATERNION_SLERP* | Quaternion Spherical LERP Interpolation (Linear). |
| *ROTATIONINTERPOLATION_QUATERNION_CUBIC* | Quaternion Smooth Cubic Interpolation (Formerly known as Losch). |

#### `CKey.SetInterpolation(self, seq, inter)` <a id="c4d.CKey.SetInterpolation"></a>

Sets the interpolation type of the key.

**Parameters:**

- **seq** ([*c4d.CCurve*](../GeListNode/BaseList2D/CCurve/index.md#c4d.CCurve)) – The curve.

- **int** –

  The new interpolation type:

  |   |   |
  |---|---|
  | *CINTERPOLATION_SPLINE* | Spline. |
  | *CINTERPOLATION_LINEAR* | Linear |
  | *CINTERPOLATION_STEP* | Step. |

#### `CKey.SetQuatInterpolation(self, seq, inter, bUndo=True)` <a id="c4d.CKey.SetQuatInterpolation"></a>

Sets the quaternion interpolation type of the key.

*New in version R18.020.*

> **Note:** Keys at the same time on other component curve will be modified.

**Parameters:**

- **seq** ([*c4d.CCurve*](../GeListNode/BaseList2D/CCurve/index.md#c4d.CCurve)) – The curve the key belongs to.

- **inter** (*int*) –

  The quaternion interpolation type to set:

  |   |   |
  |---|---|
  | *ROTATIONINTERPOLATION_QUATERNION_SLERP* | Quaternion Spherical LERP Interpolation (Linear). |
  | *ROTATIONINTERPOLATION_QUATERNION_CUBIC* | Quaternion Smooth Cubic Interpolation (Formerly known as Losch). |

- **bUndo** (*bool*) –

  **True** to add the 3 rotation keys in the undo system.  
  The caller has to to manage start/end of undo actions with `BaseDocument.StartUndo()`/`EndUndo()`.

### Key Timing <a id="c4d.CKey-method-Key-Timing"></a>

#### `CKey.GetTime(self)` <a id="c4d.CKey.GetTime"></a>

Gets the time of the key.

**Return type:** [c4d.BaseTime](../../BaseTime/index.md#c4d.BaseTime)

**Returns:** The time.

#### `CKey.GetTimeLeft(self)` <a id="c4d.CKey.GetTimeLeft"></a>

Gets the time component of the left tangent of the key.  
See class description for details on the availability of tangents.

**Return type:** [c4d.BaseTime](../../BaseTime/index.md#c4d.BaseTime)

**Returns:** The left time.

#### `CKey.GetTimeRight(self)` <a id="c4d.CKey.GetTimeRight"></a>

Gets the time component of the right tangent of the key.  
See class description for details on the availability of tangents.

**Return type:** [c4d.BaseTime](../../BaseTime/index.md#c4d.BaseTime)

**Returns:** The right time.

#### `CKey.SetTime(self, seq, t)` <a id="c4d.CKey.SetTime"></a>

Sets the time of the key.

**Parameters:**

- **seq** ([*c4d.CCurve*](../GeListNode/BaseList2D/CCurve/index.md#c4d.CCurve)) – The curve.
- **t** ([*c4d.BaseTime*](../../BaseTime/index.md#c4d.BaseTime)) – The new time.

#### `CKey.SetTimeLeft(self, seq, t)` <a id="c4d.CKey.SetTimeLeft"></a>

Sets the time component of the left tangent of the key.  
See class description for details on the availability of tangents.

**Parameters:**

- **seq** ([*c4d.CCurve*](../GeListNode/BaseList2D/CCurve/index.md#c4d.CCurve)) – The curve.
- **t** ([*c4d.BaseTime*](../../BaseTime/index.md#c4d.BaseTime)) – The time.

#### `CKey.SetTimeLeftAdjustValue(self, seq, t)` <a id="c4d.CKey.SetTimeLeftAdjustValue"></a>

Sets Time Left and adjusts Value so the angle stays the same.

*New in version R17.048.*

**Parameters:**

- **seq** ([*c4d.CCurve*](../GeListNode/BaseList2D/CCurve/index.md#c4d.CCurve)) – The curve the key belongs to.
- **t** ([*c4d.BaseTime*](../../BaseTime/index.md#c4d.BaseTime)) – The Time Left to set.

**Return type:** bool

**Returns:** **True** if successful. **False** if current Time Left is smaller than **FLT_MIN** and Value is not Zero (angle cannot stay the same).

#### `CKey.SetTimeRight(self, seq, t)` <a id="c4d.CKey.SetTimeRight"></a>

Sets the time component of the right tangent of the key.  
See class description for details on the availability of tangents.

**Parameters:**

- **seq** ([*c4d.CCurve*](../GeListNode/BaseList2D/CCurve/index.md#c4d.CCurve)) – The curve.
- **t** ([*c4d.BaseTime*](../../BaseTime/index.md#c4d.BaseTime)) – The time.

#### `CKey.SetTimeRightAdjustValue(self, seq, t)` <a id="c4d.CKey.SetTimeRightAdjustValue"></a>

Sets Time Right and adjusts Value so the angle stays the same.

*New in version R17.048.*

**Parameters:**

- **seq** ([*c4d.CCurve*](../GeListNode/BaseList2D/CCurve/index.md#c4d.CCurve)) – The curve the key belongs to.
- **t** ([*c4d.BaseTime*](../../BaseTime/index.md#c4d.BaseTime)) – The Time Right to set.

**Return type:** bool

**Returns:** **True** if successful. **False** if current Time Right is smaller than **FLT_MIN** and Value is not Zero (angle cannot stay the same).

### Key Values <a id="c4d.CKey-method-Key-Values"></a>

#### `CKey.GetValue(self)` <a id="c4d.CKey.GetValue"></a>

Gets the value of the key.  
Used to read keys of tracks that are of category `CTRACK_CATEGORY_VALUE`. This usually only does apply to `DTYPE_REAL` and `DTYPE_LONG` tracks, other data types must be read with `CKey.GetGeData()`. An exception to that rule are tracks for data types that are composed out of `float` values, like for example [`c4d.Vector`](../../Vector/index.md#c4d.Vector) or [`c4d.Matrix`](../../Matrix/index.md#c4d.Matrix). Here the type is being decomposed into multiple tracks of floating point values. E.g., for a vector into its three or four components and for a matrix first into its vectors and then each vector into its components. Call `CTrack.GetTrackCategory()` to determine the category of a track and therefore the method which has to be used to read data from its keys.

> **See also:** To read keys of tracks of the category `CTRACK_CATEGORY_DATA`, including of type `DTYPE_BOOL`, use `CKey.GetGeData()`.

**Return type:** float

**Returns:** The value.

#### `CKey.GetValueLeft(self)` <a id="c4d.CKey.GetValueLeft"></a>

Gets the value component of the left tangent of the key.  
See class description for details on the availability of tangents.

**Return type:** float

**Returns:** The value.

#### `CKey.GetValueRight(self)` <a id="c4d.CKey.GetValueRight"></a>

Gets the value component of the right tangent of the key.  
See class description for details on the availability of tangents.

**Return type:** float

**Returns:** The value.

#### `CKey.SetValue(self, seq, v)` <a id="c4d.CKey.SetValue"></a>

Sets the value of the key.  
Used to write keys of tracks that are of category `CTRACK_CATEGORY_VALUE`. This usually only does apply to `DTYPE_REAL` and `DTYPE_LONG` tracks, other data types must be written with `CKey.SetGeData()`. An exception to that rule are tracks for data types that are composed out of `float` values, like for example [`c4d.Vector`](../../Vector/index.md#c4d.Vector) or [`c4d.Matrix`](../../Matrix/index.md#c4d.Matrix). Here the type is being decomposed into multiple tracks of floating point values. E.g., for a vector into its three or four components and for a matrix first into its vectors and then each vector into its components. Call `CTrack.GetTrackCategory()` to determine the category of a track and therefore the method which has to be used to write data into its keys.

> **See also:** To write keys of tracks of the category `CTRACK_CATEGORY_DATA`, including of type `DTYPE_BOOL`, use `CKey.SetGeData()`.

**Parameters:**

- **seq** ([*c4d.CCurve*](../GeListNode/BaseList2D/CCurve/index.md#c4d.CCurve)) – The curve.
- **v** (*float*) – The new value.

#### `CKey.SetValueLeft(self, seq, v)` <a id="c4d.CKey.SetValueLeft"></a>

Sets the value component of the left tangent of the key.  
See class description for details on the availability of tangents.

**Parameters:**

- **seq** ([*c4d.CCurve*](../GeListNode/BaseList2D/CCurve/index.md#c4d.CCurve)) – The curve.
- **v** (*float*) – The new value.

#### `CKey.SetValueRight(self, seq, v)` <a id="c4d.CKey.SetValueRight"></a>

Sets the value component of the right tangent of the key.  
See class description for details on the availability of tangents.

**Parameters:**

- **seq** ([*c4d.CCurve*](../GeListNode/BaseList2D/CCurve/index.md#c4d.CCurve)) – The curve.
- **v** (*float*) – The new value.

### Tangent Modes <a id="c4d.CKey-method-Tangent-Modes"></a>

#### `CKey.GetAutomaticTangentMode(self)` <a id="c4d.CKey.GetAutomaticTangentMode"></a>

Gets the AutoTangent mode of the key.

*New in version R17.048.*

**Return type:** int

**Returns:**

The AutoTangent mode:

|   |   |
|---|---|
| *CAUTOMODE_CLASSIC* | AutoTangent first implementation. |
| *CAUTOMODE_FIXEDSLOPE* | AutoTangent with fixed slope for given time. |

#### `CKey.SetAutomaticTangentMode(self, seq, autoMode)` <a id="c4d.CKey.SetAutomaticTangentMode"></a>

Sets the AutoTangent mode of the key.

*New in version R17.048.*

**Parameters:**

- **seq** ([*c4d.CCurve*](../GeListNode/BaseList2D/CCurve/index.md#c4d.CCurve)) – The curve the key belongs to.

- **autoMode** (*int*) –

  The AutoTangent mode to set:

  |   |   |
  |---|---|
  | *CAUTOMODE_CLASSIC* | AutoTangent first implementation. |
  | *CAUTOMODE_FIXEDSLOPE* | AutoTangent with fixed slope for given time. |
