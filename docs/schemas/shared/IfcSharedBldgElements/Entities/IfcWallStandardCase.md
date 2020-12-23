# IfcWallStandardCase

The _IfcWallStandardCase_ defines a wall with certain constraints for the provision of parameters and with certain constraints for the geometric representation. The _IfcWallStandardCase_ handles all cases of walls, that are extruded vertically:

* along the positive z axis of the wall object coordinate system, and
* along the positve z axis of the global (world) coordinate system

and have a single thickness along the path for each wall layer, i.e.:

* parallel sides for straight walls
* co-centric sides for curved walls.

and have either:

* a straight line axis (straight wall), or
* a circular arc axis (round wall).

and shall not have

* aggregated components, that is, parts aggregated to a wall by _IfcRelAggregates_
* shape representation for 'Body' not being an extrusion, or clipped extrusion

The following parameter have to be provided:

* Wall height, taken from the depth of extrusion, provided by the geometric representation.
* Wall thickness, taken from the material layer set usage, attached to the wall
* Wall offset from axis, taken from the material layer set usage, attached to the wall

The _IfcWallStandardCase_ requires the provision of the wall axis either a straight line that is parallel to the x-axis of the object coordinate system, or a circular arc where the tangent at start is parallel to the x-axis of the object coordinate system. The direction of the wall axis shall be the positive direction of that x-axis.

The material of the wall is defined by the _IfcMaterialLayerSetUsage_ and is attached by the _IfcRelAssociatesMaterial_ objectified relationship. It is accessible by the inverse _HasAssociations_ relationship. The material layer set usage has to be given (enforced by where rule).

An 'Axis' and a 'Body' shape representation has to be provided, and it is invalid to exchange a 'Tessellation', 'SurfaceModel', 'Brep' or 'MappedRepresentation' representation for the 'Body' shape representation of the _IfcWallStandardCase_.

> HISTORY&nbsp; New entity in IFC2x.

## Formal Propositions

### HasMaterialLayerSetUsage
A valid instance of _IfcWallStandardCase_ relies on the provision of an _IfcMaterialLayerSetUsage_.
