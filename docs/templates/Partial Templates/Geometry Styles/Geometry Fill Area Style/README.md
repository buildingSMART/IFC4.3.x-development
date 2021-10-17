Geometry Fill Area Style
========================



```
concept {
    IfcFillAreaStyle:Name -> IfcLabel
    IfcFillAreaStyle:FillStyles -> IfcColourRgb
    IfcFillAreaStyle:FillStyles -> IfcFillAreaStyleHatching
    IfcFillAreaStyle:ModelorDraughting -> IfcBoolean
    IfcFillAreaStyleHatching:HatchLineAppearance -> IfcCurveStyle
    IfcFillAreaStyleHatching:StartOfNextHatchLine -> IfcVector
    IfcFillAreaStyleHatching:PointOfReferenceHatchLine -> IfcCartesianPoint
    IfcFillAreaStyleHatching:PatternStart -> IfcCartesianPoint
    IfcFillAreaStyleHatching:HatchLineAngle -> IfcPlaneAngleMeasure
}
```
