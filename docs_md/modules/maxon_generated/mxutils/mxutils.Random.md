<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/mxutils/mxutils.Random.html -->

# mxutils.Random <a id="mxutils-random"></a>

## Description <a id="module-mxutils.Random"></a><a id="description"></a>

Generates pseudo-random floating point, integer, vector, color, and matrix values in a deterministic manner.

Offered are two groups of methods: Methods that are prefixed with *Random* generate random values using the *random* module from the Python standard library. The characteristic of this approach is that one does not need any inputs except for an initial seed, the values are picked from a sequence of outputs. The other option are methods that are prefixed with *Hash*, they generate pseudo-random values using a hash function which requires an input value for each call, the to be hashed value.

The advantage of hash functions is that they generate pseudo-random values that are consistent across multiple calls for the same entity, no matter of the order they are made in. Imagine having a list of points and one wants to associate each point with a random float value. Using the *random* module, one would have to reseed the generator with the same seed every time one wants to generate the random values for the same point list. Calling *random.Random.seed* is not only such an expensive call that hashing usually outperforms *random* based random value generation by an order of magnitude, but also cannot be done in a thread safe manner and cannot deal with reordering, increasing, or decreasing of the inputs. Hash functions do not share any of these problems.

> **Note:**
>
> `mxutils.g_random` is a global instance of this class that can be used directly.

> **Note:** Most functions in this class deliberately do not perform type checks on their arguments to ensure a better performance, as they are expected to be called very often. It is the responsibility of the caller to ensure that the passed arguments are of the correct type.

> **Note:** The hash function used in this class is not suitable for cryptographic purposes. It is a simple hash function that exploits the periodicity of the sine function to compute a pseudo-random hash. See the *Hash* method for more information.

**Example:**

```python
import c4d
import mxutils

# Import the global random number generator instance.
from mxutils import g_random

obj: c4d.PointObject # Some point object we are given in code.

# Associate each point with a random float value using RandomFloat. The tuples will be different each time the code
# is run unless we reset the seed before each call (which is a very expensive operation). This is based on the
# random module from the Python standard library.
values: list[tuple[c4d.Vector, float]] = [(p, g_random.RandomFloat()) for p in obj.GetAllPoints()]

# Generate point, random float pairs using a hash function, here hashing the point index. The tuples will be
# the same each time the code is run unless the point order/indices change.
values: list[tuple[c4d.Vector, float]] = [(p, g_random.HashNumberToNumber(i)) for i, p enumerate(in obj.GetAllPoints())]

# And finally generate the tuples using the point values itself. A given point will always be associated with the
# same random float value, no matter the count and order of points in #obj.
values: list[tuple[c4d.Vector, float]] = [(p, g_random.HashVectorToNumber(p)) for p in obj.GetAllPoints()]
```

