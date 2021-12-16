Path Connectivity
=================

Elements based on an 'Axis' representation such as walls, beams, and columns use a path connectivity relationship to indicate parameters for the connection, indicating which side takes precedence for material layers or profiles.

```
concept {
    IfcElement_0:ConnectedFrom -> IfcRelConnectsPathElements:RelatedElement
    IfcRelConnectsPathElements:RelatedElement -> IfcElement_1
    IfcRelConnectsPathElements:ConnectionGeometry -> IfcConnectionCurveGeometry
    IfcRelConnectsPathElements:RelatingPriorities -> IfcInteger_0
    IfcRelConnectsPathElements:RelatedPriorities -> IfcInteger_1
    IfcRelConnectsPathElements:RelatedConnectionType -> IfcConnectionTypeEnum_0
    IfcRelConnectsPathElements:RelatingConnectionType -> IfcConnectionTypeEnum_1
    IfcConnectionCurveGeometry:CurveOnRelatingElement -> IfcPolyline_0
    IfcConnectionCurveGeometry:CurveOnRelatedElement -> IfcPolyline_1
    IfcPolyline_0:Points -> IfcCartesianPoint_0
    IfcPolyline_1:Points -> IfcCartesianPoint_1
    IfcRelConnectsPathElements:RelatedElement[binding="RelatedElement"]
}
```
