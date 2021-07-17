IfcAnnotation
=============

An annotation is an information element within the geometric (and spatial) context of a project, that adds a note or meaning to the objects which constitutes the project model. Annotations include additional points, curves, text, dimensioning, hatching and other forms of graphical notes. It also includes virtual or symbolic representations of additional model components, not representing products or spatial structures, such as event elements, survey points, contour lines or similar.

> NOTE&nbsp; Additional presentation information (often 2D) such as tag number or hatching, that is directly related to a particular product representation is included within the _IfcProductDefinitionShape_ having various _IfcShapeRepresentation_'s of the _IfcElement_ (and its subtypes). Only those presentation information, that cannot be directly related to a single product, have to be wrapped within the _IfcAnnotation_.

If available, the annotation should be related to the spatial context of the project, by containing the annotation within the appropriate level of the building structure (site, facility, facility part or building, storey, or space). This is handled by the _IfcRelContainedInSpatialStructure_ relationship.

The _IfcAnnotation_ can provide specific 0D, 1D, and 2D geometric items as representation of the annotation, offering annotation point, curves, and surfaces. In addition to the predefined type values in _IfcAnnotationTypeEnum_, the following values can be used for the _ObjectType_ (with _PredefinedType_ attribute value USERDEFINED).  

*  **'Annotation point'** is an annotation provided by a point that has additional semantic. The inherited attribute _ObjectType_ should be used to capture the type of point annotation, some suggested values are:  
    *  **'SurveyPoint'**: A single survey point represented by a Cartesian point. A property set may add the conditions (method, accuracy, etc. to the survey point).
    *  **'SurveyArea'**: A set of survey points represented by Cartesian point. These coordinates are determined relative to the coordinates of a reference point, which acts as the datum for the survey. Properties attached apply equally to all points. The difference in elevation of the survey points enables terrain to be determined.

*  **'Annotation curve'** is an annotation provided by a curve that has additional semantic. The inherited attribute _ObjectType_ should be used to capture the type of curve annotation, some suggested values are:   
    *  **'ContourLine'**: A line of constant elevation typically used on geographic maps where the spacing of lines at constant intervals of elevation may be used as an indication of slope.
    *  **'IsoBar'**: A line of constant pressure typically used on weather maps or to show pressure gradient in spaces, chambers or externally.
    *  **'IsoLux'**: A line of constant illumination typically used to show the distribution of illumination levels and/or day lighting in a space or externally.
    *  **'IsoTherm'**: A line of constant temperature typically used to show the distribution and effect of heating or cooling within a space or to show temperature distribution on a geographic map.
    
*  **'Annotation surface'**: is an annotation provided by a surface that has additional semantic. The inherited attribute _ObjectType_ should be used to capture the type of surface annotation, some suggested values are:   
     * **'SurveyArea'**: A surface patch based on survey points.
  

> HISTORY&nbsp; New entity in IFC2x2.
