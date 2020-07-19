IfcMechanicalFastenerType
=========================
The element component type
[_IfcMechanicalFastenerType_]($element://{C9802B77-59CB-4096-9A14-359EE13F72B2})
defines commonly shared information for occurrences of mechanical fasteners.
The set of shared information may include:  

  

  * common properties with shared property sets
  

  * common representations
  

  * common materials
  

  * common composition of elements
  

  
It is used to define a mechanical fastener type specification indicating the
specific product information that is common to all occurrences of that product
type. The
[_IfcMechanicalFastenerType_]($element://{C9802B77-59CB-4096-9A14-359EE13F72B2})
may be declared within
[_IfcProject_]($element://{261F430C-03B3-4a9e-A414-1452166DEDA0}) or
[_IfcProjectLibrary_]($element://{CA5982C4-A63E-4729-B01F-DD56944575CF}) using
[_IfcRelDeclares_]($element://{2B5611F4-8815-497d-B43E-430F01D3B9F4}) and may
be exchanged with or without occurrences of the type. Occurrences of
[_IfcMechanicalFastenerType_]($element://{C9802B77-59CB-4096-9A14-359EE13F72B2})
are represented by instances of
[_IfcMechanicalFastener_]($element://{A305A665-0E0D-4738-BFC3-7F84F805B605}).  
HISTORY New entity in IFC2x2  
IFC4 CHANGE Supertype changed from IfcFastenerType to IfcElementComponentType.
Attributes _PredefinedType_, NominalDiameter, NominalLength added.  
  
 **Classification Use Definition**  
Mechanical fasteners, especially bolts, are often standardized. To refer to a
formal fastener designation according to a standard (a product norm),
[_IfcRelAssociatesClassification_]($element://{EEF332B8-5B1A-4d36-9FDF-852E4452DF0E})
together with
[_IfcClassificationReference_]($element://{6D22EB0A-9E82-42a8-A519-616F620F85EA})
should be used.  

  

  * [_IfcClassificationReference_]($element://{6D22EB0A-9E82-42a8-A519-616F620F85EA}).Identification contains a machine-readable form of the formal fastener designation from the norm. Example: ''M16X80-10.9-HV'' for a high-strength structural bolting assembly for preloading with hexagon bolt and nut. (On the other hand, [_IfcMechanicalFastenerType_]($element://{C9802B77-59CB-4096-9A14-359EE13F72B2}).Name contains a displayable name which may not necessarily be the same as the formal designation.)
  

  * [_IfcClassificationReference_]($element://{6D22EB0A-9E82-42a8-A519-616F620F85EA}).Name carries the short name of the fastener norm. Example: ''EN 14399-4'' as the respective European standard for high-strength hexagon bolts.
  

  * Optionally, the norm can be further described by [_IfcClassificationReference_]($element://{6D22EB0A-9E82-42a8-A519-616F620F85EA}).ReferencedSource_, including information like publisher and date of issue of the norm.
  

  
Furthermore,
[_IfcRelAssociatesLibrary_]($element://{68D050C3-952D-4773-B635-972EF50F751C})
together with
[_IfcLibraryReference_]($element://{84A75DA4-9FC6-430d-BB80-2C1E591BE76A}) may
be used to refer to a library which contains fastener definitions.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedcomponentelements/lexical/ifcmechanicalfastenertype.htm)


