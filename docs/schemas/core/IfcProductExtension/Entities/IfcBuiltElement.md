# IfcBuiltElement

The <font color="#ff0000">built </font>element comprises all elements that are primarily part of the construction of a built facility, i.e., its structural and space separating system. <font color="#ff0000">Built </font>elements are all physically existent and tangible things  
> NOTE Definition from ISO 6707-1:  Major functional part of a building, examples are foundation, floor, roof, wall.  
This _Ifc<font color="#ff0000">Built</font>Element_ is a generalization of all elements that participate in a building system. Typical examples of __Ifc<font color="#ff0000">Built</font>Element__'s are (among others):  
* <font color="#ff0000">built </font>elements within a space separation systems
* <font color="#ff0000">built </font>elements within an enclosure system (such as a facade)
* <font color="#ff0000">built </font>elements within a fenestration system
* <font color="#ff0000">built </font>elements within a load bearing system
* <font color="#ff0000">built </font>elements within a foundation system

  
> EXAMPLE <font color="#ff0000">built </font>elements are walls, curtain wall, doors, columns, pile, and others.  
<font color="#ff0000">REMOVE{</font> The _Ifc<font color="#ff0000">Built</font>Element_ is an abstract entity that cannot be instantiated. For arbitrary building elements, that cannot be expressed by a subtype of _Ifc<font color="#ff0000">Built</font>Element_, use _IfcB<font color="#ff0000">uilt</font>ElementProxy_.<font color="#ff0000">}</font>  
<font color="#ff0000">The IfcBuiltElement can be instantiated in the case when arbitrary built elements cannot be expressed by a subtype of IfcBuiltElement.</font>  
> HISTORY New entity in IFC1.0

## WhereRules

### MaxOneMaterialAssociation
There should be only a maximum of one material association assigned to an building element.
> NOTE&nbsp; The material association can assign a single material, a set of materials, a set of material layers, or a set of material profiles by a single association relationship.

{ .change-ifc2x4}
> FC2x4 CHANGE The where rule has been promoted from the subtype _IfcWall_.
