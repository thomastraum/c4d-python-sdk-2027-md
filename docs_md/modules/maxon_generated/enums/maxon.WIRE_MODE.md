<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/maxon_generated/enums/maxon.WIRE_MODE.html -->

# maxon.WIRE_MODE <a id="maxon-wire-mode"></a>

## Description <a id="module-maxon.WIRE_MODE"></a><a id="description"></a>

WIRE_MODE is used for the wires in a Wires object to control whether a wire is set, inherited or hidden.  
This is an ordered enumeration with NONE < MIN < NORMAL < MAX. Other values  
shouldn’t be used for ordered comparisons.

## Inheritance diagram <a id="inheritance-diagram"></a>

## Attributes <a id="attributes"></a>

|   |   |
|---|---|
| [`maxon.WIRE_MODE.ALL`](maxon.WIRE_MODE.ALL.md#maxon.WIRE_MODE.ALL) | A mask for all explicit modes. |
| [`maxon.WIRE_MODE.ALL_INCLUDING_IMPLICIT`](maxon.WIRE_MODE.ALL_INCLUDING_IMPLICIT.md#maxon.WIRE_MODE.ALL_INCLUDING_IMPLICIT) | A mask for all modes |
| [`maxon.WIRE_MODE.AMBIGUOUS`](maxon.WIRE_MODE.AMBIGUOUS.md#maxon.WIRE_MODE.AMBIGUOUS) | Used for shortcut wires when the sources are ambiguous. |
| [`maxon.WIRE_MODE.AUTO_PROPAGATION`](maxon.WIRE_MODE.AUTO_PROPAGATION.md#maxon.WIRE_MODE.AUTO_PROPAGATION) | A wire with auto-propagation priority. |
| [`maxon.WIRE_MODE.CONNECT_DEFAULT`](maxon.WIRE_MODE.CONNECT_DEFAULT.md#maxon.WIRE_MODE.CONNECT_DEFAULT) |  |
| [`maxon.WIRE_MODE.FLAG0`](maxon.WIRE_MODE.FLAG0.md#maxon.WIRE_MODE.FLAG0) | A wire flag which can be used for wires which don’t interpret the wire mode as priority, but as a bit set. |
| [`maxon.WIRE_MODE.FLAG1`](maxon.WIRE_MODE.FLAG1.md#maxon.WIRE_MODE.FLAG1) | A wire flag which can be used for wires which don’t interpret the wire mode as priority, but as a bit set. |
| [`maxon.WIRE_MODE.FLAGS_MASK`](maxon.WIRE_MODE.FLAGS_MASK.md#maxon.WIRE_MODE.FLAGS_MASK) | Mask for FLAG0 \| FLAG1. |
| [`maxon.WIRE_MODE.FULL_MASK`](maxon.WIRE_MODE.FULL_MASK.md#maxon.WIRE_MODE.FULL_MASK) | Complete mask for all bits of WIRE_MODE. |
| [`maxon.WIRE_MODE.GETCONNECTIONS_DEFAULT`](maxon.WIRE_MODE.GETCONNECTIONS_DEFAULT.md#maxon.WIRE_MODE.GETCONNECTIONS_DEFAULT) |  |
| [`maxon.WIRE_MODE.IMPLICIT`](maxon.WIRE_MODE.IMPLICIT.md#maxon.WIRE_MODE.IMPLICIT) | Used as mask for implicit wires in `MutablePort.GetConnections()`. |
| [`maxon.WIRE_MODE.INHERIT`](maxon.WIRE_MODE.INHERIT.md#maxon.WIRE_MODE.INHERIT) | Used for `MutablePort.Connect()` to tell that the wire mode shall be inherited. |
| [`maxon.WIRE_MODE.MAX`](maxon.WIRE_MODE.MAX.md#maxon.WIRE_MODE.MAX) | A wire with maximum priority. |
| [`maxon.WIRE_MODE.MIN`](maxon.WIRE_MODE.MIN.md#maxon.WIRE_MODE.MIN) | A wire with minimum priority. |
| [`maxon.WIRE_MODE.NONE`](maxon.WIRE_MODE.NONE.md#maxon.WIRE_MODE.NONE) | No wire. |
| [`maxon.WIRE_MODE.NORMAL`](maxon.WIRE_MODE.NORMAL.md#maxon.WIRE_MODE.NORMAL) | A wire with normal priority. |
| [`maxon.WIRE_MODE.PRIORITY_MASK`](maxon.WIRE_MODE.PRIORITY_MASK.md#maxon.WIRE_MODE.PRIORITY_MASK) | Mask for the priority bits. |
| [`maxon.WIRE_MODE.PROPAGATION`](maxon.WIRE_MODE.PROPAGATION.md#maxon.WIRE_MODE.PROPAGATION) | A wire with propagation priority. |
| [`maxon.WIRE_MODE.REMOVE`](maxon.WIRE_MODE.REMOVE.md#maxon.WIRE_MODE.REMOVE) | Only used for :`MutablePort.Connect()` to tell that the an existing wire shall be removed. |
