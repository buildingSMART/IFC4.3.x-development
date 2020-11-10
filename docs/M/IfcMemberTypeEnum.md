IfcMemberTypeEnum
=================
This enumeration defines the different types of linear elements an _IfcMember_
or _IfcMemberType_ object can fulfill.  
> HISTORY New enumeration type in IFC2x2.  
{ .change-ifc2x2}  
> IFC2x2 CHANGE The additional identifiers CHORD, PLATE, STUD are added.  
{ .change-ifc2x3}  
> IFC2x3 CHANGE The additional identifier MULLION are added.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcmembertypeenum.htm)


Attribute definitions
---------------------
| Attribute        | Description                                                                                                                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| STRUT            | A linear element often used within a girder or truss.                                                                                                                                                         |
| STAY_CABLE       | A sloped element suspending a structure (such as bridge deck) from a pylon.                                                                                                                                   |
| POST             | FORMER: A linear member (usually used vertically) within a roof structure to support purlins.PROPOSED: A linear (usually vertical) member used to support something or to mark a point.                       |
| ARCH_SEGMENT     | Individual segment of an arch structure.                                                                                                                                                                      |
| STIFFENING_RIB   | A linear element added to a flange or a web plate of a girder for local stiffening.                                                                                                                           |
| STRUCTURALCABLE  | A linear cable element used to secure or stabilise a structure by resisting lateral and longitudinal loading through tension only, but cannot resist compression. usually formed of a flexible cable or wire. |
| STUD             |                                                                                                                                                                                                               |
| RAFTER           | A linear elements used to support roof slabs or roof covering, usually used with slope.                                                                                                                       |
| BRACE            | A linear element (usually sloped) often used for bracing of a girder or truss.                                                                                                                                |
| PLATE            |                                                                                                                                                                                                               |
| TIEBAR           | A linear bar element used to secure or stabilise a structure by resisting lateral and longitudinal loading through tension and or compression. usually formed by a solid bar.                                 |
| MEMBER           | A linear element within a girder or truss with no further meaning.                                                                                                                                            |
| COLLAR           | A linear element (usually used horizontally) within a roof structure to connect rafters and posts.                                                                                                            |
| STRINGER         | A linear element used to support stair or ramp flights, usually used with slope.                                                                                                                              |
| SUSPENSION_CABLE | A suspended element, typically comprising steel wire, sheath, etc.                                                                                                                                            |
| CHORD            | Upper or lower longitudinal member of a truss, used horizontally or sloped.                                                                                                                                   |
| PURLIN           | A linear element (usually used horizontally) within a roof structure to support rafters.                                                                                                                      |
| MULLION          | A linear element within a curtain wall system to connect two (or more) panels.                                                                                                                                |
| SUSPENDER        | A vertical element suspending a structure (such as bridge deck) from a suspension cable or an arch.                                                                                                           |

