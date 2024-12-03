Earthworks Cuttings
===================

Earthworks Cuttings represent a voiding of an existing or constructed Earthen element (referred to as the voided element)  usually represented by a subtype of _IfcGeotechnicalElement_ or an _IfcEarthworksFill_. The _IfcEarthworksCut_ semantically represents the work of removing/excavating material from the voided element, and the associated geometrical representation is the resulting void created. A _IfcEarthworksCut_ may optionally be filled (fully or partially) with another element such as a foundation, earthen fill or foundation utilising the _IfcRelFillsElement_ relationship.

> NOTE In future editions of the standard, use cases may be elaborated where surface-to-solid or surface-to-surface Boolean operations are specified to allow procedurally modelling the geometric outcomes of the excavation operation in case of terrains exchanged as surface models. Currently, no CSG operation is expected to be performed on import for this template.

```
concept {
    IfcElement:HasOpenings -> IfcRelVoidsElement:RelatingBuildingElement
    IfcRelVoidsElement:RelatedOpeningElement -> IfcEarthworksCut
    IfcEarthworksCut:FillsVoids -> IfcRelFillsElement:RelatedBuildingElement
    IfcEarthworksCut:PredefinedType -> IfcEarthworksCutTypeEnum
    IfcRelFillsElement:RelatedBuildingElement -> IfcCourse
    IfcRelFillsElement:RelatedBuildingElement -> IfcDeepFoundation
    IfcRelFillsElement:RelatedBuildingElement -> IfcEarthworksFill
    IfcRelFillsElement:RelatedBuildingElement -> IfcFooting
    IfcRelFillsElement:RelatedBuildingElement -> IfcPavement
    IfcRelFillsElement:RelatedBuildingElement -> IfcSlab
    IfcElement:HasOpenings[binding="HasOpenings"]
    IfcRelVoidsElement:RelatedOpeningElement[binding="RelatedEarthworksCut"]
    IfcEarthworksCut:FillsVoids[binding="FillsVoids"]
    IfcRelFillsElement:RelatedBuildingElement[binding="RelatedBuiltElement"]
    IfcEarthworksCut:PredefinedType[binding="EarthworksCutType"]
}
```
