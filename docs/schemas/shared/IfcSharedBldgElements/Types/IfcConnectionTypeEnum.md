# IfcConnectionTypeEnum

This enumeration defines the different ways how path based elements (such as _IfcWallStandardCase_) can connect, as shown in Figure 1.

> HISTORY&nbsp; New type in IFC2.0

The enumerated items shall be used in the following combinations:

<table>
<tr>
<td>
<table class="gridtable">
<tr>
 <th width="260" valign="top" align="left">Connection type</th>
 <th width="300" valign="top" align="left">Illustration</th>
</tr>
<tr>
</tr><tr>
<td width="260" valign="top" align="left">
<p>L-Shape Connection</p>
<ul>
<li>RelatingConnectionType: AtStart</li>
<li>RelatedConnectionType: AtStart</li>
</ul>
</td>
<td width="300"><img src="../../../../figures/IfcConnectionTypeEnum-Fig03.gif" width="143" height="132" border="0"></td>
</tr>
<tr>
<td width="260" valign="top" align="left">
<p>L-Shape Connection</p>
<ul>
<li>RelatingConnectionType: AtEnd</li>
<li>RelatedConnectionType: AtStart</li>
</ul>
</td>
<td width="300"><img src="../../../../figures/IfcConnectionTypeEnum-Fig01.gif" width="193" height="132" border="0"></td>
</tr>
<tr>
<td width="260" valign="top" align="left">
<p>T-Shape Connection</p>
<ul>
<li>RelatingConnectionType: AtPath</li>
<li>RelatedConnectionType: AtStart</li>
</ul>
</td>
<td width="300"><img src="../../../../figures/IfcConnectionTypeEnum-Fig02.gif" width="145" height="133" border="0"></td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<p class="figure">Figure 1 &mdash; Connection types</p>
</td>
</tr>
</table>

## Items

### ATPATH
Connection along the path of the connected element.

### ATSTART
Connection at the start of the connected element.

### ATEND
Connection at the end of the connected element.

### NOTDEFINED

