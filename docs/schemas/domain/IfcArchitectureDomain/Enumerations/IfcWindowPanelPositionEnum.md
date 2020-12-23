This enumeration defines the basic configuration of the window type in terms of the location of window panels. The window configurations are given for windows with one, two or three panels (including fixed panels) as shown in Figure 1. It corresponds to the _OperationType_ of the _IfcWindowStyle_ definition, which references the _IfcWindowPanelProperties_.

Windows which are subdivided into more than three panels have to be defined by the geometry only. The type of such windows is given by an _IfcWindowType.OperationType_ = USERDEFINED or NOTDEFINED (see _IfcWindowStyleOperationEnum_ for details).

<table><tr><td>
 <table class="gridtable"> 
	<tr valign="top"> 
	  <th width="30%" valign="top" align="left"><i>Enumerator from IfcWindowStyleOperationEnum</i></th> 
	  <th width="30%" valign="top" align="left"><i>Use of enumerators from IfcWindowPanelPositionEnum</i></th> 
	  <th width="23%" valign="top" align="left"><i>Figure</i></th> 
	</tr> 
	<tr valign="top"> 
	  <td width="30%" valign="top" align="left">DoublePanelVertical</td> 
	  <td width="30%" valign="top" align="left">first
		 IfcWindowPanelProperties with PanelPosition = LEFT<br>second
		 IfcWindowPanelProperties with PanelPosition = RIGHT</td> 
	  <td width="23%" valign="top" align="left"><img src="../../../../figures/ifcwindowpanelpositionenum-fig01.gif" width="152" height="151" border="0"></td> 
	</tr> 
	<tr valign="top"> 
	  <td width="30%" valign="top" align="left">DoublePanelHorizontal</td> 
	  <td width="30%" valign="top" align="left">first
		 IfcWindowPanelProperties with PanelPosition = TOP<br>second
		 IfcWindowPanelProperties with PanelPosition = BOTTOM</td> 
	  <td width="23%" valign="top" align="left"><img src="../../../../figures/ifcwindowpanelpositionenum-fig02.gif" width="152" height="151" border="0"></td> 
	</tr> 
	<tr valign="top"> 
	  <td width="30%" valign="top" align="left">TriplePanelVertical</td> 
	  <td width="30%" valign="top" align="left">first
		 IfcWindowPanelProperties with PanelPosition = LEFT<be>second
		 IfcWindowPanelProperties with PanelPosition = MIDDLE<br>third
		 IfcWindowPanelProperties with PanelPosition = RIGHT</be></td> 
	  <td width="23%" valign="top" align="left"><img src="../../../../figures/ifcwindowpanelpositionenum-fig03.gif" width="209" height="152" border="0"></td> 
	</tr> 
	<tr valign="top"> 
	  <td width="30%" valign="top" align="left">TriplePanelHorizontal </td> 
	  <td width="30%" valign="top" align="left">first
		 IfcWindowPanelProperties with PanelPosition = TOP<br>second
		 IfcWindowPanelProperties with PanelPosition = MIDDLE<br>third
		 IfcWindowPanelProperties with PanelPosition = BOTTOM</td> 
	  <td width="23%" valign="top" align="left"><img src="../../../../figures/ifcwindowpanelpositionenum-fig04.gif" width="151" height="208" border="0"></td> 
	</tr> 
	<tr valign="top"> 
	  <td width="30%" valign="top" align="left">TriplePanelBottom</td> 
	  <td width="30%" valign="top" align="left">first
		 IfcWindowPanelProperties with PanelPosition = LEFT<br>second
		 IfcWindowPanelProperties with PanelPosition = RIGHT<br>third
		 IfcWindowPanelProperties with PanelPosition = BOTTOM</td> 
	  <td width="23%" valign="top" align="left"><img src="../../../../figures/ifcwindowpanelpositionenum-fig05.gif" width="151" height="208" border="0"></td> 
	</tr> 
	<tr valign="top"> 
	  <td width="30%" valign="top" align="left">TriplePanelTop</td> 
	  <td width="30%" valign="top" align="left">first
		 IfcWindowPanelProperties with PanelPosition = TOP<br>second
		 IfcWindowPanelProperties with PanelPosition = LEFT<br>third
		 IfcWindowPanelProperties with PanelPosition = RIGHT</td> 
	  <td width="23%" valign="top" align="left"><img src="../../../../figures/ifcwindowpanelpositionenum-fig06.gif" width="151" height="208" border="0"></td> 
	</tr> 
	<tr valign="top"> 
	  <td width="30%" valign="top" align="left">TriplePanelLeft</td> 
	  <td width="30%" valign="top" align="left">first
		 IfcWindowPanelProperties with PanelPosition = LEFT<br>second
		 IfcWindowPanelProperties with PanelPosition = TOP<br>third
		 IfcWindowPanelProperties with PanelPosition = BOTTOM</td> 
	  <td width="23%" valign="top" align="left"><img src="../../../../figures/ifcwindowpanelpositionenum-fig07.gif" width="209" height="152" border="0"></td> 
	</tr> 
	<tr valign="top"> 
	  <td width="30%" valign="top" align="left">TriplePanelRight</td> 
	  <td width="30%" valign="top" align="left">first
		 IfcWindowPanelProperties with PanelPosition = TOP<br>second
		 IfcWindowPanelProperties with PanelPosition = BOTTOM<br>third
		 IfcWindowPanelProperties with PanelPosition = RIGHT</td> 
	  <td width="23%" valign="top" align="left"><img src="../../../../figures/ifcwindowpanelpositionenum-fig08.gif" width="209" height="152" border="0"></td> 
	</tr> 
 </table> 
</td></tr>
<tr><td><p class="figure">Figure 1 &mdash; Window panel positions</p></td></tr>
</table>

> HISTORY&nbsp; New enumeration in IFC2.0.

NOTE

1. The figures are shown as elevations in the XZ plane of the local placement of the window, looking into the direction of the positive Y axis.
2. These figures are only shown as illustrations.