IfcQuantityTime
===============
_IfcQuantityTime_ is an element quantity that defines a time measure to
provide a property of time related to an element. It is normally given by the
recipe information of the element under the specific measure rules given by a
method of measurement.  
  
> EXAMPLE  The amount of time needed to pour concrete for a wall is given as a
> time quantity for the labor part of the recipe information.  
  
> HISTORY  New entity in IFC2x2.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcquantityresource/lexical/ifcquantitytime.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                                                                                                                                                                                                           |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TimeValue   | Time measure value of this quantity.                                                                                                                                                                                                                                                                                                                                  |
| Formula     | A formula by which the quantity has been calculated. It can be assigned in addition to the actual value of the quantity. Formulas could be mathematic calculations (like width x height), database links, or a combination. The formula is for informational purposes only.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE Attribute added to the end of the attribute list. |

