IfcBeamTypeEnum
===============
This enumeration defines the different predefined types of beams that can
further specify an _IfcBeam_ or _IfcBeamType_.  
  
> HISTORY  New enumeration type in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The enumerators HOLLOWCORE and SPANDREL have been added.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcbeamtypeenum.htm)


Attribute definitions
---------------------
| Attribute      | Description                                                                                                                                                                                                                               |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BEAM           | A standard beam usually used horizontally.                                                                                                                                                                                                |
| HATSTONE       | A beam on top of a retaining wall or a wing wall, preventing earth movement.                                                                                                                                                              |
| T_BEAM         | A beam that forms part of a slab construction and acts together with the slab which its carries. Such beams are often of T-shape (therefore the English name), but may have other shapes as well, e.g. an L-Shape or an Inverted-T-Shape. |
| EDGEBEAM       | A beam on the longitudinal edge of bridge slab, usually concrete, providing additional stiffening and protection from the elements.                                                                                                       |
| LINTEL         | A beam or horizontal piece of material over an opening (e.g. door, window).                                                                                                                                                               |
| GIRDER_SEGMENT | A segment of a girder (e.g. each span of a continuous girder).                                                                                                                                                                            |
| DIAPHRAGM      | End portion of a girder transmitting loads to supports and providing moment resistance to adjoining segment.                                                                                                                              |
| JOIST          | A beam used to support a floor or ceiling.                                                                                                                                                                                                |
| CORNICE        | A non-loadbearing beam on the longitudinal edge of bridge slab, usually encasing installations.                                                                                                                                           |
| SPANDREL       | A tall beam placed on the facade of a building. One tall side is usually finished to provide the exterior of the building. Can be used to support joists or slab elements on its interior side.                                           |
| PIERCAP        | A transversal beam on top of a pier (on a single column or extending from one column of a pier to another column of the same pier).                                                                                                       |
| HOLLOWCORE     | A wide often prestressed beam with a hollow-core profile that usually serves as a slab component.                                                                                                                                         |

