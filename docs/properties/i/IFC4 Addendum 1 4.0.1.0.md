IFC4 Addendum 1 4.0.1.0
=======================

{ .std}
The first Addendum of the IFC4 release has the main scope to provide documentation improvements, resolve issues that had occurred since the official release of IFC4 in March 2013, and to addresses implementation issues and concerns.

The main change incorporated into IFC4 ADD1 schema is:

* Improvement and simplification of the explicit geometric representation of composite curves: addition of a new geometric item for indexed based poly curves. It requires the addition of the following entities and types: 
    * entities _IfcIndexedPolyCurve_, _IfcCartesianPointList2D_
    * select type _IfcSegmentIndexSelect_
    * defined types _IfcArcIndex_, _IfcLineIndex_ 

Minor corrections and improvements to the IFC4 ADD1 schema include:

* Use of defined types throughout the schema, i.e. using _IfcInteger_ instead of <emINTEGER, including the addition of _IfcBinary_
* Use of the new type _IfcPositiveInteger_ to restrict the indices used e.g. for tessellated items to positive, one-based integers
* Adding the missing attribute _LongName_ to _IfcBuildingSystem_ in order to make it consistent with _IfcDistributionSystem_.
* Promoting the inverse attribute _HasCoverings_ from _IfcBuildingElement_ to _IfcElement_ to enable the inverse navigation also for _IfcDistributionElement_
* Adding the inverse attribute _HasCoordinateOperation_ to _IfcGeometricRepresentationSystem_ and _IfcCoordinateReferenceSystem_ to enable the inverse navigation to the GIS coordinate transformation
* Making the indespensible _Name_ attribute mandatory at _IfcCoordinateReferenceSystem_ while making the _GeodeticDatum_ optional
* Changing the cardinality of the inverse attribute _DefinesOccurrence_ at _IfcPropertySetDefinition_ to allow property sets to be shared by many such relationships
* Adding the where rule _NoCoordOperation_ to _IfcGeometricRepresentationSubContext_ to prevent the use of conflicting GIS transformations of sub contexts
* Adding the where rule _UnboundedSurface_ to _IfcBoxedHalfSpace_ to prevent the use of bounded surfaces as clipping planes
* Adding the where rule _UniquePropertySetNames_ at _IfcObject_ and _IfcTypeObject_ to enforce property sets attached to a single object to have unique names
* Remove the where rule _HasOwnerHistory_ at _IfcProject_ to enable model views not using owner history information
* Remove the where rule _CorrectShapeDecomposition_ at _IfcRamp_, _IfcRoof_, _IfcStair_ to enable model views to determine correct use of geometric shape representations
