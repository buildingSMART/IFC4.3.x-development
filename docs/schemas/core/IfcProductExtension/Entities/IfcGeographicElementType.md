An _IfcGeographicElementType_ is used to define an element specification of a geographic element (i.e. the specific product information, that is common to all occurrences of that product type). Geographic element types include for different types of element that may be used to represent information within a geographical landscape external to a building. Within the world of geographic information they are referred to generally as 'features'. _IfcGeographicElementType_'s include:

* point features such as seating, bus shelters, signage, trees;
* linear features such as layby's;
* area features such as ponds, lakes, woods and forests;
* drainage such as catchment, reserver or outfall.


<!-- end of short definition -->

The specification of the specific types are given by the inherited attribute _IfcElementType.ElementType_ given as an _IfcLabel_.

Geographic element types are frequently identified in feature catalogs that are produced for particular purposes. The _IfcGeographicElementType_ entity enables the continued use of existing feature catalogs through capture of their identity and attributes.

Information from feature catalogs might be captured in various ways:

* via property sets, some of which will be specifically defined within the IFC property set catalog whilst others will be created for local use; this is the form of capture that is expected to be most widely used
* through use of the IFC classification model whereby features might be identified through an _IfcClassificationReference_ with additional description; in which case, any further attributes required would still need to be captured in property sets.

> NOTE This is due to the range of choices of element type that are available and their expression in different languages. It is not considered possible to create a reasonably full list of types within an enumeration. It is suggested that selection of the relevant type be drawn from an available 'feature catalog'.

> HISTORY New entity in IFC4.

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
