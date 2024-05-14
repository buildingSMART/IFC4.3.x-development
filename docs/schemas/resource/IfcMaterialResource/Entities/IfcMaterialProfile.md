# IfcMaterialProfile

_IfcMaterialProfile_ is a single and identifiable cross section of an element which is constructed of a number of profiles (one or more).<!-- end of definition -->

> NOTE In case of multiple _MaterialProfiles_, the relative positioning of individual profiles in _IfcMaterialProfileSet_ are defined using the concept of _IfcCompositeProfileDef_ in _IfcProfileResource_ schema; otherwise, only one _MaterialProfile_ is given and defined by an individual _IfcProfileDef_ (subtype).

> HISTORY New entity in IFC4

## Attributes

### Name
The name by which the material profile is known.

### Description
Definition of the material profile in descriptive terms.

### Material
Optional reference to the material from which the profile is constructed.

### Profile
Identification of the profile for which this material profile is associating material.

### Priority
The relative priority of the profile, expressed as normalised integer range [0..100]. Controls how profiles intersect in connections and corners of building elements: A profile from one element protrudes into (i.e. displaces) a profile from another element in a joint of these elements if the former element's profile has higher priority than the latter. The priority value for a material profile in an element has to be set and maintained by software applications in relation to the material profiles in connected elements.

### Category
Category of the material profile, e.g. the role it has in the profile set it belongs to. The list of keywords might be extended by model view definitions, however the following keywords shall apply in general:
* 'LoadBearing' — the material profile having a load bearing function.
* 'Insulation' — the material profile having an insolating function.
* 'Finish' — the material profile being the finish.

### ToMaterialProfileSet
Material profile set in which this material profile is included.

## Formal Propositions

### NormalizedPriority
The _Property_ shall all be given as a normalized integer range [0..100], where 0 is the lowest and 100 the highest priority of the material profile.
