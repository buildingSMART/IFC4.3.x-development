IfcDistributionSystemEnum
=========================
This enumeration identifies different types of distribution systems. It is
used to designate systems by their function as well as ports of devices within
such systems to restrict connectivity to compatible connections.  
  
> HISTORY  New enumeration in IFC4.  
  
Ports for cable carriers may be connected using _IfcCableCarrierSegment_ and
_IfcCableCarrierFitting_. Type objects for cable carrier segments and fittings
(_IfcCableCarrierSegmentType_ and _IfcCableCarrierFittingType_ that are not
specific to a particular system type may have ports with _PredefinedType_ of
NOTDEFINED which indicates that occurrences of such objects may connect to
ports of any other cable-carrier based port. Valid enumerations for cable
carriers are the same as that for cables, and may be asserted if ports of the
contained cables are all of the same type.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgserviceelements/lexical/ifcdistributionsystemenum.htm)


Attribute definitions
---------------------
| Attribute                   | Description                                                                                                                                                  |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RETURN_CIRCUIT              | A distribution system which forms the intended path for the traction return current and the current under fault conditions.                                  |
| MUNICIPALSOLIDWASTE         | Items consumed and discarded, commonly known as trash or garbage.                                                                                            |
| POWERGENERATION             | A path for power generation.                                                                                                                                 |
| SIGNAL                      | A raw analog signal, such as modulated data or measurements from sensors.                                                                                    |
| GAS                         | Gas-phase materials such as methane or natural gas.                                                                                                          |
| WATERSUPPLY                 | Arbitrary water supply.                                                                                                                                      |
| OVERHEAD_CONTACTLINE_SYSTEM | An overhead contact line system above the upper limit of the train using an overhead contact line and a catenary system to supply current to traction units. |
| ELECTROACOUSTIC             | An amplified audio signal such as for loudspeakers.                                                                                                          |
| COMMUNICATION               | $                                                                                                                                                            |
| CHILLEDWATER                | Nonpotable chilled water, such as circulated through an evaporator.                                                                                          |
| RAINWATER                   | Rainwater resulting from precipitation which directly falls on a parcel.                                                                                     |
| STORMWATER                  | Stormwater resulting from precipitation which runs off or travels over the ground surface.                                                                   |
| VACUUM                      | Vacuum distribution system.                                                                                                                                  |
| AUDIOVISUAL                 | A transport of a single media source, having audio and/or video streams.                                                                                     |
| FUEL                        |                                                                                                                                                              |
| LIGHTING                    |                                                                                                                                                              |
| ELECTRICAL                  | A circuit for delivering electrical power.                                                                                                                   |
| WASTEWATER                  | Water adversely affected in quality by anthropogenic influence, possibly originating from sewage, drainage, or other source.                                 |
| VENT                        | Vent system for wastewater piping systems.                                                                                                                   |
| DOMESTICHOTWATER            | Heated potable water distribution system.                                                                                                                    |
| DOMESTICCOLDWATER           | Unheated potable water distribution system.                                                                                                                  |
| SECURITY                    |                                                                                                                                                              |
| CONTROL                     |                                                                                                                                                              |
| CONDENSERWATER              | Nonpotable water, such as circulated through a condenser.                                                                                                    |
| OPERATIONAL                 | Operating supplies system.                                                                                                                                   |
| FIREPROTECTION              | Fire protection sprinkler system.                                                                                                                            |
| AIRCONDITIONING             | Conditioned air distribution system for purposes of maintaining a temperature range within one or more spaces.                                               |
| SEWAGE                      | Sewage collection system.                                                                                                                                    |
| DRAINAGE                    | Drainage collection system.                                                                                                                                  |
| CHEMICAL                    | Arbitrary chemical further qualified by property set, such as for medical or industrial use.                                                                 |
| DATA                        |                                                                                                                                                              |
| LIGHTNINGPROTECTION         | A path for conducting lightning current to the ground.                                                                                                       |
| REFRIGERATION               | Refrigerant distribution system for purposes of fulfilling all or parts of a refrigeration cycle.                                                            |
| EXHAUST                     | Exhaust air collection system for removing stale or noxious air from one or more spaces.                                                                     |
| CATENARY_SYSTEM             | A longitudinal distribution system that supports contact wires, including catenary wire droppers and stich wires.                                            |
| OIL                         |                                                                                                                                                              |
| CONVEYING                   | Arbitrary supply of substances.                                                                                                                              |
| HAZARDOUS                   | Hazardous material or fluid collection system.                                                                                                               |
| TV                          | A transport of multiple media sources such as analog cable TV, satellite TV, or over-the-air TV.                                                             |
| DISPOSAL                    |                                                                                                                                                              |
| HEATING                     |                                                                                                                                                              |
| TELEPHONE                   |                                                                                                                                                              |
| VENTILATION                 |                                                                                                                                                              |
| EARTHING                    | A path for equipotential bonding, conducting current to the ground.                                                                                          |
| COMPRESSEDAIR               | Compressed air system.                                                                                                                                       |

