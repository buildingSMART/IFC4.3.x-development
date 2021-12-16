Revolved Area Basic Profile
===========================



```
concept {
    IfcRevolvedAreaSolid:Position -> IfcAxis2Placement3D
    IfcRevolvedAreaSolid:Axis -> IfcAxis1Placement
    IfcRevolvedAreaSolid:Angle -> IfcPlaneAngleMeasure
    IfcRevolvedAreaSolid:SweptArea -> IfcProfileDef_0
    IfcRevolvedAreaSolid:SweptArea -> IfcProfileDef_1
    IfcRevolvedAreaSolid:StyledByItem -> IfcStyledItem_0:Item
    IfcRevolvedAreaSolid:StyledByItem -> IfcStyledItem_1:Item
    IfcAxis2Placement3D:Location -> IfcCartesianPoint
    IfcAxis2Placement3D:Axis -> IfcDirection_0
    IfcAxis2Placement3D:RefDirection -> IfcDirection_1
    IfcProfileDef_0 -> Circle_Hollow_Profile_Definition
    IfcProfileDef_0 -> Circle_Profile_Definition
    IfcProfileDef_0 -> Ellipse_Profile_Definition
    IfcProfileDef_0 -> Rectangle_Hollow_Profile_Definition
    IfcProfileDef_0 -> Rectangle_Profile_Definition
    IfcProfileDef_0 -> Rectangle_Rounded_Profile_Definition
    IfcStyledItem_0:Styles -> IfcSurfaceStyle
    IfcStyledItem_0:Name -> IfcLabel
    IfcRevolvedAreaSolid:SweptArea[binding="Profile"]
}
```
