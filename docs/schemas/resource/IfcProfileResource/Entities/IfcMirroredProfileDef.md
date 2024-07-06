The _IfcMirroredProfileDef_ defines the profile by mirroring the parent profile about the y axis of the parent profile coordinate system. That is, left and right of the parent profile are swapped.

<!-- end of short definition -->


Notes:

_IfcMirroredProfileDef_ is primarily useful together with _IfcCShapeProfileDef_, _IfcLShapeProfileDef_, _IfcUShapeProfileDef_, or _IfcZShapeProfileDef_ as parent profile but can be used with other parent profile types as well.

Mirroring of an _IfcParameterizedProfileDef_ is performed after translation and rotation according to its _Position_ attribute. For example, if the parent profile's _Position_ offsets it by half of its width to the right, then the mirrored profile will be offset by half of its width to the left.

Mirroring about the x axis, i.e. swapping top and bottom, can be achieved by mirroring about the y axis coupled with 180 degree rotation about the z axis. In general, rotation happens in a containing object such as _IfcSweptAreaSolid_, i.e. after mirroring by _IfcMirroredProfileDef_ was performed. If the parent profile is an _IfcParameterizedProfileDef_, rotation can alternatively happen already in the parent profile by means of its _Position_ attribute, i.e. before mirroring by _IfcMirroredProfileDef_ was performed.

> HISTORY New entity in IFC4.

## Attributes

### Operator

