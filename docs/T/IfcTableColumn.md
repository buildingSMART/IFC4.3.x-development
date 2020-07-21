IfcTableColumn
==============
An _IfcTableColumn_ is a data structure that captures column information for
use in an _IfcTable_. Each instance defines the identifier, name, description,
and units of measure that are applicable to the columnar data associated with
the _IfcTableRow_ objects.  
  
The use of _IfcTableColumn_ supersedes the _IsHeading_ flag associated with
_IfcTableRow_.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcutilityresource/lexical/ifctablecolumn.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Identifier  | The _Identifier_ identifies the column within the table. If provided, it must be unique within the table. Columns may be cross-referenced across multiple tables by sharing the same column identifier.                                     |
| Name        | The _Name_ is a human-readable caption for the table column. It is not necessarilly unique.                                                                                                                                                 |
| Description | The _Description_ provides human-readable text describing the table column.                                                                                                                                                                 |
| Unit        | The _Unit_ indicates the unit of measure to be used for this column''s data. If not provided, then project default units are assumed. If _ReferencePath_ is provided, the the unit must be of the same measure as the referenced attribute. |

Associations
------------
| Attribute     | Description   |
|---------------|---------------|
| ReferencePath |               |
|               |               |

