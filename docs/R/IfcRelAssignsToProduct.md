IfcRelAssignsToProduct
======================
The objectified relationship\S\ _IfcRelAssignsToProduct_ handles the
assignment of objects (subtypes of _IfcObject_) to a product (subtypes of
_IfcProduct_). The _Name_ attribute should be used to classify the usage of
the _IfcRelAssignsToProduct_ objectified relationship. The following _Name_
values are proposed:  
  
* ''Context'' : Assignment of a context specific representation, such as of structural members to a different context representation (with potentially different decomposition breakdown) such as of building elements\S\ for a specific\S\ context specific representation.\S\   
* ''View'' : Assignment of a product (via _RelatingProduct_) that is decomposed according to a discipline view, to another product (via _RelatedObjects_) that is decomposed according to a different discipline view. An example is the assignment of the architectural slab to a different decomposition of the pre manufactured sections of a slab (under a precast concrete discipline view).  
  
> HISTORY  New entity in IFC2x  
  
{ .change-ifc2x3}  
> IFC2x3 CHANGE \S\ The reference of a product within a spatial structure is
> now handled by a new relationship object
> _IfcRelReferencedInSpatialStructure_. The _IfcRelAssignsToProduct_ shall not
> be used to represent this relation from IFC2x3 onwards.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcrelassignstoproduct.htm)


Attribute definitions
---------------------
| Attribute       | Description                                                                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RelatingProduct | Reference to the product or product type to which the objects are assigned to.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE Datatype expanded to include _IfcProduct_ and _IfcTypeProduct_. |

