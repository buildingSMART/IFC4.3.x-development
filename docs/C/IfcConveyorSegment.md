IfcConveyorSegment
==================
A conveyor segment defines an occurrence of a flow segment/ continuous run
within a conveyor system that joins two sections of the system. these can
utilise different carrying methods such as belt, rope, chain, screw etc.  
NOTE Definition according to ISO6707-1: machine that continuously transports
material or objects along a gentle slope using an endless belt, rope or chain,
or rollers.


Attribute definitions
---------------------
| Attribute      | Description                                                                                                                                                                                                                                                                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PredefinedType | Identifies the predefined type of a conveyor segment from which the type modelled, may be set. This type may associate additional specific property sets.NOTE The PredefinedType shall only be used, if no [_IfcConveyorSegmentType_]($element://{4481E1F9-4957-4775-9B65-2C038CCA4F50}) is assigned, providing its own IfcConveyorSegmentType.PredefinedType. |

