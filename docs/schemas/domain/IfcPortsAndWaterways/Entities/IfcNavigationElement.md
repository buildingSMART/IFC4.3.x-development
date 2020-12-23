# IfcNavigationElement

A navigation element is an active or passive built element who's primary function is provide navigational instructions and warnings to vessels, this could be in the form of a floating buoy, a fixed beacon.
Navigation elements can aggregate other components and elements to form the entire structure. this might include frame structure to form the body, instances of [<font color="#0000ff"><u>IfcSign</u></font>]($element://{4BE0513F-EDAF-4911-92C7-421EA6CD62A3}) for signage or instances of [<font color="#0000ff"><u>IfcSignal</u></font>]($element://{15911371-83A2-4660-B0A2-B479E9560615}) for supplementary lights an/or sound signals.

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset(e.g. because an _IfcNavigationElementType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcNavigationElementType_.
