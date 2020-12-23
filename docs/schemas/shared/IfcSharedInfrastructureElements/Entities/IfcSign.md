# IfcSign

A sign is a notice on display that gives information or instructions in a written, symbolic or other form. Signs are passive with the most common form of a pictorial panel. An instance of [<font color="#0000ff"><u>IfcSign</u></font>]($element://{4BE0513F-EDAF-4911-92C7-421EA6CD62A3}) refers to the occurrence of an individual panel which can be applied to a surface such as a wall or be aggregated within a Signal Assembly which can include multiple sign occurrences and the associated supporting structural elements (see Signal Assembly for examples).

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset(e.g. because an _IfcSignType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcSignType_.
