IfcReinforcingMeshType
======================
The reinforcing element type **IfcReinforcingMeshType** defines commonly
shared information for occurrences of reinforcing meshs. The set of shared
information may include:  
  
* common properties with shared property sets  
* common representations  
* common materials  
* common composition of elements  
  
It is used to define a reinforcing mesh type specification indicating the
specific product information that is common to all occurrences of that product
type. The **IfcReinforcingMeshType** may be declared within _IfcProject_ or
_IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or
without occurrences of the type. Occurrences of **IfcReinforcingMeshType** are
represented by instances of _IfcReinforcingMesh_.  
  
> HISTORY  New entity in IFC4.  
  
{ .use-head}  
Geometry Use Definition  
  
The _IfcReinforcingMeshType_ may define the shared geometric representation
for many mesh occurrences. The _RepresentationMaps_ attribute refers to a list
of _IfcRepresentationMap_''s, that allow for multiple geometric
representations.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralelementsdomain/lexical/ifcreinforcingmeshtype.htm)


