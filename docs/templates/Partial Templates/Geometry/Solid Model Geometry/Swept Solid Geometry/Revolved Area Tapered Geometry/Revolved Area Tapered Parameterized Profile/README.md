Revolved Area Tapered Parameterized Profile
===========================================



```
concept {
    IfcRevolvedAreaSolidTapered:SweptArea -> IfcProfileDef
    IfcRevolvedAreaSolidTapered:SweptArea -> IfcParameterizedProfileDef
    IfcRevolvedAreaSolidTapered:StyledByItem -> IfcStyledItem
    IfcRevolvedAreaSolidTapered:Position -> IfcAxis2Placement3D
    IfcRevolvedAreaSolidTapered:Axis -> IfcAxis1Placement
    IfcRevolvedAreaSolidTapered:Angle -> IfcPlaneAngleMeasure
    IfcRevolvedAreaSolidTapered:EndSweptArea -> IfcParameterizedProfileDef
    IfcRevolvedAreaSolidTapered:EndSweptArea -> IfcDerivedProfileDef
    IfcStyledItem:Name -> IfcLabel
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcAxis2Placement3D:Location -> IfcCartesianPoint
    IfcAxis2Placement3D:Axis -> IfcDirection
    IfcAxis2Placement3D:RefDirection -> IfcDirection
    IfcAxis1Placement:Location -> IfcCartesianPoint
    IfcAxis1Placement:Axis -> IfcDirection
    IfcRevolvedAreaSolidTapered:SweptArea[binding="Profile"]
}
```
