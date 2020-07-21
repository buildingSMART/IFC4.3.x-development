IfcMaterialDefinition
=====================
_IfcMaterialDefinition_ is a general supertype for all material related
information items in IFC that have common material related properties that may
include association of material with some shape parameters or assignments to
identified parts of a component.  
  
There are three ways of assigning materials to a single component or multiple
components; they are characterized as:  
  
* by layer - assigning a material to a layer with constant thickness  
* by profile - assigning a material to a profile with a constant of varying shape along an extrusion  
* by constituents - assigning a material to an identified part of a component shape; the identification is by a keyword rather than by a shape parameter  
  
Each instantiable subtype of _IfcMaterialDefinition_ may have material
properties assigned, or have an external classification of its definition. It
can be assigned to either a subtype of _IfcElement_, or a subtype of
_IfcElementType_ by using the objectified relationship
_IfcRelAssociatesMaterial_.  
  
> HISTORY\S\ New entity in IFC4  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcmaterialresource/lexical/ifcmaterialdefinition.htm)


Associations
------------
| Attribute             | Description   |
|-----------------------|---------------|
| HasExternalReferences |               |
| HasProperties         |               |
| AssociatedTo          |               |

