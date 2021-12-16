Earthworks Cuttings
===================

Earthworks Cuttings represent a voiding of an existing or constructed Earthen element (referred to as the voided element)  usually represented by a subtype of _IfcGeotechnicalElement_ or an _IfcEarthworksFill_. The _IfcEarthworksCut_ semantically represents the work of removing/excavating material from the voided element, and the associated geometrical representation is the resulting void created. A _IfcEarthworksCut_ may optionally be filled (fully or partially) with another element such as a foundation, earthen fill or foundation utilising the _IfcRelFillsElement_ relationship.

The resulting geometry of the relationship, when applied, is the result of CSG operations where the _IfcEarthworksCut_ representation is subtracted from the voided element representation.

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
