# IfcOpeningStandardCase

The standard opening, _IfcOpeningStandardCase_, defines an opening with certain constraints for the dimension parameters, position within the voided element, and with certain constraints for the geometric representation. The _IfcOpeningStandardCase_ handles all cases of openings, that:

* are true openings where the opening depth is greater than or equal to the thickness of the element, and the _Predefinedtype_ is set correctly to .OPENING.
* are true recesses where the opening depth is lower than the thickness of the element, and the _Predefinedtype_ is set correctly to .RECESS.
* are extruded perpendicular to the wall plane in case of openings in a wall
* are extruded perpendicular to the slab plane in case of openings in a slab
* have a local placement relative to the local placement of the voided element
* have a 'Body' shape representation with 'SweptSolid' representation type
* have only a single extrusion body within the 'Body' shape representation

> HISTORY  New entity in IFC4

## Concepts

### Body Geometry

The 'Body' representation of IfcOpeningElement can be represented using the representation types 'SweptSolid'. The following attribute values for the IfcShapeRepresentation holding this geometric representation shall be used:

* _IfcShapeRepresentation.RepresentationIdentifier_: 'Body'
* _IfcShapeRepresentation.RepresentationType_: 'SweptSolid'

The following constraints are recommended:

* _IfcShapeRepresentation.Items_ may include a single, or multiple, instances of IfcExtrudedAreaSolid.
* _IfcExtrudedAreaSolid.SweptArea_ shall support IfcRectangleProfileDef, IfcCircleProfileDef and IfcArbitraryClosedProfileDef.
* If multiple instances of IfcExtrudedAreaSolid are used, the extrusion direction of each extrusion should be equal.

There are two main extrusion directions: perpendicular and parallel.

**Perpendicular Swept Solid Representation Type**

For a perpendicular swept solid, _IfcExtrudedAreaSolid.ExtrudedDirection_ shall extrude the profile perpendicular to the element it is voiding. This may be horizontal (perpendicular to the extrusion direction of the voided element such as for wall openings), or vertical (in the extrusion direction of the voided element such as for for floor openings).

![standard opening](../../../../figures/ifcopeningelement_horizontal-layout1.png "Figure FULLEXTRUSION &mdash; Opening with full extrusion")

![recess](../../../../figures/ifcopeningelement_recess-layout1.png "Figure RECESS &mdash; Opening with recess extrusion")

> NOTE  The local placement directions for the IfcOpeningElement in Figure FULLEXTRUSION and Figure RECESS are only given as an example, other directions are valid as well.

> NOTE  Rectangles are now defined centrally, so the placement location has to be set to IfcCartesianPoint(XDim/2,YDim/2)

**Parallel Swept Solid Representation Type**

For a parallel swept solid,_IfcExtrudedAreaSolid.ExtrudedDirection_ shall extrude the profile parallel to the element it is voiding. This may be vertical in the case of walls.

Parallel extrusions shall be used when an opening or recess has a non rectangular foot print geometry that does not change along the height of the opening or recess.

Figure VERTEXTRUDE shows a vertical extrusion with multiple extrusion bodies for the opening. Each extrusion body has a different extrusion length.

![vertical extrusion](../../../../figures/ifcopeningelement_vertical-layout1.png "Figure VERTEXTRUDE &mdash; Opening with multiple extrusions")

> NOTE  The local placement directions for the IfcOpeningElement in Figure VERTEXTRUDE are only given as an example, other directions are valid as well.

### Product Local Placement

The following constraint is mandatory for IfcOpeningStandardCase

* The PlacementRelTo relationship of IfcLocalPlacement should point to the local placement of the same element, which is voided by the opening, i.e. referred to by _VoidsElement.RelatingBuildingElement_.

