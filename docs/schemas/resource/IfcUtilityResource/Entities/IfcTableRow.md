# IfcTableRow

_IfcTableRow_ contains data for a single row within an _IfcTable_.<!-- end of definition -->

Limitation: For backward compatibility, all _IfcTableRow_ objects referenced by an _IfcTable_ shall have the same number of Row Cells. The actual number of Cells shall be taken from the number of cells of the first _IfcTableRow_ for that table. The number of Cells is calculated by the derived attribute _NumberOfCellsInRow_ in the associated _IfcTable_.

> NOTE  The attribute _IsHeading_ exists for backward compatibility. _IfcTableColumn_ should be used instead beginning with IFC4.

![](../../../../figures/ifctablerow_image1.gif)

Figure 337 — Table row use

Figure 337 illustrates table row use.

![](../../../../figures/ifctablerow_image2.gif)

Figure 338 — Table row use alternative

Figure 338 depicts how table rows were structured prior to IFC4 with the use of the <em>IsHeading</em> flag. Note that the use of the <em>IfcTableColumn</em> constructs should be used instead of the <em>IsHeading</em> flag (which remains for backward compatibility only).

> HISTORY  New entity in IFC1.5.

## Attributes

### RowCells
The data value of the table cell..

### IsHeading
Flag which identifies if the row is a heading row or a row which contains row values.
> NOTE - If the row is a heading, the flag takes the value = TRUE.
