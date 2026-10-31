<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/frameworks/graph/datatype/maxon.Wires.html -->

# maxon.Wires <a id="maxon-wires"></a>

## Description <a id="module-maxon.Wires"></a><a id="description"></a>

A port connection consists of up to eight independent wires:

1. The /value/ wire is used to pass data values along the connection.
2. The /event/ wire is used when events shall flow along the connection.
3. The /dependency/ wire is only needed for internal connections within evaluation nodes such as core node wrappers.
4. computed output port needs to have a dependency wire from each input port which is required for its computation.
5. The /context/ wire connects a port which shall define a context to an input port which introduces that context.
6. The /hidden/ wire is used mark a connection as hidden.  
   What this means exactly is model-specific, for example [`maxon.NodesGraphModelInterface`](../../nodes/interface/maxon.NodesGraphModelInterface.md#module-maxon.NodesGraphModelInterface) doesn’t show those connections.
7. The /inhibit/ wire is used to temporarily disable the other wires.  
   When this wire is present, the other wires should be considered as non-existing.
8. The /slink/ wire is a marker which is used for node-specific purposes, where the source port of the connection  
   determines the meaning.  
   For example it connects the output port of a context parameter node to the input port which introduces the context.
9. The /tlink/ wire is a marker which is used for node-specific purposes, where the target port of the connection determines the meaning.

In most cases you only need a combination of a value, event and dependency wire.

The Wires class has the members #value, #event, #dependency, #context, #hidden, #inhibit, #slink, #tlink to store information about these wires for a connection.  
Each of them has the enumeration type [`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE) with the following possible values:

- WIRE_MODE.NONE means that there is no such wire in the connection.  
  This does not necessarily mean that there is no such wire at all because a wire might be “inherited” from a base node system, or there may be an “implicit wire” due to an enclosing connection.
- WIRE_MODE.MIN, WIRE_MODE.NORMAL and WIRE_MODE.MAX indicate that a wire exists.  
  The values are priorities, so whenever an ambiguity between multiple wires has to be resolved, the wires with highest priority are taken.

The wires of a connection can also be accessed by index, see VALUE, EVENT, DEPENDENCY, CONTEXT, HIDDEN, INHIBIT, SLINK, TLINK and #operator[].  
For a loop over the wires you have to use COUNT as upper bound:

```python
>>> w = Wires()
>>> for i in range(Wires.COUNT):
...    print(w[i])

>>> w.value = WIRE_MODE.NONE
# Same as line above
>>> w[Wires.VALUE] = WIRE_MODE.NONE
```

A Wires object can also be used as a mask to test another Wires object.  
Wires masks use the mask values of WIRE_MODE(WIRE_MODE.NONE, WIRE_MODE.ALL, WIRE_MODE.IMPLICIT, WIRE_MODE.ALL_INCLUDING_IMPLICIT, WIRE_MODE.INHERIT, WIRE_MODE.FULL_MASK).  
Testing against a mask is done by the bitwise operators && and ||.

## Inheritance diagram <a id="inheritance-diagram"></a>

Parent Class:

- [`maxon.Struct`](../../../datatypes/base_core/maxon.Struct.md#module-maxon.Struct)
- [`maxon.Data`](../../../datatypes/base_core/maxon.Data.md#module-maxon.Data)

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| `maxon.Wires.CONTEXT` | The index to address the context part, used in #operator[] and Wires(Int,WIRE_MODE). |
| [`maxon.Wires.COUNT`](maxon.Wires.COUNT.md#maxon.Wires.COUNT) | The number of wires (currently 8). |
| `maxon.Wires.DEPENDENCY` | The index to address the dependency part, used in #operator[] and Wires(Int,WIRE_MODE). |
| `maxon.Wires.EVENT` | The index to address the event part, used in #operator[] and Wires(Int,WIRE_MODE). |
| `maxon.Wires.HIDDEN` | The index to address the hidden part, used in #operator[] and Wires(Int,WIRE_MODE). |
| `maxon.Wires.INHIBIT` | The index to address the inhibit part, used in #operator[] and Wires(Int,WIRE_MODE). |
| [`maxon.Wires.NONE`](maxon.Wires.NONE.md#maxon.Wires.NONE) | Constant indicating no wires at all. |
| `maxon.Wires.SLINK` | The index to address the slink part, used in #operator[] and Wires(Int,WIRE_MODE). |
| `maxon.Wires.TLINK` | The index to address the tlink part, used in #operator[] and Wires(Int,WIRE_MODE). |
| `maxon.Wires.VALUE` | The index to address the value part, used in #operator[] and Wires(Int,WIRE_MODE). |
| [`maxon.Wires.context`](maxon.Wires.CONTEXT.md#maxon.Wires.context) | The mode for the context part of the connection. |
| [`maxon.Wires.dependency`](maxon.Wires.DEPENDENCY.md#maxon.Wires.dependency) | The mode for the dependency part of the connection. |
| [`maxon.Wires.event`](maxon.Wires.EVENT.md#maxon.Wires.event) | The mode for the event part of the connection. |
| [`maxon.Wires.hidden`](maxon.Wires.HIDDEN.md#maxon.Wires.hidden) | The mode for the hidden part of the connection. |
| [`maxon.Wires.inhibit`](maxon.Wires.INHIBIT.md#maxon.Wires.inhibit) | The mode for the inhibit part of the connection. |
| [`maxon.Wires.slink`](maxon.Wires.SLINK.md#maxon.Wires.slink) | The mode for the slink part of the connection. |
| [`maxon.Wires.tlink`](maxon.Wires.TLINK.md#maxon.Wires.tlink) | The mode for the tlink part of the connection. |
| [`maxon.Wires.value`](maxon.Wires.VALUE.md#maxon.Wires.value) | The mode for the value part of the connection. |

## Methods Signature <a id="methods-signature"></a>

|   |   |
|---|---|
| [`All`](#maxon.Wires.All)([mode]) | Returns a Wires value where all wire modes are set to the given *mode*. |
| [`Combine`](#maxon.Wires.Combine)(other) | Returns the parallel combination of this Wires object and other. |
| [`Concat`](#maxon.Wires.Concat)(other) | Returns the concatenation of this [`maxon.Wires`](#module-maxon.Wires) object and other. |
| [`EqualWires`](#maxon.Wires.EqualWires)(other) | Returns the wire-wise comparison of this and other. |
| [`GetHashCode`](#maxon.Wires.GetHashCode)() | Returns the hash code of this [`maxon.Wires`](#module-maxon.Wires). |
| [`MaskByPriority`](#maxon.Wires.MaskByPriority)(priorityMask) | Returns a [`maxon.Wires`](#module-maxon.Wires) object which contains only those wires of this Wires object |
| [`ToInt`](#maxon.Wires.ToInt)() |  |
| [`ToMask`](#maxon.Wires.ToMask)() | Converts this [`maxon.Wires`](#module-maxon.Wires) object into a mask which uses WIRE_MODE.FULL_MASK for wires which are set in this Wires object, otherwise WIRE_MODE.NONE. |
| [`ToString`](#maxon.Wires.ToString)() | Returns a String representation of this [`maxon.Wires`](#module-maxon.Wires) |
| [`__and__`](#maxon.Wires.__and__)(other) |  |
| [`__bool__`](#maxon.Wires.__bool__)() | Checks if there is any wire. |
| [`__eq__`](#maxon.Wires.__eq__)(other) | Returns the wire-wise comparison of this and other. |
| [`__getitem__`](#maxon.Wires.__getitem__)(item) | Returns the mode for the wire indexed by *index*. |
| [`__hash__`](#maxon.Wires.__hash__)() | Return hash(self). |
| [`__iand__`](#maxon.Wires.__iand__)(other) |  |
| [`__init__`](#maxon.Wires.__init__)([value, event, dependency, …]) | Create a new Wire Only few call are allowed: |
| [`__int__`](#maxon.Wires.__int__)() |  |
| [`__invert__`](#maxon.Wires.__invert__)() |  |
| [`__iter__`](#maxon.Wires.__iter__)() | Generator over each value of the Wires |
| [`__ne__`](#maxon.Wires.__ne__)(other) | Returns the wire-wise comparison of this and other. |
| [`__or__`](#maxon.Wires.__or__)(other) | Return self\|value. |
| [`__setitem__`](#maxon.Wires.__setitem__)(key, value) | Set the mode to *value* for the wire indexed by *index*. |
| [`__str__`](#maxon.Wires.__str__)() | Return str(self). |

## Methods Definition <a id="methods-definition"></a>

### *static* `Wires.All(mode=63)` <a id="maxon.Wires.All"></a>

Returns a Wires value where all wire modes are set to the given *mode*.  
With the default WIRE_MODE.ALL this can be used as a mask which represents all wires, this is useful as argument to `PortTemplate.GetConnections()` to get all connections.

**Parameters:** **mode** ([`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)) – The mode to use for all wires, WIRE_MODE.ALL by default.

