Reference SweptSolid PolyCurve Geometry
=======================================

The _Reference SweptSolid PolyCurve Geometry_ is the reference representation of the 3D shape of a product by swept solid models, only allowing for the basic extruded area solids and revolved area solids. Being a reference representation it is normally not displayed and it is not used in a voiding relationship.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Reference'
* _IfcShapeRepresentation_._RepresentationType_ = 'SweptSolid'
* _IfcShapeRepresentation_._Items_ = _IfcExtrudedAreaSolid_, _IfcRevolvedAreaSolid_
* _IfcShapeRepresentation_._Items[1..n].SweptArea_ = _IfcArbitraryClosedProfileDef_, _IfcArbitraryProfileDefWithVoids_
* _IfcShapeRepresentation_._Items[1..n].SweptArea.OuterCurve_ = _IfcIndexedPolyCurve_
* _IfcShapeRepresentation_._Items[1..n].SweptArea.InnerCurves_ = _IfcIndexedPolyCurve_

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcSweptAreaSolid
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
}
```
