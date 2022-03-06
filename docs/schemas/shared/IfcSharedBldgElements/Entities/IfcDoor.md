# IfcDoor

The door is a built element that is predominately used to provide controlled access for people, goods, animals and vehicles. It includes constructions with hinged, pivoted, sliding, and additionally revolving and folding operations. A door can:

* be a "free standing" door, contained in an _IfcSpatialElement_ such as an _IfcBuildingStorey_.
* fill an opening, typically in a wall. The door will then have a _FillsVoids_ attribute which uses the _IfcRelFillsElement_ relationship to relate the _IfcDoor_ with the _IfcOpeningElement_;
* be part of an element assembly, typically an _IfcCurtainWall_. The door will then have a _Decomposes_ attribute which uses the the _IfcRelAggregates_ relationship to relate the door with the assembly of elements;

There are two main representations for door occurrences:

 * _IfcDoor_ entities that have a 3D rectangle 'Profile' shape representation defined. This profile can then be used to parametrically generate the geometry of a door. If not provided, the profile of the _IfcOpeningElement_ can be used if the door fills an opening. The parameters are specified on the relating _IfcDoorType_ that references _IfcDoorLiningProperties_ and _IfcDoorPanelProperties_ for each panel in the door;
 * _IfcDoor_ entities that are not parametrically generated and have only 'Brep', or 'SurfaceModel' geometry.

In addition, an _IfcDoor_ may commonly include a 'FootPrint' representation defining the 2D shape of the door and its swing.

The parameters of a door are defined by both the _IfcDoor_ occurence and its _IfcDoorType_. The _IfcDoor_ specifies:

 * the door width and height
 * the door opening direction (by the positive y-axis of the _ObjectPlacement_)

The _IfcDoorType_ specifies parameters which are common to all of its occurrences of _IfcDoor_:

 * the operation type (single swing, double swing, revolving, etc.)
 * the door hinge side (by using two different styles for right and left opening doors)
 * the particular attributes for the lining by the _IfcDoorLiningProperties_
 * the particular attributes for the panels by the _IfcDoorPanelProperties_

> REFERENCE  Definition according to ISO 6707-1: construction for closing an opening, intended primarily for access with hinged, pivoted or sliding operation.

> NOTE  The entity _IfcDoorStandardCase_ has been deleted. Use an _IfcDoor_ with a 'Profile' representation instead. The _IfcDoor_ should also have an _IfcDoorType_ with _ParameterTakesPrecedence_ set to 'TRUE'.

> HISTORY  New entity in IFC1.0.

{ .change-ifc2x4}
> IFC4 CHANGE  The attributes _PredefinedType_ and _OperationType_ are added, the applicable type object has been changed to _IfcDoorType_.

## Attributes

### OverallHeight
Overall measure of the height, it reflects the Z Dimension of a bounding box, enclosing the body of the door opening. If omitted, the _OverallHeight_ should be taken from the geometric representation of the _IfcOpening_ in which the door is inserted.

> NOTE The body of the door might be taller then the door opening (e.g. in cases where the door lining includes a casing). In these cases the _OverallHeight_ shall still be given as the door opening height, and not as the total height of the door lining.

### OverallWidth
Overall measure of the width, it reflects the X Dimension of a bounding box, enclosing the body of theE door opening. If omitted, the _OverallWidth_ should be taken from the geometric representation of the _IfcOpening_ in which the door is inserted.

> NOTE The body of the door might be wider then the door opening (e.g. in cases where the door lining includes a casing). In these cases the _OverallWidth_ shall still be given as the door opening width, and not as the total width of the door lining.

### PredefinedType


### OperationType
Type defining the general layout and operation of the door type in terms of the partitioning of panels and panel operations.

> NOTE The _OperationType_ shall only be used, if no type object _IfcDoorType_ is assigned, providing its own _IfcDoorType.OperationType_.

### UserDefinedOperationType
Designator for the user defined operation type, shall only be provided, if the value of _OperationType_ is set to USERDEFINED.

## Formal Propositions

### CorrectStyleAssigned
Either there is no door type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcDoorType_.
> NOTEnbsp; The deprecated type _IfcDoorStyle_ is still included for backward compatibility reasons.

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcDoorType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no door type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcDoorType_.

## Concepts

### Door Attributes

The opening direction is determined by the local placement of IfcDoor and the OperationType of the IfcDoorType.

The IfcDoorTypeOperationEnum defines the general layout of the door type and its symbolic presentation. Depending on the enumerator, the appropriate instances of IfcDoorLiningProperties and IfcDoorPanelProperties are attached in the list of HasPropertySets. The IfcDoorTypeOperationEnum mainly determines the hinge side (left hung, or right hung), the operation (swinging, sliding, folding, etc.) and the number of panels.

There are different definitions in various countries on what a left opening or left hung or left swing door is (same for right). Therefore the IFC definition may derivate from the local standard and need to be mapped appropriately. Example mappings are shown in Table 228, where it assumes that the 'inside/private/primary' space is above (top in the pictures) and the 'outside/public/secondary' space is below (bottom in the pictures).

