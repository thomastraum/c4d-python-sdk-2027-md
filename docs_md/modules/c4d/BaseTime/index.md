<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/BaseTime/index.html -->

# c4d.BaseTime <a id="c4d-basetime"></a>

## *class* `c4d.BaseTime` <a id="c4d.BaseTime"></a>

A BaseTime represents a time value within Cinema 4d.

Here is an example how to use a BaseTime object.

```python
import c4d

bc1 = c4d.BaseTime(5, 10) # reduced to 1/2
bc2 = c4d.BaseTime(5)     # 5/1
bc3 = bc1 / bc2
doc.SetTime(bc3)
```

## Overview <a id="overview"></a>

**Magic Methods**

- [`BaseTime.__add__()`](#c4d.BaseTime.__add__): Add two times and return the result.
- [`BaseTime.__cmp__()`](#c4d.BaseTime.__cmp__): Compare two times with each other.
- [`BaseTime.__div__()`](#c4d.BaseTime.__div__): Divide two times and return the result.
- [`BaseTime.__eq__()`](#c4d.BaseTime.__eq__): Check if two different BaseTime represents the same time.
- [`BaseTime.__ge__()`](#c4d.BaseTime.__ge__): Check if the passed BaseTime is greater or equal than self.
- [`BaseTime.__gt__()`](#c4d.BaseTime.__gt__): Check if the passed BaseTime is greater than self.
- [`BaseTime.__init__()`](#c4d.BaseTime.__init__): Initializes the internal time value from a real value in seconds.
- [`BaseTime.__le__()`](#c4d.BaseTime.__le__): Check if the passed BaseTime is lesser or equal than self.
- [`BaseTime.__lt__()`](#c4d.BaseTime.__lt__): Check if the passed BaseTime is lesser than self.
- [`BaseTime.__mul__()`](#c4d.BaseTime.__mul__): Multiply two times and return the result.
- [`BaseTime.__ne__()`](#c4d.BaseTime.__ne__): Check if two different BaseTime don’t represents the same time.
- [`BaseTime.__sub__()`](#c4d.BaseTime.__sub__): Subtract two times and return the result.

**Rational Components**

- [`BaseTime.GetDenominator()`](#c4d.BaseTime.GetDenominator): Get the denominator part of the internally stored time.
- [`BaseTime.GetNumerator()`](#c4d.BaseTime.GetNumerator): Get the numerator part of the internally stored time.
- [`BaseTime.SetDenominator()`](#c4d.BaseTime.SetDenominator): Get the denominator part of the internally stored time.
- [`BaseTime.SetNumerator()`](#c4d.BaseTime.SetNumerator): Set the numerator part of the internally stored time.

**Time Measurement Operations**

- [`BaseTime.Get()`](#c4d.BaseTime.Get): Return the time in seconds.
- [`BaseTime.GetFrame()`](#c4d.BaseTime.GetFrame): Get the number of frames equivalent to this time for the given number of frames per second.
- [`BaseTime.Quantize()`](#c4d.BaseTime.Quantize): Quantize the internal value so that it is a multiple of the specified framerate.
- [`BaseTime.TimeDif()`](#c4d.BaseTime.TimeDif): Check which is the largest between the time and *t2*.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.BaseTime-method-Magic-Methods"></a>

#### `BaseTime.__add__(self, other)` <a id="c4d.BaseTime.__add__"></a>

Add two times and return the result.

**Parameters:** **other** ([*c4d.BaseTime*](#c4d.BaseTime)) – The other value.

**Return type:** [c4d.BaseTime](#c4d.BaseTime)

**Returns:** The result.

#### `BaseTime.__cmp__(self, other)` <a id="c4d.BaseTime.__cmp__"></a>

Compare two times with each other.

**Parameters:** **other** ([*c4d.BaseTime*](#c4d.BaseTime)) – The time value to compare with.

#### `BaseTime.__div__(self, other)` <a id="c4d.BaseTime.__div__"></a>

Divide two times and return the result.

**Parameters:** **other** ([*c4d.BaseTime*](#c4d.BaseTime)) – The other value.

**Return type:** [c4d.BaseTime](#c4d.BaseTime)

**Returns:** The result.

#### `BaseTime.__eq__(self, other)` <a id="c4d.BaseTime.__eq__"></a>

Check if two different BaseTime represents the same time.

**Parameters:** **other** ([*c4d.BaseTime*](#c4d.BaseTime)) – The time value to compare with.

**Return type:** bool

**Returns:** **True** if the BaseTime are similar, otherwise **False**.

#### `BaseTime.__ge__(self, other)` <a id="c4d.BaseTime.__ge__"></a>

Check if the passed BaseTime is greater or equal than self.

**Parameters:** **other** ([*c4d.BaseTime*](#c4d.BaseTime)) – The other BaseTime.

**Return type:** bool

**Returns:** **True** if other BaseTime is greater or equal than self

#### `BaseTime.__gt__(self, other)` <a id="c4d.BaseTime.__gt__"></a>

Check if the passed BaseTime is greater than self.

**Parameters:** **other** ([*c4d.BaseTime*](#c4d.BaseTime)) – The other BaseTime.

**Return type:** bool

**Returns:** **True** if other BaseTime is greater than self

#### `BaseTime.__init__(self, z=0.0, n=0.0)` <a id="c4d.BaseTime.__init__"></a>

Initializes the internal time value from a real value in seconds.  
This will multiply the seconds by 1000.0 and store it as a fraction with the denominator at 1000.0.

**Parameters:**

- **z** (*int*) – Optional time in seconds.
- **n** (*Union*[*bool*, *int*]) – If *n* is **False**, disable the automatic fraction-reduction and if int, set the denominator.

#### `BaseTime.__le__(self, other)` <a id="c4d.BaseTime.__le__"></a>

Check if the passed BaseTime is lesser or equal than self.

**Parameters:** **other** ([*c4d.BaseTime*](#c4d.BaseTime)) – The other BaseTime.

**Return type:** bool

**Returns:** **True** if other BaseTime is lesser or equal than self

#### `BaseTime.__lt__(self, other)` <a id="c4d.BaseTime.__lt__"></a>

Check if the passed BaseTime is lesser than self.

**Parameters:** **other** ([*c4d.BaseTime*](#c4d.BaseTime)) – The other BaseTime.

**Return type:** bool

**Returns:** **True** if other BaseTime is lesser than self

#### `BaseTime.__mul__(self, other)` <a id="c4d.BaseTime.__mul__"></a>

Multiply two times and return the result.

**Parameters:** **other** ([*c4d.BaseTime*](#c4d.BaseTime)) – The other value.

**Return type:** [c4d.BaseTime](#c4d.BaseTime)

**Returns:** The result.

#### `BaseTime.__ne__(self, other)` <a id="c4d.BaseTime.__ne__"></a>

Check if two different BaseTime don’t represents the same time.

**Return type:** bool

**Returns:** **True** if the BaseTime don’t represent the same time, otherwise **False**.

#### `BaseTime.__sub__(self, other)` <a id="c4d.BaseTime.__sub__"></a>

Subtract two times and return the result.

**Parameters:** **other** ([*c4d.BaseTime*](#c4d.BaseTime)) – The other value.

**Return type:** [c4d.BaseTime](#c4d.BaseTime)

**Returns:** The result.

### Rational Components <a id="c4d.BaseTime-method-Rational-Components"></a>

#### `BaseTime.GetDenominator(self)` <a id="c4d.BaseTime.GetDenominator"></a>

Get the denominator part of the internally stored time.

**Return type:** float

**Returns:** The denominator

#### `BaseTime.GetNumerator(self)` <a id="c4d.BaseTime.GetNumerator"></a>

Get the numerator part of the internally stored time.

**Return type:** float

**Returns:** The numerator.

#### `BaseTime.SetDenominator(self, r)` <a id="c4d.BaseTime.SetDenominator"></a>

Get the denominator part of the internally stored time.

**Parameters:** **r** (*number*) – The denominator.

#### `BaseTime.SetNumerator(self, r)` <a id="c4d.BaseTime.SetNumerator"></a>

Set the numerator part of the internally stored time.

**Parameters:** **r** (*number*) – The numerator.

### Time Measurement Operations <a id="c4d.BaseTime-method-Time-Measurement-Operations"></a>

#### `BaseTime.Get(self)` <a id="c4d.BaseTime.Get"></a>

Return the time in seconds.

**Return type:** float

**Returns:** Time in seconds.

#### `BaseTime.GetFrame(self, fps)` <a id="c4d.BaseTime.GetFrame"></a>

Get the number of frames equivalent to this time for the given number of frames per second.

**Parameters:** **fps** (*int*) – The number of frames for this time.

**Return type:** int

**Returns:** The frames per second to use to calculate the frame number for this time.

#### `BaseTime.Quantize(self, fps)` <a id="c4d.BaseTime.Quantize"></a>

Quantize the internal value so that it is a multiple of the specified framerate.

**Parameters:** **fps** (*number*) – The number of frames per second to make this time a multiple of.

#### `BaseTime.TimeDif(self, t2)` <a id="c4d.BaseTime.TimeDif"></a>

Check which is the largest between the time and *t2*.

**Parameters:** **t2** ([*c4d.BaseTime*](#c4d.BaseTime)) – The time to compare with.

**Return type:** int

**Returns:** *-1* if the time is < *t2*, *0* if they are equal and *1* if the time is > *t2*.