## Inheritance diagram <a id="inheritance-diagram"></a>

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`mxutils.Random.Magic`](mxutils.Random.Magic.md#mxutils.Random.Magic) | Gets or sets the magic numbers used by the hash function. |
| [`mxutils.Random.Random`](mxutils.Random.Random.md#mxutils.Random.Random) | Returns the internal Python *random.Random* instance. |
| [`mxutils.Random.Seed`](mxutils.Random.Seed.md#mxutils.Random.Seed) | Gets or sets the seed of the instance used by both the pseudo-random number generator and the hash function. |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`Hash`](#mxutils.Random.Hash)(value) | Returns a pseudo-random hash in the interval *[-1, 1]* for the passed numeric value. |
| [`HashNumberToColor`](#mxutils.Random.HashNumberToColor)(value[, hueInterval, …]) | Returns a pseudo-random color hash for the passed numeric value. |
| [`HashNumberToMatrix`](#mxutils.Random.HashNumberToMatrix)(value[, …]) | Returns a pseudo-random transform matrix hash for the passed numeric value. |
| [`HashNumberToNumber`](#mxutils.Random.HashNumberToNumber)(value) | Returns a pseudo-random float in the interval *[0, 1]* for the passed numeric value. |
| [`HashNumberToVector`](#mxutils.Random.HashNumberToVector)(value[, dtype]) | Returns a pseudo-random vector in the interval *[[0, 0, 0], [1, 1, 1]]* for the passed numeric value. |
| [`HashVectorToColor`](#mxutils.Random.HashVectorToColor)(value[, hueInterval, …]) | Returns a pseudo-random color hash for the passed vector. |
| [`HashVectorToMatrix`](#mxutils.Random.HashVectorToMatrix)(value[, …]) | Returns a pseudo-random transform matrix hash for the passed vector. |
| [`HashVectorToNumber`](#mxutils.Random.HashVectorToNumber)(value) | Returns a pseudo-random float in the interval *[0, 1]* for the passed vector. |
| [`HashVectorToVector`](#mxutils.Random.HashVectorToVector)(value[, dtype]) | Returns a pseudo-random vector in the interval *[[0, 0, 0], [1, 1, 1]]* for the passed vector. |
| [`RandomColor`](#mxutils.Random.RandomColor)([hueInterval, …]) | Returns a random color in RGB space defined by the passed hue, saturation, and value intervals. |
| [`RandomDistribution`](#mxutils.Random.RandomDistribution)(items, binCount[, bias, …]) | Partitions the passed items into *binCount* bins of random sizes where each item appears in exactly one bin. |
| [`RandomFloat`](#mxutils.Random.RandomFloat)([lower, upper]) | Returns a random floating point number in the interval *[lower, upper]*. |
| [`RandomInt`](#mxutils.Random.RandomInt)([lower, upper]) | Returns a random integer in the interval *[lower, upper]*. |
| [`RandomMatrix`](#mxutils.Random.RandomMatrix)([positionInterval, …]) | Returns a random transform matrix with components in the passed bounds. |
| [`RandomVector`](#mxutils.Random.RandomVector)([lower, upper, dtype]) | Returns a random vector of the passed type with components in the interval *[lower, upper]*. |
| [`__init__`](#mxutils.Random.__init__)([seed, magic, noPyReseed]) | Initializes the random number generator with the passed seed. |

## Methods Definition <a id="methods-definition"></a>

### `Random.Hash(value: float | int) → float` <a id="mxutils.Random.Hash"></a>

Returns a pseudo-random hash in the interval *[-1, 1]* for the passed numeric value.

This hash uses the common trick to exploit the periodicity of the sine function to create a pseudo-random hash. It is not suitable for cryptographic purposes and not the fastest thing around, but it is simple and works well for computer graphics applications.

> **Note:** You can reattach/overwrite this method when you prefer a different hash function. All other Hash* methods in this class decompose into calls to this method.

**Parameters:** **value** (*float*) – The value to hash.

**Returns:** The hash of the value.

**Return type:** float

**Example:**

```python
import mxutils

# Create a custom random number generator with a seed of 42.
rnd: mxutils.Random = mxutils.Random()

# Compute a hash for the value 42.
h: float = rnd.Hash(42) # Will return a pseudo-random float in the interval [-1, 1].

# Attach a custom hash function to the random number generator.
def myHash(self, value: float | int) -> float | int:
    return value / 2

rnd.Hash = myHash

# Compute a hash for the value 42 using the custom hash function.
h: int = rnd.Hash(42) # Will return 21
```

### `Random.HashNumberToColor(value: float | int, hueInterval: tuple = (0.0, 360.0), saturationInterval: tuple = (0.5, 1.0), valueInterval: tuple = (0.5, 1.0), alphaInterval: tuple = (1.0, 1.0), dtype: Type = <class 'c4d.Vector'>) → c4d.Vector | c4d.Vector4d | maxon.vector.Color64 | maxon.vector4d.ColorA64` <a id="mxutils.Random.HashNumberToColor"></a>

Returns a pseudo-random color hash for the passed numeric value.

The returned value is a color in RGB space but lies the passed hue, saturation, and value intervals.

**Parameters:**

- **value** (*float* or *int*) – The value to hash.
- **hueInterval** (*tuple*[*float*, *float*], *optional*) – The interval of the hue component in degrees, defaults to *[0.0, 360.0]*.
- **saturationInterval** (*tuple*[*float*, *float*], *optional*) – The interval of the saturation component, defaults to *[0.5, 1.0]*.
- **valueInterval** (*tuple*[*float*, *float*], *optional*) – The interval of the value component, defaults to *[0.5, 1.0]*.
- **alphaInterval** (*tuple*[*float*, *float*], *optional*) – The interval of the alpha component, defaults to *[1.0, 1.0]*.
- **dtype** – The type of the color to return, defaults to *c4d.Vector*.

**Dtype type:** typing.Type, optional

**Returns:** The hashed color.

**Return type:** [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector) or [c4d.Vector4d](../../c4d/Vector4d/index.md#c4d.Vector4d) or maxon.Color or maxon.ColorA

**Raises:** **ValueError** – If an invalid color type is passed for dtype.

**Example:**

```python
import c4d
import mxutils

# Hash the value 42 to a pseudo-random RGBA color in the intervals hue(0, 90), saturation(0.5, 1.0), 
# value(0.5, 1.0), and alpha(0.5, 1.0) using the global random instance and the c4d.Vector4d type.
rgba: c4d.Vector4d = mxutils.g_random.HashNumberToColor(
    42, (0.0, 90.0), (0.5, 1.0), (0.5, 1.0), (0.5, 1.0), c4d.Vector4d)
```

### `Random.HashNumberToMatrix(value: float | int, positionInterval: tuple[c4d.Vector, c4d.Vector] | None = None, rotationInterval: tuple[c4d.Vector, c4d.Vector] | None = None, scaleInterval: tuple[c4d.Vector, c4d.Vector] | None = None) → c4d.Matrix` <a id="mxutils.Random.HashNumberToMatrix"></a>

Returns a pseudo-random transform matrix hash for the passed numeric value.

> **Note:** Will return the identity matrix if all intervals are *None*.

**Parameters:**

- **value** (*float* or *int*) – The value to hash.
- **positionInterval** (*tuple*[[*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector), [*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)], *optional*) – The interval for the offset component of the transform, will be ignored if *None*. Defaults to *None*.
- **rotationInterval** (*tuple*[[*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector), [*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)], *optional*) – The interval for the rotation component of the transform in radians, will be ignored if *None*. Defaults to *None*.
- **scaleInterval** (*tuple*[[*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector), [*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)], *optional*) – The interval for the scale component of the transform, will be ignored if *None*. Defaults to *None*.

**Returns:** The hashed matrix.

**Return type:** [c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix)

**Example:**

```python
import c4d
import mxutils

deg45: float = c4d.utils.DegToRad(45.0) # 45° in radians

# Hash the value 42 into a matrix whose offset lies in the interval [[0, 0, 0], [100, 100, 100]], but has no 
# rotation and a scale of 1.
m: c4d.Matrix = mxutils.g_random.HashNumberToMatrix(42, (c4d.Vector(0), c4d.Vector(100))

# Hash the value 42 into a matrix with a rotation in the interval [[-45, -45, -45], [45, 45, 45]] degrees.
m: c4d.Matrix = mxutils.g_random.HashNumberToMatrix(42, rotationInterval=(c4d.Vector(-deg45), c4d.Vector(deg45)))

# Hash the value 42 into a transform that has an offset in the interval [0, 0, 0], [0, 0, 100], a rotation 
# in the interval [[-45, 0, 0], [45, 0, 0]] degrees, and a scale in the interval [1, 1, 0.5], [1 1, 2.0].
m: c4d.Matrix = mxutils.g_random.HashNumberToMatrix(42, (c4d.Vector(0), c4d.Vector(0, 0, 100)),
                                                    (c4d.Vector(-deg45, 0, 0), c4d.Vector(deg45, 0, 0)),
                                                    (c4d.Vector(1, 1, 0.5), c4d.Vector(1, 1, 2.0)))
```

### `Random.HashNumberToNumber(value: float | int) → float` <a id="mxutils.Random.HashNumberToNumber"></a>

Returns a pseudo-random float in the interval *[0, 1]* for the passed numeric value.

**Parameters:** **value** (*float* or *int*) – The value to hash.

**Returns:** The hashed value.

**Return type:** float

**Example:**

```python
import mxutils

# Hash the value 42 to a pseudo-random float in the interval [0, 1] using the global random instance.
h: float = mxutils.g_random.HashNumberToNumber(42)
```

### `Random.HashNumberToVector(value: float | int, dtype: Type = <class 'c4d.Vector'>) → c4d.Vector | maxon.vector.Vector64` <a id="mxutils.Random.HashNumberToVector"></a>

Returns a pseudo-random vector in the interval *[[0, 0, 0], [1, 1, 1]]* for the passed numeric value.

**Parameters:**

- **value** (*float* or *int*) – The value to hash.
- **dtype** – The type of the vector to return. Supported are *c4d.Vector* and *maxon.Vector*. Defaults to *c4d.Vector*.

**Dtype type:** typing.Type, optional

**Returns:** The hashed vector.

**Return type:** [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector) or maxon.Vector

**Example:**

```python
import c4d
import mxutils

# Hash the value 42 to a pseudo-random c4d vector in the interval [0, 0, 0], [1, 1, 1] using the global 
# random instance.
h: c4d.Vector = mxutils.g_random.HashNumberToVector(42)
```

### `Random.HashVectorToColor(value: c4d.Vector, hueInterval: tuple = (0.0, 3.6), saturationInterval: tuple = (0.5, 1.0), valueInterval: tuple = (0.5, 1.0), alphaInterval: tuple = (1.0, 1.0), dtype: Type = <class 'c4d.Vector'>) → c4d.Vector | c4d.Vector4d | maxon.vector.Color64 | maxon.vector4d.ColorA64` <a id="mxutils.Random.HashVectorToColor"></a>

Returns a pseudo-random color hash for the passed vector.

The returned color is in RGB space defined by the passed hue, saturation, and value intervals.

**Parameters:**

- **value** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The vector to hash.
- **hueInterval** (*tuple*[*float*, *float*], *optional*) – The interval of the hue component in degrees, defaults to *[0.0, 360.0]*.
- **saturationInterval** (*tuple*[*float*, *float*], *optional*) – The interval of the saturation component, defaults to *[0.5, 1.0]*.
- **valueInterval** (*tuple*[*float*, *float*], *optional*) – The interval of the value component, defaults to *[0.5, 1.0]*.
- **alphaInterval** (*tuple*[*float*, *float*], *optional*) – The interval of the alpha component, defaults to *[1.0, 1.0]*.
- **dtype** – The type of the color to return, defaults to *c4d.Vector*.

**Dtype type:** typing.Type, optional

**Returns:** The hashed color.

**Return type:** [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector) or [c4d.Vector4d](../../c4d/Vector4d/index.md#c4d.Vector4d) or maxon.Color or maxon.ColorA

**Raises:** **ValueError** – If an invalid color type is passed for dtype.

**Example:**

```python
import c4d
import mxutils

# Hash the vector (1, 2, 3) to a pseudo-random RGBA color in the intervals hue(0, 90), saturation(0.5, 1.0), 
# value(0.5, 1.0), and alpha(0.5, 1.0) using the global random instance and the c4d.Vector4d type.
rgba: c4d.Vector4d = mxutils.g_random.HashVectorToColor(
    c4d.Vector(1, 2, 3), (0.0, 90.0), (0.5, 1.0), (0.5, 1.0), (0.5, 1.0), c4d.Vector4d)
```

### `Random.HashVectorToMatrix(value: c4d.Vector, positionInterval: tuple[c4d.Vector, c4d.Vector] | None = None, rotationInterval: tuple[c4d.Vector, c4d.Vector] | None = None, scaleInterval: tuple[c4d.Vector, c4d.Vector] | None = None) → c4d.Matrix` <a id="mxutils.Random.HashVectorToMatrix"></a>

Returns a pseudo-random transform matrix hash for the passed vector.

> **Note:** Will return the identity matrix if all intervals are *None*.

**Parameters:**

- **value** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The vector to hash.
- **positionInterval** (*tuple*[[*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector), [*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)], *optional*) – The interval for the offset component of the transform, will be ignored if *None*. Defaults to *None*.
- **rotationInterval** (*tuple*[[*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector), [*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)], *optional*) – The interval for the rotation component of the transform in radians, will be ignored if *None*. Defaults to *None*.
- **scaleInterval** (*tuple*[[*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector), [*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)], *optional*) – The interval for the scale component of the transform, will be ignored if *None*. Defaults to *None*.

**Returns:** The hashed matrix.

**Return type:** [c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix)

**Example:**

```python
import c4d
import mxutils

deg45: float = c4d.utils.DegToRad(45.0) # 45° in radians

# Hash the vector [1, 2, 3] into a matrix whose offset lies in the interval [[0, 0, 0], [100, 100, 100]], 
# but has no rotation and a scale of 1.
m: c4d.Matrix = mxutils.g_random.HashVectorToMatrix(c4d.Vector(1, 2, 3), (c4d.Vector(0), c4d.Vector(100))

# Hash the vector [1, 2, 3] into a matrix with a rotation in the interval [[-45, -45, -45], [45, 45, 45]] degrees.
m: c4d.Matrix = mxutils.g_random.HashVectorToMatrix(c4d.Vector(1, 2, 3), 
                                                    rotationInterval=(c4d.Vector(-deg45), c4d.Vector(deg45)))

# Hash the vector [1, 2, 3] into a transform that has an offset in the interval [0, 0, 0], [0, 0, 100], a
# rotation in the interval [[-45, 0, 0], [45, 0, 0]] degrees, and a scale in the interval [1, 1, 0.5], [1 1, 2.0].
m: c4d.Matrix = mxutils.g_random.HashVectorToMatrix(c4d.Vector(1, 2, 3), 
                                                    (c4d.Vector(0), c4d.Vector(0, 0, 100)),
                                                    (c4d.Vector(-deg45, 0, 0), c4d.Vector(deg45, 0, 0)),
                                                    (c4d.Vector(1, 1, 0.5), c4d.Vector(1, 1, 2.0)))
```

### `Random.HashVectorToNumber(value: c4d.Vector) → float` <a id="mxutils.Random.HashVectorToNumber"></a>

Returns a pseudo-random float in the interval *[0, 1]* for the passed vector.

> **Note:** This method takes the expensive route of hashing each component of the vector separately. When you do not care that much about collision resistance, consider calling *HashNumberToNumber(v.x + v.y + v.z)* instead.

**Parameters:** **value** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The vector to hash.

**Returns:** The hashed float.

**Return type:** float

**Example:**

```python
import c4d
import mxutils

# Hash the vector [1, 2, 3] to a pseudo-random float in the interval [0, 1] using the global random instance.
h: float = mxutils.g_random.HashVectorToNumber(c4d.Vector(1, 2, 3))
```

### `Random.HashVectorToVector(value: c4d.Vector, dtype: Type = <class 'c4d.Vector'>) → c4d.Vector | maxon.vector.Vector64` <a id="mxutils.Random.HashVectorToVector"></a>

Returns a pseudo-random vector in the interval *[[0, 0, 0], [1, 1, 1]]* for the passed vector.

**Parameters:**

- **value** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)) – The vector to hash.
- **dtype** – The type of the vector to return. Supported are *c4d.Vector* and *maxon.Vector*. Defaults to *c4d.Vector*.

**Dtype type:** typing.Type, optional

**Returns:** The hashed vector.

**Return type:** [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector) or maxon.Vector

**Example:**

```python
import c4d
import mxutils

# Hash the vector [1, 2, 3] to a pseudo-random c4d vector in the interval [0, 0, 0], [1, 1, 1] using the 
# global random instance.
h: c4d.Vector = mxutils.g_random.HashVectorToVector(c4d.Vector(1, 2, 3))
```

### `Random.RandomColor(hueInterval: tuple = (0.0, 3.6), saturationInterval: tuple = (0.0, 1.0), valueInterval: tuple = (0.0, 1.0), alphaInterval: tuple = (0.0, 1.0), dtype: Type = <class 'c4d.Vector'>) → c4d.Vector | c4d.Vector4d | maxon.vector.Color64 | maxon.vector4d.ColorA64` <a id="mxutils.Random.RandomColor"></a>

Returns a random color in RGB space defined by the passed hue, saturation, and value intervals.

**Parameters:**

- **hueInterval** (*tuple*[*float*, *float*], *optional*) – The interval of the hue component in degrees, defaults to *[0.0, 360.0]*.
- **saturationInterval** (*tuple*[*float*, *float*], *optional*) – The interval of the saturation component, defaults to *[0.0, 1.0]*.
- **valueInterval** (*tuple*[*float*, *float*], *optional*) – The interval of the value component, defaults to *[0.0, 1.0]*.
- **alphaInterval** (*tuple*[*float*, *float*], *optional*) – The interval of the alpha component, defaults to *[0.0, 1.0]*.
- **dtype** – The type of the color to return, defaults to *c4d.Vector*.

**Dtype type:** typing.Type, optional

**Returns:** The randomly generated color.

**Return type:** [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector) or [c4d.Vector4d](../../c4d/Vector4d/index.md#c4d.Vector4d) or maxon.Color or maxon.ColorA

**Raises:** **ValueError** – If an invalid color type is passed for dtype.

**Example:**

```python
import c4d
import mxutils

# Generate a random RGBA color in the intervals hue(0, 90), saturation(0.5, 1.0), value(0.5, 1.0), and 
# alpha(0.5, 1.0), using the global random instance and the c4d.Vector4d type.
rgba: c4d.Vector4d = mxutils.g_random.RandomColor((0.0, 90.0), (0.5, 1.0), (0.5, 1.0), (0.5, 1.0), c4d.Vector4d)
```

### `Random.RandomDistribution(items: list, binCount: int, bias: float | int = 0.25, preserveOrder: bool = False) → list` <a id="mxutils.Random.RandomDistribution"></a>

Partitions the passed items into *binCount* bins of random sizes where each item appears in exactly one bin.

> **Note:** The partitioning is done by randomly selecting a bin for each item. The probability of selecting a bin is proportional to the number of items already in the bin raised to the power of the bias. This function is meant to provide random results and even for a bias of *0.0* the distribution might not be perfectly even. And in some cases, the distribution might be quite even for a bias of *1.0*. As with all sampling, this effect will be less pronounced the more items you have. Please use the std lib *random.sample* function when you want to precisely control the distribution of items pulled from a population.

**Parameters:**

- **items** (*list*[*typing.Any*]) – The items to partition.
- **binCount** (*int*) – The number of bins to create.
- **bias** (*float* or *int*, *optional*) – The larger the bias, the more uneven the distribution of the items will be. A bias of *0.0* will result in a roughly even distribution, while a bias of *1.0* will result in a very uneven distribution. Defaults to *0.25*.
- **preserveOrder** (*bool*, *optional*) – When *True*, the order of the items is preserved in the bins. This is a quite expensive operation for large inputs as it rebuilds the output after the initial partitioning. Defaults to *False*.

**Returns:** The partitioned items.

**Return type:** list[list[typing.Any]]

**Example:**

```python
import mxutils

items: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Partition the items into 3 bins with the default bias of 0.25.
bins: list[list[int]] = mxutils.g_random.RandomDistribution(items, 3)
# Output: [['a', 'g'], ['b', 'd', 'i'], ['c', 'e', 'f', 'h', 'j']]

# Partition the items into 3 bins with a bias of 0, i.e., a very even outcome. Because our 
# sample size is quite small and we got a bit unlucky, the distribution is quite uneven. When 
# run often enough, we will also see the 'perfect' outcome of (3, 3, 4) items in the bins.
bins = mxutils.g_random.RandomDistribution(items, 3, 0.0)
# Output: [['b'], ['e', 'f', 'g', 'h', 'i', 'j'], ['a', 'c', 'd']]

# Partition the items into 3 bins with a bias of 1.0, i.e., a very uneven outcome. Here we 
# get two bins with one item and one bin with all the other items. Even for a bias of 1,
# each bin will always contain at least one item.
bins = mxutils.g_random.RandomDistribution(items, 3, 1.0)
# Output: [['j'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], ['i']]

# Partition the items into 3 bins while preserving the order of the input list. Preserving the 
# order does not mean that the result will be sorted, just that items are placed in the bins 
# in the order in which they appear in the input list. In this case the input list was sorted, 
# so the output will not only preserve the order but also be sorted.
bins = mxutils.g_random.RandomDistribution(items, 3, preserveOrder=True)
# Output: [['a', 'b', 'c', 'd'], ['e'], ['f', 'g', 'h', 'i', 'j']]

# And finally some partitioning with a larger sample size, here we see a more clear effect of the bias.
# But this is still a random function and the outcome is meant to vary.
items: list[int] = list(range(1000))
for bias in [.0, .5, 1.]:
    bins = g_random.RandomDistribution(data, 3, bias=bias)
    binCounts = list(len(bin) for bin in bins)
    print(f"{bias = }, {binCounts = }")

# bias = 0.0, binCounts = [339, 324, 337]
# bias = 0.5, binCounts = [391, 311, 298]
# bias = 1.0, binCounts = [455, 444, 101]
```

### `Random.RandomFloat(lower: float = 0.0, upper: float = 1.0) → float` <a id="mxutils.Random.RandomFloat"></a>

Returns a random floating point number in the interval *[lower, upper]*.

**Parameters:**

- **lower** (*float*, *optional*) – The lower bounds of the output interval, defaults to *0.0*.
- **upper** (*float*, *optional*) – The upper bounds of output interval, defaults to *1.0*.

**Returns:** The randomly generated floating point number.

**Return type:** float

**Raises:** **ValueError** – When the inputs cannot be converted to floats.

**Example:**

```python
import mxutils

# Use the global random number generator to generate a random float in the interval [0., 100.].
f: float = mxutils.g_random.RandomFloat(0., 100.)
```

### `Random.RandomInt(lower: int = 0, upper: int = 1) → int` <a id="mxutils.Random.RandomInt"></a>

Returns a random integer in the interval *[lower, upper]*.

**Parameters:**

- **lower** (*int*, *optional*) – The lower bounds of the output interval, defaults to *0*.
- **upper** (*int*, *optional*) – The upper bounds of output interval, defaults to *1*.

**Returns:** The randomly generated integer.

**Return type:** int

**Raises:** **ValueError** – When the inputs cannot be converted to integers.

**Example:**

```python
import mxutils

# Use the global random number generator to generate a random integer in the interval [0, 100].
i: int = mxutils.g_random.RandomInt(0, 100)
```

### `Random.RandomMatrix(positionInterval: tuple[c4d.Vector, c4d.Vector] | None = None, rotationInterval: tuple[c4d.Vector, c4d.Vector] | None = None, scaleInterval: tuple[c4d.Vector, c4d.Vector] | None = None) → c4d.Matrix` <a id="mxutils.Random.RandomMatrix"></a>

Returns a random transform matrix with components in the passed bounds.

> **Note:** Will return the identity matrix if all intervals are *None*.

**Parameters:**

- **positionInterval** (*tuple*[[*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector), [*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)], *optional*) – The interval of the position component, will be ignored if *None*. Defaults to *None*.
- **rotationInterval** (*tuple*[[*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector), [*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)], *optional*) – The interval of the rotation component in radians, will be ignored if *None*. Defaults to *None*.
- **scaleInterval** (*tuple*[[*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector), [*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector)], *optional*) – The interval of the scale component, will be ignored if *None*. Defaults to *None*.

**Returns:** The randomly generated transform matrix.

**Return type:** [c4d.Matrix](../../c4d/Matrix/index.md#c4d.Matrix)

**Example:**

```python
import c4d
import mxutils

deg45: float = c4d.utils.DegToRad(45.0) # 45° in radians

# Generate matrix whose offset lies in the interval [[0, 0, 0], [100, 100, 100]], but has no rotation and a 
# scale of 1.
m: c4d.Matrix = mxutils.g_random.RandomMatrix((c4d.Vector(0), c4d.Vector(100))

# Generate a random transform matrix with a rotation in the interval [[-45, -45, -45], [45, 45, 45]] degrees.
m: c4d.Matrix = mxutils.g_random.RandomMatrix(rotationInterval=(c4d.Vector(-deg45), c4d.Vector(deg45)))

# Generate a transform that has an offset in the interval [0, 0, 0], [0, 0, 100], a rotation in the interval
# [[-45, 0, 0], [45, 0, 0]] degrees, and a scale in the interval [1, 1, 0.5], [1 1, 2.0].
m: c4d.Matrix = mxutils.g_random.RandomMatrix((c4d.Vector(0), c4d.Vector(0, 0, 100)),
                                                (c4d.Vector(-deg45, 0, 0), c4d.Vector(deg45, 0, 0)),
                                                (c4d.Vector(1, 1, 0.5), c4d.Vector(1, 1, 2.0)))
```

### `Random.RandomVector(lower: c4d.Vector = Vector(0, 0, 0), upper: c4d.Vector = Vector(1, 1, 1), dtype: Type = <class 'c4d.Vector'>) → c4d.Vector | maxon.vector.Vector64` <a id="mxutils.Random.RandomVector"></a>

Returns a random vector of the passed type with components in the interval *[lower, upper]*.

**Parameters:**

- **lower** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector), *optional*) – The lower bounds of the output interval, defaults to *c4d.Vector(0)*.
- **upper** ([*c4d.Vector*](../../c4d/Vector/index.md#c4d.Vector), *optional*) – The upper bounds of output interval, defaults to *c4d.Vector(1)*.
- **dtype** – The type of the vector to return. Defaults to *c4d.Vector*.

**Dtype type:** typing.Type, optional

**Returns:** The randomly generated vector.

**Return type:** [c4d.Vector](../../c4d/Vector/index.md#c4d.Vector) or maxon.Vector

**Raises:** **ValueError** – If an invalid vector type is passed for dtype.

**Example:**

```python
import c4d
import mxutils

from mxutils import g_random

# Generate a random c4d vector in the default interval [0, 1] and a maxon vector in the interval [-1, 1] 
# using the global random instance.
u: c4d.Vector = g_random.RandomVector()
v: maxon.Vector = g_random.RandomVector(lower=c4d.Vector(-1), dtype=maxon.Vector)
```

### `Random.__init__(seed: float | None = None, magic: tuple = 721.0561, 333567.5412, noPyReseed: bool = False) → None` <a id="mxutils.Random.__init__"></a>

Initializes the random number generator with the passed seed.

**Parameters:**

- **seed** (*typing.Any*) – The seed used by the pseudo random number generator and the hash function. When of type *int*, the seed seed is set to *abs(seed if seed != 0 else 1)* but otherwise used directly. When of type *None*, the system time is used. When of any other type, the seed is created by either calling *__hash__*, *__repr__*, or *__str__* on the passed seed object. The final seed value is then always hashed to an integer. Defaults to *None*.
- **magic** (*tuple*[*float*, *float*]) – The magic numbers to use by the hash function. Defaults to *(721.0561, 333567.5412)*.
- **noPyReseed** – When *True*, the internal Python *random.random* instance will not be reseeded when the seed property is set. This can be useful when you need to reseed the generator in a loop when using the hash functions or something similarly performance critical. Defaults to *False*.

**Raises:**

- **ValueError** – When the seed object cannot be converted to a valid seed.
- **ValueError** – When the magic numbers are not a tuple of two floats.
