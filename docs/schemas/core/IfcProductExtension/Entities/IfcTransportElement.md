# IfcTransportElement

A transport element is a generalization of all transport related objects that move people, animals or goods within a <font color="#ff0000">REMOVE {</font>building or building complex<font color="#ff0000">} Facility</font>. The [<font color="#0000ff"><u>IfcTransportElement</u></font>]($element://{9CF73480-06BE-4997-B578-8F3958E77111}) defines the occurrence of a transport element, that (if given), is expressed by the [<font color="#0000ff"><u>IfcTransportElementType</u></font>]($element://{827AB441-28FB-4320-A57A-76E6CC5BA21D}) .  
> EXAMPLE Transportation elements include elevator (lift), escalator, moving walkway, etc.  
> NOTE More detailed equipment that may be a part of a transportation device, like a lifting hook, is defined as _IfcDiscreteAccessory_. It maybe included as a part of the _IfcTransportElement_ by virtue of the objectified relationship _IfcRelAggregates_.  
<font color="#ff0000">Transport element can describe fixed or non fixed elements, which can either be identified as specified operational assets within a facility or vehicles that interact with the facility as a user or customer.</font>  
<font color="#ff0000">In the case of operational assets, instances of </font>[<font color="#ff0000"><u>IfcTransportElement</u></font>]($element://{9CF73480-06BE-4997-B578-8F3958E77111})<font color="#ff0000">s can represent individual identifiable vehicles or structures with properties such as serial numbers, registration numbers etc. and be typed accordingly by instances of </font>[<font color="#ff0000"><u>IfcTransportElementType</u></font>]($element://{827AB441-28FB-4320-A57A-76E6CC5BA21D})<font color="#ff0000">.</font>  
<font color="#ff0000">In the case transport elements that interact as users or customers, such as cars on a road or vessels at a port, </font>[<font color="#ff0000"><u>IfcTransportElementType</u></font>]($element://{827AB441-28FB-4320-A57A-76E6CC5BA21D})<font color="#ff0000"> is used to define element specifications which are used to design, analyse and provide operational constraints to the facility.</font>  
Depending on local classification systems transport elements and transportation systems in buildings are either considered as part of a <font color="#ff0000">built </font>system, or as part of a <font color="#ff0000">built </font>service system. Within IFC they are considered as part of a <font color="#ff0000">built </font>system and may have to be mapped appropriately.

## Attributes

### PredefinedType


## WhereRules

### CorrectPredefinedType
Either the _IfcTransportElement_ attribute is unset (e.g. because an _IfcTransportElementType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no transport element type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcTransportElementType_.
