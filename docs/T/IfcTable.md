IfcTable
========
An _IfcTable_ is a data structure for the provision of information in the form
of rows and columns. Each instance may have _IfcTableColumn_ instances that
define the name, description and units for each column. The rows of
information are stored as a list of _IfcTableRow_ objects.  
  
Limitation: For backwards compatibility, the rows of an _IfcTable_ object are
constrained to have the same number of cells. The first row of the table
provides the number of cells. All other rows are forced to include the same
number of cells. This is enforced by the WR2.  
  
Figure 1 illustrates table use.  
  
!(../figures/ifctable_image1.gif "Figure 1 -- Table use")  
  
Figure 2 depicts how tables were structured prior to IFC4.  
  
!(../figures/ifctable_image2.gif "Figure 2 -- Table use alternative")  
  
> HISTORY  New entity in IFC1.5.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Columns attribute added.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcutilityresource/lexical/ifctable.htm)


Attribute definitions
---------------------
| Attribute          | Description                                                                                                                                                                                                              |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rows               |                                                                                                                                                                                                                          |
| Columns            |                                                                                                                                                                                                                          |
| Name               | $                                                                                                                                                                                                                        |
| NumberOfCellsInRow | The number of cells in each row, this complies to the number of columns in a table. See WR2 that ensures that each row has the same number of cells. The actual value is derived from the first member of the Rows list. |
| NumberOfHeadings   | The number of headings in a table. This is restricted by WR3 to max. one.                                                                                                                                                |
| NumberOfDataRows   | The number of rows in a table that contains data, i.e. total number of rows minus number of heading rows in table.                                                                                                       |

