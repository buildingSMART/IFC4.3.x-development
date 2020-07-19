IfcRepresentation
=================
The _IfcRepresentation_ defines the general concept of representing product
properties and in particular the product shape.  
  
{ .extDef}  
> NOTE  Definition from ISO 10303-43:  
> A representation is a collection of one or more representation items that
> are related in a specified representation context. The relationship of
> representation item to representation context is the basis for
> distinguishing which representation item entities are related.  
>  
> A representation item can be related to a representation context directly,
> when it occurs as an element is a representation, or indirectly, when it is
> referenced through any number of intervening entities, each of type
> representation item.  
  
> NOTE  Entity adapted from **representation** defined in ISO 10303-42.  
  
> HISTORY  New entity in IFC2.0  
  
{ .change-ifc2x3}  
> IFC2x3 CHANGE  The inverse attributes _LayerAssignments_
> and_RepresentationMap_ have been added with upward compatibility.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Entity _IfcRepresentation_ has been changed into an ABSTRACT
> supertype.  
  
{ .use-head}  
Representation Use Definition  
  
Each representation, either _IfcShapeRepresentation_, or
_IfcTopologyRepresentation_ shall have a well defined:  
  
* _ContextOfItems_: Reference to an _IfcGeometricRepresentationContext_ as agreed for this representation.   
* _RepresentationIdentifier_: Name of the representation, for example, ''Body'' for 3D shape, ''FootPrint'' for 2D ground view, ''Axis'' for reference axis.   
* _RepresentationType_: Name for the geometric, or topological representation type, for example, ''SweptSolid'' for 3D swept solids, ''Brep'' for boundary representation.   
  
> NOTE  Guidelines for applying correct values to those attributes are
> provided in the geometry use definition section at each subtype of
> _IfcElement_. These guidelines can be further refined in view definitions or
> implementer agreements.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcrepresentationresource/lexical/ifcrepresentation.htm)


