# IfcRail

A rail is a predominately linear built element that has a special section profile. Rail is distinctive from built elements with similar geometric shapes (e.g. beam, member) that its major function is to ensure guidance of moving for vehicles or other kinds of machineries.
<!-- end of short definition -->

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcRailType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcRailType_.
