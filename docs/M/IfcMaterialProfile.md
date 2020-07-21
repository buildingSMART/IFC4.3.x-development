IfcMaterialProfile
==================
_IfcMaterialProfile_ is a single and identifiable cross section of an element
which is constructed of a number of profiles (one or more).  
  
> NOTE  In case of multiple _MaterialProfiles_, the relative positioning of
> individual profiles in _IfcMaterialProfileSet_ are defined using the concept
> of _IfcCompositeProfileDef_ in _IfcProfileResource_ schema; otherwise, only
> one _MaterialProfile_ is given and defined by an individual _IfcProfileDef_
> (subtype).  
  
> HISTORY\S\ New entity in IFC4  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcmaterialresource/lexical/ifcmaterialprofile.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name        | The name by which the material profile is known.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Description | Definition of the material profile in descriptive terms.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Priority    | The relative priority of the profile, expressed as normalised integer range [0..100]. Controls how profiles intersect in connections and corners of building elements: A profile from one element protrudes into (i.e. displaces) a profile from another element in a joint of these elements if the former element''s profile has higher priority than the latter. The priority value for a material profile in an element has to be set and maintained by software applications in relation to the material profiles in connected elements. |
| Category    | Category of the material profile, e.g. the role it has in the profile set it belongs to. The list of keywords might be extended by model view definitions, however the following keywords shall apply in general:\X\0D* ''LoadBearing'' -- the material profile having a load bearing function.\X\0D* ''Insulation'' -- the material profile having an insolating function.\X\0D* ''Finish'' -- the material profile being the finish.                                                                                                        |

Formal Propositions
-------------------
| Rule               | Description   |
|--------------------|---------------|
| NormalizedPriority |               |

Associations
------------
| Attribute            | Description   |
|----------------------|---------------|
| Material             |               |
| Profile              |               |
| ToMaterialProfileSet |               |

