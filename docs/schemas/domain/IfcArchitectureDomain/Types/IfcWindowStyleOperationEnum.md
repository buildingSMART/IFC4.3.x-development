This enumeration defines the basic configuration of the window type in terms of the number of window panels and the subdivision of the total window. The window configurations are given for windows with one, two or three panels (including fixed panels) as shown in Figure 1.

Windows which are subdivided into more than three panels have to be defined by the geometry only. The type of such windows is USERDEFINED.

<table>
<tr>
<td>
<table class="gridtable">
<tr valign="top">
<th width="30%" valign="top" align="left"><i>Enumerator</i></th>
<th width="46%" valign="top" align="left"><i>Description</i></th>
<th width="23%" valign="top" align="left"><i>Figure</i></th>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">SinglePanel</td>
<td width="46%" valign="top" align="left">Window with one panel.<br></td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcwindowstyleoperationenum-fig01.gif" width="58" height="115" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">DoublePanelVertical</td>
<td width="46%" valign="top" align="left">Window with two panels. The configuration of the panels is
vertically.<br></td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcwindowstyleoperationenum-fig02.gif" width="115" height="115" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">DoublePanelHorizontal</td>
<td width="46%" valign="top" align="left">Window with two panels. The configuration of the panels is
horizontally.<br></td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcwindowstyleoperationenum-fig03.gif" width="115" height="115" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">TriplePanelVertical</td>
<td width="46%" valign="top" align="left">Window with three panels. The configuration of the panels is
vertically.<br></td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcwindowstyleoperationenum-fig04.gif" width="171" height="115" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">TriplePanelHorizontal</td>
<td width="46%" valign="top" align="left">Window with three panels. The configuration of the panels is
horizontally.</td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcwindowstyleoperationenum-fig05.gif" width="115" height="171" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">TriplePanelBottom</td>
<td width="46%" valign="top" align="left">Window with three panels. The configuration of two panels is vertically and
the third one is horizontally at the bottom.<br></td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcwindowstyleoperationenum-fig06.gif" width="115" height="171" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">TriplePanelTop</td>
<td width="46%" valign="top" align="left">Window with three panels. The configuration of two panels is vertically and
the third one is horizontally at the top.<br></td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcwindowstyleoperationenum-fig07.gif" width="115" height="171" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">TriplePanelLeft</td>
<td width="46%" valign="top" align="left">Window with three panels. The configuration of two panels is horizontally and
the third one is vertically at the left hand side.<br></td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcwindowstyleoperationenum-fig08.gif" width="171" height="115" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">TriplePanelRight</td>
<td width="46%" valign="top" align="left">Window with three panels. The configuration of two panels is horizontally and
the third one is vertically at the right hand side.<br></td>
<td width="23%" valign="top" align="left"><img src="../../../../../../figures/ifcwindowstyleoperationenum-fig09.gif" width="171" height="115" border="0"></td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">UserDefined</td>
<td width="46%" valign="top" align="left">user defined operation type</td>
<td width="23%" valign="top" align="left">&nbsp;</td>
</tr>
<tr valign="top">
<td width="30%" valign="top" align="left">NotDefined</td>
<td width="46%" valign="top" align="left">&nbsp;</td>
<td width="23%" valign="top" align="left">&nbsp;</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<p class="figure">Figure 1 &mdash; Window style operations</p>
</td>
</tr>
</table>

> HISTORY&nbsp; New Enumeration in IFC2.0.

NOTE

1. The way how each panel operates is defined at the _IfcWindowPanelProperties.OperationType_.
2. The reference from the window panel to the location of that panel in the window style configuration is handled by the _IfcWindowPanelProperties.PanelPosition_.
3. The figures are shown as elevations in the XZ plane of the local placement of the window, looking into the direction of the positive Y axis.
4. These figures are only shown as illustrations