# IfcBuiltElement

The built element comprises all elements that are primarily part of the construction of a built facility, i.e., its structural and space separating system. Built elements are all physically existent and tangible things  

{ .extDef}
> NOTE Definition from ISO 6707-1:  
> Major functional part of a building, examples are foundation, floor, roof, wall. 

This _IfcBuiltElement_ is a generalization of all elements that participate in a building system. Typical examples of _IfcBuiltElement_'s are (among others):  

* built elements within a space separation systems
* built elements within an enclosure system (such as a facade)
* built elements within a fenestration system
* built elements within a load bearing system
* built elements within a foundation system

  
> EXAMPLE&nbsp; built elements are walls, curtain wall, doors, columns, pile, and others.  
 
The IfcBuiltElement can be instantiated in the case when arbitrary built elements cannot be expressed by a subtype of IfcBuiltElement.

> HISTORY&nbsp; New entity in IFC1.0

## Formal Propositions

### MaxOneMaterialAssociation
There should be only a maximum of one material association assigned to an building element.
> NOTE&nbsp; The material association can assign a single material, a set of materials, a set of material layers, or a set of material profiles by a single association relationship.

{ .change-ifc2x4}
> FC2x4 CHANGE The where rule has been promoted from the subtype _IfcWall_.
