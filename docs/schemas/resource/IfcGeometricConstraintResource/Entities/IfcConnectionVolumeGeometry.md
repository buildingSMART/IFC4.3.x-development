# IfcConnectionVolumeGeometry

_IfcConnectionVolumeGeometry_ is used to describe the geometric constraints that facilitate the physical connection (or overlap) of two objects at a volume defined by a solid or closed shell. It is envisioned as a control that applies to the element connection or interference relationships.
<!-- end of short definition -->


The _IfcSolidModel_ (or the _IfcClosedShell_) at the _VolumeOnRelatingElement_ attribute defines the volume where the basic geometry items of the interfering elements overlap. The volume geometry and coordinates are provided within the local coordinate system of the _RelatingElement_, as specified at the subtypes of the relationship _IfcRelConnects_ that utilizes the _IfcConnectionSurfaceGeometry_. Optionally, the same volume geometry and coordinates can also be provided within the local coordinate system of the _RelatedElement_ by using the _VolumeOnRelatedElement_ attribute.

> HISTORY   New entity in IFC4.

## Attributes

### VolumeOnRelatingElement
Volume at which related object overlaps with the relating element, given in the LCS of the relating element.

### VolumeOnRelatedElement
Volume at which related object overlaps with the relating element, given in the LCS of the related element.
