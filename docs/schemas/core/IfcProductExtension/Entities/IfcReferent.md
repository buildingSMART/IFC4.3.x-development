# IfcReferent

_IfcReferent_ defines a position at a particular offset along an alignment curve.

Referents may be used for several scenarios:

* positioning physical elements at common locations along an alignment curve (e.g. bridge piers)
* indicating transitions for cross-sections (e.g. beginning of curvature where road is relatively flat, maximum curvature having super-elevated cross-slope to accommodate design speed)
* indicating events at a specific location (e.g. change in width or superelevation)
* indicating broken chainage where distance measurements reset or reverse directions
* indicating domain-specific design parameters (via property sets) at locations along an alignment curve

## Attributes

### PredefinedType
Predefined types to define the particular type of the referent.

### RestartDistance
Optional value in case of broken linear referencing required to keep stationing further down the alignment unchanged.
