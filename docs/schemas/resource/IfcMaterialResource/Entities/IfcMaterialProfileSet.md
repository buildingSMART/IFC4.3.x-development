# IfcMaterialProfileSet

The _IfcMaterialProfileSet_ is a designation by which individual material(s) of a prismatic element (for example, beam or column) constructed of a single or multiple material profiles is known.

> NOTE  In case of multiple _MaterialProfiles_, the relative positioning of individual profiles in _IfcMaterialProfileSet_ are defined using the concept of _IfcCompositeProfileDef_ in _IfcProfileResource_ schema; otherwise, only one _MaterialProfile_ is given and defined by an individual _IfcProfileDef_ (subtype).

> HISTORY New entity in IFC4.

## Attributes

### Name
The name by which the material profile set is known.

### Description
Definition of the material profile set in descriptive terms.

### MaterialProfiles
Identification of the profiles from which the material profile set is composed.

### CompositeProfile
Reference to the composite profile definition for which this material profile set associates material to each of its individual profiles. If only a single material profile is used (the most typical case) then no _CompositeProfile_ is asserted.

> NOTE  The referenced _IfcCompositeProfileDef_ instance shall be composed of all of the _IfcProfileDef_ instances which are used via the MaterialProfiles list in the current _IfcMaterialProfileSet_.
