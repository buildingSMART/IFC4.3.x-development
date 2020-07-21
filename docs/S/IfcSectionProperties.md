IfcSectionProperties
====================
_IfcSectionProperties_ defines the cross section properties for a single
longitudinal piece of a cross section. It is a special-purpose helper class
for _IfcSectionReinforcementProperties_.  
  
> HISTORY  New entity in IFC2x2.  
  
The section piece may be either uniform or tapered. In the latter case an end
profile should also be provided. The start and end profiles are assumed to be
of the same profile type. Generally only rectangular or circular cross section
profiles are assumed to be used.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcprofileresource/lexical/ifcsectionproperties.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                               |
|-------------|-----------------------------------------------------------------------------------------------------------|
| SectionType | An indicator whether a specific piece of a cross section is uniform or tapered in longitudinal direction. |

Associations
------------
| Attribute    | Description   |
|--------------|---------------|
| EndProfile   |               |
| StartProfile |               |
|              |               |

