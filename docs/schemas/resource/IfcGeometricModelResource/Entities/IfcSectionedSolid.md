# IfcSectionedSolid

An _IfcSectionedSolid_ is an abstract base type for solids constructed by sweeping potentially variable cross sections along a directrix.

## Attributes

### Directrix
The curve used to define the sweeping operation.

### CrossSections
List of cross sections in sequential order along the _Directrix_.

## Formal Propositions

### DirectrixIs3D
The curve entity which is the underlying directrix shall have the dimensionality of 3.

### ConsistentProfileTypes
The profile type (either AREA or CURVE) shall be consistent within the list of the profiles defining the cross sections.

### SectionsSameType
The entity type for each section must be the same.
