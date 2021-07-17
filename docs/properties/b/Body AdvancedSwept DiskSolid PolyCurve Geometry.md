Body AdvancedSwept DiskSolid PolyCurve Geometry
===============================================

The _Body AdvancedSwept DiskSolid PolyCurve Geometry_ is the representation of the 3D shape of a product by swept disk solid models, where the directrix is created by an indexed poly curve.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Body'
* _IfcShapeRepresentation_._RepresentationType_ = 'AdvancedSweptSolid'
* _IfcShapeRepresentation_._Items_ = _IfcSweptDiskSolid_, _IfcSweptDiskSolidPolygonal_
* _IfcShapeRepresentation_._Items[1..n].Directrix_ = _IfcIndexedPolyCurve_
