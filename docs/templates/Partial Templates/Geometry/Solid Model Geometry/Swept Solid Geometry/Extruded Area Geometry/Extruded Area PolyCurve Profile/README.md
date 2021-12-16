Extruded Area PolyCurve Profile
===============================



```
concept {
    IfcExtrudedAreaSolid:Position -> IfcAxis2Placement3D
    IfcExtrudedAreaSolid:ExtrudedDirection -> IfcDirection_2
    IfcExtrudedAreaSolid:Depth -> IfcPositiveLengthMeasure
    IfcExtrudedAreaSolid:SweptArea -> IfcArbitraryClosedProfileDef
    IfcExtrudedAreaSolid:SweptArea -> IfcArbitraryProfileDefWithVoids
    IfcExtrudedAreaSolid:SweptArea -> IfcProfileDef
    IfcExtrudedAreaSolid:StyledByItem -> IfcStyledItem_0:Item
    IfcExtrudedAreaSolid:StyledByItem -> IfcStyledItem_1:Item
    IfcAxis2Placement3D:Location -> IfcCartesianPoint
    IfcAxis2Placement3D:Axis -> IfcDirection_0
    IfcAxis2Placement3D:RefDirection -> IfcDirection_1
    IfcArbitraryClosedProfileDef -> PolyCurve_Profile_Definition
    IfcArbitraryProfileDefWithVoids -> PolyCurve_with_Voids_Profile_Definition
    IfcStyledItem_0:Styles -> IfcSurfaceStyle
    IfcStyledItem_0:Name -> IfcLabel
    IfcExtrudedAreaSolid:SweptArea[binding="Profile"]
}
```
