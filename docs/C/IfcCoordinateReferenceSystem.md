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


Attribute definitions
---------------------
| Attribute     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name          | Name by which the coordinate reference system is identified.\X\0D> NOTE  The name shall be taken from the list recognized by the European Petroleum Survey Group EPSG. It should then be qualified by the EPSG name space, for example as ''EPSG:5555''.                                                                                                                                                                                                                                                                                                                                           |
| Description   | Informal description of this coordinate reference system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| GeodeticDatum | Name by which this datum is identified. The geodetic datum is associated with the coordinate reference system and indicates the shape and size of the rotation ellipsoid and this ellipsoid''s connection and orientation to the actual globe/earth. It needs to be provided, if the _Name_ identifier does not unambiguously define the geodetic datum as well.\X\0D\X\0D{ .examples}\X\0D> EXAMPLE  geodetic datums include: { .note}\X\0D> * ED50\X\0D> * EUREF89\X\0D> * WSG84                                                                                                                 |
| VerticalDatum | Name by which the vertical datum is identified. The vertical datum is associated with the height axis of the coordinate reference system and indicates the reference plane and fundamental point defining the origin of a height system. It needs to be provided, if the _Name_ identifier does not unambiguously define the vertical datum as well and if the coordinate reference system is a 3D reference system.\X\0D\X\0D{ .examples}\X\0D> EXAMPLE  vertical datums include: { .note}\X\0D> * DHHN92: the German ''Haupthohennetz''\X\0D> * EVRS2007; the European Vertical Reference System |

Associations
------------
| Attribute              | Description   |
|------------------------|---------------|
|                        |               |
| HasCoordinateOperation |               |

