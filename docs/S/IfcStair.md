IfcStair
========
A stair is a vertical passageway allowing occupants to walk (step) from one
floor level to another floor level at a different elevation. It may include a
landing as an intermediate floor slab.  
NOTE Definition according to ISO 6707-1: Construction comprising a succession
of horizontal stages (steps or landings) that make it possible to pass on foot
to other levels.  
The [_IfcStair_]($element://{0337199C-5D07-4169-8EC0-DBBFF9379F50}) shall
either be represented:  

  

  * as a stair assembly entity that aggregates all parts (stair flight, landing, etc. with own representations), or
  

  * as a single stair entity without decomposition including all representation directly at the stair entity.
  

  
NOTE In case of an
[_IfcStair_]($element://{0337199C-5D07-4169-8EC0-DBBFF9379F50}) being the
aggregate of all parts of the stair the aggregation is handled by the
[_IfcRelAggregates_]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5})
relationship, relating an
[_IfcStair_]($element://{0337199C-5D07-4169-8EC0-DBBFF9379F50}) with the
related
[__IfcStairFlight__]($element://{4DE4D930-4828-4b9a-BD82-23AB19ACEA81}) and
landings, [_IfcSlab_]($diagram://{1182D5EE-2F52-4bc3-BE1D-334563D6DA07}) with
PredefinedType=LANDING.
[_IfcRailing_]($element://{89899895-CA28-49ad-B428-BE0AA0DB81A9})'s belonging
to the stair may also be included into the aggregation.  
NOTE Model View Definitions and implementer agreements may restrict the
[_IfcStair_]($element://{0337199C-5D07-4169-8EC0-DBBFF9379F50}) being an
assembly to not have an independent shape representation, but to always
require that the decomposed parts have a shape representation. In this case,
at least the ''Body'' geometric representations shall not be provided directly
at [_IfcStair_]($element://{0337199C-5D07-4169-8EC0-DBBFF9379F50}) if it is an
assembly. The ''Body'' geometric representation of the
[_IfcStair_]($element://{0337199C-5D07-4169-8EC0-DBBFF9379F50}) is then the
sum of the ''Body'' shape representation of the parts within the decomposition
structure.  
HISTORY New entity in IFC2.0.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcstair.htm)


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

