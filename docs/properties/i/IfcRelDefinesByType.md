IfcRelDefinesByType
===================

The objectified relationship _IfcRelDefinesByType_ defines the relationship between an object type and object occurrences. The _IfcRelDefinesByType_ is a 1-to-N relationship, as it allows for the assignment of one type information to a single or to many objects. Those objects then share the same object type, and the property sets and properties assigned to the object type.

The _IfcRelDefinesByType_ links the object type definition with the object occurrence. Both may define properties by assigning an _IfcPropertySet_, including one or many subtypes of _IfcProperty_ to either the object type or object occurrence, as shown in Figure 1.

There are several scenarios to define the same property set on the object type definition and object occurrence side:

1. All properties for all object occurrences of a common object type have the same value - then only the object type definition has a property set assigned.
2. All properties for all object occurrences are different, that is there are no common property values for the object type definition - then each of the object occurrence has a property set assigned.
3. Some properties within the same property set have common values and are assigned to the object type definition and some are occurrence specific and assigned (with potentially different values) to the object occurrences - then: 
    * The sum of all properties within a given property set applicable to an object occurrence is the union of properties assigned to the object type definition plus the properties assigned to the object occurrence.
    * If the object occurrence has a property with the same _IfcProperty.Name_ in an _IfcPropertySet_, as the corresponding object type definition, then the occurrence property value overrides the type property value. 

<table border="0" cellpadding="0" cellspacing="0" summary="relationship usage">
<tr><td valign="top"><img src="../../../../../../figures/ifcreldefinesbytype_fig-1.png" alt="instance diagram" border="0"></td></tr>
<td valign="top"><p class="figure">Figure 1 &mdash; Type definition relationships</p></td>
</table>

The following table provides an example of assigning

<table border="1" cellpadding="2" cellspacing="2" summary="example for property assignment">
<tr valign="top">
<td><small><b>properties assigned to <em>IfcWall</em></b></small></td>
<td><small><b>properties assigned to <em>IfcWallType</em></b></small></td>
<td><small><b>resulting property value for individual wall</b></small></td>
</tr>
<tr valign="top">
<td><small><em>Pset_WallCommon</em></small></td>
<td><small><em>Pset_WallCommon</em></small></td>
<td> </td>
</tr>
<tr valign="top">
<td><em><small> - ExtendToStructure</small> = TRUE</em></td>
<td> </td>
<td><small>TRUE</small></td>
</tr>
<tr valign="top">
<td> </td>
<td><small><em> - ThermalTransmittance</em> = 0.375</small></td>
<td><small>0.375</small></td>
</tr>
<tr valign="top">
<td><small><em> - ExtendToStructure</em> = FALSE</small></td>
<td><small><em> - ExtendToStructure</em> = TRUE</small></td>
<td><small>FALSE</small></td>
</tr>
</table>

> HISTORY&nbsp; New entity in IFC2x.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute _RelatedObjects_ had been demoted from the supertype _IfcRelDefines_ to _IfcRelDefinesByType_.
