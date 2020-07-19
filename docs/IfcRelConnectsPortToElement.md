IfcRelConnectsPortToElement
===========================
_IfcRelConnectsPortToElement_ is a relationship between a distribution element
and dynamically connected ports where connections are realised to other
distribution elements.  
  
Ports contained in different elements are connected to each other using the
_IfcRelConnectsPorts_ relationship.  
  
> NOTE  See _IfcRelNests_ for its usages to represent an ordered collection of
> ports that are contained by an element and relevant subtypes of
> _IfcDistributionElement_ for examples and port use definition sections.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The objectified relation _IfcRelConnectsPortToElement_ is now
> specialized for use of dynamically connected ports. For fixed ports, use
> _IfcRelNests_ instead. Previously this objectified relationship
> _IfcRelConnectsPortToElement_ defined the relationship that is made between
> a port and the _IfcElement_ in which it is contained. It is a 1 to 1
> relationship. The _IfcRelConnectsPortToElement_ established a whole part
> relationship between the element and its port. The port is used as the means
> to connect to other ports in other elements.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcrelconnectsporttoelement.htm)