**Returns:** Wires value having all wire modes set to *mode*.

**Return type:** [`maxon.Wires`](#module-maxon.Wires)

### `Wires.Combine(other)` <a id="maxon.Wires.Combine"></a>

Returns the parallel combination of this Wires object and other.  
This takes the maximum of each wire value.

**Parameters:** **other** ([`maxon.Wires`](#module-maxon.Wires)) – Another Wires object.

**Returns:** The parallel combination (maximum) of the wires.

**Return type:** [`maxon.Wires`](#module-maxon.Wires)

### `Wires.Concat(other)` <a id="maxon.Wires.Concat"></a>

Returns the concatenation of this [`maxon.Wires`](#module-maxon.Wires) object and other.  
This takes the minimum of each wire value.

**Parameters:** **other** ([`maxon.Wires`](#module-maxon.Wires)) – Another Wires object.

**Returns:** The concatenation (minimum) of the wires.

**Return type:** [`maxon.Wires`](#module-maxon.Wires)

### `Wires.EqualWires(other)` <a id="maxon.Wires.EqualWires"></a>

Returns the wire-wise comparison of this and other.  
This uses [`maxon.WIRE_MODE.FULL_MASK`](../../../enums/maxon.WIRE_MODE.FULL_MASK.md#maxon.WIRE_MODE.FULL_MASK) for a wire with the same value in this and other, of [`maxon.WIRE_MODE.NONE`](../../../enums/maxon.WIRE_MODE.NONE.md#maxon.WIRE_MODE.NONE) if the values differ.

**Parameters:** **other** ([`maxon.Wires`](#module-maxon.Wires)) – Another Wires object.

**Returns:** Wire-wise comparison of this and other.

**Return type:** [`maxon.Wires`](#module-maxon.Wires)

### `Wires.GetHashCode()` <a id="maxon.Wires.GetHashCode"></a>

Returns the hash code of this [`maxon.Wires`](#module-maxon.Wires).

**Returns:** Hash code of this `maxon.CLASS`.

**Return type:** int

### `Wires.MaskByPriority(priorityMask)` <a id="maxon.Wires.MaskByPriority"></a>

Returns a [`maxon.Wires`](#module-maxon.Wires) object which contains only those wires of this Wires object which aren’t below the priority values given in *priorityMask*.

**Parameters:** **priorityMask** ([`maxon.Wires`](#module-maxon.Wires)) – Another Wires object.

**Returns:** Those wires which aren’t below the values of *priorityMask*.

**Return type:** [`maxon.Wires`](#module-maxon.Wires)

### `Wires.ToInt()` <a id="maxon.Wires.ToInt"></a>

### `Wires.ToMask()` <a id="maxon.Wires.ToMask"></a>

Converts this [`maxon.Wires`](#module-maxon.Wires) object into a mask which uses WIRE_MODE.FULL_MASK for wires which are set in this Wires object, otherwise WIRE_MODE.NONE.

**Returns:** Mask object to mask those wires which are present in this Wires object.

**Return type:** [`maxon.Wires`](#module-maxon.Wires)

### `Wires.ToString()` <a id="maxon.Wires.ToString"></a>

Returns a String representation of this [`maxon.Wires`](#module-maxon.Wires)

**Returns:** String representation of this [`maxon.Wires`](#module-maxon.Wires).

**Return type:** str

### `Wires.__and__(other)` <a id="maxon.Wires.__and__"></a>

### `Wires.__bool__()` <a id="maxon.Wires.__bool__"></a>

Checks if there is any wire.

**Returns:** **True** if at least one of the wire modes differs from WIRE_MODE.NONE, **False** otherwise.

**Return type:** bool

### `Wires.__eq__(other)` <a id="maxon.Wires.__eq__"></a>

Returns the wire-wise comparison of this and other.  
This uses WIRE_MODE.FULL_MASK for a wire with the same value in this and other, of WIRE_MODE.NONE if the values differ.

**Parameters:** **other** ([`maxon.Wires`](#module-maxon.Wires)) – Another Wires object.

**Returns:** Wire-wise comparison of this and other.

**Return type:** bool

### `Wires.__getitem__(item)` <a id="maxon.Wires.__getitem__"></a>

Returns the mode for the wire indexed by *index*.

**Parameters:** **item** (*int*) – The index of the wire, one of VALUE, EVENT, DEPENDENCY, CONTEXT, HIDDEN, INHIBIT, SLINK, TLINK.

**Returns:** Mode for the wire.

**Return type:** [`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)

### `Wires.__hash__()` <a id="maxon.Wires.__hash__"></a>

Return hash(self).

### `Wires.__iand__(other)` <a id="maxon.Wires.__iand__"></a>

### `Wires.__init__(value=0, event=0, dependency=0, context=0, hidden=0, inhibit=0, slink=0, tlink=0)` <a id="maxon.Wires.__init__"></a>

Create a new Wire Only few call are allowed:

- Wires(Int index, WIRE_MODE mode = WIRE_MODE.NORMAL)
- Wires(WIRE_MODE mode) : value(mode), event(mode), dependency(mode)
- **Wires(value=WIRE_MODE.NONE vent=WIRE_MODE.NONE, dependency=WIRE_MODE.NONE,** context=WIRE_MODE.NONE, hidden=WIRE_MODE.NONE, inhibit=WIRE_MODE.NONE, slink=WIRE_MODE.NONE, tlink=WIRE_MODE.NONE)

**Parameters:**

- **value** ([`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)) – The value to set
- **event** ([`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)) – The event to set
- **dependency** ([`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)) – The dependency to set
- **context** ([`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)) – The context to set
- **hidden** ([`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)) – The hidden to set
- **inhibit** ([`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)) – The inhibit to set
- **slink** ([`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)) – The slink to set
- **tlink** ([`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)) – The tlink to set

### `Wires.__int__()` <a id="maxon.Wires.__int__"></a>

### `Wires.__invert__()` <a id="maxon.Wires.__invert__"></a>

### `Wires.__iter__()` <a id="maxon.Wires.__iter__"></a>

Generator over each value of the Wires

### `Wires.__ne__(other)` <a id="maxon.Wires.__ne__"></a>

Returns the wire-wise comparison of this and other.  
This uses WIRE_MODE.FULL_MASK for a wire with the same value in this and other, of WIRE_MODE.NONE if the values differ.

**Parameters:** **other** ([`maxon.Wires`](#module-maxon.Wires)) – Another Wires object.

**Returns:** Wire-wise comparison of this and other.

**Return type:** bool

### `Wires.__or__(other)` <a id="maxon.Wires.__or__"></a>

Return self|value.

### `Wires.__setitem__(key, value)` <a id="maxon.Wires.__setitem__"></a>

Set the mode to *value* for the wire indexed by *index*.

**Parameters:**

- **key** (*int*) – The index of the wire, one of VALUE, EVENT, DEPENDENCY, CONTEXT, HIDDEN, INHIBIT, SLINK, TLINK.
- **value** ([`maxon.WIRE_MODE`](../../../enums/maxon.WIRE_MODE.md#module-maxon.WIRE_MODE)) – Mode for the wire.

### `Wires.__str__()` <a id="maxon.Wires.__str__"></a>

Return str(self).
