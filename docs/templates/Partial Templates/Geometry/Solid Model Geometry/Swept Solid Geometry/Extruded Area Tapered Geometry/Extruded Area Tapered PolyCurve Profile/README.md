Extruded Area Tapered PolyCurve Profile
=======================================



```
concept {
    IfcExtrudedAreaSolidTapered:SweptArea -> IfcProfileDef
    IfcExtrudedAreaSolidTapered:StyledByItem -> IfcStyledItem:Item
    IfcExtrudedAreaSolidTapered:EndSweptArea -> IfcDerivedProfileDef
    IfcExtrudedAreaSolidTapered:Position -> IfcAxis2Placement3D_0
    IfcExtrudedAreaSolidTapered:Position -> IfcAxis2Placement3D_1
    IfcExtrudedAreaSolidTapered:ExtrudedDirection -> IfcDirection_2
    IfcExtrudedAreaSolidTapered:Depth -> IfcPositiveLengthMeasure
    IfcProfileDef -> PolyCurve_with_Voids_Profile_Definition
    IfcStyledItem:Name -> IfcLabel
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcDerivedProfileDef -> Transformed_Profile_Definition
    IfcAxis2Placement3D_0:Location -> IfcCartesianPoint
    IfcAxis2Placement3D_0:Axis -> IfcDirection_0
    IfcAxis2Placement3D_0:RefDirection -> IfcDirection_1
    IfcExtrudedAreaSolidTapered:SweptArea[binding="Profile"]
}
```
