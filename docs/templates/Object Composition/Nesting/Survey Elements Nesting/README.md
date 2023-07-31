Survey Elements Nesting
=======================

The ordered arrangement of survey annotations, such as point, lines, curves.

For set of survey elements where the order of items is not relevant (e.g., point clouds or collections of survey string lines), the Survey Elements Grouping template can be used.

> NOTE  Having an _IfcAnnotation_ nesting a list of _IfcAnnotation_'s, properties can be associated to the each annotation of the list (i.e., to each point and line) as well as to the annotation collecting all survey elements.

```
concept {
    IfcAnnotation:IsNestedBy -> IfcRelNests_0:RelatingObject
    IfcRelNests_0:RelatedObjects -> IfcAnnotation_1
    IfcAnnotation:PredefinedType -> SURVEY_
    IfcAnnotation_1:PredefinedType -> SURVEY
}
```