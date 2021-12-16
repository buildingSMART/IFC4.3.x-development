Revolved Area PolyCurve Profile
===============================



```
concept {
    IfcRevolvedAreaSolid:Position -> IfcAxis2Placement3D
    IfcRevolvedAreaSolid:Axis -> IfcAxis1Placement
    IfcRevolvedAreaSolid:Angle -> IfcPlaneAngleMeasure
    IfcRevolvedAreaSolid:SweptArea -> IfcArbitraryProfileDefWithVoids
    IfcRevolvedAreaSolid:SweptArea -> IfcProfileDef
    IfcRevolvedAreaSolid:StyledByItem -> IfcStyledItem_0:Item
    IfcRevolvedAreaSolid:StyledByItem -> IfcStyledItem_1:Item
    IfcAxis2Placement3D:Location -> IfcCartesianPoint_0
    IfcAxis2Placement3D:Axis -> IfcDirection_0
    IfcAxis2Placement3D:RefDirection -> IfcDirection_1
    IfcAxis1Placement:Location -> IfcCartesianPoint_1
    IfcAxis1Placement:Axis -> IfcDirection_2
    IfcArbitraryProfileDefWithVoids -> PolyCurve_with_Voids_Profile_Definition
    IfcStyledItem_0:Styles -> IfcSurfaceStyle
    IfcStyledItem_0:Name -> IfcLabel
    IfcRevolvedAreaSolid:SweptArea[binding="Profile"]
}
```
