# IfcWindow

The window is a building element that is predominately used to provide natural light and fresh air. It includes vertical opening but also horizontal opening such as skylights or light domes. It includes constructions with swinging, pivoting, sliding, or revolving panels and fixed panels. A window consists of a lining and one or several panels.

{ .extDef}
> NOTE  Definition according to ISO 6707-1
> Construction for closing a vertical or near vertical opening in a wall or pitched roof that will admit light and may admit fresh air.

The _IfcWindow_ defines a particular occurrence of a window inserted in the spatial context of a project. A window can:

* be inserted into an _IfcOpeningElement_ using the _IfcRelFillsElement_ relationship, then the _IfcWindow_ has an inverse attribute _FillsVoids_ provided,
* be part of an element assembly, often an _IfcCurtainWall_, using the _IfcRelAggregates_ relationship, then the inverse attribute _Decomposes_ is provided.
* or be a "free standing" window, then the _IfcWindow_ has no inverse attributes _FillsVoids_ or _Decomposes_ provided.

> NOTE  View definitions or implementer agreements may restrict the relationship to only include one window (or door) into one opening.

There are two main representations for window occurrences:

- _IfcWindow_ with a shape representation having RepresentationIdenfifier='Profile' is used for all occurrences of windows, that have a 'Profile' shape representation defined to which a set of shape parameters for lining and framing properties apply. Additionally it requires the provision of an _IfcWindowType_ that references one _IfcWindowLiningProperties_ and on to many _IfcWindowPanelProperties_.

- _IfcWindow_ used for all other occurrences of windows, particularly for windows having only 'Brep', or 'SurfaceModel' geometry without applying shape parameters.

> NOTE  The entity _IfcWindowStandardCase_ has been deprecated.

The actual parameter of the window and/or its shape is defined at the _IfcWindow_ as the occurrence definition (or project instance), or by the _IfcWindowType_ as the specific definition (or project type). The following parameters are given:

* at the _IfcWindow_ for occurrence specific parameters. The _IfcWindow_ specifies:
    * the window width and height
    * the window opening direction (by the y-axis of the _ObjectPlacement_)
* at the _IfcWindowType_ to which the _IfcWindow_ is related by the inverse relationship _IsDefinedBy_ pointing to _IfcRelDefinesByType_, for type parameters common to all occurrences of the same type.
    * the partitioning type (single panel, double panel, tripel panel, more panels)
    * the operation type (swing, tilt and turn, pivot revolve, fixed case ment, etc.)
    * the window panel hinge side (by using two different styles for right and left opening windows)
    * the construction material type
    * the particular attributes for the lining by the _IfcWindowLiningProperties_
    * the particular attributes for the panels by the  _IfcWindowPanelProperties_

> HISTORY  New entity in IFC1.0.

{ .change-ifc2x4}
> IFC4 CHANGE  The attributes _PredefinedType_ and _OperationType_ are added, the applicable type object has been changed to _IfcDoorType_.

{ .use-head}
Parameteric Representation using parameters at _IfcWindowType_

The parameters, which define the shape of the _IfcWindow_, are given at the _IfcWindowType_ and the property sets, which are included in the _IfcWindowType_. The _IfcWindow_ only defines the local placement. The overall size of the _IfcWindow_ to be used to apply the lining or panel parameter provided by the _IfcWindowType_ is determined by the IfcShapeRepresentation with the RepresentationIdentifier = 'Profile'. Only in case of an _IfcWindow_ inserted into an _IfcOpeningElement_ using the _IfcRelFillsElement_ relationship, having a horizontal extrusion (along the y-axis of the _IfcWindow_), the overall size is determined by the extrusion profile of the _IfcOpeningElement_.

Figure 1 illustrates the insertion of a window into the _IfcOpeningElement_ by creating an instance of _IfcWindow_ with _PartitioningType = DoublePanelHorizontal_. The parameters _OverallHeight_ and _OverallWidth_ show the extent of the window in the positive Z and X axis of the local placement of the window. The lining and the transom are created by the given parameters.

