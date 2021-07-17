IfcDoorLiningProperties
=======================

The door lining is the frame which enables the door leaf to be fixed in position. The door lining is used to hang the door leaf. The parameters of the door lining define the geometrically relevant parameter of the lining.

> NOTE&nbsp; The _IfcDoorLiningProperties_ shall only be applied by the receiving application to parametrically define the 3D shape of a door, if the attribute _IfcDoorType_.ParameterTakesPrecedence is set TRUE.

The _IfcDoorLiningProperties_ are included in the list of properties of _IfcDoorType_.HasPropertySets. More information about the door lining can be included in the same list of the _IfcDoorTyype_ using another _IfcPropertySet_ for dynamic extensions.

The _IfcDoorLiningProperties_ does not hold its own geometric representation. However it defines parameters which can be used to create the shape of the door type (which is inserted by the _IfcDoor_ into the spatial context of the project) as shown in Figure 1. The parameters of the _IfcDoorLiningProperties_ define a standard door lining, including (if given) a threshold and a transom. The outer boundary of the lining is determined by the 'Profile' shape representation assigned to the _IfcDoor_, which inserts the _IfcDoorType_.

&nbsp;

<table>
 <tr>
  <td>
   <table class="gridtable">
    <tr valign="top">
     <td align="left" valign="top"><img src="../../../../../../figures/ifcdoorliningproperties-fig01.png" alt="lining 1" border="0" height="250" width="280"></td>
     <td align="left" valign="top">The lining is applied to the left, right and upper side of the opening reveal. The parameters are:
      <ul>
       <li class="small"><em>LiningDepth</em>, if omited, equal to wall thickness - this only takes effect if a value for <em>LiningThickness</em> is given. If both parameters are not given, then there is no lining.</li>
       <li class="small"><em>LiningThickness</em></li>
       <li class="small"><em>LiningToPanelOffsetX</em></li>
       <li class="small"><em>LiningToPanelOffsetY</em></li>
      </ul>
      <blockquote class="note">NOTE&nbsp; The parameters <em>LiningToPanelOffsetX</em> and <em>LiningToPanelOffsetY</em> are added in IFC4.</blockquote>
     </td>
    </tr>
    <tr valign="top">
     <td align="left" valign="top"><img src="../../../../../../figures/ifcdoorliningproperties-fig02.png" alt="lining 2" border="0" height="250" width="280"></td>
     <td align="left" valign="top">The lining can only cover part of the opening reveal.
      <ul>
       <li class="small"><em>LiningOffset</em> : given if lining edge has an offset to the x axis of the local placement.</li>
      </ul>
      <blockquote class="note">NOTE&nbsp; In addition to the <em>LiningOffset</em>, the local placement of the <em>IfcDoor</em> can already have an
       offset to the wall edge and thereby shift the lining along the y axis. The actual position of the lining is calculated from the
       origin of the local placement along the positive y axis with the distance given by <em>LiningOffset</em>.</blockquote>
     </td>
    </tr>
    <tr valign="top">
     <td align="left" valign="top"><img src="../../../../../../figures/ifcdoorliningproperties-fig03.png" alt="lining 3" border="0" height="250" width="280"></td>
     <td align="left" valign="top">The lining may include a casing, which covers part of the wall faces around the opening. The
      casing covers the left, right and upper side of the lining on both sides of the wall. The parameters are:
      <ul>
       <li class="small"><em>CasingDepth</em></li>
       <li class="small"><em>CasingThickness</em></li>
      </ul>
     </td>
    </tr>
    <tr>
     <td align="left" valign="top"><img src="../../../../../../figures/ifcdoorliningproperties-fig04.png" alt="lining 4" border="0" height="250" width="250"></td>
     <td align="left" valign="top">The lining may include a threshold, which covers the bottom side of the opening. The parameters are:
      <ul>
       <li><em>ThresholdDepth</em> &mdash; if omited, equal to wall thickness - this only takes effect if a value for <em>ThresholdThickness</em> is
        given. If both parameters are not given, then there is no threshold.</li>
       <li class="small"><em>ThresholdThickness</em></li>
       <li class="small"><em>ThresholdOffset</em> (not shown in figure): given, if the threshold edge has an offset to the x axis of the local placement.</li>
      </ul>
     </td>
    </tr>
    <tr valign="top">
     <td align="left" valign="top"><img src="../../../../../../figures/ifcdoorliningproperties-fig05.png" alt="lining 5" border="0" height="300" width="250"></td>
     <td align="left" valign="top">The lining may have a transom which separates the door panel from a window panel. The transom, if given, is defined by:
      <ul>
       <li class="small"><em>TransomOffset</em> : a parallel edge to the x axis of the local placement</li>
       <li class="small"><em>TransomThickness</em></li>
      </ul>
      <p>The depth of the transom is identical to the depth of the lining and not given as separate parameter.</p>
     </td>
    </tr>
   </table>
  </td>
 </tr>
 <tr>
  <td><p class="figure">Figure 1 &mdash; Door lining properties</p></td>
 </tr>
</table>

> NOTE&nbsp; _LiningDepth_ describes the length of the lining along the reveal of the door opening. It can be given by an absolute value if the door lining has a specific depth depending on the door style. However often it is equal to the wall thickness. If the same door style is used (like the same type of single swing door), but inserted into different walls with different thicknesses, it would be necessary to create a special door style for each wall thickness. Therefore several CAD systems allow to set the value to "automatically aligned" to wall thickness. This should be exchanged by leaving the optional attribute LiningDepth unassigned. The same agreement applies to _ThresholdDepth_.

> HISTORY&nbsp; New entity in IFC2.0. Has been renamed from _IfcDoorLining_ in IFC2x.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The following attributes have been added _LiningToPanelOffsetX_, _LiningToPanelOffsetY_. The attribute _ShapeAspectStyle_ is deprecated and shall no longer be used. Supertype changed to new _IfcPreDefinedPropertySet_.
