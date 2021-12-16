Extruded Area Standardized Profile
==================================



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
    IfcProfileDef_0 -> C-Shape_Profile_Definition
    IfcProfileDef_0 -> I-Shape_Asymmetric_Profile_Definition
    IfcProfileDef_0 -> I-Shape_Profile_Definition
    IfcProfileDef_0 -> L-Shape_Profile_Definition
    IfcProfileDef_0 -> T-Shape_Profile_Definition
    IfcProfileDef_0 -> U-Shape_Profile_Definition
    IfcProfileDef_0 -> Z-Shape_Profile_Definition
    IfcStyledItem_0:Styles -> IfcSurfaceStyle
    IfcStyledItem_0:Name -> IfcLabel
    IfcExtrudedAreaSolid:SweptArea[binding="Profile"]
}
```
