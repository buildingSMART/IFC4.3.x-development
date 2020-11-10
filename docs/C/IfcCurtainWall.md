IfcCurtainWall
==============
A curtain wall is an exterior wall of a building which is an assembly of
components, hung from the edge of the floor/roof structure rather than bearing
on a floor. Curtain wall is represented as a building element assembly and
implemented as a subtype of _IfcBuildingElement_ that uses an
_IfcRelAggregates_ relationship.  
  
{ .extDef}  
> NOTE  Definition according to ISO 6707-1: non load bearing wall positioned
> on the outside of a building and enclosing it.  
  
> HISTORY  New entity in IFC2.0  
  
The geometric representation of _IfcCurtainWall_ is given by the
_IfcProductDefinitionShape_, allowing multiple geometric representations.
Independent ''Body'' geometric representation, as described below, should only
be used when the _IfcCurtainWall_ is not defined as an aggregate. If defined
as an aggregate, the geometric representation is the sum of the
representations of the components within the aggregate.  
  
The geometric representation of _IfcCurtainWall_ is defined using the
following multiple shape representations for its definition:  
  
* Axis: A two-dimensional open curve (for restrictions see below) defining the axis for the curtain wall.   
* This is an optional representation for curtain walls.   
* Body: A surface model or boundary representation model representation defining the 3D shape of the curtain wall.   
* If the _IfcCurtainWall_ has components (referenced by _SELF\\\IfcObject.IsDecomposedBy_) then no independent shape representation with _RepresentationType_ = ''Body'' shall be defined. The body of _IfcCurtainWall_ is then geometrically represented by the shape representation of its components. The components are accessed via _SELF\\\IfcObject.IsDecomposedBy[1].RelatedObjects_.   
* If the _IfcCurtainWall_ has no components defined (empty set of _SELF\\\IfcObject.IsDecomposedBy_) then the _IfcCurtainWall_ may be represented by an shape representation with the _RepresentationIdentifier_ =''Body''.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifccurtainwall.htm)


Attribute definitions
---------------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

