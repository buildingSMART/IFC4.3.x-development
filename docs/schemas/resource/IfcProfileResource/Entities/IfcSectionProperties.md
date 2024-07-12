# IfcSectionProperties

_IfcSectionProperties_ defines the cross section properties for a single longitudinal piece of a cross section. It is a special-purpose helper class for _IfcSectionReinforcementProperties_.
<!-- end of short definition -->


> HISTORY New entity in IFC2x2.

The section piece may be either uniform or tapered. In the latter case an end profile should also be provided. The start and end profiles are assumed to be of the same profile type. Generally only rectangular or circular cross section profiles are assumed to be used.

## Attributes

### SectionType
An indicator whether a specific piece of a cross section is uniform or tapered in longitudinal direction.

### StartProfile
The cross section profile at the start point of the longitudinal section.

### EndProfile
The cross section profile at the end point of the longitudinal section.
