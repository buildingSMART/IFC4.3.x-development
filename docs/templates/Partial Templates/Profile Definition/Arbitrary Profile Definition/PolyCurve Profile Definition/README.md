PolyCurve Profile Definition
============================

Poly curve profile definitions define the closed two-dimensional curve used for the cross-section by a indexed poly curve having straight and circular arc segments.

> NOTE&nbsp; The indexed poly curve has been introduced to provide a less complex and less data set size consuming definition compared to the composite curve.

```
concept {
    IfcArbitraryClosedProfileDef:ProfileType -> IfcProfileTypeEnum
    IfcArbitraryClosedProfileDef:ProfileName -> IfcLabel
    IfcArbitraryClosedProfileDef:OuterCurve -> IfcIndexedPolyCurve
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Segments -> IfcLineIndex
    IfcIndexedPolyCurve:Segments -> IfcArcIndex
    IfcIndexedPolyCurve:SelfIntersect -> IfcBoolean
}
```
