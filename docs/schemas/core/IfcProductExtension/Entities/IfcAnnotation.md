An annotation is an information element within the geometric (and spatial) context of a project, that adds a note or meaning to the objects which constitutes the project model. Annotations include additional points, curves, text, dimensioning, hatching and other forms of graphical notes. It also includes virtual or symbolic representations of additional model components, not representing products or spatial structures, such as survey points and lines, contour lines or similar.

<!-- end of short definition -->


> NOTE Additional presentation information (often 2D) such as tag number or hatching, that is directly related to a particular product representation is included within the _IfcProductDefinitionShape_ having various _IfcShapeRepresentation_'s of the _IfcElement_ (and its subtypes). Only those presentation information, that cannot be directly related to a single product, have to be wrapped within the _IfcAnnotation_.

If available, the annotation should be related to the spatial context of the project, by containing the annotation within the appropriate level of the building structure (site, facility, facility part or building, storey, or space). This is handled by the _IfcRelContainedInSpatialStructure_ relationship.

The predefined type values in _IfcAnnotationTypeEnum_ suggest some of the type of annotations that can be used.

> HISTORY New entity in IFC2x2.

## Attributes

### ContainedInStructure
Relationship to a spatial structure element, to which the associate is primarily associated.

### PredefinedType

## Concepts

### Annotation 2D Geometry

The Annotation 2D Geometry concept template applies to this entity as shown below:

| Identifier | Type   | Items     | Description     |
|------------|--------------|-----------------------|--------------------------------|
| Annotation | Annotation2D | IfcGeometricCurveSet | Any point or curve    |
| Annotation | Annotation2D | IfcAnnotationFillArea | Area for hatching    |
| Annotation | Annotation2D | IfcTextLiteral  | Text literal for applying text |


### Annotation 3D Geometry

The Annotation 3D Geometry concept template applies to this entity as shown below:

| Identifier | Type   | Items   | Description            |
|------------|--------------|-----------------|---------------------------------------------------------|
| Annotation | GeometricSet | IfcGeometricSet | Any point, curve or surface representing the annotation |

### Single Survey Point


### Single Survey Point Linearly Placed


### Set Of Survey Points


### Single Survey Line


### Survey Elements Grouping


### Survey Elements Nesting


### Property Sets for Objects



