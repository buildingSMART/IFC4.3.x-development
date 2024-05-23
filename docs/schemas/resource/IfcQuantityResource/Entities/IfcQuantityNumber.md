IfcQuantityNumber is a physical quantity that defines a derived number measure (integer or non-integer) to provide an element's physical property. It is normally derived from the physical properties of the element under the specific measure rules given by a method of measurement.

<!-- end of short definition -->


> HISTORY IFC4.3.0.0 New entity. It has been introduced to provide additional clarity to have IfcQuantityCount strictly constrained to an integer.

## Attributes

### NumberValue
Count measure value of this quantity.

### Formula
A formula by which the quantity has been calculated. It can be assigned in addition to the actual value of the quantity. Formulas could be mathematic calculations (like width x height), database links, or a combination. The formula is for informational purposes only.

> IFC4 CHANGE Attribute added to the end of the attribute list.
