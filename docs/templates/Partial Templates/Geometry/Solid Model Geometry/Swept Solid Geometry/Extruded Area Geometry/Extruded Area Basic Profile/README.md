Extruded Area Basic Profile
===========================



```
concept {
    IfcExtrudedAreaSolid:Position -> IfcAxis2Placement3D
    IfcExtrudedAreaSolid:ExtrudedDirection -> IfcDirection_2
    IfcExtrudedAreaSolid:Depth -> IfcPositiveLengthMeasure
    IfcExtrudedAreaSolid:SweptArea -> IfcProfileDef_0
    IfcExtrudedAreaSolid:SweptArea -> IfcProfileDef_1
    IfcExtrudedAreaSolid:StyledByItem -> IfcStyledItem_0:Item
    IfcExtrudedAreaSolid:StyledByItem -> IfcStyledItem_1:Item
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
    IfcExtrudedAreaSolid:SweptArea[binding="Profile"]
}
```
