SurfaceCurve SweptArea PolyCurve Profile
========================================



```
concept {
    IfcSurfaceCurveSweptAreaSolid:SweptArea -> IfcProfileDef
    IfcSurfaceCurveSweptAreaSolid:Position -> IfcAxis2Placement3D
    IfcSurfaceCurveSweptAreaSolid:Directrix -> IfcIndexedPolyCurve
    IfcSurfaceCurveSweptAreaSolid:Directrix -> IfcPcurve
    IfcSurfaceCurveSweptAreaSolid:StartParam -> IfcParameterValue_0
    IfcSurfaceCurveSweptAreaSolid:EndParam -> IfcParameterValue_1
    IfcSurfaceCurveSweptAreaSolid:ReferenceSurface -> IfcSurfaceOfLinearExtrusion
    IfcSurfaceCurveSweptAreaSolid:ReferenceSurface -> IfcSurfaceOfRevolution
    IfcSurfaceCurveSweptAreaSolid:StyledByItem -> IfcStyledItem_0:Item
    IfcSurfaceCurveSweptAreaSolid:StyledByItem -> IfcStyledItem_1:Item
    IfcProfileDef -> PolyCurve_with_Voids_Profile_Definition
    IfcStyledItem_0:Styles -> IfcSurfaceStyle
    IfcStyledItem_0:Name -> IfcLabel
    IfcSurfaceCurveSweptAreaSolid:SweptArea[binding="Profile"]
}
```
