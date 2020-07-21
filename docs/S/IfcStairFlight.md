IfcStairFlight
==============
A stair flight is an assembly of building components in a single "run" of
stair steps (not interrupted by a landing). The stair steps and any stringers
are included in the stair flight. A winder is also regarded a part of a stair
flight.  
  
An _IfcStairFlight_ is normally aggregated by an _IfcStair_ through the
_IfcRelAggregates_ relationship, the stair flight is then included in the set
of _IfcRelAggregates.RelatedObjects_. An _IfcStairFlight_ normally connects
the floor slab of zero to two different storeys (or partial storeys, or
landings) within a building. The connection relationship between the
_IfcStairFlight_ and the _IfcSlab_ can be expressed using the
_IfcRelConnectsElements_ relationship.  
  
> HISTORY  New entity in IFC2.0.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcstairflight.htm)


Attribute definitions
---------------------
| Attribute      | Description                                                                                                                                                                                                                                                                                                           |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NumberOfRisers | Number of the risers included in the stair flight\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE The attribute has been deprecated it shall only be exposed with a NIL value. Use _Pset_StairFlightCommon.NumberOfRisers_ instead.                                                                                           |
| NumberOfTreads | Number of treads included in the stair flight.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE The attribute has been deprecated it shall only be exposed with a NIL value. Use _Pset_StairFlightCommon.NumberOfTreads_ instead.                                                                                              |
| RiserHeight    | Vertical distance from tread to tread. The riser height is supposed to be equal for all stairs in a stair flight.\X\0D \X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE The attribute has been deprecated it shall only be exposed with a NIL value. Use _Pset_StairFlightCommon.RiserHeight_ instead.                        |
| TreadLength    | Horizontal distance from the front to the back of the tread. The tread length is supposed to be equal for all steps of the stair flight.\X\0D \X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE The attribute has been deprecated it shall only be exposed with a NIL value. Use _Pset_StairFlightCommon.TreadLength_ instead. |

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

