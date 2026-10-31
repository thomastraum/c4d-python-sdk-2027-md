<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/RangeData/index.html -->

# c4d.RangeData <a id="c4d-rangedata"></a>

## *class* `c4d.RangeData` <a id="c4d.RangeData"></a>

Range data type (*CUSTOMDATATYPE_RANGE*) for [`RangeCustomGui`](../../../c4d.gui/BaseCustomGui/RangeCustomGui/index.md#c4d.gui.RangeCustomGui).

*New in version R19.*

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Color Modes**

- [`RangeData.IsPerRangeColorMode()`](#c4d.RangeData.IsPerRangeColorMode): Checks if the color mode is stored per range, or just as single color.
- [`RangeData.IsRandomColorMode()`](#c4d.RangeData.IsRandomColorMode): Checks if the colors are randomized or user defined.
- [`RangeData.SetColorMode()`](#c4d.RangeData.SetColorMode): Sets the mode indicating if the color need to be stored per range, or just as single color.
- [`RangeData.SetRandomColorMode()`](#c4d.RangeData.SetRandomColorMode): Sets the random color mode.

**Initialization And Copying**

- [`RangeData.CopyTo()`](#c4d.RangeData.CopyTo): Copies the range data.
- [`RangeData.Init()`](#c4d.RangeData.Init): Initializes the range data with the passed range number.
- [`RangeData.Reset()`](#c4d.RangeData.Reset): Resets the range data to the initial state.

**Knot Values**

- [`RangeData.GetKnotValue()`](#c4d.RangeData.GetKnotValue): Retrieves the value for a knot.
- [`RangeData.SetKnotValue()`](#c4d.RangeData.SetKnotValue): Sets the value for a knot.

**Magic Methods**

- [`RangeData.__init__()`](#c4d.RangeData.__init__): Creates a [`c4d.RangeData`](#c4d.RangeData).

**Range And Knot Structure**

- [`RangeData.DeleteKnot()`](#c4d.RangeData.DeleteKnot): Deletes a knot.
- [`RangeData.GetKnotIndexByValue()`](#c4d.RangeData.GetKnotIndexByValue): Searches for a knot with the specified *value*.
- [`RangeData.GetKnotsCount()`](#c4d.RangeData.GetKnotsCount): Retrieves the numbers of knots.
- [`RangeData.GetRange()`](#c4d.RangeData.GetRange): Retrieves the range at the specified *index*.
- [`RangeData.GetRangeIndex()`](#c4d.RangeData.GetRangeIndex): Returns the range index for the specified *value*.
- [`RangeData.GetRangesCount()`](#c4d.RangeData.GetRangesCount): Retrieves the number of ranges.

**Range Colors**

- [`RangeData.GetRangeColor()`](#c4d.RangeData.GetRangeColor): Retrieves the range color for the specified range *index*.
- [`RangeData.SetRangeColor()`](#c4d.RangeData.SetRangeColor): Sets the range color at the specified range *index*.

**Selection**

- [`RangeData.GetSelectedKnot()`](#c4d.RangeData.GetSelectedKnot): Retrieves the selected knot.
- [`RangeData.GetSelectedRange()`](#c4d.RangeData.GetSelectedRange): Retrieves the selected range.
- [`RangeData.SetSelectedKnot()`](#c4d.RangeData.SetSelectedKnot): Sets the selected knot.
- [`RangeData.SetSelectedRange()`](#c4d.RangeData.SetSelectedRange): Sets the selected range.

**Value Management**

- [`RangeData.AddValue()`](#c4d.RangeData.AddValue): Adds a value and splits existing range.
- [`RangeData.GetCurrentValue()`](#c4d.RangeData.GetCurrentValue): Retrieves the current value.
- [`RangeData.SetCurrentValue()`](#c4d.RangeData.SetCurrentValue): Sets the current value.

## Members <a id="members"></a>

### Color Modes <a id="c4d.RangeData-method-Color-Modes"></a>

#### `RangeData.IsPerRangeColorMode(self)` <a id="c4d.RangeData.IsPerRangeColorMode"></a>

Checks if the color mode is stored per range, or just as single color.

**Return type:** bool

**Returns:** **True** if the color is stored is stored per range, otherwise **False**.

#### `RangeData.IsRandomColorMode(self)` <a id="c4d.RangeData.IsRandomColorMode"></a>

Checks if the colors are randomized or user defined.

**Return type:** bool

**Returns:** **True** if the colors are randomized, otherwise **False**.

#### `RangeData.SetColorMode(self, perRange)` <a id="c4d.RangeData.SetColorMode"></a>

Sets the mode indicating if the color need to be stored per range, or just as single color.

**Parameters:** **perRange** (*bool*) – **True** to store the color per range, **False** to store it just as single color.

#### `RangeData.SetRandomColorMode(self, random)` <a id="c4d.RangeData.SetRandomColorMode"></a>

Sets the random color mode.

**Parameters:** **random** (*bool*) – **True** to randomize colors, otherwise **False**.

### Initialization And Copying <a id="c4d.RangeData-method-Initialization-And-Copying"></a>

#### `RangeData.CopyTo(self, dest)` <a id="c4d.RangeData.CopyTo"></a>

Copies the range data.

**Parameters:** **dest** ([*c4d.RangeData*](#c4d.RangeData)) – The destination range data.

#### `RangeData.Init(self, rangeNumber)` <a id="c4d.RangeData.Init"></a>

Initializes the range data with the passed range number.

> **Note:** The interval in between ranges will be the same.

**Parameters:** **rangeNumber** (*int*) – The number of ranges.

#### `RangeData.Reset(self, invalidateObject=False)` <a id="c4d.RangeData.Reset"></a>

Resets the range data to the initial state.

**Parameters:** **invalidateObject** (*bool*) – **True** to initialize the ranges after reset operation, otherwise the object will be initialized but functions with one single range.

### Knot Values <a id="c4d.RangeData-method-Knot-Values"></a>

#### `RangeData.GetKnotValue(self, knotIndex)` <a id="c4d.RangeData.GetKnotValue"></a>

Retrieves the value for a knot.

**Parameters:** **knotIndex** (*int*) – The knot index to get the value.

**Return type:** float

**Returns:** The knot value.

#### `RangeData.SetKnotValue(self, knotIndex, value)` <a id="c4d.RangeData.SetKnotValue"></a>

Sets the value for a knot.

**Parameters:**

- **knotIndex** (*int*) – The knot index to set the value.
- **value** (*float*) – The value to set.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

### Magic Methods <a id="c4d.RangeData-method-Magic-Methods"></a>

#### `RangeData.__init__(self, v)` <a id="c4d.RangeData.__init__"></a>

Creates a [`c4d.RangeData`](#c4d.RangeData).

**Parameters:** **v** ([*c4d.RangeData*](#c4d.RangeData)) – An optional [`c4d.RangeData`](#c4d.RangeData) to copy.

### Range And Knot Structure <a id="c4d.RangeData-method-Range-And-Knot-Structure"></a>

#### `RangeData.DeleteKnot(self, knotIndex)` <a id="c4d.RangeData.DeleteKnot"></a>

Deletes a knot.

**Parameters:** **knotIndex** (*int*) – The index of the knot to delete.

#### `RangeData.GetKnotIndexByValue(self, value)` <a id="c4d.RangeData.GetKnotIndexByValue"></a>

Searches for a knot with the specified *value*.

**Parameters:** **value** (*float*) – The value used to search for.

**Return type:** int

**Returns:** The knot index, or **NOTOK**/**-1** if not found.

#### `RangeData.GetKnotsCount(self)` <a id="c4d.RangeData.GetKnotsCount"></a>

Retrieves the numbers of knots.

**Return type:** int

**Returns:** The knots count.

#### `RangeData.GetRange(self, index)` <a id="c4d.RangeData.GetRange"></a>

Retrieves the range at the specified *index*.

**Parameters:** **index** (*int*) – The range index.

**Return type:** Tuple[float, float]

**Returns:** The range minimum and maximum values. *(0, 0)* if the function failed.

#### `RangeData.GetRangeIndex(self, value)` <a id="c4d.RangeData.GetRangeIndex"></a>

Returns the range index for the specified *value*.

**Parameters:** **value** (*float*) – The value, must be in the range *[0.0, 1.0]*.

**Return type:** int

**Returns:** The range index. *0* if the function failed

#### `RangeData.GetRangesCount(self)` <a id="c4d.RangeData.GetRangesCount"></a>

Retrieves the number of ranges.

**Return type:** int

**Returns:** The ranges count.

### Range Colors <a id="c4d.RangeData-method-Range-Colors"></a>

#### `RangeData.GetRangeColor(self, index)` <a id="c4d.RangeData.GetRangeColor"></a>

Retrieves the range color for the specified range *index*.

**Parameters:** **index** (*int*) – The index of the range to get the color.

**Return type:** [c4d.Vector](../../Vector/index.md#c4d.Vector)

**Returns:** The range color, or a default [`c4d.Vector()`](../../Vector/index.md#c4d.Vector) if the function failed.

#### `RangeData.SetRangeColor(self, index, color)` <a id="c4d.RangeData.SetRangeColor"></a>

Sets the range color at the specified range *index*.

> **Note:** If [`IsPerRangeColorMode()`](#c4d.RangeData.IsPerRangeColorMode) returns **False**, the range *index* is not evaluated and the color is stored at the first index.

**Parameters:**

- **index** (*int*) – The index of the range to set the color.
- **color** ([*c4d.Vector*](../../Vector/index.md#c4d.Vector)) – The color to be assigned to the range.

### Selection <a id="c4d.RangeData-method-Selection"></a>

#### `RangeData.GetSelectedKnot(self)` <a id="c4d.RangeData.GetSelectedKnot"></a>

Retrieves the selected knot.

**Return type:** int

**Returns:** The selected knot index, or **NOTOK**/**-1** if not found.

#### `RangeData.GetSelectedRange(self)` <a id="c4d.RangeData.GetSelectedRange"></a>

Retrieves the selected range.

**Return type:** int

**Returns:** The selected range index, or **NOTOK**/**-1** if not found.

#### `RangeData.SetSelectedKnot(self, knotIndex)` <a id="c4d.RangeData.SetSelectedKnot"></a>

Sets the selected knot.

**Parameters:** **knotIndex** (*int*) – The index to select, or **NOTOK**/**-1** to deselect all.

#### `RangeData.SetSelectedRange(self, rangeIndex)` <a id="c4d.RangeData.SetSelectedRange"></a>

Sets the selected range.

**Parameters:** **rangeIndex** (*int*) – The range index to select, or **NOTOK**/**-1** to deselect all.

### Value Management <a id="c4d.RangeData-method-Value-Management"></a>

#### `RangeData.AddValue(self, value)` <a id="c4d.RangeData.AddValue"></a>

Adds a value and splits existing range.

**Parameters:** **value** (*float*) – The value to add.

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**.

#### `RangeData.GetCurrentValue(self)` <a id="c4d.RangeData.GetCurrentValue"></a>

Retrieves the current value.

**Return type:** float

**Returns:** the current value.

#### `RangeData.SetCurrentValue(self, value)` <a id="c4d.RangeData.SetCurrentValue"></a>

Sets the current value.

**Parameters:** **value** (*float*) – The value, must be in the range *[0.0, 1.0]*.
