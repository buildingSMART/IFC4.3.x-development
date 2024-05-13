# IfcSectionReinforcementProperties

_IfcSectionReinforcementProperties_ defines the cross section properties of reinforcement for a single longitudinal piece of a cross section with a specific reinforcement usage type.<!-- end of definition -->

> HISTORY  New entity in IFC2x2.

Several sets of cross section reinforcement properties represented by instances of _IfcReinforcementBarProperties_ may be attached to the section reinforcement properties (_IfcReinforcementDefinitionProperties_ of _IfcStructuralElementsDomain_ schema), one for each combination of steel grades and reinforcement bar types and sizes.

## Attributes

### LongitudinalStartPosition
The start position in longitudinal direction for the section reinforcement properties.

### LongitudinalEndPosition
The end position in longitudinal direction for the section reinforcement properties.

### TransversePosition
The position for the section reinforcement properties in transverse direction.

### ReinforcementRole
The role, purpose or usage of the reinforcement, i.e. the kind of loads and stresses it is intended to carry, defined for the section reinforcement properties.

### SectionDefinition
Definition of the cross section profile and longitudinal section type.

### CrossSectionReinforcementDefinitions
The set of reinforcment properties attached to a section reinforcement properties definition.
