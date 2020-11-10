IfcRelInterferesElements
========================
The _IfcRelInterferesElements_ objectified relationship indicates that two
elements interfere. Interference is a spatial overlap between the two
elements. It is a 1 to 1 relationship. The concept of two elements interfering
physically or logically is described independently from the elements. The
interference may be related to the shape representation of the entities by
providing an interference geometry.  
  
* When the interference geometry is available it can be passed by the optional attribute _InterferenceGeometry_ pointing to _IfcConnectionGeometry_. The connection geometry is provided as a point, curve, surface, or volume within the local placement coordinate systems of the connecting elements. The _IfcConnectionVolumeGeometry_ is the default type to be used for interference in 3D space, as indicated in e.g. clash detections.  
* If the interference geometry is omitted then the interference is provided as a logical relationship. Under this circumstance, the connection point, curve, surface, or solid has to be recalculated by the receiving application.  
  
The _RelatingElement_ and _RelatedElement_ define the two elements in the
relationship, that may have different roles. This is controlled by the
attribute _ImpliedOrder_.  
  
* _ImpliedOrder_=TRUE\S\ The _RelatingElement_ constitutes the primary element of the interference relationship. If the interference is to be resolved by subtracting the overlapping part, it should be subtracted from the _RelatingElement_. The net result would be the _RelatingElement_ subtracted by the _InterferenceGeometry_. This would be the case in interference relationships where the _RelatedElement_ creates a void in the _RelatingElement_ dynamically.  
* _ImpliedOrder_=FALSE\S\ The _RelatingElement_ and _RelatedElement_ have no priority among each other. If the interference is to be resolved then no information about whether the _InterferenceGeometry_ should be subtracted from the _RelatingElement_ or thed _RelatedElement_ can be traced. This would be the case for clash detection results.  
* _ImpliedOrder_=UNKNOWN No information about the priorities is provided.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcrelinterfereselements.htm)


Attribute definitions
---------------------
| Attribute            | Description                                                                                                                                                                                                                                                                           |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| InterferenceGeometry |                                                                                                                                                                                                                                                                                       |
| RelatedElement       |                                                                                                                                                                                                                                                                                       |
| RelatingElement      |                                                                                                                                                                                                                                                                                       |
| InterferenceType     | Optional identifier that describes the nature of the interference. Examples include ''Clash'', ''ProvisionForVoid'' (physical elements), and “Crosses”, “PassesThrough” “PassesOver” “PassesUnder” (spatial elements).                                                                |
| ImpliedOrder         | Logical value indicating whether the interference geometry should be subtracted from the _RelatingElement_ (if TRUE), or whether it should be either subtracted from the _RelatingElement_ or the _RelatedElement_ (if FALSE), or whether no indication can be provided (if UNKNOWN). |

