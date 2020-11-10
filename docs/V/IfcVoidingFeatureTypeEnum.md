IfcVoidingFeatureTypeEnum
=========================
This enumeration qualifies a voiding feature regarding its shape and
configuration relative to the voided element.  
  
> HISTORY  New type in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralelementsdomain/lexical/ifcvoidingfeaturetypeenum.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                    |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HOLE        | A circular or slotted or threaded hole, typically but not necessarily of smaller dimension than what would be considered a cutout.                                             |
| MITER       | A skewed plane end cut, removing material across the entire profile of the voided element.                                                                                     |
| NOTCH       | An external cutout of with a mostly rectangular cutting profile. The edges between cutting planes may be overcut or undercut, i.e. rounded.                                    |
| CHAMFER     | A skewed plane end cut, removing material only across a part of the profile of the voided element.                                                                             |
| EDGE        |                                                                                                                                                                                |
| CUTOUT      | An internal cutout (creating an opening) or external cutout (creating a recess) of arbitrary shape. The edges between cutting planes may be overcut or undercut, i.e. rounded. |

