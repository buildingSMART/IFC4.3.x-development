Clothoid Transition Segment
===========================

A clothoid segment is based on the IfcClothoid where the value for the clothoid constant _A_, known as _flatness_ or _homothetic parameter_ of the clothoid, is specified as:

$$ A=\sqrt{LR}$$

where, L is the length measured from the inflection point; and R is the radius of the clothoid.

```
concept {
    IfcCurveSegment:ParentCurve -> IfcClothoid
    IfcCurveSegment:SegmentStart -> IfcLengthMeasure_0
    IfcCurveSegment:SegmentLength -> IfcLengthMeasure_1
    IfcClothoid:ClothoidConstant -> IfcLengthMeasure
}
```
