PolyCurve with Voids Profile Definition
=======================================

Poly curve profile definitions define the closed two-dimensional curve used for the cross-section by a indexed poly curve having straight and circular arc segments.

> NOTE&nbsp; The indexed poly curve has been introduced to provide a less complex and less data set size consuming definition compared to the composite curve.

```
concept {
    IfcArbitraryProfileDefWithVoids:ProfileType -> IfcProfileTypeEnum
    IfcArbitraryProfileDefWithVoids:ProfileName -> IfcLabel
    IfcArbitraryProfileDefWithVoids:OuterCurve -> IfcIndexedPolyCurve_0
    IfcArbitraryProfileDefWithVoids:InnerCurves -> IfcIndexedPolyCurve_1
    IfcIndexedPolyCurve_0:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve_0:Segments -> IfcArcIndex
    IfcIndexedPolyCurve_0:Segments -> IfcLineIndex
    IfcIndexedPolyCurve_0:SelfIntersect -> IfcBoolean
}
```
