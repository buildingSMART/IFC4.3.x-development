Extruded Area Tapered Geometry
==============================



```
concept {
    IfcExtrudedAreaSolidTapered:SweptArea -> IfcProfileDef
    IfcExtrudedAreaSolidTapered:StyledByItem -> IfcStyledItem
    IfcExtrudedAreaSolidTapered:Position -> IfcAxis2Placement3D
    IfcExtrudedAreaSolidTapered:ExtrudedDirection -> IfcDirection
    IfcExtrudedAreaSolidTapered:Depth -> IfcPositiveLengthMeasure
    IfcStyledItem:Name -> IfcLabel
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcAxis2Placement3D:Location -> IfcCartesianPoint
    IfcAxis2Placement3D:Axis -> IfcDirection
    IfcAxis2Placement3D:RefDirection -> IfcDirection
    IfcExtrudedAreaSolidTapered:SweptArea[binding="Profile"]
}
```
