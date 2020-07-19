IfcCoordinateReferenceSystem
============================
The _IfcCoordinateReferenceSystem_ is a definition of a coordinate reference
system by means of qualified identifiers only. The interpretation of the
identifier is expected to be well-known to the receiving software.  
  
{ .extDef}  
> NOTE  Definition from OpenGIS Abstract Specification, Topic 2:  
> A coordinate reference system is a coordinate system which is related to the
> real world by a datum. The coordinate system is composed of a set of
> coordinate axes with specified units of measure. The datum specifies the
> relationship of a coordinate system to the earth. The resulting combination
> of coordinate system and datum is a coordinate reference system.  
  
The unambiguous identifier by which the coordinate reference system is know,
is stored in the _Name_ attribute. Well defined identifiers include the
geodetic and often also the vertical datum. In these cases the _GeodeticDatum_
and the _VerticalDatum_ can be omitted.  
  
> EXAMPLE  The identifier ''EPSG:25832'' defines the geodetic datum ''ETRS89''
> in additon to the projection and the zone. ''EPSG:5555'' defined the
> geodetic datum ''ETRS89'' and the vertical datum ''DHHN92''.  
  
> NOTE  One widely-used, publicly-available authority is the European
> Petroleum Survey Group (EPSG), and use of this authority is currently
> specified in several OGC Implementation Specifications. Software used to
> transport IFC engineering models into GIS applications (and vice versa) is
> expected to have knowledge about the OGC Implementation Specifications.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcrepresentationresource/lexical/ifccoordinatereferencesystem.htm)


