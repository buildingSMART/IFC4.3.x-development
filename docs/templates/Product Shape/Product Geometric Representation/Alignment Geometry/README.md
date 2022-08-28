Alignment Geometry
==================

Base for a standard two (Alignment Geometry Gradient) or three (Alignment Geometry Cant) level layout alignment geometric representation.

_RepresentationIdentifier_ = 'Axis'
_RepresentationType_ = Curve3D'

```
concept {
    IfcLinearElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Axis"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=Curve3D"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    
    IfcShapeRepresentation:Items -> IfcCompositeCurve
    IfcCompositeCurve:Segments -> IfcCurveSegment
    IfcCurveSegment:ParentCurve -> IfcThirdOrderPolynomialSpiral
}
```

# Check and process the Business Logic of alignment
:construction: :construction: :construction: 
There are two important parts where consistency checks on Alignment definition within IFC files will be applied:
- the [Business Logic](#Business-Logic) part (IfcAlignment, IfcAlignmentHorizontal, IfcAlignmentVertical, IfcAlignmentCant, IfcAlignmentHorizontalSegment, IfcAlignmentVerticalSegment and IfcAlignmentCantSegment)
- the [Geometry Definition](#Geometry-Definition) part (IfcCompositeCurve, IfcGradientCurve, IfcSegmentedReferenceCurve, IfcCurveSegment, IfcCircle, IfcClothoid, IfcCosineSpiral, IfcLine, IfcPolynomialCurve, IfcSecondOrderPolynomialSpiral, IfcSeventhOrderPolynomialSpiral, IfcSineSpiral, IfcThirdOrderPolynomialSpiral)


## Business Logic
Each Alignment is build up from segments, it is checked if connected segments are at least continuous given a certain epsilon (what is a proper epsilon value is something to discuss, especially when coping with legacy data there could be considerable inconsistencies).
A check if the values make sense, i.e. a defined StartRadiusOfCurvature / EndRadiusOfCurvature in the context of a LINE does not make sense as well as non-equal values of in the context of a CIRCULARARC. In case of Spirals the radius of curvature actually should be different.

## Geometry Definition
In case geometry is defined the following consistency checks are applied:
- the defined geometry is in line with the business logic (the next part of this document described how this mapping can be applied from mathematical point-of-view)
- the bounded curves (IfcCompositeCurve, IfcGradientCurve and IfcSegmentedReferenceCurve) are structured correctly, i.e. right order of IfcCurveSegments, correct BaseCurve.


### Horizontal Alignment

| Business Logic                             | Geometrical Definition (ParentCurve)       |
|--------------------------------------------|--------------------------------------------|
| [BLOSSCURVE](#BLOSSCURVE-(Horizontal))     | IfcThirdOrderPolynomialSpiral              |
| [CIRCULARARC](#CIRCULARARC-(Horizontal))   | IfcCircle                                  |
| [CLOTHOID](#CLOTHOID-(Horizontal))         | IfcClothoid                                |
| [COSINECURVE](#COSINECURVE-(Horizontal))   | IfcCosine                                  |
| [CUBIC](#CUBIC-(Horizontal))               | IfcPolynomialCurve                         |
| [HELMERTCURVE](#HELMERTCURVE-(Horizontal)) | IfcSecondOrderPolynomialSpiral (two parts) |
| [LINE](#LINE-(Horizontal))                 | IfcLine                                    |
| [SINECURVE](#SINECURVE-(Horizontal))       | IfcSine                                    |
| [VIENNESEBEND](#VIENNESEBEND-(Horizontal)) | IfcSeventhOrderPolynomialSpiral            |

Within the description of the individual transition curves the IfcCurveSegment.SegmentStart is expected to be zero and IfcCurveSegment.SegmentLength to be the segment length or horizontal length (vertical and cant alignment) unless written otherwise. This is not possible in all cases of a CLOTHOID for example as IfcClothoid does not have an attribute for ConstantTerm.


#### BLOSSCURVE (Horizontal)
For the BlossCurve one instance of IfcCurveSegment with ParentCurve IfcThirdOrderPolynomialSpiral will be created.
Change of curvature is defined as:

![](https://i.imgur.com/1ps1mhd.png)

- <details><summary>Calculation of relevant terms</summary>
    
    ```
    double  factor = 
                (endRadiusOfCurvature ? segmentLength / endRadiusOfCurvature : 0.)
                - (startRadiusOfCurvature ? segmentLength / startRadiusOfCurvature : 0.),
            constantTerm  =   0. * factor + (startRadiusOfCurvature ? segmentLength / startRadiusOfCurvature : 0.),
            linearTerm    =   0. * factor,
            quadraticTerm =   3. * factor,
            cubicTerm     = - 2. * factor;
    ``` 
  </details>

- <details><summary>Population of IfcThirdOrderPolynomialSpiral entity</summary>
    
    ```
    cubicTerm     ? segmentLength * pow(std::fabs(cubicTerm),     -1. / 4.) * cubicTerm     / std::fabs(cubicTerm)     : 0.
    quadraticTerm ? segmentLength * pow(std::fabs(quadraticTerm), -1. / 3.) * quadraticTerm / std::fabs(quadraticTerm) : 0.
    linearTerm    ? segmentLength * pow(std::fabs(linearTerm),    -1. / 2.) * linearTerm    / std::fabs(linearTerm)    : 0.
    constantTerm  ? segmentLength * pow(std::fabs(constantTerm),  -1. / 1.) * constantTerm  / std::fabs(constantTerm)  : 0.

    ``` 
  </details>

#### CIRCULARARC (Horizontal)
For the CircularArc one instance of IfcCurveSegment with ParentCurve IfcCircle will be created.
Curvature is constant, i.e. change of curvature is zero.

- <details><summary>Calculation of relevant terms</summary>
    
    ```
    double  radius = startRadiusOfCurvature;
    ``` 
  </details>

- <details><summary>Population of IfcThirdOrderPolynomialSpiral entity</summary>
        
    ```
    radius
    ``` 
  </details>

#### CLOTHOID (Horizontal)
For the Clothoid one instance of IfcCurveSegment with ParentCurve IfcClothoid will be created.
Change of curvature is defined as:

![](https://i.imgur.com/7awWJBT.png)

- <details><summary>Calculation of relevant terms</summary>
    
    ```
    double  factor, offset;
    if ((std::fabs(startRadiusOfCurvature) < std::fabs(endRadiusOfCurvature) && startRadiusOfCurvature) || endRadiusOfCurvature == 0.) {
        factor = segmentLength / startRadiusOfCurvature +
                        (endRadiusOfCurvature ? segmentLength / (endRadiusOfCurvature - startRadiusOfCurvature) : 0.);
        offset = -segmentLength - (endRadiusOfCurvature ? segmentLength * startRadiusOfCurvature / (endRadiusOfCurvature - startRadiusOfCurvature) : 0.);
    }
    else {
        assert(std::fabs(startRadiusOfCurvature) > std::fabs(endRadiusOfCurvature) || startRadiusOfCurvature == 0.);
        factor = segmentLength / endRadiusOfCurvature +
            (startRadiusOfCurvature ? segmentLength / (startRadiusOfCurvature - endRadiusOfCurvature) : 0.);
        offset = startRadiusOfCurvature ? segmentLength * endRadiusOfCurvature / (startRadiusOfCurvature - endRadiusOfCurvature) : 0.;
    }
    ``` 
  </details>

- <details><summary>Population of IfcThirdOrderPolynomialSpiral entity</summary>
    
    ```
    if ((std::fabs(startRadiusOfCurvature) < std::fabs(endRadiusOfCurvature) && startRadiusOfCurvature) || endRadiusOfCurvature == 0.) {
        linearTernm = -startRadiusOfCurvature * pow(std::fabs(factor), 1. / 2.);
    }
    else {
        linearTernm = endRadiusOfCurvature * pow(std::fabs(factor), 1. / 2.);
    }
    ``` 
  </details>

... To Be Completed
