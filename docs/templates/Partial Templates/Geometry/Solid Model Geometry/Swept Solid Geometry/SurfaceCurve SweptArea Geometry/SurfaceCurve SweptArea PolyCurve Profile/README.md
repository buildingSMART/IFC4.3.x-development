SurfaceCurve SweptArea PolyCurve Profile
========================================



```
concept {
    IfcSurfaceCurveSweptAreaSolid:SweptArea -> IfcProfileDef
    IfcSurfaceCurveSweptAreaSolid:Position -> IfcAxis2Placement3D
    IfcSurfaceCurveSweptAreaSolid:Directrix -> IfcIndexedPolyCurve
    IfcSurfaceCurveSweptAreaSolid:Directrix -> IfcPcurve
    IfcSurfaceCurveSweptAreaSolid:StartParam -> IfcParameterValue
    IfcSurfaceCurveSweptAreaSolid:EndParam -> IfcParameterValue
    IfcSurfaceCurveSweptAreaSolid:ReferenceSurface -> IfcSurfaceOfLinearExtrusion
    IfcSurfaceCurveSweptAreaSolid:ReferenceSurface -> IfcSurfaceOfRevolution
    IfcSurfaceCurveSweptAreaSolid:StyledByItem -> IfcStyledItem
    IfcSurfaceCurveSweptAreaSolid:StyledByItem -> IfcStyledItem
    IfcSurfaceCurveSweptAreaSolid:StyledByItem -> IfcStyledItem
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcStyledItem:Name -> IfcLabel
    IfcStyledItem:Name -> IfcLabel
    IfcStyledItem:Name -> IfcLabel
    IfcSurfaceCurveSweptAreaSolid:SweptArea[binding="Profile"]
}
```
