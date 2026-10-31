<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/mxutils/mxutils.Random.Seed.html -->

# mxutils.Random.Seed <a id="mxutils-random-seed"></a>

## *property* `Random.Seed` <a id="mxutils.Random.Seed"></a>

Gets or sets the seed of the instance used by both the pseudo-random number generator and the hash function.

> > **Note:** Seed objects that are not of type *int*, *float*, or *str* are converted to a valid seed by converting them using the *__hash__*, *__repr__*, or *__str__* methods. This method checks if the passed seed object implements any of these methods in the mentioned order and uses the first one that is found. A seed object which does not implement any of these methods cannot be converted to a valid seed and will raise a *ValueError*.

> **Warning:** Calling this method will also reseed the Python *random.Random* instance held by this class. Calling *random.Random.seed* is an expensive operation and should be avoided if possible in performance critical code. When you are only using the hash functions of this class, and must reseed the generator in a loop, or something similarly performance critical, pass *noPyReseed=True* to the constructor of this type. Then you can write to the *Seed* property of your instance without reseeding the internal Python *random.Random* instance.

**Parameters:** **seed** (*typing.Any*) – The seed used by the pseudo random number generator and the hash function. When of type *int*, the seed seed is set to *abs(seed if seed != 0 else 1)* but otherwise used directly. When of type *None*, the system time is used. When of any other type, the seed is created by either calling *__hash__*, *__repr__*, or *__str__* on the passed seed object. The final seed value is then always hashed to an integer. Defaults to *None*.

**Raises:** **ValueError** – When a seed object cannot be converted to a valid seed.

**Returns:** The current seed of the random number generator.

**Return type:** float

**Example:**

```python
import mxutils

# Create a custom random number generator with a seed of 42.
rnd: mxutils.Random = mxutils.Random(42)

# Reseed the random number generator with the current system time.
rnd.Seed = None

# Use a scene element as the seed (effectively using its UUID as the seed).
obj: c4d.BaseObject = c4d.BaseObject(c4d.Onull)
rnd.Seed = obj
```
