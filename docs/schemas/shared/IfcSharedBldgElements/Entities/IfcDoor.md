# IfcDoor

The door is a <font color="#ff0000">built</font> element that is predominately used to provide controlled access for people, goods<font color="#ff0000">, animals and vehicles</font>. It includes constructions with hinged, pivoted, sliding, and additionally revolving and folding operations. <font color="#ff0000">REMOVE: A door consists of a lining and one or several panels.</font>  
NOTE Definition according to ISO 6707-1: construction for closing an opening, intended primarily for access with hinged, pivoted or sliding operation.  
The _IfcDoor_ defines a particular occurrence of a door inserted in the spatial context of a project. A door can:  
* be inserted as a filler in an opening using the _IfcRelFillsElement_ relationship, then the _IfcDoor_ has an inverse attribute _FillsVoids_ provided;  NOTE View definitions or implementer agreements may restrict the relationship to only include one door into one opening 

  
* be part of an element assembly, in general an _IfcCurtainWall_, using the _IfcRelAggregates_ relationship, then the _IfcDoor_ has an inverse attribute _Decomposes_ is provided;

  
* be a "free standing" door, then the _IfcDoor_ has no inverse attributes _FillsVoids_ or _Decomposes_ provided.

  
This specification provides two entities for door occurrences:  
* _IfcDoorStandardCase_ used for all occurrences of doors, that have a ''Profile'' shape representation defined to which a set of shape parameters for lining and framing properties apply. Additionally it requires the provision of an _IfcDoorType_ that references one _IfcDoorLiningProperties_ and on to many _IfcDoorPanelProperties_;  NOTE see _IfcDoorStandardCase_ for all specific constraints imposed by this subtype.

  
* _IfcDoor_ used for all other occurrences of doors, particularly for doors having only ''Brep'', or ''SurfaceModel'' geometry without applying shape parameters.

  
The actual parameters of the door and/or its shape are defined by the _IfcDoor_ as the occurrence definition (or project instance), or by the _IfcDoorType_ as the specific definition (or project type). The following parameters are given:  
at the _IfcDoor_ or _IfcDoorStandardCase_ for occurrence specific parameters. The _IfcDoor_ specifies:  
*  the door width and height
* the door opening direction (by the y-axis of the _ObjectPlacement_)\* at the _IfcDoorType_, to which the _IfcDoor_ is related by the inverse relationship _IsTypedBy_ pointing to _IfcRelDefinesByType_, for type parameters common to all occurrences of the same type.

  
at the IfcDoorType, to which the IfcDoor is related by the inverse relationship IsTypedBy pointing to IfcRelDefinesByType, for type parameters common to all occurrences of the same type.  
*  the operation type (single swing, double swing, revolving, etc.)
* the door hinge side (by using two different styles for right and left opening doors)
* the construction material type
* the particular attributes for the lining by the _IfcDoorLiningProperties_
* the particular attributes for the panels by the _IfcDoorPanelProperties_

  
The geometric representation of _IfcDoor_ is given by the _IfcProductDefinitionShape_, allowing multiple geometric representations. The _IfcDoor_ may get its parameter and shape from the _IfcDoorType_. If an _IfcRepresentationMap_ (a block definition) is defined for the _IfcDoorType_, then the _IfcDoor_ inserts it through the _IfcMappedItem_.  
The geometric representation of _IfcDoor_ is defined using the following (potentially multiple) _IfcShapeRepresentation_''s for its _IfcProductDefinitionShape_:  
* **'Profile'**: A<font color="#0000ff">''Curve3D''</font> consisting of a single losed curve defining the outer boundary of the door (lining). The door parametric representation uses this profile in order to apply the door lining and panel parameter. If not provided, the profile of the _IfcOpeningElement_ is taken.

  
* '**FootPrint**': A ''GeometricCurveSet'', or ''Annotation2D'' representation defining the 2D shape of the door

  
* '**Body**': A ''SweptSolid'', ''SurfaceModel'', or ''Brep'' representation defining the 3D shape of the door.

  
In addition the parametric representation of a (limited) door shape is available by applying the parameters from _IfcDoorType_ referencing _IfcDoorLiningProperties_ and _IfcDoorPanelProperties_. The purpose of the parameter is described at those entities and below (door opening operation by door type).  
The overall size of the _IfcDoor_ to be used to apply the lining or panel parameter provided by the _IfcDoorType_ is determined by the IfcShapeRepresentation with the RepresentationIdentifier = ''Profile''.

## Attributes

### OverallHeight
Overall measure of the height, it reflects the Z Dimension of a bounding box, enclosing the body of the door opening. If omitted, the _OverallHeight_ should be taken from the geometric representation of the _IfcOpening_ in which the door is inserted.
 NOTE The body of the door might be taller then the door opening (e.g. in cases where the door lining includes a casing). In these cases the _OverallHeight_ shall still be given as the door opening height, and not as the total height of the door lining.

### OverallWidth
Overall measure of the width, it reflects the X Dimension of a bounding box, enclosing the body of theE door opening. If omitted, the _OverallWidth_ should be taken from the geometric representation of the _IfcOpening_ in which the door is inserted.
 NOTE The body of the door might be wider then the door opening (e.g. in cases where the door lining includes a casing). In these cases the _OverallWidth_ shall still be given as the door opening width, and not as the total width of the door lining.

### PredefinedType


### OperationType
Type defining the general layout and operation of the door type in terms of the partitioning of panels and panel operations.
 NOTE The _OperationType_ shall only be used, if no type object _IfcDoorType_ is assigned, providing its own _IfcDoorType.OperationType_.

### UserDefinedOperationType
Designator for the user defined operation type, shall only be provided, if the value of _OperationType_ is set to USERDEFINED.

## WhereRules

### CorrectStyleAssigned
Either there is no door type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcDoorType_.
> NOTEnbsp; The deprecated type _IfcDoorStyle_ is still included for backward compatibility reasons.
