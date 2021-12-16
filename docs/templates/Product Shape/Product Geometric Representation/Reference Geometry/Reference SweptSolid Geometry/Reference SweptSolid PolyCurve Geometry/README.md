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
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcSweptAreaSolid
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Reference"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=SweptSolid"]
    IfcSweptAreaSolid -> Extruded_Area_PolyCurve_Profile
    IfcSweptAreaSolid -> Revolved_Area_PolyCurve_Profile
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
}
```
