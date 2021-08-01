PolyCurve with Voids Profile Definition
=======================================

Poly curve profile definitons define the closed two-dimensional curve used for the cross-section by a indexed poly curve having straight and circular arc segments.

> NOTE&nbsp; The indexed poly curve has been introduced to provide a less complex and less data set size consuming definition compared to the composite curve.

```
concept {
    IfcArbitraryProfileDefWithVoids:ProfileType -> IfcProfileTypeEnum
    IfcArbitraryProfileDefWithVoids:ProfileName -> IfcLabel
    IfcArbitraryProfileDefWithVoids:OuterCurve -> IfcIndexedPolyCurve
    IfcArbitraryProfileDefWithVoids:InnerCurves -> IfcIndexedPolyCurve
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Segments -> IfcArcIndex
    IfcIndexedPolyCurve:Segments -> IfcLineIndex
    IfcIndexedPolyCurve:SelfIntersect -> IfcBoolean
}
```
