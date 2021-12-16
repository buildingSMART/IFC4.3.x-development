Extruded Area Tapered Parameterized Profile
===========================================



```
concept {
    IfcExtrudedAreaSolidTapered:SweptArea -> IfcProfileDef
    IfcExtrudedAreaSolidTapered:SweptArea -> IfcParameterizedProfileDef_0
    IfcExtrudedAreaSolidTapered:StyledByItem -> IfcStyledItem:Item
    IfcExtrudedAreaSolidTapered:Position -> IfcAxis2Placement3D_0
    IfcExtrudedAreaSolidTapered:Position -> IfcAxis2Placement3D_1
    IfcExtrudedAreaSolidTapered:ExtrudedDirection -> IfcDirection_2
    IfcExtrudedAreaSolidTapered:Depth -> IfcPositiveLengthMeasure
    IfcExtrudedAreaSolidTapered:EndSweptArea -> IfcParameterizedProfileDef_1
    IfcParameterizedProfileDef_0 -> Circle_Hollow_Profile_Definition
    IfcParameterizedProfileDef_0 -> Circle_Profile_Definition
    IfcParameterizedProfileDef_0 -> Ellipse_Profile_Definition
    IfcParameterizedProfileDef_0 -> Rectangle_Hollow_Profile_Definition
    IfcParameterizedProfileDef_0 -> Rectangle_Profile_Definition
    IfcParameterizedProfileDef_0 -> Rectangle_Rounded_Profile_Definition
    IfcParameterizedProfileDef_0 -> C-Shape_Profile_Definition
    IfcParameterizedProfileDef_0 -> I-Shape_Asymmetric_Profile_Definition
    IfcParameterizedProfileDef_0 -> I-Shape_Profile_Definition
    IfcParameterizedProfileDef_0 -> L-Shape_Profile_Definition
    IfcParameterizedProfileDef_0 -> T-Shape_Profile_Definition
    IfcParameterizedProfileDef_0 -> U-Shape_Profile_Definition
    IfcParameterizedProfileDef_0 -> Z-Shape_Profile_Definition
    IfcStyledItem:Name -> IfcLabel
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcAxis2Placement3D_0:Location -> IfcCartesianPoint
    IfcAxis2Placement3D_0:Axis -> IfcDirection_0
    IfcAxis2Placement3D_0:RefDirection -> IfcDirection_1
    IfcExtrudedAreaSolidTapered:SweptArea[binding="Profile"]
}
```
