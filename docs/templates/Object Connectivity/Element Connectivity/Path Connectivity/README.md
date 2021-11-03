Path Connectivity
=================

Elements based on an 'Axis' representation such as walls, beams, and columns use a path connectivity relationship to indicate parameters for the connection, indicating which side takes precedence for material layers or profiles.

```
concept {
    IfcElement:ConnectedFrom -> IfcRelConnectsPathElements:RelatedElement
    IfcRelConnectsPathElements:RelatedElement -> IfcElement
    IfcRelConnectsPathElements:ConnectionGeometry -> IfcConnectionCurveGeometry
    IfcRelConnectsPathElements:RelatingPriorities -> IfcInteger
    IfcRelConnectsPathElements:RelatedPriorities -> IfcInteger
    IfcRelConnectsPathElements:RelatedConnectionType -> IfcConnectionTypeEnum
    IfcRelConnectsPathElements:RelatingConnectionType -> IfcConnectionTypeEnum
    IfcConnectionCurveGeometry:CurveOnRelatingElement -> IfcPolyline
    IfcConnectionCurveGeometry:CurveOnRelatedElement -> IfcPolyline
    IfcPolyline:Points -> IfcCartesianPoint
    IfcPolyline:Points -> IfcCartesianPoint
    IfcPolyline:Points -> IfcCartesianPoint
    IfcPolyline:Points -> IfcCartesianPoint
    IfcRelConnectsPathElements:RelatedElement[binding="RelatedElement"]
}
```
