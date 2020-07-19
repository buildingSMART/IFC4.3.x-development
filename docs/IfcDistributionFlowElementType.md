IfcDistributionFlowElementType
==============================
The element type
[_IfcDistributionFlowElementType_]($element://{A464A3D9-9012-463a-A349-D7E871CDE796})
defines a list of commonly shared property set definitions of an element and
an optional set of product representations. It is used to define an element
specification (the specific product information that is common to all
occurrences of that product type).  
Distribution flow element types (or the instantiable subtypes) may be
exchanged without being already assigned to occurrences.  
The occurrences of the
[_IfcDistributionFlowElementType_]($element://{A464A3D9-9012-463a-A349-D7E871CDE796})
are represented by instances of
[_IfcDistributionFlowElement_]($element://{8F559036-DE32-4999-B800-D4C2D744B169})
or its subtypes.  
HISTORY New entity in IFC2x2.  
IFC4 CHANGE Ports may now be defined using
[_IfcRelNests_]($element://{17E0F5E7-BE95-4850-8294-6B964506C1D9}) to enable
definition of ports at type definitions (both forward and backward
compatible), provide a logical order, and reduce the number of relationship
objects needed. The relationship
[_IfcRelConnectsPortToElement_]($element://{BB19D6A5-C718-4ecb-9977-170B771837FC})
is still supported on occurrence objects, however is now specific to
dynamically connected ports.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgserviceelements/lexical/ifcdistributionflowelementtype.htm)


