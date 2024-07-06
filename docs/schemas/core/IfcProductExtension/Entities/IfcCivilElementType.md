An _IfcCivilElementType_ is used to define an element specification of an element used within civil engineering works. Civil element types include for different types of element that may be used to represent information for construction works external to a building. _IfcCivilElementType_'s may include:

* linear elements such as sections of a roadway (including carriageway/pavement, verge, median, marker line, kerb etc.);
* elements for connections and junctions including traffic roundabouts, T junctions, 4 way junctions;
* elements for supporting structures such as piers, piles, pylons, and similar.


<!-- end of short definition -->

The specification of the specific types is provided by the inherited attribute _IfcElementType.ElementType_ given as an _IfcLabel_.

> NOTE This is due to the range of choices of element type that are available and their expression in different languages. It is not considered possible to create a reasonably full list of types within an enumeration. It is suggested that selection of the relevant type be drawn from an available 'feature catalog'.

> NOTE The _IfcCivilElementType_ has been introduced as a stub for future extensions of this specification to include an object model for civil engineering works.

> HISTORY New entity in IFC4.

> IFC4.3.0.0 DEPRECATION This entity is deprecated. Usage of a generic element type for civil engineering works is no longer desirable with specific types now provided as subtypes of IfcBuiltElement, IfcEarthworksElement, IfcFacility and IfcGeotechnicalElement.
