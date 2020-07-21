IfcSpace
========
A space represents an area or volume bounded actually or theoretically. Spaces
are areas or volumes that provide for certain functions within a building.  
A space is associated to a building storey (or in case of exterior spaces to a
site). A space may span over several connected spaces. Therefore a space group
provides for a collection of spaces included in a storey. A space can also be
decomposed in parts, where each part defines a partial space. This is defined
by the CompositionType attribute of the supertype
[_IfcSpatialStructureElement_]($element://{30E08EC3-5B14-45f4-8246-B4811D2ECF1B})
which is interpreted as follow:  

  

  * COMPLEX = space group
  

  * ELEMENT = space
  

  * PARTIAL = partial space
  

  
NOTE View definitions and implementation agreements may restrict spaces with
_CompositionType_ =ELEMENT to be non-overlapping.  
The [_IfcSpace_]($element://{51F70274-0484-4e6b-899A-1D0445F25124}) is used to
build the spatial structure of a building (that serves as the primary project
breakdown and is required to be hierarchical). The spatial structure elements
are linked together by using the objectified relationship
[_IfcRelAggregates_]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5}).  
Figure 187 shows the
[_IfcSpace_]($element://{51F70274-0484-4e6b-899A-1D0445F25124}) as part of the
spatial structure. It also serves as the spatial container for space related
elements.  
NOTE Detailed requirements on mandatory element containment and placement
structure relationships are given in view definitions and implementer
agreements.  
[ _space composition_]($imageman://id=1306137201;mdg=Global;name=space
composition;type=Bitmap;)  
Figure 187 — Space composition  
  
The following guidelines should apply for using the _Name_ , _Description_ ,
_LongName_ and _ObjectType_ attributes.  

  

  * _Name_ holds the unique name (or space number) from the plan.
  

  * _Description_ holds any additional information field the user may have specified, there are no further recommendations.
  

  * _LongName_ holds the full name of the space, it is often used in addition to the _Name_, if a number is assigned to the room, then the descriptive name is exchanged as _LongName_.
  

  * _ObjectType_ holds the space type, i.e. usually the functional category of the space .
  

  
NOTE In cases of inconsistency between the geometric representation of the
_IfcSpace_ and the combined geometric representations of the surrounding
_IfcRelSpaceBoundary_, the geometric representation of the space should take
priority over the geometric representation of the surrounding space
boundaries.  
Figure 188 describes the heights and elevations of the
[_IfcSpace_]($element://{51F70274-0484-4e6b-899A-1D0445F25124}).  

  

  * elevation of the space (top of construction slab) equals elevation of storey: provided by _IfcBuildingStorey.Elevation_ relative to _IfcBuilding.ElevationOfRefHeight_
  

  * elevation of the space flooring (top of flooring on top of slab): provided by _IfcSpace.ElevationWithFlooring_ relative to _IfcBuilding.ElevationOfRefHeight_
  

  * height of space (top of slab below to bottom of slab above): provided by BaseQuantity with Name="Height"
  

  * floor height of space (top of slab below to top of flooring): provided by BaseQuantity with Name="FinishFloorHeight"
  

  * net height of space (top of flooring to bottom of suspended ceiling): provided by BaseQuantity with Name="FinishCeilingHeight"
  

  
[
_Space_elevations_]($imageman://id=2124549269;mdg=Global;name=Space_elevations;type=Bitmap;)  
Figure 188 — Space elevations  
HISTORY New entity in IFC1.0  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcspace.htm)


Attribute definitions
---------------------
| Attribute             | Description                                                                                                                                              |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ElevationWithFlooring | Level of flooring of this space; the average shall be taken, if the space ground surface is sloping or if there are level differences within this space. |

Formal Propositions
-------------------
| Rule                  | Description   |
|-----------------------|---------------|
| CorrectPredefinedType |               |
| CorrectTypeAssigned   |               |

Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| BoundedBy      |               |
| PredefinedType |               |
| HasCoverings   |               |

