IfcColumnTypeEnum
=================
This enumeration defines the different predefined types of columns that can
further specify an _IfcColumn_ or _IfcColumnType_.  
  
> HISTORY  New Enumeration in IFC2x2.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifccolumntypeenum.htm)


Attribute definitions
---------------------
| Attribute        | Description                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PIERSTEM         | An individual vertical part of a pier, may be a simple column, i.e. no breakdown into segments or separate structural parts such as flanges and web(s), or may be an aggregation of segments and/or parts. |
| PIERSTEM_SEGMENT | A vertical segment of a pier column.                                                                                                                                                                       |
| PILASTER         | A column element embedded within a wall that can be required to be load bearing but may also only be used for decorative purposes.                                                                         |
| COLUMN           | A standard member usually vertical and requiring resistance to vertical forces by compression but also sometimes to lateral forces.                                                                        |
| STANDCOLUMN      | A column transmitting vertical loads from superstructure to an arch below it.                                                                                                                              |

