# IfcElement

An element is a generalization of all components that make up an AEC product.

Elements are physically existent objects, although they might be void elements, such as holes. Elements either remain permanently in the AEC product, or only temporarily, as formwork does. Elements can be either assembled on site or pre-manufactured and built in on site.

> EXAMPLE&nbsp; Examples of elements in a building construction context are walls, floors, windows and recesses.

The elements can be logically contained by a spatial structure element that constitutes a certain level within a project structure hierarchy (site, building, storey or space). This is done by using the _IfcRelContainedInSpatialStructure_ relationship. An element can have material and quantity information assigned through the _IfcRelAssociatesMaterial_ and _IfcRelDefinesByProperties_ relationship.

In addition an element can be declared to be a specific occurrence of an element type (and thereby be defined by the element type properties) using the _IfcRelDefinesByType_ relationship. An element can also be defined as an element assembly that is a group of semantically and topologically related elements that form a higher level part of the AEC product. Those element assemblies are defined by virtue of the _IfcRelAggregates_ relationship.

> EXAMPLE&nbsp; Examples for element assembly are complete Roof Structures, made by several Roof Areas, or a Stair, composed by Flights and Landings.

Elements that performs the same function may be grouped by an "Element Group By Function". It is realized by an instance of _IfcGroup_ with the _ObjectType_ ='ElementGroupByFunction'.

> HISTORY&nbsp; New entity in IFC1.0

## Attributes

### Tag
The tag (or label) identifier at the particular instance of a product, e.g. the serial number, or the position number. It is the identifier at the occurrence level.

### FillsVoids
Reference to the _IfcRelFillsElement_ Relationship that puts the element as a filling into the opening created within another element.

### ConnectedTo
Reference to the element connection relationship. The relationship then refers to the other element to which this element is connected to.

### IsInterferedByElements
Reference to the interference relationship to indicate the element that is interfered. The relationship, if provided, indicates that this element has an interference with one or many other elements.
> NOTE&nbsp; There is no indication of precedence between _IsInterferedByElements_ and _InterferesElements_.

{ .change-ifc2x4}
> IFC4 CHANGE New inverse relationship.

### InterferesElements
Reference to the interference relationship to indicate the element that interferes. The relationship, if provided, indicates that this element has an interference with one or many other elements.
> NOTE&nbsp; There is no indication of precedence between _IsInterferedByElements_ and _InterferesElements_.

{ .change-ifc2x4}
> IFC4 CHANGE New inverse relationship.

### HasProjections
Projection relationship that adds a feature (using a Boolean union) to the _IfcBuildingElement_.

### HasOpenings
Reference to the _IfcRelVoidsElement_ relationship that creates an opening in an element. An element can incorporate zero-to-many openings. For each opening, that voids the element, a new relationship _IfcRelVoidsElement_ is generated.

### IsConnectionRealization
Reference to the connection relationship with realizing element. The relationship, if provided, assigns this element as the realizing element to the connection, which provides the physical manifestation of the connection relationship.

### ProvidesBoundaries
Reference to space boundaries by virtue of the objectified relationship _IfcRelSpaceBoundary_. It defines the concept of an element bounding spaces.

### ConnectedFrom
Reference to the element connection relationship. The relationship then refers to the other element that is connected to this element.

### ContainedInStructure
Containment relationship to the spatial structure element, to which the element is primarily associated. This containment relationship has to be hierachical, i.e. an element may only be assigned directly to zero or one spatial structure.

### HasCoverings
Reference to _IfcCovering_ by virtue of the objectified relationship _IfcRelCoversBldgElement_. It defines the concept of an element having coverings associated.

### HasSurfaceFeatures
Reference to the _IfcRelAdheresToElement_ relationship that adheres a _IfcSurfaceFeature_ to an element. An element can incorporate zero-to-many surface features in one relationship.
