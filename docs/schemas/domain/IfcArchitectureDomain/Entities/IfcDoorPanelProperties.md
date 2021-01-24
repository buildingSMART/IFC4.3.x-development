# IfcDoorPanelProperties

A door panel is normally a door leaf that opens to allow people or goods to pass. The parameters of the door panel define the geometrically relevant parameter of the panel,

The _IfcDoorPanelProperties_ are used to parametrically describe the shape and operation of door panels. The parametric definition can be added solely or additionally to the explicit shape representation of the door.

The _IfcDoorType_ can define doors consisting of more then one panel. In this case, one instance of _IfcDoorPanelProperties_ has to be included for each door panel. The _PanelPosition_ attribute, in conjunction with the _IfcDoorStyle.OperationType_ attribute, determines to which panel the _IfcDoorPanelProperties_ apply. The _IfcDoorPanelProperties_ are included in the list of properties , given by attribute _HasPropertySets_ of the _IfcDoorType_. More information about the door panel can be included in the same list of the _IfcDoorStyle_ using the _IfcPropertySet_ for dynamic extensions.

The _IfcDoorPanelProperties_ does not hold a geometric representation. However it defines parameters which can be used to create the shape of the door type(which is inserted by the _IfcDoor_ into the spatial context of the project) as shown in Figure 1.

The parameters of the _IfcDoorPanelProperties_ define a standard door panel, including (if given) a proportional width to define non-uniform double swing (or sliding, or folding) doors. The outer boundary of the panel is determined by the 'Profile' shape representation assigned to the _IfcDoor_, which inserts the _IfcDoorType_. It has to take the lining parameter into account as well.

&nbsp;

<table>
 <tr>
  <td>
   <table class="gridtable">
    <tr valign="top">
     <td align="left" valign="top"><img src="../../../../../../figures/ifcdoorpanelproperties-fig01.gif" alt="panel 1" border="0" height="187" width="266"></td>
     <td align="left" valign="top">The depth of the panel (swinging, double-acting, and sliding panels) is defined by the <em>PanelDepth</em> parameter.
      <ul>
       <li class="small"><em>PanelDepth</em></li>
      </ul>
     </td>
    </tr>
    <tr valign="top">
     <td align="left" valign="top"><img src="../../../../../../figures/ifcdoorpanelproperties-fig02.gif" alt="panel 2" border="0" height="259" width="304"></td>
     <td align="left" valign="top">For door operation types that include more than one panel, the width of (at least) one panel is
      given by a normalised ratio measure. It determines the width of that panel, which is defined as a ratio of the overall width of the door opening.
      <ul>
       <li class="small"><em>PanelWidth</em></li>
      </ul>
     </td>
    </tr>
   </table>
  </td>
 </tr>
 <tr>
  <td><p class="figure">Figure 1 &mdash; Door panel properties</p></td>
 </tr>
</table>

> HISTORY&nbsp; New entity in IFC2.0.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Supertype changed to new _IfcPreDefinedPropertySet_.

## Attributes

### PanelDepth
Depth of the door panel, measured perpendicular to the plane of the door leaf.

### PanelOperation
The _PanelOperation_ defines the way of operation of that panel. The _PanelOperation_ of the door panel has to correspond with the _OperationType_ of the _IfcDoorStyle_ by which it is referenced.

### PanelWidth
Width of this panel, given as ratio relative to the total clear opening width of the door. If omited, it defaults to 1. A value has to be provided for all doors with _OperationType_'s at _IfcDoorStyle_ defining a door with more then one panel.

### PanelPosition
Position of this panel within the door. The _PanelPosition_ of the door panel has to correspond with the _OperationType_ of the _IfcDoorStyle_ by which it is referenced.

### ShapeAspectStyle
Pointer to the shape aspect, if given. The shape aspect reflects the part of the door shape, which represents the door panel.
{ .deprecated}
> DEPRECATION&nbsp; The attribute is deprecated and shall no longer be used, i.e. the value shall be NIL ($).

## Formal Propositions

### ApplicableToType
The _IfcDoorPanelProperties_ shall only be used in the context of an _IfcDoorType_.
> NOTE&nbsp; The deprecated entity _IfcDoorStyle_ is applicable as well.
