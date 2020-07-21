IfcReinforcingMesh
==================
A reinforcing mesh is a series of longitudinal and transverse wires or bars of
various gauges, arranged at right angles to each other and welded at all
points of intersection; usually used for concrete slab reinforcement. It is
also known as welded wire fabric. In scope are plane meshes as well as bent
meshes.  
  
> HISTORY  New entity in IFC2x2  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  All attributes are optional now. Several attributes are
> deprecated; their information is now provided by _IfcReinforcingMeshType_.
> Attribute _PredefinedType_ added.  
  
{ .use-head}  
Geometry Use Definition  
  
Placement and representation are defined at the supertype
_IfcElementComponent_.  
  
The representation map of a mapped ''Outline'' representation should contain a
representation of type ''Curve3D'' which holds an _IfcPolyline_.  
  
The representation map of a mapped ''Body'' representation should contain a
representation of type ''AdvancedSweptSolid'' which holds multiple
_IfcSweptDiskSolid_ (including subtype _IfcSweptDiskSolidPolygonal_).  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralelementsdomain/lexical/ifcreinforcingmesh.htm)


Attribute definitions
---------------------
| Attribute                       | Description                                                                                                                                                     |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MeshLength                      | Deprecated.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Attribute deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead.                   |
| MeshWidth                       | Deprecated.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Attribute deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead.                   |
| LongitudinalBarNominalDiameter  | Deprecated.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead. |
| TransverseBarNominalDiameter    | Deprecated.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead. |
| LongitudinalBarCrossSectionArea | Deprecated.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead. |
| TransverseBarCrossSectionArea   | Deprecated.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead. |
| LongitudinalBarSpacing          | Deprecated.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead. |
| TransverseBarSpacing            | Deprecated.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Attribute made optional and deprecated. Use respective attribute at _IfcReinforcingMeshType_ instead. |

Formal Propositions
-------------------
| Rule                  | Description   |
|-----------------------|---------------|
| CorrectPredefinedType |               |
| CorrectTypeAssigned   |               |

Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

