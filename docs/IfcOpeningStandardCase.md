IfcOpeningStandardCase
======================
The standard opening, _IfcOpeningStandardCase_, defines an opening with
certain constraints for the dimension parameters, position within the voided
element, and with certain constraints for the geometric representation. The
_IfcOpeningStandardCase_ handles all cases of openings, that:  
  
* are true openings where the opening depth is greather than or equal to the thickness of the element, and the _Predefinedtype_ is set correctly to .OPENING.  
* are true recesses where the opening depth is lower than the thickness of the element, and the _Predefinedtype_ is set correctly to .RECESS.  
* are extruded perpendicular to the wall plane in case of openings in a wall  
* are extruded perpendicular to the slab plane in case of openings in a slab  
* have a local placement relative to the local placement of the voided element  
* have a ''Body'' shape representation with ''SweptSolid'' representation type  
* have only a single extrusion body within the ''Body'' shape representation  
  
> HISTORY  New entity in IFC4  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcopeningstandardcase.htm)


