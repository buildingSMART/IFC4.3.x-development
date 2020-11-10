IfcAlignment
============
An alignment is used to define a reference system to position elements mainly
for linear construction works, such as roads, rails, bridges, and others. The
relative positioning along the alignment is defined by the linear referencing
methodology.  
  
> NOTE  See ISO 19148 Geographic information - Linear referencing for general
> definitions about linear referencing.  
  
A single alignment may have:  
  
* a horizontal alignment defined in the x/y plane of the engineering coordinate system  
* an accompanying vertical alignment, defined along the horizontal alignment in the distance along / z coordinate space  
* a relative alignment, defined as a span within another alignment and/or at constant or variable offsets  
* a 3D alignment, either computed from the horizontal and vertical alignment, or extracted from geospatial data.  
  
Alignments may be aggregated into referents (_IfcReferent_) or derivative
alignments. Derivative alignments may be used to indicate dependent
alignments, such as an alignment for a bridge that is relative to a parent
alignment for a road, where the child _IfcAlignment_ may have _Axis_ set to
_IfcOffsetCurveByDistances_ that starts and ends at a span within the extent
of the _IfcAlignmentCurve_ defined at the _Axis_ of the parent _IfcAlignment_.  
  
Alignments may be assigned to groups using _IfcRelAssignsToGroup_, where
_IfcGroup_ or subtypes may capture information common to multiple alignments.  
  
Supported representations of IfcAlignment.Axis are:  
  
* _IfcAlignmentCurve_ as a 3D horizontal and vertical alignment (represented by their alignment segments)  
* _IfcAlignmentCurve_ as a 2D horizontal alignment (represented by its horizontal alignment segments) without a vertical alignment  
* _IfcOffsetCurveByDistances_ as a 2D or 3D curve defined relative to an _IfcAlignmentCurve_ or another _IfcOffsetCurveByDistances_  
* _IfcPolyline_ as a 3D alignment by a 3D polyline representation (such as coming from a survey)  
* _IfcPolyline_ as a 2D horizontal alignment by a 2D polyline representation (such as in very early planning phases or as a map representation)  
  
> NOTE  Although _Axis_ is an _IfcCurve_ base type, only derived types
> _IfcAlignmentCurve_, _IfcOffsetCurveByDistances_, and _IfcPolyline_ are
> meant to be supported types. Derivative specifications (Model View
> Definitions) may expand this set to include additional curve types.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcalignment.htm)


Attribute definitions
---------------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

