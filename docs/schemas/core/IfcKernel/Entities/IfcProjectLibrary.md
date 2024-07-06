An _IfcProjectLibrary_ collects all library elements that are included within a referenced project data set.

<!-- end of short definition -->


Examples for project libraries include:

* type libraries (also called style or family libraries): a collection of subtypes of _IfcTypeObject_
* property definition libraries: a collection of _IfcPropertySetTemplate_ or _IfcPropertyTemplate_ entities

The inherited attributes _RepresentationContext_ and _UnitsInContext_ have the following meaning:

* Context of the representations used within the project library. When the project library includes shape representations for its library type objects, one or several geometric representation contexts need to be included that define the coordinate system, the coordinate space dimensions, and/or the precision factor,
* Units locally assigned to measure types used within the context of this project library.

> NOTE It is generally discouraged to use a different length measure and plane angle measure in an included project library compared with the project itself. It may lead to unexpected results for the shape representation of items included in the project library.

Instances of _IfcProjectLibrary_ are assigned to the project context using the _IfcRelDeclares_ relationship and accessible through the inverse attribute _HasContext_. Individual object types and property (set) templates are assigned to the _IfcProjectLibrary_ using the _IfcRelDeclares_ relationship and are accessible through the inverse attribute _Declares_. An _IfcProjectLibrary_ may be decomposed into sub libraries using the relationship _IfcRelNests_. Sub libraries are accessed by the _IfcProjectLibrary_ through the inverse attribute _IsNestedBy_.

> HISTORY New entity in IFC4.
