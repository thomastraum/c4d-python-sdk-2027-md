<!-- Source: https://developers.maxon.net/docs/py/2027_0_0/modules/c4d/CustomDataType/UnitScaleData/index.html -->

# c4d.UnitScaleData <a id="c4d-unitscaledata"></a>

## *class* `c4d.UnitScaleData` <a id="c4d.UnitScaleData"></a>

Unit scale data type (*CUSTOMDATATYPE_UNITSCALE*).

This type is called by value.

Parent Class:

- [`c4d.CustomDataType`](../index.md#c4d.CustomDataType)

## Overview <a id="overview"></a>

**Magic Methods**

- [`UnitScaleData.__init__()`](#c4d.UnitScaleData.__init__)

**Unit Scale Values**

- [`UnitScaleData.GetUnitScale()`](#c4d.UnitScaleData.GetUnitScale): Retrieves the values of the unit scale data type.
- [`UnitScaleData.SetUnitScale()`](#c4d.UnitScaleData.SetUnitScale): Sets the values for the unit scale data type.

## Members <a id="members"></a>

### Magic Methods <a id="c4d.UnitScaleData-method-Magic-Methods"></a>

#### `UnitScaleData.__init__(self, v)` <a id="c4d.UnitScaleData.__init__"></a>

**Parameters:** **v** ([*c4d.UnitScaleData*](#c4d.UnitScaleData)) – Copy constructor.

### Unit Scale Values <a id="c4d.UnitScaleData-method-Unit-Scale-Values"></a>

#### `UnitScaleData.GetUnitScale(self)` <a id="c4d.UnitScaleData.GetUnitScale"></a>

Retrieves the values of the unit scale data type.

```python
scale, unit = data.GetUnitScale()
```

**Return type:** Tuple[float, int]

**Returns:** The scale and unit data

#### `UnitScaleData.SetUnitScale(self, scale, unit)` <a id="c4d.UnitScaleData.SetUnitScale"></a>

Sets the values for the unit scale data type.

**Parameters:**

- **scale** (*float*) – The unit scale.

- **unit** (*int*) –

  One of the following unit:

  | Symbol ID | Description |
  |---|---|
  | DOCUMENT_UNIT_UNDEFINED | Undefined. |
  | DOCUMENT_UNIT_KM | Kilometer. |
  | DOCUMENT_UNIT_M | Meter. |
  | DOCUMENT_UNIT_CM | Centimeter. |
  | DOCUMENT_UNIT_MM | Millimeter. |
  | DOCUMENT_UNIT_MICRO | Micrometer. |
  | DOCUMENT_UNIT_MILE | Mile. |
  | DOCUMENT_UNIT_YARD | Yard. |
  | DOCUMENT_UNIT_FOOT | Foot. |
  | DOCUMENT_UNIT_INCH | Inch. |

**Return type:** bool

**Returns:** **True** if successful, otherwise **False**
