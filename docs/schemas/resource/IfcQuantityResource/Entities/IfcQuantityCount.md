# IfcQuantityCount

_IfcQuantityCount_ is a physical quantity that defines a derived count measure to provide an element's physical property. It is normally derived from the physical properties of the element under the specific measure rules given by a method of measurement.
<!-- end of short definition -->

> EXAMPLE An radiator may be measured according to its number of coils. The actual counting method depends on the method of measurement used.

> HISTORY New entity in IFC2x. It replaces the calcXxx attributes used in previous IFC Releases.

## Attributes

### CountValue
Count measure value of this quantity.

### Formula
A formula by which the quantity has been calculated. It can be assigned in addition to the actual value of the quantity. Formulas could be mathematic calculations (like width x height), database links, or a combination. The formula is for informational purposes only.
{ .change-ifc2x4}
> IFC4 CHANGE Attribute added to the end of the attribute list.

## Formal Propositions

### WR21
The value of the count shall be greater than or equal to zero.
