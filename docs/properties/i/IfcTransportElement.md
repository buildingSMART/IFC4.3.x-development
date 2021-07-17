IfcTransportElement
===================

A transport element is a generalization of all transport related objects that move people, animals or goods within a Facility. The _IfcTransportElement_ defines the occurrence of a transport element, that (if given), is expressed by the _IfcTransportElementType_.

> EXAMPLE Transportation elements include elevator (lift), escalator, moving walkway, etc.  

> NOTE&nbsp; More detailed equipment that may be a part of a transportation device, like a lifting hook, is defined as _IfcDiscreteAccessory_. It maybe included as a part of the _IfcTransportElement_ by virtue of the objectified relationship _IfcRelAggregates_.  

Transport element can describe fixed or non fixed elements, which can either be identified as specified operational assets within a facility or vehicles that interact with the facility as a user or customer. 
In the case of operational assets, instances of _IfcTransportElement_ can represent individual identifiable vehicles or structures with properties such as serial numbers, registration numbers etc. and be typed accordingly by instances of _IfcTransportElementType_.  

In the case transport elements that interact as users or customers, such as cars on a road or vessels at a port, _IfcTransportElementType_ is used to define element specifications which are used to design, analyse and provide operational constraints to the facility. 

Depending on local classification systems transport elements and transportation systems in buildings are either considered as part of a built system, or as part of a built service system. Within IFC they are considered as part of a built system and may have to be mapped appropriately.

> HISTORY&nbsp; New entity in IFC2x.

{ .change-ifc2x}
> IFC2x CHANGE&nbsp; The attribute _PredefinedType_ (previously OperationType) is made optional.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The last attributes CapacityByWeight and CapacityByNumber are removed, use Pset_TransportElementCommon instead.
