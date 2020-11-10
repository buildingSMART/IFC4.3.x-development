IfcComplexProperty
==================
_IfcComplexProperty_ is used to define complex properties to be handled
completely within a property set. The included set of properties may be a
mixed or consistent collection of _IfcProperty_ subtypes. This enables the
definition of a set of properties to be included as a single ''property''
entry in an _IfcPropertySet_. The definition of such an _IfcComplexProperty_
can be reused in many different _IfcPropertySet_''s.  
  
> NOTE  Since an _IfcComplexProperty_ may contain other complex properties,
> sets of properties can be nested. This nesting may be restricted by view
> definitions and implementer agreements.  
  
> HISTORY  New entity in IFC2.0.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpropertyresource/lexical/ifccomplexproperty.htm)


Attribute definitions
---------------------
| Attribute     | Description                                                                                                                                                                                                                                                                                                                   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HasProperties |                                                                                                                                                                                                                                                                                                                               |
| UsageName     | Usage description of the _IfcComplexProperty_ within the property set which references the _IfcComplexProperty_.\X\0D> NOTE  Consider a complex property for glazing properties. The _Name_ attribute of the _IfcComplexProperty_ could be _Pset_GlazingProperties_, and the UsageName attribute could be _OuterGlazingPane_. |

