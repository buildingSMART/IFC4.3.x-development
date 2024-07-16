# IfcCourseType

The _IfcCourseType_ provides the type information for _IfcCourse_ occurrences.
<!-- end of short definition -->

A course is a built element whose length greatly exceeds its thickness and often also its width, usually of a single material laid on site on top of another horizontal or nearly horizontal built element. A course is distinctive from a earthworks element in that a course is a graded granular (which can be bound or unbound) material that is generally processed in some fashion, where as earthworks elements are soil earthen based structure that can be formed by removal and transport of general ground material.
Structurally a course does not have capacity to carry loads over open span, or to be removed or replaced as a single unit.

## Attributes

### PredefinedType
Identifies the predefined types of a course element. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
