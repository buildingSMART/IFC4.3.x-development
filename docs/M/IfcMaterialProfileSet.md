IfcMaterialProfileSet
=====================
The _IfcMaterialProfileSet_ is a designation by which individual material(s)
of a prismatic element (for example, beam or column) constructed of a single
or multiple material profiles is known.  
  
> NOTE  In case of multiple _MaterialProfiles_, the relative positioning of
> individual profiles in _IfcMaterialProfileSet_ are defined using the concept
> of _IfcCompositeProfileDef_ in _IfcProfileResource_ schema; otherwise, only
> one _MaterialProfile_ is given and defined by an individual _IfcProfileDef_
> (subtype).  
  
> HISTORY\S\ New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcmaterialresource/lexical/ifcmaterialprofileset.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                  |
|-------------|--------------------------------------------------------------|
| Name        | The name by which the material profile set is known.         |
| Description | Definition of the material profile set in descriptive terms. |

Associations
------------
| Attribute        | Description   |
|------------------|---------------|
| MaterialProfiles |               |
| CompositeProfile |               |
|                  |               |
|                  |               |

