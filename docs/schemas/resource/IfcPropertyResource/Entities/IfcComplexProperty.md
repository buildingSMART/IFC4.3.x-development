_IfcComplexProperty_ is used to define complex properties to be handled completely within a property set. The included set of properties may be a mixed or consistent collection of _IfcProperty_ subtypes. This enables the definition of a set of properties to be included as a single 'property' entry in an _IfcPropertySet_. The definition of such an _IfcComplexProperty_ can be reused in many different _IfcPropertySet_'s.

<!-- end of short definition -->


> NOTE Since an _IfcComplexProperty_ may contain other complex properties, sets of properties can be nested. This nesting may be restricted by view definitions and implementer agreements.

> HISTORY New entity in IFC2.0.

## Attributes

### UsageName
Usage description of the _IfcComplexProperty_ within the property set which references the _IfcComplexProperty_.
> NOTE Consider a complex property for glazing properties. The _Name_ attribute of the _IfcComplexProperty_ could be _Pset_GlazingProperties_, and the UsageName attribute could be _OuterGlazingPane_.

### HasProperties
Set of properties that can be used within this complex property (may include other complex properties).

## Formal Propositions

### WR21
The IfcComplexProperty should not reference itself within the list of HasProperties.

### WR22
Each property within the complex property shall have a unique name attribute.
