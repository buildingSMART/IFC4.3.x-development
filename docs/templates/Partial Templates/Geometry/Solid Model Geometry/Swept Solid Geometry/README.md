Swept Solid Geometry
====================



```
concept {
    IfcSweptAreaSolid:SweptArea -> IfcProfileDef
    IfcSweptAreaSolid:StyledByItem -> IfcStyledItem:Item
    IfcStyledItem:Name -> IfcLabel
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcSurfaceStyle -> Surface_Color_Style
    IfcSweptAreaSolid:SweptArea[binding="Profile"]
}
```