![window 1](../../../../figures/ifcwindow-layout1.gif)

Figure 1 &mdash; Window placement

Figure 2 illustrates the final window (DoublePanelHorizontal) with first panel having _PanelPosition = TOP_, _OperationType = BOTTOMHUNG_ and second panel having _PanelPosition = BOTTOM_ and _OperationType = TILTANDTURNLEFTHAND_.

![window 2](../../../../figures/ifcwindow-layout2.gif)

Figure 2 &mdash; Window planes

{ .use-head}
Window opening operation by window type

The parameters that defines the shape of the _IfcWindow_, are given at the _IfcWindowType_ and the property sets, which are included in the _IfcWindowType_. The _IfcWindow_ only defines the local placement which determines the opening direction of the window. The overall layout of the _IfcWindow_ is determined by its _IfcWindowType.PartitioningType_. Each window panel has its own operation type, provided by _IfcWindowPanelProperties.OperationType_. All window panels are assumed to open into the same direction (if relevant for the particular window panel operation. The hindge side (whether a window opens to the left or to the right) is determined by the _IfcWindowPanelProperties_._OperationType_.

> NOTE   There are different conventions in different countries on how to show the symbolic presentation of the window panel operation (the "triangles"). Either as seen from the exterior, or from the interior side. The following figures/ show the symbolics from the exterior side (the convention as used predominately in Europe).

Table 3 illustrates window operation types.

| Diagram | Description |
| --- | --- |
| ![fig 1](../../../../figures/ifcwindow-fig01.gif) | The window panel (for side hung windows) opens always into the direction of the positive Y axis of the local placement.  The determination of whether the window opens to the left or to the right is done at <em>IfcWindowPanelProperties.OperationType</em>. Here it is a left side opening window given by <em>OperationType</em> = SideHungLeftHand.  |
| ![fig 2](../../../../figures/ifcwindow-fig02.gif) | If the window should open to the other side, then the local placement has to be changed. It is still a left hung window, given by <em>IfcWindowPanelProperties.OperationType</em> = SideHungLeftHand. |
| ![fig 3](../../../../figures/ifcwindow-fig03.gif) | If the window panel (for side hung windows) opens to the right, a separate window panel style needs to be used (here <em>IfcWindowPanelProperties.OperationType</em> = SideHungRightHand) and it always opens into the direction of the positive Y axis of the local placement. |
| ![fig 4](../../../../figures/ifcwindow-fig04.gif) | If the window should open to the other side, then the local placement has to be changed. It is still a right hung window, given by <em>IfcWindowPanelProperties.OperationType</em> = SideHungRightHand. |

Table 3 &mdash; Window operations

## Attributes

### OverallHeight
Overall measure of the height, it reflects the Z Dimension of a bounding box, enclosing the window opening. If omitted, the _OverallHeight_ should be taken from the geometric representation of the _IfcOpening_ in which the window is inserted.

> NOTE  The body of the window might be taller then the window opening (for example in cases where the window lining includes a casing). In these cases the _OverallHeight_ shall still be given as the window opening height, and not as the total height of the window lining.

### OverallWidth
Overall measure of the width, it reflects the X Dimension of a bounding box, enclosing the window opening. If omitted, the _OverallWidth_ should be taken from the geometric representation of the _IfcOpening_ in which the window is inserted.

> NOTE  The body of the window might be wider then the window opening (for example in cases where the window lining includes a casing). In these cases the _OverallWidth_ shall still be given as the window opening width, and not as the total width of the window lining.

### PredefinedType
Predefined generic type for a window that is specified in an enumeration. There may be a property set given specifically for the predefined types.
> NOTE  The _PredefinedType_ shall only be used, if no _IfcWindowType_ is assigned, providing its own _IfcWindowType.PredefinedType_.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

### PartitioningType
Type defining the general layout of the window in terms of the partitioning of panels.
> NOTE  The _PartitioningType_ shall only be used, if no type object _IfcWindowType_ is assigned, providing its own _IfcWindowType.PartitioningType_.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

### UserDefinedPartitioningType
Designator for the user defined partitioning type, shall only be provided, if the value of _PartitioningType_ is set to USERDEFINED.

## Formal Propositions

### CorrectStyleAssigned
Either there is no window type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcWindowType_.
> NOTEnbsp; The deprecated type _IfcWindowStyle_ is still included for backward compatibility reasons.

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcWIndowType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no door type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcWindowType_.

## Concepts

### Door Attributes



### Material Constituent Set

The material of the IfcWindow is defined by the IfcMaterialConstituentSet or as fall back by IfcMaterial and attached by the IfcRelAssociatesMaterial.RelatingMaterial. It is accessible by the inverse HasAssociations relationship.

If the fall back single IfcMaterial is referenced, it applies to the lining and framing of the window.

#### Lining

Indicates that the material constituent applies to the window lining.

#### Framing

Indicates that the material constituent applies to the windows panels(s); if not provided, the 'Lining' material information applies to panel(s) as well.

#### Glazing

Indicates that the material constituent applies to the glazing part.

### Object Typing



### Product Local Placement

The following restriction is imposed:

1. The PlacementRelTo relationship of IfcLocalPlacement shall point to the local placement of the same element (if given), in which the IfcWindow is used as a filling (normally an IfcOpeningElement), as provided by the IfcRelFillsElement relationship.
2. If the IfcWindow is not inserted into an IfcOpeningElement, then the PlacementRelTo relationship of IfcLocalPlacement shall point (if given) to the local placement of the same IfcSpatialStructureElement that is used in the ContainedInStructure inverse attribute or to a referenced spatial structure element at a higher level.
3. If the relative placement is not used, the absolute placement is defined within the world coordinate system.

> NOTE&nbsp; The product placement is used to determine the opening direction of the window.

### Profile 3D Geometry

The window profile is represented by a three-dimensional closed curve within a particular shape representation. The profile is used to apply the parameter of the parametric window representation. The following attribute values for the IfcShapeRepresentation holding this geometric representation shall be used:

* RepresentationIdentifier : 'Profile'
* RepresentationType : 'Curve3D', only a single closed curve shall be contained in the set of _IfcShapeRepresentation.Items_.

A 'Profile' representation has to be provided if:

* a parametric representation shall be applied to the window AND
*  
    * the window is 'free standing', or
    * the opening into which the window is inserted is not extruded horizontally (i.e. where the opening profile does not match the window profile)

### Property Sets for Objects



### Quantity Sets



### Spatial Containment

The IfcWindow, as any subtype of IfcBuildingElement, may participate alternatively in one of the two different containment relationships:

* the _Spatial Containment_ (defined here), or
* the _Element Composition_.

The IfcWindow may also be connected to the IfcOpeningElement in which it is placed as a filler. In this case, the spatial containment relationship shall be provided, see Figure 1.

<table>
 
<tr valign="bottom">
  <td><img src="../../../../figures/ifcwindow_containment-01.png" alt="Containment" width="600" height="550" border="0"></td>
  <td>
   <blockquote class="note">NOTE&nbsp; The containment shall be defined independently of the filling relationship, that is, even if the 
    <em>IfcWindow</em> is a filling of an opening established by <em>IfcRelFillsElement</em>, it is also contained in the spatial structure 
    by an <em>IfcRelContainedInSpatialStructure</em>.</blockquote>
  </td>
 </tr>
 
<tr>
  <td><p class="figure">Figure 1 &mdash; Window spatial containment</p></td>
  <td>&nbsp;</td>
 </tr>

</table>

### Window Attributes



