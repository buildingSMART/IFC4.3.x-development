IfcNavigationElement
====================
A navigation element is an active or passive built element who's primary
function is provide navigational instructions and warnings to vessels, this
could be in the form of a floating buoy, a fixed beacon.  
Navigation elements can aggregate other components and elements to form the
entire structure. this might include frame structure to form the body,
instances of [_IfcSign_]($element://{4BE0513F-EDAF-4911-92C7-421EA6CD62A3})
for signage or instances of
[_IfcSignal_]($element://{15911371-83A2-4660-B0A2-B479E9560615}) for
supplementary lights an/or sound signals.  


Attribute definitions
---------------------
| Attribute      | Description                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PredefinedType | Identifies the predefined type of a navigational element from which the type modelled, may be set. This type may associate additional specific property sets.NOTE The PredefinedType shall only be used, if no [_IfcNavigationElementType_]($element://{632D826D-90EE-4587-8EE3-DCF77AD5CE12})[ __]($element://{B09C5B5F-9AC4-4620-8F66-3DAC7AC707EA}) is assigned, providing its own IfcNavigationElementType.PredefinedType. |

