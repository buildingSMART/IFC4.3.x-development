IfcRelConnectsStructuralMember
==============================
The entity _IfcRelConnectsStructuralMember_ defines all needed properties
describing the connection between structural members and structural connection
objects (nodes or supports).  
  
> HISTORY  New entity in IFC2x2.  
  
**Use Definition**  
  
_Point Connection_  
Instances of the entity _IfcRelConnectsStructuralMember_ shall be used to
describe a connection between an instance of _IfcStructuralPointConnection_
and either an instance of _IfcStructuralCurveMember_ or
_IfcStructuralSurfaceMember_. The _RelatedStructuralConnection_ for point
connections has to be of type _IfcStructuralPointConnection_.  
  
_Curve Connection_  
Instances of the entity _IfcRelConnectsStructuralMember_ shall be used to
describe a connection between an instance of _IfcStructuralCurveConnection_
and an instance of either _IfcStructuralCurveMember_ or
_IfcStructuralSurfaceMember_. The _RelatedStructuralConnection_ for curve
connections has to be of type _IfcStructuralCurveConnection_.  
  
_Surface Connection_  
Instances of the entity _IfcRelConnectsStructuralMember_ shall be used to
describe a connection between an instance of _IfcStructuralSurfaceConnection_
and an instance of _IfcStructuralSurfaceMember_. The
_RelatedStructuralConnection_ for curve connections has to be of type
_IfcStructuralSurfaceConnection_.  
  
_Coordinate System for Applied Conditions_  
All values defined by _AppliedCondition_ or _AdditionalConditions_ are given
within the coordinate system provided by _ConditionCoordinateSystem_, which is
defined relative to the local coordinate system of the structural member. If
the _ConditionCoordinateSystem_ is not defined, the local coordinate system of
the structural member is used instead.  
  
_Supported Length_  
Optionally a supported length can be given, which specifies the length (or
width) of the physical connection along a curve connection.  
  
Figure 1 illustrates the appropriate definition of support lengths.  
  
  
  
  

![supported length](figures/ifcrelconnectsstructuralmember-fig1.gif)

  
  
  
---  
  
  
  

Figure 1 -- Structural member support lengths

  
  
  
  
  
[_bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralanalysisdomain/lexical/ifcrelconnectsstructuralmember.htm)