| Opening | Definitions | US Mapping | German Mapping |
| --- | --- | --- | --- |
| ![fig 1](../../../../figures/ifcdoor-fig01.gif) | The door panel (for swinging doors) opens always into the direction of the positive Y axis of the local placement. The determination of whether the door opens to the left or to the right is done at the level of the _IfcDoorType_.  Here it is a left side opening door given by IfcDoorType.OperationType = SingleSwingLeft | LEFT HAND (LH) | DIN-R (right hung) |
| ![fig 2](../../../../figures/ifcdoor-fig02.gif) | If the door should open to the other side, then the local placement has to be changed. It is still a left side opening door, given by _IfcDoorType_._OperationType_ = SingleSwingLeft | RIGHT HAND REVERSE (RHR) | DIN-R (right hung) |
| ![fig 3](../../../../figures/ifcdoor-fig03.gif) | If the door panel (for swinging doors) opens to the right, a separate door style needs to be used (here _IfcDoorType_._OperationType_ = SingleSwingRight) and it always opens into the direction of the positive Y axis of the local placement. | RIGHT HAND (RH) | DIN-L (left hung) |
| ![fig 4](../../../../figures/ifcdoor-fig04.gif) | If the door panel (for swinging doors) opens to the right, and into the opposite directions, the local placement of the door need to change. The door style is given by _IfcDoorType_._OperationType_ = SingleSwingRight. | LEFT HAND REVERSE (LHR) | DIN-L (left hung) |

Table 228 — Mappings of openings to local standards

> NOTE  The OverallWidth and OverallHeight parameters are for informational purpose only.

### Material Constituent Set

#### Lining

Indicates that the material constituent applies to the door lining.

#### Framing

Indicates that the material constituent applies to the door panel(s); if not provided, the 'Lining' material information applies to panel(s) as well.

#### Glazing

Indicates that the material constituent applies to the glazing part.

### Object Typing

#### IfcDoorStyle

> NOTE This type is deprecated

### Product Local Placement

The following restriction is imposed:

1. The PlacementRelTo relationship of IfcLocalPlacement shall point to the local placement of the same element (if given), in which the IfcDoor is used as a filling (normally an IfcOpeningElement), as provided by the IfcRelFillsElement relationship;
2. If the IfcDoor is part of an assembly, e.g. an IfcCurtainWall, then the PlacementRelTo relationship of IfcLocalPlacement shall point (if given) to the local placement of that assembly;
3. If the IfcDoor is not inserted into an IfcOpeningElement, then the PlacementRelTo relationship of IfcLocalPlacement shall point (if given) to the local placement of the same IfcSpatialStructureElement that is used in the ContainedInStructure inverse attribute or to a referenced spatial structure element at a higher level.

> NOTE  The product placement is used to determine the opening direction of the door.

### Profile 3D Geometry

The door profile is represented by a three-dimensional closed curve lying in the xz plane. The profile is used to apply the parameters of a parametric door representation. The following attribute values for the IfcShapeRepresentation holding this geometric representation shall be used:

* RepresentationIdentifier: 'Profile'
* RepresentationType: 'Curve3D' or 'GeometricCurveSet'. In case of 'GeometricCurveSet' only a single closed curve shall be contained in the set of IfcShapeRepresentation.Items.

The following additional constraints apply to the 'Profile' representation type:

* Curve: being an _IfcPolyline_ defining a rectangle.
* Position: The curve shall lie in the xz plane of the object placement coordinate (the y coordinate values of the IfcCartesianPoint's shall be 0.).

Figure 229 illustrates applying the door lining parameters to the door profile shape representation. The profile defines the outer boundary to which the door lining parameters relate as:

* IfcDoorLiningProperties.LiningDepth starting at distance defined by LiningOffset going into the positive y direction.
* IfcDoorLiningProperties.LiningThickness offset into the inner side of the rectangle.
* IfcDoorLiningProperties.LiningOffset distance along the positive y direction to where the LiningDepth applies.
* IfcDoorLiningProperties.ThresholdThickness starting at the bottom edge of the rectangle into the inner side of the rectangle
* IfcDoorLiningProperties.ThresholdDepth starting at distance defined by LiningOffset going into the positive y direction.
* IfcDoorLiningProperties.TransomOffset starting at the bottom edge of the rectangle (along local x axis) into the inner side of the rectangle, distance provided as percentage of overall height. Distance to the centre line of the transom.

![standard door](../../../../figures/ifcdoorstandardcase-01.png)

Figure 229 — Door profile

### Property Sets for Objects

### Quantity Sets

### Spatial Containment

The IfcDoor, as any subtype of IfcBuildingElement,
may participate alternatively in one of the two different containment relationships:


* the Spatial Containment (defined here), or
* the Element Composition.


The IfcDoor may also be connected to the IfcOpeningElement in which it is placed as a filler. In this case, the spatial containment relationship shall be provided, see Figure 230.


![Containment](../../../../figures/ifcdoor_containment-01.png)

Figure 230 — Door spatial containment

Even if the _IfcDoor_ is a filling of an opening established by _IfcRelFillsElement_, it must also contained in the spatial structure by _IfcRelContainedInSpatialStructure_.

#### IfcBuildingStorey

Default spatial container

#### IfcBuilding

Spatial container for the element if it cannot be assigned to a building storey

#### IfcSite

Spatial container for the element in case that it is placed on site (outside of building)

#### IfcSpace

In particular use cases, a door maybe assigned directly to space
