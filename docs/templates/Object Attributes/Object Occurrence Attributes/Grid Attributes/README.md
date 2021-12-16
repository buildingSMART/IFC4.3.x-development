Grid Attributes
===============

Grids may be used to provide a layout reference for building elements.

```
concept {
    IfcGrid:PredefinedType -> IfcGridTypeEnum
    IfcGrid:UAxes -> IfcGridAxis_0
    IfcGrid:VAxes -> IfcGridAxis_1
    IfcGrid:WAxes -> IfcGridAxis_2
    IfcGridAxis_0:AxisTag -> IfcLabel_0
    IfcGridAxis_0:AxisCurve -> IfcIndexedPolyCurve_0
    IfcGridAxis_0:AxisCurve -> IfcCircle_0
    IfcGridAxis_0:SameSense -> IfcBoolean_0
    IfcGridAxis_1:AxisTag -> IfcLabel_1
    IfcGridAxis_1:AxisCurve -> IfcIndexedPolyCurve_1
    IfcGridAxis_1:AxisCurve -> IfcCircle_1
    IfcGridAxis_1:SameSense -> IfcBoolean_1
    IfcGrid:UAxes[binding="UAxes"]
    IfcGrid:VAxes[binding="VAxes"]
    IfcGrid:WAxes[binding="WAxes"]
}
```
