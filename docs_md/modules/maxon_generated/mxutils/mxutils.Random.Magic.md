<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/mxutils/mxutils.Random.Magic.html -->

# mxutils.Random.Magic <a id="mxutils-random-magic"></a>

## *property* `Random.Magic` <a id="mxutils.Random.Magic"></a>

Gets or sets the magic numbers used by the hash function.

> **Note:** The magic numbers are used by the hash function to generate pseudo-random numbers. The internal default values are *721.0561* and *333567.5412*. Modifying the magic numbers is usually not necessary, use the *Seed* property to get ‘different’ hash patterns instead.

**Parameters:** **magic** (*tuple*[*float*, *float*]) – The magic numbers to set. The second value should be larger than the first one and both values must be greater than *1.0*.

**Raises:**

- **TypeError** – When the magic numbers are not a tuple of two floats.
- **ValueError** – When the magic numbers are less than or equal to *1.0* or the second value is less than the first one.

**Returns:** The magic numbers used by the hash function.

**Return type:** tuple[float, float]

**Example:**

```python
import mxutils

# Create a custom random number generator with a seed of 42 and custom magic numbers.
rnd: mxutils.Random = mxutils.Random(42, (123.0, 4567.0))

# Get the magic numbers used by the hash function.
magic: tuple[float, float] = rnd.Magic

# Set the magic numbers used by the hash function.
rnd.Magic = (98.76, 543.21)
```
