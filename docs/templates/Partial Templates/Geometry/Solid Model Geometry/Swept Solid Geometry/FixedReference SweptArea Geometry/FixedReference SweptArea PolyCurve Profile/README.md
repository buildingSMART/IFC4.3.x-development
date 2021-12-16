FixedReference SweptArea PolyCurve Profile
==========================================



```
concept {
    IfcFixedReferenceSweptAreaSolid:SweptArea -> IfcProfileDef
    IfcFixedReferenceSweptAreaSolid:Position -> IfcAxis2Placement3D
    IfcFixedReferenceSweptAreaSolid:Directrix -> IfcIndexedPolyCurve
    IfcFixedReferenceSweptAreaSolid:Directrix -> IfcPcurve
    IfcFixedReferenceSweptAreaSolid:StartParam -> IfcParameterValue_0
    IfcFixedReferenceSweptAreaSolid:EndParam -> IfcParameterValue_1
    IfcFixedReferenceSweptAreaSolid:FixedReference -> IfcDirection
    IfcFixedReferenceSweptAreaSolid:StyledByItem -> IfcStyledItem_0:Item
    IfcFixedReferenceSweptAreaSolid:StyledByItem -> IfcStyledItem_1:Item
    IfcProfileDef -> PolyCurve_with_Voids_Profile_Definition
    IfcStyledItem_0:Styles -> IfcSurfaceStyle
    IfcStyledItem_0:Name -> IfcLabel
    IfcFixedReferenceSweptAreaSolid:SweptArea[binding="Profile"]
}
```
