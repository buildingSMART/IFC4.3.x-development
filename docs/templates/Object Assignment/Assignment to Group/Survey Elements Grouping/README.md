Survey Elements Grouping
========================

The assignment of survey annotations, such as point and lines, to a group. The template can be used when the order of the elements is irrelevant, for example for point clouds or collections of survey string lines.

For ordered list of survey elements, use the Survey Elements Nesting template.

> NOTE  Having an _IfcGroup_ grouping a list of _IfcAnnotation_'s, properties can be associated to each annotation (i.e., to each point and line) as well as to the group collecting all survey elements.

```
concept {
    IfcAnnotation:HasAssignments -> IfcRelAssignsToGroup:RelatedObjects
    IfcAnnotation:PredefinedType -> IfcAnnotationTypeEnum
    IfcAnnotationTypeEnum -> constraint_2
    constraint_2[label="=SURVEY"]
    IfcRelAssignsToGroup:RelatingGroup -> IfcGroup:IsGroupedBy
    IfcAnnotation:Name -> IfcLabel_0
    IfcGroup:Name -> IfcLabel_1
    IfcAnnotation:HasAssignments[binding="IsAssigned"]
    IfcGroup:Name[binding="GroupName"]
}
```
