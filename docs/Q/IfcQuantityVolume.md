IfcQuantityVolume
=================
_IfcQuantityVolume_ is a physical quantity that defines a derived volume
measure to provide an element''s physical property. It is normally derived
from the physical properties of the element under the specific measure rules
given by a method of measurement.  
  
> EXAMPLE  A thick brick wall may be measured according to its volume. The
> actual size of the volume depends on the method of measurement used.  
  
> HISTORY  New entity in IFC2x. It replaces the calcXxx attributes used in
> previous IFC Releases.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcquantityresource/lexical/ifcquantityvolume.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                                                                                                                                                                                                           |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VolumeValue | Volume measure value of this quantity.                                                                                                                                                                                                                                                                                                                                |
| Formula     | A formula by which the quantity has been calculated. It can be assigned in addition to the actual value of the quantity. Formulas could be mathematic calculations (like width x height), database links, or a combination. The formula is for informational purposes only.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE Attribute added to the end of the attribute list. |

